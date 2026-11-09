# Chat, search, image, voice: the kinds of AI

<p class="ep-meta"><span>Ch. 4 · 4.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - You can sort the tools called "AI" by ==what goes in and what comes out==.
    - Text chatbots, search chatbots, image and voice tools, and coding helpers are each good at different jobs.
    - Knowing the kinds makes it easier to pick the right tool, and to know what to doubt when it slips.

## A toolbox

A hammer, a screwdriver, and a tape measure are all "tools," but they do different jobs. You wouldn't use a screwdriver on a nail.

"AI" is one name for many tools that do different things. Look at what you put in (the input) and what comes out (the output), and it gets easier to tell them apart.

!!! tip "In 10-year-old words"
    AI is a toolbox. Look at what goes in and what comes out, and you can tell which tool it is.

## Sorting the kinds

| Kind | What goes in → what comes out | Good for | Watch out for |
|---|---|---|---|
| Text chatbot | Text → text | Writing, explaining, ideas, translating | Hallucination, missing recent news |
| Chatbot with search | Question → an answer from web results, with sources | Recent news, questions where facts need checking | It can sum up sources wrong |
| Image maker | Text (or a photo) → picture | Illustrations, mock-ups, idea sketches | Hands or lettering can look odd; copyright |
| Voice | Speech → speech | Asking and listening out loud, interpreting, transcribing | Hearing words wrong; privacy |
| Coding helper | A description or code → code | Writing programs, finding bugs | You must run the code to check it |
| Agent | A goal → it carries out several steps on its own | Handing off multi-step jobs | Small mistakes can pile up (Part IV) |

This table is a rough way to sort things, to help you understand. These days, one service often offers several of these kinds together.

## Coming together

Karpathy's intro talk on large language models describes where they are heading. They handle more than text, like images and sound, and they use tools, like web browsing and a calculator. That's why you can now upload a photo, ask about it, get an answer from a web search, and get a table back, all in one chatbot.

But the same service can offer different features depending on your plan and the date. Check for yourself what the service you use can do right now.

!!! note "★ Going deeper"
    - A model that handles text, images, and sound together is called **multimodal**. One way it works: images get cut into pieces like tokens and read alongside the text. Once you learn about tokens and embeddings in Part III, this gets easier to follow.
    - Many image makers don't work by picking the next word. A common method starts from noise and cleans it up step by step until a picture appears. Researchers are also building models that make text and images together. This book focuses on text chatbots.

## Try it yourself

Write down 5 things you asked an AI to do in the past week. Then, for each one, decide which kind from the table you used.

- Did you ask for something that needed a search, using a chatbot with no search?
- Did you leave something that had to be exact to a chatbot alone?

## Use it today

1. **Ask about recent events with a tool that can search.** A regular chatbot may not know what happened after it was trained.
2. **Treat AI pictures as drafts, and check any text or numbers in them yourself.** Lettering inside images is easy to get wrong.
3. **Always run code before you trust it.** Code from a coding helper can be wrong too.
4. **Read the feature list of the service you use, once.** There may be features you've never tried because you didn't know about them.
5. **Don't try to do everything with one tool.** Pick the right tool for each job.

## Common mix-ups

- "AI is all the same AI." Each kind is good at different things, and goes wrong in different ways.
- "If it has search, it's always right." Search helps, but it can still sum up what it found the wrong way.
- "Image AI guesses the next word, like a text chatbot." Different tools make things in different ways.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Andrej Karpathy, [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g), YouTube, 2023-11-23. Chapters "Tool Use (Browser, Calculator, Interpreter, DALL-E)" (00:27:43) and "Multimodality (Vision, Audio)" (00:33:32), checked through Rosetta's unofficial, auto-generated [chapter list and transcript](https://rosetta.to/u/andrejkarpathy/1hr-talk-intro-to-large-language-models). We could not watch the video ourselves.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The table of kinds is our own. We left out product names and feature lists because they change fast. The note on how image makers work is a general overview without a specific source.
