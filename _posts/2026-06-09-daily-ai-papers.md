---
title: "Daily AI Papers — June 09, 2026"
date: 2026-06-09
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-09/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - benchmarks
  - llm-agents
  - reasoning
---

## 1. SWE-Explore: Benchmarking How Coding Agents Explore Repositories

**Authors:** Shaoqiu Zhang, Yuhang Wang, Jialiang Liang, Yuling Shi, Wenhao Zeng, et al. (Shanghai Jiao Tong University)

**Summary:** SWE-bench and similar benchmarks treat repository-level bug fixing as a binary resolved/unresolved prediction problem, obscuring whether agents actually understand the codebase. SWE-Explore isolates repository exploration as a standalone skill, requiring agents to return a ranked list of relevant code regions under a fixed line budget; with 848 issues across 10 languages and 203 repos, it shows that agentic explorers form a clear tier above classical retrieval while line-level coverage and efficient ranking remain key differentiators.

**arxiv:** [arxiv.org/abs/2606.07297](https://arxiv.org/abs/2606.07297)

**GitHub:** [github.com/Qiushao-E/SWE-Explore-Bench](https://github.com/Qiushao-E/SWE-Explore-Bench) (10 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Surgical decomposition of a capability everyone uses but no one measures — fills a genuine evaluation gap in the coding-agent ecosystem.

---

## 2. On the Geometry of On-Policy Distillation

**Authors:** Zhennan Shen, Yanshu Li, Qingyu Yin, Chak Tou Leong, Zhilin Wang (Hong Kong University of Science and Technology)

**Summary:** On-policy distillation (OPD) is increasingly used to improve LLM reasoning but its training dynamics are opaque. This paper shows OPD operates in a "relaxed off-principal regime" relative to SFT and RLVR — fewer weights are affected, principal gradient directions are more strongly avoided — and exhibits "subspace locking" where cumulative updates rapidly collapse into a narrow low-dimensional channel that is functionally sufficient for OPD.

**arxiv:** [arxiv.org/abs/2606.07082](https://arxiv.org/abs/2606.07082)

**Sources:** HuggingFace Daily Papers

**Why trending:** Provides the first geometric characterization of OPD, offering theoretical grounding for a widely-used but poorly-understood training technique.

---

## 3. LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents

**Authors:** Aofan Yu, Chenyu Zhou, Tianyi Xu, Zihan Guo, Rong Shan

**Summary:** Agent systems that inject textual skills into context at every step pay substantial prefill overhead and expose skill content as plaintext. LatentSkill converts textual skills into plug-and-play LoRA adapters via a pretrained hypernetwork, storing skill knowledge in weight space; on ALFWorld it improves success by 21.4 points (seen) / 13.4 points (unseen) while using 64.1% fewer prefill tokens.

**arxiv:** [arxiv.org/abs/2606.06087](https://arxiv.org/abs/2606.06087)

**GitHub:** [github.com/SorrowTea/LatentSkill](https://github.com/SorrowTea/LatentSkill) (referenced)

**Sources:** HuggingFace Daily Papers

**Why trending:** Clean solution to a real efficiency and privacy problem in agentic systems, with strong benchmark results and a conceptually novel weight-space skill representation.

---

## 4. Latent Spatial Memory for Video World Models

**Authors:** Weijie Wang, Haoyu Zhao, Yifan Yang, Feng Chen, Zeyu Zhang (Microsoft Research)

**Summary:** Video world models typically build 3D spatial memory as explicit point clouds in RGB space — expensive to render and lossy through the VAE round-trip. Mirage instead stores scene information directly in diffusion latent space via depth-guided back-projection and queries it through latent-space warping, achieving up to 10.57× faster end-to-end video generation and a 55× reduction in memory footprint relative to explicit 3D baselines.

**arxiv:** [arxiv.org/abs/2606.09828](https://arxiv.org/abs/2606.09828)

**GitHub:** [github.com/microsoft/LatentSpatialMemory](https://github.com/microsoft/LatentSpatialMemory) (70 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Dramatic efficiency gains on a core world-model primitive from a high-credibility lab, with strong quantitative results on WorldScore and RealEstate10K.

---

## 5. CoVEBench: Can Video Editing Models Handle Complex Instructions?

**Authors:** Jiangtao Wu, Jiaming Wang, Yiwen He, Yuanxing Zhang, Shihao Li (NJU-LINK Lab)

**Summary:** Text-guided video editing models excel at simple style transfer or object insertion but consistently fail at compositional instructions that require multiple coupled edits simultaneously. CoVEBench provides 416 source videos, 626 multi-point editing instructions, and 9,990 fine-grained checklist items, and reveals that current models frequently omit edits, violate preservation constraints, or introduce artifacts when handling compound operations.

**arxiv:** [arxiv.org/abs/2606.08415](https://arxiv.org/abs/2606.08415)

**GitHub:** [github.com/NJU-LINK/CoVEBench](https://github.com/NJU-LINK/CoVEBench) (9 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Exposes a clear and important failure mode of a rapidly-maturing modality, with a rigorous evaluation framework that will likely drive future model development.

---

## 6. FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention

**Authors:** Yan Wang, Qifan Zhang, Jiachen Yu, Tian Liang, Dongyang Ma

**Summary:** Standard LLMs keep the full KV cache resident in GPU memory during decoding, creating a severe bottleneck for ultra-long context serving. FlashMemory-DeepSeek-V4 introduces Lookahead Sparse Attention (LSA), which enables lightning-fast KV cache indexing and drastically reduces memory pressure without degrading output quality.

**arxiv:** [arxiv.org/abs/2606.09079](https://arxiv.org/abs/2606.09079)

**GitHub:** [github.com/libertywing/FlashMemory-Deepseek-V4](https://github.com/libertywing/FlashMemory-Deepseek-V4) (10 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Long-context efficiency is a top practical bottleneck for deploying frontier models; this addresses it with a concrete architectural technique built on DeepSeek-V4.

---

## 7. SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks

**Authors:** Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang

**Summary:** Most spatial reasoning benchmarks assess passive perception rather than interactive decision-making in 3D environments. SpatialWorld evaluates multimodal large language models on interactive spatial reasoning tasks grounded in real-world scenarios, revealing significant gaps in MLLMs' ability to plan and act in physical space.

**arxiv:** [arxiv.org/abs/2606.09669](https://arxiv.org/abs/2606.09669)

**GitHub:** [github.com/Hongcheng-Gao/SpatialWorld](https://github.com/Hongcheng-Gao/SpatialWorld) (30 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Moves spatial reasoning evaluation from static QA to interactive agency — timely as embodied AI and robotics scale up.

---

## 8. Human Psychometric Questionnaires Mischaracterize LLM Behavior

**Authors:** Woojung Song, Dongmin Choi, Yoonah Park, Jongwook Han, Eun-Ju Lee

**Summary:** A growing body of work attempts to characterize LLMs using human psychometric instruments (personality scales, cognitive style questionnaires, etc.), but this paper shows those questionnaire results do not reliably predict how LLMs behave in actual user interactions. Analysis of 8 open-source LLMs reveals systematic disconnects between psychometric profiles and real conversational behavior.

**arxiv:** [arxiv.org/abs/2509.10078](https://arxiv.org/abs/2509.10078)

**Sources:** HuggingFace Daily Papers

**Why trending:** Challenges a popular and rapidly-growing sub-field, with direct implications for AI safety and alignment research that relies on personality-style evaluations.

---

## 9. Echo-Memory: A Controlled Study of Memory in Action World Models

**Authors:** Wayne King, Zeyue Xue, Yuxuan Bian, Jie Huang, Haoran Li (JD Future Academy)

**Summary:** Echo-Memory isolates and controls for memory mechanisms in action-conditioned world models that generate multi-segment videos from a first frame, text prompt, and camera-action sequences. The controlled study reveals how different memory architectures affect temporal consistency and generation quality across extended video sequences.

**arxiv:** [arxiv.org/abs/2606.09803](https://arxiv.org/abs/2606.09803)

**GitHub:** [github.com/Echo-Team-Joy-Future-Academy-JD/Echo-Memory](https://github.com/Echo-Team-Joy-Future-Academy-JD/Echo-Memory) (87 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Principled ablation study of memory in world models — a critical but underexplored axis — backed by strong community interest (87 GitHub stars on day one).

---

## 10. OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics

**Authors:** Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang

**Summary:** Game benchmarks for VLM agents currently report a single first-attempt score per (agent, game) pair, hiding whether agents are actually learning or just getting lucky. OmniGameArena uses Unreal Engine 5 to track improvement dynamics over repeated attempts, providing a richer picture of VLM game-playing capabilities and learning trajectories.

**arxiv:** [arxiv.org/abs/2606.09826](https://arxiv.org/abs/2606.09826)

**GitHub:** [github.com/mxlin043/OmniGameArena](https://github.com/mxlin043/OmniGameArena) (30 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Novel evaluation angle for VLM game agents — improvement dynamics are more informative than one-shot scores, and UE5 integration raises the benchmark's production quality.

---

## 11. End-to-End Context Compression at Scale

**Authors:** Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen

**Summary:** KV cache growth with context length is the central bottleneck for long-context inference, and existing compression techniques either hurt model quality substantially or only compress superficially. This paper presents an end-to-end context compression approach that maintains output quality at scale by learning to compress context holistically rather than with hand-crafted heuristics.

**arxiv:** [arxiv.org/abs/2606.09659](https://arxiv.org/abs/2606.09659)

**GitHub:** [github.com/LeonLixyz/LCLM](https://github.com/LeonLixyz/LCLM) (5 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Addresses the core infrastructure constraint for production long-context LLM deployments with a clean learned approach.

---

## 12. SwiftVR: Real-Time One-Step Generative Video Restoration

**Authors:** Jiaqi Yan, Xiangyu Chen, Xinlin Zhong, Haibin Huang, Chi Zhang

**Summary:** Live-stream video restoration demands high-resolution outputs under strict per-frame latency constraints that multi-step diffusion models cannot meet. SwiftVR achieves real-time performance by distilling a one-step diffusion model with techniques that preserve restoration fidelity, enabling deployment in latency-sensitive production settings.

**arxiv:** [arxiv.org/abs/2606.09516](https://arxiv.org/abs/2606.09516)

**GitHub:** [github.com/H-oliday/SwiftVR](https://github.com/H-oliday/SwiftVR) (8 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Practical deployment gap closed for an increasingly high-demand use case (live stream quality enhancement) with a clean one-step diffusion solution.

---

## 13. Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses

**Authors:** Xiaojun Wu, Cehao Yang, Honghao Liu, Xueyuan Lin, Wenjie Zhang

**Summary:** LLM agents depend on external inference conditions — prompts, tools, memory, SOPs, and harness feedback — that can improve task execution without touching model weights. Bayesian-Agent treats these harness components as probabilistic parameters and uses Bayesian posterior updates to evolve the skill set over time, enabling principled adaptation without full retraining.

**arxiv:** [arxiv.org/abs/2606.08348](https://arxiv.org/abs/2606.08348)

**GitHub:** [github.com/DataArcTech/Bayesian-Agent](https://github.com/DataArcTech/Bayesian-Agent) (22 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Principled probabilistic framework for harness optimization is a compelling alternative to ad-hoc prompt engineering, with real engineering applicability.

---

## 14. AHA-WAM: Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing

**Authors:** Jisong Cai, Long Ling, Shiwei Chu, Zhongshan Liu, Jiayue Kang

**Summary:** World-action models for robot manipulation jointly model visual scene dynamics and actions, but existing approaches suffer from fixed temporal horizons that mismatch real task dynamics. AHA-WAM introduces asynchronous horizon-adaptive prediction and an observation-guided context router that dynamically selects relevant scene history for each action decision.

**arxiv:** [arxiv.org/abs/2606.09811](https://arxiv.org/abs/2606.09811)

**Sources:** HuggingFace Daily Papers

**Why trending:** Addresses a core rigidity in world-action models for robotics — adaptive temporal reasoning is crucial for real-world manipulation tasks.

---

## 15. Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill

**Authors:** Tao Chen, Gangwei Jiang, Pengyu Cheng, Siyuan Huang, Yihao Liu (Qwen team)

**Summary:** Reward models for LLM post-training face a fundamental challenge: different tasks require radically different evaluation criteria, and a single RM cannot fairly adjudicate across them. Skill-RM unifies these heterogeneous criteria by grounding reward computation in agent skill representations, allowing a single model to serve diverse RL and RFT pipelines.

**arxiv:** [arxiv.org/abs/2606.03980](https://arxiv.org/abs/2606.03980)

**GitHub:** [github.com/Qwen-Applications/Skill-RM](https://github.com/Qwen-Applications/Skill-RM) (4 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Reward model quality is the key bottleneck for RLHF and RFT pipelines; a skill-grounded unification approach from the Qwen team carries significant credibility.

---

## 16. DEI: Diversity in Evolutionary Inference for Quality-Diversity Search

**Authors:** John Donaghy, Shikhar Rastogi (Gensyn AI)

**Summary:** Quality-diversity (QD) search using LLMs as mutation operators typically deploys a single homogeneous model, limiting the behavioral diversity of evolved solutions. DEI assigns heterogeneous LLMs across peer nodes in a distributed QD framework, showing that model diversity at the operator level translates directly to richer solution diversity.

**arxiv:** [arxiv.org/abs/2605.27130](https://arxiv.org/abs/2605.27130)

**GitHub:** [github.com/gensyn-ai/dei](https://github.com/gensyn-ai/dei) (2 ★)

**Sources:** HuggingFace Daily Papers

**Why trending:** Elegant insight from Gensyn AI — diversity at the model level compounds into diversity at the solution level, with implications for open-ended AI search.

---

## 17. Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders

**Authors:** Georgii Aparin, Vadim Popov, Tasnima Sadekova, Assel Yermekova

**Summary:** Whisper ASR is known to hallucinate coherent but entirely fabricated transcriptions when processing non-speech audio or silence. This paper applies mechanistic interpretability techniques — hidden representation steering and sparse autoencoders — to detect the internal signals that precede hallucinations and intervene at inference time to suppress them.

**arxiv:** [arxiv.org/abs/2606.07473](https://arxiv.org/abs/2606.07473)

**Sources:** HuggingFace Daily Papers

**Why trending:** Applies the cutting-edge interpretability toolkit (SAEs, activation steering) to a concrete production problem in ASR — a practical bridge between mechanistic interpretability research and deployment.

---

## 18. SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating

**Authors:** Zequn Xie, Junjie Wang, Dan Yang, Jie Feng, Yue Shen

**Summary:** Deep research agents are computationally expensive because accuracy-focused training paradigms reward thoroughness without penalizing compute. SlimSearcher introduces adaptive reward gating that conditions training rewards on computational efficiency, producing agents that achieve competitive research quality at dramatically lower inference cost.

**arxiv:** [arxiv.org/abs/2606.07074](https://arxiv.org/abs/2606.07074)

**Sources:** HuggingFace Daily Papers

**Why trending:** Efficiency-aware training for agents is an underexplored axis — as deep research agents scale, cost becomes the binding constraint, making this work highly timely.

---

## 19. Reasoning Arena: Trace Tournaments When Verifiable Rewards Fall Short

**Authors:** Han Zhou, Adam X. Yang, Laurence Aitchison, Anna Korhonen, Albert Q. Jiang

**Summary:** RLVR has become the leading paradigm for improving LLM reasoning, but it requires verifiable rewards — a precondition that fails for open-ended reasoning tasks where correctness cannot be checked automatically. Reasoning Arena uses trace tournaments (pairwise comparisons of reasoning chains by other LLMs) as a reward signal when verifiable rewards are unavailable, enabling RLVR-style training on a much wider problem class.

**arxiv:** [arxiv.org/abs/2606.09380](https://arxiv.org/abs/2606.09380)

**Sources:** HuggingFace Daily Papers

**Why trending:** Extends RLVR beyond math/code to open-domain reasoning — a long-standing limitation — with a practical tournament-based alternative to verifiable rewards.

---

## 20. Why Muon Outperforms Adam: A Curvature Perspective

**Authors:** Shuche Wang, Fengzhuo Zhang, Jiaxiang Li, Dirk Bergemann, Zhuoran Yang

**Summary:** Muon improves LLM training efficiency over Adam by roughly 2× but the geometric reason for this advantage has been unclear. This paper provides a curvature-based analysis showing that Muon's update direction better aligns with the loss landscape's principal curvature directions, explaining why it escapes sharp minima more effectively than Adam's coordinate-wise scaling.

**arxiv:** [arxiv.org/abs/2606.04662](https://arxiv.org/abs/2606.04662)

**Sources:** HuggingFace Daily Papers

**Why trending:** Muon has attracted intense practitioner interest as an Adam alternative; this theoretical grounding from a curvature perspective is exactly the mechanistic explanation the community has been waiting for.
