# How to ask for changes

<p class="ep-meta"><span>Ch. 2 · 2.2</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - "Try again" alone doesn't tell the chatbot **what** to change or **how**.
    - Point out what you don't like ==one thing at a time, and clearly==.
    - Say "keep this part" about the parts you liked. Then they are more likely to stay.

## "Just make it different" at the hair salon

What happens if you tell a hairdresser, "Just make it a little different"? They don't know where, how much, or in which direction. You'll likely leave unhappy. "Shorter bangs, leave the sides alone" gets you what you want.

Chatbots work the same way. As Chapter 1 showed, a chatbot looks at all the text before it to pick the next word. So its earlier answer stays part of what it reads. But "try again" gives it no clue about which part was the problem.

!!! tip "In 10-year-old words"
    When you ask for a fix, say where and how. And tell it which parts you liked, so it keeps them.

## Weak feedback and strong feedback

| Weak feedback | Strong feedback |
|---|---|
| Meh. Try again. | The second paragraph is too hard. Use words a 4th grader would know. |
| Shorter. | Cut the whole thing to 5 sentences or fewer, and keep the numbers. |
| Too stiff. | Keep it polite, but make it sound more relaxed, like talking to a neighbor. |
| Something else. | These are all about price. This time, give me 3 ideas about ease of use. |

## How to ask for a fix

1. **Fix one thing at a time.** If you ask to change the length, tone, and content all at once, it's hard to tell which change helped.
2. **Say what to keep.** For example: "Keep the first paragraph as is, and change from the second one on." If you don't say so, it may rewrite everything, including the parts you liked.
3. **Give a reason.** "The readers are older folks, so..." With a reason, the chatbot can fix other parts that have the same problem.
4. **Give a one-line sample.** Paste one sentence you like and say "more like this." That sets the direction fast.
5. **Ask for a few versions.** "Give me 3 versions that differ from each other." Then you just pick. After fixing, compare it with your very first request.

```text
In what you just wrote, keep the first paragraph as is.
Only change the second paragraph. It's too hard to follow,
so use simple words a grade schooler would understand.
```

!!! note "★ Going deeper"
    - As a chat goes on, the earlier answers and requests mostly pile up in the context window. (Some apps summarize or drop older parts.) Anthropic's docs say that as text gets longer, the model gets worse at finding and recalling things. So after many rounds of fixes, it may forget or mix up your first rules. The next page covers when to switch to a new chat.
    - If you send the same request again, it draws fresh words from the score table, so the answer may change. Some apps have a "regenerate" button for this. Even so, it's safer to assume that writing down what you want changed works better than repeating yourself.

## Try it yourself

Ask a chatbot this, then give feedback on its answer in two ways.

```text
Write a short birthday message for a friend.
```

- Way A: "Meh. Try again."
- Way B: Start a new chat and make the same request. Then say: "The first sentence is good, but it's too formal. Make it casual, like texting a friend in their 20s. No emoji."

Was the second answer closer to what you wanted?

## Use it today

1. **Learn a feedback template.** "Change [where] to [how]. [Reason]. Keep [what to keep]."
2. **After a fix, ask what changed.** "Tell me in 3 lines what you changed." That makes it easy to check.
3. **Get several and mix.** Pick the pieces you like: "Combine the first sentence of version 1 with the last sentence of version 3."
4. **If three fixes still miss, rewrite your request from scratch.** The next page explains why.

## Common mix-ups

- "If I get angry, it'll try harder." Feelings are not information. What's wrong, and where, is the information.
- "Every fix makes it better." After several rounds, the first rules can get blurry, and things can get worse.
- "If I like it, I don't need to say anything." When you keep editing, you need to say which parts to keep.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), Claude Platform Docs. Being specific and explaining your reasons. Read on 2026-11-09.
    - Anthropic, [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), Claude Platform Docs. Accuracy and recall can drop as text grows (context rot). Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The five fixing tips are common practice, not quotes from the docs. The hair salon comparison is ours.
