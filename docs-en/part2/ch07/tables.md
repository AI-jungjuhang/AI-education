# Help with tables and spreadsheet formulas

<p class="ep-meta"><span>Ch. 7 · 7.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - AI helps a lot with turning text into tables, explaining tables, and figuring out Excel or Google Sheets formulas.
    - When you ask about a formula, give ==the app, the column names, two or three example rows, and the result you want==.
    - Test any formula on a small set of data first, and check in the app's help that the function really exists.

## A recipe and ingredients

If you tell a cook "Make something tasty," that's hard. If you tell them what's in your fridge and what flavor you want, they can give you a recipe. Formula questions work the same way. Tell AI what your table has (the ingredients) and the result you want (the flavor), and it can give you a formula (the recipe).

!!! tip "In 10-year-old words"
    Don't just say "Give me a formula." Say "I have this kind of table, and I want this result."

## Text to table, table to text

**Text → table.** Turn scattered information into a table.

```text
From the text below, pull out each product name, price, and number
in stock, and make a table. If the text doesn't give a value, leave
the cell blank and write "none."
<text>(paste here)</text>
```

**Table → text.** Explain what a table shows in words. Make sure no numbers change.

## How to ask about a formula

A good question has four parts.

1. **The app.** Excel or Google Sheets? (Functions differ a little.)
2. **Column names.** What's in column A, column B, and so on.
3. **Two or three example rows.** What your real data looks like (with personal details hidden).
4. **The result you want.** Which cell, and what value should show up, with an example.

```text
I'm using Google Sheets.
Column A: Name, Column B: Department, Column C: Sales (a number)
Example row: Alex / Sales / 120
I want the total sales for the Sales department in cell E2.
Give me one formula, and explain what each part means, one line each.
```

Test the formula on a small set of data first. Anthropic's guide on consistent output says to spell out the exact format you want and to use examples to guide the result. When you show an example of the result you want, you're more likely to get the right answer.

## When the formula doesn't work

- Copy the exact error message and share it, like "#NAME?" or "#VALUE!".
- Share the values and the range in the cells the formula uses.
- Check in the app's help or official guide that the function **really exists**. AI can make up functions that don't exist (hallucination).
- Some functions only exist in some versions. Say which version you're using.

!!! note "★ Going deeper"
    - It usually works better to give **the column names and a few example rows** than to paste in a huge table. A long table takes up a lot of room in the context, and accuracy can drop (Chapters 2 and 6).
    - Some services let you upload a file, and the AI runs code to do the math itself (Part IV). Then the code does the math, but you still need to check which code ran on which columns.
    - For tables with personal details, blank them out using the methods from Chapter 3. Deleting the name column or swapping in fake data is enough for a formula question.

## Try it yourself

Pick a table you use (or make a 5-row practice table).

1. Decide what you want to work out. (A total, a count of rows that match something, an average, and so on.)
2. Ask using the four parts: app, column names, examples, and result.
3. Put the formula into your small table and check that it matches what you get by hand.

## Use it today

1. **Save a question template.** It has four slots: app, column names, example rows, and result.
2. **Swap personal details for fake data.** A formula question doesn't need real names.
3. **Check a few rows by hand.** About three rows is enough to catch a pattern of mistakes.
4. **Ask for an explanation of the formula too.** If you know what each part means, you can fix it yourself next time.
5. **If it fails, paste the error message as is.** That's the fastest way to a fix.

## Common mix-ups

- "Every function AI gives me exists." It can give you a function that doesn't exist, or one from a different app.
- "I have to paste the whole table for it to be accurate." Column names and a few example rows are often enough.
- "AI can do the math, so I don't need formulas." Formulas and tools are surer for math. The next page goes into this.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Increase output consistency](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency), Claude Platform Docs. "Specify the output format you want" and "Constrain with examples." Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The four parts of a formula question are our own tip. "AI can make up functions" follows from how hallucination works in general. We didn't find a study about spreadsheets specifically.
