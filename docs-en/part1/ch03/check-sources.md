# How to check sources

<p class="ep-meta"><span>Ch. 3 · 3.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Check a source the chatbot gives you in three steps: ==Is it real? Does it say that? Can you trust it?==
    - Asking for sources is good. But a chatbot can make up the sources too.
    - Don't stop at one place. Check somewhere else as well.

## When a friend says "I saw it online"

A friend says, "I read online that eating potatoes makes you taller." What do you do? You ask, "Where did you see that? Send me the link." And even with the link, you open it to see if it really says that, and who wrote it.

Do the same when a chatbot says "according to a study..." As Chapter 1 showed, it continues text with likely words. So it can make up a study or a link that looks real but doesn't exist.

!!! tip "In 10-year-old words"
    Ask three questions: "Where did you see it?" "Did you open it?" "Does anyone else say so?"

## Three steps to check

**Step 1: Is it real?**

- Does the link open? For a book or paper, search the title and see if it really exists.
- Do the author, year, and title match what the chatbot said?

**Step 2: Does it say that?**

- Is the chatbot's claim really written in that source? Open it and search for a key word (Ctrl+F, or Cmd+F on a Mac).
- Have any numbers or quotes been changed a little?

**Step 3: Can you trust it?**

- Who wrote it? A research group, a government office, a news outlet, or one person's blog?
- When was it written? The information may be out of date.
- Do other trustworthy places say the same thing?

## Read sideways

Researchers at Stanford, Sam Wineburg and Sarah McGrew, watched how people judge websites. Professional fact checkers did something different from the others. When they landed on a site they didn't know, they didn't read it top to bottom. They quickly left it, opened new tabs, and looked up who was behind it. The researchers called this **lateral reading**, or reading sideways. You can do the same with a source a chatbot gives you. Before you read on, search in another tab: "Who runs this, and can I trust them?"

## Make the chatbot show its evidence

Anthropic's guide to reducing hallucinations suggests a way to make answers easy to check. Have the chatbot attach a quote and a source to each claim. If it can't find a quote that backs a claim, it should take that claim back.

```text
Answer using only the material below. After each claim, add the exact
sentence from the material that supports it, in quotation marks.
If you can't find support in the material, don't make the claim.
Write "not in the material" instead.
<material>
(paste here)
</material>
```

When it answers from material you pasted in, the source is right in front of you. That makes checking easy.

!!! note "★ Going deeper"
    - When a chatbot uses web search, the pages it pulls in become its evidence. But it can still sum them up wrong or quote the wrong part. Use the same three steps on search-powered chatbots too. Part IV covers search and tools.
    - Anthropic's guide lists ways to reduce hallucinations. It also says these methods lower hallucinations a lot but don't get rid of them. Always check important information.

## Try it yourself

Ask a chatbot this:

```text
Give me 3 trustworthy sources about the nutrition of potatoes,
with titles and links.
```

Open each link and run the three steps: Is it real? Does it say that? Can you trust it? Did any link fail to open, or say something different? Count how many pass. That gives you a feel for how much to trust a chatbot's sources.

## Use it today

1. **Always open the source.** If it won't open, it may be made up. If it opens, you still need to check that it says what the chatbot claims.
2. **Find the key sentence in the original.** With Ctrl+F (or Cmd+F), it takes seconds.
3. **Read new sources sideways.** For a site you don't know, search its name in a new tab and find out who runs it.
4. **The more it matters, the more you read the original yourself.** Use the chatbot as a guide that points you to the original.
5. **Check the date.** If you need up-to-date facts, see when it was written.

## Common mix-ups

- "It has a link, so it's true." Even if the link opens, it may say something different from what the chatbot said.
- "If I ask for sources, it won't make things up." It can make up the sources too. That's why you open them.
- "If it's a famous site, I can trust it all." Famous sites can be wrong or out of date too. Look at who wrote it and when.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Sam Wineburg and Sarah McGrew, [Lateral Reading: Reading Less and Learning More When Evaluating Digital Information](https://doi.org/10.2139/ssrn.3048994), Stanford History Education Group working paper, SSRN, 2017-10-25. A shorter version appeared in Teachers College Record in 2019.
    - Anthropic, [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations), Claude Platform Docs. "Verify with citations," and the reminder to always check critical information. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We confirmed the paper's title, authors, and date in the DOI record. We could not open the full paper from our work environment. Our description of lateral reading comes from summaries of the study, so it still needs checking against the paper itself. The three-step check is our own practical summary.
