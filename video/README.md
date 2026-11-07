# 영상 (v0.2)

각 주제 페이지를 세로 쇼츠 한 편으로 만드는 작업 폴더예요. 만드는 방법과 원칙은 `.claude/skills/video-script/SKILL.md`에 있어요.

| 번호 | 영상 | 원본 페이지 | 길이 | 상태 |
|---|---|---|---|---|
| 001 | 챗봇은 '다음 말'을 맞히는 기계 | 1.1.1 | 41초 | v2(팝 스티커·박자 편집), 평가 대기 |

## 만들기

```bash
cd video/shorts/001-next-word
bash build.sh        # 프레임 렌더링 → 음악 → mp4 (out/ 폴더)
```

필요한 것: Node와 Playwright(Chromium), ffmpeg, Python 3와 numpy, scipy. 처음부터 끝까지 이 환경에서 약 1~2분 걸렸어요.

## 구성

- `script.md`: 장면표와 근거(원본 페이지의 어느 부분인지), 평가 질문
- `scene.html`: 모든 장면. `seek(t)`로 시간을 정하면 그 시점의 화면이 그려져요
- `render.js`: 프레임마다 `seek`하고 JPEG로 저장
- `make_music.py`: 배경음악과 효과음을 직접 합성(저작권 문제 없음). 박자는 128bpm이에요
- `out/timeline.json`: 렌더링할 때 만들어지는 효과음 목록(박자와 종류)
- `build.sh`: 위를 이어서 mp4와 썸네일 생성
