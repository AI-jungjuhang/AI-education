# How a long answer keeps going

<p class="ep-meta"><span>Ch. 12 · 12.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A long answer is ==draw one token, add it to the input, and run the math again, over and over==.
    - Once a word is drawn, it can't be taken back, and it affects every choice after it.
    - For long writing, get an outline first and write it in parts. The flow drifts less.

## A relay race

In a relay race, one runner runs and then hands the baton to the next. If the first runner stumbles, the next one has to start from wherever things stand. Nobody gets to run that leg over again.

That's how a long answer gets made. **Each time a token is drawn, the baton (everything written so far) passes along**, and what's already written can't change.

!!! tip "In 10-year-old words"
    A long answer is a relay race. A leg that's been run can't be redone, and the next leg starts from there.

## The life of one token

3Blue1Brown's lesson describes a simple way to make long text with a prediction model:

1. **Give it some starting text.**
2. **Predict the next word.** (Make the score table.)
3. **Draw one at random from the chances.** (The last two pages.)
4. **Add it to the end of the text.**
5. **Use the whole text, new word included, as input, and predict again.**

This **predict-and-draw loop** is what happens when you chat with ChatGPT. That's why the words seem to come out one at a time, and why text appears bit by bit on the screen.

## What makes the relay tricky

| Feature | Result |
|---|---|
| A drawn word can't be taken back | A slip early on carries through to the end |
| Earlier text becomes later input | Phrases used early tend to repeat later |
| The whole thing is recalculated every time | Long answers take time and cost more |
| On the surface, it adds one token at a time (inside, it may look ahead) | The longer the piece, the more the flow can drift |

That doesn't mean the model never plans. Research suggests some of its inner math looks ahead (see "Going deeper"). But on the surface, a token that's been drawn can't be undone.

!!! note "★ Going deeper"
    - Anthropic's interpretability research reported a surprise with poems. The researchers expected the model not to look ahead, but they found it **planning in advance**. Before writing a line, it picked a rhyme word for the end and then wrote toward it. So even a one-token-at-a-time design can do math that considers what comes later. Chapter 19 goes into this.
    - Having it **write out its thinking in the middle** before answering often makes answers more accurate, because that text gives later choices something to build on ("think step by step," Chapter 7). Today's reasoning models are trained to think at length before answering (Chapter 20).
    - In long writing, what's already written takes up room in the context window and affects later choices (Chapter 11). The longer the text so far, the longer the input, and the more math each new token needs.

## Try it yourself

Ask for a long piece in two ways.

```text
1. Write a 300-word post introducing our town library.
```

```text
2. I want to write a 300-word post introducing our town library.
   First, suggest an outline of 5 paragraphs (one line each). Don't write it yet.
   (I'll fix the outline, and then we'll write it paragraph by paragraph.)
```

Does the first one drift from its topic or repeat itself near the end? If you get an outline with the second one and write a paragraph at a time, how does the flow change?

## Use it today

1. **Get an outline first for long writing.** If the direction is wrong, you can fix it early (Chapter 5).
2. **Have it write paragraph by paragraph.** The shorter each stretch, the less it drifts.
3. **Check more closely toward the end.** Contradictions with earlier parts and repetition show up there.
4. **Set length with a number, but treat it as rough.** "Under 300 words" may not be exact (tokens, Chapter 1).
5. **If an answer stops in the middle, say "Keep going."** It often hit a length limit (Chapter 11).

## Common mix-ups

- "AI plans the whole piece and then writes it." On the surface, it draws one token at a time and keeps going. Inside, some math may look ahead.
- "A long answer means it tried hard." Length and accuracy are separate.
- "If I ask it to fix one part, the rest will adjust to match." Check that the whole thing still fits together.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), 2024-04-01. Predicting from starting text, drawing at random, adding it, and running again, and why words seem to come out one at a time. Read on 2026-11-09.
    - Anthropic, [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model), 2025-03-27. The poem-planning finding. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** "Repetition grows toward the end" is a common pattern, not something we found measured. The relay comparison and the feature table are ours.
