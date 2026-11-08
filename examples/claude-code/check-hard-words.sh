#!/bin/bash
# docs 폴더의 페이지마다 "10살이 어려워할 단어"를 찾아 out/ 폴더에 저장한다.
set -euo pipefail
mkdir -p out

for f in $(find docs -name '*.md' | sort); do
  name=$(echo "$f" | tr '/' '_')
  cat "$f" | claude --bare -p \
      "10살이 읽기에 어려운 단어를 목록으로만 알려 줘. 없으면 '없음'." \
      --allowedTools "Read" --max-turns 3 > "out/${name}.txt"
  echo "끝: $f"
done
