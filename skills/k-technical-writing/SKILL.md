---
name: k-technical-writing
description: Write, edit, or review Korean technical text (docs, READMEs, runbooks, changelogs, API references, code comments, alert text, commit messages, PRs) in the style of Korean technical docs and commercial software changelogs. Use whenever an agent writes or changes Korean prose, and whenever the user corrects Korean wording, so the correction becomes a learned rule.
license: MIT
metadata:
  author: bryanjuho
  version: "1.2.0"
---

# 한국어 기술 문서

## 참고 파일

| 파일 | 내용 |
|---|---|
| 학습 규칙 `learned-rules.md` | 사용자 피드백으로 추가한 규칙. 최우선 |
| [style.md](references/style.md) | ST: 지켜야 하는 규칙, D: 상황에 따라 참고하는 사용자 선택 항목 |
| [doc-types.md](references/doc-types.md) | 문서 종류별 템플릿 |
| [terminology.md](references/terminology.md) | 용어, 동사 표기 |
| [checks.md](references/checks.md) | 맞춤법, 번역투, AI 문체 점검 |

## 작성

- 사실은 코드, diff, 설정에서 확인. 확인하지 못한 내용은 `(확인 필요)` 표시
- 백틱 안 텍스트, 코드 블록, 경로, 명령, 설정 키와 값, 버전, 번호, URL은 원문 유지
- 새로 쓰거나 고치는 문장만 변경
- 부정, 조건, 인과, 기본값, 범위 유지

## 검토

- 기존 글 검토 요청 시 수정 전에 보고
- 오류: 사실 훼손, 맞춤법, 문체 혼용, ST와 학습 규칙 위반. 바로 수정
- 개선: 번역투, AI 문체, D와 다른 형식. 제안만
- 고칠 내용이 없으면 "수정 사항 없음"

```markdown
오류 1건, 개선 1건

1. [오류] `docs/backup.md:12` "보존 기간을 7일로 둔다." → "보존 기간을 7일로 설정합니다."
2. [개선] `docs/backup.md:30` "`pg_dump`를 통해 백업" → "`pg_dump`로 백업"
```

## 학습

사용자가 한국어 표현을 수정하거나 선호를 말한 경우

1. `feedback-log.md` 맨 위에 원문, 수정본, 사용자 말 기록. 사람 이름, 회사 내부 정보는 일반 표현으로 변경
2. `learned-rules.md`에 `LR-NNN` 규칙과 전후 예시 추가. 수정은 예시로 취급하고 예외를 막는 규칙으로 만들지 않음
3. 추가한 규칙을 한 줄로 보고

| 범위 | 위치 |
|---|---|
| 프로젝트 | `<저장소 루트>/.k-technical-writing/` |
| 개인, 직접 클론 | `<스킬 디렉터리>/references/` |
| 개인, 플러그인 또는 패키지 설치 | `~/.config/k-technical-writing/` |

- `~/.claude/`, `~/.codex/`, `~/.pi/`, `~/.agents/` 아래 클론은 플러그인 설치로 취급
- 학습 규칙이 쌓이면 style.md로 이동(직접 클론만). 이동 시 `metadata.version`, `.claude-plugin/`, `.codex-plugin/`, `package.json`의 `version` 변경
- `scripts/harvest_feedback.py --since YYYY-MM-DD --ai-pattern '<정규식>'`: 에이전트가 쓴 줄을 사람이 고친 사례를 git 이력에서 수집. 사용자 요청 시에만 실행
