# k-technical-writing

AI 에이전트가 한국어 기술 문서를 국내 클라우드와 핀테크 개발자 문서와 같은 문체로 쓰도록 돕는 스킬입니다. 사용자 피드백을 규칙으로 기록하고 다음 작업부터 적용합니다.

[English](README_EN.md)

## 다루는 문서

- README, 가이드, 런북, 장애 기록
- CHANGELOG, 릴리즈 노트
- API 레퍼런스
- 코드와 설정 파일 주석, 알림 텍스트
- 커밋 메시지, PR 본문

## 문체 기준

NAVER Cloud, NHN Cloud, Kakao Cloud, Toss Payments의 공개 개발자 문서를 읽고 공통 규칙을 정리했습니다. 기준 문서끼리 다른 부분은 문장 후보를 비교해 고른 예시를 기본값으로 둡니다. 예시는 절대 규칙이 아니어서 맥락에 따라 다른 형식을 씁니다. 주요 규칙은 다음과 같습니다.

| 항목 | 규칙 |
|---|---|
| 문장 | 합니다체 |
| 제목, 표 칸, 변경 기록 항목 | 명사형, 마침표 없음 |
| 영어 단어와 코드 뒤 조사 | 붙여 쓰고 발음에 맞춤(`API를`, `` `helm`과 ``) |
| 이름과 개념 | 제품과 리소스 이름은 영어, 일반 개념은 한국어 |
| 값 변화 | 항목과 표에서 `` `7d` → `14d` `` |
| 줄표(—) | 쓰지 않음 |

전체 규칙은 [style.md](skills/k-technical-writing/references/style.md), 출처는 [style-sources.md](skills/k-technical-writing/references/style-sources.md)에 있습니다.

## 설치

### git으로 설치(권장)

피드백으로 학습한 규칙을 스킬 저장소에 기록하고 커밋하려면 git 작업 트리로 설치합니다.

```bash
git clone https://github.com/bryanjuho/k-technical-writing.git ~/src/k-technical-writing
mkdir -p ~/.claude/skills
ln -s ~/src/k-technical-writing/skills/k-technical-writing ~/.claude/skills/k-technical-writing
```

Agent Skills 형식을 지원하는 다른 에이전트는 그 에이전트의 스킬 디렉터리에 같은 방법으로 연결합니다.

### Claude Code 플러그인으로 설치

```bash
claude plugin marketplace add bryanjuho/k-technical-writing
claude plugin install k-technical-writing@k-technical-writing
```

### skills CLI로 설치

```bash
npx skills add bryanjuho/k-technical-writing
```

플러그인이나 skills CLI로 설치한 스킬은 업데이트할 때 파일이 덮어써집니다. 이 경우 학습 규칙은 `~/.config/k-technical-writing/`에 기록됩니다.

## 사용 방법

한국어 문서를 쓰거나 고치는 작업에서 에이전트가 스킬을 자동으로 불러옵니다. 직접 요청할 수도 있습니다.

```text
이 CHANGELOG 항목을 k-technical-writing 스킬로 검토해 줘.
```

검토 요청에는 바로 고치지 않고 심각도별(오류, 개선, 참고) 보고와 diff를 먼저 보여 줍니다.

## 피드백 학습

에이전트가 쓴 한국어를 고쳐 주면 에이전트가 다음 순서로 학습합니다.

1. 피드백 로그(`feedback-log.md`)에 원문, 수정본, 사용자의 말을 기록합니다.
2. 수정을 설명하는 규칙을 학습 규칙 파일(`learned-rules.md`)에 추가합니다. 학습 규칙은 다른 모든 규칙보다 우선합니다.
3. 추가한 규칙을 한 줄로 알려 줍니다.
4. 학습 규칙이 쌓이면 문체 기준(`style.md`)으로 옮깁니다. git 설치에서만 옮깁니다.

git 설치에서는 학습 규칙과 피드백 로그가 공개 저장소에 올라갈 수 있습니다. 에이전트는 로그에 회사 내부 정보를 적지 않고 일반적인 표현으로 바꿔 기록합니다.

규칙 저장 위치는 다음과 같습니다.

| 범위 | 위치 |
|---|---|
| 프로젝트 | 프로젝트 루트의 `.k-technical-writing/learned-rules.md` |
| 개인(git 설치) | `skills/k-technical-writing/references/learned-rules.md` |
| 개인(플러그인, skills CLI 설치) | `~/.config/k-technical-writing/learned-rules.md` |

git 이력에서 사람이 고친 표현을 모아 학습 후보로 쓸 수도 있습니다.

```bash
python3 ~/.claude/skills/k-technical-writing/scripts/harvest_feedback.py --since 2026-10-01 --ai-pattern '<에이전트가 쓴 커밋을 구분하는 정규식>'
```

`--ai-pattern`에는 에이전트가 쓴 커밋의 메시지에만 맞는 정규식을 지정합니다. 스크립트는 그 커밋이 쓴 한국어 줄을 사람이 나중에 고친 사례를 찾습니다.

## 라이선스

MIT. [LICENSE](LICENSE)를 참고하세요.
