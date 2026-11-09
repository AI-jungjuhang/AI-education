# Check numbers and quotes

<p class="ep-meta"><span>Ch. 3 · 3.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Numbers, dates, and sentences inside quotation marks are where chatbots ==go wrong in ways that look right==.
    - Check numbers against the original, a rough estimate, and a calculator.
    - Find each quote word for word in the original.

## Spot the difference

Have you played "spot the difference" with two pictures that look almost the same? The big shapes match, so you have to stare to find the small changes.

A wrong number from a chatbot looks just like that. It looks reasonable, so it's easy to miss. As Chapter 1 showed, a chatbot picks a likely next word. So it can give you a number that is likely-looking, not checked.

!!! tip "In 10-year-old words"
    Treat numbers and quotes like a spot-the-difference game. Compare them one more time.

## Where it goes wrong most

| Kind | How it often goes wrong |
|---|---|
| Numbers | A close but different value, or a mixed-up unit (dollars and euros, millions and billions) |
| Dates | The year or day is off by a little |
| Names | Mixed up with a similar person or company |
| Quotes | The meaning is close, but the words aren't the original's |
| Math | A middle step in a long calculation is wrong |

## Three ways to check

**1. Match it with the original.** Find the number in the original source and see if it's the same. If you pasted in your own material, ask the chatbot to put the original sentence next to each number.

**2. Make a rough estimate.** First see if it's in the right ballpark. Say a chatbot tells you 20% of 330 million people. That should be around 66 million. If it says 6 million or 660 million, you know right away something is off.

**3. Use a calculator or a spreadsheet for math.** For exact math, a calculator is surer than a chatbot. Have the chatbot write the formula, and get the value from the tool. Some chatbots connect to tools and do math with them. (Part IV covers this.)

## Checking quotes

Words inside quotation marks seem to promise "these are the exact words." But a chatbot may remember the meaning roughly and put different words inside the quotes. Checking is simple.

1. Pick the key words from the quote.
2. Search for them in the original with Ctrl+F (Cmd+F on a Mac).
3. If you can't find them, the quote may not be exact. (A scanned page or odd spacing can also block a search, so glance at the page too.)

Anthropic's guide gives a tip for long documents. First have the chatbot pull out the relevant sentences word for word. Then have it answer based only on those sentences. The quotes stay in the answer as evidence, which makes checking easy.

!!! note "★ Going deeper"
    - One reason chatbots struggle with numbers: they read numbers as tokens too (Chapter 1). A long number gets chopped into chunks. With one public tokenizer we tried, `7006652` became `700` `665` `2`. That's not how people line up digits to do math. Karpathy's tokenizer lecture links some trouble with simple math to tokenization. Newer models do much better, but they can still slip on long calculations.
    - Anthropic's guide also describes "best-of-N" checking: send the same question several times and compare the answers. If a number changes each time, that's a reason for doubt. The next page covers this.

## Try it yourself

```text
What is 1234 × 5678? Show your work.
```

Check it on a calculator. (The answer is 7,006,652.) Did it get it right? If not, look through its steps to find where it went wrong. Then try this:

```text
Just write the formula for this calculation. I'll work out the value
on a calculator.
```

Which of the two ways makes you feel surer?

## Use it today

1. **Ask for "the source sentence too" with every number.** With the original sentence next to each number, checking is easy.
2. **Make rough estimates a habit.** If the size is off, you'll catch it right away.
3. **Leave math to tools.** Let the chatbot write the formula, and get the value from a calculator or spreadsheet.
4. **Find quoted sentences in the original.** If you can't find one, don't use it as a quote.
5. **Check units and the year a number refers to.** The same number can mean different things in different units or years.

## Common mix-ups

- "The more detailed the number, the more accurate it is." A number with lots of decimal places can still be wrong. Detail is not proof.
- "If it shows its work, the answer is right." The steps can look fine and still go wrong in the middle. Check the value on its own.
- "If it's in quotation marks, those are the exact words." You don't know until you check.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations), Claude Platform Docs. "Use direct quotes for factual grounding" and "Best-of-N verification." Read on 2026-11-09.
    - Andrej Karpathy, [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE), YouTube, 2024-02-20. In the intro, he links trouble with simple arithmetic to tokenization (checked through Rosetta's unofficial, auto-generated [transcript](https://rosetta.to/u/andrejkarpathy/let-s-build-the-gpt-tokenizer)).
    - OpenAI, [tiktoken](https://github.com/openai/tiktoken). We split `7006652` with the `o200k_base` tokenizer ourselves on 2026-11-09.
    - Our earlier page on tokens: [It reads text in small pieces called tokens](../ch01/tokens.md).

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The table of error types is our own summary. Other chatbots use other tokenizers and may split numbers differently.
