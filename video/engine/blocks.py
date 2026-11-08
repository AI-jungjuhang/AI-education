"""재료 상자: 장면 조각(블록) 모음. 각 블록은 (html, 기본 길이)를 돌려준다. 시각은 모두 '박' 단위(128bpm).
장면 JSON에서 "at": {"이름": 박}으로 개별 시각을, "beats": 숫자로 장면 길이를 바꿀 수 있다."""
import html as H

BG = {'blue': '#2F7FD8', 'yellow': '#FFD93D', 'white': '#FCFCFC', 'orange': '#FC5424'}
DARK_BG = ('yellow', 'white')          # 밝은 바탕에서는 글자를 먹색으로
COLORS = ('red', 'yellow', 'green', 'blue', 'ink')

import re as _re
def esc(t):
    x = H.escape(str(t), quote=False).replace('\n', '<br>')
    return _re.sub(r'==(.+?)==', r'<mark class="hl">\1</mark>', x)   # ==핵심== 은 형광펜이 그어진다
def num(x): return f'{x:g}'
def cc(c): return f' c-{c}' if c else ''

class Ctx:
    """장면 하나를 만드는 동안 시각을 모아 주는 도우미."""
    def __init__(self, a, sc):
        self.a, self.sc, self.at = a, sc, sc.get('at', {})
        self.last = 0.0
    def t(self, name, default):
        v = self.at.get(name, default)
        self.last = max(self.last, v)
        return v
    def b(self, name, default): return num(self.a + self.t(name, default))

def lines_html(cx, lines, bg, size='huge', key='line', start=0.0, step=1.0, last_yel=False, fs=None):
    dark = ' dark' if bg in DARK_BG else ''
    out = []
    for i, ln in enumerate(lines):
        yel = ' yel' if last_yel and i == len(lines) - 1 else ''
        st = f' style="font-size:{fs}px"' if fs else ''
        out.append(f'<div class="st{dark}{yel} {size}" data-b="{cx.b(f"{key}{i}", start + i * step)}" data-anim="slam" data-sfx="slam"{st}>{esc(ln)}</div>')
    return '\n  '.join(out)

def sticker(cx, name, default_t, text, c=None, anim='pop', rot=0, sfx=None, size=None):
    sfx = sfx or ('whoosh' if anim.startswith('slide') else 'pop')
    st = f' style="font-size:{size}px"' if size else ''
    r = f' data-rot="{rot}"' if rot else ''
    return f'<div class="sticker{cc(c)}" data-b="{cx.b(name, default_t)}" data-anim="{anim}"{r} data-sfx="{sfx}"{st}>{esc(text)}</div>'

def mascot_html(cx, m):
    if not m: return ''
    if isinstance(m, str): m = {'face': m}
    face = m.get('face', 'happy:grin'); side = m.get('side', 'right')
    pos = {'right': 'right:50px;top:1250px', 'left': 'left:40px;top:1140px', 'center': 'left:395px;top:1330px;width:290px;height:325px'}[side]
    if m.get('y'): pos = pos.replace('top:' + pos.split('top:')[1].split('px')[0] + 'px', 'top:%dpx' % m['y'])
    return f'<div class="mas" data-face="{face}" data-b="{cx.b("mascot", m.get("at", 4.4))}" data-anim="pop" data-sfx="pop" style="{pos}"></div>'


