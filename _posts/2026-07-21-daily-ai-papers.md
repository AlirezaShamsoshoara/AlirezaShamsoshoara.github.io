---
title: "Daily AI Papers — July 21, 2026"
date: 2026-07-21
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-21/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - video-understanding
  - embodied-ai
  - reinforcement-learning
---

## 1. TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs

**Authors:** Yuhan Zhu, Changlian Ma, Xiangyu Zeng, Xinhao Li, Zhiqiu Zhang, Songze Li, Jun Zhang, Tianxiang Jiang, Yuandong Yang, Ziang Yan, Zikang Wang, Xinyu Chen, Haoran Chen, Shaowei Zhang, Limin Wang

TimeLens2 tackles generalist video temporal grounding, where a single model must predict a variable-cardinality set of evidence intervals across video lengths, domains, query forms, and viewpoints. The authors identify shortcomings in existing training strategies for video MLLMs and propose a new approach for jointly describing and precisely localizing evidence in video.

**arXiv:** [arxiv.org/abs/2607.17423](https://arxiv.org/abs/2607.17423)
**Sources:** HuggingFace Daily Papers
**Why trending:** Highest engagement on HF Daily Papers today (126 upvotes), by far the top vote count in the entire day's cohort.

---

## 2. DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment

**Authors:** Xinyu Geng, Xuanhua He, Sixiang Chen, Yanjing Xiao, Fan Zhang, Shijue Huang, Haitao Mi, Zhenwen Liang, Tianqing Fang, Yi R. Fung

DeepSearch-World (built on DeepSearch-Evolve) introduces a self-distillation framework for training web/tool-use agents to improve from their own experience, addressing the weaknesses of fixed teacher-distilled trajectories (SFT) and sparse-reward RL for long-horizon interactions. The framework operates in a verifiable environment to provide denser, more reliable supervision signal.

**arXiv:** [arxiv.org/abs/2607.07820](https://arxiv.org/abs/2607.07820)
**Sources:** HuggingFace Daily Papers
**Why trending:** Second-highest HF engagement (69 upvotes, 3 comments) — strong interest in agentic search/self-improvement methods.

---

## 3. EvolvingWorld: An Open-Schema Framework for Co-Evolving Role-Play Agents and World Model in Interactive Literary World

**Authors:** Qing Zong, Yue Guo, Mengxin Yang, Yiwen Guo, Yangqiu Song

EvolvingWorld is a framework and benchmark for character-and-world co-evolution in interactive literary simulations, moving beyond static persona imitation or isolated scene generation. It models how characters and the surrounding world evolve jointly over time in open-ended narrative settings.

**arXiv:** [arxiv.org/abs/2607.17250](https://arxiv.org/abs/2607.17250)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL recent listing
**Why trending:** 67 HF upvotes plus independent confirmation as a fresh submission on the arXiv cs.CL recent list.

---

## 4. SWE-Pruner Pro: The Coder LLM Already Knows What to Prune

**Authors:** Yuhang Wang, Yuling Shi, Shaoqiu Zhang, Jialiang Liang, Shilin He, Siyu Ye, Yuting Chen, Kai Cai, Xiaodong Gu

SWE-Pruner Pro studies context pruning for coding agents, finding that the coder LLM itself already encodes internal representations that indicate the relevance of tool-output context, without needing a separate classifier as prior work (SWE-Pruner) required. This enables more efficient context management for long-running software-engineering agents.

**arXiv:** [arxiv.org/abs/2607.18213](https://arxiv.org/abs/2607.18213)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL recent listing
**Why trending:** 64 HF upvotes and cross-listed on arXiv cs.CL recent — strong signal given ongoing interest in efficient coding-agent infrastructure.

---

## 5. HOMIE: Human-object Centric Video Personalization via Multimodal Intelligent Enhancement

**Authors:** Yiyang Cai, Nan Chen, Rongchang Xie, Junwen Pan, Chunyang Jiang, Cheng Chen, Wen Zhou, Zhenbang Sun, Wei Xue, Wenhan Luo, Yike Guo

HOMIE addresses human-object centric video personalization (HOCVP), a core subtask of subject-driven video generation, tackling the difficulty of balancing high subject fidelity with accurate human-object interaction patterns. It proposes a multimodal enhancement pipeline to improve personalized video generation quality.

**arXiv:** [arxiv.org/abs/2607.18217](https://arxiv.org/abs/2607.18217)
**Sources:** HuggingFace Daily Papers, HuggingFace Trending, arXiv cs.CV recent listing
**Why trending:** The only paper today confirmed on three independent surfaces (HF Daily, HF Trending, and arXiv cs.CV recent), indicating unusually broad cross-platform pickup for a video-generation paper.

---

## 6. Apple-π: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence

**Authors:** Runmao Yao, Kairui Hu, Yukang Cao, Ruisi Wang, Shulin Tian, Ziang Cao, Weichen Fan, Ziqi Huang, Yuhao Dong, Hao Li, Zhaoxi Chen, Zhongang Cai, Lei Yang, Ziwei Liu

Apple-π introduces the first benchmark that evaluates whether video generation "world models" reach physically plausible outputs through a faithful, law-grounded reasoning process, rather than judging plausibility only at the output level. It targets the gap between apparent physical realism and genuine understanding of physical law in generative video models.

**arXiv:** [arxiv.org/abs/2607.16401](https://arxiv.org/abs/2607.16401)
**Sources:** HuggingFace Daily Papers
**Why trending:** 36 HF upvotes — reflects sustained community interest in evaluating "world model" claims for video generators.

---

## 7. RynnBrain 1.1: Towards More Capable and Generalizable Embodied Foundation Model

**Authors:** Kehan Li, Bohan Hou, Minghao Zhu, Tianyi Zhang, Zesen Cheng, Zhikai Wang, Sicong Leng, Xin Li, Xiao Lin, Biying Yao, Minghua Zeng, Jiangpin Liu, Ronghao Dang, Jiayan Guo, Siteng Huang, Haoyu Zhao, Heng Ping, Yaxi Zhao, Kexiang Wang, Tong Lu, and additional co-authors

RynnBrain 1.1 is a family of embodied foundation models at 2B, 9B, and 122B-A10B scales, trained with a unified spatio-temporal, physically-grounded framework for embodied perception, spatial reasoning, localization, and planning. Compared to RynnBrain 1.0, it adds contact-point prediction and broader generalization capability.

**arXiv:** [arxiv.org/abs/2607.17977](https://arxiv.org/abs/2607.17977)
**Sources:** HuggingFace Daily Papers
**Why trending:** 31 HF upvotes — a major multi-scale embodied-AI foundation model release draws strong interest.

---

## 8. GigaChat Audio: Time-aware Large Audio Language Model

**Authors:** Aleksandr Kutsakov, Mariia Sadovina, Georgii Gospodinov, Alexandr Maximenko, Oleg Kutuzov, Pavel Bogomolov, Fyodor Minkin

GigaChat Audio is a time-aware audio LLM that can answer questions with explicit timestamps over recordings up to 120 minutes long, interleaving periodic time markers with continuous audio tokens. It is trained with large-scale synthetic supervision from a cascaded data-generation pipeline to solve temporal grounding in long-form audio.

**arXiv:** [arxiv.org/abs/2607.10387](https://arxiv.org/abs/2607.10387)
**Sources:** HuggingFace Daily Papers
**Why trending:** 29 HF upvotes — notable interest in long-context, time-grounded audio LLMs from the GigaChat ecosystem.

---

## 9. GigaAM Multilingual: Foundation Model for Underrepresented Languages

**Authors:** Andrei Kuzmenko, Alexandr Maximenko, Aleksandr Kutsakov, Georgii Gospodinov, Dmitrii Bolotov, Oleg Kutuzov, Pavel Bogomolov, Fyodor Minkin

GigaAM Multilingual is a Conformer-encoder-based foundation model targeting robust ASR for underrepresented Central Asian languages (Kazakh, Kyrgyz, Uzbek), addressing severe long-tail data scarcity in multilingual speech recognition. It builds on the GigaAM line of speech models with a multilingual pretraining recipe.

**arXiv:** [arxiv.org/abs/2607.10371](https://arxiv.org/abs/2607.10371)
**Sources:** HuggingFace Daily Papers
**Why trending:** 27 HF upvotes — companion release to GigaChat Audio, drawing related community attention to low-resource speech models.

---

## 10. ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams

**Authors:** Xiaokang Ma, Yifan Sun, Zhihong Jin, Jie Gu, Yudong Luo, Shenyi Shao, Chu Tang, Jingmin Chen, Li Pu

ReflectWorld-MM proposes an entity-oriented multimodal memory system for assistants that continually watch open-ended video streams, aiming to overcome the limits of keeping memory purely inside a model's context window. It targets long-term reasoning over accumulated multimodal experience for streaming-video agents.

**arXiv:** [arxiv.org/abs/2607.09759](https://arxiv.org/abs/2607.09759)
**Sources:** HuggingFace Daily Papers
**Why trending:** 23 HF upvotes with above-average comment activity (4 comments) — active discussion around long-term multimodal memory architectures.

---

## 11. Group Entropy-Controlled Policy Optimization

**Authors:** Guangran Cheng, Chengqi Lyu, Songyang Gao, Wenwei Zhang, Kai Chen

This paper studies entropy control in RL post-training of LLMs, noting that training on mixtures of heterogeneous tasks induces distinct entropy regimes under the same policy, which undermines global or token-level entropy-control schemes. It proposes a group-level entropy-controlled policy optimization method to better balance exploration and exploitation across heterogeneous task mixtures.

**arXiv:** [arxiv.org/abs/2607.16850](https://arxiv.org/abs/2607.16850)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL recent listing
**Why trending:** 22 HF upvotes plus independent confirmation on arXiv cs.CL recent — continued strong interest in RLHF/RLVR training dynamics.

---

## 12. FlowMimic: Mask-free Visual Editing and Generation with Pixel-pair Warped Flow Field for Online Video Editing Data Generation and Modality Mimicry

**Authors:** Dingyun Zhang, Lixue Gong, Wei Liu

FlowMimic unifies generation and editing for video/image modalities in a single model, replacing labor-intensive mask-annotation pipelines for collecting video-editing data with a pixel-pair warped flow field approach. This enables scalable, mask-free online data generation and modality mimicry for video editing.

**arXiv:** [arxiv.org/abs/2607.18227](https://arxiv.org/abs/2607.18227)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV recent listing
**Why trending:** 20 HF upvotes and cross-listed on arXiv cs.CV recent — interest in scalable, annotation-free video-editing data pipelines.

---

## 13. Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning

**Authors:** Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen, Qingze Guan, Zhengxing Wu, Wanke Zhan, Yang Sun, Zhiyi Huang, and additional co-authors

Open-AoE is an open, community-oriented egocentric-manipulation dataset and toolchain, combining low-cost continuous capture with manipulation-level structured annotations and reusable robot-learning tools. It addresses the scarcity of resources that combine all three properties for scalable embodied-intelligence supervision.

**arXiv:** [arxiv.org/abs/2607.14183](https://arxiv.org/abs/2607.14183)
**Sources:** HuggingFace Daily Papers
**Why trending:** 20 HF upvotes — strong interest in open datasets/toolchains for embodied learning from egocentric video.

---

## 14. Environment-free Synthetic Data Generation for API-Calling Agents

**Authors:** Seanie Lee, Sanjoy Chowdhury, Chao Jiang, Cheng-Yu Hsieh, Ting-Yao Hu, Alexander T Toshev, Oncel Tuzel, Raviteja Vemulapalli

This paper proposes a method to generate high-quality training trajectories for API-calling LLM agents without needing fully implemented environments with executable APIs and realistic backend databases. This removes a major scalability bottleneck for training tool-use agents at scale.

**arXiv:** [arxiv.org/abs/2607.16900](https://arxiv.org/abs/2607.16900)
**Sources:** HuggingFace Daily Papers
**Why trending:** 13 HF upvotes — practical interest in reducing infrastructure cost for agent training data generation.

---

## 15. Do Language Models Dream of Binding Molecules? Benchmarking LLMs under Spatial Constraints

**Authors:** Thomas MacDougall, Maksim Kuznetsov, Roman Schutski, Rim Shayakhmetov, Maxim Malkov, Vladimir Aladinskiy, Alex Aliper, Alex Zhavoronkov

This paper benchmarks LLM-based methods against diffusion models for structure-based drug design (SBDD), which leverages 3D protein-target structure and spatial constraints to generate candidate binding molecules. It evaluates how well LLM-based molecular design methods handle spatial constraints compared to the dominant diffusion-model paradigm.

**arXiv:** [arxiv.org/abs/2607.18144](https://arxiv.org/abs/2607.18144)
**Sources:** HuggingFace Daily Papers, arXiv cs.LG recent listing
**Why trending:** 11 HF upvotes plus arXiv cs.LG cross-listing — niche but notable crossover interest between LLMs and drug discovery.

---

## 16. DiffGI: Differentiable Geometry Images for High-Fidelity Thin-Shell 3D Generation

**Authors:** Eungjune Shim, Hansol Lee, Eunjung Ju

DiffGI proposes a surface-centric, geometry-image-based alternative to implicit volumetric 3D generative models, which struggle to represent thin-shell and non-manifold geometries such as garments. It replaces discrete binary occupancy maps with a differentiable geometry-image representation for higher-fidelity thin-shell generation.

**arXiv:** [arxiv.org/abs/2607.13365](https://arxiv.org/abs/2607.13365)
**Sources:** HuggingFace Daily Papers
**Why trending:** 10 HF upvotes — steady interest in improved representations for 3D generative modeling of thin/non-manifold shapes.

---

## 17. HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis

**Authors:** Lingwei Dang, Juntong Li, Zonghan Li, Hongwen Zhang, Liang An, Wei Min, Yebin Liu, Qingyao Wu

HarmoHOI is a unified diffusion framework for multi-view-consistent hand-object interaction (HOI) synthesis, jointly generating synchronized appearance and 3D motion despite complex hand motions and occlusions. It targets applications in animation production and embodied AI that require realistic HOI content.

**arXiv:** [arxiv.org/abs/2607.17097](https://arxiv.org/abs/2607.17097)
**Sources:** HuggingFace Daily Papers
**Why trending:** 8 HF upvotes — continued interest in hand-object interaction synthesis for animation and embodied-AI pipelines.

---

## 18. LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks

**Authors:** Tianzhu Ye, Li Dong, Guanheng Chen, He Zhu, Xun Wu, Shaohan Huang, Furu Wei

This paper proposes Experiential Learning (EL), which repurposes an LLM-as-a-Judge feedback model into an "LLM-as-a-Coach" that preserves rich textual feedback instead of compressing evaluation into a single scalar reward. This aims to give richer training signal for RL on open-ended, non-verifiable tasks where standard reward scalarization loses information.

**arXiv:** [arxiv.org/abs/2607.18110](https://arxiv.org/abs/2607.18110)
**Sources:** HuggingFace Daily Papers, arXiv cs.LG recent listing
**Why trending:** 7 HF upvotes plus arXiv cs.LG cross-listing — from a well-known Microsoft Research author group (Furu Wei et al.), drawing attention despite modest raw upvote count.

---

## 19. Distilled Reinforcement Learning for LLM Post-training

**Authors:** Chen Wang, Zhaochun Li, Jionghao Bai, Yining Zhang, Hexuan Deng, Ge Lan, Yue Wang

This paper studies LLM post-training methods, contrasting reinforcement learning (RL, which relies on coarse-grained outcome supervision and suffers from difficult credit assignment) with on-policy distillation (OPD). It proposes a distilled-RL approach intended to combine the strengths of both paradigms for post-training.

**arXiv:** [arxiv.org/abs/2607.17247](https://arxiv.org/abs/2607.17247)
**Sources:** HuggingFace Daily Papers
**Why trending:** 5 HF upvotes — part of the continuing wave of interest in LLM post-training method comparisons.

---

## 20. Token-Level Off-Policy Learning for Faithful Generation Under Distribution Shift

**Authors:** Zitong Huang, Gustavo Lucas Carvalho, Deqing Fu, Robin Jia

This paper introduces Token-Level Off-Policy Labeling (TOPL), which reframes post-training as a token-level correctness-prediction task, training models to distinguish good from bad tokens in a response. This aims to steer generation towards "good" tokens while avoiding failure modes of standard off-policy training under distribution shift.

**arXiv:** [arxiv.org/abs/2607.17524](https://arxiv.org/abs/2607.17524)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL recent listing
**Why trending:** 4 HF upvotes plus arXiv cs.CL cross-listing, edging out a same-upvote-count competitor for the last slot due to the extra cross-platform confirmation.
