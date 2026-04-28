---
title: "Daily AI Papers — April 28, 2026"
date: 2026-04-28
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-28/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal
  - agentic-ai
  - reinforcement-learning
---

## 1. World-R1: Reinforcing 3D Constraints for Text-to-Video Generation
**Authors:** Weijie Wang, Xiaoxuan He, Youping Gu  
**arXiv:** [arxiv.org/abs/2604.24764](https://arxiv.org/abs/2604.24764)  
**Sources:** HuggingFace, arXiv  
**Why trending:** RL applied to text-to-video generation for geometric consistency is a hot frontier — combines R1-style RL reward shaping with 3D priors without expensive architectural overhauls.

Recent video foundation models suffer from geometric inconsistencies despite impressive synthesis quality. World-R1 proposes a reinforcement learning framework that aligns video generation with 3D constraints by treating geometry as a verifiable reward signal, achieving scalable 3D-consistent world modeling without modifying the base architecture.

---

## 2. ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents
**Authors:** Fanqing Meng, Lingxiao Du, Zijian Wu et al.  
**arXiv:** [arxiv.org/abs/2604.23781](https://arxiv.org/abs/2604.23781)  
**Sources:** HuggingFace, arXiv, emergentmind, claw-mark.com (dedicated site)  
**Why trending:** Dedicated benchmark website + multiple platform presence. Tests agents as persistent coworkers across changing real-world environments — fills a critical gap in agent evaluation.

Existing benchmarks don't capture how agents must operate over multiple working days while environments evolve — new emails arrive, calendar entries shift, knowledge bases update. ClawMark introduces a living-world evaluation framework spanning multi-turn, multi-day, multimodal contexts including images, PDFs, audio, video, and spreadsheets.

---

## 3. Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation
**Authors:** Zhiheng Liu, Weiming Ren, Xiaoke Huang et al.  
**arXiv:** [arxiv.org/abs/2604.24763](https://arxiv.org/abs/2604.24763)  
**Sources:** HuggingFace, arXiv, emergentmind  
**Why trending:** Challenges the foundational assumption that pretrained vision encoders are necessary for multimodal models — native pixel-level unified models are a hot architecture direction.

Unified multimodal models typically rely on pretrained vision encoders and separate visual representations for understanding vs. generation, creating misalignment. Tuna-2 operates directly on pixel embeddings, enabling fully end-to-end optimization from raw pixels for both understanding and generation without architectural separation.

---

## 4. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms
**Authors:** Qi Li, Bo Yin, Weiqi Huang et al.  
**arXiv:** [arxiv.org/abs/2604.23775](https://arxiv.org/abs/2604.23775)  
**Sources:** HuggingFace, arXiv, ICLR 2026 spotlight (agentic robotics & safety)  
**Why trending:** As VLA models become the substrate for embodied robots, safety becomes critical — irreversible physical consequences make this uniquely urgent vs. text-only LLM safety.

VLA models face a new class of safety challenges: irreversible physical consequences, a multimodal attack surface across vision/language/state, real-time latency constraints on defense, and error propagation over long-horizon tasks. This survey maps the threat landscape and proposes evaluation mechanisms specific to embodied intelligence systems.

---

## 5. From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company
**Authors:** Zhengxu Yu, Yu Fu, Zhiyuan He et al.  
**arXiv:** [arxiv.org/abs/2604.22446](https://arxiv.org/abs/2604.22446)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Addresses the missing organizational layer in multi-agent systems — fixed team structures and tightly coupled coordination remain major bottlenecks for production agentic workflows.

Multi-agent systems remain constrained by fixed team structures, tightly coupled coordination logic, and session-bound learning. This work introduces a principled organizational layer modeled after real-world companies, governing how a workforce of heterogeneous agents is assembled, governed, and improved over time.

---

## 6. Zero-to-CAD: Agentic Synthesis of Interpretable CAD Programs at Million-Scale Without Real Data
**Authors:** (from arxiv 2604.24479)  
**arXiv:** [arxiv.org/abs/2604.24479](https://arxiv.org/abs/2604.24479)  
**Sources:** HuggingFace, arXiv, ICLR 2026, paperium  
**Why trending:** ICLR 2026 presence + multi-platform. Generating construction-history CAD programs at scale without real data is a breakthrough for 3D design AI.

CAD models encode design intent as parametric construction histories, but large-scale 3D datasets only contain B-Reps or meshes that strip this procedural information. Zero-to-CAD uses agentic synthesis to generate interpretable CAD programs at million scale without requiring real training data, solving the fundamental data scarcity problem.

---

## 7. SketchVLM: Vision Language Models Can Annotate Images to Explain Thoughts and Guide Users
**Authors:** Brandon Collins, Logan Bolton, Hung Huy Nguyen et al.  
**arXiv:** [arxiv.org/abs/2604.22875](https://arxiv.org/abs/2604.22875)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Humans naturally point and draw to explain reasoning — this gives VLMs the same capability via SVG overlays, making AI explanations verifiable and editable.

Modern VLMs like Gemini-3-Pro and GPT-5 only respond with text, making visual reasoning hard to verify. SketchVLM is a training-free, model-agnostic framework that enables VLMs to produce non-destructive, editable SVG overlays directly on images to annotate and explain their reasoning visually.

---

## 8. Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis
**Authors:** Zhisong Qiu, Shuofei Qiao, Kewei Xu et al.  
**arXiv:** [arxiv.org/abs/2604.24198](https://arxiv.org/abs/2604.24198)  
**Sources:** HuggingFace, arXiv  
**Why trending:** PRMs have conquered math reasoning — applying them to dynamic data analysis agents is a natural and important next frontier for scientific AI.

Process Reward Models have succeeded in augmenting LLM reasoning in static domains like math, but their use in dynamic data analysis tasks is unexplored. This paper reveals that general-domain PRMs fail to supervise data analysis agents and introduces a scientific-process-aware PRM trained to reward sound analytical methodology.

---

## 9. Stabilizing Efficient Reasoning with Step-Level Advantage Selection
**Authors:** Han Wang, Xiaodong Yu, Jialian Wu et al.  
**arXiv:** [arxiv.org/abs/2604.24003](https://arxiv.org/abs/2604.24003)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Efficient reasoning is one of the hottest LLM topics — reducing verbose chain-of-thought without sacrificing accuracy has massive deployment implications.

LLMs achieve strong reasoning by generating long reasoning traces, but efficient reasoning via length-based rewards or pruning often introduces instability. This work proposes step-level advantage selection to stabilize training, enabling reliable efficient reasoning without the instability of existing post-training approaches.

---

## 10. Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining
**Authors:** (from arxiv 2604.16391)  
**arXiv:** [arxiv.org/abs/2604.16391](https://arxiv.org/abs/2604.16391)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Addresses the fundamental 2D/3D misalignment in VLA models and unlocks learning from massive action-free web video — critical for scaling robot foundation models.

VLA models face a dilemma: 2D image forecasting and 3D action prediction are misaligned, and action-entangled training can't leverage large-scale web video data. Disentangled pretraining separates forward dynamics (vision) from inverse dynamics (action prediction), enabling VLAs to learn from action-free video at web scale.

---

## 11. ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning
**Authors:** Yiming Zhang, Jiacheng Chen, Jiaqi Tan et al.  
**arXiv:** [arxiv.org/abs/2604.24300](https://arxiv.org/abs/2604.24300)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Current spatial benchmarks are systematically invalid for modern VLMs — important for the field to have reliable evaluation of 3D reasoning capabilities.

Current spatial intelligence benchmarks derive QA pairs from point-cloud annotations designed for traditional 3D perception, making them systematically invalid when used with video-based VLMs. ReVSI rebuilds the evaluation framework from scratch to provide accurate, artifact-free assessment of VLM spatial reasoning.

---

## 12. How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models
**Authors:** Kristian Schwethelm, Daniel Rueckert, Georgios Kaissis  
**arXiv:** [arxiv.org/abs/2604.21106](https://arxiv.org/abs/2604.21106)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Scaling laws research for novel architectures is always high-value — quantifying recurrence's worth in equivalent parameters informs architectural decisions at scale.

This work measures how much one extra recurrence is worth to a looped (depth-recurrent) language model in equivalent unique parameters. From 116 pretraining runs spanning 50x in training compute, the paper fits a joint scaling law with recurrence count, establishing when looping beats parameter-scaling for language modeling.

---

## 13. Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment
**Authors:** Bobo Li, Rui Wu, Zibo Ji et al.  
**arXiv:** [arxiv.org/abs/2604.19548](https://arxiv.org/abs/2604.19548)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Role-playing in multi-agent frameworks is widely used — finding that it introduces systematic biases (actor-observer asymmetry) has immediate practical implications.

Multi-agent frameworks use specialized roles for self-reflection and mutual auditing, but role-playing introduces actor-observer asymmetry: agents systematically over-attribute errors to situational factors when acting but to disposition when observing others. Dialectical alignment addresses this bias to improve multi-agent reliability.

---

## 14. For-Value: Efficient Forward-Only Data Valuation for Finetuning LLMs and VLMs
**Authors:** Wenlong Deng, Qi Zeng, Jiaming Zhang et al.  
**arXiv:** [arxiv.org/abs/2508.10180](https://arxiv.org/abs/2508.10180)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Gradient-based data valuation is computationally prohibitive for billion-parameter models — forward-only methods unlock transparency and data accountability at scale.

Existing data valuation methods rely on gradient computations, making them infeasible for billion-parameter LLMs and VLMs and precluding batch parallelization. For-Value introduces a forward-only data valuation approach that is efficient, parallelizable, and applicable to production-scale models.

---

## 15. Improving Vision-Language Models with Perception-Centric Process Reward Models
**Authors:** Yingqian Min, Kun Zhou, Yifan Li et al.  
**arXiv:** [arxiv.org/abs/2604.24583](https://arxiv.org/abs/2604.24583)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Applying RLVR (reinforcement learning with verifiable rewards) to VLMs is a major trend — adding fine-grained perception supervision at the process level is a meaningful advance.

RLVR has significantly improved VLM complex reasoning but its outcome-level supervision is too coarse to diagnose and correct reasoning chain errors. Perceval introduces a perception-centric process reward model that provides step-level supervision aligned with visual grounding, improving VLM reasoning accuracy.

---

## 16. Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing
**Authors:** Anastasiia Filippova, David Grangier, Marco Cuturi  
**arXiv:** [arxiv.org/abs/2604.22782](https://arxiv.org/abs/2604.22782)  
**Sources:** HuggingFace, arXiv  
**Why trending:** KV cache memory is a dominant serving cost — adaptive depth-wise sharing is a novel angle on compression that preserves model quality while reducing memory footprint.

KV cache memory significantly impacts transformer serving costs, but existing approaches largely address layer-wise sparsity. Stochastic KV Routing introduces depth-wise adaptive cache sharing, allowing different layers to share KV caches stochastically based on learned routing, reducing memory without uniform compression.

---

## 17. Discovering Agentic Safety Specifications from 1-Bit Danger Signals
**Authors:** Víctor Gallego  
**arXiv:** [arxiv.org/abs/2604.23210](https://arxiv.org/abs/2604.23210)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Aligning agents to safety specs without dense human feedback is a key open problem — learning from binary danger signals is practical and deployable.

EPO-Safe (Experiential Prompt Optimization for Safe Agents) enables an LLM to discover hidden safety objectives through experience alone. The agent iteratively generates action plans, receives sparse binary danger warnings, and evolves a natural language behavioral specification through reflection — no dense reward required.

---

## 18. Efficient Agent Evaluation via Diversity-Guided User Simulation
**Authors:** Itay Nakash, George Kour, Ateret Anaby-Tavor  
**arXiv:** [arxiv.org/abs/2604.21480](https://arxiv.org/abs/2604.21480)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Monte Carlo evaluation of multi-turn agents is computationally expensive — diversity-guided simulation cuts cost while maintaining evaluation fidelity.

Current agent evaluation relies on linear Monte Carlo rollouts across complete conversations, which is computationally inefficient due to repeated regeneration of identical sub-paths. Diversity-guided user simulation intelligently focuses rollouts on underexplored conversation branches, dramatically reducing evaluation compute.

---

## 19. TexOCR: Advancing Document OCR Models for Compilable Page-to-LaTeX Reconstruction
**Authors:** Chengye Wang, Lin Fu, Zexi Kuang et al.  
**arXiv:** [arxiv.org/abs/2604.22880](https://arxiv.org/abs/2604.22880)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Reconstructing scientific PDFs into compilable LaTeX (not just Markdown) is a significant step for AI-assisted scientific publishing pipelines.

Existing document OCR targets plain text or Markdown, discarding the structural and executable properties of LaTeX essential for scientific publishing. TexOCR introduces TexOCR-Bench (benchmark) and TexOCR-Train (large-scale training corpus) for page-level reconstruction of scientific PDFs into compilable LaTeX.

---

## 20. Quantum Kernel Advantage over Classical Collapse in Medical Foundation Model Embeddings
**Authors:** (from arxiv 2604.24597)  
**arXiv:** [arxiv.org/abs/2604.24597](https://arxiv.org/abs/2604.24597)  
**Sources:** HuggingFace, arXiv  
**Why trending:** Evidence of practical quantum advantage over classical methods — even in simulation — using production medical foundation model embeddings is a notable result.

This paper provides evidence of quantum kernel advantage under noiseless simulation in binary insurance classification on MIMIC-CXR chest radiographs, using quantum SVMs with frozen embeddings from medical foundation models (MedSigLIP-448, RAD-DINO, ViT-patch32). A two-tier fair comparison framework ensures rigorous classical vs. quantum benchmarking.

---

*Generated: 2026-04-28 | Sources: HuggingFace Daily Papers, arXiv, emergentmind, Papers With Code, ICLR 2026, Reddit r/ML, Hacker News*
