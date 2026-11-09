# 런북 절차

해라체 나열로 쓴 절차를 번호 절차로 바꾼 예입니다.

## 전

```markdown
인증서가 만료되면 먼저 `kubectl get certificate -A` 로 상태를 본다. READY 가 False 인 것을 찾아서
`kubectl describe` 로 이벤트를 확인하고, DNS 검증 실패면 토큰을 갱신한 뒤 시크릿을 지워서 재발급을 낸다.
시크릿을 지우면 잠깐 HTTPS 가 끊길 수 있다.
```

## 후

````markdown
## 인증서 재발급

만료된 인증서를 찾아 다시 발급하는 방법은 다음과 같습니다.

1. 인증서 상태를 확인합니다.

   ```bash
   kubectl get certificate -A
   ```

   `READY`가 `False`인 인증서가 재발급 대상입니다.

2. 대상 인증서의 이벤트를 확인합니다.

   ```bash
   kubectl describe certificate <이름> -n <네임스페이스>
   ```

   `Events`에 실패 원인이 표시됩니다.

3. 이벤트에 DNS 검증 실패가 있으면 DNS API 토큰을 갱신합니다.

> **주의**
> 인증서 시크릿을 삭제하면 재발급이 끝날 때까지 HTTPS 연결이 끊길 수 있습니다.

4. 인증서 시크릿을 삭제합니다.

   ```bash
   kubectl delete secret <시크릿 이름> -n <네임스페이스>
   ```

   잠시 후 `READY`가 `True`로 바뀌면 재발급이 끝난 것입니다.
````

## 바꾼 점

- 한 단계에 동작 하나만 썼습니다(ST-04).
- 명령마다 목적과 정상 결과를 썼습니다(ST-20).
- 연결이 끊길 수 있는 단계 앞에 `주의` 블록을 두었습니다(ST-19).
- `재발급을 낸다`처럼 뜻이 넓은 동사를 구체적인 동작으로 바꿨습니다(terminology.md 동사 표).
- 상태 값 `READY`, `False`, `True`를 백틱으로 감쌌습니다(ST-10).
