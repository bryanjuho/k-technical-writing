#!/usr/bin/env python3
"""Harvest implicit Korean-wording feedback from git history.

Finds later human edits to Korean lines that an AI-assisted commit wrote:

1. Walk non-merge commits in the range whose author is not a bot and whose
   message does not match --ai-pattern (the agent-written commits).
2. For each diff hunk of such a commit that removes lines containing Hangul,
   run `git blame` on the removed lines in the parent commit.
3. Keep the removed lines whose blamed commit message matches --ai-pattern, and
   pair them with the lines the human wrote in the same hunk.

Output: one JSON object per line on stdout,
  {"commit", "author", "date", "path", "before", "after", "ai_commit"}
plus a short summary on stderr. Pairs are candidates only; a person decides
which ones become rules (see SKILL.md, 피드백 학습).

Read-only: runs only `git log`, `git diff`, `git blame` and `git show`, with
GIT_OPTIONAL_LOCKS=0 so git does not refresh the index. No network access.
Python 3 standard library only.
"""

from __future__ import annotations

import argparse
import codecs
import json
import os
import re
import subprocess
import sys
from typing import Dict, Iterator, List, Optional, Tuple

HANGUL = re.compile("[\uac00-\ud7a3]")  # Hangul syllables U+AC00..U+D7A3
HANGUL_WORD = re.compile("[\uac00-\ud7a3]+")
AI_TRAILER: "re.Pattern[str]"  # set from --ai-pattern in main()
HUNK_HEADER = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
SHA = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")

GIT_ENV = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_PAGER="cat", LC_ALL="C.UTF-8")


