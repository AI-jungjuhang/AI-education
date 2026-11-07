#!/usr/bin/env python3
"""배경음악을 스크립트로 직접 작곡한다(저작권 문제 없음). 사용: python3 make_music.py <출력.wav> [길이초=58]
느린 화음 패드 + 부드러운 아르페지오 + 낮은 베이스. 72bpm, Cmaj7 - Am7 - Fmaj7 - G6 반복."""
import sys, numpy as np, wave
out = sys.argv[1]; D = float(sys.argv[2]) if len(sys.argv) > 2 else 58.0
SR = 44100; n = int(SR * D); t = np.arange(n) / SR
bpm = 72; beat = 60 / bpm; bar = beat * 4
chords = [([130.81, 164.81, 196.00, 246.94], 65.41), ([110.00, 130.81, 164.81, 196.00], 55.00),
          ([87.31, 110.00, 130.81, 164.81], 43.65), ([98.00, 123.47, 146.83, 164.81], 49.00)]
L = np.zeros(n); R = np.zeros(n)
def env(x, a, r, d):  # 부드러운 시작과 끝
    return np.clip(x / a, 0, 1) * np.clip((d - x) / r, 0, 1)
nb = int(np.ceil(D / bar)) + 1
for k in range(nb):
    notes, bass = chords[k % 4]; s = k * bar
    i0 = int(s * SR); dur = bar + 0.9; m = min(n - i0, int(dur * SR))
    if m <= 0: break
    x = np.arange(m) / SR; e = env(x, 0.9, 0.9, dur)
    for j, f in enumerate(notes):
        for det, pan in ((1.0, -0.4 + 0.25 * j / 3), (1.004, 0.4 - 0.25 * j / 3)):
            w = (np.sin(2 * np.pi * f * det * x) + 0.25 * np.sin(2 * np.pi * 2 * f * det * x)) * e * 0.045
            L[i0:i0 + m] += w * (1 - pan) / 2; R[i0:i0 + m] += w * (1 + pan) / 2
    wb = np.sin(2 * np.pi * bass * x) * env(x, 0.3, 0.8, dur) * 0.16
    L[i0:i0 + m] += wb; R[i0:i0 + m] += wb
    # 아르페지오: 8분음표마다 화음의 음을 한 옥타브 위에서 부드럽게 튕긴다
    order = [0, 2, 1, 3, 2, 1, 3, 2]
    for q in range(8):
        ts = s + q * beat / 2; ia = int(ts * SR)
        if ia >= n: break
        f = notes[order[q]] * 2; mm = min(n - ia, int(1.6 * SR)); xx = np.arange(mm) / SR
        p = (np.sin(2 * np.pi * f * xx) + 0.3 * np.sin(2 * np.pi * 2 * f * xx)) * np.exp(-xx * 3.2) * np.clip(xx / 0.006, 0, 1) * 0.07
        pan = 0.35 if q % 2 else -0.35
        L[ia:ia + mm] += p * (1 - pan) / 2; R[ia:ia + mm] += p * (1 + pan) / 2
# 간단한 에코로 공간감
def echo(a, delay, fb, mix):
    d = int(delay * SR); y = a.copy()
    for i in range(d, n): y[i] += a[i - d] * 0.0
    buf = np.zeros(n)
    for r in range(1, 4):
        sh = d * r
        if sh < n: buf[sh:] += a[:n - sh] * (fb ** r)
    return a + buf * mix
L = echo(L, 0.375, 0.5, 0.6); R = echo(R, 0.5, 0.5, 0.6)
fade = np.clip(t / 1.5, 0, 1) * np.clip((D - t) / 2.5, 0, 1)
L *= fade; R *= fade
pk = max(np.abs(L).max(), np.abs(R).max()); L, R = L / pk * 0.7, R / pk * 0.7
st = (np.stack([L, R], axis=1) * 32767).astype(np.int16)
with wave.open(out, 'wb') as wf:
    wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes(st.tobytes())
print('음악 생성', out, f'{D}초')
