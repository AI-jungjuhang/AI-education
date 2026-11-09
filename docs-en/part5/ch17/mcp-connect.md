# Hands-on: connect an outside service

<p class="ep-meta"><span>Ch. 17 · 17.3</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Connect a remote server with one command, then give permission by **signing in (OAuth)** from `/mcp`.
    - Learn the order: connect, then test by asking Claude to only read.
    - The example is Notion. Other services follow the same pattern.

## What you need

- Claude Code (we checked against version 2.1.319)
- An account on the service you want to connect. We use Notion as the example. It's safest to use **a practice page or workspace, not an account full of important documents**.

## Connect it

Here's the pattern for a remote HTTP server, with the Notion example from the official docs:

```bash
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

- `--transport http`: connect to a remote server.
- `notion`: a name you choose.
- The last part is the server's address.

When you see a line like `Added …`, the setting is saved. At this point, you **haven't signed in yet**.

## Sign in (give permission)

Open Claude Code and type `/mcp`. Pick `notion` from the list. It shows that sign-in is needed, and your browser opens a sign-in and permission screen. Read the access the service lists carefully, and where you get a choice, choose the least. Note, though, that a connection like this may not be limited to "just one page." It may reach whatever your account can see. (This differs by service, and we didn't confirm Notion's scope ourselves.) That's why **a separate practice account or workspace with nothing important in it** is the safest choice.

When it's connected, `/mcp` shows it as connected. `claude mcp list` also shows a status next to each server, like `✔ Connected` or `! Needs authentication`. If you remove the server (`claude mcp remove notion`), Claude Code deletes the sign-in tokens it stored. But it **doesn't cancel those tokens at the service that issued them**. The next page covers that.

## Test it by asking it only to read

```text
In Notion, read just the title and first paragraph of the "Practice" page and tell me. Don't change anything.
```

If you get an answer, it worked. But asking it to "only read" doesn't actually block writing. To block writes, connect with read-only permission on the service's side, or block write tools with Claude Code's permission rules (18.1). When a permission prompt appears, read it, and say no to writes you didn't want. Depending on your mode or earlier approvals, a prompt may not appear at all.

!!! tip "In 10-year-old words"
    One line to connect, one sign-in, one reading test. Do it in that order, and it's safe.

!!! note "★ Going deeper"
    To share a server with your team, save it at project scope (`--scope project`) in `.mcp.json`. When someone else gets the repository, Claude Code asks them for permission before connecting a `.mcp.json` server the first time. But with `claude -p`, it connects without asking (see the safety page in 17.1). So read and trust `.mcp.json` too.

## Try it yourself

1. Get a practice account or workspace ready.
2. Run the connect command above, and sign in from `/mcp`.
3. Try the "read only" test. If it works, check the connection status in `/mcp`.
4. When you're done, disconnect with `claude mcp remove notion`, and also remove the app's access in the service's own settings. Cleaning up like this is the topic of the next page.

## Use it today

- Before connecting, decide "read only" or "read and write." If you can, allow reading only.
- Practice with a practice account or page.
- Name servers after their service (`notion`, `github`). It's easier to tell them apart as the list grows.

## Common mix-ups

- "Connecting means the AI learns from all my documents." A connection is a path Claude uses to read things when needed. How your documents are handled depends on the service's and the AI company's policies, which you should check separately. We don't claim either way.
- "Once `/mcp` says connected, I'm done." Not quite. You also need to know how to disconnect.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. The Notion server address is the example from the official docs. An actual connection and sign-in can only be tested with a real account, so we didn't run them ourselves for this book.
- **Source of facts:** [Official docs: Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp). Read on 2026-11-09.
- **Learning order:** [claude-howto 05-mcp](https://github.com/luongnv89/claude-howto/tree/main/05-mcp) (MIT; rewritten in our own words).
