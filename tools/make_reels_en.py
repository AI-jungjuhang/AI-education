#!/usr/bin/env python3
"""영어 쇼츠 설명글 초안을 만든다: video/all-en/reels-captions.csv
첫 줄(이모지 + 첫 장면 제목), 둘째 줄(첫 장면 스티커), 📌 Use it today(마지막 체크리스트),
👉 안내, 📖 책 위치(book-en.yml), 해시태그. 이모지는 한국어 예약표의 같은 편에서 가져온다.
손으로 고친 문장은 video/all-en/caption-overrides.json에 {"편": {"hook": [...], "tips": [...]}}로 둔다.
사용: python3 tools/make_reels_en.py"""
import csv, json, re, pathlib, yaml
root = pathlib.Path(__file__).resolve().parent.parent
book = yaml.safe_load(open(root / 'book-en.yml', encoding='utf-8'))
loc = {}
for p in book['parts']:
    for c in p.get('chapters') or []:
        for s in c['sections']:
            for i, q in enumerate(s['pages'], 1):
                loc[q['slug']] = (p['title'], f"Ch. {c['num']} {c['title']}", f"{s['num']} {s['title']}", f"{s['num']}.{i} {q['title']}", c['num'])
ko = {r[0].lstrip('﻿'): r for r in csv.reader(open(root / 'video/all/reels-schedule.csv', encoding='utf-8-sig'))}
ov_path = root / 'video/all-en/caption-overrides.json'
ov = json.load(open(ov_path, encoding='utf-8')) if ov_path.exists() else {}
TAGS = [((1, 4), '#AIForBeginners'), ((5, 8), '#AIAtWork'), ((9, 12), '#HowAIWorks'), ((13, 15), '#AIAgents'), ((16, 18), '#ClaudeCode'), ((19, 23), '#AIDeepDive')]
def clean(t): return re.sub(r'\s+', ' ', re.sub(r'==', '', t.split('||')[0]).replace('\n', ' ')).strip()
def first_text(sc):
    for k in ('lines',):
        if sc.get(k): return [clean(' '.join(sc[k]))]
    for k in ('title', 'head', 'say'):
        if sc.get(k): return [clean(sc[k])]
    if sc.get('items') and isinstance(sc['items'][0], dict) and sc['items'][0].get('t'): return [clean(sc['items'][0]['t'])]
    return ['']
rows = []
for d in sorted((root / 'video/shorts-en').iterdir()):
    if not (d / 'episode.json').exists(): continue
    n, slug = d.name[:3], d.name[4:]
    ep = json.load(open(d / 'episode.json', encoding='utf-8')); s0 = ep['scenes'][0]
    hook = first_text(s0)
    st = s0.get('sticker')
    if st: hook.append(clean(st['t'] if isinstance(st, dict) else st))
    tips = []
    for sc in reversed(ep['scenes']):
        if sc['type'] in ('check', 'tip'):
            tips = [clean(x) for x in (sc.get('items') or [' '.join(sc.get('lines', []))])]; break
    o = ov.get(n, {}); hook = o.get('hook', hook); tips = o.get('tips', tips)
    part, ch, sec, page, chn = loc[slug if slug != 'token-effects' else 'tokens']
    if slug == 'tokens': page += ' (1/2)'
    if slug == 'token-effects': page += ' (2/2)'
    emoji = ko[n][6].split(' ')[0] if n in ko else '🤖'
    tag = next(t for (a, b), t in TAGS if a <= chn <= b)
    body = f"{emoji} {hook[0]}" + (f"\n{hook[1]}" if len(hook) > 1 and hook[1] else '')
    if tips: body += '\n\n📌 Use it today\n' + '\n'.join(f'- {t}' for t in tips)
    elif o.get('extra'): body += '\n\n' + '\n'.join(o['extra'])
    body += f"\n\n👉 Want more? It's all in the book site (link in profile)\n📖 Part {part} › {ch}\n   › {sec} › {page}"
    body += f"\n\n#AIStartToFinish #LearnAI #ArtificialIntelligence #Chatbot #AITextbook {tag}"
    title = hook[0]
    rows.append([n, '', '', f'en-{d.name}.mp4', ep['tag'], ep.get('name', ''), title, body])
out = root / 'video/all-en/reels-captions.csv'
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f); w.writerow(['편', '예약 날짜', '예약 시각', '영상 파일', '번호', '이름', '제목', '설명글']); w.writerows(rows)
# 릴스 예약표: 한국어 예약표와 같은 열·같은 시간표(하루 10편). 2026-11-10 사용자 결정: 2026-11-11부터, 영어 전용 새 계정.
import datetime
START = datetime.date(2026, 11, 11)
TIMES = ['08:00', '09:30', '11:00', '12:30', '14:00', '15:30', '17:00', '18:30', '20:00', '21:30']
sch = root / 'video/all-en/reels-schedule.csv'
with open(sch, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f); w.writerow(['편', '예약 날짜', '예약 시각', '영상 파일', '번호', '이름', '설명글'])
    for i, r in enumerate(rows):
        w.writerow([r[0], (START + datetime.timedelta(days=i // 10)).isoformat(), TIMES[i % 10], r[3], r[4], r[5], r[7]])
print(f'{len(rows)}편 → {out.relative_to(root)}, {sch.relative_to(root)}')
