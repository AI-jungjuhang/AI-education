# Permission modes and safety

<p class="ep-meta"><span>Ch. 18 · 18.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A permission mode is **the range of things Claude may do without asking**. It's a trade between convenience and safety.
    - To start, Manual and plan mode are enough. Open up the others step by step, when you have a reason.
    - `bypassPermissions` is a mode ==only for use inside containers or virtual machines==.

## A car's driver-assist features

When you first learn to drive, you go slowly and grip the wheel tight. Later you might use cruise control, but only on safe stretches of highway. Permission modes are like those driver-assist features. The official docs describe each mode as a different trade between convenience and oversight.

| Mode | Runs without asking | Good for |
|---|---|---|
| Manual (setting value `default`) | Reads only | Checking every action yourself; sensitive work |
| `acceptEdits` | Reads, file edits, and common file commands (`mkdir`, `touch`, `mv`, `cp`, and so on) | Repeating work while you review the results |
| `plan` | Reads (plus classifier-approved commands when auto mode is available) | Exploring before changing anything |
| `auto` | Nearly everything, with background safety checks | Long jobs, cutting down on constant questions |
| `dontAsk` | Only pre-approved tools; everything else is denied | Locked-down automation (CI) |
| `bypassPermissions` | Everything | Isolated containers and virtual machines only |

You can cycle through modes during a chat with `Shift+Tab` (some modes don't appear in the cycle unless you start with them), and set one at launch with `--permission-mode`.

**Check which mode your chat starts in.** The official docs say that in Claude Code v2.1.283 and later, a new session in a terminal starts in `auto` by default. (If auto mode isn't available, for example because of your organization's settings or your model, it starts in Manual.) One-line mode (`claude -p`) starts in Manual (`default`). Look at the mode name in the status bar. If you want to check every action, start like this:

```bash
claude --permission-mode default
```

## Rules on top

A mode sets the baseline. On top of it, you can add **permission rules** that pre-approve or block specific tools. The official docs say deny rules apply in every mode, even `bypassPermissions`. `/permissions` shows your allow, ask, and deny rules in one place and lets you change them.

## What no mode approves automatically

The official docs list things that aren't auto-approved in any mode, not even `bypassPermissions`. These include tools you've marked "ask," tools that need a person's input, and deleting important paths with `rm`. Also, writing to protected paths is never auto-approved except in `bypassPermissions` mode (and in plan sessions where bypass is available).

## Our choices

| Job | Mode |
|---|---|
| Writing book pages, making videos | Manual or `acceptEdits` (because we review the results) |
| Designing a big change | `plan` |
| Scripts that repeat the same job automatically | `dontAsk`, with only the needed tools allowed |
| `bypassPermissions` | We don't use it |

!!! tip "In 10-year-old words"
    Permission modes are driver-assist features. Turn them on one at a time, only on roads you know.

!!! note "★ Going deeper"
    For automation (CI), the official docs show a precise allow-list approach: run `claude -p` with `--permission-mode dontAsk` and allow only the exact tools needed. To run fully unattended, they show `--dangerously-skip-permissions`, but only inside a container, virtual machine, or sandbox. This book doesn't cover that last approach.

## Try it yourself

1. Open `/permissions` and read your current allow, ask, and deny rules. If there's a rule you don't recognize, find out where it came from.
2. Press `Shift+Tab` and watch the mode name change in the status bar. Don't stop in the middle. Cycle back to the mode you started in.

## Use it today

- In a new folder or someone else's repository, start with `--permission-mode default` and just look around in plan mode.
- Turn on `acceptEdits` only for jobs where you'll open and check the results.
- Make sure `bypassPermissions` isn't set in your settings files.

## Common mix-ups

- "Auto mode means it's safe." Auto mode has safety checks, but no system is perfect. For important work, check things yourself.
- "Once set, the mode stays the same." It can change during a chat, and approving a plan changes it too. Glance at the current mode now and then.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. Auto mode isn't available in every setup; it depends on your model and organization settings.
- **Source of facts:** [Official docs: Choose a permission mode](https://code.claude.com/docs/en/permission-modes) and [Configure permissions](https://code.claude.com/docs/en/permissions). Read on 2026-11-09.
- **Learning order:** [claude-howto 09-advanced-features](https://github.com/luongnv89/claude-howto/tree/main/09-advanced-features) (MIT; rewritten in our own words).
