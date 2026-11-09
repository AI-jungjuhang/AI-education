# AI 정주행 (부제: 열 살도 이해하는 AI 교과서)

이름 규칙(2026-11-07 결정): 채널·시리즈 이름은 **AI 정주행**, 책 부제와 영상의 약속은 **열 살도 이해하는 AI 교과서**다. (2026-11-07 변경) 사이트 주소는 GitHub Pages(계정 아이디가 주소에 들어가는 것을 사용자가 허용했다). 영상에는 주소를 쓰지 않고 "프로필 링크의 책 사이트"라고만 말한다.

AI를 기초부터 심화까지 다루는 한국어 웹 교과서(MkDocs Material, GitHub Pages)이고, 각 주제 페이지는 짧은 유튜브 영상 한 편으로도 만든다.

- 구조: 부 > 장 > 절 > 주제 페이지. 부는 I 처음 쓰는 AI / II 일에 붙이기 / III 원리 한 스푼 / IV 도구와 에이전트 / V Claude Code 실전 / VI 원리로 쓰기★ / 부록. ★는 심화.
- 독자: AI를 써 보고 싶은 일반인. 읽고 나면 실제로 써먹을 수 있어야 하고, 다음 페이지가 궁금해야 한다.
- 문체: 내용 수준은 높게, 설명은 10살 눈높이로. 영어 원전은 문장을 옮기지 않고 소화해서 다시 쓴다. 페이지마다 출처와 기준 날짜.
- 진행: 사용자가 "그만"이라고 할 때까지 페이지를 계속 쓴다(사용자 승인, 2026-11-07). 매 페이지: 원전 링크 확인 → 작성 → mkdocs build → design-check → 커밋·푸시 → 미리보기 갱신. 영상화는 v0.2부터.
- 페이지 작성은 `.claude/skills/topic-page`, 디자인은 `.claude/skills/frontend-design`을 따른다.
- 개발 브랜치: `claude/korean-ai-textbook-site-kbmkii`. 빌드: `mkdocs build`.

## V부 Claude Code 실전 (2026-11-07 추가, 기준 Claude Code 2.1.319)
- 구조: V부 = 16장 5A 첫걸음(5.1~5.4) / 17장 5B 자동화와 연결(5.5~5.8) / 18장 5C 고급★(5.9~5.10). 기존 V부는 VI부(19~22장)로 옮겼다. 폴더는 part5(새), part6(기존).
- 원전: luongnv89/claude-howto(MIT). 사실 기준은 https://code.claude.com/docs. 페이지마다 기준 버전과 날짜를 적고, 원전 문장은 옮기지 않는다.
- 검증용 예시: `studio` 플러그인(`claude plugin validate`로 통과 확인), 형식 검사 훅 스크립트, 반복문 스크립트(가짜 claude로 구조만 확인). 모델을 호출한 실제 결과는 확인하지 못했다.
- 레벨 6(2026-11-07 추가): VI부 23장 "원리로 쓰기" 4절 8페이지(컨텍스트 관리, 프롬프트를 원리로, 모델 고르기, 검증 루프). 모델 별명·노력 단계·기본값은 빨리 낡으니 갱신 때 model-config 문서로 다시 확인한다.
- **빌드 확인은 `mkdocs build --strict`를 `-q` 없이, 종료 코드로 확인한다.** `-q`를 붙이면 경고가 있어도 종료 코드가 0이 되어 깨진 링크를 놓친다(2026-11-07에 겪음).

## 한국어 다듬기와 AI 티 줄이기 (2026-11-08)
- `.claude/skills/natural-writing-kr`(slobbie/natural-writing-kr, MIT, 변경 없이 복사)로 한국어 문장을 다듬는다. 영상은 `video-script` 스킬의 "AI 티 점검표"를 따른다.

## 나중에 할 일: 인터뷰·대담을 참고 자료에 포함
- 대상 예: Karpathy, Sam Altman, Geoffrey Hinton 등 AI를 만든 사람들의 인터뷰와 강연. 목적은 AI 발전 방향과 그들의 통찰을 담는 것.
- 인터뷰는 사실이 아니라 **발언과 견해**다. 본문에서 "누가, 언제, 어디서 한 말"인지 밝히고 사실 설명과 구분한다. 예측은 예측이라고 쓴다.
- 인용은 최소로 하고 다시 써서 설명한다. 말하지 않은 것을 말한 것처럼 쓰지 않는다. 링크와 날짜를 확인한 것만 적는다.
- 견해는 시간이 지나면 바뀌므로 기준 날짜를 꼭 적는다. 서로 다른 입장은 한쪽만 싣지 않고 함께 보여 준다.
- 이 규칙은 `.claude/skills/topic-page`에도 반영한다.

