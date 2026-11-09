# The context window: how much it sees at once

<p class="ep-meta"><span>Ch. 11 · 11.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - There's a limit to how much text a chatbot can see at once. That range is its **context window**.
    - Your whole chat and its new answer all have to fit inside, and ==the longer it gets, the more accuracy can drop==.
    - Even as windows grow, choosing what goes in still matters.

## The size of a desk

How many books and notebooks you can spread out depends on the size of your desk. A small desk holds a few. A big desk holds many. But if the desk is a total mess, even a big one makes it hard to find what you need.

The context window is the chatbot's **desk**. Everything it can look at while writing an answer has to be on that desk.

!!! tip "In 10-year-old words"
    The context window is the chatbot's desk. It can only see what's on the desk, and if the desk is too messy, it gets confused.

## Why is there a limit?

3Blue1Brown's lesson explains that a transformer can only look at **a fixed number of vectors at a time**. That number is its **context size**. GPT-3 was trained with a context size of 2,048 tokens. The lesson says this limit is why, in long chats with early versions of ChatGPT, the bot seemed to lose the thread of the conversation.

There's a deeper reason too. The attention pattern from the earlier page is a **grid** where every token looks at every token. So its size is the **context size squared**. Double the tokens, and there are four times as many cells to work out. The lesson says this is why growing the context size isn't easy, and that researchers have come up with many changes to the design to make bigger contexts possible.

## How big is it now?

It's grown a lot since 2,048 tokens in 2020. Anthropic's docs (read on 2026-11-09) say many current Claude models have a context window of **up to 1 million tokens**, and some others have 200,000. The docs describe the context window as **the whole conversation so far plus the new answer**. Each turn, the full earlier conversation and your new message go in as input, and the answer piles up after them.

These numbers depend on the model, the service, and your plan. Check your own service's help pages for its limits.

## Bigger isn't automatically better

Anthropic's docs make this point clearly. A bigger window lets a model handle longer, more complicated input, **but more context isn't automatically better**. As the number of tokens grows, accuracy and recall drop. They call this **context rot**. So choosing what goes into the window matters as much as how much fits.

The study from Chapter 6, "Lost in the Middle," points the same way. Models did much worse when the key information sat in the middle of a long input (with the models of 2023).

!!! note "★ Going deeper"
    - When the window fills up, some services **drop or summarize older parts** to make room. Anthropic's docs present server-side compaction, where earlier parts get summarized automatically, as the main way to manage long conversations and agent tasks. Each service does this its own way.
    - Every token in the context also affects cost and speed (pricing by the token, Chapter 4). So cutting out what isn't needed helps with accuracy and with cost.
    - What a model saw during training (its knowledge) is different from what's in its context window (its working memory). It can refer to text in the context exactly, but it remembers training text only fuzzily. That's why pasting in your own material cuts down on made-up answers (Chapter 1).

## Try it yourself

**Play "the desk game."** In a single chat, do this:

1. At the very start, write: "My secret code is potato-1019. Remember it."
2. Ask 10 to 20 unrelated questions. (Questions with long answers work best.)
3. At the end, ask: "What was my secret code?"

Did it remember? Some services remember well even in very long chats, and some lose it. Either way, you get a feel for how the "stuff on the desk" is handled. (Results differ by service.)

## Use it today

1. **Put key conditions at the start and the end.** The middle of a long input is easy to miss (Chapter 6).
2. **When a chat gets long, summarize it and move to a new chat.** You learned this in Chapter 2.
3. **Paste in only the parts you need.** Putting in more doesn't mean it understands more.
4. **Don't fill the window just because it's big.** Organized input is more accurate and faster.
5. **Check your service's limits.** Knowing them helps you understand "Why did it forget?"

## Common mix-ups

- "A chatbot always remembers the whole chat perfectly." Even inside the window, it can miss things as the chat grows. And it can't see anything outside the window at all.
- "With a 1-million-token window, ten books is no problem." Fitting in and being used well are not the same.
- "It still knows everything when I open a new chat." A new chat starts with an empty desk (except for services with a separate memory feature).

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), Deep Learning Chapter 5, 2024-04-01. GPT-3's context size of 2,048 tokens, and early ChatGPT seeming to lose the thread. Read on 2026-11-09.
    - 3Blue1Brown, [Attention in transformers, step-by-step](https://www.3blue1brown.com/lessons/attention), Deep Learning Chapter 6, 2024-04-07. The attention pattern's size being the square of the context size, and design changes for larger contexts.
    - Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), Claude Platform Docs. What the context window holds, up to 1 million tokens (200,000 for some models), context rot, and server-side compaction. Read on 2026-11-09.
    - Nelson F. Liu and others, [Lost in the Middle](https://arxiv.org/abs/2307.03172), arXiv, 2023-07-06.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** Context sizes for each model change often. These numbers are right only as of the date we read the docs. Results of "Try it yourself" differ by service. The desk comparison is ours.
