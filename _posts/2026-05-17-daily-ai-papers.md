---
title: "Daily AI Papers — May 17, 2026"
date: 2026-05-17
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-17/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reasoning
  - agent-memory
  - video-generation
---

## 1. Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling

**Authors:** Yafu Li, Runzhe Zhan, Haoran Zhang, Shunkai Zhang, Yizhuo Li  
**arXiv:** [arxiv.org/abs/2605.13301](https://arxiv.org/abs/2605.13301)  
**Sources:** HuggingFace (140 upvotes)  
**Why trending:** Highest-upvoted paper this week — claims gold-medal-level IMO/IPhO performance via a surprisingly simple unified recipe, directly challenging the assumption that olympiad reasoning requires massive bespoke architectures.

**Summary:** Introduces a two-stage recipe for converting a post-trained reasoning backbone into a rigorous olympiad-level solver: a reverse-perplexity curriculum for SFT instills proof-search and self-checking behaviors, then those behaviors are scaled through additional RL. Achieves gold-medal-level performance on International Mathematical Olympiad and International Physics Olympiad benchmarks without specialized architectural changes.

---

## 2. Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation

**Authors:** Min Zhao, Hongzhou Zhu, Kaiwen Zheng, Zihan Zhou, Bokai Yan  
**arXiv:** [arxiv.org/abs/2605.15141](https://arxiv.org/abs/2605.15141)  
**Sources:** HuggingFace (84 upvotes)  
**Why trending:** Real-time interactive video generation is a hot frontier; this pushes distillation to frame-wise 1-2 step generation, far below the typical 4-step chunk-wise regime.

**Summary:** Studies the aggressive setting of frame-wise autoregressive video generation with only 1–2 sampling steps, identifying student initialization as the key bottleneck in current distillation approaches. Proposes improved initialization and causal conditioning techniques that enable low-latency, streaming, controllable video rollout.

---

## 3. Self-Distilled Agentic Reinforcement Learning

**Authors:** Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu  
**arXiv:** [arxiv.org/abs/2605.15155](https://arxiv.org/abs/2605.15155)  
**Sources:** HuggingFace (82 upvotes)  
**Why trending:** Combining RL with self-distillation for multi-turn LLM agents is a research direction gaining rapid momentum; this paper directly addresses the instability problem that blocks real deployment.

**Summary:** Proposes On-Policy Self-Distillation (OPSD) to complement trajectory-level RL with dense token-level guidance from a teacher branch augmented with privileged context. Addresses multi-turn instability and asymmetric skill-conditioning challenges that arise when applying OPSD to agentic settings with long-horizon interactions.

---

## 4. MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models

**Authors:** Xiyu Ren, Zhaowei Wang, Yiming Du, Zhongwei Xie, Chi Liu  
**arXiv:** [arxiv.org/abs/2605.14906](https://arxiv.org/abs/2605.14906)  
**Sources:** HuggingFace (68 upvotes)  
**Why trending:** Memory in multimodal agents is an unsolved problem; this benchmark fills a gap by requiring genuine multimodal evidence across sessions rather than text-only retrieval.

**Summary:** Introduces MEMLENS, a comprehensive benchmark of 789 questions across five memory abilities (information extraction, multi-session reasoning, temporal reasoning, knowledge update, and conflict resolution) in multimodal multi-session conversations. Systematically compares long-context LVLMs vs memory-augmented agents on tasks that genuinely require preserved multimodal evidence.

---

## 5. SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer

**Authors:** Haoyi Zhu, Haozhe Liu, Yuyang Zhao, Tian Ye, Junsong Chen  
**arXiv:** [arxiv.org/abs/2605.15178](https://arxiv.org/abs/2605.15178)  
**Sources:** HuggingFace (67 upvotes)  
**Why trending:** Open-source world model at 720p minute-scale generation with camera control, matching industrial baselines like LingBot-World at a fraction of the compute.

**Summary:** Introduces SANA-WM, a 2.6B-parameter open-source world model natively trained for one-minute video generation at 720p with 6-DoF camera control. Uses a hybrid architecture combining frame-wise Gated DeltaNet (linear attention) with softmax attention for memory-efficient long-context modeling, achieving visual quality comparable to large-scale industrial baselines.

---

## 6. MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory

**Authors:** Minghao Guo, Qingyue Jiao, Zeru Shi, Yihao Quan, Boxuan Zhang  
**arXiv:** [arxiv.org/abs/2605.15128](https://arxiv.org/abs/2605.15128)  
**Sources:** HuggingFace (54 upvotes)  
**Why trending:** Identifies that current memory benchmarks can be solved with captions alone — a fundamental flaw this work fixes by demanding fine-grained visual evidence preservation.

**Summary:** Introduces MemEye, a framework evaluating agent memory along two dimensions: granularity of decisive visual evidence retained and reasoning across temporally changing visual states. Closes the gap where prior benchmarks allow text-caption shortcuts, ensuring agents must actually preserve and reason over raw visual content.

---

## 7. Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning

**Authors:** Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang  
**arXiv:** [arxiv.org/abs/2605.14386](https://arxiv.org/abs/2605.14386)  
**Sources:** HuggingFace (50 upvotes)  
**Why trending:** Training-free model merging for improved reasoning has broad appeal — no GPU cost, just recombining existing checkpoints to unlock frontier-level capability.

**Summary:** Presents Darwin Family, a training-free evolutionary merging framework using gradient-free weight-space recombination with a 14-dimensional adaptive merge genome for fine-grained component/block-level control. Introduces MRI-Trust Fusion to adaptively balance layer-importance signals with evolutionary search, achieving competitive reasoning performance without any additional training.

---

## 8. Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems

**Authors:** Shihao Qi, Jie Ma, Rui Xing, Wei Guo, Xiao Huang  
**arXiv:** [arxiv.org/abs/2605.14892](https://arxiv.org/abs/2605.14892)  
**Sources:** HuggingFace (44 upvotes)  
**Why trending:** Comprehensive surveys of multi-agent LLM systems are rare; this one uniquely covers the underexplored failure attribution and self-evolution dimensions.

**Summary:** Surveys LLM-based multi-agent systems with a focus on three underexplored challenges: structured collaboration among specialized agents, failure attribution when errors propagate across agent interactions, and mechanisms for self-improvement and structural evolution. Provides a unified taxonomy that goes beyond standard capability-centric surveys.

---

## 9. WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation

**Authors:** Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu  
**arXiv:** [arxiv.org/abs/2605.10912](https://arxiv.org/abs/2605.10912)  
**Sources:** HuggingFace (40 upvotes)  
**Why trending:** Most agent benchmarks use synthetic sandboxes; this one evaluates agents in real CLI runtimes on human-authored tasks averaging 8 minutes each — a significantly harder bar.

**Summary:** Introduces WildClawBench, a native-runtime benchmark of 60 human-authored, bilingual, multimodal tasks across six thematic categories for evaluating LLM agents on realistic long-horizon CLI work. Each task averages ~8 minutes of wall-clock execution time and uses real service APIs rather than mock environments.

---

## 10. STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?

**Authors:** Hanxiang Chao, Yihan Bai, Rui Sheng, Tianle Li, Yushi Sun  
**arXiv:** [arxiv.org/abs/2605.06527](https://arxiv.org/abs/2605.06527)  
**Sources:** HuggingFace (39 upvotes)  
**Why trending:** Identifies "Implicit Conflict" — a failure mode where outdated memory persists without explicit negation — as a blind spot in all current LLM memory systems.

**Summary:** Identifies the critical failure mode of Implicit Conflict: a later observation invalidates an earlier memory without explicit negation, requiring contextual inference and commonsense reasoning to detect. Introduces STALE, a benchmark of 400 expert-validated conflict scenarios to rigorously evaluate whether LLM agents can revise stale beliefs.

---

## 11. Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video

**Authors:** Yifan Wang, Tong He  
**arXiv:** [arxiv.org/abs/2605.15182](https://arxiv.org/abs/2605.15182)  
**Sources:** HuggingFace (36 upvotes)  
**Why trending:** Training-free camera control for video generation from a single video is a practical breakthrough for content creators and robotics sim-to-real applications.

**Summary:** Proposes Warp-as-History, a training-free interface that converts camera-induced geometric warps into history conditioning signals for video diffusion models. Avoids expensive camera encoder post-training or test-time optimization, enabling generalizable camera-controlled video generation without large-scale annotated data.

---

## 12. RouteProfile: Elucidating the Design Space of LLM Profiles for Routing

**Authors:** Jingjun Xu, Hongji Pu, Tao Feng, Haozhen Zhang, Jiaxuan You  
**arXiv:** [arxiv.org/abs/2605.00180](https://arxiv.org/abs/2605.00180)  
**Sources:** HuggingFace (28 upvotes)  
**Why trending:** LLM routing is becoming critical infrastructure as multi-model deployments scale; understanding what capability profiles to use is a practical and underexplored problem.

**Summary:** Investigates how LLM profile design — the representation of each model's capabilities — affects routing performance across different router mechanisms. Disentangles profile design from router design to enable fairer comparisons and more principled development of LLM routing systems.

---

## 13. PREPING: Building Agent Memory without Tasks

**Authors:** Yumin Choi, Sangwoo Park, Minki Kang, Jinheon Baek, Sung Ju Hwang  
**arXiv:** [arxiv.org/abs/2605.13880](https://arxiv.org/abs/2605.13880)  
**Sources:** HuggingFace (25 upvotes)  
**Why trending:** Cold-start memory for agents is a practical bottleneck in production deployments; this addresses it with synthetic pre-task practice.

**Summary:** Studies pre-task memory construction: building procedural agent memory before observing any target-environment tasks using only self-generated synthetic practice. Identifies that naive synthetic interaction is insufficient and introduces structured control over what to practice and what to store to bridge the cold-start gap.

---

## 14. VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction

**Authors:** Kaixin Zhu, Yiwen Tang, Yifan Yang, Renrui Zhang, Bohan Zeng  
**arXiv:** [arxiv.org/abs/2605.15186](https://arxiv.org/abs/2605.15186)  
**Sources:** HuggingFace (23 upvotes)  
**Why trending:** Extends VGGT-style feed-forward 3D reconstruction to interactive editing, replacing the blurry 2D-lifting pipeline with direct 3D field prediction.

**Summary:** Proposes a feed-forward architecture for native 3D scene editing that responds to dynamic text instructions via residual field prediction directly in 3D space. Avoids the 2D-lifting strategy (edit views independently, lift back to 3D) that produces blurry textures and inconsistencies, enabling high-fidelity interactive edits.

---

## 15. Long Context Pre-Training with Lighthouse Attention

**Authors:** Bowen Peng, Subho Ghosh, Jeffrey Quesnelle  
**arXiv:** [arxiv.org/abs/2605.06554](https://arxiv.org/abs/2605.06554)  
**Sources:** HuggingFace (21 upvotes)  
**Why trending:** A training-only, drop-in replacement for SDPA that makes extreme-context pre-training feasible without a complicated custom backward pass.

**Summary:** Introduces Lighthouse Attention, a training-only symmetrical selection-based hierarchical attention algorithm that wraps standard SDPA and can be removed at inference. Achieves subquadratic complexity for pre-training at extreme sequence lengths using gradient-free hierarchical selection, eliminating the need for complex custom backward kernels.

---

## 16. Realiz3D: 3D Generation Made Photorealistic via Domain-Aware Learning

**Authors:** Ido Sobol, Kihyuk Sohn, Yoav Blum, Egor Zakharov, Max Bluvstein  
**arXiv:** [arxiv.org/abs/2605.13852](https://arxiv.org/abs/2605.13852)  
**Sources:** HuggingFace (21 upvotes)  
**Why trending:** Tackles the persistent domain gap problem in 3D generation — synthetic renders look fake even when geometry is correct — with a targeted domain-aware training approach.

**Summary:** Identifies that fine-tuning image generators on synthetic 3D renders introduces an unintended association between render-style artifacts and geometry control signals, degrading photorealism. Proposes domain-aware learning to decouple these associations, enabling geometry/material/viewpoint control while preserving the realism of pre-trained image generators.

---

## 17. EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents

**Authors:** Jiaqi Liu, Xinyu Ye, Peng Xia, Zeyu Zheng, Cihang Xie  
**arXiv:** [arxiv.org/abs/2605.13941](https://arxiv.org/abs/2605.13941)  
**Sources:** HuggingFace (21 upvotes)  
**Why trending:** Goes beyond static retrieval pipelines by co-evolving both stored knowledge and the retrieval mechanism itself — a step toward truly adaptive agent memory.

**Summary:** Presents EvolveMem, a self-evolving memory architecture that exposes retrieval configuration (scoring functions, fusion strategies, answer-generation policies) as a structured action space optimized by an LLM-powered diagnosis module. Enables co-evolution of stored knowledge and the retrieval mechanism rather than freezing the infrastructure at deployment.

---

## 18. Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding

**Authors:** Valeriy Vyaltsev, Alsu Sagirova, Anton Andreychuk, Oleg Bulichev, Yuri Kuratov  
**arXiv:** [arxiv.org/abs/2605.07637](https://arxiv.org/abs/2605.07637)  
**Sources:** HuggingFace (17 upvotes)  
**Why trending:** Scalable MAPF is critical for warehouse robotics and autonomous logistics; local communication learning offers a practical path past the NP-hard global planning wall.

**Summary:** Proposes a decentralized MAPF solver framing the problem as a Dec-POMDP where each agent learns local communication policies for coordinating with neighbors. Achieves scalable, efficient multi-robot trajectory planning for large environments relevant to logistics and search-and-rescue applications.

---

## 19. FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale

**Authors:** Runyuan He, Qiuyang Mang, Shang Zhou, Kaiyuan Liu, Hanchen Li  
**arXiv:** [arxiv.org/abs/2605.14445](https://arxiv.org/abs/2605.14445)  
**Sources:** HuggingFace (17 upvotes)  
**Why trending:** Open-ended coding (no known optimal solution) is the weak spot in current LLM coding benchmarks; synthetic problem generation at scale addresses the data scarcity directly.

**Summary:** Introduces FrontierSmith, an automated system that iteratively evolves open-ended coding problems from existing closed-ended tasks, generating training data for LLMs on problems with no known optimal solution. Addresses the scarcity of open-ended training examples that limits current LLM coding capabilities beyond competitive programming.

---

## 20. ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both

**Authors:** Ziyu Guo, Rain Liu, Xinyan Chen, Pheng-Ann Heng  
**arXiv:** [arxiv.org/abs/2605.15198](https://arxiv.org/abs/2605.15198)  
**Sources:** HuggingFace (17 upvotes)  
**Why trending:** Unifies the two main paradigms for visual reasoning (agentic tool-use vs. latent embedding) with a single lightweight approach, avoiding latency and generalization tradeoffs of each.

**Summary:** Proposes ATLAS, a unified approach for visual reasoning that bridges agentic methods (code/tool calls with context-switching latency) and latent methods (learnable hidden embeddings with poor generalization). Achieves competitive performance on both paradigms with minimal architectural overhead — "one word" refers to a single control token that routes between modes.
