# Short en-078 · A super skill for making videos

- **Source page:** 18.2.2 [Hands-on: a super skill for making videos](../../../docs-en/part5/ch18/super-skill.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a super skill is writing that lists the order of tools you already built. Write in the order, where to stop, and where you decide.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | A super skill is a list of steps / It calls the tools you already made | "What you'll learn" second point; "In 10-year-old words" |
| 2 | 9–21 | The steps: 1. researcher → key points / 2. scriptwriter → scenes / 3. reviewer → check the page / 4. You decide the fixes | The four steps in `skills/episode/SKILL.md` |
| 3 | 21–33 | Always write: The order (who, when) / Where to stop (on problems) / Where you decide (before fixes) | "Use it today" first item; "stop and tell the user", "only after the user decides" |
| 4 | 33–43 | Call it: `/studio:episode docs-en/part1/ch01/tokens.md` / It makes files, so it runs only when you call it | "Use it"; `disable-model-invocation: true` explanation |
| 5 | 43–58 | Use it today: It handles the order and hand-offs / Test on one short page first / Save results where you can check them | "It doesn't change the helpers' instructions"; "Use it today" items 2 and 3 |

## Choices and notes
- The Korean opener ("not new magic, it calls the tools in order") is a "not X but Y" line. The English one states the point and keeps only "It calls the tools you already made".
- The command in scene 4 uses the English page's path `docs-en/part1/ch01/tokens.md` exactly.
- "It creates files and takes time" is shortened to "It makes files".
- The `--bare` and `references/` notes from "Going deeper" are left out.
