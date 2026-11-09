# Why size matters: parameters

<p class="ep-meta"><span>Ch. 9 · 9.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - **Parameters** are the numbers inside a model that get adjusted during training. A number like "70B" in a model's name is how many there are.
    - Research found that growing the model, the data, and the computing power improves results by a steady rule.
    - But ==size alone doesn't decide things==. The amount of data and the way a model is tuned matter too.

## The knobs on a radio

Old radios had knobs to tune the station and the sound. With two or three knobs, you can't adjust much. With hundreds of billions of knobs, you could tune things very finely.

A chatbot has knobs like these, called **parameters**: billions to hundreds of billions of them. Training means turning each knob a tiny bit (page 9.1.1). In model names like "7B" or "70B," the B usually stands for billion, the number of parameters. 175B means 175 billion.

!!! tip "In 10-year-old words"
    Parameters are knobs the model turns while it learns. More knobs let it tune things more finely, but having lots of knobs doesn't make it good all by itself.

## Bigger gets better: scaling laws

In 2020, a paper by Jared Kaplan and others, *Scaling Laws for Neural Language Models*, found a pattern. A language model's error score drops in a steady way, following what's called a **power law**, as you grow three things: the model's size, the amount of data, and the computing power used for training. Some of these trends held across a range of more than ten million times. Details of the design, like how wide or deep the network was, mattered little within a wide range.

Put simply: add more resources, and the score table improves by a rule you can predict. That's why companies kept investing in bigger models.

## But it's not just size

**Data has to grow too.** In 2022, a paper by Jordan Hoffmann and others argued that for a fixed amount of computing, it's most efficient to grow the model and the training data **at the same rate**. If you double the model, double the training tokens too. They concluded that big models of the time had grown without enough extra data, so they were **undertrained**. To test this, they built **Chinchilla**, with 70 billion parameters and four times as much data, using the same computing budget as a bigger model. Chinchilla beat much larger models across many tests, including Gopher (280 billion), GPT-3 (175 billion), and Megatron-Turing NLG (530 billion).

**How you tune it matters too.** The InstructGPT model on the last page was 100 times smaller, and people still preferred it.

!!! warning "Please note"
    These studies are from 2020 and 2022, and AI has changed a lot since. Today, steps after training, the way models reason, and tool use all add a lot to how well they do. Don't read this as "size is everything." Read it as "size is one important factor."

## What comes with being big

- **It's heavy.** More parameters need more memory and more computer power to run. As a rough example, if each parameter takes 2 bytes, 175 billion parameters take about 350 GB just for the numbers (175 × 10⁹ × 2 bytes). That's why big models usually run on a company's servers, not on a home computer.
- **It's slow and costly.** Each question needs more computing (see free vs paid in Chapter 4).
- **For some jobs, a smaller model is better.** For simple jobs, a small, fast model is often enough.

!!! note "★ Going deeper"
    - The 2020 scaling laws paper concluded that, for a fixed budget, it's efficient to train a very large model on a fairly modest amount of data and stop early. The Chinchilla paper corrected that: grow the model and the data together. This is research fixing earlier research, the way science moves forward.
    - Chinchilla reported an average accuracy of 67.5% on a test called MMLU, the best at the time. Chapter 21 covers what tests like this mean and where they fall short.
    - Researchers also work on helping small models catch up to big ones (for example, "distillation"), and on designs that use only part of the model for each input ("mixture of experts"). This book doesn't cover those.
    - Using more computing for "thinking time" is covered in Chapter 20.

## Try it yourself

Practice reading the numbers in model names.

1. How many is 175B? (175 billion)
2. How many times bigger is 175B than 70B? (2.5 times)
3. If each parameter takes 2 bytes, about how much space do a 70B model's numbers need? (70 × 10⁹ × 2 = 140 × 10⁹ bytes, about 140 GB)

Then look on your service's help pages to see which model it uses. Does the name tell you its size? (Often it doesn't.)

## Use it today

1. **Don't assume a bigger model is always better.** Look at how hard the job is, and at speed and cost too.
2. **Use a fast model for easy jobs and a big one for hard jobs.** If your service lets you choose.
3. **Don't read the number in a model's name as a quality score.** Parameter count is size, not quality.
4. **Be careful with old comparison articles.** Model rankings change within months.
5. **Big models get things wrong too.** Size doesn't make hallucinations go away.

## Common mix-ups

- "More parameters means smarter." Data, training methods, and tuning all play a part.
- "The number of parameters is the amount of knowledge." It doesn't map that neatly. Parameters are knobs, not drawers.
- "Make it bigger and hallucinations will disappear." Size alone doesn't fix that (Chapter 1).

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Jared Kaplan and others, [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), arXiv, 2020-01-23. Power laws, trends over more than seven orders of magnitude, and the small effect of width and depth come from the abstract.
    - Jordan Hoffmann and others, [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556), arXiv, 2022-03-29. Scaling model and tokens equally, Chinchilla (70B, 4 times the data) beating Gopher, GPT-3, Jurassic-1, and Megatron-Turing NLG, and 67.5% on MMLU come from the abstract.
    - Long Ouyang and others, [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155), arXiv, 2022-03-04.
    - Tom B. Brown and others, [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), arXiv, 2020-05-28.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** We read only the abstracts. These are older studies, so they may not apply directly to today's models. The 350 GB and 140 GB figures are our own rough math for storing the numbers only. Running a model takes more. "B" for billion in model names is a common habit, not a rule.
