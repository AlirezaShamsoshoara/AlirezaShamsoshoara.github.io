---
title: "Daily AI Papers — May 16, 2026"
date: 2026-05-16
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-16/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - long-context
  - video-generation
  - agentic-frameworks
---

## #1 — Long Context Pre-Training with Lighthouse Attention
**Authors:** Bowen Peng, Subho Ghosh, Jeffrey Quesnelle (NousResearch)
**Upvotes:** 18 | **Sources:** HuggingFace Daily Papers, GitHub (16 stars)
**Arxiv:** [arxiv.org/abs/2605.06554](https://arxiv.org/abs/2605.06554)

Lighthouse Attention is a training-only, gradient-free hierarchical attention algorithm that wraps standard SDPA to handle extreme sequence lengths without quadratic memory cost. A two-stage recipe pre-trains with Lighthouse Attention then recovers a full attention model at the end, achieving lower final loss and faster training than vanilla full attention. Trending because NousResearch open-sourced the full implementation and it solves a critical long-context training bottleneck without changing inference architecture.

---

## #2 — VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction
**Authors:** Kaixin Zhu, Yiwen Tang, Yifan Yang, Renrui Zhang, Bohan Zeng
**Upvotes:** 13 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.15186](https://arxiv.org/abs/2605.15186)

VGGT-Edit extends feed-forward 3D reconstruction models to support text-conditioned scene editing by injecting edit signals via depth-synchronized text injection and predicting geometric displacements as residual fields. Unlike 2D-lifting approaches that edit views independently and suffer from multi-view inconsistency, this method edits natively in 3D space in a single forward pass. Attention-worthy for closing the gap between static 3D reconstruction and interactive scene editing without per-scene optimization.

---

## #3 — PanoWorld: Towards Spatial Supersensing in 360° Panorama World
**Authors:** Changpeng Wang, Xin Lin, Junhan Liu, Yuheng Liu, Zhen Wang
**Upvotes:** 13 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.13169](https://arxiv.org/abs/2605.13169)

PanoWorld introduces spherical spatial cross-attention into MLLMs to natively process equirectangular panoramic images, enabling full-surround spatial reasoning without decomposing into perspective crops. Geometry-aware supervision preserves the spherical structure, yielding strong performance on navigation, 3D scene understanding, and robotic search tasks. Notable for pushing beyond the narrow field-of-view bottleneck that limits most vision-language models.

---

## #4 — Orchard: An Open-Source Agentic Modeling Framework
**Authors:** Baolin Peng, Wenlin Yao, Qianhui Wu, Hao Cheng, Xiao Yu (Microsoft Research)
**Upvotes:** 12 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.15040](https://arxiv.org/abs/2605.15040)

Orchard is a fully open-source framework for scalable agentic LLM training, covering coding agents, GUI navigation, and personal assistant tasks through specialized training recipes. It directly addresses the gap where most open-source projects focus on orchestration/evaluation rather than training infrastructure. Trending because it democratizes the training side of agentic AI that has been dominated by proprietary stacks.

---

## #5 — ViMU: Benchmarking Video Metaphorical Understanding
**Authors:** Qi Li, Xinchao Wang (National University of Singapore)
**Upvotes:** 10 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.14607](https://arxiv.org/abs/2605.14607)

ViMU is the first benchmark targeting implicit/metaphorical understanding in video—testing whether models grasp what videos *mean* rather than just what they *show*. It evaluates the gap between surface-level visual comprehension and deeper social/cultural subtext interpretation in current video-language models. Interesting because it exposes a systematic weakness in VLMs: strong literal understanding but poor figurative/metaphorical reasoning.

---

## #6 — Forcing-KV: Hybrid KV Cache Compression for Efficient Autoregressive Video Diffusion Models
**Authors:** Yicheng Ji, Zhizhou Zhong, Jun Zhang, Qin Yang, XiTai Jin
**Upvotes:** 7 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.09681](https://arxiv.org/abs/2605.09681)

Forcing-KV addresses the KV cache memory explosion in autoregressive video diffusion by categorizing attention heads as static (compressible via pooling) or dynamic (requiring per-frame retention), and applies a tailored hybrid compression strategy. This enables long-horizon video generation at reduced memory overhead without sacrificing temporal coherence. Timely as AR video diffusion models (e.g., Self Forcing) gain traction for real-time interactive generation.

---

## #7 — RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO
**Authors:** Yanzuo Lu, Ronglai Zuo, Jiankang Deng
**Upvotes:** 6 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.15190](https://arxiv.org/abs/2605.15190)

RAVEN combines causal autoregressive video distillation with GRPO-based reinforcement learning applied to consistency model sampling, closing the train-inference distribution gap that degrades quality over long generation horizons. CM-GRPO provides a principled alignment step that improves coherence without requiring additional supervision data. Draws interest as a practical path to high-quality real-time streaming video generation.

---

## #8 — Does Synthetic Layered Design Data Benefit Layered Design Decomposition?
**Authors:** Kam Man Wu, Haolin Yang, Qingyu Chen, Yihu Tang, Jingye Chen
**Upvotes:** 6 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.15167](https://arxiv.org/abs/2605.15167)

This work systematically studies whether synthetic layered image data (foreground, background, text layers) can substitute for scarce proprietary layered design assets when training decomposition models. Results show synthetic data significantly improves layer decomposition quality and enables better control over layer distribution at scale. Relevant for teams building design tools that need to edit AI-generated or scanned images post-hoc.

---

## #9 — CurveBench: A Benchmark for Exact Topological Reasoning over Nested Jordan Curves
**Authors:** Amirreza Mohseni, Mona Mohammadi, Morteza Saghafian, Naser Talebizadeh Saradari
**Upvotes:** 6 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.14068](https://arxiv.org/abs/2605.14068)

CurveBench tasks vision-language models with recovering the full containment tree of nested Jordan curves from images — a test of exact topological spatial reasoning that existing models mostly fail. The structured prediction formulation requires no approximation: partial credit is not given for wrong topology. Highlights that VLMs' spatial reasoning is mostly heuristic pattern-matching, not rigorous geometric inference.

---

## #10 — BOOKMARKS: Efficient Active Storyline Memory for Role-playing
**Authors:** Letian Peng, Ziche Liu, Yiming Huang, Longfei Yun, Kun Zhou
**Upvotes:** 6 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.14169](https://arxiv.org/abs/2605.14169)

BOOKMARKS replaces recurrent summarization in role-playing agents with a search-based memory system that actively maintains task-relevant structured bookmarks capturing character behaviors and story details. Unlike compression-heavy profiles, bookmarks preserve fine-grained details needed for long-horizon character consistency. Practically relevant as roleplay and interactive fiction agents scale to multi-session contexts.

---

## #11 — WildTableBench: Benchmarking Multimodal Foundation Models on Table Understanding In the Wild
**Authors:** Junzhe Huang, Xiaoxiao Sun, Yan Yang, Yuxuan Hou, Ruotian Zhang (U. Queensland)
**Upvotes:** 6 | **Sources:** HuggingFace Daily Papers, GitHub
**Arxiv:** [arxiv.org/abs/2605.01018](https://arxiv.org/abs/2605.01018)

WildTableBench introduces 402 real-world table images from online sources paired with 928 QA pairs spanning 17 subtypes, testing whether MLLMs can handle the messy table images people actually encounter. Only one of 21 tested frontier models exceeds 50% accuracy, exposing severe weaknesses in structural perception and numerical reasoning over visually complex tables.

---

## #12 — Learning to Build the Environment: Self-Evolving Reasoning RL via Verifiable Environment Synthesis
**Authors:** Yucheng Shi, Zhenwen Liang, Kishan Panaganti, Dian Yu, Wenhao Yu
**Upvotes:** 5 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.14392](https://arxiv.org/abs/2605.14392)

Instead of generating training data, this method trains LLMs to construct executable reasoning environments (that sample problem instances, compute references, and score responses), enabling self-improvement via stable solve-verify asymmetry. The key insight is that environment construction is harder than solving, so a model that can build good environments has implicitly learned the domain deeply. A notable rethink of the zero-data RL loop.

---

## #13 — PRISM: Prior Rectification and Uncertainty-Aware Structure Modeling for Diffusion-Based Text Image Super-Resolution
**Authors:** Zihang Xu, Xiaoyang Liu, Zheng Chen, Yulun Zhang, Xiaokang Yang
**Upvotes:** 5 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.13027](https://arxiv.org/abs/2605.13027)

PRISM addresses two failure modes in diffusion-based text super-resolution: unreliable text priors extracted from degraded low-quality inputs, and the underdetermination of fine stroke boundaries by global priors. It applies flow-matching prior rectification and uncertainty-aware residual encoding to handle both problems. Critical for OCR and document restoration pipelines where wrong character topology breaks readability.

---

## #14 — PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation
**Authors:** Yidong Huang, Zun Wang, Han Lin, Dong-Ki Kim, Shayegan Omidshafiei
**Upvotes:** 4 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.14269](https://arxiv.org/abs/2605.14269)

PhyMotion introduces a physics-grounded reward signal for human motion video generation that evaluates kinematic plausibility, contact consistency, and dynamic feasibility in 3D body space rather than 2D perceptual signals. RL post-training with this reward substantially reduces physically implausible motion artifacts. Addresses a persistent realism gap in human video generation that 2D-only rewards cannot detect.

---

## #15 — Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning
**Authors:** Zihao Han, Tiangang Zhang, Huaibin Wang, Yilun Sun
**Upvotes:** 4 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.11458](https://arxiv.org/abs/2605.11458)

ATESD dynamically adjusts how much of the reference solution a teacher sees during on-policy self-distillation, using a learnable policy controller to modulate teacher exposure based on student capability. This resolves teacher-side exposure mismatch where an always-fully-informed teacher gives guidance too far beyond the student's current level. Practical improvement to OPSD-style training that is gaining momentum in reasoning model post-training.

---

## #16 — Aligning Latent Geometry for Spherical Flow Matching in Image Generation
**Authors:** Tuna Han Salih Meral, Kaan Oktay, Hidir Yesiltepe, Adil Kaan Akan, Pinar Yanardag (Virginia Tech)
**Upvotes:** 3 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.15193](https://arxiv.org/abs/2605.15193)

This work shows that VAE latents concentrate on thin spherical shells and proposes replacing linear flow interpolation with spherical linear interpolation (slerp) along geodesic paths, keeping trajectories on the manifold throughout diffusion. Decoupling radial and angular components reveals that semantic content lives in direction, not magnitude. Consistently improves ImageNet-256 FID across tokenizers with no architecture changes.

---

## #17 — Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image
**Authors:** Ming Qian, Zimin Xia, Changkun Liu, Shuailei Ma, Wen Wang
**Upvotes:** 3 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.14984](https://arxiv.org/abs/2605.14984)

Sat3DGen generates photorealistic, geometrically accurate street-level 3D scenes from a single overhead satellite image using a geometry-first pipeline that decouples structure estimation from texture synthesis. Prior methods trade off between geometric fidelity and semantic richness; this approach achieves both via novel geometric constraints and training strategies. High value for autonomous driving sim, urban planning, and geospatial AI.

---

## #18 — FutureSim: Replaying World Events to Evaluate Adaptive Agents
**Authors:** Shashwat Goel, Nikhil Chandak, Arvindh Arun, Ameya Prabhu, Steffen Staab
**Upvotes:** 3 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.15188](https://arxiv.org/abs/2605.15188)

FutureSim builds evaluation environments by chronologically replaying real news articles and world events beyond an agent's knowledge cutoff, testing whether agents can adapt and forecast correctly as new information arrives. Current agents fail significantly on long-horizon world prediction once they pass their training cutoff. Important benchmark for the emerging class of continual/adaptive agents.

---

## #19 — Topology-Preserving Neural Operator Learning via Hodge Decomposition
**Authors:** Dongzhe Zheng, Tao Zhong, Christine Allen-Blanchette
**Upvotes:** 3 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.13834](https://arxiv.org/abs/2605.13834)

This paper applies Hodge decomposition to solution operators of physical PDEs on meshes, isolating unlearnable topological degrees of freedom from learnable geometric dynamics to eliminate spectral interference. The resulting hybrid Eulerian-Lagrangian architecture is more accurate and efficient on physical simulation benchmarks. Notable for applying rigorous differential geometry to make neural operators structure-aware rather than black-box function approximators.

---

## #20 — RewardHarness: Self-Evolving Agentic Post-Training
**Authors:** Yuxuan Zhang, Penghui Du, Bo Li, Cong Wei, Junwen Miao
**Upvotes:** 3 | **Sources:** HuggingFace Daily Papers
**Arxiv:** [arxiv.org/abs/2605.08703](https://arxiv.org/abs/2605.08703)

RewardHarness reframes reward modeling as an agentic tool-building task: given a few human demonstrations, the system iteratively constructs and refines evaluation tools that score instruction-guided image edits without large-scale preference annotation. It achieves superior performance over existing reward models from minimal human input. Noteworthy for reducing the data bottleneck in RLHF-style post-training for image generation.
