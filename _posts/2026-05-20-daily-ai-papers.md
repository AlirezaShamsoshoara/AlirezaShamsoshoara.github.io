---
title: "Daily AI Papers — May 20, 2026"
date: 2026-05-20
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-20/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal-ai
  - rl-reasoning
  - video-generation
---

## #1 — When Vision Speaks for Sound

**Authors:** Xiaofei Wen, Wenjie Jacky Mo, Xingyu Fu, Rui Cai, Tinghui Zhu, Wendi Li, Yanan Xie, Muhao Chen, Peng Qi

**arxiv:** [arxiv.org/abs/2605.16403](https://arxiv.org/abs/2605.16403) | **Project:** [rakanwen.github.io/when-vision-speaks-for-sound](https://rakanwen.github.io/when-vision-speaks-for-sound/) | **Code:** [github.com/rakanWen/wvs-code](https://github.com/rakanWen/wvs-code)

**Sources:** HuggingFace Daily Papers (64 upvotes), arxiv

**Summary:** Video-capable multimodal LLMs exhibit an "audio-visual Clever Hans effect" — they appear to understand audio but actually exploit visual-acoustic correlations without verifying the audio stream at all. The paper introduces THUD, an intervention-driven probing framework with three counterfactual edits (Shift, Mute, Swap), and a two-stage alignment recipe that achieves +28pp improvement across intervention dimensions.

**Why trending:** Exposes a critical failure mode in today's state-of-the-art omni models (including closed-source models from Google and OpenAI), with practical diagnosis+fix. High relevance to multimodal AI safety.

---

## #2 — Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information

**Authors:** Guobin Shen, Xiang Cheng, Chenxiao Zhao, Lei Huang, Jindong Li, Dongcheng Zhao, Xing Yu

**arxiv:** [arxiv.org/abs/2605.11609](https://arxiv.org/abs/2605.11609) | **Code:** [github.com/FloyedShen/AntiSD](https://github.com/FloyedShen/AntiSD)

**Sources:** HuggingFace Daily Papers (60 upvotes), arxiv

**Summary:** Standard on-policy self-distillation for math reasoning fails because privileged context inflates teacher confidence on trivial tokens (connectives, verifiable claims) while suppressing deliberation tokens ("Wait", "Let", "Maybe") that drive multi-step search. AntiSD reverses the divergence direction and adds an entropy-triggered gate, reaching GRPO baseline accuracy in 2–10× fewer training steps with up to +11.5pp final accuracy gain on models from 4B–30B parameters.

**Why trending:** A clean PMI-based analysis that explains why self-distillation underperforms for reasoning, and a simple drop-in fix — directly relevant to the GRPO/RL-for-reasoning wave.

---

## #3 — GoLongRL: Capability-Oriented Long Context Reinforcement Learning with Multitask Alignment

**Authors:** Minxuan Lv, Tiehua Mei, Tanlong Du, Junmin Chen, Zhenpeng Su, Ziyang Chen, Ziqi Wang et al.

**arxiv:** [arxiv.org/abs/2605.19577](https://arxiv.org/abs/2605.19577) | **Code:** [github.com/xiaoxuanNLP/GoLongRL](https://github.com/xiaoxuanNLP/GoLongRL) | **Project:** [huggingface.co/collections/Kwai-Klear/golongrl](https://huggingface.co/collections/Kwai-Klear/golongrl)

**Sources:** HuggingFace Daily Papers (50 upvotes, 23 GitHub stars), arxiv

**Summary:** GoLongRL is a fully open-source post-training recipe for long-context RLVR, releasing a 23K-sample dataset spanning 9 task types with natural evaluation metrics and a complete construction pipeline. It introduces TMN-Reweight (task-level mean normalization + difficulty-adaptive weighting), and the resulting Qwen3-30B-A3B model matches DeepSeek-R1-0528 and Qwen3-235B-A22B performance on long-context tasks.

**Why trending:** Open-source challenge to closed-source long-context RL data; the dataset alone outperforms QwenLong-L1.5 under identical GRPO training.

---

## #4 — OpenComputer: Verifiable Software Worlds for Computer-Use Agents

**Authors:** Jinbiao Wei, Qianran Ma, Yilun Zhao, Xiao Zhou, Kangqi Ni

**arxiv:** [arxiv.org/abs/2605.19769](https://arxiv.org/abs/2605.19769) | **Code:** [github.com/echo0715/OpenComputer](https://github.com/echo0715/OpenComputer)

**Sources:** HuggingFace Daily Papers (50 upvotes, 10 GitHub stars), arxiv

**Summary:** OpenComputer is a verifier-grounded framework for building reproducible, grounded benchmarks for computer-use agents, integrating app-specific state verifiers, a self-evolving verification layer, a task-generation pipeline, and an agent execution harness over real desktop applications. It addresses the core problem that existing computer-use benchmarks rely on brittle screenshot matching or LLM-as-judge evaluation.

**Why trending:** Computer-use agents are a hot area; this paper directly tackles the evaluation bottleneck with a rigorous, scalable approach.

---

## #5 — Active Learners as Efficient PRP Rerankers

**Authors:** Jeremías Figueiredo Paschmann, Juan Kaplan, Francisco Nattero, Santiago Barron, Juan Wisznia

**arxiv:** [arxiv.org/abs/2605.14236](https://arxiv.org/abs/2605.14236) | **Code:** [github.com/jerecoder/IReranker](https://github.com/jerecoder/IReranker)

**Sources:** HuggingFace Daily Papers (46 upvotes), arxiv

**Summary:** Pairwise Ranking Prompting (PRP) uses LLMs to make pairwise comparisons for ranking, but standard sorting algorithms waste calls on redundant pairs given noisy, intransitive judgments. This paper reframes reranking as active learning — using uncertainty to select the most informative pairs — achieving top-k ranking quality with far fewer LLM calls than sorting baselines.

**Why trending:** LLM-as-judge / reranking is fundamental to RLHF pipelines and RAG systems; a principled efficiency gain here has broad applicability.

---

## #6 — AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration

**Authors:** Jiaqi Liu, Shi Qiu, Mairui Li, Bingzhou Li, Haonian Ji

**arxiv:** [arxiv.org/abs/2605.20025](https://arxiv.org/abs/2605.20025) | **Project:** [github.com/aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw)

**Sources:** HuggingFace Daily Papers (45 upvotes), arxiv

**Summary:** AutoResearchClaw models scientific discovery as an iterative, multi-perspective critique loop rather than a linear pipeline — agents challenge hypotheses from multiple angles, accumulate failures as lessons, and self-reinforce across cycles. Human-AI collaboration gates are built in so humans can redirect at critical junctions without breaking agent continuity.

**Why trending:** AI for science automation is a major 2026 theme; this paper provides a more realistic process model than single-shot "idea → paper" systems.

---

## #7 — Process Rewards with Learned Reliability (BetaPRM)

**Authors:** Jinyuan Li, Langlin Huang, Chengsong Huang, Shaoyang Xu, Donghong Cai

**arxiv:** [arxiv.org/abs/2605.15529](https://arxiv.org/abs/2605.15529) | **Code:** [github.com/JinYuanLi0012/Beta-Binomial-PRM](https://github.com/JinYuanLi0012/Beta-Binomial-PRM)

**Sources:** HuggingFace Daily Papers (43 upvotes), arxiv

**Summary:** Current Process Reward Models (PRMs) output a single scalar per reasoning step, forcing downstream methods to treat every prediction as equally trustworthy. BetaPRM models each step reward as a Beta-Binomial distribution, capturing both the predicted reward and learned uncertainty — enabling downstream reasoning algorithms to discount unreliable PRM predictions.

**Why trending:** PRMs are central to step-level RLHF and inference-time scaling for reasoning; adding calibrated uncertainty is an obvious but previously missing piece.

---

## #8 — EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL

**Authors:** Minrui Xu, Zilin Wang, Mengyi Deng, Zhiwei Li, Zhicheng Yang

**arxiv:** [arxiv.org/abs/2605.18703](https://arxiv.org/abs/2605.18703) | **Code:** [github.com/LARK-AI-Lab/EnvFactory](https://github.com/LARK-AI-Lab/EnvFactory)

**Sources:** HuggingFace Daily Papers (37 upvotes, *42 GitHub stars*), arxiv

**Summary:** EnvFactory addresses the two bottlenecks for agentic RL with tools: scarce, brittle execution environments and training data that lacks implicit human reasoning. It introduces a synthesis pipeline that automatically generates executable, sandboxed tool environments from API schemas, paired with robust RL training that handles environment failures gracefully.

**Why trending:** Highest GitHub traction in today's HF batch; tool-use agent training at scale is a core infrastructure problem for 2026.

---

## #9 — Stable Audio 3

**Authors:** Zach Evans, Julian D. Parker, Matthew Rice, CJ Carr, Zack Zukowski (Stability AI)

**arxiv:** [arxiv.org/abs/2605.17991](https://arxiv.org/abs/2605.17991)

**Sources:** Hacker News (25 points), arxiv

**Summary:** Stable Audio 3 is a family of fast latent diffusion models (small/medium/large) for variable-length audio generation and editing from Stability AI. Models support inpainting for targeted audio editing and continuation of recordings, with variable-length generation to avoid cost of full-length synthesis for short sounds.

**Why trending:** Major lab release from Stability AI; music/audio generation is a fast-growing segment and this is a significant architectural and capability update from the Stable Audio lineage.

---

## #10 — CogOmniControl: Reasoning-Driven Controllable Video Generation via Creative Intent Cognition

**Authors:** Hongji Yang, Songlian Li, Yucheng Zhou, Xiaotong Zhao, Alan Zhao

**arxiv:** [arxiv.org/abs/2605.19995](https://arxiv.org/abs/2605.19995) | **Project:** [um-lab.github.io/CogOmniControl](https://um-lab.github.io/CogOmniControl/)

**Sources:** HuggingFace Daily Papers (31 upvotes), arxiv

**Summary:** Existing diffusion-based video generation models break down under abstract, sparse, or professional conditions like storyboard sketches and clay renders. CogOmniControl couples a reasoning VLM to a diffusion backbone via a creative intent cognition module that interprets ambiguous conditions before injection, dramatically improving robustness in production workflows.

**Why trending:** Professional video generation workflows are a large market; reasoning-augmented controllability is the next frontier after raw quality improvements.

---

## #11 — Artifact-Bench: Evaluating MLLMs on Detecting and Assessing Artifacts of AI-Generated Videos

**Authors:** Yuqi Tang, Yang Shi, Zhuoran Zhang, Qixun Wang, Xuehai Bai

**arxiv:** [arxiv.org/abs/2605.18984](https://arxiv.org/abs/2605.18984) | **Code:** [github.com/FrankYang-17/Artifact-Bench](https://github.com/FrankYang-17/Artifact-Bench)

**Sources:** HuggingFace Daily Papers (21 upvotes), arxiv

**Summary:** As video generative models improve, their outputs still exhibit temporal inconsistencies, structural distortions, and semantic incoherence — but current MLLMs have no standardized benchmark for detecting such artifacts. Artifact-Bench fills this gap with a comprehensive evaluation suite testing MLLM perception and reasoning on AI-generated video artifacts.

**Why trending:** AI-generated content detection is increasingly important for trust/safety; this benchmark directly enables measuring MLLM progress on a critical task.

---

## #12 — Aurora: Unified Video Editing with a Tool-Using Agent

**Authors:** Yongsheng Yu, Ziyun Zeng, Zhiyuan Xiao, Zhenghong Zhou, Hang Hua

**arxiv:** [arxiv.org/abs/2605.18748](https://arxiv.org/abs/2605.18748) | **Code:** [github.com/yeates/Aurora](https://github.com/yeates/Aurora) | **Project:** [yongshengyu.com/Aurora-Page](https://www.yongshengyu.com/Aurora-Page/)

**Sources:** HuggingFace Daily Papers (15 upvotes, 10 GitHub stars), arxiv

**Summary:** Rather than a single unified diffusion model for all editing tasks, Aurora introduces a tool-using agent that decomposes natural language edit requests into a sequence of specialized video editing operations. The agent handles text, reference images, and spatial grounding automatically, freeing users from model-ready inputs.

**Why trending:** Agentic video editing is a practical step beyond raw generation; combining tool-use with video diffusion is a novel architecture approach.

---

## #13 — OmniGUI: Benchmarking GUI Agents in Omni-Modal Smartphone Environments

**Authors:** Felix Henry, Xiaochen Lin, Jiangyou Zhu, Yangfan, Bingqian Zhang

**arxiv:** [arxiv.org/abs/2605.18758](https://arxiv.org/abs/2605.18758) | **Code:** [github.com/omni-gui/OmniGUI](https://github.com/omni-gui/OmniGUI) | **Project:** [omni-gui.github.io](https://omni-gui.github.io/)

**Sources:** HuggingFace Daily Papers (12 upvotes, 9 GitHub stars), arxiv

**Summary:** Most GUI agent benchmarks rely on static screenshots, but real smartphone interaction requires processing transient audio cues and temporal video dynamics at the moment of action. OmniGUI is the first step-level GUI benchmark in omni-modal settings, covering audio + video + UI state jointly.

**Why trending:** GUI agents are a top practical use case for LLMs/VLMs; this is the first benchmark to match real-world multimodal complexity.

---

## #14 — CEPO: RLVR Self-Distillation via Contrastive Evidence Policy Optimization

**Authors:** Ahmed Heakl, Abdelrahman M. Shaker, Youssef Mohamed, Rania Elbadry, Omar Fetouh

**arxiv:** [arxiv.org/abs/2605.19436](https://arxiv.org/abs/2605.19436) | **Code:** [github.com/ahmedheakl/CEPO](https://github.com/ahmedheakl/CEPO)

**Sources:** HuggingFace Daily Papers (12 upvotes), arxiv

**Summary:** Under RLVR, correct solutions give all tokens the same reward regardless of whether they were decisive reasoning steps or grammatical filler. CEPO identifies the crucial "contrastive evidence" tokens by comparing the model's output with and without access to the correct answer, then applies policy optimization that up-weights these tokens.

**Why trending:** Complements the AntiSD paper (#2) — both address token-level reward signal quality in RL-for-reasoning, showing this is a hot sub-problem.

---

## #15 — MSAVBench: Comprehensive Evaluation of Multi-Shot Audio-Video Generation

**Authors:** Yujie Wei, Yujin Han, Zhekai Chen, Yongming Li, Kaixun Jiang

**arxiv:** [arxiv.org/abs/2605.20183](https://arxiv.org/abs/2605.20183)

**Sources:** HuggingFace Daily Papers (11 upvotes), arxiv

**Summary:** Video generation is evolving from single-shot clips to complex multi-shot audio-video narratives, but existing evaluation pipelines are too narrow and inflexible to benchmark modern MSAV models systematically. MSAVBench introduces a comprehensive, diverse benchmark covering both quality and consistency across multi-shot sequences.

**Why trending:** Long-form video generation (film-length content) is the next frontier; proper evaluation is a prerequisite for progress.

---

## #16 — Harnessing LLM Agents with Skill Programs (HASP)

**Authors:** Hongjun Liu, Yifei Ming, Shafiq Joty, Chen Zhao

**arxiv:** [arxiv.org/abs/2605.17734](https://arxiv.org/abs/2605.17734)

**Sources:** HuggingFace Daily Papers (11 upvotes), arxiv

**Summary:** Reusable skills for LLM agents are typically encoded as text descriptions that are advisory rather than executable. HASP reframes skills as executable programs with explicit invocation logic — when conditions are met, the skill code directly intervenes in the agent loop rather than simply providing guidance.

**Why trending:** Skill-based agent memory/adaptation is a key area for long-horizon agentic tasks; making skills executable rather than advisory is a significant architectural shift.

---

## #17 — Semantic Generative Tuning for Unified Multimodal Models (SGT)

**Authors:** Songsong Yu, Yuxin Chen, Ying Shan, Yanwei Li

**arxiv:** [arxiv.org/abs/2605.18714](https://arxiv.org/abs/2605.18714) | **Code:** [github.com/song2yu/SGT](https://github.com/song2yu/SGT) | **Project:** [song2yu.github.io/SGT](https://song2yu.github.io/SGT/)

**Sources:** HuggingFace Daily Papers (7 upvotes, *45 GitHub stars — highest today*), arxiv

**Summary:** Unified multimodal models independently optimize understanding via sparse text signals and generation via dense pixel objectives, creating misaligned representation spaces. SGT bridges this with semantic generative tuning — aligning the representation space by tying the generation objective to semantic understanding targets, without architectural changes.

**Why trending:** Highest GitHub stars in today's full HF batch (45), indicating strong practitioner interest; unified multimodal models (understanding + generation) are the dominant architecture trend.

---

## #18 — PixVerve: Advancing Native UHR Image Generation to 100MP

**Authors:** Haojun Chen, Haoyang He, Chengming Xu, Qingdong He, Junwei Zhu

**arxiv:** [arxiv.org/abs/2605.20147](https://arxiv.org/abs/2605.20147) | **Code:** [github.com/HaojunChen663/PixVerve-95K](https://github.com/HaojunChen663/PixVerve-95K) | **Project:** [haojunchen663.github.io/projects/PixVerve](https://haojunchen663.github.io/projects/PixVerve/)

**Sources:** HuggingFace Daily Papers (8 upvotes), arxiv

**Summary:** Text-to-image generation has stalled around 1K–2K resolution while demand for ultra-high-resolution (UHR) content is growing. PixVerve introduces a large-scale 95K high-quality UHR dataset and a native generation architecture that scales to 100 megapixels without tiling artifacts.

**Why trending:** 100MP native generation is a milestone; the dataset release enables the broader community to push UHR research.

---

## #19 — Video Models Can Reason with Verifiable Rewards (VideoRLVR)

**Authors:** Tinghui Zhu, Sheng Zhang, James Y. Huang, Selena Song, Xiaofei Wen

**arxiv:** [arxiv.org/abs/2605.15458](https://arxiv.org/abs/2605.15458) | **Code:** [github.com/luka-group/VideoRLVR](https://github.com/luka-group/VideoRLVR) | **Project:** [darthzhu.github.io/VideoRLVR-page](https://darthzhu.github.io/VideoRLVR-page/)

**Sources:** HuggingFace Daily Papers (8 upvotes), arxiv

**Summary:** Video diffusion models optimize for perceptual realism rather than verifiable reasoning, limiting their use in tasks with explicit spatial, temporal, or logical constraints. VideoRLVR applies RLVR to video generation, training models to satisfy verifiable conditions (physics, causality, instructions) with reward signals rather than pure pixel-level supervision.

**Why trending:** Extends the RLVR paradigm from language to video — a natural and impactful generalization as video models mature.

---

## #20 — Generative Recursive Reasoning (GRR)

**Authors:** Junyeob Baek, Mingyu Jo, Minsu Kim, Mengye Ren, Yoshua Bengio, Sungjin Ahn

**arxiv:** [arxiv.org/abs/2605.19376](https://arxiv.org/abs/2605.19376)

**Sources:** Hacker News (2 points), arxiv

**Summary:** Recursive Reasoning Models (RRMs) perform iterative latent-state refinement as an alternative to autoregressive sequence extension for extended computation. GRR makes RRMs stochastic by introducing latent trajectory sampling, enabling exploration across multiple reasoning paths and achieving better coverage on hard reasoning tasks with a 10M parameter model.

**Why trending:** Yoshua Bengio co-authorship signals academic weight; the approach offers a fundamentally different compute-scaling path from chain-of-thought token extension.
