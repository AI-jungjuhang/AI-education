# Short en-068 · Hands-on: connect an outside service

- **Source page:** 17.3 [Hands-on: connect an outside service](../../../docs-en/part5/ch17/mcp-connect.md)
- **Format:** vertical 9:16, 30fps, about 26 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** connect with one command, sign in from `/mcp`, then test by asking it only to read.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Connect, sign in, then test reading / In that order, it's safe | "What you'll learn"; "In 10-year-old words" |
| 2 | 9–19 | 1. Connect (e.g. Notion): `claude mcp add --transport http notion https://mcp.notion.com/mcp` / Saved, but you haven't signed in yet | "Connect it" (command copied exactly) |
| 3 | 19–30 | 2. Sign in: Type /mcp / Pick notion / Allow it in the browser | "Sign in (give permission)" |
| 4 | 30–40 | 3. A reading test: In Notion, read just the title and first paragraph of the "Practice" page and tell me. Don't change anything. / Saying "only read" doesn't block writing | "Test it by asking it only to read" (prompt copied exactly) |
| 5 | 40–55 | Use it today: Practice with a practice account / If you can, allow reading only / Name it after the service (e.g. notion, github) | "Use it today" |

## Choices and notes
- The page notes the book did not run a real Notion sign-in; the video shows the steps as written and makes no claim about what Notion's sign-in screen looks like.
- How to really block writes (read-only permission on the service, permission rules in 18.1) is left out to keep one idea; the bubble keeps the warning that "only read" doesn't block writing.
- The ★ note (`--scope project`, `.mcp.json`) and disconnecting are left out; the next episode covers cleanup.
