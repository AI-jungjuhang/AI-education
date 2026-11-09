# Build an automation pipeline on the command line

<p class="ep-meta"><span>Ch. 18 · 18.2</span><span>About 8 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Put `claude -p` inside **a loop**, and you get a pipeline that checks many files at once.
    - Three safety rules for automation: ==allow tools narrowly, cap the rounds and the cost, and don't read unfamiliar folders==.
    - You can get results two ways: files for people to read, and JSON for programs to read.

## Add a loop to the conveyor belt

In 16.4, you handled one file with `cat file | claude -p "..."`. What if you have 100 files? Run that one line 100 times in a loop. That's the simplest pipeline.

```bash
#!/bin/bash
# For each page in docs-en, list words a 10-year-old would find hard, and save to out/.
set -euo pipefail
mkdir -p out

find docs-en -name '*.md' -print0 | sort -z | while IFS= read -r -d '' f; do
  name=$(echo "$f" | tr '/' '_')
  claude --bare -p \
      "List only the words a 10-year-old would find hard to read. If there are none, say 'none'." \
      --allowedTools "Read" --max-turns 3 < "$f" > "out/${name}.txt"
  echo "done: $f"
done
```

We tested this script's loop and file saving with a fake `claude` command, including a file name with a space in it. Try the real model calls with your own account.

Line by line:

- `set -euo pipefail`: a safety switch that stops the script if something goes wrong.
- `find ... -print0 | ... read -r -d ''`: handles file names safely, even ones with spaces.
- `--bare`: skips the automatic loading of hooks, MCP, notes, and so on, so every run has the same conditions. (A few things, like the `env` section of settings files, still apply.) Instead of your subscription login, it needs the `ANTHROPIC_API_KEY` environment variable to use the Anthropic API. (Other providers use their own credentials.)
- `--allowedTools "Read"`: lets it use the read tool without asking. No other tools are allowed. To remove tools entirely, use `--tools`.
- `--max-turns 3`: limits it to at most 3 rounds of work per file (one-line mode only).

## Getting results a program can read

If another program needs to read the results, get them as JSON.

```bash
claude --bare -p "List the claims in this text that need checking" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"claims":{"type":"array","items":{"type":"string"}}},"required":["claims"]}' \
  | jq '.structured_output'
```

With `--json-schema`, the result's `structured_output` field follows the shape you set. But it might not be filled in, for example if the model declined the request. The official docs say to check that the field exists before using it. If you need a cost cap, there's also `--max-budget-usd` (one-line mode only). It's checked against Claude Code's own cost estimate.

## Three safety rules for automation

1. **Allow narrowly.** If it only needs to read, give it only `Read`. If it needs to write, decide which folder.
2. **Set caps.** Use `--max-turns` and `--max-budget-usd` to stop runaway jobs. (The cost cap uses an estimate, so it may not stop at exactly that amount.)
3. **Don't read unfamiliar folders.** In someone else's repository, start with `--bare` or turn hooks off (see the safety pages in 17.1 and 17.2).

Also, choose the input folder so no files with passwords or personal details get mixed in. Whatever you send goes to the AI service.

!!! tip "In 10-year-old words"
    Put a one-line command in a loop, and you've got a conveyor belt. For safety: allow narrowly, set caps, and stay out of strange folders.

!!! note "★ Going deeper"
    For automatic checks on a server (CI), the official docs' main example uses `--permission-mode dontAsk` with an exact `--allowedTools` list. In one-line mode, you can also put `/skill-name` in the prompt, and Claude Code expands that skill before running. But `--bare` doesn't find skills automatically. Load a plugin separately with `--plugin-dir`, and note that the plugin's hooks don't run under `--bare`.

## Try it yourself

1. Make two Markdown files in a practice `docs-en` folder.
2. Save the loop script above to a file, and first check only its syntax with `bash -n script.sh`.
3. If `ANTHROPIC_API_KEY` is set, run it for real and read the results in the `out/` folder. If you don't have a key, you can try it without `--bare`. Just remember that your own settings and hooks will load then.

## Use it today

- If you run the same check on ten or more files, turn it into a loop.
- Put the original path in each result file's name, so it's easy to find later.
- Before running, make sure the input folder has no secret files.

## Common mix-ups

- "Automation means no person is needed." Reading the results and making decisions is still your job. Automation makes things for you to read.
- "One-line mode works just like chat mode." Permissions, trust checks, and what loads at startup are all different. Reread the pages in 16.4 and 17.1.

## Sources and date checked

- **Version checked:** Claude Code 2.1.319, checked on 2026-11-09. We ran the script's loop with a fake `claude` command. We didn't check results from real model calls.
- The practice file is in the repository at `examples/claude-code/check-hard-words-en.sh` (Korean edition: `check-hard-words.sh`). The README there says how it was checked.
- **Source of facts:** [Official docs: Run Claude Code programmatically](https://code.claude.com/docs/en/headless), [CLI reference](https://code.claude.com/docs/en/cli-reference), and [Choose a permission mode](https://code.claude.com/docs/en/permission-modes). Read on 2026-11-09.
- **Learning order:** [claude-howto 10-cli](https://github.com/luongnv89/claude-howto/tree/main/10-cli) (MIT; rewritten in our own words).
