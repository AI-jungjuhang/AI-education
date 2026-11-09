# Short en-098 · How is handing off a job different?

- **Source page:** 23.2.2 [How is handing off a job different?](../../../docs-en/part6/ch23/prompt-agent.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** when you hand off a job, tell Claude what it can't learn from the files: where to look, what "done" looks like, and what not to do.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Handing off a job? Say what "done" is / It can't see what's only in your head | "What you'll learn"; "What AI can't see when you hand off a job" |
| 2 | 9–20 | Vague: Make a video script. / Clear: A 60-second script from tokens.md. Only what's in it. | "Vague and clear requests" table, row 1 |
| 3 | 20–32 | Three lines for a handoff / Where to look; What "done" looks like; What not to do | "A clear request has three parts" |
| 4 | 32–42 | When it's researching: Before you answer, open and read any file I mention. If you haven't opened something, say you don't know. / Fewer made-up answers about code | "When researching: read first, then answer" (the prompt is shown exactly) |
| 5 | 42–57 | Use it today: Hand over @file or a screenshot / Size matters? Give a number (e.g. help for 3 places) / Three lines: where, done, what not to do | "Use it today" 2, 3, 1 |

## Choices and notes
- The clear request in scene 2 is a short form of the page's example ("Write a 60-second shorts script based on docs-en/part1/ch01/tokens.md. Don't add anything that's not in the page..."). It is shown as a request, not as a command, so it is shortened; the full text is on the page.
- The researching prompt in scene 4 is copied word for word from the page.
- `be ambitious` and the pipe example (`cat error.log | claude -p ...`) are left out to keep one idea.
- The notes show only the three headings; bodies made them overlap.
