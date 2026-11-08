# 쇼츠 074 · 권한 모드와 안전장치

- **원본 페이지:** 18.1.2 [권한 모드와 안전장치](../../../docs/part5/ch18/permissions.md)
- **형식:** 세로 9:16, 30fps, 음성 없음, 약 28초.
- **한 가지 생각:** 권한 모드는 묻지 않고 해도 되는 범위라서, 처음엔 기본과 계획 모드로 시작하고 bypassPermissions는 격리된 환경에서만 쓴다.
- **상태:** 초안(평가 대기)

| # | 모양 | 화면 |
|---|---|---|
| 1 | bigword | 권한 모드는 운전 보조 장치 / 익숙한 길에서만 하나씩 켜요 |
| 2 | list | 묻지 않고 하는 범위: default → 읽기만 / acceptEdits → 파일 고치기까지 / plan → 읽기만 (계획) / auto → 거의 모두, 안전 점검 / dontAsk → 허락한 도구만 / bypassPermissions → 모두 |
| 3 | split | bypass Permissions ↔ 컨테이너나 가상 머신 안에서만 |
| 4 | speech | claude --permission-mode default → 기본으로 시작해서 계획 모드로만 살펴봐요 |
| 5 | check | 오늘의 써먹기: 처음엔 기본과 계획 모드면 충분 / acceptEdits는 결과를 볼 일에만 / 내 설정에 bypass가 없는지 확인 |

## 확인할 점
- 모드 이름과 범위는 원본 표(공식 문서 기준)예요. 바뀔 수 있어요.
