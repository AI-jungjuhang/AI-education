# Short en-002 · It reads text in small pieces called tokens (part 1 of 2)

- **Source page:** 1.1.2 [It reads text in small pieces called tokens](../../../docs-en/part1/ch01/tokens.md)
- **Format:** vertical 9:16, 30fps, about 35 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a chatbot doesn't read letters. It reads text as blocks called tokens, and the "next word" is really the "next block."
- **Split:** this is part 1 (what a token is). Part 2 (en-003) covers why the number of tokens matters.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Chatbots don't read letters / So what do they read? | "What you'll learn": reads tokens, not letters or whole words |
| 2 | 9–17 | Blocks called tokens! / Text gets broken into small pieces | "Reading with building blocks" |
| 3 | 17–29 | How words split: french fries → french \| fries / un \| bel \| ievable, 3 pieces / Supercalifragilistic…, 10 pieces! | The tokenizer table (o200k_base, run by the page authors) |
| 4 | 29–40 | Both are a problem: one letter at a time is too long, whole words get stuck on new ones / So instead: medium-sized pieces | "Why medium-sized pieces?" |
| 5 | 40–51 | I love french fries → [I] [love] [french] [fries] → [40] [3047] [66017] [91469] | "The chatbot reads numbers, not letters" (real IDs from the page) |
| 6 | 51–62 | How the list is made ★: Start small / Join the pair seen together most / Repeat | "★ Going deeper": byte pair encoding |
| 7 | 62–71 | Chatbots read blocks / "Next word" really means "next block" | "In 10-year-old words" box |

## Choices and notes
- All splits and IDs are the real ones the page reports, so the footnotes say "One real tokenizer. Others split a bit differently" and "Real IDs from one tokenizer" instead of "made-up numbers."
- The page shows a space dot (`·`) in front of tokens. The video leaves the dots out to keep the bubbles short.
- "unbelievable" doesn't fit on a note at full size, so the note shows the split itself ("un | bel | ievable") with "3 pieces" under it.
- "Supercalifragilisticexpialidocious" is cut to "Supercali-fragilistic…" with its token count (10) from the page.
- The Korean version's first sticker question ("So what do they read?") is kept; the title line states the point directly.
