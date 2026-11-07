#!/usr/bin/env python3
"""박자에 맞춘 신나는 배경음악과 효과음을 직접 합성한다(저작권 문제 없음).
사용: python3 make_music.py <timeline.json> <출력.wav> [soft]
두 번째 인자 soft: 드럼 없이 부드러운 패드·플럭·가벼운 박자만 쓰는 조용한 버전(효과음도 작게).
timeline.json은 render.js가 scene.html에서 뽑은 효과음 위치(박 단위). 128bpm, C - Am - F - G."""
import sys, json, numpy as np
from scipy.signal import butter, sosfilt
tl = json.load(open(sys.argv[1])); out = sys.argv[2]; SOFT = len(sys.argv) > 3 and sys.argv[3] == 'soft'
BPM = tl['bpm']; BEAT = 60 / BPM; TOTAL = tl['total']; SR = 44100
D = TOTAL * BEAT; n = int((D + 0.6) * SR)
rng = np.random.default_rng(7)
L = np.zeros(n); R = np.zeros(n)
def put(buf, x, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR)
    if i < 0: x = x[-i:]; i = 0
    m = min(len(x), n - i)
    if m <= 0: return
    L[i:i+m] += x[:m] * gain * (1 - pan) / 2 * 1.4; R[i:i+m] += x[:m] * gain * (1 + pan) / 2 * 1.4
def hp(x, f): return sosfilt(butter(2, f, 'hp', fs=SR, output='sos'), x)
def lp(x, f): return sosfilt(butter(2, f, 'lp', fs=SR, output='sos'), x)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'bp', fs=SR, output='sos'), x)
def tt(d): return np.arange(int(d * SR)) / SR
# ---- 드럼 ----
def kick():
    t = tt(0.32); f = 135 * np.exp(-t * 22) + 46
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * 1.0 + hp(rng.standard_normal(len(t)), 1800) * np.exp(-t * 90) * 0.12
def snare():
    t = tt(0.22); return (hp(rng.standard_normal(len(t)), 1200) * np.exp(-t * 20) * 0.7 + np.sin(2 * np.pi * 190 * t) * np.exp(-t * 28) * 0.4)
def clap():
    t = tt(0.2); e = sum(np.exp(-np.clip(t - d, 0, None) * 45) * (t >= d) for d in (0, 0.012, 0.026)); return bp(rng.standard_normal(len(t)), 1100, 6000) * e * 0.5
def hat(open_=False):
    t = tt(0.22 if open_ else 0.05); return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t * (14 if open_ else 80)) * 0.32
def bass(f, d):
    t = tt(d); e = np.clip(t / 0.01, 0, 1) * np.exp(-t * 3.5)
    return (np.sin(2 * np.pi * f * t) + 0.55 * np.sin(2 * np.pi * 2 * f * t) + 0.3 * np.sin(2 * np.pi * 3 * f * t)) * e * 0.55
def stab(freqs, d):
    t = tt(d); e = np.clip(t / 0.005, 0, 1) * np.exp(-t * 14); y = 0
    for f in freqs: y = y + sum(np.sin(2 * np.pi * f * k * t) / k for k in (1, 2, 3))
    return lp(y, 5500) * e * 0.10
def pluck(f, d=0.28):
    t = tt(d); return (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t)) * np.exp(-t * 12) * np.clip(t / 0.003, 0, 1) * 0.16
chords = [([261.63, 329.63, 392.00], 65.41), ([220.00, 261.63, 329.63], 55.00), ([174.61, 220.00, 261.63], 43.65), ([196.00, 246.94, 293.66], 49.00)]
lift = [tuple(x) for x in tl.get('lift', [])]
def in_lift(b): return any(a <= b < e for a, e in lift)
def pad(freqs, d):
    t = tt(d); e = np.clip(t / 0.35, 0, 1) * np.clip((d - t) / 0.4, 0, 1); y = 0
    for f in freqs: y = y + np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)
    return lp(y, 1800) * e * 0.09
def soft_kick():
    t = tt(0.25); f = 90 * np.exp(-t * 25) + 48
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 14) * 0.5
def soft_pluck(f, d=0.5):
    t = tt(d); return (np.sin(2 * np.pi * f * t) + 0.2 * np.sin(2 * np.pi * 3 * f * t)) * np.exp(-t * 7) * np.clip(t / 0.004, 0, 1) * 0.14
