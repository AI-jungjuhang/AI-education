# Review log

<p class="ep-meta"><span>Appendix</span><span>About 4 min read</span><span>2026-11-09</span></p>

This page records how we checked the English edition, what we changed along the way, and what we still haven't checked. It's here so you can judge how much to trust each part.

## How each page was checked

The English edition isn't a translation of the Korean one. We wrote each page fresh from the English sources, in this order:

1. **Open the sources again.** We reopened the links (papers, docs, posts, and transcripts) on 2026-11-09, not trusting the Korean edition's notes.
2. **Write the page.** We used our own words and kept quotes to a minimum.
3. **Check the words.** We used three standards. The book's owner agreed to them.
    - **Plain words:** a checklist from the US government's plain language guide. It asks for short sentences, common words, and so on.
    - **Reading grade:** a Flesch-Kincaid grade of **6.0 or lower** for each page's main text, measured with `tools/readability.py`. Tables, code, sources, and "★ Going deeper" boxes aren't counted.
    - **Fewer AI tells:** the `humanizer` skill (no em dashes, no stock phrases, no forced groups of three).
4. **Build the site** with `mkdocs build --strict` and check the exit code. (We don't use `-q`, because it hid a broken link once.)
5. **Check the layout** at five screen widths with the `design-check` script, then look at screenshots by eye.

## What changed from the Korean edition, and why

Rechecking the sources turned up these differences:

- **Chapter 17, skills:** the Korean page's step list included a "next episode preview." That goes against this channel's own video rules, so we left it out.
- **Chapter 17, MCP:** we added a note from the current docs. Some secret key settings, like `ANTHROPIC_API_KEY`, come out blank when used in a remote server's address.
- **Chapter 18, background tasks:** we added two facts. Repeating `/loop` tasks end after 7 days. Cloud schedules can't run more than once an hour.
- **We left out two claims** we couldn't find in the current docs. One was a version number for a `/doctor` check. The other was about which skill loads in `-p` mode.
- **Chapter 22, Hassabis:** the Korean page used only his phone interview from October 2024. For the English page, we also read his December 2024 interview. In it, he names his two worries about AI: misuse, and keeping control.
- **Chapter 23, models:** we added the `best` alias. We also noted that `ultrathink` can raise one turn to `xhigh`. Both are in the current docs.
- **Chapter 23, hands-on:** we wrote an English hook script, `examples/claude-code/check-build-en.sh`. We tested it on a small practice site, and it worked as expected.
- **Appendix:** we added Claude Code words to the glossary and three Chapter 23 prompts to the prompt collection. The reading order also has a new Claude Code path.

## Pages we couldn't open directly

- **NobelPrize.org** returned "403 Forbidden" to our page-reading tool. Fetching it with a normal browser header worked, and we read the speech and transcripts that way.
- **YouTube** blocked our setup. See the References page for how we handled videos.

## Not checked yet

- **What the model really does** in the Part V hands-on pages. For example, we didn't install the plugin, run the super skill, or watch a Stop hook send Claude back. We checked the files and scripts only.
- **Karpathy's talks.** We only had unofficial transcripts, not the real captions.
- **Exact post dates** for Sam Altman's blog, which the pages don't show.
- **Papers beyond their abstracts.** For most papers we read only the abstract.

---

## Sources and date checked

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** This log covers the English edition only. The Korean edition has its own review log. For each fact, the page that uses it lists its sources.
