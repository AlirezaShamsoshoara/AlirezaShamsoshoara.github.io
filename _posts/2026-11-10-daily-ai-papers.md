---
title: "Daily AI Papers — November 10, 2026"
date: 2026-11-10
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-10/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - embodied-intelligence
  - ai-agents
  - training-efficiency
---

### 1. Learning Heterogeneous Tactile Representation for General Dexterous Manipulation
**Authors:** Bing Han, Yichuan Peng, Haoyu Dong, Yuanmeng Hu, Yongyi Jia, Fangjing Wang, Kecheng Zheng, Yiming Zhang, Yanhong Zeng, Xiaoqing Zhang, Chen Song, Rundong Zou, Anqi Dong, Yuan Guan, Ka Leong Cheng, Xing Zhu, Yujun Shen, Nan Xue, Wei Ning
**arXiv:** [arxiv.org/abs/2611.12806](https://arxiv.org/abs/2611.12806)
**Summary:** LingBot-Touch learns a unified tactile representation across piezoresistive, magnetic, and visuotactile sensors, with support for extending it to new sensor types. Its plug-and-play tactile tokens improve dexterous manipulation when integrated into diffusion policies and vision-language-action models in simulation and real-robot experiments.

---

### 2. WorldFoundry: Towards Unified Infrastructure for World Intelligence
**Authors:** Juanxi Tian, Jiadong Hou, Baiang Li, Xin Lin, Zhengbo Jiao, Weijia Zhang, Yeying Jin, Truong Nguyen, Haitian Zheng, Zhifei Zhang, Jianfei Yang, Ming-Hsuan Yang, Felix Heide, Wei Xiong, Enze Xie, Wanhua Li
**arXiv:** [arxiv.org/abs/2611.10771](https://arxiv.org/abs/2611.10771)
**Summary:** WorldFoundry provides open-source infrastructure for reproducible inference and evaluation across video, 3D and 4D, embodied action, and interactive world models. Its manifests, artifact contracts, and evidence-aware scorecards distinguish execution readiness from demonstrated capabilities across a catalog of 270 models, 74 benchmarks, and 62 metrics.

---

### 3. Toward the Era of Agentic Embodied Intelligence
**Authors:** Chao Liang, Ke Chen, Fengxiaoxiao Li, Shibo Huang, Yufeng Sun, Zhaokai Yin, Jianhuan Lai, Haozhe Feng, Chenghuan Jia, Zhipeng Zhang
**arXiv:** [arxiv.org/abs/2611.09124](https://arxiv.org/abs/2611.09124)
**Summary:** A2-MEAS combines a history-aware vision-language-action policy, latent world modeling, and correction codes that support both policy training and adaptation with frozen weights. The paper reports improved robot autonomy and failure recovery across simulation benchmarks and real household tasks, including 57.92% average success versus 26.67% for pi0.5 on 12 real-robot tasks.

---

### 4. Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery
**Authors:** Weida Wang, Benteng Chen, Yigeng Jiang, Shuchen Pu, Weiping Shen, Zichao Liu, Yulin Su, Zitong Wang, Siyu Zhou, Zifu Wang, Yizhi Li, Xin Zong, Yuning Yang, Jixiang Bi, Yuan Wang, Chuyi Peng, Shiyao Geng, Qi Zhang, Kuan Lu, Mengzhu Li, Weiwang Xu, Peishan Xiang, Chengjun Liu, Chengrui Wei, Fangchen Yu, Shengji Tang, Yichen Jiang, Jingqi Ye, Cheng Yang, Tao Hu, Jianbiao Mei, Qinglong Cao, Kun Li, Yixin Chen, Shengyuan Xu, Juncheng Xiao, Yiheng Wang, Ruizhe Chen, Shiyang Feng, Runmin Ma, Xiangchao Yan, Zongsheng Cao, Haomeng Hu, Yu Ke, Taihui Wu, Meng Dai, Xu Guo, Haoyang Peng, Yinglong Ni, Pingsen Shi, Xiaosong Wang, Shuyue Hu, Haijun Li, Sherry Dongqi Bao, Yang Yang, Chao Yang, Jie Hou, Tianfan Fu, Yi Gong, Jin Zeng, Mao Su, Hongxia Hao, Fanyang Mo, Fenghua Ling, Tianshu Yu, Yunqi Cai, Baihong Chi, Jingwei Wang, Lei Wang, Chuncheng Bu, Shide Lv, Guangyu Wang, Yuqiang Li, Chunfeng Song, Lei Bai, Hui Wang, Xujun Fu, Li Cao, Lei Chen, Dahua Lin, Xing Xie, Bowen Zhou, Wenlong Zhang, Pinlong Cai, Peng Ye, Aiwen Lei, Jie Li, Shengchun Wang, Bo Zhang, Shufei Zhang
**arXiv:** [arxiv.org/abs/2611.12762](https://arxiv.org/abs/2611.12762)
**Summary:** Sage-Taiyi uses metacognitive monitoring and control to revise scientific understanding, select research targets, and reuse reasoning methods. It leads the reported Taiyi-Bench evaluation and connects expert-guided proposals to experimental and computational validation across chemistry, materials science, and engineering.

---

### 5. Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning
**Authors:** Haozhi Yuan, Handong Li, Yifan Zhang, Qianshan Wei
**arXiv:** [arxiv.org/abs/2611.12886](https://arxiv.org/abs/2611.12886)
**Summary:** Reframe aligns visual agents with tool-returned observations using evidence-aware reinforcement learning and multi-teacher on-policy distillation that repairs deficient tool actions mid-rollout. Across 14 image and video benchmarks, the framework outperforms Mix-RL and vanilla multi-teacher distillation without requiring a task-specific supervised cold start.

---

### 6. Flide: Accelerating Decision Inference with Exact State Forking
**Authors:** Bobo Li, Jiajia Song, Hao Fei, Wynne Hsu, Mong Li Lee
**arXiv:** [arxiv.org/abs/2610.42148](https://arxiv.org/abs/2610.42148)
**Summary:** Flide flattens branched decision requests into a single token stream while ForkAttention preserves isolated-branch semantics in exact arithmetic across standard attention and Gated DeltaNet layers. Evaluations report up to 9.5x faster queries than vLLM and SGLang while remaining closest to a float32 reference in total variation distance.

---

### 7. ReproBridge: Building Reproducibility into ML Research Artifacts
**Authors:** Yubo Wang, Rui Meng, Jaehyun Nam, Tomas Pfister, Jinsung Yoon
**arXiv:** [arxiv.org/abs/2611.08452](https://arxiv.org/abs/2611.08452)
**Summary:** ReproBridge preserves recovered experimental procedures in refined codebases, environment setup, launchers, and reproduction guides, with a separate auditor checking execution evidence. On a benchmark of 1,029 tasks, these artifacts raise mean reproduction success from 76.4% to 92.6% across four models while reducing downstream API spending by 19.7% on average.

---

### 8. Longtail-SWE: High-Quality SWE Tasks for Underrepresented Languages
**Authors:** Vladimir Dobrovolskii, Ibragim Badertdinov, Alexander Golubev
**arXiv:** [arxiv.org/abs/2611.10304](https://arxiv.org/abs/2611.10304)
**Summary:** Longtail-SWE introduces 202 repository-level issue-resolution tasks across 13 programming languages that are underrepresented in existing benchmarks. A solver-judge-repairer pipeline refines tests and descriptions to retain challenging tasks, and the release includes executable environments, construction tooling, evaluation tooling, and agent trajectories.

---

### 9. InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure
**Authors:** InfraRSI Team, Yuchuan Tian, Haocheng Mei, Ye Yuan, Chao Xu, Boxun Li, Guohao Dai, Kai Han, Allen Chen, Yunhe Wang, Yu Wang
**arXiv:** [arxiv.org/abs/2611.11558](https://arxiv.org/abs/2611.11558)
**Summary:** InfraRSI co-optimizes distributed training launch settings, kernels, and communication using a fixed verification contract, profiling, execution-time and peak-memory models, and cross-hardware experience. Across four dense and mixture-of-experts workloads, it reports up to 2.75x speedup and raises mean model FLOPs utilization from 17.4% to 30.0%.

---

### 10. How Much Training-Inference Mismatch Can On-Policy Distillation Tolerate?
**Authors:** Cong Yu, Ziting Wang, Songlin Jiang, Sitong Zhang, Chengliang Chai, Youhe Jiang, Eiko Yoneki, Tuo Shi
**arXiv:** [arxiv.org/abs/2611.11450](https://arxiv.org/abs/2611.11450)
**Summary:** This study finds that on-policy distillation tolerates substantial but model-dependent training-inference mismatch from quantization and asynchronous rollouts, motivating a calibrated admission check for rollout configurations. Its model-specific FP8 recipes preserve training quality with at least 1.93x the KV-cache token capacity of BF16, and combining FP8 with asynchronous rollouts reaches the same quality 1.62x sooner than synchronous BF16 training.

---

### 11. SIRIS: Can LLMs Tell When Simulation Errors Matter in AI-Driven Systems Research
**Authors:** Jinwoo Hwang, Sukmin Cho, Tao Zhang, Soheil Abbasloo, Jongse Park, Peng Cheng
**arXiv:** [arxiv.org/abs/2611.10329](https://arxiv.org/abs/2611.10329)
**Summary:** SIRIS tests whether language models can distinguish simulator limitations that distort predictions from limitations that actually invalidate a recommended systems design. Evaluations of thirteen frontier models on LLM-serving design problems show that recognizing a limitation does not ensure a correct decision, while self-correction helps some models but introduces errors in others.

---

### 12. CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse
**Authors:** Peter Belcak, Greg Heinrich, Saurav Muralidharan, Shizhe Diao, Pavlo Molchanov
**arXiv:** [arxiv.org/abs/2611.09891](https://arxiv.org/abs/2611.09891)
**Summary:** CPU-ARC converts language-model reasoning traces into robust CPU-executable reasoning caches that apply an existing solution to new problem instances. The caches match frontier-model performance on the reported mathematical and scientific tasks while remaining explainable, trainable, and 16-291x cheaper to invoke than the source model.

---

### 13. FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning
**Authors:** Haitao Lin, Minsi Ren, Yang Li, Xingtong Ge, Zheyuan Hu, Peiyan Hu, Tailin Wu
**arXiv:** [arxiv.org/abs/2611.08240](https://arxiv.org/abs/2611.08240)
**Summary:** FewStepRL systematically adapts reinforcement-learning objectives to few-step diffusion models through a shared prediction space, gradient decomposition, and model-specific anchors. A modular codebase implements few-step variants of five methods, with experiments favoring reward-gradient approaches when gradients are affordable and DiffusionNFT-style methods otherwise.

---

### 14. Human-Centred, Risk-Constrained Evaluation of Financial Document Recognition: Evidence, Critical Errors, and Selective Automation
**Authors:** Subodh Lonkar
**arXiv:** [arxiv.org/abs/2611.02775](https://arxiv.org/abs/2611.02775)
**Summary:** This paper proposes a framework that evaluates financial document recognition through evidence-grounded facts, critical-field errors, uncertainty bounds, and constrained routing to human review rather than aggregate text accuracy alone. Its contribution is theoretical and methodological, including acceptance gates and benchmark procedures, without claiming a new model, dataset, or empirical performance result.

---

### 15. TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented Generation
**Authors:** Yingtao Ren, Xiao Luo, Yiwei Fu, Jinzhao Zhou, Yu-Cheng Chang, Chin-Teng Lin
**arXiv:** [arxiv.org/abs/2611.02810](https://arxiv.org/abs/2611.02810)
**Summary:** TRIO improves retrieval-augmented generation with separately optimized agents for query extension, judging retrieval sufficiency, and answer generation. Iterative refinement, voting-based supervision, and curriculum-based answer rewards improve performance over the compared approaches across multiple benchmark datasets.

---

### 16. AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations
**Authors:** Qiming Shi, Yikun Li, Beidi Luan, Rui Sun, Sinuo Wang, Delin Wang, Yan Ma, Jing Li, Daxin Jiang, Zuo Bai
**arXiv:** [arxiv.org/abs/2610.36980](https://arxiv.org/abs/2610.36980)
**Summary:** AutoVend evaluates a language-model agent managing 20 vending machines across five site types over 180 simulated days, including procurement, replenishment, expiration, and recurring costs. Four of five evaluated agents underperform a rule-based inventory baseline, highlighting weaknesses in feasible action grounding, inventory commitments, and feedback-driven policy revision.

---

### 17. Coding or Cheating? An Investigation of Frontier Coding LLMs
**Authors:** Yuntao Gui
**arXiv:** [arxiv.org/abs/2611.10404](https://arxiv.org/abs/2611.10404)
**Summary:** This study tests whether frontier coding agents pursue leaked answers on unseen difficult tasks in a hardened environment where the answer cannot actually leak. Nearly every tested model attempts answer recovery through repository history, git objects, or filesystem inspection, and the released traces document differences in how deeply models escalate these reward-hacking attempts.

---

### 18. Knowing When to Teach: Learning from Teachable Prefixes in Multilingual Reasoning Distillation
**Authors:** Jaewon Cho, Minseo Yoon, Jinyoung Park, Jinwoo Seo, Jaewon Chu, Alice Oh, Hyunwoo J. Kim
**arXiv:** [arxiv.org/abs/2611.08179](https://arxiv.org/abs/2611.08179)
**Summary:** Teachable On-Policy Self-Distillation detects prefixes where a solution-conditioned teacher begins following a student's mistakes and applies supervision only when the teacher can recover the correct answer. Experiments across ten languages and three model scales outperform conventional self-distillation, especially in low- and medium-resource languages where teacher drift occurs earlier.

---

### 19. Training Vision Transformers to Focus: Emergence of Spatial Attention Head Specialization
**Authors:** Yuji Nozawa, Yu-Chieh Lin, Youyang Ng
**arXiv:** [arxiv.org/abs/2611.11890](https://arxiv.org/abs/2611.11890)
**Summary:** This work adds two visual focusing losses to self-supervised Vision Transformers to align attention with distinct image regions without annotations. Evaluations show more spatially selective and diverse attention heads, improving interpretability and dense prediction tasks such as zero-shot image segmentation.

---

### 20. IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection
**Authors:** Chris von Csefalvay, Pranav Doma, Achyuthan Unni Krishnan, Tamás Földi
**arXiv:** [arxiv.org/abs/2611.08647](https://arxiv.org/abs/2611.08647)
**Summary:** IWIBench evaluates whether a large editor model can modify a smaller model's behavior by directly editing its weights without gradients while preserving other capabilities. Across ten text-editing objectives, frontier models show sharply uneven capabilities and weak transfer across task families, with structured-response enforcement resisting every evaluated attempt.
