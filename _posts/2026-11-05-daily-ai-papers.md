---
title: "Daily AI Papers — November 05, 2026"
date: 2026-11-05
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-05/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - embodied-ai
  - video-modeling
---

### 1. Turns Matter: Advancing Streaming Video RL via Turn-Level Credit
**Authors:** Shuai Dong, Kanghui Tian, Linghan Chen, Wenqi Shao, Hongrui Wu, Haowen Hou, Yongfu Zhu, Xuehui Wang, Ziyue Wang, Wenpu Liu, Weichu Xie, Yuqi Xu, Congcong Wang, Kaiwen Tuo, Caoyuan Ma, Taiqiang Wu, Ji Zhao, Wenzheng Chang, Dianyi Wang, Siyuan Wang, Zhongyu Wei, Yu Qiao, Jiaqi Wang
**arXiv:** [arxiv.org/abs/2611.06728](https://arxiv.org/abs/2611.06728)
**Summary:** TurnWise assigns credit to individual respond-or-wait decisions in streaming video GRPO, using silence-completed prefix scoring and losses averaged equally across turns. The authors report better streaming-video understanding than prior RL approaches without a learned critic or additional rollouts.

---

### 2. From Pixels to Actions - Towards Native Vision-Language-Action Policies
**Authors:** Weichen Fan, Haiwen Diao, Penghao Wu, Siyuan Hu, Ziqi Huang, Tianqi Liu, Mingze Sun, Ziyi Wang, Zhongang Cai, Hanming Deng, Quan Wang, Lei Yang, Lewei Lu, Fangzhou Hong, Zhaoxi Chen, Dahua Lin, Ziwei Liu
**arXiv:** [arxiv.org/abs/2611.06918](https://arxiv.org/abs/2611.06918)
**Summary:** NEO-VLA replaces a fixed visual encoder with lightweight image tokenization and lets an action expert access instruction-conditioned visual representations throughout the backbone. Controlled comparisons and manipulation experiments show stronger, more robust control, with action-critical visual signals often peaking before the final representation.

---

### 3. FrontierPhysics: Evaluating Agents for End-to-End Physics Research
**Authors:** Bingran You, Wenjun Ke, Ria Rosenauer, Bo Liu, Wenbo Chen, Min Chen, Shuqi Xu, Yue Ma, Jiechao Feng, Bo Chen, Xiangkai Sun, Jiarui Liu, Jinen Guo, Zeyu Zhou, Xu Huang, Zhuohan Li, Haoyu Li, Heguang Lin, Lijie Ding, Yadong Zeng, Kangqi Zhang, Xinge Liu, Hanwen Liu, Zhenghong Li, Alexander von Recum, Yuchen Zhu, Felix Schwarzfischer, Yizhou Zhao, Jicheng Wang, Binxu Li, Qian Yu, Chan Li, Cheng Dai, Di Wang, Haoyu Zhang, Jiankai Sun, Kaituo Feng, Mian Qin, Ruihong Yin, Yiqun Luo, Weiwei Wu, Shihong Pan, Tsung Yeh Hsieh, Xiao Huang, Yan Zhang, Sihan Li, Zirui Ren, Zengji Tu, Kyoung Whan Choe, Ke Sun, Vincenzo Galia, Vaisakhi Mishra, Jiashu He, Hongyang Wang, Zhiheng Yang, Shubham Gaur, Yifan Gu, Shuyi Wang, Zihao Zuo, Steven Dillmann, Yiyou Sun, Xinyang Han, Hanchung Lee, Molei Tao, Yue Zhao, Shilong Liu, Yuchen Wu, Xuandong Zhao, Xiangyi Li, Florian Brand, Gerbrand Ceder, Hartmut Haeffner
**arXiv:** [arxiv.org/abs/2611.06910](https://arxiv.org/abs/2611.06910)
**Summary:** FrontierPhysics evaluates end-to-end scientific agents on 56 expert-created tasks across nine physics domains, combining correctness checks with research-quality rubrics. Across 22 models in 26 configurations, no configuration passes more than 46 of 168 rollouts, with manual review identifying weak reasoning rigor and expert intuition as key limitations.

---

### 4. GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling
**Authors:** Kang He, Wenshuo Peng, Chuanhao Li, Zihui Gao, Xiaojie Xu, Zhengyuan Lin, Yuzhe Ding, Donghong Ji, Kaipeng Zhang, Yongtao Ge
**arXiv:** [arxiv.org/abs/2610.37257](https://arxiv.org/abs/2610.37257)
**Summary:** GameVerse provides 69,700 gameplay clips spanning 1,655 hours, including 1,358 hours of continuous two-minute sequences, with stable camera trajectories and event-aligned captions. Dataset analysis and training experiments report stronger annotation quality and substantially longer coherent rollouts for interactive world models.

---

### 5. What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?
**Authors:** Kejian Zhu, Zhuoran Jin, Shangqing Tu, Tianyi Men, Yupu Hao, Jiachun Li, Kang Liu, Jun Zhao
**arXiv:** [arxiv.org/abs/2611.06483](https://arxiv.org/abs/2611.06483)
**Summary:** This study evaluates agentic RL across sampling breadth and interaction depth, finding that its gains depend on adequate turn budgets and concentrate in error recovery rather than uniformly better single-step decisions. BudgetMix RL varies interaction budgets during training and improves robustness across different execution settings.

---

### 6. PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data
**Authors:** Kewei Zhang, Juncheng Ma, Guodong Lv, Duomin Wang, Feixiang Ruan, Ruiyang Si, Chuanrui Zhang, Yuxuan Chen, Hao Chen, Yichen Liu, Yintianrun Zhang, Yufan Deng, Enze Xie, Daquan Zhou
**arXiv:** [arxiv.org/abs/2611.05320](https://arxiv.org/abs/2611.05320)
**Summary:** PyRUA-DataFarm uses a coding agent, one real calibration episode, simulation, and video rendering to generate verified multi-camera robot demonstrations labeled with exact actions. On five real-robot tasks, policies trained only on farm data achieve 93 successes in 100 trials versus 84 for teleoperation-trained policies, with larger gains under changed visual conditions.

---

### 7. EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL
**Authors:** Mingzhe Zheng, Yue Wu, Jing Tan, Chang Zou, Dengyang Jiang, Zeyue Tian, Xuanhua He, Ryan Xu, Yunyang Ge, Sihui Ji, Yunlong Lin, Kaihang Pan, Hongru Yan, Sixiang Chen, Dianyi Wang, Julian Zhang, Weijie Kong, Changlin Li, Lanqing Guo, Zhao Zhong, Qifeng Chen, Harry Yang
**arXiv:** [arxiv.org/abs/2611.06518](https://arxiv.org/abs/2611.06518)
**Summary:** EmoReward calibrates emotional video-generation rewards with prompt-grounded evidence, instance-level reliability gates, and memory of reward traces from completed training runs. Experiments on HunyuanVideo 1.5 and transfer studies on SD 3.5 and FLUX support adapting reward weights without updating the underlying reward models.

---

### 8. StreamDuo: A Live Commentator and a Research Agent for Unseen Games
**Authors:** Zixian Gao, Penghao Luo, Xiangcheng Cao, Lixin Xiu, Ziqi Cai, Zhen Li, Erwin Wu, Kaipeng Zhang
**arXiv:** [arxiv.org/abs/2611.01120](https://arxiv.org/abs/2611.01120)
**Summary:** StreamDuo pairs a trainable live-game commentator with a frozen wiki-reading research agent, teaching the commentator when to request information and how to use noisy answers. Training on one game and testing on ten unseen games improves entity recall from 0.082 to 0.116 and reduces source-game leakage from 9.9 percent to 1.0 percent.

---

### 9. Halley: A Predictive Control Plane for Optical AI Data Center Networks
**Authors:** Manav Mishra, Krishna M. Sivalingam
**arXiv:** [arxiv.org/abs/2611.04408](https://arxiv.org/abs/2611.04408)
**Summary:** Halley coordinates predictive controllers for laser reserves, optical switching, microring control, and module triage, with formal guarantees and fallbacks to deployed policies. Simulations report effective goodput increasing from 65.2 percent to as much as 76.5 percent under the stated outage assumption, alongside formal verification and hardware implementation checks of fallback circuits.

---

### 10. Solv3R: 3D Looped Transformer as a Multi-view Solver
**Authors:** Jeong-gi Kwak, Andrea Tagliasacchi, Sho Kagami, Yuki Ono, Kwang Moo Yi
**arXiv:** [arxiv.org/abs/2611.02857](https://arxiv.org/abs/2611.02857)
**Summary:** Solv3R learns a looped-transformer update operator that refines multi-view geometry from its current state and incorporates new observations without restarting reconstruction. A single solver supports offline and incremental reconstruction, relocalization, and streaming, with cached solved-view representations providing reusable geometric context.

---

### 11. Human-to-Robot Transfer via Bridging Representation and Action Space in VLAs
**Authors:** Junhyeong Park, Wook Jung, Taeyoung Kim, Huiwon Jang, Jinwoo Shin
**arXiv:** [arxiv.org/abs/2611.04391](https://arxiv.org/abs/2611.04391)
**Summary:** H2RB adapts pretrained vision-language-action policies using unpaired human and robot demonstrations, aligning observations geometrically and sharing action latents through decoupled decoders. Real-world experiments report substantial object and skill transfer gains that persist under object-placement shifts, reducing dependence on target-robot demonstrations.

---

### 12. MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation
**Authors:** Aryan Das, Vinay Kumar Verma, Aakansha Mishra
**arXiv:** [arxiv.org/abs/2610.41104](https://arxiv.org/abs/2610.41104)
**Summary:** Muon-RT reuses the displacement between an EMA teacher and student to eliminate hidden-weight momentum buffers, combining that update history with orthogonalized gradients. In Qwen2.5-7B self-distillation fine-tuning, it improves average accuracy by 2.6 points over AdamW while using 42 percent less persistent memory, with further gains reported in an Olmo-3-7B study.

---

### 13. Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation
**Authors:** Yifu Luo, Chuang Ma, Zeyu Chen, Enkelejda Kasneci, Qi Chen, Gjergji Kasneci
**arXiv:** [arxiv.org/abs/2610.40574](https://arxiv.org/abs/2610.40574)
**Summary:** MTA-OPSD constructs a pool of reference-conditioned teachers and lets each generated token select its preferred teacher during on-policy self-distillation. Qwen3 mathematical-reasoning experiments consistently outperform existing OPSD approaches and report an average gain of up to 5.9 points over the base model.

---

### 14. VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation
**Authors:** Yihong Luo, Tianyu Pang, Tianyang Hu
**arXiv:** [arxiv.org/abs/2611.06796](https://arxiv.org/abs/2611.06796)
**Summary:** Velocity Adversarial Distillation compares student and teacher velocity fields with a learned critic, unifying several distribution-matching objectives for few-step generation. VA-TDM applies this supervision along student trajectories and reports state-of-the-art four-step image and video results across multiple backbones, including a 33-billion-parameter video model.

---

### 15. TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit Tokens
**Authors:** Juseon Do, Sangmin Bae, Jeesu Jung, Hwanjun Song
**arXiv:** [arxiv.org/abs/2611.01926](https://arxiv.org/abs/2611.01926)
**Summary:** TAC-CoT interleaves compact latent reasoning segments with explicit tokens for tool calls, observations, and final answers, preserving an agent's communication interface without verbalizing every reasoning step. Agentic mathematics and QA experiments report accuracy gains of up to 8.8 points and up to 6.8-fold fewer model forward passes.

---

### 16. VideoMemBench: How Well Do MLLMs Remember in Video Conversations?
**Authors:** Zhengdong Hu, Chao Wang, Kaituo Feng, Huanjin Yao, Mingfei Lu, Hehe Fan, Yi Yang
**arXiv:** [arxiv.org/abs/2610.40131](https://arxiv.org/abs/2610.40131)
**Summary:** VideoMemBench measures whether multimodal models remember visual episodes and their own earlier answers across dependent turns, using 326 videos and 2,476 dialogue turns. Evaluation of more than 20 models yields a best overall score of only 45.7 percent, exposing a substantial gap in in-context video memory.

---

### 17. SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding
**Authors:** Tianyu Liu, Jun Zhang, Wenjie Huang, Yuhao Shen, Tianqi Xu, Xinyue Hao, Hongyaoxing Gu, Xuyang Liu, Baolin Zhang, Yating Zhu, Shuang Ge, Jun Dai, Lei Chen, Yue Li, Mingchen Wan
**arXiv:** [arxiv.org/abs/2611.02846](https://arxiv.org/abs/2611.02846)
**Summary:** SpecOPD parallelizes on-policy drafter sampling and target supervision across independent branches, packing them into proposal trees while preserving each branch's attention history. Across multiple target architectures and task domains, it reports up to 41.45 percent higher mean acceptance length, 16.09-fold supervised-token throughput, and 3.56-fold generation speedup over autoregressive decoding.

---

### 18. PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real World
**Authors:** Qiang Wang, Jianxin Bi, Shulong Jiang, Ruiyang Si, Wenbo Huang, Kaiqi Chen, Jiaxin Li, Liyun Li, Xuanyi Li, Daquan Zhou
**arXiv:** [arxiv.org/abs/2611.06768](https://arxiv.org/abs/2611.06768)
**Summary:** PyRUA-REAL studies embodied recursive self-improvement through real-world exploration, code refinement, and deployment, retaining experience as persistent memory and reusable executable skills. It reports average success rates of 91.1 percent across eight real-world tasks and 84.4 percent across 42 RoboDojo tasks, including deployment without an online decision-making agent.

---

### 19. AnchorComplete: Recovering Complete Scene Meshes from Partial Point Clouds
**Authors:** Weirong Chen, Ismail El-Yamany, Ganlin Zhang, Chuanxia Zheng, Andrea Vedaldi, Daniel Cremers
**arXiv:** [arxiv.org/abs/2611.03228](https://arxiv.org/abs/2611.03228)
**Summary:** AnchorComplete reconstructs complete scene meshes from partial point clouds while preserving observed geometry through partial-point conditioning and metric-scale coarse-to-fine generation. Experiments on Replica and SCRREAM outperform strong complete-scene reconstruction baselines, particularly with sparse views.

---

### 20. Dory1.0-4B: A Looped Normalized-GPT
**Authors:** Maxim Fishman, Simeng Sun, Shantanu Acharya, Faisal Ladhak, Brian Chmiel, Santiago Akle Serano, Ron Banner, Boris Ginsburg, Krishna C. Puvvada
**arXiv:** [arxiv.org/abs/2611.03998](https://arxiv.org/abs/2611.03998)
**Summary:** Dory1.0-4B is an open looped normalized-transformer language model trained on six trillion tokens whose recurrent block can be repeated to vary inference compute from one checkpoint. Additional loops improve benchmark accuracy and agentic token efficiency, while retaining only the last loop's keys and values keeps the cache footprint independent of loop count.

---
