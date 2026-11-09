# Run something automatically at the right moment: hooks

<p class="ep-meta"><span>Ch. 17 · 17.2</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A hook is a promise: "When Claude does X, ==run the program I set up, without leaving it to the AI's judgment==."
    - With skills and notes, the AI chooses whether to follow them. Hooks run **without the AI deciding**, whenever the moment comes (as long as they're set up right and not turned off).
    - You'll learn four common moments (events) and where the settings file goes.

## A motion-sensor porch light

A motion-sensor light on your porch turns on for anyone who walks up. That's different from asking someone, "Don't forget to turn on the light." A hook is the motion-sensor light. The official docs say hooks give you **deterministic control**: certain actions always happen, rather than relying on the model to choose to run them. CLAUDE.md rules are read as background and can be ignored. A hook can't be.

## Four common moments

| Moment (event) | When | Use |
|---|---|---|
| `PreToolUse` | Just **before** a tool runs | Blocking risky actions |
| `PostToolUse` | Just **after** a tool runs | Checks, automatic cleanup |
| `Notification` | When Claude is waiting for your input | Sending you an alert |
| `SessionStart` | When a session starts or is resumed | Loading needed information ahead of time |

There are many more, like `Stop` (when Claude finishes answering) and `PreCompact` (just before a summary). The full list is in the official hooks reference.

## Where the settings go

Hooks go in the `hooks` section of a settings file. Where the file lives decides its reach.

| Location | Reach |
|---|---|
| `~/.claude/settings.json` | All your projects |
| `.claude/settings.json` | This project (commit it to share) |
| `.claude/settings.local.json` | This project, just you |

Here's a hook that alerts you when Claude is waiting for input (for macOS), from the official docs:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

The `matcher` is a filter that picks "only in these cases." What it filters depends on the event. For `PreToolUse` and `PostToolUse`, it's the tool name (like `Edit|Write`). For `Notification`, it's the kind of notification. For `SessionStart`, it's how the session started (fresh, resumed, cleared, and so on). Leave it empty to run in every case. After setting it up, type `/hooks` to see the list of registered hooks. If yours isn't there, check the brackets and commas in the settings file first.

!!! tip "In 10-year-old words"
    A hook is a motion-sensor light. It turns on at the promised moment, even if nobody asks.

!!! note "★ Going deeper"
    Shell commands aren't the only kind of hook. There are also prompt-based and agent-based hooks, where a Claude model makes a judgment, and HTTP hooks that send a signal to a web address. Use the AI kinds for checks that need judgment, and command hooks for checks with clear rules. In this book, we'll try just a command hook.

## Try it yourself

Put the `Notification` hook above in `~/.claude/settings.json`. (Not on a Mac? The docs give commands for Linux, like `notify-send`, and for Windows.) Check with `/hooks` that it's listed. Then ask Claude to do something that needs permission, switch to another window, and wait for the alert. If no alert comes, check the brackets and commas, and make sure the command matches your operating system.

## Use it today

- Turn "must always happen" into a hook, not a note.
- Start with harmless hooks, like alerts.
- After adding a hook, always check it with `/hooks`.

## Common mix-ups

- "A hook is something the AI does." No. It's a program your computer runs. That's why the last page of this section is all about safety.
- "Adding hooks makes Claude smarter." It doesn't get smarter. Your promises just get kept.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide) and [Hooks reference](https://code.claude.com/docs/en/hooks). Read on 2026-11-09.
- **Learning order:** [claude-howto 06-hooks](https://github.com/luongnv89/claude-howto/tree/main/06-hooks) (MIT; rewritten in our own words).
