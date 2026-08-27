---
title: "Daily AI Papers — August 27, 2026"
date: 2026-08-27
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-27/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-rl
  - video-generation
  - multimodal-reasoning
---

### 1. VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction
**Authors:** Zhifei Xie, Jiaqi Lang, Ze An, Yifan Zhao, Dongchao Yang, Kai Li, Ziyang Ma, Mingbao Lin, Chunyan Miao, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2608.26005](https://arxiv.org/abs/2608.26005)
**Summary:** Conversational systems, such as duplex speech language models (SLMs), still lack a streaming, accurate, and empathetic memory system as their soul. We introduce VoiceMem, a simple memory architecture with a parallel informational left brain, an emotional right brain, and streaming memory I/O mechanisms.
**Trending because:** 141 HuggingFace upvotes + a dual-brain streaming memory design for real-time speech agents

---
### 2. VGI-BENCH: Probing Visual Intelligence in Video Generation Models
**Authors:** Xuan He, Cong Wei, Yuhao Cheng, Linrui Ma, Yuxuan Zhang, Zuojun Li, Yuhao Wen, Zeyi Liu, Yuren Hao, Songcheng Cai, Keming Wu, Penghui Du, Kai Zou, Rui Yang, Chenkai Sun, Ke Yang, Ping Nie, Kelsey R Allen, Chenglong Wang, Michel Galley, Jianfeng Gao, ChengXiang Zhai
**arXiv:** [arxiv.org/abs/2608.19583](https://arxiv.org/abs/2608.19583)
**Summary:** Recent studies suggest that video generation models can exhibit certain forms of zero-shot visual reasoning through generated frames. Yet reliable evaluation remains challenging: benchmarks should adopt inputs aligned with the visual priors of current video models, require valid evolving processes rather than only plausible final states, and calibrate task difficulty to remain challenging yet partly feasible.
**Trending because:** 127 HuggingFace upvotes + a rigorous benchmark for zero-shot visual reasoning in video generators

---
### 3. FrontierChallenge: Evaluating Scientific Workflow Completion
**Authors:** Liangcai Su, Zhaopeng Feng, Zhuo Chen, Zhen Zhang, Xiang Lin, Ruilin Li, Handuo Zhang, Ning Wang, Kailong Wen, Yueqi Guo, Feng Xing, Yiling Guo, Chenxiong Qian, Simon Shaolei Du, Lidong Bing, Xinyu Wang
**arXiv:** [arxiv.org/abs/2608.24979](https://arxiv.org/abs/2608.24979)
**Summary:** Scientific agents increasingly analyze data, execute code, and produce research artifacts, yet most benchmarks emphasize final answers, isolated programs, or a single domain. We introduce FrontierChallenge, a cross-domain benchmark comprising 300 end-to-end scientific workflows.
**Trending because:** 124 HuggingFace upvotes + a 300-task cross-domain benchmark for end-to-end scientific agents

---
### 4. WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploration and Exploitation
**Authors:** Zihao Wu, Hongyao Tang, Yi Ma, Huizhong Song, Pengyi Li, Yifu Yuan, Fei Ni, Jinyi Liu, Wei Wei, Jianrong Wang, Yan Zheng, Jianye Hao
**arXiv:** [arxiv.org/abs/2608.24479](https://arxiv.org/abs/2608.24479)
**Summary:** Massively parallel simulation changes the data regime in which off-policy reinforcement learning (RL) is trained, challenging stabilizers designed for data-limited replay. Through controlled experiments across eight benchmark families, we show that these stabilizers are data-regime-dependent: parameter normalization helps with narrow replay coverage but restricts value fitting when data are abundant, while clipped double-Q can be relaxed in high-throughput manipulation.
**Trending because:** 106 HuggingFace upvotes + rethinking off-policy RL stabilizers for massively parallel simulation

---
### 5. JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution
**Authors:** Guibin Zhang, Leo Lu, Fangzhou Xie, Kang Zhu, Junhao Wang, Zhifei Xie, Zhaochen Yu, Zihang Liu, Zhongxiang Sun, Qiankun Li, Yue Liao, Heng Chang, Xiaobin Hu, Qibing Ren, Wangchunshu Zhou, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2608.25593](https://arxiv.org/abs/2608.25593)
**Summary:** Agent capability is not determined by the model alone. The agent harness, encompassing memory management, planning strategy, action protocol, and tool/skill orchestration, can dominate the contribution of the underlying foundation model.
**Trending because:** 47 HuggingFace upvotes + just-in-time evolution of the agent harness itself

---
### 6. VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning
**Authors:** Junxiang Xu, Ruisi Wang, Fanyi Pu, Maijunxian Wang, Ran Ji, Tongxi Zhou, Chenyang Gu, Jing Zuo, Hongcan Xiao, Yimeng Geng, Wanqi Yin, Wei Chen, Oscar Qian, Zhengan Yan, Ziqi Huang, Haiwen Diao, Liang Pan, Bo Li, Xiangyu Fan, Dezhi Luo, Fengyuan Yu, Zehong Zhao, Qingying Gao, Tinghui Zhu, Yilan Zhang, Jingqi Tong, Pinyuan Feng, Zhengze Jiang, Letian Wang, Ziyu Guo, Renrui Zhang, Jieneng Chen, Sonia Joseph, Constantin Venhoff, Saman Motamed, Mengyue Yang, Chandra Sripada, Alan Yuille, Philip Torr, Lvmin Zhang, Vikash Kumar, Daniel Khashabi, Nikolaus Kriegeskorte, Raphaël Millière, Vincent C. Müller, Anyi Rao, Quan Wang, Ziwei Liu, Dahua Lin, Lei Yang, Hokin Deng, Zhongang Cai
**arXiv:** [arxiv.org/abs/2608.26105](https://arxiv.org/abs/2608.26105)
**Summary:** Native visual reasoning treats visual generation as the medium of reasoning itself: visual states (i.e. images and videos) are not merely inputs to be understood or outputs to be rendered, but first-class substrates for problem solving beyond language.
**Trending because:** 40 HuggingFace upvotes + treating visual generation as a first-class reasoning medium

---
### 7. D^3-MOPD: Adaptive Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation
**Authors:** Zechen Sun, Zhiwei Zhang, Fei Zhao, Juntao Li, Mu Chuan, Huayu Deng, Guojian Zhan, Wenliang Chen, Yao Hu, Min Zhang
**arXiv:** [arxiv.org/abs/2608.24987](https://arxiv.org/abs/2608.24987)
**Summary:** Multi-teacher on-policy distillation (MOPD) distills several domain-expert teachers into a single student by minimizing per-domain reverse-KL divergence on the student's own rollouts. Existing approaches typically fix the per-domain data mixture before training, overlooking the fact that different domains converge at substantially different rates: some plateau early while others continue to improve throughout the training budget.
**Trending because:** 21 HuggingFace upvotes + adaptive per-domain scheduling for multi-teacher distillation

---
### 8. Agent-G^2: Gaussian Guidance for Agentic Reinforcement Learning
**Authors:** Zixuan Wang, Yanrui Miao, Zhengxi Lu, Teng Pan, Yiwen Qiu, Hongxing Li, Peng Qiu, Ruiqing Zhang, Yongliang Shen
**arXiv:** [arxiv.org/abs/2608.23318](https://arxiv.org/abs/2608.23318)
**Summary:** Hint-based reinforcement learning addresses reward sparsity in long-horizon agentic tasks by retaining a prefix of an expert trajectory before each rollout, letting the policy explore from a state closer to success. Its effectiveness hinges on the guidance depth: how much of the trajectory to keep.
**Trending because:** 20 HuggingFace upvotes + Gaussian-guided exploration depth for long-horizon agentic RL

---
### 9. Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies under no-CoT Data
**Authors:** Yinhao Tang, Youqing Fang, Yanan Sun, Jiangning Liu, Ziyi Wang, Xun Zhao, Weiming Zhang, Bin Liu, Kuikun Liu, Wenwei Zhang, Kai Chen
**arXiv:** [arxiv.org/abs/2608.23256](https://arxiv.org/abs/2608.23256)
**Summary:** Recent work proposes next-chunk reasoning RL for leveraging no-CoT data---corpora such as worked solutions and textbook derivations that contain reasoning-rich content but lack explicit chain-of-thought annotations. The method trains a model to generate implicit reasoning traces and rewards them by their ability to predict the next chunk of text.
**Trending because:** 19 HuggingFace upvotes + a critical re-examination of RL vs SFT on no-CoT data

---
### 10. Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds
**Authors:** Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li, Yaowei Li, Yuming Li, Yijun Liu, Xin Lu, Xiaoxiao Ma, Yanwen Ma, Yaofeng Su, Yilang Sun, Haoyu Wang, Zeyue Xue, Songchun Zhang, Junhao Zhuang
**arXiv:** [arxiv.org/abs/2608.23383](https://arxiv.org/abs/2608.23383)
**Summary:** Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts. We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants.
**Trending because:** 19 HuggingFace upvotes + unified audio-visual generation for persistent interactive worlds

---
### 11. Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation
**Authors:** Huan-ang Gao, Haohan Chi, Yong Yan, Shiyuan Feng, Hanlin Wu, Zheng Jiang, Bingxiang He, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
**arXiv:** [arxiv.org/abs/2608.19098](https://arxiv.org/abs/2608.19098)
**Summary:** Multi-teacher on-policy distillation (M-OPD) has emerged as a promising paradigm for consolidating domain-specialized reinforcement learning (RL) experts into a single generalist student via dense, token-level reward supervision. Despite its practical success, the optimization dynamics governing multi-teacher capability integration remain poorly understood, and open, rigorously reproducible recipes are conspicuously lacking.
**Trending because:** 17 HuggingFace upvotes + an open, reproducible recipe fixing capability imbalance in M-OPD

---
### 12. StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action Models
**Authors:** Zhe Liu, Jinghua Hou, Yuxiang Lu, Zhenya Yang, Xianzhe Fan, Junwei Luo, Junyi Li, Ruihua Han, Zhi Hou, Hengshuang Zhao
**arXiv:** [arxiv.org/abs/2608.26067](https://arxiv.org/abs/2608.26067)
**Summary:** Vision-Language-Action (VLA) models have demonstrated effectiveness in robot manipulation, yet state-of-the-art models such as pi0.5 operate under a single-frame paradigm, limiting their ability to retain past observations and develop precise spatial perception. In this paper, we propose StreamPI, a streaming multimodal temporal modeling framework that equips single-frame VLA with temporal reasoning capability without introducing any additional parameters.
**Trending because:** 15 HuggingFace upvotes + adding temporal reasoning to single-frame VLA models for free

---
### 13. Video-IFBench: Evaluating Instruction Following of Multimodal LLMs in Video Understanding Scenarios
**Authors:** Hongbo Liu, Peixian Chen, Sihan Liu, Peiyuan Zhang, Kai Zou, Dian Zheng, Xiaoxing Hu, Yuhao Dong, Mengdan Zhang, Yunhang Shen, Haoyu Cao, Wei Liu, Weibo Gu, Xing Sun, Shengjie Zhao
**arXiv:** [arxiv.org/abs/2608.25529](https://arxiv.org/abs/2608.25529)
**Summary:** Multimodal Large Language Models (MLLMs) have shown strong performance in video understanding. However, their ability to follow instructions in this domain remains under-explored.
**Trending because:** 14 HuggingFace upvotes + a dedicated benchmark for instruction following in video MLLMs

---
### 14. SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?
**Authors:** Deyao Hong, Yizhe Chi, Wenyi Li, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na
**arXiv:** [arxiv.org/abs/2608.23564](https://arxiv.org/abs/2608.23564)
**Summary:** Modern software systems accumulate technical debt over decades of development, which makes migration expensive and largely manual. As coding agents become increasingly capable at bug fixing, can they autonomously perform such migrations?
**Trending because:** 13 HuggingFace upvotes + testing coding agents on whole-repository stack migrations

---
### 15. Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments
**Authors:** Guo Gan, Yilun Zhao, Cong Chen, Jinbiao Wei, Tingyu Song, Zheyuan Yang, Lin Fu, Hong Zhou
**arXiv:** [arxiv.org/abs/2608.24099](https://arxiv.org/abs/2608.24099)
**Summary:** GUI agents often encounter dynamic anomalies when deployed on Android devices, from unexpected pop-ups to action misuse, yet existing benchmarks lack systematic evaluation of agent robustness against runtime anomalies. We introduce AnTrap, a comprehensive benchmark that injects dynamic perturbations into agent execution trajectories.
**Trending because:** 12 HuggingFace upvotes + stress-testing Android GUI agents against runtime anomalies

---
### 16. Code World Model: Coding Agent as World Brain
**Authors:** Yiwen Chen, Guosheng Lin, Chi Zhang
**arXiv:** [arxiv.org/abs/2608.25927](https://arxiv.org/abs/2608.25927)
**Summary:** World models aim to simulate how complex environments evolve under actions and events, yet existing video-based world models primarily learn dynamics from visual observations, which reveal outcomes rather than the underlying knowledge, rules, and mechanisms governing world evolution. This makes it difficult to maintain persistent consequences and support coherent, open-ended evolution.
**Trending because:** 12 HuggingFace upvotes + using code as the substrate for a persistent world model

---
### 17. The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents
**Authors:** Roy Ganz, Mor Shpigel Nacson, Adi Kalyanpur, Ron Litman
**arXiv:** [arxiv.org/abs/2608.24358](https://arxiv.org/abs/2608.24358)
**Summary:** Coding agents perform long-running tasks spanning dozens of model calls, tool uses, and code edits. As these runs unfold, users face a practical cost-quality trade-off: escalating to a stronger model when a cheaper one struggles, or downshifting once the hard reasoning is complete.
**Trending because:** 12 HuggingFace upvotes + quantifying the cost of switching models mid-trajectory

---
### 18. V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning
**Authors:** Shulin Tian, Minglun Li, Yuhao Dong, Hao Ding, Jiarui Yao, Haiwen Diao, Jingkang Yang, Hongyuan Zhu, Ziwei Liu
**arXiv:** [arxiv.org/abs/2608.25580](https://arxiv.org/abs/2608.25580)
**Summary:** Vision-language models can produce fluent answers that are insufficiently grounded in the visual evidence: a single unsupported object, chart value, or intermediate inference can undermine an otherwise plausible response. We argue that this is a credit-assignment failure in multimodal post-training.
**Trending because:** 12 HuggingFace upvotes + rubric-based RL to enforce visual faithfulness

---
### 19. Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation
**Authors:** Tianyi Xiong, Zhengyuan Yang, Xiaofei Wang, Chung-Ching Lin, Ruichun Ma, Kevin Lin, Zhendong Wang, Linjie Li, Chenxi Liu, Ruibo Chen, Ramani Duraiswami, Heng Huang, Lijuan Wang
**arXiv:** [arxiv.org/abs/2608.24138](https://arxiv.org/abs/2608.24138)
**Summary:** Large vision-language models have shown strong progress in UI-to-code generation, yet their test-time self-evolution remains unstable. We first identify a fundamental obstacle, termed visual repair coupling: a local code edit may propagate through layout, style, and component dependencies, correcting one visual mismatch while degrading regions that were previously faithful.
**Trending because:** 11 HuggingFace upvotes + stabilizing self-evolving UI-to-code generation with rubrics

---
### 20. LAION-BVD: A 10-Million-Hour Open Video Dataset for Multimodal Pre-training
**Authors:** Andreas Hochlehnert, Marianna Nezhurina, Mehdi Cherti, Andrej Radonjic, Thaddäus Wiedemer, Christoph Schuhmann, Romain Beaumont, Wieland Brendel, Bernhard Schölkopf, A. Sophia Koepke, Jenia Jitsev, Matthias Bethge
**arXiv:** [arxiv.org/abs/2608.24845](https://arxiv.org/abs/2608.24845)
**Summary:** We present LAION-BVD, a large-scale open video dataset for multimodal learning, which contains 1.3B platform-specific video URLs collected from CommonCrawl. From these, we download 80M videos with a total duration of 10 million hours.
**Trending because:** 10 HuggingFace upvotes + a 10-million-hour open video corpus for multimodal pretraining

---
