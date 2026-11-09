#!/bin/bash
# For each page in docs-en, list words a 10-year-old would find hard, and save to out/.
set -euo pipefail
mkdir -p out

find docs-en -name '*.md' -print0 | sort -z | while IFS= read -r -d '' f; do
  name=$(echo "$f" | tr '/' '_')
  claude --bare -p \
      "List only the words a 10-year-old would find hard to read. If there are none, say 'none'." \
      --allowedTools "Read" --max-turns 3 < "$f" > "out/${name}.txt"
  echo "done: $f"
done
