# 참고 자료 목록

<p class="ep-meta"><span>부록</span><span>2026-11-07 기준</span></p>

이 책의 모든 페이지는 맨 아래 "출처와 기준"에 참고한 자료를 적었어요. 이 페이지는 그 링크를 **자동으로 모은 목록**이에요. 오른쪽 칸은 그 자료를 쓴 페이지예요.

!!! warning "이해관계와 한계를 알려 드려요"
    - **이 책의 초안은 AI(Claude)의 도움으로 쓰였어요.** 그 AI는 Anthropic이 만들었고, 이 책은 **Anthropic의 문서와 연구 글을 여러 번 인용해요.** 특히 질문 요령, 환각, 해석 가능성, 에이전트 이야기에서 그래요. 독자는 이 점을 알고 읽어야 하고, Anthropic이 **아닌** 출처로도 확인해 보시길 권해요.
    - **확인 수준이 자료마다 달라요.** 논문은 대부분 **초록만** 읽었고, 블로그 글과 에세이는 **일부 또는 전문**을 읽었어요. 각 페이지의 "출처와 기준"에 어디까지 읽었는지 적었어요.
    - **영상은 YouTube 자막을 직접 가져올 수 없었어요.** 이 작업 환경의 접속을 YouTube가 막아서(봇 확인 요구) 영상을 직접 볼 수 없었어요. Karpathy 영상 세 편은 제3자 사이트 Rosetta가 자막에서 자동 생성한 **비공식 자막과 챕터**로만 일부 대조했고(오류 가능), 나머지 영상(3Blue1Brown 등)은 제목만 확인하거나 같은 내용의 텍스트판을 읽었어요.
    - **한국 공식 안내서(개인정보보호위원회, 문화체육관광부·한국저작권위원회)는 공식 원문을 열지 못하고 보도로만 확인했어요.**
    - **번역은 의역이에요.** 영어 원문과 대조가 필요해요. 문장은 옮기지 않고 이해한 대로 다시 썼어요.
    - **시간이 지나면 낡아요.** 모델 이름, 수치, 기능, 요금은 열람한 날(2026-11-07) 기준이에요.

<!-- AUTO:refs -->
### 논문 (arXiv, DOI) (35개)

| 자료 | 이 책에서 쓴 페이지 |
|---|---|
| [Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004) | [스케일링: 크게 만들면 좋아질까](../part6/ch20/scaling.md) |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | [어텐션: 중요한 곳을 골라 본다](../part3/ch11/attention-idea.md), [트랜스포머 한 층의 모양](../part3/ch11/transformer-layer.md) |
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) | [강화학습과 추론 모델](../part6/ch20/rl-reasoning.md) |
| [Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference](https://arxiv.org/abs/2403.04132) | [벤치마크의 함정](../part6/ch21/benchmarks.md) |
| [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) | [정렬: 사람의 뜻에 맞추기](../part6/ch20/alignment.md) |
| [Deep contextualized word representations](https://arxiv.org/abs/1802.05365) | [문맥에 따라 뜻이 달라진다](../part3/ch10/context-meaning.md) |
| [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | [강화학습과 추론 모델](../part6/ch20/rl-reasoning.md) |
| [Don't Make Your LLM an Evaluation Benchmark Cheater](https://arxiv.org/abs/2311.01964) | [벤치마크의 함정](../part6/ch21/benchmarks.md) |
| [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) | [비슷한 뜻은 가까이 있다](../part3/ch10/closeness.md), [토큰이 숫자 묶음이 된다](../part3/ch10/tokens-to-vectors.md) |
| [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682) | [스케일링: 크게 만들면 좋아질까](../part6/ch20/scaling.md) |
| [Evaluating and Mitigating Discrimination in Language Model Decisions](https://arxiv.org/abs/2312.03689) | [편향과 한계 알아보기](../part1/ch03/bias.md) |
| [Experimental evidence on the productivity effects of generative artificial intelligence](https://doi.org/10.1126/science.adh2586) | [초안 만들기](../part2/ch05/first-draft.md) |
| [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) | [환각은 어떻게 재나](../part6/ch21/eval-hallu.md) |
| [Faith and Fate: Limits of Transformers on Compositionality](https://arxiv.org/abs/2305.18654) | [계산을 맡길 때 조심할 것](../part2/ch07/math-caution.md) |
| [Fine-Tuning Language Models from Human Preferences](https://arxiv.org/abs/1909.08593) | [사람에게 배우기: 미세조정과 피드백](../part3/ch09/tuning.md) |
| [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) | [벤치마크의 함정](../part6/ch21/benchmarks.md) |
| [International AI Safety Report](https://arxiv.org/abs/2501.17805) | [안전과 위험을 보는 눈](../part6/ch21/risks.md) |
| [Language Model Tokenizers Introduce Unfairness Between Languages](https://arxiv.org/abs/2305.15425) | [글자를 '토큰'이라는 조각으로 쪼개 읽는다](../part1/ch01/tokens.md), [편향과 한계 알아보기](../part1/ch03/bias.md) |
| [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | [읽고 따라 하기: 사전학습](../part3/ch09/pretraining.md), [크기가 왜 중요할까: 파라미터](../part3/ch09/scale.md) |
| [Lateral Reading: Reading Less and Learning More When Evaluating Digital Information](https://doi.org/10.2139/ssrn.3048994) | [출처 확인하는 법](../part1/ch03/check-sources.md) |
| [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | [요약하기](../part2/ch05/summarize.md), [긴 자료 읽고 정리하기](../part2/ch06/long-docs.md), [컨텍스트 창: 한 번에 보는 범위](../part3/ch11/context-window.md) |
| [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520) | [편향과 한계 알아보기](../part1/ch03/bias.md), [비슷한 뜻은 가까이 있다](../part3/ch10/closeness.md) |
| [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) | [벤치마크의 함정](../part6/ch21/benchmarks.md) |
| [Measuring short-form factuality in large language models](https://arxiv.org/abs/2411.04368) | [환각은 어떻게 재나](../part6/ch21/eval-hallu.md) |
| [Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality](https://doi.org/10.2139/ssrn.4573321) | [일에 적용하기 전 체크리스트](../part2/ch08/rollout-check.md) |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | [검색을 붙이면 달라지는 것](../part4/ch13/search-rag.md) |
| [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | [크기가 왜 중요할까: 파라미터](../part3/ch09/scale.md), [스케일링: 크게 만들면 좋아질까](../part6/ch20/scaling.md) |
| [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) | [강화학습과 추론 모델](../part6/ch20/rl-reasoning.md) |
| [Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention](https://doi.org/10.1111/j.1467-9280.2006.01693.x) | [공부 도우미로 쓰기](../part2/ch06/tutor.md) |
| [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751) | [샘플링: 뽑는 방법](../part3/ch12/sampling.md) |
| [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) | [편향과 한계 알아보기](../part1/ch03/bias.md), [두 번째 의견 구하기](../part1/ch03/second-opinion.md), [사람에게 배우기: 미세조정과 피드백](../part3/ch09/tuning.md) |
| [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | [크기가 왜 중요할까: 파라미터](../part3/ch09/scale.md), [스케일링: 크게 만들면 좋아질까](../part6/ch20/scaling.md) |
| [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) | [크기가 왜 중요할까: 파라미터](../part3/ch09/scale.md), [사람에게 배우기: 미세조정과 피드백](../part3/ch09/tuning.md), [정렬: 사람의 뜻에 맞추기](../part6/ch20/alignment.md) |
| [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958) | [환각은 어떻게 재나](../part6/ch21/eval-hallu.md) |
| [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664) | [그럴듯하지만 틀릴 수 있다: 환각](../part1/ch01/hallucination.md), [환각은 어떻게 재나](../part6/ch21/eval-hallu.md) |

### Anthropic 문서와 글 (16개)

| 자료 | 이 책에서 쓴 페이지 |
|---|---|
| [Building effective AI agents](https://www.anthropic.com/research/building-effective-agents) | [에이전트가 실패하는 모습과 안전장치](../part4/ch14/failures.md), [계획하고, 행동하고, 확인한다](../part4/ch14/loop.md), [에이전트란 무엇일까](../part4/ch14/what-agent.md), [평가하고 고치기](../part4/ch15/evaluate.md), [좋은 지시문 쓰기](../part4/ch15/instructions.md), [도구를 잘 설계하기](../part4/ch15/tool-design.md) |
| [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) | [내 일에 맞는 AI 고르기](../part1/ch04/choose.md), [무료와 유료는 뭐가 다를까](../part1/ch04/free-paid.md) |
| [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) | [맥락을 주면 답이 달라진다](../part1/ch02/context.md), [새 대화가 나을 때](../part1/ch02/fresh-start.md), [고쳐 달라고 말하는 법](../part1/ch02/iterate.md), [요약하기](../part2/ch05/summarize.md), [긴 자료 읽고 정리하기](../part2/ch06/long-docs.md), [컨텍스트 창: 한 번에 보는 범위](../part3/ch11/context-window.md) |
| [Define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) | [자주 쓰는 질문 모아 두기](../part2/ch08/prompt-library.md), [일에 적용하기 전 체크리스트](../part2/ch08/rollout-check.md), [평가하고 고치기](../part4/ch15/evaluate.md) |
| [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | [계획하고, 행동하고, 확인한다](../part4/ch14/loop.md) |
| [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude) | [특징: 모델 안의 개념들](../part6/ch19/features.md) |
| [Increase output consistency](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency) | [회의록과 메일 정리](../part2/ch07/meeting-notes.md), [표와 엑셀 함수 도움받기](../part2/ch07/tables.md) |
| [Introducing Claude for Education](https://www.anthropic.com/news/introducing-claude-for-education) | [공부 도우미로 쓰기](../part2/ch06/tutor.md) |
| [Mapping the Mind of a Large Language Model](https://www.anthropic.com/research/mapping-mind-language-model) | [특징: 모델 안의 개념들](../part6/ch19/features.md), [왜 모델 속을 봐야 할까](../part6/ch19/interp-intro.md) |
| [Our framework for safe and trustworthy agents](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents) | [에이전트가 실패하는 모습과 안전장치](../part4/ch14/failures.md), [정렬: 사람의 뜻에 맞추기](../part6/ch20/alignment.md) |
| [Project Vend: Can Claude run a small shop?](https://www.anthropic.com/research/project-vend-1) | [에이전트가 실패하는 모습과 안전장치](../part4/ch14/failures.md), [좋은 지시문 쓰기](../part4/ch15/instructions.md) |
| [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | [맥락을 주면 답이 달라진다](../part1/ch02/context.md), [고쳐 달라고 말하는 법](../part1/ch02/iterate.md), [역할, 형식, 예시를 정해 준다](../part1/ch02/role-format.md), [구체적으로 쓰되 한 번에 하나씩](../part1/ch02/specific.md), [나만의 질문 틀 만들기](../part1/ch02/templates.md), [초안 만들기](../part2/ch05/first-draft.md), [고쳐 쓰기와 말투 바꾸기](../part2/ch05/rewrite.md), [요약하기](../part2/ch05/summarize.md), [긴 자료 읽고 정리하기](../part2/ch06/long-docs.md), [낯선 분야 빠르게 파악하기](../part2/ch06/quick-intro.md), [회의록과 메일 정리](../part2/ch07/meeting-notes.md), [좋은 지시문 쓰기](../part4/ch15/instructions.md) |
| [Reduce hallucinations](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) | [그럴듯하지만 틀릴 수 있다: 환각](../part1/ch01/hallucination.md), [숫자와 인용 대조하기](../part1/ch03/check-numbers.md), [출처 확인하는 법](../part1/ch03/check-sources.md), [두 번째 의견 구하기](../part1/ch03/second-opinion.md), [낯선 분야 빠르게 파악하기](../part2/ch06/quick-intro.md) |
| [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) | [파일을 읽고 코드를 실행하는 AI](../part4/ch13/files-code.md), [검색을 붙이면 달라지는 것](../part4/ch13/search-rag.md) |
| [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model) | [그럴듯하지만 틀릴 수 있다: 환각](../part1/ch01/hallucination.md), [긴 답이 이어지는 과정](../part3/ch12/long-answer.md), [회로: 생각의 길 따라가기](../part6/ch19/circuits.md), [왜 모델 속을 봐야 할까](../part6/ch19/interp-intro.md), [정렬: 사람의 뜻에 맞추기](../part6/ch20/alignment.md), [강화학습과 추론 모델](../part6/ch20/rl-reasoning.md) |
| [Writing effective tools for AI agents](https://www.anthropic.com/research/writing-tools-for-agents) | [평가하고 고치기](../part4/ch15/evaluate.md), [도구를 잘 설계하기](../part4/ch15/tool-design.md) |

### 영상과 강의 (6개)

| 자료 | 이 책에서 쓴 페이지 |
|---|---|
| [Attention in transformers, step-by-step (Deep Learning 6장)](https://www.3blue1brown.com/lessons/attention) | [어텐션: 중요한 곳을 골라 본다](../part3/ch11/attention-idea.md), [컨텍스트 창: 한 번에 보는 범위](../part3/ch11/context-window.md) |
| [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) | [그럴듯하지만 틀릴 수 있다: 환각](../part1/ch01/hallucination.md), [챗봇은 '다음 말'을 맞히는 기계](../part1/ch01/next-word.md), [글자를 '토큰'이라는 조각으로 쪼개 읽는다](../part1/ch01/tokens.md), [읽고 따라 하기: 사전학습](../part3/ch09/pretraining.md), [강화학습과 추론 모델](../part6/ch20/rl-reasoning.md), [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |
| [How might LLMs store facts (Deep Learning 7장)](https://www.3blue1brown.com/lessons/mlp) | [트랜스포머 한 층의 모양](../part3/ch11/transformer-layer.md) |
| [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |
| [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | [글자를 '토큰'이라는 조각으로 쪼개 읽는다](../part1/ch01/tokens.md), [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |
| [Transformers, the tech behind LLMs (Deep Learning 5장)](https://www.3blue1brown.com/lessons/gpt) | [챗봇은 '다음 말'을 맞히는 기계](../part1/ch01/next-word.md), [글자를 '토큰'이라는 조각으로 쪼개 읽는다](../part1/ch01/tokens.md), [읽고 따라 하기: 사전학습](../part3/ch09/pretraining.md), [비슷한 뜻은 가까이 있다](../part3/ch10/closeness.md), [문맥에 따라 뜻이 달라진다](../part3/ch10/context-meaning.md), [토큰이 숫자 묶음이 된다](../part3/ch10/tokens-to-vectors.md), [컨텍스트 창: 한 번에 보는 범위](../part3/ch11/context-window.md), [트랜스포머 한 층의 모양](../part3/ch11/transformer-layer.md), [긴 답이 이어지는 과정](../part3/ch12/long-answer.md), [샘플링: 뽑는 방법](../part3/ch12/sampling.md), [온도: 얼마나 모험할까](../part3/ch12/temperature.md) |

### 사람들이 직접 쓴 글과 공개 발언 (12개)

| 자료 | 이 책에서 쓴 페이지 |
|---|---|
| [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) | [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |
| [Banquet speech](https://www.nobelprize.org/prizes/physics/2024/hinton/speech/) | [Geoffrey Hinton의 시선](../part6/ch22/hinton.md) |
| [Deep Neural Nets: 33 years ago and 33 years from now](https://karpathy.github.io/2022/03/14/lecun1989/) | [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |
| [Interview](https://www.nobelprize.org/prizes/chemistry/2024/hassabis/interview/) | [Demis Hassabis의 시선](../part6/ch22/hassabis.md) |
| [Interview](https://www.nobelprize.org/prizes/physics/2024/hinton/interview/) | [Geoffrey Hinton의 시선](../part6/ch22/hinton.md) |
| [Machines of Loving Grace](https://darioamodei.com/essay/machines-of-loving-grace) | [Dario Amodei의 시선](../part6/ch22/amodei.md) |
| [Reflections](https://blog.samaltman.com/reflections) | [Sam Altman의 시선](../part6/ch22/altman.md) |
| [Statement on AI Extinction Risk](https://safe.ai/work/statement-on-ai-risk) | [Dario Amodei의 시선](../part6/ch22/amodei.md), [Demis Hassabis의 시선](../part6/ch22/hassabis.md), [Geoffrey Hinton의 시선](../part6/ch22/hinton.md), [입장 비교: 어디서 갈릴까](../part6/ch22/views-compare.md) |
| [The Gentle Singularity](https://blog.samaltman.com/the-gentle-singularity) | [Sam Altman의 시선](../part6/ch22/altman.md) |
| [The Urgency of Interpretability](https://darioamodei.com/post/the-urgency-of-interpretability) | [Dario Amodei의 시선](../part6/ch22/amodei.md) |
| [Three Observations](https://blog.samaltman.com/three-observations) | [Sam Altman의 시선](../part6/ch22/altman.md) |
| [블로그 목록](https://karpathy.github.io/) | [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |

### 표준과 가이드 (3개)

| 자료 | 이 책에서 쓴 페이지 |
|---|---|
| [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | [팀에서 정하는 규칙](../part2/ch08/team-rules.md), [안전과 위험을 보는 눈](../part6/ch21/risks.md) |
| [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) | [에이전트가 실패하는 모습과 안전장치](../part4/ch14/failures.md) |
| [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) | [도구를 연결하는 표준: MCP](../part4/ch13/connectors.md) |

### 보도와 기타 (7개)

| 자료 | 이 책에서 쓴 페이지 |
|---|---|
| [Deep Dive](https://rosetta.to/u/andrejkarpathy/deep-dive-into-llms-like-chatgpt) | [그럴듯하지만 틀릴 수 있다: 환각](../part1/ch01/hallucination.md), [챗봇은 '다음 말'을 맞히는 기계](../part1/ch01/next-word.md), [글자를 '토큰'이라는 조각으로 쪼개 읽는다](../part1/ch01/tokens.md), [읽고 따라 하기: 사전학습](../part3/ch09/pretraining.md), [강화학습과 추론 모델](../part6/ch20/rl-reasoning.md), [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |
| [보도 내용](https://www.heraldk.com/article/2025110215591135596) | [저작권과 표절](../part1/ch03/copyright.md) |
| [보도 내용](https://view.asiae.co.kr/article/2026022609294663830) | [저작권과 표절](../part1/ch03/copyright.md) |
| [보도 내용](https://v.daum.net/v/20250806130146966) | [개인정보와 민감한 자료](../part1/ch03/privacy.md), [팀에서 정하는 규칙](../part2/ch08/team-rules.md) |
| [여러 보도](https://community.openai.com/t/sam-altmans-a-new-blog-post-june-10-2025/1284906) | [Sam Altman의 시선](../part6/ch22/altman.md) |
| [자막·챕터](https://rosetta.to/u/andrejkarpathy/let-s-build-the-gpt-tokenizer) | [글자를 '토큰'이라는 조각으로 쪼개 읽는다](../part1/ch01/tokens.md), [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |
| [챕터 목록·자막](https://rosetta.to/u/andrejkarpathy/1hr-talk-intro-to-large-language-models) | [그럴듯하지만 틀릴 수 있다: 환각](../part1/ch01/hallucination.md), [챗봇은 '다음 말'을 맞히는 기계](../part1/ch01/next-word.md), [나만의 질문 틀 만들기](../part1/ch02/templates.md), [챗봇, 검색형, 이미지, 음성: 종류 나누기](../part1/ch04/kinds.md), [Andrej Karpathy의 시선](../part6/ch22/karpathy.md) |

<!-- /AUTO:refs -->

---

## 출처와 기준

- **기준 날짜:** 2026-11-07
- **검토 상태:** 초안. 위 목록은 `tools/collect_refs.py`로 모든 페이지의 출처 링크를 모아 만들었어요.
- **확인 필요:** 링크는 열람한 시점에 열렸어요. 링크가 깨졌는지 주기적으로 점검해야 해요. 자료별 확인 수준(초록/일부/전문)은 각 페이지에서 확인하세요.