# ---------------- 아이콘 (의미를 돕는 그림, 24x24 선 그림) ----------------
_P = 'fill="none" stroke="#242424" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    'person': f'<circle cx="12" cy="8" r="3.6" {_P}/><path d="M4.5 20c.8-4 3.6-6 7.5-6s6.7 2 7.5 6" {_P}/>',
    'pin': f'<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z" {_P}/><circle cx="12" cy="10" r="2.4" {_P}/>',
    'book': f'<path d="M12 6c-2-1.6-5-2-8-1.5v13c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5v-13c-3-.5-6-.1-8 1.5z" {_P}/><path d="M12 6v13" {_P}/>',
    'target': f'<circle cx="12" cy="12" r="8.5" {_P}/><circle cx="12" cy="12" r="4.6" {_P}/><circle cx="12" cy="12" r="1.2" fill="#242424"/>',
    'sliders': f'<path d="M4 7h16M4 12h16M4 17h16" {_P}/><circle cx="9" cy="7" r="2.2" fill="#fff" stroke="#242424" stroke-width="2"/><circle cx="15" cy="12" r="2.2" fill="#fff" stroke="#242424" stroke-width="2"/><circle cx="8" cy="17" r="2.2" fill="#fff" stroke="#242424" stroke-width="2"/>',
    'doc': f'<path d="M6 3h8l4 4v14H6z" {_P}/><path d="M14 3v4h4M9 12h6M9 16h6" {_P}/>',
    'bulb': f'<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z" {_P}/>',
    'question': f'<circle cx="12" cy="12" r="9" {_P}/><path d="M9.2 9.4a2.9 2.9 0 1 1 4.4 2.5c-1 .6-1.6 1.2-1.6 2.4" {_P}/><circle cx="12" cy="17" r="1.1" fill="#242424"/>',
    'thought': f'<path d="M7 17a4 4 0 0 1-.5-7.9 5 5 0 0 1 9.6-1A4.2 4.2 0 0 1 17 17z" {_P}/><circle cx="7" cy="20" r="1.2" fill="#242424"/><circle cx="4.5" cy="22" r=".8" fill="#242424"/>',
    'lock': f'<rect x="5" y="11" width="14" height="10" rx="2" {_P}/><path d="M8 11V8a4 4 0 0 1 8 0v3" {_P}/>',
    'search': f'<circle cx="10.5" cy="10.5" r="6" {_P}/><path d="M15 15l5.5 5.5" {_P}/>',
    'warn': f'<g transform="translate(0,-1.8)"><path d="M12 3.5l9.5 16.5H2.5z" {_P}/><path d="M12 10v4.5" {_P}/><circle cx="12" cy="17.2" r="1" fill="#242424"/></g>',
    'chat': f'<path d="M4 5h16v11H11l-5 4v-4H4z" {_P}/><path d="M8 9.5h8M8 12.5h5" {_P}/>',
    'clock': f'<circle cx="12" cy="12" r="9" {_P}/><path d="M12 7v5l3 2" {_P}/>',
    'check': f'<path d="M5 12.5l4.5 4.5L19 7" {_P}/>',
    'no': '<path d="M5.5 5.5l13 13M18.5 5.5l-13 13" fill="none" stroke="#E02424" stroke-width="3.6" stroke-linecap="round"/>',
    'yes': '<circle cx="12" cy="12" r="7.5" fill="none" stroke="#14A36B" stroke-width="3.6"/>',
    'people': f'<circle cx="8.5" cy="8.5" r="3" {_P}/><circle cx="16.5" cy="9.5" r="2.5" {_P}/><path d="M2.5 19c.6-3.3 2.8-5 6-5s5.4 1.7 6 5M15 14.5c2.7-.2 4.7 1.2 5.5 4" {_P}/>',
}
import os as _os
ICON_LAV = _os.environ.get('ICON_COLOR', '#C9B8FF')   # 모든 아이콘 배지의 기본색: 상자 색(노랑·초록·분홍·하늘)과 다른 하나의 색으로 통일
ICON_BG = {'no': '#fff', 'yes': '#fff', 'warn': '#FC5424'}
def _lum(c):
    c = c.lstrip('#'); c = ''.join(x*2 for x in c) if len(c) == 3 else c; r, g, b = (int(c[i:i + 2], 16) / 255 for i in (0, 2, 4)); return 0.2126 * r + 0.7152 * g + 0.0722 * b

