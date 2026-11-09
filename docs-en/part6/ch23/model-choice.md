# How do you choose a model?

<p class="ep-meta"><span>Ch. 23 · 23.3</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Choosing a model is ==a trade between power, speed, and cost==. The default is enough for most work.
    - Pick by **alias** (a short nickname), not by exact name. Then you keep up when models change.
    - A simple rule: everyday work, the default. Light jobs, a small model. The hardest and longest jobs, the biggest model.

## Bike, car, or plane

You bike to the corner shop, drive to the next town, and fly to another country. A plane isn't always best. Flying to the corner shop would cost a lot and take more time. AI models are like that too. Big models handle hard jobs well but are slower and cost more. Small models are quick and cheap.

## Choose by alias

Here are the aliases the official docs list. The right-hand column is what they pointed to **on the Anthropic API, as of 2026-11-09**.

| Alias | What it's for | On this date |
|---|---|---|
| `default` | Go back to your account's default | Depends on your plan |
| `sonnet` | Everyday coding | Sonnet 5.5 |
| `opus` | Complex reasoning | Opus 5.5 |
| `haiku` | Quick, simple jobs | Haiku 5.5 |
| `fable` | Your hardest, longest-running jobs | Fable 5.1 (never the default; you pick it yourself) |
| `best` | The top model you can use | Same as `fable` if you have it, otherwise `opus` |
| `opusplan` | Opus while planning, Sonnet while doing | Goes with plan mode (Chapter 18) |

What an alias points to can differ by provider. On some cloud providers, `sonnet` and `haiku` point to older versions. So instead of memorizing model names, use aliases and check with `/model`.

## How to choose

Here's the official best practices advice, in plain words:

- **The default model** handles most coding well. You don't need to change it at first. (On most plans, that's Opus 5.5 at medium effort.)
- **Sonnet** costs less on routine work.
- **Haiku** fits helpers (subagents) doing simple jobs, like a `researcher` helper from Chapter 17.
- **Fable** is for jobs too big for one sitting. The docs say Fable models keep working on their own for a long time, look into things before acting, and check their own work more often.

For a video channel, that might look like this: a `researcher` that checks page links runs on Haiku or Sonnet, a `scriptwriter` uses the default, and a plan to restructure the whole book uses `opusplan` or Fable. **That's our suggestion, not a rule.** Test it against your own work and budget.

## How to switch

- **In a chat:** type `/model sonnet`. That also saves it as your default. To change it for this chat only, open the picker with `/model` and press `s` on the model's row. (`Enter` in the picker saves it as your default.)
- **When starting:** `claude --model sonnet`
- **For a helper:** the `model:` field in its file (Chapter 17)

!!! tip "In 10-year-old words"
    Bike for short trips, plane for long ones. Pick the model that fits the job.

!!! note "★ Going deeper"
    - The docs describe **automatic fallback**: if a model is busy or a safety check flags a request, Claude Code can switch to another model.
    - Admins can limit which models people in their organization can pick. If your `/model` list differs from this page, that may be why.
    - Sonnet 5.5 and Opus 5.5 need fairly recent versions of Claude Code. If one fails, run `claude update`.

## Try it yourself

1. Open `/model` and check which model you're on and what else you can choose.
2. Give the same small job (like summarizing a page) to `haiku` and to the default. Use `s` so it only changes for this chat. Compare the results and how long each took.
3. Check `/usage` to see how your usage changed.

## Use it today

1. **Small model for light, repeated jobs. Big model for big, tricky ones.**
2. **Use aliases, not exact model names,** and check with `/model`.
3. **Compare for yourself: same job, two models.** Other people's rankings may not fit your work (Chapter 21).

## Common mix-ups

- "The most expensive model is always best." For some jobs, it's a waste.
- "An alias always means the same model." Aliases point to the latest version, so they change over time. That's why this page has a date.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. Model names and what aliases point to go out of date faster than anything else in this book.
- **Source of facts:** [Official docs: Model configuration](https://code.claude.com/docs/en/model-config) and [Best practices: Change the model and effort](https://code.claude.com/docs/en/best-practices). Read on 2026-11-09.
