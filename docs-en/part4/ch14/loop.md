# Plan, act, check

<p class="ep-meta"><span>Ch. 14 · 14.1</span><span>About 6 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - An agent's basic shape is ==a loop: plan → act (use a tool) → check the result → decide what's next==.
    - There are a few common ways to build that loop: chains, routing, parallel work, a conductor with workers, and a writer with a reviewer.
    - Good loops include checkpoints where a person looks, and conditions for stopping.

## A scavenger hunt

Picture a scavenger hunt. You read a clue (plan), go to the spot (act), see whether you found the next clue (check), and head to wherever it points (decide what's next). The loop keeps going until you find the treasure.

That's how an agent works. As on the last page, it **repeats while watching the feedback from its surroundings**.

!!! tip "In 10-year-old words"
    An agent runs a scavenger hunt loop: read the clue, go look, check, and move on to the next clue.

## One trip around the loop

1. **Get the goal.** A person tells it the job.
2. **Plan.** Decide what to do.
3. **Act.** Use a tool, like search, reading a file, or running code (Chapter 13).
4. **Look at the result.** Read what the tool returned and judge the progress.
5. **Decide whether to keep going.** If there's more to do, go back to step 2. If it's done, stop.

Anthropic's post on agents names two common ways to stay in control. One is **pausing to ask a person**, at checkpoints or when it's stuck. The other is **stopping conditions**, like a maximum number of steps.

## Five ways to build the loop

The same post describes five **workflow patterns** that agents build on.

| Pattern | What it does | Everyday comparison |
|---|---|---|
| Prompt chaining | Splits a job into **set steps in order**, where each step takes the last one's result. Checks ("gates") can go in between | A relay race |
| Routing | **Sorts** the input and sends it to the right specialist | A hospital front desk |
| Parallelization | Runs parts **at the same time** (splitting the work), or runs the same job several times and **gathers different results** (voting) | Splitting a group project; solving a problem several ways and comparing |
| Orchestrator-workers | A central model **breaks the job down as it goes**, hands pieces to worker models, and combines the results | A director assigning crew on the spot |
| Evaluator-optimizer | One model writes, another **grades it and gives feedback**, and it improves round by round | Writing and then revising |

The post explains that **orchestrator-workers** looks like parallelization, but the difference is that **the smaller jobs aren't set ahead of time**. They depend on the input. In coding, for example, which files need changing, and how, differs every time. **Evaluator-optimizer** fits when there are clear standards for grading, and when another round of fixing really makes things better.

## What matters in a loop

- **Stopping conditions.** Decide when it's done, and set a maximum number of rounds. Without them, it may keep going.
- **Real feedback.** It has to actually read what happened. It must not carry on as if a failure were a success.
- **A person's checks.** At important points, it pauses for a person's approval.
- **A record.** Keep track of what it did, so you can look back later.

!!! note "★ Going deeper"
    - "Voting" in parallelization is the same idea as **asking the same question several times and comparing** from Chapter 3. You run the same job several times and pick the more trustworthy result.
    - In a separate post, *Effective context engineering for AI agents* (2025-09-29), Anthropic looks at how agents should manage their context during long jobs. (We checked only its title and date for this page.) The longer an agent works, the more its context window fills up (Chapter 11), so this problem grows.
    - The post on agents says again and again: add complexity only when it clearly improves results. Measuring and improving is the heart of it (Chapter 15).

## Try it yourself

Break an everyday job into a loop. For example, "plan a family day out this weekend."

```text
Goal: Plan a family day out this weekend that works even if it rains.
Go in this order, and show me each step when it's done.
1) Suggest 3 places.
2) When I pick one, look up travel time and cost.
3) When I say it's OK, make a schedule.
```

- At which points do you stop and check?
- If the agent had a search tool, which step would use it?

## Use it today

1. **Make "Show me the plan first" a habit.** You can check the direction before the loop starts.
2. **Set a pause after each step.** For example: "After each step, check with me before going on."
3. **Give a stopping condition.** "If it doesn't work after 5 tries, stop and tell me."
4. **Check the results yourself.** Even if the agent says "Done," look at what actually happened.
5. **Give it a standard to grade against.** "Check your work against these standards and fix it" is a tiny version of evaluator-optimizer.

## Common mix-ups

- "An agent makes the whole plan at once, then carries it out." It's a loop that changes the plan as results come in.
- "The more rounds, the better the result." More rounds cost more, and mistakes can pile up.
- "Several models working together is always better." The post suggests adding complexity only when simple methods fall short.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 2024-12-19. Checkpoints, stopping conditions, prompt chaining, routing, parallelization (splitting and voting), orchestrator-workers, and evaluator-optimizer. Read on 2026-11-09.
    - Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), 2025-09-29. We checked only the title and date.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** The everyday comparisons (relay race, front desk, and so on) and the four "what matters" points are ours. The post notes that its tools have changed since December 2024.
