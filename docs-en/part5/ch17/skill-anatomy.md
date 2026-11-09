# What does a SKILL.md look like?

<p class="ep-meta"><span>Ch. 17 · 17.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - A skill is one folder, and the `SKILL.md` inside is its instruction sheet. The top part is a **label**, and the rest is **the steps**.
    - Normally, ==only the label (the description) sits in memory space. The body loads only when the skill is used.== So even a long skill costs little.
    - You'll learn the two switches that decide who can call a skill.

## A recipe card, not a whole cookbook

Imagine a kitchen with 100 cookbooks. If the cook read all 100 before starting every dish, nothing would ever get cooked. Skills work the other way. At first, only **each card's title and one-line description** are pinned to the wall. The cook pulls out only the cards they need and reads those all the way through. The official docs say the same: a skill's body loads only when it's used, so even long reference material costs almost nothing until then.

The CLAUDE.md note from 16.2 is different. It's read in full at the start of every session. So "facts it always needs" go in the note, and "steps it sometimes needs" go in a skill.

## What the files look like

```text
make-short/
├── SKILL.md        ← required: label + steps
├── template.html   ← a reference file (read only when needed)
└── scripts/
    └── render.sh   ← a tool it runs (run, not read)
```

The top of `SKILL.md` is a label, called **frontmatter**, written between two `---` lines. These are the fields you'll use most.

| Field | What it means |
|---|---|
| `name` | The command name. If you leave it out, the folder name is used |
| `description` | What it does and when to use it. **Claude reads this to decide whether to use it** |
| `disable-model-invocation` | If `true`, Claude can't call it on its own. Only you can, with `/name` |
| `user-invocable` | If `false`, you can't call it. Only Claude can (for background knowledge) |
| `allowed-tools` | Tools it can use without asking while the skill runs |
| `argument-hint` | A hint shown in the prompt for what to type after the name |

Field names must match the table exactly, letter for letter. Unknown field names are ignored without any error, so a typo just silently doesn't work.

## Who can call it: two switches

- **Jobs with side effects, like sending or deploying,** get `disable-model-invocation: true`, so they run only when you call them yourself. The official docs explain it this way: you don't want Claude deciding to deploy just because your code looks ready.
- **Background knowledge, like how an old system works,** gets `user-invocable: false`, so only Claude reads it when it needs to.

!!! tip "In 10-year-old words"
    A skill is a recipe card. Only the titles are pinned to the wall, and you pull out just the card you need.

!!! note "★ Going deeper"
    The `description` (together with an optional `when_to_use`) is cut off at 1,536 characters in the skill list, so put the main use first. With `context: fork`, a skill runs in a separate workspace (a subagent), so it doesn't clutter your conversation. With `paths`, you can make a skill turn on automatically only when Claude works with certain files. Section 17.4 covers subagents.

## Try it yourself

1. Open the `~/.claude/skills/easy/SKILL.md` you made in 16.1.
2. Add one line to the label: `argument-hint: [text to fix]`.
3. In Claude Code, type `/easy`. Does the hint show up? If not, compare the field name with the table, letter by letter.
4. Type `/skills` and check that `easy` appears in your list.

## Use it today

- In `description`, write one sentence for "what it does" and one for "when to use it." Claude needs the "when" to call it on its own.
- When the body gets long, move reference material into its own file, and add one line in SKILL.md saying when to read it.
- For any skill with side effects, add `disable-model-invocation: true` first.

## Common mix-ups

- "Lots of skills always slow things down." The body loads only when used, so short descriptions keep the cost low. Still, lots of descriptions use some memory space too.
- "The `description` can be sloppy." It's the most important field. Claude uses it to decide whether to call the skill on its own.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Extend Claude with skills](https://code.claude.com/docs/en/skills) and [Commands](https://code.claude.com/docs/en/commands) (for `/skills`). Read on 2026-11-09.
- **Learning order:** [claude-howto 03-skills](https://github.com/luongnv89/claude-howto/tree/main/03-skills) (MIT; rewritten in our own words).
