#!/usr/bin/env python3
"""영어판 페이지가 쉬운지 학년 점수로 잰다 (2026-11-09 사용자 결정: 본문 6학년 이하).

사용: python3 tools/readability.py [파일...]      (파일을 안 주면 docs-en/ 아래 index.md가 아닌 페이지 전부)
필요: pip install textstat==0.7.8   (0.7.9 이후는 음절 사전을 실행 중에 인터넷에서 받는데, 작업 환경에서 막힌다.
      0.7.8은 사전을 패키지로 함께 설치한다. 사이트 배포에는 필요 없어서 requirements.txt에 넣지 않았다)

재는 것: Flesch-Kincaid 학년 점수(FK). 미국 학년으로 몇 학년이면 읽는지 어림한 값이다.
재지 않는 곳: 코드 블록, 표, 제목 줄, ★ 심화 상자("Going deeper"), "Sources" 절 이후.
  심화 상자는 전문 용어를 모아 두는 곳이라 일부러 뺀다.
기준: FK가 6.0을 넘으면 실패(종료 코드 1). 25단어가 넘는 문장은 따로 보여 준다.
한계: 점수는 문장 길이와 음절 수만 본다. 'token', 'hallucination' 같은 꼭 필요한 용어도 점수를 올리고,
  쉬운 말로 쓴 엉터리 문장도 통과한다. 사람이 읽는 점검을 대신하지 않는다.
"""
import pathlib, re, sys
import textstat

LIMIT, LONG = 6.0, 25
root = pathlib.Path(__file__).resolve().parent.parent

def prose(md: str) -> str:
    out, lines, i = [], md.split('\n'), 0
    if lines and lines[0].strip() == '---':          # 머리말(front matter)
        i = lines.index('---', 1) + 1 if '---' in lines[1:] else 0
    fence = False
    skip_box = False
    while i < len(lines):
        ln = lines[i]; i += 1
        s = ln.strip()
        if s.startswith('```'):
            fence = not fence; continue
        if fence: continue
        if re.match(r'^##\s+Sources', s): break
        if s.startswith('!!!') or s.startswith('???'):
            skip_box = '★' in s or 'going deeper' in s.lower()
            continue
        if skip_box:
            if ln.startswith('    ') or not s: continue
            skip_box = False
        if not s or s.startswith('#') or s.startswith('|') or s.startswith('<'):
            continue
        s = re.sub(r'<[^>]+>', '', s)                     # HTML
        s = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', s)   # 링크와 그림
        s = re.sub(r'\{[^}]*\}', '', s)                   # attr_list
        s = re.sub(r'`[^`]*`', 'code', s)                 # 인라인 코드
        s = s.replace('==', '').replace('**', '')
        s = re.sub(r'^([-*+]|\d+\.)\s+', '', s)           # 목록 표시
        if s and s[-1] not in '.!?:': s += '.'           # 목록 항목도 한 문장으로 센다
        out.append(s)
    return '\n'.join(out)

def main():
    files = [pathlib.Path(a) for a in sys.argv[1:]] or sorted(
        p for p in (root / 'docs-en').rglob('*.md') if p.name != 'index.md' and not p.is_symlink())
    files = [f for f in files if not any(part in ('assets', 'stylesheets', 'javascripts') for part in f.parts)]
    if not files:
        print('검사할 영어 페이지가 없어요.'); return 0
    bad = 0
    for f in files:
        text = prose(f.read_text(encoding='utf-8'))
        if not text.strip(): continue
        fk = textstat.flesch_kincaid_grade(text)
        sents = [x for x in re.split(r'(?<=[.!?])["\')]*\s+', text.replace('\n', ' ')) if x.strip()]
        avg = sum(len(x.split()) for x in sents) / max(len(sents), 1)
        ok = fk <= LIMIT
        bad += not ok
        print(f"{'통과' if ok else '실패'}  FK {fk:4.1f}  평균 {avg:4.1f}단어/문장  {f}")
        for x in sents:
            if len(x.split()) > LONG: print(f'      긴 문장({len(x.split())}단어): {x[:110]}')
    print(f'기준: FK {LIMIT} 이하. 실패 {bad}개.')
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main())
