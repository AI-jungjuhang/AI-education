# Habits that save memory space ★

<p class="ep-meta"><span>Ch. 23 · 23.1 · Deeper</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - There are four tools for tidying the desk: ==`/clear` (start fresh), `/compact` (summarize), partial summaries, and helpers (read elsewhere)==.
    - When a chat is summarized, **some things survive and some get lost**. Put important rules where they survive.
    - The goal isn't to save space for its own sake. It's to keep Claude focused.

## Four tidying tools

| Tool | When | What it does |
|---|---|---|
| `/clear` | You're moving to a totally different task | Clears the desk. The old chat won't get in the way of the next task |
| `/compact` plus what to focus on | Same task, but the chat got long | Swaps the chat for a summary. You say what to keep |
| `/rewind`, then a summarize option | The early part matters, but the later part is messy (or the other way around) | Summarizes only the part before or after the message you pick |
| A helper (subagent) | Research that means reading a lot | The reading happens elsewhere; you get back a summary |

You can steer `/compact`. The docs' example is "focus on the auth bug fix." Then the summary keeps what you chose, instead of what the automatic pass guesses is important.

```text
/compact keep the decisions for the page I'm writing and the links I haven't checked yet
```

One catch: on a long chat, `/compact` is itself a big request, because it reads the whole conversation to summarize it.

## What survives a summary

Here's the docs' table, in plain words:

| After the summary | How |
|---|---|
| CLAUDE.md at the top of the project | Read again from the file |
| Auto memory | Read again from the file |
| Skill descriptions | Rebuilt from your current skills |
| Files Claude read or changed | Up to 5 are read again, newest changes first. A file over 5,000 tokens comes back as just its path |
| Skills Claude already used | Put back, up to 5,000 tokens each and 25,000 in total. The oldest drop first |
| **Instructions you only gave in chat** | **Can get lost in the summary** |

That leads to a rule: **if Claude must keep following a rule, don't just say it in chat. Write it in the CLAUDE.md at the top of your project.** The docs warn that CLAUDE.md files in subfolders, and rules tied to certain files, can get summarized away too. If a rule must last, move it to the top-level CLAUDE.md.

Long skills get cut to fit, and the cut keeps the start. So **put the most important instructions near the top of SKILL.md.**

## Drop the old advice

People used to say "manage your context window aggressively." The official best practices now say that's outdated. Most current models have a big window and summarize on their own, so running out is rare. But `/clear` between tasks is still worth it.

So keep these habits light. Not "save every scrap," but **"clear when the task changes, and keep rules in the right place."**

The docs add one more tip. If you've corrected the same thing **twice** and it's still wrong, don't try a third time. The chat now holds two failed tries that Claude keeps re-reading. Run `/clear` and write one better prompt that includes what you learned.

!!! tip "In 10-year-old words"
    When you switch tasks, wipe the whiteboard. Rules you must always follow go on the wall poster (CLAUDE.md), not the whiteboard.

!!! note "★ Going deeper"
    - `/autocompact` lets you set how full the desk gets before the automatic summary runs.
    - A `SessionStart` hook can add text back in right after a summary. If a note must come back every time, use a hook. It's the same idea as the hooks page in Chapter 17: a promise that doesn't depend on the AI's judgment.
    - `/clear oauth-migration` gives the chat you're leaving a name, so you can come back to it later.

## Try it yourself

1. In the middle of a chat, check `/context`. Then run `/compact keep only the decisions for what I'm working on`.
2. Check `/context` again to see how much room you got back.
3. Pick one rule you only said in chat. Does Claude still follow it after the summary? If not, move it into CLAUDE.md.

## Use it today

1. **New task: `/clear`. Same task, too long: `/compact` plus what to keep.**
2. **Put lasting rules in the top-level CLAUDE.md, not in chat.**
3. **Put the most important lines at the top of each skill.**
4. **After two failed corrections, start fresh with a better prompt.**

## Common mix-ups

- "A summary keeps everything." Summaries shrink things, so details can get lost.
- "`/clear` erases CLAUDE.md too." No. A new chat reads CLAUDE.md again.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. Rebuilding skill descriptions after a summary needs v2.1.304 or later. The token limits may change when the docs change.
- **Source of facts:** [Official docs: Context window, what survives compaction](https://code.claude.com/docs/en/context-window), [Best practices](https://code.claude.com/docs/en/best-practices) (including "What you can stop doing"), and [Checkpointing](https://code.claude.com/docs/en/checkpointing). Read on 2026-11-09.
