---
title: "Daily AI Papers — July 28, 2026"
date: 2026-07-28
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-28/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - open-frontier-models
  - diffusion-models
  - computer-use-agents
---

## 1. Kimi K3: Open Frontier Intelligence

**Authors:** Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, M. C., et al. (402 authors)

**Summary:** Kimi K3 is a 2.8T-parameter Mixture-of-Experts model with 104B activated parameters, native vision capability, and a 1M-token context window, built on new "Kimi Delta Attention" and "Stable LatentMoE" (16-of-896 routed experts) architectures. The combination of architectural advances and refined data/training recipes yields roughly a 2.5x improvement in compute efficiency over prior generations.

**arXiv:** [arxiv.org/abs/2607.24653](https://arxiv.org/abs/2607.24653)
**Sources:** HuggingFace Daily Papers (237 upvotes — highest of the day)
**Why trending:** A new open-weight frontier-scale MoE model from Kimi/Moonshot directly competing with closed frontier labs; scale (2.8T params, 1M context) and open release make it the clear top story.

---

## 2. JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents

**Authors:** Yunlong Lin, Zixu Lin, Zhaohu Xing, Biqiang Li, Chenxin Li, et al. (26 authors)

**Summary:** JarvisHub is an open harness for long-horizon, canvas-native creative agents that must manage references, drafts, edits, tool actions, and human feedback across evolving multimodal projects, not just single prompt-output generations. It provides infrastructure for representing this evolving creative state so agents can iterate the way human creators do.

**arXiv:** [arxiv.org/abs/2607.23588](https://arxiv.org/abs/2607.23588)
**Sources:** HuggingFace Daily Papers (100 upvotes)
**Why trending:** Strong community interest in agent harnesses for creative/multimodal generation workflows beyond one-shot image/video synthesis.

---

## 3. From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent Protocol Distillation in Agentic Search

**Authors:** Junlin Liu, Jiangwang Chen, Zixin Song, Shuaiyu Zhou, Chunji Lv, et al. (10 authors)

**Summary:** The paper tackles the sparse-reward problem in RL-trained agentic search by distilling reasoning/retrieval behavior from proprietary teacher models into open-source students, avoiding the pitfalls of naive logit-matching across differing model families. It proposes a multi-agent protocol-level distillation scheme to densify supervision while preserving the student's own distribution.

**arXiv:** [arxiv.org/abs/2607.24280](https://arxiv.org/abs/2607.24280)
**Sources:** HuggingFace Daily Papers (63 upvotes)
**Why trending:** Addresses the practical, widely-discussed problem of closing the open-vs-proprietary agent capability gap for search/RAG-style agents.

---

## 4. Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation

**Authors:** Bingnan Li, Haozhe Wang, Haozhong Xiong, Fangtai Wu, Jinpeng Yu, et al. (8 authors)

**Summary:** The authors show that standard on-policy diffusion distillation (OPD), which naively matches teacher/student CFG-composed velocities, is under-identified at the positive/negative branch level. They propose a corrected formulation that properly disentangles guidance branches during distillation.

**arXiv:** [arxiv.org/abs/2607.24731](https://arxiv.org/abs/2607.24731)
**Sources:** HuggingFace Daily Papers (60 upvotes)
**Why trending:** Fixes a subtle but consequential flaw in a technique widely used to speed up diffusion model inference, relevant to nearly every fast image/video generator.

---

## 5. Progress Reward Modeling for Robotic Learning: A Comprehensive Survey

**Authors:** Jianshu Zhang, Keliang Wu, Haoran Lu, Anbang Liu, Ce Zhang, et al. (11 authors)

**Summary:** This survey unifies the fragmented literature on "progress rewards" — dense feedback signals that tell a robot whether it is making, stalling, or undoing progress toward a task, unlike terminal-only success signals. It proposes a shared framework for comparing existing methods across observation types and reward formulations.

**arXiv:** [arxiv.org/abs/2607.21655](https://arxiv.org/abs/2607.21655)
**Sources:** HuggingFace Daily Papers (55 upvotes)
**Why trending:** Robotics/embodied-AI reward design is a hot subfield, and a comprehensive survey filling a framework gap draws high community reference value.

---

## 6. StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents

**Authors:** Yan Yang, Xiangru Jian, Ziyang Luo, Zirui Zhao, Yutong Dai, et al. (10 authors)

**Summary:** StateAct argues computer-use agents should reason over underlying program state (files, DOM, backend data) rather than lossy screenshot pixels, since different states can render identically. It introduces a code-first, multi-agent harness where the main agent inspects and manipulates state directly instead of purely visual grounding.

**arXiv:** [arxiv.org/abs/2607.22798](https://arxiv.org/abs/2607.22798)
**Sources:** HuggingFace Daily Papers (51 upvotes)
**Why trending:** Computer-use agents are a major current focus area, and this challenges the pixel-first paradigm most existing agent frameworks follow.

---

## 7. Data Pyramid for Embodied Manipulation

**Authors:** Yifan Ye, Yankai Fu, Yaoxu Lv, Bohan Hou, Jun Cen, et al. (29 authors)

**Summary:** The paper organizes the embodied-data ecosystem into a five-level "pyramid" (real-robot, UMI-style, ego/exocentric, simulation, and general vision-language data) to clarify how these heterogeneous sources should be combined. It analyzes the tradeoffs of each layer for training generalizable manipulation policies.

**arXiv:** [arxiv.org/abs/2607.24744](https://arxiv.org/abs/2607.24744)
**Sources:** HuggingFace Daily Papers (29 upvotes)
**Why trending:** Data strategy for embodied AI/robotics is a persistent bottleneck topic, and a structured taxonomy is broadly useful to practitioners.

---

## 8. Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification

**Authors:** Haopeng Li, Yitong Li, Junsong Chen, Tian Ye, Haozhe Liu, et al. (11 authors)

**Summary:** Sol-Attn is a training-free dynamic sparse attention method for video diffusion transformers that addresses the rigid, costly block-routing of prior sparsification approaches. It adaptively selects key-value blocks on the fly to cut inference cost while preserving accuracy on long video token sequences.

**arXiv:** [arxiv.org/abs/2607.24027](https://arxiv.org/abs/2607.24027)
**Sources:** HuggingFace Daily Papers (23 upvotes)
**Why trending:** Video generation inference cost is a major practical pain point, and training-free speedups are immediately adoptable.

---

## 9. OmniVAE: An Audio-Video VAE with Cross-Modal Alignment for Joint Generation

**Authors:** Jun Zhan, Chen Yang, Yitian Gong, Donghua Yu, Kuangwei Chen, et al. (26 authors)

**Summary:** OmniVAE addresses the misalignment between separately-trained audio and video VAE latent spaces that hampers joint audio-video generation. It introduces cross-modal alignment so a downstream generative model can learn synchronized audio-video correspondence more directly from the shared latent space.

**arXiv:** [arxiv.org/abs/2607.23855](https://arxiv.org/abs/2607.23855)
**Sources:** HuggingFace Daily Papers (20 upvotes)
**Why trending:** Joint audio-video generation with true sync is one of the next frontiers beyond silent video models, drawing strong interest.

---

## 10. The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation

**Authors:** Tianyi Men, Zhuoran Jin, Kang Liu, Jun Zhao (4 authors)

**Summary:** The authors build a controlled multi-turn environment to systematically study how long-horizon planning ability is acquired across pre-training and post-training stages, since standard internet-scale training data is too opaque to isolate this. They analyze single- vs. multi-teacher on-policy agentic distillation as levers for improving planning.

**arXiv:** [arxiv.org/abs/2607.24720](https://arxiv.org/abs/2607.24720)
**Sources:** HuggingFace Daily Papers (19 upvotes)
**Why trending:** Mechanistic, controlled study of agent planning capability acquisition — a rigorous complement to the many black-box agent benchmark papers.

---

## 11. Oxygen-TryOn: Fashion-Native Foundation Model for Any-item Virtual Try-On

**Authors:** Yong Liu, Xiaolong Fu, Zihang Xu, Wen Xue, Xueheng Li, et al. (13 authors)

**Summary:** Oxygen-TryOn is a foundation model built specifically for virtual try-on (rather than repurposing a general image editor), using a dedicated data engine and try-on-specific training. It can synthesize photorealistic images of a subject wearing arbitrary reference items across fashion categories, going beyond prior systems' narrower item-type support.

**arXiv:** [arxiv.org/abs/2607.21694](https://arxiv.org/abs/2607.21694)
**Sources:** HuggingFace Daily Papers (19 upvotes)
**Why trending:** Virtual try-on has strong commercial applications in e-commerce, and a purpose-built foundation model (vs. generic editors) is a notable step up.

---

## 12. Chamaileon: Cross-Context Binder Design with Contextualized Modeling and Mixed Sampling

**Authors:** Hengyuan Cao, Shizhuo Cheng, Mingxuan Liu, Weicheng Huang, Yunhong Lu, et al. (8 authors)

**Summary:** Chamaileon extends protein binder design beyond the common single-target, single-state assumption to model multi-target and multi-state interactions needed for advanced function-oriented design. It combines contextualized sequence-structure modeling with a mixed sampling strategy for generation.

**arXiv:** [arxiv.org/abs/2607.23518](https://arxiv.org/abs/2607.23518)
**Sources:** HuggingFace Daily Papers (6 upvotes)
**Why trending:** AI-for-biology / protein design remains a high-interest cross-over field between ML and structural biology research communities.

---

## 13. dRAE: Representation Autoencoder with Hyper-Spherical Codes

**Authors:** Tianren Ma, Lin Long, Chuyan Chen, Mu Zhang, Junbo Zhao, et al. (7 authors)

**Summary:** dRAE tackles codebook collapse in visual tokenization by identifying a metric mismatch — standard Euclidean codebook objectives don't fit the anisotropic geometry of representation space — and instead uses hyper-spherical codes aligned to that geometry. This allows discretizing high-dimensional visual representations to bridge vision and language models without losing semantic coherence.

**arXiv:** [arxiv.org/abs/2607.22148](https://arxiv.org/abs/2607.22148)
**Sources:** HuggingFace Daily Papers (6 upvotes)
**Why trending:** Visual tokenization quality is foundational to multimodal LLMs, and codebook collapse is a well-known unsolved pain point.

---

## 14. DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes

**Authors:** Jiahao Xie, Zhongbin Guo, Qianle Wang, Ruiqi Lu, Dongling Xiao, et al. (7 authors)

**Summary:** DecoupleMix turns VLM pretraining data-mixture design, currently mostly heuristic, into a systematic mixture-optimization problem. It decouples ratio search from convex budget allocation to produce a reproducible, attributable method for constructing pretraining data recipes at scale.

**arXiv:** [arxiv.org/abs/2607.24516](https://arxiv.org/abs/2607.24516)
**Sources:** HuggingFace Daily Papers (5 upvotes)
**Why trending:** Data-mixture optimization is a recurring bottleneck for VLM training that most labs treat as a trade secret; a principled, reproducible method fills a real gap.

---

## 15. ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding

**Authors:** Hangjie Yuan, Yichen Qian, Zhiwei Tang, Xianzhe Xu, Lirong Wu, et al. (24 authors)

**Summary:** ClinFusion is a vision-centric multimodal LLM designed to absorb knowledge from heterogeneous 2D and 3D medical imaging, aiming at holistic clinical understanding rather than narrow single-modality tasks. It also proposes evaluation protocols aligned with actual radiologist practice for fine-grained, factuality-driven assessment.

**arXiv:** [arxiv.org/abs/2607.24743](https://arxiv.org/abs/2607.24743)
**Sources:** HuggingFace Daily Papers (4 upvotes)
**Why trending:** Medical multimodal AI with clinician-aligned evaluation addresses a recognized weakness (misaligned benchmarks) in healthcare AI research.

---

## 16. Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models

**Authors:** Junlin Fang, Do Nguyen-Thanh, Xiaogang Xu, Zhen Fang, Sean Du (5 authors)

**Summary:** The paper identifies that long reasoning traces from large reasoning models contain noisy irrelevant and repetitive steps that obscure signals useful for hallucination detection. It proposes a "Reasoning Denoiser" that filters these noisy steps to substantially improve hallucination-detection performance.

**arXiv:** [arxiv.org/abs/2607.22098](https://arxiv.org/abs/2607.22098)
**Sources:** HuggingFace Daily Papers (4 upvotes)
**Why trending:** Hallucination detection in reasoning models (o1/R1-style) is a top safety/reliability concern as reasoning-trace-based models proliferate.

---

## 17. Codifying the Judge: Scalable Evaluation via Program Distillation

**Authors:** Tzu-Heng Huang, Shengqi Qiu, Frederic Sala (3 authors)

**Summary:** Instead of prompting an LLM-as-judge at evaluation time (costly, slow, opaque), this work distills the judge's decision logic into a committee of inspectable programs that score candidates directly. This yields transparent, editable, and cheap evaluators as a scalable alternative to LLM-as-judge.

**arXiv:** [arxiv.org/abs/2607.22561](https://arxiv.org/abs/2607.22561)
**Sources:** HuggingFace Daily Papers (4 upvotes)
**Why trending:** LLM-as-judge cost/opacity is a widely-felt pain point in eval pipelines; a program-distillation alternative is immediately practical.

---

## 18. FilmBench: A Film-Grade Benchmark for Cinematic Video Generation

**Authors:** Shengyi Wang, Niantong Li, Guangzheng Hu, Hong Qi, Fei Ding, et al. (30 authors)

**Summary:** FilmBench critiques existing video-generation benchmarks for relying on web/LLM-templated prompts and generic multimodal scorers rather than professional cinematic-language criteria. It introduces evaluation taxonomies grounded in how films are actually made and judged by industry professionals.

**arXiv:** [arxiv.org/abs/2607.24241](https://arxiv.org/abs/2607.24241)
**Sources:** HuggingFace Daily Papers (3 upvotes)
**Why trending:** As video generation quality approaches professional footage, benchmark rigor grounded in filmmaking craft is a timely and needed contribution.

---

## 19. A Frozen 12B Beats Frontier Models on Verified Work: 100% Accuracy, 0 Tokens, Bit-Exact, Forever

**Authors:** Sietse Schelpe (1 author)

**Summary:** Instead of retraining models to improve them, this work keeps a 12B model frozen and grows a persistent memory of independently-verified solutions beside it — once a problem family is solved and verified without consulting the answer key, future instances are answered at zero generation tokens, deterministically. Across 180 fresh test instances, this frozen-model-plus-memory approach reportedly matches or beats frontier model accuracy on verified work.

**arXiv:** [arxiv.org/abs/2607.23806](https://arxiv.org/abs/2607.23806)
**Sources:** HuggingFace Daily Papers (3 upvotes)
**Why trending:** A provocative, contrarian claim (no retraining needed, zero-token deterministic answers) against the industry's retrain-everything norm — the kind of title that draws outsized discussion relative to its author count.

---

## 20. GNM Head: A Generative aNthropometric Model of the human head

**Authors:** Stylianos Ploumpis, Jan Bednarik, Gaspard Zoss, Ruslan Guseinov, Luca Prasso, et al. (29 authors)

**Summary:** GNM Head is a new parametric/generative model of the human head that extends anatomical scope beyond outer geometry alone to include intra-oral and ocular structures, addressing gaps in existing publicly available head models. It is designed to serve as a conditioning signal for generative vision models needing tight spatial control over head/face imagery.

**arXiv:** [arxiv.org/abs/2607.23687](https://arxiv.org/abs/2607.23687)
**Sources:** HuggingFace Daily Papers (3 upvotes)
**Why trending:** Parametric head models underpin a wide swath of avatar/animation/generative-portrait pipelines, and anatomical completeness is a recognized gap this fills.
