# Short en-063 · Before you open someone else's skills and settings

- **Source page:** 17.1 [Before you open someone else's skills and settings](../../../docs-en/part5/ch17/skill-safety.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** someone else's `.claude/` folder can run things on your computer, so read it before you open the repository.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Someone's repo? Read .claude/ first / Its files may run on your computer | "What you'll learn" |
| 2 | 9–20 | In a repo you don't know: claude -p (never shows a trust prompt) X / Open it in chat mode first (check for the trust prompt) O | "The trust prompt, and its gaps"; checklist step 5 |
| 3 | 20–32 | Check first: 1. settings.json → hooks / 2. .mcp.json → servers / 3. SKILL.md → !` lines, allowed-tools / 4. CLAUDE.md → strange instructions | "Checklist before opening someone else's repository", steps 1 to 4 |
| 4 | 32–42 | If you must use -p: --bare / Skips the project's hooks, skills, and MCP servers. Still, read it first. | Paragraph after the checklist (`--bare`; even with it some settings still apply, so reading first is the basic rule) |
| 5 | 42–57 | Use it today: Before opening, read the settings (.claude/ and .mcp.json) / Trust prompt? Only with a reason / Sharing a skill? Check its ! lines | "Use it today" |

## Choices and notes
- The Korean episode opens with "read before you open." The English title adds "Someone's repo?" so the point is clear in the first screen; the house-rules story is left out.
- The `--bare` list on the page is longer (commands, subagents, plugins too); the bubble shows three items and adds "Still, read it first" because the page says some settings can still apply.
- `--setting-sources user`, `disableAllHooks` and the ★ note (`disableSkillShellExecution`) are left out.
