---
title: "Daily AI Papers — September 30, 2026"
date: 2026-09-30
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-30/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - multimodal-memory
  - embodied-ai
---

### 1. Raven: The Harness of Harnesses for Composable Agentic Intelligence
**Authors:** EverMind AI
**arXiv:** [arxiv.org/abs/2609.33439](https://arxiv.org/abs/2609.33439)
**Summary:** Raven is an open-source multi-agent ecosystem that automatically constructs, improves, and orchestrates modular model-harness pairs for long-horizon work across domains. Its Host Agent, persistent archive, EverOS, and Skill Forge coordinate specialized agents and reuse experience, while experiments show stronger performance than evaluated state-of-the-art agent systems on complex tasks.

---

### 2. In-Context Learning for Robots: Methods and Applications
**Authors:** Haojian Huang, Zexi Li, Junhao Guo, Yehang Zhang, Wenxuan Peng, Bohan Zhou, Weilin Ruan, Leyi Wu, Chenxu Wang, Jianchong Su, Binghui Xie, Wosong Chen, Yingjie Xu, Tianhao Zhou, Suzeyu Chen, Pukun Zhao, Jiaqi He, Xinyi Li, Runze Li, Peiran Dong, Shaoxiang Dang, Jing Huang, Yingbing Chen, Yifan Chang, Tianyi Zhang, Shiyuan Deng, Haozhi Wang, Yangkai Wei, Wenqian Li, Han Yang, Kaiwen Zhou, Huaping Liu, James Cheng, Rui Shao, Donglin Wang, Yaochu Jin, Jianye Hao, Ying-Cong Chen, Yinchuan Li
**arXiv:** [arxiv.org/abs/2609.36012](https://arxiv.org/abs/2609.36012)
**Summary:** This survey organizes robot in-context learning into context-conditioned policies, geometric demonstration transfer, world-model-based control, and skill- or agent-based execution. It compares how these interfaces use demonstrations, interaction, correspondence, and memory to transfer taught behavior across changing objects, environments, and execution conditions.

---

### 3. MaLiang-Harness: A Programmable Path to Image and Video Generation
**Authors:** Haoyu Zhao, Zihao Zhang, Xudong Wang, Jiaxi Gu, Zuxuan Wu, Yu-Gang Jiang, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2609.34309](https://arxiv.org/abs/2609.34309)
**Summary:** MaLiang-Harness addresses the gap between runnable visual programs and outputs that actually satisfy requested composition, appearance, and motion by preserving executable state, traceable revisions, and verification against the current rendering. Across its image and video benchmarks, the best evaluated model reaches 100% generation success but lower all-threshold visual quality, exposing limits that general capability scores do not predict.

---

### 4. Omni-IO Skills: Harnessing Your Agent Omni-Native
**Authors:** Yanlin Li, Mingyang Hao, Shengqiong Wu, Hao Fei, Mong-Li Lee, Wynne Hsu
**arXiv:** [arxiv.org/abs/2609.31847](https://arxiv.org/abs/2609.31847)
**Summary:** Omni-IO Skills gives existing agents a plug-and-play harness for coordinating text, images, audio, video, documents, 3D assets, and code through hierarchical skills, execution graphs, and a persistent asset registry. Its 27 skills cover 38 tasks, raising two frontier agents' input-support rates to 100% and substantially improving coupled semantic-quality scores without changing their reasoning cores.

---

### 5. VoxMem: Benchmarking Multimodal Memory in Large Audio Language Models
**Authors:** Yang Xiao, Vidhyasaharan Sethu, Eun-Jung Holden, Ting Dang
**arXiv:** [arxiv.org/abs/2609.32607](https://arxiv.org/abs/2609.32607)
**Summary:** VoxMem benchmarks whether large audio language models remember not only words but also speaker identity, paralinguistic cues, environmental sounds, and evolving information across sessions. Its 3,196 instances span 34,743 spoken sessions and four memory operations, with no evaluated model exceeding 40% at a 32K context budget.

---

### 6. PanoVLN: Towards Effective Panoramic Vision-and-Language Navigation
**Authors:** Zhen Wang, Changpeng Wang, Zhe Liu, Zhangyang Qi, Yuxiang Lu, Zimo Zeng, Donglian Qi, Xi Chen
**arXiv:** [arxiv.org/abs/2609.34759](https://arxiv.org/abs/2609.34759)
**Summary:** PanoVLN combines longer action prediction, confidence-guided execution, branch-rich training routes, and joint semantic-geometric panorama features to exploit wide visual context for navigation. With a 4B RGB-only backbone, it improves success rates over the previous state of the art by 11.9% on R2R-CE and 8.7% on RxR-CE Val-Unseen, while also reducing pauses on a real quadruped.

---

### 7. LEGO-Anything: Coding Agents for 3D Scene Reconstruction
**Authors:** Xirui Li, Peng Shi, Mingwen Dong, Sheng Zhang, Zhuoyan Xu, Dongkyu Lee, Shuaichen Chang, Yi Xiang, Lin Pan, Jiarong Jiang
**arXiv:** [arxiv.org/abs/2609.36380](https://arxiv.org/abs/2609.36380)
**Summary:** LEGO-Anything uses a coding agent to iteratively write, execute, inspect, and revise Blender programs that reconstruct editable 3D scenes from single images. Its 208-image LEGO-Bench reveals large geometry and appearance gaps, while a training-free construction plugin improves all six evaluated models by as much as 62.7% relative overall.

---

### 8. What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling
**Authors:** Renping Zhou, Zanlin Ni, Zihao Fan, Guohao Fu, Zeyu Liu, Hao Shi, Jie Zhang, Chi Bene Chen, Yang Yue, Xueyang Fu, Gao Huang
**arXiv:** [arxiv.org/abs/2609.34981](https://arxiv.org/abs/2609.34981)
**Summary:** Controlled comparisons show that world action models lose their generalization advantage when the action expert cannot condition on future representations, even if in-distribution performance remains similar. Simple-WAM preserves the useful first denoising-step signal with one forward pass over fully noised video tokens, outperforming explicit models on generalization at efficiency comparable to latent variants.

---

### 9. SAKI: Maximal-Coupling-Routed Teacher Supervision for On-Policy Distillation
**Authors:** Miteto Wei, Xiaohan Wang, Zehao Chen, Jiajun Chai, Sichao Liu, Li Wang, Haoyuan Xu, Zhaoyu Hu, Wei Lin, Guojun Yin
**arXiv:** [arxiv.org/abs/2609.36601](https://arxiv.org/abs/2609.36601)
**Summary:** SAKI guides weak students with KL-constrained teacher rollouts and maximal coupling, routing reverse-KL supervision to accepted tokens and direct teacher supervision to corrections. An engine-resident verifier improves matched-workload rollout throughput by 4.22 times, and the method beats its teacher-guided baseline across seven mathematical reasoning benchmarks for 1.7B and 0.6B students.

---

### 10. Think Before You Score: Thinking Reward Model for Visual Generation
**Authors:** Xuehai Bai, Zhenchen Tang, Yang Shi, Dianyi Wang, Tengfei Liu, Wanshun Su, Xuanyu Zhu, Ruohui Wang, Haiwen Diao, Haotian Wang, Xiaoling Gu, Yuanxing Zhang
**arXiv:** [arxiv.org/abs/2609.37372](https://arxiv.org/abs/2609.37372)
**Summary:** The Thinking Reward Model first creates a case-specific rubric, then uses it to assess visual outputs and issue fine-grained pointwise rewards instead of immediately predicting one score. Paired with PD-GRPO to avoid score polarization, it leads open-source reward models on image generation and editing benchmarks and supplies effective reinforcement-learning signals to multiple generators.

---

### 11. Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies
**Authors:** Hui Ren, Lei Fan, Henry Pao, Han Guo, Zeeshan Zia, Ying Chen, Alexander Schwing, Gang Hua
**arXiv:** [arxiv.org/abs/2609.38155](https://arxiv.org/abs/2609.38155)
**Summary:** Grounded Entity Biographies links visually grounded observations of the same physical object across long-video clips, making each entity's history retrievable alongside episodic evidence. Across four benchmarks it improves long-video question answering, reaching 72.0% on EgoLifeQA, 4.4 percentage points above the best published result.

---

### 12. Beyond Dyadic Memory: Interaction-Aware Multimodal Memory with Adaptive Agentic Retrieval for Multi-Party Spoken Conversations
**Authors:** Wenxu Jia, Xize Cheng, Zihan Zhang, Dongjie Fu, Linjun Li, Wenshi Chen, Yangyang Wu, Tao Jin
**arXiv:** [arxiv.org/abs/2609.32522](https://arxiv.org/abs/2609.32522)
**Summary:** VoxPolyMem combines incremental speaker identification with interaction memories, facts, participant profiles, and an agent that adaptively chooses queries, tools, and memory layers for multi-party spoken conversations. It scores 85.0 on the new VoxPolyBench, beating the strongest evaluated baseline by 23.6 points and also outperforming public memory baselines on two existing benchmarks.

---

### 13. LLMs are General Asynchronous Agents
**Authors:** George Yakushev, Denis Mazur, Vladimir Bartenev, Vyacheslav Zhdanovskiy, Timofey Byzov, Vladimir Kaurkin, Vadim Pastushenko
**arXiv:** [arxiv.org/abs/2609.35427](https://arxiv.org/abs/2609.35427)
**Summary:** This work generalizes asynchronous agents through user- or agent-defined inference coroutines whose memory states can overlap while new inputs and tasks arrive. The framework demonstrates untrained asynchronous operation with Qwen 3.x models on streaming video understanding, video games, and monitoring.

---

### 14. Follow the Entities: A Corpus Map for Agentic Search
**Authors:** Soyeong Jeong, Sujay Kumar Jauhar, Sung Ju Hwang, Andrew Joohun Nam
**arXiv:** [arxiv.org/abs/2609.37226](https://arxiv.org/abs/2609.37226)
**Summary:** CorpusMap builds reusable entity pages that aggregate information and links across a document collection, letting search agents navigate relationships instead of rediscovering them for every query. Experiments with seven models on three datasets improve evidence discovery and answer quality while using fewer tokens than raw-corpus search and outperforming four alternative navigation layers.

---

### 15. EngiWorld: What Can Frontier Agents Deliver in Professional Engineering Environments?
**Authors:** Hongcheng Gao, Hailong Qu, Yu Lei, Henghui Sun, Haoyang Li, Yipeng Wei, Naihao Xue, Xiaohan Yu, Zhuo Tao, Yihe Zang, Yajiao Wang, Jingyi Tang, Yi Li, Jingjing Zhou, Jie Luo, Bohan Zeng, Chengyu Shen, Hao Jiang, Chong Chen, Bowen Qu, Olive Huang, Zeqiang Wang
**arXiv:** [arxiv.org/abs/2609.37686](https://arxiv.org/abs/2609.37686)
**Summary:** EngiWorld introduces 1,301 expert-curated tasks across six engineering domains and 26 professional software platforms, covering complete workflows through both GUI and CLI interfaces. Artifact-centric verifiers check geometry, physical feasibility, and rule compliance, revealing that the strongest of seven frontier models reaches only 44.3 EngiScore and succeeds on 3.6% of multi-software attempts.

---

### 16. Periodic Weak Spots: Phase Sensitivity from Chunked KV-Cache Compression
**Authors:** Xingyu Zhu, Pu, Yi, Ziheng Cheng, Ang Lv, Jing Liu, Lexing Ying, Yiyuan Ma, Xin Dong
**arXiv:** [arxiv.org/abs/2609.36322](https://arxiv.org/abs/2609.36322)
**Summary:** Chunked KV-cache compression creates phase sensitivity, where retrieval depends on a token's position relative to compression-window boundaries and can vary by up to 40 percentage points. Controlled pretraining and causal interventions identify phase-specialized attention components, showing why average long-context scores can hide periodic positional failures.

---

### 17. OmniTaskonomy: When Does Visual Generation Improve Visual Understanding?
**Authors:** Jiaxin Ge, Yiming Qin, Ji Xie, Haozhe Jiang, Xiaochuang Han, Junyi Zhang, Andrew Dai, Yinfei Yang, Jitendra Malik, Ranjay Krishna, Sewon Min, Haiwen Feng, Le Xue, Baifeng Shi, Trevor Darrell, XuDong Wang
**arXiv:** [arxiv.org/abs/2609.38079](https://arxiv.org/abs/2609.38079)
**Summary:** OmniTaskonomy maps transfer between 19 image-generation tasks and 25 visual-understanding capabilities using controlled image-to-image and image-to-text task pairs. Generation supervision improves understanding selectively, and stronger gradient alignment predicts larger gains, providing a basis for choosing useful multimodal training curricula.

---

### 18. LongCat-DeepResearch Technical Report
**Authors:** Meituan LongCat Team, He Zhu, Yue Xu, Wanli Wu, Haolin Ren, Yuxin Bian, Jiarui Zhao, Rongzhi Zhang, Quanchi Weng, Jinghao Cui, Yu Fan, Yuhan Liu, Yunhu Ye, Jiyuan Ren, Fengcheng Yuan, Zhao Yang, Jiacheng Zhang, Yuchuan Dai, Ruixuan Xiao, Haozhe Sun, Xiangyuan Liu, Cheng Sun, Yao Du, Yiming Hao, Hongbo Guo, Shuo He, Lei Wang, Xunliang Cai, Yan Chen, Fan Yang, Lingchuan Liu
**arXiv:** [arxiv.org/abs/2609.36071](https://arxiv.org/abs/2609.36071)
**Summary:** LongCat-DeepResearch separates global planning from parallel section-level investigation, then uses global review to target local revisions instead of repeatedly rewriting complete reports. The system reaches 55.25 on DeepResearchBench, 51.35 on DeepResearchBench II, and 79.83 on ResearchRubrics, with analyses supporting multiple planning perspectives and additional editing.

---

### 19. Learning Beyond What You Sample: Off-Policy-Aware Cross-Model Trajectory Exchange for RLVR
**Authors:** Doohyuk Jang, Yoonsik Park, Gyouk Chu, Sihwan Park, Eunho Yang
**arXiv:** [arxiv.org/abs/2609.37868](https://arxiv.org/abs/2609.37868)
**Summary:** GRAFT replaces all-fail RLVR rollout groups with peer-model trajectories, transferring successes and failures while controlling off-policy mismatch through sequence weights and token-level clipping. Across three heterogeneous model pairs and five math benchmarks, it improves both models by 2.1 points on average at the same per-model rollout budget, with most gains retained using stored trajectories.

---

### 20. Anisotropic Representations Improve Planning in JEPA World Models
**Authors:** Mingu Kang, Yoori Oh, Sookyung Kim, Joonseok Lee
**arXiv:** [arxiv.org/abs/2609.37441](https://arxiv.org/abs/2609.37441)
**Summary:** AnisoWM replaces isotropic Gaussian representation regularization with a learnable diagonal covariance constrained to fixed trace and anisotropy, while leaving prediction and Euclidean planning unchanged. The induced geometry better aligns latent distance with task outcomes and improves planning success over LeWorldModel in all four evaluated visual-control environments.
