---
title: "Daily AI Papers — July 19, 2026"
date: 2026-07-19
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-19/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - interpretability
  - world-models
---

## 1. Understanding Reasoning from Pretraining to Post-Training

**Authors:** Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum, Matus Telgarsky, Pavel Izmailov
**arXiv:** [arxiv.org/abs/2607.16097](https://arxiv.org/abs/2607.16097)

This paper studies RL post-training and the pretraining that precedes it jointly rather than in isolation, asking how pretraining choices (model size, data) shape the returns to RL compute and what RL actually changes inside the model. Using controlled compute sweeps it disentangles behaviors attributable to pretraining versus reinforcement learning, addressing questions that the standard uncontrolled-corpus LLM setting makes hard to answer.

**Sources found:** arXiv (cs.AI, July 17 submission)
**Why trending:** A foundational, mechanism-level treatment of the pretraining-to-RL pipeline from a heavyweight author list (Goldblum, Telgarsky, Izmailov) — exactly the kind of "what does RL really do" paper that tends to drive discussion.

---

## 2. Verbalizable Representations Form a Global Workspace in Language Models

**Authors:** Wes Gurnee, Nicholas Sofroniew, Adam Pearce, Mateusz Piotrowski, Isaac Kauvar, Runjin Chen, Anna Soligo, Paul Bogdan, Euan Ong, Rowan Wang, Ben Thompson, David Abrahams, Subhash Kantamneni, Emmanuel Ameisen, Joshua Batson, Jack Lindsey
**arXiv:** [arxiv.org/abs/2607.15495](https://arxiv.org/abs/2607.15495)

The authors introduce the "Jacobian lens," an interpretability technique that identifies the representations a model is poised to verbalize at any point in processing, and show these form a "J-space" with the functional properties of a cognitive global workspace. They argue this reveals an analog of the human distinction between consciously accessible information (available for verbal report and flexible reasoning) and the rest of a model's internal computation.

**Sources found:** arXiv (cs.CL, July 16 submission)
**Why trending:** A large interpretability team (including Wes Gurnee, Jack Lindsey, Joshua Batson) advancing a bold cognitive-science framing of LLM internals — the kind of conceptual interpretability result that reliably generates broad debate.

---

## 3. Frontier Language Models Struggle to Copy: Text Can Be Better Viewed in 2D

**Authors:** Haodong Wen, Yiran Zhang, Yingfa Chen, Kaifeng Lyu
**arXiv:** [arxiv.org/abs/2607.16072](https://arxiv.org/abs/2607.16072)

The paper shows that even frontier LLMs fail at the trivial task of exactly copying an input string well within their context window, tracing the failure to positional-encoding inductive biases that favor local-context shortcut matching over precise position location. It introduces 2D-RoPE, which lays text out on a 2D grid rather than a 1D sequence to fix the copying failure.

**Sources found:** arXiv (cs.CL, July 17 submission)
**Why trending:** A counterintuitive "frontier models can't do this simple thing" result with a concrete architectural fix (2D-RoPE) — the kind of crisp negative finding that spreads quickly.

---

## 4. When Does Muon Help Agentic Reinforcement Learning?

**Authors:** Kai Ruan, Jinghao Lin, Zihe Huang, Ziqi Zhou, Qianshan Wei, Xuan Wang, Hao Sun
**arXiv:** [arxiv.org/abs/2607.16169](https://arxiv.org/abs/2607.16169)

This study evaluates the Muon optimizer in sparse-reward agentic RL with matched single-seed comparisons against AdamW on ALFWorld using Qwen2.5-0.5B-Instruct, finding that applying Muon only to hidden weight matrices under GiGPO raises final-window validation success from 0.290 to 0.546 (+88%). The benefit is shown to depend strongly on the advantage estimator and learning rate, so Muon is not a universal win for RL post-training.

**Sources found:** arXiv (cs.AI, July 17 submission)
**Why trending:** Muon-vs-AdamW is one of the most actively argued optimizer questions right now, and extending it to agentic RL with large, condition-dependent effects lands squarely in that debate.

---

## 5. Orbis 2: A Hierarchical World Model for Driving

**Authors:** Sudhanshu Mittal, Arian Mousakhan, Silvio Galesso, Karim Farid, Johannes Dienert, Rajat Sahay, Thomas Brox
**arXiv:** [arxiv.org/abs/2607.15898](https://arxiv.org/abs/2607.15898)

Orbis 2 is a hierarchical driving world model that factorizes future prediction into a high-level predictor forecasting coarse scene structure over long horizons and a low-level generator producing detailed conditioned predictions. This two-scale decomposition aims to add the spatial reasoning and semantic understanding that single-abstraction, perceptual-fidelity-focused world models lack.

**Sources found:** arXiv (cs.AI, July 17 submission)
**Why trending:** World models for driving are an intensely watched area, and a hierarchical design from Thomas Brox's group targets the well-known reasoning gap in perception-first world models.

---

## 6. Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA

**Authors:** Ce Zhang, Ziyang Wang, Yulu Pan, Oluwatumininu Oguntola, Pranav Wagh, Qiyu Wu, Hiromi Wakaki, Mohit Bansal, Gedas Bertasius
**arXiv:** [arxiv.org/abs/2607.16189](https://arxiv.org/abs/2607.16189)

VideoTreeSearch (VTS) recasts grounded long-video QA as iterative, self-correcting search over a tree of video segments, adding fine-to-coarse backtracking that single-action `crop_video` agents lack. This lets the agent recover from early localization mistakes instead of converging prematurely on a wrong evidence interval.

**Sources found:** arXiv (cs.CV, July 17 submission)
**Why trending:** Long-video understanding plus agentic search is a hot intersection, and the author list (Mohit Bansal, Gedas Bertasius) draws attention to a clean fix for a known failure mode.

---

## 7. ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning

**Authors:** Shuaiyu Zhou, Fengpeng Yue, Zengjie Hu, Yuanzhe Shen, Chenyang Zhang, Feng Hong, Cao Liu, Ke Zeng
**arXiv:** [arxiv.org/abs/2607.15660](https://arxiv.org/abs/2607.15660)

ToolVerse automatically builds massive executable agent-training environments from nearly 400 real-world Model Context Protocol servers, scaling up the diversity and dynamism of environments available for agentic RL. It targets the gap where LLM agents reason well in compact settings but break down on large-scale, tool-integrated, long-horizon tasks.

**Sources found:** arXiv (cs.AI, July 17 submission)
**Why trending:** Environment scaling is widely seen as the current bottleneck for agentic RL, and grounding training environments in real MCP servers is a directly practical contribution.

---

## 8. When Do Multi-Agent Systems Help? An Information Bottleneck Perspective

**Authors:** Wendi Yu, Lianhao Zhou, Xiangjue Dong, Sai Sudarshan Barath, Declan Staunton, Byung-Jun Yoon, Xiaoning Qian, James Caverlee, Shuiwang Ji
**arXiv:** [arxiv.org/abs/2607.16133](https://arxiv.org/abs/2607.16133)

The paper offers an information-bottleneck account of when LLM multi-agent systems beat single-agent systems, observing that a single agent accumulates its full reasoning trace in one shared context while a multi-agent system relies on isolated local contexts linked by bounded relay messages. It shows that with infinite relay bandwidth any single agent can be simulated by a multi-agent system, framing the real trade-off in terms of finite relay capacity.

**Sources found:** arXiv (cs.AI, July 17 submission)
**Why trending:** "Do multi-agent systems actually help?" is a recurring, contentious question, and a theory-grounded answer (rather than another benchmark) is the kind of framing practitioners cite.

---

## 9. When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis

**Authors:** S. Aaron McClendon
**arXiv:** [arxiv.org/abs/2607.16062](https://arxiv.org/abs/2607.16062)

This work builds the comparison that model-merging papers usually skip — merging independently trained RL specialists (TIES, RAM+) versus a jointly trained multi-task baseline on the same data. Training difficulty-1 and difficulty-2 Qwen3-8B specialists on the AppWorld agent benchmark with LOOP, it finds merging matches joint RL on task-goal completion, and analyzes the task-vector geometry that explains when this holds.

**Sources found:** arXiv (cs.AI, July 17 submission)
**Why trending:** Model merging as a cheap substitute for multi-task training is widely assumed but rarely tested against the real baseline; a head-to-head in the RL/agent setting is a genuinely missing experiment.

---

## 10. QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides

**Authors:** Zhengyang Zhuge, Hao Yu, Xin Wang, Zheng Li, Yizhong Cao, Dayiheng Liu, Jianwei Zhang
**arXiv:** [arxiv.org/abs/2607.15810](https://arxiv.org/abs/2607.15810)

QUADS tackles the instability of using the emerging NVFP4 (W4A4 FP4) format to accelerate rollout generation in RL for Mixture-of-Experts LLMs, where naive NVFP4 rollout with BF16 training collapses after ~150 steps due to growing rollout-trainer log-probability gaps. It aligns quantization error across the rollout and training sides to keep low-precision MoE RL stable while retaining FP4 throughput gains.

**Sources found:** arXiv (cs.LG, July 17 submission)
**Why trending:** Low-precision RL rollout for MoE models sits at the intersection of two active efficiency frontiers (FP4/NVFP4 and MoE RL), with a concrete stability fix practitioners can apply.

---

## 11. VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs

**Authors:** Shahrzad Esmat, Dhawal Shah, Ali Jannesari
**arXiv:** [arxiv.org/abs/2607.15498](https://arxiv.org/abs/2607.15498)

VarRate argues that both leading training-free KV-cache families are structurally limited — token eviction (SnapKV, Ada-KV) is irreversible and collapses under query-agnostic reuse, while uniform low-rank coding wastes budget by spending equal rank everywhere. Its fix is to allocate rank rather than evict tokens, giving a variable-rate compression scheme that keeps every token at adaptively chosen precision.

**Sources found:** arXiv (cs.CL, July 16 submission)
**Why trending:** KV-cache memory is the dominant long-context inference bottleneck, and a training-free method that reframes the problem as rank allocation is immediately usable.

---

## 12. Kolmogorov–Arnold Networks for Small Language Models

**Authors:** Felippe Alves, Renato Vicente
**arXiv:** [arxiv.org/abs/2607.15525](https://arxiv.org/abs/2607.15525)

The paper tests Kolmogorov–Arnold Networks (KANs) as an interpretable alternative to transformer feed-forward layers in small LMs, reconstructing all 884,736 feed-forward edges of a 10M-parameter B-spline KAN and finding most edges active while low-activity edges prune away with negligible loss. It separately probes KANs' interpretability claims and their competitiveness with structured MLP pruning, replicating the audit on BabyLM.

**Sources found:** arXiv (cs.LG, July 17 submission)
**Why trending:** KANs remain a polarizing architecture, and a careful edge-level audit applied to actual language modeling (rather than toy tasks) speaks to the community's lingering skepticism.

---

## 13. DSWorld: A Data Science World Model for Efficient Autonomous Agents

**Authors:** Zherui Yang, Fan Liu, Hao Liu
**arXiv:** [arxiv.org/abs/2607.15901](https://arxiv.org/abs/2607.15901)

DSWorld introduces the idea of a Data Science World Model that predicts environment state transitions from the current workflow state and a candidate operation, letting an agent anticipate the effect of a data-science action before actually executing it. This aims to replace the expensive trial-and-error loops that dominate current autonomous data-science agents.

**Sources found:** arXiv (cs.AI, July 17 submission)
**Why trending:** Applies the increasingly popular "world model for agents" idea to the concrete, compute-heavy domain of data-science automation, where avoiding wasted executions has clear payoff.

---

## 14. Process Reward Informed Tree Rollout for Effective Multi-Turn RL

**Authors:** Xintong Li, Sha Li, Yuwei Zhang, Changlong Yu, Rongmei Lin, Hongye Jin, Shuyi Guan, Xin Liu, Linwei Li, Qingyu Yin, Jingbo Shang
**arXiv:** [arxiv.org/abs/2607.15610](https://arxiv.org/abs/2607.15610)

This paper replaces the uniform, independently-sampled full-trajectory rollouts used by GRPO/RLOO with a process-reward-informed tree rollout that organizes an agent's multi-turn trajectory as a tree, treating each turn as a branching decision point. This concentrates rollout budget on promising intermediate states instead of wasting it on uninformative dead-end attempts in long-horizon agentic tasks.

**Sources found:** arXiv (cs.CL, July 17 submission)
**Why trending:** Rollout efficiency is a live pain point in agentic RL, and exploiting the natural tree structure of multi-turn trajectories is an intuitive, directly applicable improvement.

---

## 15. Adaptive Multi-Step Lookahead Decoding for Diffusion Language Models

**Authors:** Yingqian Cui, Wei Deng, Lantao Mei, Hang Li, Charu C. Aggarwal, Hui Liu, Yue Xing
**arXiv:** [arxiv.org/abs/2607.15655](https://arxiv.org/abs/2607.15655)

The authors improve decoding for masked diffusion language models, showing that the common shallow one-step lookahead is suboptimal for longer decoding horizons while a naive fixed-depth deeper lookahead is also ineffective. They propose an adaptive multi-step lookahead scheme that adjusts how far ahead to explore before committing token updates, improving the accuracy–efficiency trade-off.

**Sources found:** arXiv (cs.CL, July 17 submission)
**Why trending:** Diffusion LMs are a fast-moving alternative to autoregressive decoding, and better lookahead decoding directly targets their central accuracy-vs-speed tension.

---

## 16. Induction in Both Directions: A Mechanistic Analysis of In-Context Learning in Masked Diffusion Language Models

**Authors:** Andy Catruna, Emilian Radoi
**arXiv:** [arxiv.org/abs/2607.15893](https://arxiv.org/abs/2607.15893)

This work mechanistically analyzes how masked diffusion language models implement induction — the repeated-context copying circuit behind in-context learning — comparing matched attention-only autoregressive models against absorbing-mask DLMs. It finds DLMs learn a bidirectional induction circuit in which previous-token and next-token heads both contribute, unlike the unidirectional circuit in autoregressive transformers.

**Sources found:** arXiv (cs.CL, July 17 submission)
**Why trending:** Mechanistic interpretability of diffusion LMs is largely unexplored, and showing induction works bidirectionally is a clean, novel structural finding for a rising model family.

---

## 17. More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe

**Authors:** Stefan Maria Ailuro, Mario Markov, Mohammad Mahdi, Luc Van Gool, Danda Pani Paudel
**arXiv:** [arxiv.org/abs/2607.15942](https://arxiv.org/abs/2607.15942)

The paper challenges the assumption that remote-sensing vision-language models need domain-specific encoders, alignment modules, or task-specific fusion, showing a generally capable VLM can reach competitive or state-of-the-art performance on hard Earth-observation benchmarks when trained at sufficient scale. It argues that architectural specialization is often unnecessary for open-ended reasoning over remote-sensing data.

**Sources found:** arXiv (cs.CV, July 17 submission)
**Why trending:** A "simpler recipe beats specialized architectures" result (from Luc Van Gool's group) fits the broader bitter-lesson narrative and is immediately relevant to the growing remote-sensing VLM community.

---

## 18. SlotMem: Character-Addressable Internal Memory for Narrative Long Video Generation

**Authors:** Yilai Liu, Xin Zhang, Shiyuan Zhang, Hongyang Du
**arXiv:** [arxiv.org/abs/2607.15772](https://arxiv.org/abs/2607.15772)

SlotMem introduces a character-addressable internal memory for narrative long-video generation, addressing how existing methods either retrieve memory with cues misaligned to identity preservation or use coarse frame-level KV memory that entangles identity with incidental visual factors. Its slot-based memory keeps recurring character identities consistent across scene transitions and long temporal gaps under a limited memory budget.

**Sources found:** arXiv (cs.CV, July 17 submission)
**Why trending:** Character consistency across long, multi-scene videos is one of the most-cited open problems in video generation, and a dedicated identity-addressable memory is a targeted approach.

---

## 19. SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction

**Authors:** Xue Yu, Bo Yuan, Pengshuai Yang, Kailin Zhao, Hong Hu, Junlan Feng
**arXiv:** [arxiv.org/abs/2607.15550](https://arxiv.org/abs/2607.15550)

SeerGuard is a consequence-aware safety framework for mobile GUI agents that shifts from reactive to proactive risk handling via pre-execution instruction-level screening and action-level risk assessment. By predicting the consequences of a proposed action before execution, it aims to catch the single erroneous taps that can cause irreversible damage on real devices.

**Sources found:** arXiv (cs.AI, July 17 submission)
**Why trending:** GUI/computer-use agents are moving toward real deployment, and pre-execution safety prediction addresses the exact irreversible-action risk that makes practitioners nervous.

---

## 20. Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?

**Authors:** Sergey Rodionov
**arXiv:** [arxiv.org/abs/2607.15439](https://arxiv.org/abs/2607.15439)

This paper runs an ablation over a prior ARC-AGI-3 agent by building four nested Codex-based agents — a textual baseline, a flexible-interface executable world model without replay verification, that model plus scheduled simplification, and a fixed-interface variant requiring exact reproduction of recorded observations — to attribute which idea drove performance. It evaluates all four with gpt-5.4 and gpt-5.5 to isolate the contribution of executable world modeling, simplification, and verification.

**Sources found:** arXiv (cs.AI, July 16 submission)
**Why trending:** ARC-AGI-3 is a marquee reasoning benchmark, and a controlled attribution study over world-modeling/verification components on frontier GPT-5.x models speaks directly to how agents should be built.