def icon(name, size=84, pos='', bg=None, t=None):
    if not name: return ''
    bg = bg or ICON_BG.get(name, ICON_LAV)
    anim = f' data-b="{t}" data-anim="pop" data-sfx="pop"' if t is not None else ''
    svg_body = ICONS[name]
    if _lum(bg) < 0.45: svg_body = svg_body.replace('#242424', '#ffffff')   # 어두운 배지에는 흰 선
    return (f'<span class="ico"{anim} style="width:{size}px;height:{size}px;background:{bg};{pos}">'
            f'<svg viewBox="0 0 24 24" width="{int(size*0.7)}" height="{int(size*0.7)}">{svg_body}</svg></span>')

# ---------------- 블록 ----------------
def b_title(cx, sc, bg):
    L = sc['lines']; n = len(L)
    parts = [lines_html(cx, L, bg, sc.get('size', 'huge'))]
    if sc.get('sticker'):
        s = sc['sticker']; s = {'t': s} if isinstance(s, str) else s
        parts.append(sticker(cx, 'sticker', n + 0.4, s['t'], s.get('c', 'yellow'), s.get('anim', 'pop'), s.get('rot', -3), size=s.get('size')))
    dur = max(4, cx.last + 2.6)
    return parts, dur, ''

def b_choices(cx, sc, bg):
    p = [sticker(cx, 'say', 0, sc['say'], None, 'slideL', 0, 'pop', 78),
         sticker(cx, 'ask', 2, sc['ask'], 'yellow', 'pop', -2)]
    chips = []
    for i, ch in enumerate(sc['chips']):
        ch = {'t': ch} if isinstance(ch, str) else ch
        chips.append(f'<div class="chip c-{ch.get("c", COLORS[i % 3])}" data-b="{cx.b(f"chip{i}", 3 + i)}" data-anim="pop" data-sfx="pop">{esc(ch["t"])}</div>')
    p.append('<div class="chips">' + '\n    '.join(chips) + '</div>')
    if sc.get('no'):
        p.append(f'<div class="chip no" data-b="{cx.b("no", 3 + len(chips) + 0.2)}" data-anim="shake" data-sfx="buzz">{esc(sc["no"])}</div>')
    return p, max(4, cx.last + 2.8), ''

def b_bars(cx, sc, bg):
    p = [lines_html(cx, [sc['title']], bg, 'big')]
    for i, r in enumerate(sc['rows']):
        t = cx.b(f'row{i}', 1.5 + i); dim = ' dim' if r.get('dim') else ''
        val = (f'<div class="v" style="font-size:50px">{esc(r["label"])}</div>' if r.get('label')
               else f'<div class="v" data-b="{t}" data-anim="count" data-v="{r["pct"]}" data-fmt="%">0%</div>')
        p.append(f'<div class="sticker row{dim}" data-b="{t}" data-anim="slideL" data-sfx="pop"><div class="l">{esc(r["name"])}</div>'
                 f'<div class="track"><div class="bar" data-b="{t}" data-anim="grow" data-v="{r["bar"]}"></div></div>{val}</div>')
    if sc.get('note'): p.append(sticker(cx, 'note', 1.5 + len(sc['rows']) + 0.5, sc['note'], 'yellow', 'pop', -5, 'ding', 64))
    return p, max(4, cx.last + 2.0), ''

def b_dice(cx, sc, bg):
    cx.t('die', 1)
    p = [lines_html(cx, [sc['title']], bg, 'big'),
         f'<div class="dieW" id="dieW" data-b="{cx.b("die", 1)}" data-anim="dice" data-sfx="rattle" data-dur="2.5"><div class="die" id="die">' + '<i></i>' * 7 + '</div></div>',
         f'<div class="sticker c-yellow" data-b="{cx.b("result", 4)}" data-anim="slam" data-sfx="ding" style="font-size:120px">{esc(sc["result"])}</div>']
    for i, ln in enumerate(sc.get('lines', [])):
        p.append(f'<div class="st sm" data-b="{cx.b(f"dl{i}", 5.4 + i * 1.2)}" data-anim="{"slideL" if i % 2 == 0 else "slideR"}" data-sfx="pop">{esc(ln)}</div>')
    return p, max(8, cx.last + 1.6), ''

