# Short en-079 · Build an automation pipeline on the command line

- **Source page:** 18.2.3 [Build an automation pipeline on the command line](../../../docs-en/part5/ch18/cli-automation.md)
- **Format:** vertical 9:16, 30fps, about 28 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** put `claude -p` in a loop to check many files at once, and keep it safe: allow narrowly, set caps, and don't read unfamiliar folders.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Put claude -p in a loop / It checks many files at once | "What you'll learn" first point |
| 2 | 9–22 | Safety switches: --bare → same setup every run / --allowedTools "Read" → read only / --max-turns 3 → at most 3 rounds / set -euo pipefail → stop on errors | "Line by line" under the loop script (flags exactly as in the script) |
| 3 | 22–33 | Three rules: Allow narrowly (only Read) / Set caps (rounds, cost) / Unfamiliar folders? Don't read | "Three safety rules for automation" |
| 4 | 33–44 | For people to read: text files in out/ / For programs to read: --output-format json | "What you'll learn" third point; the loop saves to `out/`; "Getting results a program can read" |
| 5 | 44–59 | Use it today: Ten or more files? Use a loop / Put the original path in result names / Check for secret files before running | "Use it today" list |

## Choices and notes
- The Korean version put the flags on sticky notes and split `--allowedTools` across two lines. The English version shows the flags in a list so each one stays whole and exact.
- The Korean "100 files" opener is left out; the page uses 100 only as a "what if".
- `--json-schema`, `--max-budget-usd`, and the API key note are left out to keep one idea.
- The `> "out/${name}.txt"` redirect is described in words ("text files in out/") so it fits.
