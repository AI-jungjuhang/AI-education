# Scaling: does bigger mean better? ★

<p class="ep-meta"><span>Ch. 20 · 20.1 · Deeper</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - **Scaling laws** say that as models get bigger, their scores get better in a way you can predict.
    - Some say new skills "pop up" once a model is big enough. Others say this ==may be a trick of how the scores are kept==.
    - Knowing this debate helps you read "AI can suddenly do X!" headlines with a level head.

## A growth chart

A child's growth chart is a smooth curve. But some records seem to jump. When you go from 0 push-ups to 1, then from 1 to 5, it can feel like it happened overnight. Really, you were getting stronger a little each day. It only looked sudden because of the yardstick: **"Can you do a full push-up or not?"**

The fight over AI skills that "pop up" is a lot like that.

!!! tip "In 10-year-old words"
    As models grow, their scores rise steadily. But "it suddenly gained a new skill" might be an illusion, depending on how you measure it.

## First, scaling laws

Here's a recap of the two papers from Chapter 9.

- **Kaplan and others (2020):** a language model's error score drops by a steady rule (a **power law**) as model size, data, and training computer power grow. Some trends held across a huge range of sizes.
- **Hoffmann and others (2022, Chinchilla):** for a fixed amount of computing, it's most efficient to grow **model size and training data at the same rate**. They found that big models of the time were **undertrained**.

These laws say the **average score improves smoothly**.

## Emergent abilities: the claim that they appear suddenly

A 2022 paper, *Emergent Abilities of Large Language Models* by Jason Wei and others, points to something different. Scaling up usually improves results in a predictable way. But the authors describe abilities that are **missing in smaller models and present in larger ones**. They call these **emergent abilities**. You **can't predict them just by extending the trend from smaller models**. So, they argue, more scaling could unlock even more abilities.

## The pushback: an illusion from measuring?

A 2023 paper, *Are Emergent Abilities of Large Language Models a Mirage?* by Rylan Schaeffer and others, pushes back. Emergent abilities seem exciting for two reasons. They're **sharp** (absent, then suddenly present), and **unpredictable** (they show up at sizes nobody expected). But the authors argue the effect may come from **the yardstick researchers choose**. With **all-or-nothing scoring**, you get changes that look sudden. With **scoring that gives partial credit**, you see **smooth, predictable change**. They explain this with a simple math model and test it several ways, including on the InstructGPT and GPT-3 family and on a large set of tests called BIG-Bench. They even show they can create "emergent" abilities in image models just by picking the scoring method.

In push-up terms: if you score "1 point only for a perfect answer," it looks like the model learned it **all at once**. If you score "how close was it," you see it **getting better bit by bit**.

| | Emergence claim (2022) | Mirage claim (2023) |
|---|---|---|
| Main idea | Abilities missing in small models appear in big ones | How you score makes things look sudden |
| Predictable? | Hard to predict from small models | Predictable with partial-credit scoring |
| What it suggests | Scaling up more may unlock new abilities | Don't overrate the "suddenness" |

You could say the two papers look at the same thing with different yardsticks, more than they contradict each other. But that's our own reading. We didn't check how researchers have settled this debate since.

!!! note "★ Going deeper"
    - Whichever side is right, one lesson is clear: **the yardstick changes the conclusion**. You'll meet this again in Chapter 21, on the traps in benchmarks.
    - Scaling isn't only about "bigger models." As the next page shows, spending more computing on **thinking longer while answering** is a new direction researchers are exploring.
    - Kaplan and Hoffmann reached different conclusions (very big models versus a balance of model and data), and the later work corrected the earlier. That's how science moves forward.

## Try it yourself

**The yardstick experiment.** Give a friend a 5-question quiz, scored "1 point if right, 0 if wrong." Then score the same answers with partial credit (0 to 1) for how close they were. Does the same set of answers look **sudden** with one yardstick and **smooth** with the other? It shows up best with two people of very different skill, like a little kid and an adult.

## Use it today

1. **When you read "AI can suddenly do X," check the yardstick.** Which test was it, and how was it scored?
2. **When a new model comes out, test it on your own work.** Scores measured by others may not match your job (Chapter 8).
3. **Don't assume bigger is always better.** Data and tuning matter too (Chapter 9).
4. **Read "unpredictable" with care.** It's a topic still being argued.
5. **In science news, tell "researchers argue" apart from "it was proven."**

## Common mix-ups

- "Past a certain size, AI always gains new abilities." That's debated, and the effect of the yardstick has been pointed out.
- "Emergence has been proven fake." There's a strong counterargument, but it's hard to say the field has settled on one answer.
- "Bigger always means better." Scores on average tend to go up. But so do costs, and limits remain.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Jason Wei and others, [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682), arXiv, 2022-06-15. We summarized the abstract.
    - Rylan Schaeffer and others, [Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004), arXiv, 2023-04-28. We summarized the abstract.
    - Jared Kaplan and others, [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), arXiv, 2020-01-23.
    - Jordan Hoffmann and others, [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556), arXiv, 2022-03-29.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstracts. We didn't check how the two views have been settled in later research. The push-up comparison and the "same thing, different yardsticks" reading are ours. This field changes very fast.