def b_chain(cx, sc, bg):
    W = sc['words']; n = len(W)
    p = [sticker(cx, 'head', 0, sc['head'], 'blue', 'slideL', 0, 'whoosh', 78),
         f'<div class="wd" data-b="{cx.b("start", 1.2)}" data-anim="pop" data-sfx="pop">{esc(sc["start"])}</div>']
    items = []
    for i, w in enumerate(W):
        t = cx.b(f'w{i}', 3 + 2 * i); y = ' c-yellow' if i < n - 1 or w != '…' else ''
        items.append(f'<span class="arrow" data-b="{t}" data-anim="pop">→</span><span class="wd{y}" data-b="{t}" data-anim="slam" data-sfx="tick">{esc(w)}</span>')
    p.append('<div style="display:flex;gap:18px;align-items:center;flex-wrap:wrap;justify-content:center;width:940px">' + ''.join(items) + '</div>')
    if sc.get('tail'): p.append(sticker(cx, 'tail', 2 * n + 2, sc['tail'], 'red', 'pop', 3, 'ding', 78))
    return p, max(6, cx.last + 2.0), ''

def b_stack(cx, sc, bg):
    p = [lines_html(cx, [sc['title']], bg, 'big')]
    for i, it in enumerate(sc['items']):
        it = {'t': it} if isinstance(it, str) else it
        last = i == len(sc['items']) - 1
        anim = 'slam' if last else ('slideL' if i % 2 == 0 else 'slideR')
        p.append(sticker(cx, f'item{i}', 1.8 + 1.4 * i, it['t'], it.get('c'), anim, 0, 'ding' if last else 'pop', it.get('size', 90 + 22 * i)))
    extra = ''
    if sc.get('confetti', True):
        extra = f'<div id="conf" data-b="{cx.b("confetti", 1.8 + 1.4 * (len(sc["items"]) - 1))}" data-anim="confetti"></div>'
    return p, max(6, cx.last + 3.4), extra

def b_cards(cx, sc, bg):
    p = [lines_html(cx, sc['lines'], bg, 'big', start=0, step=1.6, last_yel=True, fs=120)]
    for i, c in enumerate(sc['cards']):
        t = cx.b(f'card{i}', 4 + 1.2 * i)
        p.append(f'<div class="card" data-b="{t}" data-anim="slideR" data-sfx="pop"><div class="n">{esc(c["label"])}</div><div class="ln">'
                 f'<b style="width:100%;background:var(--green)"></b><b style="width:{c["red"]}%;background:var(--red)"></b></div></div>')
    st = []
    for i, s in enumerate(sc.get('stickers', [])):
        st.append(f'<div class="sticker c-{s.get("c", "green")}" data-b="{cx.b(f"st{i}", 4 + 1.2 * len(sc["cards"]) + 0.8 + 1.6 * i)}" data-anim="pop" data-sfx="ding" style="font-size:62px">{esc(s["t"])}</div>')
    if st: p.append('<div style="display:flex;gap:22px;flex-wrap:wrap;justify-content:center">' + ''.join(st) + '</div>')
    if sc.get('note'): p.append(f'<div class="small" data-b="{cx.b("note", 4)}" data-anim="pop">{esc(sc["note"])}</div>')
    return p, max(8, cx.last + 2.2), ''

def b_tip(cx, sc, bg):
    p = [sticker(cx, 'label', 0, sc.get('label', '오늘의 써먹기'), 'red', 'slam', 0, 'slam', 78)]
    dark = 'st dark big'
    for i, ln in enumerate(sc['lines']):
        color = ';color:var(--red)' if i == len(sc['lines']) - 1 else ''
        p.append(f'<div class="{dark}" data-b="{cx.b(f"line{i}", 1.6 + 1.4 * i)}" data-anim="slam" data-sfx="slam" style="-webkit-text-stroke:0{color}">{esc(ln)}</div>')
    if sc.get('badges'):
        bd = ''.join(f'<div class="sticker c-blue" data-b="{cx.b(f"badge{i}", 4.8 + 0.8 * i)}" data-anim="pop" data-sfx="tick" style="font-size:96px;padding:10px 46px">{esc(x)}</div>' for i, x in enumerate(sc['badges']))
        p.append(f'<div style="display:flex;gap:28px">{bd}</div>')
    if sc.get('sticker'): p.append(sticker(cx, 'sticker', 8.4, sc['sticker'], 'yellow', 'pop', -2, 'ding', 66))
    return p, max(8, cx.last + 3.6), ''

