# Agent teams

<p class="ep-meta"><span>Ch. 18 · 18.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - An agent team is several Claude Code sessions that ==work together through a shared task list and message each other directly==.
    - If subagents are errand runners, an agent team is coworkers.
    - **It's an experimental feature, and it's off by default.** Before using it, see whether a lighter option will do.

## Errand runners and coworkers

A subagent runs an errand and reports back only to you. Members of an agent team talk to each other, take tasks from the same to-do list, and even push back on each other's findings. One session acts as the team lead, splitting up the work and pulling the results together. Each teammate works in its own memory space. You can also talk to any teammate directly.

| | Subagents | Agent teams |
|---|---|---|
| Memory space | Each has its own; results return to whoever called it | Each has its own; fully independent |
| Talking | Reports back to the caller | Teammates message each other directly |
| Splitting work | The main session manages everything | They coordinate themselves through messages and a shared task list |
| Token cost | Lower: results come back summarized | Higher: each teammate is a separate Claude |

## When it's worth it

The official docs say teams work best when exploring in parallel adds real value. Examples: researching different sides of a problem at once, testing competing ideas for a bug, or each teammate owning a separate piece that doesn't overlap. On the other hand, for jobs that must happen in order, edits to the same file, or work with lots of dependencies, a single session or subagents work better.

Here's an example that might fit our channel: making the screens for three different scenes at the same time, since the scene files don't overlap. (This isn't an example from the docs. It's our own idea, based on the docs' rule that teammates should work independently.)

## Before you turn it on

- It's off by default. To turn it on, set the environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in your settings or environment. Without it, no team is set up, and Claude won't create or suggest teammates.
- Teams add coordination work and **use far more tokens** than a single session. They cost more than working alone.
- The docs list known limitations. Read that list before you start.

!!! tip "In 10-year-old words"
    Subagents are errand runners. An agent team is coworkers who talk to each other. Coworkers cost more.

!!! note "★ Going deeper"
    There are lighter options than a team. With **cross-session messaging**, you run several sessions yourself and Claude passes findings between them. **Agent view** (the previous page) shows many jobs on one screen without a team. If the pieces don't need to talk to each other, these are usually cheaper and steadier.

## Try it yourself

You can learn this without turning teams on. Pick one job you'd like to do, and answer these questions:

1. Can this job be split into pieces that don't touch each other?
2. Do the pieces really need to talk to each other?
3. Wouldn't subagents (17.4) or background sessions (previous page) be enough?

Only consider a team if the answers point to "not enough."

## Use it today

- Try subagents first, before a team.
- If you do use a team, test it on one small job and check your usage.
- Split the work so two teammates never edit the same file.

## Common mix-ups

- "A bigger team is faster and more accurate." Coordination costs grow, and things can drift apart.
- "Even an experimental feature should be stable." Experimental means it may change or have problems.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. Agent teams are experimental.
- **Source of facts:** [Official docs: Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams) and [Create custom subagents](https://code.claude.com/docs/en/sub-agents). Read on 2026-11-09.
- **Learning order:** [claude-howto 09-advanced-features](https://github.com/luongnv89/claude-howto/tree/main/09-advanced-features) (MIT; rewritten in our own words).
