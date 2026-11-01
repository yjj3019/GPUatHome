# controller

PC3 허브 제어 로직.

## 역할

- PC1·PC2 워커 등록 및 상태 수집
- `llama-server --rpc`로 모델 분할 실행
- 단일 GPU 모델은 Ollama 대리 경로로 전환 가능

## 구조

```
PC3 (hub + client)
  → llama-server --rpc
    → PC1 rpc-server (GPU)
    → PC2 rpc-server (GPU)
```

VPN 지연이 RPC 호출마다 누적된다. 측정 후 성능 확인 필요.
