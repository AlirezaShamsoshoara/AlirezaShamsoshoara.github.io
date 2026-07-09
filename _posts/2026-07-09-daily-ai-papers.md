---
title: "Daily AI Papers — July 09, 2026"
date: 2026-07-09
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-09/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - robotic-manipulation
  - world-models
  - agentic-rl
---

## 1. Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning

**Authors:** Chen Tang, Yizhou Wang, Jianyu Wu, Lintao Wang, Shixiang Tang, et al.  
**arXiv:** [arxiv.org/abs/2607.07708](https://arxiv.org/abs/2607.07708)  
**Sources:** HuggingFace Daily Papers (69 upvotes — top paper today)  
**Why Trending:** Highest-upvoted paper on HuggingFace today, tackling a joint representation-and-reasoning challenge spanning biology, chemistry, and materials science.

Structure-property relationships are foundational across biology, chemistry, and materials science, but explaining them requires interpreting structural evidence through physical principles like stereochemistry, symmetry, and energetics. This paper introduces a deep native structural reasoning approach that preserves domain-specific structural information while reasoning transparently about the physical constraints that link structure to function.

---

## 2. Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation

**Authors:** Hongyu Qu, Jianzhe Gao, Xiaobin Hu, Shaohuan Yang, Xinlei Yu, et al.  
**arXiv:** [arxiv.org/abs/2607.07608](https://arxiv.org/abs/2607.07608)  
**Sources:** HuggingFace Daily Papers (44 upvotes)  
**Why Trending:** Second-highest HuggingFace upvotes today; addresses a core limitation of mainstream VLA models on long-horizon, temporally dependent robot tasks.

Mainstream Vision-Language-Action models predict actions primarily from the current observation under a Markovian assumption, causing them to struggle with long-horizon tasks. This paper proposes a dual latent memory that lives inside the VLA's native embedding space, letting historical experience interleave fluidly with multimodal reasoning instead of being bolted on as external retrieval.

---

## 3. Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence

**Authors:** Shuailei Ma, Jiaqi Liao, Xinyang Wang, Jingjing Wang, Chaoran Feng, et al.  
**arXiv:** [arxiv.org/abs/2607.07675](https://arxiv.org/abs/2607.07675)  
**Sources:** HuggingFace Daily Papers (38 upvotes)  
**Why Trending:** Third-highest HuggingFace upvotes; tackles the domain mismatch between content-generation-focused video models and the physical realism needed for robot control.

Video generative models are typically optimized for visual fidelity and creativity, not the computational efficiency and physical realism robotics needs. LingBot-Video introduces a DiT-based, Mixture-of-Experts video pretraining paradigm purpose-built for embodied intelligence, trading dense compute for a better capacity-efficiency tradeoff at scale.

---

## 4. Infinite Worlds with Versatile Interactions

**Authors:** Zelin Gao, Qiuyu Wang, Jiapeng Zhu, Jingye Chen, Zichen Liu, et al.  
**arXiv:** [arxiv.org/abs/2607.07534](https://arxiv.org/abs/2607.07534)  
**Sources:** HuggingFace Daily Papers (20 upvotes)  
**Why Trending:** Strong HuggingFace traction; pushes interactive video world models toward unbounded, real-time generation — a capability with obvious gaming and simulation applications.

LingBot-World 2.0 (LingBot-World-Infinity) advances interactive video world generation with an unbounded interaction horizon that maintains consistent quality via a causal pretraining paradigm. A distilled real-time variant can drive 720p video streams at 60 fps, a significant leap for playable, long-horizon generative worlds.

---

## 5. LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL

**Authors:** Yujin Kim, Namgyu Ho, Sangmin Hwang, Joonkee Kim, Yongjin Yang, et al.  
**arXiv:** [arxiv.org/abs/2607.04412](https://arxiv.org/abs/2607.04412)  
**Sources:** HuggingFace Daily Papers (20 upvotes)  
**Why Trending:** Tied for 4th on HuggingFace; addresses a key blind spot in RLHF-style training where prompt difficulty and policy skill drift out of sync.

RL for non-verifiable instruction following increasingly leans on LLM judges with rubrics as reward signals, but training prompts are usually static and drawn from fixed corpora. LLM-as-a-Tutor adapts the training prompts themselves to the evolving policy, keeping prompt difficulty aligned with model capability so the judge can keep recovering a useful reward signal.

---

## 6. JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications

**Authors:** Oxygen AIIC Team, Chan Long, Chao Liu, Chaofan Chen, Chaohui Dong, et al.  
**arXiv:** [arxiv.org/abs/2606.28070](https://arxiv.org/abs/2606.28070)  
**Sources:** HuggingFace Daily Papers (13 upvotes)  
**Why Trending:** Rare industrial-scale deployment paper — JD.com's production LLM/VLM system serving 700M+ users and billions of SKUs.

JD.com operates one of the world's largest e-commerce platforms, where structured item knowledge at massive scale directly drives consumer experience and operating cost. Oxygen AIIC V1 presents an industrial LLM/VLM-centric system addressing fast-emerging concepts, high-quality knowledge production, and diverse downstream requirements across tens of billions of SKUs.

---

## 7. RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies

**Authors:** Tianxing Chen, Yue Chen, Zixuan Li, Junyuan Tang, Kailun Su, et al.  
**arXiv:** [arxiv.org/abs/2607.04434](https://arxiv.org/abs/2607.04434)  
**Sources:** HuggingFace Daily Papers (6 upvotes)  
**Why Trending:** Fills a recognized gap — most robot manipulation benchmarks are either sim-only or real-only, not both.

Generalist robot manipulation policies have advanced quickly, but existing benchmarks remain narrow, short-horizon, and split between simulation-only or real-world-only evaluation. RoboDojo unifies sim-and-real testing into a single comprehensive benchmark, aiming to give the field a common yardstick for generalist manipulation capability.

---

## 8. Attending to Multimodal Generation One Token at a Time

**Authors:** Varun Gupta, Vineet Gandhi, Makarand Tapaswi  
**arXiv:** [arxiv.org/abs/2607.03738](https://arxiv.org/abs/2607.03738)  
**Sources:** HuggingFace Daily Papers (6 upvotes)  
**Why Trending:** Novel interpretability angle — most MLLM interpretability work studies "where" attention lives, this studies "when" it shifts during generation.

Multimodal LLMs generate responses autoregressively, but the token-level dynamics of how attention shifts between image, text, instruction, and prior output during generation remain underexplored. This paper introduces "One Token at a Time" (OTaT), tracking per-token attention role-switching and proposing new tasks that require explicit visual-textual attention transitions.

---

## 9. Rank-Then-Act: Reward-Free Control from Frame-Order Progress

**Authors:** Yuriy Maksyuta, George Bredis, Ruslan Rakhimov, Daniil Gavrilov  
**arXiv:** [arxiv.org/abs/2607.01897](https://arxiv.org/abs/2607.01897)  
**Sources:** HuggingFace Daily Papers (6 upvotes)  
**Why Trending:** Elegant reward-free control formulation — avoids brittle scalar reward models in favor of a correlation-based signal derived from progress ranking.

Rank-Then-Act learns control policies from expert video demonstrations without any environment reward, training a VLM offline as a progress-based ordinal scorer via GRPO over shuffled frame sequences. Rather than using this scorer as a direct scalar reward, the method derives a correlation-based RL reward, forcing the model to recover genuine temporal/causal structure instead of exploiting trivial time cues.

---

## 10. SWE-Review: Closing the Loop on Issue Resolution with Agentic Code Review

**Authors:** Ruoyu Wang, Jierun Chen, Shaowei Wang, Chaofan Tao, Sidi Yang, et al.  
**arXiv:** [arxiv.org/abs/2607.06065](https://arxiv.org/abs/2607.06065)  
**Sources:** HuggingFace Daily Papers (5 upvotes)  
**Why Trending:** Directly relevant to the fast-growing coding-agent space — most PR-generation agents today skip systematic review entirely.

Coding agents increasingly generate pull requests for real issues, but this is typically open-loop: PRs are proposed with no systematic review or revision step. SWE-Review closes that loop with a reviewer agent that explores the repository, judges whether a PR should be accepted, and gives structured revision feedback, evaluated via the new SWE-Review-Bench.

---

## 11. PluraMath: Extending Mathematical Reasoning Evaluation Beyond High-Resource Languages

**Authors:** Daryna Dementieva, Nikolay Babakov, Kathy Hämmerl, Ilseyar Alimova, Jindřich Libovický, et al.  
**arXiv:** [arxiv.org/abs/2607.05992](https://arxiv.org/abs/2607.05992)  
**Sources:** HuggingFace Daily Papers (5 upvotes)  
**Why Trending:** Addresses a well-known blind spot in LLM math evaluation — benchmarks are dominated by English and Chinese despite growing multilingual reasoning claims.

Mathematical reasoning benchmarks for LLMs remain heavily biased toward high-resource languages, with the recent PolyMath dataset covering only 18 such languages. PluraMath extends PolyMath with 18 additional underrepresented languages spanning six language families, giving the field a much more linguistically diverse math reasoning testbed.

---

## 12. 3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance

**Authors:** Dongyoon Hwang, Byungkun Lee, Dongjin Kim, Hyojin Jang, Hoiyeong Jin, et al.  
**arXiv:** [arxiv.org/abs/2606.31329](https://arxiv.org/abs/2606.31329)  
**Sources:** HuggingFace Daily Papers (5 upvotes)  
**Why Trending:** Fixes a structural flaw in hierarchical VLA design — 2D trajectory guidance forces incorrect depth assumptions on 3D-aware low-level policies.

Hierarchical VLA models decouple high-level planning from low-level control, but state-of-the-art low-level policies operate on 3D point clouds while receiving only 2D end-effector trajectory guidance lacking depth. 3D HAMSTER replaces this with genuine 3D trajectory guidance, removing the depth-assignment mismatch between planner and controller.

---

## 13. Automating the Design of Embodied Agent Architectures

**Authors:** Jian Zhou, Sihao Lin, Jin Li, Shuai Fu, Gengze Zhou, Qi Wu  
**arXiv:** [arxiv.org/abs/2606.30111](https://arxiv.org/abs/2606.30111)  
**Sources:** HuggingFace Daily Papers (4 upvotes)  
**Why Trending:** Extends the emerging "agent architecture search" trend from text-only agents into the harder, perceptually grounded embodied setting.

Embodied agents are typically hand-designed compositions of perception, memory, planning, and action modules, with architecture choices still relying on researcher intuition. This paper systematically evaluates Agent Architecture Search — previously validated only on text-domain agents — on perceptual embodied agents through simulation.

---

## 14. WildCity: A Real-World City-Scale Testbed for Rendering, Simulation, and Spatial Intelligence

**Authors:** Xiangyu Han, Mengyu Yang, Jiaqi Li, Bowen Chang, Ziyu Chen, et al.  
**arXiv:** [arxiv.org/abs/2607.06838](https://arxiv.org/abs/2607.06838)  
**Sources:** HuggingFace Daily Papers (4 upvotes)  
**Why Trending:** Notable co-author lineup including Marco Pavone; tackles city-scale spatial intelligence data, a major bottleneck for embodied AI research.

Humans can form coherent spatial mental maps spanning tens of square kilometers, but AI systems have lacked the city-scale data needed to attempt the same. WildCity introduces a real-world multimodal dataset from autonomous fleets covering 18 trajectories averaging 83.7 km each, aimed at scaling rendering, simulation, and spatial intelligence research to full-city scope.

---

## 15. HunyuanOCR-1.5: Making Lightweight OCR VLMs Faster and Better

**Authors:** Gengluo Li, Xingyu Wan, Shangpin Peng, Weinong Wang, Hao Feng, et al.  
**arXiv:** [arxiv.org/abs/2607.04884](https://arxiv.org/abs/2607.04884)  
**Sources:** HuggingFace Daily Papers (4 upvotes)  
**Why Trending:** Practical, deployable OCR system update from Tencent's Hunyuan line — unifies five OCR-adjacent tasks in one lightweight VLM.

HunyuanOCR-1.5 is a lightweight end-to-end OCR-specialized VLM unifying document parsing, text spotting, information extraction, text-image translation, and multi-image document understanding. It keeps the HunyuanOCR-1.0 backbone but adapts DFlash decoding to sharply cut latency on long structured outputs like dense documents, tables, and formulas.

---

## 16. When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic Retrieval Buffers

**Authors:** Yushi Sun, Bowen Cao, Wai Lam  
**arXiv:** [arxiv.org/abs/2607.00394](https://arxiv.org/abs/2607.00394)  
**Sources:** HuggingFace Daily Papers (4 upvotes)  
**Why Trending:** Counterintuitive empirical finding — classic cache heuristics (LRU, LFU) actually underperform naive FIFO for LLM agent memory buffers.

LLM agents increasingly rely on retrieval buffers to reuse past experience, yet the cache replacement policies governing them remain ad hoc. Testing 8 replacement policies on MemoryBench-Full, this paper finds that LRU and LFU consistently underperform a naive FIFO baseline once items are matched by embedding similarity with continuous hit quality rather than binary hits.

---

## 17. AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation

**Authors:** Andrey Podivilov, Vadim Lomshakov, Sergey Savin, Matvei Startsev, Roman Pozharskiy, et al.  
**arXiv:** [arxiv.org/abs/2607.06624](https://arxiv.org/abs/2607.06624)  
**Sources:** HuggingFace Daily Papers (3 upvotes)  
**Why Trending:** Pushes coding-agent evaluation beyond pass/fail toward the full trajectory experience users actually have with these agents.

Most code-agent benchmarks reduce a run to a single bit — did the task pass — but real users experience the entire trajectory, including tool use, self-verification, and error recovery. AgentLens evaluates the whole trajectory, pairing formal verification with LLM-written trajectory reviews for a more production-realistic assessment.

---

## 18. Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

**Authors:** Zhenyu Hou, Yujiang Li, Jie Tang, Yuxiao Dong  
**arXiv:** [arxiv.org/abs/2607.07508](https://arxiv.org/abs/2607.07508)  
**Sources:** HuggingFace Daily Papers (3 upvotes)  
**Why Trending:** Tackles training stability in asynchronous RL, an efficiency approach gaining traction for long-horizon agentic LLM post-training.

Synchronous, batch-interleaved RL pipelines for LLMs are inefficient for long-horizon agentic tasks, and newer asynchronous RL systems that update as rollouts arrive tend to prioritize throughput over stability. This paper identifies a key issue — group-wise sampling in GRPO breaks down asynchronously — and proposes a single-rollout optimization scheme that preserves both efficiency and training stability.

---

## 19. Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity

**Authors:** Loïc Cabannes, Pierre-Emmanuel Mazaré, Gergely Szilvasy, Matthijs Douze, Maria Lomeli, Ilze Amanda Auzina, Justin Carpentier, Gabriel Synnaeve, Hervé Jégou  
**arXiv:** [arxiv.org/abs/2607.07386](https://arxiv.org/abs/2607.07386)  
**Sources:** HuggingFace Daily Papers (3 upvotes); Meta FAIR authorship (Douze, Synnaeve, Jégou)  
**Why Trending:** From Meta FAIR researchers; addresses the long-standing recall gap between linear-attention models and full softmax attention.

Linear attention models offer fixed compute and state size per token but lag behind softmax-attention transformers on long-context recall, and naively growing their state raises FLOPs. Sparse Delta Memory (SDM) extends Gated DeltaNet with a sparse addressing scheme that scales hidden-state capacity by orders of magnitude without a proportional compute increase.

---

## 20. Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training

**Authors:** Zijian Zhang, Rizhen Hu, Athanasios Glentis, Dawei Li, Chung-Yiu Yau, et al.  
**arXiv:** [arxiv.org/abs/2607.01232](https://arxiv.org/abs/2607.01232)  
**Sources:** HuggingFace Daily Papers (3 upvotes)  
**Why Trending:** Surprising, resource-saving result — challenges the default assumption that RL post-training needs to update every transformer layer.

RL post-training for LLMs typically updates all parameters uniformly, implicitly assuming every layer contributes equally to the gains. Through a systematic layer-wise study, this paper finds that training a single, well-chosen transformer layer can match full-parameter RL training performance — a potentially large compute saver for RL post-training pipelines.
