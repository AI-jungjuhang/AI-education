# Design good tools

<p class="ep-meta"><span>Ch. 15 · 15.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - An agent's work depends a lot on its tools. And tools for agents should be ==built for an AI to read and use, not just for people==.
    - Anthropic names five principles: choose the right tools, name them clearly, return useful information, save tokens, and write careful descriptions.
    - Even if you're not a developer, you can use the same ideas when you organize the files and material you give an AI.

## A toolbox for a new hire

Imagine giving a new hire a toolbox with hundreds of tools and no labels on the drawers. They'd wander around, unsure what to use. Now imagine each drawer says "Use this when...", with only the tools they need. They'd get to work fast.

Tools for agents are the same. Anthropic's post on tool design, *Writing effective tools for agents — with agents* (2025-09-11), starts with a question. With MCP (Chapter 13), an agent might have hundreds of tools. How do you make those tools **work well**?

!!! tip "In 10-year-old words"
    A good toolbox has labels and instructions on every drawer, and only the tools you really need.

## A tool is a deal between two kinds of systems

The post explains it this way. Ordinary computer programs are **deterministic**: the same input always gives the same output. An agent is **non-deterministic**: it can respond differently even in the same situation. Ordinary software is a deal between deterministic systems. A tool is a deal **between a deterministic system and a non-deterministic agent**. So you have to design it with the agent in mind, thinking about how it might read the tool and how it might misunderstand it.

## Five principles

The post names five key principles for making tools.

| Principle | What it means | Everyday comparison |
|---|---|---|
| Choose the right tools | Build fewer tools, made for the jobs that matter most. Too many, or overlapping ones, can distract an agent | Only the tools you need in the box |
| Name them clearly | Group tools by service and resource so their limits are clear, like `asana_search` and `asana_users_search` | A label on every drawer |
| Return useful information | Give back what the agent can use for its next decision, like readable names instead of long ID codes | A clue that says "next, go here" |
| Save tokens | Keep responses short, with page-by-page results, filters, and trimming (the context window is limited, Chapter 11). Claude Code limits tool responses to 25,000 tokens by default | Keep reports short and to the point |
| Write careful descriptions | Treat tool descriptions as prompts, and write them carefully | An instruction manual |

## How to write the manual

The post explains that a tool's description goes into the agent's context and guides how it calls the tool. **Describe the tool as you would to a new teammate.** Write down the context you take for granted: special ways of asking for things, what technical terms mean, how pieces of information relate. Avoid anything vague. Use clear names for inputs, like `user_id` instead of `user`. The post says that even small fixes to descriptions can make a big difference.

It also says error messages should explain how to fix the problem, instead of giving a code nobody understands.

## Using this as an everyday user

(This section is our own take on how to apply a developer post to everyday use. The post doesn't say this directly.)

Even if you never write code, you can use the same ideas when you **give an AI files and material**.

- **Fewer, clearer files.** If a folder has hundreds of files, the AI gets lost too. Give it only what this job needs.
- **Label file names and column names.** "2026_sales_by_month.xlsx" beats "final_FINAL_v2.xlsx." Give columns clear names too.
- **A one-page guide.** Add a note: "This folder holds these files, and this column means this."
- **Short results.** Asking the AI to "summarize the results" keeps the context from filling up for the next step.

!!! note "★ Going deeper"
    - The post says to **measure tools with evaluations**. Build a quick version, test it on many realistic, multi-step tasks with checkable outcomes, then work with an agent like Claude Code to improve the tools. It tracks accuracy, time, number of tool calls, token use, and errors. The next page covers evaluation.
    - The post gives one example of saving tokens: a "concise" response option used about a third of the tokens of the "detailed" one. Giving the agent that choice lets it trade detail for cost.
    - The earlier post, *Building effective agents*, calls the point where an agent meets its tools the **agent-computer interface (ACI)**. It says to put as much care into it as people put into interfaces for humans.

## Try it yourself

Give a "toolbox check" to some material you often share with AI (files or a folder).

| Check | Yes / No |
|---|---|
| Are only the files this job needs included? | |
| Can you tell what's in each file from its name? | |
| Do the table's columns have clear names? | |
| Is there a one-page guide? | |
| Are personal details included? (Chapter 3) | |

Fix the rows where you answered "No," then ask the same question again. Does the answer change?

## Use it today

1. **Give the AI less material.** Only what's needed is the best kind of organizing.
2. **Name things so both future-you and the AI can understand them.**
3. **Add a line like "this column means this."** Without it, the AI guesses.
4. **Ask for short results.** Long tool results fill up the context.
5. **Write as if explaining to a new hire.** The key is getting what's in your head down in writing.

## Common mix-ups

- "More tools make an agent smarter." Too many make it hard to choose. Keep only what's needed.
- "AI figures out what my files mean." Without names and notes, it guesses.
- "Only developers need to think about tools." The files and settings you give an AI are tools to it too.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Writing effective tools for agents — with agents](https://www.anthropic.com/research/writing-tools-for-agents), 2025-09-11. The deterministic and non-deterministic framing, the five principles with their examples, the 25,000-token default in Claude Code, the new-teammate comparison, and the evaluation-driven process. Read on 2026-11-09.
    - Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 2024-12-19. The agent-computer interface (ACI).

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** "Using this as an everyday user" and the toolbox checklist are our own adaptation of a developer post. The toolbox and drawer-label comparisons are ours.
