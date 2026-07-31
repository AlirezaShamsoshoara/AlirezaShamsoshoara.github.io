---
title: "Daily AI Papers — July 31, 2026"
date: 2026-07-31
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-31/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-memory
  - gui-agents
  - world-models
---

## 1. Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents

**Authors:** Hanzhang Zhou, Panrong Tong, Xu Zhang, Quyu Kong, Chenglin Cai, et al.

**Summary:** Presents Qwen-UI-Agent, a foundation GUI agent designed to operate reliably on real devices across platforms, combining GUI interaction with CLI execution for long-horizon tasks. The system aims to proactively initiate useful services and autonomously improve its own capabilities with minimal human supervision.

**arXiv:** [arxiv.org/abs/2607.28227](https://arxiv.org/abs/2607.28227)
**Sources:** HuggingFace Daily Papers (229 upvotes, 3 comments — top of the day)
**Why trending:** Highest upvote count on HF today by a wide margin; a major-lab (Qwen/Alibaba) technical report on GUI agents taps into the hottest current agent-research theme.

---

## 2. Metis: Memory Foundation Model

**Authors:** Zeyu Zhang, Ziliang Guo, Yihang Sun, Xichong Zhang, Xixuan Hao, et al.

**Summary:** Introduces Metis, an attempt to natively internalize agent memory capability into a foundation model rather than bolting it on as an external module. Positions native memory as an underexplored counterpart to the internalized reasoning/tool-use capabilities seen in recent large reasoning models.

**arXiv:** [arxiv.org/abs/2607.26760](https://arxiv.org/abs/2607.26760)
**Sources:** HuggingFace Daily Papers (211 upvotes, 2 comments)
**Why trending:** Second-highest upvotes; "memory as a foundation model capability" is a fast-growing subfield with at least 3 other papers in today's top 20 addressing memory (Memory Decoder, MemHarness, Filesystem-Based Memory).

---

## 3. AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis

**Authors:** Bing Yan, Gregory Wolfe, Stefano Martiniani, Kyunghyun Cho, et al.

**Summary:** Proposes a claim-centered (rather than document-ranking) infrastructure for chemistry literature search, letting scientists and AI agents assemble cross-paper, provenance-verified answers instead of manually sifting document lists.

**arXiv:** [arxiv.org/abs/2607.28618](https://arxiv.org/abs/2607.28618)
**Sources:** HuggingFace Daily Papers (198 upvotes, 1 comment)
**Why trending:** High upvotes driven by strong author lineup (Kyunghyun Cho) and interest in AI-for-science literature tooling.

---

## 4. PhiZero: A World Model Built Around Physical Language

**Authors:** Shuyao Shang, Yuqi Wang, Ruopeng Gao, Xu Chen, Tieniu Tan, et al.

**Summary:** Introduces "physical language," a compact discrete representation of world-state transitions, as the backbone of a new physical world model — moving away from predicting raw future video pixels toward abstracted predictive structure.

**arXiv:** [arxiv.org/abs/2607.28624](https://arxiv.org/abs/2607.28624)
**Sources:** HuggingFace Daily Papers (148 upvotes, 1 comment)
**Why trending:** World-model research remains a hot area; the "discrete physical language" framing is a novel angle drawing significant early engagement.

---

## 5. Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering

**Authors:** Junlin Yang, Che Jiang, Yu Fu, Tianwei Luo, Can Ren, et al.

**Summary:** Introduces OpenMLE, a full-stack open system for studying recursive self-improvement (RSI) through machine learning engineering as a concrete, verifiable testbed, spanning task environments, operator learning, and long-horizon training.

**arXiv:** [arxiv.org/abs/2607.28568](https://arxiv.org/abs/2607.28568)
**Sources:** HuggingFace Daily Papers (114 upvotes, 1 comment)
**Why trending:** Recursive self-improvement / "AI building AI" is a headline topic in frontier AI safety and capability discourse.

---

## 6. VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System

**Authors:** Haodong Li, Tianfei Ren, Xiaoxiao Ma, Chunmei Qing, Zhen Fang, et al.

**Summary:** Tackles the physical-consistency problem in text-to-video generation by using executable code as an intermediate chain-of-thought representation instead of non-executable or sparse intermediate plans, via a dual-engine agentic system.

**arXiv:** [arxiv.org/abs/2607.27380](https://arxiv.org/abs/2607.27380)
**Sources:** HuggingFace Daily Papers (61 upvotes, 1 comment)
**Why trending:** Bridges two hot threads — code-as-reasoning and video generation physics — appealing to both the agents and generative-video communities.

---

## 7. Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory

**Authors:** Rubin Wei, Jiaqi Cao, Jiarui Wang, Junming Zhang, Qipeng Guo, et al.

**Summary:** Scales the "Memory Decoder" parametric long-term memory module up to 6.9B parameters pretrained on 300B tokens, addressing the entanglement of long-term memory and reasoning in decoder-only LLMs.

**arXiv:** [arxiv.org/abs/2607.27919](https://arxiv.org/abs/2607.27919)
**Sources:** HuggingFace Daily Papers (44 upvotes, 1 comment)
**Why trending:** Direct scaling follow-up to a known architecture idea; part of today's broader wave of memory-focused papers.

---

## 8. Beacon: Knowing When and How to Perform Agentic Visual Reasoning

**Authors:** Qixun Wang, Yang Shi, Letian Cheng, Zhuoran Zhang, Yan He, et al.

**Summary:** Reframes agentic visual reasoning around two axes — Mode Adaptiveness and Tool Effect — aiming to boost MLLM task success rates rather than just adding sophisticated but inefficient reasoning chains.

**arXiv:** [arxiv.org/abs/2607.28595](https://arxiv.org/abs/2607.28595)
**Sources:** HuggingFace Daily Papers (43 upvotes, 1 comment)
**Why trending:** Addresses efficiency of agentic tool-use in multimodal reasoning, a practical pain point for deployed MLLM agents.

---

## 9. BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation Paradigms

**Authors:** Pengyu Wang, Benfeng Xu, Shaohan Wang, Xin Zeng, Huarui Wu, et al.

**Summary:** A controlled scaling study across 28 nested corpus-size tiers (roughly 450x range) comparing lexical, dense, graph-based, and agentic RAG paradigms, finding classic BM25 lexical retrieval remains highly competitive at scale.

**arXiv:** [arxiv.org/abs/2607.26497](https://arxiv.org/abs/2607.26497)
**Sources:** HuggingFace Daily Papers (38 upvotes, 3 comments)
**Why trending:** Provocative, counter-narrative title challenging the assumption that dense/agentic retrieval always wins — high comment-to-upvote ratio suggests active debate.

---

## 10. Flux-OPD: On-Policy Distillation with Evolving Contexts

**Authors:** Yuran Wang, Zekun Wang, Bohan Zeng, Ruixu Zhang, Wenxuan Liu, et al.

**Summary:** Addresses training in open-ended domains lacking verifiable rewards by using contexts that evolve alongside student performance during on-policy distillation, rather than static distilled preference contexts.

**arXiv:** [arxiv.org/abs/2607.28022](https://arxiv.org/abs/2607.28022)
**Sources:** HuggingFace Daily Papers (35 upvotes, 1 comment)
**Why trending:** On-policy distillation is a hot post-training technique; evolving-context angle is a fresh contribution to RLHF-adjacent methods.

---

## 11. MPIE-Bench: Benchmarking Anatomically Plausible Multi-Person Interaction Editing

**Authors:** Jiajia Lin, Mingxuan Du, Tuowen Zhou, Benfeng Xu, Hongtao Xie, et al.

**Summary:** Introduces a benchmark targeting a known failure mode of text-to-image/personalized editing models: multi-person contact interactions (embrace, carry, grapple) that produce fused limbs and anatomical errors.

**arXiv:** [arxiv.org/abs/2607.27616](https://arxiv.org/abs/2607.27616)
**Sources:** HuggingFace Daily Papers (35 upvotes, 1 comment)
**Why trending:** Fills a clearly visible, relatable gap in image-generation evaluation that's easy to demo and discuss.

---

## 12. ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine

**Authors:** Yukang Cao, Haozhe Xie, Beichen Wen, Runmao Yao, Yinghao Liu, et al.

**Summary:** Presents a data engine for embodied intelligence that jointly captures first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch to overcome fragmentation in existing embodied datasets.

**arXiv:** [arxiv.org/abs/2607.28625](https://arxiv.org/abs/2607.28625)
**Sources:** HuggingFace Daily Papers (33 upvotes, 0 comments)
**Why trending:** Embodied-AI data bottleneck is a widely cited constraint; a unified multi-modal capture pipeline draws robotics/embodied-AI interest.

---

## 13. Beyond Borrowed Histories: Person-Aligned User Simulation for Interactive Role-Playing Evaluation

**Authors:** Yuhang Zhu, Mingxuan Du, Benfeng Xu, Jie Gao, Lingyun Yu, et al.

**Summary:** Proposes a person-aligned user-simulation approach for evaluating role-playing agents (RPAs) through genuinely interactive multi-turn conversation rather than continuation of a fixed dialogue history.

**arXiv:** [arxiv.org/abs/2607.27816](https://arxiv.org/abs/2607.27816)
**Sources:** HuggingFace Daily Papers (29 upvotes, 1 comment)
**Why trending:** Role-playing/companion agents are a major consumer LLM application category with weak existing evaluation standards.

---

## 14. RefCaptioner: Multi-Reference Image-Grounded Video Captioning

**Authors:** Tengfei Liu, Yang Shi, Yuran Wang, Xiaohan Zhang, Yuqing Wen, et al.

**Summary:** Introduces a new task — multi-reference image-grounded video captioning — requiring phrase-level grounding of captions to multiple reference images, along with a two-stage post-training framework (RefCaptioner) to solve it.

**arXiv:** [arxiv.org/abs/2607.28509](https://arxiv.org/abs/2607.28509)
**Sources:** HuggingFace Daily Papers (24 upvotes, 1 comment)
**Why trending:** Extends video captioning toward more precise, controllable grounding — relevant to video-editing and retrieval pipelines.

---

## 15. SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them

**Authors:** Yang Zhou, Zixuan Huang, Sunzhu Li, Zhuo Yang, Chen Zhang, et al.

**Summary:** Targets the capability mismatch in VLMs between task-level reasoning and fine-grained visual/spatial detail by first teaching models to use specialist spatial tools, then distilling that ability so tools are no longer needed at inference.

**arXiv:** [arxiv.org/abs/2607.27703](https://arxiv.org/abs/2607.27703)
**Sources:** HuggingFace Daily Papers (21 upvotes, 1 comment)
**Why trending:** "Learn with tools, then internalize" is a compelling recipe for efficient VLM deployment, echoing broader distillation trends.

---

## 16. See2Think: Do Multimodal Models Really Use Intermediate Visual States?

**Authors:** Siyu Yan, Zhuoran Yan, Haiying Xu, Panhao Zhou, Jingyu Chen, et al.

**Summary:** A diagnostic benchmark probing whether MLLMs genuinely rely on intermediate visual states (sketches, annotations, tool outputs) during reasoning, rather than just producing plausible final answers.

**arXiv:** [arxiv.org/abs/2607.26769](https://arxiv.org/abs/2607.26769)
**Sources:** HuggingFace Daily Papers (19 upvotes, 1 comment)
**Why trending:** Interpretability-flavored critique of multimodal chain-of-thought, relevant to the current scrutiny of whether visual CoT is "real" reasoning.

---

## 17. ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow

**Authors:** Jin Cao, Zian Meng, Kaipeng Zhang, et al.

**Summary:** Proposes a representational fix for action-conditioned video world models, learning unified dynamics representations from paired video-and-shadow signals to enable precise, generalizable action control without needing exact structured action encodings.

**arXiv:** [arxiv.org/abs/2607.28362](https://arxiv.org/abs/2607.28362)
**Sources:** HuggingFace Daily Papers (16 upvotes, 2 comments)
**Why trending:** Creative "video and its shadow" framing for action-controllable world models stands out in the crowded video-world-model space.

---

## 18. Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers

**Authors:** Chongjian Ge, Hanwen Jiang, Tianyu Wang, Jiuxiang Gu, Yiran Xu, et al.

**Summary:** Introduces Chimera, a hybrid visual diffusion backbone combining Kimi Delta Attention with other mechanisms to process text, image, and video tokens in a single raster-ordered stream without positional embeddings, with a Chinchilla-style scaling recipe.

**arXiv:** [arxiv.org/abs/2607.28611](https://arxiv.org/abs/2607.28611)
**Sources:** HuggingFace Daily Papers (15 upvotes, 0 comments)
**Why trending:** Addresses the quadratic-attention cost bottleneck for high-res/long-video diffusion generation with a principled scaling law study.

---

## 19. MemHarness: Memory Is Reconstructed, Not Replayed

**Authors:** Rong Wu, Daocheng Fu, Licheng Wen, Xuemeng Yang, Shu Zou, et al.

**Summary:** Challenges the common "replay" paradigm in memory-augmented LLM agents, which injects retrieved experiences verbatim regardless of relevance, proposing instead that retrieved memories should be reconstructed to fit the agent's current situation.

**arXiv:** [arxiv.org/abs/2607.28272](https://arxiv.org/abs/2607.28272)
**Sources:** HuggingFace Daily Papers (13 upvotes, 1 comment)
**Why trending:** Another entry in today's strong memory-architecture cluster, with a cognitive-science-flavored critique of the dominant retrieval paradigm.

---

## 20. Can Large Language Models Execute Parent Orders?

**Authors:** Zane Shen, Xinli Xu, Guangyi Zhang, Jialong Chen, Jinsong Zhou, et al.

**Summary:** The first systematic study of LLMs on parent-order execution in algorithmic trading — splitting a large order into smaller ones to minimize execution cost — comparing against approaches that rely on fixed market assumptions or task-specific training.

**arXiv:** [arxiv.org/abs/2607.28410](https://arxiv.org/abs/2607.28410)
**Sources:** HuggingFace Daily Papers (12 upvotes, 1 comment)
**Why trending:** Niche but notable application of LLMs to quantitative finance/algo-trading, a domain with growing AI adoption interest.
