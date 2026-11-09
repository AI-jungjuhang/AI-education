# Short en-064 · Run something automatically at the right moment: hooks

- **Source page:** 17.2 [Run something automatically at the right moment: hooks](../../../docs-en/part5/ch17/hook-basics.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a hook runs your program at a set moment, without leaving it to the AI's judgment.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | A hook runs at a set moment / It runs without the AI deciding | "What you'll learn" |
| 2 | 9–20 | Notes and skills: The AI chooses to follow or not / Hooks: Always run at the moment | "What you'll learn", second bullet; "A motion-sensor porch light" (deterministic control) |
| 3 | 20–32 | 4 moments: PreToolUse → just before a tool / PostToolUse → just after a tool / Notification → waiting for you / SessionStart → a session starts | "Four common moments" table |
| 4 | 32–42 | Example: an alert hook: When Claude waits for my input, show an alert / Put it in: ~/.claude/settings.json | The `Notification` example and "Try it yourself" |
| 5 | 42–57 | Use it today: Must always happen? A hook, not a note / Start with harmless hooks / Added one? Check with /hooks | "Use it today" |

## Choices and notes
- The Korean episode's title is the porch-light metaphor. The English title states what a hook does; the metaphor is left out.
- The page's "(as long as they're set up right and not turned off)" is not on screen; "Always run" in scene 2 is the page's "deterministic control" in short.
- The JSON example is not shown (too long for a phone screen). The `matcher`, the settings-file table and the ★ note (prompt, agent and HTTP hooks) are left out.
