# The standard for connecting tools: MCP

<p class="ep-meta"><span>Ch. 13 · 13.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - **MCP (Model Context Protocol)** is ==a shared standard for connecting AI apps to outside systems==, like files, databases, and tools.
    - It's like a USB-C port: one kind of plug for many devices.
    - Connecting something means **giving permission**, so deciding how much to allow matters.

## A USB-C port

Not long ago, every phone had a different charger, so you'd pack several for a trip. A shared standard called USB-C fixed that with one plug.

AI had a similar problem. To connect a chatbot to a calendar, a notes app, or a database, someone had to build a separate connection for each service. **MCP is an attempt to give these connections a shared standard.**

!!! tip "In 10-year-old words"
    MCP is AI's USB-C port. With one kind of plug, you can connect lots of tools.

## What the official MCP docs say

The official MCP docs describe it this way. MCP is **an open-source standard for connecting AI apps to outside systems**. With it, AI apps like Claude or ChatGPT can connect to:

- **data sources** (files on your computer, databases),
- **tools** (search engines, calculators),
- **workflows** (special prompts),

so they can reach important information and get things done. The docs compare MCP to "a USB-C port for AI applications."

The docs give examples of what it makes possible. An agent can use your Google Calendar and Notion to act as a more personal assistant. Claude Code can build a whole web app from a Figma design. A company chatbot can connect to many databases so people can analyze data by chatting. And an AI can make a 3D design in Blender and print it on a 3D printer.

## Who benefits?

| Who | Benefit (from the docs) |
|---|---|
| Developers | Less time and complexity when building or connecting AI apps and agents |
| AI apps and agents | Access to a wide set of data, tools, and apps, which makes them more capable |
| Everyday users | More capable AI that can reach your data and act for you when needed |

The docs say MCP is supported by many apps, including Claude, ChatGPT, Visual Studio Code, and Cursor.

## Connecting means giving permission

Once you connect a tool, the chatbot can **read your data or act on your behalf**. That's handy, and it raises the risk too.

- **Tell reading apart from writing.** Should it only view your calendar, or also create and delete events?
- **Allow only what's needed.** "This one folder," not "all my files."
- **Use connections only from sources you trust.** If you don't know who made it, don't use it.
- **Read approval requests.** When the chatbot asks "May I do this?", read what it wants before you approve.
- **Do things that can't be undone yourself.** Deleting, paying, and sending things outside should be done by a person.

!!! note "★ Going deeper"
    - The MCP docs have a separate **security** section. Outside connections can open a path for prompt injection (Chapter 2): text a connected tool pulls in might hide instructions. We didn't read the security section in detail for this page.
    - MCP servers can run on your own computer (local) or somewhere else (remote). A local server can more easily reach your files. A remote one can more easily reach outside services. (What it can actually reach depends on its setup and permissions.) The risks are different.
    - A standard also makes tools easier to swap. Apps that support MCP can reuse the same connections.

## Try it yourself

Look in your AI app for a menu called something like "Connections," "Connectors," "Apps," or "Extensions."

1. What can it connect to? (Calendar, file storage, notes, and so on.)
2. What permissions does each connection ask for? (Read only? Write too?)
3. Where do you go to disconnect?

You don't have to connect anything. Just reading the permission screens is good practice.

## Use it today

1. **Read the permission list before you connect.** Ask yourself whether read-only would be enough.
2. **Start small.** Try it with one folder or one calendar.
3. **Disconnect what you don't use.** Permissions stay open even when you're not using them.
4. **Be careful with important accounts.** Think hard before connecting work accounts or anything that handles payments.
5. **Don't click "approve" out of habit.** Check that the action is what you actually wanted.

## Common mix-ups

- "MCP is the name of an AI model." It's not a model. It's a standard for connections.
- "It's a standard, so it's safe." Having a standard doesn't make every connected server or its content safe.
- "Once it's connected, the chatbot will handle everything." What it can do depends on the connected tool and on what you approve.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Model Context Protocol, [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro), official docs (version 2026-07-28). The definition, the USB-C comparison, the examples, the benefits, and the list of supporting apps. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The five permission tips and the read/write distinction are our own practical tips. We didn't read MCP's security section in detail. The link to prompt injection is a general explanation. The MCP docs are updated often.
