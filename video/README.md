# 영상 (v0.2)

각 주제 페이지를 세로 쇼츠 한 편으로 만드는 작업 폴더예요. 만드는 방법과 원칙은 `.claude/skills/video-script/SKILL.md`에 있어요.

| 번호 | 영상 | 원본 페이지 | 길이 | 상태 |
|---|---|---|---|---|
| 001 | 챗봇은 '다음 말'을 맞히는 기계 | 1.1.1 | 40초 | 확정(사용자 평가 반영) |
| 002 | 글자를 '토큰'이라는 조각으로 쪼개 읽는다 | 1.1.2 | 25초 | 초안, 평가 대기 |

## 만들기

영상은 **재료 상자**(`video/engine`)로 만들어요. 새 영상은 `shorts/NNN-이름/episode.json`(장면표)만 쓰고 이렇게 실행해요. 블록 종류와 쓰는 법은 [engine/README.md](engine/README.md)에 있어요.

```bash
bash video/engine/build.sh video/shorts/002-tokens        # 조용한 음악(기본)
MUSIC=loud bash video/engine/build.sh video/shorts/002-tokens   # 신나는 음악
```

필요한 것: Node와 Playwright(Chromium), ffmpeg, Python 3와 numpy, scipy. 편당 약 1분이에요.

## 폴더 구성

- `engine/`: 재료 상자(블록 라이브러리, 장면 생성기, 렌더러, 음악 합성, 빌드 스크립트)
- `shorts/NNN-이름/episode.json`: 장면표(영상의 원본). `scene.html`과 `out/`은 여기서 만들어져요
- `shorts/NNN-이름/script.md`: 근거와 평가 질문
