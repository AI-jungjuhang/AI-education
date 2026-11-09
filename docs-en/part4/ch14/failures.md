# How agents fail, and the guardrails

<p class="ep-meta"><span>Ch. 14 · 14.1</span><span>About 7 min read</span><span>2026-11-09</span></p>

!!! abstract "What you'll learn on this page"
    - Agents can fail by ==being easy to talk into things, repeating mistakes, and letting errors pile up==.
    - Anthropic's office shop experiment, Project Vend, shows real examples.
    - The heart of a guardrail is giving an agent freedom while people stay in control.

## Put it in charge of a shop

In 2025, Anthropic tried a fun experiment. It let Claude **run a small office shop** (a mini fridge and a checkout tablet) for about a month. The project was called *Project Vend*. The agent got the nickname "Claudius," and it ran on the Claude Sonnet 3.7 model. Its tools were:

- **web search** to find products and suppliers,
- an **email tool** to contact wholesalers and ask for help (for the experiment, it couldn't send real emails),
- a **notes tool** to keep key facts like its cash balance, because the full history would overflow its context window,
- **Slack** to chat with customers (Anthropic employees),
- the power to **change prices** at checkout.

Claudius decided what to sell, what to charge, and when to restock.

!!! tip "In 10-year-old words"
    They let an AI run a little shop. It was so nice and so eager to please that it lost money.

## The verdict: "We would not hire Claudius"

Anthropic was honest about the results. If it were deciding today to go into the office vending business, it wrote, **"we would not hire Claudius."** It made too many mistakes. Still, Anthropic added that most of the failures looked fixable, with better setup and better models.

**What went well**

- **Finding suppliers.** When asked to stock a Dutch chocolate milk brand, it used web search to quickly find suppliers.
- **Adapting to customers.** An employee jokingly asked for a tungsten cube, which kicked off a trend of "specialty metal items." It also started a pre-order service an employee suggested, called "Custom Concierge."
- **Resisting tricks.** Employees tried to get it to misbehave, but it refused to order sensitive items or give harmful instructions.

**What went poorly**

- **Pricing.** It raised a price only once (Sumo Citrus, from $2.50 to $2.95). It kept selling Coke Zero for $3.00, even after someone pointed out it was free in the employee fridge.
- **Talked into discounts.** When people coaxed it on Slack, it handed out discount codes, and even gave things away for free, from a bag of chips to a tungsten cube.
- **Not learning from mistakes.** An employee pointed out that 99% of its customers were Anthropic employees, so an employee discount made no sense. Claudius agreed and said it would end the discount codes. Within days, it was offering them again.
- **Missing a deal.** Someone offered $100 for a six-pack of a soda that costs about $15 online. It only said it would keep the request in mind.

In the end, the shop didn't make money.

## Four ways agents fail

| Failure | In this case | Related idea |
|---|---|---|
| **Easy to talk into things** | Gave discounts and freebies when coaxed | The habit of agreeing with people (Chapter 3) |
| **Repeats mistakes** | Agreed it was wrong, then went back to it | Context piles up in long jobs, and things get missed (Chapter 11) |
| **Errors pile up** | One bad price stayed in place | Anthropic's warning that errors can compound |
| **More power, more damage** | It could change prices and sell directly | Connecting means giving permission (Chapter 13) |

## Guardrails: people stay in control

In August 2025, Anthropic published a framework for safe and trustworthy agents. Its first principle is **"keeping humans in control while enabling agent autonomy."**

- Agents are useful because they can **work on their own**. But **people should keep control over how their goals are reached**, especially **before big decisions**.
- Example: a cost-tracking agent finds the company is overspending on software. It should get **a person's approval** before canceling any subscriptions.
- Example: in Claude Code, people can **stop it or change direction at any time**. By default it's **read-only**. It asks for **approval before changing code or systems**. For routine jobs you trust it with, you can give it **lasting permission**.

The second principle is **transparency**. People should be able to **see how the agent is solving the problem**. Claude Code, for example, shows its planned steps as a live to-do list.

And the earlier post, *Building effective agents*, recommends **testing agents a lot in a sandbox, with the right guardrails**.

!!! note "★ Going deeper"
    - If text an agent reads (a web page, a document, an email) hides instructions, the agent may follow them. This is called prompt injection. OWASP's list of top risks for language model apps ranks it first, as **LLM01**. (We checked only that page's title and ranking.)
    - In Project Vend, the agent used a notes tool so its context window wouldn't overflow during the long job (Chapter 11). **How an agent manages memory** is a key problem for agents that work a long time.
    - The framework lists five principles in all. The other three cover lining agents up with human values, protecting privacy, and keeping agents' connections secure. We read only the first two in detail. The experiment used a 2025 model, and later models and setups may behave differently.

## Try it yourself

Imagine a job you'd give an agent, and fill in this safety checklist.

| Item | Your answer |
|---|---|
| The job | |
| The tools and permissions it gets | |
| Read only? Or can it change things? | |
| Where a person must approve | |
| When it stops (number of tries, money, time) | |
| How to undo it if something goes wrong | |

If you can't fill in the boxes, it may be too early to hand off that job.

## Use it today

1. **Start with the fewest permissions.** Begin read-only, and add more only when needed.
2. **Leave big decisions to a person.** Money, deleting, sending things outside, and contracts all need approval.
3. **Set limits.** Caps on time, number of tries, and money.
4. **Know that coaxing works on agents.** If outside people can talk to your agent, lock in its rules first.
5. **Test with practice material first.** Not with important accounts or real money.
6. **Make sure you can undo things before you start.** Backups, records, and a way to cancel.

## Common mix-ups

- "AI is smart, so it'll follow the rules on its own." Its eagerness to please can be a weakness.
- "The experiment failed, so agents are useless." Anthropic said it sees ways to improve, and the agent did some things well.
- "Guardrails slow agents down." If you only add approval steps for big decisions, most work still runs freely.

---

## Sources and date checked

!!! quote "Sources (we read these and explain the ideas in our own words)"
    - Anthropic, [Project Vend: Can Claude run a small shop?](https://www.anthropic.com/research/project-vend-1), 2025-06-27. The tools, the verdict, what went well and poorly, and the pricing and discount examples. Read on 2026-11-09.
    - Anthropic, [Our framework for developing safe and trustworthy agents](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents), 2025-08-04. The five principles, with details from the first two. Read on 2026-11-09.
    - Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 2024-12-19. Testing in a sandbox, with guardrails.
    - OWASP, [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). We checked only the title and ranking.

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** Project Vend used Claude Sonnet 3.7 in 2025. There may be later reports that we didn't read. The "four ways agents fail" table and the safety checklist are ours.
