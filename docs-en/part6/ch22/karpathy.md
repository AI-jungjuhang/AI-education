# How Andrej Karpathy sees it ★

<p class="ep-meta"><span>Ch. 22 · 22.1 · Deeper</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! warning "How to read this page"
    This page shares **views and predictions from one person's writing**. They're not facts. Most of what follows comes from posts on his own blog. **We couldn't pull YouTube transcripts directly, so we checked parts of his video lectures only against unofficial, auto-generated transcripts and chapters on a third-party site (Rosetta), which may contain errors. Those notes are kept separate, in section 5.** We kept quotes to a minimum and put the rest in our own words.

!!! abstract "What you'll learn on this page"
    - In 2022, Karpathy guessed what AI would look like in 2055: ==much the same in its basic shape, just far bigger==.
    - He saw people moving away from building a new model for each job. Instead, they start from one big model and tweak it.
    - In 2019, he warned that training these models looks easy, but ==it isn't plug and play==

## Whose writing, and which?

Andrej Karpathy, whose video lectures have come up since Chapter 1, writes posts on his blog (karpathy.github.io). We read these:

| Post | Date | About |
|---|---|---|
| *Deep Neural Nets: 33 years ago and 33 years from now* | 2022-03-14 | Rebuilds a 1989 paper and predicts 33 years ahead |
| *A Recipe for Training Neural Networks* | 2019-04-25 | A process for avoiding mistakes when training neural networks |
| *microgpt* | 2026-02-12 | We checked only its one-line description in the blog list |

## The 2022 post: 33 years back, 33 years ahead

Karpathy rebuilt a 1989 paper by Yann LeCun and others on reading handwritten zip codes. To his knowledge, he wrote, it was the earliest real-world use of a neural network trained end to end with backpropagation. Only the data (7,291 handwritten digits) and the network (just 1,000 neurons) were small. The paper was surprisingly modern, so he used it as a case study of how deep learning has progressed.

At the end, he makes predictions about **2055**. Here they are in our own words:

- **Same at a high level, but far bigger.** Neural networks in 2055 will look much like 2022's at the big-picture level, only bigger. People then will see today's data and models as a joke. Both, he says, will be about **10 million times** larger.
- **Today's best model in a minute.** In 2055, you could train a 2022 state-of-the-art model on a personal computer in about a minute.
- **Training from scratch is going out of style.** Building a network from scratch for each task is quickly becoming outdated, thanks to **fine-tuning** and **foundation models** like GPT. A few institutions with huge computing power train the foundation models. Most uses then just lightly adjust part of one, write prompts, or distill it into a small special-purpose model.
- **The most extreme prediction:** if this trend continues and grows, people won't want to train neural networks at all. In 2055, you'll ask a "megabrain" 10 million times bigger to do things, by **speaking (or thinking) in English**, and if you ask nicely, it will. He ends roughly with: yes, you could train a neural net too, but why would you?

## The 2019 post: the illusion of easy

*A Recipe for Training Neural Networks* starts by saying that neural network training is a **"leaky abstraction"**. Libraries show off "30-line miracle snippets" that give the false impression it's plug and play. Unlike tidy interfaces in regular software, neural networks stop being an off-the-shelf tool the moment you step slightly away from the standard case. So instead of listing mistakes, the post lays out **a process for avoiding them, or fixing them fast**.

## Connecting to earlier chapters

| What Karpathy says | In this book |
|---|---|
| Foundation models plus light tuning and prompts are the main path | Chapter 2 asking tips; Chapter 9 pretraining and fine-tuning |
| You'll give instructions in English (plain language) | Chapters 2 and 15 |
| Models will get much bigger | Chapter 9 parameters; Chapter 20 scaling and the debate |
| It looks easy, but it's not plug and play | Chapter 8 checks before using AI at work; Chapter 21 testing |

## From his video lectures (checked against unofficial transcripts)

