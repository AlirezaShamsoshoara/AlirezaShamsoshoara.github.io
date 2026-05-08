---
title: "Daily AI Papers — May 09, 2026"
date: 2026-05-09
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-09/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - mathematical-reasoning
  - agentic-systems
  - llm-training
---

## 1. AI Co-Mathematician: Accelerating Mathematicians with Agentic AI

**Authors:** Daniel Zheng, Ingrid von Glehn, Yori Zwols, Iuliya Beloshapka, Lars Buesing, Daniel M. Roy, Martin Wattenberg, Bogdan Georgiev, Tatiana Schmidt, Andrew Cowie, Fernanda Viegas, Dimitri Kanevsky (Google DeepMind)

**Summary:** Google DeepMind introduces an interactive AI workbench where mathematicians can leverage AI agents to pursue open-ended research — covering ideation, literature synthesis, and proof exploration. The system achieves a new high score on the FrontierMath benchmark, signaling a step change in AI-assisted mathematical discovery.

**arXiv:** [arxiv.org/abs/2605.06651](https://arxiv.org/abs/2605.06651)

**Sources:** HuggingFace Daily Papers, officechai.com, Nature.com, YouTube (JX6nCEsuBDw)

**Why trending:** High-profile Google DeepMind release with benchmark-breaking results on FrontierMath; earned media coverage in Nature and general AI press, plus a dedicated YouTube explainer.

---

## 2. EMO: Pretraining Mixture of Experts for Emergent Modularity

**Authors:** Ryan Wang, Akshita Bhagia, Sewon Min (Allen Institute for AI)

**Summary:** EMO shows that by pretraining with a Mixture-of-Experts objective that encourages emergent specialization, you can obtain a model whose expert subsets serve as standalone narrow specialists (code, math, domain knowledge) without losing general capability. This challenges the assumption that MoE routing only saves compute — it can also yield modular, deployable sub-models.

**arXiv:** [arxiv.org/abs/2605.06663](https://arxiv.org/abs/2605.06663)

**Sources:** HuggingFace Daily Papers, HuggingFace Blog (AllenAI), Emergent Mind

**Why trending:** AllenAI published an accompanying blog post on HuggingFace, and the modular LLM angle resonates strongly with practitioners seeking efficient deployment.

---

## 3. Prescriptive Scaling Laws for Data Constrained Training

**Authors:** Justin Lovelace, Christian Belardi, Srivatsa Kundurthy, Shriya Sudhakar, Kilian Q. Weinberger

**Summary:** The classical Chinchilla scaling law assumes unlimited unique training tokens, but data is now the bottleneck. This paper derives new prescriptive scaling laws that tell practitioners exactly how to allocate compute when tokens are scarce — including when and how much to repeat data — going beyond descriptive observation to actionable guidance.

**arXiv:** [arxiv.org/abs/2605.01640](https://arxiv.org/abs/2605.01640)

**Sources:** HuggingFace Daily Papers, mbrenndoerfer.com blog

**Why trending:** Directly addresses the "data wall" problem every serious LLM training team faces; prescriptive (not just descriptive) framing makes it immediately actionable.

---

## 4. TIDE: Every Layer Knows the Token Beneath the Context

**Authors:** Ajay Jaiswal, Lauren Hannah, Han-Byul Kim, Duc Hoang, Mehrdad Farajtabar, Minsik Cho

**Summary:** TIDE challenges the universal design choice of injecting token identity only once at the input embedding layer. By re-injecting token positional identity at every Transformer layer, it mitigates the "Rare Token Problem" (where Zipf-distributed rare tokens lose identity through depth) and improves long-context understanding without architectural overhaul.

**arXiv:** [arxiv.org/abs/2605.06216](https://arxiv.org/abs/2605.06216)

**Sources:** HuggingFace Daily Papers, Emergent Mind

**Why trending:** Simple architectural tweak with broad applicability; directly addresses a known failure mode in all current LLMs.

---

## 5. Balanced Aggregation: Understanding and Fixing Aggregation Bias in GRPO

**Authors:** Zhiyuan Zeng, Jiameng Huang, Zhangyue Yin, Jiashuo Liu, Ziniu Li, Bingrui Li, Yuhao Wu, Yining Zheng, Ge Zhang, Wenhao Huang, Xipeng Qiu

**Summary:** GRPO-style RL training for LLM reasoning is widely adopted, but this paper identifies a previously overlooked aggregation bias in how group rewards are computed — biasing gradients and hurting training stability. The fix (Balanced Aggregation) is lightweight and significantly improves final reasoning performance.

**arXiv:** [arxiv.org/abs/2605.04077](https://arxiv.org/abs/2605.04077)

**Sources:** HuggingFace Daily Papers

**Why trending:** GRPO is the de facto RL fine-tuning method for reasoning models; a bug-fix paper with strong results attracts immediate practitioner attention.

---

## 6. Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling

**Authors:** Yuan Wang, Ouxiang Li, Yulong Xu, Borui Liao, Jiajun Liang, Jinghan Li, Meng Wang, Xintao Wang, Pengfei Wang, Kuien Liu, Xiang Wang

**Summary:** Current video reward models conflate reasoning and scoring, leading to noisy, inaccurate reward signals for generative video training. This paper decouples reasoning (understanding video quality dimensions) from scoring (emitting a reward signal), yielding sharper reward estimates that significantly improve post-training and test-time scaling for video generation.

**arXiv:** [arxiv.org/abs/2605.05922](https://arxiv.org/abs/2605.05922)

**Sources:** HuggingFace Daily Papers

**Why trending:** Video generation post-training is a hot frontier; cleaner reward models directly translate to better Sora/Wan-class models.

---

## 7. Verifier-Backed Hard Problem Generation for Mathematical Reasoning

**Authors:** Yuhang Lai, Jiazhan Feng, Yee Whye Teh, Ning Miao

**Summary:** LLMs are good at solving math problems but poor at generating new, genuinely hard, valid problems — a bottleneck for autonomous AI-driven curriculum generation. This paper uses formal verifiers as a backbone to guarantee problem validity while a generative model steers toward difficulty, enabling reliable hard problem synthesis at scale.

**arXiv:** [arxiv.org/abs/2605.06660](https://arxiv.org/abs/2605.06660)

**Sources:** arXiv cs.AI, Papers With Code

**Why trending:** Directly addresses the data flywheel problem for math reasoning models; combines symbolic verification with neural generation in a principled way.

---

## 8. Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients

**Authors:** Mingwei Xu, Hao Fang

**Summary:** Standard RLVR training for LLMs requires both positive and negative rollout examples, but negative samples are expensive and often uninformative. This paper shows that an implicit negative gradient signal can be derived purely from positive rollouts, enabling more sample-efficient policy optimization with comparable or better reasoning performance.

**arXiv:** [arxiv.org/abs/2605.06650](https://arxiv.org/abs/2605.06650)

**Sources:** arXiv cs.LG

**Why trending:** Sample efficiency in RL fine-tuning is a key pain point; removing the need for negative rollouts simplifies training pipelines.

---

## 9. The Granularity Axis: A Micro-to-Macro Latent Direction for Social Roles in Language Models

**Authors:** Chonghan Qin, Xiachong Feng, Ziyun Song, Xiaocheng Feng, Jing Xiong, Lingpeng Kong

**Summary:** LLMs are routinely prompted to adopt social roles from individual personas to institutional voices, yet it is unclear whether their internal representations encode this "granularity" dimension. This paper identifies a linear micro-to-macro latent direction in LLM activations and shows it can be steered to improve role-consistent generation.

**arXiv:** [arxiv.org/abs/2605.06196](https://arxiv.org/abs/2605.06196)

**Sources:** HuggingFace Daily Papers

**Why trending:** Mechanistic interpretability of role-playing behavior is directly relevant to persona-based AI systems and alignment research.

---

## 10. Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents

**Authors:** Hailey Onweller, Elias Lumer, Austin Huber, Pia Ramchandani, Vamse Kumar Subbiah, Corey Feld

**Summary:** Deep research agents like Gemini Deep Research and Perplexity cite hundreds of sources, but those citations are often inaccurate or unverifiable. This paper introduces a systematic framework to parse, trace, and evaluate source attribution fidelity in LLM research agents, revealing alarming rates of miscitation.

**arXiv:** [arxiv.org/abs/2605.06635](https://arxiv.org/abs/2605.06635)

**Sources:** arXiv cs.CL

**Why trending:** Hallucinated citations in research agents are a serious trust and liability issue; this is the first systematic evaluation framework for the problem.

---

## 11. Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less

**Authors:** Yuxing Liu, Jianyu Wang, Tong Zhang

**Summary:** A surprising empirical finding: when fine-tuning LLMs with the same optimizer used during pretraining (rather than a default like AdamW), catastrophic forgetting is substantially reduced. The paper provides theoretical grounding for this "optimizer-model consistency" principle and shows it generalizes across architectures and tasks.

**arXiv:** [arxiv.org/abs/2605.06654](https://arxiv.org/abs/2605.06654)

**Sources:** arXiv cs.LG

**Why trending:** Immediately actionable insight for anyone running full fine-tuning pipelines; challenges the default of always using AdamW for finetuning.

---

## 12. The Structural Origin of Attention Sink: Variance Discrepancy, Super Neurons, and Dimension Disparity

**Authors:** Siquan Li, Kaiqi Jiang, Jiacheng Sun, Tianyang Hu

**Summary:** The attention sink phenomenon — where initial tokens monopolize attention scores — is well-documented but mechanistically unexplained. This paper traces it to three structural causes: variance discrepancy across layers, "super neuron" activations, and dimension disparity in key/query projections, opening principled paths to mitigation.

**arXiv:** [arxiv.org/abs/2605.06611](https://arxiv.org/abs/2605.06611)

**Sources:** arXiv cs.LG

**Why trending:** Mechanistic understanding of attention sinks is prerequisite for fixing them; affects long-context performance in every transformer-based LLM.

---

## 13. MASPO: Joint Prompt Optimization for LLM-based Multi-Agent Systems

**Authors:** Zhexuan Wang, Xuebo Liu, Li Wang, Zifei Shan, Yutong Wang, Zhenxi Song, Min Zhang

**Summary:** In LLM multi-agent systems, each agent has a role-specific prompt, but these prompts are typically tuned independently, ignoring cross-agent interactions. MASPO jointly optimizes all agent prompts by modeling the MAS as a cooperative game, significantly improving collaborative task performance over per-agent baselines.

**arXiv:** [arxiv.org/abs/2605.06623](https://arxiv.org/abs/2605.06623)

**Sources:** arXiv cs.AI

**Why trending:** Multi-agent systems are rapidly proliferating; joint prompt optimization is an underexplored but high-leverage lever for MAS performance.

---

## 14. Crafting Reversible SFT Behaviors in Large Language Models

**Authors:** Yuping Lin, Pengfei He, Yue Xing, Yingqian Cui, Jiayuan Ding, Subhabrata Mukherjee, Hui Liu, Zhen Xiang

**Summary:** Supervised fine-tuning imprints behaviors into LLMs without any built-in mechanism to reverse them — a problem for alignment and model updates. This paper proposes a training method that deliberately structures new SFT behaviors into a reversible subnetwork, enabling clean removal without degrading other capabilities.

**arXiv:** [arxiv.org/abs/2605.06632](https://arxiv.org/abs/2605.06632)

**Sources:** arXiv cs.CL

**Why trending:** Model editing and alignment rollback are increasingly important as models are deployed and need behavioral updates post-deployment.

---

## 15. The Scaling Properties of Implicit Deductive Reasoning in Transformers

**Authors:** Enrico Vompa, Tanel Tammet

**Summary:** Using Horn clause theorem proving as a controlled testbed, this paper systematically studies how implicit deductive reasoning scales with Transformer depth, width, and training data. It finds that depth is the primary driver of reasoning depth, providing clean scaling laws for deductive capability.

**arXiv:** [arxiv.org/abs/2605.04330](https://arxiv.org/abs/2605.04330)

**Sources:** HuggingFace Daily Papers

**Why trending:** Clean empirical scaling laws for reasoning (not just loss) are rare; the controlled Horn clause setting makes results highly interpretable.

---

## 16. STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?

**Authors:** Hanxiang Chao, Yihan Bai, Rui Sheng, Tianle Li, Yushi Sun

**Summary:** LLM agents with persistent memory stores face a critical failure mode: implicit conflicts where new observations contradict stored beliefs without explicit signaling. STALE introduces a benchmark and methodology for evaluating whether agents can detect and revise stale memories, revealing major gaps in current systems.

**arXiv:** [arxiv.org/abs/2605.06527](https://arxiv.org/abs/2605.06527)

**Sources:** arXiv cs.AI

**Why trending:** Long-term memory staleness is a critical unsolved problem for deployed personal AI agents; the benchmark fills a gap left by static fact-retrieval evaluations.

---

## 17. LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG

**Authors:** Yijia Zheng, Marcel Worring

**Summary:** Multi-step agentic RAG is powerful but slow due to repeated LLM calls for planning and retrieval. LatentRAG moves reasoning into a latent space, enabling joint reasoning and retrieval in a single forward pass, drastically reducing latency while matching or exceeding multi-step accuracy.

**arXiv:** [arxiv.org/abs/2605.06285](https://arxiv.org/abs/2605.06285)

**Sources:** arXiv cs.IR

**Why trending:** Efficiency of agentic RAG is a major production concern; single-pass latent reasoning is an elegant departure from the dominant multi-step paradigm.

---

## 18. TACT: Mitigating Overthinking and Overacting in Coding Agents via Activation Steering

**Authors:** Yuan Sui, Yulin Chen, Yibo Li, Xue Jiang, Yufei He, Yihong Dong, Xiaoxin He, Tianyu Gao, Bryan Hooi

**Summary:** Coding agents degrade over long trajectories through "agent drift" — either overthinking (redundant reasoning) or overacting (issuing unnecessary tool calls). TACT uses activation steering to suppress these failure modes at inference time, improving SWE-bench performance without any additional fine-tuning.

**arXiv:** [arxiv.org/abs/2605.05980](https://arxiv.org/abs/2605.05980)

**Sources:** arXiv cs.SE

**Why trending:** Coding agents are among the highest-value deployments of LLMs; activation steering as an inference-time fix (no retraining) is immediately applicable.

---

## 19. MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval

**Authors:** Chunyu Li, Jingyi Kang, Ding Chen, Mengyuan Zhang, Jiajun Shen, Bo Tang, Xuanhe Zhou, Feiyu Xiong, Zhiyu Li

**Summary:** Standard rerankers in agent memory systems rely on semantic similarity, which fails when relevant memories require multi-hop reasoning to connect to the query. MemReranker introduces a reasoning-aware reranker that explicitly reasons over candidate memories before scoring, substantially improving long-term agent performance on complex tasks.

**arXiv:** [arxiv.org/abs/2605.06132](https://arxiv.org/abs/2605.06132)

**Sources:** arXiv cs.AI

**Why trending:** Agent memory retrieval is a critical bottleneck for long-horizon tasks; reasoning-aware reranking is a natural but previously underexplored direction.

---

## 20. GeoStack: A Framework for Quasi-Abelian Knowledge Composition in VLMs

**Authors:** Pranav Mantini, Shishir K. Shah

**Summary:** Vision-Language Models suffer from catastrophic forgetting when accumulating expertise across domains. GeoStack introduces a modular geometric framework that treats independently trained domain experts as composable building blocks — using quasi-Abelian structure to guarantee interference-free combination without full retraining.

**arXiv:** [arxiv.org/abs/2605.06477](https://arxiv.org/abs/2605.06477)

**Sources:** HuggingFace Daily Papers

**Why trending:** Continual learning and modular composition for VLMs is a persistent challenge; the geometric formulation provides a theoretically grounded approach to a practical problem.
