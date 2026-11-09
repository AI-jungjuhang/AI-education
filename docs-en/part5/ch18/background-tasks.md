# Background and scheduled tasks

<p class="ep-meta"><span>Ch. 18 · 18.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Long jobs can ==run in the background, so you don't have to watch them==.
    - There are three ways to repeat a job on a schedule (`/loop`, desktop scheduled tasks, cloud scheduled tasks).
    - Because they run on their own, **what you've allowed them to do** matters even more.

## A robot vacuum and a timer

Start a robot vacuum before you leave for school, and the house is clean when you get back. Set it to start at 7 every morning, and you don't even have to tell it. Background jobs and scheduled tasks are like that.

## Running things in the background

Typing `claude agents` opens **agent view**. The official docs describe it as one screen for all your background sessions: what's running, what needs your input, and what's done. You can send off a new session, do something else, and jump in when it needs you. The docs note that agent view is a research preview, so the screens and shortcuts may change.

## Running on a schedule: three ways

| | `/loop` | Desktop scheduled task | Cloud scheduled task |
|---|---|---|---|
| Runs on | Your computer | Your computer | The cloud |
| Computer must be on? | Yes | Yes | No |
| Chat must be open? | Yes | No | No |
| Your local files | Yes | Yes | No (a fresh copy of the repository) |
| Shortest interval | 1 minute | 1 minute (when Claude sets it) | 1 hour |

For example, use `/loop` to check a deploy every 5 minutes, or to peek now and then at whether a long build is done:

```text
/loop 5m check whether the deploy finished
```

If it has to keep running after you close the chat, use a scheduled task instead. `/loop` is tied to your session. When you reopen the session, only tasks that haven't expired come back. Repeating `/loop` tasks also **expire automatically after 7 days**, so a forgotten loop can't run forever.

## For our channel

- After writing each book page, send the site build check to the background, and keep writing the next page.
- Make a scheduled task that checks every Monday morning whether any links in last week's videos are broken. (A cloud task runs on a fresh copy of the repository, so all it needs is the repository.)

!!! tip "In 10-year-old words"
    Start the vacuum and go to school. Set the timer, and it runs by itself every morning.

!!! note "★ Going deeper"
    The official docs note that background sessions don't simply carry over `bypassPermissions`. It can be ignored, or need your acceptance again. So plan for background jobs to run only within what you've allowed. Also, if a scheduled task uses a skill that lives only in `~/.claude/skills/` on your computer, a cloud task can't find it. Cloud sessions use only what's in the repository (see the skill locations in 16.1).

## Try it yourself

1. Type `claude agents` and just see the screen open. It'll be empty at first.
2. In a practice folder, send off a small job in the background, like "Skim the names of 10 files and make a list." Watch its status change.

## Use it today

- Send jobs that take more than 5 minutes to the background, and do something else.
- Start scheduled tasks with read-only jobs (link checks, status checks).
- In a scheduled task's instructions, write first what it must not do.

## Common mix-ups

- "Once it's scheduled, I can turn off my computer." It depends on the type. Check the table to see whether your type needs the computer on.
- "It's in the background, so it doesn't cost anything." Background sessions use the same usage limits.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. Agent view is a research preview and may change.
- **Source of facts:** [Official docs: Agent view](https://code.claude.com/docs/en/agent-view), [Run prompts on a schedule (/loop)](https://code.claude.com/docs/en/scheduled-tasks), [Routines (cloud)](https://code.claude.com/docs/en/routines), and [Choose a permission mode](https://code.claude.com/docs/en/permission-modes). Read on 2026-11-09.
- **Learning order:** [claude-howto 09-advanced-features](https://github.com/luongnv89/claude-howto/tree/main/09-advanced-features) (MIT; rewritten in our own words).
