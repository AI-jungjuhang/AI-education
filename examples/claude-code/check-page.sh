#!/bin/bash
# 페이지를 고친 뒤 "출처와 기준" 절이 있는지 확인한다.
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE" in
  */docs/*.md) ;;
  *) exit 0 ;;
esac

if ! grep -q "^## 출처와 기준" "$FILE"; then
  echo "이 페이지에는 '## 출처와 기준' 절이 없어요. 출처와 기준 날짜를 추가해 주세요: $FILE" >&2
  exit 2
fi
exit 0
