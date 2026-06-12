---
title: "Daily AI Papers — June 12, 2026"
date: 2026-06-12
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-12/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - sparse-attention
  - agentic-systems
  - multimodal-models
---

## 1. MiniMax Sparse Attention

**Authors:** Xunhao Lai, Weiqi Xu, Yufeng Yang, Qiaorui Chen et al. (MiniMax)  
**arXiv:** [arxiv.org/abs/2606.13392](https://arxiv.org/abs/2606.13392)

Ultra-long context (100K–1M tokens) is increasingly required for agentic workflows and repository-scale reasoning, but softmax attention's quadratic cost makes this intractable at deployment scale. MiniMax Sparse Attention (MSA) introduces a blockwise sparse attention mechanism that achieves near-full-attention quality while reducing computation to nearly linear, enabling MiniMax's frontier models to serve million-token contexts efficiently.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** From a frontier lab (MiniMax), directly addresses the long-context scaling wall — practical breakthrough with immediate production relevance.

---

## 2. MaxProof: Scaling Mathematical Proof with Generative-Verifier RL and Population-Level Test-Time Scaling

**Authors:** Jiacheng Chen, Xinyu Zhang, Shunkai Zhang, Yanmohan Wang et al. (MiniMax)  
**arXiv:** [arxiv.org/abs/2606.13473](https://arxiv.org/abs/2606.13473)

MaxProof trains three proof-oriented capabilities — generation, verification, and critique-conditioned repair — using a defense-in-depth generative verifier engineered for low false-positive rate, then merges them into a single model. At test time, population-level scaling runs diverse proof candidates in parallel and selects via the verifier, achieving competition-level mathematical proof in the MiniMax-M3 series.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Part of MiniMax's M3 release; combines RL, verification, and novel test-time scaling for formal math — directly competes with DeepSeek-Prover and Lean4 workflows.

---

## 3. EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments

**Authors:** Jundong Xu, Qingchuan Li, Jiaying Wu, Yihuai Lan  
**arXiv:** [arxiv.org/abs/2606.13681](https://arxiv.org/abs/2606.13681)

Nearly all LLM agent benchmarks assume static environments, but real deployments require agents to continuously update their knowledge, skills, and behavior as conditions change. EvoArena is a new benchmark that tracks memory evolution across dynamically shifting tasks, stress-testing whether agents can detect change, update correctly, and avoid stale-knowledge errors.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Fills a critical gap in agent evaluation; dynamic-environment robustness is a known blind spot of current SOTA agents.

---

## 4. SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning

**Authors:** Seokju Cho, Ryo Hachiuma, Abhishek Badki, Hang Su  
**arXiv:** [arxiv.org/abs/2606.13673](https://arxiv.org/abs/2606.13673)

Tool-augmented VLMs for spatial reasoning are bottlenecked not by the perception modules themselves but by the action interface through which tools are invoked. SpatialClaw redesigns this interface to enable richer, more expressive tool invocations, yielding substantial gains on 3D object localization, relation understanding, and motion prediction tasks.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Novel angle on VLM+tool-use — shifts focus from model capacity to interface design, with strong empirical results.

---

## 5. EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery

**Authors:** Amy Xin, Jiening Siow, Junjie Wang, Zijun Yao  
**arXiv:** [arxiv.org/abs/2606.13662](https://arxiv.org/abs/2606.13662)

As LLM capabilities improve, the bottleneck for autonomous scientific discovery is shifting from model intelligence to environment quality — how well the execution environment supports hypothesis testing, validation, and iteration. EurekAgent formalizes "agent environment engineering" and demonstrates that well-engineered environments unlock discovery performance that surpasses human-designed approaches.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Provocative thesis that environment design > model capability for AI science; directly relevant to lab automation and AI-for-science initiatives.

---

## 6. InterleaveThinker: Reinforcing Agentic Interleaved Generation

**Authors:** Dian Zheng, Harry Lee, Manyuan Zhang, Kaituo Feng  
**arXiv:** [arxiv.org/abs/2606.13679](https://arxiv.org/abs/2606.13679)

Current unified multimodal models (UMMs) are constrained to single-image generation/editing and cannot produce interleaved text-image sequences — a crucial capability for visual narratives, step-by-step guidance, and embodied manipulation. InterleaveThinker applies reinforcement learning to explicitly train interleaved generation, achieving strong results even on open-source UMMs that previously lacked this capability.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Unlocks a missing capability in open UMMs; interleaved generation is the next frontier for multimodal models beyond GPT-4o.

---

## 7. FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents

**Authors:** Jia Deng, Yimeng Chen, Xiaoqing Xiang, Ziyang Zeng  
**arXiv:** [arxiv.org/abs/2606.12087](https://arxiv.org/abs/2606.12087)

Existing deep search training datasets suffer from "shortcut collapse" — questions that appear hard based on graph structure can be answered via cheaper identifying routes, so agents never learn to actually search. FORT-Searcher formalizes shortcut awareness and synthesizes tasks specifically designed to resist these shortcuts, forcing genuine multi-step retrieval and reasoning.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Addresses a fundamental data quality problem in training search agents; directly improves the robustness of agentic web browsing systems.

---

## 8. LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories

**Authors:** Baochang Ren, Xinjie Liu, Xi Chen, Yanshuo Liu  
**arXiv:** [arxiv.org/abs/2606.13578](https://arxiv.org/abs/2606.13578)

While AI can read literature, generate hypotheses, and plan protocols, the physical execution of lab procedures still requires human operators. LabVLA adapts Vision-Language-Action models specifically to scientific laboratory settings, bridging the gap between AI reasoning and physical bench-work through domain-specific grounding and action primitives.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Lab automation is a billion-dollar bet by pharma/biotech; VLA models entering the wetlab is a meaningful milestone.

---

## 9. HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers

**Authors:** Guozhen Zhang, Xuerui Qiu, Yutao Cui, Tianhui Song  
**arXiv:** [arxiv.org/abs/2606.13289](https://arxiv.org/abs/2606.13289)

HYDRA-X is the first unified multimodal model to handle image and video tokenization within a single Vision Transformer, eliminating the need for modality-specific encoders. This "holistic" tokenizer provides a shared representation space that improves both understanding and generation tasks across images and video simultaneously.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Architectural contribution to UMMs — a single ViT for all visual modalities is cleaner and more scalable than the current patchwork of encoders.

---

## 10. WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces

**Authors:** Wanli Li, Bowen Zhou, Yunyao Yu, Zhou Xu  
**arXiv:** [arxiv.org/abs/2606.09426](https://arxiv.org/abs/2606.09426)

Computer-use agents increasingly operate across GUI, CLI, code editors, browsers, and external tools, yet existing benchmarks treat these interfaces as separable. WeaveBench provides 114 long-horizon tasks across 8 real-world work domains requiring sustained cross-interface orchestration, exposing gaps in agents that perform well on single-interface benchmarks.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Timely as Anthropic's Claude, OpenAI's Operator, and similar systems push into computer use; this benchmark directly measures their weakest link.

---

## 11. Demystifying Hidden-State Recurrence: Switchable Latent Reasoning with On-Policy Reinforcement Learning

**Authors:** Jiayu Yang, Chao Chen, Shengen Wu, Yinhong Liu  
**arXiv:** [arxiv.org/abs/2606.13106](https://arxiv.org/abs/2606.13106)

Latent chain-of-thought (replacing visible reasoning tokens with continuous hidden-state recurrence) is theoretically compelling but hard to optimize with standard on-policy RL and difficult to interpret. This paper shows that a single pair of explicit boundary tokens (entry/exit anchors) makes latent blocks compatible with on-policy RL and causally interpretable, unlocking switchable reasoning that can be toggled between latent and explicit modes.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Latent reasoning is a hot research direction (efficiency without CoT verbosity); making it compatible with GRPO/PPO is a practical unlock.

---

## 12. N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization

**Authors:** Xukun Zhu, Hang Yu, Peng Di, Linchao Zhu  
**arXiv:** [arxiv.org/abs/2606.10768](https://arxiv.org/abs/2606.10768)

GRPO-style policy optimization for LLM math reasoning suffers from redundant rollouts — token-level sampling generates paraphrases, not genuinely diverse solutions. N-GRPO mixes trajectory embeddings at the embedding level with semantically neighboring examples, producing richer, more diverse rollouts without disrupting semantic consistency, improving math benchmark performance.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** GRPO variants for math reasoning are the dominant approach post-DeepSeek-R1; any improvement to rollout diversity has broad applicability.

---

## 13. TreeSeeker: Tree-Structured Trial, Error, and Return in Deep Search

**Authors:** Zhuofan Shi, Mingzhe Ma, Lu Wang, Fangkai Yang  
**arXiv:** [arxiv.org/abs/2606.11662](https://arxiv.org/abs/2606.11662)

Deep search agents face a dilemma: greedy best-first search extends weak paths, while undirected exploration wastes budget. TreeSeeker organizes the search process as a tree with structured backtracking — agents can commit to a path, detect dead-ends, and return to promising branches, mimicking human systematic search behavior.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Principled search structure for LLM agents; complements FORT-Searcher (training) by improving inference-time search strategy.

---

## 14. VIA-SD: Verification via Intra-Model Routing for Speculative Decoding

**Authors:** Yuchen Xian, Yang He, Yunqiu Xu, Yi Yang  
**arXiv:** [arxiv.org/abs/2606.12243](https://arxiv.org/abs/2606.12243)

Standard speculative decoding uses binary accept/reject decisions — any rejected draft token triggers full recomputation. VIA-SD observes that many rejected tokens are only marginally wrong and routes them through a lightweight intra-model verifier path rather than full recomputation, substantially reducing latency while maintaining output quality.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Speculative decoding is now standard in production LLM inference; a drop-in latency improvement with no quality cost is immediately deployable.

---

## 15. MoVerse: Real-Time Video World Modeling with Panoramic Gaussian Scaffold

**Authors:** Yang Zhou, Ziheng Wang, Yuqin Lu, Haofeng Liu  
**arXiv:** [arxiv.org/abs/2606.13376](https://arxiv.org/abs/2606.13376)

MoVerse creates a fully interactively navigable 3D world from a single narrow-FOV image in real time by scaffolding a video world model on Panoramic Gaussians, allowing free-roam exploration of environments that extend far beyond the initial observation. The system runs fast enough for interactive use, unlike prior diffusion-based world models.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Real-time interactive world models are a key capability for robotics simulation and gaming; the single-image input makes it practically accessible.

---

## 16. VideoMDM: Towards 3D Human Motion Generation From 2D Supervision

**Authors:** Amir Mann, Gal Michael Harari, Merav Keidar, Or Litany  
**arXiv:** [arxiv.org/abs/2606.13364](https://arxiv.org/abs/2606.13364)

Obtaining 3D motion capture data is expensive and scarce, limiting motion diffusion models. VideoMDM uses a pretrained 2D-to-3D lifter to generate noisy 3D pseudo-labels from monocular video poses, then trains a diffusion model to denoise them — effectively learning 3D motion priors without any 3D ground truth.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Weak supervision for 3D motion from abundant 2D video is a major data bottleneck solution; has direct applications in animation, robotics, and gaming.

---

## 17. Robust-U1: Can MLLMs Self-Recover Corrupted Visual Content for Robust Understanding?

**Authors:** Jiaqi Tang, Jianmin Chen, Youyang Zhai, Wei Wei  
**arXiv:** [arxiv.org/abs/2606.08063](https://arxiv.org/abs/2606.08063)

Real-world visual corruptions (blur, noise, compression artifacts) significantly degrade MLLM performance, and existing fixes either lack interpretability or can't restore pixel-level detail. Robust-U1 asks whether MLLMs can self-recover corrupted inputs before understanding them, using internal generation capabilities to reconstruct clean visual content as an intermediate step.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Self-healing perception is a novel framing; unified models (that both generate and understand) make this newly feasible.

---

## 18. HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness

**Authors:** Xiaoxuan Wang, Haixin Wang, Alexander Taylor, Jason Cong  
**arXiv:** [arxiv.org/abs/2606.12882](https://arxiv.org/abs/2606.12882)

Agent performance is shaped not just by model capability and environment design, but also by the harness mediating agent-environment interaction — yet harnesses are almost universally hand-engineered. HarnessBridge learns a bidirectional controller that adapts the harness to both the agent's generation style and the environment's feedback, improving long-horizon task success rates.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Infrastructure-level contribution to agentic AI; learnable harnesses could compound improvements from better models and environments simultaneously.

---

## 19. EvoBrowseComp: Benchmarking Search Agents on Evolving Knowledge

**Authors:** Yunhan Wang, Jiaan Wang, Lianzhe Huang, Xianfeng Zeng  
**arXiv:** [arxiv.org/abs/2606.13120](https://arxiv.org/abs/2606.13120)

Static benchmarks like BrowseComp are vulnerable to test-set contamination — models can score well through parametric memorization rather than genuine retrieval. EvoBrowseComp continuously updates its questions to reflect evolving world knowledge, ensuring that high scores require real-time search and reasoning rather than recall.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Anti-contamination benchmark design is increasingly critical as web crawl training data and benchmarks overlap; directly relevant for evaluating production search agents.

---

## 20. Risk Under Pressure: Compute-Aware Evaluation of Adversarial Robustness in Language Models

**Authors:** Malikeh Ehghaghi, Boglárka Ecsedi, Marsha Chechik, Colin Raffel  
**arXiv:** [arxiv.org/abs/2606.11409](https://arxiv.org/abs/2606.11409)

Standard adversarial robustness evaluations report attack success rate (ASR) at a fixed query budget, ignoring that different attack strategies vary in compute cost by orders of magnitude. This paper introduces compute-aware robustness metrics that normalize ASR by attack cost, revealing that current rankings of model robustness can be significantly misleading.

**Sources:** HuggingFace Daily Papers, arXiv  
**Why trending:** Safety-critical reframing of jailbreak evaluation methodology; Colin Raffel co-authorship adds visibility; directly challenges how robustness claims are made.
