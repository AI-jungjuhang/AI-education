# What changes when you add search

<p class="ep-meta"><span>Ch. 13 · 13.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Adding search to a chatbot ==turns a closed-book test into an open-book test==.
    - Finding text close to the question, adding it in, and then answering is called **RAG (retrieval-augmented generation)**.
    - It gets better at recent facts and sources, but what it finds can be wrong or summed up badly.

## An open-book test

On a closed-book test, you answer only from what's in your head. When your memory is fuzzy, you might make something up that sounds right (hallucination, Chapter 1). On an open-book test, you can open the textbook and **look things up** as you answer.

A chatbot with search is taking an open-book test. When a question comes in, it first **finds related text**, puts it on its desk (the context window, Chapter 11), and answers while looking at it.

!!! tip "In 10-year-old words"
    Adding search turns a closed-book test into an open-book test. Looking things up can make answers more accurate, but not if it opens the wrong book.

## How it works

1. **A question comes in.** "What's our company's vacation policy?"
2. **It finds related text.** It searches policy documents or web pages for the parts closest in meaning to the question. This uses "similar meanings sit close together" from Chapter 10 (meaning-based search).
3. **It puts what it found into the context, along with the question.**
4. **The chatbot answers by reading that text.** Often it shows the sources too.

## What the original paper said

A 2020 paper by Patrick Lewis and others, *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, gave this approach its name. Here's the problem they saw. Big language models store facts inside their parameters. But they're limited at reaching that knowledge and using it precisely. And two problems were still unsolved: **showing where an answer came from**, and **keeping the knowledge up to date**. So the researchers connected the model's own memory (its parameters) to an **outside memory**, in this case Wikipedia turned into searchable vectors. A search part pulled in what was needed. They reported top results at the time on three open question-answering tasks.

## How it calls tools

Search is one kind of tool. Anthropic's tool use docs explain how tools work in general. Based on your request and each tool's description, **Claude decides on its own when to call a tool**. It sends back a structured request to call it. Then either your application runs it (client tools) or Anthropic runs it (server tools, like web search). With the web search tool, the search runs and the answer comes back **with cited sources**.

## What changes, and what doesn't

| What changes | What stays the same |
|---|---|
| It can see recent information | If what it found is wrong, the answer likely will be too |
| It can show sources | It can still sum up a source the wrong way |
| It answers based on your own documents | If it finds the wrong text, it gives a wrong answer |
| It can know things after its training date | The order of search results isn't the order of truth |

!!! note "★ Going deeper"
    - In RAG, documents are usually cut into small chunks, and each chunk is turned into a vector and stored (Chapter 10). Then it fetches **the chunks closest** to the question's vector. How you cut the chunks and how many you fetch make a big difference.
    - A web page or document it finds may hide a line like "Ignore your earlier instructions and do this" (prompt injection, Chapter 2). With search turned on, the chatbot reads text you didn't write, so the risk goes up.
    - The paper used 2020 models and Wikipedia. Today's services work differently, and they share different amounts about how their search works.

## Try it yourself

If you have a chatbot with search and one without (or a service where you can turn search on and off), compare them.

```text
Tell me about one big AI-related news story from this week,
with the source and the date.
```

1. How did the answer differ with search off and with search on?
2. Open the source link from the search answer, and use the checks from Chapter 3. Does the source really say what the chatbot claims?

## Use it today

1. **Turn on search for recent information.** Things that happened after training aren't in a plain answer.
2. **Ask for "the source and the date."** That gives you a way to check.
3. **Open the sources and check them.** See whether the chatbot's summary matches the original (Chapter 3).
4. **Don't put personal details in search questions.** Your question may be passed on to a search service (Chapter 3).
5. **Ask for two different sources.** For example: "Give me reasons for and against, each with its own source."

## Common mix-ups

- "Adding search gets rid of hallucinations." It reduces them, but doesn't remove them. It can also misread what it found.
- "If there's a source, it's true." The source itself may be wrong, or it may be summed up wrong.
- "RAG means the model learns again every time." It doesn't retrain. It finds text and adds it in at answer time. (The paper's model combined parameter memory with outside memory.)

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Patrick Lewis and others, [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), arXiv, 2020-05-22. Combining parameter memory with non-parametric memory, a vector index of Wikipedia, and top results on three open question-answering tasks come from the abstract.
    - Anthropic, [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), Claude Platform Docs. How Claude decides to call tools, client tools and server tools, and the web search tool's cited results. Read on 2026-11-09.
    - Our earlier page: [Similar meanings sit close together](../../part3/ch10/closeness.md).

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The notes on chunking and prompt injection are general explanations, not confirmed in these sources. Most services don't publish how their search works, so we didn't describe it. The open-book comparison is ours.
