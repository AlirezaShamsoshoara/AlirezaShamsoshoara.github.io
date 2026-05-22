---
title: "Daily AI Papers — May 22, 2026"
date: 2026-05-22
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-22/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - agents
  - multimodal
---

## #1 — DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards

**Authors:** Kaiyi Zhang, Wei Wu, Yankai Lin

**Summary:** RLVR (reinforcement learning from verifiable rewards) is analyzed through a new "discriminator view" showing that policy-gradient updates implicitly act as a linear discriminator over token-gradient vectors. DelTA addresses the problem of shared high-frequency token patterns diluting sparse discriminative signal by estimating token coefficients to amplify side-specific gradient directions and downweight shared ones.

**Results:** On 7 math benchmarks, DelTA outperforms same-scale baselines by +3.26 and +2.62 average points on Qwen3-8B-Base and Qwen3-14B-Base, with additional generalization gains on code generation.

**arXiv:** [arxiv.org/abs/2605.21467](https://arxiv.org/abs/2605.21467)
**Sources:** HuggingFace Daily Papers (123 upvotes)
**Why trending:** Strong results on Qwen3 with a novel theoretical framing of token credit in RLVR — high relevance given current interest in reasoning-optimized LLMs.

---

## #2 — TransitLM: A Large-Scale Dataset and Benchmark for Map-Free Transit Route Generation

**Authors:** Hanyu Guo, Jiedong Yang, Chao Chen, Longfei Xu, Kaikui Liu, Xiangxiang Chu

**Summary:** TransitLM presents a 13M+ record transit planning dataset from 4 Chinese cities covering 120,845 stations and 13,666 lines, released as a continual pre-training corpus and benchmark for three evaluation tasks. An LLM trained on TransitLM produces structurally valid routes at high accuracy and implicitly grounds GPS coordinates to correct stations without any explicit mapping layer.

**Results:** Demonstrates end-to-end, map-free route generation from origin-destination pairs, eliminating dependence on traditional routing infrastructure.

**arXiv:** [arxiv.org/abs/2605.22355](https://arxiv.org/abs/2605.22355)
**Sources:** HuggingFace Daily Papers (118 upvotes), GitHub (96 stars)
**Why trending:** Practical application of LLMs to city-scale routing; strong community interest in eliminating map infrastructure dependencies.

---

## #3 — Perception or Prejudice: Can MLLMs Go Beyond First Impressions of Personality?

**Authors:** Caixin Kang, Tianyu Yan, Sitong Gong, Mingfang Zhang, Liangyang Ouyang, Ruicong Liu, Bo Zheng, Huchuan Lu, Kaipeng Zhang, Yoichi Sato, Yifei Huang

**Summary:** Introduces Grounded Personality Reasoning (GPR) — a new task requiring MLLMs to anchor Big Five trait ratings in observable behavioral evidence via a chain of rating, reasoning, and grounding. Releases MM-OCEAN (1,104 videos, 5,320 MCQs) and benchmarks 27 MLLMs across 13 closed and 14 open models.

**Results:** Reveals a "Prejudice Gap": 51% of correct trait ratings are not grounded in retrieved evidence, and Holistic-Grounding Rate spans only 0–33.5% across tested models.

**arXiv:** [arxiv.org/abs/2605.22109](https://arxiv.org/abs/2605.22109)
**Sources:** HuggingFace Daily Papers (103 upvotes)
**Why trending:** Exposes a systematic failure mode in MLLMs for social cognition tasks — grounding vs. pattern-matching distinction is fundamental.

---

## #4 — π-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows

**Authors:** Haoran Zhang, Luxin Xu, Zhilin Wang, Runquan Gui, Shunkai Zhang, Haodi Lei

**Summary:** π-Bench is a benchmark for evaluating proactive personal assistant agents (e.g., similar to OpenClaw/Jarvis-style agents) that must handle underspecified user requests and infer unstated needs, constraints, and preferences across long-horizon workflows. Unlike existing benchmarks, it explicitly measures proactive rather than merely reactive agent capabilities.

**Results:** Current frontier LLMs struggle significantly with proactive long-horizon task completion, revealing gaps between stated instructions and implicit user intent.

**arXiv:** [arxiv.org/abs/2605.14678](https://arxiv.org/abs/2605.14678)
**Sources:** HuggingFace Daily Papers (74 upvotes, 2 comments)
**Why trending:** Directly relevant to the wave of AI assistant products; proactive behavior and long-horizon planning are key differentiators.

---

## #5 — Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps

**Authors:** Yanke Zhou, Yiduo Li, Hanlin Tang, Maohua Li, Kan Liu, Lan Tao

**Summary:** Shows that full-attention LLMs are already intrinsically sparse and can be converted into sparse attention models in under 100 training steps — without native sparse training or heuristic token eviction. The method transfers full-attention weights into a sparse structure while preserving accuracy, resolving the efficiency-training-cost-accuracy trilemma.

**Results:** Achieves competitive performance to native sparse models with dramatically lower training overhead, enabling efficient long-context inference.

**arXiv:** [arxiv.org/abs/2605.16928](https://arxiv.org/abs/2605.16928)
**Sources:** HuggingFace Daily Papers (69 upvotes)
**Why trending:** Solves a practical pain point for deploying long-context LLMs efficiently without full retraining.

---

## #6 — ACC: Compiling Agent Trajectories for Long-Context Training

**Authors:** Qisheng Su, Zhen Fang, Shiting Huang, Yu Zeng, Yiming Zhao, Kou Shi

**Summary:** Proposes "agent trajectory compilation" — using the massive multi-turn trajectories produced by LLM agents as high-quality long-context training data. Rather than expensive long-document curation, agent trajectories naturally encode the dense evidence needed for long-horizon reasoning tasks.

**Results:** Models trained on compiled trajectories show strong long-context reasoning improvements, with significant reduction in data curation cost.

**arXiv:** [arxiv.org/abs/2605.21850](https://arxiv.org/abs/2605.21850)
**Sources:** HuggingFace Daily Papers (51 upvotes)
**Why trending:** Creative data pipeline that repurposes synthetic agent activity for training — addresses a bottleneck in long-context LLM development.

---

## #7 — PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects

**Authors:** Ziang Cao, Yinghao Liu, Haitian Li, Runmao Yao, Fangzhou Hong, Zhaoxi Chen

**Summary:** PhysX-Omni is the first unified framework for generating simulation-ready 3D assets across all three major physical categories — rigid, deformable, and articulated objects. Prior methods handled only single categories; this unified approach enables broad applicability across robotics, gaming, and embodied AI.

**Results:** Achieves state-of-the-art physical fidelity and geometric accuracy across all three object types, validated in downstream simulation environments.

**arXiv:** [arxiv.org/abs/2605.21572](https://arxiv.org/abs/2605.21572)
**Sources:** HuggingFace Daily Papers (42 upvotes)
**Why trending:** High relevance to embodied AI and robotics simulation; unifying object types is a key step toward general physics-aware 3D generation.

---

## #8 — LatentOmni: Rethinking Omni-Modal Understanding via Unified Audio-Visual Latent Reasoning

**Authors:** Yifan Dai, Zhenhua Wu, Bohan Zeng, Daili Hua

**Summary:** Argues that explicit text-based CoT compresses continuous audio-visual signals into discrete tokens, weakening temporal grounding. LatentOmni proposes unified latent-space reasoning that keeps audio-visual representations continuous during intermediate reasoning steps, enabling finer-grained multi-modal evidence integration.

**Results:** Achieves improved performance on joint audio-visual reasoning benchmarks compared to text-CoT-based multimodal models.

**arXiv:** [arxiv.org/abs/2605.22012](https://arxiv.org/abs/2605.22012)
**Sources:** HuggingFace Daily Papers (32 upvotes)
**Why trending:** Novel approach to the lossy discretization problem in multi-modal reasoning — relevant to omni-modal systems like GPT-4o.

---

## #9 — WorldKV: Efficient World Memory with World Retrieval and Compression

**Authors:** Jung Yi, Minjae Kim, Paul Hyunbin Cho, Wooseok Jang

**Summary:** Addresses persistent world consistency in autoregressive video diffusion models — when revisiting a previous viewpoint, content should remain consistent. Full KV-cache attention preserves consistency but breaks real-time constraints; WorldKV introduces efficient world retrieval and KV compression to maintain consistency while controlling memory and compute.

**Results:** Enables persistent, consistent world generation at scale without sacrificing real-time performance.

**arXiv:** [arxiv.org/abs/2605.22718](https://arxiv.org/abs/2605.22718)
**Sources:** HuggingFace Daily Papers (27 upvotes)
**Why trending:** World models and consistent video generation are hot research areas; memory efficiency is a core practical bottleneck.

---

## #10 — Spreadsheet-RL: Advancing LLM Agents on Realistic Spreadsheet Tasks via Reinforcement Learning

**Authors:** Banghao Chi, Yining Xie, Mingyuan Wu, Jingcheng Yang

**Summary:** Proposes an RL-based approach to train LLM agents on realistic spreadsheet tasks (Excel/Google Sheets), addressing the limitations of prompting-based spreadsheet agents. The framework uses verifiable spreadsheet outcomes as reward signals to iteratively improve agent policies.

**Results:** Significantly outperforms prompting-based baselines on realistic spreadsheet automation tasks, demonstrating strong generalization to complex multi-step operations.

**arXiv:** [arxiv.org/abs/2605.22642](https://arxiv.org/abs/2605.22642)
**Sources:** HuggingFace Daily Papers (26 upvotes, 3 comments)
**Why trending:** Enterprise AI automation is a large market; spreadsheets are ubiquitous productivity tools that RL-trained agents can realistically automate.

---

## #11 — Forecasting Scientific Progress with Artificial Intelligence

**Authors:** Sean Wu, Pan Lu, Yupeng Chen, Jonathan Bragg, Yutaro Yamada, Peter Clark, David Clifton, Philip Torr, James Zou, Junchi Yu

**Summary:** Introduces CUSP (Cutoff-conditioned Unseen Scientific Progress), a benchmark evaluating AI systems on predicting scientific discoveries across 4,760 events from multiple disciplines. Tests feasibility assessment, mechanistic reasoning, generative solution design, and temporal prediction.

**Results:** Current frontier models fail to reliably predict whether advances will be realized and systematically misestimate timing; performance is domain-dependent and exhibits systematic overconfidence.

**arXiv:** [arxiv.org/abs/2605.22681](https://arxiv.org/abs/2605.22681)
**Sources:** HuggingFace Daily Papers (24 upvotes), University of Oxford
**Why trending:** Provocative finding that AI cannot yet serve as a scientific oracle; timely given "AI for science" hype.

---

## #12 — FlowLong: Inference-time Long Video Generation via Manifold-constrained Tweedie Matching

**Authors:** Jangho Park, Geon Yeong Park, Gihyun Kwon, Jong Chul Ye

**Summary:** Addresses the challenge of generating long, temporally consistent videos at inference time without training on long sequences. Uses manifold-constrained Tweedie matching to enforce consistency across extended video segments by constraining generation to a learned data manifold.

**Results:** Achieves high-quality long video generation with improved temporal coherence compared to sliding-window approaches.

**arXiv:** [arxiv.org/abs/2605.20910](https://arxiv.org/abs/2605.20910)
**Sources:** HuggingFace Daily Papers (21 upvotes)
**Why trending:** Long video generation remains unsolved; training-free inference-time solutions are practically attractive.

---

## #13 — SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation

**Authors:** Xiaolong Zhou, Yifei Liu, Ziyang Gong, Jiarui Li

**Summary:** SpaceDG benchmarks spatial reasoning capabilities of vision-language models under realistic visual degradation conditions (blur, noise, occlusion, low-res). Most VLM spatial benchmarks assume clean input; this work exposes robustness gaps when inputs are degraded.

**Results:** Current state-of-the-art VLMs show significant performance drops under visual degradation, revealing that spatial intelligence is brittle to realistic image quality issues.

**arXiv:** [arxiv.org/abs/2605.22536](https://arxiv.org/abs/2605.22536)
**Sources:** HuggingFace Daily Papers (20 upvotes)
**Why trending:** Robustness of spatial intelligence in VLMs is critical for real-world deployment; degraded inputs are the norm, not the exception.

---

## #14 — Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles

**Authors:** Jinyang Wu, Guocheng Zhai, Ruihan Jin, Yuhao Shen, Zhengxi Lu

**Summary:** Proposes Maestro, an RL-trained orchestrator that dynamically selects among multiple LLMs and modular skills for autonomous agents. Rather than relying on a single monolithic LLM and fixed skill logic, Maestro learns which model-skill combination is optimal per task context.

**Results:** Improves over monolithic LLM agent baselines across diverse tasks including math, code, and tool-use by leveraging complementary strengths of different models.

**arXiv:** [arxiv.org/abs/2605.22177](https://arxiv.org/abs/2605.22177)
**Sources:** HuggingFace Daily Papers (17 upvotes)
**Why trending:** Multi-agent orchestration and model routing are emerging as key techniques for efficient, capable AI systems.

---

## #15 — Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving

**Authors:** Jiahao Wang, Bo Sun, Yijing Bai, Vincent Casser, Songyou Peng

**Summary:** Addresses the sensor heterogeneity problem in autonomous driving: converts dashcam and in-the-wild sensor data into the high-fidelity format of proprietary AV sensors, enabling large-scale diverse dataset creation without expensive proprietary collection. Learns cross-embodiment sensor translation models.

**Results:** Enables effective use of internet-scale dashcam footage for AV training, significantly improving dataset scale and diversity.

**arXiv:** [arxiv.org/abs/2605.22809](https://arxiv.org/abs/2605.22809)
**Sources:** HuggingFace Daily Papers (17 upvotes, 2 comments)
**Why trending:** Data bottleneck in AV training is a known problem; sensor conversion unlocks large existing unlabeled datasets.

---

## #16 — SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers

**Authors:** Javad Rajabi, Kimia Shaban, Koorosh Roohi, David B. Lindell, Babak Taati

**Summary:** DiTs (diffusion transformers) degrade when generating at resolutions beyond their training range. SEGA modifies inference-time attention using spectral energy guidance to maintain structural coherence at higher resolutions, improving on RoPE extrapolation approaches.

**Results:** Enables higher-resolution image generation from DiTs trained at lower resolutions, with improved perceptual quality and structural fidelity.

**arXiv:** [arxiv.org/abs/2605.22668](https://arxiv.org/abs/2605.22668)
**Sources:** HuggingFace Daily Papers (16 upvotes)
**Why trending:** Resolution extrapolation for DiTs (Flux, SD3, etc.) is practically valuable — no retraining needed.

---

## #17 — Q-ARVD: Quantizing Autoregressive Video Diffusion Models

**Authors:** Siao Tang, Xinyin Ma, Gongfan Fang, Xingyi Yang, Xinchao Wang

**Summary:** Addresses the inference cost challenge in autoregressive video diffusion models (ARVDs) through model quantization. ARVDs are promising for streaming/real-time video and world modeling but face prohibitive compute costs; this work identifies and solves quantization-specific challenges unique to the autoregressive video generation setting.

**Results:** Achieves significant inference speedup with minimal quality degradation, enabling practical deployment of ARVD models.

**arXiv:** [arxiv.org/abs/2605.21072](https://arxiv.org/abs/2605.21072)
**Sources:** HuggingFace Daily Papers (15 upvotes, 2 comments)
**Why trending:** World models and real-time video generation are trending; quantization is essential for practical deployment.

---

## #18 — Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

**Authors:** Ali Hatamizadeh, Yejin Choi, Jan Kautz (NVIDIA)

**Summary:** Proposes a new linear attention architecture that decouples the erase and write operations in recurrent state updates. Prior delta-rule models subtract before writing; Gated DeltaNet-2 separates these into independent gated operations, enabling more precise memory editing and better long-range associative recall.

**Results:** Outperforms prior linear attention architectures including DeltaNet and Mamba variants on language modeling and associative recall benchmarks.

**arXiv:** [arxiv.org/abs/2605.22791](https://arxiv.org/abs/2605.22791)
**Sources:** HuggingFace Daily Papers (11 upvotes)
**Why trending:** Linear attention / SSM architectures are a hot area; NVIDIA provenance adds visibility; memory editing in fixed-size recurrent states is fundamental.

---

## #19 — GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation

**Authors:** Sixiang Chen, Zhaohu Xing, Tian Ye, Xinyu Geng, Yunlong Lin

**Summary:** GenEvolve is an image generation agent that self-improves by distilling its own generation trajectories — combining internal generative capabilities with external tool use across diverse generation challenges. The agent learns from its own visual experience without additional human annotation.

**Results:** Achieves progressive improvement on open-ended image generation tasks, outperforming static prompting approaches on complex multi-step generation.

**arXiv:** [arxiv.org/abs/2605.21605](https://arxiv.org/abs/2605.21605)
**Sources:** HuggingFace Daily Papers (10 upvotes, 2 comments)
**Why trending:** Self-improving generative agents are at the frontier of autonomous AI systems; tool-orchestrated evolution is a novel paradigm.

---

## #20 — KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving

**Authors:** Zedong Liu, Xinyang Ma, Dejun Luo, Hairui Zhao, Bing Lu

**Summary:** In disaggregated LLM serving (prefill-decode separation, KV state disaggregation), KV cache becomes an explicit cross-network payload and a dominant bottleneck. KVServe introduces service-aware, dynamic KV cache compression that adapts compression ratio to service-level objectives and network conditions.

**Results:** Significantly reduces KV transfer overhead in disaggregated serving while maintaining generation quality, improving end-to-end throughput.

**arXiv:** [arxiv.org/abs/2605.13734](https://arxiv.org/abs/2605.13734)
**Sources:** HuggingFace Daily Papers (10 upvotes)
**Why trending:** Disaggregated LLM serving is standard in production; KV transfer bottlenecks are a live engineering pain point.
