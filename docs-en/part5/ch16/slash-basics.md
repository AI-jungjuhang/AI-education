# Slash commands you'll use often

<p class="ep-meta"><span>Ch. 16 · 16.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - In Claude Code, anything that starts with `/` is ==a shortcut button, not a chat message==.
    - Seven are enough to start: `/help` `/clear` `/compact` `/context` `/model` `/init` `/rewind`
    - The list changes often, so don't memorize it. Get in the habit of looking things up with `/help`.

## Slash commands are remote control buttons

Think of a TV remote. Instead of saying "Please turn up the volume," you press one button. In Claude Code, messages that start with `/` are those buttons. Type just `/` and a list pops up. Type more letters and the list narrows down.

There are two kinds of buttons.

- **Built-in commands**: buttons Claude Code comes with, like `/help` and `/clear`.
- **Commands you make**: things you ask for often, turned into buttons. You'll make one on the next page.

## The first seven

| Command | What it does | When to use it |
|---|---|---|
| `/help` | Shows help and the list of commands | When you're not sure what to press |
| `/clear` | Starts a new, empty conversation | When you're switching to a totally different job |
| `/compact` | Summarizes the conversation so far to free up room | When the chat is long but you want to keep going |
| `/context` | Shows how much of its memory space is used, as a colored grid | When answers start going off track |
| `/model` | Switches the AI model | When you want a faster or a smarter one |
| `/init` | Makes a `CLAUDE.md` note for this folder | When you open a new project for the first time |
| `/rewind` | Takes the conversation or files back to an earlier point | When something went wrong (more in 16.3) |

`/clear` and `/compact` look alike, but they're different. `/clear` is ==wiping the whiteboard and starting over==. `/compact` is ==summing up the whiteboard on one page of notes and continuing from there==. As Chapter 11 showed, an AI's memory space (the context window) has limits, so you need both.

!!! tip "In 10-year-old words"
    Slash commands are remote control buttons. You press one instead of explaining in a long message.

!!! note "★ Going deeper"
    Some commands are really "bundled skills." For example, `/doctor` (checks your setup) and `/batch` (splits a big change into pieces and works on them in parallel) look like commands but are skills. They run on a prompt and a set of steps, not on built-in code. Section 17.1 covers skills. Some commands also exist only from a certain version on. If you type a name and see "Unknown command," check your version first (`claude --version`).

## Try it yourself

It takes two minutes.

1. In your terminal, run `claude`.
2. Type `/help` and skim the list.
3. Type `/context` to see how much memory space is used. Even in a brand-new chat, some is already used, because the default instructions and tool descriptions go in first.
4. Type `/model`, check which model you're using, and close it.

## Use it today

- When a long chat makes answers fuzzy, check `/context` first. If you're continuing the same job, use `/compact`. If it's a new job, use `/clear`.
- You can tell `/compact` what to focus on in its summary.

```text
/compact Keep only the decisions and the remaining to-dos for the skill we're building
```

- If you can't remember a name, type `/` and add letters one at a time to find it.

## Common mix-ups

- "Does `/clear` delete the files I made?" No. It clears the conversation. Files that are already saved stay as they are.
- "Does the AI handle every command?" No. Many, like `/help` and `/context`, are shown right away by the program without asking the AI.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319 (the latest version on npm), checked on 2026-11-09. Commands can be added or changed as versions go up.
- **Source of facts:** [Claude Code official docs: Commands](https://code.claude.com/docs/en/commands). Read on 2026-11-09.
- **Learning order and examples:** [luongnv89/claude-howto 01-slash-commands](https://github.com/luongnv89/claude-howto/tree/main/01-slash-commands) (MIT license; we rewrote everything in our own words).
