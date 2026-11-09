# Hand it a file and give it a job in one line

<p class="ep-meta"><span>Ch. 16 · 16.4</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - In the terminal, `|` (a pipe) is ==a tube that passes one command's output to the next command==.
    - With one line, `cat file | claude -p "..."`, you can have it read a file and do a job.
    - This one line is the first piece of the automation pipeline in 18.2.

## A conveyor belt

Picture a factory conveyor belt. The first machine makes something, and the belt carries it to the second machine. The `|` symbol in the terminal is that belt. `cat` is a machine that pulls out a file's contents, and `claude -p` is a machine that reads and works on them.

```bash
cat error.log | claude -p "Explain in three lines why this error happened"
```

To save the result to a file, add `>`.

```bash
cat script.md | claude -p "Mark any words that are hard to read" > review.md
```

The official docs show the same shape: pipe in a build error file, ask for a short explanation of the cause, and save it to a file.

## Using it for our channel's videos

After writing a script, we want to run a check on it. That check can be one line.

```bash
cat docs-en/part1/ch01/next-word.md | claude -p "Find words that would be hard for a 10-year-old. Just give me a list."
```

You can also check only what changed. The official docs show `git diff main | claude -p "..."`, which passes just the changes to look for typos.

## Setting the shape of the result

Plain text is fine for a person to read. But if another program will read it, the shape needs to be fixed.

```bash
claude -p "List the part titles of this book" --output-format json
```

`--output-format` can be `text` (the default), `json`, or `stream-json`. If the result must follow an exact shape, you can give it one with `--json-schema`. We'll try that in 18.2.

!!! tip "In 10-year-old words"
    `|` is a conveyor belt. Send a file down it to the AI, and the job's done in one line.

!!! note "★ Going deeper"
    In one-line mode, there's nobody to answer a permission question. So jobs like editing files or running commands need permission ahead of time. An option like `--allowedTools "Read,Edit"` lets those tools run without asking. Give only the permission you need, as narrowly as you can. The wider the permission, the bigger the damage if something goes wrong. (Since v2.1.302, a `-p` run with no permission mode set denies any call that needs approval.)

## Try it yourself

1. Pick any text file (a Markdown file from this book's `docs-en` folder works well).
2. Run `cat file | claude -p "Summarize this in three lines"`.
3. Add `> summary.txt` at the end and check that the result is saved to a file.

## Use it today

- Don't copy and paste long error messages. Pipe them in.
- If you run the same check twice, save the one-line command in a note. It'll soon become a skill (17.1) or a script (18.2).
- Before you pipe in a file, make sure it has no passwords or personal details. Whatever you pipe in is sent to the AI service.

## Common mix-ups

- "Only developers use pipes." No. It just passes a file's contents along. You only need to learn it once.
- "One-line mode can edit any file." `--allowedTools` sets which tools can run **without asking**. To limit which tools exist at all, use `--tools`. In one-line mode there's no one to ask, so tool calls without permission can be denied. Don't give wide permission.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: CLI reference](https://code.claude.com/docs/en/cli-reference) and [Run Claude Code programmatically](https://code.claude.com/docs/en/headless). Read on 2026-11-09.
- **Learning order:** [claude-howto 10-cli](https://github.com/luongnv89/claude-howto/tree/main/10-cli) (MIT; rewritten in our own words).
