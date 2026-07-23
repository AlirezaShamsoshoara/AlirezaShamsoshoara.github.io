---
title: "Daily AI Papers — July 23, 2026"
date: 2026-07-23
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-23/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - moe-training
  - diffusion-language-models
  - video-generation
---

## 1. SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD

**Authors:** Dongfang Li, Xiaodong Luo, Ruoyu Sun, Xuhui Chen, Linyuan Qiu, Jian Meng, et al.

**Summary:** Presents an end-to-end system for full-parameter post-training of trillion-parameter DeepSeek-V4 MoE models on Huawei's Ascend NPU SuperPOD, tackling memory pressure, communication overlap, and kernel efficiency at extreme scale. It's a rare detailed report on training frontier-scale MoE models entirely off the Nvidia/GPU stack.

**arXiv:** [arxiv.org/abs/2607.20145](https://arxiv.org/abs/2607.20145)
**Found on:** HuggingFace Daily Papers
**Why trending:** Top of today's HF board (43 upvotes) — strong interest in non-Nvidia training infra for trillion-parameter models.

---

## 2. Subliminal Clocks: Latent Time Modelling in Diffusion Language Models

**Authors:** Maximo Eduardo Rulli, Thomas Vaitses Fontanari, Simone Petruzzi, Federico Alvetreti, Giorgio Strano, Donato Crisostomi, et al.

**Summary:** Shows that diffusion language models, despite not being explicitly conditioned on a timestep, internally encode a latent "clock" signal tracking denoising progress within their residual stream. The finding has implications for controlling and interpreting DLM generation dynamics.

**arXiv:** [arxiv.org/abs/2607.01774](https://arxiv.org/abs/2607.01774)
**Found on:** HuggingFace Daily Papers (surfaced yesterday, still climbing)
**Why trending:** 35 upvotes — feeds the growing interest in diffusion LLMs as an alternative to autoregressive generation.

---

## 3. Self Gradient Forcing: Native Long Video Extrapolation

**Authors:** Junhao Zhuang, Shiyi Zhang, Yuxuan Bian, Yaowei Li, Yawen Luo, Yijun Liu, et al.

**Summary:** Extends the "Self Forcing" paradigm for autoregressive video diffusion by letting future-frame losses supervise how earlier generated latents are written into the KV cache, rather than treating the cache as frozen rollout state. This targets long-horizon video extrapolation quality directly.

**arXiv:** [arxiv.org/abs/2607.20368](https://arxiv.org/abs/2607.20368)
**Found on:** HuggingFace Daily Papers
**Why trending:** 28 upvotes — video generation long-horizon consistency remains a hot problem.

---

## 4. Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking

**Authors:** Kailin Jiang, Lei Liu, Jian Xi, Hui Xu, Junlin Liu, Baochen Fu, et al.

**Summary:** Argues that scoring retrieved documents independently (à la nDCG) ignores redundancy, conflict, and complementarity across a document *set*, and proposes an evaluate-diagnose-optimize framework for set-level retrieval quality aimed at LLM/agent consumers.

**arXiv:** [arxiv.org/abs/2607.19747](https://arxiv.org/abs/2607.19747)
**Found on:** HuggingFace Daily Papers
**Why trending:** 23 upvotes — RAG/agent retrieval quality is a persistent pain point.

---

## 5. An Exam for Active Observers

**Authors:** Jiarui Zhang, Muzi Tao, Shangshang Wang, Ollie Liu, Xuezhe Ma, Willie Neiswanger

**Summary:** Introduces ActiveVision, a benchmark testing whether multimodal LLMs perform "active observation" — iteratively redirecting attention based on intermediate hypotheses like human gaze — rather than processing a single static snapshot.

**arXiv:** [arxiv.org/abs/2607.16165](https://arxiv.org/abs/2607.16165)
**Found on:** HuggingFace Daily Papers
**Why trending:** 14 upvotes — novel benchmark angle on MLLM visual reasoning limitations.

---

## 6. Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models

**Authors:** Nischay Dhankhar, Dos Baha, Abulhair Saparov

**Summary:** Studies using hypernetworks at train time (rather than test-time adaptation) to generate fixed LoRA adapters from a large fact corpus, enabling scalable factual knowledge injection into LLMs, and characterizes how this scales.

**arXiv:** [arxiv.org/abs/2607.19604](https://arxiv.org/abs/2607.19604)
**Found on:** HuggingFace Daily Papers
**Why trending:** 10 upvotes — knowledge editing/injection remains a core open problem for keeping LLMs current.

---

## 7. Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment

**Authors:** Dwip Dalal, Shivansh Patel, Chahit Jain, Jeonghwan Kim, Utkarsh Mishra, Alex Baratian, et al.

**Summary:** Identifies that behavior-cloning finetuning of VLMs for robot policies erodes pretrained visual/semantic generalization, and that standard web-data co-training doesn't fix the resulting language-action misalignment. Proposes representation anchoring to preserve generalization.

**arXiv:** [arxiv.org/abs/2607.13429](https://arxiv.org/abs/2607.13429)
**Found on:** HuggingFace Daily Papers
**Why trending:** 8 upvotes — robotics/VLA generalization is a heavily watched subfield.

---

## 8. Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization

**Authors:** Zhicheng Cai, Xinyuan Guo, Hanlin Wu, Mingxuan Wang, Wei-Ying Ma, Ya-Qin Zhang

**Summary:** Diagnoses PPO-Clip's exploration collapse in LLM RL as stemming from measuring policy discrepancy with a Euclidean metric that's geometrically inconsistent with the policy manifold, and proposes a Riemannian isometric alternative.

**arXiv:** [arxiv.org/abs/2607.10169](https://arxiv.org/abs/2607.10169)
**Found on:** HuggingFace Daily Papers
**Why trending:** 8 upvotes — RLHF/RLVR training stability is central to current LLM post-training work.

---

## 9. AutoIndex: Learning Representation Programs for Retrieval

**Authors:** Sam O'Nuallain, Nithya Rajkumar, Ramya Narayanasamy, Hanna Jiang, Shreyas Chaudhari, Andrew Drozdov, et al.

**Summary:** Proposes searching over "representation programs" — executable transformations that slice, enrich, normalize, and reorganize documents before indexing — instead of just tuning retrievers/rerankers, using validation-guided agentic program search.

**arXiv:** [arxiv.org/abs/2607.18603](https://arxiv.org/abs/2607.18603)
**Found on:** HuggingFace Daily Papers (surfaced yesterday)
**Why trending:** 7 upvotes — agentic search over the retrieval pipeline itself is a fresh angle on RAG optimization.

---

## 10. DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations

**Authors:** Jiazhen Jiang, Boxi Cao, Lingyong Yan, Yaojie Lu, Hongyu Lin, Shuaiqiang Wang, et al.

**Summary:** Introduces a deterministically verifiable benchmark built on a taxonomy of document-manipulation tasks (atomic operations to escalating workflows), targeting the reliability of autonomous agents on real-world workspace document tasks.

**arXiv:** [arxiv.org/abs/2607.19865](https://arxiv.org/abs/2607.19865)
**Found on:** HuggingFace Daily Papers
**Why trending:** 4 upvotes — agent benchmarking for practical office/workspace automation is gaining traction.

---

## 11. FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation

**Authors:** Hao Liu, Chenghuan Huang, Ye Huang, Zhiying Wen, Hao Liu, Mohan Zhang, et al.

**Summary:** Identifies that training-free sparse attention with adaptive Top-p routing causes uneven per-head workloads under multi-GPU sequence parallelism for video Diffusion Transformers, and presents a system that rebalances this to cut the resulting straggler effect.

**arXiv:** [arxiv.org/abs/2607.16190](https://arxiv.org/abs/2607.16190)
**Found on:** HuggingFace Daily Papers
**Why trending:** 4 upvotes — systems-level efficiency for high-res video generation infra.

---

## 12. Reading and Steering Representations of Materials-Science Mechanisms in an Open-Weight Language Model

**Authors:** Markus J. Buehler

**Summary:** Uses interpretability techniques on an open-weight Gemma model to show materials-science mechanism knowledge is represented in three separable forms (readable concepts, transformation-carried orientation, and causally-controlling representations), and demonstrates steering engineering answers via these internals.

**arXiv:** [arxiv.org/abs/2607.20058](https://arxiv.org/abs/2607.20058)
**Found on:** HuggingFace Daily Papers (surfaced yesterday)
**Why trending:** 3 upvotes — science-domain mechanistic interpretability is a niche but growing area.

---

## 13. Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning

**Authors:** Md Tanvirul Alam

**Summary:** Introduces Trace, an RLVR training environment for vision-language models that factorizes task construction into a scene grammar and an executable task program, decoupling visual realization from answer computation to produce broad, exactly-verifiable training data.

**arXiv:** [arxiv.org/abs/2607.19790](https://arxiv.org/abs/2607.19790)
**Found on:** HuggingFace Daily Papers
**Why trending:** 3 upvotes — addresses the training-data bottleneck for extending RLVR to vision-language reasoning.

---

## 14. SLPO: Scaling Latent Reasoning via a Surrogate Policy

**Authors:** Runyang You, Zhiyuan Liu, Yongqi Li, Wenjie Li

**Summary:** Tackles the imitation-bound nature of latent (continuous-vector) reasoning models by introducing a surrogate policy approach, aiming to bring RLVR-style test-time scaling to latent reasoners without the token-decoding cost of explicit Chain-of-Thought.

**arXiv:** [arxiv.org/abs/2607.19691](https://arxiv.org/abs/2607.19691)
**Found on:** HuggingFace Daily Papers
**Why trending:** 2 upvotes — latent reasoning efficiency is an active efficiency-vs-capability tradeoff topic.

---

## 15. G-MAD: A Game-Based Data Generation Framework for Multi-View RGB-T Aerial Object Detection

**Authors:** Yechan Kim, JongHyun Park, Dongho Yoon, Namhoon Jung, Moongu Jeon

**Summary:** Presents an open-source framework built on the Arma3 game engine to generate synchronized multi-view RGB-thermal aerial imagery with automatic bounding-box annotation, addressing viewpoint and RGB-T alignment limitations of real-world aerial datasets.

**arXiv:** [arxiv.org/abs/2607.19942](https://arxiv.org/abs/2607.19942)
**Found on:** HuggingFace Daily Papers
**Why trending:** 2 upvotes — simulation-based data generation for a data-scarce detection niche.

---

## 16. ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion

**Authors:** Cho In, Jeonghwan Cho, Mijin Yoo, Gim Hee Lee, Seon Joo Kim

**Summary:** Addresses the loss of scene-adaptive capacity allocation in feed-forward 3D Gaussian Splatting (where Gaussian count/placement is tied to image resolution rather than scene complexity) via an adaptive token expansion mechanism for more compact, quality-preserving reconstructions.

**arXiv:** [arxiv.org/abs/2607.20417](https://arxiv.org/abs/2607.20417)
**Found on:** HuggingFace Daily Papers
**Why trending:** 2 upvotes — continued refinement of feed-forward 3DGS, a fast-moving novel-view-synthesis subfield.

---

## 17. Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations

**Authors:** Hiskias Dingeto

**Summary:** Points out a structural flaw in reconstruction-based scoring of natural-language explanations of hidden activations: the test doesn't penalize false claims that don't affect reconstruction. Demonstrates this on a released Qwen-2.5-7B verbalizer and proposes decodability supervision as a fix.

**arXiv:** [arxiv.org/abs/2607.20379](https://arxiv.org/abs/2607.20379)
**Found on:** HuggingFace Daily Papers
**Why trending:** 1 upvote — a sharp critique of a widely-used interpretability evaluation method.

---

## 18. SeededGrasp: Language-Guided Grasping in Complex Scenes with Multiple Embodiments

**Authors:** Yang Xu, Gurpreet Singh Mukker, Raymond Wang, Jasper Gerigk, Maria Attarian, Igor Gilitschenski

**Summary:** Proposes a method for language-guided robotic grasping that avoids both the limited spatial awareness of direct VLM grasp prediction and the heavy data/compute cost of joint VLM-grasping-model training, targeting multi-embodiment scalability.

**arXiv:** [arxiv.org/abs/2607.20207](https://arxiv.org/abs/2607.20207)
**Found on:** HuggingFace Daily Papers
**Why trending:** New on today's board — robotics language-grounded manipulation.

---

## 19. Moving Alphabet: A Controlled Study of Training Data for Text-to-Video Generation

**Authors:** Amber Yijia Zheng, Lu Liu, Raymond A. Yeh, Xi Yin

**Summary:** Runs controlled experiments isolating how training-data distribution and caption quality (rather than model architecture) affect text-to-video generation quality, introducing "Moving Alphabet" as a controlled testbed.

**arXiv:** [arxiv.org/abs/2607.18789](https://arxiv.org/abs/2607.18789)
**Found on:** HuggingFace Daily Papers
**Why trending:** New on today's board — data-centric analysis of an under-explored axis in video generation.

---

## 20. SLAM in Low-Light Environments: Project Report

**Authors:** Oleh Basystyi, Anna Stasyshyn, Oleksandr Kosovan, Yaroslav Prytula

**Summary:** Studies how low illumination, reduced contrast, and motion blur degrade visual SLAM feature extraction/matching, and evaluates how far camera-only SLAM can be pushed in low-light robotics scenarios versus falling back to LiDAR/depth/thermal sensors.

**arXiv:** [arxiv.org/abs/2607.17699](https://arxiv.org/abs/2607.17699)
**Found on:** HuggingFace Daily Papers
**Why trending:** New on today's board — practical robotics perception under adverse conditions.
