# What one transformer layer looks like

<p class="ep-meta"><span>Ch. 11 · 11.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A transformer is built from ==an attention block and another kind of block (an MLP), taking turns, repeated many times==.
    - At the very end, the last vector becomes the score table for the next token.
    - Because there are so many layers, it's called "deep" learning.

## A factory conveyor belt

Picture a factory. A product rides a conveyor belt. The first machine shapes it, the second paints it, then it gets shaped and painted again and again. At the end, out comes the finished product.

A transformer is similar. Each token's list of numbers passes through **the same kind of workstation** many times, and it carries a richer meaning each time.

!!! tip "In 10-year-old words"
    It's a conveyor belt where the lists of numbers take turns "gathering info" (attention) and "thinking it over" (MLP), many times, getting smarter each time.

## The big picture

Here's the overall flow that 3Blue1Brown's lesson shows.

1. **Split into tokens** (Chapter 1).
2. **Embedding:** give each token a list of numbers (Chapter 10).
3. **Attention block:** tokens share information with each other (the previous page).
4. **MLP block (multilayer perceptron):** each list of numbers gets polished on its own. The lesson compares this to asking each vector a long list of questions, then updating it based on the answers.
5. **Repeat steps 3 and 4 many times.** Attention, MLP, attention, MLP, and so on. Having this many layers is the "deep" in deep learning.
6. **Make the score table from the last vector:** all the information ends up in the last vector. A final step turns it into chances for every possible next piece (the score table from Chapter 1).

## What the two blocks do

| Block | What it does | Comparison |
|---|---|---|
| Attention | Shares information **between tokens** | Group work: talking with others to gather information |
| MLP | Works on information **inside one token** | Solo note-taking: thinking over what you gathered |

Almost all of this math is **matrix multiplication**, which is big blocks of multiplying and adding numbers. The lesson calls a transformer a giant pile of matrix multiplications. It says understanding how to read those matrices is key to understanding the model.

## The last vector's job

After all the layers, the **list of numbers for the last token** must hold everything needed to predict the next word. The lesson gives an example. Say the text is about Harry Potter, and the last word is "Professor." To predict what comes next, the last vector needs to carry "this is a Harry Potter story, and the last word is Professor." That makes "Snape" a likely next word.

From that last vector, the model works out a score for every token. Turning those scores into chances gives you the **score table** from Chapter 1. Once it draws a token, it adds that token to the input and runs the whole thing again.

!!! note "★ Going deeper"
    - At each layer, the new information is **added on** to what was already there, instead of replacing it. This is called a **residual connection**, and it helps deep models train well. (We didn't confirm the lesson's exact explanation of this, so treat it as a general note.)
    - How MLP blocks might store facts is the topic of the next lesson in the series, *How might LLMs store facts* (Deep Learning Chapter 7).
    - The 2017 *Attention Is All You Need* design had two halves for translation, an encoder and a decoder. Models like GPT are generally described as closer to the decoder half. The exact names of the parts differ from model to model.

## Try it yourself

**Draw the factory.** On a sheet of paper, draw this:

```text
[text] → [tokens] → [lists of numbers] → [attention] → [MLP] → [attention] → [MLP] → ... → [score table] → [next token]
```

Now label each step with the page you learned it on: 1.1.2 tokens, Chapter 10 embeddings, Chapter 11 attention, 1.1.1 the next word. Any gaps? Chapter 12 covers the last arrow: drawing from the score table.

## Use it today

1. **Remember "one token at a time."** The whole structure runs once to pick a single token. That's why long answers take time.
2. **Many layers doesn't mean it's always right.** A complicated design is not proof of accuracy.
3. **Know where answers differ.** The same question goes through the same math. The answers differ because of the draw at the end (Chapter 12).
4. **It's fine to skip the structure if it feels hard.** To ask good questions, knowing about attention and context is enough.
5. **Want more? Watch the lessons.** We recommend 3Blue1Brown's deep learning series.

## Common mix-ups

- "AI is built just like a human brain." That's a comparison, not a fact. They are not the same.
- "More layers always means smarter." Size, data, and tuning all matter together (Chapter 9).
- "Each layer does one clear human-like job." What each layer does is still being studied (Chapter 19).

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), Deep Learning Chapter 5, 2024-04-01. Attention and MLP blocks repeating, the "long list of questions" comparison, deep layers, the probability distribution from the last vector, the pile of matrix multiplications, and the "Professor → Snape" example. Read on 2026-11-09.
    - 3Blue1Brown, [How might LLMs store facts](https://www.3blue1brown.com/lessons/mlp), Deep Learning Chapter 7. We checked only the title.
    - Ashish Vaswani and others, [Attention Is All You Need](https://arxiv.org/abs/1706.03762), arXiv, 2017-06-12.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We didn't check sources for residual connections or for how GPT relates to the encoder and decoder. Those are general explanations. The factory and group-work comparisons are ours.
