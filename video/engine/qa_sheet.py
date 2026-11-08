#!/usr/bin/env python3
"""장면마다 끝나기 직전 프레임을 뽑아 한 장으로 붙인다(배치·글자 점검용). 사용: python3 qa_sheet.py <에피소드 폴더>"""
import json, subprocess, sys, pathlib
ep = pathlib.Path(sys.argv[1]); d = json.load(open(ep / 'episode.json', encoding='utf-8'))
BEAT = 60 / 128; t = 0; times = []
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from blocks import BLOCKS, Ctx
for i, sc in enumerate(d['scenes']):
    fn, bg = BLOCKS[sc['type']]; cx = Ctx(t, sc); parts, dur, extra = fn(cx, sc, sc.get('bg', bg)); dur = sc.get('beats', dur)
    t += dur; times.append(t * BEAT - 0.25)
mp4 = ep / 'out' / f"{d['id']}.mp4"; tmp = ep / 'out' / '_qa'; tmp.mkdir(exist_ok=True); fr = []
for i, x in enumerate(times):
    f = tmp / f'{i}.png'; subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', f'{x:.2f}', '-i', str(mp4), '-frames:v', '1', '-vf', 'scale=270:-1', str(f)]); fr.append(f)
cmd = ['ffmpeg', '-y', '-loglevel', 'error']
for f in fr: cmd += ['-i', str(f)]
cmd += ['-filter_complex', f'hstack={len(fr)}', str(ep / 'out' / 'qa.png')]
subprocess.run(cmd); [f.unlink() for f in fr]; tmp.rmdir(); print(ep / 'out' / 'qa.png')
