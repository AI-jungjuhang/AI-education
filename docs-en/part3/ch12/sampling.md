# Sampling: how it draws

<p class="ep-meta"><span>Ch. 12 · 12.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - **How the next word gets drawn** from the score table (called decoding or sampling) can change the quality of writing a lot, even with the same model.
    - Always taking the top choice tends to make ==bland, repetitive writing==.
    - Methods like "nucleus sampling" (top-p) cut out the weird long-shot choices first, then draw from the rest.

## The friend who always orders the same thing

Imagine a friend who always orders the most popular dish at every restaurant. It never goes wrong, but they eat the same thing every time, which gets boring. On the other hand, if you close your eyes and point at the menu, you'll sometimes end up with something really strange.

Drawing the next word from the score table swings between **safe and varied** in the same way.

!!! tip "In 10-year-old words"
    Always picking number one gets boring. Picking anything at all gets weird. So it picks evenly from just the good choices.

## Three ways to draw

| Method | How it draws | Result |
|---|---|---|
| Always the top choice | Always the most likely token | Steady, but bland and easily repetitive |
| Draw by the odds | Roll dice weighted by the score table | Varied, but odd long shots get picked now and then |
| Trim, then draw | First drop the weird long shots, then draw by the odds from what's left | Varied, and less strange |

## What research found

A 2019 paper by Ari Holtzman and others, *The Curious Case of Neural Text Degeneration*, found a puzzle.

- Models are **trained to make likely text more likely**, and that makes them good at many language tasks. But when you make them **write the single most likely text**, it comes out **bland and strangely repetitive**.
- Human writing and machine writing showed surprising differences in how their word choices are spread out.
- With the exact same model, **the drawing method alone can change the quality of writing a lot**.

The paper proposed **nucleus sampling** as a fix. It draws only from the "core" of the chances and **cuts off the unreliable tail**, the choices with very low chances. The authors reported that this keeps variety while staying smooth and on track, so the writing looks more like human writing. A setting called "top-p" that you may see in some tools comes from this family of methods. (That's a general note.)

## How this connects to your questions

- When a chatbot **keeps repeating the same phrases**, this may be part of the reason.
- The same question gets **slightly different answers** because of the draw (Chapter 1).
- Services often **set the drawing method and temperature themselves**. You usually can't change them.

!!! note "★ Going deeper"
    - Common ways to trim choices include **top-k**, which keeps only the k most likely choices, and **top-p (nucleus sampling)**, which keeps choices until their chances add up to p. The key idea in the paper is that the "nucleus" isn't a fixed number of choices. It grows or shrinks with the shape of the chances. (We didn't confirm the definition of top-k in this page's sources.)
    - The paper shows something interesting: "most likely" is not the same as "good." Writing we like is often **not the single most likely text**. That ties back to the last page: always taking the top choice is bland.
    - This is a 2019 study. Services differ in how much they share about the exact methods they use today.

## Try it yourself

Ask a chatbot:

```text
Write one paragraph of a story that starts with "When I woke up this morning."
```

Get three of them. Do the sentence patterns or words repeat? Then ask:

```text
Same opening, but this time go in a completely different direction
from the first three. Don't reuse any of the same phrases.
```

Compare what changed. You'll see the effect of asking for more varied choices in your question.

## Use it today

1. **If answers are bland or repetitive, ask for "something different from before."** You can't change the drawing method, but you can change your question.
2. **Get several and pick.** "Give me 5 very different versions" is the surest way.
3. **If a phrase keeps coming back, ban it.** For example: "Don't use the word 'innovative.'"
4. **If an answer is odd, try again.** A strange choice may have been drawn just once.
5. **Don't leave jobs that need exact answers to the draw.** They need a checking step.

## Common mix-ups

- "AI always picks the single most likely word." Usually it draws by the odds. Always taking the top choice actually makes writing bland.
- "Drawing more variety lowers quality." The paper found that trimming first gives you both variety and quality.
- "I can't change the settings, so there's nothing I can do." You can change your question to steer variety and repetition.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Ari Holtzman and others, [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751), arXiv, 2019-04-22. That decoding for the most likely text is bland and repetitive, that decoding alone can change quality a lot, and the nucleus sampling proposal come from the abstract.
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), 2024-04-01. Sampling from the distribution and adding to the text.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The definitions of top-k and top-p, and settings in today's services, are general explanations we didn't confirm in these sources. We read only the abstract. The restaurant comparison and the three-method table are ours.
