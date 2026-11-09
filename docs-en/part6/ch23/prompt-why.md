# Why do context, examples, and format work?

<p class="ep-meta"><span>Ch. 23 · 23.2</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - The asking tips from Part I (context, examples, format) ==come from how AI works==. It **guesses the next words from the text in front of it**.
    - Anthropic's official guide points the same way: be clear, give reasons, show examples.
    - Some old tips **aren't needed anymore**. Once you know the reason behind the tips, you can tell which.

## The idea in one line

In Part I (1.1.1), you learned that a chatbot looks at the text in front of it and picks what comes next. So **if the text in front changes, the likely next words change too.** Context, examples, and format are all ways to put better text in front of it.

## Four reasons the tips work

**1. Be clear and direct.** Anthropic's guide says to treat Claude like **a brilliant new employee** who doesn't know your team's ways yet. Its test is simple. Show your request to a coworker who knows little about the task. If they'd be confused, Claude will be too. Gaps tend to get filled with guesses (that's how made-up answers happen). The clearer you are, the less room there is to guess.

**2. Give the reason.** The guide's example, in short: "never use ellipses" works less well than explaining that the text will be **read aloud by a voice program**, which won't know how to say them. Once Claude knows why, it can apply the idea to similar cases on its own.

**3. Show examples.** The guide calls examples one of the most reliable ways to set format, tone, and structure. It says examples should be **relevant** (close to your real use), **varied**, and **set apart** with tags. It suggests 3 to 5. They need to vary because if they're all alike, Claude may copy patterns you didn't mean, like they all being the same length.

**4. Mark the parts.** If a long request mixes instructions, material, examples, and input, wrap each part in its own tag. The guide's examples use tags like `<instructions>` and `<context>`. Clear, consistent names are what matter.

```text
<instructions>Summarize the material below in 3 lines. Use only what's in it.</instructions>
<material>
(paste here)
</material>
```

## Tips you can drop

The official best practices keep a list of advice that **was good once but isn't needed now**, because models got better:

- **ALL CAPS and "IMPORTANT!!"** Current models follow a plain line. Too much emphasis makes Claude apply the rule too widely. A rule that must never bend should be a hook (Chapter 17) or a deny rule, not shouting.
- **"Think hard" or "be thorough."** These aren't magic words. They're ordinary text. How deeply Claude thinks is set by the **effort level** (the second page of 23.3).
- **"Keep going, don't be lazy."** Current models usually carry on without being told. Lines like that can lead to over-work.

The docs say one thing is still worth adding: **a way to check whether the job is done.** That's section 23.4.

!!! tip "In 10-year-old words"
    AI guesses what comes next from the words in front of it. Put good words in front (context, examples, format), and you get better answers.

!!! note "★ Going deeper"
    The guide warns that when a tip was measured on one model, you should test it on your own tasks before using it on another. Prompt tips can stop working when the model changes. Treat this page's tips as dated too (2026-11-09).

## Try it yourself

Ask for the same thing twice and compare.

1. First, ask briefly: "Summarize page 1.1.2."
2. Then ask like this, and see how the two results differ:

```text
This summary will be used as video captions, so each sentence must be 8 words or fewer. Write it like this example.
<example>Tokens are small pieces of text.</example>
<material>(paste the page 1.1.2 text)</material>
```

## Use it today

1. **Add one sentence of reason** to each request: where the result will be used.
2. **If format matters, show 2 or 3 examples** instead of describing it.
3. **Write one plain, clear line instead of shouting.** If it still isn't followed, make it a hook.

## Common mix-ups

- "Prompts have secret magic words." It's about giving more information, not spells.
- "Examples always help." With only one example, it copies that one shape. Give a variety.

## Sources and date checked

- **Date checked:** 2026-11-09. Models and guides change quickly.
- **Source of facts:** [Anthropic docs: Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) and [Claude Code best practices](https://code.claude.com/docs/en/best-practices) ("What you can stop doing"). Read on 2026-11-09.
- This page rereads Part I (how to ask) and 1.1.1 (guessing the next word) through the lens of how AI works.
