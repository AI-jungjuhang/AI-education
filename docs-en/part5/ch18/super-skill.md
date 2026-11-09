# Hands-on: a super skill for making videos

<p class="ep-meta"><span>Ch. 18 · 18.2</span><span>About 9 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Bundle **the skill, three helpers, and the hook** from Chapter 17 into one `studio` plugin, and make a super skill you call with `/studio:episode`.
    - A super skill isn't a new technology. It's ==writing that lists the order of the things you already built==.
    - Skills with side effects should always be called by you, directly.

## Put the blueprint in the box

Remember the table at the end of 17.4? That was the blueprint. Now it goes in the box.

| Part | File | Where you made it |
|---|---|---|
| Script standards | `skills/make-short/SKILL.md` | 17.1 |
| Research, script, and review helpers | `agents/researcher.md` and 2 more | 17.4 |
| Format checker | `hooks/hooks.json` + `scripts/check-page.sh` | 17.2 |
| **Super skill** | `skills/episode/SKILL.md` | This page |

## Make the super skill

Write `skills/episode/SKILL.md` like this:

```markdown
---
name: episode
description: Makes one video script by going through research, script, and review in order. Use only when the user calls it directly.
disable-model-invocation: true
argument-hint: [page path]
---

Target page: $ARGUMENTS

Follow these steps in order to make the script for one video. Pass each step's
result to the next. If you see a problem along the way, stop and tell the user.

1. Use the researcher agent to read the target page and list 3 key points with sources.
2. Pass only that summary to the scriptwriter agent to write a scene list.
   Follow the make-short skill's standards for the scene list.
3. Use the reviewer agent to compare the scene list with the target page and
   find anything the original doesn't say.
4. Show the user the review results as a list. Fix things only after the user decides.
```

The important parts:

- **`disable-model-invocation: true`**: it creates files and takes time, so it runs only when you call it.
- **"stop and tell the user"** and **"only after the user decides"**: the super skill doesn't race to the finish on its own. It keeps the points where you make the call. The more automated something is, the more it needs points where a person steps in.
- It doesn't change the helpers' instructions. The super skill handles only **the order and the hand-offs**.

## Use it

In a session where the plugin is loaded:

```bash
claude --plugin-dir ./studio
```

```text
/studio:episode docs-en/part1/ch01/tokens.md
```

Plugin skill names get the `studio:` prefix. We checked this plugin's structure with `claude plugin validate`. Try running it yourself in "Try it yourself" below.

!!! tip "In 10-year-old words"
    A super skill isn't new magic. It's a guide that calls the tools you already made, in order.

!!! note "★ Going deeper"
    To automate this one step further, you can connect it to a script that calls `claude -p` (the next page). But in one-line mode, `--bare` doesn't read the plugin's hooks. If you need the hook check, run without `--bare`, and only in a folder you trust. And if the super skill gets long, move the standards into separate files (like `references/`) so they're read only when needed.

## Try it yourself

1. Build the `studio` folder with the structure above (copy your Chapter 17 files). An English version is in `examples/claude-code/studio-en/`.
2. Run `claude plugin validate ./studio` and check for `Validation passed`.
3. Open it with `claude --plugin-dir ./studio` and run `/studio:episode` on one short page.
4. Read the scene list's source notes and the reviewer's list. Compare them with the original yourself.
5. If something's off, find which line of which file caused it, and fix it. Fixing the super skill is fixing your tools.

## Use it today

- In a super skill, write three things: the order, where to stop, and where you decide.
- Test it on just one short page at first.
- Always save the results somewhere you can check them, like with `git diff` or a file.

## Common mix-ups

- "The super skill posts the video for me." No. This skill only makes the script. You make the decisions.
- "If the skill names a helper, that helper always runs." Naming it is a request. Check the results to see whether it was called as you meant. If needed, say it more clearly: "You must use the researcher agent."

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. The `studio-en` plugin's structure passed `claude plugin validate`. We didn't include results from running the super skill with a real model.
- The practice files are in the repository at `examples/claude-code/studio-en/` (Korean edition: `studio/`). The README there says how each was checked.
- **Source of facts:** [Official docs: Create plugins](https://code.claude.com/docs/en/plugins/create), [Plugin components](https://code.claude.com/docs/en/plugins/components), [Skills](https://code.claude.com/docs/en/skills), and [Subagents](https://code.claude.com/docs/en/sub-agents). Read on 2026-11-09.
- **Learning order:** [claude-howto 07-plugins](https://github.com/luongnv89/claude-howto/tree/main/07-plugins) (MIT; rewritten in our own words).
