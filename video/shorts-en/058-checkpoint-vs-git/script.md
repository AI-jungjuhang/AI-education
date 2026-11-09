# Short en-058 · How are checkpoints different from git?

- **Source page:** 16.3 [How are checkpoints different from git?](../../../docs-en/part5/ch16/checkpoint-vs-git.md)
- **Format:** vertical 9:16, 30fps, about 27 seconds, no voice. Built from `episode.json` with `"lang": "en"`.
- **One idea:** checkpoints are a quick undo inside a session; lasting history belongs to git, so use both.
- **Status:** first draft, waiting for review

| # | Beats | On screen | From the page |
|---|---|---|---|
| 1 | 0–9 | Checkpoints: a quick undo / Lasting history is git's job | "What you'll learn" |
| 2 | 9–21 | Four things it can't undo: Terminal commands / Subagent changes / Your own edits / Linked files | "What checkpoints can't do" table |
| 3 | 21–32 | Two layers: 1. Commit before you start / 2. While working, /rewind / 3. Like it? Commit again | "The two-layer habit" |
| 4 | 32–42 | Before big jobs: Check which files have changed so far, and draft a one-line commit message. / Don't commit until I've checked it. | "Use it today" prompt, copied exactly (split over two bubbles) |
| 5 | 42–57 | Use it today: Using subagents? Commit first / Terminal changes? Undo with git / Like the result? Commit again | "Use it today"; the table ("Use git to undo it"); step 3 of the habit |

## Choices and notes
- The Korean episode opens with "checkpoints are an eraser, git is a photo album." The English title states the point directly, and the metaphor is left out to save room.
- Table rows are shortened to note headings: "Files you changed yourself, or work in another window" → "Your own edits"; "Shortcut files (symlinks) and hard-linked files" → "Linked files".
- The "No code restore" case and the ★ note (`/branch`, worktrees) are left out.
