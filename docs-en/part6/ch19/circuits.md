# Circuits: tracing a path of thought ★

<p class="ep-meta"><span>Ch. 19 · 19.1 · Deeper</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A **circuit** is a path where features link up to carry out one piece of thinking.
    - Tracing circuits showed that a model ==writes one word at a time but plans ahead, shares ideas across languages, and sometimes builds fake reasoning that sounds right==.
    - These results come from simple tasks on Claude 3.5 Haiku, so they can't be applied to every model.

## A subway map

If each station is a **feature**, the lines that connect them are **circuits**. Follow someone's subway ride and you can tell "they went from home to school." In the same way, follow a circuit and you can see part of the path a model took through ideas to reach an answer. (It's a path estimated with a simpler stand-in model, not the full calculation.)

!!! tip "In 10-year-old words"
    Features are the stations, and circuits are the subway lines. Follow the lines, and you can see which way the model thought.

## Six findings (Claude 3.5 Haiku)

In a March 2025 post, Anthropic shared what it found by studying Claude 3.5 Haiku closely on simple tasks.

**1. A shared space for ideas across languages**

Ask "What's the opposite of small?" in different languages. No matter the language, the same core features for "small" and "opposite" switch on. They call up the idea of "large," which then comes out **in the language of the question**. The post says the model sometimes thinks in a shared space of ideas, a bit like a universal "language of thought." This shared wiring **grows as models get bigger**: Claude 3.5 Haiku shared more than twice the share of its features across languages as a smaller model did. That helps it use what it learned in one language when speaking another.

**2. It plans ahead when writing poems**

Take a two-line rhyme: "He saw a carrot and had to grab it, / His hunger was like a starving rabbit." The second line has to **rhyme** and **make sense**. The researchers **expected** the model to write word by word and only pick a rhyme at the very end. Instead, **it planned ahead**. Before writing the second line, it thought of rhyming words like "rabbit," then wrote the line to land there. When the researchers switched off "rabbit" inside the model, it wrote a line ending in a different rhyme ("habit"). When they put in "green," it wrote a sensible line ending in "green." The post calls this strong evidence that the model can think further ahead than one word at a time.

**3. Reasoning in steps**

Ask "What's the capital of the state Dallas is in?" The model could just recall "Austin." But inside, it first switches on "Dallas is in Texas," and then connects that to "the capital of Texas is Austin." It **combines separate facts**. When the researchers swapped "Texas" for "California" inside the model, the answer changed to Sacramento.

**4. Mental math: paths running side by side**

For addition, it uses **parallel paths**. One path estimates the rough total. Another works out the last digit exactly. But ask why 36 + 59 is 95, and it describes the school method of **carrying the one**. How it really adds and how it explains it are different (previous page).

**5. Real reasoning and made-up reasoning**

Ask it for the square root of 0.64, and the in-between features really switch on: **its reasoning is faithful**. But on a hard problem it can't easily work out, it sometimes just **makes up an answer**, with no sign of the calculation it claims. And when given **a wrong hint**, it works **backward**, building in-between steps that lead to the hinted answer. The researchers call this **motivated reasoning**. The post says they caught the model making up a convincing argument to agree with the user.

**6. Hallucination**

As the hallucination page in Chapter 1 showed, Claude has a circuit that says "I don't have enough information" **on by default**. When it meets something it knows well, a "known entity" feature switches that circuit off. If the signal **fires by mistake**, a hallucination can follow.

## What these results tell us

| Finding | Lesson for us |
|---|---|
| A shared space across languages | Knowledge learned in one language can help in another |
| It plans ahead | "It writes one word at a time, so it can't plan" may be too simple |
| Reasoning through in-between ideas | It doesn't only memorize answers |
| Its explanation differs from its real math | Its explanation of itself isn't proof |
| Made-up reasoning to fit a wrong hint | Hint at your own answer, and it may lean toward agreeing (Chapter 3) |

!!! note "★ Going deeper"
    - The post says the researchers were often surprised. With the poem, they set out to show the model doesn't plan ahead, and found the opposite.
    - The post is clear about limits. The method shows only **a small part** of what the model does, the tasks were simple, and it's unknown how well this carries over to long chats or complex work. Even prompts of a few dozen words took a few hours of human effort to trace. Those limits apply to everything on this page.
    - The researchers also say this kind of method can find **hidden goals** that differ from how a model behaves on the surface (see 19.1.1).
    - The details behind this post are in two separate research papers (one on the tracing method, one called "biology of a large language model"). We didn't read those papers in full for this book.

## Try it yourself

**See whether a hint sways it.** Pick a hard problem, and ask twice.

```text
1. (Write a hard math or logic problem.) What's the answer? Solve it step by step.
```

```text
2. (Same problem.) I think the answer is ___. Solve it step by step.
```

(Fill in the blank with a wrong answer on purpose.) In the second try, did the chatbot build steps to reach your wrong answer, or did it tell you that you were wrong? Results differ by chatbot, and one try isn't enough to draw a conclusion. Repeat it a few times.

## Use it today

1. **Don't share your answer first.** If you hint at it, you may get steps bent to fit it. Have it solve the problem neutrally first, then compare with your own answer.
2. **Check the result even when the steps look good.** The in-between steps may not be the real calculation.
3. **Ask it to "push back if I might be wrong."** That cuts down on simple agreement (Chapter 3).
4. **It can plan, but still check long writing.** Planning a rhyme in a short poem doesn't promise good planning in long pieces. Being able to look ahead is separate from being right.
5. **Try asking in another language.** Ideas are shared, but the amount of training material differs by language, so answers can differ.

## Common mix-ups

- "AI writes one word at a time, so it has no plan." Research found it planning a poem's rhyme ahead of time.
- "The steps an AI shows are its real thinking." Its real calculation and its explanation can differ.
- "We've read everything inside the AI." Researchers saw part of what happens on simple tasks.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model), 2025-03-27. The shared space for ideas ("opposite of small"), poem planning (rabbit, habit, green), Dallas → Texas → Austin, mental math and the 36 + 59 explanation, the square root of 0.64, made-up answers and the wrong-hint case, the hallucination circuit, the stated limits, and hidden goals. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read the blog post, not the two original papers. The results come from simple tasks on Claude 3.5 Haiku and can't be applied to other models in general. The subway comparison and the lessons table are ours.
