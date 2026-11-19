---
title: "Daily AI Papers — November 19, 2026"
date: 2026-11-19
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-19/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - world-models
  - efficient-models
---

### 1. Jeveration: System One Models Now Generate
**Authors:** Yuhe Liu, Qi Li, Shihua Zhang, Xinchao Wang
**arXiv:** [arxiv.org/abs/2611.24738](https://arxiv.org/abs/2611.24738)
**Summary:** Jeveration repurposes a frozen vision-language model for single-pass image generation, using a shared random state and learned discrete-code distributions to coordinate coherent parallel predictions. One checkpoint also supports image-to-image generation and dense prediction, producing a 512x512 image in 78 ms with competitive quality and up to 122x speedup over existing unified models.

---

### 2. The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements
**Authors:** Yuanhao Zeng, Shaocheng Lan, Ao Lu, Kuang Yan, Heng Lin, Xinang Xu, Yuan Luo, Yueting Wang, Yexin Li, Ruo Shan, Kan Ren
**arXiv:** [arxiv.org/abs/2611.23068](https://arxiv.org/abs/2611.23068)
**Summary:** The Resolution Hypothesis argues that agent evolution often stalls because noisy evaluation cannot distinguish helpful candidate prompts, skills, and memories from harmful ones. Across seven evolution methods and six models with over 10 million LLM calls, the authors find unreliable candidate selection and method rankings whose small margins are overwhelmed by run-to-run variation.

---

### 3. ALIVE: Making Streaming Video Models Interactive
**Authors:** Jinzhao Li, Yuan Xu, Jinxuan Wu, Yukun Wang, Yijia Lei, Hanyu Ji, Yinuo Chen, Zining Huang, Chi Zhang, Hang Ye, Yiwu Zhong, Honglei Yan, Panwang Pan, Yizhou Wang, Yin Li, Miao Liu
**arXiv:** [arxiv.org/abs/2611.21366](https://arxiv.org/abs/2611.21366)
**Summary:** ALIVE is an interactive streaming video model supporting proactive monitoring, streaming task coordination, and feedback-seeking interactions. Contrastive supervised fine-tuning followed by reinforcement learning with Behavior-Aligned Credit Assignment trains responses and silence across turns, with the highest overall scores among compared models on four public benchmarks and the new FSI-Bench.

---

### 4. PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling
**Authors:** Minseo Yoon, Minseong Bae, Sojin Lee, Hyunwoo J. Kim
**arXiv:** [arxiv.org/abs/2611.11318](https://arxiv.org/abs/2611.11318)
**Summary:** This work formulates predictive spatiotemporal weather downscaling as forecasting future high-resolution trajectories from recent coarse states, using a shared pretrained backbone with spatial and temporal stages. PROLA splits a fixed low-rank adaptation budget between principal weight directions and their orthogonal complement, then rescales rank-1 updates with gradient signals, outperforming representative low-rank baselines in weather downscaling and additional tasks.

---

### 5. Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development
**Authors:** Xirui Jiang, Yuxi Chen, Rui Yang, Feng Luo, Pengcheng Wang, Bingxuan Li, Zihao Zhao, Yushan Li, Han Wang, Manling Li, Yang Zhang, Shiyu Chang, Tong Zhang, Huan Zhang
**arXiv:** [arxiv.org/abs/2611.24154](https://arxiv.org/abs/2611.24154)
**Summary:** Game2Player co-develops web-game environments and players, using a Builder agent to expose state and define verifiable tasks while Coding and VLM Players validate environments and collect training experience. The resulting 568 games, 3,436 tasks, and 15.7K trajectories support progress-weighted supervised training, improving Game2Player-9B progress to 31.2% on PlayerBench and 53.1% on GameWorld.

---

### 6. HINT-WAM: Hindsight-Informed Training for World Action Models
**Authors:** Phuong Tuan Dat, Qi Li, Xinchao Wang
**arXiv:** [arxiv.org/abs/2611.24789](https://arxiv.org/abs/2611.24789)
**Summary:** HINT-WAM introduces on-policy self-distillation for world action models, using future demonstration video as privileged hindsight to supervise the action expert along its own denoising trajectories. An energy-score objective matches the hindsight-conditioned teacher's action distribution from student samples, while deployment uses only ordinary observations and training needs neither environmental rewards nor simulator interaction.

---

### 7. CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning
**Authors:** Zeguan Xiao, Zhuocheng Liang, Yun Chen, Yong Wang, Guanhua Chen, Pinyan Lu
**arXiv:** [arxiv.org/abs/2611.24654](https://arxiv.org/abs/2611.24654)
**Summary:** CurvDelta constrains language-model updates to a low-curvature space that leaves a preservation loss nearly invariant, using Kronecker-factored approximate curvature and factorized projection to make the construction practical. Its low-rank CurvLoRA variant and full framework improve acquisition-retention trade-offs in mathematical reasoning, code generation, and selective knowledge unlearning relative to the evaluated baselines.

---

### 8. LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning
**Authors:** Eilam Shapira, Alan Arazi, Shoham Grunblat, Roi Reichart
**arXiv:** [arxiv.org/abs/2611.17600](https://arxiv.org/abs/2611.17600)
**Summary:** LightTAR augments PCA-reduced text and image embeddings with a few target-aware features extracted from final and intermediate encoder layers through regularized partial least squares. Across 21 tabular learners it improves average prediction performance with a small runtime increase, without changing either the pretrained encoder or the downstream learner.

---

### 9. WorldRuler: Interactive World Modeling under Configurable Rules
**Authors:** Mingliang Zhai, Chuanhao Li, Jiaming Tan, Zhen Li, Yuwei Wu, Yunde Jia, Zian Meng, Yuanyang Yin, Kaipeng Zhang
**arXiv:** [arxiv.org/abs/2611.24869](https://arxiv.org/abs/2611.24869)
**Summary:** WorldRuler connects an executable 3D rule graph, video generation, and perceptual feedback so interactive world models can follow configurable rules and restore consistent rules and states after saving and loading. Dynamic object binding and counterfactual reconstruction training support attribute control, evaluated using the RuleVerse dataset of rule-driven interactions collected from GTA-V and Habitat.

---

### 10. Code World Model 2.0: Towards Infinite Controllable Video Generation
**Authors:** Ruoyu Wang, Hao Zhong, Yanming Yang, Jiahao Tian, Lin Liu, Biao Gong, Guoshan Lu, Yiding Tian, Chunhua Shen, Zhenzhong Lan, Chi Zhang
**arXiv:** [arxiv.org/abs/2611.22925](https://arxiv.org/abs/2611.22925)
**Summary:** Invoker-Render pairs bidirectional video creation with a causal four-step streaming model under shared conditioning on structural proxies, appearance references, and language. Progressive Forcing moves training from video-derived histories to continuous self-generated rollouts, enabling versatile control and stable 30-minute racing rollouts that preserve scene and subject appearance.

---

### 11. QDA: Closed-Loop LLM Quantization Design with Agents
**Authors:** Xingyang Li, Tianlang Zhao, Song Han, Ligeng Zhu
**arXiv:** [arxiv.org/abs/2611.23388](https://arxiv.org/abs/2611.23388)
**Summary:** QDA uses an agent to design model-specific post-training quantization recipes, combining compatible public methods with fast output-KL evaluation and long-generation checks for failure modes. Across four reasoning models it improves accuracy over the strongest public recipes at several precisions, and on GLM-5.3-Flash NVFP4 W4A4 it recovers 98.3% of FP8 accuracy without adding serving-kernel overhead.

---

### 12. Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers
**Authors:** Hansheng Chen, Shengqu Cai, Jan Ackermann, Rayhan Zirvi, Gordon Wetzstein, Xinchen Yan, Leonidas Guibas
**arXiv:** [arxiv.org/abs/2611.22287](https://arxiv.org/abs/2611.22287)
**Summary:** Decoding Without a Decoder adds a linear pixel-prediction head to a finetuned diffusion transformer while retaining the original denoising head to guide sampling. Finetuning only the final blocks removes the latent decoder while preserving or improving image and video quality, including a 23% reduction in Wan video warping error and improved pixel-flow ImageNet FID.

---

### 13. StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model
**Authors:** Chuang Wang, Rui Nie, Jie Song, Junyuan Gao, Jiahe Song, Haitao Zhou, Boyu Zhu, Xing Li, Jiang Wu, Conghui He, Qian Yu, Weijia Li
**arXiv:** [arxiv.org/abs/2611.24408](https://arxiv.org/abs/2611.24408)
**Summary:** StrideWorld evaluates interactive video world models against references fixed before the motion being judged, using start-view geometry for scene rigidity and each model's initial action stride for subsequent consistency. Its validated measurements expose widespread scene deformation and route errors that fitted references can hide, while fine-tuning two models on rendered clips removes most mid-route stalls.

---

### 14. Late Entry in Looped Language Models
**Authors:** Ziqi Jin, Jiaxi Li, Weiwen Xu, Aixin Sun
**arXiv:** [arxiv.org/abs/2611.24576](https://arxiv.org/abs/2611.24576)
**Summary:** Late entry accelerates looped language models by letting new tokens skip initial recurrent passes and use a deep context cache, outperforming matched early exit after lightweight fine-tuning. Wake verification completes prior-token caches alongside later steps and supports exact or lossy decoding, reporting 5.2x greedy-exact speedup on Ouro-2.6B and larger speedups at greater recurrence depth on Huginn-3.5B.

---

### 15. RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language Models
**Authors:** Ruisi Zhao, You Li, Sihan Chen, Aosong Cheng, Chixiang Ma, Sen Pei, Zhen Yang, Hehe Fan, Dongliang He, Yi Yang
**arXiv:** [arxiv.org/abs/2611.24098](https://arxiv.org/abs/2611.24098)
**Summary:** RoughCut-Bench evaluates automatic video rough-cutting in visually driven and transcript-driven workflows, covering highlight selection, video ordering, user requirements, filler removal, deduplication, and trimming. It includes 101 visual cases with 831 source videos and 84 speech cases, pairs annotation-based scoring with a human-aligned rendered-cut evaluator, and finds current vision-language models limited at producing expert-aligned cut plans.

---

### 16. Piccolo: Co-Evolving Decision Models and Data through Recursive Self-Improvement
**Authors:** Zhenqing Ling, Qirui Jiao, Daoyuan Chen, Cheng Chen, Xinji Mai, Haowen Gao, Zhuo Zhang, Xuchen Pan, Mengsu Ding, Jiaji Deng, Yuexiang Xie, Xiaoming Qin, Weirui Kuang, Zhaoyang Liu, Yaliang Li, Bolin Ding, Jingren Zhou
**arXiv:** [arxiv.org/abs/2611.24651](https://arxiv.org/abs/2611.24651)
**Summary:** Piccolo is a family of 0.8B-to-27B multimodal decision models that co-evolves training data and capabilities through agentic data engineering and recursive self-improvement. The study reports strong decision-benchmark results and finds that backbone-recipe co-adaptation and targeted curation can outweigh model recency and size, while decreasing loss can diverge from decision accuracy.

---

### 17. Mechanistic Critics for Sample-Efficient NPU Design-Space Exploration
**Authors:** Yicheng He, Yuqi Xue, Tianyang Wu, Jian Huang, Bin Hu
**arXiv:** [arxiv.org/abs/2611.24733](https://arxiv.org/abs/2611.24733)
**Summary:** CriticNPU uses an online-calibrated Roofline-style mechanistic critic to filter weak NPU designs and explain prefill and decode bottlenecks using operator-level simulator feedback. Across six LLM workloads and 16 deployment configurations per model, it reaches best-or-tied-best latency in 74% of prefill and 87.5% of decode settings with roughly half the simulator calls of competitive baselines.

---

### 18. PReMind: When Personal Memory Meets Visual Hazards
**Authors:** Yeongtak Oh, Donghyeok Lee, Joonhee Oh, Jaewon Jeong, Sungroh Yoon
**arXiv:** [arxiv.org/abs/2611.23808](https://arxiv.org/abs/2611.23808)
**Summary:** PReMind-Bench diagnoses whether personalized vision-language assistants combine visual hazard recognition with relevant personal memories, separately assessing retrieval, grounding, abstention, and hazard response. PReMind jointly trains these behaviors through two-phase reinforcement learning and raises joint success from 12.9% to 28.6% at 4B parameters, with gains persisting under forced retrieval and a second judge.

---

### 19. Tideway: Phase-Aware Tiered Memory Management for MoE Inference on Consumer Devices
**Authors:** Yifei Wang, Tsun-yu Yang, Yechen Xu, Hancheng Ye, Qinsi Wang, Baijun Zhou, Tingjun Chen, Hai "Helen" Li, Danyang Zhuo, Yiran Chen
**arXiv:** [arxiv.org/abs/2611.14848](https://arxiv.org/abs/2611.14848)
**Summary:** TIDEWAY treats host RAM and GPU VRAM as a unified memory pool for large MoE inference on consumer devices whose model weights also spill to SSD. Phase-aware memory layouts and CUDA Graph execution under expert paging yield average 1.97x end-to-end latency speedup, 2.40x faster time to first token, and 1.61x higher decode throughput than the fastest evaluated baseline.

---

### 20. StatePortal: Agentic Checkpoint Synthesis for Testing Deep States in Interactive Software
**Authors:** Zhiyuan Peng, Wei Tao, Chenhao Ying, Yuan Luo, Yiwen Guo
**arXiv:** [arxiv.org/abs/2611.23257](https://arxiv.org/abs/2611.23257)
**Summary:** StatePortal synthesizes replayable checkpoints from natural-language functional tests and read-only source access, using a one-time application hook to reach deep GUI states without long interaction histories. A hybrid state-and-visual oracle validates checkpoints on DeepStateBench, with 98.90% verdict reproducibility across 1,361 replays and detection of 96.25% of controlled visual faults that state-only checks miss.
