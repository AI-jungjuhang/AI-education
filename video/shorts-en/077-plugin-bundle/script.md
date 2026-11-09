# Short en-077 · Bundle and share with plugins

- **Source page:** 18.2.1 [Bundle and share with plugins](../../../docs-en/part5/ch18/plugin-bundle.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a plugin bundles your skills, agents, and hooks into one folder you can install and share. Someone else's plugin runs with your permissions, so read it first.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | A plugin bundles your tools / One folder you can install and share | "What you'll learn" first point |
| 2 | 9–21 | In the box: Label plugin.json / Skills skills/ / Agents agents/ / Hooks hooks/ | "The folder layout" ("← the label") |
| 3 | 21–32 | Test it: `claude --plugin-dir ./studio` / `claude plugin validate ./studio` / Call it: `/studio:episode` | "Test it"; `name` becomes the prefix (`/studio:episode`) |
| 4 | 32–43 | Someone else's plugin: Install it right away (X), it runs with your permissions / Read hooks/ and scripts/ first (O) | "Installing, and trust" (step 1) |
| 5 | 43–58 | Use it today: Only plugin.json goes in .claude-plugin/ / Say what it runs in the README / Before installing, read the hooks | Folder layout rule; "Use it today" items 2 and 3 |

## Choices and notes
- The moving-box metaphor is left out of the first scene; it states what a plugin is.
- The "Label" note shows only `plugin.json` (the page shows it inside `.claude-plugin/`; the full path is in the checklist).
- Scene 4's list is shortened to `hooks/` and `scripts/`; the page also names `.mcp.json` and `bin/`.
- The validate result (passed, missing icon) is left out.
