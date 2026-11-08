#!/usr/bin/env python3
"""episode.json에서 화면 글 표(script.md)를 만든다. 사용: python3 make_script.py <에피소드 폴더> "<제목>" "<원본 페이지 경로(docs 기준)>" "<한 가지 생각>" "<기준 페이지 이름>" """
import json, pathlib, sys, re
ep = pathlib.Path(sys.argv[1]); title, page, idea, pname = sys.argv[2:6]
d = json.load(open(ep / 'episode.json', encoding='utf-8')); BEAT = 60 / 128
sys.path.insert(0, str(pathlib.Path(__file__).parent)); from blocks import BLOCKS, Ctx
def texts(sc):
    out = []
    for k in ('title', 'head', 'start', 'say', 'ask', 'label', 'note', 'tail', 'no'):
        if sc.get(k): out.append(str(sc[k]))
    for k in ('lines',):
        out += sc.get(k, [])
    for k in ('sticker',):
        s = sc.get(k)
        if s: out.append(s if isinstance(s, str) else s['t'])
    for k in ('items', 'chips', 'words', 'badges'):
        for it in sc.get(k, []): out.append(it if isinstance(it, str) else it.get('t', it.get('name', '')))
    for k in ('left', 'right'):
        if sc.get(k): out.append(sc[k]['t'])
    return ' / '.join(x.replace('\n', ' ') for x in out if x)
t = 0; rows = []
for i, sc in enumerate(d['scenes'], 1):
    fn, bg = BLOCKS[sc['type']]; cx = Ctx(t, sc); _, dur, _ = fn(cx, sc, sc.get('bg', bg)); dur = sc.get('beats', dur)
    rows.append(f'| {i} | {t:g}–{t + dur:g} | {texts(sc)} |'); t += dur
sec = t * BEAT
md = f'''# 쇼츠 {d['id'].split('-')[0]} · {title}

- **원본 페이지:** {pname} [{title}](../../../docs/{page})
- **형식:** 세로 9:16, 30fps, **{sec:.1f}초**, 음성 없음. 마무리 장면 없음. `episode.json`을 재료 상자로 조립해요.
- **한 가지 생각:** {idea}
- **상태:** 초안(평가 대기)

| # | 박 | 화면 글 |
|---|---|---|
''' + '\n'.join(rows) + '''

## 확인할 점
- 화면 글은 모두 원본 페이지의 내용을 짧게 줄인 거예요. 페이지에 없는 주장은 넣지 않았어요.
- 지어낸 예시는 화면에도 "예시"라고 밝히고, 단정할 수 없는 말은 "~할 수 있어요"로 썼어요.
'''
(ep / 'script.md').write_text(md, encoding='utf-8'); print(ep / 'script.md', f'{sec:.1f}초')