## 영상 내용을 확인하는 방법 (2026-11-07 기준)
- 작업 환경(클라우드)의 IP를 YouTube가 막아서 `yt-dlp`와 `youtube-transcript-api`가 실패한다("봇이 아닌지 확인" 요구, IpBlocked).
- 우회로 1(쓰는 중): 제3자 사이트 Rosetta(`rosetta.to/u/<채널>/<영상-슬러그>`)가 자막 전문과 YouTube 챕터를 제공한다. 자동 생성이라 오류가 있을 수 있으므로 **비공식 자막이라고 밝히고**, 인용은 최소로 하며, 챕터 시각은 YouTube 챕터 기준으로만 적는다.
- 우회로 2(미사용): GitHub의 `artemchuikin/youtube-skills`(TranscriptOut API), `supadata-ai/mcp`는 계정과 API 키가 필요한 상용 서비스다. 사용자의 이메일을 외부에 보내므로 사용자가 직접 요청하기 전에는 쓰지 않는다.
- 우회로 3: 사용자가 자기 컴퓨터에서 `yt-dlp --write-auto-subs --skip-download`로 자막을 받아 저장소에 올리면 가장 정확하다.

## 사이트 디자인 (2026-11-09, unslop 점검)
- `.claude/skills/unslop`(heydamir/unslop, CC BY 4.0, 출처는 SOURCE.md)으로 점검했다. 방향: 다정하고 또박또박하고 조금 장난스러운, 공책과 형광펜. 바탕은 따뜻한 종이색 단계, 포인트는 쇼츠 파랑 하나, 서명 디테일은 형광펜 밑줄.
- 굵기는 400~600, 상자 아이콘은 글자 색 하나, 로고는 감자(`docs/assets/potato-logo.svg`). 홈 첫 화면은 글 왼쪽, 감자와 페이지 미리보기 오른쪽.
- 사이트 주소는 `https://ai-jungjuhang.github.io/AI-education/`(GitHub 조직 AI-jungjuhang). 머리 부분 GitHub 표시는 뺐다(repo_url 없음).

## 영어판 (2026-11-09 시작)
- 이름(사용자 결정): 채널·시리즈 **AI, Start to Finish**, 책 부제 **The AI textbook a 10-year-old can follow**.
- 한국어판을 번역하지 않고 영어 원전에서 새로 쓴다. 사용자와는 한국어로 소통한다.
- 폴더: `docs-en/`(assets·stylesheets·javascripts는 `docs/`를 가리키는 심볼릭 링크), `book-en.yml`(목차, slug와 장·절 번호는 한국어판과 같음), `mkdocs-en.yml`, `video/shorts-en/`.
- 목차 반영: `python3 tools/build_book.py --book book-en.yml --config mkdocs-en.yml --docs docs-en`. 옵션 없이 돌리면 한국어판 그대로다.
- 빌드 확인: `mkdocs build --strict -f mkdocs-en.yml`(종료 코드 확인).
- 작업 브랜치: `claude/keen-planck-pyt819`(사용자 결정 A: 여기서 쓰고, 다 되면 한국어 브랜치에 합친다). 이 브랜치는 배포되지 않는다.
- 배포(2026-11-09 사용자 승인): `deploy.yml`을 한국어 빌드 → 영어를 `site/en/`에 빌드 → `ghp-import`로 함께 올리기로 바꿨다. 이 브랜치는 배포되지 않으므로 한국어 브랜치에 합칠 때 적용된다.
- 영어 문장 기준(2026-11-09 사용자 승인): AI 티는 `.claude/skills/humanizer`(blader/humanizer, MIT), 쉬운 글은 Federal Plain Language Guidelines 점검표, 학년 점수는 `tools/readability.py`(Flesch-Kincaid 6.0 이하, `pip install textstat==0.7.8`). 자세한 규칙은 `topic-page` 스킬의 "영어판 페이지" 절.
- 영어 홈의 첫 화면 오른쪽(페이지 미리보기 카드 + 감자)은 첫 페이지를 쓴 뒤 넣는다. 감자 위치가 카드를 기준으로 잡혀 있어 카드 없이 넣으면 모바일에서 글을 덮는다.
