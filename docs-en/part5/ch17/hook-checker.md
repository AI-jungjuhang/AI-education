# Hands-on: add an automatic checker

<p class="ep-meta"><span>Ch. 17 · 17.2</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - You'll build a hook that **automatically checks for a "Sources and date checked" section** every time a book page is edited.
    - A hook script ==reads its input, then answers with a number when it ends (an exit code)==. 2 means "there's a problem."
    - The trick is to run the script on its own first.

## A checker that keeps our book's promise

One of this book's promises is "every page lists its sources and the date checked." People (and AI) sometimes forget. So let's have a checker look right after each file edit.

## Write the check script

Save this as `.claude/hooks/check-page-en.sh`:

```bash
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
```

Here's how to read it, line by line.

- `INPUT=$(cat)`: a hook receives what happened as JSON text. This puts it in a variable.
- `jq -r '.tool_input.file_path'`: pulls just "the path of the edited file" out of the JSON. (You need `jq` installed.)
- `case … */docs-en/*.md`: if it isn't a Markdown file in the docs-en folder, it does nothing and ends.
- `exit 2` with `>&2`: the problem message goes to the error output (`>&2`), and the script ends with 2. That message is passed to Claude.

Make it runnable:

```bash
chmod +x .claude/hooks/check-page-en.sh
```

## Run it on its own first (important!)

Before Claude ever calls the hook, run it yourself with fake input:

```bash
echo '{"tool_input":{"file_path":"/path/docs-en/test.md"}}' | .claude/hooks/check-page-en.sh; echo "exit code: $?"
```

For a file without the section, you should see the message and exit code 2. For a file with it, you should see 0. We ran this exact script on both cases, plus a file outside `docs-en`, before writing this page.

## Register it

Add this to `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-page-en.sh"
          }
        ]
      }
    ]
  }
}
```

`Edit|Write` means "when a file is edited or newly written." `PostToolUse` runs right after the tool finishes, so the file has already changed. Ending with 2 here passes your message to Claude, which helps it fix the page on its own. (It's not a guarantee that it will.)

!!! tip "In 10-year-old words"
    A checker hook is a short program that only ever answers "there's a problem (2)" or "all good (0)."

!!! note "★ Going deeper"
    The hook that "stops it before it happens" is `PreToolUse`. For example, a script can block edits to a secrets file like `.env`. `PostToolUse` tells Claude after the fact; `PreToolUse` stops the action before it happens. What exit code 2 means differs by event (some events block, some only pass on a message), so check the table in the hooks reference.

## Try it yourself

1. Make the script above, and **run it on its own first** to see 0 and 2.
2. Register it, and check with `/hooks` that it appears under `PostToolUse`.
3. Ask Claude: "Create test.md in the docs-en folder with just a title." Does Claude get the checker's message and add a "Sources and date checked" section?

## Use it today

- If there's a check you always ask for in the same words, move it into a hook.
- Always run a new hook on its own before registering it.
- Don't run heavy checks (like a full build) on every file edit. Save them for when Claude finishes answering (`Stop`).

## Common mix-ups

- "If a hook errors out, the job stops." Exit codes other than 0 and 2 mostly just let things continue. Checks that must block need their own setup.
- "With a checker, I don't need to look." The checker only sees whether the section exists. Whether the sources are right still needs a person to open them.
- "An `Edit|Write` hook sees every file change." No. Claude can also create or change files by running shell commands, and this hook may not see those. If you need to catch every change, the official docs suggest adding a `Stop` hook that scans the working folder once when Claude finishes.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. We ran the script ourselves on Linux with `jq`.
- The practice file for this page is in the repository at `examples/claude-code/check-page-en.sh` (the Korean edition's version is `check-page.sh`).
- **Source of facts:** [Official docs: Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide) and [Hooks reference](https://code.claude.com/docs/en/hooks). Read on 2026-11-09.
- **Learning order:** [claude-howto 06-hooks](https://github.com/luongnv89/claude-howto/tree/main/06-hooks) (MIT; rewritten in our own words).
