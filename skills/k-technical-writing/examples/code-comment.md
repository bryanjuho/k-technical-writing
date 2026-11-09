# 코드와 설정 주석

해라체와 줄표로 쓴 주석을 명사형 주석으로 바꾼 예입니다.

## 전

```yaml
# **replicas 는 일부러 1 로 둔다** — RWO 볼륨이라 두 Pod 가 동시에 못 붙고,
# 롤링 업데이트 중에 새 Pod 가 Pending 으로 멈춘다. 그래서 strategy 도 Recreate 로 둔다.
replicas: 1
strategy:
  type: Recreate
# 1시간마다 돈다
schedule: "0 * * * *"
```

## 후

```yaml
# RWO 볼륨은 한 개의 Pod에만 연결할 수 있으므로 복제본을 늘리면 신규 Pod는 Pending에 머물게 됨
# RollingUpdate도 같은 이유로 쓸 수 없어 Recreate로 설정함
replicas: 1
strategy:
  type: Recreate
# 정각마다 실행해 백업 시각을 다른 작업과 분리
schedule: "0 * * * *"
```

## 바꾼 점

- 이유는 원인과 결과를 한 문장으로 잇고 `~됨`, `~함`으로 끝냈습니다(D-07).
- 주석 안의 굵게(`**`)와 줄표를 뺐습니다(AP-19, ST-14).
- 코드를 읽으면 알 수 있는 `# 1시간마다 돈다`는 이유를 쓰는 명사형 한 줄 주석으로 바꿨습니다. 주석에는 동작보다 이유와 함께 바꿔야 할 곳을 씁니다.
- 조사를 붙여 썼습니다(ST-08).
