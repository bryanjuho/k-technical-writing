# 알림 텍스트

## 전

```yaml
annotations:
  summary: "PVC 사용률이 높습니다!"
  description: "{{ $labels.persistentvolumeclaim }} 의 사용률이 85% 를 넘었다 — 곧 꽉 찰 수 있으니 확인 바람."
```

## 후

```yaml
annotations:
  summary: "{{ $labels.namespace }}/{{ $labels.persistentvolumeclaim }} 볼륨 사용률 85% 초과"
  description: >-
    {{ $labels.persistentvolumeclaim }} 볼륨 사용률이 15분 동안 85%를 넘었습니다.
    볼륨이 가득 차면 애플리케이션이 데이터를 쓰지 못합니다.
    볼륨 크기를 늘리거나 오래된 데이터를 삭제하세요.
```

## 바꾼 점

- `summary`는 대상과 상태를 명사형으로 썼고 느낌표와 마침표를 뺐습니다(ST-02, GR-18).
- `description`은 상태, 영향, 대응 순서의 합니다체 문장으로 썼습니다.
- `확인 바람`처럼 끝맺음이 모호한 표현 대신 할 일을 구체적으로 썼습니다.
- 템플릿 변수 뒤에는 조사 대신 `볼륨`을 넣어 발음과 상관없이 읽히게 했습니다.
