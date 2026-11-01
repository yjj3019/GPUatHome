# GPUatHome

유휴 GPU 풀링을 통한 홈 네트워크 LLM 실행 프로젝트.

## 개요

- **목표**: PC1·PC2의 유휴 GPU를 PC3에서 활용해 LLM을 실행
- **구조**:
  - PC1·PC2: GPU 워커 (`rpc-server` + 유휴 감지 에이전트)
  - PC3: 허브 (`llama-server --rpc`) + 컨트롤러
- **네트워크**: PC1·PC2는 같은 LAN, PC3는 VPN 연결
- **판정**: 조건부 가능 (llama.cpp RPC 기반)
- **구현 위치**: 이 저장소

상세 설계는 Notion 페이지를 참조.

## 디렉터리 구조

```
GPUatHome/
├── docs/          # 설계 문서, 측정 결과
├── poc/           # 수동 PoC 스크립트
├── agent/         # 유휴 감지·기동·종료 에이전트 (PC1·PC2)
├── controller/    # 허브 제어 로직 (PC3)
└── README.md
```

## 다음 단계

1. PC1·PC2에 `rpc-server` + 유휴 에이전트 배치
2. PC3에 `llama-server --rpc` 구축
3. 네트워크·성능 측정은 추후 진행

## 보안 주의

- llama.cpp `rpc-server`는 인증이 없음. LAN 바인딩 + IP 제한 + VPN 터널 필수.
- PC3 허브 구조는 VPN 지연이 RPC마다 누적됨. 측정 후 재검토 가능.
