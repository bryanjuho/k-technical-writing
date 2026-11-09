# 에이전트 작업 안내

- `AGENTS.local.md`가 있으면 먼저 확인
- 이 저장소의 한국어 문서는 `skills/k-technical-writing/references/style.md` 기준

## 구조

| 경로 | 내용 |
|---|---|
| `skills/k-technical-writing/SKILL.md` | 스킬 본문 |
| `skills/k-technical-writing/references/` | 문체 기준, 템플릿, 용어, 점검 목록, 학습 규칙 |
| `skills/k-technical-writing/scripts/harvest_feedback.py` | git 이력에서 표현 수정 사례 수집 |
| `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/`, `package.json` | Claude Code, Codex, pi 설치 정보 |

## 작업 규칙

- 규칙 변경 시 `SKILL.md`의 `metadata.version`과 각 설치 정보의 `version` 변경
- 예시 문장은 새로 작성. 회사 내부 정보 금지
- `harvest_feedback.py` 수정 시 `python3 -m py_compile`과 `--help`로 확인
