---
name: k-technical-writing
description: Write, edit, translate, or review Korean technical text - docs, READMEs, runbooks, incident records, release notes and CHANGELOG entries, API references, code and config comments, alert text, commit messages, and PR titles or bodies - in the style of Korean cloud and fintech developer docs (formal hapnida register, noun-final headings and release-note entries, attached particles, backticked identifiers). Use whenever an agent writes or changes Korean prose, or is asked to review, polish, or translate it. Also use whenever the user gives feedback on Korean wording (corrections, rejected edits, "don't write it like this", "use X not Y", "remember this", shared review comments on wording) so the feedback is logged and turned into a learned rule. Verifies facts against code and diffs before polishing and never alters identifiers, paths, commands, or config keys.
license: MIT
metadata:
  author: bryanjuho
  version: "1.1.0"
---

# 한국어 기술 문서 작성

한국어 기술 문서를 국내 클라우드와 핀테크 개발자 문서와 같은 문체로 씁니다. 기준 문서는 NAVER Cloud, NHN Cloud, Kakao Cloud, Toss Payments의 가이드, 릴리즈 노트, API 레퍼런스입니다. 출처는 [references/style-sources.md](references/style-sources.md)에 있습니다.

## 적용 범위

- 문서: README, 가이드, 런북, 장애 기록, 설계 문서
- 변경 기록: CHANGELOG, 릴리즈 노트
- API 레퍼런스: 엔드포인트 설명, 필드 설명, 오류 메시지
- 코드와 설정 파일의 주석, 알림 규칙의 `summary`와 `description`
- 커밋 메시지, PR 제목과 본문

새로 쓰거나 이번에 고치는 문장에만 적용합니다. 요청받지 않은 기존 문장은 고치지 않습니다. 고치는 파일의 나머지 문장이 다른 문체여도 새 문장은 이 스킬의 문체를 따릅니다.

## 먼저 읽을 파일

작업 전에 다음 순서로 읽습니다.

