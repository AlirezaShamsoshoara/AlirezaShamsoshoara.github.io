---
title: "Daily AI Papers — November 07, 2026"
date: 2026-11-07
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-07/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - inference-efficiency
  - multimodal-generation
---

### 1. From Autonomous Agents to Cognitive Symbionts: Toward AI-Augmented Human Intelligence
**Authors:** Hao Fei
**arXiv:** [arxiv.org/abs/2611.05376](https://arxiv.org/abs/2611.05376)
**Summary:** This perspective proposes AI-augmented human intelligence and a cognitive symbiont that maintains personal context over years, senses situations through devices, and proactively supports thinking and everyday action. It organizes the design around the gap between a person's available knowledge and working memory, treating privacy, trust, covert assistance, and adoption pressure as integral considerations rather than reporting a deployed system's performance.

---

### 2. Why Pay for Long Reasoning When Rewrite Do Trick? Causal Effects of Reasoning History Compaction on Future Generation and Agent Cost
**Authors:** Anton Hristov
**arXiv:** [arxiv.org/abs/2611.03852](https://arxiv.org/abs/2611.03852)
**Summary:** This study rewrites an open-weight model's prior reasoning into compact state records before revealing pending tool results, then compares continuations against the original history without retraining. Accepted compact histories usually shorten future reasoning in the tested models, while software-agent savings, retained quality, and rewrite-inclusive latency depend on the target model and compressor.

---

### 3. Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable Benchmark for Mathematical Modeling
**Authors:** Xiaojun Wu, Cehao Yang, Xuhui Jiang, Chengjin Xu, Jia Li, Jian Guo
**arXiv:** [arxiv.org/abs/2611.08237](https://arxiv.org/abs/2611.08237)
**Summary:** TB-MathModel evaluates complete mathematical-modeling tasks from 18 real contest problems in containerized terminals, scoring numeric answers against outstanding human papers rather than relying only on report grading. Direction-aware scoring and hard feasibility gates combine programmatic invariants with 624 Lean 4 obligations, producing a reproducible evaluation signal for long-horizon modeling agents.

---

### 4. HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation
**Authors:** Gyeonghun Kim, Donghoon Kim, Minsoo Choi, Suyun Lee
**arXiv:** [arxiv.org/abs/2611.02660](https://arxiv.org/abs/2611.02660)
**Summary:** HeLM equips a hierarchical vision-language-action model with explicit language memory, using factorized event detection and event-triggered updates to preserve task-relevant history across observations and task boundaries. Across 10 real-world tasks with 56 variants, the authors report a 12.8-percentage-point intra-episode success gain over the strongest baseline, 78 percent compositional subtask success, and lower memory use and latency than a keyframe baseline at long horizons.

---

### 5. NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion Transformers
**Authors:** Dar-Yen Chen, Yi-Zhe Song
**arXiv:** [arxiv.org/abs/2611.05648](https://arxiv.org/abs/2611.05648)
**Summary:** NitroFusion2 uses intermediate text-token states from multimodal diffusion transformers as an adversarial representation and conditions discrimination on aspects such as typography, objects, or style. The authors report one- to two-step generation at quality comparable to the conventional four- to eight-step distillation regime, including sharp rendered text and fine-grained details at one step.

---

### 6. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization
**Authors:** Qile Jiang, George Em Karniadakis
**arXiv:** [arxiv.org/abs/2611.08483](https://arxiv.org/abs/2611.08483)
**Summary:** SwarmEvolve runs hundreds of low-cost agents per evolutionary-search round, reasoning in latent space and sharing KV caches while hidden-state novelty filtering preserves diverse ideas. Across 21 mathematical-discovery and scientific-computing problems, the authors report the highest average score and median times of three to eight minutes to reach scores that comparison frameworks attain in 60 minutes.

---

### 7. SAE Interprets MoE: Sparse AutoEncoders Reveal That MoE Experts Exhibit Human-Interpretable Fine-Grained Specialization
**Authors:** Anyuan Zhuo, Shaohua Zhang, Yuan Lin, Pinyan Lu
**arXiv:** [arxiv.org/abs/2611.08089](https://arxiv.org/abs/2611.08089)
**Summary:** This study trains sparse autoencoders on mixture-of-experts layer outputs and decomposes each latent's pre-activation over experts to measure contribution rather than only router selection. Analyses of three Qwen3-30B-A3B layers reveal concentrated, fine-grained specialization, including distinct experts for Java versus front-end code and geometry versus arithmetic and polynomials.

---

### 8. Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter Readout
**Authors:** Tushaar Gangavarapu, Gil Tabak, Clemens JS Schaefer
**arXiv:** [arxiv.org/abs/2611.08376](https://arxiv.org/abs/2611.08376)
**Summary:** Muir combines sensitivity-allocated low-rank gating, matched-filter state readout, and a numerically stable parallel update to improve linear attention while reinvesting saved parameters in a wider feed-forward network. Across 166 million to 1.34 billion parameters, the authors report improved perplexity and recall, including stable extrapolation to 10-million-token streams at 1.34 billion parameters and 2.7-times faster training than a Transformer at 32K context.

---

### 9. Reducing Representational Interference in Retrieval Embeddings with Trainable Prefix Tokens
**Authors:** Seongtae Hong, Youngjoon Jang, Jungseob Lee, Chanjun Park, Heuiseok Lim
**arXiv:** [arxiv.org/abs/2611.07298](https://arxiv.org/abs/2611.07298)
**Summary:** This method prepends trainable DUMP tokens during embedding-model training while leaving the architecture, pooling strategy, and contrastive retrieval objective unchanged. Experiments across encoder and decoder embedding models report consistent retrieval and long-context improvements, with analyses suggesting that the prefixes reduce interference from low-information token-level signals.

---

### 10. LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive Worlds
**Authors:** Yusheng Dai, Vladimir Iashin, Kangdi Wang, Yuxuan Jiang, Ilpo Viertola, Weiqiang Wang, Qiuhong Ke, Min Zhao, Jianfei Cai
**arXiv:** [arxiv.org/abs/2611.05988](https://arxiv.org/abs/2611.05988)
**Summary:** LiveFoley combines a trailing sliding window that converts segment-level visual encoders into streaming modules without retraining with a causal autoregressive diffusion backend that expands denoising context. The authors report offline-comparable temporal alignment and leading quality among evaluated streaming systems, with configurable frontend latency and a choice between history-only and approximate future-conditioned audio generation.

---

### 11. Towards Real-Time Full-Waveform LiDAR Transformers via Intensity-Guided Token Reduction and Physics-Aware Augmentation
**Authors:** Kotaro Oishi, Kazuma Ikeda, Ryosei Hara, Ryo Yoshida, Mariko Isogawa, Kentaro Yoshioka
**arXiv:** [arxiv.org/abs/2611.07613](https://arxiv.org/abs/2611.07613)
**Summary:** FWL-ToPM prunes and merges full-waveform LiDAR tokens using intensity structure, while FWLAug preserves per-ray time-of-flight waveforms and frustum geometry during augmentation. On Ghost-FWL, the authors report more than eight-times speedup with a nearly nine-point F1 gain over the prior state of the art, plus augmentation gains on the standard benchmark and unseen scenes.

---

### 12. OpenFrontiers: A Collection of Open Research Problems and a Benchmark for Scientific Rediscovery
**Authors:** Jiarui Yao, Ruida Wang, Tong Zhang
**arXiv:** [arxiv.org/abs/2610.37739](https://arxiv.org/abs/2610.37739)
**Summary:** OpenFrontiers pairs a structured corpus of 12,151 open research problems with a 200-problem mathematical benchmark containing 110 problems resolved in 2026 and 90 still open, using Lean 4 statements and independent checks. Evaluation of seven agents on the HQ-50 subset finds limited closed-book rediscovery and shows that live-web success mostly reflects retrieving published solutions rather than independently solving the problems.

---

### 13. StepX-OPD: Rethinking Multi-Teacher On-Policy Distillation in Diffusion Models
**Authors:** Chenru Wang, Xuanyang Zhang, Yucheng Han, Wenbo Nie, Wei Cheng, Xianfang Zeng, Gang YU, Chi Zhang
**arXiv:** [arxiv.org/abs/2611.04386](https://arxiv.org/abs/2611.04386)
**Summary:** StepX-OPD merges capability consolidation and few-step diffusion distillation, letting frozen specialist teachers supervise a student's own short rollout while adding low-noise velocity regression. On SD3.5-Medium and FLUX.1-dev, the authors report the highest normalized average score among compared four-step methods, with approximately 37 percent fewer training GPU-hours than the stated sequential pipeline on SD3.5-Medium.

---

### 14. Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse Attention
**Authors:** Serdarcan Dilbaz, Arjun Krishna, Kiran Kamble, Daniel M. Bikel
**arXiv:** [arxiv.org/abs/2611.03768](https://arxiv.org/abs/2611.03768)
**Summary:** The Multi-layer Indexer lets sparse-attention layers reuse the preceding indexer's token selection so indexing can overlap with attention, requiring no retraining or new weights and composing with IndexCache. Across DeepSeek-V3.2 and GLM-5 serving experiments, the authors report faster decoding than equal-retention IndexCache, reaching gains of 14.5 percent and 9.8 percent respectively at one-half retention while benchmark accuracy remains within a few percentage points.

---

### 15. Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization
**Authors:** Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su, Sreeram Vennam, Zhihao Jia, Samyam Rajbhandari
**arXiv:** [arxiv.org/abs/2611.03517](https://arxiv.org/abs/2611.03517)
**Summary:** KernelSeek directs a general-purpose coding agent with short questions at decision points and a minimal verifiable-goal harness rather than operator-specific optimization knowledge or a faster implementation to imitate. The authors report dependency-free FlashAttention forward kernels correct on 182 scenarios per architecture, with geometric-mean speeds of 1.16 times FlashAttention-3 on Hopper and 1.46 times FlashAttention-4 on Blackwell.

---

### 16. Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors
**Authors:** Siddharth Jain, Venkat N. Vedam
**arXiv:** [arxiv.org/abs/2610.36544](https://arxiv.org/abs/2610.36544)
**Summary:** This framework shows that restart-monitor accuracy alone cannot determine whether restarting improves agent success, because value depends on the replacement attempt's remaining-budget opportunity. It introduces decision-sufficiency criteria and a finite-sample audit that can abstain, with SymPy agent experiments finding no positive prospective replication of an initial apparent restart gain and no live comparison meeting the stated certification threshold.

---

### 17. TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation
**Authors:** Qijun Gan, Chenwei Zhang, Xinyang Li, Meiguang Jin, Junfeng Ma, Shen Qiu
**arXiv:** [arxiv.org/abs/2611.03394](https://arxiv.org/abs/2611.03394)
**Summary:** TaoMate-HD streams digital humans by establishing coarse video at low resolution, refining it in a final high-resolution step, and retaining audiovisual history across chunks and incoming text updates. The authors report 1.6-times faster generation than direct high-resolution sampling, a further 1.9-times overall gain from stage-parallel deployment, reduced speech character errors, and support for hour-long generation.

---

### 18. Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting
**Authors:** Raz Marshanski, Liran Nochumsohn, Mayank Jauhari, Boris N. Oreshkin, Omri Azencot
**arXiv:** [arxiv.org/abs/2611.04760](https://arxiv.org/abs/2611.04760)
**Summary:** The Koopman Generative Operator combines structured latent trajectory extrapolation, single-step flow generation through a matrix exponential, and adaptive per-variable and per-horizon uncertainty. The authors report leading accuracy on 13 of 17 ProbTS benchmarks in CRPS and 16 of 17 in NMAE, with at least 25-times lower inference time than the compared iterative generative models.

---

### 19. GaussianRenderFormer: Transformer-based Rendering of 3D Gaussian Splats
**Authors:** Shahaf Valencia Levy, Sagie Benaim
**arXiv:** [arxiv.org/abs/2611.05593](https://arxiv.org/abs/2611.05593)
**Summary:** GaussianRenderFormer learns to render an image directly from Gaussian tokens and camera-ray patches using a view-independent encoder and view-dependent decoder without a rasterizer. On 300 unseen objects, it reaches 38.08 dB PSNR versus 44.02 dB for rasterizing the same pruned inputs, with diagnostics suggesting a view-decoder bottleneck and leaving under-training unresolved.

---

### 20. Information Games: Strategic Crowding and Firm Repositioning in Language-Model Space
**Authors:** Marcus Gawronsky, Chun-Sung Huang
**arXiv:** [arxiv.org/abs/2609.37820](https://arxiv.org/abs/2609.37820)
**Summary:** This study represents company news and analyst reports as dense vectors to track how firms' information geometry changes as they respond to competitive market opportunities. It develops a model of costly capacity adjustment, studies predicted responses with a sandwich estimator and multi-agent simulation, and validates findings on reports about Nasdaq-listed companies from 2018 through 2022.
