# Short en-054 · Make your own shortcut commands

- **Source page:** 16.1 [Make your own shortcut commands](../../../docs-en/part5/ch16/slash-custom.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a request you make often can be saved in a `SKILL.md` file and called with `/name`.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Save a request, call it /name / Typed it three times? Make it a button | "What you'll learn" (save it in a file, call it with `/name`; three times means make a button) |
| 2 | 9–21 | Make /easy: 1. Folder: ~/.claude/skills/easy / 2. Inside it: SKILL.md / 3. Description, then instructions / 4. Call it with /easy | "Make one: /easy" (`mkdir -p ~/.claude/skills/easy`, the `SKILL.md` file, "Save it ... type `/easy`") |
| 3 | 21–33 | description: Says what the skill is for (top part, between the --- lines) / disable-model-invocation: true: Runs only when you call it (Claude won't start it on its own) | The two lines under the `SKILL.md` example |
| 4 | 33–43 | Calling it: /easy the paragraph about tokens / Those words go where $ARGUMENTS is | "`$ARGUMENTS` gets replaced with whatever you type after the command" (example call from the page) |
| 5 | 43–58 | Use it today: Keep names short and lowercase (e.g. /easy, /summary, /check) / Write what to do, its shape, the don'ts / Same ask 3 times? Make it a file | "Use it today" |

## Choices and notes
- The Korean episode shows the three `SKILL.md` fields on sticky notes. In English, `$ARGUMENTS` and `disable-model-invocation` don't fit the note width, so scene 3 uses a top/bottom split for two fields, and `$ARGUMENTS` is shown in scene 4.
- "Without it, Claude may ... decide to use it on its own" is shortened to "Claude won't start it on its own" for the flag.
- "Three times" is the page's own rule of thumb, so it stays as a number.
- The old `.claude/commands/` way and the ★ note (where a skill lives) are left out to keep one idea.
