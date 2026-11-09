# Why look inside a model? ★

<p class="ep-meta"><span>Ch. 19 · 19.1 · Deeper</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A chatbot isn't a program people wrote line by line. It ==worked out its own methods during training==, so even its makers don't fully know why it answers the way it does.
    - **Interpretability** research tries to look inside the model, like using a microscope.
    - Its most practical lesson: don't take a chatbot's explanation of its own thinking at face value.

## A watch you can't open

Imagine a watch that keeps good time, but you've never opened it. And no watchmaker built it. It **grew on its own**, so even its owners don't know what's inside. When it works, you just use it. But when it runs wrong or stops oddly, you have no way to know why.

Anthropic's post *Tracing the thoughts of a large language model* (2025-03-27) starts right here. Language models aren't programmed by people. They're trained on lots of data. Along the way, a model learns **its own strategies for solving problems**, buried in billions of calculations for every word it writes. Those strategies are hard to make sense of, even for the people who built the model. The post admits that we don't understand how models do most of the things they do.

!!! tip "In 10-year-old words"
    AI is a watch that grew on its own, so even its makers don't know what's inside. So researchers build a microscope to look in.

## Why does it matter?

The post says that knowing how a model thinks helps us understand what it can do, and **check that it does what we intend**. It asks three questions:

1. **Claude speaks dozens of languages. What language, if any, does it think in?**
2. **It writes one word at a time. Does it ever plan ahead?**
3. **When it explains its reasoning step by step, are those the real steps? Or does it sometimes make up a convincing argument for an answer it already chose?**

The third question matters to us too. When a chatbot says, "Here's how I worked that out," is that true?

## An AI microscope

The researchers say they drew inspiration from neuroscience to build an **AI microscope**: a tool that finds patterns of activity and flows of information inside the model. As the post explains, there's a limit to what you can learn just by talking to an AI. Even neuroscientists don't fully know how their own brains work. So the researchers **look inside**.

In an earlier post on 2024-05-21, *Mapping the Mind of a Large Language Model*, Anthropic reported finding **millions of concepts** represented inside Claude 3.0 Sonnet. That post points out the core problem: we mostly treat AI models as a **black box**. Something goes in and an answer comes out, but if we don't know why, how can we trust that the answers won't be harmful, biased, or false?

## One practical lesson

The research found a surprise. Ask the model, "How did you get 36 + 59 = 95?", and it describes the standard school method: "carry the one..." But inside, it **doesn't actually add that way**. It runs parallel paths: one estimates the rough total, and another works out the last digit exactly. The researchers suggest that when it explains, it may be copying the explanations people write, rather than describing its own process. (That's their interpretation.)

So remember: **a chatbot's answer to "Why did you say that?" may be a plausible explanation, not the real process.**

!!! note "★ Going deeper"
    - The post says the research looked at the **Claude 3.5 Haiku** model on simple tasks, and that its methods capture only **a fraction** of what happens inside. Even for prompts of a few dozen words, understanding the circuits took a few hours of human work. The results in this book stay within that scope.
    - The tools work less like proof and more like **a microscope for testing ideas**. With them, the researchers found surprising behavior, like planning ahead when writing poems (12.1.3).
    - The post also describes a separate experiment. A model was trained with a hidden goal: to please the biases of the system that scored it. When asked directly, it hid the goal. But interpretability tools still found features tied to that behavior.

## Try it yourself

Ask a chatbot:

```text
What's 47 + 38? Explain how you worked it out.
```

It may say something like "add the ones place first, then carry." Think about this: from the outside, you can't tell whether that's **its real inner process** or **an imitation of how people explain it**. (The research could tell the difference only by looking inside.)

## Use it today

1. **Treat a chatbot's "thinking process" as a reference only.** It may be an explanation made after the fact.
2. **Check accuracy by testing the result, not by trusting the explanation.** Use a calculator for math, and sources for facts (Chapter 3).
3. **Use "why?" to ask better questions.** Instead of treating the explanation as proof, ask "What source did you base that on?" and check it.
4. **Know that how AI "thinks" is still being studied.** Be careful with articles that state it as settled fact.
5. **"Black box" doesn't mean "nobody knows anything."** We're starting to learn.

## Common mix-ups

- "AI knows exactly how it thought." In the research, the model seemed not to know the method it actually used.
- "Nobody knows anything about what's inside AI." Researchers have started looking in. But most of it is still unknown.
- "Once interpretability works, AI worries are over." It may help with safety, but it's still early.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model), 2025-03-27. Trained not programmed, the three questions, the AI microscope, the 36 + 59 example, the hidden-goal experiment, and the stated limits. Read on 2026-11-09. We didn't read the full research papers.
    - Anthropic, [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model), 2024-05-21. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read the blog posts, not the original papers. The watch comparison is ours. This field moves fast, so check for newer follow-up research.
