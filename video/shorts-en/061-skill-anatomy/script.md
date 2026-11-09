# Short en-061 · What does a SKILL.md look like?

- **Source page:** 17.1 [What does a SKILL.md look like?](../../../docs-en/part5/ch17/skill-anatomy.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** only a skill's label sits in memory space; the body loads only when the skill is used.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | A skill loads only when used / Like recipe cards: only titles on the wall | "What you'll learn"; "A recipe card, not a whole cookbook" |
| 2 | 9–20 | CLAUDE.md: Read in full every session (facts it always needs) / A skill: Body read only when it's used (steps it sometimes needs) | Second paragraph of "A recipe card..." |
| 3 | 20–33 | Label fields: name → the command name / description → what it does, when to use it / disable-model-invocation: true → only you can call it / user-invocable: false → only Claude can call it | The frontmatter field table |
| 4 | 33–43 | In description, write: What it does and when to use it / Claude needs the "when" to call it on its own | "Use it today", first bullet |
| 5 | 43–58 | Use it today: Side effects? Only you call it / Body too long? Move it to a file / Spell field names letter for letter (typos are ignored silently) | "Use it today"; the note under the field table |

## Choices and notes
- The Korean episode's title is the recipe-card metaphor. The English title states the point, and the recipe cards move to the sticker.
- The Korean episode shows fields on sticky notes. English field names are too wide for the notes, so scene 3 is a list.
- `allowed-tools`, `argument-hint` and the ★ note (1,536-character cut-off, `context: fork`, `paths`) are left out.
