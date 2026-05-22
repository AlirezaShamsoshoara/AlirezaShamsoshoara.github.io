---
title: "Daily AI Papers — May 23, 2026"
date: 2026-05-23
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-23/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-reasoning
  - agentic-ai
  - reinforcement-learning
---

## #1 — Unsupervised Process Reward Models

**Authors:** Artyom Gadetsky, Maxim Kodryan, Siba Smarak Panigrahi, Hang Guo

**Summary:** Process Reward Models (PRMs) provide powerful step-level supervision for LLM reasoning but require costly expert annotations for every reasoning step. This paper proposes unsupervised PRMs (uPRM) that require no human supervision — neither step-by-step annotations nor ground-truth verification — trained only on unlabeled problem sets, enabling scalable fine-grained reward signals for RLVR.

**arXiv:** [arxiv.org/abs/2605.10158](https://arxiv.org/abs/2605.10158)
**Sources:** HuggingFace (23 upvotes), arXiv
**Why trending:** Directly addresses the annotation bottleneck in RLVR training pipelines; unsupervised PRMs enable scalable step-level credit assignment without labelers.

---

## #2 — Training Large Language Models to Predict Clinical Events

**Authors:** Benjamin Turtel, Paul Wilczewski, Kris Skotheim

**Summary:** Extends Foresight Learning to clinical prediction by converting time-ordered MIMIC-III notes into prediction examples with past context, natural-language questions about future events, and labels resolved from later documentation. Demonstrates that LLMs can predict clinical events from longitudinal patient notes without structured clinical data or specialized architectures.

**arXiv:** [arxiv.org/abs/2605.12817](https://arxiv.org/abs/2605.12817)
**Sources:** HuggingFace (14 upvotes), arXiv
**Why trending:** Intersection of LLMs and healthcare; shows practical value of LLM pretraining for clinical forecasting from free-text EHR notes.

---

## #3 — Forecasting Downstream Performance of LLMs With Proxy Metrics

**Authors:** Arkil Patel, Siva Reddy, Marius Mosbach, Dzmitry Bahdanau

**Summary:** Cross-entropy loss is poorly aligned with downstream capabilities while direct evaluations are expensive and sparse; this paper proposes using proxy metrics to reliably forecast downstream LLM performance, enabling informed architecture, data, and training recipe decisions without full evaluation runs. The approach addresses a critical gap in practical model development workflows.

**arXiv:** [arxiv.org/abs/2605.18607](https://arxiv.org/abs/2605.18607)
**Sources:** HuggingFace (10 upvotes), arXiv
**Why trending:** Reducing LLM evaluation cost is a high-value industry problem; proxy-based forecasting accelerates model development iteration.

---

## #4 — ClinSeekAgent: Automating Multimodal Evidence Seeking for Agentic Clinical Reasoning

**Authors:** Juncheng Wu, Letian Zhang, Yuhan Wang, Haoqin Tu

**Summary:** Introduces ClinSeekAgent, an automated agentic framework that shifts clinical AI from passive retrieval to active, iterative multimodal evidence seeking from heterogeneous sources. The agent dynamically plans, gathers, and synthesizes evidence to support clinical decision-making in real-world workflows where evidence is not pre-curated.

**arXiv:** [arxiv.org/abs/2605.20176](https://arxiv.org/abs/2605.20176)
**Sources:** HuggingFace (7 upvotes), arXiv
**Why trending:** Agentic AI in healthcare; multimodal clinical reasoning with active evidence gathering represents a practical advance over static RAG.

---

## #5 — One Sentence, One Drama: Personalized Short-Form Drama Generation via Multi-Agent Systems

**Authors:** Yufei Shi, Weilong Yan, Naixuan Huang, Yucheng Chen

**Summary:** Proposes a multi-agent pipeline for generating short-form video dramas from a single sentence, addressing three key failures of one-shot LLM generation: narrative pacing, spatial consistency across clips, and production-level quality control. The system coordinates script, visual, and quality-control agents to produce coherent drama content.

**arXiv:** [arxiv.org/abs/2605.22144](https://arxiv.org/abs/2605.22144)
**Sources:** HuggingFace (7 upvotes), arXiv
**Why trending:** Generative media and AI content creation; multi-agent systems for end-to-end creative production pipelines.

---

## #6 — Swift Sampling: Selecting Temporal Surprises via Taylor Series

**Authors:** Dahye Kim, Bhuvan Sachdeva, Karan Uppal, Naman Gupta, Vineeth N. Balasubramanian

**Summary:** Inspired by predictive coding in the human brain, Swift Sampling is a training-free frame selection algorithm that models video as a differentiable trajectory in visual latent space and uses Taylor series to identify temporal surprises — moments where actual features deviate from predicted evolution. This enables efficient, high-information frame selection for long-form video understanding.

**arXiv:** [arxiv.org/abs/2605.22678](https://arxiv.org/abs/2605.22678)
**Sources:** HuggingFace (6 upvotes), arXiv
**Why trending:** Training-free efficiency for long-video MLLMs; elegant theory-grounded approach to video token reduction.

---

## #7 — LoREnc: Low-Rank Encryption for Securing Foundation Models and LoRA Adapters

**Authors:** Beomjin Ahn, Jungmin Kwon, Chanyong Jung, Jaewook Chung

**Summary:** LoREnc is a training-free framework that protects foundation models and LoRA adapters from IP leakage and model recovery attacks via spectral truncation and compensation. It suppresses dominant low-rank components of FM weights and compensates for missing information in authorized LoRA adapters, requiring no retraining or original dataset access.

**arXiv:** [arxiv.org/abs/2605.13163](https://arxiv.org/abs/2605.13163)
**Sources:** HuggingFace (6 upvotes), arXiv
**Why trending:** AI security and IP protection for deployed models; practical defense requiring zero retraining.

---

## #8 — AutoRubric-T2I: Robust Rule-Based Reward Model for Text-to-Image Alignment

**Authors:** Kuei-Chun Kao, Daixuan Huo, Yuanhao Ban, Cho-Jui Hsieh

**Summary:** AutoRubric-T2I uses VLM judges to automatically generate fine-grained evaluation rubrics for text-to-image alignment, replacing costly Bradley-Terry preference models trained on large human preference corpora. The rule-based reward approach is more transparent, adaptable, and less data-hungry than existing T2I reward models.

**arXiv:** [arxiv.org/abs/2605.17602](https://arxiv.org/abs/2605.17602)
**Sources:** HuggingFace (5 upvotes), arXiv
**Why trending:** T2I alignment via VLM-as-judge is an active area; rule-based rewards offer interpretability advantages for generative model alignment.

---

## #9 — SceneAligner: 3D-Grounded Floorplan Localization in the Wild

**Authors:** Junhyeong Cho, Ruojin Cai, Hadar Averbuch-Elor

**Summary:** SceneAligner addresses large-scale floorplan localization from visual observations in real-world buildings with rasterized floorplans, overcoming limitations of prior methods that assumed small-scale environments and precise vectorized maps. The approach uses 3D geometric grounding to reliably determine observer position from visual inputs.

**arXiv:** [arxiv.org/abs/2605.22581](https://arxiv.org/abs/2605.22581)
**Sources:** HuggingFace (5 upvotes), arXiv
**Why trending:** Indoor navigation and embodied AI; practical localization for robotics and AR applications in unconstrained real buildings.

---

## #10 — Segment Anything with Motion, Geometry, and Semantic Adaptation for Complex Nonlinear Visual Object Tracking

**Authors:** Deyi Zhu, Yuji Wang, Yong Liu, Yansong Tang, Bingyao Yu

**Summary:** Adapts SAM 2 for robust visual object tracking by incorporating motion, geometry, and semantic cues to handle challenging scenarios: distractors, occlusion, and nonlinear motion that defeat direct SAM 2 application. The adaptation preserves SAM 2's strong pretraining priors while adding task-specific tracking intelligence.

**arXiv:** [arxiv.org/abs/2605.22538](https://arxiv.org/abs/2605.22538)
**Sources:** HuggingFace (5 upvotes), arXiv
**Why trending:** SAM 2 adaptation is a hot research direction; generalizable visual tracking matters for robotics and video analysis.

---

## #11 — Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

**Authors:** Mingkai Deng, Jinyu Hou, Lara Sá Neves, Varad Pimpalkhute, Taylor W. Killian

**Summary:** Argues that efficient agentic reasoning requires decomposing decision-making into three systems controlling when and how to plan, rather than relying on end-to-end reactive policies with implicit chain-of-thought. The framework reduces token waste from unnecessary reasoning without sacrificing accuracy gains.

**arXiv:** [arxiv.org/abs/2605.22138](https://arxiv.org/abs/2605.22138)
**Sources:** HuggingFace (4 upvotes), arXiv
**Why trending:** Token efficiency in agentic AI systems; selective reasoning activation is increasingly important as agent deployments scale.

---

## #12 — Bernini: Latent Semantic Planning for Video Diffusion

**Authors:** Bernini Team, Chenchen Liu, Junyi Chen, Lei Li, Lu Chi

**Summary:** Proposes unifying MLLMs and diffusion models through a division of labor: MLLMs perform semantic planning over heterogeneous multimodal inputs, while diffusion models render pixels from high-level semantic guidance and low-level visual features. The result is a video generation system that combines semantic reasoning with photorealistic synthesis.

**arXiv:** [arxiv.org/abs/2605.22344](https://arxiv.org/abs/2605.22344)
**Sources:** HuggingFace (4 upvotes), arXiv
**Why trending:** Hybrid MLLM+diffusion architectures for video generation is an emerging design paradigm following rapid progress in both domains.

---

## #13 — Rule2DRC: Benchmarking LLM Agents for DRC Script Synthesis with Execution-Guided Test Generation

**Authors:** Jinuk Kim, Junsoo Byun, Donghwi Hwang, Seong-Jin Park, Hyun Oh Song

**Summary:** Introduces a benchmark for LLM agents translating natural language chip design rules into executable DRC scripts, using execution-guided test generation to evaluate correctness rather than code similarity. Addresses the labor-intensive manual process of DRC script authoring that requires deep EDA expertise.

**arXiv:** [arxiv.org/abs/2605.15669](https://arxiv.org/abs/2605.15669)
**Sources:** HuggingFace (4 upvotes), arXiv
**Why trending:** LLMs for EDA/chip design automation; execution-based evaluation is the right standard for code-generating agents.

---

## #14 — Diversed Model Discovery via Structured Table Discovery

**Authors:** Zhengyuan Dong, Renée J. Miller

**Summary:** Proposes using structured tables in model cards (performance, configuration, dataset tables) for model search, arguing that semantic text similarity produces homogeneous results while comparative table-based search enables discovery of diverse, task-aligned models. The framework treats model search as an inherently comparative problem.

**arXiv:** [arxiv.org/abs/2605.22766](https://arxiv.org/abs/2605.22766)
**Sources:** HuggingFace (4 upvotes), arXiv
**Why trending:** Improving model discoverability on HuggingFace Hub; table-structured search fills gaps left by text-only retrieval.

---

## #15 — TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks

**Authors:** Zhaoyang Chu, Jiarui Hu, Xingyu Jiang, Pengyu Zou, Han Li

**Summary:** Scalable data engine that reverse-engineers 1,530 evaluation tasks from 80,870 in-the-wild terminal recordings, spanning 18 real-world categories from everyday shell operations to 50-step workflows covering 1,280 unique commands. Provides a grounded, real-world benchmark for terminal agent evaluation beyond synthetic tasks.

**arXiv:** [arxiv.org/abs/2605.22535](https://arxiv.org/abs/2605.22535)
**Sources:** HuggingFace (3 upvotes), arXiv
**Why trending:** Real-world agent benchmarks; terminal agents are a practical deployment target for AI coding assistants.

---

## #16 — "I didn't Make the Micro Decisions": Measuring, Inducing, and Exposing Goal-Level AI Contributions in Collaboration

**Authors:** Eunsu Kim, Jessica R. Mindel, Kyungjin Kim, Sherry Tongshuang Wu

**Summary:** Introduces CoTrace, a goal-level attribution framework that decomposes explicit goals into verifiable requirements and traces AI contributions through the process of how LLMs shape users' goals — not just final artifacts. The framework enables measurement, induction, and exposure of AI's hidden influence on what users ask for.

**arXiv:** [arxiv.org/abs/2605.21363](https://arxiv.org/abs/2605.21363)
**Sources:** HuggingFace (3 upvotes), arXiv
**Why trending:** Human-AI collaboration attribution; critical for AI accountability and user reliance calibration as LLMs become more involved in goal formulation.

---

## #17 — From Reasoning Chains to Verifiable Subproblems: Curriculum RL Enables Credit Assignment for LLM Reasoning

**Authors:** Xitai Jiang, Zihan Tang, Wenze Lin, Yang Yue, Shenzhi Wang

**Summary:** SCRL (Subproblem Curriculum Reinforcement Learning) derives verifiable subproblems from reference reasoning chains and uses curriculum RL to fix the final subproblem as the original task, enabling partial credit assignment even for failed rollouts. Significantly improves RLVR efficiency on hard problems where correct final-answer rollouts are rare.

**arXiv:** [arxiv.org/abs/2605.22074](https://arxiv.org/abs/2605.22074)
**Sources:** HuggingFace (2 upvotes), arXiv
**Why trending:** Directly addresses sparse rewards in RLVR for hard reasoning tasks; curriculum-based subproblem decomposition is a practical advance.

---

## #18 — Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws

**Authors:** Nandan Kumar Jha, Brandon Reagen

**Summary:** Shows that the optimizer is not a fixed training detail but reveals a hidden scaling axis: how effectively it converts added FFN width into utilized spectral capacity. Using eigenspectra of feed-forward representations, the same Transformer architecture can realize very different effective capacities depending on optimizer choice.

**arXiv:** [arxiv.org/abs/2605.21803](https://arxiv.org/abs/2605.21803)
**Sources:** HuggingFace (2 upvotes), arXiv
**Why trending:** Revisits scaling law assumptions by showing optimizer choice creates measurable capacity gaps — important for understanding compute-optimal training.

---

## #19 — Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry

**Authors:** Pablo Marcos-Manchón, Rishi Jha, Lluís Fuentemilla

**Summary:** Tests the Platonic Representation Hypothesis in human brains using fMRI data from the Natural Scenes Dataset, proposing a self-supervised encoder that learns subject-specific embeddings from brain activity alone by exploiting repeated stimuli. Finds that universal geometry analogous to convergent representations in ANNs can be unsupervisedly recovered across human subjects.

**arXiv:** [arxiv.org/abs/2605.20496](https://arxiv.org/abs/2605.20496)
**Sources:** HuggingFace (2 upvotes), arXiv
**Why trending:** Neuro-AI bridge; extends a popular AI hypothesis to biological neural systems with empirical fMRI evidence.

---

## #20 — SAM 3D Animal: Promptable Animal 3D Reconstruction from Images in the Wild

**Authors:** Xuyi Hu, Jin Lyu, Jiuming Liu, Yebin Liu, Silvia Zuffi

**Summary:** Presents SAM 3D Animal, the first promptable framework for multi-animal 3D reconstruction from a single image, built on the SMAL+ parametric animal model with support for flexible keypoint and mask prompts. Handles large species variation, frequent occlusions, and multi-animal scenes — settings where prior methods fail.

**arXiv:** [arxiv.org/abs/2605.07604](https://arxiv.org/abs/2605.07604)
**Sources:** HuggingFace (2 upvotes), arXiv
**Why trending:** SAM-based 3D reconstruction; practical multi-animal modeling for wildlife, robotics, and biological research applications.
