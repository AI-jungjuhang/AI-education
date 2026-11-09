# Short en-059 · Chat mode and one-line mode

- **Source page:** 16.4 [Chat mode and one-line mode](../../../docs-en/part5/ch16/cli-modes.md)
- **Format:** vertical 9:16, 30fps, about 26 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** `claude -p "question"` gives one answer and ends, so it can run without a person.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | claude -p: one answer, done / No person needed, so it can run alone | "What you'll learn" (one-line mode gives an answer and ends; runs without a person) |
| 2 | 9–20 | Chat mode: claude (a restaurant: talk back and forth) / One-line mode: claude -p "question" (a vending machine: one button) | "A restaurant vs a vending machine" |
| 3 | 20–31 | Old chats: claude -c → the latest chat / claude -r "name" → by name / /resume → pick one in a chat | Command table (`-c`, `-r`) and the `/resume` line under it |
| 4 | 31–41 | Adding a folder: claude --add-dir ../another-folder / It can read and edit there. Only add folders you trust. | "Choosing the model and folders" |
| 5 | 41–56 | Use it today: One-off question? claude -p / Yesterday's work? claude -c / A named chat? claude -r "name" | "Use it today" |

## Choices and notes
- The Korean episode's title is the vending-machine metaphor. The English title states what `-p` does, and the metaphor moves to the small lines in scene 2.
- The page's `-r` example is `claude -r "name" "finish this"`; the screen shows the shorter form `claude -r "name"` that the page uses in "Use it today".
- `--model`, `--permission-mode` and the ★ note on `--bare` are left out to keep one idea.
