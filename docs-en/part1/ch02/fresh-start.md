# When a new chat works better

<p class="ep-meta"><span>Ch. 2 · 2.2</span><span>About 4 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - As a chat grows longer, the chatbot can lose track of the early parts or mix them up. And ==an answer that went wrong keeps pulling on the rest==.
    - When that happens, it's often better to write a summary and move to a new chat.
    - In a new chat, you need to tell it everything again (unless a memory feature carries things over).

## A whiteboard covered in scribbles

When a whiteboard is packed with scribbles, new notes get lost in the mess. It's faster to wipe it clean and write down just what matters.

A chat window is that whiteboard. Everything you and the chatbot have said so far is something it reads. As the chat gets long, key rules get buried. And a strange answer from earlier can keep tugging the next words off course.

!!! tip "In 10-year-old words"
    If the whiteboard is full of scribbles, wipe it and write just the main points again. Starting a new chat does exactly that.

## When to start a new chat

| When this happens | Why |
|---|---|
| It keeps missing, no matter how many times you fix it | The off-track answers are still there, still pulling |
| The chat has gotten very long | There's a limit to how much it can see at once, and accuracy can drop as text grows |
| You switch to a totally different topic | The old topic can leak into the new one |
| It keeps forgetting your first rules | The rules are buried deep in the chat |

On the other hand, if you're still polishing the same thing, there's no need to start over.

## Summarize, then move

Before you open a new chat, pull the main points out of the old one.

```text
Sum up what we've decided in this chat so far:
- Goal:
- Who will read it:
- Rules it must follow:
- What I liked so far:
- What I didn't like, and why:
Keep it short so I can paste it into a new chat.
```

Read the summary and fix anything wrong. Then paste it in as the first message of a new chat. The off-track answers don't come along, so you start clean.

!!! note "★ Going deeper"
    - Anthropic's docs compare the context window to the model's "working memory." They say accuracy and recall drop as the number of tokens grows, which they call context rot. That's why choosing what stays in context matters.
    - In long chats or agent tasks, some services **summarize older parts automatically** to save room. Anthropic's docs present this server-side "compaction" as the main way to manage long conversations. Each service does this its own way, so check how yours works.
    - Some apps have a "memory" feature that can bring past details into a new chat. What it saves, and the settings, differ from app to app.

## Try it yourself

Chat with a chatbot for about ten turns, adding one detail at a time. (For example, plan a trip, then add a budget, dates, who's coming, and food likes, one by one.) Then:

1. Send the "sum up" request above and get a summary.
2. Open a new chat, paste in the summary, and say "Make a schedule with these details."
3. Compare it with the answer from the long chat. Did either one miss a detail?

## Use it today

1. **If three fixes still miss, try a new chat.** (That's our rule of thumb.) Moving a summary over is faster than fixing forever.
2. **Put "what didn't work" in the summary too.** It helps the chatbot avoid making the same mistake again.
3. **New topic, new chat.** One job per chat works well.
4. **Put key rules at the top of every chat.** The "question template" on the next page is made for exactly this.

## Common mix-ups

- "If I open a new chat, I lose everything." Move a summary over and you keep what you need.
- "The longer we chat, the better it knows me." The longer it gets, the more it can lose track of the early parts.
- "With a memory feature, I don't need a summary." You can't always know what memory saved, or how. For rules that matter, writing them down yourself is the sure way.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), Claude Platform Docs. The "working memory" comparison, context rot, and server-side compaction. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The "when to start a new chat" table and the summary prompt are our own practical tips, not quotes from the docs. Memory and summary features in each app change over time.
