# Test it and fix it

<p class="ep-meta"><span>Ch. 15 · 15.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Instead of "it seems to work," ==set success criteria, make test questions, and measure a score==, then improve.
    - Include tricky cases in your tests, and when you fix things, change one thing at a time and measure again.
    - Add complexity only when the score clearly gets better.

## Practice tests

Athletes don't enter a race because they "feel fast." They time themselves, find weak spots, fix them, and time themselves again. Agents and prompt templates are the same. **If you don't measure, you can't tell whether it got better.**

!!! tip "In 10-year-old words"
    Take a practice test, fix the questions you got wrong, and take the test again. Check with numbers whether your score went up.

## The cycle Anthropic describes

Anthropic's guide to testing describes a cycle for improving a prompt (a template or set of instructions):

1. **Set success criteria.**
2. **Write test cases.** Don't forget the unusual ones.
3. **Write a first prompt.**
4. **Run it on the test cases.**
5. **Improve it.** Then go back to step 4.
6. **Do a final check before you ship it.**

Good success criteria are **specific** and **measurable**. Not "good performance," but something like "sorts customer feedback by feeling correctly." Numbers work best. When numbers are hard, use **a rating scale that's applied the same way every time**. The guide says even fuzzy-sounding goals like safety can become numbers, for example: "fewer than 0.1% of 10,000 outputs get flagged as harmful."

## A light version for you

For one person or a small team, try a lighter version.

**1. One line of success criteria.** "In 9 out of 10 customer questions, it quotes the right policy."

**2. Ten test questions.** Six easy, three hard, and one strange on purpose (a question the policy doesn't cover, or a vague one). That follows the guide's advice to cover unusual cases.

**3. A scorecard.** Mark each answer right or wrong (or use a 3-point scale). Write one line about what went wrong.

**4. Gather the misses and find the cause.** Were the instructions vague? Was material missing? Did a tool find the wrong thing?

**5. Fix one thing, then measure again.** If you change several things at once, you won't know which one helped.

**6. Hide a few test questions.** Keep two or three that you don't look at while fixing, and use them only at the end. That stops you from fixing it to fit just your test questions. Anthropic's post on tool design recommends this kind of **held-out** test set too.

## Who does the grading?

- **Jobs with a clear right answer:** a person or a simple rule can grade them (Are the numbers right? Are the needed words there?).
- **Jobs without one clear answer (like writing quality):** grade with a rubric a person wrote ahead of time. Anthropic's guide covers many ways to grade, from checking for an exact match to **having an AI do the grading**.
- Even when AI grades, **have a person check some of them** to make sure the grading can be trusted.

!!! note "★ Going deeper"
    - The post on building agents says again and again that **measuring performance and improving is the heart of it**, and to **add complexity only when results clearly improve** (Chapter 14). Evaluation is how you decide what "clearly" means.
    - The tool design post (previous page) measures tools with evaluations and then works with an agent like Claude Code to improve them. Anthropic's post *Demystifying evals for AI agents* (2026-01-09) looks at evaluating agents in more depth. We checked only its title and date for this page.
    - A test score is not the same as real-world performance. If the test questions don't look like the real job, the score can rise without the work getting better (the traps in benchmarks, Chapter 21).

## Try it yourself

Make a practice test for one template from Chapter 8 (or the guide you wrote earlier in this chapter).

| # | Test input | Expected result | Right / Wrong | Notes |
|---|---|---|---|---|
| 1 | (easy) | | | |
| 2 | (easy) | | | |
| ... | | | | |
| 10 | (strange on purpose) | | | |

1. Run all 10 with the template as it is, and write down the score.
2. Find the most common cause of the misses, and fix **just that one thing**.
3. Run all 10 again. Did the score go up?

## Use it today

1. **Write your success criteria in one line.** Without them, you can't say "it got better."
2. **Start with 10 test questions.** (Add more later.) Always include at least one tricky one.
3. **Fix one thing at a time.** That's how you find what worked.
4. **Hide a few test questions.** Use questions you didn't look at while fixing for the final check.
5. **When the model or service changes, measure again.** Compare with the same test (Chapter 8).

## Common mix-ups

- "I tried it a few times and it worked." A few tries can be luck. Measure with the same test.
- "The more test questions, the better." Ten is enough to start. What matters is including tricky cases.
- "AI does the grading, so no person needs to look." Check some yourself, so you can trust the grading.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), Claude Platform Docs. The improvement cycle, specific and measurable criteria, the 0.1%-of-10,000 example, covering edge cases, and ways of grading, including grading by AI. Read on 2026-11-09.
    - Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 2024-12-19. Measure and improve, and add complexity only when it helps.
    - Anthropic, [Writing effective tools for agents — with agents](https://www.anthropic.com/research/writing-tools-for-agents), 2025-09-11. Evaluation-driven improvement and held-out test sets.
    - Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026-01-09. We checked only the title and date.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The six-step light version (10 tests, hidden questions, and so on) is our own personal-sized version of the guide's developer cycle.
