---
title: "Daily AI Papers — October 26, 2026"
date: 2026-10-26
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-26/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - embodied-ai
  - multimodal-reasoning
---

### 1. UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents
**Authors:** Jujia Zhao, Jiakai Tang, Jing Yu, Wen Chen, Jian Wu, Han Zhu, Fei Sun, Suzan Verberne, Zhaochun Ren
**arXiv:** [arxiv.org/abs/2610.30932](https://arxiv.org/abs/2610.30932)
**Summary:** UserArena pairs 64,729 real e-commerce session trajectories from 11,010 users with an interactive shopping environment and five-level evaluation, including offline validation against a controlled production A/B test. Its On-Policy Trajectory Distillation method uses trajectory-level intent to supervise student rollouts, achieving the strongest fidelity among evaluated simulators and most closely reproducing the production policy effect.

---

### 2. HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games
**Authors:** Zecong Tang, Zian Guan, Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Bo Dai
**arXiv:** [arxiv.org/abs/2610.31162](https://arxiv.org/abs/2610.31162)
**Summary:** HiSTEVE combines a capability-aware planner, structured memory, and policy-coupled completion detection with one vision-language-action model that controls Minecraft through native keyboard-and-mouse inputs. Trained with world knowledge, imitation learning, and reinforcement learning, it reports 85.0% on MineStudio Bench, 37.4% average OpenHA success, and completion of long-horizon tasks such as crafting an iron pickaxe from scratch.

---

### 3. RSIHub: A Composable Framework for Agent-Evolution Methods
**Authors:** Zimu Wang, Xiaobo Wang, Siyu Ye, Jiaqi Li, Silin Chen, Yuling Shi, Ruobing Wang, Jingjing Zhang, Chaofan Wang, Kai Wu, Mengnan Qi, Kai Cai, Xiaodong Gu, Zilong Zheng
**arXiv:** [arxiv.org/abs/2610.32253](https://arxiv.org/abs/2610.32253)
**Summary:** RSIHub provides shared execution, evaluation, recovery, and lineage infrastructure for agent-evolution recipes that modify prompts, skills, tools, and orchestration while keeping evaluation outside the mutable surface. Implementations of AHE, Hyperagents, A-Evolve, and GEPA show a largest observed overall pass@1 gain of 13.5 percentage points, but rankings vary across settings and optimization gains do not always transfer to held-out tasks.

---

### 4. RynnUnify: Towards Unified Embodied Brain
**Authors:** Minghao Zhu, Bohan Hou, Kun Xiang, Zixuan Wang, Yinzhou Tang, Yifei Yang, Zhikai Wang, Tianyi Zhang, Kehan Li, Haoyu Zhao, Siteng Huang, Leigang Qu, Sicong Leng, Dongchi Huang, Mingxiu Chen, Shijian Lu, Yue Wang, Xiaodan Liang, Zhenyu Zeng, Deli Zhao, Chengju Liu, Jianfei Yang, Xin Li
**arXiv:** [arxiv.org/abs/2610.32965](https://arxiv.org/abs/2610.32965)
**Summary:** RynnUnify is a 16B embodied model that combines spatial reasoning, physical prediction, grounding, and long-horizon visual planning, with extensions for agentic video-based reasoning and robot control. It improves the Rynn-VP overall score by 9.75 points over Cosmos 3 Nano, while its world-action extension reports 51.5% success on 20 selected composite RoboCasa365 tasks and 46.7% average success across three real-robot tasks.

---

### 5. Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs
**Authors:** Zijian Liu, Chaoyou Fu, Yan Yang, Caifeng Shan, Ran He
**arXiv:** [arxiv.org/abs/2610.27103](https://arxiv.org/abs/2610.27103)
**Summary:** Omni-Woodpecker is a training-free hallucination-correction framework that detects audio-visual conflicts, separates grounding evidence from learned priors in hidden states, and rebalances those representations before decoding. With Qwen2.5-Omni-7B, it reports gains of 12.9 points on CMM and 8.6 on AVHBench, alongside smaller general-reasoning gains and transfer to VideoLLaMA2-AV.

---

### 6. Every Weight Is a Path of Shared Discrete Decisions
**Authors:** Ammar Ali, Stamatis Lefkimmiatis
**arXiv:** [arxiv.org/abs/2610.31931](https://arxiv.org/abs/2610.31931)
**Summary:** TWIG represents each neural-network weight as a path of shared discrete decisions, unifying pruning, quantization, low-rank factorization, codebooks, and weight sharing in one editable structure. On five language-model weight matrices, a flat signed-power-of-two tree requires 9-15% fewer additions than GPTQ at equal layer error on typical matrices and 20-55% fewer on matrices with strong outliers.

---

### 7. Dual Exam: Controlled Evaluation of Multimodal Agents and World Models
**Authors:** Zhefan Rao, Meng Chu, Xuan Zhang, Jingfan Chen, Guohao Cai, Runyi Li, Shiyi Du, Ning Lu, Xu Huang, Zhixuan Chen, Feng Nie, Harold Haodong Chen, Hanwen Wang, Wen-Jie Shu, Yajing Bai, Xianfeng Wu, Xuanhua He, Shuhan Guo, Ziyue Ma, Ruichuan An, Long Bai, Miaosen Chai, Wenhao Chai, Jingye Chen, Qi Chen, Xuhang Chen, Wei Chow, Minghao Fu, Yunhao Gou, Haokun Gui, Dong Huang, Wei Huang, Zi Cheng Huang, Haibo Jin, Lingdong Kong, Leung Chun Ho, Tianqin Li, Yanheng Li, Jiayuan Liu, Jiyang Liu, Mingyu Liu, Shaoteng Liu, Xiaocheng Lu, Yawen Luo, Zeyu Qin, Tiancheng Shen, Yueqi Song, Zhaolong Su, Hengkai Tan, Tianhao Tang, Yiran Tao, Juncheng Wang, Qinghe Wang, Shangshang Wang, Yingying Wang, Fang Wu, Tiange Xiang, Qiushi Yang, Weicai Ye, Weichen Yu, Jiarui Zhang, Jize Zhang, Liuzhou Zhang, Renrui Zhang, Sheng Zhang, Wenhu Zhang, Junru Zhao, Lingting Zhu, Yuxin Zuo, Yutong Bai, Long Chen, Yang Deng, Ziqi Huang, Yeying Jin, Weijia Li, Kevin Qinghong Lin, Quande Liu, See-Kiong Ng, Hongliang Ren, Hongru Wang, Shujun Wang, Qifeng Chen, Haoxuan Che
**arXiv:** [arxiv.org/abs/2610.31066](https://arxiv.org/abs/2610.31066)
**Summary:** Dual Exam evaluates multimodal agents under fixed environment responses and world models under fixed action interventions, separating action selection from state evolution across physical, digital, social, and scientific domains. Its agent track covers 1,088 items and its world-model track 400 cases, revealing uneven performance and state-preservation failures while a 150-case coupled pilot records zero task successes.

---

### 8. DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model
**Authors:** Zixian Gao, Lixin Xiu, Penghao Luo, Xiangcheng Cao, Ziqi Cai, Zhen Li, Erwin Wu, Kaipeng Zhang
**arXiv:** [arxiv.org/abs/2610.31734](https://arxiv.org/abs/2610.31734)
**Summary:** DirCast uses one streaming video-language model to select live esports camera views and generate commentary from past observations only, scanning all views at low resolution before reading the selected view at high resolution. On a dataset of 27 professional Dota 2 matches, it outperforms rule-based and zero-shot directors and wins 29.2% of commentary comparisons against GPT-4o under Proact-VL, versus 19.4% for the strongest compared streaming commentator.

---

### 9. TenetBench: A Clause-Anchored Russian Corpus for Evaluating Language Models against Professional Codes of Ethics
**Authors:** Yegor Anichkov, Valery Vinogradov, Andrey Furov, Marina Polukoshko, Sergey Bolovtsov
**arXiv:** [arxiv.org/abs/2610.29477](https://arxiv.org/abs/2610.29477)
**Summary:** TenetBench pairs 3,433 requests conflicting with clauses of fifteen Russian-language professional codes with benign counterparts, enabling evaluation tied to specific provisions rather than broad harm categories. In tests of fourteen model and reasoning-mode combinations, eleven produce conflicting content on most such requests, usually without warnings, while more conforming models decline conflicting requests and still serve legitimate counterparts.

---

### 10. On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models
**Authors:** Leon Sick, Lukas Hoyer, Yannick Strümpler, Christian Reisswig, Timo Ropinski, Federico Tombari
**arXiv:** [arxiv.org/abs/2610.32770](https://arxiv.org/abs/2610.32770)
**Summary:** On-Policy Self-Training uses only coarse topic descriptions to generate its own question-answer curriculum and privileged reasoning demonstrations, removing human-curated prompts, answers, and external task supervision from self-distillation. Experiments report consistent self-improvement across language benchmarks and visual question answering while retaining capabilities in domains not targeted by self-training.

---

### 11. FLOMSS: Generative Music Source Separation by Flow Matching
**Authors:** Shuyang Cui, Zhi Zhong, Keisuke Toyama, Koichi Saito, Qiyu Wu, Yukara Ikemiya, Junghyun Koo, Kin Wai Cheuk, Woosung Choi, Giorgio Fabbro, Wei-Hsiang Liao, Shusuke Takahashi, Yuki Mitsufuji
**arXiv:** [arxiv.org/abs/2610.17821](https://arxiv.org/abs/2610.17821)
**Summary:** FLOMSS systematically studies flow matching for full-band stereo separation into vocals, bass, drums, and other sources, comparing prediction targets, flow paths, source modeling, and mixture-consistency constraints. Evaluation on MUSDB18-HQ combines signal-level metrics, embedding-based metrics, and listening tests, with the proposed model showing competitive objective and subjective performance.

---

### 12. DraMaze: A Multi-Agent Pipeline with Future-Aware Memory for Diverse Microdrama Script Generation
**Authors:** Siyang He, Qiqi Wang, Fan Liu, Yuncheng Huang, Pengfei Xu, Xi Chen, Ziwei He, Xipeng Qiu
**arXiv:** [arxiv.org/abs/2610.32002](https://arxiv.org/abs/2610.32002)
**Summary:** DraMaze combines trope-memory-guided evolutionary search with a backward narrative dependency tree to preserve future-relevant history and diversify long-form microdrama plots. On 60-episode scripts of up to 60,000 words, it reduces causal-pattern repetition by 32.1% and reaches a Logic score of 82.5, exceeding the best-performing baseline by 8.5 points.

---

### 13. Building Auditable AI Text Detectors with Sparse Autoencoders
**Authors:** Liam Dugan, Callum McDougall, Matthew Denton, Philip Pham, Christine Kaeser-Chen, Chris Callison-Burch
**arXiv:** [arxiv.org/abs/2610.30006](https://arxiv.org/abs/2610.30006)
**Summary:** This pipeline trains sparse autoencoders on a fine-tuned AI-text detector, labels the resulting features, filters them by interpretation fidelity, and trains a lightweight classifier on human-readable concepts. The extracted features capture specific linguistic signals of generated text, and the resulting classifiers outperform the compared neural and stylometric alternatives on out-of-distribution texts.

---

### 14. MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation
**Authors:** Yuhan Sun, Jiaxin Zhao, Yongdong Luo, Yibo Hu, Meiguang Jin, Junfeng Ma, Weixun Wang, Weihang Pan, Zhongan Bi
**arXiv:** [arxiv.org/abs/2610.23234](https://arxiv.org/abs/2610.23234)
**Summary:** MultiAgent-OPD jointly trains a shared-parameter Leader-Searcher-Answerer team using reinforcement learning and a frozen teacher that supplies local token-level supervision for search and summary rollouts. Across seven datasets, it reaches 38.68% macro avg@4, exceeding Prompted Critic by 4.06 percentage points and C-MAS + RL by 2.61 percentage points.

---

### 15. MMVistaReason: Toward Open-Data and Post-Training Recipes for Multimodal Reasoning
**Authors:** Juekai Lin, Honglin Lin, Yuqian Yuan, Xiaolong Wu, Jie Cao, Liang Liang, Yunqi Cao, Yun Zhu, Wenqiao Zhang, Lijun Wu
**arXiv:** [arxiv.org/abs/2610.01352](https://arxiv.org/abs/2610.01352)
**Summary:** MMVistaReason combines systematic open-data construction with difficulty-aware supervision, specialized reinforcement-learning experts, and multi-teacher on-policy distillation to integrate multimodal reasoning capabilities. Across fifteen benchmarks, its 4B model averages 72.8 and its 9B model 74.4, with analyses showing that supervision choices and preferred distillation objectives depend on model capacity.

---

### 16. DuoLM: Fast and Effective Personalized Recommendation with Language Models
**Authors:** Jiang Wu, Yutong Song, Hongbo Wang, Guanghe Cao, Jeff Lei Liang
**arXiv:** [arxiv.org/abs/2610.24481](https://arxiv.org/abs/2610.24481)
**Summary:** DuoLM combines offline reusable item embeddings with a personalized ranker, trained through recommendation supervision and teacher distillation, plus a runtime using virtual token IDs, shared-history computation, and CUDA Graph replay. On a single H100, it reports approximately 26,400 candidate scores per second, about 60 times teacher throughput with vLLM and automatic prefix caching, while retaining comparable recommendation quality.

---

### 17. Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction
**Authors:** Ziang Zhang, Wenyou Yi, Zehan Wang, Jiachen Xu, Xintong Han, Chunchao Guo, Zhou Zhao
**arXiv:** [arxiv.org/abs/2610.32250](https://arxiv.org/abs/2610.32250)
**Summary:** Easy-3Dfy decouples single-image 3D object generation from scene-layout estimation, then aligns object-local meshes with partial scene pointmaps to compose the scene geometrically. Without complete scene-level supervision, it consistently outperforms SAM-3Dfy across multiple geometric metrics on Scene-Maker and 3D-FUTURE200.

---

### 18. Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding
**Authors:** Xin Zhang, Haochen Wang, Beibei Lin, Zhaoxiang Zhang, Robby T. Tan, Jason Li, Dacheng Tao
**arXiv:** [arxiv.org/abs/2610.29552](https://arxiv.org/abs/2610.29552)
**Summary:** Generalized CycleGRPO couples region description and localization through reconstruction-overlap rewards, extending self-evaluation across image regions, video intervals, and spatio-temporal evidence without reference captions or an external language-model judge during reinforcement learning. It raises SAMTok GroundingSuite overall gIoU from 57.5% to 68.2% and reports 51.9% tIoU on Charades and 33.3% temporal evidence coverage on the new DOVE benchmark.

---

### 19. Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models
**Authors:** Yufeng Liu, Bohao Fan, Juntu Zhao, Xinyi Wang, Hang Yu, Wenzhuan Luo, Yingzhi Wang, Qinghai Li, Yingdong Hu, Junliang Guo, Richard Wang, Dequan Wang, Yang Gao, Cheng Ma
**arXiv:** [arxiv.org/abs/2610.31569](https://arxiv.org/abs/2610.31569)
**Summary:** Echo adds stop and failure signals to each action chunk and denoises them jointly with robot actions, learning task status from successful, failed, and recovery trajectories without frame-level progress annotations. Faster signal denoising lets later action steps condition on cleaner status estimates, and real-world manipulation experiments show accurate status prediction and consistent policy improvements.

---

### 20. LoCA: Enabling Multi-Modality in Geospatial Location Encoders
**Authors:** Panagiotis Koromilas, Eleanna Vali, Diogenis Antonopoulos, Eleni Saka, Dimitris Christofis, Nikolaos Ioannis Bountos, Konstantin Klemmer, Ioannis Papoutsis, Yannis Panagakis, Mihalis A. Nicolaou
**arXiv:** [arxiv.org/abs/2610.32894](https://arxiv.org/abs/2610.32894)
**Summary:** LoCA addresses multimodal location encoding by first contrastively aligning Sentinel-1 and Sentinel-2 image encoders, then freezing them while training location and tabular-metadata projection adapters against a high-rank target. Across seventeen tasks and five compared state-of-the-art encoders, it achieves the most task wins and wins 68.8% of per-task comparisons.
