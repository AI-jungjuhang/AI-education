# Short en-039 · What one transformer layer looks like

- **Source page:** 11.1.2 [What one transformer layer looks like](../../../docs-en/part3/ch11/transformer-layer.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a transformer repeats two blocks (attention and MLP) many times, and the whole thing runs to pick one token.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Two blocks, many times / A transformer is like a conveyor belt | "What you'll learn" 1; "A factory conveyor belt" |
| 2 | 9–20 | Attention block: Tokens share info (Like group work) / MLP block: Each token thinks alone (Like solo note-taking) | "What the two blocks do" table |
| 3 | 20–32 | One token, step by step: 1. Split into tokens / 2. Add number lists / 3. Attention + MLP, repeat / 4. Score table at the end | "The big picture" steps 1 to 6 |
| 4 | 32–42 | So: The whole thing runs to pick one token / That's why long answers take time | "Use it today" 1; "The last vector's job" |
| 5 | 42–57 | Use it today: Many layers is not proof it's right / Answers differ from the draw at the end (More in Chapter 12) / Hard? It's fine to skip this part (Knowing about context is enough) | "Use it today" 2, 3, 4 |

## Choices and notes
- The page's six steps are folded into four: "Attention + MLP, repeat" covers steps 3 to 5.
- "Add number lists" is a short form of "Embedding: give each token a list of numbers".
- "Each token thinks alone" stands for the MLP "works on information inside one token" / "thinking it over".
- The Professor → Snape example and the matrix-multiplication note are left out to keep one idea.
