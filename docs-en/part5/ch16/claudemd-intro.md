# The note Claude reads every time: CLAUDE.md

<p class="ep-meta"><span>Ch. 16 · 16.2</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Each new Claude Code session ==starts with no memory of past conversations== (though it does reread CLAUDE.md and its own auto memory).
    - `CLAUDE.md` is a note it reads first, every time. Write something there once, and you don't have to explain it again.
    - The note is read as **background, not as a command**. So there are ways to write it that make it more likely to be followed.

## A smart friend who forgets every morning

Picture a movie character who loses their memory every morning. They keep a note by the bed and read it first thing when they wake up: "You're a chef. The kitchen is on the left." With that note, they can start the day right, even without their memory.

Claude Code is just like that. Start a new session, and it knows nothing about yesterday's conversation (its context window, from Chapter 11, starts empty). So if you put a note file called `CLAUDE.md` in your folder, Claude reads it when it starts.

## Where it goes

Where you put the note decides who it's for.

| Where | File | Who is it for? |
|---|---|---|
| Your whole computer | `~/.claude/CLAUDE.md` | Just you, in all your projects |
| The project | `./CLAUDE.md` | Everyone working in this folder (you can share it with your team) |
| Your private project note | `./CLAUDE.local.md` | Just you, in this project only (add it to `.gitignore` so others don't see it) |

Claude Code reads the notes in the folder you're working in and in every folder above it, and joins them together. Notes in folders below are read when Claude works with files in those folders.

## The easiest way to make one

Open Claude Code in your folder and type `/init`. Claude looks around the folder and writes a first note for you. If a note already exists, it suggests improvements instead of overwriting it. To check that the note loaded, run `/context all` and look under **Memory files**.

To add something yourself, `/memory` lists your note files so you can open them.

!!! tip "In 10-year-old words"
    CLAUDE.md is the note by the bed of a friend who forgets every morning. They read it first, every time they wake up.

!!! note "★ Going deeper"
    There are two kinds of notes. **CLAUDE.md** is the one you write. **Auto memory** is notes Claude writes for itself, based on your corrections and preferences. Both are read at the start of every session. But the official docs say both are **background, not enforced settings**. For anything that must be blocked no matter what, don't rely on a note. Use a hook instead (17.2).

## Try it yourself

1. Make an empty practice folder and run `claude` inside it.
2. Ask it to add one line to the note:

```text
Create a CLAUDE.md and write this one line: "Always answer politely, in words a 10-year-old can follow."
```

3. Run `/clear` to wipe the conversation, then ask any question. You didn't repeat the note, so is the tone still followed?

## Use it today

- The moment you're about to explain something a second time, make a note of it.
- When it gets something wrong once, add a line that same day.
- After writing the note, check with `/context all` that it loaded.

## Common mix-ups

- "If it's in the note, it's followed 100% of the time." No. It's read as background, so it's sometimes ignored. The more specific and short it is, the better it's followed (next page).
- "Changes to the note take effect in the middle of a chat." The note is read when a session starts. After you edit it, the change is surest in a new session.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: How Claude remembers your project](https://code.claude.com/docs/en/memory). Read on 2026-11-09.
- **Learning order:** [claude-howto 02-memory](https://github.com/luongnv89/claude-howto/tree/main/02-memory) (MIT; rewritten in our own words).