def b_list(cx, sc, bg):
    p = [lines_html(cx, [sc['title']], bg, 'big')]
    for i, it in enumerate(sc['items']):
        it = {'t': it} if isinstance(it, str) else it
        p.append(sticker(cx, f'item{i}', 1.8 + 1.4 * i, it['t'], it.get('c', COLORS[i % 3]), 'slideL' if i % 2 == 0 else 'slideR', 0, 'pop', it.get('size', 80)))
    if sc.get('note'): p.append(sticker(cx, 'note', 1.8 + 1.4 * len(sc['items']) + 0.4, sc['note'], 'yellow', 'pop', -2, 'ding', 62))
    return p, max(6, cx.last + 2.8), ''

def b_vs(cx, sc, bg):
    L, R = sc['left'], sc['right']
    p = [lines_html(cx, [sc['title']], bg, 'big'),
         sticker(cx, 'left', 1.8, L['t'], L.get('c', 'red'), 'slideL', 0, 'whoosh', L.get('size', 96)),
         f'<div class="st big" data-b="{cx.b("vs", 3.4)}" data-anim="slam" data-sfx="slam">VS</div>',
         sticker(cx, 'right', 4.6, R['t'], R.get('c', 'green'), 'slideR', 0, 'whoosh', R.get('size', 96))]
    if sc.get('note'): p.append(sticker(cx, 'note', 6.6, sc['note'], 'yellow', 'pop', -2, 'ding', 62))
    return p, max(8, cx.last + 2.8), ''

def b_outro(cx, sc, bg):
    cx.t('mascot', 1)
    p = [f'<div class="sticker" data-b="{cx.b("brand", 0)}" data-anim="slam" data-sfx="slam" style="font-size:120px">{esc(sc.get("brand", "AI 정주행"))}</div>',
         f'<div class="st sm" data-b="{cx.b("sub", 1.2)}" data-anim="pop" data-sfx="pop" style="font-size:62px;-webkit-text-stroke:12px var(--ink)">{esc(sc.get("sub", "열 살도 이해하는 AI 교과서"))}</div>',
         f'<div class="sticker c-red beat" data-b="{cx.b("link", 3)}" data-anim="pop" data-sfx="ding" style="font-size:68px">{esc(sc.get("link", "프로필 링크에서 보기"))}</div>']
    sc.setdefault('mascot', {'face': 'happy:grin', 'side': 'center', 'at': 1})
    return p, 8, ''


# ---------------- v3 블록: 흩어 놓는 배치와 다른 모양 ----------------
def b_speech(cx, sc, bg):
    """말풍선 대화. items: [{"who":"me|other","t":"글","name":"이름(선택)"}], 선택 mascot(표정 목록은 faces)."""
    p = []
    for i, it in enumerate(sc['items']):
        who = it.get('who', 'other'); nm = f'<small>{esc(it["name"])}</small>' if it.get('name') else ''
        av = icon(it.get('icon'), 124, 'position:absolute;top:-56px;right:-30px;') if it.get('icon') else ''
        p.append(f'<div class="bubble {who}" data-b="{cx.b(f"b{i}", sc.get('delay', 0) + 0.4 + 2.4 * i)}" data-anim="pop" data-sfx="pop" style="font-size:{it.get("size", 64)}px{';padding-right:100px' if av else ''}">{av}{nm}{esc(it["t"])}</div>')
    return p, max(5, cx.last + 3.0), ''

