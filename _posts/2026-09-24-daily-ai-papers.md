---
title: "Daily AI Papers — September 24, 2026"
date: 2026-09-24
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-24/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-memory
  - embodied-ai
  - video-generation
---

### 1. SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue
**Authors:** Haobo Zheng, Tan Tang, Yan Chen, Weijie Wang, Yingcai Wu
**arXiv:** [arxiv.org/abs/2609.26780](https://arxiv.org/abs/2609.26780)
**Summary:** SpeakerMem-R1 stores both speaker-labeled verbatim messages and structured person- and group-level states, then retrieves evidence by entity, event, and time for multi-party dialogue. Its locally deployable Writer-R1 raised memory-construction accuracy and produced leading results on GroupMemBench, SocialMemBench, EverMemBench, and LoCoMo.

---

### 2. Spatial-Interactor: Learning Spatial Reasoning through Interaction with the Observable Physical World
**Authors:** Kaixiang Yao, Xu Wang, Miao Pan, Hu Xiyue, Weishi Wang, Daniel Dahlmeier, Jintao Chen, Yongliang Shen, Xuhong Zhang, Wenqi Zhang
**arXiv:** [arxiv.org/abs/2609.23038](https://arxiv.org/abs/2609.23038)
**Summary:** Spatial-Interactor teaches vision-language models to track physical state changes through a three-level curriculum spanning passive transitions, self-motion, and long-horizon interaction. Training on the 108,000-example LSI dataset with supervised fine-tuning and on-policy distillation consistently improved local transition modeling and long-horizon spatial integration.

---

### 3. HappyWorld-Bench
**Authors:** Zhiqi Bai, Junai Cai, Yixin Chen, Jingrun Du, Tao Feng, Wei Gong, Siyuan Huang, Xiao Lin, Jiaheng Liu, Jun Luo, Yongzhe Lyu, Liya Ma, Zenan Meng, Lin Qu, Wenbo Su, Jiaming Wang, Qinghe Wang, Shaofei Wang, Yanghai Wang, Zequn Wang, Ziming Wang, Hu Wei, Jiangtao Wu, Ruiqi Wu, Jiaxin Xie, Yuchi Xu, Ze Xu, Chengting Yu, Liangyu Yuan, Gang Zeng, Yawen Zeng, Xingyao Zhang, Zizheng Zhang, Bo Zheng, Jiancheng Zhu, Song-Chun Zhu
**arXiv:** [arxiv.org/abs/2609.24308](https://arxiv.org/abs/2609.24308)
**Summary:** HappyWorld-Bench evaluates generated worlds across video, spatial, and embodied tracks, covering construction, exploration, interaction, and modification with human Elo ratings and automated metrics. Tests of 31 systems exposed persistent failures in long rollouts, spatial editing, and maintaining state across multi-step actions.

---

### 4. The Past Frames the Future: Memory for Autoregressive Video Generation
**Authors:** Harold Haodong Chen, Rongjin Guo, Disen Lan, Wen-Jie Shu, Hongfei Zhang, Hanzhe Hu, Shengtao Yao, Zixin Zhang, Guibin Zhang, Zhefan Rao, Jinxiu Liu, Yexin Liu, Rui Peng, Yuhao Liu, Bin Ren, Shuai Yang, Yukang Chen, Salman Khan, Ying-Cong Chen, Ser-Nam Lim, Rynson W. H. Lau, Nicu Sebe, Yu Cheng, Ming-Hsuan Yang, Qifeng Chen
**arXiv:** [arxiv.org/abs/2609.28466](https://arxiv.org/abs/2609.28466)
**Summary:** This review defines memory in autoregressive video generation as historical information that survives beyond a bounded active context and still shapes future frames. It organizes prior work by memory forms, functions, operations, learning, and evaluation, then identifies open problems in resource-aware architectures, reliable state updates, self-rollout learning, and standardized tests.

---

### 5. Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents
**Authors:** Yefan Zhou, Yang Li, Zeyu Leo Liu, Semih Yavuz, Shafiq Joty
**arXiv:** [arxiv.org/abs/2609.27334](https://arxiv.org/abs/2609.27334)
**Summary:** Just-in-Time Memory keeps raw agent trajectories and defers curation until read time, allowing the current task to determine a compact, relevant memory payload. It outperformed learned and heuristic write-time memory methods by up to 16.3 absolute success-rate points across ALFWorld, WebShop, and tau2-bench.

---

### 6. RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling
**Authors:** Zhenchen Tang, Yang Li, Songlin Yang, Bo Peng, Xiaotong Zhao, Shuai Li, Haotian Fan, Alan Zhao, Jing Dong
**arXiv:** [arxiv.org/abs/2609.22947](https://arxiv.org/abs/2609.22947)
**Summary:** RewardVerse inserts dynamically generated rubrics between a video-quality query and its scorer to prevent unstable scalar drift in reward models. Its two-stage Rubric-Guided Policy Optimization procedure achieved state-of-the-art pointwise and pairwise evaluation while producing more stable and interpretable rewards for video-generation RL.

---

### 7. PACT: From Credit Assignment to Critic Alignment
**Authors:** Jiayan Fu, Hang Xu, Yong Zhang, Zhaokai Luo, Yao Hu, Dongyan Zhao, Mu Chuan
**arXiv:** [arxiv.org/abs/2609.26355](https://arxiv.org/abs/2609.26355)
**Summary:** PACT derives a unique notion of token-level credit from completeness, prefix consistency, and neutrality, connecting that credit to common language-model reinforcement-learning signals. Its actor-then-critic update better aligns critic training with the updated policy, reaching 72.87% average accuracy on four math benchmarks and 67.4% on SWE-bench Verified.

---

### 8. Schrödinger's Code Repository: Have LLMs Learned SWE-bench or Memorized It?
**Authors:** Silin Chen, Yufei Yang, Xiaodong Gu, Yuling Shi, Chengcheng Wan, Haibing Guan
**arXiv:** [arxiv.org/abs/2609.27891](https://arxiv.org/abs/2609.27891)
**Summary:** SchrodingerRepo dynamically transforms benchmark repositories while preserving behavior, removing familiar names, layouts, and implementation patterns that coding agents may have memorized. Performance fell and exploration costs rose across SWE-bench Verified and SWE-QA, indicating that current agents partly rely on repository-side cues rather than robust repository reasoning.

---

### 9. PackLab: A Comprehensive Framework for Developing, Training, and Evaluating MLLMs in Robotic Bin Packing
**Authors:** Donghao Zhou, Jia-Hui Pan, Fan Zhang, Xingyuan Bu, Shilong Li, Xiaojie Gao, Yun-Hui Liu, Chi-Wing Fu, Pheng-Ann Heng
**arXiv:** [arxiv.org/abs/2609.23784](https://arxiv.org/abs/2609.23784)
**Summary:** PackLab combines a physics simulator, a packing-specialized multimodal model, and a standardized benchmark for closed-loop robotic bin packing. PackLab-VLM tracks evolving object and container state to select objects and placements, outperforming geometric heuristics, reinforcement-learning methods, and general-purpose multimodal models across configurations.

---

### 10. GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer Compression
**Authors:** Baher Mohammad, Ammar Ali, Stamatios Lefkimmiatis
**arXiv:** [arxiv.org/abs/2609.25963](https://arxiv.org/abs/2609.25963)
**Summary:** GeoPair is a training-free transformer-compression method that pairs structurally compatible projections across layers and factorizes them with a shared dictionary that preserves each layer's activation geometry. Combined with structured sparsity, it outperformed independent decompositions and heuristic pairings across multiple architectures, scales, and modalities.

---

### 11. MemBodied: Recurrent Associative Memory for Vision-Language-Action Models
**Authors:** Tej Deep Pala, Navonil Majumder, Bryce Goh, Raphael Yee, Jianfei Yang, Liming Chen, Soujanya Poria
**arXiv:** [arxiv.org/abs/2609.28256](https://arxiv.org/abs/2609.28256)
**Summary:** MemBodied gives vision-language-action models a fixed-size episodic memory composed of a recurrent associative state and an anchor for the initial scene. Across memory-dependent manipulation tasks it achieved 7.81 times the success rate of a stateless policy and beat the strongest memory baseline with 10 times fewer added parameters.

---

### 12. WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents
**Authors:** Jingjie Ning, Xueqi Li, Yibo Kong, Dongting Li
**arXiv:** [arxiv.org/abs/2609.27490](https://arxiv.org/abs/2609.27490)
**Summary:** WhatWorkedBench measures whether AI research agents can infer how component changes affect experimental outcomes after a limited measurement budget. Across 36 tasks, Gaussian-process modeling and code-equivalence information substantially improved recovery of true component effects and selection of strong configurations.

---

### 13. Hunyuan-A13B Technical Report
**Authors:** Tencent Hunyuan Team, Ao Liu, Botong Zhou, Can Xu, Chayse Zhou, ChenChen Zhang, Chengcheng Xu, Chenhao Wang, Decheng Wu, Dengpeng Wu, Dian Jiao, Dong Du, Dong Wang, Feng Zhang, Fengzong Lian, Guanghui Xu, Guanwei Zhang, Hai Wang, Haipeng Luo, Han Hu, Huilin Xu, Jiajia Wu, Jianchen Zhu, Jianfeng Yan, Jiaqi Zhu, Jihong Zhang, Jinbao Xue, Jun Xia, Junqiang Zheng, Kai Liu, Kai Zhang, Kai Zheng, Kejiao Li, Keyao Wang, Lan Jiang, Lixin Liu, Lulu Wu, Mengyuan Huang, Peijie Yu, Peiqi Wang, Qian Wang, Qianbiao Xiang, Qibin Liu, Qingfeng Sun, Richard Guo, Ruobing Xie, Saiyong Yang, Shaohua Chen, Shihui Hu, Shuai Li, Shuaipeng Li, Shuang Chen, Suncong Zheng, Tao Yang, Tian Zhang, Tinghao Yu, Weidong Han, Weijie Liu, Weijin Zhou, Weikang Wang, Wesleye Chen, Xiao Feng, Xiaoqin Ren, Xingwu Sun, Xiong Kuang, Xuemeng Huang, Xun Cao, Yanfeng Chen, Yang Du, Zhen Yang, Yangyu Tao, Yaping Deng, Yi Shen, Yigeng Hong, Yiqi Chen
**arXiv:** [arxiv.org/abs/2609.27284](https://arxiv.org/abs/2609.27284)
**Summary:** Hunyuan-A13B is an open-source mixture-of-experts language model with 80 billion total parameters and 13 billion activated per inference, pretrained on a filtered 20-trillion-token corpus. Supervised and reinforcement-learning post-training plus dual fast and slow reasoning modes yielded competitive results across math, science, coding, language understanding, and agent tasks.

---

### 14. Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms
**Authors:** Xinjie Shen, Wei Fan, Xudong Guo, Jianhong Tu, Yang Su, Chuqiao Kuang, Yinger Zhang, Dayiheng Liu
**arXiv:** [arxiv.org/abs/2609.27321](https://arxiv.org/abs/2609.27321)
**Summary:** VHD-Play generates agentic reinforcement-learning environments by solving a mathematical mechanism first and rendering its decision process as stateful tools with a shared executable scoring reference. The pipeline produced 3,300 low-cost environments, and training on three mechanism families raised a 35B model's diagnostic agent score from 0.204 to 0.815 while transferring to unseen families and external benchmarks.

---

### 15. All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation
**Authors:** Ohad Rahamim, Dvir Samuel, Idan Schwartz, Gal Chechik
**arXiv:** [arxiv.org/abs/2609.27901](https://arxiv.org/abs/2609.27901)
**Summary:** This work identifies a reciprocal correspondence gap in joint multimodal diffusion models: companion modalities attend strongly to video, but influence video much less in return. Its RecCAR regularizer aligns the weak reverse attention with video-to-modality correspondences, improving human-anatomy quality in video-motion generation and reducing audio-video desynchronization.

---

### 16. InternW0: A Foundational Physical World Model for Efficient Real-World Interactions
**Authors:** Jisong Cai, Yao Mu, Ganlin Yang, Zhe Cao, Zhangzheng Tu, Xing Gao, Kailin Li, Xinyu Zhan, Lixin Yang, Yangkun Zhu, Haoxiang Ma, Ming Zhou, Qiaojun Yu, Yufei Xue, Liqun He, Yifei Yao, Yifan Zhu, Long Ling, Bingqi Jiang, Haoyu Guo, Xueyue Zhu, Bowen Zhou, Bin Zhao, Tianfan Xue, Chunhua Shen, Weinan Zhang
**arXiv:** [arxiv.org/abs/2609.27656](https://arxiv.org/abs/2609.27656)
**Summary:** InternW0 jointly predicts visual futures and continuous robot actions with an asynchronous video-action architecture that reuses and updates predictive context instead of regenerating it at every control step. Trained on roughly 7,200 hours of heterogeneous data, it was evaluated in simulation and on long, contact-rich real-world scientific workflows.

---

### 17. On the Diffusibility of High-Dimensional Latents
**Authors:** Chao Feng, Zhiyang Xu, Bowei Chen, Yuanjun Xiong, Xiyao Wang, Jui-Hsien Wang, Richard Zhang, Zhe Lin, Andrew Owens, Yijun Li
**arXiv:** [arxiv.org/abs/2609.28473](https://arxiv.org/abs/2609.28473)
**Summary:** Fine-tuning representation autoencoders for faithful reconstruction can reduce the effective dimensionality of their latent geometry, making standard velocity prediction waste effort fitting noise directions outside the signal manifold. Switching flow matching to clean-data prediction focuses learning on that manifold and consistently improved text-to-image generation across several strong-reconstruction encoders.

---

### 18. Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models
**Authors:** Xiaoyu Luo, Tao Ren, Wenrui Yu, Xiao Li, Qiongxiu Li, Johannes Bjerva
**arXiv:** [arxiv.org/abs/2609.26637](https://arxiv.org/abs/2609.26637)
**Summary:** The authors use a standard custom-tool interface to elicit intermediate reasoning from frontier language models whose native chain of thought is hidden. Validation on open models and tests on closed systems show that the extracted traces support strong task performance and reveal systematic differences in reasoning efficiency, step types, and tree structure.

---

### 19. EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics
**Authors:** Haoxiang You, Zeyu Shen, Yilang Liu, Zhicheng Zheng, Lihan Zha, Kashu Yamazaki, Mingtong Zhang, Suning Huang, Jiankai Sun, Qianzhong Chen, Lucy He, Kaiyuan Liu, Haoran Chang, Katerina Fragkiadaki, Dhruv Shah, Mac Schwager, Peter Henderson, Ian Abraham, Canwen Xu
**arXiv:** [arxiv.org/abs/2609.27308](https://arxiv.org/abs/2609.27308)
**Summary:** EMBODIEDSWE-BENCH tests coding agents on long-horizon dexterous robotics tasks involving contact, deformable objects, and up to half an hour of interaction. EMBODIEDSWE-GEN turns verified agent solutions into diverse robot-learning trajectories, improving vision-language-action generalization and enabling a policy trained only in simulation to complete a real-robot task.

---

### 20. Calibration as a First-Class Criterion in LLM Evaluation
**Authors:** Mario Sanz-Guerrero, Katharina von der Wense
**arXiv:** [arxiv.org/abs/2609.26489](https://arxiv.org/abs/2609.26489)
**Summary:** This position paper argues that calibration—the match between model confidence and empirical correctness—should accompany the main performance metric in every language-model evaluation. It highlights risks from miscalibration in deployment and in LLM-as-judge, synthetic-data, and active-learning pipelines, while noting that most existing benchmarks already expose the inputs needed for calibration scores.

---
