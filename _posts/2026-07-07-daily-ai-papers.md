---
title: "Daily AI Papers — July 07, 2026"
date: 2026-07-07
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-07/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - gui-agents
  - embodied-ai
  - world-models
---

## #1 — UI-MOPD: Multi-Platform On-Policy Distillation for Continual GUI Agent Learning

**Authors:** Niu Lian, Alan Chen, Zhehao Yu, Chengzhen Duan, Fazhan Liu, Hui Liu, Pei Fu, Jian Luan, Yaowei Wang, Shu-Tao Xia, Jinpeng Wang  
**arXiv:** [arxiv.org/abs/2607.04425](https://arxiv.org/abs/2607.04425)  
**Sources:** HuggingFace Daily Papers (61 upvotes)  
**Why trending:** Highest-upvoted paper of the day. Introduces UI-MOPD, the first method combining multi-teacher on-policy distillation with continual learning for GUI agents. Accompanied by the Uni-GUI cross-platform dataset.

GUI agents increasingly need to operate across desktop and mobile simultaneously, but catastrophic forgetting and platform-specific behavioral drift make joint training hard. UI-MOPD addresses this by dynamically selecting a platform-specific teacher model and distilling its behavioral priors into a shared policy via platform-conditioned distillation. Achieves 38.2% task success on OSWorld and 12.0% on MobileWorld, outperforming prior continual-learning baselines.

---

## #2 — OmniOpt: Taxonomy, Geometry, and Benchmarking of Modern Optimizers

**Authors:** Siyuan Li, Jiabao Pan, Yumou Liu, Zhuoli Ouyang, Xin Jin, Xinglong Xu, Jingxuan Wei, Shengye Pang, Jintao Che, Xuanhe Zhou, Conghui He, Cheng Tan  
**arXiv:** [arxiv.org/abs/2607.04033](https://arxiv.org/abs/2607.04033)  
**GitHub:** [github.com/OpenRaiser/OmniOpt](https://github.com/OpenRaiser/OmniOpt)  
**Project:** [openraiser.github.io/OmniOpt](https://openraiser.github.io/OmniOpt/)  
**Sources:** HuggingFace Daily Papers (52 upvotes)  
**Why trending:** Comprehensive optimizer survey paper with working benchmark code. Extremely practical for large-scale training practitioners who have to choose among 100+ methods.

OmniOpt unifies over a hundred modern optimizers through a five-stage meta-pipeline and norm-constrained linear minimization oracles, then benchmarks them on a cross-domain suite spanning LLM pretraining to image classification. Provides a dual-dimension taxonomy mapping each optimizer to its mechanism family and training objective, giving practitioners a principled coordinate system for optimizer selection.

---

## #3 — PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space

**Authors:** Sensen Gao, Zhaoqing Wang, Qihang Cao, et al.  
**arXiv:** [arxiv.org/abs/2607.05373](https://arxiv.org/abs/2607.05373)  
**GitHub:** [github.com/SensenGao/PixWorld](https://github.com/SensenGao/PixWorld)  
**Project:** [sensengao.github.io/PixWorld](https://sensengao.github.io/PixWorld/)  
**Sources:** HuggingFace Daily Papers (44 upvotes)  
**Why trending:** Tackles the longstanding separation between 3D reconstruction (pixel regression) and 3D generation (latent diffusion) in a unified pixel-space model with demonstrated results.

PixWorld argues that latent-space unification loses information critical for geometric fidelity. By operating directly in pixel space with geometry-aware feature alignment and image-level supervision, it avoids the information loss introduced by encoder-decoder bottlenecks. The unified model handles both tasks without architectural changes, showing strong results on standard 3D benchmarks.

---

## #4 — ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster, Video, and Blog

**Authors:** Lingao Xiao, Yalun Dai, Yangyu Huang, Qihao Zhao, et al.  
**arXiv:** [arxiv.org/abs/2607.04438](https://arxiv.org/abs/2607.04438)  
**Project:** [aka.ms/ResearchStudio](https://aka.ms/ResearchStudio)  
**Sources:** HuggingFace Daily Papers (39 upvotes)  
**Why trending:** From Microsoft Research. Addresses a real pain point: converting papers into conference artifacts. Generates editable PowerPoint/Word outputs, unlike prior one-way renderers.

ResearchStudio-Reel composes specialized skills (poster, video script, blog) around a shared paper extractor, ensuring all artifacts stay consistent with the source contribution. Unlike previous approaches that grade quality with soft VLM-preference scores, it uses hard pass/fail quality gates that force regeneration when load-bearing sections are empty. Outputs are editable in standard office tools.

---

## #5 — ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes

**Authors:** Qihao Zhao, Yangyu Huang, Yalun Dai, Lingao Xiao, et al.  
**arXiv:** [arxiv.org/abs/2607.04439](https://arxiv.org/abs/2607.04439)  
**GitHub:** [github.com/microsoft/ResearchStudio](https://github.com/microsoft/ResearchStudio)  
**Project:** [aka.ms/ResearchStudio](https://aka.ms/ResearchStudio)  
**Sources:** HuggingFace Daily Papers (35 upvotes)  
**Why trending:** Companion paper to ResearchStudio-Reel. AI-assisted research ideation grounded in actual ML conference outcomes rather than free-form generation. Practical for the growing AI-for-science community.

ResearchStudio-Idea provides a skill suite covering literature search, novelty checking, and pattern-guided generation to produce traceable, evidence-grounded research proposals. It explicitly grounds ideas in current literature and evaluates differentiation from existing work before surfacing candidates, reducing the rate of near-duplicate proposals from AI ideation tools.

---

## #6 — GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation

**Authors:** GigaWorld Team, Angyuan Ma, Boyuan Wang, Bohan Li, et al.  
**arXiv:** [arxiv.org/abs/2607.02642](https://arxiv.org/abs/2607.02642)  
**GitHub:** [github.com/open-gigaai/giga-world-1](https://github.com/open-gigaai/giga-world-1)  
**Project:** [open-gigaai.github.io/giga-world-1](https://open-gigaai.github.io/giga-world-1/)  
**Sources:** HuggingFace Daily Papers (29 upvotes)  
**Why trending:** Important framing paper for robot evaluation infrastructure. Benchmarks what makes a world model useful for robot policy assessment rather than just visual quality.

Evaluating embodied robot foundation models requires slow, costly real-world rollouts — GigaWorld-1 proposes using world models as policy evaluators. Through systematic benchmarking, the paper finds that long-horizon rollout consistency and robot-specific controllability matter far more than short-term visual realism. This provides a principled roadmap for the robotics community building sim-to-real evaluation pipelines.

---

## #7 — Vision Pretraining for Dense Spatial Perception

**Authors:** Zelin Fu, Bin Tan, Changjiang Sun, Shaohui Liu, et al.  
**arXiv:** [arxiv.org/abs/2607.05247](https://arxiv.org/abs/2607.05247)  
**GitHub:** [github.com/Robbyant/lingbot-vision](https://github.com/Robbyant/lingbot-vision)  
**Project:** [technology.robbyant.com/lingbot-vision](https://technology.robbyant.com/lingbot-vision)  
**Sources:** HuggingFace Daily Papers (28 upvotes)  
**Why trending:** Directly relevant to embodied AI. Addresses the gap between semantic visual pretraining (which dominant ViT models optimize) and the sub-pixel geometric fidelity needed for depth estimation and manipulation.

Modern visual foundation models prioritize semantic invariance at the cost of spatial precision. This work proposes boundary-centric pretraining that learns sub-pixel representations specifically for dense spatial perception, improving depth estimation accuracy and downstream embodied AI task performance without additional architectural complexity.

---

## #8 — MANCE: Manifold Aware Concept Erasure

**Authors:** Matan Avitan, Yoav Goldberg, Yanai Elazar  
**arXiv:** [arxiv.org/abs/2607.03973](https://arxiv.org/abs/2607.03973)  
**GitHub:** [github.com/MatanAvitan/mance](https://github.com/MatanAvitan/mance)  
**Sources:** HuggingFace Daily Papers (23 upvotes)  
**Why trending:** Advances representation editing for model alignment and safety. Co-authored by Yanai Elazar (AI2/UW) with strong results on nonlinear concept removal, an open challenge.

MANCE proposes the Manifold Constraint Hypothesis: natural representations concentrate on lower-dimensional manifolds, and concept erasure should project updates onto these manifolds rather than operating in full ambient space. This prevents collateral damage to correlated concepts and achieves state-of-the-art results in nonlinear concept removal, improving alignment without degrading overall model utility.

---

## #9 — Wan-Streamer v0.2: Higher Resolution, Same Latency

**Authors:** Lianghua Huang, Zhi-Fan Wu, Yupeng Shi, Wei Wang, et al.  
**arXiv:** [arxiv.org/abs/2607.04443](https://arxiv.org/abs/2607.04443)  
**Project:** [wan-streamer.com](https://wan-streamer.com/)  
**Sources:** HuggingFace Daily Papers (22 upvotes)  
**Why trending:** Practical engineering result pushing real-time audio-visual interaction models forward. Doubles visual resolution (192×336 → 640×368) at the same ~200ms latency, enabling scene-grounded agent interactions.

Wan-Streamer v0.2 retains the v0.1 thinker-performer architecture but adds multi-GPU parallel processing to lift interactive video output from low-res to near-HD. The latency-preserving upgrade maintains 25 FPS real-time performance while enabling mid-shot agent posture and spatial awareness previously impossible at lower resolution.

---

## #10 — EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots

**Authors:** Heqing Yang, Yang Yi, Liyao Wang, Linqing Zhong, et al.  
**arXiv:** [arxiv.org/abs/2607.02646](https://arxiv.org/abs/2607.02646)  
**GitHub:** [github.com/Noietch/EVA-CLIENT](https://github.com/Noietch/EVA-CLIENT)  
**Project:** [colalab.net/projects/eva-client](https://colalab.net/projects/eva-client/)  
**Sources:** HuggingFace Daily Papers (22 upvotes)  
**Why trending:** Open-source infrastructure for robotics practitioners. Addresses the real pain of bridging policy servers and physical hardware in a single maintainable codebase.

EVA-Client provides a component-decoupled architecture sitting between a policy server and physical robot hardware, unifying data collection, inference, and evaluation into a single framework with inspectable execution workflows. It standardizes the policy iteration loop for real robots, reducing the engineering overhead that currently forces each lab to maintain its own bespoke deployment stack.

---

## #11 — InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization

**Authors:** Haoxiang Ma, Junhao Cai, Xiaoxu Xu, Hao Li, et al.  
**arXiv:** [arxiv.org/abs/2607.04988](https://arxiv.org/abs/2607.04988)  
**Project:** [internrobotics.github.io/internvla-a15.github.io](https://internrobotics.github.io/internvla-a15.github.io/)  
**Sources:** HuggingFace Daily Papers (17 upvotes)  
**Why trending:** From the InternRobotics team. Integrates future prediction in latent space with pretrained VLMs for robot manipulation, showing strong compositional generalization.

InternVLA-A1.5 addresses interference between heterogeneous objectives (understanding, prediction, action) in unified robot models by performing future prediction in latent rather than pixel space, preserving the semantics of the pretrained VLM backbone. This latent foresight enables efficient long-horizon manipulation with reduced task-switching degradation compared to prior architectures.

---

## #12 — Do All Visual Tokens Matter Equally? Object-Evidence Preserving Token Merging for Vision-Language Retrieval

**Authors:** Suhyeong Park, Junha Jung, Jungwoo Park, Jaewoo Kang  
**arXiv:** [arxiv.org/abs/2607.04605](https://arxiv.org/abs/2607.04605)  
**GitHub:** [github.com/dmis-lab/SaMer](https://github.com/dmis-lab/SaMer)  
**Project:** [suhyeong10.github.io/samer-project-page](https://suhyeong10.github.io/samer-project-page/)  
**Sources:** HuggingFace Daily Papers (14 upvotes)  
**Why trending:** Practical efficiency contribution for vision-language retrieval. Reduces storage costs significantly while preserving the fine-grained visual evidence that late-interaction models depend on.

SaMer (Salient Merging) proposes an object-aware token merging framework that compresses image-side tokens in multi-vector retrieval while preserving query-selectable object and region evidence. Unlike prior compression methods that can collapse critical visual evidence, SaMer achieves significant storage reduction with improved retrieval performance on standard vision-language benchmarks.

---

## #13 — KVpop: Key-Value Cache Compression with Predictive Online Pruning

**Authors:** Lukas Hauzenberger, Niklas Schmidinger, Anamaria-Roberta Hartl, David Stap, et al.  
**arXiv:** [arxiv.org/abs/2607.05061](https://arxiv.org/abs/2607.05061)  
**Sources:** HuggingFace Daily Papers (12 upvotes)  
**Why trending:** KV cache compression is a hot area for LLM inference efficiency. KVpop directly supervises eviction decisions using future-attention targets rather than static heuristics.

KV cache growth scales linearly with context length, making it a primary bottleneck in long-context inference. KVpop learns a fixed-budget eviction policy by supervising keep-or-drop decisions with future-attention ground truth, learning which tokens will matter rather than relying on proxy scores. This achieves high accuracy with a smaller cache footprint compared to existing heuristic eviction methods.

---

## #14 — dOPSD: On-Policy Self-Distillation for Diffusion Language Models

**Authors:** Phuong Tuan Dat, Qi Li, Xinchao Wang  
**arXiv:** [arxiv.org/abs/2607.04428](https://arxiv.org/abs/2607.04428)  
**GitHub:** [github.com/tuandattt/dOPSD](https://github.com/tuandattt/dOPSD)  
**Sources:** HuggingFace Daily Papers (12 upvotes)  
**Why trending:** Bridges the gap between diffusion LLMs and reasoning capability. Most post-training methods for dLLMs are off-policy — dOPSD uses the model's own denoising trajectories to stay on-policy.

Diffusion language models generate text by iterative masked denoising but struggle to benefit from RL-style post-training. dOPSD uses the model's internal denoising trajectories as training signal, creating on-policy self-distillation that avoids exposure bias from SFT and sparse rewards from RL. Applied to mathematical reasoning and code generation, it shows consistent improvements over both SFT and RL baselines on dLLMs.

---

## #15 — Multiplayer Interactive World Models with Representation Autoencoders

**Authors:** Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary, Chris Mulder, et al.  
**arXiv:** [arxiv.org/abs/2607.05352](https://arxiv.org/abs/2607.05352)  
**GitHub:** [github.com/mira-wm/mira](https://github.com/mira-wm/mira)  
**Project:** [mira-wm.com](https://mira-wm.com/)  
**Sources:** HuggingFace Daily Papers (11 upvotes)  
**Why trending:** First multiplayer world model for physically complex environments. Strong demo results with stable long-horizon rollouts; relevant for multi-agent simulation and game AI.

MIRA (Multiplayer Interactive Representation Autoencoder) extends world models from single-agent to multi-agent settings by conditioning on multiple action streams simultaneously, learning to attribute scene changes to the correct player. Trained on large-scale gameplay data in a highly dynamic physics-based environment, MIRA shows stable long-horizon rollouts across arbitrary combinations of simultaneous player actions.

---

## #16 — Perceptual Flow Matching for Few-Step Generative Modeling

**Authors:** Chuyang Zhao, Yifei Song, Hongfa Wang, Jianlong Yuan, et al.  
**arXiv:** [arxiv.org/abs/2607.03524](https://arxiv.org/abs/2607.03524)  
**GitHub:** [github.com/ZhaoChuyang/PFM](https://github.com/ZhaoChuyang/PFM)  
**Sources:** HuggingFace Daily Papers (9 upvotes)  
**Why trending:** Simple but effective improvement to flow matching. Moves velocity regression to perceptual feature space, substantially improving few-step generation quality — useful for anyone working on diffusion model efficiency.

Perceptual Flow Matching (PFM) replaces conventional VAE-latent velocity regression with supervision in a pretrained perceptual feature space. This simple change makes flow matching far more sample-efficient — achieving high-quality generation in 1–4 steps with significantly improved accuracy over standard flow matching, without changing the model architecture.

---

## #17 — Multi-Turn Agentic Scientific Literature Search via Workflow Induction (PaperPilot)

**Authors:** Jisen Li, Bingxuan Li, Nanyi Jiang, Xuying Ning, et al.  
**arXiv:** [arxiv.org/abs/2607.00597](https://arxiv.org/abs/2607.00597)  
**GitHub:** [github.com/mtilyxuegao/PaperPilot](https://github.com/mtilyxuegao/PaperPilot)  
**Project:** [paperpilot.papersearch.org](https://paperpilot.papersearch.org/)  
**Sources:** HuggingFace Daily Papers (9 upvotes)  
**Why trending:** Directly addresses the messy, iterative nature of real literature search. PaperPilot generates explicit, editable workflow programs that users can inspect and refine, unlike black-box search agents.

PaperPilot treats scientific literature search as a multi-turn dialogue where user intent evolves through interaction. Rather than relying on fixed pipelines or implicit language reasoning, it induces explicit executable workflows from user feedback, making search strategies inspectable and controllable. Controlled workflow corruption training improves robustness to underspecified queries.

---

## #18 — EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments

**Authors:** Deyao Zhu, Xin Zhou, Shengling Qin, Xuekai Zhu, et al.  
**arXiv:** [arxiv.org/abs/2607.05155](https://arxiv.org/abs/2607.05155)  
**Project:** [edge-bench.org](https://edge-bench.org/)  
**Sources:** HuggingFace Daily Papers (8 upvotes)  
**Why trending:** First empirical evidence of predictable scaling laws for online/RL-style learning from real environments — a missing piece in the agent scaling literature.

Analyzing ~38,000 hours of agent interaction with real-world environments across 134 diverse tasks, EdgeBench finds that overall performance follows log-sigmoid scaling laws and learning speed improves exponentially as task exposure increases. These results suggest that environment learning, like pretraining, may be predictable and amenable to controlled scaling — a key result for the agents-at-scale research program.

---

## #19 — LLM-as-a-Verifier: A General-Purpose Verification Framework

**Authors:** Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, et al.  
**arXiv:** [arxiv.org/abs/2607.05391](https://arxiv.org/abs/2607.05391)  
**GitHub:** [github.com/llm-as-a-verifier/llm-as-a-verifier](https://github.com/llm-as-a-verifier/llm-as-a-verifier)  
**Project:** [llm-as-a-verifier.com](https://llm-as-a-verifier.com/)  
**Sources:** HuggingFace Daily Papers (8 upvotes)  
**Why trending:** Positions verification as a new compute-scaling axis alongside pretraining and RL post-training. Practical framework showing consistent agent performance improvements across benchmarks.

LLM-as-a-Verifier argues that the ability to check solution correctness is orthogonal to generation capability and scales independently. The framework provides fine-grained probabilistic verification that can compose with any LLM, improving solution selection accuracy across math, code, and open-ended tasks. Benchmarks show that scaling verification compute yields reliable agent performance gains without retraining.

---

## #20 — MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing

**Authors:** Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
**arXiv:** [arxiv.org/abs/2607.05376](https://arxiv.org/abs/2607.05376)  
**Project:** [galfiebelman.github.io/mv-forcing](https://galfiebelman.github.io/mv-forcing/)  
**Sources:** HuggingFace Daily Papers (5 upvotes)  
**Why trending:** Solves a hard open problem: generating long, temporally coherent multi-view video of dynamic scenes, which prior methods couldn't do simultaneously.

MV-Forcing composes temporal and view-wise autoregression in a single diffusion framework using 4D geometric bridging — using sparse point clouds as a geometric anchor across frames and views — and spatio-temporal distillation to maintain consistency. Enables generation of arbitrarily long multi-view video of dynamic scenes while avoiding the view-inconsistency artifacts that plague separate-stream approaches.
