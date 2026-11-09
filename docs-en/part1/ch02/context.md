# Give it context and the answer changes

<p class="ep-meta"><span>Ch. 2 · 2.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A chatbot picks its words based on what you write. So ==it can't know what you don't tell it== (unless it has a memory or search feature turned on).
    - Four kinds of context change the answer a lot: who will read it, what it's for, the rules to follow, and the material you have.
    - Good context is about what's relevant, not about how much you write.

## Asking a stranger for "a good place to eat"

Imagine stopping a stranger on the street and asking, "Where's a good place to eat?" They would probably ask you back. "What kind of food? Who's coming? How much do you want to spend?"

A chatbot is in the same spot. Sometimes it asks you back, too. But often, even when your question is vague, it just ==jumps straight to a likely answer==. Remember from Chapter 1: it picks the next word based on the text in front of it. If that text says very little, lots of words fit. So you get a plain answer that would suit almost anyone.

!!! tip "In 10-year-old words"
    A chatbot can't see inside your head. If you know something about your situation, write it down so the chatbot knows it too.

## Four kinds of context

| Context | What to write | Example |
|---|---|---|
| Who will read it | The reader, and how much they already know | A 5th grader, my boss |
| What it's for | Where you'll use the result | The first slide of a talk, an apology text |
| The rules | Length, tone, things to avoid | 3 sentences, friendly, no jargon |
| Your material | Text or numbers it should use | The meeting notes pasted below |

## See the difference

```text
Weak:    Write a post for our club.

Better:  Write a post inviting new members to our college board game club.
         The readers are first-year students who have never played
         board games like ours. It's for Instagram, so keep it to
         3 sentences and keep the tone warm and casual.
         Please don't use the word "competitive." It might scare people off.
```

Look at the last line. It gives a reason along with the rule. Reasons help the chatbot understand what you're really after. Anthropic's guide for writing prompts says the same thing: explain why a rule matters, and Claude can apply the idea more widely.

## The new coworker test

Anthropic's guide also offers a quick check. Imagine handing your request to a smart coworker who knows nothing about the task, and asking them to do it. Would they be confused? If so, the chatbot will be confused too.

!!! note "★ Going deeper"
    - All the text a chatbot can look at in one go is called its **context window**. Whatever is inside that window is all the "context" it has. It's like working memory, and it's separate from the huge pile of text the model learned from.
    - More is not always better. Anthropic's docs say that as the text grows longer, the model gets less accurate at finding and recalling things. They call this **context rot**. So choosing what goes in matters as much as how much room there is. Part III covers the context window in detail.

## Try it yourself

Ask for the same thing two ways and compare.

```text
1. What should I do this weekend?
```

```text
2. I'm in my 30s and I live in Chicago. It's going to rain this weekend,
   and I want to spend less than $30. I'll be on my own, and I'd like
   somewhere within an hour of home. Give me just 3 ideas.
```

Which answer was more useful for your real life?

## Use it today

1. **Before you send, check the four boxes.** Who will read it, what it's for, the rules, your material. You don't have to fill them all. Just notice when one is empty and think, "The chatbot doesn't know this."
2. **Give a reason with each rule.** "No jargon" works less well than "The reader is a kid, so please skip the jargon."
3. **Paste your own material under your question.** When you paste in the notes, emails, or numbers yourself, the chatbot has less reason to fill gaps from memory and make things up. (Chapter 1 covered hallucination.)
4. **Remove personal details before you paste.** Take out or blank out names, phone numbers, and account numbers. Chapter 3 covers this.

## Common mix-ups

- "The longer the prompt, the better." Long stories that don't matter can confuse it. Write the details that would change the answer.
- "The chatbot can read between the lines." It continues text by likelihood. Anything you leave out gets filled in with the most common choice.
- "I told it once, so it will remember." It remembers within one chat. In a new chat, it usually starts from zero. (Some apps have a memory feature that carries over a few things.) Section 2.2 covers this.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Claude Platform Docs. The sections "Be clear and direct" (including the coworker test) and "Add context to improve performance." Read on 2026-11-09.
    - Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), Claude Platform Docs. What the context window is, and context rot. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** Docs can change as models change. The table of four kinds of context is our own summary of these ideas. It is not a list from the docs.
