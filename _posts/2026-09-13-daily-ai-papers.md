---
title: "Daily AI Papers — September 13, 2026"
date: 2026-09-13
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-13/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-agents
  - efficient-ai
  - multimodal-generation
---

### 1. MiniCPM4: Ultra-Efficient LLMs on End Devices
**Authors:** MiniCPM Team, Chaojun Xiao, Yuxuan Li, Xu Han, Yuzhuo Bai, Jie Cai, Haotian Chen, Wentong Chen, Xin Cong, Ganqu Cui, Ning Ding, Shengda Fan, Yewei Fang, Zixuan Fu, Wenyu Guan, Yitong Guan, Junshao Guo, Yufeng Han, Bingxiang He, Yuxiang Huang, Baoxi Ji, Cunliang Kong, Qiuzuo Li, Siyuan Li, Wenhao Li, Xin Li, Yanghao Li, Yishan Li, Zhen Li, Dan Liu, Biyuan Lin, Yankai Lin, Xiang Long, Quanyu Lu, Yaxi Lu, Peiyan Luo, Hongya Lyu, Litu Ou, Yinxu Pan, Lushi Pu, Zekai Qu, Qundong Shi, Zijun Song, Jiayuan Su, Zhou Su, Ao Sun, Xianghui Sun, Peijun Tang, Fangzheng Wang, Feng Wang, Shuo Wang, Yudong Wang, Zheng Wang, Yesai Wu, Zhenyu Xiao, Jie Xie, Zihao Xie, Xiaoyue Xu, Yukun Yan, Jiarui Yuan, Jinqian Zhang, Kaihuo Zhang, Lei Zhang, Linyue Zhang, Xueren Zhang, Yudi Zhang, Hengyu Zhao, Weilin Zhao, Weilun Zhao, Yuanqian Zhao, Zhi Zheng, Chuyue Zhou, Ge Zhou, Jie Zhou, Wei Zhou, Yanghao Zhou, Zihan Zhou, Zixuan Zhou, Zhiyuan Liu, Guoyang Zeng, Chao Jia, Dahai Li, Maosong Sun
**arXiv:** [arxiv.org/abs/2506.07900](https://arxiv.org/abs/2506.07900)
**Summary:** This paper introduces MiniCPM4, a highly efficient large language model (LLM) designed explicitly for end-side devices. We achieve this efficiency through systematic innovation in four key dimensions: model architecture, training data, training algorithms, and inference systems.
**Trending because:** 104 HuggingFace upvotes + targets practical, efficient LLM deployment on end devices

---

### 2. WideSeek-R1: Exploring Width Scaling for Broad Information Seeking via Multi-Agent Reinforcement Learning
**Authors:** Zelai Xu, Zhexuan Xu, Ruize Zhang, Chunyang Zhu, Shi Yu, Weilin Liu, Quanlu Zhang, Wenbo Ding, Chao Yu, Yu Wang
**arXiv:** [arxiv.org/abs/2602.04634](https://arxiv.org/abs/2602.04634)
**Summary:** Recent advancements in Large Language Models (LLMs) have largely focused on depth scaling, where a single agent solves long-horizon problems with multi-turn reasoning and tool use. However, as tasks grow broader, the key bottleneck shifts from individual competence to organizational capability.
**Trending because:** 101 HuggingFace upvotes + uses multi-agent reinforcement learning to scale broad information seeking

---

### 3. YuE: Scaling Open Foundation Models for Long-Form Music Generation
**Authors:** Ruibin Yuan, Hanfeng Lin, Shuyue Guo, Ge Zhang, Jiahao Pan, Yongyi Zang, Haohe Liu, Yiming Liang, Wenye Ma, Xingjian Du, Xinrun Du, Zhen Ye, Tianyu Zheng, Zhengxuan Jiang, Yinghao Ma, Minghao Liu, Zeyue Tian, Ziya Zhou, Liumeng Xue, Xingwei Qu, Yizhi Li, Shangda Wu, Tianhao Shen, Ziyang Ma, Jun Zhan, Chunhui Wang, Yatian Wang, Xiaowei Chi, Xinyue Zhang, Zhenzhu Yang, Xiangzhou Wang, Shansong Liu, Lingrui Mei, Peng Li, Junjie Wang, Jianwei Yu, Guojian Pang, Xu Li, Zihao Wang, Xiaohuan Zhou, Lijun Yu, Emmanouil Benetos, Yong Chen, Chenghua Lin, Xie Chen, Gus Xia, Zhaoxiang Zhang, Chao Zhang, Wenhu Chen, Xinyu Zhou, Xipeng Qiu, Roger Dannenberg, Jiaheng Liu, Jian Yang, Wenhao Huang, Wei Xue, Xu Tan, Yike Guo
**arXiv:** [arxiv.org/abs/2503.08638](https://arxiv.org/abs/2503.08638)
**Summary:** We tackle the task of long-form music generation--particularly the challenging \textbf{lyrics-to-song} problem--by introducing YuE, a family of open foundation models based on the LLaMA2 architecture. Specifically, YuE scales to trillions of tokens and generates up to five minutes of music while maintaining lyrical alignment, coherent musical structure, and engaging vocal melodies with appropriate accompaniment.
**Trending because:** 75 HuggingFace upvotes + scales an open foundation model to coherent long-form music generation

---

### 4. Efficient Memory Management for Large Language Model Serving with PagedAttention
**Authors:** Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, Ion Stoica
**arXiv:** [arxiv.org/abs/2309.06180](https://arxiv.org/abs/2309.06180)
**Summary:** High throughput serving of large language models (LLMs) requires batching sufficiently many requests at a time. However, existing systems struggle because the key-value cache (KV cache) memory for each request is huge and grows and shrinks dynamically.
**Trending because:** 69 HuggingFace upvotes + introduced PagedAttention for high-throughput LLM serving

---

### 5. AgentScope 1.0: A Developer-Centric Framework for Building Agentic Applications
**Authors:** Dawei Gao, Zitao Li, Yuexiang Xie, Weirui Kuang, Liuyi Yao, Bingchen Qian, Zhijian Ma, Yue Cui, Haohao Luo, Shen Li, Lu Yi, Yi Yu, Shiqi He, Zhiling Luo, Wenmeng Zhou, Zhicheng Zhang, Xuguang He, Ziqian Chen, Weikai Liao, Farruh Isakulovich Kushnazarov, Yaliang Li, Bolin Ding, Jingren Zhou
**arXiv:** [arxiv.org/abs/2508.16279](https://arxiv.org/abs/2508.16279)
**Summary:** Driven by rapid advancements of Large Language Models (LLMs), agents are empowered to combine intrinsic knowledge with dynamic tool use, greatly enhancing their capacity to address real-world tasks. In line with such an evolution, AgentScope introduces major improvements in a new version (1.0), towards comprehensively supporting flexible and efficient tool-based agent-environment interactions for building agentic applications.
**Trending because:** 68 HuggingFace upvotes + provides a developer-centric framework for production agentic applications

---

### 6. Very Large-Scale Multi-Agent Simulation in AgentScope
**Authors:** Xuchen Pan, Dawei Gao, Yuexiang Xie, Yushuo Chen, Zhewei Wei, Yaliang Li, Bolin Ding, Ji-Rong Wen, Jingren Zhou
**arXiv:** [arxiv.org/abs/2407.17789](https://arxiv.org/abs/2407.17789)
**Summary:** Recent advances in large language models (LLMs) have opened new avenues for applying multi-agent systems in very large-scale simulations. However, there remain several challenges when conducting multi-agent simulations with existing platforms, such as limited scalability and low efficiency, unsatisfied agent diversity, and effort-intensive management processes.
**Trending because:** 46 HuggingFace upvotes + addresses the scale and orchestration challenges of very large multi-agent simulations

---

### 7. HuggingFace's Transformers: State-of-the-art Natural Language Processing
**Authors:** Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, Alexander M. Rush
**arXiv:** [arxiv.org/abs/1910.03771](https://arxiv.org/abs/1910.03771)
**Summary:** Recent progress in natural language processing has been driven by advances in both model architecture and model pretraining. Transformer architectures have facilitated building higher-capacity models and pretraining has made it possible to effectively utilize this capacity for a wide variety of tasks.
**Trending because:** 29 HuggingFace upvotes + the foundational Transformers library paper is resurfacing in today’s feed

---

### 8. What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets
**Authors:** T. J. Barton, Chris Constantakis, Patti Hauseman, Annie Mous, Alaska Hoffman, Brian Bergeron, Hunter Goodreau
**arXiv:** [arxiv.org/abs/2609.05663](https://arxiv.org/abs/2609.05663)
**Summary:** We present a continuous, population-scale measurement record of autonomous language-model trading agents operating in production across two systems with one design lineage: DX Terminal Pro (3,505 user-funded vaults trading real ETH in Base memecoin markets for 21 days, February to March 2026) and the DXAP live alpha fleet (500 to 599 user-created agents all-history, 91 to 117 concurrently active, trading Hyperliquid perpetuals, June to August 2026). The record spans roughly six months, 7.5M single-model invocations with about 300K onchain actions, and a further 231,638 multi-tool turns producing 14,596 fills.
**Trending because:** 22 HuggingFace upvotes + reports a six-month population-scale record of production LLM trading agents

---

### 9. Open-Sora 2.0: Training a Commercial-Level Video Generation Model in $200k
**Authors:** Zangwei Zheng, Xiangyu Peng, Yuxuan Lou, Chenhui Shen, Tom Young, Xinying Guo, Binluo Wang, Hang Xu, Hongxin Liu, Mingyan Jiang, Wenjun Li, Yuhui Wang, Anbang Ye, Gang Ren, Qianran Ma, Wanying Liang, Xiang Lian, Xiwen Wu, Yuting Zhong, Zhuangyan Li, Chaoyu Gong, Guojun Lei, Leijun Cheng, Limin Zhang, Minghao Li, Ruijie Zhang, Silan Hu, Shijie Huang, Xiaokang Wang, Yuanheng Zhao, Yuqi Wang, Ziang Wei, Yang You
**arXiv:** [arxiv.org/abs/2503.09642](https://arxiv.org/abs/2503.09642)
**Summary:** Video generation models have achieved remarkable progress in the past year. The quality of AI video continues to improve, but at the cost of larger model size, increased data quantity, and greater demand for training compute.
**Trending because:** 20 HuggingFace upvotes + targets commercial-level video generation with a comparatively modest training budget

---

### 10. Composing Policy Gradients and Prompt Optimization for Language Model Programs
**Authors:** Noah Ziems, Dilara Soylu, Lakshya A Agrawal, Isaac Miller, Liheng Lai, Chen Qian, Kaiqiang Song, Meng Jiang, Dan Klein, Matei Zaharia, Karel D'Oosterlinck, Christopher Potts, Omar Khattab
**arXiv:** [arxiv.org/abs/2508.04660](https://arxiv.org/abs/2508.04660)
**Summary:** Group Relative Policy Optimization (GRPO) has proven to be an effective tool for post-training language models (LMs). However, AI systems are increasingly expressed as modular programs that mix together multiple LM calls with distinct prompt templates and other tools, and it is not clear how practitioners can best leverage online RL algorithms like GRPO to improve these systems.
**Trending because:** 7 HuggingFace upvotes + jointly optimizes policy gradients and prompts in modular language-model programs

---

### 11. Reference-Based Bias Detection in LLMs via Relative Representations of Hidden States
**Authors:** Marek Jeliński, Jan Dubiński, Maciej Chrabaszcz, Sebastian Cygert
**arXiv:** [arxiv.org/abs/2609.10060](https://arxiv.org/abs/2609.10060)
**Summary:** Existing bias auditing methods typically rely on model outputs, requiring costly benchmarks or judge models and potentially missing internal shifts that never appear in generated text. We propose a reference-based method that audits bias in hidden-state representations across related model variants, for example before and after fine-tuning.
**Trending because:** 4 HuggingFace upvotes + detects model bias through relative hidden-state representations

---

### 12. The Price of Sparsity: Sufficient Conditions for Sparse Recovery using Sparse and Sparsified Measurements
**Authors:** Youssef Chaabouni, David Gamarnik
**arXiv:** [arxiv.org/abs/2509.01809](https://arxiv.org/abs/2509.01809)
**Summary:** We consider the problem of support recovery for sparse binary signals from noisy linear measurements. For sparse Gaussian measurement matrices we identify sufficient conditions on the minimal sample size for maximum-likelihood recovery in the high-SNR regime $ds/p \to \infty$, where $p$ denotes the signal dimension, $s$ the number of non-zero components of the signal, and $d$ the expected number of non-zero components per row of measurement.
**Trending because:** 3 HuggingFace upvotes + sharpens theoretical guarantees for sparse recovery from sparse measurements

---

### 13. From Reweighting to Rewriting: Unlocking the Intervention Effects of Influential Samples in Training Data Attribution
**Authors:** Yuzhang Luo, Chenpeng Wang, Jianhui Chen, Liangming Pan
**arXiv:** [arxiv.org/abs/2609.02771](https://arxiv.org/abs/2609.02771)
**Summary:** Training data attribution (TDA) aims to identify training examples that shape model behavior, but its intervention value depends on both which examples are selected and how they are modified. Influence functions (IF) estimate behavioral changes under infinitesimal reweighting, yet IF-selected examples often show limited advantages over random selection under conventional weight-based interventions.
**Trending because:** 3 HuggingFace upvotes + turns training-data attribution from reweighting into direct rewriting interventions

---

### 14. MindTopo: Can Foundation Models Reason in Topological Space?
**Authors:** Yunfei Ge, Anbang Liu, Qineng Wang, Johnalbert Garnica, Jianwen Lyu, Zihan Wang, Reuben Tan, Jianfeng Gao, Ruohan Zhang, Yining Hong, Jiajun Wu, Manling Li
**arXiv:** [arxiv.org/abs/2609.11900](https://arxiv.org/abs/2609.11900)
**Summary:** Spatial reasoning depends not only on metric properties such as distance, angle, and shape, but also on topological relations that remain invariant under continuous deformation. Cognitive science identifies these relations as foundational to spatial understanding, yet foundation-model evaluations largely focus on metric or viewpoint-dependent relations.
**Trending because:** 0 HuggingFace upvotes + tests whether foundation models understand topology rather than only metric space

---

### 15. From Parameters to Answers: How LLMs Retrieve and Use Their Internal Knowledge
**Authors:** Wenkang Wei, Yuan Fang, Renhe Jiang, Hong Cheng, Xingtong Yu
**arXiv:** [arxiv.org/abs/2609.11859](https://arxiv.org/abs/2609.11859)
**Summary:** How does a language model's dependence on query-routing information and target knowledge change as it answers a question? We study this question through layerwise interventions on the hidden state at the end of the question.
**Trending because:** 0 HuggingFace upvotes + probes how LLMs retrieve and use internal knowledge across layers

---

### 16. A Unified Per-Token Gating Family for On-Policy Distillation: FKL/RKL Mixing with Multi-Channel and Bias Coefficients
**Authors:** Suwan Wu, Yumeng Lin, Pengcheng Yuan, Xiaolong Jiang
**arXiv:** [arxiv.org/abs/2609.11768](https://arxiv.org/abs/2609.11768)
**Summary:** Per-token gating of forward/reverse KL losses has become a standard technique for on-policy knowledge distillation (OPD), but existing methods such as EOPD (Jin et al., 2026) and ToDi (Jung et al., 2025) each fix a single gating signal and a single gating direction, and the two have never been compared directly. We introduce a four-coefficient parameterization lambda_t = sigma(a * h_t + b * u(x) + c + d * gap_t) in which direction-aligned proxies of EOPD and ToDi appear as one-dimensional (1D) restrictions, and which adds multi-channel composition and an explicit bias as further degrees of freedom.
**Trending because:** 0 HuggingFace upvotes + unifies per-token gating choices for on-policy knowledge distillation

---

### 17. When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making
**Authors:** Ken Chen, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge
**arXiv:** [arxiv.org/abs/2609.11709](https://arxiv.org/abs/2609.11709)
**Summary:** When multiple LLM agents yield conflicting answers, the decision-making process dictates whether agent diversity improves performance or merely compounds shared errors. Existing collective decision-making methods, including voting, electoral rules, and LLM judges, rely on forward reasoning: they map evidence to labels in one direction.
**Trending because:** 0 HuggingFace upvotes + offers a label-free Bayesian anchor for resolving disagreement among agents

---

### 18. RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety
**Authors:** Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser
**arXiv:** [arxiv.org/abs/2609.11758](https://arxiv.org/abs/2609.11758)
**Summary:** Allowing large language models (LLMs) to retrieve information from a set of trusted documents can increase reliability and reduce hallucination. However, recent work has demonstrated that retrieval-augmented generation (RAG) can have unintended side effects on the overall safety of the generated responses, when prompted for harmful or dangerous content.
**Trending because:** 0 HuggingFace upvotes + benchmarks safety failures introduced by retrieval-augmented generation

---

### 19. Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation
**Authors:** Jintao Zhang, Kai Jiang, Jintao Chen, Xu Wang, Deyuan Liu, Jungang Li, Dechuang Chen, Ming Lin, Jingjiang Zhou, Haopeng Jin, Qi Jia, Xiaohang Wang, Yaole Wang, Zhanqiang Zhang, Ran Li, Zhengkun Huang, Shuyue Xiong, Yuji Wang, Zikun Dai, Hui He, Yang Luo, Mang Ning, Weiqi Feng, Chengyang Ye, Xinyue Lin, Min Zhao, Hongzhou Zhu, Hengkai Tan, Zeyuan Wang, Chendong Xiang, Kaiwen Zheng, Zhijie Deng, Fan Bao, Jianfei Chen, Jun Zhu
**arXiv:** [arxiv.org/abs/2609.11638](https://arxiv.org/abs/2609.11638)
**Summary:** We present Vidu S2, which comprises Vidu S2-Avatar, a real-time interactive digital-character model, and Vidu S2-Editing, a real-time video editing model. Moreover, we explore the feasibility of real-time spatial video generation for both Vidu S2-Avatar and Vidu S2-Editing.
**Trending because:** 0 HuggingFace upvotes + pushes video generation toward real-time interaction, editing, and spatial output

---

### 20. Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification
**Authors:** Joshua Ong Jun Leang, Haonan Li, Zheng Zhao, Xinyi Shang, Wenda Li, Zhengzhong Liu, Erix Xing, Shay Cohen, Eleonora Giunchiglia
**arXiv:** [arxiv.org/abs/2609.11319](https://arxiv.org/abs/2609.11319)
**Summary:** Most of mathematical knowledge has been communicated through so-called informal use of mathematics and natural language. With large language models (LLMs) being highly adept in using natural language, they achieve strong performance, yet not perfect, in informal mathematical reasoning.
**Trending because:** 0 HuggingFace upvotes + connects informal mathematical reasoning with formal Lean verification
