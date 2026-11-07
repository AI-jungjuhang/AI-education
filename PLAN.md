# 이어 쓰기 지침서 (자동 이어쓰기용)

사용자 지시(2026-11-07): 사용자가 "그만"이라고 할 때까지, 책 전체를 처음부터 끝까지 만든다. 모르는 것은 질문하지 말고 알아서 판단한다. 시간이 남으면 인터뷰 장(19장)과 부록도 채운다. 사용량 한도가 풀리면 바로 이어서 쓴다.

## 지금 상태 확인
```bash
cd /home/user/ai-education && git checkout claude/korean-ai-textbook-site-kbmkii && git pull -q origin claude/korean-ai-textbook-site-kbmkii
python3 tools/build_book.py --status      # 진행 수와 다음에 쓸 페이지
```
저장소가 없으면: `git clone https://github.com/sehoon3554-ctrl/ai-education /home/user/ai-education` 후 위 브랜치로 이동. `pip install -r requirements.txt pyyaml`도 필요할 수 있다.

## 한 페이지를 쓰는 순서
1. `book.yml`에서 다음 `done: false` 페이지를 고른다. 순서대로 쓴다.
2. `.claude/skills/topic-page/SKILL.md`를 읽고 틀을 따른다. 기준 페이지는 `docs/part1/ch01/hallucination.md`.
3. 원전을 **실제로 열어 확인**한다(`curl -sSL`, 영상은 YouTube oembed, 논문은 export.arxiv.org). 확인 못 한 링크는 "확인 필요"로 적는다. 지어내지 않는다.
4. `docs/partN/chMM/<slug>.md`를 쓴다. 제목 아래에 `<p class="ep-meta">` 정보 줄을 넣는다(기준 페이지 참고).
5. `book.yml`에서 해당 페이지를 `done: true`로 바꾸고 `python3 tools/build_book.py`를 실행한다(메뉴·안내 페이지·홈이 자동 갱신).
6. `NO_MKDOCS_2_WARNING=1 mkdocs build -q`가 경고 없이 끝나는지 확인한다.
7. 가끔(5페이지마다 또는 CSS를 건드렸을 때) `.claude/skills/design-check`를 돌린다.
8. 커밋하고 푸시한다. 푸시 대상은 `claude/korean-ai-textbook-site-kbmkii` 브랜치뿐이다.

## 품질 규칙 (요약)
- 내용 수준은 높게, 설명은 10살 눈높이로. 영어 원전은 문장을 옮기지 않고 소화해서 다시 쓴다.
- 지어낸 숫자나 예시는 "예시"라고 밝힌다. 시간이 지나면 낡는 내용(모델 이름, 가격, 기능)은 기준 날짜와 함께 조심스럽게 쓴다.
- 모든 페이지에 "오늘 바로 써먹기"(원리에서 나온 요령)와 "출처와 기준"을 넣는다. 읽고 나서 실제로 도움이 되어야 한다.
- 인터뷰·대담은 사실이 아니라 견해다. 누가 언제 어디서 한 말인지 밝히고, 인용은 최소로, 입장이 갈리면 함께 보여 준다. 말하지 않은 것을 말한 것처럼 쓰지 않는다.
- 사용자 평가가 들어와 있으면(대화에 나오면) 이어 쓰기 전에 먼저 반영한다.

## 마무리
- `python3 tools/build_book.py --status`가 `진행: 70/70`이면 끝이다. 그때 이 예약 실행을 끈다.
- 끝낼 때: 전체 `design-check`, 모든 링크 점검(깨진 링크가 없는지), 사용자에게 요약 보고.
