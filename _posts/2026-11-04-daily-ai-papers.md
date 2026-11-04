---
title: "Daily AI Papers — November 04, 2026"
date: 2026-11-04
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-04/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - video-generation
  - embodied-ai
---

### 1. Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems
**Authors:** Pengfei Zhou, Yixing Ma, Hexin Wang, Weidong Tang, Zhenglin Wan, Wangbo Zhao, Yang You
**arXiv:** [arxiv.org/abs/2611.05275](https://arxiv.org/abs/2611.05275)
**Summary:** Route Anything studies how to route tasks among specialized models and policies, using a unified quality-cost framework and a trajectory matrix spanning 25 benchmarks and 452 candidate configurations. The authors report that learned routing improves several task scores and raises efficiency by 8.82 times on average relative to their reference model.

---

### 2. Words Caught in the Heart: Simulating Person-Specific Expression for Self-Opaque Clients in Psychotherapy
**Authors:** Mengxi Xiao, Jingjing Chen, Ziyan Kuang, Jiarong Song, Wenhao Zhao, Zuchen Han, Yihuai Xu, Xiyang Huang, Jie Gong, Yuechen Jiang, Xueqing Peng, Yankai Chen, Xiaoyan Qu, Min Peng, Qianqian Xie
**arXiv:** [arxiv.org/abs/2611.00617](https://arxiv.org/abs/2611.00617)
**Summary:** Pandora simulates psychotherapy clients by updating psychological and relational states and separately planning expression to reflect each client's language and current self-understanding. Across 115 cases it outperforms five baselines on expression similarity and disclosure alignment, with a smaller evaluator study also finding fewer AI-like judgments.

---

### 3. Think Less, Locally: Local Preference Learning for Reasoning Compression
**Authors:** Muyao Yuan, Liyan Xu, Weizhan Zhang, Muyan Jiao, Jiangnan Li, Jinchao Zhang, Jie Zhou
**arXiv:** [arxiv.org/abs/2611.04814](https://arxiv.org/abs/2611.04814)
**Summary:** LoCo constructs local preference pairs by freezing overthinking states and generating shorter verified continuations, then uses DPO to teach reasoning models when to conclude. Math-only training reduces completion length by 41.7 to 45.4 percent on mathematics and 23.4 to 36.3 percent on code while maintaining or improving accuracy.

---

### 4. MoviEdit: Long-form Multi-Shot Video Editing Made Easy
**Authors:** Suhyeon Lee, Zhengang Li, Soo Ye Kim, Peihao Zhu, Jong Chul Ye, Chun-Hao Paul Huang, Duygu Ceylan, Yan Kang, Hyeonho Jeong
**arXiv:** [arxiv.org/abs/2611.02737](https://arxiv.org/abs/2611.02737)
**Summary:** MoviEdit combines automatically generated cross-shot editing supervision with a compressed bidirectional draft followed by autoregressive propagation and refinement for long-form video editing. Its 87,000 paired editing videos and MoviEdit-Bench support experiments reporting stronger results than existing open-source editors and performance comparable to evaluated industry frontier models.

---

### 5. Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling
**Authors:** Kling Team, Dong Chen, Jialu Chen, Xinlong Chen, Yifan Dai, Haotian Dong, Binzong Geng, Yushuo Guan, Minghui Guo, Guanlin He, Guanxiao He, Jingyun Hua, Yanwei Huang, Yiyan Ji, Xueping Jia, Yizhuo Jia, Bozhou Li, Jiaze Li, Min Li, Shihao Li, Shujie Li, Shengyi Liao, Weihong Lin, Shiyuan Liu, Xinyu Liu, Siyang Mao, Xiaoru Qu, Dianmo Sheng, Yang Shi, Jiafu Tang, Longxiang Tang, Yuqi Tang, Chengzhuo Tong, Kuo Wang, Qixun Wang, Rui Wang, Tianduo Wang, Yuran Wang, Zekun Wang, Zihao Wang, Boyang Xia, Yifan Xu, Liu Yang, Zhenlong Yuan, Bohan Zeng, Mujin Zhang, Yuanxing Zhang, Zhicheng Zhang, Zhuoran Zhang, Yuanhong Zheng, Kun Gai, Chengru Song, Pengfei Wan
**arXiv:** [arxiv.org/abs/2611.04916](https://arxiv.org/abs/2611.04916)
**Summary:** This Kling report argues that controllable video generation depends on multimodal understanding throughout data preparation, conditioning, alignment, and evaluation. It describes lessons from captioning, prompt enhancement, perceptually trained text encoders, reward models, and evaluations designed to expose scoring shortcuts.

---

### 6. DreamX: Video Diffusion Model is a Universal Latent Action Learner
**Authors:** Jisoo Kim, Chaehyun Kim, Junsu Kim, Jiho Park, Seongchan Kim, Eunbeen Hong, Soowon Son, Fu-En Yang, Seungryong Kim
**arXiv:** [arxiv.org/abs/2611.05377](https://arxiv.org/abs/2611.05377)
**Summary:** DreamX repurposes a pretrained video diffusion model to learn compact latent actions that separate action dynamics from visual appearance, compressing each latent frame from 1,200 to four tokens. The authors report leading latent-action-model results on LARY-Bench, cross-embodiment zero-shot action transfer, and lower-cost policy learning in the shared action space.

---

### 7. RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild
**Authors:** Tan Sang Nguyen, Yi Ru Wang, Shailesh Shailesh, Gang Yang, Jiamo Hu, Jianuo Jiang, Haoquan Fang, Zhongzheng Ren, Zhongyi Luo, Ian Chong, Aaron Tung, Santiago Pravisani, Minghui Lin, Yao Mo, Ishneet Singh, Benjamin Tee, Harold Soh, Siddhartha Srinivasa, Dieter Fox, David Hsu, Haoming Song, Maxime Ellerbach, Thomas Wolf, Pepijn Kooijmans, Ruijie He, Michael Cho, Jiafei Duan
**arXiv:** [arxiv.org/abs/2611.02497](https://arxiv.org/abs/2611.02497)
**Summary:** RoboColosseum standardizes distributed physical evaluation of robot policies across four embodiments, including blinded open-world comparisons and a matched-data fine-tuning track. Its 5,699 pairwise comparisons at 124 sites reveal weak agreement between embodiment-specific rankings, substantial post-fine-tuning rank reversals, and persistent difficulties completing open-world tasks.

---

### 8. Factorized MLLM Embeddings for Composed Image Retrieval
**Authors:** WonJun Moon, Seongchan Kim, Dahun Kim, Seungryong Kim
**arXiv:** [arxiv.org/abs/2611.05193](https://arxiv.org/abs/2611.05193)
**Summary:** FactEmbed separates understanding an image-plus-text modification query from constructing retrieval embeddings, using factorized latents and an intermediate target-imagination objective. Factor-level contrastive learning and distillation improve composed-image retrieval, while a shared forward pass provides both global retrieval embeddings and low-cost reranking features.

---

### 9. Axion 1.0: Open Agent Foundation Models, Simplified
**Authors:** Yuqi Jia, Yunjie Tian, Jiayu Zheng, Yijun Liang, Jingchen Sun, Mengyu Zhao, Di Fu
**arXiv:** [arxiv.org/abs/2611.03233](https://arxiv.org/abs/2611.03233)
**Summary:** Axion 1.0 is an open agent foundation model trained with two lightweight supervised fine-tuning stages followed by reinforcement learning, without dedicated mid-training, DPO, or on-policy distillation. The report describes competitive results across agentic benchmarks and releases the complete data-construction, verification, prompting, and training recipe alongside the weights.

---

### 10. ToolSpace: Scaling Tool-Centric Environment Synthesis for Long-Horizon Agents
**Authors:** Guanting Dong, Zhichao Sun, Xinyu Yang, Rui Wang, Xin Deng, Jiajie Jin, Zhixiong Yang, Junhao Huang, Han Han, Mingyu Ma, Xiaotao Wang, Yuyang Hu, Xiaoshuai Song, Xiaoxi Li, Jiejun Tan, Zhecan Wang, Shihan Dou, Honglin Guo, Zhiheng Xi, Tao Gui, Tao Ji, Qi Zhang, Yutao Zhu, Ji-Rong Wen, Zhicheng Dou
**arXiv:** [arxiv.org/abs/2611.05036](https://arxiv.org/abs/2611.05036)
**Summary:** ToolSpace synthesizes long-horizon agent environments from execution-witnessed tool dependencies, using state-aware walks, rollback, and replay checks to retain valid tasks. Across seven benchmarks, the authors report substantial tool-use gains after training and show that execution-grounded composition edges outperform LLM-judged ones.

---

### 11. YANAMI: A Large-Scale Multimodal Dataset and Benchmark for Multiturn Stateful Interaction
**Authors:** Shengyu Wang, Tengyue Nong, Junming Liu, Haosong Peng, Siyu Li, Ruiqi Lei, Fushuo Huo, Yuhao Pan, Yunfeng Fan, Ding Wang, Nan Cheng, Haozhao Wang, Wenchao Xu
**arXiv:** [arxiv.org/abs/2611.05280](https://arxiv.org/abs/2611.05280)
**Summary:** YANAMI introduces 400,000 multimodal dialogues and a 400-dialogue benchmark requiring models to track and revise state across image fusion, editing, world modeling, and visual reasoning. Fine-tuning BAGEL improves the evaluated editing, generation, and stateful-interaction tasks, while benchmark results expose gaps between understanding dialogue state and realizing it visually.

---

### 12. VidUEU-Agent: A Data-Curation Agent for Multimodal Understanding, Editing, and Unified Tasks
**Authors:** Tengju Ru, Weitong Lian, Zecong Tang, Lingyi Meng, Haoran Li, Zhejun Cui, Yichen Zhu, Hangshuo Cao, Qi Kang, Yechi Liu, Kaixuan Wang, Yu-Jie Yuan, Chunwei Wang, Yu Zhang, Bo Dai
**arXiv:** [arxiv.org/abs/2611.04418](https://arxiv.org/abs/2611.04418)
**Summary:** VidUEU-Agent converts raw video into multimodal instruction data through quality filtering, signal extraction, metadata construction, and task-specific synthesis. Its feedback-driven curation produces VidUEU-100K, whose use in fine-tuning yields consistent gains across the evaluated understanding, editing, and unified-task benchmarks.

---

### 13. EvoTeam: Multi-Agent Collaboration via Evolving Teams
**Authors:** Qinuo Cao, Xin He, Dianxuan Fu, Lizhi Zhang, Zhaoqing Xing, Jiapu Wang, Xin Wang, Na Zou, Yi Chang, Qinggang Zhang
**arXiv:** [arxiv.org/abs/2610.39813](https://arxiv.org/abs/2610.39813)
**Summary:** EvoTeam evolves team organization, interaction rules, and individual skills jointly rather than improving agents in isolation. It maintains reusable teams with context-compatible collaboration experience and reports improvements across four benchmarks.

---

### 14. WebHarbor: Docking Real Websites for Evolving GUI Agent Environments
**Authors:** Zhaoyang Wang, Qianhui Wu, Boyu Gou, Demi Wang, Jiacheng Zhang, Peichun Hua, Qize Li, Shi Qiu, Yifan Jiang, Yifan Zhang, Zexu Jin, Baolin Peng, Bolin Shen, Chetan Bansal, Dehan Kong, Deren Lei, Dongshen Peng, Fengqing Jiang, Hao Cheng, Haoqing Wang, Jiaming Shan, Jicheng Wang, Jingguang Zhou, Jixuan He, Kaide Zeng, Kangyu Zhu, Lama Moukheiber, Mufan Qiu, Peng Xia, Qihan Sun, Qingwei Lin, Qiushi Sun, Ruichen Zhang, Shuqing Luo, Si Qin, Sicheng Fan, Tao Xiong, Wenlin Yao, Xinyu Zhang, Xinyue Zeng, Xuanrui Li, Xuchao Zhang, Yian Wang, Yichao Liu, Yiming Liang, Yiyang Zhou, Yizhu Jiao, Yuetai Li, Yurun Chen, Yuxuan Zhang, Zheyuan Yang, Zhiyuan Yao, Zhongyang Li, Zihao Li, Zili Wang, Jianfeng Gao, Huaxiu Yao
**arXiv:** [arxiv.org/abs/2611.03634](https://arxiv.org/abs/2611.03634)
**Summary:** WebHarbor reconstructs 153 real-world website environments as deterministic, executable Docker deployments with 3,518 multi-step and post-authentication tasks. Human-agent collaboration audits fidelity and correctness, and reinforcement learning in these environments produces a small GUI agent that generalizes competitively across four evaluated benchmarks.

---

### 15. ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost
**Authors:** Xingzhi Qian, Sungho Park, Rongyuan Tan, Jianbo Yu, Jue Zhang, Lorenzo Cavallaro, Menglin Xia, Yanzhi Chen, Xinnuo Xu, Yu Kang, Xinran Zheng, Gagan Somashekar, Xuchao Zhang, Chetan Bansal, Qingwei Lin, Victor Rühle
**arXiv:** [arxiv.org/abs/2611.02079](https://arxiv.org/abs/2611.02079)
**Summary:** ParetoSaddler separates intermediate harness-candidate promotion from deployment selection and uses Bayesian bootstrap Pareto support to retain credible gains in quality or cost. On ClawMark and GAIA2, the authors report higher task quality with lower per-task cost than both initial harnesses and quality-only optimization.

---

### 16. History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models
**Authors:** Hangyi Kuang, Chengzhi Wang, Yefei He, Weijie Wang, Yuke Zhao, Zhuokun Chen, Zisu Huang, Yifan Yang, Xiaoxuan He, Feng Chen, Bohan Zhuang
**arXiv:** [arxiv.org/abs/2611.02782](https://arxiv.org/abs/2611.02782)
**Summary:** History Forcing distills few-step autoregressive video generators with corrected teacher targets that isolate information supplied by informative historical context. It improves long-video benchmark scores and reports more plausible scene evolution and object consistency when a camera returns to previously visible regions.

---

### 17. SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding
**Authors:** Kunjun Li, Wenhao Chai, Yihao Liang, Yuezhou Hu, Shuyao Xu, Yi Pan, William X. Zheng, Kannan Ramchandran, Kurt Keutzer, Jiantao Jiao
**arXiv:** [arxiv.org/abs/2611.02501](https://arxiv.org/abs/2611.02501)
**Summary:** SpecPilot uses cost modeling, parallel agent exploration, token-level equivalence checks, and persistent memory to discover deployment-specific speculative-decoding optimizations. Across the evaluated models and hardware, it raises speedup over autoregressive decoding from 4.46 to 10.87 times for one request and from 1.94 to 3.93 times with batching without reported training or quality loss.

---

### 18. MoLRSI: A Recursive Self-Improving AI agent for Molecular Discovery
**Authors:** Yikun Zhang, Xiwei Cheng, Mingze Yuan, Yu Zhang, Brian Shim, Aarti Krishnan, Daniel Rosen, Kunyang Sun, Yingze Wang, Zhenfeng Deng, Botao Yu, Bingxu Liu, David Liu, Tianyu Liu, Yuanqi Du, Nir Hacohen, James J. Collins, Wengong Jin
**arXiv:** [arxiv.org/abs/2610.39714](https://arxiv.org/abs/2610.39714)
**Summary:** MoLRSI combines workflow and model-architecture optimization with persistent cross-task memory to improve molecular-discovery search strategies. The authors report a 15.9 percent experimental antibiotic hit rate versus 8.7 percent for a prior expert-led workflow, plus eight experimentally validated peptide-MHC binding hits in a second discovery setting.

---

### 19. Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use From Evolved Harnesses
**Authors:** Xiaoyi Zhang, Haoqing Wang, Xinjie Zhang, Xiang Ming, Xing Wang, Senqiao Yang, Kaichen Zhang, Zhaoyang Jia, Andong Tan, Xinjiang Wang, Jinghao Guo, Yifei Shen, Xiao Li, Peng Zhang, Xun Guo, Jiahao Li, Shicheng Zheng, Jinglu Wang, Zongyu Guo, Wenxuan Xie, Bin Li, Yan Lu
**arXiv:** [arxiv.org/abs/2610.40747](https://arxiv.org/abs/2610.40747)
**Summary:** Mage-VL-Cowork trains a 4B policy to combine GUI interaction with terminal and code execution through a five-stage curriculum and evolved teacher harnesses. Its reusable task-generation workflows synthesize 293,806 desktop and web tasks, and the resulting model reaches a reported 66.0 percent on OSWorld-Verified.

---

### 20. "Shall We Approve?" Consequence-Aware Approval for Autonomous Coding Agents
**Authors:** Weiheng Wu, Junkai Chen, Zhensu Sun, Jieke Shi, Yunbo Lyu, David Lo
**arXiv:** [arxiv.org/abs/2610.40753](https://arxiv.org/abs/2610.40753)
**Summary:** Caper assesses coding-agent commands by pre-executing them in a snapshotted sandbox and giving an independent approver a bounded report of observed effects before committing or rolling back. It reports lower harmful-outcome rates than six compared systems on SABER and YoloFS-Ext while blocking only 1.0 percent of the latter benchmark's safe twin tasks.
