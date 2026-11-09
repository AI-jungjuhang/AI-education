# Features: the ideas inside a model ★

<p class="ep-meta"><span>Ch. 19 · 19.1 · Deeper</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Inside a model, ==one idea is spread out over many tiny parts, and each part helps with many ideas==.
    - Researchers found groups of parts that tend to switch on together. They call each group a **feature**, and matched them to ideas we can name.
    - They found millions of features in one Claude model. Some switch on for the same idea in many languages, and even in pictures.

## Letters, words, sentences

Think about language. You combine **letters** to make **words**, and words to make **sentences**. To understand a sentence, you don't stare at each letter.

Anthropic explains the inside of a model in a similar way. Tiny parts called **neurons** join up to make **features**. Features join up to make what the model is "thinking" at a moment. To understand it, looking at features works much better than looking at single neurons.

!!! tip "In 10-year-old words"
    Letters make words, and words make sentences. In a model, neurons make features, and features make thoughts.

## Why one neuron isn't enough

Anthropic's post says that inside an AI model, **each idea is spread across many neurons, and each neuron helps with many ideas**. So you can't point at one neuron and say, "That's the potato neuron." It's like trying to understand a sentence from a single letter.

So the researchers used a method called **dictionary learning**. It finds **patterns of neuron activity that show up again and again**. Those patterns are **features**. With them, you can describe what's going on inside as **a handful of active features**, not thousands of neurons. (This ties back to Chapter 10: meanings show up as directions.)

## Millions of features

In May 2024, Anthropic said it had found **millions of features** inside a model called Claude 3.0 Sonnet. A feature switches on when the model reads about its idea, or sees a picture of it.

- **The Golden Gate Bridge feature:** it fires on the bridge's name in English. It also fires on talk about the bridge in **Japanese, Chinese, Greek, Vietnamese, and Russian, and on pictures** of it. So one feature can work across many languages, and across both words and pictures.
- **Odder ones too:** a feature for bugs in code. One for unfair ideas about which jobs are for men or women. One for talk about keeping secrets.
- The researchers could even measure a kind of **"distance"** between features. Features with similar neuron patterns sit close. Near the Golden Gate Bridge feature, for example, were features for Alcatraz Island and the 1906 earthquake.

## Turn a feature up, and behavior changes

Here's the most striking part: **turning a feature up changes how the model acts**. The researchers turned up the Golden Gate Bridge feature. Then Claude kept **bringing up the bridge**, even when the question had nothing to do with it. Asked to describe itself, it said it was the bridge. Anthropic shared this as a research demo called **"Golden Gate Claude"** for a short time, about 24 hours. It's no longer available.

The researchers say this was a careful change made right inside the model. It wasn't a prompt, and it wasn't new training. So features aren't just things to look at. They're **parts that really shape what the model does**.

!!! note "★ Going deeper"
    - The post says this discovery **could, in the future, help make AI models safer**. That's a hope, not a solved problem. The researchers also found features tied to things like flattering users untruthfully, deception, and power-seeking. Turning up a "scam email" feature made the model write a scam email, overriding its training.
    - The post is honest about limits. The features found are **a small subset** of all the ideas the model learned. Finding them all with current methods would cost too much. And knowing which features exist **doesn't tell you how the model uses them**.
    - An earlier step came in October 2023, when the same method worked on a tiny "toy" model, finding features like uppercase text and DNA sequences. The Sonnet work scaled that up.
    - 3Blue1Brown's lesson (Chapter 10) explains that high-dimensional space has room for a huge number of different directions, so many meanings can fit without crowding. Feature research checks whether ideas like this hold up inside real models.

## Try it yourself

**Make your own feature map.** On paper:

1. Write "potato" in the middle.
2. Around it, write 6 ideas it brings to mind (food, farming, french fries, Ireland, price, and so on).
3. Circle two ideas that would also "light up" for words other than "potato." (For example, "food" also lights up for "sweet potato.")

One idea lights up for many words, and one word lights up many ideas. That's a bit like how features and neurons relate. (It's only a comparison.)

## Use it today

1. **Be careful saying "AI understands ideas."** It has inside patterns that match ideas. That's not the same as the way people understand.
2. **Make use of ideas that cross languages.** Asking in another language can reach the same idea. But the token gaps between languages (Chapter 1) and differences in training material are still there.
3. **Know that the bridge-obsessed model was made on purpose, for a demo.** Still, certain words in your question can strongly switch on certain ideas.
4. **Check claims you hear.** Simple stories like "AI has a neuron for X" can be overstated.
5. **For news about this research, read the original post.** News stories tend to puff it up, like "Scientists read the AI's mind!"

## Common mix-ups

- "There's a separate potato neuron inside the AI." Ideas are spread across many neurons.
- "They found features, so we understand AI now." Finding millions is a start. Most is still unknown.
- "You can still try Golden Gate Claude." It was a research demo, offered for a short time only.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model), 2024-05-21. Ideas spread across many neurons, dictionary learning, millions of features in Claude 3.0 Sonnet, the multilingual and multimodal Golden Gate Bridge feature, abstract features, distance between features, safety-related features, and the stated limits. Read on 2026-11-09.
    - Anthropic, [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude), 2024-05-23. Turning up a feature changes behavior; a short-lived research demo that's no longer available. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read the blog posts, not the original papers. Researchers debate whether features found this way are truly "the ideas the model uses," and we didn't cover that debate. The feature map activity is a comparison.
