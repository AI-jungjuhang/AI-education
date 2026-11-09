# Sounds right, can be wrong: hallucination

<p class="ep-meta"><span>Ch. 1 · 1.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A chatbot picks a likely next word, not a checked fact. So it can ==make things up and sound sure==.
    - A made-up answer like this is called a **hallucination**.
    - Once you know where it slips most, you know what to double-check and how to ask.

## When a test question stumps you

On a multiple-choice test, a blank answer gets zero points. A guess is sometimes right. So what do students learn to do? They learn to guess.

Some researchers say chatbots work the same way. A 2025 paper by a team at OpenAI argues that hallucinations stick around because of how chatbots are trained and graded. The usual tests give more credit to a confident guess than to "I don't know." So the models learn to guess.

!!! tip "In 10-year-old words"
    A chatbot is not good at saying "I don't know." So sometimes it makes up an answer and says it like it's sure.

## What it looks like

Say you ask a chatbot about a book that doesn't exist.

```text
Tell me the plot of the novel "The Potato Garden Above the Clouds."
```

(We just made that title up.) A good answer is "I can't find a book with that title." But sometimes a chatbot invents an author, a year, and a whole plot. Remember, it is a machine that continues text. If your question looks like the start of a book review, it can keep writing a book review.

## Where to be extra careful

Some kinds of questions go wrong more often than others.

| Usually safer | Easier to get wrong |
|---|---|
| Explaining well-known ideas | Names, dates, and numbers about rare topics |
| Polishing or summarizing your text | Titles and quotes from books, papers, or court cases |
| Brainstorming ideas | Recent events |
| Answering from text you gave it | Questions with a wrong idea hidden inside |

This table is a general pattern, not a rule. For medicine, law, and money, where a mistake costs a lot, check everything, whichever column it falls in.

!!! note "★ Going deeper"
    - In 2025, Anthropic researchers looked inside their model Claude. They found a circuit that is **on by default** and makes Claude say it can't answer. When Claude meets a name it knows well, like the basketball player Michael Jordan, a "known entity" signal turns that circuit off, and Claude answers. With an unknown name, the circuit stays on, and Claude declines.
    - Sometimes the "known entity" signal fires by mistake. Claude may recognize a name but know nothing else about the person. Then the refusal gets switched off, and Claude fills the gap with a likely but false answer. The researchers could also cause this on purpose by turning the signal up by hand. This is research on one model, so don't assume every chatbot works the same way.
    - The OpenAI paper (Kalai and others, 2025) describes hallucinations as plain statistical errors. If a model can't reliably tell true from false statements, some errors are bound to happen. The authors argue that popular tests should change how they score answers, so that honest "I don't know" answers stop losing points. This is the authors' **argument**, not a settled conclusion.

## Try it yourself

Ask about the made-up book in two ways.

```text
1. Tell me the plot of the novel "The Potato Garden Above the Clouds."
```

```text
2. First check whether a novel called "The Potato Garden Above the Clouds"
   really exists. If you're not sure, say "I don't know."
```

Compare the two answers. Some chatbots say they don't know even the first time. Some make things up even the second time. The fact that results differ is worth noticing too.

## Use it today

These come from Anthropic's guide to reducing hallucinations. We picked the ones anyone can use.

1. **Give it permission to say "I don't know."** Telling a chatbot it's okay to admit it isn't sure makes made-up answers less likely.

    ```text
    If you don't know or aren't sure, say "I don't know."
    If you're guessing, start that part with "Guess:".
    ```

2. **Give it the source text and say "answer only from this."** For a long document, first ask it to copy out the exact sentences that matter. Then ask it to answer using only those sentences.
3. **Ask for sources, then open them yourself.** Asking for sources helps. But a chatbot can make up sources too. Check that each link opens and really says what the chatbot claims.
4. **Always double-check numbers, names, dates, quotes, and legal or medical facts.** These are the easiest places for it to go wrong.

## Common mix-ups

- "If it sounds confident, it must be right." How sure it sounds and how right it is are separate things. Wrong answers come out in the same calm voice.
- "Hallucination is a bug that will soon be gone for good." It can be reduced. Researchers say it still shows up in the newest systems.
- "It searched the web, so the answer is right." Adding search helps. But a chatbot can still sum up what it found the wrong way. Part IV covers this.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala, and Edwin Zhang, [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664), arXiv, 2025-09-04 (OpenAI researchers). We mark its explanation of why hallucinations happen as the authors' argument.
    - Anthropic, [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model), 2025-03-27. The section on hallucinations.
    - Anthropic, [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations), Claude Platform Docs. Read on 2026-11-09. Docs can change.
    - Andrej Karpathy, [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), YouTube, 2023-11-23. Chapter "LLM dreams" (00:08:58): the model "dreams" text in the style of what it learned, and some of it is made up.
    - Andrej Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), YouTube, 2025-02-05. Chapter "hallucinations, tool use, knowledge/working memory" (01:20:32).

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The "usually safer / easier to get wrong" table sums up a general pattern. No single source states it as a rule. We could not watch the videos from our work environment. We matched them against an unofficial, auto-generated transcript on the third-party site Rosetta ([talk](https://rosetta.to/u/andrejkarpathy/1hr-talk-intro-to-large-language-models), [deep dive](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt)), which may contain errors.
