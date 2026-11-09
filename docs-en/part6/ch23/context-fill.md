# What fills up its memory space?

<p class="ep-meta"><span>Ch. 23 · 23.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - The **context window** from Part III is Claude's working memory. It holds ==everything Claude can see in this conversation==.
    - It's not just what you typed. It also holds things loaded at the start, files Claude read, and tool results.
    - With `/context`, you can see for yourself what's filling your conversation's memory.

## It only sees what's on the desk

In Part III, you learned that AI forgets everything when a chat ends. All it can see is what's on its desk (the context window). So if you know what's on the desk, you can see why the AI acts the way it does. A full desk leaves no room for new papers. A messy desk makes the important ones hard to find.

## What lands on the desk

The official docs list what goes into Claude Code's context window:

| When | What lands there |
|---|---|
| **Before you type anything** | CLAUDE.md, auto memory, MCP tool names, and skill descriptions |
| **While Claude works** | Each file it reads, rules that load with matching files, and hook output |
| **When a helper (subagent) does the research** | Big file reads happen on the helper's own desk. Only a summary comes back to yours |

So the more skills and MCP servers you add (Chapter 17), the fuller the desk is **before you say a word**. Only names and descriptions load at the start, so each is small. But unused tools add up. That's why the plugin page in Chapter 18 said to check the context cost before you install.

## Look at your own desk

Type `/context`. It shows how much of the desk each kind of thing takes up, as colored blocks, with ideas for what to trim. It also shows which CLAUDE.md and auto memory files were loaded. To edit those memory files, use `/memory`.

## Even with a bigger desk

The docs say many current models support a **1 million token** window. With a desk that big, you'll rarely run out of room. **But big doesn't mean you can skip tidying.** The docs say `/clear` between tasks is still worth doing, because a focused context gives better answers and costs less.

Here's why it costs more. Every message sends the **whole conversation** again. So if one chat holds three unrelated tasks, the fourth task pays to re-read all three, every turn.

!!! tip "In 10-year-old words"
    AI can only see what's on its desk. A big desk is nice, but if it's messy, it can't find things.

!!! note "★ Going deeper"
    - When the desk gets close to full, Claude Code **compacts** the chat on its own: it swaps the conversation for a summary and keeps going. The next page shows what survives that.
    - The point where this kicks in depends on the model and settings. The docs keep a table of default limits. We don't copy the numbers here because they change.
    - The docs also say subagents are no longer mainly for saving room. They're still good for parallel work, keeping noisy output out of your way, and fresh reviews. But each one costs extra tokens.

## Try it yourself

1. Open Claude Code and type `/context` before you say anything. You'll see part of the desk is already full.
2. Ask Claude to read one file. Type `/context` again and see which block grew.
3. If you made skills or MCP connections in Chapter 17, find how much of the desk they take at the start.

## Use it today

1. **If answers get fuzzy or the same mistake repeats, check `/context` first.**
2. **Turn off or remove skills, MCP servers, and plugins you don't use.**
3. **Use `/clear` when you switch to an unrelated task.** It costs nothing.
4. **Hand big reading jobs to a helper when it fits.** Just remember helpers cost tokens too.

## Common mix-ups

- "With a big desk, I can keep one chat going forever." Longer chats cost more on every message and can lose focus.
- "Only what I typed is on the desk." No. Some things load before you type a word.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. Which models have a 1M window, and when compacting starts, depend on the model and settings.
- **Source of facts:** [Official docs: Explore the context window](https://code.claude.com/docs/en/context-window) and [Best practices](https://code.claude.com/docs/en/best-practices). Read on 2026-11-09.
- This page builds on Part III (context windows and tokens).
