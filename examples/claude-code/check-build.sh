#!/bin/bash
# Claude가 답을 마치려 할 때 사이트가 경고 없이 만들어지는지 확인한다.
INPUT=$(cat)

# 이미 한 번 되돌려 보냈다면 이번에는 멈추게 한다 (무한 반복 방지)
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR" || exit 0
mkdocs build --strict 1>&2 || exit 2
exit 0
