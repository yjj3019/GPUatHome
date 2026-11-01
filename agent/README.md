# agent

유휴 감지 (NVML) + `rpc-server` 기동/종료.

## 필요 패키지

```
pynvml
```

## 동작 개요

1. NVML로 GPU 사용률·VRAM 폴링
2. 유휴 조건 충족 시 `rpc-server` 기동
3. 사용자 복귀 시 drain 후 종료
4. 하트비트를 controller에 전달
