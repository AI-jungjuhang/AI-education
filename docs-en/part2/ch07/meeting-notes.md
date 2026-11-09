# Meeting notes and emails

<p class="ep-meta"><span>Ch. 7 · 7.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - AI is good at sorting messy notes and long email threads into ==what's decided, what's still open, and who does what by when==.
    - Set the format ahead of time. For anything it doesn't know, have it write "TBD" instead of making it up.
    - A person must always check who's in charge and the deadlines.

## Organizing a drawer

When a drawer is a mess, it's faster to put in dividers first and then sort things into them. Meeting notes are the same. Set up the dividers (the format) first, and sorting gets easy.

Even if your notes are jumbled, AI is good at splitting them into "decided," "still open," and "to do." But it has a habit of filling empty slots with likely-sounding guesses, so be careful.

!!! tip "In 10-year-old words"
    Put the dividers in first, and have it leave a slot empty when it doesn't know.

## A meeting notes template

```text
Sort out the meeting notes below.
Format:
1) Decided (one line each)
2) Still open (one line each)
3) To-do table: task / who / by when
Rules:
- If the notes don't name who or when, don't make it up. Write "TBD."
- Don't change any numbers or dates in the notes.
- Mark anything that needs interpreting as "needs checking."
<notes>
(paste your meeting notes)
</notes>
```

Anthropic's guide to consistent output says to spell out the exact format you want, using JSON, XML, or your own template. Then Claude follows every part of the format more reliably. If you use the same template every time, your meeting notes come out in the same shape.

## Sorting out a long email thread

When 20 emails have gone back and forth, it's handy to have AI read them.

```text
Read the email thread below and sort it out.
1) What has been agreed so far
2) Questions still waiting for an answer, and who asked them
3) What I need to do
4) A draft reply from me (polite, 5 sentences or fewer)
Don't add anything that isn't in the emails.
<emails>(paste here)</emails>
```

## What a person must always check

| Check | Why |
|---|---|
| Names of who's in charge | Similar names can get mixed up, or the wrong person assigned |
| Deadlines | Dates can shift, or "next week" can be read wrong |
| Numbers | Use the checks from Chapter 3 |
| Decided or just suggested | "Someone suggested we do it" is not "We agreed to do it" |
| Missing points | Make sure nothing important dropped out |

!!! note "★ Going deeper"
    - You may use a service that turns a meeting recording into text (speech recognition). If it mishears, names and technical terms get written down wrong, and the AI sorts out that wrong text as is. Mistakes at the input stage carry through to the end. Check names and terms separately.
    - Meetings often include personal or secret information, so the checks from Chapter 3 matter a lot here. Use the tools your workplace has approved, and check the rules on whether attendees need to agree to recording.

## Try it yourself

Pick some rough notes (5 to 10 lines) you scribbled during a recent meeting or call.

1. Use the template above to sort them out.
2. Compare the to-do table with your original notes. Are the names and deadlines right?
3. How many slots say "TBD"? Did it make up any?

## Use it today

1. **Save the meeting notes template.** Use it as one of your question templates from Chapter 2.
2. **Include the "TBD if it's not in the notes" rule.** It cuts down on made-up names and dates.
3. **Check right after sorting.** While the meeting is fresh, it's easier to catch mistakes.
4. **Before you share, have each person confirm their tasks.** Even if AI did the sorting, you're the one sending it.
5. **Blank out personal and secret details first.** Notes still sort fine with names changed to A and B.

## Common mix-ups

- "If AI sorts it, it's right." Always check names and deadlines against the notes.
- "If my notes are a mess, AI can't help." Turning messy notes into a clean structure is one of AI's strengths.
- "I can just record the whole meeting and hand it over." Mistakes in the transcript can carry right through.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Increase output consistency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency), Claude Platform Docs. "Specify the output format you want." Read on 2026-11-09.
    - Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Claude Platform Docs. Specific instructions and structure. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The meeting notes template and the checking table are our own practical tips. The point about speech recognition errors is general, and we didn't check a separate source for it.
