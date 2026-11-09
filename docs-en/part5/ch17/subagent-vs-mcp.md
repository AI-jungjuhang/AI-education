# How are subagents different from MCP?

<p class="ep-meta"><span>Ch. 17 · 17.4</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - We put this chapter's four tools (skills, hooks, MCP, subagents) into ==a table you can pick from by asking "What do I need?"==
    - Subagents and MCP get mixed up a lot. In one line: one is about **who does the work**, the other about **where it can reach**.
    - Sometimes plain old main conversation is the better choice.

## The one-line difference

- **MCP** widens **where** Claude Code can reach: outside services like Notion, GitHub, or databases.
- **Subagents** add more **workers**: the same AI, working in a separate workspace.

You can use both together. A subagent's `mcpServers` field can let "only this helper" reach Notion, and you can limit its tools as well.

## A table to pick from

| If this is your situation | Use this |
|---|---|
| You keep asking for the same steps | Skill (17.1) |
| Something must always happen, and you don't want to leave it to the AI | Hook (17.2) |
| You keep copying content from another service | MCP (17.3) |
| Long output is cluttering your conversation | Subagent (17.4) |
| You want a separate researcher and reviewer | Subagent (17.4) |
| You're going back and forth, polishing | Main conversation |

The official docs also say when to stay in the main conversation: when the job needs a lot of back-and-forth, when several stages share a lot of context, for quick targeted changes, and when speed matters. A subagent starts fresh, so it can take time to gather context.

## Applied to our channel

| Step | Tool | Why |
|---|---|---|
| Read video ideas saved in Notion | MCP | It's an outside service |
| Page → key points | researcher | Do the long reading outside your chat |
| Write the script | scriptwriter | Write from the summary only |
| Check the script | reviewer | Fresh eyes |
| The order and standards for every step | Skill | Saves the steps in writing |
| Format check after saving | Hook | A promise that must not be skipped |

This table is the blueprint for the super skill you'll build in 18.2.

!!! tip "In 10-year-old words"
    MCP adds more places to go. Subagents add more people to do the work.

!!! note "★ Going deeper"
    A **fork** is like a subagent, but different in one way. A regular subagent starts fresh. A fork inherits the whole conversation so far, so you can hand it a side task without explaining everything again. Agent teams, where several helpers run at once and coordinate, come up in Chapter 18.

## Try it yourself

Think of three things you asked AI to do in the past week. For each, write down which tool from the table above would have fit. One answer might be "the main conversation was enough." Often, that's the right answer.

## Use it today

- Before picking a tool, ask: "Do I need a method, a promise, a connection, or extra workers?"
- Start in the main conversation. Move to a tool when something repeats or gets cluttered.

## Common mix-ups

- "The more tools I use, the more of an expert I am." No. Experts use only what they need.
- "Using a subagent makes the AI smarter." It puts the same AI at a different desk. It doesn't make it smarter.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Create custom subagents (Choose between subagents and main conversation; Fork the current conversation)](https://code.claude.com/docs/en/sub-agents), [MCP](https://code.claude.com/docs/en/mcp), [Skills](https://code.claude.com/docs/en/skills), and [Hooks](https://code.claude.com/docs/en/hooks). Read on 2026-11-09.
- **Learning order:** [claude-howto 04-subagents and 05-mcp](https://github.com/luongnv89/claude-howto) (MIT; rewritten in our own words).
