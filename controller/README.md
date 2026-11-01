# controller

LAN 허브 제어 로직.

## 역할

- 워커 등록 및 상태 수집
- PC3 요청을 로컬 `llama-server`로 라우팅
- 단일 GPU 모델은 Ollama 대리 경로로 전환 가능

## 예시 구조

```
PC3 (client)
  → controller (PC1)
    → llama-server (PC1, RPC to PC2)
    or Ollama (PC1)
```
