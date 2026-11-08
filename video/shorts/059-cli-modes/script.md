# 쇼츠 059 · 대화 모드와 한 줄 모드

- **원본 페이지:** 16.4.1 [대화 모드와 한 줄 모드](../../../docs/part5/ch16/cli-modes.md)
- **형식:** 세로 9:16, 30fps, 음성 없음, 약 28초.
- **한 가지 생각:** claude는 주고받는 대화 모드, claude -p는 답만 받고 끝나는 한 줄 모드라서 자동화의 문이 된다.
- **상태:** 초안(평가 대기)

| # | 모양 | 화면 |
|---|---|---|
| 1 | bigword | claude -p는 자판기예요 / 버튼 한 번에 답 하나 받고 끝나요 |
| 2 | split | claude ↔ claude -p "질문" |
| 3 | list | 지난 대화 이어 가기: claude -c → 최근 대화 이어 가기 / claude -r "이름" → 그 대화 다시 열기 / /resume → 대화 안에서 고르기 |
| 4 | speech | claude --add-dir ../다른폴더 → 그 폴더를 고칠 권한이 생겨요. 믿을 수 있는 폴더만요 |
| 5 | check | 오늘의 써먹기: 한 번 묻고 끝나면 claude -p / 어제 하던 일은 claude -c / 이름 붙인 대화는 claude -r "이름" |

## 확인할 점
- --model, --permission-mode 옵션은 뺐어요.
