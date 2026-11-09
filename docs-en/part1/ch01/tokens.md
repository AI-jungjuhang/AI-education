# It reads text in small pieces called tokens

<p class="ep-meta"><span>Ch. 1 · 1.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A chatbot reads text as small pieces called ==tokens==, not as letters or whole words.
    - The number of tokens affects its limits, its speed, its cost, and some of its mistakes.
    - The same message can take very different numbers of tokens in different languages.

## Reading with building blocks

When you build a house out of toy bricks, some parts take one big brick. Other parts need lots of tiny ones.

A chatbot reads text the same way. It breaks the text into blocks, and each block is a token. Common words usually fit in one big block. Rare or made-up words get split into several small blocks.

Here is how one real tokenizer splits some words. (This is OpenAI's public tokenizer, `o200k_base`. We ran it ourselves. Other chatbots use their own tokenizers and split text a bit differently.)

| Text | Tokens |
|---|---|
| I love french fries | `I` `·love` `·french` `·fries` (4) |
| unbelievable | `un` `bel` `ievable` (3) |
| Supercalifragilisticexpialidocious | `Super` `cal` `if` `rag` `il` `istic` `exp` `ial` `id` `ocious` (10) |

The `·` dot stands for a space. Spaces often ride along at the front of a token.

!!! tip "In 10-year-old words"
    A chatbot doesn't read letters. It reads building blocks called tokens. The "next word" from the last page is really the "next block."

## Why medium-sized pieces?

Reading one letter at a time would make every text very long. Giving every whole word its own slot has the opposite problem. The list of words would never end, and the chatbot would be stuck on any word it had never seen.

So the makers build a list of medium-sized pieces. It holds tens of thousands to a few hundred thousand pieces. Any text can be built by joining pieces from that list. A brand-new word can still be read, because it can be split into pieces the chatbot already knows.

## The chatbot reads numbers, not letters

Every piece on the list has an ID number. From the chatbot's side, your message looks like this:

```text
What you type:    I love french fries
As tokens:        [I] [ love] [ french] [ fries]
What it gets:     [40] [3047] [66017] [91469]
```

These are the real IDs from the same tokenizer. Next, the chatbot works out which ID should come after these. The choices on the score table from the last page are these pieces.

## How tokens affect you

- **Limits.** How much a chatbot can read and keep in mind at once is counted in tokens, not letters.
- **Speed and cost.** Many services measure use and set prices by the token. Text with more tokens can be slower and cost more.
- **Counting letters is hard for it.** It sees pieces, not single letters. So a question like "How many r's are in strawberry?" can trip it up. In our test, ` strawberry` with a space in front is one single token. Newer models do better, but they still slip.
- **Languages differ.** One study translated the same texts into many languages. Some languages needed up to 15 times more tokens than others for the same meaning. English usually takes fewer tokens than most languages, because the makers trained their tokenizers on lots of English.

!!! note "★ Going deeper"
    - A common way to build the list of pieces is **byte pair encoding (BPE)**. Start with very small units. Find the pair that shows up side by side most often, and join it into one new piece. Repeat many times. The joined pieces fill up the list.
    - Many tokenizers start from bytes, the small units computers use to store text. That way they can read any character, even emoji. The cost is that a character stored as several bytes, like most Chinese, Japanese, or Korean characters, can turn into more than one token.
    - Spaces and capital letters matter. `strawberry` with no space was 3 tokens in our test (`st` `raw` `berry`), but ` strawberry` with a space was 1.
    - Inside the model, each token ID turns into a long list of numbers called a vector. Part III covers that.

## Try it yourself

Ask a chatbot this:

```text
How many letters are in "french fry basket"? Don't count the spaces.
```

Then ask again, worded like this:

```text
Write "french fry basket" one letter at a time, each on its own line.
Then count the letters you wrote. Don't count the spaces.
```

Did you get the same answer both times? Spelling it out first often helps. Can you explain why, using what you know about tokens?

## Use it today

1. **Don't trust a chatbot alone for exact counts.** For letter counts, word counts, and spelling checks, a counting tool is more reliable. The word count in your word processor is one. If a chatbot gives you a number, check it.
2. **If the chatbot must count, make it spell things out.** Ask it to "write each letter on its own line, then count." That turns tokens back into single letters, and it often cuts down on mistakes.
3. **Split long documents, and repeat key rules at the end.** It can only read so many tokens at once. In very long text, the early parts can get blurry.

## Common mix-ups

- "A token is one word." A token can be smaller or bigger than a word. Part of a word, a space, or a punctuation mark can be a token.
- "A token is one letter." Sometimes a token holds many letters. Sometimes one character takes several tokens.
- "Counting letters is easy, so chatbots must be good at it." What is easy for people is not always easy for a machine that reads pieces.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Andrej Karpathy, [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE), YouTube, 2024-02-20. Chapters "Tokenization by example in a Web UI" (00:05:50) and "Byte Pair Encoding (BPE) algorithm walkthrough" (00:23:50). In the intro he links trouble with spelling, simple math, and non-English languages to tokenization.
    - Andrej Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), YouTube, 2025-02-05. Chapter "tokenization revisited: models struggle with spelling" (02:01:11).
    - Aleksandar Petrov and others, [Language Model Tokenizers Introduce Unfairness Between Languages](https://arxiv.org/abs/2305.15425), arXiv, 2023-05-17. The "up to 15 times" difference comes from this paper's summary.
    - OpenAI, [tiktoken](https://github.com/openai/tiktoken) (MIT license). We ran the `o200k_base` tokenizer ourselves on 2026-11-09 to get every token split and ID on this page.
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), 2024-04-01.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** Token splits depend on the tokenizer. Claude, Gemini, and others use different ones, so their splits and counts will differ from our table. We could not watch the videos from our work environment. We matched the content against an unofficial, auto-generated transcript on the third-party site Rosetta ([tokenizer](https://rosetta.to/u/andrejkarpathy/let-s-build-the-gpt-tokenizer), [deep dive](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt)), which may contain errors.
