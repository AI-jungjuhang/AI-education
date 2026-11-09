# Be specific, one thing at a time

<p class="ep-meta"><span>Ch. 2 · 2.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - The more specific your request, the better. But ==too many jobs in one request get blurry==.
    - Break a big job into small steps, in order.
    - Tell the chatbot to ask you about missing details, so it doesn't fill the gaps on its own.

## One errand per sticky note

Say your mom tells you, all at once: "Go to the store, stop by the bank, mail this package, and pick up your little brother." It's easy to forget one of them. If she tells you one at a time, or writes them down in order, it's much safer.

Chatbots are the same. Give one too many jobs at once, and it may rush through one or skip it. And if what you want is fuzzy, like "write something good," it goes with the most ordinary answer.

!!! tip "In 10-year-old words"
    Be clear, and go one at a time. Split a big errand into small notes with numbers on them.

## What "specific" means

Anthropic's guide asks you to think of Claude as a brilliant but new employee who doesn't know how your team works. The more clearly you explain the job, the better the result. It also says to be specific about the format and the rules you want.

| Fuzzy request | Specific request |
|---|---|
| Write a report. | Write a one-page weekly update for my team of 5. List 3 things we did this week and 2 plans for next week. |
| Make it better. | Make the sentences shorter, and swap hard words for everyday ones. |
| Summarize this. | Give me just the main points in 3 lines. Keep all the numbers as they are. |

Words like "better," "some," or "nice" mean different things to different people. So the chatbot reads them in the most common way.

## Break big jobs into steps

When the order matters, or when no step can be skipped, the guide says to write your instructions as numbered steps.

```text
Go through the customer reviews below, step by step.
1. Sort each review into "praise," "complaint," or "question."
2. Group the complaints that are alike.
3. For the two most common complaints, suggest one fix each.
```

If that still feels like a lot, ask in three separate messages. The guide calls this prompt chaining. It says chaining is useful when you want to look at the in-between results. You check each answer before moving on, so you can see right away where things went off track.

## You fill the gaps, not the chatbot

When a chatbot is missing a detail, it often doesn't ask. It just fills the gap with something likely. You can head that off by saying this up front:

```text
Before you start, if there is information you need that I haven't
given you, ask me first. Ask no more than 3 questions.
```

This is a widely used tip. When it asks instead of guessing, you get fewer strange results.

!!! note "★ Going deeper"
    - For tricky problems, asking it to "think step by step" often helps. When it writes out its middle steps, that text becomes something to build the next words on. Many newer models already think things through before answering, so how much this helps depends on the model and the question. Chapter 20 comes back to this.
    - Anthropic's guide covers more ways to help a model stick to length and format rules. Read the guide itself for the details.

## Try it yourself

Compare one big request with several small ones.

```text
1. For our neighborhood coffee shop, make name ideas, a logo description,
   a first Instagram post, a discount event, and poster text, all at once.
```

Then start a new chat and go one at a time: "First, give me just 5 name ideas. Once I pick one, we'll use it for the next part." Which way gave you results you liked more?

## Use it today

1. **Turn "good" and "some" into numbers and standards.** For example: three lines, one page, easy enough for a 4th grader, friendly but polite.
2. **If there are more than three jobs, split them up.** (That's our rule of thumb, not a law.) You can keep going step by step in the same chat.
3. **If order matters, number the steps.** Writing 1, 2, 3 makes it less likely that one gets skipped.
4. **Make "ask me first if anything is missing" a habit.** It helps most when you're asking for something new.
5. **Check small results first.** Don't ask for the finished thing right away. Get an outline or a first draft and check it.

## Common mix-ups

- "The more I pack into one request, the smarter it gets." Packing more in leads to more things missed.
- "Being specific kills its creativity." Setting limits usually gets you more useful results inside them. If you want ideas, ask for them on purpose: "Give me 5 very different ideas."
- "If it asks me questions, it isn't very smart." A question is a good sign. It heads off a wrong answer.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Claude Platform Docs. The "brilliant but new employee" comparison, specific format and rules, numbered steps, and "Chain complex prompts." Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** "Ask me first" is a widely used tip, not a quote from the guide. How well each tip works depends on the model and the question.
