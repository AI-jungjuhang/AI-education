# Meaning changes with context

<p class="ep-meta"><span>Ch. 10 · 10.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A "bat" can be an animal or something you swing in baseball. A chatbot ==figures out which one from the words around it==.
    - Each word starts with one list of numbers, but it changes as it passes through the model's layers and takes in context.
    - That's why giving context in your question matters.

## One word, many meanings

In "A bat flew out of the cave," "He swung the bat," and "She went up to bat," the word "bat" means different things. You can tell right away from the words around it. Words like "bank," "light," and "bass" work the same way.

But the embedding from the last page gives each token one list of numbers. If "bat" has only one list, how can the model tell its meanings apart?

!!! tip "In 10-year-old words"
    "Bat" starts with one location, but it moves after looking at the words next to it. That's how the model knows whether it's the animal or the baseball bat.

## Two steps

**Step 1: The starting location (the embedding).** According to 3Blue1Brown's lesson, each token in the input first turns into one list of numbers from the lookup table. At this point, it hasn't looked at the words around it yet.

**Step 2: Adjusting for context.** Next, as the lists pass through the model's many layers, they change **under the influence of the other tokens**. In a chatbot, which reads from front to back, each token **looks back at the tokens before it** and gathers meaning from them. Here's a simple way to picture it. In "He swung the bat," "bat" looks back at "swung" and moves toward the baseball meaning. In "A bat flew out of the cave," the word "flew" comes right after "bat," so it picks up the animal meaning there. The key tool that does this is called **attention**, coming up in the next chapter.

So when the model picks the next word at the end, it uses **locations adjusted for context**, not the starting ones.

## A short history of context-aware meaning

A 2018 paper called **ELMo**, by Matthew Peters and others, showed this idea early on. It proposed word representations that change with context, to handle words with more than one meaning. It took the word vectors from the inner workings of a language model trained on lots of text in both directions. It reported big improvements on six hard language tasks, including answering questions and judging sentiment.

Today's chatbots push the same idea further, with a bigger, deeper design called the transformer.

## When chatbots misunderstand

- **Too little context.** With "How much is a bass?" and nothing else, it tends to go with the most common meaning. (It may also list the meanings, or ask you.)
- **Mixed-up context.** If a sentence could fit several meanings, it may pick the wrong one.
- **Technical words.** The same word can mean different things in different fields. "Consideration" in a contract is not the everyday "consideration." Tell it the field.

!!! note "★ Going deeper"
    - The model adjusts the lists a little at each layer. Some research suggests earlier layers handle things like grammar and word shape, and later layers handle more abstract meaning. But what each layer does differs from model to model, so it's hard to make general rules (interpretability, Chapter 19).
    - 3Blue1Brown explains that the vectors start as lookups of single words, then get updated as they pass through the network. Along the way, they soak in a richer meaning from the context around them. The next lesson in the series goes into this.
    - Chapter 11 on attention explains how these context-aware lists are made.

## Try it yourself

Ask a chatbot three times.

```text
1. What does "bat" mean?
2. In "A bat flew out of the cave at sunset," what does "bat" mean?
3. In "He swung the bat and hit a home run," what does "bat" mean?
```

In question 1, did it list several meanings, or pick the most common one? In 2 and 3, did it use the context to pick the right meaning? Then try another word with several meanings, like "bank," "light," or "bass."

## Use it today

1. **Name the field and the situation first.** For example: "In a legal contract, what does 'consideration' mean?"
2. **Spell out words that could be confusing.** "Bass (the fish)" is clearer than "bass."
3. **Define technical terms.** Saying "Here, X means this" cuts down on mix-ups.
4. **When translating, give the context too.** Translate a single word alone, and you may get the wrong meaning.
5. **If an answer seems off, suspect a misunderstood word.** Ask, "What did you take 'X' to mean?" That often shows the cause.

## Common mix-ups

- "AI gives each word one fixed meaning." Each word starts with one location, then context moves it.
- "AI knows what I mean even without context." Without context, it goes with the most common meaning.
- "Once it picks a meaning, it keeps it for the whole chat." It works out each new sentence again with its new context.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), 2024-04-01. The first embedding is a lookup for each token, and embeddings get updated and soak in context as they pass through the network. Read on 2026-11-09.
    - Matthew E. Peters and others, [Deep contextualized word representations](https://arxiv.org/abs/1802.05365), arXiv, 2018-02-15. Context-aware representations, modeling words with several meanings, a two-direction language model, and improvements on six tasks come from the abstract.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The note about what different layers do sums up general observations. We didn't check a specific source for it. The "bat" examples are ours.
