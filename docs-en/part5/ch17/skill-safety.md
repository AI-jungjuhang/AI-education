# Before you open someone else's skills and settings

<p class="ep-meta"><span>Ch. 17 · 17.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Someone else's repository may have a `.claude/` folder with **things that run on your computer**.
    - Before opening an unfamiliar folder, ==get in the habit of reading `.claude/` and `.mcp.json` first==.
    - One-line mode (`-p`) never shows a trust prompt, so be extra careful with it.

## Before you walk into a stranger's house

A friend hands you a note: "Our house rules." It says, "When you arrive, put the front door key in the mailbox." Would you do it? A person would sense something's off. But AI and automatic tools may just follow the rules as written.

When you download someone else's repository and open Claude Code there, the skills, hooks, and settings in its `.claude/` folder may be used on your computer. In a skill, a line written as `` !`command` `` runs on your computer first, when the skill is invoked. Hooks (17.2) run programs outright.

## The trust prompt, and its gaps

In chat mode, opening a new folder makes Claude Code ask, "Do you trust this folder?" The official docs spell out several cases:

- In chat mode, if you don't trust a folder, the allow rules set by that repository aren't applied.
- But **`claude -p` (one-line mode) and SDK runs never show the trust prompt at all.**
- According to the docs' table, even if you trusted only a parent folder, or ran `-p`, **hooks in the repository's settings files are still used**. A project skill's `allowed-tools` is also used, and trust never controls it in any session.
- Servers in `.mcp.json` ask before connecting in chat mode, but under `-p` they connect without asking.

So running `claude -p` in a repository you don't know is the riskiest combination.

## Checklist before opening someone else's repository

1. Open `.claude/settings.json` and read what's in the `hooks` section.
2. If there's a `.mcp.json`, read which servers it connects to.
3. In `.claude/skills/`, look in each `SKILL.md` for lines starting with `` !` `` and for `allowed-tools`.
4. Read `CLAUDE.md` for strange instructions (for example, "send the secrets file somewhere").
5. Open it in chat mode first, and see if the trust prompt appears. If you're unsure, choose not to trust it.

If you must run `-p` in someone else's repository, the official docs suggest ways to limit what runs. `--bare` makes it skip the project's hooks, skills, commands, subagents, plugins, and `.mcp.json` servers. `--setting-sources user` makes it ignore the project's settings files and `.mcp.json` altogether. And `--settings '{"disableAllHooks": true}'` turns off hooks for that run. Even with `--bare`, though, the `env` section of the project's settings and some helper commands can still apply. So with an unfamiliar repository, reading it first is the basic rule.

!!! tip "In 10-year-old words"
    Read a stranger's house rules before you follow them. `.claude/` is that note.

!!! note "★ Going deeper"
    You can turn off the `` !`command` `` lines in skills with the setting `disableSkillShellExecution: true`. It applies to skills from user, project, plugin, and added folders. With it on, a placeholder appears where each command's output would go. Still, for individuals, the habit of reading before trusting comes first.

## Try it yourself

Download any public repository that isn't this book's (don't open Claude yet). Then just check whether it has `.claude` and `.mcp.json`:

```bash
ls -a repo-folder
cat repo-folder/.claude/settings.json 2>/dev/null
```

If they exist, go through the `hooks` or `mcpServers` sections line by line and work out what they do. For parts you don't understand, ask Claude: "Don't run anything. Just read this and explain it."

## Use it today

- Before opening someone else's repository, read `.claude/` and `.mcp.json`.
- When the trust prompt appears, trust the folder only if you have a clear reason.
- Don't use `claude -p` in folders you don't know.
- Before sharing your own skills, check once more what any `!` lines run.

## Common mix-ups

- "AI blocks the dangerous stuff on its own." Trust prompts and permission rules help, but hooks set in settings files run with your permissions. A person reading the files is the last line of defense.
- "Skills from an official marketplace are safe." Even if the source is trustworthy, it's good to read the content. Every safety tip in this book comes down to: read it, give narrow permission, and clean up when you're done.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Configure permissions (What runs before you trust a folder)](https://code.claude.com/docs/en/permissions), [Security](https://code.claude.com/docs/en/security), and [Skills](https://code.claude.com/docs/en/skills). Read on 2026-11-09.
- **Learning order:** [claude-howto 03-skills](https://github.com/luongnv89/claude-howto/tree/main/03-skills) (MIT; rewritten in our own words).
