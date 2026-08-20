---
title: "Daily AI Papers — August 20, 2026"
date: 2026-08-20
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-20/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - evaluation-benchmarks
---

### 1. SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation
**Authors:** Keyu Tu, Zhuowei Chen, Mengqi Huang, Yuxin Wang, Jiahao Zhu, Zhendong Mao, Yongdong Zhang
**arXiv:** [arxiv.org/abs/2608.17426](https://arxiv.org/abs/2608.17426)
**Summary:** We introduce Semantic Task Completion Video Generation, an outcome-oriented video generation task. Under this formulation, success requires both achievement of the intended outcome and semantic grounding.
**Trending because:** 151 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 2. Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence
**Authors:** Xin Ding, Liang Mi, Mingzhe Huang, Zixuan Wang, Chao Zhang, Zixu Hao, Fu Chen, Xiangyu Li, Yikai Zheng, Yaoyu Guo, Weijun Wang, Kun Li, Hao Wu, Yunxin Liu, Ting Cao
**arXiv:** [arxiv.org/abs/2608.16590](https://arxiv.org/abs/2608.16590)
**Summary:** Embodied agents are increasingly used to close the gap left by end-to-end policy models. Yet the agentic path has not realized closed-loop learning in physical execution: existing harnesses remain largely open-loop, following fixed skills during rollout and reflecting only after an episode completes.
**Trending because:** 128 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 3. SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation
**Authors:** Yanlun Tu, Huacan Wang, Ziyue Zhou, Jie Zhou, Ningyan Zhu, Ge Chen, Wangyi Chen, Tengfei Zhou, Yifan Zhou, Dasheng Yang, Xiaofeng Mou, Hui Zhang, Yi Xu
**arXiv:** [arxiv.org/abs/2608.18565](https://arxiv.org/abs/2608.18565)
**Summary:** Programmable logic controllers (PLCs) run industrial plants, and large language models can already generate independent program organization units (POUs) for them. Whether such logic integrates into an existing PLC project and then runs correctly has been checked only in limited tests.
**Trending because:** 110 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 4. Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL
**Authors:** Yunhao Yang, Yuexin Bian, Yunjie Tian, Di Fu, Tianjin Huang, Yuanyuan Shi, Ziang Xiao, Nuno Vasconcelos, Yijiang Li
**arXiv:** [arxiv.org/abs/2608.17253](https://arxiv.org/abs/2608.17253)
**Summary:** Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its strongest successes still depend heavily on ground-truth supervision (e.g., verifiable reward). Such annotations are costly to obtain and become increasingly scarce as reasoning capabilities advance beyond what humans can reliably evaluate.
**Trending because:** 79 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 5. SPADE: Self-Play in Adaptive Synthetic Executable Environments
**Authors:** Bo Liu, Simon Yu, Yiding Jiang, Ao Qu, Andrew Zhao, Zichen Liu, Junsu Kim, Zijian Zhou, Seungone Kim, Tongzheng Ren, Mickel Liu, Hanfei Yu, Zhaorun Chen, Weiyan Shi, Paul Pu Liang, Luke Zettlemoyer, Yejin Choi, Natasha Jaques
**arXiv:** [arxiv.org/abs/2608.19197](https://arxiv.org/abs/2608.19197)
**Summary:** Continuous self-improvement requires an ever-expanding pool of self-generated, diverse, adaptive goals. For language agents, existing training environment pools (hand-curated, statically synthesized, or frozen-verifier) keep the goal distribution fixed as the learner scales.
**Trending because:** 38 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 6. Training Chemical Plausibility-Aware Large Language Models for Single-Step Retrosynthesis
**Authors:** Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev, Maksim Kuznetsov, Mathieu Reymond, Vladimir Aladinskiy, Alex Aliper, Alex Zhavoronkov
**arXiv:** [arxiv.org/abs/2608.18940](https://arxiv.org/abs/2608.18940)
**Summary:** Single-step retrosynthesis is a central component of computer-aided synthesis planning, yet its intrinsically one-to-many nature is poorly captured by single-answer evaluation and benchmarking protocols. To address this, we introduce Top-K prompting as a robust training and inference paradigm to better capture diverse, plausible reaction predictions.
**Trending because:** 29 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 7. LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents
**Authors:** Yiming Du, Yuxin Jiang, Tao Yuan, Jianbo Dai, Shaowei Wang, Jierun Chen, Chaofan Tao, Xianzhi Yu, Lifeng Shang, Kam-Fai Wong, Xiaohui Li, Haoli Bai
**arXiv:** [arxiv.org/abs/2608.17393](https://arxiv.org/abs/2608.17393)
**Summary:** Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execution feedback. However, the native execution environments of these harnesses are inherently misaligned with policy-gradient training: environmental crashes and reward hacking corrupt outcome signals, while train-inference discrepancies decouple rollout behavior from policy updates.
**Trending because:** 19 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 8. Training Leaves Traces: Centered Residual Signatures for Language Model Lineage Verification
**Authors:** Aman Singh Thakur, Rayan Khoury
**arXiv:** [arxiv.org/abs/2608.14929](https://arxiv.org/abs/2608.14929)
**Summary:** Open-weight language models are fine-tuned, quantized, pruned, and merged, yet their provenance is often undocumented. We study data-free white-box lineage verification: can weights alone reveal whether two compatible model checkpoints share ancestry?
**Trending because:** 16 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 9. Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning
**Authors:** Jiawei Wang, Ke Rui, Yushen Zuo, Yichun Feng, Minglei Li
**arXiv:** [arxiv.org/abs/2608.18746](https://arxiv.org/abs/2608.18746)
**Summary:** JEPA-style latent world models can use Euclidean distance to a goal latent as the cost for model-predictive control (MPC). Strong decoding of task variables, however, does not guarantee that this particular cost ranks candidate action sequences by real task progress.
**Trending because:** 15 HuggingFace upvotes + resonating with current research priorities

---

### 10. Looped Language Models Improve Compositional Tool Calling
**Authors:** Andrei Cristian Popescu, Haitz Sáez de Ocáriz Borde, Pietro Liò
**arXiv:** [arxiv.org/abs/2608.18171](https://arxiv.org/abs/2608.18171)
**Summary:** Looped language models have shown promising results on reasoning benchmarks, yet their potential for agentic tool use remains largely unexplored. We study this question in compositional tool-calling settings, where models must coordinate multiple API calls, maintain intermediate state, and preserve dependencies across tool interactions.
**Trending because:** 15 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 11. MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding
**Authors:** Bonan Zhang, Shiyu Dong, Quan Hung Tran, Katharina Gschwind, Shuqi Yang, Sijia Chen, Adel Ahmadyan, Seungwhan Moon, Lu Zhang, Ahmed Kirmani, Babak Damavandi, Anuj Kumar
**arXiv:** [arxiv.org/abs/2608.17402](https://arxiv.org/abs/2608.17402)
**Summary:** Vision encoders are a critical component of vision-language models, and scaling their capacity effectively improves performance. However, dense scaling increases compute cost and inference latency.
**Trending because:** 13 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 12. Scaling Creative Writing Beyond Story-Centric Data with Attribute-Guided Genre Expansion
**Authors:** Hwan Chang, Yongil Kim, Heuiyeen Yeen, Yireun Kim, Jinsik Lee, Hwanhee Lee
**arXiv:** [arxiv.org/abs/2608.13947](https://arxiv.org/abs/2608.13947)
**Summary:** High-quality creative writing data for large language models (LLMs) remains dominated by story-centric data, limiting models' ability to follow the structural and functional conventions of diverse creative formats. We propose an attribute-guided genre expansion framework for scaling creative writing data beyond story generation.
**Trending because:** 13 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 13. FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents
**Authors:** Tianyou Wang, Chongyang Gao, Kezhen Chen, Chen Dong, Yinghao He, Donghan Li, Wangcheng Xu, Hongjiu Zhang, Chi Li
**arXiv:** [arxiv.org/abs/2608.18423](https://arxiv.org/abs/2608.18423)
**Summary:** Language model agents now execute bounded tasks reliably. Whether they can sustain effective decision-making over long horizons, where actions have cumulative consequences and the environment responds to their choices, remains largely unmeasured.
**Trending because:** 12 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 14. SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation
**Authors:** Bowen Jing, Mingxin Wang, Ruiyang Hao, Chenchen Ge, Hanwen Shen, Junjie He, Yang Cui, Yiming Hou, Weitao Zhou, Jiawei Wang, Minglei Li, Dandan Zhang, Ding Zhao, Houde Liu, Xiaofan Li, Si Liu, Ping Luo, Haibao Yu
**arXiv:** [arxiv.org/abs/2608.18701](https://arxiv.org/abs/2608.18701)
**Summary:** Physical interaction quality is central to deformable-object manipulation, yet most benchmarks evaluate task success alone. A policy may complete the task while allowing slip or causing excessive compression.
**Trending because:** 12 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 15. The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning
**Authors:** Anna Borisiuk, Andrey Savchenko, Alexander Panchenko, Elena Tutubalina
**arXiv:** [arxiv.org/abs/2608.14229](https://arxiv.org/abs/2608.14229)
**Summary:** Popular facts are memorised more deeply during pretraining and resist removal longer than rare ones, yet existing LLM unlearning methods apply uniform gradient pressure regardless of training-data frequency. We propose the AdaPop (Adaptive Popularity) method, which combines local token confidence with a per-fact popularity-dependent exponent derived from an external proxy (e.g., Wikidata sitelinks, LLM-as-Judge), and automates the forget-retain balance via a dual-ascent controller that adjusts the retain penalty each epoch.
**Trending because:** 11 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 16. SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution
**Authors:** Silin Chen, Han Li, Xiaodong Gu, Yuling Shi, Haibing Guan
**arXiv:** [arxiv.org/abs/2608.18933](https://arxiv.org/abs/2608.18933)
**Summary:** Large language model (LLM) based agents have demonstrated remarkable proficiency in automated software issue resolution, yet they often struggle to resolve issues in a specific repository because they lack project-specific knowledge. Existing self-evolving approaches acquire such knowledge from repository history or online repair trajectories, but they either depend on available historical issue-resolution signals or incur substantial per-issue test-time exploration cost.
**Trending because:** 9 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 17. MathForm: Scaling Mathematical Autoformalization with Knowledge Retrieval and Verification-Guided Refinement
**Authors:** Lushi Pu, Weiming Zhang, Xinheng Xie, Zixuan Fu, Bingxiang He, Hengyu Zhao, Hongya Lyu, Xin Li, Jie Zhou, Yudong Wang
**arXiv:** [arxiv.org/abs/2608.14221](https://arxiv.org/abs/2608.14221)
**Summary:** Autoformalization is commonly framed as translating natural-language mathematical statements into machine-verifiable formal languages such as Lean 4. However, faithful formalization requires more than translation.
**Trending because:** 7 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 18. Security Assessment of DeepSeek Harness with A.I.G: Evaluating Resistance to Indirect Prompt Injection
**Authors:** Zonghao Ying, Xiangfan Wu, Huiyu Wu, Xing Zheng, Huangsheng Cheng, Xiaorong Shi, Jing Guo
**arXiv:** [arxiv.org/abs/2608.16393](https://arxiv.org/abs/2608.16393)
**Summary:** We assess indirect prompt injection in DeepSeek Harness (DSH), using AI-Infra-Guard (A.I.G) to construct tests, deliver controlled taint, execute DSH, collect traces, and judge outcomes. The study covers 14,560 controlled executions over 16 indirect-content channels, text and file carrier modes, 35 payload objectives, one unmodified baseline, and 12 attack methods.
**Trending because:** 5 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 19. Cross-Model Memory Transfer via Target-Side Reader Adaptation
**Authors:** Mingyuan Li, Guangsheng Yu, Xu Wang, Shaoxiong Ji
**arXiv:** [arxiv.org/abs/2608.17050](https://arxiv.org/abs/2608.17050)
**Summary:** Methods for improving knowledge use in large language models typically fall into two regimes. Non-parametric retrieval offers flexible access to external knowledge, but adds retrieval latency, context overhead, and only shallow integration with the backbone.
**Trending because:** 4 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 20. Personalized Auto-Research: Towards a True AI Co-Scientist
**Authors:** Bo Ni, Franck Dernoncourt, Hongjie Chen, Yu Wang, Nesreen K. Ahmed, Zhengzhong Tu, Tyler Derr, Ryan A. Rossi
**arXiv:** [arxiv.org/abs/2608.14881](https://arxiv.org/abs/2608.14881)
**Summary:** AI co-scientists that generate hypotheses, retrieve related work, design experiments, execute code, and draft full papers are beginning to change how research is carried out. Despite this rapid progress, state-of-the-art systems remain researcher-agnostic: given a research goal, they optimize novelty, validity, or reviewer score while ignoring the individual scientist who will use the output.
**Trending because:** 4 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention
