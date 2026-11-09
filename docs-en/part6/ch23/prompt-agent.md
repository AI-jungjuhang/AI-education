# How is handing off a job different? ★

<p class="ep-meta"><span>Ch. 23 · 23.2 · Deeper</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Asking a question and **handing off a job** are different. You need to tell Claude what it can't learn from the files.
    - A good handoff says ==where to look, what's wrong, and what "done" looks like==.
    - Don't describe what you have. Hand it over: the file, the screenshot, the command output.

## What AI can't see when you hand off a job

Claude Code can read the files in your folder. It can't read your mind. The official best practices say current models are very good at reading code. What they can't find is information that **was never in the folder**: a decision your team made in a meeting, or steps that live only in one person's head. Without it, Claude guesses. As Part I showed, guesses can sound right and still be wrong.

## Vague and clear requests

Here's the docs' idea, reworked for a video channel:

| Vague | Clear |
|---|---|
| "Make a video script." | "Write a 60-second shorts script based on docs-en/part1/ch01/tokens.md. Don't add anything that's not in the page. Mark any numbers as examples. Save it to video/shorts-en/002-tokens/script.md." |
| "Fix the page." | "On page 16.2, check whether the 3 links in 'Sources and date checked' open. Just list the ones that don't. Don't change anything." |

A clear request has three parts:

1. **Where to look:** the file name or folder
2. **What's wrong, and what "done" looks like:** the problem and how you'll know it's fixed
3. **What not to do:** things it must not touch

The docs add one more: if you prefer one of two reasonable ways, say so up front. Claude can't read your preference from the code.

## Hand over what you have

Handing it over is more exact than describing it.

- **A file:** type `@` and the path to put its contents in your message.
- **A screen:** paste a screenshot.
- **Command output:** pipe it in, like `cat error.log | claude -p "what's going on here"` (Chapter 16).

## You set the size of the job

The docs explain something interesting. Claude tends to read a request carefully and build **the smallest thing** that fits, because it can't tell how much you were hoping for. If you want more, say so. One phrase the docs say still helps is `be ambitious`. For example:

```text
Expand the "Try it yourself" section on this page. Be ambitious: add help for 3 places beginners might get stuck, and a way to check if they got it wrong.
```

This isn't asking Claude to think harder. It's telling it **how big the job is**.

## When researching: "read first, then answer"

To cut down on made-up answers about code, Anthropic's guide suggests telling Claude **never to guess about files it hasn't opened**. If you name a file, it should read it before answering. You can write it like this:

```text
Before you answer, open and read any file I mention. If you haven't opened something, say you don't know.
```

!!! tip "In 10-year-old words"
    When you hand off a job, say where to look, what done looks like, and what not to touch. AI can't see inside your head.

!!! note "★ Going deeper"
    - Not every request needs to be exact. The docs say a loose question like "What would you improve in this file?" is fine when you're exploring. You'll just correct a bit more along the way.
    - Before you write something down for Claude, the docs suggest two questions: could it find this by reading the code, and would it actually look? If both are yes, leave it out.
    - Requests you make again and again can become a skill (Chapter 17). Facts it always needs can go in CLAUDE.md (Chapter 16). Then you don't have to write them every time.

## Try it yourself

1. Pick one job you recently gave an AI.
2. Check it for the three parts: where, what done looks like, what not to do.
3. Fill in what was missing, ask again, and compare with the first result.

## Use it today

1. **Write three lines when you hand off a job:** where, what done looks like, what not to do.
2. **Hand things over with `@file` or a screenshot** instead of describing them.
3. **If the size of the result matters, give a number.** For example, "help for 3 places."

## Common mix-ups

- "A longer request is a better request." Length doesn't matter. What matters is whether it has the information the AI can't get.
- "The AI already knows the whole folder." It can learn the layout by reading. But your rules, your preferences, and what "done" means have to come from you.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. Whether a phrase like `be ambitious` helps can change with the model and over time.
- **Source of facts:** [Claude Code best practices: Tell Claude what it can't see; Write a specific prompt](https://code.claude.com/docs/en/best-practices) and [Anthropic docs: Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (cutting down made-up answers in agent coding). Read on 2026-11-09.
