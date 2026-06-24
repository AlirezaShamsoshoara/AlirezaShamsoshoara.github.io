---
title: "Daily AI Papers — June 24, 2026"
date: 2026-06-24
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-24/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - world-models
  - diffusion-models
---

## 1. Qwen-AgentWorld: Language World Models for General Agents
**Authors:** Yuxin Zuo, Zikai Xiao, Li Sheng, Fei Huang, Jianhong Tu, Yuxuan Liu, Tianyi Tang, Xiaomeng Hu, Yang Su, Qingfeng Lan, Ning Ding et al. (Qwen Team, Alibaba)
**arXiv:** [arxiv.org/abs/2606.24597](https://arxiv.org/abs/2606.24597)

**Summary:** Qwen releases the first language world models (Qwen-AgentWorld-35B-A3B and 397B-A17B) capable of simulating agentic environments across 7 domains via long chain-of-thought reasoning, trained on 10M+ interaction trajectories through a 3-stage CPT→SFT→RL pipeline. The models can act as decoupled environment simulators for scalable agentic RL or as unified agent foundation models, improving downstream performance across 7 agentic benchmarks.

**Sources:** HuggingFace Daily Papers (73 upvotes), arxiv
**Why trending:** Highest upvote count of the day. A major model release from the Qwen team combining world modeling with agent training at scale — rare combination of research depth and practical impact.

---

## 2. NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?
**Authors:** Yuru Wang, Lejun Cheng, Yuxin Zuo, Sihang Zeng, Bingxiang He, Che Jiang, Junlin Yang, Yuchong Wang, Kaikai Zhao, Weifeng Huang et al.
**arXiv:** [arxiv.org/abs/2606.24530](https://arxiv.org/abs/2606.24530)

**Summary:** NatureBench introduces a cross-discipline benchmark of 90 tasks distilled from peer-reviewed Nature-family publications, testing whether AI coding agents can reproduce and surpass published SOTA results — not just re-run demos. Built on NatureGym, an automated pipeline that wraps each paper into a containerized environment, the benchmark probes whether agents can engage in genuine scientific discovery.

**Sources:** HuggingFace Daily Papers (46 upvotes), arxiv
**Why trending:** Provocative question about whether coding agents can do real science, not just benchmark-chase. Appeals to the growing community excitement around AI for science.

---

## 3. MobileForge: Annotation-Free Adaptation for Mobile GUI Agents with Hierarchical Feedback-Guided Policy Optimization
**Authors:** Guangyi Liu, Pengxiang Zhao, Gao Wu, Yiwen Yin et al.
**arXiv:** [arxiv.org/abs/2606.19930](https://arxiv.org/abs/2606.19930)

**Summary:** MobileForge enables annotation-free adaptation of MLLM-based mobile GUI agents to real target apps, solving the bottleneck that apps are numerous and frequently updated yet costly to annotate. It introduces a hierarchical feedback-guided policy optimization scheme that connects target-app dynamics to agent learning without human-written demonstrations or reward labels.

**Sources:** HuggingFace Daily Papers (33 upvotes), arxiv
**Why trending:** Practical solution to one of the main friction points in deploying mobile agents commercially — strong applied interest from the mobile AI community.

---

## 4. MemGUI-Agent: An End-to-End Long-Horizon Mobile GUI Agent with Proactive Context Management
**Authors:** Guangyi Liu, Gao Wu, Congxiao Liu, Pengxiang Zhao et al.
**arXiv:** [arxiv.org/abs/2606.19926](https://arxiv.org/abs/2606.19926)

**Summary:** MemGUI-Agent addresses the failure mode of long-horizon mobile GUI agents — prompt explosion and dilution of critical facts across app transitions — by replacing passive ReAct-style prompting with proactive context management that actively curates and compresses intermediate facts. The end-to-end design maintains reliability on multi-step, multi-app tasks where prior agents degrade.

**Sources:** HuggingFace Daily Papers (32 upvotes), arxiv
**Why trending:** Companion paper to MobileForge from same group, addressing the complementary memory challenge. Long-horizon mobile automation is a hot industrial application area.

---

## 5. AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction
**Authors:** Shanhui Zhao, Jiacheng Liu, Guohong Liu, Jichao Yan et al.
**arXiv:** [arxiv.org/abs/2606.23449](https://arxiv.org/abs/2606.23449)

**Summary:** AOHP is an open-source harness that bridges the mismatch between AI agents (which need tool-calling, memory, and cross-app access) and modern operating systems (which are designed for application-centric workflows). It provides a unified OS-level substrate enabling personalized, efficient, and secure agent interaction without requiring OS modifications.

**Sources:** HuggingFace Daily Papers (25 upvotes), arxiv
**Why trending:** Open-source release of infrastructure that any agent framework can build on; directly relevant to the ongoing "AI OS" conversation sparked by products like Rabbit, Rewind, and Apple Intelligence.

---

## 6. LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis
**Authors:** Shihao Xu, Tiancheng Zhou, Jiatong Ma, Yanli Ding et al.
**arXiv:** [arxiv.org/abs/2602.09379](https://arxiv.org/abs/2602.09379)

**Summary:** LingxiDiagBench evaluates LLMs on Chinese-language psychiatric consultation via a multi-agent simulation framework where AI plays both patient and diagnostician, addressing the global shortage of psychiatrists and the inherent subjectivity of interview-based diagnosis. The benchmark covers the full consultation workflow from intake to differential diagnosis.

**Sources:** HuggingFace Daily Papers (19 upvotes), arxiv
**Why trending:** AI for mental health remains a high-impact and underserved area; the Chinese psychiatric context and multi-agent role-play design is novel and timely given China's mental health crisis.

---

## 7. OpenThoughts-Agent: Data Recipes for Agentic Models
**Authors:** Negin Raoof, Richard Zhuang, Marianna Nezhurina, Etash Guha et al.
**arXiv:** [arxiv.org/abs/2606.24855](https://arxiv.org/abs/2606.24855)

**Summary:** OpenThoughts-Agent investigates how to curate training data for broadly capable agent models, filling a gap where existing open efforts (SWE-Smith, SERA, Nemotron-Terminal) each target a single benchmark. The paper provides data recipes and ablations for training agents that generalize across diverse agentic tasks including code, tool use, and web navigation.

**Sources:** HuggingFace Daily Papers (15 upvotes), arxiv
**Why trending:** Data curation for agents is as important as architecture — this is one of the first open studies publishing actionable recipes for cross-domain agent training data.

---

## 8. Semantic Browsing: Controllable Diversity for Image Generation
**Authors:** Sara Dorfman, Maya Vishnevsky, Omer Dahary, Or Patashnik et al.
**arXiv:** [arxiv.org/abs/2606.23679](https://arxiv.org/abs/2606.23679)

**Summary:** Modern text-to-image models collapse to a single visual interpretation per prompt; Semantic Browsing reframes diversity as a structured design-choice problem rather than random noise injection, allowing users to "browse" a semantically meaningful space of interpretations. The approach produces variations driven by meaningful compositional differences rather than incidental stylistic drift.

**Sources:** HuggingFace Daily Papers (12 upvotes), arxiv
**Why trending:** Addresses a widely felt pain point in creative AI workflows — controllable variety without incoherence. Strong community appeal to artists and designers.

---

## 9. FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation
**Authors:** Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt et al.
**arXiv:** [arxiv.org/abs/2606.24876](https://arxiv.org/abs/2606.24876)

**Summary:** FLAT generates explorable 3D scenes from a single image by decoding video diffusion latents into triangle-mesh-based 3D Gaussian Splatting (3DGS) representations rather than volumetric Gaussians, producing geometrically accurate surfaces suitable for downstream rendering and simulation. The feedforward approach leverages implicit multi-view structure encoded in video diffusion latent space.

**Sources:** HuggingFace Daily Papers (11 upvotes), arxiv
**Why trending:** 3D scene generation from a single image is a coveted capability for game development, VR, and robotics. The mesh-based output is more practically useful than volumetric Gaussians.

---

## 10. FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs
**Authors:** Wenlong Cheng, Yuan Gan, Yunqiu Xu, Jiaxu Miao et al.
**arXiv:** [arxiv.org/abs/2606.22875](https://arxiv.org/abs/2606.22875)

**Summary:** FedOT addresses the risk that federated learning participants can redistribute or resell the shared global model by embedding watermarks into Latent Diffusion Models (LDMs) trained in FL settings, enabling both ownership verification and leakage tracing back to the malicious participant. The scheme preserves FL's privacy guarantees while adding accountability.

**Sources:** HuggingFace Daily Papers (9 upvotes), arxiv
**Why trending:** Security and IP protection in federated ML is an emerging regulatory concern; relevant to healthcare and finance sectors deploying FL-trained generative models.

---

## 11. Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning
**Authors:** Shiding Zhu, Yudi Qi, Yajie Wang, Jiaze Li et al.
**arXiv:** [arxiv.org/abs/2606.24428](https://arxiv.org/abs/2606.24428)

**Summary:** Single-agent self-improvement loops suffer from the Self-Confirmation Trap — wrong-but-self-consistent trajectories get reinforced because the same agent that executes also evaluates. The Execute-Distill-Verify (EDV) paradigm decouples these roles across agents to break the feedback loop, enabling more reliable experience-driven self-evolution.

**Sources:** HuggingFace Daily Papers (8 upvotes), arxiv
**Why trending:** Identifies and names a clear failure mode in popular RLVR/self-play pipelines; the fix is simple and broadly applicable to any agent self-improvement setup.

---

## 12. Are Text-to-Image Models Inductivist Turkeys? A Counterfactual Benchmark for Causal Reasoning
**Authors:** Jiayi Lei, Yuandong Pu, Xingyu Han, Rongpeng Zhu et al.
**arXiv:** [arxiv.org/abs/2606.24548](https://arxiv.org/abs/2606.24548)

**Summary:** Inspired by Russell's inductivist turkey (which learned "feeding follows footsteps" until Thanksgiving), this paper tests whether T2I models learn genuine causal structure or spurious visual-textual correlations via counterfactual image prompts that cannot be answered by pattern matching alone. Results show current SOTA models fail systematically on causal counterfactuals.

**Sources:** HuggingFace Daily Papers (5 upvotes), arxiv
**Why trending:** The "inductivist turkey" framing is memorable and the benchmark exposes a fundamental limitation of current T2I training paradigms — good for sparking debate.

---

## 13. DiffusionBench: On Holistic Evaluation of Diffusion Transformers
**Authors:** Xingjian Leng, Jaskirat Singh, Zhanhao Liang, Ethan Smith et al.
**arXiv:** [arxiv.org/abs/2606.24888](https://arxiv.org/abs/2606.24888)

**Summary:** DiffusionBench challenges the field's over-reliance on ImageNet class-conditional FID as the primary evaluation for diffusion transformers, arguing it fails to reflect real progress in generative modeling. The benchmark introduces a holistic evaluation suite covering text-to-image generation, compositional reasoning, and visual coherence across diverse conditions.

**Sources:** HuggingFace Daily Papers (4 upvotes), arxiv
**Why trending:** Benchmark critique papers drive methodology shifts; this tackles the entrenched FID monoculture in diffusion model evaluation.

---

## 14. Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning
**Authors:** Chenhao Dang, Jing Ma, Mingjie Liao et al.
**arXiv:** [arxiv.org/abs/2606.24133](https://arxiv.org/abs/2606.24133)

**Summary:** Online Data Mixing (ODM) for LLM pre-training typically optimizes a single proxy metric, but this paper frames data scheduling as a multi-objective RL problem where diversity, domain balance, and downstream task performance are jointly optimized. The holistic scheduler adapts data mixtures dynamically during training with significantly better efficiency than static mixing.

**Sources:** HuggingFace Daily Papers (2 upvotes), arxiv
**Why trending:** Data scheduling for pre-training is high-leverage but under-published; multi-objective RL framing is a fresh take with direct application at any scale.

---

## 15. QG-MIL: A Gated Transformer Aggregator for Domain-Agnostic Multiple Instance Learning in Medical Imaging
**Authors:** Luca Zedda, Davide Antonio Mura, Cecilia Di Ruberto, Maurizio Atzori et al.
**arXiv:** [arxiv.org/abs/2606.20027](https://arxiv.org/abs/2606.20027)

**Summary:** Attention-based MIL aggregators in medical imaging suffer from attention concentration — overconfident predictions from a few patches. QG-MIL introduces RMSNorm-based pre-normalization, per-head QK normalization, fine-grained gating, and cross-patch attention to stabilize and spread attention across the full slide, achieving domain-agnostic improvements across pathology datasets.

**Sources:** HuggingFace Daily Papers (2 upvotes), arxiv
**Why trending:** Computational pathology is one of the most commercially active AI verticals; a domain-agnostic improvement to the core aggregation architecture has broad applicability.

---

## 16. FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning
**Authors:** Xirui Li, Zhe Liu, Xiaoqing Ye, Wenhua Han et al.
**arXiv:** [arxiv.org/abs/2606.24231](https://arxiv.org/abs/2606.24231)

**Summary:** FlowR2A resolves the longstanding tension between scoring-based driving planners (dense reward supervision but fixed action vocabulary) and anchor-based planners (dynamic proposals but sparse supervision) by learning a reward-to-action distribution using normalizing flows. This enables both dense supervision and diverse multi-modal trajectory generation.

**Sources:** HuggingFace Daily Papers (1 upvote), arxiv
**Why trending:** Autonomous driving planning is a competitive research area; a principled unification of two dominant paradigms using flow-based models is technically novel.

---

## 17. DREAM: Dense Retrieval Embeddings via Autoregressive Modeling
**Authors:** Yixuan Tang, Yi Yang et al.
**arXiv:** [arxiv.org/abs/2606.24667](https://arxiv.org/abs/2606.24667)

**Summary:** DREAM challenges the contrastive learning dominance in dense retrieval by showing that the autoregressive next-token prediction objective — normally associated with generative LMs — can produce high-quality retrieval embeddings without requiring labeled positive/negative pairs. This makes DREAM particularly valuable for low-resource retrieval settings.

**Sources:** HuggingFace Daily Papers (1 upvote), arxiv
**Why trending:** Label-free dense retrieval is practically significant for enterprise RAG deployments; the autoregressive angle is an unexpected but compelling approach.

---

## 18. ReMMD: Realistic Multilingual Multi-Image Agentic Verification for Multimodal Misinformation Detection
**Authors:** Chenhao Dang, Dantong Zhu, Jun Yang, Conghui He et al.
**arXiv:** [arxiv.org/abs/2606.24112](https://arxiv.org/abs/2606.24112)

**Summary:** Existing multimodal misinformation benchmarks use isolated short captions with single images and binary labels — far from real viral posts that combine long multilingual narratives, multiple images, mixed provenance, and subtle text-image framing errors. ReMMD introduces a benchmark and agentic verification framework matched to this realistic setting.

**Sources:** HuggingFace Daily Papers (1 upvote), arxiv
**Why trending:** Misinformation detection at scale is a pressing societal need; the multimodal, multilingual, multi-image setting is the right threat model for current social media.

---

## 19. World Value Models for Robotic Manipulation
**Authors:** Zhihao Wang, Jianxiong Li, Yu Cui, Yuan Gao et al.
**arXiv:** [arxiv.org/abs/2606.24742](https://arxiv.org/abs/2606.24742)

**Summary:** World Value Models (WVMs) unify temporal grounding and future planning for robotic value estimation, addressing the failure of existing robotic value models that lack deep temporal understanding across long manipulation sequences. WVMs leverage world-model pretraining to produce accurate value estimates from mixed-quality robot data at scale.

**Sources:** HuggingFace Daily Papers (1 upvote), arxiv
**Why trending:** Robotic manipulation scaling via world models is an active frontier; this connects directly to the Qwen-AgentWorld theme of the day (language world models for agents).

---

## 20. ChartWalker: Benchmarking the Cross-Chart RAG Task
**Authors:** Ning Tang, Chenghan Xie, Hanyang Yuan, Yi Li et al.
**arXiv:** [arxiv.org/abs/2606.23997](https://arxiv.org/abs/2606.23997)

**Summary:** Cross-Chart RAG — retrieving and reasoning across multiple heterogeneous charts simultaneously — is critical for complex analytical tasks in science, business, and policy, but existing benchmarks focus on single charts or use lexical-overlap-prone question generation. ChartWalker introduces a new benchmark with genuinely multi-chart questions requiring visual and quantitative cross-chart reasoning.

**Sources:** HuggingFace Daily Papers (1 upvote), arxiv
**Why trending:** Enterprise BI and scientific analysis workflows increasingly require multi-chart reasoning; a dedicated benchmark will catalyze model development in this underserved area.
