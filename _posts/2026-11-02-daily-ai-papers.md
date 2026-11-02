---
title: "Daily AI Papers — November 02, 2026"
date: 2026-11-02
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-02/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - embodied-ai
  - visual-generation
---

### 1. FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation
**Authors:** Yijing Lin, Zhendong Mao, Mengqi Huang, Yuxin Wang, Yongdong Zhang
**arXiv:** [arxiv.org/abs/2610.36545](https://arxiv.org/abs/2610.36545)
**Summary:** FrameForge adapts pretrained video models for unified conditional image generation by learning input-dependent virtual temporal relationships between a visual condition and its target. Its temporal experts and latent reasoning pathway improve subject-driven generation, canny-to-image generation, and image editing on DreamBench, COCO2017, and GEdit-Bench among the compared methods.

---

### 2. R^2Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop
**Authors:** Mingda Zhang, Yun Huang, Qiang Huang, Yanjin Li, Rui Qian, Qichao Zhao, Tiesunlong Shen, Na Zhao, Jian Wang, Xiaoying Tang
**arXiv:** [arxiv.org/abs/2610.22740](https://arxiv.org/abs/2610.22740)
**Summary:** R^2Orch trains agent orchestrators through recursive self-play, combining a task proposer rewarded for learnability with an outer loop that withdraws skills once their knowledge is internalized. The authors report improvements over baselines across twelve question-answering, math, code, and interactive datasets while moving toward deployment without external skills.

---

### 3. Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?
**Authors:** Qi Wang, Yun Qu, Lizhou Cai, Heming Zou, Haoang Chi, Yiqin Lv, Xiang Li, Haiyan Feng, Mengyu Ge, Yize Geng, Yuhang Jiang, Yixiu Mao, Xiangyang Ji
**arXiv:** [arxiv.org/abs/2610.39497](https://arxiv.org/abs/2610.39497)
**Summary:** This paper proposes conditional interaction, a predict-gate-execute-update loop in which a lightweight System-1 screens candidate operations before an expensive System-2 executes them. Its theoretical analysis relates potential compute savings and selection regret to useful-interaction density and predictor error, while explicitly accounting for limits from exploration and distribution shift.

---

### 4. REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control
**Authors:** Pengfei Zhou, Yixing Ma, Zhengfeiyang Zhang, Haoyuan Chen, Zhenglin Wan, Hexin Wang, Wangbo Zhao, Yang You
**arXiv:** [arxiv.org/abs/2610.42053](https://arxiv.org/abs/2610.42053)
**Summary:** REA coordinates deliberative foundation models, an embodied router, and fast reactive policies asynchronously so that an executing policy never waits on the reasoning model. It reports 95.9% success across 3,000 LIBERO-Pro episodes with 25% fewer control steps and 17% less control time, plus evaluations on RoboTwin, BEHAVIOR-1K, and a real humanoid.

---

### 5. Apriel Voice 27B Preview: An Open Model for Speech, Reasoning, and Tool Use
**Authors:** Aman Tiwari, Akshay Kalkunte, Akintunde Oladipo, Jash Shah, Tara Bogavelli, Hoang Nguyen, Nishanth Madhusudhan, Vishal Juneja, Sridhar Nemala, Srinivas Sunkara, Sathwik Tejaswi Madhusudhan, Shruthan Radhakrishna, Masoud Hashemi, Kelechi Ogueji, Khalil Slimi, Saloni Mittal, Pulkit Pattnaik, Shashank Maiya, Dhruv Jhamb, Esakkivel Esakkiraja, Katrina Stankiewicz, Gabrielle Gauthier Melançon, Fanny Riols, Amit Saha, Lakshmi Sirisha Chodisetty, Nitin Aggarwal, Anil Madamala, Sagar Davasam, Segan Subramanian, Vikas Yadav, Sai Rajeswar Mudumba
**arXiv:** [arxiv.org/abs/2610.40738](https://arxiv.org/abs/2610.40738)
**Summary:** Apriel Voice 27B Preview is an open speech-language model that directly handles spoken requests, reasoning, responses, and tool calls through a shared backbone while retaining text and image inputs. Its two-stage speech adaptation and online distillation yield reported scores of 98.90 on Big Bench Audio and 81.13 on Speech-BFCL, with 65.51% task success on tau-Voice and 1.91-second mean latency in thinking mode.

---

### 6. WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search
**Authors:** Yingtao Ren, Aolin Li, Cheng Cheng, Huiyun Hu, Huasheng Liang, Baoxing Xie, Jun Yuan, Haijun Wu, Yiwei Fu, Chenxing Wang
**arXiv:** [arxiv.org/abs/2610.16927](https://arxiv.org/abs/2610.16927)
**Summary:** WeFair aligns personalized short-video query rewriting through a curriculum of demonstrations, consumption-based preferences, and verification against actual user reformulations or preservation targets. The deployed 2B model improves intent preservation offline, and an online A/B test reports a 2.593% relative increase in effective video-view rate and a 2.350% relative decrease in query reformulation rate.

---

### 7. Latent Reasoning in Continuous Space for Unified Multimodal Models
**Authors:** Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin
**arXiv:** [arxiv.org/abs/2610.42149](https://arxiv.org/abs/2610.42149)
**Summary:** LARC replaces discrete token-based reasoning with continuous hidden-state reasoning in unified multimodal models, using curriculum supervised fine-tuning followed by information-gain reinforcement learning. Across text-to-image benchmarks it improves prompt following and compositional fidelity, including a seven-percentage-point GenEval gain over BAGEL and stronger parallel and sequential test-time scaling.

---

### 8. HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model
**Authors:** Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang, Xinguang Xiang, Xiangbo Shu
**arXiv:** [arxiv.org/abs/2610.40373](https://arxiv.org/abs/2610.40373)
**Summary:** HiFOR jointly predicts short-term dynamics, semantic milestones, and final goals, then organizes these predictions into structured latent world representations. Its action-guided retrieval selectively supplies relevant future information during action denoising, with evaluations on two simulation benchmarks and six real-world manipulation tasks.

---

### 9. Wizard: Manipulate Any World in Real Time via Agentic Control
**Authors:** Yuzhe Wu, Zijun Lin, Yeying Jin
**arXiv:** [arxiv.org/abs/2610.40339](https://arxiv.org/abs/2610.40339)
**Summary:** Wizard combines an explicit game-state agent with skeleton- and geometry-conditioned video generation to enable precise real-time character control and zero-shot transfer to new scenes, characters, and actions. Training uses a dataset spanning 750 scenes and 178 characters, while adaptive masking aligns structured control proxies with generated video rollouts.

---

### 10. OSWAM: An Effective World Action Model with One-Step Action Generation
**Authors:** Guowen Zhang, Liyi Chen, Xu Hu, Pengfei Wang, Jingfan Chen, Chenhang He, Lei Zhang
**arXiv:** [arxiv.org/abs/2610.35850](https://arxiv.org/abs/2610.35850)
**Summary:** OSWAM generates actions in one diffusion step by replacing unstructured noise initialization with imagination tokens and distilling privileged future information into the policy. Across autonomous-driving and embodied-control evaluations it matches or exceeds compared multi-step world-action models, with approximately threefold speedup and compiled inference latency as low as 40 milliseconds on an RTX 5090.

---

### 11. ReLift: Dense 3D Tracking as Lifted Trajectory Repair
**Authors:** Assaf Singer, Maroun Khriesh, Noam Rotstein, Yoni Kasten, Or Litany
**arXiv:** [arxiv.org/abs/2610.42136](https://arxiv.org/abs/2610.42136)
**Summary:** ReLift turns dense monocular 3D tracking into repair and completion of trajectories lifted from pretrained 2D trackers and geometry models. A geometry-only trajectory corrector transfers across these components without retraining and improves WorldTrack accuracy by 2.1 APD on all points and 3.0 on dynamic points over the strongest baselines.

---

### 12. Venus-DefakerOne2: A Vision-Forensics Foundation Model with Broader Coverage
**Authors:** Chenfan Qu, Yachao Liang, Mingqi Fang, Jiangwei Xie, Zhenming Wang, Baoyue Zhang, Changjiang Jiang, Zheng Chang, Fanli Jin, Xuekang Zhu, Kaiwen Feng, Junchi Li, Weihong Zhang, Haoyue Wang, Chenfeng Zhang, Yinan Xia, Fangming Cui, Dong Fan, Jingjing Liu, Tianyi Zhang, Luobin Chen, Ji-Zhe Zhou, Sheng Li, Wei Wang, Bin Li, Ran He, Xinpeng Zhang, Linna Zhou, Jian Liu, Weiqiang Wang
**arXiv:** [arxiv.org/abs/2610.37918](https://arxiv.org/abs/2610.37918)
**Summary:** Venus-DefakerOne2 is a vision-forensics foundation model covering digital manipulation and physical spoofing across images and videos. Alternating LoRA and full-parameter tuning with entropy-based test adaptation yields reported benchmark results including 96.7% for DeepFake faces, 93.3% for AI-generated images, and 96.0% for AI-generated videos.

---

### 13. CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent Systems
**Authors:** Jongha Kim, Seohyun Lee, Jonathan Minho Chung, Jinsung Yoon, Hyunwoo J. Kim
**arXiv:** [arxiv.org/abs/2610.34722](https://arxiv.org/abs/2610.34722)
**Summary:** CEPO separates shared coordination instructions from agent-specific execution prompts and guides their optimization according to those different roles. Applied to four existing prompt optimizers, it improves performance across eleven benchmarks in four domains, with additional studies showing better optimization-budget efficiency and scaling with agent count.

---

### 14. CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents
**Authors:** Yijia Fan, Xilin He, Yilei Jiang, Dongming Wu, Jiaxu Wang, Xiangyu Yue
**arXiv:** [arxiv.org/abs/2610.40799](https://arxiv.org/abs/2610.40799)
**Summary:** CaPtain post-trains a small open vision-language model to write robot-control code using supervised fine-tuning and multi-turn reinforcement learning, without requiring a VLA or privileged state at deployment. Its simulator-state physical critic supplies training credit for delayed action effects, raising held-out LIBERO success from 55.4% after fine-tuning to 73.8% after reinforcement learning and supporting transfer to real hardware.

---

### 15. No Channels Left Behind: Understanding Diffusion Acceleration through Residual Gates
**Authors:** Junha Park, Jaemyung Yu, Jaehui Hwang, Jong-Seok Lee, Dongyoon Han
**arXiv:** [arxiv.org/abs/2610.40914](https://arxiv.org/abs/2610.40914)
**Summary:** This study links diffusion-transformer training acceleration to reorganization of AdaLN-Zero residual gates, finding that broader channel participation accompanies better generation quality across several auxiliary objectives. A teacher-free feature-norm regularizer guided by that observation improves FID over dispersive loss on ImageNet 256-by-256 with SiT-B/2.

---

### 16. Probing Spatial State Representations in Visual Foundation Models
**Authors:** Baiqiao Yin, Zhongang Cai, Ruisi Wang, Qiwei Liang, Lei Yang, Ziwei Liu
**arXiv:** [arxiv.org/abs/2610.40636](https://arxiv.org/abs/2610.40636)
**Summary:** This paper probes ten frozen visual representations under streaming egocentric observations for spatial structure, object persistence, predictive updates, and actionability. It finds that visible-scene readout does not ensure persistent or actionable spatial knowledge, and that supplying the correct goal does not reliably improve progress in the tested action predictions.

---

### 17. WorldBridge: Bridging Video and Action for Task Generalization in World Action Models
**Authors:** Jun Cen, Yubo Guo, Hao Li, Liangkai Li, Yaoxu Lyu, Meng Wei, Zeqi Xiao, Sizhe Yang, Yuqiang Yang, Yifan Ye, Shanghang Zhang, Duo Zheng
**arXiv:** [arxiv.org/abs/2610.40748](https://arxiv.org/abs/2610.40748)
**Summary:** WorldBridge separates video and action experts with structured attention and joint flow matching to study how video coverage and sparse action labels support robot task generalization. On RoboTwin 2.0 out-of-distribution tasks, adding task videos raises success from 25.07% to 55.90%, and adding one action-labeled demonstration per task raises it further to 70.70%.

---

### 18. GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching
**Authors:** Ariel Lapid, Yuval Haitman, Reuven Peretz, Arnon Netzer, Idit Diamant
**arXiv:** [arxiv.org/abs/2610.31222](https://arxiv.org/abs/2610.31222)
**Summary:** GLOW-FM performs low-light image enhancement through one-step conditional flow matching in the latent space of a frozen Tiny-VAE. Terminal Velocity Matching supports competitive image quality and cross-dataset generalization on real-world benchmarks with one function evaluation and 34 GFLOPs for the small variant.

---

### 19. On the Origin and Evolution of Training-Inference Mismatch in LLM Reinforcement Learning
**Authors:** Yu Li, Yufa Zhou, Tian Lan
**arXiv:** [arxiv.org/abs/2610.40945](https://arxiv.org/abs/2610.40945)
**Summary:** This paper decomposes LLM reinforcement-learning training-inference mismatch into numerical discrepancy and stale-policy lag, showing why these sources require different corrections. Its discrepancy-lag correction combines score centering, lag-ratio clipping, and effective-sample-size-triggered sampler resynchronization to stabilize stale-sampler training on Qwen3-0.6B and Qwen3-1.7B.

---

### 20. When Requirements Interact: Scaling Long-Horizon Coding via Interdependent Specifications
**Authors:** Yishuo Cai, Minzheng Wang, Liang Zhao, Linghao Zhang, Lei Li, Shicheng Li, Xu Sun, Fuli Luo
**arXiv:** [arxiv.org/abs/2610.40256](https://arxiv.org/abs/2610.40256)
**Summary:** CodeSpecWeave synthesizes coding tasks with interdependent requirements and executable tests, using a reviewer to audit solution trajectories for test reliability. It produces 4,670 training tasks across 2,865 repositories and a 100-task benchmark with 1,044 specifications, with reinforcement learning on the training set improving DeepSWE-v1.1 performance over the base model.
