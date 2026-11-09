# Short en-065 · Hands-on: add an automatic checker

- **Source page:** 17.2 [Hands-on: add an automatic checker](../../../docs-en/part5/ch17/hook-checker.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a hook script checks each page edit and answers with an exit code; 2 means "there's a problem."
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | A hook checks every edit / Is the sources section there? | "What you'll learn", first bullet |
| 2 | 9–20 | Exit code 0: All good / Exit code 2: There's a problem (the message goes to Claude) | "What you'll learn", second bullet; the `exit 2` with `>&2` line |
| 3 | 20–32 | 4 steps: 1. Write check-page-en.sh / 2. chmod +x so it can run / 3. Run it alone with fake input / 4. Add it to settings.json | Sections "Write the check script", "Run it on its own first", "Register it" |
| 4 | 32–42 | Before you register it: Run it alone with fake input first / No section: 2. Section there: 0. | "Run it on its own first (important!)" |
| 5 | 42–57 | Use it today: Same check often? Move it to a hook / New hook? Run it alone first / Heavy check? Save it for Stop | "Use it today" |

## Choices and notes
- The script name is the English edition's `check-page-en.sh` (the Korean episode shows `check-page.sh`).
- "The section" in scene 1 is shortened from "a 'Sources and date checked' section" so the sticker fits.
- "Every edit" means each file edit or write that the `Edit|Write` matcher catches. The page's mix-up note (shell-command changes may be missed) is left out.
- The script and JSON are not shown in full; they're too long for a phone screen.
