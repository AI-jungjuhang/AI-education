# Attention: picking out what matters

<p class="ep-meta"><span>Ch. 11 · 11.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - **Attention** is a tool that lets each token in the text ==decide "Where should I look right now?" and pull in what it finds there==.
    - Each token asks a question (a query). Other tokens answer with a key. The token takes in information (a value) from the best matches.
    - Many of these run at once (several "heads"), so the model sees many kinds of connections.

## Highlighting while you read

When you're reading a long passage and you hit the word "it," you look back and ask, "What was 'it' again?" You don't treat every word as equally important. You highlight **what you need right now**.

Attention is a tool built so the model does exactly this.

!!! tip "In 10-year-old words"
    Attention lets every word decide "Where should I look right now?" It highlights what it needs and pulls that in.

## Example: a fluffy blue creature

3Blue1Brown's lesson uses this sentence: **"A fluffy blue creature roamed the verdant forest."**

At the start, "creature" has the plain location for "creature," with no context (Chapter 10). But in front of it are "fluffy" and "blue." Attention adds what those describing words carry to the location of "creature." That moves it to a location that stands for **"a fluffy, blue creature."**

## Query, key, and value

The lesson breaks the process into three parts.

1. **Query.** Imagine the noun "creature" asking, "Are there any describing words in front of me?" That question is also made into a list of numbers (a vector).
2. **Key.** The other tokens offer an answer, like "I'm a describing word," as their key. The better a key matches the query, the higher the score.
3. **Value.** The **content (value)** of high-scoring tokens is added to the asking token's location. The value from "fluffy" is added to "creature," and its location moves toward "fluffy creature."

The steps that make queries, keys, and values are also numbers set during training (Chapter 9). Nobody taught it "describing words change nouns." Rules like that grow because they help with next-word guessing.

## The score table: the attention pattern

When every token scores every other token, you get a **grid**. Each column is adjusted so it adds up to 1, with the same math (called softmax) that makes the score table from Chapter 1. The lesson calls this grid the **attention pattern**. Each column shows how much one token should pay attention to each of the others.

**Masking.** In models like GPT, later tokens are blocked from changing earlier ones. When it's practicing next-word guessing, it mustn't peek at the answer (what comes later).

## Many sets of eyes

Looking at only one kind of connection, like describing words and nouns, isn't enough. The model also needs to see who did what, when things happened, and what a word points to. So it runs **many attention steps at once**. Each one is called a **head**. According to the lesson, GPT-3 uses **96 attention heads** in each block. Each head has its own query, key, and value steps, so each one can track a different kind of connection.

!!! note "★ Going deeper"
    - The **transformer**, a design built around attention, comes from a 2017 paper called *Attention Is All You Need* by Ashish Vaswani and others. Earlier translation models were built from more complicated parts. The transformer dropped them and used attention alone. It translated better, was easier to run in parallel, and trained much faster. On English to French translation, it set a new record after training for 3.5 days on eight graphics chips (GPUs).
    - The attention described above is **self-attention**. There is also **cross-attention**, where queries and keys come from two different sources, like two languages in translation.
    - The lesson works out that one head has about 6.3 million parameters. GPT-3 has 96 layers, with 96 heads in each. Altogether, attention uses just under 58 billion parameters, about a third of GPT-3's total.

## Try it yourself

**Play the attention game.** Read this and answer the question.

```text
Maya lent Jordan a book. She was grateful.
```

Who is "she"? You probably said Jordan, even though "Jordan" could be anyone. Where did you put your highlighter? On "lent" and "grateful," probably. Now change one word:

```text
Maya lent Jordan a book. She was proud.
```

Now who is "she"? One changed word moved where you put the highlighter. That's what attention does.

## Use it today

1. **Use names instead of "it" or "this."** When it's clear what a word points to, the chatbot is less likely to look in the wrong place.
2. **Keep key conditions close to your question.** Conditions near the question are less likely to be missed.
3. **Cut stories that don't matter.** The more there is to look at, the more its attention is split.
4. **Label things that could get mixed up.** Names like "Document A" and "Document B" keep attention from getting confused (Chapter 6).
5. **If an answer is strange, ask "What does that refer to?"** You can guess where the chatbot was looking.

## Common mix-ups

- "AI reads a sentence one word at a time, from the start." Attention connects all the tokens to each other at once. (Later words still can't change earlier ones.)
- "Attention is the same as human attention." It's a comparison. In reality, it's a score table being computed.
- "It looks at only one thing at a time." Many heads look at different connections at the same time.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - 3Blue1Brown (Grant Sanderson), [Attention in transformers, step-by-step](https://www.3blue1brown.com/lessons/attention), Deep Learning Chapter 6, 2024-04-07. The fluffy blue creature example, query, key, and value, the attention pattern and softmax, masking, 96 heads, about 6.3 million parameters per head, cross-attention, and just under 58 billion attention parameters. Read on 2026-11-09.
    - Ashish Vaswani and others, [Attention Is All You Need](https://arxiv.org/abs/1706.03762), arXiv, 2017-06-12. Attention only, with no recurrence or convolutions, better translation, easier parallel training, and 3.5 days on eight GPUs come from the abstract.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The lesson's numbers are for GPT-3. The Maya and Jordan example and the highlighter comparison are ours.
