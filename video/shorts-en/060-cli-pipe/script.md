# Short en-060 · Hand it a file and give it a job in one line

- **Source page:** 16.4 [Hand it a file and give it a job in one line](../../../docs-en/part5/ch16/cli-pipe.md)
- **Format:** vertical 9:16, 30fps, about 26 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** `|` passes one command's output to the next, so `cat file | claude -p "..."` gives a file and a job in one line.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | A \| passes output along / Like a conveyor belt from a file to the AI | "What you'll learn"; "A conveyor belt" |
| 2 | 9–19 | Example: an error: `cat error.log \| claude -p "Explain in three lines why this error happened"` / It reads the log and answers in one go | The first code example, copied exactly |
| 3 | 19–30 | Add to it: `> review.md` → save to a file / `--output-format json` → for programs / `git diff main \| …` → just changes | The `>` example, "Setting the shape of the result", the `git diff main` line |
| 4 | 30–41 | A long error message: Copy it and paste it (X) / Pipe it in (O) | "Use it today": don't copy and paste long error messages, pipe them in |
| 5 | 41–56 | Use it today: Before piping, check for passwords / Same check twice? Save the command / Keep the result: add > review.md | "Use it today"; the `>` example |

## Choices and notes
- The Korean episode's title is the pipe-as-a-tube metaphor. The English title says what `|` does, and the conveyor belt is in the sticker.
- "Passwords or personal details" is shortened to "passwords" so the checklist line fits.
- `--json-schema` and the ★ note on `--allowedTools` are left out to keep one idea.
