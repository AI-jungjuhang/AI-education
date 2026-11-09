# Chat mode and one-line mode

<p class="ep-meta"><span>Ch. 16 · 16.4</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - `claude` opens a back-and-forth **chat mode**. `claude -p "question"` is a **one-line mode** that gives you an answer and ends.
    - One-line mode ==runs without a person, so it's the door to automation==.
    - With continue (`-c`) and resume (`-r`), you can pick up yesterday's conversation.

## A restaurant vs a vending machine

Chat mode is a restaurant. You order, change your mind, and talk with the chef. One-line mode is a vending machine. Press one button, a drink comes out, and that's it. Nobody has to stand there watching.

| What you want | Command |
|---|---|
| Start a chat | `claude` |
| Start a chat with a first question | `claude "explain this project"` |
| Get just an answer, then end | `claude -p "explain this function"` |
| Continue the most recent chat (in this folder) | `claude -c` |
| Reopen a chat by name or ID | `claude -r "name" "finish this"` |
| Check the version | `claude -v` |

In chat mode, typing `/resume` also lets you pick a past conversation.

## Choosing the model and folders

You can set a few things when you start.

```bash
claude --model sonnet                 # the model to use in this session
claude --add-dir ../another-folder    # one more folder it can read and edit
claude --permission-mode plan         # start in a mode that only makes a plan first
```

Adding a folder with `--add-dir` gives it permission to read and edit files there. Only add folders you trust. Chapter 18 covers permission modes.

!!! tip "In 10-year-old words"
    `claude` is a restaurant. `claude -p` is a vending machine, and a vending machine runs on its own.

!!! note "★ Going deeper"
    When you use one-line mode for automation, adding `--bare` makes it start faster. It skips loading hooks, skills, plugins, MCP servers, auto memory, and CLAUDE.md. The official docs recommend `--bare` for scripts, and say it will become the default for `-p` in a future release. But `--bare` doesn't use your subscription login. To use the Anthropic API, set `ANTHROPIC_API_KEY` in your environment. (Other providers like Amazon Bedrock use their own credentials.) On the other hand, `-p` without `--bare` runs the project's hooks and connects its MCP servers, even in a folder you've never trusted, with no warning dialog. So be careful in folders you don't know (17.2, 17.3).

## Try it yourself

1. Run `claude -p "What is 1 plus 2 plus 3 plus 4 plus 5? Answer with just the number."` One line comes back, and the program ends.
2. Open `claude`, ask anything, then leave with `/exit`.
3. Run `claude -c` to reopen the chat you just had.

## Use it today

- For one-off questions, use `claude -p`. No need to open and close a window.
- Pick up yesterday's work with `claude -c`. You don't have to explain everything again.
- Open a named conversation with `claude -r "name"`.

## Common mix-ups

- "One-line mode is a weaker AI." No. It's the same AI, working without a back-and-forth.
- "`-c` remembers everything from yesterday." The reopened chat keeps its history. In a brand-new chat, though, it's still the CLAUDE.md note (16.2) that gets read.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: CLI reference](https://code.claude.com/docs/en/cli-reference) and [Run Claude Code programmatically](https://code.claude.com/docs/en/headless). Read on 2026-11-09.
- **Learning order:** [claude-howto 10-cli](https://github.com/luongnv89/claude-howto/tree/main/10-cli) (MIT; rewritten in our own words).
