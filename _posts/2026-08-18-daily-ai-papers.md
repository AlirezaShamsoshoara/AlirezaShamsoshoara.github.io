---
title: "Daily AI Papers — August 18, 2026"
date: 2026-08-18
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-18/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - evaluation-benchmarks
---

### 1. HarnessEval-W: Agentifying the Evaluation of Visual Worlds
**Authors:** Weiliang Chen, Haowen Sun, Jun Gao, Jiawei Chi, Hanyang Wang, Qiyu Dai, Yihao Li, Hao Li, Jingnan Gao, Yi-Hsin Hung, Xingzhuo Guo, Shangchen Miao, Zhiyuan Shi, Xiang Li, Fengrui Tian, Weihua Du, Ziqi Huang, Shenyuan Gao, Siqiao Huang, Mingyu Liu, Yifei Li, Shizun Wang, Xi Wang, Tianqi Zhang, Xue Luo, Xiyin Ren, Jinshan Ren, Xiaoyang Shen, Xiaobo Hu, Zhiyang Dou, Mingyu Ding, Yichao Yan, Xinchao Wang, Yizhou Wang, Shilong Liu, Wenzhao Zheng, Yueqi Duan, Yuan Gong, Ziwei Liu, Ming-Yu Liu, Jialong Wu, Jiangran Lyu, Fangfu Liu
**arXiv:** [arxiv.org/abs/2608.16859](https://arxiv.org/abs/2608.16859)
**Summary:** A benchmark should deliver more than a scalar score: what makes an evaluation trustworthy is the reasoning that justifies the score. This is especially critical for world models, where judging a rollout requires understanding whether physics, causality, and world state evolve correctly.
**Trending because:** 106 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 2. VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?
**Authors:** Yansong Ning, Jingwen Ye, Zhongkai Wu, Yang Sun, Yiqin Zhu, Xingyi Li, Weidong Zhang, Hao Liu
**arXiv:** [arxiv.org/abs/2608.15265](https://arxiv.org/abs/2608.15265)
**Summary:** Constructing an interactive 3D open world from a user query is important. However, existing methods are primarily evaluated on idealized, simple queries, making it difficult to systematically analyze and compare how multimodal agents understand user intent, use 3D tools, and reason over textual and visual 3D world information.
**Trending because:** 50 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 3. Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search
**Authors:** Zhongwei Yu, Yan Song, Xue Yan, Anjie Liu, Xingyu Lu, Yihang Chen, Huichi Zhou, Siyuan Guo, Luoyang Sun, Sihan Chen, Xiangning Yu, Jun Wang
**arXiv:** [arxiv.org/abs/2608.15669](https://arxiv.org/abs/2608.15669)
**Summary:** Scientific discovery often involves optimising expensive-to-evaluate objectives over vast, structured, and open-ended hypothesis spaces, such as molecules, protein sequences, and computer programs. Generative models such as large language models (LLMs) provide expressive priors over such spaces, but their likelihoods and self-assessments are unreliable proxies for the objectives and calibrated epistemic uncertainty, especially for novel candidates outside the observed data distribution.
**Trending because:** 47 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 4. Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization
**Authors:** Yixuan Wang, Yifei Chen, Haichao Zhang, Haozheng Luo, Xander Wu, Jie Ni, Yun Fu, Nuno Vasconcelos, Yijiang Li
**arXiv:** [arxiv.org/abs/2608.16072](https://arxiv.org/abs/2608.16072)
**Summary:** Reinforcement learning (RL) with group-relative advantages has become the de facto standard for post-training language model reasoners. However, when optimizing multiple reward objectives, existing methods typically scalarize the reward vector with a fixed weighted sum before group-wise standardization.
**Trending because:** 42 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 5. MOSS-VL Technical Report
**Authors:** Pengyu Wang, Chenkun Tan, Shaojun Zhou, Qirui Zhou, Yanxin Chen, Xingyang He, Huazheng Zeng, Jijun Cheng, Chenghao Wang, Xiaomeng Qian, Pengfei Wang, Zhan Huang, Shanqing Gao, Wei Huang, Longjun Cao, Wu Ran, Jie Liu, Changtai Zhu, Hongkai Wang, Yixian Tian, Chenghao Liu, Zhen Ye, Xinghao Wang, Botian Jiang, Guoguo Feng, Zhaoye Fei, Ruixiao Li, Mingshu Chen, Yang Gao, Qinyuan Cheng, Shimin Li, Xipeng Qiu
**arXiv:** [arxiv.org/abs/2608.15045](https://arxiv.org/abs/2608.15045)
**Summary:** We present MOSS-VL, an open vision-language model family that treats real-time interaction -- perceiving while it speaks -- as a first-class capability. It is co-designed across the stack: the language decoder attends to vision only through gated cross-attention, so the model can naturally see incoming frames while generating; a synthesized interaction corpus supervises when to speak, when to stay silent, and when to revise; and a staged curriculum concentrates all real-time-specific training in one light final stage over a strong offline foundation.
**Trending because:** 37 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 6. ClawGym II: Exploring Black-Box RL on Agent Harness
**Authors:** Huatong Song, Fei Bai, Ming Yang, Renyuan Li, Jia Deng, Jujie He, Zhange Zhang, Daixuan Cheng, Yan Xing, Qi Yun, Xuxing Chen, Danyang Li, Feng Chang, Chuan Hao, Ran Tao, Jian Yang, Bryan Dai, Wayne Xin Zhao, Mingjie Tang, Ji-Rong Wen
**arXiv:** [arxiv.org/abs/2608.16798](https://arxiv.org/abs/2608.16798)
**Summary:** Agent harnesses have substantially improved performance on long-horizon tasks by coordinating agent interactions with the environment. However, reinforcement learning through complex harnesses remains largely unexplored, as scaling such training to long-horizon agent tasks introduces fundamental challenges.
**Trending because:** 33 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 7. UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations
**Authors:** Zihan Ding, Longxu Dou, Qi Gao, Xiangwu Guo, Shengchao Hu, Zilong Huang, Zihang Jiang, Lei Ke, Mengcheng Lan, Weixian Lei, Hanxuan Li, Honglin Li, Xiyun Li, Zaitang Li, Leowei Liang, Xin Luo, Haozhe Ma, Jiayi Mao, Zhoujie Pan, Can Qin, Tianyuan Qu, Weiqi Wang, Wenkai Wang, Yonglin Wang, Yuxin Wang, Chenxu Wu, Yingchen Yu, Chenyu Zhang, Yuhao Zheng
**arXiv:** [arxiv.org/abs/2608.15930](https://arxiv.org/abs/2608.15930)
**Summary:** Foundation GUI agents can automate complex digital tasks, but deployment is hindered by scarce and biased training data, ambiguous prompts, and unreliable execution. Routine workflows rely on user-specific tools and tacit conventions, so unstated instructions can produce arbitrary variations across runs.
**Trending because:** 32 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 8. An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models
**Authors:** Dengyang Jiang, Ruoyi Du, Zhennan Chen, Dongyang Liu, Zanyi Wang, Mingzhe Zheng, Xiangpeng Yang, Huanqia Cai, Aiming Hao, Yuming Jiang, Peng Gao, Harry Yang, Steven Hoi
**arXiv:** [arxiv.org/abs/2608.16887](https://arxiv.org/abs/2608.16887)
**Summary:** This paper investigates an increasingly important topic in generative modeling: pixel-space diffusion models. Although numerous studies have explored this topic, most focus on small-scale or class-conditional settings.
**Trending because:** 23 HuggingFace upvotes + riding strong interest in generative visual modeling

---

### 9. Agentic Transaction: Towards ACID-Compliant Agent Systems
**Authors:** Zhaoyan Sun, Xiaoxiao Wang, Guoliang Li
**arXiv:** [arxiv.org/abs/2608.13900](https://arxiv.org/abs/2608.13900)
**Summary:** Large language model (LLM) agents are evolving from conversational assistants into autonomous systems that execute long-horizon tasks through reasoning, tool use, code generation, and workspace manipulation. As agents increasingly operate over persistent environments and multi-step workflows, they face challenges analogous to those addressed by transactional database systems: reliable execution, consistent outcomes, safe concurrency, and durable state management.
**Trending because:** 21 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 10. How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks
**Authors:** Yanlin Fei, Nazhou Liu, Xinmiao Yu, Shaolong Chen, Lei Li, Rahul Thapa, Madalina Ciobanu, Qingqing Mao, Ritankar Das
**arXiv:** [arxiv.org/abs/2608.14905](https://arxiv.org/abs/2608.14905)
**Summary:** AI has long assisted scientific research, but the rapid advance of LLMs and agentic scaffolds is reshaping the landscape; a single system can now carry whole-stage research from an initial hypothesis all the way to final published paper, which is a paradigm now referred to as AutoResearch. Existing evaluations reveal little about how these agents operate or where they break down.
**Trending because:** 20 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 11. Advancing Open and Reproducible Relational Learning: RelArena-α, TabPFN-Rel and RPI
**Authors:** Adrian Hayler, Klemens Flöge, Alan Arazi, Rishabh Ranjan, Jure Leskovec, Felix Birkel, Brendan Roof, Anurag Garg, Kristina Collins, Lydia Sidhoum, Jonas Kübler, Siyuan Guo, Oscar Key, Jan Hendrik Metzen, Rylee Grace, David Salinas, Arthur Cahu, Simon Bing, Benjamin Jäger, Tuana Çelik, Mihir Manium, Vitor Monteiro, Jake Robertson, Jerry Chen, Eliott Kalfon, Tomás Pereda, Lilly Wehrhahn, Dominik Safaric, Tobias Schroeder, Georg Grab, Diana Kriuchkova, Clara Cornu, Philipp Singer, Nick Erickson, Vahid Balazadeh, Marie Salmon, Simone Alessi, Kürşat Kaya, Philipp Jund, Léo Grinsztajn, Yann LeCun, Bernhard Schölkopf, Madelon Hulsebos, Lennart Purucker, Sauraj Gambhir, Frank Hutter, Noah Hollmann
**arXiv:** [arxiv.org/abs/2608.16319](https://arxiv.org/abs/2608.16319)
**Summary:** This first release of Prior Labs in relational learning shows our continued commitment to open science. We open-source three pieces of software that we expect to accelerate research in the field towards meaningful real-world impact.
**Trending because:** 19 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 12. GenRouter: Unified Workflow Routing for Agentic Image Generation
**Authors:** Harold Haodong Chen, Zhiyu Hou, Wen-Jie Shu, Weilin Ruan, Yingjie Xu, Litao Guo, Ying-Cong Chen
**arXiv:** [arxiv.org/abs/2608.16721](https://arxiv.org/abs/2608.16721)
**Summary:** The rapid evolution of text-to-image (T2I) generation models has effectively solved the foundational challenge of raw pixel synthesis, shifting the community's focus toward fulfilling increasingly intricate user requests. While recent agentic image generation workflows enhance static inference with advanced capabilities like external knowledge retrieval and iterative reasoning, they mostly operate in isolated silos with fixed ``one-size-fits-all" topologies.
**Trending because:** 19 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 13. Understanding Cognition-Induced Risks in Agentic AI Systems
**Authors:** Guanchu Wang, Qinuo Li, Mengnan Du, Xia Hu, Bowen Zhou
**arXiv:** [arxiv.org/abs/2608.15304](https://arxiv.org/abs/2608.15304)
**Summary:** Frontier agentic systems powered by large language models (LLMs) exhibit human-like patterns of cognition. As these systems become deeply integrated across different domains, their cognitive engagement raises critical concerns for human society that remain insufficiently studied.
**Trending because:** 15 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 14. MegaParts: Scaling Part-Aware 3D Object Generation to 300 Parts via Token-Efficient Autoregressive Modeling
**Authors:** Manwen Liao, Xinyu Lian, Jian Mao, Kaixu Chen, Li Luo, Jinghao Yan, Wanshui Gan, Qiao Yu, Weitian Zhang, Chunhua Shen, Guang Chen, Bo Dai, Xudong Xu, Zhaoyang Lyu
**arXiv:** [arxiv.org/abs/2608.14783](https://arxiv.org/abs/2608.14783)
**Summary:** Part-aware 3D object generation is essential for graphics applications such as controllable modeling, editing, and articulation, where objects are represented as coherent assemblies of semantic parts. However, existing part-aware generation methods, do not scale well to highly complex objects.
**Trending because:** 15 HuggingFace upvotes + riding strong interest in generative visual modeling

---

### 15. GRNEdit: Efficient General Video Editing from a New Binary-Evidence Perspective in Generative Refinement Networks
**Authors:** Feng Xie, Jiagao Hu, Fuhao Li, Zepeng Wang, Yuxuan Chen, Dahua Gao, Fei Wang, Daiguo Zhou
**arXiv:** [arxiv.org/abs/2608.16328](https://arxiv.org/abs/2608.16328)
**Summary:** Instruction-based general video editing seeks to unify diverse editing operations within a single, intuitive interface. Existing approaches often rely on resource-intensive conditioning, using either heavyweight branches or costly source concatenation.
**Trending because:** 12 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 16. Ventor-QTest: Threat-Model-Driven Verification of Vendor-Hosted LLM APIs
**Authors:** Xiangfan Wu, Zonghao Ying, Huiyu Wu, Xing Zheng, Huangsheng Cheng, Xiaorong Shi, Jing Guo
**arXiv:** [arxiv.org/abs/2608.16391](https://arxiv.org/abs/2608.16391)
**Summary:** As large language models become increasingly widespread, third-party providers that deploy open-weight models have become an important part of the ecosystem. Auditing the quality of their inference APIs is therefore an open problem.
**Trending because:** 12 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 17. R^3-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets
**Authors:** Peisong Wang, Zhiwei Ma, Bowen Liu, Feixue Liu, Aochuan Chen, Chenyi Zi, Hongchuan Zeng, Yuhan Li, Jia Li
**arXiv:** [arxiv.org/abs/2608.16033](https://arxiv.org/abs/2608.16033)
**Summary:** In cognitive science, resource rationality asks how an agent should allocate limited computation to maximize expected value. Most reasoning and agent benchmarks use independent per-task budgets; existing shared-budget studies do not calibrate suite performance against the same model's demonstrated single-problem competence.
**Trending because:** 11 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 18. TRACE-Bench: Decomposing and Diagnosing Multi-Reference Image Generation
**Authors:** Haoran Wang, Chaofan Ma, Ran Yi, Lizhuang Ma
**arXiv:** [arxiv.org/abs/2608.16765](https://arxiv.org/abs/2608.16765)
**Summary:** Despite recent advances in unified multimodal models for multi-reference image generation, existing benchmarks remain organized around predefined task types (e.g., "subject composition"), which are ill-suited to this combinatorial setting and lead to fragmented coverage, uncontrolled complexity, and little diagnostic value. Recognizing that diverse multi-reference tasks share a common set of atomic operations, we adopt a capability-oriented perspective and formalize four operators: Anchor (f), Disentangle (g), Apply (oplus), and Compose (C).
**Trending because:** 9 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 19. VideoGAIA: A Benchmark for General AI Assistants on Agentic Video Understanding
**Authors:** Fan Zhang, Guangming Yao, Jinyang Wu, Hao Wu, Zheng Lian, Xinyu Geng, Jingdong Chen, Yi Yuan, Pheng-Ann Heng
**arXiv:** [arxiv.org/abs/2608.14718](https://arxiv.org/abs/2608.14718)
**Summary:** Video understanding is a fundamental task for evaluating the capabilities of multimodal large language models (MLLMs). However, existing leading models have already achieved approximately 90% accuracy on the Video-MME leaderboard, suggesting that conventional single-turn video understanding tasks are becoming increasingly saturated and insufficient for assessing the intelligence of advanced MLLMs.
**Trending because:** 9 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 20. Improving the matrix multiplication exponent with modern optimization and AlphaEvolve
**Authors:** Emilien Dupont, Marvin Eisenberger, Borislav Kozlovskii, Abbas Mehrabian, Francisco J. R. Ruiz, Abigail See, Renfei Zhou, Josh Alman, Virginia Vassilevska Williams, Matej Balog
**arXiv:** [arxiv.org/abs/2608.16884](https://arxiv.org/abs/2608.16884)
**Summary:** The current best bounds on the matrix multiplication exponent ω are obtained through a refinement of the laser method called combination loss analysis (Duan et al., 2022; Williams et al., 2024; Alman et al., 2025). In this note, we address the optimization problem at the core of this approach and propose several improvements.
**Trending because:** 8 HuggingFace upvotes + resonating with current LLM research interest

---
