# Give it a test it can check itself against ★

<p class="ep-meta"><span>Ch. 23 · 23.4 · Deeper</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Claude ==stops when the job looks done==. Without a way to check, "looks done" is all it has to go on.
    - The fix is to give it **a check that answers pass or fail**. Then a loop runs: make it, check it, fix it.
    - Checks come in four strengths. And always ask for **evidence**.

## Grading your own homework

If you do your homework and never check the answers, you hand it in with mistakes. With an answer key, you can grade it, fix it, and hand it in right. In Part I (1.1.3), you learned that AI can say things that sound right but are wrong. So a job should end on **a signal you can check**, not on "sounds right." The official best practices say the same. Without a check, you become the tester, and mistakes stay until you notice them.

## Four strengths of check

The docs list these, from loosest to strictest:

| Strength | How | Who decides it's done |
|---|---|---|
| 1. In the request | "Run the tests after, and keep going until they pass" | Claude decides when it's satisfied |
| 2. As a goal | `/goal` plus a condition | A separate model checks the condition after every turn |
| 3. A Stop hook | The `Stop` hook from Chapter 17 | Claude Code itself enforces it. The turn can't end until the check passes (up to a limit) |
| 4. Someone else reviews | `/code-review`, or a reviewer helper | Eyes that never saw your chat |

A check can be almost anything, as long as Claude can read the result:

- A test file, a build's exit code, or a linter (a style-checking tool)
- A script that compares the output to an expected file
- A screenshot set next to the design

The docs add: if your project already has a check like this, the most useful line in your CLAUDE.md is the command that runs it.

## Always ask for evidence

"All tests pass," on its own, tells you very little. The docs say to ask for **evidence: the command Claude ran and its output, or a screenshot**. For a chat you weren't watching, that's the only evidence you have. And reading the output is faster than running the check again yourself.

```text
Before you say you're done, show me the check command and its full output.
```

## Tell reviewers to skip style

One tip for the review step. If you ask a reviewer to find problems, **it will always find something.** If you fix every finding, you end up with extra layers and tests for cases that can't happen. The best practices say to narrow the job, like "report gaps that affect correctness, and skip style." That's why the `reviewer` helper in Chapter 17 says "If there are no problems, just say 'No problems.'"

!!! tip "In 10-year-old words"
    You grade homework with an answer key. Give the AI an answer key (a check), so it can grade and fix its own work.

!!! note "★ Going deeper"
    - After Claude says it's done, the docs suggest running `/verify`. Claude builds and runs your app and looks at the result. That catches problems tests and type checks miss.
    - A Stop hook can't block forever. If it blocks **eight times in a row** with no tool use in between, Claude Code steps in and ends the turn. Your hook should check `stop_hook_active` to see if it already sent Claude back (next page).
    - `/goal` matters most for long runs nobody is watching. In a normal chat, you rarely need it.

## Try it yourself

1. Think of a recent job where an AI said "Done!"
2. Write down whether there was a pass-or-fail check that showed it was really done. If not, what check could there have been?
3. Next time, end the request with "Show me the check command and its output," and compare.

## Use it today

1. **Write "done" as pass or fail:** for example, "zero warnings from the link check."
2. **Narrow the reviewer's job:** "correctness only, skip style."
3. **Ask for the command and its output** with every "done."

## Common mix-ups

- "It passed the check, so it's perfect." A check can't catch what it doesn't test. A link can open and the content can still be wrong.
- "Having the AI review its own work is enough." A reviewer that never saw your chat looks without that bias (Chapter 17). Self-review alone may not be enough.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Claude Code best practices: give Claude a check, review against a spec, enforce the check with a Stop hook](https://code.claude.com/docs/en/best-practices), [/goal](https://code.claude.com/docs/en/goal), and [/code-review](https://code.claude.com/docs/en/code-review-local). Read on 2026-11-09.
- Why AI makes things up is covered in 1.1.3, "Sounds right, can be wrong: hallucination."
