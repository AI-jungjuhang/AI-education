#!/usr/bin/env bash
# 영어판 한 쪽을 끝냈을 때: 학년 점수 → 대시 검사 → book-en.yml done 표시 → 목차 반영 → strict 빌드
# 사용: bash tools/en_page_done.sh docs-en/part1/ch01/tokens.md
set -e
f="$1"; slug=$(basename "$f" .md)
python3 tools/readability.py "$f"
# 대시 검사: 인용한 제목(*...* 또는 [...] 안)의 대시는 원문 그대로 두므로 넘어간다
python3 - "$f" <<'PY'
import re, sys
bad = []
for i, line in enumerate(open(sys.argv[1], encoding='utf-8'), 1):
    t = re.sub(r'\*[^*]+\*|\[[^\]]+\]', '', line)
    if '—' in t or '–' in t: bad.append(f'{i}: {line.strip()[:100]}')
if bad:
    print('\n'.join(bad)); print('대시(—, –)가 있어요. 고쳐 주세요.'); sys.exit(1)
PY
python3 - "$slug" <<'PY'
import re, sys, pathlib
p = pathlib.Path('book-en.yml'); s = p.read_text(encoding='utf-8'); slug = sys.argv[1]
n = re.subn(r'(\{slug: ' + re.escape(slug) + r',.*?done: )false\}', r'\1true}', s)
p.write_text(n[0], encoding='utf-8'); print('book-en.yml:', slug, 'done' if n[1] else '(이미 done이거나 slug 없음)')
PY
python3 tools/build_book.py --book book-en.yml --config mkdocs-en.yml --docs docs-en
out=$(mktemp -d)
if mkdocs build --strict -f mkdocs-en.yml -d "$out" > "$out.log" 2>&1; then echo "빌드 통과"; else grep -E "WARN|ERR" "$out.log"; echo "빌드 실패"; exit 1; fi
rm -rf "$out" "$out.log"
