# Adjust its thinking time (effort level)

<p class="ep-meta"><span>Ch. 23 · 23.3</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - The effort level is ==the main dial for how long Claude thinks==. It replaces "think hard" in your prompt.
    - The levels are `low`, `medium`, `high`, `xhigh`, and `max`. The default depends on the model.
    - Higher levels take more time and tokens. Turn it up only when you need to.

## Time on a test

Spending ages on an easy question wastes time. Rushing a hard one leads to mistakes. The effort level is a dial for that kind of thinking time. The official docs call it the main control for how long Claude thinks. At a higher level, Claude **tests more edge cases and checks more of its work** before it answers. That costs more time and tokens.

## Levels and defaults

You change it with `/effort`. Which levels you get depends on the model. As of 2026-11-09, Opus 5.5, Sonnet 5.5, and Haiku 5.5 support `low`, `medium`, `high`, `xhigh`, and `max`, and **start at `medium`**. If you pick a level the model doesn't support, it drops to the highest one it does support below that.

| Level | When (the official advice, in short) |
|---|---|
| `low` | Quick back-and-forth where you check every result: brainstorming, a first draft, renaming things |
| `medium` | Everyday work with a clear scope (the default on these models) |
| `high` or `xhigh` | When it's easy to miss a case: a bug in code you didn't write, a test that sometimes fails, a change where every place that uses something must be found |
| `max` | A very hard problem you want Claude to work on without you, like hunting for a security hole. On ordinary jobs it tends to **overthink**, so you may pay more for an answer no better than `high` |

To go deeper **for just one message**, put `ultrathink` in that message. Your setting stays the same.

The docs add a note: each model has its own effort scale. So `medium` on one model doesn't mean the same as `medium` on another.

## Wording doesn't turn the dial

"Think hard" and "be thorough" aren't magic words. The docs say they're ordinary text. They may nudge Claude a little, but they can't lift it past its effort setting. So if the thinking seems shallow, don't write a longer plea. Try turning up `/effort`.

## How long a change lasts

- `/effort` then `Enter` (or typing a level, like `/effort high`): **saves it as your default** for later chats.
- `/effort` then `s`: **this chat only** (Claude Code 2.1.257 or later).
- `max` applies to this chat only, unless you set it with an environment variable.

!!! tip "In 10-year-old words"
    Easy question, answer fast. Hard question, take your time. The thinking-time dial is `/effort`.

!!! note "★ Going deeper"
    - Effort has an order of priority: environment variable first, then what you pick in the chat, then `--effort` at launch, then your settings, then the model's default.
    - Skills and helpers can have their own `effort:` field. A research helper can run low and a review helper high (Chapter 17).
    - In the terminal, `ultrathink` can also raise that one turn to `xhigh`. When it does, the word shows in rainbow colors (Claude Code 2.1.311 or later).
    - We describe effort the way the docs do: the model decides how much to think at each step. We didn't check how it works inside.

## Try it yourself

1. Type `/effort` to see your current level.
2. Give a hard job, like "Find every claim on this page that isn't in its source," once at `low` and once at `high`. Use `s` so it only changes for this chat.
3. Write down each result's length, how many it found, and how long it took. Compare.

## Use it today

1. **Quick back-and-forth: `low`. A review that must be right: `high`.**
2. **Save `max` for rare, very hard problems.**
3. **Just one deep answer: put `ultrathink` in that message.**

## Common mix-ups

- "Higher is always more accurate." On ordinary jobs, it may only add time and cost.
- "Writing 'try harder' does the same thing." The docs say it doesn't.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. Supported levels and defaults change by model and over time.
- **Source of facts:** [Official docs: Model configuration, Adjust effort level](https://code.claude.com/docs/en/model-config) and [Best practices: Change the model and effort; What you can stop doing](https://code.claude.com/docs/en/best-practices). Read on 2026-11-09.
