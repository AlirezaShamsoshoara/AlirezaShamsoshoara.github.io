---
title: "Daily AI Papers — October 17, 2026"
date: 2026-10-17
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-17/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robotics
  - reinforcement-learning
---

### 1. Behavioral Compositionality of Sparse Autoencoder Representations
**Authors:** Haotian Ma, Ziye Mei, Frederic Sala
**arXiv:** [arxiv.org/abs/2610.21261](https://arxiv.org/abs/2610.21261)
**Summary:** SAE Additivity Residuals quantify how much behavioral variation remains unexplained above a chosen interaction order, letting the authors compare learned sparse-autoencoder coordinates with random rotations of the same subspace. Across 18 model-behavior settings, learned coordinates are more first-order compositional, but pairwise terms still substantially improve coalition ordering and combined steering fidelity.

---

### 2. Can World and Action Modeling Benefit Each Other under Unified Causal Training?
**Authors:** Yue Su, Bokai Lin, Xinkai Wang, Chubin Zhang, Xiangnan Wu, Kuan Zhang, Weiyang Jin, Jiwen Yu, Yiming Li, Cewu Lu, Lixin Yang, Xihui Liu
**arXiv:** [arxiv.org/abs/2610.21095](https://arxiv.org/abs/2610.21095)
**Summary:** OneWM places action-conditioned world prediction and policy learning in one shared causal video-action architecture to test whether the two objectives help each other. Experiments on LIBERO, LIBERO-Plus, RoboCasa365, and real robots show that world prediction improves policy performance and generalization, while action learning improves multi-view prediction fidelity.

---

### 3. OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling
**Authors:** Bowei Liu, Xinchen Zhang, Xuhuan Li, Tianlin Zhang, Kaian Jiang, Jingwei Liu, Congyang Zhao, Yifei Qian, Junhong Liu, Zhiheng Li, Yujiu Yang, Yang Cai, Ling Yang
**arXiv:** [arxiv.org/abs/2610.22355](https://arxiv.org/abs/2610.22355)
**Summary:** OmniVerifier-C1 decomposes complex multimodal rules into fine-grained components and assigns graded scores instead of a single binary judgment, using decoupled reinforcement learning for local and global alignment. The structured verifier generalizes better to out-of-domain critique tasks, and pairwise verification with reference images proves more accurate on rule-governed worlds such as mazes and Sudoku.

---

### 4. Each Reward to Its Relevant Tokens: Reward-Specific Token-Level Credit Assignment for Multi-Reward RL
**Authors:** Skylar Zhai, Haonan Wang, Zhining Liu, Linxin Song, Xuwei Ding, Jingcheng Liang, Jian Kang
**arXiv:** [arxiv.org/abs/2610.21439](https://arxiv.org/abs/2610.21439)
**Summary:** MRTPO assigns each reward's advantage only to response tokens relevant to that verifier, estimating relevance from the Jensen-Shannon distance between policy predictions with and without verifier information. Without auxiliary models or token annotations, it converges faster and outperforms comparison methods on text-to-SQL, multi-constraint instruction following, and tool calling.

---

### 5. Data World: Scaling Data Environments from Scratch
**Authors:** Zhanli Li, Zeyuan Xu, Chaoxu Pang, Zeyuan Liu, Anyang Ji, Te Sun, Kongcheng Zhang, Wenbo Xu, Xubin Yue, Shipeng Luo, Junjie Zhao, Yingfan Hua, Jingqing Ruan, Zhongda Su, Feng Hong, Zhizhao Zeng, Ke Zeng, Xunliang Cai, Hanjia Ye
**arXiv:** [arxiv.org/abs/2610.21656](https://arxiv.org/abs/2610.21656)
**Summary:** Data World generates the mechanisms behind heterogeneous files before synthesizing the files, tasks, and evaluation rubrics, with independent audits checking whether targets are recoverable. Its benchmark exposes a persistent computation-insight gap, while RL-zero training on 2,135 synthetic tasks improves a Qwen3.6-based agent across DataWorld-Bench and three external benchmarks.

---

### 6. MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering
**Authors:** Shangheng Du, Jinxin Shi, Shuaiyu Zhang, Yiming Wu, Junpeng Zhao, Shiyang Feng, Xin Li, Liang He, Xiangchao Yan, Bo Zhang
**arXiv:** [arxiv.org/abs/2610.22344](https://arxiv.org/abs/2610.22344)
**Summary:** MLExpert is a 35B mixture-of-experts agent trained for autonomous machine-learning engineering through outcome-guided hierarchical SFT and Windowed Interaction RL over blocks of experimental decisions. It raises the base model's MLE-Bench Lite medal rate from 37.9% to 72.7% and transfers its optimization capability to scientific, scaffold, and algorithm optimization tasks.

---

### 7. Trajectory-Level Speculation with Semantic Verification for Tool-Using Agents
**Authors:** Zilin Wang, Yinhong Liu, Chao Chen, Qun Liu, Zhijiang Guo
**arXiv:** [arxiv.org/abs/2610.21463](https://arxiv.org/abs/2610.21463)
**Summary:** SpecAgent lets a weak model draft grounded, read-only tool trajectories while a strong model reviews an entire segment in one prefill pass, accepting the longest valid prefix and repairing the first rejected step. It nearly matches the strong model on tau-squared-Bench while roughly halving memory traffic and wall time, and recovers much of the weak-to-strong quality gap on other agent benchmarks.

---

### 8. Learning Self-Orchestration in Decentralized Agent Swarms
**Authors:** Guowei Xu, Zhenting Qi, Amani Kiruga, Himabindu Lakkaraju, Yilun Du
**arXiv:** [arxiv.org/abs/2610.22322](https://arxiv.org/abs/2610.22322)
**Summary:** Market-based post-training jointly learns agent actions and decentralized orchestration by using bids to decide participation and distribute local credit without a central coordinator. Learned swarms outperform fixed coordination strategies across crafting, navigation, and deep research, while adapting faster, scaling better, and losing less performance under agent dropout.

---

### 9. CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance
**Authors:** Zixuan Wang, Yuqi Liu, Yuxin Chen, Sengqiao Yang, Jinhui Ye, Pengguang Chen, Changsheng Lu, Shu Liu, Bei Yu, Jiaya Jia
**arXiv:** [arxiv.org/abs/2610.21453](https://arxiv.org/abs/2610.21453)
**Summary:** CarryOn adds a persistent planning loop and a safety-focused execution loop around a frozen vision-language-action policy so robot assistance can reflect user preferences and recover from failures. On real and simulated robots, it reduces safety violations from 52.6% to 6.1% and raises recovery success from 13% to 80% when refined skills are reused.

---

### 10. Virtual Head Attention
**Authors:** Xibo Ding, Guoxia Wang, Jinle Zeng, Jiabin Yang, Sirui Tao, Chao Yang, Dianhai Yu
**arXiv:** [arxiv.org/abs/2610.17959](https://arxiv.org/abs/2610.17959)
**Summary:** Virtual Head Attention uses query premixing and a low-rank linear postmix to recover head diversity while allowing both operations to fold into standard GQA projections at inference. Across pretraining scales it improves quality while shrinking KV cache and compute, and its long-context model reaches an average RULER score of 84.4 versus 73.0 for GQA.

---

### 11. CoDA: Co-Evolution of Data Engines and Action Policies
**Authors:** Tianjiao Yu, Zhilin Ou, Yifan Shen, Xinzhuo Li, Yuanzhe Liu, Onkar Kishor Susladkar, Fan Wang, Ismini Lourentzou
**arXiv:** [arxiv.org/abs/2610.22362](https://arxiv.org/abs/2610.22362)
**Summary:** CoDA lets a simulation data engine and robot policy co-evolve through shared memory that records environment construction, policy failures, and learning progress, then turns critic diagnoses into generation and training programs. It lifts out-of-distribution manipulation success from 5.3% to 27.6% and produces especially large gains on LIBERO-Pro perturbations under a fixed generation budget.

---

### 12. Beyond Policy Rollouts: Embedding-Space Directional Exploration with Anchored Noise for LLM RLVR
**Authors:** Daijiao Liu, Huiyi Wang, Lina Yao, Dong Gong
**arXiv:** [arxiv.org/abs/2610.16105](https://arxiv.org/abs/2610.16105)
**Summary:** EDEN diversifies RLVR rollouts by appending a perturbed embedding position to a fraction of prompts, combining Gaussian noise with a shared anchor while leaving model architecture and test-time inference unchanged. Under the same rollout budget it beats GRPO and exploration controls on mathematical reasoning, especially in sampled-solution coverage and the number of prompt groups yielding useful advantage signals.

---

### 13. FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention
**Authors:** Guoxia Wang, Qianyue He, Siming Wu, Haoyang Xie, Qiwen Bao, Jinle Zeng, Jiabin Yang, Tian Wu, Dianhai Yu
**arXiv:** [arxiv.org/abs/2610.17901](https://arxiv.org/abs/2610.17901)
**Summary:** FlashMask-3 extends linear-size structured masks to Hopper GPUs and distributed context parallelism through zero-communication mask localization, sparsity-aware balancing, and communication pruning. It delivers substantial attention throughput gains across single- and multi-GPU tests and raises end-to-end throughput by 7.3% to 11.0% when training a 118B-A14B model at 128K context.

---

### 14. SUPRA-TEX: 3D Generation with Super-Aligned Texture
**Authors:** Chen Yang, Jiemin Fang, Fanpeng Meng, Zihao Huang, Jichen Pang, Guanjun Wu, Zhikuan Bao, Qi Tian
**arXiv:** [arxiv.org/abs/2610.22352](https://arxiv.org/abs/2610.22352)
**Summary:** SUPRA-Tex separates visible-material estimation, surface alignment, and completion, anchoring projected PBR maps in the generator's native latent space while filling unseen regions. Trained only on public data, it reaches state-of-the-art results for geometry-conditioned texturing and end-to-end asset generation while preserving reference-view details.

---

### 15. Cowork-Gym: Synthesizing Interactive Work Environments at Scale
**Authors:** Anni Zou, Cheng Chen, Jiaji Deng, Weikang Zhou, Xinji Mai, Yue Wu, Jianing Lin, Lipeng Xie, Lixiong Qin, Qingyue Zhao, Que Shen, Shuchang Tao, Xuchen Pan, Yaliang Li, Yunpeng Zhai, Yushuo Chen, Zhihai Wang, Zhuo Zhang, Zhaoyang Liu, Bolin Ding, Jingren Zhou
**arXiv:** [arxiv.org/abs/2610.17670](https://arxiv.org/abs/2610.17670)
**Summary:** Cowork-Gym synthesizes interactive work environments through a build-execute-revise loop that validates objectives, resources, user behavior, and success criteria with execution evidence. Its 64.9K environments improve post-trained Qwen agents by 4.1 to 8.7 points across six benchmarks, with the 27B model outperforming systems above 100B parameters on PawBench and ClawEval.

---

### 16. LEASH: Uncertainty-Aware Weak-to-Strong Escalation and Oversight for Computer-Use Agents
**Authors:** Qingni Wang, Changdae Oh, Yuzhe Yang, Sharon Li, Jiachen Yang, Ang Li, Xin Eric Wang
**arXiv:** [arxiv.org/abs/2610.22280](https://arxiv.org/abs/2610.22280)
**Summary:** LEASH routes computer-use tasks from a weak agent to a strong one using latent uncertainty, then monitors the black-box strong agent through a shadow observer after handoff. Across four model backbones it beats random escalation at matched rates, and with Qwen3.5-35B-A3B it matches always-on Claude Opus 5 task success while cutting inference cost by 19.2%.

---

### 17. Mine, Sample, Render: Test-Time Diversity Alignment Of Generative Models
**Authors:** Kostas Triaridis, Morris E. Sharp, Nebojsa Jojic
**arXiv:** [arxiv.org/abs/2610.21185](https://arxiv.org/abs/2610.21185)
**Summary:** MINE-SAMPLE-RENDER extracts an interpretable categorical schema and statistics from a real corpus, samples attribute combinations explicitly, and uses the generative model only as a conditional renderer. Across text, user simulation, web design, image, and 3D tasks, this test-time pipeline improves both distribution alignment and output diversity.

---

### 18. Gen4P: Video Generators are 4D Perceivers
**Authors:** Yitong Xia, Zeren Jiang, Chuanxia Zheng
**arXiv:** [arxiv.org/abs/2610.22371](https://arxiv.org/abs/2610.22371)
**Summary:** Gen4P repurposes a pretrained video generator as a feed-forward 4D perceiver, answering spatial and continuous-time queries from clean video latents without iterative denoising. With a frozen video-depth prior, it achieves state-of-the-art or competitive results in 3D point tracking, video depth, and camera-pose estimation while preserving complex motion structure.

---

### 19. SERO: Learning from Executable Oracle Continuations for Long-Horizon Agentic Reinforcement Learning
**Authors:** Dingyi Rong, Yue Shi, Chaofan Ma, Zongrui Wang, Jiezhang Cao, Yixin Cao, Liang He, Ning Liu
**arXiv:** [arxiv.org/abs/2610.19397](https://arxiv.org/abs/2610.19397)
**Summary:** SERO restores a state reached by the current policy and lets a training-only oracle execute the continuation in the real environment, exposing downstream observations and actions that ordinary failed rollouts never visit. Policy-reachability weighting gradually activates deeper oracle supervision, improving long-horizon learning on ALFWorld and out-of-distribution performance without using the oracle at inference.

---

### 20. MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents
**Authors:** Huanyao Zhang, Jiepeng Zhou, Jiaye Lin, Ontai Tang, Jingtian Hao, Mugeng Liu, Ru Peng, Lang Mei, Xiaohan Yu, Liyan Liu, Chong Chen, Wentao Zhang
**arXiv:** [arxiv.org/abs/2610.22240](https://arxiv.org/abs/2610.22240)
**Summary:** MMSearch-OPD expands simple multimodal questions into harder long-horizon searches with controlled reasoning depth and cross-modal evidence requirements, then combines reinforcement learning with on-policy distillation. Reward-gap-modulated token guidance and a decaying distillation coefficient improve multimodal deep-search capability beyond supervised fine-tuning.

---
