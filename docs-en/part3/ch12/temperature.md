# Temperature: how adventurous to be

<p class="ep-meta"><span>Ch. 12 · 12.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - **Temperature** is a setting that decides ==how much to favor the most popular choices== when drawing the next word from the score table.
    - At high temperature, choices get drawn more evenly. At low temperature, the top choice wins almost every time.
    - Setting the temperature to 0 doesn't get rid of wrong answers.

## How many of each ball in the box

Picture a box of balls: 30 red, 20 blue, and 15 yellow. Red comes up most often, but the others come up too. (That's the score table from Chapter 1.)

Temperature is **a dial that changes the box**. Turn it down, and there are even more red balls and fewer of the others, so you get red almost every time. Turn it up, and the counts even out, so blue and yellow come up more often.

!!! tip "In 10-year-old words"
    Temperature is an adventure dial. Turn it down and it always takes the safe path. Turn it up and it sometimes takes a strange path.

## How the lesson explains temperature

3Blue1Brown's lesson explains it like this. In the last step, a bit of math called softmax turns scores into chances. If you **add a number T** to that math, you can change how spread out the chances are. It's called "temperature" because it looks like temperature in physics.

- **When T is large:** lower scores get more weight, so the chances are **spread more evenly**. Draws become more varied.
- **When T is small:** the biggest scores **take over**. The top choice gets picked almost every time.
- **When T is 0:** **all the weight** goes to the biggest score. In theory, the same top choice gets picked every time. (In real services, "temperature 0" doesn't promise exactly the same answer every time.)

## Low and high temperature

| | Low temperature | High temperature |
|---|---|---|
| What answers look like | Safe and similar | Varied, sometimes strange |
| Asking the same thing again | Nearly the same answer | Different answers each time |
| Good for | Jobs with one right answer, like sorting facts, summaries, labeling | Jobs that need variety, like ideas, names, creative writing |

(The "Good for" row sums up common practice. Every job is different, so test it yourself.)

## What temperature can't do

- **Lowering the temperature doesn't remove hallucinations.** If the top choice on the score table is wrong, a low temperature makes it pick that wrong choice **more consistently**. Low temperature means "steady," not "correct."
- **High temperature doesn't promise creativity.** It just lets less common words come up, which can be merely odd.
- **Many apps hide the temperature.** In most everyday chatbot apps, you won't see a dial. Developer settings (an API) sometimes have one, but whether you can change it, and how far, depends on the model and the service.

!!! note "★ Going deeper"
    - The raw scores before they become chances are called **logits**. Temperature works by dividing the logits by T before softmax. (The lesson describes this as putting T in the exponent.)
    - Temperature 0 is the same as always taking the top choice, which is called **greedy decoding**. Research shows that this doesn't always make good writing (next page).
    - Some services may give slightly different results even at temperature 0, for example because of tiny differences in how the math runs. We didn't confirm a source for this, so treat it as a note to check.

## Try it yourself

Make the same request three times, then try changing the "temperature" with your wording.

```text
1. Give me 5 names for a cafe that's perfect on rainy days. (Ask this three times.)
2. Give me 5 of the most common, safe names.
3. Give me 5 really unusual, quirky names.
```

How different were the three tries of question 1? How did 2 and 3 differ? You'll see that wording can have a similar effect. (Wording doesn't change the temperature itself. It changes the score table.)

## Use it today

1. **For jobs that must be right, rely on checking, not on "steady."** Wrong answers can stay even at low temperature.
2. **For ideas, ask for several.** "Give me 10" has an effect a bit like a higher temperature.
3. **If the answers feel bland, say "more unusual."** Wording can add variety.
4. **Different answers to the same question are normal.** For answers that matter, get a few and compare (Chapter 3).
5. **If your tool shows a temperature setting, experiment.** The best value differs by job.

## Common mix-ups

- "Temperature 0 makes it accurate." It makes it consistent, not accurate.
- "Higher temperature makes it more cleverly creative." It just lets less common words through.
- "Every chatbot lets you set the temperature." Many hide it and don't let you change it.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), Deep Learning Chapter 5, 2024-04-01. Adding T to softmax; what happens when T is large, small, and 0; and the term logits. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** "Low temperature for exact jobs, high for creative jobs" is common practice, not something we confirmed in these sources. Whether you can set temperature depends on the service. The ball box comparison is ours.
