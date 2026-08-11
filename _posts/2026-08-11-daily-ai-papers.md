---
title: "Daily AI Papers — August 11, 2026"
date: 2026-08-11
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-11/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-coding
  - agent-memory
  - benchmarks
---

### 1. BDH-CQ: In-Context Learning with Recurrent Latent Reasoning
**Authors:** Björn Engdahl, Adrian Kosowski, Jan Chorowski, Zuzanna Stamirowska, Przemysław Uznański, Junlin Jiang, Rohan Phadke, Remigiusz Kinas, Richard Zhong
**arXiv:** [arxiv.org/abs/2608.09888](https://arxiv.org/abs/2608.09888)
**Summary:** We introduce BDH-CQ, a reasoning model that combines in-context learning with recurrent latent reasoning. Inputs presented at inference time continuously update the model's recurrent memory; the model then solves a query through iterative computation in a high-dimensional latent space, without verbalizing its intermediate reasoning.
**Trending because:** 161 HuggingFace upvotes + one of the most-upvoted papers in today's feed.

---

### 2. Macaron-V1: Towards Open Continual Learning with Self-Improvement and Mixture-of-LoRA
**Authors:** Mind Lab, Vin Bo, Asher Cai, Jingwei Cao, Song Cao, Vic Cao, Amelia Chen, Andrew Chen, Kaijie Chen, Cleon Cheng, Steven Chiang, Kaixuan Fan, Hera Feng, Huan Feng, Arthur Fu, Jun Gao, Pyke Han, Nolan Ho, Ori Hong, Hailee Hou, Piers Hua, Charles Huang, Miles Jiang, Nora Jiang, Yuyi Jiang, Qiuyu Jin, Fancy Kong, Kuss Koo, Jaron Lee, Andrew Lei, Alexy Li, Dawn Li, Lucian Li, Ray Li, Ricardo Li, Smith Li, Theo Li, Allen Lin, Elliot Lin, Fan Lin, Chen Ling, Kairus Liu, Kieran Liu, Logan Liu, Neo Liu, Xiang Liu, Yuxin Lu, Maeve Luo, Pony Ma, Verity Niu, Cole Qiao, Guian Qiu, Vince Qu, Sentry, Niko Song, Vincent Wang, Bo Wu, Rio Yang, Evelyn Ye, Fiona Ye, Ina Ye, Regis Ye, Josh Ying, Atlas Zeng, Danney Zeng, Salmon Zhan, Anya Zhang, Di Zhang, Mia Zhang, Sueky Zhang, Wei Zhao, Ada Zhou, Adrian Zhou, Yuhua Zhou, Juno Zhu, Murphy Zhuang
**arXiv:** [arxiv.org/abs/2608.09819](https://arxiv.org/abs/2608.09819)
**Summary:** Macaron-V1 is an open agent-model family for experiential intelligence: learning from experience in real environments and continuing to learn after deployment. It is organized around two system goals.
**Trending because:** 138 HuggingFace upvotes + one of the most-upvoted papers in today's feed.

---

### 3. SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring
**Authors:** Yuling Shi, Jinghan Xu, Kelin Fu, Wenhao Zeng, Shilin He, Lei Zhang, Yue Liu, Zelin Zhao, Terry Yue Zhuo, Jialun Cao, Siyu Ye, Tianyu Liu, Kai Cai, Shing-Chi Cheung, Xiaodong Gu
**arXiv:** [arxiv.org/abs/2608.09802](https://arxiv.org/abs/2608.09802)
**Summary:** As AI coding agents take on increasingly complex, long-horizon software engineering tasks, existing benchmarks are rapidly saturating and their evaluation quality has come under serious scrutiny: a recent audit found that nearly 60% of unsolved SWE-bench Verified instances contain flawed tests -- either overly narrow tests that reject correct solutions or overly broad tests that check unstated requirements -- and that frontier models can verbatim reproduce gold patches from training data. Code refactoring, which requires coordinated, behavior-preserving changes across many files, offers a substantially harder and more realistic test of agent capability, yet remains underserved by current benchmarks.
**Trending because:** 115 HuggingFace upvotes + one of the most-upvoted papers in today's feed.

---

### 4. Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution
**Authors:** Anton Razzhigaev, Andrei Gritsaev, Andrei Kaznacheev, Nikita Dragunov, Roman Yampolskiy, Andrei Kuznetsov
**arXiv:** [arxiv.org/abs/2608.08311](https://arxiv.org/abs/2608.08311)
**Summary:** We present Ouroboros, a self-developing agent harness whose tools, prompts, context assembly, and core implementation improve through reviewed commits that become the runtime for later work. Core evolution proceeds in two modes.
**Trending because:** 61 HuggingFace upvotes + one of the most-upvoted papers in today's feed.

---

### 5. Agent Memory Distillation: Empowering Small LLM Agents with Hierarchical Teacher Memory
**Authors:** Taeil Kim, Kangsan Kim, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2608.07169](https://arxiv.org/abs/2608.07169)
**Summary:** Memory systems have shown promise for improving agent performance, but their potential remains largely unexplored for small language models, which struggle to generate sufficient successful trajectories on their own. We propose Agent Memory Distillation (AMD), a training-free framework that transfers structured knowledge from a large teacher agent to a small student agent through hierarchical memory.
**Trending because:** 29 HuggingFace upvotes + one of the most-upvoted papers in today's feed.

---

### 6. Motif 3: Technical Report
**Authors:** Junghwan Lim, Joon Son Chung, Sungmin Lee, Wai Ting Cheung, Gihun Cho, Minsu Ha, Sangho Kang, Beomgyu Kim, Dongseok Kim, Jangwoong Kim, Taehyun Kim, Taewhan Kim, Jeesoo Lee, Jeongdoo Lee, Junhyeok Lee, Dongpin Oh, Hyeyeon Cho, Dahye Choi, Jaeheui Her, Hanbin Jung, Changjin Kang, Minjae Kim, Youngrok Kim, Hyukjin Kweon, Hongjoo Lee, Yeongjae Park, Bokki Ryu
**arXiv:** [arxiv.org/abs/2608.09119](https://arxiv.org/abs/2608.09119)
**Summary:** We introduce Motif 3, a decoder-only Mixture-of-Experts language model with 314 billion total parameters and 13.2 billion activated per token. Each sparse MoE layer contains 384 routed experts, with eight selected per token.
**Trending because:** 27 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 7. MatrAIx: Simulating the World with 8.3 Billion Persona Agents
**Authors:** Xiaomin Li, Yuexing Hao, Jianheng Hou, Jintao Huang, Qianfeng Wen, Shirley Huang, Yifan Liu, Xiaoyi Liu, Yilan Fan, Yijun Wang, Koutian Wu, Ruoqi Gao, Muhammad Ahmed Mohsin, Jing Tang, Brihi Joshi, Heming Liu, Zheyuan Deng, Zonglin Di, Sankalp Jajee, Jiuyao Lu, Zhiwei Zhang, Saksham Kapoor, Ishan Gupta, Yunhan Zhao, Chanwoo Park, Yucheng Lu, Bing Hu, Weihang Xiao, Aravind Mohan, Hanwen Xing, Runyu Zhang, Mihir Kulshreshtha, Yuanda Xu, Qianyu Zhu, Dianzhuo Wang, Yuxin Xiao, Bowen Jiang, Yongye Su, Wenhao Chai, Zuxin Liu, Lawrence Yunliang Chen, Xuandong Zhao, Ethan Ye, Shivam Patel, Jason Xie, Alex Martin Richmond, Weixiang Ding, Emre Okcular, Diya Mathew, Ziheng Wang, Rana M. Shahroz Khan, Zhejian Peng, Fang Wu, Fan Nie, Xinyang Han, Yubin Kim, Jiawei Zhang, Zhenting Qi, Huangyuan Su, Xu Pan, Abinitha Gourabathina, Hyewon Jeong, Hemanth Neelgund Ramesh, Kumail Alhamoud, Kimia Hamidieh, Zidi Xiong, Samuel Schmidgall, Pengrui Han, Yepeng Huang, Yongheng Wang, Bowen Yang, Alex Gu, Yuchu Wang, Akshay Paruchuri, Brenna Li, Hejie Cui, Jiayuan Ding, Chaosheng Dong, Jiahao Wang, Yixuan He, Chi Wang, Pamela Bhattacharya, Tianyi Peng, Paul Pu Liang, Mitchell Gordon, Yilun Du, Marinka Zitnik, James Zou, Prasanna Tambe, Philip Torr, Emily Fox, Asu Ozdaglar, Dawn Song
**arXiv:** [arxiv.org/abs/2608.04205](https://arxiv.org/abs/2608.04205)
**Summary:** Human evaluation of AI systems and digital products is costly, slow, and difficult to scale. Offline evaluations are more scalable but often abstract away human diversity and interactive behavior.
**Trending because:** 24 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 8. What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conversational Systems
**Authors:** Zhijing Zhang, Jinpeng Yu, Xin Song, Bingnan Li, Chuyue Li, Changhui Du, Xiaolin Fang, Jiaming Liu, Ruihua Huang
**arXiv:** [arxiv.org/abs/2608.07565](https://arxiv.org/abs/2608.07565)
**Summary:** Conversational assistants increasingly recommend follow-up edits to help users continue a task. Existing systems primarily target text-only interactions, leaving image-creation conversations underexplored.
**Trending because:** 22 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 9. Sci-VBench: Evaluating Knowledge- and Reasoning-Intensive Video Generation in Science Domains
**Authors:** Diandian Zhang, Tingyu Song, Lin Fu, Zheyuan Yang, Yilun Zhao
**arXiv:** [arxiv.org/abs/2608.09873](https://arxiv.org/abs/2608.09873)
**Summary:** We introduce Sci-VBench, a comprehensive benchmark for evaluating knowledge- and reasoning-intensive video generation across scientific domains. It contains 1,253 expert-annotated examples spanning 60 subjects across four core disciplines: Natural Science, Healthcare, Humanities & Social Sciences, and Engineering.
**Trending because:** 22 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 10. SPOT: Sparse Probing and Outcome Calibration for On-Policy Distillation
**Authors:** Zikun Qu, Min Zhang, Mingze Kong, Zhiwei Shang, Yikun Ban, Shuang Qiu, Zhongxiang Dai
**arXiv:** [arxiv.org/abs/2608.04419](https://arxiv.org/abs/2608.04419)
**Summary:** On-policy distillation (OPD) provides dense teacher supervision on student-generated trajectories, but standard reverse-KL training can assign insufficient probability to other plausible continuations. Teacher entropy alone does not reveal whether uncertainty is concentrated among a few plausible next tokens or dispersed over a long probability tail, nor whether the student already represents those candidates well.
**Trending because:** 16 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 11. DCAS: Decoupling CLI Agent Scaffolding to Internalize Planning across Scaffolds
**Authors:** Kishanthan Thangarajah, Boyuan Chen, Ahmed E. Hassan
**arXiv:** [arxiv.org/abs/2608.06113](https://arxiv.org/abs/2608.06113)
**Summary:** CLI-based software-engineering agents have matured rapidly, yet the open ecosystem has converged on a single training environment: trajectory datasets used to fine-tune open models are collected almost exclusively under OpenHands. Models fine-tuned on this data score well under OpenHands but degrade substantially when deployed under any non-training scaffold.
**Trending because:** 16 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 12. Stealing Reasoning Traces from Proprietary LLM APIs
**Authors:** Alexander Panfilov, David Schmotz, Ilia Shumailov, Luca Beurer-Kellner, Joachim Schaeffer, Ameya Prabhu, Jonas Geiping, Maksym Andriushchenko
**arXiv:** [arxiv.org/abs/2608.09867](https://arxiv.org/abs/2608.09867)
**Summary:** Leading large language model providers now conceal their models' step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as blocks of encrypted text, which the client passes back with each subsequent request.
**Trending because:** 16 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 13. OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching
**Authors:** Can Xiao, Sukmin Cho, Junbong We, Zhixiong Niu, Jianyi Cheng, Yiren Zhao, Youngjin Kwon, Yongqiang Xiong, Rui Ma, Junyi Liu
**arXiv:** [arxiv.org/abs/2608.08097](https://arxiv.org/abs/2608.08097)
**Summary:** Large language model (LLM) inference serving is increasingly constrained by memory rather than compute. As long-context and long-form reasoning workloads become more prevalent, the key-value (KV) cache dominates both memory footprint and memory traffic during LLM token generation, i.e., decode.
**Trending because:** 15 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 14. Scaling Inherently Interpretable Language Models
**Authors:** Guide Labs Team, Andreas Madsen, Aya Abdelsalam Ismail, Giang Nguyen, Isaac Plant, Muawiz Chaudhary, Nathaniel Monson, Saqib Azim, Zhichen Guo, Julius Adebayo
**arXiv:** [arxiv.org/abs/2608.07594](https://arxiv.org/abs/2608.07594)
**Summary:** Interpretability is often treated as a tax on capability: language models are trained as opaque systems, then explained after the fact, with methods whose reliability is difficult to establish. In this work, we challenge this premise.
**Trending because:** 11 HuggingFace upvotes + strong engagement in today's HuggingFace feed.

---

### 15. RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States
**Authors:** Yi Yang, Zhennan Chen, Yihong Zhuang, Tiehan Fan, Yinan Chen, Jian Li, Jian Yang, Ying Tai
**arXiv:** [arxiv.org/abs/2608.02508](https://arxiv.org/abs/2608.02508)
**Summary:** Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space.
**Trending because:** 9 HuggingFace upvotes + featured in today's HuggingFace papers feed.

---

### 16. Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection
**Authors:** Xuechao Zou, Shun Zhang, Kai Li, Yi Zhou, Xinyu Sun, Yuhui Chen, Zhe Wu, Congyan Lang, Junliang Xing
**arXiv:** [arxiv.org/abs/2608.06865](https://arxiv.org/abs/2608.06865)
**Summary:** The malicious use of generative artificial intelligence to create highly realistic deepfake videos raises serious ethical concerns and poses substantial challenges to AI safety. However, existing deepfake video benchmarks provide limited coverage of recent synthesis methods and generally lack reliable fine-grained textual annotations.
**Trending because:** 9 HuggingFace upvotes + featured in today's HuggingFace papers feed.

---

### 17. Evidence-RL: Towards Evidence-intensive Visual Reasoning
**Authors:** Haojie Huang, Xinlei Yu, Chengming Xu, Zhangquan Chen, Cheng Yang, Qingdong He, Yu Yang, Jiangning Zhang, Xiaobin Hu
**arXiv:** [arxiv.org/abs/2608.08021](https://arxiv.org/abs/2608.08021)
**Summary:** Vision-Language Models (VLMs) should answer from concrete image evidence rather than language priors, dataset shortcuts, or irrelevant visual context. Existing perception-aware post-training methods encourage image use through global perturbations or attention proxies, but they do not test whether a sampled answer causally depends on the local evidence that supports it.
**Trending because:** 8 HuggingFace upvotes + featured in today's HuggingFace papers feed.

---

### 18. Evo-Bench: Can Language Models Improve Agent Harness?
**Authors:** Lisheng Huang, Chen Yang, Hao Zhou, Huatong Song, Zongchao Chen, Ran Le, Yang Song, Wayne Xin Zhao, Tao Zhang
**arXiv:** [arxiv.org/abs/2608.09096](https://arxiv.org/abs/2608.09096)
**Summary:** Large Language Models (LLMs) have driven rapid progress in autonomous agents, yet standard evaluations remain confined to static task solving. An emerging frontier is harness evolution---the agent's capacity to autonomously optimize its own operating harness.
**Trending because:** 8 HuggingFace upvotes + featured in today's HuggingFace papers feed.

---

### 19. DuplexGen: Adaptive Synthesis of Human-AI Turn-Taking Dialogues
**Authors:** Takyoung Kim, Kang-wook Kim, Sang Hoon Woo, Julia Hirschberg, Gunhee Kim, Dilek Hakkani-Tür
**arXiv:** [arxiv.org/abs/2607.26178](https://arxiv.org/abs/2607.26178)
**Summary:** Turn-taking is a central component of full-duplex interaction. Which turn-taking behaviors are appropriate varies with the scenario, yet current models apply a single norm regardless of context.
**Trending because:** 7 HuggingFace upvotes + featured in today's HuggingFace papers feed.

---

### 20. A^2E : An End-to-End Agent Auditing Engine
**Authors:** Haoning Wang, Mingxun Zhang, Chenyue Yu, Yingjun Shang, Xia Hu, Guanchu Wang, Na Zou
**arXiv:** [arxiv.org/abs/2608.07346](https://arxiv.org/abs/2608.07346)
**Summary:** With the rapid advancement of large language models (LLMs), harnesses have become essential infrastructure for deploying agents across a wide range of domains. The fast-evolving harness ecosystem has also made rigorous capability evaluation increasingly important.
**Trending because:** 6 HuggingFace upvotes + featured in today's HuggingFace papers feed.
