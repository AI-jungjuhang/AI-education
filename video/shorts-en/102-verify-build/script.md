# Short en-102 · Hands-on: this channel's checking loop

- **Source page:** 23.4.2 [Hands-on: this channel's checking loop](../../../docs-en/part6/ch23/verify-build.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** checks are gatekeepers that decide when "done" is allowed. Make sure a quiet option doesn't hide failures, and give any hook that sends Claude back a loop guard.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Checks decide when it's "done" / Three layers of gatekeepers | "What you'll learn" (first two points) |
| 2 | 9–21 | Three gatekeepers / 1. Format: Each edit / 2. Build: Before it finishes / 3. Content: Matches the source | "Three gatekeepers" table ("When" and "What it checks" columns) |
| 3 | 21–32 | For the build check: mkdocs build --strict -q (-q let a broken link pass) / mkdocs build --strict (We ran into this) | "Don't add -q (quiet)" in "The build check script" |
| 4 | 32–42 | A hook that sends Claude back needs a loop guard so it can't loop forever / If it already sent Claude back once, let it stop | "What you'll learn" (safety switch); the `stop_hook_active` bullet |
| 5 | 42–57 | Use it today: Does -q hide failures? Test once / Test new checks with fail and pass cases / Hook sends it back? Add a loop guard | "Use it today" 1, 2, 3 |

## Choices and notes
- Commands are exactly `mkdocs build --strict -q` and `mkdocs build --strict`, as on the page. The page reports exit code 0 with `-q` and 1 without it on a site with a broken link; the sticker says this in words.
- "Does it say anything the original doesn't?" is shortened to "Matches the source."
- `stop_hook_active` is described in words in scene 4 instead of shown as code, so the bubble stays readable.
- The script itself, the settings.json registration, and the eight-block limit are left out to keep one idea.
