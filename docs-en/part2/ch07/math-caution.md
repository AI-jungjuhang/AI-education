# Be careful when it does math

<p class="ep-meta"><span>Ch. 7 · 7.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Chatbots write well, but ==in exact math with many steps, small mistakes can pile up==.
    - Let AI set up the formula, and let a calculator work out the value.
    - For things where a mistake costs a lot, like money, taxes, or medicine doses, always check separately.

## Long multiplication in your head

Short addition is easy in your head. But try four-digit multiplication in your head. Get one middle step wrong, and the answer is wrong, because the bad number carries forward.

Something similar can happen when a chatbot does math. As Chapter 1 showed, it writes one piece at a time and never goes back to change a piece it already wrote.

!!! tip "In 10-year-old words"
    AI sets up the math problem. The calculator finds the answer. Don't ask a mental-math champ to do long multiplication in their head.

## What research says

A 2023 paper by Nouha Dziri and others, called "Faith and Fate," tested transformer language models on problems that must be solved in small steps. These included long multiplication, logic grid puzzles, and a classic planning problem. The models seemed to solve them by matching patterns they had seen before. They did not seem to have a real step-by-step method. They also argued something about writing one piece at a time. As problems get harder, accuracy can fall fast, because errors build up step by step.

Andrej Karpathy gives similar advice in his "Deep Dive" lecture. A model can only do a limited amount of computing for each token. So spread the work across many tokens, ask for in-between results, and use tools, like having it run code, whenever you can.

That paper tested 2023 models. Today's models do much better, since many use tools or think things through before answering. But you should still check for mistakes in complicated math.

## A guide by kind of math

| Math | How to hand it off |
|---|---|
| Short addition, simple ratios | Fine to hand off, but check with a rough estimate |
| Averages, totals, percentages | Have it write the formula; get the value from a calculator or spreadsheet |
| Dates (how many days until, which weekday) | Check with a calendar or tool. These go wrong easily |
| Exchange rates, unit conversions | It may not know today's rates, so enter them yourself and ask only for the formula |
| Loan interest, taxes, retirement savings | Use it to understand the formula; get values from an official calculator or an expert |
| Medicine doses, medical math | Don't hand this to AI. Ask a doctor or pharmacist |

## How to ask for the formula

```text
Help me with this problem. Don't calculate the numbers yourself.
1) Write out the steps as formulas, one step at a time.
2) Explain what each number in each formula stands for.
I'll do the math on a calculator.
Problem: On weekdays, I spend $4.50 on coffee and $12 on lunch.
I don't spend anything on weekends. How much do I spend in 4 weeks?
```

With the formulas and explanations, you can check that you understand while you work out the values on a calculator. This catches math mistakes, and it also catches places where the problem was misunderstood.

!!! note "★ Going deeper"
    - When a chatbot is connected to a tool, like a calculator or code runner, the code works out exact values, which helps a lot (Part IV). But if the formula is wrong, an exact value still gives a wrong answer. A person needs to read and check the formula.
    - "Think step by step" often helps because writing out middle steps gives the model text to build its next pieces on. Today's reasoning models are trained to think at length on their own (Chapter 20). But steps can look right and still be wrong.
    - The study above looked at the limits of multi-step problems in general, not just math. Some people think long pieces of writing that contradict themselves share the same cause. The study didn't show that directly, though.

## Try it yourself

Try it two ways.

```text
1. What is 3,847 × 2,916?
```

```text
2. Break 3,847 × 2,916 into formulas, digit by digit, and write them out.
   I'll work out the values on a calculator.
```

Compare answer 1 with a calculator. (The right answer is 11,217,852.) If you follow the formulas from answer 2 on a calculator, do you get the right answer? If something went wrong, where was it?

## Use it today

1. **Ask for the formula instead of the value.** You can read and understand a formula.
2. **Make a rough estimate.** If you know 3,800 × 2,900 is about 11 million, you'll catch an answer that's way off.
3. **Check dates and units separately.** Weekdays, leap years, and unit conversions are easy to get wrong.
4. **For money and health, use official calculators or experts.** Use AI only to help you understand.
5. **Check the formula even when a tool is connected.** An exact value is no use if the formula is wrong.

## Common mix-ups

- "If it shows its work, it's right." The steps can look fine and still go wrong in the middle.
- "It's a computer, so its math is perfect." A chatbot is a machine that continues text, not a calculator.
- "It got it right once, so it'll get it right again." Ask the same problem again and the answer can change (Chapter 1).

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Nouha Dziri and others, [Faith and Fate: Limits of Transformers on Compositionality](https://arxiv.org/abs/2305.18654), arXiv, 2023-05-29. We summarized the abstract. It tested the transformer models of that time.
    - Andrej Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), YouTube, 2025-02-05. Chapter "models need tokens to think" (01:46:56): spread computation across tokens, ask for intermediate results, and prefer tools such as code. Checked through Rosetta's unofficial, auto-generated [transcript](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt).

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstract of the paper. This page doesn't measure how far today's models have moved past these limits. The guide table is our own. We checked the multiplication answer (11,217,852) ourselves.
