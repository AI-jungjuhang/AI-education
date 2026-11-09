# Short en-070 · Subagents share out the work

- **Source page:** 17.4.1 [Subagents share out the work](../../../docs-en/part5/ch17/subagent-intro.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** a subagent is a helper AI with its own workspace. It does a job and sends back just a summary, so your chat stays small.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | A subagent is a helper AI / It does a job and sends back a summary | "What you'll learn": a helper AI with its own workspace; sends back just a summary |
| 2 | 9–22 | What a helper has: Its own workspace / Sends back a summary / Limited tools, read-only if you like / A cheaper model, like Haiku | "Subagents have these traits" list |
| 3 | 22–33 | Built in: Explore, Plan, read-only / Your own: one Markdown file, put it in .claude/agents/ | "Helpers that come built in" table; "How to make your own" |
| 4 | 33–43 | When logs pile up: "Use a subagent and just give me a summary" / Your chat doesn't balloon | "Use it today" first tip; "your conversation doesn't balloon" |
| 5 | 43–58 | Use it today: Hand long searches to a helper / Keep helper descriptions short / Commit first, then let it change files (Rewind usually can't undo a helper's file changes) | "Use it today" list |

## Choices and notes
- The Korean episode opens with the errand-friend metaphor. Following the rule that the first scene states the point, the English one opens with "A subagent is a helper AI" and keeps the metaphor out.
- "~/.claude/agents/" (all projects) is left out; the screen shows only the project folder `.claude/agents/`, written as on the page.
- "Its own memory space, instructions, tool list, and permissions" is shortened to "Its own workspace", the page's own phrase.
- The 15,000-token warning is left out (no exact numbers on screen); the tip just says keep descriptions short.
- "The rewind feature from 16.3" is shortened to "Rewind".
