---
title: "Daily AI Papers — May 15, 2026"
date: 2026-05-15
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-15/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reasoning
  - agentic-memory
  - video-generation
---

## 1. Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling

**Authors:** Yafu Li, Runzhe Zhan, Haoran Zhang, Shunkai Zhang, Yizhuo Li, Zhilin Wang et al.

**Summary:** This paper introduces a simple, unified recipe for converting a post-trained reasoning backbone into a gold-medal-level olympiad solver, achieving top performance on IMO and IPhO benchmarks. The approach uses a reverse-perplexity curriculum for SFT to instill rigorous mathematical reasoning, followed by reinforcement learning on verifiable olympiad-level problems.

**Arxiv:** [arxiv.org/abs/2605.13301](https://arxiv.org/abs/2605.13301)

**Sources:** HuggingFace Daily Papers (#1, 119 upvotes, 1 comment), arXiv cs.AI

**Why trending:** Highest-upvoted paper of the day by a wide margin — gold-medal IMO/IPhO performance via a "simple and unified" recipe is a major milestone for AI reasoning, and the accessible approach (no exotic architecture) makes it highly reproducible.

---

## 2. Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation

**Authors:** Min Zhao, Hongzhou Zhu, Kaiwen Zheng, Zihan Zhou

**Summary:** Causal Forcing++ pushes autoregressive video diffusion distillation into the frame-wise 1–2 step regime, enabling real-time, streaming video generation with low latency and precise controllability. It addresses coarse response granularity and sampling latency bottlenecks that prior chunk-wise 4-step AR distillation methods leave unsolved.

**Arxiv:** [arxiv.org/abs/2605.15141](https://arxiv.org/abs/2605.15141)

**Sources:** HuggingFace Daily Papers (#2, 70 upvotes, 2 comments), arXiv cs.CV

**Why trending:** Real-time interactive video is a highly sought-after capability; this advances state-of-the-art distillation to sub-2-step generation, a significant engineering and research breakthrough.

---

## 3. Self-Distilled Agentic Reinforcement Learning

**Authors:** Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang

**Summary:** SDAIRL addresses the coarse trajectory-level reward problem in RL-trained LLM agents by introducing On-Policy Self-Distillation (OPSD), which provides dense token-level guidance from a teacher branch augmented with privileged context. The method stabilizes multi-turn agent training where previous OPSD approaches failed due to compounding instability.

**Arxiv:** [arxiv.org/abs/2605.15155](https://arxiv.org/abs/2605.15155)

**Sources:** HuggingFace Daily Papers (#3, 62 upvotes), arXiv cs.LG

**Why trending:** RL-based agentic post-training is a dominant research direction; dense supervision for long-horizon agents solves a core credit-assignment problem the community has been grappling with.

---

## 4. MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models

**Authors:** Xiyu Ren, Zhaowei Wang, Yiming Du, Zhongwei Xie

**Summary:** MemLens is a comprehensive benchmark of 789 questions across five memory task types, systematically comparing long-context LVLMs against memory-augmented agents on questions that genuinely require multimodal evidence. It closes an important gap where prior benchmarks could be solved from text captions alone, without preserving visual memory.

**Arxiv:** [arxiv.org/abs/2605.14906](https://arxiv.org/abs/2605.14906)

**Sources:** HuggingFace Daily Papers (#4, 59 upvotes, 4 comments), arXiv cs.CV

**Why trending:** Multimodal long-term memory is an open problem as agents become more capable; this is the first benchmark that rigorously demands visual evidence retention, making it a key community resource.

---

## 5. SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer

**Authors:** Haoyi Zhu, Haozhe Liu, Yuyang Zhao, Tian Ye

**Summary:** SANA-WM is an efficient 2.6B-parameter open-source world model for one-minute, 720p video generation with precise camera control, matching visual quality of large industrial baselines like LingBot-World at significantly lower compute. Its hybrid architecture combines frame-wise Gated DeltaNet with softmax attention, enabling linear-time modeling over long video sequences.

**Arxiv:** [arxiv.org/abs/2605.15178](https://arxiv.org/abs/2605.15178)

**Sources:** HuggingFace Daily Papers (#5, 48 upvotes, 1 comment), arXiv cs.CV

**Why trending:** Open-source minute-scale world models at 720p are rare; combining efficiency with quality and camera control addresses a major gap between industrial and academic video generation capabilities.

---

## 6. MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory

**Authors:** Minghao Guo, Qingyue Jiao, Zeru Shi, Yihao Quan

**Summary:** MemEye introduces a visual-centric evaluation framework for multimodal agent memory, specifically testing whether agents preserve fine-grained visual evidence for downstream reasoning — not just text captions or traces. The framework exposes a systematic weakness in current memory-augmented agents that prior text-only evaluations missed.

**Arxiv:** [arxiv.org/abs/2605.15128](https://arxiv.org/abs/2605.15128)

**Sources:** HuggingFace Daily Papers (#6, 47 upvotes, 1 comment), arXiv cs.AI

**Why trending:** Complements MemLens (#4) on the same day — the community is clearly focused on multimodal memory as a critical frontier, and MemEye adds a targeted visual-evidence angle.

---

## 7. Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning

**Authors:** Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi

**Summary:** Darwin Family presents a training-free evolutionary merging framework for LLMs using a 14-dimensional adaptive merge genome and gradient-free weight-space recombination, showing that frontier-level reasoning can be improved by reorganizing latent capabilities already encoded in existing checkpoints. It challenges the assumption that scaling reasoning always requires additional training compute.

**Arxiv:** [arxiv.org/abs/2605.14386](https://arxiv.org/abs/2605.14386)

**Sources:** HuggingFace Daily Papers (#7, 42 upvotes, 2 comments), arXiv cs.LG

**Why trending:** Training-free scaling of reasoning is a highly desirable property for resource-constrained practitioners; evolutionary model merging is gaining traction as a competitive alternative to continued training.

---

## 8. Beyond Individual Intelligence: Surveying Collaboration, Failure Attribution, and Self-Evolution in LLM-based Multi-Agent Systems

**Authors:** Shihao Qi, Jie Ma, Rui Xing, Wei Guo

**Summary:** This comprehensive survey maps the landscape of LLM-based multi-agent systems with a focus on how errors propagate across agents, how failure can be attributed to specific components, and how systems can self-evolve. It identifies tighter coordination as a double-edged sword — enabling complex tasks but amplifying cascading failure risks.

**Arxiv:** [arxiv.org/abs/2605.14892](https://arxiv.org/abs/2605.14892)

**Sources:** HuggingFace Daily Papers (#8, 38 upvotes, 2 comments), arXiv cs.AI

**Why trending:** As multi-agent systems move into production, failure attribution and self-evolution are urgent unsolved problems; a survey that unifies these themes is a valuable reference for the community.

---

## 9. STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?

**Authors:** Hanxiang Chao, Yihan Bai, Rui Sheng, Tianle Li

**Summary:** STALE introduces a new benchmark targeting "Implicit Conflict" — the failure mode where a later observation invalidates an earlier memory without explicit negation, which current agents fail to detect. The paper demonstrates that existing LLM agents overwhelmingly rely on stale memories when new evidence is implicit rather than contradictory.

**Arxiv:** [arxiv.org/abs/2605.06527](https://arxiv.org/abs/2605.06527)

**Sources:** HuggingFace Daily Papers (#9, 37 upvotes, 1 comment), arXiv cs.CL

**Why trending:** Memory validity is a subtle and underappreciated failure mode for production agents; this benchmark crystallizes the problem and provides a concrete evaluation protocol.

---

## 10. WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation

**Authors:** Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding

**Summary:** WildClawBench evaluates LLM and VLM agents on realistic, long-horizon CLI tasks drawn from real user workflows — not synthetic sandboxes — using actual service APIs and end-to-end process verification. It reveals a large gap between agent performance on existing synthetic benchmarks and real-world deployment scenarios.

**Arxiv:** [arxiv.org/abs/2605.10912](https://arxiv.org/abs/2605.10912)

**Sources:** HuggingFace Daily Papers (#10, 35 upvotes, 2 comments), arXiv cs.AI

**Why trending:** The gap between benchmark performance and real-world capability is a major credibility problem for the agent field; WildClawBench's emphasis on real CLIs and long horizons makes it uniquely positioned to drive the next generation of agent evaluation.

---

## 11. Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video

**Authors:** Yifan Wang, Tong He

**Summary:** Warp-as-History achieves camera-controlled video generation without training on large-scale camera-annotated datasets, instead using a single training video by treating geometric warping as an implicit history signal. This training-free approach to camera conditioning sidesteps the expensive post-training pipelines required by encoder- or attention-modification-based methods.

**Arxiv:** [arxiv.org/abs/2605.15182](https://arxiv.org/abs/2605.15182)

**Sources:** HuggingFace Daily Papers (#11, 32 upvotes, 1 comment), arXiv cs.CV

**Why trending:** Removing the need for large annotated camera datasets democratizes camera-controlled video generation significantly.

---

## 12. RouteProfile: Elucidating the Design Space of LLM Profiles for Routing

**Authors:** Jingjun Xu, Hongji Pu, Tao Feng, Haozhen Zhang

**Summary:** RouteProfile systematically explores how the design of LLM capability profiles — rather than the routing mechanism itself — affects routing performance across benchmarks and domains. It finds that profile design is an underexplored but critical factor, with poorly designed profiles causing significant routing degradation even with strong router architectures.

**Arxiv:** [arxiv.org/abs/2605.00180](https://arxiv.org/abs/2605.00180)

**Sources:** HuggingFace Daily Papers (#12, 24 upvotes, 1 comment), arXiv cs.LG

**Why trending:** LLM routing is increasingly important for cost-efficient inference; shifting focus to profile design is a fresh and practically valuable angle.

---

## 13. PREPING: Building Agent Memory without Tasks

**Authors:** Yumin Choi, Sangwoo Park, Minki Kang, Jinheon Baek

**Summary:** PREPING addresses the cold-start gap for agents entering new environments without task-specific experience, constructing agent memory proactively from environment structure rather than from curated demonstrations or post-deployment interactions. This allows agents to build useful memory before any tasks are assigned.

**Arxiv:** [arxiv.org/abs/2605.13880](https://arxiv.org/abs/2605.13880)

**Sources:** HuggingFace Daily Papers (#13, 23 upvotes, 1 comment), arXiv cs.AI

**Why trending:** Cold-start is a fundamental deployment challenge for memory-augmented agents; solving it without requiring any task experience is a meaningful practical advance.

---

## 14. EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents

**Authors:** Jiaqi Liu, Xinyu Ye, Peng Xia, Zeyu Zheng

**Summary:** EvolveMem argues that truly adaptive long-term memory requires co-evolution of both stored knowledge and retrieval mechanisms — scoring functions, fusion strategies, and answer-generation policies should evolve alongside stored content across sessions. The system uses automated research to continuously improve retrieval infrastructure without human-defined update rules.

**Arxiv:** [arxiv.org/abs/2605.13941](https://arxiv.org/abs/2605.13941)

**Sources:** HuggingFace Daily Papers (#14, 20 upvotes, 1 comment), arXiv cs.AI

**Why trending:** Thematically unified with today's cluster of memory papers (STALE, MemLens, MemEye, PREPING); EvolveMem's self-evolving retrieval angle is the most ambitious and distinguishes itself with the AutoResearch mechanism.

---

## 15. Realiz3D: 3D Generation Made Photorealistic via Domain-Aware Learning

**Authors:** Ido Sobol, Kihyuk Sohn, Yoav Blum, Egor Zakharov

**Summary:** Realiz3D addresses the domain gap between synthetic 3D renders and real photographs when fine-tuning image generators for 3D-consistent generation, using domain-aware learning to preserve photorealism while maintaining geometric, material, and viewpoint control. The approach bridges the realism gap that emerges when standard fine-tuning on render data degrades the visual quality of generated images.

**Arxiv:** [arxiv.org/abs/2605.13852](https://arxiv.org/abs/2605.13852)

**Sources:** HuggingFace Daily Papers (#15, 18 upvotes, 1 comment), arXiv cs.CV

**Why trending:** 3D-consistent photorealistic generation is a key enabler for AR/VR, gaming, and product visualization; tackling the domain gap directly is a practical contribution.

---

## 16. ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both

**Authors:** Ziyu Guo, Rain Liu, Xinyan Chen, Pheng-Ann Heng

**Summary:** ATLAS unifies agentic visual reasoning (via code/tool calls) and latent visual reasoning (via learnable hidden tokens) with a single-word switch, showing that both paradigms can be supported by the same model without architectural changes. This flexibility lets the model select the most compute-efficient reasoning mode depending on task complexity.

**Arxiv:** [arxiv.org/abs/2605.15198](https://arxiv.org/abs/2605.15198)

**Sources:** HuggingFace Daily Papers (#16, 16 upvotes, 1 comment), arXiv cs.CV

**Why trending:** Unifying two competing visual reasoning paradigms in a single model is an elegant result with strong practical implications for deployment flexibility.

---

## 17. Learning to Communicate Locally for Large-Scale Multi-Agent Pathfinding

**Authors:** Valeriy Vyaltsev, Alsu Sagirova, Anton Andreychuk, Oleg Bulichev

**Summary:** This paper introduces a local communication learning approach for multi-agent pathfinding (MAPF) that scales to large numbers of agents without the combinatorial explosion of global coordination. The method enables agents to learn efficient, sparse communication graphs that are sufficient for collision-free navigation in dense environments.

**Arxiv:** [arxiv.org/abs/2605.07637](https://arxiv.org/abs/2605.07637)

**Sources:** HuggingFace Daily Papers (#17, 15 upvotes, 2 comments), arXiv cs.MA

**Why trending:** Scalable MAPF is critical for warehouse robotics and autonomous fleet management; learning local communication graphs is a principled and deployable solution.

---

## 18. DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models

**Authors:** Quanhao Li, Junqiu Yu, Kaixun Jiang, Yujie Wei

**Summary:** DiffusionOPD proposes a unified multi-task RL distillation framework for text-to-image diffusion models that avoids the cross-task interference and catastrophic forgetting of joint training or cascade RL approaches. It reframes on-policy distillation across tasks as a unified optimization problem with a shared policy backbone.

**Arxiv:** [arxiv.org/abs/2605.15055](https://arxiv.org/abs/2605.15055)

**Sources:** HuggingFace Daily Papers (#18, 14 upvotes, 1 comment), arXiv cs.CV

**Why trending:** Multi-task RL for diffusion models is the next frontier after single-task RLHF for image generation; DiffusionOPD's unified perspective provides both theoretical grounding and practical recipe.

---

## 19. IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation

**Authors:** Shijie Lian, Bin Yu, Xiaopeng Lin, Zhaolong Shen

**Summary:** IntentVLA addresses the multimodality problem in robot imitation learning, where similar visual-language observations may be followed by different action chunks because demonstrators act with different short-horizon intents. By explicitly modeling short-horizon intent as a latent variable, the policy resolves action aliasing without relying on longer context windows.

**Arxiv:** [arxiv.org/abs/2605.14712](https://arxiv.org/abs/2605.14712)

**Sources:** HuggingFace Daily Papers (#19, 14 upvotes, 1 comment), arXiv cs.RO

**Why trending:** Action aliasing under partial observability is a core unsolved problem for VLA-based robot policies; explicit intent modeling is a clean and principled solution.

---

## 20. FrontierSmith: Synthesizing Open-Ended Coding Problems at Scale

**Authors:** Runyuan He, Qiuyang Mang, Shang Zhou, Kaiyuan Liu

**Summary:** FrontierSmith automatically synthesizes open-ended coding problems — those with no known optimal solution — at scale, targeting a weak spot where LLMs lack both training data and evaluation infrastructure. The system generates novel, verifiable open-ended challenges by combining program synthesis with automated difficulty calibration.

**Arxiv:** [arxiv.org/abs/2605.14445](https://arxiv.org/abs/2605.14445)

**Sources:** HuggingFace Daily Papers (#20, 13 upvotes, 1 comment), arXiv cs.SE

**Why trending:** Open-ended coding is where LLMs are weakest and where frontier research is most needed; synthesizing training and evaluation data at scale directly enables progress on this gap.
