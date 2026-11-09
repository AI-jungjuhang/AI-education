# Subagents share out the work

<p class="ep-meta"><span>Ch. 17 · 17.4</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A subagent is ==a helper AI with its own workspace (its own context)==. It does a job and sends back **just a summary**.
    - Your desk doesn't get cluttered, so your conversation doesn't balloon.
    - You'll learn the difference between the built-in helpers (Explore, Plan) and ones you make yourself.

## A friend who runs errands

Say you're studying for a test and need to dig through ten books at the library. If you go yourself, your desk fills up with books. If you ask a friend, "Bring back just the parts that matter, in three lines," your desk stays clear and you get a summary. A subagent is that friend. The official docs say to use one when a side task would flood your main conversation with search results, logs, or file contents you won't look at again.

Subagents have these traits:

- Each has its own memory space, its own instructions, its own tool list, and its own permissions.
- When it's done, only a summary of the result comes back to your conversation.
- You can limit its tools. You can make a helper that only reads.
- You can hand jobs to a faster, cheaper model (like Haiku) to save money.

## Helpers that come built in

Claude Code has built-in helpers, and Claude uses them when it needs to.

| Name | What it does | Notes |
|---|---|---|
| Explore | Finds files and skims code | Read-only (no writing or editing) |
| Plan | Gathers information in plan mode | Read-only |

To stay fast and cheap, these two start without reading your CLAUDE.md. Other built-in helpers, and the ones you make, read CLAUDE.md by default.

## How to make your own

A helper is **one Markdown file**. The label at the top gives its name and description, and below that come its instructions. Only `name` and `description` are required. Here's what the docs' example looks like:

```markdown
---
name: code-improver
description: Reads files and suggests ways to make them easier to read. Use after writing or changing code.
tools: Read, Grep, Glob
model: sonnet
---

You are a code improvement expert. For each issue, explain why, and show the current code next to an improved version.
```

Put the file in `~/.claude/agents/` to use it in all your projects, or in a project's `.claude/agents/` to use it there. You can also just ask Claude to create a new helper for you. Once it exists, call it like this:

```text
Use the code-improver agent to suggest improvements in this project
```

!!! tip "In 10-year-old words"
    A subagent is a friend who runs errands. They don't mess up your desk. They just bring back a summary.

!!! note "★ Going deeper"
    Helpers have more fields too, like `maxTurns` (how many rounds before it stops), `skills` (skills to load ahead of time), and `isolation: worktree` (work in a separate copy of the repository). Multi-word field names use camelCase and must match exactly. A field Claude Code doesn't recognize is ignored without any error. Helpers can also start helpers of their own, up to a depth limit.

## Try it yourself

1. In Claude Code, ask: "Use the Explore agent to skim what files are in this folder."
2. Check that the helper's name shows up as one line in the conversation.
3. If you already have a `~/.claude/agents/` folder, look at the file names inside.

## Use it today

- When long search results or logs start piling up in your chat, say "Use a subagent and just give me a summary."
- Keep helper descriptions short. If all their descriptions together get too long (over 15,000 tokens), you'll see a warning at startup.
- Commit before letting a helper change files. The rewind feature from 16.3 usually can't undo files a subagent changed.

## Common mix-ups

- "Helpers are free." No. Each helper sends its own requests, which count toward the same usage limits. Running several at once uses more.
- "The more helpers, the better." No. Work that needs a lot of back-and-forth, or where steps depend on each other, is better done in the main conversation.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Create custom subagents](https://code.claude.com/docs/en/sub-agents). Read on 2026-11-09.
- **Learning order:** [claude-howto 04-subagents](https://github.com/luongnv89/claude-howto/tree/main/04-subagents) (MIT; rewritten in our own words).
