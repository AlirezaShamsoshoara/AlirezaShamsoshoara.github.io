---
title: "Daily AI Papers — October 25, 2026"
date: 2026-10-25
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-25/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - embodied-ai
  - diffusion-language-models
---

### 1. EvalResearchBench: Can AI Agents Build Their Own Feedback for Recursive Self-Improvement?
**Authors:** Yaolun Zhang, Tianyi Xu, Yujie Zhao, Jishen Zhao, Qingyun Wu, Huazheng Wang
**arXiv:** [arxiv.org/abs/2610.04184](https://arxiv.org/abs/2610.04184)
**Summary:** EvalResearchBench tests whether AI agents can design compact, executable evaluators for coding, co-work, and reasoning under fixed time and API budgets. Across 9 researcher agents, 13 candidate models, and 14 target benchmarks, the best evaluators agree with target orderings on about 75% of model pairs, below a 91% target-agreement ceiling, while human-designed public-task samples remain strong baselines.

---

### 2. F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation
**Authors:** Jinyu Zhang, Haitao Lin, Jiashu Hou, Xiangyang Xue, Yanwei Fu
**arXiv:** [arxiv.org/abs/2610.31623](https://arxiv.org/abs/2610.31623)
**Summary:** F2G-Pose lifts visual foundation features into partial point clouds and directly predicts category-level object pose, metric size, and completed camera-frame shape from one RGB-D observation. With its task-specific network trained on synthetic SOPE data and a frozen pretrained RADIO backbone, it reports state-of-the-art SOPE and ROPE accuracy, 28 FPS pose-only inference, and transfer to real objects and manipulation settings.

---

### 3. UniAVC: Unified Audio-Video Creation via Progressive Training and Asymmetric Scheduling
**Authors:** Kien T. Pham, Yuhao Liu, Chong Hou Choi, Zhenqi He, Yanghao Wang, Chenyang Lei, Rui Liu, Qifeng Chen, Long Chen
**arXiv:** [arxiv.org/abs/2610.24791](https://arxiv.org/abs/2610.24791)
**Summary:** UniAVC first trains audio and video branches on abundant unimodal data, then uses paired data to learn cross-modal correspondence for joint generation and editing. Independent modality noise schedules and clean-modality conditioning support asymmetric generation, intent-aware editing, and selective self-refinement from one set of weights without task-specific adapters.

---

### 4. What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models
**Authors:** Jinya Sakurai, Xun Xu, Jaehong Yoon
**arXiv:** [arxiv.org/abs/2610.31576](https://arxiv.org/abs/2610.31576)
**Summary:** This controlled study separates the effects of teacher targets, training states, policy inputs, and overhead in learned token-unmasking policies for diffusion language models. Its 856K-parameter policy uses trajectory-contraction targets, confidence, and hidden states to achieve the strongest reported GSM8K accuracy-versus-evaluation frontier and throughput on LLaDA-8B-Instruct, with competitive results on other tasks and substantial transfer to Dream-7B-Instruct.

---

### 5. Foundation4D: Towards a unified perception and reconstruction model for autonomous vehicles
**Authors:** NVIDIA: Sérgio Agostinho, Maximilian Apodaca, Emmanuel Attia, Guillem Braso, George Dong, Ilya Fedorov, Michele Fenzi, Gang Huang, Jiahui Huang, Shengyu Huang, Bingxin Ke, Laura Leal-Taixé, Kuan-Ting Lee, Mingxuan Liu, Tian Liu, Tim Meinhardt, Aljoša Ošep, Naveen Kumar Rai, Kefei Ren, Cristiano Saltori, Keqiang Wu, Ning Xu, Fei Xue, Jin-Bey Yu, Lei Zhang, Qunjie Zhou
**arXiv:** [arxiv.org/abs/2610.30340](https://arxiv.org/abs/2610.30340)
**Summary:** Foundation4D unifies geometry estimation, 3D detection, semantic occupancy, and Gaussian reconstruction from multi-camera driving video with a shared spatiotemporal backbone. The authors release a 1,253-clip benchmark, report leading results among compared methods after benchmark-specific fine-tuning, and show that joint training improves detection and geometry while supporting lidarless driving-scene reconstruction.

---

### 6. Who Takes the Lead? Model Ability and Task-Conditioned Collaboration with Humans
**Authors:** Weien Li, Haochen Liu, Zeyu Li, Rui Song, Zixuan Dong, Ye Yuan
**arXiv:** [arxiv.org/abs/2610.27148](https://arxiv.org/abs/2610.27148)
**Summary:** This study uses a shared-control maze to distinguish appropriate division of labor from poor collaboration by varying whether a human or an LLM agent has the shorter route to a common goal. Across four models, stronger solo solvers involve humans selectively, including roughly 80% of initial decisions when humans have a route advantage, whereas the weakest model lacks that selectivity.

---

### 7. MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models
**Authors:** Khuyen Pham, Tran Nguyen Le, Edoardo Fazzari, Cesare Stefanini
**arXiv:** [arxiv.org/abs/2610.22951](https://arxiv.org/abs/2610.22951)
**Summary:** MambaAct replaces the transformer action expert in a flow-matching vision-language-action policy with a compact Mamba expert and compressed visual-language conditioning while retaining the pretrained prefix encoder. It reports a 10-fold smaller action expert, denoising-latency reductions of 64.8% on LIBERO and 58.8% in real-world deployment, and a 1.08-percentage-point mean LIBERO success gain across three fine-tuning seeds.

---

### 8. TILDE: Teacher-in-the-Loop Distillation from Embodied Foundation Models
**Authors:** Yuxiang Lu, Yantong Liu, Jinghua Hou, Xueli Sun, Ruihua Han, Zhe Liu, Hengshuang Zhao
**arXiv:** [arxiv.org/abs/2610.25376](https://arxiv.org/abs/2610.25376)
**Summary:** TILDE transfers embodied foundation-model capabilities to student policies by combining on-policy teacher supervision with teacher-executed recovery trajectories. Its AutoDAgger pipeline uses a robotic reward model to trigger interventions without human monitoring, collecting recovery experience more than twice as fast as a human-in-the-loop method and improving performance by up to 4.1 times over behavior cloning across three real-world tasks.

---

### 9. HyperDrone: Simulation-to-Reality Transfer at Millions of Frames per Second
**Authors:** Jonas Eschmann, Giuseppe Loianno
**arXiv:** [arxiv.org/abs/2610.28950](https://arxiv.org/abs/2610.28950)
**Summary:** HyperDrone combines GPU multirotor dynamics with the HyperLux ray-tracing engine to render rich visual observations at millions of frames per second on consumer GPUs, reporting more than 20-fold faster batch simulation than compared state-of-the-art quadrotor simulators. The authors demonstrate simulation-to-reality transfer by training a vision-based yaw-control policy entirely in simulation and running it onboard a camera-equipped Crazyflie quadrotor.

---

### 10. Diffusion Language Models Change Speed Across Tasks and Languages
**Authors:** Mohsen Fayyaz, Ali Modarressi, Daniel Israel, Lucas Bandarkar, Nanyun Peng
**arXiv:** [arxiv.org/abs/2610.25835](https://arxiv.org/abs/2610.25835)
**Summary:** An analysis of two diffusion language models across 10 tasks finds that forward passes per token depend on output novelty, word rarity, task type, and language tokenization, with story writing costing over three times as many passes as grammar correction in DiffusionGemma. Decoding effort also tracks correctness, and weighting math-answer candidates by decoding speed improves over majority voting by up to 4.2 points without extra inference cost.

---

### 11. LLM-Attack Suite: A Unified Red-Team Framework for Privacy Evaluation of Split and Distributed LLM Systems
**Authors:** Georgios Politis, Evangelos Pappas
**arXiv:** [arxiv.org/abs/2610.22722](https://arxiv.org/abs/2610.22722)
**Summary:** LLM-Attack Suite standardizes privacy evaluations of split language models by recording attacker access, datasets, scoring rules, undefended controls, and untested attacks while saving predictions for independent scoring. In a controlled GPT-2 experiment, exposing returned training gradients raises token recovery from 94.20% to 97.38% and exact-document recovery from 13.71% to 37.77%, illustrating how attacker access changes privacy conclusions.

---

### 12. SplatLab: Autonomous Scientific Discovery for 3DGS Research
**Authors:** Seemandhar Jain, Manmohan Chandraker
**arXiv:** [arxiv.org/abs/2610.30468](https://arxiv.org/abs/2610.30468)
**Summary:** SplatLab autonomously reproduces 3D Gaussian Splatting baselines, proposes and evaluates extensions, runs ablations, and writes manuscripts while binding every reported number to a logged training run. Its PSNR-targeted experiments report gains of 0.18 to 3.78 dB over reproduced targets, using evolutionary tournaments and a standing falsifier to select candidates and test claims.

---

### 13. IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems
**Authors:** Jie Mao, Pingchen Lu, Zikun Qu, Jiahang Sun, Xiangyi Wang, Zhiwei Shang, Zhiyong Wang, Guojun Xiong, Zhongxiang Dai
**arXiv:** [arxiv.org/abs/2610.24383](https://arxiv.org/abs/2610.24383)
**Summary:** IF-MAP uses controlled semantic prompt perturbations and local response models to prioritize agents whose improvement is most likely to increase end-to-end multi-agent performance, without model parameters or gradients. Across six workflows, optimizing selected prompts yields a 3.81-percentage-point macro-average gain versus 1.85 for uniform selection, with substantial token savings relative to improving every agent.

---

### 14. TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments
**Authors:** Yicheng Xu, Zhikai Xu, Ziyuan Chen, Yuhang Dong, Tao Zhang, Zhucun Xue, Yong Liu, Jiangning Zhang
**arXiv:** [arxiv.org/abs/2610.30043](https://arxiv.org/abs/2610.30043)
**Summary:** TARSphere combines physics simulation, embodied non-player characters, constrained dialogue, hierarchical memory, and executable skills to evaluate long-horizon robot agents in changing physical and social environments. Its benchmark contains 360 episodes across 30 indoor scenes, and evaluation of eight multimodal models exposes persistent difficulties with task updates, human interaction, collisions, and falls.

---

### 15. Skeleton-Grounded Latent Action Model for Robot World Models
**Authors:** Qi Lv, Jiayi Lin, Yuxin Jiang, Jianzong Wang, Xiang Deng, Mike Shou Zheng
**arXiv:** [arxiv.org/abs/2610.31474](https://arxiv.org/abs/2610.31474)
**Summary:** SkeLAM separates skeleton-grounded robot kinematics from residual visual dynamics and learns a lightweight adapter from robot controls to support controllable world-model rollouts. On DROID it reports 19.5% lower end-effector displacement error and 11.1% lower LPIPS than DreamDojo, alongside generated human-to-robot motion transfer and agreement between predicted and real robot policy success rates.

---

### 16. Bridging Exploration and Persona: Information-Directed Dueling for Test-Time Agent Personalization
**Authors:** Jie Mao, Pingchen Lu, Xiangyi Wang, Hengquan Huang, Shuang Qiu, Min Zhang, Zhongxiang Dai
**arXiv:** [arxiv.org/abs/2610.24385](https://arxiv.org/abs/2610.24385)
**Summary:** ID-TAP personalizes LLM agents at test time through binary response comparisons, combining a query-conditioned neural utility model with a lightweight Bradley-Terry explorer and similarity-weighted warm starts. Across seven user-conditioned generation benchmarks with simulated preferences, it achieves the strongest aggregate performance among compared baselines under a fixed ten-round comparison budget.

---

### 17. SEAM: Spectral Embedding Alignment and Merging for Low-Resource TTS
**Authors:** Walaa Othman, Baher Mohammad, Stamatios Lefkimmiatis, Ammar Ali
**arXiv:** [arxiv.org/abs/2610.26252](https://arxiv.org/abs/2610.26252)
**Summary:** SEAM initializes embeddings for unseen text-to-speech tokens without paired audio by preserving subtoken phonetic order with a spectral filter and aligning embeddings through closed-form ridge regression. Across three languages and two TTS architectures, it approaches or matches baseline performance with up to four times less training data than random initialization and mean pooling.

---

### 18. Realism VS Accuracy: Event Sequence Forecasting from a Generative Modeling Perspective
**Authors:** Dmitry Osin, Egor Surkov, Petr Mokrov, Igor Udovichenko, Ivan Karpukhin, Evgeny Burnaev, Egor Shvetsov, Alexander Korotin
**arXiv:** [arxiv.org/abs/2610.12586](https://arxiv.org/abs/2610.12586)
**Summary:** This work frames multi-horizon event-sequence forecasting as conditional generative modeling and introduces a benchmark that measures both prediction accuracy and distributional realism. Its evaluation finds a trade-off between the two, while the proposed Wasserstein BaryBooster converts samples from a realism-strong diffusion model into a state-of-the-art predictor.

---

### 19. MMedAgent-Plus: Scaling Multimodal Medical Agents across Modalities, Tasks and Workflows
**Authors:** Ruoxin Wang, Yuanting Pan, Binxu Li, Ruiyang Ji, Yaqian Chen, Jiayuan Ding, Qifan Wang, Lifu Huang, Mingjie Li, Yu Zhang, Ehsan Adeli, Kilian Pohl, Zhe Xu, Zihao Lin, Haoyu Dong, Yixin Wang
**arXiv:** [arxiv.org/abs/2610.27233](https://arxiv.org/abs/2610.27233)
**Summary:** MMedAgent-Plus combines an instruction-tuned vision-language planner with 18 specialist models across 12 medical tasks and 8 modalities to coordinate tool calls and synthesize grounded responses. In 350 end-to-end evaluation cases across seven tasks, it invokes the required specialist correctly in 90.6% of cases and reaches 0.98 final-answer accuracy, matching the dedicated leading specialist.

---

### 20. A Fix for Softmax and Cross-Entropy
**Authors:** Jonathan T. Barron, Dan Gnanapragasam, Michael Tschannen
**arXiv:** [arxiv.org/abs/2610.31642](https://arxiv.org/abs/2610.31642)
**Summary:** This paper identifies numerical bugs in standard softmax and cross-entropy implementations that can zero the target gradient or produce nonzero gradients when student and teacher logits match, and supplies corrected implementations. The fixes eliminate the reported Slingshot phenomenon, accelerate grokking with weight decay, prevent accuracy collapse without it, and stop distillation students from drifting away from their teachers.
