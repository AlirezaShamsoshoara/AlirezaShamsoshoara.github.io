---
title: "Daily AI Papers — July 25, 2026"
date: 2026-07-25
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-25/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-rl
  - inference-efficiency
  - ai-security
---

## 1. NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs

**Authors:** Jiarong Zhao, Zhikai Lei, Zhiheng Xi, Rui Zheng, Hang Yan, Jie Zhou, Qin Chen, Liang He

**Summary:** Introduces a requirement-driven framework that synthesizes diverse, executable agent training tasks (terminal and office) directly from high-level capability requirements, avoiding the substrate bias of tool/repo-bound task generation pipelines. Scaling to 43.2K synthesized tasks lifts Qwen3.5-35B-A3B to 75.3% on Terminal-Bench 2.1 and 1585 Elo on GDPval, matching or beating several frontier proprietary systems.

**arXiv:** [arxiv.org/abs/2607.14186](https://arxiv.org/abs/2607.14186)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 15 upvotes — a scalable recipe for open agent post-training data that closes the gap with frontier proprietary agents.

---

## 2. Can Multimodal Large Language Models Understand OCT?

**Authors:** Baochen Fu, Wenzhi Deng, Baihao Jin, Yang Li, Zihan Nie, Kailin Jiang, Yuntao Du, Weiye Song

**Summary:** Introduces OCT-Bench, a 10,076-question benchmark spanning perception, cognition, and reasoning over optical coherence tomography retinal images, evaluating 20 MLLMs including proprietary, open-source, and medical-domain models. Finds current models fall well short of reliable OCT understanding, and neither medical fine-tuning nor scale reliably fixes the gap.

**arXiv:** [arxiv.org/abs/2607.16609](https://arxiv.org/abs/2607.16609)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 8 upvotes — a rigorous clinical-imaging benchmark exposing a real capability gap in medical MLLMs.

---

## 3. Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents

**Authors:** Paul Kassianik, Blaine Nelson, Yaron Singer

**Summary:** Argues security-agent benchmarks should measure economic efficiency, not just peak success, evaluating LLM agents on offensive Cybench challenges and defensive Splunk BOTS investigations at fixed cost levels. Finds offensive CTF performance scales cleanly with test-time compute while defensive SOC investigation depends more on disciplined tool use than raw reasoning budget.

**arXiv:** [arxiv.org/abs/2607.15263](https://arxiv.org/abs/2607.15263)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 8 upvotes — cost-aware framing is an increasingly practical lens for real-world security agent deployment.

---

## 4. Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL

**Authors:** Darshan Deshpande

**Summary:** Formalizes text-based world modeling as a steerable transition-dynamics problem and shows masked diffusion LMs, via bidirectional anchor-aware denoising, beat autoregressive world models over 4x their size on coherence and rollout diversity at comparable latency. A GRPO training framework built on these world models achieves up to 47% absolute zero-shot transfer gains across ScienceWorld, ALFWorld, and AppWorld.

**arXiv:** [arxiv.org/abs/2607.16204](https://arxiv.org/abs/2607.16204)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 7 upvotes — diffusion LMs as world models for agentic RL environments is a fresh angle on scaling training diversity.

---

## 5. Nonuniformity Principle in Human-AI Coworking

**Authors:** An Luo, Jie Ding

**Summary:** Studies where to place human oversight checkpoints in long AI agent workflows, formalizing the tradeoff between oversight cost and output quality/rework. Derives a "nonuniformity principle" — optimal schedules place oversight stages with non-decreasing gaps along the workflow — validated empirically on literature-review and website-building agent tasks.

**arXiv:** [arxiv.org/abs/2607.16530](https://arxiv.org/abs/2607.16530)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 6 upvotes — a rare theoretical treatment of human-in-the-loop scheduling for agentic workflows.

---

## 6. DiFA: Inference-Time Forward-Process Alignment for Diffusion Models

**Authors:** Shigui Li, Delu Zeng

**Summary:** Reframes diffusion-model inference as sequential state estimation rather than pure numerical integration, using a Kalman-filter-inspired temporal consensus over past denoising predictions plus a deviation-guidance mechanism to avoid over-smoothing. Training-free and yields significant FID/IS/FD-DINOv2 gains on CIFAR-10 and ImageNet.

**arXiv:** [arxiv.org/abs/2607.17972](https://arxiv.org/abs/2607.17972)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 6 upvotes — a training-free inference upgrade for diffusion generation with clear quantitative gains.

---

## 7. FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications

**Authors:** Krish Agarwal, Zhuoming Chen, Yanyuan Qin, Zhenyu Gu, Atri Rudra, Beidi Chen

**Summary:** Presents an agent harness that lifts simple reference implementations of real-time multimodal pipelines (voice agents, video world models) into optimized multi-GPU deployments via a chain-of-program transformation and measurement-gated optimization loop. Delivers up to ~70x latency reduction and 3.6x throughput improvement on NVIDIA B200/AMD MI355X GPUs, including a 65% latency cut versus expert-tuned vLLM-Omni.

**arXiv:** [arxiv.org/abs/2607.18171](https://arxiv.org/abs/2607.18171)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 6 upvotes — agent-driven systems optimization beating hand-tuned expert deployments is directly relevant to inference-serving work.

---

## 8. SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcement Learning

**Authors:** Mingyuan Wu, Jingcheng Yang, Shengyi Qian, Xudong Wang, Jize Jiang, Qifan Wang, et al.

**Summary:** Introduces a multi-turn RL framework where a VLM issues its own binary self-verdict on proposed answers, triggering a second-chance rethink on "No" before finalizing for outcome-based reward, with no external critics needed. Built on GRPO with asynchronous multi-turn rollouts, it substantially beats standard GRPO baselines on vision-language reasoning benchmarks.

**arXiv:** [arxiv.org/abs/2607.10966](https://arxiv.org/abs/2607.10966)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 5 upvotes — self-verification as a training signal is a growing thread in multimodal reasoning RL.

---

## 9. Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?

**Authors:** Yimeng Chen, Nathanaël Denis, Roberto Di Pietro, Jürgen Schmidhuber

**Summary:** Defines "self-state attacks" — compromising a self-hosted AI agent by corrupting its own memory/config files via legitimate OS calls — and characterizes a four-axis attack space with 43 concrete operations tested against live agent traces. Finds a layered OS defense stack handles most attack cells, but a structurally indistinguishable residual attack surface remains at the OS level.

**arXiv:** [arxiv.org/abs/2607.17986](https://arxiv.org/abs/2607.17986)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 5 upvotes — co-authored by Jürgen Schmidhuber, tackling a novel OS-level security threat model for self-hosted agents.

---

## 10. WorldCupArena: Fine-Grained Evaluation of Language Models and Deep-Research Agents on Football Forecasting

**Authors:** Zhaokai Wang, Tianlin Gui, Jiayuan Rao, Shangzhe Di, Yihong Tang, Dingli Liang

**Summary:** Builds a dynamic, non-contaminable benchmark using the 2026 FIFA World Cup where models must forecast match results, scorelines, players, and events using either provided evidence or live search before kickoff. Across 104 matches and 13 systems, the best models only modestly beat betting-market and human-fan baselines on exact outcomes but show a clearer edge on nuanced scoreline prediction.

**arXiv:** [arxiv.org/abs/2607.18084](https://arxiv.org/abs/2607.18084)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 5 upvotes — a timely, contamination-resistant forecasting benchmark tied to a live global event.

---

## 11. ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders

**Authors:** Zhongyuan Peng, Dan Huang, Chuyu Zhang, Caijun Xu, Changyi Xiao, Shibo Hong, David Lo, Lin Qiu, Xuezhi Cao, Jiyuan He, Yixin Cao

**Summary:** Targets the "vibe-coding" shift by benchmarking coding agents on interactive project building from fuzzy requirements rather than fully specified tasks, using an automated User Agent grounded in real open-source repos to reveal hidden constraints. Evaluates agents with standardized black-box tests plus multi-dimensional diagnostics covering functional correctness, API/structural fidelity, and design quality.

**arXiv:** [arxiv.org/abs/2607.21217](https://arxiv.org/abs/2607.21217)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 5 upvotes — addresses a real gap as coding-agent evaluation shifts from static specs to interactive requirement discovery.

---

## 12. OpenForgeRL: Train Harness-native Agents in Any Environment

**Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao

**Summary:** Presents an open-source framework enabling end-to-end RL training of agents inside real inference harnesses (Claude Code, Codex, OpenClaw-style stacks) via a lightweight proxy that records harness model calls as RL training data, plus a Kubernetes orchestrator for scalable per-rollout containers. Using only hundreds to thousands of tasks, the resulting agents outperform similarly-sized open baselines on ClawEval, OSWorld-Verified, Online-Mind2Web, and WebVoyager.

**arXiv:** [arxiv.org/abs/2607.21557](https://arxiv.org/abs/2607.21557)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** 5 upvotes — directly tackles the hard problem of training agents in the actual complex harnesses they're deployed in.

---

## 13. JoyNexus: Service-Oriented Multi-Tenant Post-Training for VLA Models

**Authors:** Haoran Sun, Wentao Zhang, Junyang Hua, Hedan Yang, Yongjian Guo, Yifei Zhang, et al.

**Summary:** Proposes a multi-tenant compute service for Vision-Language-Action model post-training that decouples training, inference, and environment simulation into shared APIs with tenant-isolated state, replacing exclusive single-tenant GPU allocation. Introduces group batching across heterogeneous VLA data schemas, reducing aggregate GPU time versus isolated single-tenant execution.

**arXiv:** [arxiv.org/abs/2607.16074](https://arxiv.org/abs/2607.16074)
**Found on:** HuggingFace Trending/Weekly
**Why trending:** Featured on HF's weekly board — infrastructure for shared, efficient robotics/VLA post-training at scale.

---

## 14. Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context

**Authors:** Alagappan Valliappan

**Summary:** Identifies that built-in Multi-Token-Prediction draft heads for speculative decoding run full attention over the entire KV cache at every draft step, so cost grows linearly with context and can make speculation net-negative at million-token scale. Applies a StreamingLLM-style sliding window to the draft's attention only (verification stays full-attention and lossless), cutting per-decode-step cost 28–44% at 1M context across Qwen GDN-MoE and Mamba2-hybrid architectures on SGLang.

**arXiv:** [arxiv.org/abs/2607.21535](https://arxiv.org/abs/2607.21535)
**Found on:** arXiv cs.LG (recent)
**Why trending:** Ranked for topical significance (weekend, no engagement signal available) — a lossless, training-free fix for a real bottleneck in long-context speculative decoding.

---

## 15. Error Certificates for KV-Cache Eviction via Randomized Design

**Authors:** Peng Xie

**Summary:** Proves deterministic top-k KV-cache eviction cannot self-certify its own error, since evicted values can be adversarially altered without changing what the serving system retains. Shows Poisson-sampled randomized eviction restores identifiability, yielding a per-step error certificate with 0.97 empirical coverage that separates cache-induced from inherent model failures better than output confidence.

**arXiv:** [arxiv.org/abs/2607.21475](https://arxiv.org/abs/2607.21475)
**Found on:** arXiv cs.LG (recent)
**Why trending:** Ranked for topical significance — a theoretically grounded critique of standard KV-cache eviction with a practical fix for serving-time reliability.

---

## 16. Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence

**Authors:** Jay Gor, Karm Dave, Akshita Abrol, Rajesh Gupta, Sudeep Tanwar, Zhengkui Wang

**Summary:** A survey arguing visual token compression, MoE routing, KV-cache policy, and low-bit quantization for multimodal LLMs cannot be optimized independently — each interacts with and constrains the others under edge hardware limits. Introduces Temporal Routing Consistency as a diagnostic for video MoE models and maps open research directions in routing-aware compression and cross-modal cache management.

**arXiv:** [arxiv.org/abs/2607.20981](https://arxiv.org/abs/2607.20981)
**Found on:** arXiv cs.AI (recent)
**Why trending:** Ranked for topical significance — a timely systems-level synthesis of efficiency techniques for multimodal edge deployment.

---

## 17. Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems

**Authors:** Gaurav Dadhich

**Summary:** Argues production agent failures stem from unmanaged reasoning context rather than reasoning ability, reframing context/memory handling as a lifecycle problem (deciding what to remember, structuring, consolidating, forgetting, compacting) rather than pure storage-and-retrieval. A reference implementation reports 92% on LongMemEval and 93.2% on LoCoMo with linear rather than quadratic token cost growth.

**arXiv:** [arxiv.org/abs/2607.21503](https://arxiv.org/abs/2607.21503)
**Found on:** arXiv cs.AI (recent)
**Why trending:** Ranked for topical significance — agent memory/context cost is one of the most cited pain points in production agent deployments.

---

## 18. Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs

**Authors:** Yidu Wu, Xiang Wang, Kejie Zhao, Zhangchi Wang, Qinghai Guo, Xiaoying Tang

**Summary:** Converts off-the-shelf pre-trained LLMs into depth-sparse models without full retraining, using cosine similarity between each layer's input/output hidden states to assign layer-wise token retention ratios and a lightweight per-layer token router. Substantially reduces inference FLOPs on GPT-NeoX and Qwen2.5 while degrading accuracy less than MoD, D-LLM, and DLO baselines at comparable sparsity.

**arXiv:** [arxiv.org/abs/2607.21291](https://arxiv.org/abs/2607.21291)
**Found on:** arXiv cs.CL (recent)
**Why trending:** Ranked for topical significance — a retraining-free path to cheaper inference on existing pre-trained checkpoints.

---

## 19. Progressive Cramming: Reliable Token Compression and What It Reveals

**Authors:** Dmitrii Tarasov, Timofei Lashukov, Elizaveta Goncharova, Andrey Kuznetsov

**Summary:** Studies "token cramming" (compressing sequences into learned embeddings) by progressively growing the compressed prefix until reconstruction fails within a fixed optimization budget, revealing that near-perfect reconstruction is achievable through brittle steering rather than transferable semantics. Crammed embeddings still cause accuracy drops on downstream tasks even with the original prefix present, tracing the degradation to early-layer attention interactions.

**arXiv:** [arxiv.org/abs/2607.21231](https://arxiv.org/abs/2607.21231)
**Found on:** arXiv cs.CL (recent)
**Why trending:** Ranked for topical significance — a sobering, mechanistically-grounded look at the actual limits of context/token compression.

---

## 20. Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs

**Authors:** Muyang Du, Shuang Yu, Junjie Lai

**Summary:** Accelerates all neural components of the IndexTTS-2 autoregressive TTS model using NVIDIA TensorRT/TensorRT-LLM, adding streaming synthesis and batched inference for production deployment. Achieves up to 5.0x speedup on the autoregressive GPT stage and 3.6x end-to-end on the Seed-TTS benchmark with minimal quality degradation.

**arXiv:** [arxiv.org/abs/2607.21042](https://arxiv.org/abs/2607.21042)
**Found on:** arXiv cs.AI (recent)
**Why trending:** Ranked for topical significance — a concrete, practical GPU-acceleration recipe for real-time TTS deployment.
