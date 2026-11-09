# Read and sort out long documents

<p class="ep-meta"><span>Ch. 6 · 6.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - For long reports, papers, or contracts, ==decide your question first, and have it pull out the supporting sentences== before it sums things up.
    - Put the material on top and your question at the bottom.
    - The longer the text, the more AI can miss in the middle. So split it up or check the evidence.

## Finding a book in a big library

If you walk into a library and say "Look into these books," you won't know where to start. If you say "Find the parts about the history of the potato," you can go straight to them.

Long documents work the same way. "Sort this out" is vague, so you get an ordinary summary. Once you decide **what you want to know**, you get something useful.

!!! tip "In 10-year-old words"
    When you hand it a long book, first tell it what to look for.

## Four steps

**Step 1: Decide your question.** Write down in a sentence or two what you want to learn from the material.

**Step 2: Material on top, question at the bottom.** Anthropic's guide says to put long material (20,000 tokens or more) near the top of your prompt and your question and instructions at the end. It says that in its tests, putting the question at the end improved answers by up to 30%.

**Step 3: Pull out supporting sentences first.** For long documents, the guide suggests having Claude first quote the relevant parts word for word. That helps it focus on what matters.

**Step 4: Sum up.** Have it answer using only the quotes it pulled out.

```text
<material>
(the full report)
</material>

Read the material above and answer this question.
Question: What are the three biggest risks in this plan?
Steps: 1) First, quote the sentences from the material that relate to
the question, word for word, and number them.
2) Then answer using only those numbered quotes.
If a quote can't back something up, don't write it. Say "not in the material."
```

## Comparing several documents

When there are several documents, give each one a label so they don't get mixed up. Anthropic's guide shows wrapping each document in its own tag, along with where it came from.

```text
<document index="1" source="2025 business plan">...</document>
<document index="2" source="2026 business plan">...</document>
Make a table of what changed between the two documents. Next to each item,
say which document and which sentence it comes from.
```

## The longer the text, the more care it needs

One study found that language models can do much worse when the key information sits in the middle of a long text (2023, with the models of that time). Today's models have likely improved, but it's hard to say the problem is completely gone. So for things that matter, check like this:

- **Ask in parts.** Asking about each chapter on its own means less gets missed.
- **Check the supporting sentences.** Find them in the original yourself.
- **Ask the same question with the documents in a different order.** If the answer changes, it needs checking.

!!! note "★ Going deeper"
    - Another way to handle long documents is to cut them into chunks and pull in only the chunks you need. This is called **retrieval-augmented generation (RAG)**. Part IV covers it.
    - When you upload a file, it may be turned into text. A PDF may be handled as both page images and text. (This differs by service and file type.) Tables and charts can get scrambled along the way, so check the results against the original when tables matter.
    - Anthropic's docs say that even with a big context window, accuracy can drop as the text gets longer (context rot). Choosing what goes in matters more than stuffing in as much as you can.

## Try it yourself

Pick a long text, like a report of 10 pages or more, or a set of articles.

1. First, ask "Summarize this" and get a summary.
2. Then pick one question and use the "supporting sentences first" template above.
3. Compare the two. Which one helped more with your question? Were the supporting sentences really in the original?

## Use it today

1. **Start by writing your question in one sentence.** You'll likely get better results than with "sort this out."
2. **Material on top, question at the bottom.** Just changing the order can make a difference.
3. **Get numbered supporting sentences.** They make checking easy.
4. **For contracts and legal papers, use AI only to flag risks.** Leave the final call to an expert, or read it yourself.
5. **Blank out personal and secret details before you upload.** Chapter 3 covers this.

## Common mix-ups

- "If I upload a long document, it understands all of it." The longer it is, the more it can miss.
- "Reading the summary is enough." For important decisions, read the relevant parts of the original.
- "I gave it the document, so it won't make things up." Material helps, but it doesn't stop made-up answers completely. Check with the supporting sentences.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Claude Platform Docs. The section "Long context prompting": material on top, question at the end, quotes first, and structuring several documents. "Up to 30 percent" is the guide's own test result. Read on 2026-11-09.
    - Nelson F. Liu and others, [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172), arXiv, 2023-07-06. We summarized the abstract.
    - Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), Claude Platform Docs. Context rot. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The Liu study tested 2023 models. We haven't checked whether today's models behave the same. How each service converts files varies, so that part is general. The four steps are our summary, based on the guide.
