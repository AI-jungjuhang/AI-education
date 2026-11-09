# Hands-on: research, script, and review agents

<p class="ep-meta"><span>Ch. 17 · 17.4</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Split the flow of making one video across **three helpers**: research → script → review.
    - ==Give each helper a different job and a different set of tools==. The reviewer can only read.
    - Linking the steps together is your job (the main conversation's job).

## Why split it into three?

When writers check their own work, they miss mistakes. They already know what they meant, so they read it that way. Review works best with **fresh eyes**. A subagent starts in its own memory space, so it has exactly those fresh eyes.

| Helper | Job | Tools it can use | Why |
|---|---|---|---|
| researcher | Reads the book page and sources; lists 3 key points and sources | Read, web fetch | It must not change anything |
| scriptwriter | Turns the summary into a scene-by-scene script and saves it | Read, Write | It needs to write the script file |
| reviewer | Checks whether the script says anything the original page doesn't | Read and search only | It points out problems; it doesn't fix them |

## Make three files

Create them in the `.claude/agents/` folder.

**researcher.md**

```markdown
---
name: researcher
description: Reads a book page and its sources and lists 3 key points with sources. Use before writing a video script.
tools: Read, Grep, Glob, WebFetch
---

Read the given page and list:
1. The 3 key points (one sentence each)
2. Where on the page each point appears
3. Source links and the date checked
Mark anything you couldn't confirm as "needs checking." Don't fill gaps with guesses.
```

**scriptwriter.md**

```markdown
---
name: scriptwriter
description: Turns a 3-point summary into a short video scene list under 60 seconds and saves it to a file.
tools: Read, Write
---

Write the scene list using only the summary you were given. Don't add anything that isn't in it.
Keep on-screen text short. For each scene, note which summary point it's based on.
Save the result as script.md in the given folder under video/shorts-en/.
```

**reviewer.md**

```markdown
---
name: reviewer
description: Checks whether a script says anything the original page doesn't, and whether numbers match. Use after a script is saved.
tools: Read, Grep, Glob
---

Compare the script with the original page, and give me only a list of:
- Claims that aren't in the original
- Places where numbers or names differ
- Scenes with no source noted
Don't change any files. If there are no problems, just say "No problems."
```

## Run them in order

Linking the three helpers is the main conversation's job. Say the order in one sentence:

```text
Use researcher to summarize docs-en/part1/ch01/next-word.md, pass the result to scriptwriter to write the script, then use reviewer to check it and give me the list of problems.
```

The official docs say the same: for multi-step work, ask Claude to use subagents in sequence. Each one finishes its task and returns its results to Claude, which passes along the relevant context to the next.

!!! tip "In 10-year-old words"
    One friend researches, one writes, one checks. The checking friend can only look, not change anything.

!!! note "★ Going deeper"
    Why not let the reviewer fix the script itself? Because separating the eyes that spot problems from the hands that fix them removes "I wrote it, so it's probably fine." Going further, the `skills:` field can preload the `make-short` instructions from 17.1 into a helper. Bundling all of this so you can call it at once is the super skill in 18.2.

## Try it yourself

1. Make the three files above. If you just created a new `.claude/agents/` folder, restart Claude Code so it can find the helpers.
2. First, save the current state with `git commit` (files made by helpers are hard to undo).
3. Run the three helpers in order on one short page of the book.
4. In the reviewer's list, sort the real problems from the false alarms yourself. That sorting is where the learning happens.

## Use it today

- Give each helper one job. Two jobs means two helpers.
- For helpers that only need to read, leave writing out of `tools`.
- Always include "If you don't know, say so" in a helper's instructions.

## Common mix-ups

- "Using three helpers guarantees accuracy." No. The reviewer is AI too, and can miss things or flag things wrongly. You make the final call.
- "The helpers talk to each other on their own." By default, the main conversation receives each result and hands it to the next helper. The helpers don't share a chat.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. We used only fields from the official docs' table (`name`, `description`, `tools`). We didn't include results from actually running the three helpers; try it in your own setup.
- **Source of facts:** [Official docs: Create custom subagents (including "Chain subagents")](https://code.claude.com/docs/en/sub-agents). Read on 2026-11-09.
- **Learning order:** [claude-howto 04-subagents](https://github.com/luongnv89/claude-howto/tree/main/04-subagents) (MIT; rewritten in our own words).
