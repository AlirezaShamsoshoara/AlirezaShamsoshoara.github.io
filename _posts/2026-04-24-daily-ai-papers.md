---
title: "Daily AI Papers — April 24, 2026"
date: 2026-04-24
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-24/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal
  - world-models
  - agents
---

## 1. LLaTiSA: Towards Difficulty-Stratified Time Series Reasoning from Visual Perception to Semantics

- **Authors:** Yueyang Ding, HaoPeng Zhang, Rui Dai, Yi Wang, Tianyu Zong, et al. (7 total)
- **arXiv:** [arxiv.org/abs/2604.17295](https://arxiv.org/abs/2604.17295)
- **Sources:** HuggingFace Daily Papers (75 upvotes — top of the day), arXiv
- **Why trending:** Introduces HiTSR — an 83k-sample hierarchical time-series reasoning dataset with verified CoT trajectories — and a 4-level taxonomy formalizing TSR. The companion VLM-based model fuses visualized patterns with precision-calibrated tables and shows strong OOD generalization, addressing a long-standing fragmentation in time-series LLM evaluation.

## 2. WorldMark: A Unified Benchmark Suite for Interactive Video World Models

- **Authors:** Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, et al. (8 total)
- **arXiv:** [arxiv.org/abs/2604.21686](https://arxiv.org/abs/2604.21686)
- **Sources:** HuggingFace Daily Papers (29 upvotes), arXiv
- **Why trending:** First unified benchmark to put Genie, YUME, HY-World, Matrix-Game and others on apples-to-apples scenes via a shared WASD action vocabulary. Ships a 500-case test suite plus a public "World Model Arena" ([warena.ai](https://warena.ai)) for live side-by-side battles — directly attacks the comparability crisis in world-model research.

## 3. UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling

- **Authors:** Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, et al. (6 total)
- **arXiv:** [arxiv.org/abs/2604.19734](https://arxiv.org/abs/2604.19734)
- **Sources:** HuggingFace Daily Papers (25 upvotes), arXiv
- **Why trending:** Unified Latent Action Tokenizer that bridges human egocentric data and humanoid kinematics through a tri-branch cross-reconstruction (vision↔action) trick. Demonstrates zero-shot task transfer on humanoid sim and real hardware — a meaningful step toward scaling humanoid foundation models past the data bottleneck.

## 4. StyleID: A Perception-Aware Dataset and Metric for Stylization-Agnostic Facial Identity Recognition

- **Authors:** Kwan Yun, Changmin Lee, Ayeong Jeong, Youngseo Kim, Seungmi Lee, et al. (6 total)
- **arXiv:** [arxiv.org/abs/2604.21689](https://arxiv.org/abs/2604.21689)
- **Sources:** HuggingFace Daily Papers (18 upvotes), arXiv
- **Why trending:** Releases StyleBench-H (human verification judgments) and StyleBench-S (psychometric 2AFC supervision) for measuring facial identity across diffusion- and flow-matching-based stylization. Calibrating semantic encoders against human perception yields large robustness gains on artist-drawn portraits — a tooling gap many stylization papers have ignored.

## 5. Seeing Fast and Slow: Learning the Flow of Time in Videos

- **Authors:** Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, et al. (9 total)
- **arXiv:** [arxiv.org/abs/2604.21931](https://arxiv.org/abs/2604.21931)
- **Sources:** HuggingFace Daily Papers (13 upvotes), arXiv
- **Why trending:** Treats *time* as a first-class learnable visual concept: self-supervised playback-speed estimation curates the largest in-the-wild slow-motion dataset to date, then enables speed-conditioned generation and temporal super-resolution. Opens a fresh axis for video world models that reason about how events unfold.

## 6. COSPLAY: Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks

- **Authors:** Xiyang Wu, Zongxia Li, Guangyao Shi, Alexander Duffy, Tyler Marques, et al. (8 total)
- **arXiv:** [arxiv.org/abs/2604.20987](https://arxiv.org/abs/2604.20987)
- **Sources:** HuggingFace Daily Papers (10 upvotes), arXiv
- **Why trending:** Pairs an LLM decision agent with a learnable skill bank curated by a second skill-management agent — both co-evolve from unlabeled rollouts. An 8B base model beats four frontier-LLM baselines by >25% average reward across six game environments, a strong signal for skill-reuse architectures.

## 7. TingIS: Real-time Risk Event Discovery from Noisy Customer Incidents at Enterprise Scale

- **Authors:** Jun Wang, Ziyin Zhang, Rui Wang, Hang Yu, Peng Di, et al. (6 total)
- **arXiv:** [arxiv.org/abs/2604.21889](https://arxiv.org/abs/2604.21889)
- **Sources:** HuggingFace Daily Papers (9 upvotes), arXiv
- **Why trending:** Production-scale system handling 300k messages/day with P90 alert latency of 3.5 minutes and 95% high-priority discovery. Combines LLM-driven event linking, cascaded routing, and behavioral noise reduction — practical, deployed work that resonates with infra/SRE crowds.

## 8. Hybrid Policy Distillation for LLMs

- **Authors:** Wenhong Zhu, Ruobing Xie, Rui Wang, Pengfei Liu
- **arXiv:** [arxiv.org/abs/2604.20244](https://arxiv.org/abs/2604.20244)
- **Sources:** HuggingFace Daily Papers (9 upvotes), arXiv
- **Why trending:** Reframes LLM knowledge distillation as a unified token-level reweighted log-likelihood and proposes HPD, blending forward+reverse KL with off-policy data and lightweight on-policy sampling. Improves stability and final quality across math reasoning, dialogue, and code — a clean theory-driven contribution that practitioners can drop in.

## 9. VLAA-GUI: Knowing When to Stop, Recover, and Search — A Modular Framework for GUI Automation

- **Authors:** Qijun Han, Haoqin Tu, Zijun Wang, Haoyue Dai, Yiyang Zhou, et al. (14 total)
- **arXiv:** [arxiv.org/abs/2604.21375](https://arxiv.org/abs/2604.21375)
- **Sources:** HuggingFace Daily Papers (6 upvotes), arXiv
- **Why trending:** Three-component framework (Completeness Verifier, Loop Breaker, on-demand Search Agent) hits 77.5% on OSWorld and 61.0% on WindowsAgentArena — and three of five backbones (Opus 4.5/4.6, Gemini 3.1 Pro) surpass human performance on OSWorld in a single pass. Big numbers in a hot benchmark space.

## 10. Context Unrolling in Omni Models

- **Authors:** Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, et al. (19 total)
- **arXiv:** [arxiv.org/abs/2604.21921](https://arxiv.org/abs/2604.21921)
- **Sources:** HuggingFace Daily Papers (5 upvotes), arXiv
- **Why trending:** Unified multimodal model natively trained on text/image/video/3D/hidden-rep, with explicit "Context Unrolling" reasoning across modal representations before predicting. Strong scores on multimodal generation + understanding plus in-context generation across modalities.

## 11. EditCrafter: Tuning-free High-Resolution Image Editing via Pretrained Diffusion Model

- **Authors:** Kunho Kim, Sumin Seo, Yongjun Cho, Hyungjin Chung
- **arXiv:** [arxiv.org/abs/2604.10268](https://arxiv.org/abs/2604.10268)
- **Sources:** HuggingFace Daily Papers (5 upvotes), arXiv
- **Why trending:** Edits images at resolutions far above the T2I model's training resolution without any fine-tuning, using tiled inversion plus a noise-damped manifold-constrained CFG (NDCFG++). A pragmatic recipe for the "I have a 4K photo" problem most editing pipelines ignore.

## 12. UniGenDet: A Unified Generative-Discriminative Framework for Co-Evolutionary Image Generation and Generated Image Detection

- **Authors:** Yanran Zhang, Wenzhao Zheng, Yifei Li, Bingyao Yu, Yu Zheng, et al. (8 total)
- **arXiv:** [arxiv.org/abs/2604.21904](https://arxiv.org/abs/2604.21904)
- **Sources:** HuggingFace Daily Papers (3 upvotes), arXiv
- **Why trending:** Couples a generator and a generated-image detector via symbiotic multimodal self-attention so each improves the other (more interpretable detection ↔ higher-fidelity generation). Argues against the architectural divide between gen and det — relevant to the deepfake / authenticity arms race.

## 13. WebGen-R1: Incentivizing LLMs to Generate Functional and Aesthetic Websites with Reinforcement Learning

- **Authors:** Juyong Jiang, Chenglin Cai, Chansung Park, Jiasi Shen, Sunghun Kim, et al. (7 total)
- **arXiv:** [arxiv.org/abs/2604.20398](https://arxiv.org/abs/2604.20398)
- **Sources:** HuggingFace Daily Papers (3 upvotes), arXiv
- **Why trending:** End-to-end RL framework with a cascaded multimodal reward (structure + execution + aesthetics) that turns a 7B base into a multi-page website generator beating 72B open-source baselines and rivaling DeepSeek-R1 (671B) on functional success while exceeding it on rendering and aesthetics.

## 14. Trust but Verify: Introducing DAVinCI — A Framework for Dual Attribution and Verification in Claim Inference for Language Models

- **Authors:** Vipula Rawte, Ryan Rossi, Franck Dernoncourt, Nedim Lipka
- **arXiv:** [arxiv.org/abs/2604.21193](https://arxiv.org/abs/2604.21193)
- **Sources:** HuggingFace Daily Papers (2 upvotes), arXiv
- **Why trending:** Two-stage framework: attribute generated claims to internal components and external sources, then verify via entailment + confidence calibration. 5-20% gains on FEVER / CLIMATE-FEVER over verification-only baselines, with a modular pluggable implementation released.

## 15. Vista4D: Video Reshooting with 4D Point Clouds

- **Authors:** Kuan Heng Lin, Zhizheng Liu, Pablo Salamanca, Yash Kant, Ryan Burgert, et al. (12 total)
- **arXiv:** [arxiv.org/abs/2604.21915](https://arxiv.org/abs/2604.21915)
- **Sources:** HuggingFace Daily Papers (2 upvotes), arXiv
- **Why trending:** Re-synthesizes a video from a different camera trajectory by grounding both the input video and the target camera in a 4D point cloud — with static-pixel segmentation and multiview dynamic training to survive depth-estimation artifacts. Strong baseline for dynamic-scene expansion and 4D recomposition.

## 16. Coevolving Representations in Joint Image-Feature Diffusion (CoReDi)

- **Authors:** Theodoros Kouzelis, Spyros Gidaris, Nikos Komodakis
- **arXiv:** [arxiv.org/abs/2604.17492](https://arxiv.org/abs/2604.17492)
- **Sources:** HuggingFace Daily Papers (2 upvotes), arXiv
- **Why trending:** Lets the semantic representation space *evolve* during diffusion training via a lightweight learnable projection (with stop-gradient + normalization to prevent collapse). Works in both VAE-latent and pixel-space diffusion, yielding faster convergence and higher quality than fixed-rep counterparts.

## 17. Encoder-Free Human Motion Understanding via Structured Motion Descriptions (SMD)

- **Authors:** Yao Zhang, Zhuchenyang Liu, Thomas Ploetz, Yu Xiao
- **arXiv:** [arxiv.org/abs/2604.21668](https://arxiv.org/abs/2604.21668)
- **Sources:** HuggingFace Daily Papers (1 upvote), arXiv
- **Why trending:** Skips the motion encoder entirely — converts joint sequences into rule-based natural language describing joint angles, body-part motion, and global trajectory. Hits 66.7% BABEL-QA / 90.1% HuMMan-QA / R@1 0.584 on HumanML3D and ports across 8 LLMs with only LoRA — a refreshingly simple alternative to learned alignment.

## 18. Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI

- **Authors:** Hieu Man, Van-Cuong Pham, Nghia Trung Ngo, Franck Dernoncourt, Thien Huu Nguyen
- **arXiv:** [arxiv.org/abs/2604.21300](https://arxiv.org/abs/2604.21300)
- **Sources:** HuggingFace Daily Papers (1 upvote), arXiv
- **Why trending:** EAVAE separates style from content via supervised contrastive pretraining + dual-encoder VAE, with a discriminator that not only judges style/content matches but generates natural-language explanations for its decisions. SOTA on Amazon Reviews / PAN21 / HRS plus strong few-shot AI-text detection on M4.

## 19. Test-Time Adaptation for EEG Foundation Models: A Systematic Study under Real-World Distribution Shifts

- **Authors:** Gabriel Jason Lee, Jathurshan Pradeepkumar, Jimeng Sun
- **arXiv:** [arxiv.org/abs/2604.16926](https://arxiv.org/abs/2604.16926)
- **Sources:** HuggingFace Daily Papers (1 upvote), arXiv
- **Why trending:** Introduces NeuroAdapt-Bench and finds that gradient-based TTA methods *degrade* EEG foundation models under realistic distribution shifts, while optimization-free methods are stable — a useful negative result that should reset expectations for clinical EEG deployment.

## 20. PersonalAI: A Systematic Comparison of Knowledge Graph Storage and Retrieval Approaches for Personalized LLM Agents

- **Authors:** Mikhail Menschikov, Dmitry Evseev, Victoria Dochkina, Ruslan Kostoev, Ilia Perepechkin, et al. (8 total)
- **arXiv:** [arxiv.org/abs/2506.17001](https://arxiv.org/abs/2506.17001)
- **Sources:** HuggingFace Daily Papers, arXiv
- **Why trending:** External-memory framework built on AriGraph with a hybrid design supporting standard edges and two hyper-edge types for richer temporal/semantic representation. Compares A*, WaterCircles, beam search and hybrid retrieval across TriviaQA / HotpotQA / DiaASQ — a useful systematic baseline for the personalized-agent memory crowd.
