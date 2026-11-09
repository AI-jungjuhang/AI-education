# Hands-on: this channel's checking loop ★

<p class="ep-meta"><span>Ch. 23 · 23.4 · Deeper</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - You'll put **three layers of checks** on the flow for making a video script: a format check (hook), a build check (Stop hook), and a content review (reviewer helper).
    - The checks become gatekeepers that decide when "done" is allowed. But you need ==a safety switch so it can't loop forever==.
    - Test each check on its own first, with both a failing case and a passing case.

## Three gatekeepers

| Layer | What it checks | When | Tool |
|---|---|---|---|
| 1. Format | Does the page have a "Sources and date checked" section? | Every time a file changes | `PostToolUse` hook (`check-page-en.sh` from Chapter 17) |
| 2. Build | Does the site build with no warnings (broken links included)? | When Claude tries to finish | `Stop` hook |
| 3. Content | Does it say anything the original doesn't? | After the script is saved | `reviewer` helper (Chapter 17) |

You already made 1 and 3. On this page, you'll make 2.

## The build check script

Save this as `.claude/hooks/check-build-en.sh`:

```bash
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
```

```bash
chmod +x .claude/hooks/check-build-en.sh
```

Three things matter here:

- **`--strict`** counts any warning as a failure. Broken links are warnings, so they get caught.
- **Don't add `-q` (quiet).** We ran into this while writing this book. With `mkdocs build --strict -q`, a site with a broken link still gave exit code 0, so the check looked like it passed. Without `-q`, the same site gave exit code 1. Make sure a tool's quiet mode doesn't hide its warnings.
- **`stop_hook_active`** is true if this hook already sent Claude back. Then the script lets it stop. The docs say Claude Code steps in after a Stop hook blocks eight times in a row, and they tell you to check this value.

## Test it on its own first

Try both cases with fake input, from your site's folder:

```bash
export CLAUDE_PROJECT_DIR=$PWD
echo '{"stop_hook_active": false}' | .claude/hooks/check-build-en.sh; echo "exit code: $?"
echo '{"stop_hook_active": true}'  | .claude/hooks/check-build-en.sh; echo "exit code: $?"
```

- With a broken link, the first should give 2 (block) and the second 0 (let it stop).
- With no problems, both give 0.

We tested this on a small practice site with one broken link. We got 2, then 0, and 0 again after fixing the link. On the same site, `--strict -q` gave 0 and `--strict` alone gave 1.

## Register it

In `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-build-en.sh" }
        ]
      }
    ]
  }
}
```

A build can take a few seconds or much longer. A `Stop` hook runs every time Claude tries to finish, so it can slow you down. If that bothers you, turn the hook off and step down to strength 1: add "Before you finish, run `mkdocs build --strict` and show me the output" to your request.

!!! tip "In 10-year-old words"
    Put a gatekeeper at the door: "You can't say you're done until the check passes." And make sure the gatekeeper only sends you back once, so it doesn't repeat itself forever.

!!! note "★ Going deeper"
    - Hooks run with your computer's permissions, so the safety rules from Chapter 17 still apply. This script only runs `mkdocs`. Avoid passing outside input straight into a hook script.
    - To use the same loop in one-shot `claude -p` runs (Chapter 18), first check how hooks behave in that mode.
    - If your check really needs more than eight rounds, the docs say you can raise the limit with `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`.

## Try it yourself

1. Make the script and test both cases on their own. Add a broken link on purpose, then remove it.
2. Register it, then ask Claude: "Make test.md in docs and put the link `[x](nope.md)` in it."
3. Watch whether Claude gets the build error and fixes the link. If it can't, check that it stops the second time.
4. When you're done, delete test.md and decide whether to keep the hook.

## Use it today

1. **Check once that a tool's quiet option (`-q`) doesn't hide failures.**
2. **Test every new check with a failing case and a passing case** before you register it.
3. **Add a loop guard to any hook that sends Claude back.**

## Common mix-ups

- "If the build passes, the content is right." The build only checks format and links. The content is for the reviewer (layer 3) and your own eyes.
- "More checks means more safety." If they get slow and annoying, people turn them off. Two or three important layers are better.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319 and MkDocs 1.6.1, checked on 2026-11-09. We checked `check-build-en.sh`'s exit codes (2 and 0) on a practice site ourselves, and the `-q` problem (exit code 0 versus 1) too. We didn't check Claude actually being sent back. Try that in your own setup.
- The practice file is in the repository at `examples/claude-code/check-build-en.sh` (the Korean edition's version is `check-build.sh`). The README there says how it was checked.
- **Source of facts:** [Claude Code best practices: enforce the check with a Stop hook](https://code.claude.com/docs/en/best-practices) and [Hooks guide: Stop hook block limit](https://code.claude.com/docs/en/hooks-guide). Read on 2026-11-09.