def b_notes(cx, sc, bg):
    """메모지 흩어 붙이기(최대 4장). 제목은 왼쪽 위."""
    slots = [(40, 580, -4), (560, 660, 3), (60, 1110, 2.5), (550, 1190, -3)]
    cols = ['#FFE680', '#9BE7C4', '#FFB3C1', '#A9D2FF']; HLC = ['#FF9EB1', '#FFD93D', '#FFE680', '#FFE680']
    ex = [f'<div class="tapeTitle st dark big" data-b="{cx.b("title", 0)}" data-anim="slam" data-sfx="slam" style="top:270px;font-size:112px">{esc(sc["title"])}</div>']
    if len(sc['items']) == 3: slots[2] = (275, 1090, 0)
    for i, it in enumerate(sc['items']):
        x, y, r = slots[i]
        ex.append(f'<div class="note" data-b="{cx.b(f"n{i}", 1.4 + 1.6 * i)}" data-anim="pop" data-rot="{r}" data-sfx="pop" style="left:{x}px;top:{y}px;background:{cols[i]};--hlc:{HLC[i]}">{icon(it.get("icon"), 124, "position:absolute;top:-52px;right:-30px;", it.get("icon_bg") or ICON_LAV)}<b>{esc(it["head"])}</b><span class="nbody">{esc(it["body"])}</span></div>')
    return [], max(6, cx.last + 3.0), '\n'.join(ex)

def b_split(cx, sc, bg):
    """위아래 두 판. top/bottom: {"label","t","c"(색),"small"(선택)}."""
    T, B = sc['top'], sc['bottom']
    if sc.get('marks', True): T.setdefault('icon', 'no'); B.setdefault('icon', 'yes')
    def panel(it, y, h, key, t0, anim):
        col = {'red': 'var(--red);color:#fff', 'green': 'var(--green);color:var(--ink)', 'yellow': 'var(--yellow);color:var(--ink)', 'blue': 'var(--blue);color:#fff', 'white': '#fff;color:var(--ink)'}[it.get('c', 'red')]
        sm = f'<div style="font-size:42px;margin-top:22px;opacity:.9">{esc(it["small"])}</div>' if it.get('small') else ''
        pr = 'padding-right:330px;' if it.get('icon') else ''
        return (f'<div class="panel" data-b="{cx.b(key, t0)}" data-anim="{anim}" data-sfx="whoosh" style="top:{y}px;height:{h}px;background:{col};{pr}">'
                f'{icon(it.get("icon"), 190, "position:absolute;top:%dpx;right:70px;" % (it.get("icon_y", 545 if key == "top" else 205)))}<small>{esc(it["label"])}</small><div class="big2" style="font-size:{it.get("size", 84)}px">{esc(it["t"])}</div>{sm}</div>')
    ex = [panel(T, 0, 940, 'top', 0.2, 'slideL').replace('class="panel"', 'class="panel topp"'), panel(B, 940, 980, 'bottom', 3.6, 'slideR')]
    if sc.get('vs', False):
        ex.append(f'<div class="sticker c-yellow" data-b="{cx.b("vs", 3.4)}" data-anim="slam" data-sfx="slam" style="position:absolute;left:440px;top:880px;font-size:76px;padding:6px 30px;z-index:5">VS</div>')
    return [], max(8, cx.last + 4.0), '\n'.join(ex)

