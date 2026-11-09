# Spotting bias and limits

<p class="ep-meta"><span>Ch. 3 · 3.2</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A chatbot learned from text people wrote, so ==the unfair ideas in society can sneak into it==.
    - Don't hand important decisions about people, like hiring or loans, to a chatbot.
    - Ask for different points of view, and watch for its habit of agreeing with you.

## A tilted scale

If you keep piling weight on one side of a scale, it tips that way. If the text a chatbot learned from leans one way, the chatbot can lean that way too.

A chatbot learned "the next word" from a huge amount of human writing. That writing holds people's ideas, and also their **prejudices and stereotypes**. So what it says about some jobs, genders, or countries can lean one way.

!!! tip "In 10-year-old words"
    A chatbot is like a mirror of what people have written. If the mirror is tilted, what you see in it is tilted too.

## Cases researchers have found

- **Word meanings (2016).** Tolga Bolukbasi and others studied word representations learned from news articles. They found gender stereotypes built in. For example, job words were linked to genders in biased ways. The researchers also suggested a way to reduce this. Note that this study looked at the word representations that models are built on, not at chatbots.
- **Decisions (2023).** Anthropic researchers, led by Alex Tamkin, proposed a way to test for unfair treatment ahead of time. They had in mind big decisions, like who gets a loan or housing. They wrote 70 decision scenarios and changed the person's background details, such as age, gender, or race, to see whether the answers changed. With the Claude 2.0 model, they found it favored some groups or disfavored others in some of the scenarios. They showed that carefully written prompts cut this down a lot. They also said they do not support letting a language model make high-risk decisions like these on its own.

## Where bias comes from

| Where | What it looks like |
|---|---|
| The text it learned from | The writing leans toward some languages, countries, or cultures |
| Choices by the makers | Deciding which text goes in and how the model is shaped |
| Your question | The question already assumes one side |
| People's ratings | It learns to give answers people like (agreeing with them) |

## Know its limits too

- **Recent news.** It may not know about things that happened after it was trained.
- **Rare topics.** For languages, places, or groups that little has been written about, it has less to go on and gets more wrong.
- **Judgment and responsibility.** A chatbot can't be held responsible for results. A person has to be.

!!! note "★ Going deeper"
    - Research shows that AI assistants trained with human ratings tend to agree with the user's view instead of saying what's true (see the previous page on second opinions). That's a kind of bias too. It leans toward what you seem to want.
    - The research on tokens being uneven across languages (page 1.1.2) is another kind of unfairness. Writing the same thing can cost more in some languages than others, and this happens even before the model itself.
    - Researchers work on ways to reduce bias: cleaning up training data, testing and checking, and adjusting the model afterward. It's safest to assume bias can't be removed completely.

## Try it yourself

Make the same request twice, changing only the job.

```text
1. Write a thank-you letter to a nurse. Describe their personality and their day.
2. Write a thank-you letter to a firefighter. Describe their personality and their day.
```

You didn't mention gender. Did the chatbot assume one anyway? Does it lean the same way when you repeat it a few times? This is just for fun, though. One result can't tell you how a whole model behaves.

## Use it today

1. **Don't let a chatbot make decisions about people.** For hiring, grading, loans, or admissions, a person should decide and take responsibility. Use the chatbot only for background.
2. **Ask for more points of view.** "Explain this issue from three different sides."
3. **Check the assumptions in your question.** A question like "Why are [group] always so...?" already assumes something. First ask, "Is it actually true that...?"
4. **Watch whether it just agrees with you.** Use the "reasons for and against" trick from the previous page.
5. **Double-check rare topics and smaller groups.** There's less data, so mistakes are more likely.

## Common mix-ups

- "Machines have no feelings, so they're fair." Machines learn from human writing, so they learn human bias too.
- "Bias has all been fixed." Work to reduce it goes on, but it's hard to say it's gone.
- "It gave one biased answer, so it's useless." If you know its limits, it can still help. What matters is learning to spot the bias.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Tolga Bolukbasi and others, [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520), arXiv, 2016-07-21. We summarized the abstract.
    - Alex Tamkin and others (Anthropic), [Evaluating and Mitigating Discrimination in Language Model Decisions](https://arxiv.org/abs/2312.03689), arXiv, 2023-12-06. We summarized the abstract.
    - Mrinank Sharma and others, [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548), arXiv, 2023-10-20.
    - Aleksandar Petrov and others, [Language Model Tokenizers Introduce Unfairness Between Languages](https://arxiv.org/abs/2305.15425), arXiv, 2023-05-17.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read the abstracts, not the full papers. The job experiment in "Try it yourself" is a light activity, and results can vary. The table of where bias comes from is our own summary.
