# MCP is Claude's plug socket

<p class="ep-meta"><span>Ch. 17 · 17.3</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - MCP is ==a standard plug for connecting Claude Code to outside services== like Notion, GitHub, or databases.
    - It takes "AI that uses tools" from Chapter 13 and stretches it to your own services.
    - The more you connect, the handier it gets, and **the more risk you take on**.

## Holes in a power strip

If every device had a different plug, life would be a pain. That's why wall sockets follow a standard. MCP (Model Context Protocol) is the "socket standard" for AI tools. A service can run a server that follows the standard. Then Claude Code can plug into it. The official docs call MCP an open standard for linking AI and tools.

When do you need it? The docs give a simple test: **if you keep copying things from another tool into the chat**, it's time to connect. Then Claude can read those things itself. No more pasting issue lists or Notion pages by hand.

## Skills, hooks, and MCP side by side

| | What it does | Comparison |
|---|---|---|
| Skills (17.1) | Teach Claude **how** to do a job | A recipe card |
| Hooks (17.2) | Run **automatically** at set moments | A motion-sensor light |
| MCP (17.3) | Connect to **outside services** | A wall socket |
| Subagents (17.4) | **Share out** the work | An assistant |

## What kinds are there?

There are a few ways to connect (called transports). To start, you only need one: **remote HTTP servers**. The official docs suggest HTTP for online services. Some servers run right on your computer instead (stdio). Those run programs with your permissions, so the safety page covers them.

Where the connection info is saved (its scope) also differs.

| Scope | Where it works | Shared with team |
|---|---|---|
| Local | This project only | No |
| Project | This project only | Yes (the repository's `.mcp.json`) |
| User | All your projects | No |

!!! tip "In 10-year-old words"
    MCP is AI's socket standard. Because the shape is the same, you can plug in any service.

!!! note "★ Going deeper"
    MCP servers can offer more than tools. They can also share data ("resources") and prompts. With lots of tools connected, their descriptions take up memory space. Claude Code has a **tool search** feature, on by default. It looks up only the tools it needs, which cuts that cost. Claude Code can also act as an MCP server itself, so other apps can call it.

## Try it yourself

In Claude Code, type `/mcp`. You'll see the list of connected servers and their status. If you haven't connected anything yet, it'll be empty. You can also check from the terminal:

```bash
claude mcp list
```

## Use it today

- Copied the same outside content more than three times? Note it as something to connect.
- Before connecting, decide: does Claude only need to **read** from this service, or also **write** to it?
- Check your connections with `/mcp` now and then, and disconnect what you don't use.

## Common mix-ups

- "Once I connect MCP, Claude knows the service perfectly." Connecting just opens the door. You still have to tell it what to do.
- "If it's in an official directory, it's safe." The official docs say to check that you trust a server before you connect it. Anthropic checks connectors against its rules before listing them. But it **does not security-audit or manage any MCP server**.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp) and [Security](https://code.claude.com/docs/en/security). Read on 2026-11-09.
- **Learning order:** [claude-howto 05-mcp](https://github.com/luongnv89/claude-howto/tree/main/05-mcp) (MIT; rewritten in our own words).
