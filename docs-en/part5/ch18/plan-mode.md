# Make a plan first, then hand it off

<p class="ep-meta"><span>Ch. 18 · 18.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Plan mode is ==a mode where Claude researches and plans without editing your files==.
    - Real work starts only after you read the plan and approve it, or ask for changes.
    - For big or confusing jobs, it builds the habit of "look at the blueprint before you build."

## A blueprint before the house

You wouldn't tell a builder, "Just start putting up walls." You'd look at the blueprint first and say, "Make this a door, not a window," and then they'd build. Plan mode is that blueprint step. The official docs describe it as a mode where Claude researches and proposes changes without making them. It reads files and runs commands to explore, then writes a plan, but it doesn't edit your source.

## Turning it on and off

- Press `Shift+Tab` until the status bar shows plan mode. (It cycles through the other modes too.)
- To plan just once, start your message with `/plan`.
- To start in plan mode from the beginning:

```bash
claude --permission-mode plan
```

When the plan is ready, Claude shows it and asks how to go on.

| Choice | What it means |
|---|---|
| Yes, and use auto mode | Approve, and let it carry on in auto mode (if auto mode is available; otherwise the option auto-accepts edits) |
| Yes, manually approve edits | Approve, but review each edit yourself |
| No, keep planning | Stay in plan mode and tell Claude what to change |

You can press `Ctrl+G` to open the plan in your own text editor and change it directly. Approving ends plan mode and the work begins. To leave plan mode without approving, press `Shift+Tab` again.

## Using it for our channel

A job like "Make a video for page 1.1.2 on tokens" can easily go off track if you ask for it all at once. Use plan mode like this:

```text
/plan Make a plan to turn docs-en/part1/ch01/tokens.md into a short video. Tell me how many scenes, which parts of the page each uses, and which files you'll create. Don't create any files yet.
```

If you spot "this scene isn't in the original" in the plan, don't approve. Say, "Drop that scene and plan again." Fixing a wrong plan is much cheaper than undoing work that went the wrong way.

!!! tip "In 10-year-old words"
    Plan mode is the blueprint step. Look at the blueprint, fix it, and then start building.

!!! note "★ Going deeper"
    How plan mode handles shell commands depends on your setup. If auto mode is available, a classifier reviews each command and lets the safe ones run. If not, commands outside a built-in read-only set ask you first. And in interactive terminal sessions where bypass permissions are available, edits aren't actually blocked during planning. Claude is told not to edit, but nothing stops it if it tries. So don't treat plan mode as your only safety net.

## Try it yourself

1. In a practice folder, start with `claude --permission-mode plan`.
2. Ask: "Make a plan to create a README.md in this folder."
3. When the plan appears, don't approve it. Say: "Don't use emoji in the title. Update the plan with that."
4. When you like it, choose "Yes, manually approve edits" and watch it carry out the plan.

## Use it today

- For jobs that touch three or more files, plan first.
- In the plan, check: which files it will create, where its facts come from, and whether it's adding anything you didn't ask for.
- If the plan is vague, ask questions instead of approving.

## Common mix-ups

- "Plan mode always stops file edits." It usually does, but not in every setup (see "Going deeper").
- "I approved the plan, so the result is right." Approving means you OK'd the direction. Check the result separately.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Choose a permission mode (Analyze before you edit with plan mode)](https://code.claude.com/docs/en/permission-modes). Read on 2026-11-09.
- **Learning order:** [claude-howto 09-advanced-features](https://github.com/luongnv89/claude-howto/tree/main/09-advanced-features) (MIT; rewritten in our own words).
