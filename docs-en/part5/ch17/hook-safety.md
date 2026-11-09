# Hooks run with your permissions

<p class="ep-meta"><span>Ch. 17 · 17.2</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Command hooks run ==with all of your account's permissions==. They can delete files, and they can read them.
    - Hooks that come with someone else's repository can run **on your computer, under your name**.
    - You'll learn five safety rules for before and after adding a hook.

## Handing over your keys

A motion-sensor light is handy, but installing one means working with electrical wiring. Wire it wrong, and you could start a fire. Hooks are like that. The official docs carry a warning: command hooks run shell commands with your full user permissions, and they can change, delete, or read any file your account can reach. So the docs say to read and test every hook command before you add it.

## Hooks from someone else's repository

A repository's `.claude/settings.json` can contain hooks. Here are the rules the official docs describe:

- **In chat mode,** Claude Code holds back hooks from every settings file, even your own `~/.claude/settings.json`, until you accept the trust prompt for the folder (or for a parent folder whose trust covers it).
- **But one-line mode (`claude -p`) and the SDK never show the prompt and treat the folder as trusted.** So hooks committed in a repository you've never trusted run anyway.

If you must run `-p` on someone else's repository, the official docs suggest three things: read its `.claude/` settings first, start with `--bare`, or turn hooks off for that run with `--settings '{"disableAllHooks": true}'`. Putting `disableAllHooks` in your own settings isn't enough, because the project's settings take priority and can switch it back.

## Five safety rules

1. **Read before you add.** Don't add commands you don't understand. Read someone else's hook line by line, and add it only when you can explain what it does.
2. **Run it on its own first.** Test with fake input, as in the hands-on page.
3. **Start small.** Begin with hooks that don't delete or send anything, like alerts and checks.
4. **Be careful with paths.** File paths and names a hook receives can be untrustworthy input. Always put variables in quotes (`"$VAR"`, not `$VAR`) so spaces and odd characters are handled safely. The official docs also say to check paths for `..` and to stay away from sensitive files like `.env`, `.git/`, and keys.
5. **Know how to turn them off.** If something seems wrong, check the list with `/hooks`. You can turn all hooks off at once with `"disableAllHooks": true` in your settings. But hooks set by your organization's managed policy can't be turned off from your own settings.

!!! tip "In 10-year-old words"
    A hook opens doors with your keys. Read it, test it small, and know how to turn it off.

!!! note "★ Going deeper"
    Hook settings are combined from many places: your settings, the project, local settings, your organization's policy, plugins, and the top of skill and subagent files. They add up instead of replacing each other. So a hook you never added yourself can run. When you install a plugin (18.2), check whether it contains hooks too.

## Try it yourself

Count how many hooks are on your computer.

1. In Claude Code, type `/hooks`.
2. Read which commands are attached to each event.
3. If there's a hook you don't remember adding, or can't explain, find where it came from (your settings, the project, or a plugin).

## Use it today

- When you get a new repository, look for `hooks` in `.claude/settings.json` first and read it.
- When you use `claude -p` for automation, make `--bare` a habit.
- Don't use delete commands (`rm`) in hook scripts. If you need to, first make a test version that only prints what it would delete.

## Common mix-ups

- "Hooks made by AI are safe." No. Commands AI writes still run with your permissions. You still need to read and test them.
- "I can rely on the trust prompt." The prompt helps in chat mode, but `-p` has no prompt.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Hooks reference (security warning, workspace trust, security best practices, disabling hooks)](https://code.claude.com/docs/en/hooks), [Configure permissions (What runs before you trust a folder)](https://code.claude.com/docs/en/permissions), and [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide). Read on 2026-11-09.
- **Learning order:** [claude-howto 06-hooks](https://github.com/luongnv89/claude-howto/tree/main/06-hooks) (MIT; rewritten in our own words).
