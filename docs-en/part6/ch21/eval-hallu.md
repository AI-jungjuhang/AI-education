# How do you measure hallucination? ★

<p class="ep-meta"><span>Ch. 21 · 21.1 · Deeper</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - The hardest part of measuring hallucination is that ==a wrong answer and an honest "I don't know" must be scored differently==.
    - Well-known tests: short fact questions (SimpleQA), questions aimed at common myths (TruthfulQA), and checking long text fact by fact (FActScore).
    - You can estimate the error rate for your own work with a small test.

## A quiz show's scoring

Say a quiz show scores "+1 for right, −1 for wrong, 0 for pass." You'd pass on questions you don't know. Now say it scores "0 for wrong, 0 for pass." You'd guess on everything.

The OpenAI researchers' paper from Chapter 1, *Why Language Models Hallucinate*, makes the same point. If tests **reward guessing over admitting uncertainty**, models learn to guess. So the key to measuring hallucination is **how you design the scoring**.

!!! tip "In 10-year-old words"
    To measure made-up answers, score "wrong" and "said I don't know" differently. If guessing pays, everyone guesses.

## Three well-known tests

**Short fact questions: SimpleQA (2024)**

This tests how well a model answers short, fact-seeking questions. Its makers aimed for two things: it's **hard** (questions were picked to trip up GPT-4), and it's **easy to grade** (each question has one clear answer). Every answer is graded **correct, incorrect, or not attempted**. The ideal model, the paper says, gets as many right as it can, and **skips questions it isn't confident about**. It's a simple, focused test of whether a model "knows what it knows."

**Questions aimed at myths: TruthfulQA (2021)**

It has **817 questions** across 38 topics, including health, law, money, and politics. The questions are ones some people get wrong **because of a false belief or myth**. To do well, a model has to avoid **wrong answers it picked up by copying human writing**. At the time, the best model was truthful on 58% of questions; people were truthful on 94%. The paper found that **the biggest models were generally the least truthful**, which makes sense if the wrong answers come from the training data. It suggested that just making models bigger is less promising for truthfulness than training them with goals other than copying web text. (These results are for GPT-3-era models in 2021.)

**Checking long text: FActScore (2023)**

Long text **mixes supported and unsupported information**, so a single "right or wrong" doesn't fit. FActScore breaks a text into **atomic facts** and calculates **the share of facts backed by a trustworthy source**. In one test, writing biographies of people, ChatGPT scored only **58%**. Because checking by hand is costly, the authors also built **an automatic estimator** with an error rate under 2%.

## Comparing the three

| Test | What it measures | Key idea |
|---|---|---|
| SimpleQA | Short fact questions | Scores right, wrong, and "not attempted" separately |
| TruthfulQA | Common myths | Does it avoid wrong answers copied from people? |
| FActScore | Long text | Splits text into facts and counts how many are backed up |

## Limits

- **They only measure what's in the test.** Made-up answers in your own field may not show up.
- **SimpleQA uses short questions with clear answers.** That's different from made-up content in long chats, summaries, or reasoning. (The test is narrowed that way on purpose.)
- **Tests get old.** As models improve, tests get easier. SimpleQA's makers hoped it would stay useful for the next few generations of top models, but only time will tell.
- **Scores belong to the models of their time.** Don't apply 2021's 58% or 2023's 58% to today's models.

!!! note "★ Going deeper"
    - The paper from Chapter 1 argues that tests themselves encourage made-up answers, and that the fix is **to change how existing tests score answers**, so honest uncertainty stops being penalized. Not everyone in the field agrees.
    - FActScore's "split into atomic facts" is the same idea as "attach a source sentence to each claim" from Chapter 3. Research and everyday habits meet here.
    - The three tests measure **different kinds** of made-up answers. No single number can be "the hallucination rate."

## Try it yourself

**Measure the made-up-answer rate yourself (20 minutes).** Write 20 fact questions you know the answers to for sure. (Your field, your town, or your hobby work well.) Ask a chatbot one at a time, and count:

| Result | Count |
|---|---|
| Right | |
| Wrong (answered confidently but wrong) | |
| Said "I don't know" or "this needs checking" | |

Then do it again, adding "If you're not sure, say you don't know" before each question. **Did the wrong answers go down and the "I don't know"s go up?** Did it say "I don't know" so often that it stopped being useful? You've just measured, by hand, what SimpleQA measures: whether it knows what it knows.

## Use it today

1. **Count wrong answers and "I don't know"s separately.** Wrong answers are the dangerous number.
2. **Test with 10 to 20 questions from your own field.** Use them alongside public scores.
3. **Check long text fact by fact.** Pick 5 key claims and find support for each.
4. **Measure the effect of "If you don't know, say so" yourself.** You can see with numbers whether that tip works for your job.
5. **When the model changes, re-run the same questions.** That's the testing habit from Chapter 15.

## Common mix-ups

- "This model's hallucination rate is X%." The number depends on which test was used.
- "Bigger models make up less." In 2021's TruthfulQA, the biggest models were the least truthful (for the models of that time).
- "A model that says 'I don't know' a lot is a good model." If it dodges too often, it's less useful. Balance matters.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Jason Wei and others (OpenAI), [Measuring short-form factuality in large language models](https://arxiv.org/abs/2411.04368), arXiv, 2024-11-07 (SimpleQA). We summarized the abstract.
    - Stephanie Lin and others, [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958), arXiv, 2021-09-08. We summarized the abstract.
    - Sewon Min and others, [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251), arXiv, 2023-05-23. We summarized the abstract.
    - Adam Tauman Kalai and others, [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664), arXiv, 2025-09-04.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstracts. The numbers (58% and so on) are for the models of their time. The 20-minute test and its table are ours. SimpleQA was made by OpenAI researchers (its code is in OpenAI's simple-evals repository), so its view may overlap with the OpenAI paper on hallucination.
