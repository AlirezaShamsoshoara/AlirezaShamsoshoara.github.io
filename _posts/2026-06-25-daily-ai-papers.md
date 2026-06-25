---
title: "Daily AI Papers — June 25, 2026"
date: 2026-06-25
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-25/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - video-generation
  - multimodal-reasoning
---

## 1. Are We Ready For An Agent-Native Memory System?
**Authors:** Wei Zhou, Xuanhe Zhou, Shaokun Han, Hongming Xu, Guoliang Li, Zhiyu Li, Feiyu Xiong, Fan Wu (SJTU)
**arXiv:** [arxiv.org/abs/2606.24775](https://arxiv.org/abs/2606.24775)

**Summary:** This paper presents the first systematic experimental study of agent memory from a data management perspective, decomposing it into four core modules: representation & storage, extraction, retrieval & routing, and maintenance. Evaluating 12 representative memory systems across 11 datasets reveals no single architecture dominates; effectiveness depends on workload-memory alignment, and localized maintenance is more cost-efficient than global reorganization.

**Sources:** HuggingFace Daily Papers (#1, 84 upvotes, 3 comments)
**Why Trending:** Top upvoted paper of the day; directly addresses the critical gap in agent systems where memory is benchmarked only via end-to-end metrics, treating it as a black box. Highly relevant for LLM agent developers.

---

## 2. DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation
**Authors:** Nan Chen, Yiyang Cai, Rongchang Xie, Junwen Pan, Cheng Chen, Weinan Jia, Zhuowei Chen, Wen Zhou, Zhenbang Sun, Wenhan Luo
**arXiv:** [arxiv.org/abs/2606.26058](https://arxiv.org/abs/2606.26058)

**Summary:** DomainShuttle proposes a subject-to-video generation framework that flexibly handles both in-domain (high fidelity) and cross-domain (flexible style adaptation) scenarios. It introduces Domain-MoT for domain-aware feature decoupling, Video-Reference DualRoPE for precise spatial modeling, and Cross-Pair Consistent Loss for extracting intrinsic subject features independent of irrelevant attributes.

**Sources:** HuggingFace Daily Papers (#2, 55 upvotes, 1 comment)
**Why Trending:** Strong video generation result with demo video attached; addresses key limitation of existing S2V methods that sacrifice cross-domain flexibility for fidelity.

---

## 3. Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models
**Authors:** Lianghua Huang, Zhifan Wu, Wei Wang, Yupeng Shi, Mengyang Feng, Junjie He et al.
**arXiv:** [arxiv.org/abs/2606.25041](https://arxiv.org/abs/2606.25041)

**Summary:** Wan-Streamer is a native-streaming multimodal foundation model designed for real-time, low-latency, full-duplex audio-visual interaction within a single Transformer. Language, audio, and video are modeled as interleaved tokens for both input and output, enabling seamless interactive experiences without separate module pipelines.

**Sources:** HuggingFace Daily Papers (#3, 38 upvotes, 2 comments)
**Why Trending:** End-to-end real-time multimodal interaction is a highly sought capability; single-model approach vs. pipelined systems is architecturally significant.

---

## 4. ShutterMuse: Capture-Time Photography Guidance with MLLMs
**Authors:** Jiayu Li, Yixiao Fang, Tianyu Hu, Wei Cheng, Ping Huang, Zheheng Fan et al.
**arXiv:** [arxiv.org/abs/2606.25763](https://arxiv.org/abs/2606.25763)

**Summary:** ShutterMuse addresses real-world photography guidance — telling photographers how to frame their shot and direct subjects in real time. It introduces CaptureGuide-Bench, a new benchmark that goes beyond post-hoc crop prediction to evaluate both camera framing and subject pose recommendations from MLLMs.

**Sources:** HuggingFace Daily Papers (#4, 36 upvotes, 1 comment)
**Why Trending:** Practical MLLM application for photography; new benchmark that fills a gap in MLLM evaluation beyond standard aesthetic cropping tasks.

---

## 5. Improved Large Language Diffusion Models (iLLaDA)
**Authors:** Shen Nie, Qiyang Min, Shaoxuan Xu, Zihao Huang, Yuxuan Song, Yong Shan et al.
**arXiv:** [arxiv.org/abs/2606.25331](https://arxiv.org/abs/2606.25331)

**Summary:** iLLaDA is an 8B masked diffusion language model trained from scratch with fully bidirectional attention, scaled to 12T pretraining tokens and 25B fine-tuning tokens. It maintains the masked diffusion objective throughout both pretraining and SFT, representing a significant challenge to the autoregressive paradigm as a viable large-scale alternative.

**Sources:** HuggingFace Daily Papers (#5, 27 upvotes, 1 comment)
**Why Trending:** Diffusion LLMs as a credible alternative to autoregressive models remains one of the most debated topics; scaling to 8B with 12T tokens is a major milestone for this line of work.

---

## 6. Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence
**Authors:** Xuanle Zhao, Qiushi Sun, Jingyu Xiao, Xuexin Liu, Haoyue Yang, Qiaosheng Chen et al.
**arXiv:** [arxiv.org/abs/2606.15932](https://arxiv.org/abs/2606.15932)

**Summary:** This survey systematically covers LLM code generation that goes beyond text-only inputs, cataloging tasks where intent is specified via screenshots, charts, vector drawings, videos, and interactive UI states. It maps out how models must connect visual perception to executable programs, where correctness depends on layout, data semantics, and interaction patterns — not just syntax.

**Sources:** HuggingFace Daily Papers (#6, 27 upvotes, 1 comment)
**Why Trending:** Comprehensive structured survey filling a gap in the code intelligence literature; directly relevant to GUI agents and programming assistants.

---

## 7. MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
**Authors:** JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira
**arXiv:** [arxiv.org/abs/2606.26087](https://arxiv.org/abs/2606.26087)

**Summary:** MVTrack4Gen uses multi-view point tracking as a geometric supervision signal to synthesize novel-view videos from monocular reference videos along target camera trajectories. Unlike methods relying on explicit 3D reconstruction that fail on dynamic objects, this approach maintains geometric consistency and motion fidelity without needing accurate off-the-shelf reconstruction modules.

**Sources:** HuggingFace Daily Papers (#7, 24 upvotes, 1 comment)
**Why Trending:** 4D video generation with dynamic scene handling is a frontier problem; avoids the brittleness of explicit reconstruction pipelines.

---

## 8. V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning
**Authors:** Haoxiang Sun, Zhihang Yi, Langxuan Deng, Yuhao Zhou, Peiqi Jia, Jian Zhao et al.
**arXiv:** [arxiv.org/abs/2606.25319](https://arxiv.org/abs/2606.25319)

**Summary:** V-Zero enables fine-grained visual reasoning in MLLMs without requiring any labeled answers or costly annotation of reasoning traces. It uses contrastive evidence gating to identify task-relevant visual evidence regions, and on-policy distillation trains the model on its own outputs without ground-truth labels or hand-designed verification rules.

**Sources:** HuggingFace Daily Papers (#8, 19 upvotes, 1 comment)
**Why Trending:** Label-free training for visual reasoning eliminates a major bottleneck; addresses both cost and supervision quality problems simultaneously.

---

## 9. UnityShots: Memory-Driven Multi-Shot Audio-Video Generation with Boundary-Aware Gating
**Authors:** Jiehui Huang, Yuechen Zhang, Bin Xia, Jiahao Wang, Xu He, Zhenchao Tang et al.
**arXiv:** [arxiv.org/abs/2606.21661](https://arxiv.org/abs/2606.21661)

**Summary:** UnityShots generates coherent multi-shot videos by maintaining structured cross-shot memory for subject appearance, scene context, and speaker identity across cuts. It uses boundary-aware gating to selectively update memory at shot transitions, avoiding both the scalability limits of end-to-end sequence training and the linear memory growth of shot-by-shot banks.

**Sources:** HuggingFace Daily Papers (#9, 19 upvotes, 1 comment)
**Why Trending:** Long-form coherent video generation with shot consistency is a key commercial use case; efficient memory architecture is technically novel.

---

## 10. IV-CoT: Implicit Visual Chain-of-Thought for Structure-Aware Text-to-Image Generation
**Authors:** Zixuan Li, Haokun Lin, Yicheng Xiao, Zhiwei Li, Xinyang Song, Zelong Zheng et al.
**arXiv:** [arxiv.org/abs/2606.24849](https://arxiv.org/abs/2606.24849)

**Summary:** IV-CoT disentangles structural planning (object counts, spatial layout, attribute binding) from appearance rendering in unified MLLMs by introducing an implicit visual chain-of-thought conditioning stream. This separation improves prompt following fidelity for compositional scenes where structure-unaware generation fails.

**Sources:** HuggingFace Daily Papers (#10, 13 upvotes, 1 comment)
**Why Trending:** Compositional text-to-image generation remains a persistent failure mode; separating structure from style via CoT is an elegant architectural fix.

---

## 11. EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies
**Authors:** Ning Gao, Jinliang Zheng, Xing Gao, Haoxiang Ma, Hanqing Wang, Yukai Wang et al.
**arXiv:** [arxiv.org/abs/2606.18239](https://arxiv.org/abs/2606.18239)

**Summary:** EBench is a simulation benchmark with 26 manipulation tasks annotated along 5 capability dimensions and 4 generalization dimensions, providing granular diagnosis beyond a single success rate. Evaluation of π₀, π₀.₅, XVLA, and InternVLA-A1 reveals critical failure modes invisible to scalar metrics.

**Sources:** HuggingFace Daily Papers (#11, 13 upvotes, 1 comment)
**Why Trending:** Robotics community needs diagnostic benchmarks beyond success rates; head-to-head comparison of major SOTA models is immediately useful.

---

## 12. Causal-rCM: Autoregressive Diffusion Distillation for Streaming Video Generation and Interactive World Models
**Authors:** Kaiwen Zheng, Guande He, Min Zhao, Jintao Zhang, Huayu Chen, Jianfei Chen
**arXiv:** [arxiv.org/abs/2606.25473](https://arxiv.org/abs/2606.25473)

**Summary:** Causal-rCM extends the rCM diffusion distillation framework to autoregressive video diffusion transformers using a unified teacher-forcing and self-forcing recipe. The approach enables real-time streaming video generation and action-conditioned interactive world models by leveraging complementarity between forward and reverse divergences.

**Sources:** HuggingFace Daily Papers (#12, 12 upvotes)
**Why Trending:** Interactive world models with real-time streaming are critical for robotics simulation and game AI; distillation approach offers practical speedups.

---

## 13. The Hitchhiker's Guide to Agentic AI: From Foundations to Systems
**Authors:** Haggai Roitman (Snowflake)
**arXiv:** [arxiv.org/abs/2606.24937](https://arxiv.org/abs/2606.24937)

**Summary:** A comprehensive practitioner's reference for building autonomous AI systems, covering the full stack from transformer architecture and GPU systems to memory, planning, tool use, multi-agent coordination, and production deployment. Organized around the thesis that building great agentic systems requires understanding every layer of the pipeline.

**Sources:** HuggingFace Daily Papers (#13, 9 upvotes)
**Why Trending:** Comprehensive agentic AI reference at a time when the field is maturing rapidly; practitioner-focused rather than purely academic.

---

## 14. Autodata: An Agentic Data Scientist to Create High Quality Synthetic Data
**Authors:** Ilia Kulikov, Chenxi Whitehouse, Tianhao Wu, Yixin Nie, Swarnadeep Saha, Eryk Helenowski (Meta AI)
**arXiv:** [arxiv.org/abs/2606.25996](https://arxiv.org/abs/2606.25996)

**Summary:** Autodata trains AI agents to act as data scientists that build high-quality training and evaluation data, then meta-optimizes those agents to create even stronger data. It introduces Agentic Self-Instruct as a practical implementation and demonstrates improvements on computer science tasks.

**Sources:** HuggingFace Daily Papers (#14, 8 upvotes)
**Why Trending:** Meta AI paper on automated synthetic data generation; meta-optimization of data creation agents is a novel and scalable approach for data-hungry models.

---

## 15. Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do
**Authors:** Zhuoran Jin, Kejian Zhu, Hongbang Yuan, Yupu Hao, Pengfei Cao, Yubo Chen et al.
**arXiv:** [arxiv.org/abs/2606.22565](https://arxiv.org/abs/2606.22565)

**Summary:** This paper systematically investigates the capabilities and limits of multimodal CoT reasoning in large models, evaluating across diverse tasks to understand when visual chain-of-thought helps versus hurts. It provides concrete analysis of failure modes and conditions under which multimodal reasoning chains produce reliable versus unreliable outputs.

**Sources:** HuggingFace Daily Papers (#15, 7 upvotes, 1 comment)
**Why Trending:** Critical analysis of multimodal CoT limitations fills an important gap as practitioners rely increasingly on these techniques without understanding their boundaries.

---

## 16. TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
**Authors:** Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao et al.
**arXiv:** [arxiv.org/abs/2606.26092](https://arxiv.org/abs/2606.26092)

**Summary:** TryOnCrafter enables video virtual try-on with free camera viewpoint control by constructing a renderable 4D try-on proxy that decouples garment fitting from camera trajectory. Existing VVT methods are locked to the source camera; this work enables omnidirectional viewpoint exploration for the first time.

**Sources:** HuggingFace Daily Papers (#16, 6 upvotes, 1 comment)
**Why Trending:** Commercial relevance for e-commerce; novel 4D proxy representation enables a capability not achievable with prior VVT methods.

---

## 17. Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods
**Authors:** Xingsong Ye, Yongkun Du, Jiaxin Zhang, Haojie Zhang, Chong Sun, Chen Li
**arXiv:** [arxiv.org/abs/2606.24484](https://arxiv.org/abs/2606.24484)

**Summary:** This work advances artistic/WordArt scene text recognition by introducing new datasets and methods specifically designed for highly customized fonts, textures, and layouts that defeat standard STR models. The paper benchmarks existing methods, highlights the domain gap, and proposes targeted architectural solutions.

**Sources:** HuggingFace Daily Papers (#17, 6 upvotes, 1 comment)
**Why Trending:** Artistic text recognition is a long-standing weakness of OCR systems with direct practical applications in design, signage, and document understanding.

---

## 18. ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation
**Authors:** Chen Lin, Kedi Chen, Wei Zhang
**arXiv:** [arxiv.org/abs/2606.23104](https://arxiv.org/abs/2606.23104)

**Summary:** ReNIO discovers a consistent asymmetry in on-policy distillation: training only on incorrect (negative) student-generated outputs outperforms training only on correct ones, suggesting negative trajectories carry disproportionately informative signal. It proposes a reweighting strategy that leverages this asymmetry for more efficient LLM reasoning distillation.

**Sources:** HuggingFace Daily Papers (#18, 5 upvotes, 1 comment)
**Why Trending:** Counterintuitive finding with direct implications for LLM training efficiency; challenges the default assumption that positive samples drive learning.

---

## 19. RL-Index: Reinforcement Learning for Retrieval Index Reasoning
**Authors:** Yongjia Lei, Nedim Lipka, Zhisheng Qi, Utkarsh Sahu, Koustava Goswami, Franck Dernoncourt et al.
**arXiv:** [arxiv.org/abs/2606.16316](https://arxiv.org/abs/2606.16316)

**Summary:** RL-Index applies reinforcement learning to teach models which retrieval index to use for complex queries requiring implicit reasoning (e.g., math problems needing the same theorem, code requiring deep reasoning). This goes beyond semantic similarity matching to learn index selection as a reasoning problem.

**Sources:** HuggingFace Daily Papers (#19, 5 upvotes, 1 comment)
**Why Trending:** RAG systems are widely deployed but index selection remains heuristic; applying RL here is a novel and practically impactful contribution.

---

## 20. CAVEWOMAN: How Large Language Models Behave Under Linguistic Input and Output Compression
**Authors:** Morayo Danielle Adeyemi, Ryan A. Rossi, Franck Dernoncourt
**arXiv:** [arxiv.org/abs/2606.24083](https://arxiv.org/abs/2606.24083)

**Summary:** CAVEWOMAN evaluates LLM behavior when prompts use telegraphic "caveman-style" compression (dropping grammar, minimizing words) — a popular prompt hack to cut inference costs. Using a two-channel protocol, it measures task accuracy, realized per-item cost, and reference-text agreement to assess whether this actually saves anything and how it affects output quality.

**Sources:** HuggingFace Daily Papers (#20, 4 upvotes, 1 comment)
**Why Trending:** Directly addresses a widely-used but understudied prompt engineering practice; findings have immediate practical implications for cost-conscious LLM deployments.
