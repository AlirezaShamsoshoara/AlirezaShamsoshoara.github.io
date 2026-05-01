---
title: "Daily AI Papers — May 01, 2026"
date: 2026-05-01
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-01/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multi-agent-systems
  - visual-generation
  - llm-efficiency
---

## 1. Eywa: Heterogeneous Scientific Foundation Model Collaboration
**Authors:** Zihao Li, Jiaru Zou, Feihao Fang, Xuying Ning, Mengting Ai, Tianxin Wei, Sirui Chen, Xiyuan Yang, Jingrui He (UIUC)
**arXiv:** [arxiv.org/abs/2604.27351](https://arxiv.org/abs/2604.27351)
**Sources:** HuggingFace Daily Papers (172 upvotes), GitHub
**Why Trending:** Highest-upvoted paper on HuggingFace today by a wide margin; introduces a drop-in multi-agent framework enabling LLMs to collaborate with non-language scientific foundation models (e.g., biology, physics, social science). The GitHub repo and project page went live simultaneously.

Eywa is a heterogeneous agentic framework that bridges language-centric LLM systems with domain-specific scientific foundation models (e.g., protein structure predictors, climate simulators) via language-model-based reasoning interfaces. It operates as a drop-in single-agent replacement (EywaAgent), integrates into multi-agent systems (EywaMAS), or uses a planning-based orchestrator (EywaOrchestra) that dynamically routes tasks to the right specialist model across physical, life, and social science domains.

---

## 2. Visual Generation in the New Era: From Atomic Mapping to Agentic World Modeling
**Authors:** Keming Wu, Zuhao Yang, Kaichen Zhang, Shizun Wang, Haowei Zhu, Sicong Leng, Zhongyu Yang, Qijie Wang et al.
**arXiv:** [arxiv.org/abs/2604.28185](https://arxiv.org/abs/2604.28185)
**Sources:** HuggingFace Daily Papers (68 upvotes)
**Why Trending:** Comprehensive survey arguing that visual generation must evolve from photorealism toward causal, spatially-aware "world modeling"; positions the field's next frontier clearly and attracted strong discussion.

This survey catalogues major recent advances in visual generation — photorealism, typography, instruction-following, interactive editing — and argues that persistent state, spatial reasoning, long-horizon consistency, and causal understanding remain unsolved. It proposes a taxonomy from atomic pixel/token mapping through semantic understanding to agentic world modeling, charting a research roadmap for intelligent visual generation systems.

---

## 3. Nemotron 3 Nano Omni: Efficient and Open Multimodal Intelligence
**Authors:** NVIDIA Research — Amala Sanjay Deshmukh, Kateryna Chumachenko, Tuomas Rintamaki, Matthieu Le, Tyler Poon, Danial Mohseni Taheri, Ilia Karmanov, Guilin Liu et al.
**arXiv:** [arxiv.org/abs/2604.24954](https://arxiv.org/abs/2604.24954)
**Sources:** NVIDIA Developer Blog, arxiv, Reddit/LocalLLaMA, Hacker News
**Why Trending:** NVIDIA's first open multimodal model natively supporting audio + text + image + video in a single efficient model; immediately drew community benchmarking and deployment attempts on consumer hardware.

Nemotron 3 Nano Omni is NVIDIA's latest in the Nemotron series, the first to natively support audio inputs alongside text, images, and video. It delivers accuracy improvements over Nemotron Nano V2 VL across all modalities via architecture advances and improved training recipes, achieving leading results on real-world document understanding, long audio-video comprehension, and agentic tasks — all at an efficient parameter count targeting on-device deployment.

---

## 4. TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate
**Authors:** Amir Zandieh, Majid Daliri, Majid Hadian, Vahab Mirrokni (Google Research)
**arXiv:** [arxiv.org/abs/2504.19874](https://arxiv.org/abs/2504.19874)
**Sources:** Google Research Blog, arxiv, Hacker News
**Why Trending:** Google Research published a blog post this week showcasing TurboQuant enabling ~6x KV-cache memory reduction for LLM inference; the practical implication for inference efficiency generated significant HN and ML community interest.

TurboQuant addresses vector quantization for high-dimensional Euclidean vectors with near-optimal distortion rates for both MSE and inner product objectives. The data-oblivious online algorithms are particularly suited for KV-cache compression in LLM inference, achieving near-optimal distortion within a small constant factor while being computationally lightweight enough for real-time application — enabling dramatic memory savings without quality degradation.

---

## 5. Co-Evolving Policy Distillation
**Authors:** Naibin Gu, Chenxu Yang, Qingyi Si, Chuanyu Qin et al.
**arXiv:** [arxiv.org/abs/2604.27083](https://arxiv.org/abs/2604.27083)
**Sources:** HuggingFace Daily Papers (33 upvotes)
**Why Trending:** Provides a principled unified analysis of RLVR vs. Online Policy Distillation for consolidating multiple expert capabilities — directly relevant to post-training workflows that every major lab is currently running.

This paper offers a unified framework comparing RLVR and OPD post-training paradigms for merging multiple expert capabilities into one model. It identifies that mixed RLVR suffers from inter-capability divergence cost while sequential OPD-after-experts fails to preserve all capabilities. Co-Evolving Policy Distillation (CEPD) is proposed as a solution that jointly evolves teacher and student policies to avoid both failure modes, improving multi-capability consolidation.

---

## 6. ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control
**Authors:** Yanghao Zhou, Jingyu Ma, Yibo Peng, Zhenguo Sun et al.
**arXiv:** [arxiv.org/abs/2604.27711](https://arxiv.org/abs/2604.27711)
**Sources:** HuggingFace Daily Papers (30 upvotes)
**Why Trending:** Connects video diffusion with humanoid robotics in a novel exocentric framing; directly relevant to the robotics-meets-generative-AI trend that's been building since the humanoid boom.

ExoActor reframes humanoid control as a video generation problem from an exocentric (third-person) perspective, capturing spatial context, temporal dynamics, robot actions, and task intent jointly. Rather than relying on conventional control pipelines, the model learns fluent interaction-rich behavior from video priors, enabling generalization to novel environments and object interactions without task-specific engineering.

---

## 7. RoundPipe: Efficient LLM Training on Multiple Consumer GPUs
**Authors:** Yibin Luo, Shiwei Gao, Huichuan Zheng, Youyou Lu et al.
**arXiv:** [arxiv.org/abs/2604.27085](https://arxiv.org/abs/2604.27085)
**Sources:** HuggingFace Daily Papers (21 upvotes)
**Why Trending:** Directly addresses fine-tuning LLMs on cheap consumer hardware — a perennially hot topic in the open-source community; the "weight binding" fix is a concrete, actionable technique.

RoundPipe targets LLM fine-tuning on consumer-grade GPUs with limited VRAM and slow PCIe interconnects by combining pipeline parallelism with CPU offloading. It identifies and resolves the "weight binding issue" in existing pipeline schedules — where uneven layer binding causes GPU bubbles and memory waste — via a round-robin binding strategy that balances computation and memory efficiently across heterogeneous setups.

---

## 8. Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows
**Authors:** Chenxin Li, Zhengyang Tang, Huangxin Lin, Yunlong Lin et al.
**arXiv:** [arxiv.org/abs/2604.28139](https://arxiv.org/abs/2604.28139)
**Sources:** HuggingFace Daily Papers (17 upvotes)
**Why Trending:** Addresses a well-known shortcoming of static agent benchmarks (data contamination, frozen task sets); the "live" benchmark concept resonates strongly with the agent evaluation research community.

Claw-Eval-Live introduces a continuously-updated benchmark where tasks reflect real evolving workflows across software tools, business services, and local workspaces. Unlike static benchmarks that grade only final responses, it verifies execution correctness and measures performance against evolving workflow demands, preventing leakage and providing more reliable signal for agent capability assessment.

---

## 9. Leveraging Verifier-Based Reinforcement Learning in Image Editing
**Authors:** Hanzhong Guo, Jie Wu, Jie Liu, Yu Gao et al.
**arXiv:** [arxiv.org/abs/2604.27505](https://arxiv.org/abs/2604.27505)
**Sources:** HuggingFace Daily Papers (15 upvotes)
**Why Trending:** Applies RLHF/verifier-based RL (hugely successful for text generation) to image editing — a relatively unexplored frontier; the reward modeling approach is novel and practically relevant.

This paper extends verifier-based reinforcement learning to image editing, addressing the lack of robust general reward models that can evaluate arbitrary editing instructions. Rather than holistic scoring, it decomposes editing quality into verifiable sub-criteria per instruction type, enabling targeted RL feedback that improves instruction-following precision across diverse image editing tasks without requiring task-specific reward models.

---

## 10. Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling
**Authors:** Zhen Zhang, Changyi Yang, Zijie Xia, Zhen Yang et al.
**arXiv:** [arxiv.org/abs/2604.27039](https://arxiv.org/abs/2604.27039)
**Sources:** HuggingFace Daily Papers (15 upvotes)
**Why Trending:** Tackles a concrete inference efficiency problem (over-generation / under-generation) with a principled token-level framework; relevant to anyone optimizing LLM inference cost vs. quality.

LenVM (Length Value Model) introduces fine-grained token-level length modeling for autoregressive models, moving beyond coarse sequence-level length controls. By pretraining a value function that predicts optimal remaining generation length at each token, it enables dynamic length adjustment during inference that balances reasoning performance against computational cost — reducing unnecessary token generation without sacrificing answer quality.

---

## 11. Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists
**Authors:** Yujun Wu, Dongxu Zhang, Xinchen Li, Jinhang Xu et al.
**arXiv:** [arxiv.org/abs/2604.28158](https://arxiv.org/abs/2604.28158)
**Sources:** HuggingFace Daily Papers (11 upvotes)
**Why Trending:** Timely as AI-driven research agents proliferate; Intern-Atlas provides structured methodological provenance that is missing from citation graphs — essential infrastructure for AI-native scientific workflows.

Intern-Atlas builds a methodological evolution graph over the scientific literature, capturing not just citation links but the structured relationships explaining how and why research methods emerge, adapt, and build upon one another. This graph serves as infrastructure for AI research agents, enabling them to understand methodological lineage, identify conceptual gaps, and propose grounded next steps — moving beyond document-centric knowledge retrieval toward genuine scientific reasoning.

---

## 12. InteractWeb-Bench: Can Multimodal Agents Escape Blind Execution in Website Generation?
**Authors:** Qiyao Wang, Haoran Hu, Longze Chen, Hongbo Wang et al.
**arXiv:** [arxiv.org/abs/2604.27419](https://arxiv.org/abs/2604.27419)
**Sources:** HuggingFace Daily Papers (7 upvotes)
**Why Trending:** Benchmarks a practical and high-value use case — AI-assisted web development — and exposes blind execution failures in current multimodal coding agents.

InteractWeb-Bench evaluates multimodal LLM agents on interactive website generation, moving beyond idealized structured inputs to realistic messy specifications. It reveals that current agents suffer from "blind execution" — generating code without understanding interactive behavior, state management, or visual consistency — and provides a structured evaluation framework with automated correctness verification for interactive web elements.

---

## 13. Representation Fréchet Loss for Visual Generation
**Authors:** Jiawei Yang, Zhengyang Geng, Xuan Ju, Yonglong Tian et al.
**arXiv:** [arxiv.org/abs/2604.28190](https://arxiv.org/abs/2604.28190)
**Sources:** HuggingFace Daily Papers (6 upvotes)
**Why Trending:** Makes Fréchet Distance — a gold-standard evaluation metric — usable as a training objective for the first time, potentially reshaping how generative image models are trained.

This work demonstrates that Fréchet Distance (FD), long considered impractical as a training loss, can be effectively optimized in representation space by decoupling population size for FD estimation (50k samples) from batch size for gradient computation (1024). The resulting FD-loss enables direct optimization of distribution-level quality metrics during training, revealing that FD-optimized models exhibit markedly different generation characteristics than models trained with per-sample losses.

---

## 14. Synthetic Computers at Scale for Long-Horizon Productivity Simulation
**Authors:** Tao Ge, Baolin Peng, Hao Cheng, Jianfeng Gao (Microsoft Research)
**arXiv:** [arxiv.org/abs/2604.28181](https://arxiv.org/abs/2604.28181)
**Sources:** HuggingFace Daily Papers (6 upvotes)
**Why Trending:** Addresses a key bottleneck in training computer-use agents: the lack of realistic, user-specific synthetic environments; Microsoft Research's involvement adds credibility.

This paper introduces a scalable methodology for generating realistic synthetic computer environments conditioned on user-specific directory structures and content-rich artifacts, enabling large-scale training data creation for long-horizon productivity agents. By simulating realistic computer states — file systems, documents, application states — it allows agents to train on the kind of complex, context-dependent real-world tasks that existing simulators cannot capture.

---

## 15. Compliance versus Sensibility: On the Reasoning Controllability in Large Language Models
**Authors:** Xingwei Tan, Marco Valentino, Mahmud Elahi Akhter, Yuxiang Zhou et al.
**arXiv:** [arxiv.org/abs/2604.27251](https://arxiv.org/abs/2604.27251)
**Sources:** HuggingFace Daily Papers (5 upvotes)
**Why Trending:** Probes a fundamental question — can LLM reasoning patterns (induction, deduction, abduction) be decoupled from specific problem instances? — with implications for model controllability and interpretability research.

This paper investigates whether fundamental reasoning patterns (induction, deduction, abduction) in LLMs can be decoupled from specific problem content via Chain-of-Thought prompting. It finds a persistent tension between compliance (following instructed reasoning patterns) and sensibility (producing correct answers), revealing that current models lack reliable reasoning controllability — they cannot reliably apply a specified reasoning strategy independent of problem type.

---

## 16. The Last Human-Written Paper: Agent-Native Research Artifacts
**Authors:** Jiachen Liu, Jiaxin Pei, Jintao Huang, Chenglei Si et al.
**arXiv:** [arxiv.org/abs/2604.24658](https://arxiv.org/abs/2604.24658)
**Sources:** HuggingFace Daily Papers (4 upvotes)
**Why Trending:** Provocative framing ("the last human-written paper") and substantive argument about the structural costs of current scientific publishing attracted philosophical and practical discussion in ML circles.

The paper argues that scientific publications impose two structural costs when compressing iterative research into linear narratives: a Storytelling Tax (discarding failed experiments, rejected hypotheses, branching exploration) and an Engineering Tax (the gap between published methods and reproducible implementations). It proposes "Agent-Native Research Artifacts" — structured, machine-readable research objects that preserve the full branching research process for consumption by AI research agents.

---

## 17. MoCapAnything V2: End-to-End Motion Capture for Arbitrary Skeletons
**Authors:** Kehong Gong, Zhengyu Wen, Dao Thien Phong, Mingxi Xu et al.
**arXiv:** [arxiv.org/abs/2604.28130](https://arxiv.org/abs/2604.28130)
**Sources:** HuggingFace Daily Papers (3 upvotes)
**Why Trending:** End-to-end motion capture for arbitrary skeletons (not just human) from monocular video is a long-standing hard problem; the V2 improvement over factorized pipelines is a concrete advance for animation and robotics.

MoCapAnything V2 replaces the factorized Video-to-Pose + analytical IK pipeline with a fully end-to-end approach for arbitrary-skeleton motion capture from monocular video. By jointly predicting joint positions and rotations in an integrated model, it resolves the fundamental ambiguity in the factorized approach (joint positions alone don't uniquely determine rotations), achieving improved accuracy across diverse skeleton types including humans, animals, and robots.

---

## 18. PhyCo: Learning Controllable Physical Priors for Generative Motion
**Authors:** Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker et al.
**arXiv:** [arxiv.org/abs/2604.28169](https://arxiv.org/abs/2604.28169)
**Sources:** HuggingFace Daily Papers (2 upvotes)
**Why Trending:** Tackles the persistent physical plausibility failure in video diffusion — objects drifting, unrealistic collisions — with continuous, interpretable physical priors rather than post-hoc corrections.

PhyCo introduces continuous, interpretable physical priors into video diffusion models via controllable parameters for material properties, collision dynamics, and object interactions. Rather than relying on appearance-only generation, it learns physical priors from simulation data and transfers them to real-world video generation, enabling explicit control over physical behavior (friction, elasticity, mass) while maintaining photorealistic appearance.

---

## 19. FlashRT: Memory-Efficient Red-Teaming for Prompt Injection and Knowledge Corruption
**Authors:** Yanting Wang, Chenlong Yin, Ying Chen, Jinyuan Jia et al.
**arXiv:** [arxiv.org/abs/2604.28157](https://arxiv.org/abs/2604.28157)
**Sources:** HuggingFace Daily Papers, arxiv security community
**Why Trending:** Addresses security vulnerabilities in long-context LLMs (Gemini-3.1-Pro, Qwen-3.5) with practical efficiency improvements; relevant to both researchers and practitioners deploying LLMs in production RAG/agent systems.

FlashRT is a computationally and memory-efficient red-teaming framework targeting prompt injection and knowledge corruption attacks in long-context LLMs. By reducing the memory footprint of adversarial suffix search through selective context caching and approximate gradient computation, it enables quantitative security evaluation of long-context models that was previously computationally prohibitive — exposing new vulnerability patterns in RAG and agentic deployments.

---

## 20. Safety Drift After Fine-Tuning: Evidence from High-Stakes Domains
**Authors:** Emaan Bilal Khan, Amy Winecoff, Miranda Bogen, Dylan Hadfield-Menell et al.
**arXiv:** [arxiv.org/abs/2604.24902](https://arxiv.org/abs/2604.24902)
**Sources:** HuggingFace Daily Papers, AI safety community
**Why Trending:** Empirically validates a widely-feared but under-studied phenomenon — that domain fine-tuning degrades safety properties of base models — across 100 models in medical and legal domains, with actionable findings for practitioners.

This paper empirically tests whether safety properties persist through fine-tuning by analyzing 100 models including widely-deployed fine-tunes in medical and legal domains alongside controlled adaptations. It finds consistent safety drift: fine-tuned models systematically exhibit degraded refusal behavior and increased harmful output rates compared to base models, even when fine-tuning data contains no harmful content — challenging the common practice of safety-testing only base models.
