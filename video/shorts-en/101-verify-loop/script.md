# Short en-101 · Give it a test it can check itself against

- **Source page:** 23.4.1 [Give it a test it can check itself against](../../../docs-en/part6/ch23/verify-loop.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** Claude stops when the job looks done, so give it a pass-or-fail check, and ask for the command and its output as evidence.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Give Claude a test it can check / It stops when the job looks done | "What you'll learn" (first two points) |
| 2 | 9–21 | 4 strengths of check / 1. In the request / 2. /goal and a condition / 3. A Stop hook / 4. Someone else reviews / Stricter as you go down | "Four strengths of check" table ("from loosest to strictest") |
| 3 | 21–32 | When it reports: "All tests pass" (On its own, this tells you little) / Ask for evidence: The command and its output | "Always ask for evidence" |
| 4 | 32–42 | When asking for a review: Report gaps that affect correctness. Skip style. / Ask it to find problems, and it always finds some | "Tell reviewers to skip style" |
| 5 | 42–57 | Use it today: Write "done" as pass or fail (e.g. zero warnings from the link check) / Narrow the review: correctness only / Ask for the command and its output | "Use it today" 1, 2, 3 |

## Choices and notes
- `/goal` and `Stop` are written as on the page ("/goal plus a condition" became "/goal and a condition").
- The review prompt in scene 4 is the page's example ("report gaps that affect correctness, and skip style"), split into two short sentences.
- `/code-review`, `/verify`, and the Stop hook's block limit are left out to keep one idea.
- The page's "full output" is shortened to "output" in scene 3 so the line fits; the page's example prompt asks for "its full output."
