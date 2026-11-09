# Bundle and share with plugins

<p class="ep-meta"><span>Ch. 18 · 18.2</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A plugin is ==a box that bundles skills, agents, hooks, and MCP into one folder you can install and share==.
    - All it takes is the right folder layout and one `plugin.json` file.
    - **An installed plugin runs with your permissions.** You'll learn how to make one and how to decide whether to trust one.

## Moving boxes

When you move house, you don't carry things one at a time. You pack them in boxes. If the skills, helpers, and hooks you made in Chapter 17 are scattered around, they're a pain to move to a new computer or share with a teammate. A plugin is the moving box that holds them all. The official docs describe a plugin as a folder that bundles skills, agents, hooks, MCP servers, and more, so they install and load as one unit.

## The folder layout

```text
studio/
├── .claude-plugin/
│   └── plugin.json        ← the label (only this goes here!)
├── skills/
│   ├── make-short/SKILL.md
│   └── episode/SKILL.md
├── agents/
│   ├── researcher.md
│   ├── scriptwriter.md
│   └── reviewer.md
├── hooks/
│   └── hooks.json
└── scripts/
    └── check-page.sh
```

`plugin.json` is short:

```json
{
  "name": "studio",
  "description": "Tools for turning one book page into a short video script",
  "version": "0.1.0",
  "author": { "name": "Channel production team" }
}
```

- `name` is required, with no spaces. It becomes the prefix in front of skill names, so you call them like `/studio:episode`.
- Put only `plugin.json` inside `.claude-plugin/`. Other files placed there won't load.
- Inside hooks, refer to the plugin's scripts with a path like `${CLAUDE_PLUGIN_ROOT}/scripts/...`.

## Test it

You can load a plugin just once to test it, without installing:

```bash
claude --plugin-dir ./studio
```

There's also a command that checks whether the folder follows the rules:

```bash
claude plugin validate ./studio
```

We ran this check on this book's example plugin (the English version is in `examples/claude-code/studio-en/`), and it passed. The only note was a missing icon, which matters when you submit to the official directory, not for using it on your own computer.

## Installing, and trust

You find and install other people's plugins from `/plugin`. The official docs are clear about the risk: **an installed plugin can run any code with your user permissions.** The hooks, MCP servers, and background monitors inside a plugin can run outside Claude Code's permission rules and sandbox. So before installing:

1. Read the plugin's `hooks/`, `.mcp.json`, `scripts/`, and `bin/`.
2. Check which marketplace it came from. A marketplace name tells you who published the catalog. It doesn't mean every plugin in it is safe.
3. If auto-update is on, know that what you read can change later.
4. If you don't use it, disable or remove it (`claude plugin disable`).

!!! tip "In 10-year-old words"
    A plugin is a moving box. Label your own boxes before you share them, and open other people's boxes before you take them.

!!! note "★ Going deeper"
    An enabled plugin affects **every conversation where it's on**. The names and descriptions of its skills and agents go into Claude's memory space each turn, which uses up usage and room. The docs say the official marketplace shows an estimated "context cost" in `/plugin` before you install. Plugins you haven't used for a while show up in a "not used recently" group in your installed list.

## Try it yourself

1. Gather the skill, agent, and hook files you made in Chapter 17 into the folder layout above.
2. Write `plugin.json` and run `claude plugin validate`. Does it pass?
3. Open it with `claude --plugin-dir ./studio`, and look in `/skills` or the `/` list for names starting with `studio:`.

## Use it today

- Once you have more than three or four skills, hooks, and agents, bundle them into a plugin.
- When you share one, write in the README what it runs (hooks, scripts).
- Before installing, check: Did I read the hooks, MCP, scripts, and bin? Did I check where it came from?

## Common mix-ups

- "If it's in an official marketplace, I can trust it." Even in an official-sounding marketplace, it's good to read each plugin.
- "Making a plugin means writing code." Skills and agents are plain writing (Markdown). Only hook scripts, if you need them, are code.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. We made the example plugin for this book and checked it with `claude plugin validate`. We didn't include results from actually installing or running it.
- The practice files are in the repository at `examples/claude-code/studio-en/` (Korean edition: `studio/`). The README there says how each was checked.
- **Source of facts:** [Official docs: Plugins](https://code.claude.com/docs/en/plugins), [Create plugins](https://code.claude.com/docs/en/plugins/create), and [Plugin security and trust](https://code.claude.com/docs/en/plugins/security). Read on 2026-11-09.
- **Learning order:** [claude-howto 07-plugins](https://github.com/luongnv89/claude-howto/tree/main/07-plugins) (MIT; rewritten in our own words).
