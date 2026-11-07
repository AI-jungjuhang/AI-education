#!/usr/bin/env python3
"""episode.json → scene.html. 사용: python3 make_scene.py <에피소드 폴더>
episode.json: {"id","tag","scenes":[{"type":"title","lines":[...],...}, ...]}  (블록 종류와 항목은 blocks.py와 README 참고)"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from blocks import BLOCKS, BG, mascot_html, Ctx, num

GAP = {'title': 34, 'choices': 34, 'bars': 26, 'dice': 30, 'chain': 30, 'stack': 34, 'cards': 20, 'tip': 32, 'outro': 34, 'list': 30, 'vs': 30}

def build(ep_dir):
    ep_dir = pathlib.Path(ep_dir); ep = json.load(open(ep_dir / 'episode.json', encoding='utf-8'))
    secs, a = [], 0.0; seen = set()
    for i, sc in enumerate(ep['scenes']):
        typ = sc['type']
        if typ not in BLOCKS: raise SystemExit(f'알 수 없는 블록: {typ} (장면 {i + 1})')
        if typ in ('dice', 'stack') and typ in seen: raise SystemExit(f'{typ} 블록은 한 영상에 한 번만 쓸 수 있어요')
        seen.add(typ)
        fn, default_bg = BLOCKS[typ]; bg = sc.get('bg', default_bg)
        cx = Ctx(a, sc)
        parts, dur, extra = fn(cx, sc, bg)
        dur = sc.get('beats', dur)
        m = mascot_html(cx, sc.get('mascot'))
        gap = sc.get('gap', GAP.get(typ, 28))
        style = f'gap:{gap}px' + (';bottom:520px' if typ == 'outro' else '') + (';top:250px' if typ == 'cards' else '')
        lift = ' data-lift="1"' if sc.get('lift') else ''
        body = '\n  '.join(parts)
        secs.append(f'<!-- {i + 1}. {typ} {num(a)}~{num(a + dur)}박 -->\n<section class="scene" data-a="{num(a)}" data-e="{num(a + dur)}" data-bg="{BG[bg]}"{lift}><div class="in" style="{style}">\n  {body}\n</div>{extra}{m}</section>\n')
        a += dur
    tpl = open(pathlib.Path(__file__).parent / 'template.html', encoding='utf-8').read()
    out = tpl.replace('{{SCENES}}', '\n'.join(secs)).replace('{{TOTAL}}', num(a)).replace('{{TAG}}', ep.get('tag', ''))
    (ep_dir / 'scene.html').write_text(out, encoding='utf-8')
    print(f'scene.html 생성: 장면 {len(secs)}개, {num(a)}박 ({a * 60 / 128:.1f}초)')

if __name__ == '__main__': build(sys.argv[1])
