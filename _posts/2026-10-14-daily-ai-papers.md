---
title: "Daily AI Papers — October 14, 2026"
date: 2026-10-14
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-14/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - world-models
  - reinforcement-learning
---

### 1. VideoJev: System One Model for Video Understanding and Interaction
**Authors:** Zhu, Yuhan, Zeng, Xiangyu, Si, Qingyi, Yang, Chenxu, Li, Yifei, Qin, Luozheng, Zhou, Junhao, Yao, Dingyu, Zhang, Jun, Qin, Chuanyu, Zhang, Zhiqiu, Yang, Yuandong, Xu, Yuqi, Zhang, Tianyu, Guo, Hongcheng, Wang, Jiaqi, Duan, Nan, Wang, Limin
**arXiv:** [arxiv.org/abs/2610.18615](https://arxiv.org/abs/2610.18615)
**Summary:** VideoJev replaces autoregressive answer decoding with a shared scoring head that turns video evidence into temporal spans or answer choices while reusing visual computation across queries. Its 4B and 35B-A3B variants improve mean temporal-grounding mIoU by 6.7 and 10.8 points over their backbones, with 2.8–3.1-times grounding speedups and more than 100-times speedups on video QA.

---

### 2. Agent-Reflex: Teaching Language Agents to Act Reflectively
**Authors:** Dong, Guanting, Yang, Xinyu, Jin, Jiajie, Hu, Yuyang, Song, Xiaoshuai, Chen, Yifei, Li, Xiaoxi, Tan, Jiejun, Zhu, Yutao, Chua, Tat-Seng, Wen, Ji-Rong, Dou, Zhicheng
**arXiv:** [arxiv.org/abs/2610.17953](https://arxiv.org/abs/2610.17953)
**Summary:** Agent-Reflex combines reflection-skill discovery, reflective supervised fine-tuning, and on-policy reflective policy optimization to teach agents proactive recovery from noisy tools and user corrections. Built on Qwen3-8B, it reaches 58.6 overall on five long-horizon tool-use benchmarks and 29.1 on AgentNoiseBench while improving robustness to interaction noise.

---

### 3. Jeva: System One Models from First Principles
**Authors:** Li, Qi, Wang, Xinchao
**arXiv:** [arxiv.org/abs/2610.18773](https://arxiv.org/abs/2610.18773)
**Summary:** Jeva is a decision-native System One architecture designed to be null-aware, permutation-invariant, scalable to changing option sets, and cacheable across requests. It achieves strong typed-decision performance with near-perfect null detection, no decision flips under tested permutations, support for thousands of candidates, and lower latency through option reuse.

---

### 4. Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes
**Authors:** Wang, Yu, Dai, Rui, Chen, Wei, Wang, Yi, Dang, Bo, Liu, Kaikui, Chu, Xiangxiang, Li, Yansheng
**arXiv:** [arxiv.org/abs/2610.18356](https://arxiv.org/abs/2610.18356)
**Summary:** Urbex reframes city-scale 3D grounding as active spatial search, letting a vision-language agent query landmarks, zoom into regions, render oblique views, and commit a bounding box. Reinforcement learning on CityRefer yields the best Hit@1 and IoU, faster inference than the strongest ranking baseline, and improved zero-shot robustness on STPLS3D-Refer.

---

### 5. GreenWAM: A World Foundation Model for Robotics
**Authors:** Sidorov, Gennady, Kornilov, Valerii, Grankin, Denis, Fedotova, Polina, Postnikov, Aleksey
**arXiv:** [arxiv.org/abs/2610.18774](https://arxiv.org/abs/2610.18774)
**Summary:** GreenWAM unifies robot world modeling and control through a shared anatomical action space spanning 20 robot families, joint multimode training, and policies split from the generator. It posts top-tier world-prediction and control results, transfers to a real humanoid better than compared policies, and can be distilled into a real-time single-step controller.

---

### 6. AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards
**Authors:** Gao, Xin, Yang, Yifan, Li, Xin, Wang, Pan, Li, Yan, Tian, Muzhao, Cheng, Mingxi, Liu, Bei, Qiu, Kai, Dai, Qi, Chen, Dong, Dong, Yue, Tassiulas, Leandros, Ying, Rex, Li, Ji, Luo, Chong
**arXiv:** [arxiv.org/abs/2610.18860](https://arxiv.org/abs/2610.18860)
**Summary:** AesCode guides code generation with a reference image, represents the target as a design graph, and optimizes separate verifiable and visual reward channels. Its 8B and 32B models improve visual quality over same-scale Qwen3-VL baselines by 31.1 and 22.4 percentage points while retaining structured, editable, and verifiable outputs.

---

### 7. Harness^2: Recursive Agent Harnessing for an Open World
**Authors:** Xu, Ruiyao, Chen, Yanfei, CuiZhu, Zhongying, Mishra, Bhavana Dalvi, Ming, Yifei, Yu, Han, Han, Rujun, Lee, Chen-Yu, Pfister, Tomas
**arXiv:** [arxiv.org/abs/2610.14224](https://arxiv.org/abs/2610.14224)
**Summary:** Harness^2 recursively improves an agent's execution harness without ground-truth verifiers, then distills task-level edits into a continual harness for future tasks. One recursion step improves GLM-5 and Gemini 3.5 Flash across three professional benchmarks, with gains up to 11.5 points on WorkBuddy-Bench and 11.8 percentage points on LAB.

---

### 8. TPPO: Tracking-Value PPO For Language Model Reasoning
**Authors:** Wang, Futing, Li, Chenxi, Yan, Jianhao, Luo, Yun, Wang, Zhi, Li, Yizhuo, Zhan, Runzhe, Cheng, Yu, Lin, Tao
**arXiv:** [arxiv.org/abs/2610.16794](https://arxiv.org/abs/2610.16794)
**Summary:** TPPO models token-level value evolution as additive updates in log-odds space and reconstructs prefix values from cumulative position-wise outputs. It improves aggregate mathematical-reasoning scores over PPO by 7.0 points on Qwen3-4B-Base and 8.4 points on Qwen3-8B-Base, with gains extending to other models and tasks.

---

### 9. Vela: User Behavior as Supervision Sparks LLM Intelligence
**Authors:** Xiao, Yang, Sun, Yusong, Wu, Haoyi, Hui, Wenyang, Hang, Weiqiang, Wang, Luqing, Wang, Zejian, Tu, Zirui, Mao, Jingsheng, Hu, Shaobo, Luo, Yang, Guo, Jiale, Zhang, Jin, Liu, Yudan, Luo, Zhaokai, Huan, Ren, Hu, Yao, Jiang, Chengyue, Li, Wenjie, Mu, Chuan
**arXiv:** [arxiv.org/abs/2610.14709](https://arxiv.org/abs/2610.14709)
**Summary:** Vela converts anonymized long-term behavior from 100,000 users into tasks and trajectories that supervise preference, intent, and future-action inference. Fine-tuning Qwen3.6-35B-A3B improves user-related tasks by up to 11.5 points and general benchmarks by four points on average, with further gains from reinforcement learning.

---

### 10. DoSA: Dots Sparse Attention
**Authors:** Meng, Fanxu, Fang, Taosong
**arXiv:** [arxiv.org/abs/2610.13990](https://arxiv.org/abs/2610.13990)
**Summary:** DoSA preserves exact Top-K sparse-attention selection while conditionally avoiding full scoring for candidates that can be safely rejected. Its GPU implementation accelerates the complete indexer by up to 2.74 times and delivers time-to-first-token speedups up to 1.94 times on GLM-5.2 and 1.50 times on DeepSeek-V3.2.

---

### 11. X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning
**Authors:** Wang, Yi, Yuan, Zhenlong, Guo, Yuchan, Huang, Maolei, Song, Zijian, Zhang, Dapeng, Tan, Rongbin, Wang, Jiyuan, Wang, Zhiyuan, Lin, Fangfang, Song, Shuhan, Cao, Huawei
**arXiv:** [arxiv.org/abs/2610.16811](https://arxiv.org/abs/2610.16811)
**Summary:** X-Ragent learns when chest X-ray reasoning needs auxiliary evidence while validity-gating quantitative measurements so inapplicable values do not enter the diagnosis. After agentic supervised fine-tuning and GRPO, it achieves the strongest results on three benchmarks, including an 8.6-point gain on the fully held-out ChestAgentBench.

---

### 12. WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution
**Authors:** He, Hang, Wang, Linting, Liu, Guanming, Mao, Bo, Liu, Jinxiu, Suo, Yiran, Zhou, Maosen, Xi, Zhiheng, Dong, Guanting, Shao, Zhou, Zheng, Rui, Zhou, Jie, Wan, Chengcheng, Gui, Tao, Zhang, Qi, Qiu, Xipeng, Huang, Xuanjing
**arXiv:** [arxiv.org/abs/2610.18067](https://arxiv.org/abs/2610.18067)
**Summary:** WorkRover recursively evolves aligned work contexts, executable tasks, and evidence-grounded verifiers, using compatibility replay for repairs and verifier-to-turn credit for training. Its Qwen3.5-35B-A3B agent improves over the base model by 26.27 points on JobBench, 29.32 points on OfficeQA Pro, and 413.25 Elo on GDPval v2.

---

### 13. ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling
**Authors:** Peng, Xinge, Fang, Zhen, Wang, Ruibing, Lv, Yongxuan, Li, Haodong, Zhang, Guohui, Ma, Xiaoxiao, Lu, Yiting, Chen, Lin, Che, Zehui, Zhao, Feng
**arXiv:** [arxiv.org/abs/2610.15166](https://arxiv.org/abs/2610.15166)
**Summary:** ExeWorldBench evaluates whether coding agents can infer physical and causal structure and realize it as executable 3D worlds. Its three task levels span individual mechanisms, compositional systems, and intent-driven synthesis, revealing substantial limitations in frontier models' physically grounded and causally coherent world construction.

---

### 14. LeWAM: End-to-End World and Action Modeling with JEPAs
**Authors:** Fu, Minghao, Siebert, Tavis, Halicki, Eryk, Balestriero, Randall
**arXiv:** [arxiv.org/abs/2610.12818](https://arxiv.org/abs/2610.12818)
**Summary:** LeWAM jointly trains latent next-state prediction and action flow matching in an end-to-end JEPA that supports direct policy execution and sampled-action planning. It raises visual-planning success from 28.6% to 89.7% on contact-rich tasks and from 10.9% to 46.2% on long-horizon tasks while planning 32.3 times faster.

---

### 15. Scoring Higher, Answering Worse: Mitigating Reward Hacking in Rubric-Based RL via Protocol-Level Rubrics
**Authors:** Liu, Maoqi, He, Junwei, Zhang, Bowen, Li, Feiran, Ma, Wentao, Lin, Rongyi, Zhong, Shuhan, Fang, Quan
**arXiv:** [arxiv.org/abs/2609.38847](https://arxiv.org/abs/2609.38847)
**Summary:** This work shows that weighted-sum rubric rewards let policies compensate for missing crucial decisions with irrelevant checklist points, producing higher scores but worse clinical answers. Protocol-level Rubrics instead require grouped criteria to hold together, improving appropriateness by 10.8 points without sacrificing coverage and leading the seven-benchmark average at both tested scales.

---

### 16. Multics: Generative Multi-Player World Model with Hierarchical Communication
**Authors:** Huang, Kaiyi, Yu, Wangbo, Huang, Yukun, Yu, Jiwen, Liu, Kunhao, Yang, Donglin, Hu, Wenbo, Shan, Ying, Liu, Xihui
**arXiv:** [arxiv.org/abs/2610.17201](https://arxiv.org/abs/2610.17201)
**Summary:** Multics uses player-, group-, and global-level communication plus dynamic trajectory-based grouping to scale generative multi-player world models without fully connected attention. It achieves state-of-the-art results for four and six players and generalizes from four-player training to as many as ten players while reducing attention computation.

---

### 17. EviScene: Beyond "Is It AI?" for Agentic Image Factuality Assessment
**Authors:** Wang, ZiAn, Liu, Ruiqi, Zhang, Zhengbo, Han, Yi, Shen, Jialiang, Chen, Ruoxin, Cui, Manni, Zhu, Ximo, Jiang, Jin, Liu, Mingzhe, Wang, Linhao, Wang, Wenhao, Wu, Shu
**arXiv:** [arxiv.org/abs/2610.14609](https://arxiv.org/abs/2610.14609)
**Summary:** EviScene reframes image verification as evidence-grounded factuality assessment and introduces EviLens, a 10,174-image benchmark covering twelve factual error types. Its trained Qwen3.5-9B ReAct agent reaches 79.05% balanced accuracy and 52.26% strict evidence sufficiency, improving the base agent by 6.71 and 9.37 points.

---

### 18. UltraBERT: Beyond the Limit of BERT Pre-Training
**Authors:** Park, Jungwoo, Lee, Taewhoo, Kang, Jaewoo
**arXiv:** [arxiv.org/abs/2610.15028](https://arxiv.org/abs/2610.15028)
**Summary:** UltraBERT revisits bidirectional-encoder pretraining with separate language-model heads for low and high masking ratios and distillation restricted to the low-ratio path. The resulting single encoder reaches state of the art on both classification and retrieval, scoring 91.0 on GLUE and 47.7 on BEIR.

---

### 19. SALD: Self-Referenced Advantage Learning for Diffusion Models
**Authors:** Das, Aryan, Dey, Surjo, Biswas, Koushik, Roy, Swalpa Kumar, Abdar, Moloud, Bhattacharya, Arnab, Verma, Vinay Kumar
**arXiv:** [arxiv.org/abs/2610.01496](https://arxiv.org/abs/2610.01496)
**Summary:** SALD trains one diffusion model against its own behavior at two noise levels, using the easier path as a no-gradient reference and the harder path for optimization. Advantage-guided weighting, temporal advantage memory, and spectral decomposition improve generation quality across architectures and datasets without an external teacher, extra trainable parameters, or inference changes.

---

### 20. APEX: Asynchronous Prefix Denoising for Extreme Compression
**Authors:** Dinkevich, David, Chiprut, Nisan, HaCohen, Yoav, Lischinski, Dani
**arXiv:** [arxiv.org/abs/2610.12843](https://arxiv.org/abs/2610.12843)
**Summary:** APEX combines a hierarchical latent space with asynchronous denoising over channel groups so aggressive compression can preserve structure and detail without adding tokens. On ImageNet-512 it outperforms existing methods at every evaluated channel count under 64-times and 128-times compression and beats a 256-token model at matched training and sampling compute.

---
