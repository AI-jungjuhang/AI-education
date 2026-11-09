# Short en-074 · Permission modes and safety

- **Source page:** 18.1.2 [Permission modes and safety](../../../docs-en/part5/ch18/permissions.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a permission mode sets what Claude may do without asking. Start with Manual and plan mode, and keep `bypassPermissions` for containers and virtual machines.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | A mode sets what Claude may do without asking / A trade between ease and safety | "What you'll learn" first point |
| 2 | 9–22 | Runs freely: Manual (default) → reads only / acceptEdits → reads, file edits / plan → reads / auto → nearly everything, with safety checks / dontAsk → pre-approved tools only / bypassPermissions → everything | The mode table ("Runs without asking" column) |
| 3 | 22–33 | On your own computer: bypassPermissions, everything runs without asking (X) / bypassPermissions is only for containers or virtual machines (O) | "What you'll learn" third point; table row "Isolated containers and virtual machines only" |
| 4 | 33–43 | Someone else's repository? `claude --permission-mode default` / Then just look around in plan mode | "Use it today" first item; the code block |
| 5 | 43–58 | Use it today: Start with Manual and plan mode / acceptEdits only if you'll check results / Keep out of settings: bypassPermissions | "What you'll learn" second point; "Use it today" items 2 and 3 |

## Choices and notes
- The driver-assist metaphor is left out of the first scene; it states what a mode is.
- The English page calls the default mode "Manual (setting value `default`)", so the list says "Manual (default)". The Korean version said "default".
- The `acceptEdits` row is shortened to "reads, file edits" (the page adds common file commands like `mkdir`).
- The fact that new terminal sessions may start in `auto` (v2.1.283 and later) is left out to keep one idea.
- "Convenience" is shortened to "ease" in scene 1.
