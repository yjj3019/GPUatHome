# poc

수동 PoC 스크립트 및 측정 기록.

## 예시

```bash
# PC2 (worker)
./rpc-server -H 0.0.0.0 -p 50052

# PC1 (hub)
./llama-server -m model.gguf --rpc <PC2_IP>:50052 -ngl 99
```
