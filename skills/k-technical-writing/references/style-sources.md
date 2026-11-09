# 기준 문서

[style.md](style.md)의 규칙은 아래 문서를 읽고 정리했습니다. 문체를 확인하는 용도로만 참고했고, 인용은 한 문장 이내로 줄였습니다. 확인한 날짜는 2026년 11월 9일입니다.

| 문서 | 주로 참고한 내용 |
|---|---|
| [NAVER Cloud 사용 가이드](https://guide.ncloud-docs.com/docs/home) | 가이드 문장, 콘솔 절차, 화면 요소 표기, 참고와 주의 블록 |
| [NAVER Cloud 릴리스 노트(2026년 9월 17일)](https://guide.ncloud-docs.com/docs/releasenote-20260917) | 릴리스 노트 분류와 명사형 항목 |
| [NAVER Cloud API 레퍼런스](https://api.ncloud-docs.com/docs/home) | 필드 설명과 제약 표기 |
| [NHN Cloud 개요](https://docs.nhncloud.com/ko/nhncloud/ko/overview/) | 서비스 소개 문장 |
| [NHN Cloud Instance 콘솔 사용 가이드](https://docs.nhncloud.com/ko/Compute/Instance/ko/console-guide/) | 가이드 문장, 콘솔 절차, 참조 문장 |
| [NHN Cloud Instance API 가이드](https://docs.nhncloud.com/ko/Compute/Instance/ko/public-api/) | 파라미터 표, 필드 설명 |
| [NHN Cloud Compute 릴리스 노트](https://docs.nhncloud.com/ko/Compute/Compute/ko/release-notes/) | 날짜 제목, 명사형 항목, 버그 수정 항목 |
| [Kakao Cloud 문서](https://docs.kakaocloud.com/) | 가이드 문장, 절차, 명령 뒤 정상 결과 문장 |
| [Kakao Cloud API 변경 사항](https://docs.kakaocloud.com/openapi/changelogs) | API 변경이력 표, 필드 설명 |
| [Toss Payments API 레퍼런스](https://docs.tosspayments.com/reference) | 필드와 열거 값 설명, 응답과 오류 문장 |
| [Toss Payments 릴리스 노트](https://docs.tosspayments.com/resources/release-note) | 제거와 대체 수단을 함께 쓰는 형식 |

## 짧은 인용

문체를 보여 주는 문장만 골랐습니다.

| 출처 | 인용 | 관련 규칙 |
|---|---|---|
| NAVER Cloud | 서버는 최대 10개까지 생성할 수 있습니다. | ST-01, ST-06 |
| NAVER Cloud | Workspace 삭제 시 하위 Dataset이 함께 삭제되지 않던 문제 수정 | ST-22 |
| NAVER Cloud | 액션 기본 메모리 256MB에서 128MB로 변경 | ST-02, ST-15 |
| NHN Cloud | 국가 또는 지역을 선택합니다. | D-01 |
| NHN Cloud | 한번 선택한 블록 스토리지 타입은 변경할 수 없습니다. | ST-06 |
| NHN Cloud | NVIDIA 드라이버 업데이트: 580.105.08 → 580.173.02 | ST-13 |
| NHN Cloud | 이 API는 요청 본문을 요구하지 않습니다. | ST-23 |
| Kakao Cloud | 삭제한 시크릿은 복구할 수 없습니다. | ST-06 |
| Kakao Cloud | 요청 필드 `description`을 필수에서 선택으로 변경 | ST-08, ST-22 |
| Kakao Cloud | 시크릿 접근 제어 활성화 여부 | ST-23 |
| Toss Payments | 최대 길이는 200자입니다. | ST-23 |
| Toss Payments | 값을 넣지 않으면 기본값인 `0`으로 설정됩니다. | ST-06, ST-10 |

## 기준 문서끼리 다른 점

| 항목 | NAVER Cloud | NHN Cloud | Kakao Cloud | Toss Payments |
|---|---|---|---|---|
| 절차 단계 어미 | `-해 주십시오` | `-합니다` | `-합니다`(콘솔), `-하세요`(튜토리얼) | `-하세요` |
| 다른 문서 참조 | `참고해 주십시오` | `참고합니다` | `참고하세요` | `참고하세요` |
| 변경이력 형식 | 3열 표(구분, 변경 내용, 상세 경로), 명사형 | 서비스별 소제목, 명사형 항목, 합니다체 하위 항목 | API 변경 사항은 명사형 표, 서비스 릴리스 노트는 합니다체 문단 | 명사형 제목 + 해요체 문단 |
| 변경이력 날짜 | `2026. 9. 17.` | `2026. 08. 20.` | `2026.11.05.` | `2026년 10월` |
| API 제약 표기 | 명사형 줄 | 명사형 줄 | 명사형 줄 | 합니다체 문장 |
| 버튼 표기 | **[버튼]** | **버튼** | [버튼] | '**버튼**' |
| 가운뎃점 | 거의 없음 | 없음(짝 명사는 `/`) | 짝 명사와 나열 | 짝 명사와 나열 |
| `release` 표기 | 릴리스 | 릴리스 | 릴리즈 | 릴리즈 |
| `snapshot` 표기 | 스냅샷 | 스냅숏 | 확인하지 않음 | 확인하지 않음 |

다른 점은 사용자가 후보를 비교해 고른 뒤 style.md의 선택 예시(D)로 정리했습니다.
