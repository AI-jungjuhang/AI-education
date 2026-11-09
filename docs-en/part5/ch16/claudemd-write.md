# How to write a good CLAUDE.md

<p class="ep-meta"><span>Ch. 16 · 16.2</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Notes get followed best when they're ==short, specific, and don't contradict each other==.
    - The official docs suggest keeping each file under about 200 lines.
    - We look at this book project's real CLAUDE.md to see what works and what could be better.

## Vague words don't get followed

"Keep it tidy" is hard even for a person to act on. The official docs give examples like these:

| Vague | Checkable |
|---|---|
| Format code properly | Use 2-space indentation |
| Test your changes | Run `npm test` before committing |
| Keep files organized | API handlers live in `src/api/handlers/` |

The trick is to write things you can **check were done or not done**.

## Short, grouped, and consistent

- **Short.** Aim for under about 200 lines per file. Longer files use more memory space and get followed less.
- **Grouped.** Use headings and bullet points. They're easier to follow than dense paragraphs.
- **Consistent.** If two instructions contradict each other, Claude may pick either one. Clear out old instructions now and then. Running `/doctor prompt-audit` has Claude look for outdated or conflicting instructions and suggest fixes. It doesn't change your files until you ask it to.

Also sort what belongs in the note and what doesn't. Facts it always needs (commands, rules, decisions you can't see from the code) go in the note. Multi-step procedures go in a skill (17.1).

## A real example: this book's CLAUDE.md

This book's repository has a CLAUDE.md. Here are the kinds of things in it:

- The book's name and subtitle, and a rule not to put a personal name in the site address
- The book's structure (part > chapter > section > topic page) and its readers
- Writing rules: high-level content, explained so a 10-year-old can follow
- The work order: check source links → write → build → design check → commit
- The development branch name and the build command

What works: it writes down **decisions that are easy to forget**, like naming rules. You can't figure those out from the code or the files. The official docs agree: don't write what Claude can learn by reading the repository, like the folder layout. Write only what isn't there. What could be better: some long procedures, like how to check video content, are mixed in. Moving those into skills would make the note lighter.

!!! tip "In 10-year-old words"
    Keep the note short, and write it in words you can check: did it do it or not?

!!! note "★ Going deeper"
    When the note grows, you can split it into topic files in a `.claude/rules/` folder, and scope a rule so it applies only to certain kinds of files. You can also pull in another file with `@path`, but imported content still uses memory space, so it doesn't make things shorter. After `/compact`, Claude rereads the project's root CLAUDE.md from disk. So unlike something you only said in the chat, a rule in the note survives the summary.

## Try it yourself

Open the CLAUDE.md of your project (or this book's folder) and pick three instructions. Is each one something you could check? Rewrite the vague ones.

## Use it today

```text
Read CLAUDE.md and find any instructions that contradict each other or look outdated. Don't change anything. Just give me a list.
```

- Put the most important rules at the top, with one line explaining why.
- Write each new rule as one line: what, where, and how.

## Common mix-ups

- "The longer I write, the better it understands." It's the opposite. Longer notes use more memory space and get followed less.
- "Write the note once and you're done." When the project changes, the note goes stale. Check it now and then.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: How Claude remembers your project](https://code.claude.com/docs/en/memory) and [Commands](https://code.claude.com/docs/en/commands) (for `/doctor prompt-audit`). Read on 2026-11-09.
- **Learning order:** [claude-howto 02-memory](https://github.com/luongnv89/claude-howto/tree/main/02-memory) (MIT; rewritten in our own words).
- This book's CLAUDE.md is a file in our own project.
