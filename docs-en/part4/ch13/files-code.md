# AI that reads files and runs code

<p class="ep-meta"><span>Ch. 13 · 13.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Chatbots can read files, and some can ==write code, run it, and bring back the results==.
    - For things that must be exact, like math, tables, and charts, code is more reliable than the chatbot just talking.
    - But watch for personal details in files, hidden instructions, and wrong code.

## A student with a calculator and pencil

Try big multiplication on a test with no calculator or pencil, and mistakes come easily. With a calculator and pencil, you get it right. The student didn't suddenly get smarter. **They got to use tools.**

As Chapter 7 showed, chatbots can slip on long math. But if they **write code and have a computer run it**, the math comes out exact. That's what a code execution tool does.

!!! tip "In 10-year-old words"
    When a chatbot gets a calculator and pencil (running code), its math and tables get much more accurate. But you still need to check what it calculated.

## How it works

It's the same kind of tool use as on the last page. According to Anthropic's tool use docs, when the chatbot wants a tool, it sends back **a structured request to call it**, and either your app or Anthropic runs it. Anthropic's **code execution tool** runs Python and Bash code in a **sandboxed container** to analyze data and make files. Roughly, it goes like this:

1. You ask: "Add up the monthly sales in this file and make a chart."
2. The chatbot **writes code** that does the job.
3. The code **runs**, and results come out (numbers, a chart).
4. The chatbot reads the results and **explains** them to you.

So the math is done by the computer, not by the chatbot "talking." Anthropic's docs also list a **web fetch tool** that pulls in the full content of web pages and PDFs.

## What happens when you upload a file

- The file gets **turned into text** the chatbot can read (a PDF may also be handled as page images), and goes into the context (Chapter 6). Tables and charts can get scrambled along the way.
- If the file is long, it may only be able to **read part of it**, because of the context limit (Chapter 11).
- Allowed file types and sizes differ by service.

## Jobs where running code helps

| Job | Why |
|---|---|
| Totals, averages, percentages | Code does math exactly |
| Cleaning tables, removing duplicates, changing formats | These follow clear rules |
| Making charts | Code can draw pictures |
| Handling lots of files at once | Code is good at repeating things |

## What to watch for

- **See which code ran.** If the formula is wrong, an exact value is still a wrong answer (Chapter 7). Ask "Show me the code you ran."
- **Check files for personal details.** Uploaded files are sent to the service (Chapter 3).
- **Files can hide instructions.** A document someone sent you might hide a line like "Ignore your earlier instructions," and the chatbot might follow it (prompt injection, Chapter 2).
- **Keep the original separately.** Don't let a converted file replace your original.
- **Check a few lines of the result yourself.** For a table, work out a few rows by hand.

!!! note "★ Going deeper"
    - A **sandbox** is a walled-off space, set up so the code can't touch your own computer. But some tools run code directly on your computer, like a terminal tool. Those have much more power, and much more risk. Chapter 14 on agents comes back to this.
    - A tool call may not happen just once. It's common to look at the result, fix the code, and run it again (Chapter 14).
    - The step-by-step flow above is a general description. Each service builds it differently.

## Try it yourself

If your service lets you upload files and run code:

1. Make a small table (5 to 10 rows). Columns for name, date, and amount work well. Use fake names.
2. Upload it and say:

```text
Add up the amounts by month and show me a table.
Also show me the code you used, so I can see what you calculated.
```

3. Compare the result with your own math. Read which columns the code used, and how.

If your service can't run code, you can do the same thing by asking for a spreadsheet formula (Chapter 7).

## Use it today

1. **For exact math, ask it to run code.** Some services understand "Use code to calculate this."
2. **Ask to see the code it ran.** Even if you can't read code, you can usually spot the column names and conditions.
3. **Remove personal details before uploading.** Once you upload a file, it's been sent.
4. **Upload a copy, not your original.** That protects it from accidental changes.
5. **Check part of the result by hand.** About three rows is enough.

## Common mix-ups

- "If code did the math, it must be right." The math is exact, but if the formula is wrong, so is the answer.
- "It read my file, so it understands all of it." With long or complicated files, it can miss parts.
- "Running code is dangerous, so I shouldn't use it." Tools that run code in a sandbox are fairly safe. Tools with lots of power over your computer are the risky ones.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), Claude Platform Docs. Structured tool calls run by your app or by Anthropic, the code execution tool (Python and Bash in a sandboxed container), and the web fetch tool. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** How file conversion works differs by service, so that part is general. We didn't read the code execution tool's own page in full. The calculator-and-pencil comparison is ours.
