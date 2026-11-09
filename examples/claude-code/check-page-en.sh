#!/bin/bash
# English edition: after a page is edited, check that it has a "Sources and date checked" section.
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

case "$FILE" in
  */docs-en/*.md) ;;
  *) exit 0 ;;
esac

if ! grep -q "^## Sources and date checked" "$FILE"; then
  echo "This page has no '## Sources and date checked' section. Please add sources and the date checked: $FILE" >&2
  exit 2
fi
exit 0
