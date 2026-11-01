# PC1 hub 기동 예시
param(
    [string]$Model = "model.gguf",
    [string]$RpcEndpoint = "192.168.1.20:50052",
    [int]$Port = 8080
)

Write-Host "Starting llama-server with RPC $RpcEndpoint"
.\llama-server.exe -m $Model --rpc $RpcEndpoint -ngl 99 --host 0.0.0.0 --port $Port
