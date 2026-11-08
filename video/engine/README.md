# 재료 상자 (영상 엔진)

영상 한 편을 **장면 조각(블록)** 으로 조립하는 도구예요. 새 영상은 `episode.json`(장면표)만 쓰면 돼요. 화면 모양, 박자(128bpm), 효과음, 마스코트, 음악은 엔진이 맡아요.

```bash
bash video/engine/build.sh video/shorts/001-next-word        # 조용한 음악(기본)
MUSIC=loud bash video/engine/build.sh video/shorts/001-next-word   # 드럼 있는 신나는 음악
```

결과는 에피소드 폴더의 `out/<id>.mp4`와 `out/<id>-thumbnail.jpg`예요. 필요한 것: Node+Playwright, ffmpeg, Python 3+numpy+scipy. 편당 약 1분이에요.

## episode.json

```json
{"id": "002-tokens", "tag": "1.1.2",
 "scenes": [ {"type": "title", "lines": ["...", "..."], "sticker": "..."}, ... ]}
```

모든 장면에서 쓸 수 있는 공통 칸: `bg`(blue·yellow·white·orange), `beats`(장면 길이, 박), `at`(항목별 등장 시각 덮어쓰기), `mascot`(`{"face":"wide:o","side":"right|left|center","at":4.4}`), `gap`, `lift`(드럼 음악일 때 더 신나게).
마스코트 표정은 눈 `open|wide|happy` + 입 `smile|o|grin` 조합이에요(예: `happy:grin`).

## 블록

| type | 쓰임새 | 필수 칸 |
|---|---|---|
| `title` | 큰 글자가 쾅쾅 나오는 제목 장면 | `lines`, 선택 `sticker`(글 또는 `{t,c,anim,rot}`) |
| `choices` | 말풍선 + 후보 칩(하나는 줄 긋기) | `say`, `ask`, `chips`, 선택 `no` |
| `bars` | 후보별 점수 막대 | `title`, `rows`(`name`,`pct`,`bar`,`label`,`dim`), 선택 `note` |
| `dice` | 주사위 뽑기(영상에 한 번만) | `title`, `result`, 선택 `lines` |
| `chain` | 말이 뒤에 이어 붙는 사슬 | `head`, `start`, `words`, 선택 `tail` |
| `stack` | 점점 커지는 스티커 + 색종이(한 번만) | `title`, `items`(`t`,`c`,`size`) |
| `cards` | 답 카드 여러 장 비교(겹침 초록, 다름 빨강) | `lines`, `cards`(`label`,`red`), 선택 `stickers`,`note` |
| `tip` | 오늘의 써먹기 | `lines`, 선택 `label`,`badges`,`sticker` |
| `list` | 항목이 좌우로 번갈아 들어오는 목록 | `title`, `items`, 선택 `note` |
| `vs` | 왼쪽 VS 오른쪽 | `title`, `left`, `right`, 선택 `note` |
| `outro` | 마무리(채널 이름·약속·프로필 링크·마스코트) | 없음 |

색은 `red`, `yellow`, `green`, `blue`, `ink`예요. 글 안의 `\n`은 줄바꿈이에요.

## 형광펜과 아이콘

- 글 안의 `==핵심 말==`은 등장한 뒤 형광펜이 왼쪽에서 오른쪽으로 그어져요. 장면 바탕과 비슷한 색이면 장면에 `"hl": "#FF9EB1"`처럼 형광펜 색을 정해요. 한 장면에 두 군데 안팎으로만 써요.
- 말풍선·메모지·분할·체크리스트·큰 글자 장면에는 `"icon": "bulb"`처럼 아이콘을 넣을 수 있어요(`blocks.py`의 `ICONS`: person, pin, book, target, sliders, doc, bulb, question, thought, lock, search, warn, chat, clock, check, people).
- 모든 요소는 기울이지 않아요(`data-rot`은 자동으로 지워져요).

## 규칙

- 한 화면의 글은 약 35자 이하로, 글자가 흰·먹색 테두리 안에서 읽히게 써요.
- 다음 편 예고는 넣지 않아요(2026-11-07 결정). 끝은 `outro`로 마무리해요.
- 새 블록이 필요하면 `blocks.py`에 함수를 더하고 `BLOCKS`에 등록해요. 새 블록을 만든 뒤에는 기존 영상(001)을 다시 만들어 모양이 그대로인지 확인해요.