def b_check(cx, sc, bg):
    """체크리스트 종이. 항목 뒤에 "||보조 설명"을 달면 작은 회색 글씨로 아래에 나온다. 줄 높이는 글자 수로 어림해서 체크 표시 위치를 맞춘다."""
    items = sc['items']; top = sc.get('top', 400); fs = int(sc.get('fs', 72)); d = sc.get('delay', 0)
    SUBFS = 40
    parsed = []
    for t in items:
        main, _, sub = t.partition('||'); parsed.append((main, sub))
    rh = []
    for main, sub in parsed:
        h = len(main.split('\n')) * fs * 1.2 + 34 * 2 + 5
        if sub: h += len(sub.split('\n')) * SUBFS * 1.25 + 8
        rh.append(int(h))
    ex = [f'<div class="sticker c-red" data-b="{cx.b("label", d)}" data-anim="slam" data-sfx="slam" style="position:absolute;left:90px;top:{top - 150}px;font-size:68px;z-index:6">{esc(sc.get("label", "오늘의 써먹기"))}</div>'] + ([icon(sc['icon'], 132, f'position:absolute;right:100px;top:{top - 215}px;z-index:6', None, cx.b('icon', d + 0.6))] if sc.get('icon') else [])
    rows = ''
    for i, (main, sub) in enumerate(parsed):
        sb = f'<div class="sub">{esc(sub)}</div>' if sub else ''
        rows += f'<div class="row2" data-b="{cx.b(f"r{i}", d + 1.4 + 2.0 * i)}" data-anim="slideL" data-sfx="pop" style="font-size:{fs}px"><div class="bx"></div><div>{esc(main)}{sb}</div></div>'
    ex.append(f'<div class="check" style="top:{top}px">{rows}</div>')
    y = top + 20
    for i in range(len(parsed)):
        ex.append(f'<div class="tick" data-b="{cx.b(f"t{i}", d + 2.2 + 2.0 * i)}" data-anim="pop" data-sfx="tick" style="left:122px;top:{y + (rh[i] - 92) // 2}px">✓</div>')
        y += rh[i]
    if sc.get('note'):
        ex.append(sticker(cx, 'note', d + 2.0 + 2.0 * len(items) + 0.4, sc['note'], 'yellow', 'pop', 0, 'ding', 54).replace('class="sticker', 'style="position:absolute;left:110px;top:%dpx" class="sticker' % (top + 110 + sum(rh) + 20), 1))
    return [], max(8, cx.last + 3.2), '\n'.join(ex)

def b_bigword(cx, sc, bg):
    """한 마디를 크게, 왼쪽 위에. 아래쪽에 작은 설명 스티커."""
    dark = ' dark' if bg in DARK_BG else ''
    ex = []
    for i, ln in enumerate(sc['lines']):
        ex.append(f'<div class="tapeTitle st{dark} huge" data-b="{cx.b(f"line{i}", i * 1.0)}" data-anim="slam" data-sfx="slam" style="top:{sc.get("y", 310) + i * 205}px;font-size:{sc.get("fs", 170)}px">{esc(ln)}</div>')
    if sc.get('sticker'):
        s = sc['sticker']; s = {'t': s} if isinstance(s, str) else s
        ex.append(f'<div class="sticker c-{s.get("c", "yellow")}" data-b="{cx.b("sticker", len(sc["lines"]) + 0.6)}" data-anim="{s.get("anim", "slideR")}" data-rot="{s.get("rot", -3)}" data-sfx="whoosh" style="position:absolute;right:70px;top:{s.get("y", 900)}px;font-size:{s.get("size", 64)}px;max-width:820px;text-align:left">{esc(s["t"])}</div>')
    if sc.get('icon'): ex.append(icon(sc['icon'], sc.get('icon_size', 210), f'position:absolute;right:90px;top:{sc.get("icon_y", sc.get("y", 310) + len(sc["lines"]) * 205 + 40)}px;', None, cx.b('icon', len(sc['lines']) + 0.2)))
    return [], max(5, cx.last + 2.6), '\n'.join(ex)

BLOCKS = {'title': (b_title, 'blue'), 'choices': (b_choices, 'white'), 'bars': (b_bars, 'blue'), 'dice': (b_dice, 'orange'),
          'chain': (b_chain, 'white'), 'stack': (b_stack, 'yellow'), 'cards': (b_cards, 'blue'), 'tip': (b_tip, 'white'),
          'list': (b_list, 'yellow'), 'vs': (b_vs, 'blue'), 'outro': (b_outro, 'blue'),
          'speech': (b_speech, 'white'), 'notes': (b_notes, 'blue'), 'split': (b_split, 'white'), 'check': (b_check, 'white'), 'bigword': (b_bigword, 'blue')}
