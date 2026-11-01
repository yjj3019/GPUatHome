# PC3 hub 기동
param(
    [string]$Model = "model.gguf",
    [string]$RpcEndpoints = "192.168.1.10:50052,192.168.1.20:50052",
    [int]$Port = 8080
)

Write-Host "Starting llama-server with RPC $RpcEndpoints"
.\llama-server.exe -m $Model --rpc $RpcEndpoints -ngl 99 --host 0.0.0.0 --port $Port
