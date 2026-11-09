# Get a second opinion

<p class="ep-meta"><span>Ch. 3 · 3.1</span><span>About 5 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - For answers that matter, don't trust a single try. Get a ==second opinion==.
    - You can ask again, have it check its own answer, ask for the other side, or check somewhere else.
    - Two answers can agree and both be wrong. So the bigger the job, the more checking you do.

## Seeing a second doctor

When a doctor tells someone they have a serious illness, many people see a second doctor. The news is too important to rest on one person's word.

The same goes for chatbot answers. The more it matters, the more a second opinion helps. As Chapter 1 showed, a chatbot draws its answer from a score table, so the same question can get different answers. Where the answers differ is a clue.

!!! tip "In 10-year-old words"
    For anything important, check one more time, the way you'd see a second doctor. The bigger the deal, the more you check.

## Ways to get a second opinion

**1. Ask the same question again.** Ask the same question two or three times, each in a new chat, and compare. If the answers disagree on something, be extra careful about that part. Anthropic's guide calls this "best-of-N" checking. It says answers that don't match could be a sign of hallucination.

**2. Have it check an answer.** Paste the earlier answer back in and ask the chatbot to check it. The guide says that using an answer as the input for a follow-up question can catch things that don't add up.

```text
In the answer below, find any facts that are wrong or weakly supported,
and list them. Mark anything you're not sure about as "needs checking."
<answer>
(paste the earlier answer)
</answer>
```

**3. Ask for the other side.** Try "Give me the three strongest arguments against this claim." It helps you notice an answer that leans one way.

**4. Check somewhere else.** Ask a different chatbot, search the web, read official pages or a book, or ask an expert.

## Match the checking to the size of the job

| How big is the job? | How to check |
|---|---|
| Small (ideas, polishing tone) | Read it once and use it |
| Medium (work emails, report drafts) | Ask again, and check a few key facts |
| Important (money, contracts, schoolwork you hand in) | Check the original sources and a second source |
| Serious (health, law, safety) | Always check with an expert in that field |

!!! note "★ Going deeper"
    - **Two answers can agree and both be wrong.** Different chatbots may have learned from similar text, so they can be wrong in the same way. Getting the same answer several times doesn't make it right. Mix in a different kind of evidence, like the original source or an official page.
    - **Telling you what you want to hear.** In 2023, Anthropic researchers (Mrinank Sharma and others) tested five AI assistants trained with human feedback. All five tended to shape their answers to match what the user seemed to believe, instead of what was true. This is called **sycophancy**. The researchers found that people rating answers often preferred ones that agreed with them, which may be part of the cause. So if you ask "I'm right, aren't I?", it may just agree.

## Try it yourself

Try this with a chatbot.

```text
1. (A claim you believe) is true, right? Tell me I'm right.
```

```text
2. Give me 3 reasons (the same claim) is true and 3 reasons it might not be.
   At the end, tell me which side is more convincing, and why.
```

Compare the two answers. Did it agree with you easily in the first one? What changed in the second?

## Use it today

1. **Instead of "I'm right, aren't I?", ask for reasons on both sides.** That kind of question makes it less likely to just agree.
2. **For answers that matter, ask again in a new chat.** A fresh chat gives you a more independent second opinion than asking again in the same chat.
3. **Check only the parts that disagree.** Don't try to check everything. Start where the answers differ.
4. **Decide the size of the job first.** If you set your checking level ahead of time, like in the table above, you won't wear yourself out.
5. **For serious matters, check with a person.** For health, law, and safety, use the chatbot's answer only as a starting point.

## Common mix-ups

- "Another chatbot said the same thing, so it's right." They can be wrong the same way. Check the original or an official source too.
- "If I tell it to check itself, it'll catch everything." It helps, but it's not perfect. Use it to find the spots a person should check.
- "Asking several times costs too much." Do it only for things that matter. Step up your checking as the job gets bigger.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations), Claude Platform Docs. "Best-of-N verification" and "Iterative refinement." Read on 2026-11-09.
    - Mrinank Sharma and others, [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548), arXiv, 2023-10-20 (revised 2025-05-10). Also on Anthropic's site: [Towards understanding sycophancy in language models](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models), 2023-10-23. We summarized the abstract.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** "Different chatbots can be wrong the same way" is a common understanding. We did not find one source that tests it directly. The table of job sizes is our own.
