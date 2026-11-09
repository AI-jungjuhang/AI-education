# Short en-076 · Agent teams

- **Source page:** 18.1.4 [Agent teams](../../../docs-en/part5/ch18/agent-teams.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** an agent team is several sessions that share a task list and message each other. It's experimental and costs more, so try subagents first.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Agent teams are sessions that work together / They share one task list and message each other | "What you'll learn" first point |
| 2 | 9–20 | Subagents: report back to the caller, like errand runners / Agent teams: message each other directly, like coworkers | "Errand runners and coworkers" and its table ("Talking" row) |
| 3 | 20–32 | Before you turn it on: Off by default (experimental) / Far more tokens (costs more) / Known limits (read them) | "Before you turn it on" |
| 4 | 32–42 | e.g. our channel (our own idea): Make three scene screens at the same time / Split it so no file has two teammates | "When it's worth it" (the page marks the channel example as its own idea, not from the docs) |
| 5 | 42–57 | Use it today: Try subagents first, before a team / Test a small job and check your usage / One file, never two teammates | "Use it today" list |

## Choices and notes
- The Korean opening called a team "coworkers"; the English first scene states what a team is, and the coworker comparison moves to scene 2.
- The environment variable `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is left off screen; scene 3 just says it's off by default.
- The speech label says "our own idea" because the page says the channel example isn't from the docs.
