# k-technical-writing

An agent skill that makes AI agents write Korean technical text in the style of Korean cloud and fintech developer docs. It records user feedback as rules and applies them from the next task on.

[한국어](README.md)

## What it covers

- READMEs, guides, runbooks, incident records
- CHANGELOGs and release notes
- API references
- Code and config comments, alert text
- Commit messages and PR descriptions

## Style baseline

The rules were derived from the public developer docs of NAVER Cloud, NHN Cloud, Kakao Cloud, and Toss Payments. Where those docs disagree, the author compared candidate sentences and picked examples that serve as defaults. They are examples, not hard rules, so other forms are used when the context calls for them. Highlights:

| Area | Rule |
|---|---|
| Sentences | Formal declarative register (합니다체) |
| Headings, table cells, changelog entries | Noun-final, no period |
| Particles after English words and code | Attached, chosen by pronunciation (`API를`, `` `helm`과 ``) |
| Names vs. concepts | Product and resource names in English, generic concepts in Korean |
| Value changes | `` `7d` → `14d` `` in entries and tables |
| Em dashes | Not used |

Full rules: [style.md](skills/k-technical-writing/references/style.md). Sources: [style-sources.md](skills/k-technical-writing/references/style-sources.md).

## Install

### With git (recommended)

Install as a git working tree so rules learned from feedback can be committed back to the skill.

```bash
git clone https://github.com/bryanjuho/k-technical-writing.git ~/src/k-technical-writing
mkdir -p ~/.claude/skills
ln -s ~/src/k-technical-writing/skills/k-technical-writing ~/.claude/skills/k-technical-writing
```

For other agents that support the Agent Skills format, link the same directory into that agent's skills directory.

### As a plugin or package

Install straight from the GitHub repository. Nothing is published to npm.

| Agent | Commands |
|---|---|
| Claude Code | `claude plugin marketplace add bryanjuho/k-technical-writing`<br>`claude plugin install k-technical-writing@k-technical-writing` |
| Codex | `codex plugin marketplace add bryanjuho/k-technical-writing`<br>`codex plugin add k-technical-writing@k-technical-writing` |
| pi | `pi install git:github.com/bryanjuho/k-technical-writing` |
| Other agents | `npx skills add bryanjuho/k-technical-writing` |

Plugin and package installs are overwritten on update, so learned rules go to `~/.config/k-technical-writing/` instead.

## Self-improvement

When you correct Korean an agent wrote, the agent logs the correction, adds a rule to `learned-rules.md` (which takes precedence over every other rule), and tells you in one line what it added. Once enough rules accumulate, they are promoted into `style.md` (git installs only). With a git install, learned rules and the feedback log can end up in a public repository, so the agent rewrites company-internal details into generic wording before logging them.

| Scope | Location |
|---|---|
| Project | `.k-technical-writing/learned-rules.md` at the project root |
| Personal (git install) | `skills/k-technical-writing/references/learned-rules.md` |
| Personal (plugin or package) | `~/.config/k-technical-writing/learned-rules.md` |

`scripts/harvest_feedback.py` collects later human edits to Korean lines that AI-assisted commits wrote, as rule candidates. Pass `--ai-pattern` with a regular expression that matches only agent-written commit messages.

## License

MIT. See [LICENSE](LICENSE).
