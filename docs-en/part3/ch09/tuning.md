# Learn from people: fine-tuning and feedback

<p class="ep-meta"><span>Ch. 9 · 9.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A pretrained model knows a lot, but it still has to learn ==how to answer questions helpfully==.
    - People show it good answers and rank its answers, and that shapes it into a helper.
    - Because it learns from people's ratings, it can lean the way those ratings lean.

## A well-read student practices for an interview

Imagine a student who has read a huge number of books. They know a lot. But in an interview, when asked a question, they just ramble on as if continuing a story. Then a coach has them practice: "Answer the question, short and clear." Now they do much better.

A pretrained model is that student. It knows a lot, but it has to learn separately **how to answer a question helpfully**.

!!! tip "In 10-year-old words"
    A teacher shows the well-read student good answers and says "this answer is better," until the student becomes a good helper.

## How InstructGPT did it

In 2022, OpenAI researchers published the InstructGPT paper. They pointed out that making a model bigger doesn't, by itself, make it better at doing what users want. A big model can still say things that are **untrue, harmful, or simply unhelpful**. So they used feedback from people to shape it.

1. **Learn from good answers (supervised fine-tuning).** People (called labelers) write the answers they'd want for a set of prompts. The model learns by imitating them.
2. **Rank answers.** The model gives several answers to the same prompt, and people rank them from best to worst.
3. **Learn from the rankings (reinforcement learning from human feedback, or RLHF).** The model is tuned again, so the kinds of answers people preferred come up more.

The result was striking. In people's ratings, answers from the **1.3-billion-parameter InstructGPT** were preferred over answers from the **175-billion-parameter GPT-3**, even though it was about 100 times smaller. It was also more truthful and gave fewer harmful outputs. Still, the researchers admitted it made simple mistakes.

## How this connects to the chatbots you use

- **Why instructions work:** It practiced following instructions. That's why the asking tips in Chapter 2 work.
- **The friendly tone and the way it says no:** It was shaped toward answers people rated well.
- **Why "I don't know" is hard for it:** If people rate a confident guess higher than "I don't know," it can lean toward guessing (hallucination in Chapter 1, agreeing with you in Chapter 3).

## Limits

Learning from people's ratings means **learning people's tastes and blind spots too**.

- If people prefer answers that agree with them, the model agrees more (the study in Chapter 3).
- If people prefer long, confident answers, you get more long, confident answers.
- The culture and values of the raters soak into the model.

So a polite, confident tone doesn't mean an answer is right.

!!! note "★ Going deeper"
    - This idea was studied before InstructGPT. A 2019 paper by Daniel Ziegler and others, *Fine-Tuning Language Models from Human Preferences*, used people's comparisons to shape a language model. It also noticed a catch: on summaries, the model learned to copy whole sentences, and the raters liked it. The authors suspected it was taking advantage of the simple rules of thumb the raters used.
    - A common way to do step 3: first train a separate "scoring model" (a **reward model**) on people's rankings. Then use reinforcement learning to push the chatbot toward higher scores. Researchers are also studying ways to have AI help with the rating (Chapter 20).
    - For going deeper, Karpathy's "Deep Dive" lecture has chapters on "post-training data (conversations)" (01:01:06) and "reinforcement learning from human feedback (RLHF)" (02:48:26).

## Try it yourself

Ask the same thing in two ways.

```text
1. How do I keep potatoes fresh for a long time?
```

```text
2. Continue the text that comes after this sentence: "How do I keep potatoes
   fresh for a long time?" Don't answer the question. Write as if this
   sentence is part of a longer piece of writing.
```

Answer 1 will likely sound like a helper. Answer 2 may look more like text being continued. The difference is a trace of the "learned to follow instructions" stage. (Results can vary by service.)

## Use it today

1. **Give specific instructions.** It was trained to follow instructions, so specific ones work well.
2. **Don't treat a polite tone as proof.** The tone was polished; the facts are a separate matter.
3. **Instead of asking whether you're right, ask for reasons for and against.** That helps with its habit of agreeing (Chapter 3).
4. **Find out what the thumbs-up and thumbs-down buttons do.** Services differ on whether and how ratings are used. Check the settings and help pages.
5. **Keep saying "If you don't know, say so."** That one line pushes back on the habit of guessing.

## Common mix-ups

- "People taught the AI every answer, one by one." It does pretraining on its own. People supply some good answers and some rankings.
- "Bigger models follow instructions better." In the paper, a tuned model 100 times smaller was preferred.
- "It was tuned with human feedback, so it's safe and accurate." Mistakes and bias went down, but they're still there.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Long Ouyang and others, [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155), arXiv, 2022-03-04. The three steps, 1.3B preferred over 175B, better truthfulness and less harmful output, and "still makes simple mistakes" come from the abstract.
    - Daniel M. Ziegler and others, [Fine-Tuning Language Models from Human Preferences](https://arxiv.org/abs/1909.08593), arXiv, 2019-09-18. We summarized the abstract.
    - Mrinank Sharma and others, [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548), arXiv, 2023-10-20.
    - Andrej Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), YouTube, 2025-02-05. Chapter titles checked through Rosetta's unofficial [chapter list](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt).

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstracts. The "reward model, then reinforcement learning" description is a widely known summary, not a sentence from these abstracts. Public details on how today's models are tuned are limited, so we didn't go into specifics. Results of "Try it yourself" vary by service.
