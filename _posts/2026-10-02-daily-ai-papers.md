---
title: "Daily AI Papers — October 02, 2026"
date: 2026-10-02
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-02/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - multimodal-ai
  - reinforcement-learning
---

### 1. OneStreamer: Unifying Perception, Memory, and Proactive Response in Streaming Video Interaction
**Authors:** Xiangyu Zeng, Yuandong Yang, Zhiqiu Zhang, Yuhan Zhu, Xinhao Li, Qingyi Si, Dingyu Yao, Changlian Ma, Haoran Chen, Xinyu Chen, Yansong Shi, Junhao Zhou, Yifei Li, Jun Zhang, Chuanyu Qin, Chenxu Yang, Xinlei Yu, Kun Ouyang, Yuchen Shao, Qianshan Wei, Changhai Zhou, Jun Gao, Jiaqi Wang, Limin Wang
**arXiv:** [arxiv.org/abs/2610.01762](https://arxiv.org/abs/2610.01762)
**Summary:** OneStreamer jointly learns query-independent evidence recording and task response for streaming video through proactive hierarchical caption memory and state-transition learning. Its 4B model leads the compared methods on all eight evaluated streaming-video benchmarks, while retained captions improve historical question answering without hurting real-time perception.

---

### 2. Adaptive Reward Routing: Dynamic Multi-Reward Optimization for Joint Audio-Video Diffusion via Forward-Process RL
**Authors:** Songlin Yang, Xiaotong Zhao, Jiacheng Zhang, Zhe Wang, Toyota Li, Eric Liu, Alan Zhao, Anyi Rao
**arXiv:** [arxiv.org/abs/2609.37200](https://arxiv.org/abs/2609.37200)
**Summary:** Adaptive Reward Routing dynamically chooses where multi-reward updates act in a joint audio-video diffusion model and adjusts how competing rewards are combined during forward-process reinforcement learning. Experiments show consistent gains in modality quality, semantic consistency, and audio-video synchronization over strong reinforcement-learning baselines.

---

### 3. Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States
**Authors:** Yu Luo, Jiamin Jiang, Yimin Zuo, Xidao Wen, Rongchen Gao, Yongqian Sun, Shenglin Zhang, Guiyang Liu, Cheng Zhang, Fang Situ, Qi Zhou, Dan Pei
**arXiv:** [arxiv.org/abs/2610.01415](https://arxiv.org/abs/2610.01415)
**Summary:** PoS maintains an explicit belief state that combines the agent's estimate of the world with unresolved requirements, then detects and recovers from belief trapping when progress stalls. Across four execution and diagnosis benchmarks and three LLM backbones, it achieves the best overall performance while remaining resilient as context grows.

---

### 4. Agent Priors-guided Policy Learning
**Authors:** Puming Jiang, Tianrun Hu, Haozhe Du, Yibo Li, Zhiwei Xue, Xinhu Li, Harold Soh
**arXiv:** [arxiv.org/abs/2609.35690](https://arxiv.org/abs/2609.35690)
**Summary:** APPL exposes each learned robot skill's structural prior to the composition layer, connecting where a policy generalizes with when a planning agent should use it. On MetaWorld and long-horizon ManiSkill tasks, this interface improves out-of-distribution skill generalization and enables previously unseen skill combinations.

---

### 5. Hierarchical Continuous Diffusion Language Models
**Authors:** Hui Ren, Zihan Li, Chang Liu, Huidong Liu, Alexander Schwing
**arXiv:** [arxiv.org/abs/2610.02193](https://arxiv.org/abs/2610.02193)
**Summary:** HC-DLM couples discrete token generation to a persistent continuous latent trajectory, using decoded tokens as a scaffold for each subsequent latent update. At matched model size it improves over discrete and continuous diffusion baselines on Sudoku, Countdown, and LM1B language modeling.

---

### 6. Sharpening Tax in Post-Training
**Authors:** Changdae Oh, Qi Zeng, Qi Qi, Andrey Zhmoginov, Deren Lei, Yun He, Hoang Phan, Hangoo Kang, Azalia Mirhoseini, Sharon Li
**arXiv:** [arxiv.org/abs/2610.01509](https://arxiv.org/abs/2610.01509)
**Summary:** The paper finds that post-training often concentrates an LLM's behavior into reliably solved or unsolved tasks, improving single-shot consistency while reducing solution coverage under repeated sampling. Its Sharpening Tax metric quantifies that loss across 42 model-benchmark cases, and posterior-tempered group sampling reduces the tax while improving single-shot accuracy.

---

### 7. A Missing Piece for Trustworthy AI Reviewers: From Benchmarking Rhetorical Robustness to SciCore Review
**Authors:** Chenguang Wang, Ming Li, Chengrui Fan, Jianpeng Chen, Han Chen, Tianyi Zhou, Dawei Zhou
**arXiv:** [arxiv.org/abs/2609.39027](https://arxiv.org/abs/2609.39027)
**Summary:** RobustReview tests whether AI reviewers remain stable across content-preserving rewrites without collapsing their ability to distinguish papers, revealing that rhetorical robustness and human alignment rank systems differently. SciCore combines full-manuscript judgment with a structured science-core review and achieves a leading stability-discrimination profile in the paper's primary comparison.

---

### 8. World Observer: Joint Actor-Observer Generation for Persistent World Modeling
**Authors:** Hyunwook Choi, Dahyun Chung, Hyunsung Kim, Siyoon Jin, Jinhyeok Choi, Junyoung Seo, Seungryong Kim
**arXiv:** [arxiv.org/abs/2610.02162](https://arxiv.org/abs/2610.02162)
**Summary:** World Observer jointly generates an actor view and freely placed observer views so a video world model can preserve the evolving state of objects outside the actor's field of view. The method substantially improves out-of-view dynamics while remaining competitive in visual fidelity, camera control, and 3D adherence.

---

### 9. ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization
**Authors:** Sungho Park, Wonjoong Kim, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Victor Rühle
**arXiv:** [arxiv.org/abs/2610.00906](https://arxiv.org/abs/2610.00906)
**Summary:** ActiveSaddler treats agent-harness curriculum selection as a non-stationary bandit that tracks recurring failure patterns and balances revisiting weaknesses with exploring new scenarios. On GAIA2 and Terminal-Bench 2.0, it improves test Pass@1 by 4.4 and 7.5 percentage points over the same optimizer with a fixed scenario order.

---

### 10. AutoGUIWorld: Image Generators as Visual World Models for GUI Agent
**Authors:** Cheng Yang, Yifan Wu, Yutao Huang, Zhaohua Zhang, Beiduo Chen, Muxi Chen, Chenchen Zhao, Hexuan Deng, Haolin Yang, Geyuan Zhu, Sa Zhu, Jianhuan Zhuo, Qiuyong Xiao, Jianhao Ruan, Yiran Peng, Jiayi Zhang, Tian Ye, Xinlei Yu, Tianwen Jiang, Jihong Zhang, Yuyu Luo
**arXiv:** [arxiv.org/abs/2610.01215](https://arxiv.org/abs/2610.01215)
**Summary:** AutoGUIWorld uses a planner and image generator to synthesize visually grounded GUI interaction trajectories without installing or running the target software. Fine-tuning on its 79,266 annotated steps raises OSWorld mean task score from 33.0% to 40.8% and ScienceBoard success from 14.0% to 32.2%.

---

### 11. ROWBench: Do Video Models Render What the Program Specifies?
**Authors:** Zheng-Hui Huang, Guixu Lin, Yu-Ju Tsai, Jian-Kai Zhu, Fengbo Lan, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang, Zhixiang Wang
**arXiv:** [arxiv.org/abs/2610.02205](https://arxiv.org/abs/2610.02205)
**Summary:** PROWBench evaluates whether generated videos faithfully render program-specified events using replayable world records, synchronized views, and metrics for control, memory, and interaction success. Its 170 constructed episodes and 600 proxy videos target fine-grained rule adherence that conventional visual-quality and controllability benchmarks largely miss.

---

### 12. E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models
**Authors:** Arseny Ivanov, Alexander Kolesov, Alexander Korotin, Ivan Oseledets, Mikhail Goncharov
**arXiv:** [arxiv.org/abs/2609.37533](https://arxiv.org/abs/2609.37533)
**Summary:** E-MoE models the reverse process of masked diffusion as a mixture of factorized distributions over a shared discrete routing latent, avoiding the posterior-collapse risk of continuous-latent alternatives. Without increasing active parameters over the factorized baseline, it improves few-step generation on synthetic multimodal tasks, binarized MNIST, and LM1B.

---

### 13. Retrieval-Augmented Skill Optimization via Cross-Harness Adaptation
**Authors:** Jaewon Chu, Ji Soo Lee, Jihwan Park, Dohwan Ko, Jeehye Na, Seunghun Lee, Taehoon Lee, Minseo Yoon, Minseok Joo, Yunyang Xiong, Hyunwoo J. Kim
**arXiv:** [arxiv.org/abs/2609.38024](https://arxiv.org/abs/2609.38024)
**Summary:** RASO retrieves knowledge from a large external skill corpus and adapts it across domain and harness mismatches during both skill initialization and iterative updating. Across four agent benchmarks and two models, it consistently outperforms skill-optimization baselines that do not use retrieval-augmented initialization and updates.

---

### 14. Make Sparse Rewards Count: Density-Aware Reward Aggregation for Multi-Reward RL
**Authors:** Tong Zheng, Skylar Zhai, Zhan Cheng, TianMing Sha, Youling Huang, Shuo Zhou, Shaotong Qi, Jingcheng Liang, Xuwei Ding, Pengcheng Xu
**arXiv:** [arxiv.org/abs/2610.00574](https://arxiv.org/abs/2610.00574)
**Summary:** DARA corrects residual imbalance in multi-reward reinforcement learning by weighting reward signals according to how often they provide active advantages in each rollout batch. It reaches high tool-format compliance in up to 26% fewer steps and near-saturated mathematical length compliance in up to 65% fewer steps than GDPO while retaining competitive final performance.

---

### 15. EgoTools: Towards Tool-Centric Reasoning in Real-World Egocentric Videos
**Authors:** Shulin Tian, Junsu Kim, Shuai Liu, Hao Li, Yujiao Shen, Sihan Li, Zhe Yang, Yeongon Kim, Feiyu Li, Jialin Wu, Yichi Zhang, Wenhui Wang, Runmao Yao, Yuhao Dong, Zhaoxi Chen, Fangzhou Hong, Antonino Furnari, Jingkang Yang, Hongyuan Zhu, Ziwei Liu
**arXiv:** [arxiv.org/abs/2609.39378](https://arxiv.org/abs/2609.39378)
**Summary:** EgoTools contributes 100 hours of egocentric tool-use recordings plus a 1,000-question benchmark spanning perception, geometry, procedure, and causal reasoning. Current models remain weak at visual grounding, while supervised training on EgoTools-Data improves Qwen3-VL-8B-Instruct from 50.0% to 60.9% on the full benchmark.

---

### 16. Decentralized Master-Mind: Joint Action Refinement through Iterative Intent Denoising in Multi-Agent Pathfinding
**Authors:** Valeriy Vyaltsev, Anton Andreychuk, Taisia Zlotnikova, Konstantin Yakovlev, Aleksandr Panov, Alexey Skrynnik
**arXiv:** [arxiv.org/abs/2609.32019](https://arxiv.org/abs/2609.32019)
**Summary:** DMM replaces independent one-shot action sampling in decentralized multi-agent pathfinding with iterative communication-based refinement of action intents. It solves 1,598 of 1,600 MovingAI tasks after MICPO fine-tuning and scales to more than one million simultaneously acting agents.

---

### 17. Scaling and Distilling Text Embeddings for Better Diffusibility
**Authors:** Zekai Zhang, Yunjie Tian, Yanjin He, Xiaoyan Zhang, Dongdi Zhao, Qing Qu, Di Fu
**arXiv:** [arxiv.org/abs/2610.01016](https://arxiv.org/abs/2610.01016)
**Summary:** The authors show that stronger text encoders improve continuous diffusion language models but overly separated embeddings can make valid words hard to reach during sampling. Distilling T5Gemma-2 with soft decoded probabilities creates a more connected latent space and yields better generative perplexity than GPT-2-M on OpenWebText.

---

### 18. GraphForge: Training Working Agents with Graph-Anchored Workspace Synthesis
**Authors:** Qisheng Su, Hanchen Wang, Guanru Zhu, Huicheng Jiang, Qiuyinzhe Zhang, Kou Shi, Zhen Fang, Ziao Zhang, Qingnan Ren, Zehui Chen, Tao Gui, Feng Zhao
**arXiv:** [arxiv.org/abs/2609.38923](https://arxiv.org/abs/2609.38923)
**Summary:** GraphForge builds agent-training workspaces from real files and an evidence graph that jointly grounds task requirements and verifiable rubrics. Fine-tuning on 2,169 trajectories improves GDPVal, Workspace-Bench-Lite, and SpreadsheetBench II, with evidence-anchored rejection fine-tuning adding further gains.

---

### 19. Beyond the Current Scene: Event-Referential Grasping with Active View Selection
**Authors:** Hyunjoon Lee, Haebeom Jung, Eunsung Cha, Daeun Lee, Yu-Chiang Frank Wang, Jaesung Choe, Jaesik Park
**arXiv:** [arxiv.org/abs/2609.39375](https://arxiv.org/abs/2609.39375)
**Summary:** BeyondSCe identifies grasp targets referred to by their role in past events and selects new camera views when those targets are occluded. Using pretrained models without task-specific training, it reaches 76% and 77% grasp success for initially visible and occluded targets and improves performance in heavily occluded scenes.

---

### 20. InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation
**Authors:** Zhuo Lin, Sirui Xu, Liuyu Bian, Yu-Xiong Wang, Liang-Yan Gui
**arXiv:** [arxiv.org/abs/2610.02196](https://arxiv.org/abs/2610.02196)
**Summary:** InterEvolve represents humanoid loco-manipulation tasks as staged reward programs that an LLM revises from execution feedback while a numerical optimizer tunes constants. The evolved programs unlock new behaviors from an existing controller in simulation, and the resulting skills run autonomously on a physical Unitree G1 using onboard perception.
