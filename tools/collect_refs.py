#!/usr/bin/env python3
"""모든 페이지의 '출처와 기준' 섹션에서 링크를 모아 docs/appendix/references.md의 목록 부분을 만든다.
사용: python3 tools/collect_refs.py   (그다음 python3 tools/build_book.py는 필요 없음)"""
import re, pathlib, collections, urllib.parse
root = pathlib.Path(__file__).resolve().parent.parent
docs = root / 'docs'
link = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
refs = collections.OrderedDict()
for md in sorted(docs.rglob('*.md')):
    if md.name == 'references.md': continue
    t = md.read_text(encoding='utf-8')
    if '## 출처와 기준' not in t: continue
    title = re.search(r'^# (.+)$', t, re.M).group(1).replace(' ★', '').strip()
    sec = t.split('## 출처와 기준', 1)[1]
    rel = md.relative_to(docs).as_posix()
    for text, url in link.findall(sec):
        url = url.rstrip('.,')
        r = refs.setdefault(url, {'texts': [], 'pages': []})
        r['texts'].append(text); r['pages'].append((rel, title))
def kind(u):
    h = urllib.parse.urlparse(u).netloc
    if 'arxiv.org' in h or 'doi.org' in h: return '1 논문'
    if 'anthropic.com' in h or 'claude.com' in h: return '2 Anthropic 문서와 글'
    if '3blue1brown' in h or 'youtube.com' in h: return '3 영상과 강의'
    if 'nobelprize' in h or 'safe.ai' in h or h.endswith('samaltman.com') or 'darioamodei' in h or 'karpathy.github.io' in h: return '4 사람들의 글과 발언'
    if 'nist.gov' in h or 'modelcontextprotocol' in h or 'owasp' in h: return '5 표준과 가이드'
    return '6 보도와 기타'
groups = collections.defaultdict(list)
for u, r in refs.items():
    best = max(r['texts'], key=len)
    groups[kind(u)].append((best, u, r['pages']))
names = {'1 논문': '논문 (arXiv, DOI)', '2 Anthropic 문서와 글': 'Anthropic 문서와 글', '3 영상과 강의': '영상과 강의', '4 사람들의 글과 발언': '사람들이 직접 쓴 글과 공개 발언', '5 표준과 가이드': '표준과 가이드', '6 보도와 기타': '보도와 기타'}
out = []
for k in sorted(groups):
    out.append(f'### {names[k]} ({len(groups[k])}개)\n')
    out.append('| 자료 | 이 책에서 쓴 페이지 |\n|---|---|')
    for text, u, pages in sorted(groups[k], key=lambda x: x[0].lower()):
        pg = ', '.join(f'[{t}](../{p})' for p, t in dict.fromkeys(pages))
        out.append(f'| [{text}]({u}) | {pg} |')
    out.append('')
body = '\n'.join(out)
ref = docs / 'appendix' / 'references.md'
head = ref.read_text(encoding='utf-8') if ref.exists() else ''
if '<!-- AUTO:refs -->' in head:
    head = re.sub(r'<!-- AUTO:refs -->.*?<!-- /AUTO:refs -->', lambda m: f'<!-- AUTO:refs -->\n{body}\n<!-- /AUTO:refs -->', head, flags=re.S)
    ref.write_text(head, encoding='utf-8')
print(f'자료 {len(refs)}개를 모았어요.')
