# How are checkpoints different from git?

<p class="ep-meta"><span>Ch. 16 · 16.3</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Checkpoints are ==a quick undo inside the current session==. Long-lasting history is git's job.
    - Learn the four kinds of things checkpoints **can't** undo.
    - The safe habit is two layers: save points plus commits.

## A pencil eraser and a photo album

Checkpoints are like an eraser for pencil writing. You can quickly erase what you just wrote, but if the notebook sits for a long time, things fade. Git is a photo album. You take pictures of important moments, look them up months later, and share them with others. The official docs say the same: checkpoints are for quick recovery within a session, and long-lasting history and teamwork belong to version control like git.

## What checkpoints can't do

| Can't undo | Why, and what to do |
|---|---|
| Files changed only by terminal (Bash) commands | If Claude never edited the file with its file-editing tools, it isn't tracked. Use git to undo it |
| Files changed by subagents | These usually aren't restored. Use git |
| Files you changed yourself, or work in another window | Changes outside this Claude Code session usually aren't tracked |
| Shortcut files (symlinks) and hard-linked files | They're skipped, with a warning |

One more: a message you send while Claude is still working has no save point of its own, so it may show "No code restore." In that case, pick the message that started that turn and rewind from there.

## The two-layer habit

1. Before starting new work, commit the current state. A commit is putting it in the photo album.
2. While working, try things freely. If something goes wrong, `/rewind` takes you back fast.
3. When you get a result you like, commit again.

This book's repository gets a commit after every page. For jobs with lots of files, like making videos, relying only on checkpoints may not protect video files made by terminal commands.

!!! tip "In 10-year-old words"
    Checkpoints are an eraser. Git is a photo album. Put the important stuff in the photo album.

!!! note "★ Going deeper"
    There's also `/branch`, which forks the same conversation so you can try another approach, and "worktrees," which give you separate working folders so jobs don't get in each other's way. You'll see both again in Chapter 18.

## Try it yourself

In a practice folder, run `git init`. Have Claude make a file, and commit it. Then ask, "Rename all the files." This time, undo it with `git restore` or `git checkout` instead of `/rewind`. How do the two ways feel different?

## Use it today

- Before big jobs, ask for this first:

```text
Check which files have changed so far, and draft a one-line commit message. Don't commit until I've checked it.
```

- Always commit before using subagents (17.4).

## Common mix-ups

- "I have checkpoints, so I don't need git." Not true. Old snapshots get cleaned up, and some changes aren't tracked at all.
- "If I don't know git, I can't use Claude Code." You can. But as your work gets more important, learning git is worth more and more.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Checkpointing (Limitations)](https://code.claude.com/docs/en/checkpointing). Read on 2026-11-09.
- **Learning order:** [claude-howto 08-checkpoints](https://github.com/luongnv89/claude-howto/tree/main/08-checkpoints) (MIT; rewritten in our own words).
