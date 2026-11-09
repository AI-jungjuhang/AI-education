# Summarize

<p class="ep-meta"><span>Ch. 5 · 5.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Summarizing is one of the most common AI jobs. But ==things that aren't in the original can slip in==.
    - Set the reader, the length, and what to keep (numbers, dates), and you get a useful summary.
    - Check the summary against the original. For long text, summarize in parts, then combine.

## The blurb on the back of a book

Have you ever bought a book because of the blurb on the back, then found the book was about something else? A summary passes the content along to someone who hasn't read the original. If the summary is wrong, that person ends up believing something wrong.

AI summarizes fast. But as Chapter 1 showed, it continues text with likely words. So **words that aren't in the original can slip in**.

!!! tip "In 10-year-old words"
    A summary is like the blurb on the back of a book. It shouldn't say anything the book doesn't.

## What to set when you ask for a summary

```text
Summarize the text below.
- Reader: my manager, who hasn't read it
- Goal: to see what we need to decide at the meeting
- Length: 5 sentences or fewer
- Must keep: numbers, dates, and the names of who's in charge
- Don't add anything that isn't in the original. If the original is
  unsure about something, say it's unsure.
<text>
(paste here)
</text>
```

| What to set | Why |
|---|---|
| Reader | Different readers care about different parts |
| Goal | A summary for making a decision differs from one for understanding |
| Length | If you don't set it, you get an in-between length |
| What to keep | Numbers and dates are easy to change while summarizing |

## Summarizing long text

Very long text is hard to summarize in one go. Anthropic's guide gives tips for long documents (20,000 tokens or more). Put the long material at the top, and put your question and instructions at the end. The guide says that in its tests, putting the question at the end improved answers by up to 30%. It also suggests asking Claude to first pull out the relevant parts as exact quotes, then do the task. That helps it focus on what matters and ignore the rest.

You can also summarize in parts.

1. Split the text by chapter or section.
2. Summarize each part on its own.
3. Put the part summaries together and make one overall summary.

## Checking a summary

| What to check | How |
|---|---|
| Anything that isn't in the original? | For each summary sentence, find the sentence in the original that backs it up |
| Are numbers and dates right? | Put them side by side with the original |
| Anything important missing? | Skim the original's headings and first sentences and compare |
| Did the tone shift? | Check that "might be" didn't turn into "is" |

```text
For each sentence in the summary above, add the sentence from the
original that supports it, in quotation marks. If you can't find
support, mark that sentence "no support."
```

!!! note "★ Going deeper"
    - A 2023 study by Nelson Liu and others, called "Lost in the Middle," found that models did worst when the key information sat in the middle of a long input. They did best when it was at the beginning or end. Anthropic's docs also describe context rot: accuracy drops as text grows. So splitting long text into parts is often the safer choice.
    - Researchers also study hallucinations in summaries. A summary has one big advantage: the original is right there, so it's easy to check. Chapter 21 covers how hallucinations are measured.

## Try it yourself

Pick an article or report and ask for two summaries.

1. "Summarize this in 3 lines."
2. The template above (with reader, goal, length, and what to keep).

Check both against the original. Which one had more things that weren't in the original? Were the numbers right?

## Use it today

1. **Save a summary template.** It has four slots: reader, goal, length, and what to keep.
2. **Add "don't add anything that isn't in the original."** One line saves a lot of trouble.
3. **Put the long text on top and your question at the bottom.** That's what the guide recommends.
4. **Check every summary against the original at least once.** Especially numbers and dates.
5. **Check with "add the supporting sentence."** Be suspicious of any sentence marked "no support."

## Common mix-ups

- "The original is right there, so the summary can't be wrong." Even with the original, made-up words can slip in.
- "The shorter the summary, the better." Too short, and key numbers and conditions drop out.
- "I can paste in long text all at once." Accuracy can drop as text grows, so splitting it up often works better.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Claude Platform Docs. The section "Long context prompting": long data at the top, the question at the end, and pulling out quotes first. "Up to 30 percent" is the guide's own test result. Read on 2026-11-09.
    - Nelson F. Liu and others, [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172), arXiv, 2023-07-06. We summarized the abstract.
    - Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), Claude Platform Docs. Context rot. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstract of the Liu study. Its results are for the models of 2023, and we haven't checked whether today's models behave the same way. Summarizing in parts and the checking table are our own practical tips.
