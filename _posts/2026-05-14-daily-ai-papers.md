---
title: "Daily AI Papers — May 14, 2026"
date: 2026-05-14
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-14/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-agents
  - diffusion-models
  - multimodal
---

## 1. MinT: Managed Infrastructure for Training and Serving Millions of LLMs

**Authors:** Mind Lab, Song Cao, Vic Cao, Andrew Chen, Kaijie Chen, Cleon Cheng et al.

**Summary:** MinT is a managed infrastructure system for LoRA post-training and online serving designed for settings where many fine-tuned policies are produced over a small number of expensive base-model deployments. Instead of materializing each policy as a merged full checkpoint, MinT keeps the base model resident and dynamically loads exported LoRA adapter revisions, enabling efficient multi-tenant LLM serving at massive scale.

**Arxiv:** [arxiv.org/abs/2605.13779](https://arxiv.org/abs/2605.13779)

**Sources:** HuggingFace Daily Papers (#1, 3 upvotes)

**Why trending:** Highest-upvoted paper today on HuggingFace; addresses a critical MLOps challenge — serving millions of fine-tuned LoRA models without N×base-model memory overhead, highly relevant to production AI infrastructure teams.

---

## 2. Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion

**Authors:** Chien Van Nguyen, Chaitra Hegde, Van Cuong Pham, Ryan A. Rossi, Franck Dernoncourt, Thien Huu Nguyen

**Summary:** Orthrus introduces a dual-architecture framework unifying the exact generation fidelity of autoregressive LLMs with the high-speed parallel token generation of diffusion models. The sequential nature of standard autoregressive decoding is a fundamental throughput bottleneck that Orthrus addresses by using diffusion-based parallel decoding while retaining AR-quality outputs.

**Arxiv:** [arxiv.org/abs/2605.12825](https://arxiv.org/abs/2605.12825)

**Sources:** HuggingFace Daily Papers (2 upvotes)

**Why trending:** Inference speed and memory efficiency are top priorities across the field; combining AR fidelity with diffusion parallelism is a compelling architectural direction.

---

## 3. Revisiting DAgger in the Era of LLM-Agents

**Authors:** Changhao Li, Rushi Qiang, Jiawei Huang, Chenxiao Gao, Chao Zhang, Niao He

**Summary:** Long-horizon LM agents trained from multi-turn interaction suffer from covariate shift with SFT (off-policy teacher data) and sparse rewards with RL. This paper revisits DAgger — the classic interactive imitation learning algorithm — showing it elegantly bridges both failure modes for LLM agents by providing on-policy teacher corrections at training time.

**Arxiv:** [arxiv.org/abs/2605.12913](https://arxiv.org/abs/2605.12913)

**Sources:** HuggingFace Daily Papers (2 upvotes)

**Why trending:** Agentic LLM training is one of the hottest research areas; reframing a classical algorithm (DAgger) for modern LLM agent settings gives the community a concrete and principled recipe.

---

## 4. MulTaBench: Benchmarking Multimodal Tabular Learning with Text and Image

**Authors:** Alan Arazi, Eilam Shapira, Shoham Grunblat, Mor Ventura, Elad Hoffer, Gioia Blayer

**Summary:** MulTaBench is a comprehensive benchmark for multimodal tabular learning that natively incorporates text and image modalities alongside structured numerical and categorical data. It reveals that tabular foundation models relying on frozen pretrained embeddings for unstructured inputs underperform tuned end-to-end multimodal models on real-world tabular tasks.

**Arxiv:** [arxiv.org/abs/2605.10616](https://arxiv.org/abs/2605.10616)

**Sources:** HuggingFace Daily Papers (2 upvotes)

**Why trending:** Tabular learning is ubiquitous in industry; adding multimodal support is a natural frontier and this benchmark sets a standard for the field.

---

## 5. AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation

**Authors:** Yuchao Gu, Guian Fang, Yuxin Jiang, Weijia Mao, Song Han

**Summary:** AnyFlow addresses a core limitation of consistency-distilled video diffusion models: performance degrades as more sampling steps are allocated at test time. By replacing the off-policy consistency trajectory with on-policy flow map distillation, AnyFlow achieves high-quality generation at any number of inference steps without the typical step-count performance cliff.

**Arxiv:** [arxiv.org/abs/2605.13724](https://arxiv.org/abs/2605.13724)

**Sources:** HuggingFace Daily Papers

**Why trending:** Video generation is a highly competitive space; flexible step-count inference is a practical requirement for real deployments where compute budgets vary.

---

## 6. Qwen-Image-VAE-2.0 Technical Report

**Authors:** Zekai Zhang, Deqing Li, Kuan Cao, Yujia Wu, Chenfei Wu

**Summary:** Qwen-Image-VAE-2.0 is a suite of high-compression Variational Autoencoders achieving significant advances in both reconstruction fidelity and diffusability. It adopts an improved architecture featuring Global Skip Connections (GSC) and expanded latent channels, scaled to billions of training images to address reconstruction bottlenecks at high compression ratios.

**Arxiv:** [arxiv.org/abs/2605.13565](https://arxiv.org/abs/2605.13565)

**Sources:** HuggingFace Daily Papers

**Why trending:** The Qwen series (Alibaba) is one of the most influential open model families; a new VAE release directly improves downstream image generation quality for the entire Qwen ecosystem and compatible models.

---

## 7. Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context

**Authors:** Zhaowei Wang, Lishu Luo, Haodong Duan, Weiwei Liu, Sijin Wu

**Summary:** Long-context modeling is becoming core to modern VLMs for document understanding, video analysis, and multi-turn agentic workflows, yet practical training recipes remain underexplored. This work provides a systematic study of designing and balancing long-context data mixtures, yielding models that generalize beyond 128K context with strong performance on long-document and video benchmarks.

**Arxiv:** [arxiv.org/abs/2605.13831](https://arxiv.org/abs/2605.13831)

**Sources:** HuggingFace Daily Papers

**Why trending:** 128K+ context VLMs unlock entirely new application categories; actionable training recipes for this capability are rare and highly sought after by practitioners.

---

## 8. The DAWN of World-Action Interactive Models (WAIMs)

**Authors:** Hongbo Lu, Liang Yao, Chenghao He, Haoyu Wang, Xiang Gu

**Summary:** DAWN formalizes World-Action Interactive Models (WAIMs), which address the mutual dependency between scene evolution and maneuver planning — existing World Action Models treat these as isolated parallel branches or rigid predict-then-plan pipelines, missing the critical bidirectional coupling. WAIMs explicitly model this reciprocity, enabling more coherent and physically plausible embodied agent behavior.

**Arxiv:** [arxiv.org/abs/2605.11550](https://arxiv.org/abs/2605.11550)

**Sources:** HuggingFace Daily Papers

**Why trending:** World models for embodied AI and autonomous driving are a major research frontier; formalizing the world-action interaction loop is a conceptual contribution that will influence future architectures.

---

## 9. Many-Shot CoT-ICL: Making In-Context Learning Truly Learn

**Authors:** Tsz Ting Chung, Lemao Liu, Mo Yu, Dit-Yan Yeung

**Summary:** Many-shot in-context learning with chain-of-thought (CoT) can match fine-tuning performance using dozens to hundreds of demonstrations, yet the scaling behavior on reasoning tasks is poorly understood. This paper provides a rigorous study of many-shot CoT-ICL, revealing how it differs from few-shot ICL and identifying conditions under which it truly learns vs. merely pattern-matches.

**Arxiv:** [arxiv.org/abs/2605.13511](https://arxiv.org/abs/2605.13511)

**Sources:** HuggingFace Daily Papers

**Why trending:** Understanding the limits and mechanisms of in-context learning is foundational; as long-context models become standard, many-shot ICL becomes a practical alternative to fine-tuning.

---

## 10. Learning Agentic Policy from Action Guidance

**Authors:** Yuxiang Ji, Zengbin Wang, Yong Wang, Shidong Yang, Ziyu Ma

**Summary:** Agentic RL for LLMs critically depends on exploration — when the base policy cannot reach reward states, learning stalls. This paper proposes using explicit action guidance to provide external scaffolding that bootstraps the agent into the reward region, avoiding costly iterative prompting or manual curriculum design.

**Arxiv:** [arxiv.org/abs/2605.12004](https://arxiv.org/abs/2605.12004)

**Sources:** HuggingFace Daily Papers

**Why trending:** Exploration in sparse-reward LLM agent training is a known bottleneck; principled solutions that don't require expensive human-in-the-loop guidance are highly practical.

---

## 11. Asymmetric Flow Models

**Authors:** Hansheng Chen, Jan Ackermann, Minseo Kim, Gordon Wetzstein, Leonidas Guibas

**Summary:** Flow-based generation in high-dimensional spaces is hampered because velocity prediction requires modeling high-dimensional noise, even when data has strong low-rank structure. AsymFlow restricts noise prediction to a low-rank subspace while keeping data prediction full-dimensional, analytically recovering the full-rank velocity field from this asymmetric parameterization.

**Arxiv:** [arxiv.org/abs/2605.12964](https://arxiv.org/abs/2605.12964)

**Sources:** HuggingFace Daily Papers

**Why trending:** Flow matching models (used in Stable Diffusion 3, Flux, etc.) are the dominant generative paradigm; a principled efficiency improvement from Guibas's group at Stanford is likely to have broad impact.

---

## 12. FrameSkip: Learning from Fewer but More Informative Frames in VLA Training

**Authors:** Bin Yu, Shijie Lian, Xiaopeng Lin, Zhaolong Shen, Yuliang Wei

**Summary:** Vision-Language-Action policies trained from dense robot teleoperation trajectories suffer from temporal supervision imbalance — long low-change segments dominate training while manipulation-critical transitions are underrepresented. FrameSkip selectively skips redundant frames during training, improving both efficiency and policy quality on manipulation tasks.

**Arxiv:** [arxiv.org/abs/2605.13757](https://arxiv.org/abs/2605.13757)

**Sources:** HuggingFace Daily Papers

**Why trending:** VLA training is a bottleneck for scaling robot foundation models; a simple frame selection strategy that improves sample efficiency is immediately applicable to ongoing robotics research.

---

## 13. Edit-Compass & EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling

**Authors:** Xuehai Bai, Yang Shi, Yi-Fan Zhang, Xuanyu Zhu, Yuran Wang

**Summary:** Existing image editing benchmarks fail to faithfully reflect human judgment for strong frontier models due to limited task difficulty and coarse evaluation. Edit-Compass provides a harder, finer-grained benchmark while EditReward-Compass evaluates reward models used for alignment, establishing a unified evaluation ecosystem for instruction-based image editing.

**Arxiv:** [arxiv.org/abs/2605.13062](https://arxiv.org/abs/2605.13062)

**Sources:** HuggingFace Daily Papers

**Why trending:** Image editing is a commercially important capability; rigorous benchmarking is essential as models saturate existing evals, and this fills a clear gap.

---

## 14. TrackCraft3R: Repurposing Video Diffusion Transformers for Dense 3D Tracking

**Authors:** Jisu Nam, Jahyeok Koo, Soowon Son, Jaewoo Jung, Honggyu An

**Summary:** Dense 3D tracking from monocular video is fundamental to dynamic scene understanding, but existing approaches either rely on synthetic-data-trained iterative paradigms or fine-tune 3D foundation models with limited motion priors. TrackCraft3R repurposes pretrained video diffusion transformers — which have strong motion priors from large-scale video training — for dense 3D point tracking.

**Arxiv:** [arxiv.org/abs/2605.12587](https://arxiv.org/abs/2605.12587)

**Sources:** HuggingFace Daily Papers

**Why trending:** Repurposing generative video models for perception tasks is a productive research trend; 3D tracking is critical for robotics and AR/VR applications.

---

## 15. HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution

**Authors:** Dongming Jiang, Yi Li, Guanpeng Li, Qiannan Li, Bingzhe Li

**Summary:** Memory retrieval in agentic LLM systems is typically treated as a static lookup using flat vector search or fixed binary relational graphs. HAGE proposes a weighted multi-relational memory framework where graph edge weights evolve via reinforcement learning, capturing the varying strength, confidence, and query-dependent relevance of relationships between events.

**Arxiv:** [arxiv.org/abs/2605.09942](https://arxiv.org/abs/2605.09942)

**Sources:** HuggingFace Daily Papers

**Why trending:** Agentic memory is an active area; moving from static vector lookup to dynamically evolving graph-based memory is a promising direction for long-horizon agent reasoning.

---

## 16. Retrieval is Cheap, Show Me the Code: Executable Multi-Hop Reasoning for RAG

**Authors:** Jiashuo Sun, Jimeng Shi, Yixuan Xie, Saizhuo Wang, Jash Rajesh Parekh

**Summary:** Existing RAG systems remain brittle on multi-hop questions because intermediate reasoning states are implicit in free-form natural language, making it hard to validate and chain retrieval steps. This paper proposes representing reasoning as executable code, where each intermediate state is an explicit, verifiable computation that drives the next retrieval step.

**Arxiv:** [arxiv.org/abs/2605.12975](https://arxiv.org/abs/2605.12975)

**Sources:** HuggingFace Daily Papers

**Why trending:** Multi-hop RAG is a well-known failure mode for production QA systems; using code as a structured reasoning substrate is an elegant solution that connects retrieval with program synthesis.

---

## 17. PresentAgent-2: Towards Generalist Multimodal Presentation Agents

**Authors:** Wei Wu, Ziyang Xu, Zeyu Zhang, Yang Zhao, Hao Tang

**Summary:** PresentAgent-2 is an agentic framework that generates full presentation videos from open-ended user queries — it summarizes the query into a focused topic, performs deep research, assembles multimodal slides with text and visuals, and delivers them in an interactive presentation format. It extends beyond static slide generation to end-to-end presentation video production with grounded research.

**Arxiv:** [arxiv.org/abs/2605.11363](https://arxiv.org/abs/2605.11363)

**Sources:** HuggingFace Daily Papers

**Why trending:** Automated presentation generation is a high-value practical application; multi-step agentic pipelines that bridge research, content creation, and media production are gaining traction.

---

## 18. RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data

**Authors:** Harold Haodong Chen, Sirui Chen, Yingjie Xu, Wenhang Ge, Ying-Cong Chen

**Summary:** Scalable robotic manipulation is bottlenecked by scarcity of task-aligned physical interaction data; VLMs suffer from semantic-spatial misalignment and video generation models from physical hallucinations. RoboEvolve couples a VLM planner and a video generation model simulator in a co-evolution loop that mutually corrects each other's failure modes, enabling data synthesis from limited demonstrations.

**Arxiv:** [arxiv.org/abs/2605.13775](https://arxiv.org/abs/2605.13775)

**Sources:** HuggingFace Daily Papers

**Why trending:** Data scarcity is the central bottleneck for robot learning; co-evolution of planning and simulation models is a novel approach to self-improving synthetic data generation.

---

## 19. Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling

**Authors:** Eilam Shapira, Moshe Tennenholtz, Roi Reichart

**Summary:** AI agents negotiate and transact in natural language with unfamiliar counterparts whose internal LLMs, prompts, and control logic are hidden — yet each decision may have monetary consequences. This paper asks whether an agent can predict an unfamiliar counterpart's decisions from limited interaction history using a text-tabular modeling approach that combines linguistic and behavioral signals.

**Arxiv:** [arxiv.org/abs/2605.12411](https://arxiv.org/abs/2605.12411)

**Sources:** HuggingFace Daily Papers

**Why trending:** As AI agents increasingly interact with each other in economic and strategic settings, theory of mind and opponent modeling capabilities become essential for safety and performance.

---

## 20. Offline Preference Optimization for Rectified Flow with Noise-Tracked Pairs

**Authors:** Yunhong Lu, Qichao Wang, Hengyuan Cao, Xiaoyin Xu, Min Zhang

**Summary:** Existing preference datasets for text-to-image models store only final winner/loser images, which is insufficient for rectified flow (RF) models that follow nearly straight denoising trajectories indexed by a specific prior noise sample. This paper proposes tracking noise samples across trajectories to create noise-paired preference data, enabling principled DPO-style alignment for RF models without the trajectory estimation errors of prior diffusion alignment approaches.

**Arxiv:** [arxiv.org/abs/2605.09433](https://arxiv.org/abs/2605.09433)

**Sources:** HuggingFace Daily Papers

**Why trending:** Rectified flow (used in Stable Diffusion 3, Flux) is the dominant text-to-image architecture; extending RLHF/DPO alignment properly to this paradigm is an important open problem.
