#!/usr/bin/env python3
"""episode.json → scene.html. 사용: python3 make_scene.py <에피소드 폴더>
episode.json: {"id","tag","scenes":[{"type":"title","lines":[...],...}, ...]}  (블록 종류와 항목은 blocks.py와 README 참고)"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from blocks import BLOCKS, BG, mascot_html, Ctx, num

GAP = {'speech': 70, 'notes': 20, 'split': 20, 'check': 20, 'bigword': 20, 'title': 34, 'choices': 34, 'bars': 26, 'dice': 30, 'chain': 30, 'stack': 34, 'cards': 20, 'tip': 32, 'outro': 34, 'list': 30, 'vs': 30}

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
        if i == len(ep['scenes']) - 1 and not sc.get('nohold'): dur += 3   # 마지막 글자까지 다 읽고 처음으로 돌아가도록 끝에 여유
        foot = ''
        if sc.get('foot'):
            fcls = 'foot dk' if bg in ('blue', 'orange') else 'foot'
            foot = f'<div class="{fcls}" data-b="{num(a + sc.get("foot_at", 1.5))}" data-anim="pop">{__import__("blocks").esc(sc["foot"])}</div>'
        m = mascot_html(cx, sc.get('mascot'))
        gap = sc.get('gap', GAP.get(typ, 28))
        style = f'gap:{gap}px' + {'top': ';justify-content:flex-start', 'bottom': ';justify-content:flex-end'}.get(sc.get('vpos'), '') + {'left': ';align-items:flex-start', 'right': ';align-items:flex-end'}.get(sc.get('align'), '') + (';bottom:520px' if typ == 'outro' else '') + (';top:250px' if typ == 'cards' else '')
        lift = ' data-lift="1"' if sc.get('lift') else ''
        body = '\n  '.join(parts)
        hl = f' style="--hlc:{sc["hl"]}"' if sc.get('hl') else ''
        secs.append(f'<!-- {i + 1}. {typ} {num(a)}~{num(a + dur)}박 -->\n<section class="scene" data-a="{num(a)}" data-e="{num(a + dur)}" data-bg="{BG[bg]}"{lift}{hl}><div class="in" style="{style}">\n  {body}\n</div>{extra}{foot}{m}</section>\n')
        a += dur
    tpl = open(pathlib.Path(__file__).parent / 'template.html', encoding='utf-8').read()
    out = tpl.replace('{{SCENES}}', '\n'.join(secs)).replace('{{TOTAL}}', num(a)).replace('{{TAG}}', __import__('blocks').esc((ep.get('tag', '') + ' ' + ep.get('name', '')).strip()))
    import re
    out = re.sub(r' data-rot="[^"]*"', '', out)   # 정지 상태에서 기울어지는 요소는 쓰지 않는다(사용자 요청 2026-11-08)
    (ep_dir / 'scene.html').write_text(out, encoding='utf-8')
    print(f'scene.html 생성: 장면 {len(secs)}개, {num(a)}박 ({a * 60 / 128:.1f}초)')

if __name__ == '__main__': build(sys.argv[1])
