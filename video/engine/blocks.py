"""재료 상자: 장면 조각(블록) 모음. 각 블록은 (html, 기본 길이)를 돌려준다. 시각은 모두 '박' 단위(128bpm).
장면 JSON에서 "at": {"이름": 박}으로 개별 시각을, "beats": 숫자로 장면 길이를 바꿀 수 있다."""
import html as H

BG = {'blue': '#2F7FD8', 'yellow': '#FFD93D', 'white': '#FCFCFC', 'orange': '#FC5424'}
DARK_BG = ('yellow', 'white')          # 밝은 바탕에서는 글자를 먹색으로
COLORS = ('red', 'yellow', 'green', 'blue', 'ink')

def esc(t): return H.escape(str(t), quote=False).replace('\n', '<br>')
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
    return f'<div class="mas" data-face="{face}" data-b="{cx.b("mascot", m.get("at", 4.4))}" data-anim="pop" data-sfx="pop" style="{pos}"></div>'

# ---------------- 블록 ----------------
def b_title(cx, sc, bg):
    L = sc['lines']; n = len(L)
    parts = [lines_html(cx, L, bg, sc.get('size', 'huge'))]
    if sc.get('sticker'):
        s = sc['sticker']; s = {'t': s} if isinstance(s, str) else s
        parts.append(sticker(cx, 'sticker', n + 0.4, s['t'], s.get('c', 'yellow'), s.get('anim', 'pop'), s.get('rot', -3)))
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
         sticker(cx, 'left', 1.8, L['t'], L.get('c', 'red'), 'slideL', 0, 'whoosh', 96),
         f'<div class="st big" data-b="{cx.b("vs", 3.4)}" data-anim="slam" data-sfx="slam">VS</div>',
         sticker(cx, 'right', 4.6, R['t'], R.get('c', 'green'), 'slideR', 0, 'whoosh', 96)]
    if sc.get('note'): p.append(sticker(cx, 'note', 6.6, sc['note'], 'yellow', 'pop', -2, 'ding', 62))
    return p, max(8, cx.last + 2.8), ''

def b_outro(cx, sc, bg):
    cx.t('mascot', 1)
    p = [f'<div class="sticker" data-b="{cx.b("brand", 0)}" data-anim="slam" data-sfx="slam" style="font-size:120px">{esc(sc.get("brand", "AI 정주행"))}</div>',
         f'<div class="st sm" data-b="{cx.b("sub", 1.2)}" data-anim="pop" data-sfx="pop" style="font-size:62px;-webkit-text-stroke:12px var(--ink)">{esc(sc.get("sub", "열 살도 이해하는 AI 교과서"))}</div>',
         f'<div class="sticker c-red beat" data-b="{cx.b("link", 3)}" data-anim="pop" data-sfx="ding" style="font-size:68px">{esc(sc.get("link", "프로필 링크에서 보기"))}</div>']
    sc.setdefault('mascot', {'face': 'happy:grin', 'side': 'center', 'at': 1})
    return p, 8, ''

BLOCKS = {'title': (b_title, 'blue'), 'choices': (b_choices, 'white'), 'bars': (b_bars, 'blue'), 'dice': (b_dice, 'orange'),
          'chain': (b_chain, 'white'), 'stack': (b_stack, 'yellow'), 'cards': (b_cards, 'blue'), 'tip': (b_tip, 'white'),
          'list': (b_list, 'yellow'), 'vs': (b_vs, 'blue'), 'outro': (b_outro, 'blue')}
