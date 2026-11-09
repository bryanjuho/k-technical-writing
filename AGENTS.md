# 에이전트 작업 안내

이 저장소는 한국어 기술 문서 작성 스킬 `k-technical-writing`을 배포합니다. `AGENTS.local.md`가 있으면 이 파일보다 먼저 읽고 따릅니다.

## 구조

| 경로 | 내용 |
|---|---|
| `skills/k-technical-writing/SKILL.md` | 스킬 본문 |
| `skills/k-technical-writing/references/` | 문체 기준, 템플릿, 용어, 패턴, 학습 규칙 |
| `skills/k-technical-writing/examples/` | 고치기 전후 예시 |
| `skills/k-technical-writing/scripts/harvest_feedback.py` | git 이력에서 표현 수정 사례를 모으는 스크립트 |
| `.claude-plugin/` | Claude Code 플러그인 정보 |

## 작업 규칙

- 이 저장소의 한국어 문서는 스킬 자신의 문체 기준(`references/style.md`)을 따릅니다.
- 규칙을 추가하거나 바꾸면 관련 예시와 함께 SKILL.md의 `metadata.version`, `.claude-plugin/plugin.json`과 `.claude-plugin/marketplace.json`의 `version`을 올립니다.
- 예시 문장은 새로 씁니다. 특정 회사의 내부 정보나 기준 문서의 긴 문장을 넣지 않습니다.
- `scripts/harvest_feedback.py`를 수정하면 다음 명령으로 확인합니다.

  ```bash
  python3 -m py_compile skills/k-technical-writing/scripts/harvest_feedback.py
  python3 skills/k-technical-writing/scripts/harvest_feedback.py --help
  ```
