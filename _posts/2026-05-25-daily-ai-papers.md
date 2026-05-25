---
title: "Daily AI Papers — May 25, 2026"
date: 2026-05-25
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-25/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - text-to-image
  - multimodal
---

## #1 — SkillOpt: Executive Strategy for Self-Evolving Agent Skills

**Authors:** Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo
**Organization:** Microsoft Research
**arXiv:** [arxiv.org/abs/2605.23904](https://arxiv.org/abs/2605.23904)
**GitHub:** [github.com/microsoft/SkillOpt](https://github.com/microsoft/SkillOpt)
**Project:** [microsoft.github.io/SkillOpt](https://microsoft.github.io/SkillOpt/)
**Sources:** HuggingFace Daily Papers (147 upvotes), Papers With Code, arXiv

**Summary:** SkillOpt introduces the first systematic text-space optimizer for agent skills, treating skills as external agent state trained with the same discipline as model weights. A separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a skill document, accepting only changes that strictly improve a held-out validation score. Across six benchmarks, seven target models, and three execution harnesses (direct chat, Codex, Claude Code), SkillOpt is best or tied on all 52 evaluated cells. On GPT-5.5 it lifts average no-skill accuracy by +23.5 points in direct chat, +24.8 in Codex, and +19.1 in Claude Code.

**Why trending:** Massive 147 upvotes on HuggingFace; addresses a key bottleneck in agentic AI systems with rigorous optimizer-style skill training. Strong GitHub traction (72 stars). Microsoft Research pedigree and impressive benchmark dominance across top models.

---

## #2 — Lens: Rethinking Training Efficiency for Foundational Text-to-Image Models

**Authors:** Dong Chen, Fangyun Wei, Ziyu Wan, Dongdong Chen, Jiawei Zhang, Jinjing Zhao
**Organization:** Microsoft
**arXiv:** [arxiv.org/abs/2605.21573](https://arxiv.org/abs/2605.21573)
**GitHub:** [github.com/microsoft/Lens](https://github.com/microsoft/Lens)
**Sources:** HuggingFace Daily Papers (88 upvotes), arXiv, HuggingFace Hub

**Summary:** Lens is a 3.8B-parameter T2I model that matches or surpasses SOTA models with >6B parameters while requiring only ~19.3% of the training compute of Z-Image. The efficiency comes from maximizing data information density per training batch and architectural choices that reduce redundant computation. Lens demonstrates that carefully curated training strategies can compensate for smaller model scale.

**Why trending:** 88 HF upvotes and 113 GitHub stars. Directly challenges the "bigger is better" narrative in generative AI — a 3.8B model outperforming 6B+ models on training efficiency is a meaningful result for the community. Practical implications for democratizing T2I training.

---

## #3 — Rethinking Cross-Layer Information Routing in Diffusion Transformers

**Authors:** Chao Xu, Maohua Li, Qirui Li, Yixuan Xu, Yanke Zhou, Yunhe Li
**Organization:** RTP-LLM
**arXiv:** [arxiv.org/abs/2605.20708](https://arxiv.org/abs/2605.20708)
**Sources:** HuggingFace Daily Papers (82 upvotes), arXiv

**Summary:** Diffusion Transformers (DiTs) have had nearly every design axis revisited except the residual stream that governs cross-layer information flow, which has been inherited directly from the original Transformer. This paper presents a systematic empirical analysis of cross-layer information routing in DiTs, jointly analyzing how different routing strategies affect generation quality, training stability, and efficiency. The work proposes improved routing mechanisms that outperform standard residual connections.

**Why trending:** 82 upvotes — DiT architecture improvements are high-interest given their centrality to modern image/video generation. Fills a notable gap in DiT research by tackling the one design axis that had been overlooked.

---

## #4 — SciAtlas: A Large-Scale Knowledge Graph for Automated Scientific Research

**Authors:** Shuofei Qiao, Yunxiang Wei, Jiazheng Fan, Bin Wu, Busheng Zhang, Mengru Wang
**Organization:** University College London CS / Zhejiang University (ZJUNLP)
**arXiv:** [arxiv.org/abs/2605.22878](https://arxiv.org/abs/2605.22878)
**GitHub:** [github.com/zjunlp/SciAtlas](https://github.com/zjunlp/SciAtlas)
**Sources:** HuggingFace Daily Papers (44 upvotes), arXiv, Papers With Code

**Summary:** SciAtlas is a large-scale knowledge graph designed to combat the "information explosion" in academic research, going beyond keyword and vector-space retrieval to provide topological reasoning over complex interdisciplinary connections. It provides structured knowledge linking papers, methods, datasets, and findings to enable AI agents to perform deep scientific research. The system is designed to support agentic research workflows that require multi-hop reasoning across the scientific literature.

**Why trending:** 44 upvotes and 38 GitHub stars. Scientific AI agents and automated research are hot topics; this provides critical infrastructure for that paradigm. UCL/ZJUNLP collaboration gives it credibility.

---

## #5 — StepAudio 2.5 Technical Report

**Authors:** Bin Lin, Bo Zhao, Boyong Wu, Chao Yan, Chen Wu, Cheng Yi et al.
**arXiv:** [arxiv.org/abs/2605.23463](https://arxiv.org/abs/2605.23463)
**Sources:** HuggingFace Daily Papers (36 upvotes), arXiv

**Summary:** StepAudio 2.5 is a unified audio-language foundation model targeting ASR, TTS, and real-time spoken interaction — bridging the gap between generalist unified models and depth of specialized systems. The report details architectural innovations that allow a single model to match or exceed specialized baselines across multiple speech/audio tasks while maintaining the reasoning capabilities of large language models. It introduces improvements in streaming latency and multilingual ASR performance.

**Why trending:** 36 upvotes. Unified audio-language models are at the frontier of voice AI. StepFun has been pushing rapidly with the Step series and this technical report gives the community a detailed look at the architecture and training of a competitive speech foundation model.

---

## #6 — See What I Mean (SWIM): Aligning Vision and Language for Video Fine-grained Object Understanding

**Authors:** Boyuan Sun, Bowen Yin, Yuanming Li, Xihan Wei, Qibin Hou
**Organization:** TongyiLab (Tongyi / Alibaba)
**arXiv:** [arxiv.org/abs/2605.18018](https://arxiv.org/abs/2605.18018)
**GitHub:** [github.com/HumanMLLM/SWIM](https://github.com/HumanMLLM/SWIM)
**Sources:** HuggingFace Daily Papers (28 upvotes), arXiv

**Summary:** SWIM is a training strategy that aligns vision and language representations to enable fine-grained object understanding in video from textual prompts alone — no explicit visual prompts (masks or points) needed at inference. It uses mask supervision only during training to guide cross-modal attention, letting the model automatically attend to user-specified objects. Analysis of pretrained MLLMs reveals misalignment between visual attention and language intent, which SWIM directly corrects.

**Why trending:** 28 upvotes and 83 GitHub stars — strong community interest. Removing the need for visual prompts at inference is a key usability improvement for video understanding. Tongyi/Alibaba backing and a compelling open-source implementation drive traction.

---

## #7 — From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills

**Authors:** Zisu Huang, Jingwen Xu, Yifan Yang, Ziyang Gong, Qihao Yang, Muzhao Tian
**Organization:** Microsoft Research
**arXiv:** [arxiv.org/abs/2605.23899](https://arxiv.org/abs/2605.23899)
**Project:** [microsoft.github.io/SkillLens](https://microsoft.github.io/SkillLens/)
**Sources:** HuggingFace Daily Papers (22 upvotes), arXiv

**Summary:** This companion paper to SkillOpt provides the first comprehensive study spanning the full lifecycle of model-generated agent skills — from extraction through retrieval to consumption. It analyzes how different skill extraction strategies, storage formats, and retrieval methods affect downstream agent performance, and provides a unified evaluation framework called SkillLens. The study reveals that skill quality degrades predictably at each lifecycle stage and proposes best practices for robust skill pipelines.

**Why trending:** 22 upvotes. Pairs naturally with SkillOpt (#1) as a complementary empirical study — both from Microsoft Research and both advancing the emerging field of skill-based agent training.

---

## #8 — PhotoFlow: Agentic 3D Virtual Photography Missions

**Authors:** Jiarui Guo, Haojia Wei, Yiming Zhang, Yifei Liu, Yuning Gong, Hongjie Zhang
**Organization:** Visionary Laboratory
**arXiv:** [arxiv.org/abs/2605.23771](https://arxiv.org/abs/2605.23771)
**GitHub:** [github.com/Visionary-Laboratory/PhotoFlow](https://github.com/Visionary-Laboratory/PhotoFlow)
**Project:** [visionary-laboratory.github.io/PhotoFlow](https://visionary-laboratory.github.io/PhotoFlow/)
**Sources:** HuggingFace Daily Papers (20 upvotes), arXiv

**Summary:** PhotoFlow frames virtual photography as an agentic task: given a 3D scene and a language intent, an agent must infer suitable shots, select camera parameters, and render final photographs — with no preselected pose or reference image. It introduces a benchmark that jointly evaluates 3D spatial understanding and aesthetic judgment, two capabilities that are hard to measure together. The paper shows that current VLMs still struggle at this combined task, and PhotoFlow's agent achieves state-of-the-art performance.

**Why trending:** 20 upvotes and 24 GitHub stars. Creative AI + agentic 3D reasoning is a compelling combination. The benchmark aspect also gives the community something concrete to compete against.

---

## #9 — VGenST-Bench: A Benchmark for Spatio-Temporal Reasoning via Active Video Synthesis

**Authors:** Jinho Park, Youbin Kim, Hogun Park, Eunbyung Park
**arXiv:** [arxiv.org/abs/2605.22570](https://arxiv.org/abs/2605.22570)
**GitHub:** [github.com/zinosii/VGenST-Bench](https://github.com/zinosii/VGenST-Bench)
**Project:** [zinosii.github.io/VGenST-Bench](https://zinosii.github.io/VGenST-Bench/)
**Sources:** HuggingFace Daily Papers (18 upvotes), arXiv, Papers With Code

**Summary:** VGenST-Bench is a new benchmark for spatio-temporal reasoning in MLLMs that uses generative video models to actively synthesize evaluation data — going beyond static image sets or passively curated videos. By controlling exactly what spatial and temporal relationships appear in generated videos, it enables more precise evaluation of fine-grained spatio-temporal reasoning. Evaluation of leading MLLMs reveals significant gaps in their ability to reason about object motion, relative positions, and temporal sequences.

**Why trending:** 18 upvotes. Benchmarks that stress-test MLLM spatio-temporal reasoning are in demand as these models are deployed in robotics and autonomous systems. The generative synthesis approach is novel and more controllable than manual annotation.

---

## #10 — PiD: Fast and High-Resolution Latent Decoding with Pixel Diffusion

**Authors:** Yifan Lu, Qi Wu, Jay Zhangjie Wu, Zian Wang, Huan Ling, Sanja Fidler
**Organization:** NVIDIA Research
**arXiv:** [arxiv.org/abs/2605.23902](https://arxiv.org/abs/2605.23902)
**Project:** [research.nvidia.com/labs/sil/projects/pid](https://research.nvidia.com/labs/sil/projects/pid/)
**Sources:** HuggingFace Daily Papers (17 upvotes), arXiv

**Summary:** PiD replaces the reconstruction-oriented latent decoder in high-resolution text-to-image systems with a pixel diffusion model, enabling more expressive and efficient decoding at megapixel scale. Unlike standard VAE decoders that optimize for reconstruction fidelity, PiD synthesizes fine detail via a fast diffusion process that operates in pixel space. It is compatible with both latent diffusion and autoregressive generation pipelines and delivers significant improvements in detail quality without proportional compute overhead.

**Why trending:** 17 upvotes from NVIDIA Research. High-resolution generation is a major bottleneck and this tackles the decoder — an often overlooked component. NVIDIA's SIL lab has a strong track record and the pixel diffusion decoder framing is novel.

---

## #11 — RankE: End-to-End Post-Training for Discrete Text-to-Image Generation with Decoder Co-Evolution

**Authors:** Siyong Jian, Siyuan Li, Luyuan Zhang, Zedong Wang, Xin Jin, Ying Li
**Organization:** Westlake University
**arXiv:** [arxiv.org/abs/2605.21195](https://arxiv.org/abs/2605.21195)
**GitHub:** [github.com/syjmelody/RankE](https://github.com/syjmelody/RankE)
**Sources:** HuggingFace Daily Papers (14 upvotes), arXiv

**Summary:** RankE addresses Latent Covariate Shift in discrete AR text-to-image models — where policy-only post-training causes the token distribution to drift away from what the frozen VQ decoder was trained on. By jointly optimizing both the AR policy and the VQ decoder during post-training (decoder co-evolution), RankE eliminates this misalignment and significantly improves generation quality. The approach is analogous to REPA-E for continuous VAE-based models but applied to discrete tokenization.

**Why trending:** 14 upvotes. Discrete AR T2I models (like those behind GPT-4o image generation) are increasingly relevant, and fixing the decoder alignment bottleneck is practically important.

---

## #12 — ETCHR: Editing To Clarify and Harness Reasoning

**Authors:** Beichen Zhang, Yuhong Liu, Jinsong Li, Yuhang Zang, Jiaqi Wang, Dahua Lin
**Organization:** Intern Large Models (Shanghai AI Lab)
**arXiv:** [arxiv.org/abs/2605.23897](https://arxiv.org/abs/2605.23897)
**GitHub:** [github.com/InternLM/ETCHR](https://github.com/InternLM/ETCHR)
**Sources:** HuggingFace Daily Papers (9 upvotes), arXiv

**Summary:** ETCHR enables "thinking with images" for MLLMs by using a dedicated image editing model to generate clarifying intermediate images during visual reasoning chains — rather than relying on fixed tool sets or noisy unified multimodal generation. The editing model and understanding model are decoupled, enabling high-quality, focused intermediate visualizations that guide reasoning for questions requiring fine-grained focus or view transformations. ETCHR outperforms both tool-based and unified approaches on visual reasoning benchmarks.

**Why trending:** 9 upvotes. "Thinking with images" paradigm is gaining momentum as a natural extension of chain-of-thought for visual tasks. InternLM/Shanghai AI Lab has strong open-source credibility.

---

## #13 — SCOPE: Simulating Cross-game Operations in Playable Environments for FPS World Models

**Authors:** Zizhao Tong, Hongfeng Lai, Zeqing Wang, Zhaohu Xing, Kexu Cheng, Haoran Xu
**arXiv:** [arxiv.org/abs/2605.23345](https://arxiv.org/abs/2605.23345)
**GitHub:** [github.com/z2tong/SCOPE](https://github.com/z2tong/SCOPE)
**Project:** [z2tong.github.io/SCOPE](https://z2tong.github.io/SCOPE/)
**Sources:** HuggingFace Daily Papers (8 upvotes), arXiv

**Summary:** SCOPE addresses interactive world models for FPS games by observing that FPS actions are spatially selective: firing/reloading affects only a localized weapon region while camera/movement signals govern stable background dynamics. The model uses this spatial decomposition to handle high-frequency overlapping control signals at every frame without disrupting unaffected regions. It trains across multiple FPS titles, enabling cross-game generalization that previous single-title models could not achieve.

**Why trending:** 8 upvotes and 26 GitHub stars. World models for video games are a strong proxy for general world modeling, and FPS games are particularly demanding. The cross-game generalization angle and spatial action decomposition are novel.

---

## #14 — LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws

**Authors:** Xu Ouyang, Deyi Liu, Yuhang Cai, Jing Liu, Yuan Yang, Chen Zheng
**arXiv:** [arxiv.org/abs/2605.23901](https://arxiv.org/abs/2605.23901)
**Sources:** HuggingFace Daily Papers (7 upvotes), arXiv

**Summary:** Existing LLM scaling laws (monotonic power laws) fail to explain non-monotonic phenomena like catastrophic overtraining and quantization-induced degradation. This paper proposes the Shannon Scaling Law, modeling LLM training as information transmission over a noisy channel grounded in the Shannon-Hartley theorem. By mapping model parameters to channel bandwidth and training data to signal power, the framework predicts both the benefits of scaling and the failure modes — providing a unified theoretical basis for when scaling helps and when it hurts.

**Why trending:** 7 upvotes. A fresh theoretical angle on LLM scaling laws using information theory. The ability to explain catastrophic overtraining and quantization degradation — phenomena that current laws cannot predict — gives it immediate practical relevance.

---

## #15 — Geo-Align: Video Generation Alignment via Metric Geometry Reward

**Authors:** Zizun Li, Haoyu Guo, Runzhe Teng, Chunhua Shen, Tong He
**arXiv:** [arxiv.org/abs/2605.23903](https://arxiv.org/abs/2605.23903)
**GitHub:** [github.com/LiZizun/GeoAlign](https://github.com/LiZizun/GeoAlign)
**Project:** [lizizun.github.io/geo-align-page](https://lizizun.github.io/geo-align-page/)
**Sources:** HuggingFace Daily Papers (5 upvotes), arXiv

**Summary:** Geo-Align addresses the scarcity of synchronized multi-view real-world video data for camera-controlled video generation by using metric geometry rewards to align video generation with physical camera scales and trajectories. Instead of relying on SFT with synthetic datasets, it trains with geometry-based rewards that penalize deviations from physically accurate camera motion. This enables better generalization to out-of-distribution real-world videos compared to supervised fine-tuning approaches.

**Why trending:** 5 upvotes and 13 GitHub stars. Camera-controlled video generation is hot, and the geometry reward formulation offers a data-efficient alternative to large synthetic dataset collection.

---

## #16 — From Seeing to Thinking: Decoupling Perception and Reasoning Improves VLM Post-Training

**Authors:** Juncheng Wu, Hardy Chen, Haoqin Tu, Xianfeng Tang, Freda Shi, Hui Liu
**arXiv:** [arxiv.org/abs/2605.20177](https://arxiv.org/abs/2605.20177)
**GitHub:** [github.com/UCSC-VLAA/VLM-CapCurriculum](https://github.com/UCSC-VLAA/VLM-CapCurriculum)
**Project:** [ucsc-vlaa.github.io/VLM-CapCurriculum](https://ucsc-vlaa.github.io/VLM-CapCurriculum/)
**Sources:** HuggingFace Daily Papers (5 upvotes), arXiv

**Summary:** This paper challenges the assumption that VLM performance is limited by reasoning — finding instead that visual perception is the primary bottleneck. By decomposing VLM post-training into three sequential stages (visual perception, visual reasoning, textual reasoning) with specialized training at each stage, the approach consistently outperforms joint training. The perception-first curriculum reveals that long chain-of-thought reasoning provides little benefit when the model cannot first accurately perceive what it sees.

**Why trending:** 5 upvotes. Counterintuitive and practically important result — the community has been focused on reasoning improvements, and this reframes the problem as a perception bottleneck. UCSC VLAA lab is well-regarded in multimodal research.

---

## #17 — Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR

**Authors:** Chongyu Fan, Gaowen Liu, Mingyi Hong, Ramana Rao Kompella, Sijia Liu
**Organization:** OPTML Group @ MSU
**arXiv:** [arxiv.org/abs/2605.19282](https://arxiv.org/abs/2605.19282)
**GitHub:** [github.com/OPTML-Group/Pion](https://github.com/OPTML-Group/Pion)
**Project:** [chongyu-fan.netlify.app/posts/pion](https://chongyu-fan.netlify.app/posts/pion/)
**Sources:** HuggingFace Daily Papers (4 upvotes), arXiv

**Summary:** The Muon optimizer's uniform spectral whitening via Newton-Schulz iterations helps LLM pretraining but fails in two post-pretraining regimes: VLA training (where low-rank action gradients cause amplification of noise) and RLVR (where reward-signal dynamics are incompatible with uniform singular value normalization). The paper identifies the root cause as a high-pass filtering failure and proposes Pion, a modified optimizer with high-pass spectral remedies that restores Muon's benefits in these settings.

**Why trending:** 4 upvotes. Muon has been a hot optimizer in 2025-2026 and understanding its failure modes for VLA and RL fine-tuning is timely. Practical guide for teams adapting Muon to post-training workloads.

---

## #18 — LatentUMM: Dual Latent Alignment for Unified Multimodal Models

**Authors:** Yinyi Luo, Wenwen Wang, Hayes Bai, Marios Savvides, Jindong Wang
**Organization:** Carnegie Mellon University
**arXiv:** [arxiv.org/abs/2605.17766](https://arxiv.org/abs/2605.17766)
**Sources:** HuggingFace Daily Papers (4 upvotes), arXiv

**Summary:** Unified Multimodal Models (UMMs) often exhibit functional inconsistency between understanding and generation despite sharing a latent space — not because representations aren't shared, but because the transformations mapping into and out of the latent space are misaligned. LatentUMM introduces a dual latent alignment objective that explicitly aligns the encoder and decoder transformation paths, ensuring that generation and re-encoding follow consistent trajectories. This reduces semantic drift and improves both understanding and generation performance simultaneously.

**Why trending:** 4 upvotes. CMU group identifying a concrete alignment failure in UMMs and providing a principled fix. Relevant to any team building unified understanding-generation models.

---

## #19 — HINT-SD: Targeted Hindsight Self-Distillation for Long-Horizon Agents

**Authors:** Woongyeng Yeo, Yumin Choi, Taekyung Ki, Sung Ju Hwang
**Organization:** KAIST AI
**arXiv:** [arxiv.org/abs/2605.17873](https://arxiv.org/abs/2605.17873)
**Sources:** HuggingFace Daily Papers (3 upvotes), arXiv

**Summary:** Training long-horizon LLM agents with RL is hampered by sparse outcome rewards that reveal task success but not which intermediate actions failed or how to correct them. HINT-SD generates targeted hindsight hints only for critical failing turns — identified by a learned critic — rather than every turn, making feedback generation efficient and focused. Combined with self-distillation on the corrected trajectories, HINT-SD significantly improves performance on long-horizon agent benchmarks with substantially less compute than turn-level feedback methods.

**Why trending:** 3 upvotes. Long-horizon agent training is a core open problem and KAIST AI has been consistently strong in this space. The selective hindsight approach is elegant and efficient.

---

## #20 — Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers

**Authors:** Shuhong Zheng, Michael Oechsle, Erik Sandström, Marie-Julie Rakotosaona, Federico Tombari, Igor Gilitschenski
**Organization:** University of Toronto / Google
**arXiv:** [arxiv.org/abs/2605.23892](https://arxiv.org/abs/2605.23892)
**GitHub:** [github.com/zsh2000/gotohunt](https://github.com/zsh2000/gotohunt)
**Project:** [zsh2000.github.io/good-token-hunting](https://zsh2000.github.io/good-token-hunting.github.io/)
**Sources:** HuggingFace Daily Papers (2 upvotes), arXiv

**Summary:** Visual geometry transformers for multi-view 3D reconstruction face quadratic computational cost from global attention over long token sequences. This paper presents a systematic study of token selection strategies for these models — restricting key/value tokens each query attends to based on geometric priors (depth, surface normals, view overlap) — achieving significant speedups with minimal quality degradation. The work provides practical guidelines for building efficient 3D reconstruction transformers at scale.

**Why trending:** 2 upvotes and 7 GitHub stars. 3D reconstruction at scale is increasingly important for robotics and embodied AI. U of Toronto + Google collaboration and the systematic nature of the study make it a useful reference for practitioners.
