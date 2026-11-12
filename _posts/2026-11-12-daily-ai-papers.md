---
title: "Daily AI Papers — November 12, 2026"
date: 2026-11-12
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-12/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - reinforcement-learning
  - efficient-inference
---

### 1. One Table, Many Queries: Benchmarking Generalist Tabular Models Across Generation, Imputation, and Prediction
**Authors:** Yuanrui Wang, Kaifang Li, Xuanyue Li, Ziyun Li, Yan Lu, Xingxuan Zhang, Peng Cui
**arXiv:** [arxiv.org/abs/2611.13001](https://arxiv.org/abs/2611.13001)
**Summary:** The One Table Benchmark compares tabular generation, imputation, and prediction across 56 datasets, 46 registered methods, and 20 capability axes using aligned splits and explicit task contracts. Its experiments show that shared objectives can improve utility, but their benefits depend on the backbone and existing objectives, while faithful distributional modeling often still favors specialists.

---

### 2. Scaling Mathematical Proof Supervision from Structured Textbooks
**Authors:** Youqing Fang, Zhouqi Hua, Yinhao Tang, Yuzhe Gu, Lingkai Kong, Bin Liu, Weiming Zhang, Kai Chen, Yanan Sun, Wenwei Zhang
**arXiv:** [arxiv.org/abs/2610.40394](https://arxiv.org/abs/2610.40394)
**Summary:** TOME-Math turns 2,118 university mathematics textbooks into approximately 380K proof-supervision records while preserving curricular order, proposition-proof links, dependencies, and provenance. Fine-tuning on the full corpus improves the mean score across held-out evaluations and public benchmarks by 16.7 percentage points over the base model and exceeds the three public instruction-data baselines evaluated in aggregate.

---

### 3. SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering
**Authors:** Genming Cui, Xiangyu Li, Zixu Hao, Xin Ding, Yunxin Liu, Ting Cao
**arXiv:** [arxiv.org/abs/2611.13410](https://arxiv.org/abs/2611.13410)
**Summary:** SteerDistill uses a full-precision teacher and execution feedback to iteratively correct a quantized agent's failed responses, then distills those verified corrections into the student for unassisted inference. Across five agentic benchmarks and three models, its W4A16 agents beat the strongest quantized baseline by 1.67 to 2.18 average-score points and remain within one point of BF16, while using 67% fewer training GPU-hours than QeRL on the reported comparison.

---

### 4. Embodied First Exam
**Authors:** Kangrui Wang, Qineng Wang, Changhe Chen, Pingyue Zhang, Chi Gui, Feishi Wang, Canyu Chen, Wenli Xiao, Xiaoyu Huang, Tonghe Zhang, Linjie Li, Zihan Wang, Minyeong Kim, Yiyou Sun, Mingkai Deng, Jinyu Hou, Qi Zhu, Han Liu, Eric P. Xing, Huaxiu Yao, Zhiwen Fan, Yuejiang Liu, Dawn Song, Pieter Abbeel, Li Fei-Fei, Jiajun Wu, Yuke Zhu, Guanya Shi, Ruohan Zhang, Manling Li
**arXiv:** [arxiv.org/abs/2611.12177](https://arxiv.org/abs/2611.12177)
**Summary:** Embodied First Exam evaluates coding agents that may directly control robots, write control code, or train policies across 1,156 tasks in 35 suites on 47 robots. Its standard, realtime, and privileged settings expose physical-world constraints, and the strongest of eight agents succeeds on only 34% of the 456 core tasks in the Standard Setting.

---

### 5. Incentivizing Self-Learning in Large Language Models via Reinforcement Learning
**Authors:** Lingkai Kong, Yuzhe Gu, Haiteng Zhao, Zijian Wu, Youqing Fang, Zhouqi Hua, Yanan Sun, Kai Chen, Wenwei Zhang
**arXiv:** [arxiv.org/abs/2610.39671](https://arxiv.org/abs/2610.39671)
**Summary:** BookNavigator lets language models navigate long-form textbooks, learn relevant principles, and construct proofs without access to reference solutions, while reinforcement learning rewards this self-learning process. The method raises Intern-S2-Preview-35B's overall proof accuracy from 51.5% to 79.5%, beats textbook-free and fixed-retrieval RL baselines, and transfers gains to other textbooks and long-context tasks.

---

### 6. The Surprising Effectiveness of Deleting Weights in LLM Post-Training
**Authors:** Jack Lu, Zhenbang Yang, Mike Lasby, Tejas Pote, Yani Ioannou, Mengye Ren
**arXiv:** [arxiv.org/abs/2611.10866](https://arxiv.org/abs/2611.10866)
**Summary:** Deletion Tuning learns a binary mask over transformer gate projections, acquiring capabilities by zeroing fewer than 0.05% of a pretrained language model's weights with no other modification. It matches full fine-tuning across reinforcement learning with verifiable rewards, supervised fine-tuning, and on-policy distillation while producing far smaller checkpoints and substantially less forgetting.

---

### 7. Read Less, Solve More: Token-Efficient Sparse Reading of External Content for AI Agents
**Authors:** Zedong Liu, Jiaan Wu, Xinyang Ma, Le Xu, Kai Wang, Yuanchao Hu, Dingwen Tao, Guangming Tan
**arXiv:** [arxiv.org/abs/2608.22237](https://arxiv.org/abs/2608.22237)
**Summary:** SparseRead is a model-independent reading layer that tracks an agent's evidence needs, chooses adaptive reading backends, and limits raw content exposure with a faithful full-view fallback. Across six models and five scenarios, it cuts total tokens by up to 92.9% and wall time by up to 89.0% while preserving or improving task quality in 97% of settings.

---

### 8. Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference
**Authors:** Saul Urso, Emanuele Carlini, Patrizio Dazzi, Matteo Mordacchini
**arXiv:** [arxiv.org/abs/2611.10193](https://arxiv.org/abs/2611.10193)
**Summary:** PISA estimates model capabilities for each prompt, and PISA-E uses those estimates to choose both ensemble members and ensemble size under an adjustable inference-time cost-quality preference. Across four routing benchmarks, PISA leads the evaluated single-model routers on macro-average cost-performance hypervolume, while selected PISA-E operating points outperform the strongest ensemble competitors at approximately 36% and 25% lower average inference cost in the in-distribution and out-of-distribution settings.

---

### 9. GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning
**Authors:** Jiajun Chen, Shicheng Fang, Jiahao Lu, Yuxin Wang, Xipeng Qiu
**arXiv:** [arxiv.org/abs/2611.13028](https://arxiv.org/abs/2611.13028)
**Summary:** GTAGym provides automatically verifiable GTA V tasks for agent evaluation and reinforcement learning, with 103 online tasks, 47 image-based shooting tasks, and screenshot-plus-keyboard-mouse interaction. The best evaluated configuration reaches 70.9% accuracy on GTAVBench-AGI, while LoRA reinforcement learning on generated navigation tasks transfers to native GTA V tasks and improves performance there from 15% to 23%.

---

### 10. From Tool State to Scientific Action: Auditing Decision Provenance in Biomedical Research Agents
**Authors:** Xingyu Yi, Xinya Zhang, Yunshen Zhou, Haoyu Bao
**arXiv:** [arxiv.org/abs/2611.01527](https://arxiv.org/abs/2611.01527)
**Summary:** BioAgent-DF restores or transplants captured scientific computation values to audit how biomedical agents' evidence use and decisions depend on their tool state, showing that unchanged verdicts can hide changed reads and citations. In a cardiac-safety assay allocation experiment, restoring execution state and supplying certified scores recovered all 39 changed decisions after silent numerical faults, whereas replacing the prediction file alone recovered none.

---

### 11. Evolving Infra: Agent-Adaptive LLM Serving at Scale
**Authors:** Hao Kang, Weili Xu, Ziyang Li, Zheng Du, Hanchen Li, Tian Xia, Song Bian, Tushar Krishna, Huizi Mao, Ion Stoica, Song Han
**arXiv:** [arxiv.org/abs/2611.12304](https://arxiv.org/abs/2611.12304)
**Summary:** Evolving Infra decouples compute allocation from KV-cache management so serving nodes can switch between prefill and decode, with an online planner and an agent-aware distributed cache manager adapting to changing workloads. Across coding, math, and computer-use tasks on up to 256 GB300 GPUs, it reduces mean end-to-end request latency and P95 time to first token by up to 4.1x and 14x relative to NVIDIA Dynamo.

---

### 12. Micius-Flash: Lightweight Agentic Intelligence for Engineering
**Authors:** Hongcheng Gao, Weiheng Li, Yipeng Wei, Yu Lei, Shuo Sun, Yi Li, Yajiao Wang, Jie Luo, Jianwei Wen, Xinyi Zhou, Hongda Li, Yibing Zhang, Henghui Sun, Yufan Zhou, Tianfang Hao, Naihao Xue, Hailong Qu, Jingjing Zhou, Peng Xu, Yongzheng Wei, Yichen Zhu, Ziying Wang, Yibo Wang, Jianshu Zeng, Yuhang Lei, Zeqiang Wang
**arXiv:** [arxiv.org/abs/2611.10015](https://arxiv.org/abs/2611.10015)
**Summary:** Micius-Flash is a 27-billion-parameter engineering model with multimodal input and a 256K-token context, trained through a knowledge-tree data pipeline and multi-teacher on-policy distillation. It scores 64.2% on hardware-code benchmarks and 62.4% on a semiconductor-specific agent benchmark, exceeding same-size baselines by 15.0 and 17.2 points respectively, and uses an industrial harness to work with EDA tools and KiCad.

---

### 13. Test-Time Scaling for Diffusion Language Models with Frequency-Aware Remasking
**Authors:** Bowen Zuo, Yue Yu, Dongruo Zhou, Yinglun Zhu
**arXiv:** [arxiv.org/abs/2611.10486](https://arxiv.org/abs/2611.10486)
**Summary:** This two-stage diffusion-language-model sampler solves easier questions with a fast base strategy, then uses token prediction-change frequency to allocate remasking and exploration to harder questions. Experiments with LLaDA-8B-Instruct and Dream-7B-Instruct improve MATH-500 accuracy by up to 3.73 and 7.33 percentage points and HumanEval coverage by up to 11.39 and 10.98 points over a strong adaptive-allocation baseline.

---

### 14. DyCraft: An Agentic System for Long-Horizon 4D Scene Generation
**Authors:** Jeff Tan, Hang Dai, Zeqian Long, Yanzhe Lyu, R. Kenny Jones, Shangzhe Wu, Chen Geng, Jiajun Wu
**arXiv:** [arxiv.org/abs/2610.40754](https://arxiv.org/abs/2610.40754)
**Summary:** DyCraft builds long-horizon animated 3D scenes by turning a prompt into a plan, a static scene, verified storyboard poses, and local motions between those poses. Across 24 multi-shot animation tasks, this decomposition reduces physical violations and produces higher-quality scenes preferred more often by human raters than a native coding agent and prior agentic baselines.

---

### 15. Are Causal Neuron Circuits Unique and Transferable?
**Authors:** Ömer Tekin Yavuz
**arXiv:** [arxiv.org/abs/2611.13885](https://arxiv.org/abs/2611.13885)
**Summary:** This study exhaustively tests all 4,096 subsets of selected 12-neuron groups to ask whether causal intervention effects require a unique group and transfer across inputs. It finds that a few neurons or multiple disjoint subsets can often flip an answer, that ablation effects need not indicate question-specific content, and that transfer is stronger for rephrasings than for other relation chains.

---

### 16. LEASH: Stay Safe in Agentic Robotics
**Authors:** Qinfeng Zhu, Weiguang Zhao, Ke Sun, Xihao Guo, Yunxi Jiang, Rui Zhang, Lei Fan, Kaizhu Huang
**arXiv:** [arxiv.org/abs/2611.14115](https://arxiv.org/abs/2611.14115)
**Summary:** RoboRisk evaluates agentic robotics safety in 92 simulated and 13 physical-robot tasks across refusal, plan repair, execution-time hazards, injection, and sequential memory. The proposed LEASH harness shares a safety policy across the planner and task, action, and commit gates, reducing harm across six foundation models while largely preserving task completion with little time and token overhead.

---

### 17. Shortcuts and Boundaries: Verifiable RL Misalignment and Contextual Safety Learning
**Authors:** Xinjie Shen
**arXiv:** [arxiv.org/abs/2611.12865](https://arxiv.org/abs/2611.12865)
**Summary:** This work constructs verifiable reward-context conflicts in interactive tasks, showing that RL can favor unauthorized shortcuts even when compliant completion remains feasible. Execution-history checks provide a binary safety penalty that improves capability and compliance together, raising safe completion on 32 unseen changing-evidence tasks from 53.1% to 89.1% relative to task-only training while both policies complete all real work.

---

### 18. Market-Conditioned JEPA: Learning from Unpredictable Market Shocks
**Authors:** Yuqi Wang, Fengyuan Liu, Mukai Li, Haochen Luo, Lei Li, Qi Liu
**arXiv:** [arxiv.org/abs/2611.13572](https://arxiv.org/abs/2611.13572)
**Summary:** Market-Conditioned JEPA learns financial time-series representations by conditioning each asset's training prediction on a leave-one-out market signal built from other assets' future target embeddings. On 11 years of minute-level Chinese A-share data, it improves over per-asset JEPA across nine targets, with the strongest gains in exposure, risk, and liquidity, and leads the evaluated baselines on the reported portfolio backtest.

---

### 19. Are Dense Rewards Worth Their Tokens in GRPO?
**Authors:** Vikash Singh, Weicong Chen, Debargha Ganguly, Yanyan Zhang, Mohsen Hariri, Sreehari Sankar, Wang Yang, Chaoda Song, Alexander Nemecek, Osama Zafar, Yuting Shao, Kai Ye, Biyao Zhang, Xinpeng Li, Shouren Wang, Erman Ayday, Jing Ma, Sanmukh Rao Kuppannagari, Vipin Chaudhary
**arXiv:** [arxiv.org/abs/2611.13560](https://arxiv.org/abs/2611.13560)
**Summary:** A matched-compute study of dense process rewards in GRPO compares training interventions at equal generated-token and GPU-hour budgets across 1,668 runs on six models. Matching compute reverses apparent per-update gains: on Qwen2.5-1.5B, a Monte-Carlo reward finishes 14.3 accuracy points below GRPO at equal tokens and 7.8 points below at equal training time, while targeted prompt selection yields smaller reproducible improvements.

---

### 20. Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated Users in Interactive Worlds
**Authors:** Chenhao Zheng, Zixian Ma, Kai Li, Kanchana Ranasinghe, Jieyu Zhang, Artemis Panagopoulou, Weikai Huang, Jianxu Shangguan, Yuanyuan Tan, Silvio Savarese, Juan Carlos Niebles, Ranjay Krishna, Ran Xu, Honglu Zhou
**arXiv:** [arxiv.org/abs/2611.08286](https://arxiv.org/abs/2611.08286)
**Summary:** Interactive Visual Gym jointly simulates task environments and persona-conditioned users to evaluate visual assistants in closed-loop cooking, household manipulation, and mobile-interface scenarios, with 315 IVG-Bench interactions. The best evaluated model completes only 53.4% of tasks within the time limit, while a human study supports the interaction-quality metric and a proof-of-concept GRPO experiment improves both task success and interaction quality.

---
