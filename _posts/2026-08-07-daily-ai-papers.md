---
title: "Daily AI Papers — August 07, 2026"
date: 2026-08-07
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-07/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-rl
  - vla-robotics
  - benchmarks
---

### 1. Recursive Synthesis for Long-Horizon Terminal Tasks
**Authors:** Zhongzhi Li, Yucheng Shi, Zongxia Li, Ruhan Wang, Anhao Li, Zixun Huang, Junyao Yang, Lei Ke, Ninghao Liu, Haitao Mi, Leowei Liang
**arXiv:** [arxiv.org/abs/2608.05466](https://arxiv.org/abs/2608.05466)
**Summary:** High-quality long-horizon training data for terminal agents is expensive to produce, often costing hundreds to thousands of dollars per task, because each task must keep the instruction, environment, reference solution, and verifier mutually consistent. Human authoring does not scale, and direct generation with large language models (LLMs) often breaks these dependencies.
**Trending because:** 205 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 2. AgentOPSD: Recursive Self-Distillation for Agentic Reinforcement Learning
**Authors:** Zi-Han Wang, Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Jie Wu, Zhengzhou Cai, Yueqing Sun, Ziang Ye, Linji Hao, Qi Gu, Xunliang Cai, Yongliang Shen, Yujiu Yang
**arXiv:** [arxiv.org/abs/2608.05987](https://arxiv.org/abs/2608.05987)
**Summary:** Reinforcement learning (RL) with verifiable rewards constructs trajectory-level advantage estimates, yet it often fails to credit the few pivotal decisions that determine outcomes in long-horizon, multi-turn agentic tasks. Recent work introduces privileged self-distillation for credit assignment, providing denser supervision, but it remains unclear how such local signals should represent sequential credit.
**Trending because:** 62 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 3. WorldClaw: Agentic 3D Open-World Generation at Scale
**Authors:** Chunchao Guo, Jinpeng Li, Yang Li, Zilong Huang
**arXiv:** [arxiv.org/abs/2608.05248](https://arxiv.org/abs/2608.05248)
**Summary:** Generating large-scale, freely explorable 3D worlds from open-ended text remains challenging because a system must jointly maintain global spatial coherence, rich local content, and explicit assets suitable for downstream editing and reuse. We present WorldClaw, a fully agentic, coarse-to-fine framework for open-world 3D scene generation.
**Trending because:** 44 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 4. GST-Bench: Can VLMs Develop Global Spatial Awareness from Video?
**Authors:** Qifeng Zhang, Kaixiang Huang, Heng Dong, Huang Fang, Junting Chen, Junjie Zhu, Yonghang Chen, Zhiyu Zhang, Wei Li
**arXiv:** [arxiv.org/abs/2608.05747](https://arxiv.org/abs/2608.05747)
**Summary:** Spatial intelligence is fundamental to embodied agents, yet existing benchmarks focus on local spatial perception from single or few viewpoints, overlooking global spatial awareness over continuous, long-horizon visual streams. To address this limitation, we introduce the Global-Spatial-Temporal Benchmark (GST-Bench), a VQA benchmark for global spatial intelligence in video understanding, comprising human-verified questions derived from 6,790 minutes of synthetically generated video.
**Trending because:** 30 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 5. EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning
**Authors:** Zishan Xu, Zhiyuan Yao, Yuxin Chen, Yifu Guo, Zhengxi Lu, Yuquan Lu, Jinyang Huang, Yan Xu, Yasheng Wang, Weinan Zhang, Xingshan Zeng, Weiwen Liu
**arXiv:** [arxiv.org/abs/2608.06197](https://arxiv.org/abs/2608.06197)
**Summary:** Training large language model agents for long-horizon tool use typically relies on interactions with real or synthesized executable environments, whose construction and verification are costly, or on external simulators that are difficult to ground. We introduce EnvACE, an agentic reinforcement learning method that replaces external environment interaction during training with world rehearsal.
**Trending because:** 28 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 6. Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval
**Authors:** Zelong Sun, Jun Wang, Kaicheng Yang, Tiancheng Gu, Ziyong Feng, Zhiwu Lu
**arXiv:** [arxiv.org/abs/2608.06060](https://arxiv.org/abs/2608.06060)
**Summary:** Unified multimodal retrieval aims to identify candidates that satisfy complex user intent expressed through heterogeneous inputs. Although Large Vision-Language Model (LVLM)-based retrievers are efficient and scalable, directly encoding raw multimodal inputs often misses fine-grained discriminative cues, leading to confusion among semantically similar candidates.
**Trending because:** 26 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 7. ChronoVision: Temporal Reasoning via Latent State Reconstruction
**Authors:** Yifan Shen, Jian Xu, Boyi Li, Yuner Zhang, Tianjiao Yu, Bingxuan Li, Houze Yang, Rushi Wang, Xu Cao
**arXiv:** [arxiv.org/abs/2608.05631](https://arxiv.org/abs/2608.05631)
**Summary:** Multimodal large language models excel at passive perception but struggle with complex visual cognitive tasks requiring multi-step temporal reasoning. This degradation largely stems from the inherent ambiguity of language-based reasoning, which often fails to accurately articulate continuous visual transformations.
**Trending because:** 24 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 8. From Economic Agents to Agentic Economies: A Systems Blueprint for Economic World Models
**Authors:** Jiale Han, Xiang Li, Jing Qian, Wenyuan Gu, Pin Gao, Ye Luo, Hongyuan Zha, Dacheng Tao, Benyou Wang, Lin William Cong
**arXiv:** [arxiv.org/abs/2608.06020](https://arxiv.org/abs/2608.06020)
**Summary:** Economic World Models (EWMs) are generative economic models that simulate how economies evolve from within by modeling heterogeneous agents, their beliefs and actions, and the market and institutional mechanisms through which their interactions produce aggregate outcomes. This paper develops an implementation roadmap for building economic world models as generative engines in which heterogeneous agents act, interact, adapt, and co-evolve with markets and institutions, thereby producing economic dynamics from the inside.
**Trending because:** 23 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 9. Interpretable MEG Decoding of Perceived Speech: Cortical Sources and the Stimulus Features That Drive Retrieval
**Authors:** Ilia Semenkov, Daria Kleeva, Ivan Dakhtin, Zarina Maksudova, Alex Ossadtchi
**arXiv:** [arxiv.org/abs/2608.01481](https://arxiv.org/abs/2608.01481)
**Summary:** Short segments of perceived speech can be retrieved from non-invasive magnetoencephalographic (MEG) recordings by deep networks trained with a CLIP-style objective against wav2vec 2.0 audio embeddings. Yet their weights do not map onto electrophysiological quantities, and it remains unclear which speech properties drive retrieval.
**Trending because:** 23 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 10. HarnessOpt-Bench: Evaluating LLMs at Harness Optimization
**Authors:** Varun Ursekar, Apaar Shanker, Yash Maurya, Shehab Yasser, Vijay S. Kalmath, Veronica Chatrath, Yuan Xue
**arXiv:** [arxiv.org/abs/2608.06301](https://arxiv.org/abs/2608.06301)
**Summary:** As LLMs are increasingly deployed within agentic systems, their capabilities depend not only on the model weights but also on the harness: the prompts, tools, control flow, memory, and orchestration code surrounding them. This makes automated harness optimization -- the iterative and evaluation-guided improvement of a harness by an AI system -- both an important route to improving AI systems and a demanding capability for AI systems themselves.
**Trending because:** 20 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 11. On-Policy Delta Distillation for Multilingual Math Reasoning
**Authors:** Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
**arXiv:** [arxiv.org/abs/2608.05802](https://arxiv.org/abs/2608.05802)
**Summary:** On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored. We study OPD and its advanced variant, On-Policy Delta Distillation (OPD^2), for mathematical reasoning in English, Korean, and Japanese.
**Trending because:** 20 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 12. DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces
**Authors:** Boyan Li, Zhuowen Liang, Yupeng Xie, Xiaotian Lin, Tianqi Luo, Xinyu Liu, Yizhang Zhu, Zhangyang Peng, Yuan Li, Zhengxuan Zhang, Jiayi Zhang, Nan Tang, Guoliang Li, Yuyu Luo
**arXiv:** [arxiv.org/abs/2608.03451](https://arxiv.org/abs/2608.03451)
**Summary:** Data agents enable natural-language analytics over organizational workspaces, where relevant evidence may be scattered across databases, structured files, long documents, and multimedia. Existing benchmarks largely isolate structured querying, retrieval, or open-ended analysis, leaving heterogeneous evidence discovery, complete tabular outputs, and deterministic evaluation insufficiently unified.
**Trending because:** 19 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 13. Teaching Nemotron Greek: Mining a Corpus, Adapting Retrieval, and Grounding Generation for Modern Greek across Specialist Domains
**Authors:** Ayoub Kirouane, Christos Petrocheilos
**arXiv:** [arxiv.org/abs/2608.05138](https://arxiv.org/abs/2608.05138)
**Summary:** Modern Greek is absent from NVIDIA's Nemotron retrieval models and from major multilingual retrieval benchmarks, despite being important for retrieval-augmented generation (RAG) in legal, energy, financial, and medical applications. We present an end-to-end adaptation of the Nemotron retrieval stack for Modern Greek, including corpus mining, synthetic supervision, retrieval model training, reranker adaptation, reader fine-tuning, and a new benchmark called HERA.
**Trending because:** 16 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 14. DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation
**Authors:** Junfeng Li, Junjie He, Zhide Zhong, Yangyang Zheng, Pingyue Sheng, Jiayu Dong, Ruixin Li, Haodong Yan, Jiaguan Zhu, Tianran Zhang, Runze Yu, Wen Chen, Liuqing Yang, Yuxiang Gao, Haoang Li
**arXiv:** [arxiv.org/abs/2608.06374](https://arxiv.org/abs/2608.06374)
**Summary:** Vision-Language-Action (VLA) models have become a powerful paradigm for robot manipulation, but training a single generalist policy for heterogeneous robot embodiments remains an open problem. Existing methods have two main limitations.
**Trending because:** 15 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 15. World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation
**Authors:** Yuhao Pan, Haosong Peng, Zhengshen Zhang, Zhengyang Yan, Yalun Dai, Fushuo Huo, Chujie Wang, Tianyu Qi, Xiucheng Wang, Nan Cheng, Wenchao Xu
**arXiv:** [arxiv.org/abs/2608.05369](https://arxiv.org/abs/2608.05369)
**Summary:** Vision-language-action (VLA) models often treat main-view and wrist-view observations as parallel visual inputs, overlooking their distinct roles in robot manipulation. Fine-grained manipulation, however, benefits from anticipating how wrist-local interactions may evolve under the global task context.
**Trending because:** 14 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 16. EffectLearner: World-Aware Object-Effect Reasoning for Real-World Video Object Removal
**Authors:** Feier Wu, Wanke Xia, Xu He, Zilang Zhou, Si Chen, Dongxia Liu, Liyang Chen, Qimeng Wu, Zhengbo Zhang, Wenming Yang, Zhiyong Wu
**arXiv:** [arxiv.org/abs/2608.05565](https://arxiv.org/abs/2608.05565)
**Summary:** Video object removal must eliminate not only the target object but also its induced effects while maintaining high-fidelity and spatiotemporally coherent restoration. Existing methods mainly learn object-effect correspondences implicitly from predefined effect categories and fixed data distributions, limiting their generalization to complex real-world scenes involving compositional effects, spatially detached or weakly correlated effects, long-tail physical phenomena, and dynamically evolving interactions.
**Trending because:** 12 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 17. CalibForge: Adversarial Solver Calibration for Scaling Learnable Terminal Tasks
**Authors:** Fanzhe Meng, Guoxin Chen, Jiale Zhao, Shuang Sun, Zhiyu Lin, Wayne Xin Zhao, Ruihua Song, Ji-Rong Wen, Kai Jia
**arXiv:** [arxiv.org/abs/2608.06352](https://arxiv.org/abs/2608.06352)
**Summary:** Training terminal agents requires executable and verifiable tasks that are not merely solvable, but appropriately challenging for learning. Executable validation establishes feasibility, yet does not reveal how a task behaves relative to a given solver setting.
**Trending because:** 11 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 18. SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding
**Authors:** Yue Zhang, Yingzhao Jian, Yunqiu Xu, Xiaoxiao Sun, Hehe Fan
**arXiv:** [arxiv.org/abs/2608.05137](https://arxiv.org/abs/2608.05137)
**Summary:** Understanding 3D scenes is fundamental to embodied intelligence, requiring joint reasoning over heterogeneous information from multiple modalities, including visual and geometric cues. However, the relevance of these modalities often varies across queries.
**Trending because:** 11 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 19. Lossless Tensor Compression as Program Synthesis
**Authors:** Jieke Shi, Junda He, Wenjia Jiang, Weifeng Sun, Shidong Pan, Zhensu Sun, Chengran Yang, Peixin Zhang, Yifan Jia, Zhou Yang, Thong Hoang, Xiwei Xu, Zhenchang Xing, David Lo
**arXiv:** [arxiv.org/abs/2608.02162](https://arxiv.org/abs/2608.02162)
**Summary:** Model checkpoints are growing in both number and size, which makes archival, transfer, and deployment increasingly costly. General-purpose compressors can reduce storage requirements but ignore tensor structure, whereas existing tensor-specific compressors rely on fixed and format-specific pipelines.
**Trending because:** 10 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 20. PaDoc: Layout-Grounded Parallel Decoding for Document Parsing
**Authors:** Hao Yu, Jiabo Zhan, Kang Liu, Linnan Zhao, Dongxu Yue, Rui Chen, Jinglin Wang, Chong Sun, Chen Li, Jing Lyu, Chun Yuan
**arXiv:** [arxiv.org/abs/2608.06146](https://arxiv.org/abs/2608.06146)
**Summary:** End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content, whereas crop-based two-stage parsers expose region-level parallelism at the cost of repeated visual prefills and fragmented page context.
**Trending because:** 10 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