The three videos used in earlier chapters have transcripts and chapter lists on a third-party site, [Rosetta](https://rosetta.to/u/andrejkarpathy/1hr-talk-intro-to-large-language-models). The site says they're auto-generated and may have errors. Below is our **paraphrase** of what we read there. (To know exactly what he said, watch the videos.)

| Video | What we found (paraphrased) | In this book |
|---|---|---|
| [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) ([transcript](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt)) | A model with only pretraining is **"not yet an assistant" but "a token autocomplete,"** and a probabilistic system. Even so, guessing the next token teaches it a lot about the world, stored in its parameters. | [Next word, Ch. 1](../../part1/ch01/next-word.md); [Pretraining, Ch. 9](../../part3/ch09/pretraining.md) |
| Same video, chapter "hallucinations, tool use, knowledge/working memory" (01:20:32) | Hallucination is **the model making things up**. It's a big problem that has existed since early models, and **mitigations have helped somewhat**. | [Hallucination, Ch. 1](../../part1/ch01/hallucination.md) |
| Same video, chapter "models need tokens to think" (01:46:56) | **Spread computation over many tokens**, have it build in-between results, and **use tools whenever possible**. Don't fully trust it to do everything in one go. | [Math, Ch. 7](../../part2/ch07/math-caution.md); [Reasoning models, Ch. 20](../ch20/rl-reasoning.md) |
| Same video, chapter "tokenization revisited: models struggle with spelling" (02:01:11) | **Models see tokens, not letters**, so they struggle to count letters. "How many R's in strawberry?" was a well-known example. For a long time, top models insisted on two. He says they get it right now. | [Tokens, Ch. 1](../../part1/ch01/tokens.md) |
| [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) ([transcript](https://rosetta.to/u/andrejkarpathy/let-s-build-the-gpt-tokenizer)) | Using a Korean example, he explains that because **there's far more English data**, models and tokenizers favor English, and **non-English languages are at a disadvantage**. | [Tokens, Ch. 1](../../part1/ch01/tokens.md) |
| [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) ([chapters and transcript](https://rosetta.to/u/andrejkarpathy/1hr-talk-intro-to-large-language-models)) | Chapters include "LLM dreams" (00:08:58), "Tool Use" (00:27:43), "Multimodality" (00:33:32), "LLM OS" (00:42:15), "Jailbreaks" (00:46:14), and "Prompt Injection" (00:51:30). | [Hallucination, Ch. 1](../../part1/ch01/hallucination.md); [Kinds, Ch. 4](../../part1/ch04/kinds.md); [Templates, Ch. 2](../../part1/ch02/templates.md) |

These line up with the explanations in earlier chapters. We didn't find his views on risk or safety in these videos.

## Fact, observation, or prediction?

| Type | What it covers |
|---|---|
| Stated as fact in the post | The 1989 paper's data and network size; that he rebuilt it |
| His observation | That fine-tuning and foundation models are replacing training from scratch |
| **Prediction** | 2055's scale (10 million times), training in a minute, a megabrain you ask in English |

2055 is **33 years after the post**, so we have no way to check it. For context, the post was written in March 2022, before ChatGPT came out. (The post gives its own date. The ChatGPT launch date, November 30, 2022, comes from Altman's *Reflections*, on the Altman page in this chapter.)

!!! note "★ Going deeper"
    - In what we read, this post has **no discussion of risk or safety**. So we can't describe his views on safety from it. That's why it shouldn't simply be lined up against Hinton's or Amodei's writing.
    - "10 million times" is a rough figure for both data and models, not an exact calculation.
    - For *microgpt* (February 2026), we checked only the one-line description in the blog list: a GPT trainer and runner in about 200 lines of pure Python. You could read it as a habit of rebuilding ideas small to understand them, but that's our interpretation. We didn't read the post itself.

## Try it yourself

**Imagine 2055.** Spend 5 minutes on these:

1. Karpathy predicted an age of "asking in English." How close is that to how you ask AI for things now?
2. If he's right, will "asking good questions" matter more or less? Write one line explaining why.
3. If he's wrong, how might he be wrong?

There's no right answer. It's practice in **reading a prediction and forming your own view**.

## Use it today

1. **Read predictions as predictions.** "2055" can't be checked. Be careful with confident claims tied to a year.
2. **You can already use the observation that plain-language instructions are the key tool.** Practice with Chapters 2 and 15.
3. **The easier a tool looks, the more you need a checking habit.** The "leaky abstraction" warning applies to people using AI tools too (Chapters 3 and 8).
4. **To learn more, read and watch his own work.** We read only part of it.
5. **Don't draw conclusions about a whole field from one person.** The next pages show other views.

## Common mix-ups

- "This prediction is the answer for 2055." It's a prediction. This book doesn't judge whether it will come true.
- "This is what Karpathy thinks about AI risk." These posts don't discuss risk, so we can't say.
- "People who train neural networks will soon be unnecessary." He framed it as the trend taken to an extreme, with that condition attached.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Andrej Karpathy, [Deep Neural Nets: 33 years ago and 33 years from now](https://karpathy.github.io/2022/03/14/lecun1989/), blog, 2022-03-14. Read on 2026-11-09.
    - Andrej Karpathy, [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/), blog, 2019-04-25. We read the introduction. Read on 2026-11-09.
    - Andrej Karpathy, [blog index](https://karpathy.github.io/). We checked only the one-line description of *microgpt* (2026-02-12).
    - Videos on YouTube: [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), and [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE). We checked titles and IDs on YouTube, and parts of the content against Rosetta's unofficial, auto-generated transcripts. We couldn't watch the videos ourselves.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** Our summaries of his posts are paraphrases and should be compared with the originals. The video content was checked only in part, against unofficial auto-generated transcripts. We didn't check his more recent views on risk or safety (talks and interviews). The tables and comparisons are ours.
