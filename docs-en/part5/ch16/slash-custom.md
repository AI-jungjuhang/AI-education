# Make your own shortcut commands

<p class="ep-meta"><span>Ch. 16 · 16.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Things you ask for often can be ==saved in a file and called with `/name`==.
    - "Commands" have now merged with **skills**. There's one way to make them, and the folder name becomes the command name.
    - If you've typed the same request three times, it's time to make a button.

## If you keep typing the same request

Say that every time you finish a video script, you ask the same thing: "Rewrite this so a grade schooler gets it. Explain hard words with one comparison. Keep sentences short." Typing it every time is a chore, and some days you forget part of it. Write that request in a file, name it `/easy`, and you can call it up in one go.

## The old way and the new way

It used to be that putting a file in `.claude/commands/` made it a command. The official docs now say custom commands have merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both make the same `/deploy` command, and old command files keep working. For new ones, skills are the better choice. A skill folder can hold extra reference files, and there are settings for who can call it.

## Make one: /easy

Let's make it a "personal skill" you can use anywhere on your computer. Create the folder under `~/.claude/skills/`.

```bash
mkdir -p ~/.claude/skills/easy
```

Inside that folder, write a `SKILL.md` file like this:

```markdown
---
description: Use when rewriting hard text so a 10-year-old can follow it.
disable-model-invocation: true
---

Rewrite the text below so a 10-year-old can follow it. $ARGUMENTS

- The first time a hard word appears, explain it with one comparison
- Keep sentences short and friendly
- Don't change any facts. If you don't know something, say so
```

The part between the `---` lines describes what the skill is. Below that are the instructions Claude follows.

- `$ARGUMENTS` gets replaced with whatever you type after the command. Call `/easy the paragraph about tokens`, and those words go in.
- `disable-model-invocation: true` means "run only when I call it." Without it, Claude may read the description and decide to use it on its own. For jobs where you want to control the timing, it's safer to turn this on.

Save it, open Claude Code, and type `/easy`. It shows up in the list. If you edit the file, Claude Code picks up the change in the same session, with no restart. (Content that was already loaded stays in the conversation.)

!!! tip "In 10-year-old words"
    Write down a request you make often in one folder, and you can call it up with one name.

!!! note "★ Going deeper"
    Where you put a skill decides where it works. A personal folder (`~/.claude/skills/`) works in all your projects. A project folder (`.claude/skills/`) works in that repository, and if you commit it, your team can use it too. If the same name exists in both, the personal one wins (and company-managed skills beat both). You can also take several values by position, with `$0`, `$1`, and so on. Section 17.1 covers how skills are built.

## Try it yourself

Make the `/easy` skill above and give it one hard paragraph. If you don't like the result, change one line in `SKILL.md` and call it again. Does it change? Learning to change results by editing instructions is the real lesson of this page.

## Use it today

- If you've typed the same request three or more times, make it a file.
- Keep names short (lowercase letters and hyphens are safest): `/easy`, `/summary`, `/check`.
- In the instructions, write one line each for what to do, what shape it should take, and what not to do.

## Common mix-ups

- "You have to program to make a command." No. Plain-language instructions are all it takes.
- "Once I make it, it'll always be followed." A skill is just instructions, so it sometimes drifts. For things that must always happen, use hooks (17.2).

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Extend Claude with skills](https://code.claude.com/docs/en/skills) and [Commands](https://code.claude.com/docs/en/commands). Read on 2026-11-09.
- **Learning order:** [claude-howto 01-slash-commands](https://github.com/luongnv89/claude-howto/tree/main/01-slash-commands) (MIT; rewritten in our own words).
