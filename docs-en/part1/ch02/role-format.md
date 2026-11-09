# Set the role, the format, and an example

<p class="ep-meta"><span>Ch. 2 · 2.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A **role** sets the voice and point of view. A **format** sets the shape of the result. An **example** shows a sample of what you want.
    - When you set these three, the "next words" the chatbot picks are ==more likely to go where you want==.
    - Giving it a role does not teach it facts it doesn't know.

## An outfit, a container, and a sample

Think of asking a cook for help.

- **The role is the outfit.** Say "Explain it like a grade school teacher," and the tone and style of the explanation change.
- **The format is the container.** "As a table," "in three lines," or "as a numbered list" sets the shape the answer comes in.
- **The example is the sample.** Showing one thing and saying "like this" works faster than a long description.

!!! tip "In 10-year-old words"
    Give the chatbot an outfit (role), a container (format), and a sample (example). Then it is less likely to wander off in a strange direction.

## Role: set the point of view and the voice

```text
You are a middle school science teacher. A student asks,
"Why is the sky blue?" Explain it so a 7th grader can follow.
```

Anthropic's guide says that even one sentence about a role helps focus Claude's behavior and tone. In terms of next-word picking, the chatbot starts choosing words that someone in that role would likely use.

But a role is an outfit, not knowledge. Saying "You are the world's best doctor" does not give it facts it doesn't have. The risk of hallucination stays the same.

## Format: set the shape of the result

```text
Sort out the meeting notes below. Use this format:
- Decided: up to 3 items, one line each
- Still open: up to 3 items
- Next steps: a table with who and by when
```

If you decide the shape up front, you get something you can use right away. You don't need to ask for one fix after another. The guide also says to be specific about the output format and the rules you want.

## Example: show a sample

```text
I'm naming products. Use this style:
Example 1) Potato → Fluffy Spud Buddy
Example 2) Milk → A Cup of White Cloud
In the same style, give me 5 names for "strawberry."
```

Anthropic's guide calls examples one of the most reliable ways to steer the format, tone, and structure. It suggests 3 to 5 examples, and it says to make them a bit different from each other. If all your examples look alike, the chatbot may copy what they have in common, even the parts you didn't mean.

!!! note "★ Going deeper"
    - Giving examples in your prompt is called **few-shot prompting**. One example is one-shot. No example is zero-shot.
    - When instructions, examples, and material are mixed in one long prompt, label each part with a tag, like `<example>`. Anthropic's guide shows how XML tags help Claude tell the parts apart.
    - Why does any of this work? Think back to next-word picking. The text in front of the chatbot changes the chances of every next word.

## Try it yourself

Ask about the same topic three ways.

```text
1. Tell me what's good about potatoes.
2. You are a grade school teacher. Tell a 3rd grader what's good about potatoes.
3. Do the same as 2, but make it a table with two columns:
   "Why it's good" and "Easy example."
```

Compare the answers. Which changes came from the role, and which from the format? Sorting that out is part of the fun.

## Use it today

1. **Keep a three-line template.** Save "Role: / Format: / Example:" in your notes app and fill it in when you need it.
2. **Use writing you like as the sample.** Paste an old answer that came out well, or something you wrote, and say "like this." That makes it easier to match a tone.
3. **Pick examples that differ.** If you only give similar examples, you only get similar results.
4. **Use roles for tone and point of view, not for facts.** For facts, paste in the source material or check them yourself.

## Common mix-ups

- "A role gives it an expert's knowledge." It changes the voice and point of view. It doesn't add knowledge.
- "Setting a format makes the content worse." Usually it makes the answer easier to read. But a format that is too tight may leave no room for what needs saying.
- "More examples are always better." The guide suggests about 3 to 5. Too many make the prompt long and can tilt the results one way.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Claude Platform Docs. The sections "Be clear and direct," "Use examples effectively" (3 to 5 varied examples), "Structure prompts with XML tags," and "Give Claude a role." Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The "outfit, container, sample" comparison and the sample prompts are ours. The guide's advice, such as how many examples to use, may change as models change.
