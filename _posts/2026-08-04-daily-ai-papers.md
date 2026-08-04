---
title: "Daily AI Papers — August 04, 2026"
date: 2026-08-04
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-04/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - computer-use-agents
  - agentic-rl
  - llm-evaluation
---

### 1. Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language Models in Commonsense Reasoning
**Authors:** Zheng Wu, Chenhao Xue, Shijie Zheng, Yijie Lu, Cheng Yang, Zhuosheng Zhang
**arXiv:** [arxiv.org/abs/2607.28478](https://arxiv.org/abs/2607.28478)
**Summary:** LLMs over-prioritize explicit inputs like numbers, causing "Salience Bias" where irrelevant distractors crowd out implicit commonsense prerequisites needed to answer everyday reasoning questions. Testing 12 state-of-the-art LLMs, the authors show this is a suppression failure, not a knowledge gap — a context-free probe recovers over 90% of failures, and lightweight inference-time prompting alone substantially closes the gap.
**Trending because:** One of only two genuinely new papers in today's HF Daily Papers feed; diagnoses a widely-relevant blind spot across all mainstream LLMs and ships a public benchmark (SaliTrap).

---

### 2. SGTP: Sampling-based Game-Theoretic Planning for Real-Time Multi-Vehicle Autonomous Racing
**Authors:** Zhouheng Li, Fangguo Zhao, Mattia Piccinini, Baha Zarrouki, Yuan Gao, Zitong Shan, Johannes Betz, Chen Lv, Lei Xie
**arXiv:** [arxiv.org/abs/2607.25388](https://arxiv.org/abs/2607.25388)
**Summary:** Proposes SGTP, a real-time planner combining game-theoretic reasoning with GPU-accelerated sampling of control sequences to generate diverse, competitive racing behavior among multiple autonomous vehicles. It reports a 95.24% win rate and 99.35% task-completion ratio in interactive races, scaling to 10-agent scenarios with ~0.095s mean solve time, and releases an open-source multi-agent racing benchmark.
**Trending because:** Second of the two genuinely fresh HF Daily Papers entries today; strong quantitative results and an open benchmark release for a niche but active robotics/autonomy subfield.

---

### 3. Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs
**Authors:** Woongkyu Lee, Jungwook Choi
**arXiv:** [arxiv.org/abs/2607.28573](https://arxiv.org/abs/2607.28573)
**Summary:** Examines how inference-time compute scaling behaves for computer-use agents run locally, analyzing where scaling breaks down and what compute/accuracy tradeoffs emerge. Directly relevant to the fast-growing computer-use-agent space where cost and latency are practical deployment blockers.
**Trending because:** Computer-use agents are one of the hottest active research threads; failure-mode analyses of inference-time scaling address a widely-shared practical pain point.

---

### 4. How Benchmarks Mis-Score Computer-Use Agents
**Authors:** Zihan Dong, Zhiyuan Ma, Zekun Wang, Yunqing Li, Zirou Liu, Ruixuan Deng, Qishi Zhan, Rui Qian
**arXiv:** [arxiv.org/abs/2607.28367](https://arxiv.org/abs/2607.28367)
**Summary:** Argues that current benchmarks systematically mis-score computer-use agents, identifying scoring artifacts that distort comparisons between agent systems. A methodological critique aimed at improving evaluation rigor in a subfield where benchmark trust is currently shaky.
**Trending because:** Companion-topic paper to #3 above — both landed in the same arXiv cs.AI batch, reflecting a coordinated push to scrutinize computer-use agent evaluation.

---

### 5. InfoOps Bench: A Live Information Operations Safety Benchmark
**Authors:** Dorian Quelle, Lisa-Maria Neudert, Jonathan Bright, John Gallacher
**arXiv:** [arxiv.org/abs/2607.28503](https://arxiv.org/abs/2607.28503)
**Summary:** Introduces a live benchmark for evaluating AI systems' vulnerability to and role in information operations (disinformation/influence campaigns), an increasingly urgent AI-safety concern. Framed as a continuously updated ("live") benchmark rather than a static one-off dataset.
**Trending because:** Addresses AI safety and societal risk, a top-tier significance topic, with a design choice (live benchmark) intended to resist rapid obsolescence.

---

### 6. A Foundation Model of Numerical Intelligence with Cross-Disciplinary Generalization
**Authors:** Chenghan Wu, Zongmin Yu, Liu Yang
**arXiv:** [arxiv.org/abs/2607.28432](https://arxiv.org/abs/2607.28432)
**Summary:** Proposes a foundation model specifically targeting numerical/quantitative reasoning that generalizes across disciplines rather than being tuned to one domain. Part of a broader trend toward specialized foundation models for structured reasoning tasks that general LLMs still handle unreliably.
**Trending because:** Numerical reasoning remains a persistent LLM weak spot; a dedicated foundation-model approach with claimed cross-disciplinary transfer is a notable architectural bet.

---

### 7. When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust with Privileged-Modality Reliability Evidence
**Authors:** Zongheng Guo, Tao Chen, Tianli Li, Mingzhe Cui, Yang Jiao, Lei Xie, Yi Pan, Xiao Hu, Manuela Ferrario
**arXiv:** [arxiv.org/abs/2607.28421](https://arxiv.org/abs/2607.28421)
**Summary:** Studies how LLMs over-trust derived/computed measurements versus raw evidence, proposing a "privileged-modality reliability" mechanism to quantify and correct this over-trust. Ships code alongside a substantial empirical evaluation (19 tables).
**Trending because:** Extends the growing "LLM calibration/over-trust" literature into a specific, underexplored failure mode (derived vs. raw evidence), with released code lowering the bar for follow-up work.

---

### 8. GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation
**Authors:** Maya Arseven, Anette Frank, Beni Egressy, Johann Higl, Moritz Plenz
**arXiv:** [arxiv.org/abs/2607.28397](https://arxiv.org/abs/2607.28397)
**Summary:** Combines graph language models with retrieval-augmented generation to reason over graph-structured knowledge rather than flat text passages. Targets the RAG-over-structured-data niche, which is gaining traction as enterprises push RAG beyond plain documents.
**Trending because:** Graph-RAG is a fast-growing applied-AI niche as teams look to ground LLMs in structured/relational data instead of just unstructured text.

---

### 9. Beyond Rephrasing: Book-Level Organization Improves Synthetic Textbook Data for Mid-Training
**Authors:** Jiawen Tao, Miao Peng, Yaoming Li, Xiaokun Yuan, Mengzhou Wu, Wenhan Yu, Guoan Wang, Nuo Chen, Tong Yang, Maxm Pan
**arXiv:** [arxiv.org/abs/2607.28109](https://arxiv.org/abs/2607.28109)
**Summary:** Shows that structuring synthetic training data at the "book level" (coherent long-form organization) rather than simple sentence-level rephrasing improves outcomes for LLM mid-training. A 31-page study with substantial empirical backing (11 tables).
**Trending because:** Synthetic data quality for pretraining/mid-training is one of the most consequential open problems in scaling LLMs, and this offers a concrete, testable recipe improvement.

---

### 10. Group-Reflective Self-Distillation for Agentic Reinforcement Learning
**Authors:** Binbin Zheng, Zijun Xie, Guanqun Zhao, Enlei Gong, Xing Ma, Xiaoliang Fu, Zeyu Chen
**arXiv:** [arxiv.org/abs/2607.28076](https://arxiv.org/abs/2607.28076)
**Summary:** Introduces a self-distillation method that uses group-level reflection to improve agentic RL training for LLM agents, aiming to make agent policies more sample-efficient and self-correcting. Fits the broader "self-improving agent" research wave.
**Trending because:** Agentic RL and self-distillation are two of the most active current LLM-training research threads; combining them targets a clear efficiency gap.

---

### 11. SKILL-KD: Contrastive Skill Distillation for LLM Agents
**Authors:** Qiming Shi, Yibo Dou, Jiawen Zhu, Yulong Tao, Linbo Jin, Zhaolu Kang, Yunfan Zhou, Di Weng
**arXiv:** [arxiv.org/abs/2607.28048](https://arxiv.org/abs/2607.28048)
**Summary:** Proposes contrastive distillation of discrete "skills" from larger to smaller LLM agents, aiming to transfer agentic capability more efficiently than standard knowledge distillation. Targets cheaper deployment of capable agent models.
**Trending because:** Skill-level (vs. token-level) distillation is a natural next step as agentic LLM deployment costs become a bigger practical concern.

---

### 12. Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation for Large Reasoning Models
**Authors:** Yecheng Wu, Song Han, Han Cai
**arXiv:** [arxiv.org/abs/2607.28449](https://arxiv.org/abs/2607.28449)
**Summary:** An update to on-policy distillation for large reasoning models that addresses "style bias" introduced when distilling from a different teacher model, improving cross-teacher transfer fidelity. Comes from a team with a strong track record in efficient-model research (Song Han's lab).
**Trending because:** On-policy distillation for reasoning models is a hot efficiency technique post-o1/R1-style training; a "2.0" iteration signals active, validated follow-up work.

---

### 13. Beyond a Single Judge: Simulating Social Persona Panels for Generative UI Evaluation
**Authors:** Zheng Wu, Yibo Luo, Pu Zhang, Cheng Yang, Zhuosheng Zhang
**arXiv:** [arxiv.org/abs/2607.28439](https://arxiv.org/abs/2607.28439)
**Summary:** Proposes evaluating generative UI outputs using simulated panels of diverse social personas instead of a single LLM judge, aiming to better capture varied human preferences. Shares authors with paper #1 in today's list, suggesting a coordinated research program on LLM evaluation robustness.
**Trending because:** LLM-as-judge reliability is a widely-debated evaluation bottleneck, and generative UI is a fast-emerging application area needing better assessment methods.

---

### 14. HARGO: Heterogeneity-Aware Reward-Guided Optimization for RL Post-Training of LLMs on HPC Tasks
**Authors:** Tiangang Li, Xiangbo Tian
**arXiv:** [arxiv.org/abs/2607.28301](https://arxiv.org/abs/2607.28301)
**Summary:** Proposes a reward-guided RL post-training method that accounts for hardware/task heterogeneity when optimizing LLMs specifically for HPC (high-performance computing) tasks. A domain-specialization play for LLM post-training beyond general chat/coding use cases.
**Trending because:** Extends RL post-training techniques into a less-explored applied domain (HPC), reflecting the broader trend of specializing reasoning-RL recipes per vertical.

---

### 15. From Expert Reduction to Behavioral Divergence: Tracing Numerical State through Sparse MoE Inference
**Authors:** Tianyang Zhu
**arXiv:** [arxiv.org/abs/2607.28097](https://arxiv.org/abs/2607.28097)
**Summary:** Investigates how numerical precision/state changes propagate through sparse Mixture-of-Experts inference, tracing how expert routing reduction leads to behavioral divergence in outputs. Relevant to understanding and debugging quantized/compressed MoE deployment.
**Trending because:** MoE architectures now underpin many frontier models, and interpretability/robustness of sparse routing under numerical pressure is an increasingly practical deployment concern.

---

### 16. Contrastive Reinforced Policy Optimization via Privileged Self-Distillation
**Authors:** Xingjian Wu, Junlin Liu, Xingchen Liu, Xuhang Zhu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
**arXiv:** [arxiv.org/abs/2607.28026](https://arxiv.org/abs/2607.28026)
**Summary:** Combines contrastive learning with reinforced policy optimization and privileged self-distillation to improve RL-based LLM training, likely aimed at more stable/efficient policy gradients. Large industry-style author list (Xunliang Cai is a known Meituan LLM researcher) suggests an applied, production-oriented contribution.
**Trending because:** Another entry in the fast-moving RL-post-training-for-LLMs space, combining three distinct optimization techniques into one recipe.

---

### 17. Building a User Foundation Model for the Open Web
**Authors:** Solal Vernier, Ivan Can Arisoy, Merwan Barlier, Blaž Škrlj
**arXiv:** [arxiv.org/abs/2607.28019](https://arxiv.org/abs/2607.28019)
**Summary:** Proposes a foundation model trained to represent user behavior across the open web, aimed at generalizable personalization/recommendation applications. Accepted to RecSys 2026, indicating peer-reviewed validation in the recommender-systems community.
**Trending because:** "Foundation model" framing applied to user/behavioral modeling (rather than language or vision) reflects the broader trend of foundation-model paradigms spreading into recommendation systems; RecSys'26 acceptance adds credibility.

---

### 18. TAPO: Transition-Aware Policy Optimization for LLM Agents
**Authors:** Cong Li, Peixi Peng, Yisen Zhao, Xinyu Hu, Shudong Liu, Zhan Su, Zhuojian Li
**arXiv:** [arxiv.org/abs/2607.27973](https://arxiv.org/abs/2607.27973)
**Summary:** Introduces a policy optimization method for LLM agents that explicitly models state transitions rather than treating agent trajectories as flat token sequences. Aimed at improving credit assignment in multi-step agentic tasks.
**Trending because:** Transition/state-aware RL formulations are gaining traction as a fix for poor credit assignment in long-horizon LLM agent training, a widely-recognized limitation of naive RLHF/RLVR setups.

---

### 19. Beyond Frame Selection: Generative Latent Evidence Aggregation for Long-Video Understanding
**Authors:** Bowen Liu, Shuning Wang, Xinpeng Ding, Zhiheng Wu, Bodong Du, Xiaomeng Li
**arXiv:** [arxiv.org/abs/2607.28516](https://arxiv.org/abs/2607.28516)
**Summary:** Moves beyond simple frame-selection strategies for long-video understanding by generatively aggregating latent evidence across a video, aiming to better capture information that's spread across many frames. Targets a persistent bottleneck in long-video multimodal LLMs.
**Trending because:** Long-video understanding is a major open challenge for multimodal LLMs as context windows grow; generative aggregation is a notable departure from the dominant frame-sampling paradigm.

---

### 20. Scaling Vision-Language Models Is Not Enough to Mitigate Bias
**Authors:** Ioannis Sarridis, Ioannis Kompatsiaris, Symeon Papadopoulos
**arXiv:** [arxiv.org/abs/2607.28211](https://arxiv.org/abs/2607.28211)
**Summary:** Demonstrates empirically that simply scaling up vision-language models does not reduce (and may not address) bias in their outputs, challenging a common assumption that scale alone improves fairness. A cautionary, evaluation-driven contribution to VLM bias research.
**Trending because:** Directly challenges the "scale solves everything" narrative in a high-stakes area (bias/fairness), relevant to any team relying on larger VLMs as a fairness fix.
