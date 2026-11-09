# Experiment freely with rewind

<p class="ep-meta"><span>Ch. 16 · 16.3</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Each time you send a message, Claude Code ==automatically saves the state of your files just before it== (a checkpoint).
    - With `/rewind` (or pressing `Esc` twice in an empty prompt), you can take the conversation and the files back, separately or together.
    - Some things can't be undone. The next page covers those.

## Like a save point in a game

In a game, if you save before a boss fight, you can try again when you lose. Claude Code saves "the state of the files right now" every time you send a message. So when you think "That's not the direction I wanted," you can go back to that point. That means you can say "What if we tried this?" without worry.

## How to rewind

Press `Esc` twice when the prompt is empty, or type `/rewind`. A list of the messages you sent appears. Pick the point you want, then pick what to do.

| Option | What it means |
|---|---|
| Restore code and conversation | Both files and conversation go back to that point |
| Restore conversation | Files stay as they are now; only the conversation goes back |
| Restore code | Only the files go back; the conversation stays |
| Summarize from here | Squeeze everything after that point into a summary, to free up memory space |
| Summarize up to here | Squeeze everything before that point into a summary |
| Never mind | Leave without changing anything |

If there's text in the prompt, pressing `Esc` twice clears the text instead. In that case, `/rewind` is the surer way.

The summarize options are like running `/compact` from a point you choose. Summarizing doesn't change any files, and the original messages stay in the session record, so Claude can still look back at the details.

!!! tip "In 10-year-old words"
    Every message you send is an automatic save. If things go the wrong way, go back to a save point.

!!! note "★ Going deeper"
    Claude Code keeps file snapshots for the 100 most recent checkpoints in a session. They're saved with the conversation, so `/rewind` still works after you resume a session. By default, a session's snapshots are cleaned up about 30 days after it last saved one, so rewinding in a very old session can fail. If you want to branch off and try a different approach while keeping the original session untouched, use `/branch` instead of rewinding.

## Try it yourself

In a practice folder, try this:

1. Ask it to make a file called `notes.txt` with a short shopping list.
2. Then ask: "Rewrite everything in notes.txt in Spanish."
3. Open `/rewind` and pick the point just before step 2. Choose **Restore code**.
4. Open `notes.txt`. Is it back in English? The conversation should still be there.

## Use it today

- Before asking for a big change, think "my last message is a save point," and go ahead.
- If you can't decide between two approaches, try one. If you don't like it, restore just the code and try the other.
- In a long chat where memory space is full, summarize from the middle so your first instructions stay intact.

```text
/rewind
```

## Common mix-ups

- "Rewinding always erases the conversation." No. You can choose files only, conversation only, or both.
- "Once I rewind, that's it." After rewinding, sending a new message starts a new path. So look carefully at which point you pick.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Checkpointing](https://code.claude.com/docs/en/checkpointing) and [Commands](https://code.claude.com/docs/en/commands). Read on 2026-11-09.
- **Learning order:** [claude-howto 08-checkpoints](https://github.com/luongnv89/claude-howto/tree/main/08-checkpoints) (MIT; rewritten in our own words).