def git(repo: str, *args: str, check: bool = True) -> str:
    """Run a read-only git command and return decoded stdout."""
    proc = subprocess.run(
        ["git", "-C", repo, "-c", "core.quotepath=off", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=GIT_ENV,
        check=False,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(
            "git %s failed: %s" % (" ".join(args[:2]), proc.stderr.decode("utf-8", "replace").strip())
        )
    return proc.stdout.decode("utf-8", "replace")


def has_ai_trailer(message: str) -> bool:
    return bool(AI_TRAILER.search(message))


def is_bot(author: str, email: str) -> bool:
    return author.endswith("[bot]") or email.endswith("[bot]@users.noreply.github.com")


def unquote_path(raw: str) -> str:
    """Undo git's C-style quoting of a diff path ("a/foo\\tbar")."""
    raw = raw.rstrip("\t")
    if len(raw) >= 2 and raw[0] == '"' and raw[-1] == '"':
        body = raw[1:-1].encode("utf-8")
        return codecs.escape_decode(body)[0].decode("utf-8", "replace")
    return raw


class Hunk:
    __slots__ = ("old_path", "new_path", "old_start", "removed", "added")

    def __init__(self, old_path: str, new_path: str, old_start: int) -> None:
        self.old_path = old_path
        self.new_path = new_path
        self.old_start = old_start
        self.removed: List[str] = []
        self.added: List[str] = []


def iter_hunks(diff: str) -> Iterator[Hunk]:
    """Parse `git diff --unified=0` output into hunks (binary files skipped)."""
    old_path: Optional[str] = None
    new_path: Optional[str] = None
    hunk: Optional[Hunk] = None
    rem_left = add_left = 0
    for line in diff.split("\n"):
        if hunk is not None and (rem_left or add_left):
            if line.startswith("-") and rem_left:
                hunk.removed.append(line[1:])
                rem_left -= 1
                continue
            if line.startswith("+") and add_left:
                hunk.added.append(line[1:])
                add_left -= 1
                continue
            if line.startswith("\\"):
                continue
        if hunk is not None and not rem_left and not add_left:
            yield hunk
            hunk = None
        if line.startswith("diff --git "):
            old_path = new_path = None
        elif line.startswith("--- "):
            p = unquote_path(line[4:])
            old_path = None if p == "/dev/null" else p[2:] if p.startswith(("a/", '"a/')) else p
        elif line.startswith("+++ "):
            p = unquote_path(line[4:])
            new_path = None if p == "/dev/null" else p[2:] if p.startswith(("b/", '"b/')) else p
        elif line.startswith("@@"):
            m = HUNK_HEADER.match(line)
            if not m or old_path is None or new_path is None:
                continue  # added or deleted file, or unparsable header
            old_start = int(m.group(1))
            rem_left = 1 if m.group(2) is None else int(m.group(2))
            add_left = 1 if m.group(4) is None else int(m.group(4))
            hunk = Hunk(old_path, new_path, old_start)
            if not rem_left and not add_left:
                hunk = None
    if hunk is not None:
        yield hunk


def blame_lines(repo: str, rev: str, path: str, start: int, count: int) -> Dict[int, str]:
    """Map final line number -> commit sha for lines start..start+count-1 of path@rev."""
    out = git(
        repo, "blame", "--porcelain", "-L", "%d,+%d" % (start, count), rev, "--", path, check=False
    )
    result: Dict[int, str] = {}
    for line in out.split("\n"):
        if not line or line.startswith("\t"):
            continue
        parts = line.split(" ")
        if len(parts) >= 3 and SHA.match(parts[0]):
            try:
                result[int(parts[2])] = parts[0]
            except ValueError:
                pass
    return result


class MessageCache:
    def __init__(self, repo: str) -> None:
        self.repo = repo
        self.cache: Dict[str, str] = {}

    def get(self, sha: str) -> str:
        if sha not in self.cache:
            self.cache[sha] = git(self.repo, "show", "-s", "--format=%B", sha, check=False)
        return self.cache[sha]


def iter_commits(repo: str, since: str, until: Optional[str], paths: List[str]) -> Iterator[Tuple[str, str, str, str, str, str]]:
    """Yield (sha, parent, author, email, date, message) for non-merge commits, newest first."""
    args = ["log", "--no-merges", "--format=%H%x00%P%x00%an%x00%ae%x00%ad%x00%B%x1e", "--date=short"]
    if since:
        args.append("--since=" + since)
    if until:
        args.append("--until=" + until)
    args.append("--")
    args.extend(paths)
    out = git(repo, *args)
    for record in out.split("\x1e"):
        record = record.lstrip("\n")
        if not record:
            continue
        fields = record.split("\x00", 5)
        if len(fields) < 6:
            continue
        sha, parents, author, email, date, message = fields
        parent = parents.split()[0] if parents.strip() else ""
        yield sha, parent, author, email, date, message


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="harvest_feedback.py",
        description=(
            "List later human edits to Korean lines that an AI-assisted commit wrote. "
            "Prints JSON lines {commit, author, date, path, before, after, ai_commit}. "
            "Read-only: never mutates git state and never uses the network."
        ),
        epilog=(
            "Example: python3 <skill-dir>/scripts/harvest_feedback.py "
            "--since 2026-10-01 --paths docs CHANGELOG.md --max 20 --ai-pattern '<regex>'"
        ),
    )
    parser.add_argument("--since", default="90 days ago",
                        help="only commits after this date (git date syntax, default: '90 days ago')")
    parser.add_argument("--until", default=None, help="only commits before this date")
    parser.add_argument("--paths", nargs="*", default=[],
                        help="limit to these pathspecs (default: whole repository)")
    parser.add_argument("--max", type=int, default=50, help="stop after this many pairs (default: 50)")
    parser.add_argument("--max-commits", type=int, default=400,
                        help="scan at most this many human commits (default: 400)")
    parser.add_argument("--max-hunk-lines", type=int, default=40,
                        help="skip hunks removing more lines than this; they are usually rewrites or moves (default: 40)")
    parser.add_argument("--include-deletions", action="store_true",
                        help="also report hunks that only delete AI-written lines (after is empty)")
    parser.add_argument("--keep-identifier-only", action="store_true",
                        help="also report pairs whose Korean words are unchanged (only SHAs, paths or values changed)")
    parser.add_argument("--max-growth", type=float, default=3.0,
                        help="skip hunks that add more than this many times the removed lines; "
                             "they are usually rewrites, not wording fixes (default: 3, 0 disables)")
    parser.add_argument("--repo", default=".", help="repository path (default: current directory)")
    parser.add_argument("--ai-pattern", required=True,
                        help="regular expression that matches only agent-written commit messages "
                             "(case-insensitive, multiline)")
    args = parser.parse_args(argv)

    global AI_TRAILER
    try:
        AI_TRAILER = re.compile(args.ai_pattern, re.I | re.M)
    except re.error as exc:
        print("error: invalid --ai-pattern: %s" % exc, file=sys.stderr)
        return 2

    try:
        repo = git(args.repo, "rev-parse", "--show-toplevel").strip()
    except RuntimeError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2

    messages = MessageCache(repo)
    stats = {"commits_seen": 0, "human_commits": 0, "hunks_checked": 0, "pairs": 0}
    emitted = 0

    try:
        commits = list(iter_commits(repo, args.since, args.until, args.paths))
    except RuntimeError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 2

    for sha, parent, author, email, date, message in commits:
        stats["commits_seen"] += 1
        if emitted >= args.max or stats["human_commits"] >= args.max_commits:
            break
        if not parent or is_bot(author, email) or has_ai_trailer(message):
            continue
        stats["human_commits"] += 1
        diff = git(
            repo, "diff", "--no-color", "--no-ext-diff", "--unified=0", "-M",
            "--diff-filter=MR", parent, sha, "--", *args.paths, check=False,
        )
        # Lines that reappear elsewhere in the same commit were moved, not reworded.
        added_anywhere = set()
        hunks = list(iter_hunks(diff))
        for h in hunks:
            added_anywhere.update(a.strip() for a in h.added if a.strip())

        for h in hunks:
            if emitted >= args.max:
                break
            if not h.removed or len(h.removed) > args.max_hunk_lines:
                continue
            if not any(HANGUL.search(r) for r in h.removed):
                continue
            if not h.added and not args.include_deletions:
                continue
            if args.max_growth and len(h.added) > args.max_growth * max(1, len(h.removed)):
                continue
            stats["hunks_checked"] += 1
            blame = blame_lines(repo, parent, h.old_path, h.old_start, len(h.removed))
            by_ai: Dict[str, List[str]] = {}
            for offset, text in enumerate(h.removed):
                if not HANGUL.search(text) or text.strip() in added_anywhere:
                    continue
                origin = blame.get(h.old_start + offset)
                if origin and has_ai_trailer(messages.get(origin)):
                    by_ai.setdefault(origin, []).append(text)
            if not by_ai:
                continue
            removed_set = {r.strip() for r in h.removed}
            after = "\n".join(a for a in h.added if a.strip() not in removed_set)
            for ai_sha, lines in by_ai.items():
                if emitted >= args.max:
                    break
                before = "\n".join(lines)
                if not args.keep_identifier_only and after and \
                        HANGUL_WORD.findall(before) == HANGUL_WORD.findall(after):
                    continue  # Korean wording unchanged; only identifiers or values moved
                record = {
                    "commit": sha[:12],
                    "author": author,
                    "date": date,
                    "path": h.new_path,
                    "before": before,
                    "after": after,
                    "ai_commit": ai_sha[:12],
                }
                if h.old_path != h.new_path:
                    record["old_path"] = h.old_path
                print(json.dumps(record, ensure_ascii=False))
                emitted += 1
                stats["pairs"] += 1

    print(
        "harvest_feedback: %(commits_seen)d commits scanned, %(human_commits)d human commits, "
        "%(hunks_checked)d Korean hunks blamed, %(pairs)d pairs" % stats,
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
