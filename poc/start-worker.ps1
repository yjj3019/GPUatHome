# PC1 또는 PC2 worker 기동
param(
    [string]$BindIp = "192.168.1.10",
    [int]$Port = 50052
)

Write-Host "Starting rpc-server on ${BindIp}:${Port}"
.\rpc-server.exe -H $BindIp -p $Port
