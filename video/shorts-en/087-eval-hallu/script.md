# Short en-087 · How do you measure hallucination?

- **Source page:** 21.1.2 [How do you measure hallucination?](../../../docs-en/part6/ch21/eval-hallu.md)
- **Format:** vertical 9:16, 30fps, about 26 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** to measure made-up answers, score "wrong" and "I don't know" differently. Then test it on your own questions.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Score "wrong" and "don't know" apart / If guessing pays, everyone guesses | "What you'll learn" (first point); "In 10-year-old words" |
| 2 | 9–20 | If a quiz scores Wrong: 0, Pass: 0 / You guess on everything. If it scores Wrong: −1, Pass: 0 / You pass when you don't know | "A quiz show's scoring" |
| 3 | 20–31 | Three famous tests / SimpleQA: short fact questions / TruthfulQA: questions aimed at myths / FActScore: long text, fact by fact | "Three well-known tests" and the comparison table |
| 4 | 31–41 | Test your own work: Ask 10 to 20 questions from your own field / Wrong answers are the dangerous number | "Use it today" items 1 and 2 |
| 5 | 41–56 | Use it today: Check long text fact by fact / Add "Say if unsure" and count the change / New model? Re-run the same questions | "Use it today" items 3, 4, 5 |

## Choices and notes
- The page's quiz example uses "+1 for right"; the split shows only the wrong/pass part, which is where the two scorings differ.
- "Well-known" became "famous" so the title doesn't break at the hyphen.
- "If you don't know, say so" is shortened to "Say if unsure" to fit one line.
- "Pick 5 key claims" from the page is left out; the checklist keeps "fact by fact."
- Test names are kept exact. Their numbers (817, 58%) are left out because the page says they belong to old models.
