#!/bin/bash
# When Claude tries to finish, check that the site builds with no warnings.
INPUT=$(cat)

# If this hook already sent Claude back once, let it stop this time (no endless loop)
if [ "$(echo "$INPUT" | jq -r '.stop_hook_active')" = "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR" || exit 0
mkdocs build --strict 1>&2 || exit 2
exit 0
