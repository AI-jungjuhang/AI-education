# The traps in benchmarks ★

<p class="ep-meta"><span>Ch. 21 · 21.1 · Deeper</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A **benchmark** is a shared test for comparing AI models. But ==a high score doesn't mean it's good at your work==.
    - Traps include test questions leaking into training data, the scoring yardstick, and the gap between what people like and what's correct.
    - With a short checklist, you can read "Model X is number one!" headlines calmly.

## The top student's test

A student who aces the math test isn't automatically a great cook or singer. What matters is **what the test measures**. And if the student saw the questions ahead of time, the score means even less.

AI models are the same. Every new model comes with "Number one on test X!" But how much that test looks like your work is a separate question.

!!! tip "In 10-year-old words"
    A score means it's good at that test. It doesn't mean it's good at your job, especially if the test questions leaked out early.

## Some well-known tests

| Test | What it is (from the papers' summaries) |
|---|---|
| **MMLU** (2020) | **57 subjects**, including grade school math, US history, computer science, and law. Back then, the biggest GPT-3 beat random guessing by only about 20 percentage points on average. Models were **uneven**, **often didn't know when they were wrong**, and were near random on subjects like morality and law |
| **HELM** (2022) | Looks beyond accuracy, with **7 measures** (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) across **16 core scenarios**. It compared 30 models under the same conditions. Before HELM, models had been tested on only **17.9%** of those core scenarios on average, and some well-known models didn't share a single one |
| **Chatbot Arena** (2024) | People **see two chatbots' answers side by side and pick the better one**. It had gathered over 240,000 votes, and the authors found the crowd's votes agreed well with expert raters |

## Five traps

**1. The questions leaked (contamination).** A 2023 paper, *Don't Make Your LLM an Evaluation Benchmark Cheater*, looks at **benchmark leakage**: test data accidentally ending up in a model's training data. It's become more common, because training data is often gathered before the test is run. The authors found that leakage can **dramatically raise scores**, giving a false picture of how good the model is.

**2. The yardstick changes the conclusion.** As Chapter 20 showed, the scoring method can make "sudden new abilities" appear or disappear.

**3. Averages hide things.** Even on MMLU, models were **uneven** across subjects. A high average score can hide weakness in the area you need. This is the "jagged frontier" from Chapter 8.

**4. What people like isn't the same as what's correct.** Chatbot Arena measures **which answers people prefer**. A confident, smooth answer may win, whether or not its facts are right (the limits of human feedback in Chapter 9, and agreeing with you in Chapter 3). That doesn't make it a bad test. It means you should know **what it measures**.

**5. The test isn't your job.** A score on multiple-choice questions may say little about how well it writes your weekly report.

!!! note "★ Going deeper"
    - The HELM paper treats **saying what's missing** as part of honest testing. It lists gaps itself, like question answering in under-studied English dialects, and measures of trustworthiness.
    - Benchmarks **saturate**. When nearly every model scores near 100%, the test can't tell them apart, and new tests are needed. "Hide some test questions" from Chapter 15 comes from the same worry as contamination.
    - Crowd votes depend on who asks what. The Chatbot Arena paper found its questions varied and good at telling models apart, but that doesn't mean they represent every use.

## Try it yourself

Pick one recent "Model X is number one" story and check it.

| Check | Your answer |
|---|---|
| Which test was it? | |
| Who ran it? (The company that made the model, or someone else?) | |
| What does the score measure? (Accuracy? What people prefer? Speed?) | |
| Could the test questions have been in the training data? | |
| Does it look like your work? | |
| When was it measured? (Are the model and test current?) | |

If you can't fill in the boxes, read the story as background only.

## Use it today

1. **Look at the test name and scoring next to the score.** Don't trust "number one" by itself.
2. **Double-check scores the model's maker published.** Compare them with results from others.
3. **Test it on your own work.** The light testing method from Chapter 15 helps here.
4. **Remember that a ranking of what people like isn't a ranking of what's right.** Check accuracy separately.
5. **Don't trust old rankings.** Models and tests change fast.

## Common mix-ups

- "A high score means it's good at everything." It only shows what the test measures.
- "Benchmarks are useless." They're a useful starting point for comparing. Just know their limits.
- "The crowd's favorite is the most accurate." What people like and what's correct can differ.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Dan Hendrycks and others, [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300), arXiv, 2020-09-07. We summarized the abstract.
    - Percy Liang and others, [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110), arXiv, 2022-11-16. We summarized the abstract, including the 17.9% figure.
    - Wei-Lin Chiang and others, [Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference](https://arxiv.org/abs/2403.04132), arXiv, 2024-03-07. We summarized the abstract.
    - Kun Zhou and others, [Don't Make Your LLM an Evaluation Benchmark Cheater](https://arxiv.org/abs/2311.01964), arXiv, 2023-11-03. We summarized the abstract.
    - Also the Schaeffer and others (2023) and Dell'Acqua and others (2023) papers from Chapters 20 and 8.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstracts. Each number is about the models and tests of its year and differs today. "People may prefer smooth, confident answers" is our interpretation, not a claim from the Chatbot Arena paper. The five traps and the checklist are ours.
