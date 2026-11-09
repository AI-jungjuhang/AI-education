# Read and imitate: pretraining

<p class="ep-meta"><span>Ch. 9 · 9.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A chatbot's first round of school is ==reading a gigantic amount of text and practicing guessing what comes next==.
    - The right answers are already in the text, so no person has to grade each guess.
    - A model that has only done this is not yet a helpful assistant. It's closer to a machine that continues text.

## A quiz where the answer is in the book

Picture a quiz where you cover up part of a sentence in a book and ask, "What word goes here?" The answer is already printed in the book, so you can grade yourself with no teacher.

That's a chatbot's first round of school. It takes huge amounts of text, hides what comes next, **guesses the next token**, and adjusts a little whenever it's wrong. It repeats this an enormous number of times. This is called **pretraining**.

!!! tip "In 10-year-old words"
    It reads tons of books and plays a "guess the next word" quiz by itself. The answers are in the books, so it doesn't need a teacher to grade it.

## One round of practice

1. **Gather text.** Lots of it: books, web pages, code.
2. **Cut it into tokens.** The pieces from Chapter 1.
3. **Show the start and have it guess the next token.**
4. **Compare its score table with the right answer.** If it gave the right answer a low score, it adjusts by a lot.
5. **Nudge the numbers inside the model (the parameters).** This is what "learning" means here.
6. **Back to step 1.** Repeat a huge number of times.

After all that practice, its score table gets good. It can pick a pretty likely next word, even for sentences it has never seen.

## What does it end up learning?

To guess the next word well, it helps to pick up a lot about the text: grammar, tone, facts, how stories flow, the rules of code. All of these soak in along the way. Nobody decided "let's teach it grammar." It grew out of the practice.

The GPT-3 paper (2020) reported something surprising. A model this big, with pretraining alone, could do many tasks like translation and answering questions when given just a few examples or simple instructions in plain text. GPT-3 had 175 billion parameters, 10 times more than any earlier language model of its kind. The tip from Chapter 2, "give an example and it will follow," comes from this ability.

## The limits of this stage

- **It also learns the wrong facts and prejudices in what it reads.** That's the root of the bias from Chapter 3.
- **Its reading stops at some date.** It doesn't know what happened after that. So recent news needs a search (Chapter 4, Part IV).
- **It's weak on things that rarely appear in text.** Rare facts and less common languages get more mistakes (hallucination, Chapter 1).
- **It isn't a smooth "assistant" yet.** It's a machine that continues text. Give it a question, and it may just keep writing what comes after the question. The next page shows how it becomes a helper.

!!! note "★ Going deeper"
    - More formally, the model compares the chances it gave each next token with the right answer. This gives a number called the **cross-entropy loss**. Training nudges the parameters a little at a time to make that number smaller, using a method called **gradient descent**. 3Blue1Brown's deep learning series explains this very well.
    - Research shows that when you scale up this "read and guess" training, the score table improves in a steady, predictable way. (See the page after next.)
    - The GPT-3 paper also pointed out datasets where the model still struggled, and problems that come from training on big piles of web text. It's good to read the weak spots, not just the strong ones.

## Try it yourself

**Play "human pretraining."** Show three friends or family members the same sentence and have each write the next word.

```text
"On a rainy day, I love a warm cup of ____"
```

Did everyone write the same word? Think of the most common answer as the top choice on the score table from Chapter 1. The more people disagree, the flatter the score table for that sentence. Pretraining is this game played across millions of books.

## Use it today

1. **Ask about recent news with a tool that can search.** It doesn't know what happened after its reading stopped.
2. **Be extra careful in fields with little text.** Local news and very specialized topics may have little training material.
3. **Ask "Up to what date do you know about?"** It may not answer exactly, but it gives you a rough idea.
4. **Keep giving examples.** That works well because it grew out of pretraining.
5. **Remember that wrong facts can come from what it read.** That's why the checking habits from Chapter 3 matter.

## Common mix-ups

- "AI memorized the whole internet." It learns patterns more than it memorizes. It can sometimes repeat bits word for word, but that's not how it usually works.
- "The more it reads, the fewer mistakes it makes." It reads wrong things too, so it can learn wrong things.
- "Once pretraining is done, it's a chatbot." Not yet. There's another stage that turns it into a helper.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Tom B. Brown and others, [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), arXiv, 2020-05-28. The 175 billion parameters, "10x more than any previous non-sparse language model," doing tasks from a few examples or instructions, and the noted struggles and web-training issues all come from the abstract.
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), 2024-04-01. Recommended for going deeper.
    - Andrej Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), YouTube, 2025-02-05. Chapters "pretraining data (internet)" (00:01:00), "tokenization" (00:07:47), and "neural network I/O" (00:14:27), and the point that a pretrained-only model is "a token autocomplete." Checked through Rosetta's unofficial, auto-generated [transcript and chapters](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt).

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the paper's abstract. The six-step description is our own summary of the general idea. Public details about how today's models are trained are limited, so we didn't go into specifics.
