# What is an agent?

<p class="ep-meta"><span>Ch. 14 · 14.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - An **agent** is ==an AI that decides how to do a job, uses tools, looks at the results, and keeps working==.
    - It differs from a **workflow**, which follows set steps, in who decides the steps.
    - Agents cost more and can pile up mistakes, so experts suggest using them only when you really need them.

## A recipe card and a chef

A recipe card lists the steps: "1. Chop the onion. 2. Fry it. 3. Add salt." If you follow the card, you don't have to think about the order. But picture a chef who's only told, "Make our guests a great dinner." The chef opens the fridge, sees what's there, and **decides on their own** what to make.

The first is a **workflow**. The second is an **agent**.

!!! tip "In 10-year-old words"
    A workflow is a robot following a recipe card. An agent is a chef who opens the fridge and decides what to cook.

## How Anthropic draws the line

In December 2024, Anthropic published a post called *Building effective agents*. It separates the two like this:

- **Workflows:** systems where language models and tools follow **paths set in code ahead of time**.
- **Agents:** systems where the language model **directs its own process and tool use**. The model is in charge of how the job gets done.

The post describes how an agent works. It starts from a person's request or a conversation. Once the job is clear, it **plans and acts on its own**. At each step, it checks **real feedback from its surroundings**, like the result of a tool call or of running code, to judge its progress. It can **pause at checkpoints, or when it's stuck, to ask a person**. It stops when the job is done, but it's also common to set **stopping conditions**, like a maximum number of steps. And the post adds: agents can handle complicated jobs, but how they're built is often simple. Usually it's just **a language model using tools in a loop, based on feedback from its surroundings**.

## When to use one, and when not to

The post's advice is surprisingly careful.

- **Find the simplest solution that works, and add complexity only when it helps.** Sometimes the answer is not to build an agent at all.
- Agent systems usually **trade speed and cost for better results**. Check whether that trade is worth it.
- Often, a single request improved with search and examples is enough.
- Agents fit **open-ended problems where you can't predict the number of steps or set a fixed path**. But they **cost more and can pile up mistakes**, so the post suggests testing them a lot in a sandbox, with guardrails.

!!! warning "Please note"
    The post carries a note saying the tools it describes have changed a lot since December 2024. Remember **the distinctions and principles**, more than specific tool names.

## Agents around us

The post's examples include **customer support agents**, which can look up orders and issue refunds, and **coding agents**, whose work can be checked with automatic tests. Tools like these read files, change code, run it, look at the results, and decide what to do next.

!!! note "★ Going deeper"
    - The post names three principles: **keep the agent's design simple**, **put transparency first** by showing the agent's planning steps, and **carefully build the connection between the agent and its tools** (the agent-computer interface) with good tool docs and testing.
    - You can think of an agent as the "one token at a time" loop from Chapter 12, wrapped in **one more loop on the outside**. Inside the writing loop, there's another loop of calling tools.
    - The post we read is from December 2024, and this field moves fast. For newer approaches, see Anthropic's later posts and docs.

## Try it yourself

Think of three jobs you recently gave an AI, and sort them.

| Job | Were the steps set? | Did it use tools? | Did it have to make its own decisions? |
|---|---|---|---|
| | | | |

- If the steps were set and no decisions were needed, a plain question or a workflow is enough.
- If you couldn't know the steps ahead of time and it needed tools several times, that's a job for an agent.

## Use it today

1. **Try the simplest way first.** An agent is too much for a job one question can handle.
2. **Hand off fixed-order jobs step by step.** That's "one thing at a time" from Chapter 2.
3. **Set a stopping point when you hand a job to an agent.** For example: "within 10 steps," or "do this much, then report back."
4. **Build in checkpoints.** The classic one: "Show me your plan first, and start once I approve."
5. **Test in a setting you're watching.** Use practice files, not important accounts or files.

## Common mix-ups

- "Agents are always better than plain chatbots." They cost more and risk more mistakes, so they're too much for simple jobs.
- "An agent is a totally new kind of AI." According to the post, it's a language model using tools in a loop.
- "An agent handles it, so I don't need to watch." Mistakes can pile up, so it needs checking.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 2024-12-19. Workflows versus agents, how agents work, when to use them, cost and piling-up mistakes, the three principles, the examples, and the note that tools have changed. Read on 2026-11-09.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** Because the post says its tools have changed, we left out specific tools. "One more loop around Chapter 12's loop" is our own comparison, and so is the chef.
