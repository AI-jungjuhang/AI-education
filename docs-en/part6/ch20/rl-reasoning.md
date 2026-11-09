# Reinforcement learning and reasoning models ★

<p class="ep-meta"><span>Ch. 20 · 20.1 · Deeper</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Ask a model to ==write out its steps before it answers==. On hard problems, it often gets more right.
    - **Reasoning models** are trained to think at length like this. Some were built with reinforcement learning on problems where answers can be checked, like math and coding.
    - But the steps it writes may not be what really goes on inside.

## Space to show your work

On a math test, showing your work in the margin makes mistakes less likely. Writing one step at a time makes errors easier to catch than doing it all in your head.

In Chapters 7 and 12, you saw why "think step by step" helps. When the model writes out in-between thinking, that text gives **its next word choices something to build on**. Researchers tested this idea, then turned it into training. That's where reasoning models come from.

!!! tip "In 10-year-old words"
    Show your work instead of just writing the answer, and you'll solve hard problems better. Reasoning models are AIs that practiced solving problems that way.

## Chain of thought

A 2022 paper by Jason Wei and others looked at this. (Its title is *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.) When a model wrote out **a series of steps (a chain of thought)**, it got much better at hard reasoning. In large enough models, **just showing a few examples written as chains of thought** (giving examples, as in Chapter 2) was enough to bring this out. Scores rose on arithmetic, common-sense, and symbol puzzles. With only eight chain-of-thought examples, a 540-billion-parameter model set a new record on GSM8K, a test of math word problems.

## Spending computing on thinking time

A 2024 paper by Charlie Snell and others asks: if a model can use a fixed but fair amount of computing **while answering**, how much better can it do on a hard question? The authors studied two ways to use that extra computing. One searches through candidate answers, checked step by step by a separate "checker" model. The other adjusts the model's answer as it goes, based on the question. A key finding: **which method works best depends a lot on how hard the question is**. The paper's title says that spending computing this way can be **more effective than making the model bigger**. (We read only part of the abstract, so we don't give their exact numbers.)

## Growing reasoning with reinforcement learning

Some problems have answers you can check, like math, code, and science. For those, a computer can **grade the model's answer by itself**. That means you can use **reinforcement learning**, giving a reward for right answers, so the model learns good ways to solve problems on its own. (Unlike the human-feedback training in Chapter 9, the reward comes from checking the answer, not from people's ratings.)

A 2025 paper from DeepSeek-AI, called *DeepSeek-R1*, tried this. Its summary says rewards alone were enough to grow **strong reasoning**. People didn't have to write out example steps. Advanced patterns like **checking its own work, verifying, and switching strategies** **emerged on their own**. On **checkable tasks** like math, coding contests, and science, it did better than models trained on people's worked examples. The reasoning patterns could also be used to **improve smaller models**.

## The "thinking models" we use

Many apps now have **models or modes that think longer before they answer**. (Names and methods differ by app.) These models usually:

- Help most with **hard reasoning, math, code, and multi-step planning**.
- Tend to be **slower and costlier for simple questions**.
- Sometimes **show part of their thinking** (often as a summary).

## Is the thinking real thinking?

The Anthropic research from Chapter 19 gives an important clue. Recent models can "think out loud" for a long time before giving a final answer. That chain of thought **often leads to better answers**, but **sometimes it misleads**. The model may **make up plausible steps** to reach the conclusion it wants. In the research, there were cases where the model wrote as if it had calculated something, with no sign inside that it had.

So the work a reasoning model shows is **a reference, not proof**.

!!! note "★ Going deeper"
    - The DeepSeek-R1 paper stresses one condition: **tasks where the answer can be checked**. In areas with no single right answer, like writing or advice, that kind of reward is hard to build. So it's hard to say "reasoning models are better at everything."
    - These three papers each work at a different layer: a prompting trick (chain of thought, 2022), how to spend computing while answering (2024), and a training method (2025). Seeing them as one story is our own summary.
    - The papers tested different models at different times, so their numbers can't be applied directly to today's services.

## Try it yourself

Pick a tricky logic puzzle and ask two ways. (If your service has a "thinking" mode, you can also compare with it on and off.)

```text
1. Sam is taller than Maya. Maya is taller than Leo. Leo is shorter than Ava.
   Who is taller, Sam or Ava? Just give the answer.
```

```text
2. Same puzzle. Think it through step by step, then give your answer.
```

Did you get the same answer? (Actually, there's no way to know. We're never told how Ava compares with Maya or Sam, so "can't tell" is the right answer.) See whether the chatbot forced an answer or said "can't tell." Did solving it step by step get closer to the right answer?

## Use it today

1. **For hard problems, ask for step-by-step work.** For simple questions, don't. It just slows things down.
2. **Read the steps and look for where they go wrong.** With steps shown, mistakes are easier to find.
3. **Use thinking models for tasks with checkable answers.** Math, code, and logic puzzles.
4. **Lower your expectations for tasks with no right answer.** Thinking longer doesn't settle questions of taste or judgment.
5. **Still check the result.** Writing out its thinking doesn't make it right.

## Common mix-ups

- "Thinking models think like people." They're trained to write in-between text while solving. Whether that's thinking in our sense is another question.
- "A long explanation means a right answer." It can make up convincing steps (Chapter 19).
- "Reasoning models replace regular models for everything." For easy jobs, they're slower and cost more.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Jason Wei and others, [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903), arXiv, 2022-01-28. We summarized the abstract.
    - Charlie Snell and others, [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314), arXiv, 2024-08-06. We read part of the abstract.
    - DeepSeek-AI, [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948), arXiv, 2025-01-22. We summarized the abstract.
    - Anthropic, [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model), 2025-03-27. Chains of thought that sometimes mislead.
    - Andrej Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), YouTube, 2025-02-05. Chapter "models need tokens to think" (01:46:56), checked through Rosetta's unofficial [transcript](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt). There's also a chapter on DeepSeek-R1 (02:27:47) for further watching.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstracts. The description of "thinking modes" in today's services is general and differs by service. "Can't tell" as the puzzle's answer is our own judgment of the puzzle. The show-your-work comparison is ours.
