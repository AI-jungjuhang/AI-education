# Write good instructions

<p class="ep-meta"><span>Ch. 15 · 15.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Write an agent's instructions like ==a first-day guide for a smart new employee==.
    - Include its role, its goal, its limits, rules for using tools, when to stop, and what to do when it doesn't know.
    - Have a coworker read your instructions, then improve them.

## A first-day guide

When someone new joins, you tell them: "Here's what this place does. Here's your job. Don't do these things. If you're unsure, ask this person." Without a guide like that, even a smart person can end up doing the wrong thing.

Agents are the same. The asking tips from Chapter 2 matter even more in **instructions for an agent that works for a long time**. It works through many steps on its own, so if the first direction is off, it can stay off to the very end.

!!! tip "In 10-year-old words"
    Give your agent a first-day guide. The clearer the guide, the better it works on its own.

## What goes in the guide

Anthropic's docs compare Claude to **a brilliant new employee who doesn't know how your team works**. The more clearly you explain what you want, the better the result. Add the principles from the post on building agents (keep it simple, make the plan visible, set stopping conditions), and you get a guide like this.

| Section | What to write | Example |
|---|---|---|
| Role | Who it's acting as | An events helper for the town library |
| Goal | What it's for, and why it matters | Help visitors find events that suit them |
| Tools | Which tools, and when to use them | Search the events file to find answers |
| Limits | What it must not do | Don't make bookings, take payments, or ask for personal details |
| Steps | In order, if needed | 1) Check the question 2) Search 3) Answer with evidence |
| When unsure | What to do | Say it doesn't know, and give the help desk contact |
| When to stop | When to finish or hand off to a person | If two searches find nothing, stop and point to a person |
| Report format | How to show results | A list of date, place, and who it's for, plus the supporting lines |

## Sample instructions

```text
You are an events helper for our town library.
Goal: Help visitors find events that suit them. Accuracy matters most,
because wrong information sends people on a wasted trip.
Tools: Search the events file. Don't mention anything that isn't in it.
Don't: Make bookings or take payments. Don't ask for personal details.
Steps: 1) Check what kind of event the person wants. If it's unclear,
ask one question. 2) Search the events file. 3) List the date, place,
and who it's for, and show the rows you used.
If you don't know: Say "I couldn't find that in the events list," and
give the library help desk's contact details.
When to stop: If two searches find nothing, stop searching and give
the message above.
```

## Writing tips

- **Give reasons.** "Accuracy matters, because people could make a wasted trip." A reason helps it stay on course in similar situations (Chapter 2).
- **Number the steps when order matters.**
- **Don't just list "don'ts." Say "do this instead."** Next to each closed road, point out an open one.
- **Make its plan and reasoning visible.** Anthropic's post on agents recommends **showing the agent's planning steps** to make it more transparent.
- **Start simple.** The same post says to find the simplest solution first. Add rules one at a time, when you need them.

!!! note "★ Going deeper"
    - Instructions take up room in the agent's context window and go in as input at every step (Chapter 11). If they're too long, key rules can get buried. A common tip is to put the most important rules at the start and the end (Chapter 6; that research used 2023 models).
    - Rules in the instructions can bend when users push. In Project Vend (Chapter 14), the agent gave discounts when people coaxed it. For rules that truly must hold, it's safer to also enforce them **a second way**, through tool permissions or approval steps.
    - In developer tools, instructions usually go in the system prompt, with information that changes each conversation added separately. Everyday users often put them in an app's "custom instructions" or "projects" feature (it differs by service).

## Try it yourself

Write a guide for a job you give AI over and over (or one you'd like to hand off).

1. Fill in the eight sections from the table above.
2. **The coworker test:** have a friend read only your guide. Is anything confusing? If they're confused, the chatbot will be too (Chapter 2).
3. Give the guide to a chatbot, then ask one easy question and one tricky one. Does it follow the guide?

## Use it today

1. **Put the role, the goal, and the reason in the first three lines.** That sets the direction.
2. **Always include "when you don't know."** It's a key section for cutting down on made-up answers and wild guesses.
3. **Include when to stop.** So it doesn't loop forever.
4. **Pair each limit with an alternative.** Next to "don't," write "instead, do this."
5. **Keep improving the guide.** Each time you see odd behavior, add a line, and save it in your prompt collection from Chapter 8.

## Common mix-ups

- "The longer the instructions, the better the agent follows them." Long instructions bury what matters. Write only what's needed.
- "Write it well once, and it works everywhere." It goes off course in situations you didn't expect. Test and fix it.
- "Once the rules are written, it's safe." Written rules can bend. Back them up with permissions and approvals.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Claude Platform Docs. The new-employee comparison, specific instructions, giving reasons, and numbered steps. Read on 2026-11-09.
    - Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 2024-12-19. Simplicity, transparent planning steps, and stopping conditions.
    - Anthropic, [Project Vend: Can Claude run a small shop?](https://www.anthropic.com/research/project-vend-1), 2025-06-27.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The eight sections and the library example are ours. "Enforce it a second way through permissions" is our own takeaway from the Chapter 14 case, not a direct recommendation from these sources. Custom instruction features differ by service.
