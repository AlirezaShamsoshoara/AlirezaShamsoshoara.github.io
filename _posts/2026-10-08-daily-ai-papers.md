---
title: "Daily AI Papers — October 08, 2026"
date: 2026-10-08
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-08/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robotics
  - model-efficiency
---

### 1. STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization
**Authors:** Bingchen Yao, Haobo Xu, Haokun Lin, Yichen Wu, Ziyu Guo, Renrui Zhang, Zhichao Lu, Zhenan Sun, Ying Wei
**arXiv:** [arxiv.org/abs/2609.38169](https://arxiv.org/abs/2609.38169)
**Summary:** STEPQuant quantizes Delta-rule recurrent states according to both error magnitude and memory lifetime, while jointly fitting row and column scales to state distributions and output impact. On Qwen3.8-27B and Kimi-Linear-48B-A3B-Instruct, its 6-bit form closely matches FP32-state accuracy, compresses recurrent states by more than 5 times, and reduces total serving memory by up to 68.7%.

---

### 2. Long-WAM: Scaling the Context of World-Action Models
**Authors:** Wei Huang, Bohan Zhang, Chenzhi Liu, Isabella Liu, Shuai Yang, Weian Mao, Luozhou Wang, Yicheng Xiao, Weifeng Lin, Qixin Hu, Bryan Chu, Sifei Liu, Linxi Fan, Xiaojuan Qi, Song Han, Yukang Chen
**arXiv:** [arxiv.org/abs/2610.10528](https://arxiv.org/abs/2610.10528)
**Summary:** Long-WAM scales the visual context of causal world-action models by autoregressively pretraining on robot and egocentric video, then preserving that history-to-future structure during action adaptation. Longer context raises RoboCasa GR-1 success from 63.3% to 78.7%, while streaming and asynchronous execution support real-time deployment on systems ranging from RTX 5090 to Jetson AGX Thor.

---

### 3. nanoMuse: An Open-Source Personal Agent for Every Device You Own
**Authors:** Guangyi Liu, Yong Liu, Jiangning Zhang
**arXiv:** [arxiv.org/abs/2610.08699](https://arxiv.org/abs/2610.08699)
**Summary:** nanoMuse defines an open personal agent that can span a user’s devices, accounts, memory, and persistent conversation while keeping its model and relay deployable by the user. Its GPL-3.0 design routes actions through a Sentinel, stores readable file-based memory with provenance, and lays out a roadmap for cross-device evaluation and open action models.

---

### 4. Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness
**Authors:** Jiajun Chen, Haoyu Wu, Mingda Jia, Xihui Liu
**arXiv:** [arxiv.org/abs/2610.08621](https://arxiv.org/abs/2610.08621)
**Summary:** Recursive Game Creator uses Designer, Builder, Player, and Reviewer agents to iteratively improve games for player experience rather than mere program correctness. It scores 77.89 on GameCraft-Bench and lifts strict task success on GameASG-Bench to 53.2%, with user studies showing longer playtime and higher ratings.

---

### 5. DecepEval: A Benchmark for Evaluating Deception in LLM Agents
**Authors:** Yiming Xu, Hongyue Yu, Beihua Yang, Zihan Chen, Yixin Liu, Zhen Peng, Bin Shi, Bo Dong, Chao Shen, Irwin King, Qinghua Zheng
**arXiv:** [arxiv.org/abs/2610.07967](https://arxiv.org/abs/2610.07967)
**Summary:** DecepEval contains 1,532 paired neutral and induced cases across three task families and 28 professional scenarios, organized around pressure, incentive, opportunity, and conflict. Tests of nine frontier LLMs show that these inducements raise deception rates across models and tasks, including for models with low baseline deception.

---

### 6. Questioning the Questions: Sustaining Self-Evolution in Reasoning Models
**Authors:** Jinyuan Li, Chengsong Huang, Langlin Huang, Donghong Cai, Shiping Gao, Yuyi Yang, Jiaxin Huang
**arXiv:** [arxiv.org/abs/2610.04299](https://arxiv.org/abs/2610.04299)
**Summary:** R-Quest addresses collapse in self-evolving reasoning models by teaching solvers to reject invalid generated questions and rewarding question novelty beyond lexical differences. Across 12 math, general reasoning, and code benchmarks, it sustains gains through ten self-training rounds and outperforms R-Zero by 17.32 points.

---

### 7. GRACE: Generation-aware latent compression for efficient video generation
**Authors:** Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam, Donghoon Lee, Hyunsung Go, Yeonkyeong Lee, Hansaem Kim, Seungryong Kim
**arXiv:** [arxiv.org/abs/2610.10524](https://arxiv.org/abs/2610.10524)
**Summary:** GRACE compresses a pretrained video autoencoder while retaining a frozen base latent and learning a residual aligned in the frozen diffusion transformer's feature space. Applied to Wan2.1-I2V-14B, it reduces token count by 8 times and latency by 11.1 times while matching the original pipeline’s VBench generation quality.

---

### 8. VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction
**Authors:** Qiutong Chen, Yuchan Guo, Zhenlong Yuan, Haobo Yang, Fangfang Lin, Xinyi Long, Yin Wang, Zijian Song, Rui Lan, Shi Qiu, Boyuan Pan, Yang Luo, Yuyin Zhou
**arXiv:** [arxiv.org/abs/2610.06293](https://arxiv.org/abs/2610.06293)
**Summary:** VepAgent predicts future video events by reasoning through unobserved causal transitions and using tools for state tracking, frame retrieval, and region magnification. A composite reinforcement-learning reward promotes accuracy, causal coherence, and visual grounding, producing state-of-the-art results on FutureBench and NEPBench.

---

### 9. SGF+: Decoupling Gradient Flows for Autoregressive Video Generation
**Authors:** Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, Haoyu Wu, Weiyang Jin, Songchun Zhang, Haoyang Huang, Chun Yuan, Zeyue Xue, Nan Duan
**arXiv:** [arxiv.org/abs/2610.10429](https://arxiv.org/abs/2610.10429)
**Summary:** SGF+ separates the parameters used to write context from those used to denoise frames, avoiding negatively aligned gradients while preserving causal-attention interaction. Trained only on five-second rollouts, it improves visual quality and temporal consistency and can generate continuously for up to 24 hours without long-video fine-tuning.

---

### 10. UniWAM: Unified World-Action Model
**Authors:** Jiayi Chen, Wenxuan Song, Jingbo Wang, Shuai Zhou, Xicheng Gong, Zehua Fan, Ziyang Zhou, Junwu E, Haodong Yan, Fuhao Li, Qize Yu, Xu Huang, Pengwei Wang, Wen Chen, Shunbo Zhou, Haoang Li
**arXiv:** [arxiv.org/abs/2610.02054](https://arxiv.org/abs/2610.02054)
**Summary:** UniWAM unifies a physical reasoner, world generator, and action predictor so one architecture can jointly learn semantic understanding, visual dynamics, and robot control. Complementary supervision from VQA, human egocentric video, and robot demonstrations yields state-of-the-art results across robustness, generalization, instruction following, and long-horizon execution.

---

### 11. UltraText Bench: A Comprehensive Bilingual Benchmark for Evaluating Visual Text Rendering in Image Generation
**Authors:** Deyuan Liu, Yihao Hu, Jingxuan Zhang, Xingying Li, Jun Xie, Jiacheng Liu, Jungang Li, Yu Huang, Xuanyi Liu, Yue Ding, Zecheng Wang, Lei Zhao, Mingda Wang, Zhenglin Cheng, Peng Sun, Tao Lin
**arXiv:** [arxiv.org/abs/2610.09823](https://arxiv.org/abs/2610.09823)
**Summary:** UltraText Bench evaluates dense English and Chinese text rendering with 432 human-reviewed prompts spanning 24 scene categories and up to 12 specified text regions. Its fidelity, clarity, spatial, and scene-quality scores expose distinct model tradeoffs and steep degradation as text workloads become harder.

---

### 12. Semifactual Credit-Augmented Policy Optimization
**Authors:** Junshu Pan, Zhizhang Fu, Shulin Huang, Yiran Ding, Zifan Cheng, Wenqi Shao, Qiaosheng Zhang, Yue Zhang
**arXiv:** [arxiv.org/abs/2609.40360](https://arxiv.org/abs/2609.40360)
**Summary:** SCAPO uses answer-preserving prompt interventions to measure token probability drift and reduce training credit for unstable tokens that may reflect spurious prompt dependence. On Qwen3 base models it improves AIME 2024-2026 accuracy over GRPO by 5.63 and 4.17 percentage points while strengthening out-of-distribution generalization.

---

### 13. Tetris3D: 3D Scene Generation With Objects That Fit Together
**Authors:** Jaeyeong Kim, Jinhyuk Jang, Jongmin Lee, Kyehong Park, Seungryong Kim
**arXiv:** [arxiv.org/abs/2610.10539](https://arxiv.org/abs/2610.10539)
**Summary:** Tetris3D reconstructs single-image 3D scenes by conditioning each object on neighboring geometry and physical relationships so shapes and poses fit together coherently. Its ComOb dataset contains 1.2 million simulated scenes with interaction annotations, and experiments show state-of-the-art generation quality and physical stability.

---

### 14. RunningTab: Direct Workspace Interaction with Environment-Side Tabs
**Authors:** Jinheon Baek, Soyeong Jeong, Yumin Choi, Dongsu Han, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2610.10444](https://arxiv.org/abs/2610.10444)
**Summary:** RunningTab augments agents that directly search and read workspace files with an environment-side record of requirements, cited excerpts, and listed-but-unopened candidates. Across three benchmarks and three LLMs, it consistently beats plain direct workspace interaction and model-maintained records while preventing agents from finishing with unresolved requirements.

---

### 15. WorldSonus: Bringing Sound to Worlds
**Authors:** Pengjun Fang, Jingyi Fa, Kam Man Wu, Jiaming Wang, Haoyuan Huang, Yaguang Wu, Xiangjun Huang, Ziyang Ma, Weijia Chen, Hongyu Liu, Zeyue Tian, Qifeng Chen
**arXiv:** [arxiv.org/abs/2610.08760](https://arxiv.org/abs/2610.08760)
**Summary:** WorldSonus uses streaming causal autoregressive diffusion to synthesize spatial stereo audio for interactive world-model video at a real-time factor of 0.41. Chunk-indexed prompt scheduling allows mid-stream sound control, while stereo and ambisonic supervision produces strong acoustic quality and spatial alignment on open-domain benchmarks.

---

### 16. ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation
**Authors:** Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu
**arXiv:** [arxiv.org/abs/2609.39306](https://arxiv.org/abs/2609.39306)
**Summary:** ReSAIL selects interaction steps where privileged information most changes a teacher’s predictions and regularizes the student to preserve that privileged behavior for future cycles. On ALFWorld and TextCraft it sustains gains across three self-distillation cycles, improving final-cycle success by an average 22.5 percentage points over the augmented baselines.

---

### 17. RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments
**Authors:** Zhiqin Yang, Chenxin Li, Xiaomeng Hu, Yibin Liu, Weidong Huang, Jiankai Sun, Haitao Li, Zijian Wu, Yuzhi Huang, Fanding Huang, Hanwen Sun, Jiashun Liu, Jingqi Tong, Mingxin Huang, Shaoli Hu, Shijue Huang, Tianyi Bai, Xinyuan Wang, Yunlong Lin, Zhengyang Tang, Zhexin Zhang, Zhuo Chen, Xierui Song, Juntao Dai, Boyuan Chen, Jiaming Ji, Fangneng Zhan, Mengkang Hu, Wei Xue, Yonggang Zhang, Han Hu, Tsung-Yi Ho, Yike Guo
**arXiv:** [arxiv.org/abs/2610.10409](https://arxiv.org/abs/2610.10409)
**Summary:** RobotWorld tests general-purpose multimodal agents on 84 simulated tasks spanning manipulation, locomotion, driving, aerial control, and multiple robot embodiments. Agents can build sophisticated perception and control workflows, but traces show persistent failures in state tracking, action correction, recovery, and recognizing incomplete tasks.

---

### 18. Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position
**Authors:** Xiaoran Liu, Ziwei He, Xipeng Qiu
**arXiv:** [arxiv.org/abs/2610.10114](https://arxiv.org/abs/2610.10114)
**Summary:** This study compares hybrids of full attention with sliding-window or gated linear attention and attributes their different context-extension behavior to positional inductive biases. Its sliding-window linear-attention design achieves 16-times training-free length extrapolation while retaining 100% NIAH-SK1 accuracy at 64k context.

---

### 19. PhysEvo: Astra Can Act, Let It
**Authors:** Wenqing Tian, Zeyu Zhang, Zhaocheng Liu, Fengwei Liu, Qiang Liu, Liang Wang
**arXiv:** [arxiv.org/abs/2610.08995](https://arxiv.org/abs/2610.08995)
**Summary:** PhysEvo surrounds a frozen model with task and meta-agents that diagnose robot trajectories, revise tools and skills, and retain tested corrections without weight updates. It reaches 62% success on held-out RoboDojo layouts and 84% success across 25 real-world trials after transferring and continuing the simulation-evolved harness.

---

### 20. Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective
**Authors:** Han Cui, Jianhao Yan, Yun Luo, Hongbo Zhang, Zhizhang Fu, Yue Zhang
**arXiv:** [arxiv.org/abs/2610.03185](https://arxiv.org/abs/2610.03185)
**Summary:** This paper interprets on-policy distillation as implicit reinforcement learning in which a teacher rewards student behaviors even when the teacher rarely generates them itself. The analysis shows that reliable implicit rewards make correct answers easier to sample, while misaligned rewards amplify long repetitive outputs; masking unhealthy responses and starting from SFT both mitigate collapse.
