# Glossary

<p class="ep-meta"><span>Appendix</span><span>For looking things up</span><span>2026-11-09</span></p>

Words from this book, in A to Z order. Each meaning is a plain version of how this book explains it. The page on the right has the full story. ★ marks deeper topics.

| Word | Plain meaning | In this book |
|---|---|---|
| Agent | An AI that picks its own steps, uses tools, looks at results, and keeps working | [Ch. 14 What is an agent?](../part4/ch14/what-agent.md) |
| Alignment | Getting AI to act the way people really want | [Ch. 20 Alignment](../part6/ch20/alignment.md) |
| Attention | The part that lets each token decide "where should I look?" and pull in that information | [Ch. 11 Attention](../part3/ch11/attention-idea.md) |
| Autoregressive generation ★ | Picking one token, adding it to the input, and picking the next, over and over | [Ch. 1 Next word](../part1/ch01/next-word.md), [Ch. 12 Long answers](../part3/ch12/long-answer.md) |
| Benchmark | A shared test for comparing AI models with the same questions | [Ch. 21 Benchmark traps](../part6/ch21/benchmarks.md) |
| Benchmark leakage (contamination) ★ | Test questions slipping into the training data, which inflates scores | [Ch. 21 Benchmark traps](../part6/ch21/benchmarks.md) |
| Chain of thought | Having the model write out in-between steps before it answers | [Ch. 20 Reasoning models](../part6/ch20/rl-reasoning.md) |
| Circuit ★ | A path where features link up to do one calculation | [Ch. 19 Circuits](../part6/ch19/circuits.md) |
| CLAUDE.md | A file of notes and rules that Claude Code reads at the start of every chat | [Ch. 16 CLAUDE.md](../part5/ch16/claudemd-intro.md) |
| Compaction | Swapping a long chat for a summary so work can go on | [Ch. 23 Saving memory space](../part6/ch23/context-habits.md) |
| Constitutional AI, RLAIF ★ | AI judging AI using a list of principles people wrote, so it learns from that | [Ch. 20 Alignment](../part6/ch20/alignment.md) |
| Context rot ★ | Accuracy and recall dropping as the input gets longer | [Ch. 11 Context window](../part3/ch11/context-window.md) |
| Context window | How much text a chatbot can see at once, counted in tokens. The chatbot's desk | [Ch. 11 Context window](../part3/ch11/context-window.md), [Ch. 23 What fills it](../part6/ch23/context-fill.md) |
| Effort level | The dial for how long Claude thinks before it answers | [Ch. 23 Effort level](../part6/ch23/model-effort.md) |
| Embedding | Turning a token into a list of numbers (a point on a map) | [Ch. 10 Tokens to numbers](../part3/ch10/tokens-to-vectors.md) |
| Emergent abilities ★ | Abilities said to appear in big models but not small ones. Some argue it's a side effect of how they're measured | [Ch. 20 Scaling](../part6/ch20/scaling.md) |
| Feature ★ | A pattern inside a model that tends to light up together and matches an idea people understand | [Ch. 19 Features](../part6/ch19/features.md) |
| Few-shot ★ | Showing a few examples so the AI copies the shape you want | [Ch. 2 Role, format, examples](../part1/ch02/role-format.md) |
| Fine-tuning | Training a pretrained model further, for example on answers people wrote | [Ch. 9 Learning from people](../part3/ch09/tuning.md) |
| Gradient descent ★ | Learning by nudging the numbers inside a model a little, based on how wrong it was | [Ch. 9 Pretraining](../part3/ch09/pretraining.md) |
| Hallucination | Making up something that sounds right and saying it with confidence | [Ch. 1 Hallucination](../part1/ch01/hallucination.md), [Ch. 21 Measuring it](../part6/ch21/eval-hallu.md) |
| Head (attention head) ★ | One of several attention processes running side by side | [Ch. 11 Attention](../part3/ch11/attention-idea.md) |
| Held-out test ★ | Test questions you don't look at while fixing, saved for the final check | [Ch. 15 Evaluate](../part4/ch15/evaluate.md) |
| Hook | A script Claude Code runs automatically at set moments, like after every file edit | [Ch. 17 Hook basics](../part5/ch17/hook-basics.md) |
| Interpretability ★ | Research that tries to look inside a model, like a microscope | [Ch. 19 Why look inside?](../part6/ch19/interp-intro.md) |
| Jailbreak | Trying to get an AI to break the rules it was given | [Ch. 14 Failures and safeguards](../part4/ch14/failures.md) |
| Logits ★ | The raw scores, before they're turned into chances | [Ch. 12 Temperature](../part3/ch12/temperature.md) |
| Masking | Stopping later tokens from affecting earlier ones | [Ch. 11 Attention](../part3/ch11/attention-idea.md) |
| MCP (Model Context Protocol) | A shared standard for connecting AI to outside tools and data | [Ch. 13 MCP](../part4/ch13/connectors.md), [Ch. 17 MCP](../part5/ch17/mcp-intro.md) |
| Multimodal ★ | Handling images and sound, not just text | [Ch. 4 Kinds of AI](../part1/ch04/kinds.md) |
| Parameters | The numbers (dials) inside a model that change as it learns. The "70B" in a model's name is how many | [Ch. 9 Parameters](../part3/ch09/scale.md) |
| Plugin | A folder that bundles skills, helpers, hooks, and MCP so you can install and share them | [Ch. 18 Plugins](../part5/ch18/plugin-bundle.md) |
| Pretraining | The first stage, where a model learns by guessing the next token across huge amounts of text | [Ch. 9 Pretraining](../part3/ch09/pretraining.md) |
| Prompt | What you give an AI: your question and instructions | [Ch. 2 Give context](../part1/ch02/context.md) |
| Prompt injection ★ | Hidden instructions in pasted or fetched text that the chatbot ends up following | [Ch. 2 Templates](../part1/ch02/templates.md), [Ch. 14 Failures and safeguards](../part4/ch14/failures.md) |
| RAG (retrieval-augmented generation) | Finding related text first and having the AI answer while looking at it | [Ch. 13 Search](../part4/ch13/search-rag.md) |
| Reasoning model | A model trained to think for longer before answering | [Ch. 20 Reasoning models](../part6/ch20/rl-reasoning.md) |
| Reinforcement learning | Teaching by rewarding good actions so they happen more | [Ch. 9 Learning from people](../part3/ch09/tuning.md), [Ch. 20 Reasoning models](../part6/ch20/rl-reasoning.md) |
| RLHF ★ | Reinforcement learning from human feedback | [Ch. 9 Learning from people](../part3/ch09/tuning.md) |
| Sampling | How the next token is picked from the score sheet | [Ch. 12 Sampling](../part3/ch12/sampling.md) |
| Sandbox | A walled-off test space where mistakes can't cause harm outside | [Ch. 13 Running code](../part4/ch13/files-code.md), [Ch. 14 Failures and safeguards](../part4/ch14/failures.md) |
| Scaling laws | Findings that models improve in a steady pattern as model size, data, and computing grow | [Ch. 9 Parameters](../part3/ch09/scale.md), [Ch. 20 Scaling](../part6/ch20/scaling.md) |
| Score sheet | The chance given to each possible next word, for how well it fits | [Ch. 1 Next word](../part1/ch01/next-word.md) |
| Skill | A folder of instructions Claude loads when a matching job comes up | [Ch. 17 Skill anatomy](../part5/ch17/skill-anatomy.md) |
| Softmax | The math that turns scores into chances that add up to 1 | [Ch. 11 Attention](../part3/ch11/attention-idea.md), [Ch. 12 Temperature](../part3/ch12/temperature.md) |
| Subagent | A helper with its own context window that Claude can hand a job to | [Ch. 17 Subagents](../part5/ch17/subagent-intro.md) |
| Sycophancy | Giving answers that match what the user thinks rather than the facts | [Ch. 3 Second opinion](../part1/ch03/second-opinion.md) |
| Temperature | How much picking from the score sheet favors the top choices | [Ch. 12 Temperature](../part3/ch12/temperature.md) |
| Token | A piece of text the chatbot reads. Not always a letter or a word | [Ch. 1 Tokens](../part1/ch01/tokens.md) |
| Transformer | A model design where attention blocks and MLP blocks take turns, many times over | [Ch. 11 One transformer layer](../part3/ch11/transformer-layer.md) |
| Vector | Several numbers grouped in one row. The point that stands for a token's meaning | [Ch. 10 Tokens to numbers](../part3/ch10/tokens-to-vectors.md) |
| Workflow | An AI job where the order of steps is set in advance | [Ch. 14 What is an agent?](../part4/ch14/what-agent.md) |

---

## Sources and date checked

The meanings here come from this book's pages. The sources for each meaning are on the page linked on the right, under "Sources and date checked."

- **Date checked:** 2026-11-09
- **Status:** First draft
- **Note:** These plain meanings are short versions of this book's explanations, so they may not match technical definitions exactly. When new pages are added, this table needs updating. Compared with the Korean edition, we added a few Claude Code terms (CLAUDE.md, compaction, effort level, hook, plugin, skill, subagent).
