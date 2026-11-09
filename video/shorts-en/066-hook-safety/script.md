# Short en-066 · Hooks run with your permissions

- **Source page:** 17.2 [Hooks run with your permissions](../../../docs-en/part5/ch17/hook-safety.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** command hooks run with all your account's permissions, so read, test and know how to turn them off.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Hooks run with your permissions / They can delete files, and read them too | "What you'll learn", first bullet |
| 2 | 9–20 | Someone else's repo: Run claude -p right away (no trust prompt, so its hooks run) X / First, read its hooks O | "Hooks from someone else's repository"; "Use it today", first bullet |
| 3 | 20–33 | 5 rules: 1. Read before you add / 2. Run it alone first / 3. Start small / 4. Put "$VAR" in quotes / 5. Know how to turn it off | "Five safety rules" (headings; rule 4 shown by its main tip) |
| 4 | 33–43 | In hook scripts: Don't use rm, the delete command / If you really need to: First make a test that only prints what it would delete | "Use it today", third bullet |
| 5 | 43–58 | Use it today: New repo? Read its hooks first / claude -p for jobs? Add --bare / Something odd? Check /hooks | "Use it today"; rule 5 (`/hooks`) |

## Choices and notes
- The Korean episode opens with "a hook opens doors with your keys." The English title states the point directly.
- The page has five rules; the Korean episode showed four on notes. The English list shows all five. Rule 4 ("Be careful with paths") is shown as its main tip, quoting variables.
- `--settings '{"disableAllHooks": true}'` and the ★ note (hook settings add up from many places) are left out.
