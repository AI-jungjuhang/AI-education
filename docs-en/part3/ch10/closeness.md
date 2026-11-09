# Similar meanings sit close together

<p class="ep-meta"><span>Ch. 10 · 10.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - If you think of the lists of numbers as locations, ==words with similar meanings tend to sit close together, and unlike words sit far apart==.
    - There are famous examples where "direction" carries meaning too, but they don't always work exactly.
    - Close doesn't mean the same. And society's prejudices get built into the distances too.

## Seats in the lunchroom

In a lunchroom, close friends usually sit near each other, and kids who don't talk much sit farther apart. Just from the seating, you can tell who's close to whom.

Embeddings are easy to picture this way. On the last page, each token got a location. In that space, **tokens with similar meanings gather close together**. "Cat" and "dog" are close. "Cat" and "refrigerator" are far apart.

!!! tip "In 10-year-old words"
    Words with similar meanings sit at the same lunch table. That's how a computer can measure "similar" as a distance.

## Not just distance: direction carries meaning too

A 2013 study (the paper behind word2vec) reported that word vectors learned this way did well on tests of word similarity, catching both grammar patterns and meaning.

3Blue1Brown's lesson shows a more fun example. The difference between the vectors for "woman" and "man," which is a **direction** from one point to the other, looks a lot like the difference between "queen" and "king." So if you start at "king" and move in the "woman minus man" direction, you land near "queen." This is a classic example. But the lesson adds that it only works **roughly**. In the model used for the video, the real "queen" sat a bit farther away than the math predicted.

So remember it like this: **differences in meaning can show up as directions, but the math isn't always exact.**

## Where this gets used

(These are widely known uses. Each service builds them its own way.)

- **Searching by meaning.** It finds text that means something close, even if the words don't match. For example, you search "food that helps with a cold" and get a post called "what to eat when you're feeling sick."
- **Recommending similar things.** Distances help find similar articles or products.
- **Linking languages.** Models can be trained so the same idea in different languages sits close together.

## The limits of "close"

- **Similar isn't the same.** "Cheap," "inexpensive," and "affordable" sit close, but they feel different. Opposites can sit close too, because they show up in the same kinds of sentences. ("Hot" and "cold" are both about temperature.)
- **The prejudices in text show up in the distances.** The 2016 study from Chapter 3 found that, in word vectors learned from news, gender stereotypes lined up along **a single direction**. "Close" is shaped by what people have written.
- **It may not match the "close" you mean.** Things that often appear together in the training text end up close. That may differ from what "similar" means in your work.

!!! note "★ Going deeper"
    - Closeness is usually measured by the **angle between two vectors (cosine similarity)** or by distance. The more two vectors point the same way, the closer their meanings.
    - 3Blue1Brown explains that a space with very many dimensions has a huge number of different directions. So many kinds of meaning, like gender, size, or feelings, can each get their own direction without crowding each other. This idea leads to the "features" in Chapter 19.
    - Today's meaning-based search tools turn a whole passage into one vector and compare those. Adding search to a chatbot (RAG) builds on this idea (Chapter 13).

## Try it yourself

**Make two groups.** Split these 6 words into two groups of close words.

```text
cat / dog / tiger / car / bus / train
```

Then ask a chatbot:

```text
List these words in order of how close their meanings are, and explain why:
cat, dog, tiger, car, bus, train
```

Did it match your groups? Then ask about "how they're similar but different." You'll see that close and the same aren't the same thing.

## Use it today

1. **Search with a description.** In tools that search by meaning, a sentence describing your situation often works better than a few keywords.
2. **Ask for "3 similar examples."** Finding close things is something AI does well.
3. **Also ask "how are they similar but different?"** That keeps you from missing small differences in meaning.
4. **Try a similar word.** If you don't like the answer, swap a key word for a close one. It can open a different path.
5. **Don't leave judgments about people to "closeness."** It can carry prejudice (Chapter 3).

## Common mix-ups

- "Similar words can be swapped with no change." They're close, but they feel and work differently.
- "King minus man plus woman equals queen, every time." It's a classic example, and it only works roughly.
- "Distance is neutral math." It's learned from human writing, so it carries society's prejudices too.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), 2024-04-01. The direction example (king, woman minus man, queen), the note that it's only rough, and the point about many directions in many dimensions. Read on 2026-11-09.
    - Tomas Mikolov and others, [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), arXiv, 2013-01-16. Word vectors catch both grammar and meaning similarity (abstract).
    - Tolga Bolukbasi and others, [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520), arXiv, 2016-07-21.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The uses (meaning search, recommendations, linking languages) are a summary of widely known uses, not confirmed in these sources. The cosine similarity note is a general explanation. Results of "Try it yourself" vary by chatbot.
