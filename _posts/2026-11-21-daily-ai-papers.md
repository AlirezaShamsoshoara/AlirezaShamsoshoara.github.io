---
title: "Daily AI Papers — November 21, 2026"
date: 2026-11-21
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-21/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - code-models
  - embodied-ai
  - generative-models
---

### 1. InCoder-32B: Code Foundation Model for Industrial Scenarios
**Authors:** Jian Yang, Wei Zhang, Jiajun Wu, Junhang Cheng, Shawn Guo, Haowen Wang, Weicheng Gu, Yaxin Du, Joseph Li, Fanglin Xu, Yizhi Li, Lin Jing, Yuanbo Wang, Yuhan Gao, Ruihao Gong, Chuan Hao, Ran Tao, Aishan Liu, Tuney Zheng, Ganqu Cui, Zhoujun Li, Mingjie Tang, Chenghua Lin, Wayne Xin Zhao, Xianglong Liu, Ming Zhou, Bryan Dai, Weifeng Lv
**arXiv:** [arxiv.org/abs/2603.16790](https://arxiv.org/abs/2603.16790)
**Summary:** InCoder-32B is a 32-billion-parameter code model trained for industrial domains including chip design, GPU kernels, embedded systems, compiler optimization, and 3D modeling. The authors combine general and industrial code training, longer-context reasoning data, and execution-grounded post-training, reporting competitive results on 14 general-code and nine industrial benchmarks.

---

### 2. Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold
**Authors:** Xingang Pan, Ayush Tewari, Thomas Leimkühler, Lingjie Liu, Abhimitra Meka, Christian Theobalt
**arXiv:** [arxiv.org/abs/2305.10973](https://arxiv.org/abs/2305.10973)
**Summary:** DragGAN lets users manipulate generated images by dragging selected points, combining feature-based motion supervision with tracking in the generator's feature space. The authors report improved image manipulation and point tracking over prior approaches, and demonstrate editing real images through GAN inversion.

---

### 3. Sharp Monocular View Synthesis in Less Than a Second
**Authors:** Lars Mescheder, Wei Dong, Shiwei Li, Xuyang Bai, Marcel Santos, Peiyun Hu, Bruno Lecouat, Mingmin Zhen, Amaël Delaunoy, Tian Fang, Yanghai Tsin, Stephan R. Richter, Vladlen Koltun
**arXiv:** [arxiv.org/abs/2512.10685](https://arxiv.org/abs/2512.10685)
**Summary:** SHARP predicts a metric 3D Gaussian scene representation from a single photograph in less than a second on a standard GPU, enabling real-time rendering of nearby views. The authors report robust zero-shot generalization and substantial perceptual-quality improvements over the compared prior model, with code and weights released.

---

### 4. RL Post-Training in Diffusion Transformers Is Activation Steering
**Authors:** Tuna Han Salih Meral, Kaan Oktay, Alec Helbling, Atakan Kara, Duen Horng Chau, Pinar Yanardag
**arXiv:** [arxiv.org/abs/2611.26627](https://arxiv.org/abs/2611.26627)
**Summary:** The authors fit fixed activation-steering vectors to frozen diffusion transformers to test how much of RL post-training's gains can be reproduced without input-dependent weight transformations. These vectors recover 90.0-96.3% of the reward gains of six evaluated image models while using 65 times fewer parameters than the compared SD3.5-M LoRA, and online RL of the vectors also improves selected rewards.

---

### 5. CompoundingKernel: Self-Improving from Zero to First
**Authors:** Qian Qu, Hongyang Wang, Wenbo Chen, Yichuan Li, Jingguo Liu, Xian Li, Xuan Wang, Ruochen Wen, Leo Fan, Yiming Yan, Zheshen Wang, Benoit Dumoulin
**arXiv:** [arxiv.org/abs/2611.19230](https://arxiv.org/abs/2611.19230)
**Summary:** CompoundingKernel uses an LLM controller, parallel search agents, an external archive of correct kernels, and independent correctness checks to optimize GPU kernels from PyTorch definitions. The authors report site-verified solutions for all 235 problems and 4.40-times reference-baseline speed on 209 public-board problems, emphasizing reliable measurement throughput as a scaling bottleneck.

---

### 6. Online Mistake Detection in Instruction-Conditioned Procedural Video
**Authors:** Amit Feldman, Ilan Shimshoni, Rotem Dror
**arXiv:** [arxiv.org/abs/2611.25567](https://arxiv.org/abs/2611.25567)
**Summary:** This work detects mistakes online in egocentric procedural videos by conditioning predictions on instructions, observed footage, and previous predictions. A joint model achieves 84.1% binary mistake-detection F1 at the evaluated overlap threshold versus 80.7% for a modular pipeline, with a particularly large improvement on slips.

---

### 7. VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models
**Authors:** Suho Yoo, Youngjoon Jang, Hyebin Cho, Taeyeop Lee, Jaewook Jeong, Joon Son Chung
**arXiv:** [arxiv.org/abs/2611.22666](https://arxiv.org/abs/2611.22666)
**Summary:** VSpark accelerates autoregressive vision-language-action models using calibrated-noise rollouts, draft-feature alignment, and reuse of target predictions from rejected draft continuations. Across four VLAs and four manipulation benchmarks, the authors report 1.28-2.10-times speedup while preserving lossless target decoding.

---

### 8. Twice-Told Critiques: Claim-Level Homogenization of Peer Review in the LLM Era
**Authors:** Ilya Gusev
**arXiv:** [arxiv.org/abs/2611.26286](https://arxiv.org/abs/2611.26286)
**Summary:** This study measures overlap between claims in conference and journal peer reviews and finds increasing redundancy across the analyzed review collections. Reviews flagged by the MELD LLM-text detector overlap more within a paper than unflagged reviews, providing observational evidence of reduced critique diversity rather than establishing a causal effect of LLM use.

---

### 9. Embeddings vs. Grep: Rethinking the Dense Advantage in Code Search
**Authors:** Siqiao Xue, Ziyin Zhang, Zihan Liao, Jin Qin, Yixiang Mu, Hang Yu
**arXiv:** [arxiv.org/abs/2611.20455](https://arxiv.org/abs/2611.20455)
**Summary:** Repo-Premium evaluates repository-level code retrieval across six languages and a preregistered pool of 91 repositories, exposing benchmark choices and missing identifiers that can exaggerate dense retrieval's advantage. LLM-generated query identifiers let BM25 match dense retrieval in every evaluated Python pool, motivating fair lexical baselines, retrieval fusion, and identifier-aware queries.

---

### 10. Accord: Universal Online Metric Localization and Dense Mapping from one Camera and an IMU
**Authors:** Jaafar Mahmoud, Arthur Movsesyan, Cuong Huynh, Mikhail Iumanov, Sergey Zagoruyko, Sergey Kolyubin
**arXiv:** [arxiv.org/abs/2611.25279](https://arxiv.org/abs/2611.25279)
**Summary:** Accord combines visual-inertial odometry, pose-conditioned depth prediction, metric anchors, multi-view depth agreement, and factor-graph fusion to build online dense maps from a camera and IMU. A single untuned mapping configuration achieves the best or second-best mean F-score at five centimeters across all evaluated platforms, and the authors release the system and phone-rig dataset.

---

### 11. Language Models Can Rewrite Their Own Weights
**Authors:** Jiajun Fan, Neil He, Changyi Yang, Andy Mao, Xi Zhu, Chaoran Cheng, Kaiqu Liang, Shuaike Shen, Zetian Li, Ruihan Guo, Ge Liu
**arXiv:** [arxiv.org/abs/2611.21885](https://arxiv.org/abs/2611.21885)
**Summary:** This work allows an open 27B model to inspect its weights and graded answers, diagnose failures, and propose weight edits using forward passes rather than gradient training. The authors report a 6.6-percentage-point improvement on unseen problems, monotonically improving accuracy across eight sessions, and partial repair of a damaged model copy.

---

### 12. System 1 agents: a method for local, reliable and fast agentic AI
**Authors:** Eleftherios Tzanis, Michail E. Klontzas
**arXiv:** [arxiv.org/abs/2611.21053](https://arxiv.org/abs/2611.21053)
**Summary:** System 1 agents compile tool schemas and user requests into multiple-choice decisions, selecting tools and arguments locally without generating free-form text. On 1,952 requests to 157 biomedical tools, the best evaluated agent reaches 97.0% correct tool selection or refusal and introduces no invented content in its calls.

---

### 13. NarrowSpec: Draft Hidden Width Need Not Match the Target in Speculative Decoding
**Authors:** Alagappan Valliappan, Ankit More, Dheevatsa Mudigere, Jatin Mitra
**arXiv:** [arxiv.org/abs/2611.23835](https://arxiv.org/abs/2611.23835)
**Summary:** NarrowSpec reduces hidden-state-conditioned speculative draft models to half or one-quarter of the target model's width while largely preserving token acceptance. Tests of DFlash and EAGLE-3 in SGLang report end-to-end decoding improvements on B200 and GB10 hardware, including 1.13-1.44-times speedup on GB10 at batch size one.

---

### 14. Teaching Vision-Language-Action Models to Stop Safely
**Authors:** Zheyuan Liu, Chuhan Wang, Jinduo Guo, Yue Huang, Xiangchi Yuan, Ningshan Ma, Meng Jiang
**arXiv:** [arxiv.org/abs/2611.26239](https://arxiv.org/abs/2611.26239)
**Summary:** State-Aware Fallback Imitation teaches vision-language-action policies stationary arm commands and appropriate gripper targets for stopping prohibited tasks at intermediate execution states. On the evaluated LIBERO tasks, the authors report 1.3% aggregate prohibited completion after takeover, no recorded physical incidents or action saturation, and preserved performance on retained tasks.

---

### 15. TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs
**Authors:** Yang Wan, Linchao Zhu
**arXiv:** [arxiv.org/abs/2611.26248](https://arxiv.org/abs/2611.26248)
**Summary:** TwinLab-Bench evaluates AI scientists on self-designed experiments in 52 tasks grounded in records from real physical-science, life-science, and engineering laboratories. Task-specific environment agents support more than 100 experimental action types, while hidden laboratory answers score reports and reveal substantial remaining difficulty for the evaluated frontier models.

---

### 16. A CPU Inside an LLM: Zero-Gradient Compilation of Exact Circuits into Pretrained Weights
**Authors:** Tanmay Sah
**arXiv:** [arxiv.org/abs/2611.26450](https://arxiv.org/abs/2611.26450)
**Summary:** This work analytically compiles deterministic arithmetic and Boolean circuits into pretrained language-model weights without gradient updates, training examples, or runtime hooks. The authors report 99.17% and 100.00% six-digit arithmetic ALU-prefix accuracy on evaluated Granite and Qwen configurations, alongside tests intended to check preservation of natural-language behavior.

---

### 17. Do Probing and Steering Favor the Same Directions Within and Across Language Models?
**Authors:** Afshin Sadeghi, Daniel Becker
**arXiv:** [arxiv.org/abs/2611.19499](https://arxiv.org/abs/2611.19499)
**Summary:** Across three instruction-tuned model families, this study finds that directions best suited to probing truthfulness or sentiment are generally not those best suited to activation steering. The separation appears in 59 of 60 layer-model-concept combinations, while transfer experiments and an abstention application show that probing and causal intervention also generalize differently.

---

### 18. Phantom Success, Silent Failure: Auditing the Success Checkers of Simulated Manipulation Benchmarks
**Authors:** Zirui Song, Jiadong Zhang, Zheng Lu, Xiaosong Ma, Xiaojun Chang, Xiuying Chen
**arXiv:** [arxiv.org/abs/2611.25179](https://arxiv.org/abs/2611.25179)
**Summary:** SimAudit analyzes manipulation-task instructions and success-checker code, recreates predicted disagreements in simulation, and verifies behavior with multi-view renderings. Across three benchmark suites, the authors identify 61 distinct checker defects in 49 tasks, including 40 accepted incomplete executions and 21 rejected valid executions.

---

### 19. One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning
**Authors:** Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang, Ivor Tsang, Mike Zheng Shou
**arXiv:** [arxiv.org/abs/2611.26617](https://arxiv.org/abs/2611.26617)
**Summary:** O2LaF initializes inverse and forward dynamics from the same pretrained video diffusion transformer, learning compact transferable latent actions from unlabeled visual transitions. The authors report leading few-shot action-probing results and stronger zero-shot transfer across navigation and robotic manipulation, and extend the framework to predictive representation priors such as V-JEPA2.

---

### 20. Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain
**Authors:** Shuang Wu, Jiachen Qian, Youtian Lin, Feihu Zhang, Philip Torr, Yao Yao, Xun Cao
**arXiv:** [arxiv.org/abs/2611.26511](https://arxiv.org/abs/2611.26511)
**Summary:** Direct3D-V3 removes the VAE bottleneck and trains a diffusion transformer directly on signed-distance voxel grids for native 3D generation. Neighboring-voxel regularization, rendered-normal supervision, and auxiliary camera prediction improve geometric reliability and image alignment, with the same representation supporting refinement for generative reconstruction.
