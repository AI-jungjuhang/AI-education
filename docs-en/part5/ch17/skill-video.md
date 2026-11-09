# Hands-on: a skill that makes one video

<p class="ep-meta"><span>Ch. 17 · 17.1</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - We bundle **a job our channel does over and over**, turning one book page into a short video, into a skill.
    - A skill isn't code. It's ==writing that lays out the steps and the standards==. So you can write one yourself.
    - This skill grows into the agents in 17.4 and the super skill in 18.2.

## Find the job you repeat

Every time our channel makes a video, it follows the same flow: read a book page, write a scene list, build the screens, render, and check. That flow is already written down in this repository's `.claude/skills/video-script/SKILL.md`. On this page, you'll build a small skill that does the same kind of job, from scratch.

## How to make it

Make the folder. (If you put it inside the project, it's shared along with the repository.)

```bash
mkdir -p .claude/skills/make-short
```

Then write this in `.claude/skills/make-short/SKILL.md`:

```markdown
---
name: make-short
description: Use when turning one book page into a vertical short video script under 60 seconds. Use for requests like "make this a video" or "write a shorts script."
disable-model-invocation: true
argument-hint: [page path]
---

Target page: $ARGUMENTS

1. Read the target page and CLAUDE.md. Pick **one idea** from the page
   and **one action** for viewers to take away.
2. Write a scene list. For each scene, note which part of the page it comes from.
3. Don't add anything that isn't in the page. Label any made-up numbers
   on screen as "example."
4. Keep on-screen text short. Show what viewers will learn within the first 5 seconds.
5. Don't add an ending scene or a preview of the next episode. Don't show a web address.
6. Save the result as script.md in a new folder under video/shorts-en/.
   At the bottom, list anything you left out or couldn't check.
```

Three things matter most here.

- `disable-model-invocation: true`: making a video takes time and creates files. It should run only when you call it.
- `$ARGUMENTS`: pass the page in, like `/make-short docs-en/part1/ch01/next-word.md`.
- Numbered steps: when order matters, numbers keep steps from being skipped.

## Write it, then improve it

Run `/make-short docs-en/part1/ch01/next-word.md` and read the script it makes. If something bothers you, fix that line in the skill file. For example, if the first scene is flat, add "Start the first screen with a one-line question." **Looking at the results and fixing the instructions** is how a skill grows.

!!! tip "In 10-year-old words"
    Write down the steps and standards of a job you repeat. Then you can call it by one name and have it done the same way.

!!! note "★ Going deeper"
    This repository's real `video-script` skill covers more than the script. It also guides rendering and checking, and it keeps template files and build scripts in the same folder. Scripts inside a skill folder are helper files the skill reads or runs when it needs them. Start with just the writing, like above. As you use it more, add scripts and templates one at a time.

## Try it yourself

1. Make the skill above.
2. Run it on any page of this book.
3. In the scene list it makes, look for anything that isn't in the original page. If you find something, add a line to the instructions that rules it out.

## Use it today

- If the answer to "Will I do this again?" is yes, make it a skill.
- Don't aim for perfect on the first try. Five lines is enough for version one. Improve it as you use it.
- For skills that save files, say in the instructions where to save them.

## Common mix-ups

- "With a skill, the result is always the same." Even with the same instructions, AI answers can vary (as you learned in 1.1.1). That's why you need a checking step.
- "The skill makes the video itself." The skill above only makes the script. Jobs like rendering need scripts and tools attached.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09.
- **Source of facts:** [Official docs: Extend Claude with skills](https://code.claude.com/docs/en/skills). Read on 2026-11-09.
- The example is our own, based on this repository's `.claude/skills/video-script`.
- **Learning order:** [claude-howto 03-skills](https://github.com/luongnv89/claude-howto/tree/main/03-skills) (MIT; rewritten in our own words).
