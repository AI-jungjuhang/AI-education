# A chatbot guesses the next word

<p class="ep-meta"><span>Ch. 1 · 1.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A chatbot's one job is to ==pick the next word==.
    - It does that job again and again, and the words pile up into an answer.
    - That is why the same question can get a different answer each time.

## A game you already know

Your friend says, "For lunch I'm getting a burger and..." and then stops. What comes next? Fries, probably. Maybe a shake or onion rings. Nobody says "a spaceship."

A chatbot plays this same game. It looks at all the text so far and picks one word to come next. Then it looks again, this time with the new word included, and picks another. It keeps going until the answer is done. Word by word, that becomes a sentence, and then a whole email.

## It scores every choice, then draws one

Before it picks, the chatbot gives each possible next word a score. The score says how well that word fits.

| Next word | Chance (example) |
|---|---|
| fries | 40% |
| a shake | 20% |
| onion rings | 10% |
| a spaceship | almost 0% |

We made these numbers up to show the idea. A real model scores tens of thousands of choices, not four.

Then it draws one word from the list, a bit like rolling dice that are weighted toward the high scores. High-scoring words come up most of the time. But now and then a lower one gets picked. (Some apps set the chatbot to always take the top word instead.) This is why you can ask the same thing twice and get two different answers.

## Repeat, and you get an answer

```text
Start:   "The sky is blue because"
Step 1:  "The sky is blue because"           → "sunlight"
Step 2:  "The sky is blue because sunlight"  → "hits"
Step 3:  "... because sunlight hits"         → "the"
...      (and so on, until it decides to stop)
```

Each word it picks becomes part of the input for the next pick. It never goes back to change a word. So if it takes a slightly wrong turn early on, the rest of the answer can follow that wrong turn.

## So how does it hold a conversation?

It helps to think of two stages of learning.

1. **Read and copy.** The model reads a huge amount of text and practices one thing: guessing what comes next. A model that has only done this stage is like super-powered autocomplete. Ask it a question, and it may just keep writing more text that looks like the page the question came from.
2. **Learn to be a helper.** Next, it studies example conversations that people wrote, where a helpful assistant answers questions well. It also learns from people rating its answers. Now, when you ask something, it answers you.

!!! tip "In 10-year-old words"
    A chatbot is like a friend playing "finish my sentence" over and over, really fast, until a whole answer comes out.

!!! note "★ Going deeper"
    - The model does not really predict whole words. It predicts **tokens**, which are small chunks of text. The next page is about tokens.
    - A setting called **temperature** changes how the scores are used. Low temperature makes the top choice win almost every time, so answers stay alike. High temperature gives lower-scoring words more of a chance, so answers vary more and can drift.
    - Making text one token at a time, where each new token is fed back in, is called **autoregressive generation**.
    - "One word at a time" describes the output, not everything inside. In 2025, Anthropic researchers looked inside their model Claude while it wrote rhyming poems. They found it picked a rhyme word for the end of a line before writing that line, then wrote toward it.

## Try it yourself

Ask a chatbot the same question three times: "Give me 5 names for a cozy cafe that's busiest on rainy days." Are the lists the same? Use the score table above to explain why they changed.

## Use it today

- **Ask three times, and look at what repeats.** Check the parts that show up in all three answers first. Repeating does not prove something is right. But a part that changes every time deserves a closer look.
- **Spell out your situation.** The chatbot picks each word based on the text before it, and that includes your question. The more detail you give, the more the scores shift toward words that fit. That makes an off-target answer less likely.

    ```text
    Weak:    Write some marketing copy.
    Better:  Write 3 Instagram captions for a new strawberry latte at a cafe
             near a college campus. Keep each one under 15 words.
    ```

- **If it goes off track, start a new chat.** Every word it has already written pulls the next words along. So it often works better to fix your question and start fresh than to ask for one change after another.

## Common mix-ups

- "A chatbot searches the internet and copies the answer." That is not what it does by default. It makes up the next words from patterns it learned. (Some chatbots can also use a search tool. Part IV covers that.)
- "A chatbot knows the right answer." It does not check what is true. It picks ==a likely next word==. That gap leads straight to the next big topic: hallucination.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Andrej Karpathy, [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), YouTube, 2023-11-23. Chapters "How do they work?" (00:11:22: the network predicts the next word) and "Finetuning into an Assistant" (00:14:14: the same training, with conversations written by people).
    - Andrej Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), YouTube, 2025-02-05. Chapters "inference" (00:26:01: sample a token, add it, repeat) and "Llama 3.1 base model inference" (00:42:52: a model with only pretraining is "a token autocomplete," not yet an assistant).
    - 3Blue1Brown (Grant Sanderson), [Transformers, the tech behind LLMs](https://www.3blue1brown.com/lessons/gpt), 2024-04-01. Predicting a probability for each possible next chunk, sampling, adding it, and repeating. Also explains temperature.
    - Anthropic, [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model), 2025-03-27. The rhyming poem finding in "Going deeper."

- **Date checked:** 2026-11-09
- **Status:** First draft, waiting for the author's review.
- **Note:** We checked the video titles and dates on YouTube. We could not watch the videos from our work environment. We matched the content against an unofficial, auto-generated transcript on the third-party site Rosetta ([talk](https://rosetta.to/u/andrejkarpathy/1hr-talk-intro-to-large-language-models), [deep dive](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt)), which may contain errors.
