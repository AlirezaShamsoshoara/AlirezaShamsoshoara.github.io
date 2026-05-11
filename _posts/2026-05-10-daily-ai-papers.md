---
title: "Daily AI Papers — May 10, 2026"
date: 2026-05-10
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-10/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - reinforcement-learning
  - multimodal
---

## 1. Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction

**Authors:** Zhuofeng Li, Haoxiang Zhang, Cong Wei et al.
**arxiv:** [arxiv.org/abs/2605.05242](https://arxiv.org/abs/2605.05242)
**Upvotes:** 75 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

Modern retrieval systems expose a corpus through a fixed similarity interface that compresses access into a single top-k retrieval step before reasoning. This abstraction is efficient, but for agentic search it becomes a bottleneck — exact lexical constraints, sparse clue conjunctions, local context checks, and multi-step hypothesis refinement are difficult to express through similarity alone. The authors introduce Direct Corpus Interaction (DCI), enabling agents to query raw text directly, outperforming traditional retrieval methods across agentic search benchmarks.

**Why trending:** Highest-upvoted paper of the day; tackles a fundamental limitation of RAG/semantic search for AI agents — highly relevant to the LLM agent ecosystem.

---

## 2. Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning

**Authors:** Yaorui Shi, Yuxin Chen, Zhengxi Lu et al.
**arxiv:** [arxiv.org/abs/2605.06130](https://arxiv.org/abs/2605.06130)
**Upvotes:** 64 | **Comments:** 2
**Sources:** HuggingFace Daily Papers, arxiv

A persistent skill library allows language model agents to reuse successful strategies across tasks, requiring three coupled capabilities: skill selection, utilization, and distillation. Skill1 is a unified framework that trains a single policy to simultaneously evolve all three capabilities using reinforcement learning, addressing the fragmentation of existing approaches that optimize each in isolation with separate reward sources.

**Why trending:** Directly addresses agent memory and skill reuse — a hot topic in the LLM agent community; strong upvote signal on day of release.

---

## 3. MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction

**Authors:** Junbo Cui, Bokai Xu, Chongyi Wang et al.
**arxiv:** [arxiv.org/abs/2604.27393](https://arxiv.org/abs/2604.27393)
**Upvotes:** 60 | **Comments:** 2
**Sources:** HuggingFace Daily Papers, arxiv, r/LocalLLaMA

Recent progress in multimodal LLMs has advanced from static processing to real-time streaming interaction, but still falls short of human-level multimodal interaction. MiniCPM-o 4.5 enables real-time full-duplex multimodal interaction through Omni-Flow, a unified streaming framework that aligns inputs and outputs temporally — tackling the interaction paradigm as the core bottleneck rather than just modality coverage.

**Why trending:** Practical edge-deployable multimodal model with full-duplex real-time interaction; strong community interest in r/LocalLLaMA for on-device use.

---

## 4. Continuous Latent Diffusion Language Model (Cola DLM)

**Authors:** Hongcan Guo, Qinyu Zhao, Yian Zhao et al.
**arxiv:** [arxiv.org/abs/2605.06548](https://arxiv.org/abs/2605.06548)
**Upvotes:** 59 | **Comments:** 2
**Sources:** HuggingFace Daily Papers, arxiv

Large language models have achieved remarkable success under the autoregressive paradigm, yet high-quality text generation need not be tied to left-to-right order. Cola DLM proposes a hierarchical latent diffusion language model that uses text-to-latent mapping, global semantic prior modeling, and conditional decoding — jointly achieving generation efficiency, scalable representation learning, and effective global semantic modeling without autoregressive constraints.

**Why trending:** Challenges the dominant autoregressive paradigm for LLMs; diffusion-based language modeling has strong community interest across arxiv and HF.

---

## 5. MiA-Signature: Approximating Global Activation for Long-Context Understanding

**Authors:** Yuqing Li, Jiangnan Li, Mo Yu et al.
**arxiv:** [arxiv.org/abs/2605.06416](https://arxiv.org/abs/2605.06416)
**Upvotes:** 49 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

Cognitive science suggests that reportable conscious access is associated with global ignition over distributed memory systems, yet individuals cannot directly enumerate all activated contents. Drawing on this insight, MiA-Signature proposes a compact representation that approximates the full global activation state in LLMs, enabling richer long-context understanding without the computational cost of full attention over all tokens.

**Why trending:** Novel cognitive-science-inspired approach to long-context understanding in LLMs — a critical practical problem; cross-disciplinary framing drives discussion.

---

## 6. RaguTeam at SemEval-2026 Task 8: Judge-Orchestrated LLM Ensemble for Multi-Turn RAG Evaluation

**Authors:** Ivan Bondarenko, Roman Derunets, Oleg Sedukhin et al.
**arxiv:** [arxiv.org/abs/2605.04523](https://arxiv.org/abs/2605.04523)
**Upvotes:** 39 | **Comments:** 5
**Sources:** HuggingFace Daily Papers, arxiv

Winning system for SemEval-2026 Task 8 (MTRAGEval), tackling faithful multi-turn response generation with reference passages. The method uses a heterogeneous ensemble of seven LLMs with dual prompting strategies, where a GPT-4o-mini judge selects the best candidate per instance — achieving a conditioned harmonic mean of 0.7827 and ranking 1st out of 26 teams.

**Why trending:** First-place system paper from a major NLP competition; practical LLM-as-judge ensemble methodology with immediate applicability.

---

## 7. When to Trust Imagination: Adaptive Action Execution for World Action Models

**Authors:** Rui Wang, Yue Zhang, Jiehong Lin et al.
**arxiv:** [arxiv.org/abs/2605.06222](https://arxiv.org/abs/2605.06222)
**Upvotes:** 36 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

World Action Models (WAMs) jointly predict future visual observations and actions for robotic manipulation, but current WAMs execute a fixed number of predicted actions after each model inference, leaving the robot blind to divergence between imagined and actual futures. This work introduces adaptive action execution that monitors consistency between the imagined future and physical rollout, enabling the robot to interrupt and re-plan when predictions become unreliable.

**Why trending:** Important safety-relevant improvement to embodied AI; WAMs are a fast-growing paradigm in robotics and this addresses a core reliability gap.

---

## 8. MARBLE: Multi-Aspect Reward Balance for Diffusion RL

**Authors:** Canyu Zhao, Hao Chen, Yunze Tong et al.
**arxiv:** [arxiv.org/abs/2605.06507](https://arxiv.org/abs/2605.06507)
**Upvotes:** 34 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

Reinforcement learning fine-tuning has become the dominant approach for aligning diffusion models with human preferences, but assessing images is intrinsically multi-dimensional. Existing practice trains one specialist model per reward and optimizes a weighted-sum objective. MARBLE introduces a gradient-space optimization framework that addresses all rewards simultaneously without specialist models, resolving reward imbalance issues in diffusion model alignment.

**Why trending:** Diffusion model RL alignment is a key research direction; practical improvement over standard weighted-sum reward approaches for image generation.

---

## 9. SkillOS: Learning Skill Curation for Self-Evolving Agents

**Authors:** Siru Ouyang, Jun Yan, Yanfei Chen et al.
**arxiv:** [arxiv.org/abs/2605.06614](https://arxiv.org/abs/2605.06614)
**Upvotes:** 32 | **Comments:** 2
**Sources:** HuggingFace Daily Papers, arxiv

LLM-based agents deployed on streaming tasks often remain one-off problem solvers that fail to learn from past interactions. SkillOS enables self-evolving LLM agents to learn complex long-term skill curation policies through reinforcement learning, where reusable skills distilled from experience serve as the substrate for self-evolution — outperforming manual and heuristic skill curation approaches.

**Why trending:** Self-evolving agents that get better over time is a core goal in AI agent research; RL-based skill curation is a novel take on the problem.

---

## 10. Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration (LoPE)

**Authors:** Langlin Huang, Chengsong Huang, Jinyuan Li et al.
**arxiv:** [arxiv.org/abs/2605.05566](https://arxiv.org/abs/2605.05566)
**Upvotes:** 31 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

GRPO reinforcement learning with verifiable rewards has advanced LLM reasoning, but suffers from the zero-advantage problem: when all sampled rollouts for a query fail, relative advantage collapses to zero and training stalls. LoPE addresses this by injecting Lorem Ipsum perturbations into the prompt space to broaden reasoning exploration in complex tasks, breaking the symmetry that causes stagnation.

**Why trending:** Creative and counterintuitive solution to a real GRPO training failure mode; immediately applicable to anyone training reasoning models with RL.

---

## 11. Audio-Visual Intelligence in Large Foundation Models (Survey)

**Authors:** You Qin, Kai Liu, Shengqiong Wu et al.
**arxiv:** [arxiv.org/abs/2605.04045](https://arxiv.org/abs/2605.04045)
**Upvotes:** 26 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

Audio-Visual Intelligence (AVI) has emerged as a central frontier in AI, bridging auditory and visual modalities to enable machines that can perceive, generate, and interact in the multimodal real world. This comprehensive survey covers joint modeling of audio and vision in the era of large foundation models, cataloging the landscape of perception, generation, and interaction tasks across AVI.

**Why trending:** Timely survey of a rapidly expanding area; provides orientation for researchers entering the audio-visual multimodal space.

---

## 12. Continuous-Time Distribution Matching for Few-Step Diffusion Distillation

**Authors:** Tao Liu, Hao Yan, Mengting Chen et al.
**arxiv:** [arxiv.org/abs/2605.06376](https://arxiv.org/abs/2605.06376)
**Upvotes:** 24 | **Comments:** 4
**Sources:** HuggingFace Daily Papers, arxiv

Step distillation is a leading technique for accelerating diffusion models. This work migrates Distribution Matching Distillation (DMD) from discrete to continuous-time optimization, enabling arbitrary points along the ODE trajectory to be leveraged for matching rather than a fixed set of discrete steps — improving both quality and efficiency of few-step generation.

**Why trending:** Practical advance in fast image/video generation via diffusion; continuous-time formulation is theoretically elegant and empirically effective.

---

## 13. CreativityBench: Evaluating Agent Creative Reasoning via Affordance-Based Tool Repurposing

**Authors:** Cheng Qian, Hyeonjeong Ha, Jiayu Liu et al.
**arxiv:** [arxiv.org/abs/2605.02910](https://arxiv.org/abs/2605.02910)
**Upvotes:** 20 | **Comments:** 2
**Sources:** HuggingFace Daily Papers, arxiv

Recent advances in LLMs yield strong performance on reasoning and environment-interaction tasks, yet creative problem-solving remains underexplored. CreativityBench evaluates this via creative tool use — repurposing available objects by reasoning about affordances — revealing that current LLMs demonstrate limited creativity when required to think outside their trained use patterns.

**Why trending:** Novel benchmark targeting a genuine gap in LLM evaluation; affordance-based reasoning is a fresh angle on agent capability assessment.

---

## 14. StraTA: Incentivizing Agentic RL with Strategic Trajectory Abstraction

**Authors:** Xiangyuan Xue, Yifan Zhou, Zidong Wang, Philip Torr, Wanli Ouyang et al.
**arxiv:** [arxiv.org/abs/2605.06642](https://arxiv.org/abs/2605.06642)
**Upvotes:** 17 | **Comments:** 2
**Sources:** HuggingFace Daily Papers, arxiv

Current agentic RL methods are purely reactive, weakening exploration and credit assignment over long trajectories. StraTA introduces an explicit trajectory-level strategy: sampling a compact strategy from the initial task state and conditioning all subsequent actions on it, with hierarchical GRPO-style rollout training enhanced by diverse strategy rollout and critical self-judgment. Achieves 93.1% on ALFWorld and 84.2% on WebShop.

**Why trending:** Strong empirical results on well-known agentic benchmarks; notable authors including Philip Torr and Wanli Ouyang.

---

## 15. Auto Research with Specialist Agents Develops Effective Training Recipes

**Authors:** Jingjie Ning, Xiaochuan Li, Ji Zeng et al.
**arxiv:** [arxiv.org/abs/2605.05724](https://arxiv.org/abs/2605.05724)
**Upvotes:** 12 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

Auto research operates as a closed empirical loop: each trial carries a hypothesis, an executable code edit, an evaluator-owned outcome, and feedback shaping the next proposal. Specialist agents iteratively refine code based on evaluation feedback, producing an auditable trajectory of proposals and code diffs — achieving improved performance across ML tasks without human intervention.

**Why trending:** AI-driven automated ML research is a hot frontier; the auditable trajectory of proposals addresses transparency concerns in autonomous research.

---

## 16. A²TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-Level Clipping

**Authors:** Dingwei Chen, Zefang Zong, Zhipeng Ma et al.
**arxiv:** [arxiv.org/abs/2605.06200](https://arxiv.org/abs/2605.06200)
**Upvotes:** 11 | **Comments:** 4
**Sources:** HuggingFace Daily Papers, arxiv

Agentic LLM RL typically relies on sparse trajectory-level outcome rewards, making it difficult to evaluate individual tool-calls in multi-turn interactions. A²TGPO addresses credit assignment at the turn-group level within multi-turn interactions, introducing adaptive turn-level clipping to provide finer-grained policy updates without external process reward models.

**Why trending:** Practical RL improvement for multi-turn agentic LLMs — a critical engineering problem as agents handle longer, more complex task sequences.

---

## 17. Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key (ScaleLogic)

**Authors:** Tianle Wang, Zhaoyang Wang, Guangchen Lan et al.
**arxiv:** [arxiv.org/abs/2605.06638](https://arxiv.org/abs/2605.06638)
**Upvotes:** 11 | **Comments:** 5
**Sources:** HuggingFace Daily Papers, arxiv

A systematic study of how RL training scales with task difficulty in LLM reasoning has been hampered by lack of controlled environments. ScaleLogic introduces a synthetic logical reasoning framework with independent control over reasoning depth and breadth, demonstrating that RL training compute scales as a power law with reasoning depth and that model expressiveness determines the ceiling.

**Why trending:** Rigorous scaling analysis for RL-trained reasoning — directly informs training decisions for anyone building reasoning-capable LLMs.

---

## 18. AI Co-Mathematician: Accelerating Mathematicians with Agentic AI

**Authors:** Daniel Zheng, Ingrid von Glehn, Yori Zwols et al.
**arxiv:** [arxiv.org/abs/2605.06651](https://arxiv.org/abs/2605.06651)
**Upvotes:** 10 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

The AI co-mathematician is an interactive workbench for mathematicians to leverage AI agents for open-ended research, optimized for holistic support across the full mathematical workflow: ideation, literature search, computational exploration, theorem proving, and theory building. Unlike prior automated theorem provers, it positions AI as a collaborative research partner rather than a solver.

**Why trending:** Represents a new paradigm for AI-assisted scientific research; interactive and exploratory design is a meaningful step beyond automated theorem provers.

---

## 19. TabEmbed: Benchmarking and Learning Generalist Embeddings for Tabular Understanding

**Authors:** Minjie Qiang, Mingming Zhang, Xiaoyi Bao et al.
**arxiv:** [arxiv.org/abs/2605.04962](https://arxiv.org/abs/2605.04962)
**Upvotes:** 7 | **Comments:** 3
**Sources:** HuggingFace Daily Papers, arxiv

Foundation models have established unified representations for NLP and vision, yet this paradigm remains largely unexplored for tabular data. TabEmbed introduces a generalist embedding model that unifies tabular classification and retrieval tasks within a shared embedding space, addressing the fundamental limitations of LLM-based approaches (no retrieval-compatible vectors) and text embedding models (poor tabular structure capture).

**Why trending:** Fills a notable gap — tabular data foundation models are underexplored relative to text/vision; practical implications for enterprise ML pipelines.

---

## 20. UniPool: A Globally Shared Expert Pool for Mixture-of-Experts

**Authors:** Minbin Huang, Han Shi, Chuanyang Zheng et al.
**arxiv:** [arxiv.org/abs/2605.06665](https://arxiv.org/abs/2605.06665)
**Upvotes:** 7 | **Comments:** 4
**Sources:** HuggingFace Daily Papers, arxiv

Modern MoE architectures allocate expert capacity through a rigid per-layer rule where each transformer layer owns a separate expert set, coupling depth scaling with linear expert-parameter growth. UniPool challenges this convention with a globally shared expert pool that decouples expert capacity from depth, reducing parameter growth with depth while maintaining or improving performance across standard MoE benchmarks.

**Why trending:** MoE efficiency is critical as models scale; a globally shared pool is an elegant architectural rethink with immediate practical implications.
