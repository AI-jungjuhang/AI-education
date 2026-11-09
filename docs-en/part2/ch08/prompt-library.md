# Keep your favorite prompts

<p class="ep-meta"><span>Ch. 8 · 8.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Save prompts that worked well, ==give them names, and tweak them each time you use them==. They become your own toolbox.
    - For each template, also write down when to use it, a good example, and what to watch for.
    - Don't just collect them. Test them now and then, and fix them.

## Making a cookbook

When a dish turns out great, writing down the recipe lets you make it again. Without it, you end up asking, "What did I put in that time?"

Prompts work the same way. If you collect the question templates from Chapter 2, you won't have to start from scratch each time. And as you use them, they keep getting better.

!!! tip "In 10-year-old words"
    Write your good prompts in a cookbook. Use them again, and make them a little better each time.

## What to write for each one

| Field | What to write | Example |
|---|---|---|
| Name | A name you'll recognize at a glance | Weekly update draft |
| When to use | The situation it fits | Every Friday, reporting to the team |
| Template | The prompt, with blanks | (a question template from Chapter 2) |
| A good example | An input and result that worked well | Last week's update |
| Watch for | Where this template goes wrong | Check whether numbers changed |
| Last updated | When you last changed it | 2026-11-09 |

## Where to keep them

- **A notes app or a single document** is plenty. You don't need a fancy tool to start.
- **Pick a naming rule.** For example, "[Type] Kind: name," like "[Writing] Summary: for my manager."
- **Start with about ten.** (That's our suggestion.) With too many, it gets hard to use them.
- If your service has a feature like "custom instructions" or "projects," you may be able to save templates there. (It differs by service.)

## Test and improve

Anthropic's guide to building tests describes how to improve a prompt. Set success criteria. Write test cases, including tricky ones. Test the prompt. Fix it, and repeat. It says success criteria should be **specific and measurable**.

For personal use, you can make it lighter:

1. **One line of success criteria.** For example: "Not a single number changes, and it's 5 sentences or fewer."
2. **Three test inputs.** Keep two normal ones and one tricky one.
3. **Re-test with all three after each fix.** See whether fixing one thing made another worse.

!!! note "★ Going deeper"
    - **When the model changes, results can change too.** If a template that used to work starts missing, check it again with your three test inputs. It's a common good practice to re-run your tests after a model update.
    - Sharing a collection of templates with your team helps a lot. Just don't put "good examples" with personal or secret details in it (Chapter 3).
    - There are tools that run tests like these automatically (evaluation tools). For personal templates, they may be more than you need.

## Try it yourself

1. Pick the 3 most useful question templates you've made from this book.
2. Fill in every field from the table above and save them in your notes app.
3. Use them for a week, and add what really happened to "A good example" and "Watch for."

## Use it today

1. **Save a prompt once you've used it three times.** Write it by hand twice, then save it the third time.
2. **"Watch for" is the most important field.** Your mistakes are what fill it in.
3. **Write your success criteria in one line.** You need a standard for "it worked" before you can improve anything.
4. **Clean up once a month.** Delete the ones you don't use, and improve the ones you use often.
5. **Remove personal details before sharing.** Make sure no names are hiding in "A good example."

## Common mix-ups

- "The more templates, the better." Too many are hard to find, so you won't use them. Start with ten or fewer.
- "Once I make one, I'm done." Models and your work both change. Test now and then.
- "I can just use someone else's templates." That's a fine start, but you'll need to adjust them to your work.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests), Claude Platform Docs. Specific and measurable success criteria, tests that include edge cases, and the test-and-refine cycle. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The light personal method (one line of criteria, three test inputs) is our own shortened version of the guide's developer method. "Re-test after a model update" is a general good practice, not a sentence we confirmed in the guide. Saving features differ by service.
