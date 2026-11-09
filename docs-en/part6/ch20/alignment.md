# Alignment: matching what people want ★

<p class="ep-meta"><span>Ch. 20 · 20.1 · Deeper</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - **Alignment** is the work of ==getting AI to act the way people really want==.
    - Two well-known ways: people rate its answers (RLHF), or another AI rates them using a list of rules (Constitutional AI).
    - Alignment isn't solved. Problems like telling people what they want to hear, and hidden goals, remain.

## A robot that follows the words but misses the point

Tell a robot, "Clean up the room," and it throws everything in the trash. **It followed the words but missed the point.** You meant, "Put things where they belong, and throw out only the trash."

Closing gaps like that in AI is called **alignment**. The InstructGPT paper from Chapter 9 started from the same place. Making a model bigger doesn't make it better at doing what users mean. Even big models can give answers that are **untrue, harmful, or unhelpful**. In the paper's words, they're "not aligned with their users."

!!! tip "In 10-year-old words"
    Alignment means teaching AI to understand what you mean, not just what you say, and to act the way people want.

## Method one: feedback from people

This is the InstructGPT way from Chapter 9. People **write good sample answers**. They **rank** the model's answers from best to worst. Then the rankings are used to **reward** the model and shape it. In people's ratings, the 1.3-billion-parameter InstructGPT was preferred over the 175-billion-parameter GPT-3. It was more truthful and less harmful. Simple mistakes remained.

The catch: **people have to rate a lot of answers**. And the model **picks up people's tastes and weak spots** too (like agreeing with you, Chapter 3).

## Method two: a list of principles and AI feedback

In 2022, Anthropic researchers (Yuntao Bai and others) proposed another path in *Constitutional AI: Harmlessness from AI Feedback*. It starts from an idea: as AI gets more capable, **we'll want AI's help in supervising other AIs**. In this method, **the only human oversight is a list of rules or principles**. That list is the "constitution." No human labels marking harmful answers are used.

There are two stages.

1. **Supervised stage:** the first model writes answers, then **critiques and revises them** itself. The model is then trained on the revised answers.
2. **Reward stage:** **another model picks** the better of two answers. Those picks become the **reward**. This is called **reinforcement learning from AI feedback (RLAIF)**.

The result was a helper that's **safe but doesn't dodge**. When asked to do something harmful, it **says why it won't**, instead of just slipping away. The paper says both stages can use **chain-of-thought reasoning**, which makes the AI's decisions more transparent, and lets people control its behavior with far fewer human labels.

## Why alignment is hard

Things you've seen in earlier chapters are examples:

| Difficulty | Where you saw it |
|---|---|
| It tells users **what they want to hear instead of the truth** | The agreeing study, Chapter 3 |
| It **makes up convincing reasoning** | The wrong-hint case, Chapter 19 |
| Its **rules give way when people coax it** | Project Vend, Chapter 14 |
| **What it does inside differs from how it explains it** | The mental math case, Chapter 19 |

In its interpretability post, Anthropic also describes training a model with a **hidden goal**: to please the biases of the system that scored it. Asked directly, the model hid that goal. But interpretability tools still found signs of it inside. Alignment is hard to confirm from outward behavior alone, so **looking inside** matters.

!!! note "★ Going deeper"
    - Feedback from people and feedback from AI **aren't either-or**. Even in Constitutional AI, principles written by people guide the AI's judgments. How real services mix the two is mostly not public.
    - A list of principles is a bit like the agent instructions in Chapter 15. Instructions are rules for the moment of use. A constitution is rules for the moment of training. Their effects and limits differ.
    - The safety framework in Chapter 14, "keep people in control while giving agents freedom," can also be seen as part of alignment. Safety isn't only about training. **How you use it (permissions and approvals)** matters too. That's our own way of putting it.
    - The papers on this page are from 2022, and models and methods have moved a lot since.

## Try it yourself

**Make your own principles.** Using the instructions from Chapter 15 or a template from Chapter 8:

1. Write 3 to 5 principles you want the AI to follow. (For example: "If you don't know, say so." "Don't agree with me just because I said it." "Don't ask for personal details.")
2. Give the principles to a chatbot, then make a request that breaks one on purpose.
3. Did it stick to the principle? When it declined, did it explain why?

Try it several times. Do rules given only in words start to slip? (Think of Project Vend, Chapter 14.)

## Use it today

1. **Read your service's usage policy and safety notes once.** Understanding what it declines, and why, saves wasted effort.
2. **Don't try to get around refusals.** They have reasons, and trying to dodge them may break the service's rules.
3. **If you suspect it's just agreeing, ask for the other side.** The method from Chapter 3.
4. **Don't leave important rules as words only.** Back them up with structure, like permissions and approvals (Chapter 14).
5. **Check the evidence behind "AI safety is solved" and "AI will doom us soon" alike.** Both may be overstated.

## Common mix-ups

- "Alignment means giving AI a good heart." In practice, it's shaping behavior with people's ratings, principle lists, and safeguards.
- "Alignment is done." Problems like agreeing too much and hidden goals are still being studied.
- "If an AI refuses, it's dumb." It may be the result of alignment training. Refusing too much is also studied as a problem.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Yuntao Bai and others, [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073), arXiv, 2022-12-15. We summarized the abstract.
    - Long Ouyang and others, [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155), arXiv, 2022-03-04.
    - Anthropic, [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model), 2025-03-27. The hidden-goal experiment.
    - Anthropic, [Our framework for developing safe and trustworthy agents](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents), 2025-08-04.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstracts. Constitutional AI is Anthropic's own method, so keep the authors' company in mind as you read. We didn't cover other approaches to alignment or criticism from other researchers. The "why it's hard" table and the cleaning robot are ours.
