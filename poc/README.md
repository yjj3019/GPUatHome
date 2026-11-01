# poc

수동 PoC 스크립트. 측정은 추후 진행.

## 구조

- PC1·PC2: GPU 워커 (`rpc-server`)
- PC3: 허브 (`llama-server --rpc`)

## Worker (PC1 또는 PC2)

```powershell
# LAN IP만 바인딩
.\rpc-server.exe -H 192.168.1.10 -p 50052
```

## Hub (PC3)

```powershell
# 워커 등록 후 시작 (VPN 경유)
.\llama-server.exe -m model.gguf --rpc 192.168.1.10:50052,192.168.1.20:50052 -ngl 99 --host 0.0.0.0 --port 8080
```

## 단일 GPU (Ollama 대안)

PC1·PC2에서 Ollama 실행 후 PC3에서:

```powershell
$env:OLLAMA_HOST = "http://192.168.1.10:11434"
ollama run qwen3:8b
```

## 보안

- `rpc-server`는 인증 없음. 방화벽으로 PC3 IP만 허용.
- VPN 터널 내부에서만 노출.