nb = int(TOTAL)
if SOFT:
    mel = [0, 2, 1, 2, 0, 2, 1, 0]
    for i in range(nb):
        t0 = i * BEAT; bar = i // 4; ch, root = chords[bar % 4]; ph = i % 4
        if ph == 0:
            put(L, pad(ch + [root * 4], BEAT * 4.2), t0, 1.0, 0.0)
            put(L, bass(root * 2, BEAT * 1.6), t0, 0.35)
        if ph in (0, 2): put(L, soft_kick(), t0, 0.5)
        put(L, hat(), t0 + BEAT / 2, 0.18, 0.25 if i % 2 else -0.25)
        k = mel[(i // 1) % len(mel)]
        if ph in (0, 1, 3) or in_lift(i): put(L, soft_pluck(ch[k] * 2), t0 + (0.5 * BEAT if ph == 3 else 0), 0.8, (-0.3, 0.3)[i % 2])
else:
    for i in range(nb):
      t0 = i * BEAT; bar = i // 4; ch, root = chords[bar % 4]; ph = i % 4
      put(L, kick(), t0, 1.0 if i else 1.2)
      if ph in (1, 3): put(L, snare(), t0, 0.9); put(L, clap(), t0, 0.7)
      put(L, hat(), t0 + BEAT / 2, 0.8, 0.25)
      if ph == 3: put(L, hat(True), t0 + BEAT / 2, 0.7, -0.25)
      if in_lift(i):
          for q in (0.25, 0.75): put(L, hat(), t0 + q * BEAT, 0.55, 0.3 if q < .5 else -0.3)
          for q, f in enumerate([ch[0], ch[1], ch[2], ch[1] * 2]): put(L, pluck(f * 2), t0 + q * BEAT / 4 * 1, 0.8, (-0.4, 0.4)[q % 2])
      if ph == 0:
          for pos in (0, 0.75, 1.5, 2.0, 2.75, 3.5): put(L, bass(root, BEAT * 0.4), t0 + pos * BEAT, 1.0)
          put(L, stab(ch, 0.2), t0 + 0.5 * BEAT, 0.9, 0.2); put(L, stab(ch, 0.2), t0 + 2.5 * BEAT, 0.9, -0.2)
# ---- 효과음 ----
def sfx_pop():
    t = tt(0.14); f = 950 * np.exp(-t * 20) + 260; return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 26) * 0.8
def sfx_slam():
    t = tt(0.5); f = 150 * np.exp(-t * 13) + 38
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 6.5) * 1.1 + hp(rng.standard_normal(len(t)), 900) * np.exp(-t * 38) * 0.55
def sfx_whoosh():
    t = tt(0.42); nz = rng.standard_normal(len(t)); y = np.zeros(len(t)); k = 7
    for s in range(k):
        a, b = int(s * len(t) / k), int((s + 1) * len(t) / k); c = 500 * (1.55 ** s)
        y[a:b] = bp(nz, c, c * 1.9)[a:b]
    env = np.sin(np.pi * np.clip(t / 0.42, 0, 1)) ** 2; return y * env * 1.4
def sfx_tick():
    t = tt(0.06); return (np.sin(2 * np.pi * 2300 * t) * 0.7 + hp(rng.standard_normal(len(t)), 3000) * 0.5) * np.exp(-t * 85)
def sfx_ding():
    t = tt(1.0); return sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t * d) for f, a, d in ((1175, 0.6, 4.5), (1760, 0.35, 6), (2349, 0.25, 8), (3136, 0.12, 10))) * np.clip(t / 0.002, 0, 1)
def sfx_buzz():
    t = tt(0.42); f = np.where(t < 0.2, 150, 105); ph = np.cumsum(f) / SR * 2 * np.pi
    return lp(np.sign(np.sin(ph)) + 0.7 * np.sign(np.sin(ph * 1.03)), 1400) * np.exp(-t * 2.2) * 0.45
def sfx_rattle(d):
    t = tt(d); y = np.zeros(len(t)); step = int(0.042 * SR); 
    for i in range(0, len(t) - 400, step):
        j = i + int(rng.integers(0, 300)); seg = hp(rng.standard_normal(500), 1800) * np.exp(-np.arange(500) / SR * 150) * rng.uniform(0.4, 1.0)
        y[j:j+500] += seg[:len(y[j:j+500])]
        y[j:j+500] += (np.sin(2 * np.pi * rng.uniform(300, 700) * np.arange(500) / SR) * np.exp(-np.arange(500) / SR * 70) * 0.5)[:len(y[j:j+500])]
    return y * np.sin(np.pi * np.clip(t / d, 0, 1)) ** 0.5 * 0.9
G = {'pop': 0.75, 'slam': 0.95, 'whoosh': 0.5, 'tick': 0.55, 'ding': 0.5, 'buzz': 0.6, 'rattle': 0.5}
if SOFT: G = {'pop': 0.09, 'slam': 0.10, 'whoosh': 0.05, 'tick': 0.07, 'ding': 0.08, 'buzz': 0.08, 'rattle': 0.07}   # 음악보다 확실히 작게
_put = put
if SOFT:
    def put(buf, x, t0, gain=1.0, pan=0.0): return _put(buf, lp(x, 3500), t0, gain, pan)
for e in tl['sfx']:
    t0 = e['b'] * BEAT; k = e['t']
    if k == 'pop': put(L, sfx_pop(), t0, G[k])
    elif k == 'slam': put(L, sfx_slam(), t0, G[k])
    elif k == 'whoosh': put(L, sfx_whoosh(), t0 - 0.2, G[k])
    elif k == 'tick': put(L, sfx_tick(), t0, G[k])
    elif k == 'ding': put(L, sfx_ding(), t0, G[k])
    elif k == 'buzz': put(L, sfx_buzz(), t0, G[k])
    elif k == 'rattle': put(L, sfx_rattle(max(0.3, e['d'] * BEAT)), t0, G[k])
fade = np.clip((D + 0.5 - np.arange(n) / SR) / 0.5, 0, 1)
L *= fade; R *= fade
L = np.tanh(L * 1.1); R = np.tanh(R * 1.1)
pk = max(abs(L).max(), abs(R).max()); L, R = L / pk * 0.89, R / pk * 0.89
import wave
st = (np.stack([L, R], 1) * 32767).astype(np.int16)
with wave.open(out, 'wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes(st.tobytes())
print('음악과 효과음 생성', out, f'{D:.2f}초, 효과음 {len(tl["sfx"])}개')