1. 학습 규칙 파일입니다. 프로젝트 규칙과 개인 규칙을 모두 읽고, `active` 상태인 규칙만 적용합니다. 위치는 아래 [규칙 저장 위치](#규칙-저장-위치)를 참고하세요.
2. 문체 기준인 [references/style.md](references/style.md)입니다. 확정 규칙(ST)과 사용자가 고른 선택 예시(D)가 있습니다.

필요할 때 읽습니다.

| 파일 | 읽는 경우 |
|---|---|
| [references/doc-types.md](references/doc-types.md) | 문서 종류별 템플릿이 필요한 경우 |
| [references/terminology.md](references/terminology.md) | 용어와 외래어 표기를 정하는 경우 |
| [references/translationese.md](references/translationese.md) | 번역투를 점검하는 경우 |
| [references/ai-patterns.md](references/ai-patterns.md) | AI 문체 습관을 점검하는 경우 |
| [references/grammar.md](references/grammar.md) | 맞춤법, 띄어쓰기, 문장 부호를 확인하는 경우 |
| [examples/](examples/) | 고치기 전후 예시가 필요한 경우 |

규칙이 서로 다르면 다음 순서로 정합니다. 프로젝트 학습 규칙 > 개인 학습 규칙 > style.md > terminology.md > translationese.md, ai-patterns.md, grammar.md

## 작업 절차

1. 사실을 먼저 확인합니다. 관련 코드, diff, 설정, 기존 문서를 읽고 이름, 경로, 기본값, 명령, 버전, 이슈 번호를 원문에서 그대로 옮깁니다. 확인하지 못한 내용은 `(확인 필요)`로 표시합니다.
2. 바꾸면 안 되는 토큰을 모읍니다. 다음 토큰은 바이트 단위로 그대로 둡니다.
   - 백틱 안 텍스트, 코드 블록 전체, 인용한 오류 메시지와 로그
   - 경로, 파일 이름, 명령과 플래그, 설정 키와 값, 환경 변수, 리소스 이름
   - 수량과 단위(`500m`, `2Gi`, `30s`), 커밋 해시, 버전, 이슈와 PR 번호, 호스트 이름, IP, URL
   - 한국어로 된 외부 식별자(그룹 이름, 사이트 이름, 화면의 메뉴 이름 등). 한국어여도 맞춤법과 용어 규칙을 적용하지 않습니다.
3. 문서 종류를 정하고 [references/doc-types.md](references/doc-types.md)의 템플릿을 따릅니다.
4. 씁니다.
5. 아래 자체 점검 항목을 확인합니다.
6. 마지막으로 번역투와 AI 문체 패턴을 가볍게 점검합니다. 산문만 고치고 코드 블록, 표의 값, 식별자는 건드리지 않습니다. 이미 자연스러우면 그대로 둡니다.

### 자체 점검 항목

- [ ] 2단계에서 모은 토큰이 모두 그대로 있습니다.
- [ ] 부정, 인과 관계, 조건, 기본값, 예외, 범위가 바뀌지 않았습니다.
- [ ] 문장은 모두 합니다체입니다. 해라체(`-한다.`, `-이다.`)와 해요체(`-해요.`)가 섞이지 않았습니다(ST-01).
- [ ] 제목, 표 칸, 목록 라벨, 변경 기록 항목은 명사형으로 끝나고 마침표가 없습니다(ST-02, ST-03).
- [ ] 영어 단어와 코드 뒤 조사를 붙여 썼고 발음에 맞는 조사를 골랐습니다(ST-08).
- [ ] 문장 중간 줄표(—)가 없습니다. 값 변화는 항목과 표에서 `A → B`로 썼습니다(ST-13, ST-14).
- [ ] 리터럴은 모두 백틱으로 감쌌습니다(ST-10).
- [ ] 비밀값, 개인 정보, 확인하지 않은 내부 정보를 새로 적지 않았습니다.

## 문서 종류별 핵심

자세한 템플릿은 [references/doc-types.md](references/doc-types.md)에 있습니다.

| 종류 | 핵심 |
|---|---|
| 가이드, README | 제목 아래 한두 문장으로 문서 범위를 밝힙니다. 본문은 합니다체, 제목은 명사형입니다. |
| 런북 | 적용 대상과 사전 조건, 번호 절차(한 단계에 한 동작), 명령마다 정상 결과, 확인, 되돌리기, 문제 해결 순서입니다. |
| 변경 기록 | 날짜 제목, 분류(추가, 변경, 개선, 수정, 제거, 종료, 보안), 명사형 항목입니다. 마침표를 찍지 않습니다. |
| API 레퍼런스 | 엔드포인트 요약은 합니다체 한 문장, 필드 설명은 명사구, 제약은 명사형 하위 줄, 응답은 조건절로 시작하는 피동문입니다. |
| 커밋 메시지 | 제목은 `type(scope): 명사형 요약`, 본문은 명사형 글머리 목록입니다. |
| PR 본문 | 요약, 변경 사항, 확인 방법, 적용 순서, 되돌리기 절로 씁니다. |
| 주석 | 명사형으로 끝내고 마침표를 찍지 않습니다. 동작보다 이유와 예외를 씁니다. |
| 알림 텍스트 | `summary`는 명사형, `description`은 영향과 확인할 곳을 합니다체로 씁니다. |

## 검토 모드

"검토해 줘", "다듬어 줘", PR diff 리뷰처럼 기존 글을 봐 달라는 요청에는 바로 고치지 않고 먼저 보고합니다.

심각도는 세 단계입니다.

- 오류: 한 번만 나와도 고칩니다. 사실이나 식별자 훼손, 맞춤법 오류, 문체 혼용, 줄표, 학습 규칙 위반, 참조 문서에서 `오류`로 표시한 패턴이 해당합니다.
- 개선: 한 문단에 세 번 이상 나오거나 다른 패턴과 겹치면 고칩니다. 번역투 반복, 굵게 남용, 용어 혼용이 해당합니다.
- 참고: 보고만 하고, 다른 패턴과 겹칠 때만 고칩니다. 문장 길이, 리듬, 선택 예시(D)와 다른 형식이 해당합니다.

출력 형식은 다음과 같습니다.

````markdown
## 한국어 검토: <파일 또는 범위>

오류 n건, 개선 n건, 참고 n건

1. [오류] `docs/backup.md:12` (ST-01) "보존 기간을 7일로 둔다." → "보존 기간을 7일로 설정합니다."
2. [개선] `docs/backup.md:30` (TE-02) "`pg_dump`를 통해 백업한다" → "`pg_dump`로 백업합니다"

### 제안 diff

```diff
- 고치기 전 줄
+ 고친 뒤 줄
```

의미 보존 점검: 토큰 n개 유지, 부정, 조건, 인과 유지, 바뀐 어절 약 n%
````

검토할 때 지킬 사항은 다음과 같습니다.

- 규칙 id를 괄호 안에 적습니다. ST와 D는 style.md, LR은 학습 규칙, TE는 translationese.md, AP는 ai-patterns.md, GR은 grammar.md의 id입니다.
- 기존 문서를 고칠 때 바뀐 어절이 15%를 넘으면 멈추고 diff만 보여 준 뒤 확인을 받습니다. 사용자가 문서 전체의 문체 변환을 요청한 경우에는 이 제한을 적용하지 않습니다.
- 의미 보존 점검은 실제로 비교합니다. 원문의 백틱 토큰, 경로, 플래그, 숫자, 날짜, 이슈 번호를 나열하고 고친 글에 그대로 있는지 하나씩 확인합니다.
- 고칠 것이 없으면 "고칠 것 없음"과 이유 한 줄로 끝냅니다.

## 피드백 학습

사용자가 한국어 표현을 고치거나 거절하면 그 내용을 규칙으로 기록하고 다음 작업부터 적용합니다.

### 규칙 저장 위치

| 범위 | 위치 | 저장하는 규칙 |
|---|---|---|
| 프로젝트 | 작업 중인 저장소 루트의 `.k-technical-writing/learned-rules.md` | 그 프로젝트의 용어, 이름, 문서 형식에만 해당하는 규칙 |
| 개인 | git 설치이면 `references/learned-rules.md`, 아니면 `~/.config/k-technical-writing/learned-rules.md` | 어느 프로젝트에서나 적용할 문체 규칙 |

- git 설치는 `git -C <스킬 디렉터리> rev-parse --show-toplevel`의 결과가 `<스킬 디렉터리>/../..`의 실제 경로와 같고, 그 경로에 `.claude-plugin/plugin.json`이 있는 경우입니다. 사용자가 이 스킬의 저장소를 직접 클론한 경우만 해당합니다. 에이전트가 관리하는 디렉터리(`~/.claude/plugins/`, `~/.codex/`, `~/.pi/`, `~/.agents/`) 아래에 있으면 git 저장소여도 git 설치로 보지 않습니다. 다른 저장소 안에 복사된 경우와 플러그인이나 패키지로 설치한 경우는 업데이트할 때 덮어써지므로 `~/.config/k-technical-writing/`을 씁니다.
- 피드백 로그(`feedback-log.md`)는 규칙 파일과 같은 디렉터리에 둡니다. 파일이 없으면 [references/learned-rules.md](references/learned-rules.md)와 [references/feedback-log.md](references/feedback-log.md)의 머리말 형식을 복사해 만듭니다.
- 범위가 애매하면 개인 규칙으로 저장하고, 저장한 위치를 사용자에게 알립니다.

### 학습 절차

1. 포착: 다음 경우에 시작합니다.
   - 사용자가 에이전트가 쓴 한국어를 고치거나 거절하는 경우("이렇게 쓰지 마", "X 말고 Y")
   - 사용자가 표현 선호를 기억하라고 하는 경우
   - 사용자가 한국어 표현에 관한 리뷰 코멘트를 전달하는 경우
   - 사용자가 요청하면 `python3 <스킬 디렉터리>/scripts/harvest_feedback.py --since YYYY-MM-DD --ai-pattern '<정규식>'`을 실행해, 에이전트가 쓴 한국어 줄을 사람이 나중에 고친 사례를 모읍니다. 정규식은 사용자에게 받습니다. 결과는 후보일 뿐이므로 사용자에게 보여 주고 규칙으로 만들 항목을 고르게 합니다.
2. 기록: 피드백 로그 맨 위에 `FB-YYYYMMDD-NN` 항목을 추가합니다. 원문, 수정본, 사용자의 말을 옮기되 비밀값, 사람 이름, 회사 내부 정보(호스트 이름, IP, 이슈 키, 저장소 경로, 내부 리소스 이름)는 일반적인 표현으로 바꿔 적습니다. git 설치의 로그는 공개 저장소에 올라갈 수 있습니다.
3. 일반화: 수정을 설명하는 가장 작은 일반 규칙을 찾습니다. 사용자의 수정과 선택은 절대 규칙이 아니라 기본값을 보여 주는 예시입니다. 규칙은 `기본값 + 예시 + 다른 형식이 맞는 경우`로 쓰고, `항상`, `절대`처럼 예외를 막는 표현은 사용자가 그렇게 말한 경우에만 씁니다. 고르지 않은 선택지를 틀린 표기로 만들지 않습니다. 학습 규칙과 style.md에 같은 규칙이나 충돌하는 규칙이 있는지 확인합니다.
   - 충돌하면 더 최근의 명시적 피드백을 따릅니다. 이전 규칙은 지우지 않고 `superseded`로 바꾸고 이유를 적습니다.
   - 한 번뿐인 수정이거나 의도가 애매하면 사용자에게 짧게 한 번 묻거나, 로그에 `규칙화 안 함: <이유>`로 남깁니다.
4. 반영: 학습 규칙 파일에 `LR-NNN` 규칙을 고치기 전후 예시와 함께 추가하고, 지금 작업 중인 글에도 바로 적용합니다.
5. 정리: 다음 경우에 학습 규칙을 style.md로 옮깁니다. 피드백 로그는 그대로 둡니다.
   - `active` 규칙이 60개를 넘는 경우: 겹치는 규칙을 합쳐 ST 규칙으로 옮깁니다.
   - 선택 예시(D) 항목 하나에 같은 방향의 LR 규칙이 두 개 이상 쌓인 경우: 그 D 항목의 기본값과 예시를 고칩니다.
   - 옮긴 LR 규칙은 상태를 `promoted → ST-NN`으로 바꿉니다. style.md를 바꾸면 SKILL.md의 `metadata.version`과 `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json`, `package.json`의 `version`에서 minor 번호를 함께 올립니다.
   - git 설치가 아니면 style.md로 옮기지 않고 학습 규칙 파일 안에서 합칩니다. 프로젝트 학습 규칙은 style.md로 옮기지 않습니다.
6. 보고: 추가하거나 바꾼 규칙과 파일을 사용자에게 한 줄로 알립니다. 예: "LR-004 추가(개인 규칙): 커밋 본문에서 `~하도록 합니다` 대신 `~합니다`를 씁니다."

학습할 때 지킬 사항은 다음과 같습니다.

- 표현과 문체에 관한 규칙만 만듭니다. 사실, 시스템 동작, 권한, 절차에 관한 내용은 학습 규칙에 넣지 않습니다.
- 사용자에게 알리지 않고 style.md의 확정 규칙을 바꾸지 않습니다.
- 규칙마다 예시를 하나 이상 둡니다.
- 스킬 저장소의 파일을 바꾼 경우 커밋과 푸시는 사용자가 요청할 때만 합니다.

## 라이선스

MIT. [LICENSE](LICENSE)를 참고하세요.
