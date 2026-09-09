---
title: "Daily AI Papers — September 09, 2026"
date: 2026-09-09
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-09/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - world-action-models
  - ai-agents
  - efficient-inference
---

### 1. NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness
**Authors:** NeoHorse Team, Guoliang Cao, Guohao Dai, Tianyu Guo, Kai Han, Hailin Hu, Zihan Jiang, Xiang Kuang, Boxun Li, Yulong Li, Zehua Pei, Yuchuan Tian, Jiamin Wang, Yu Wang, Yunhe Wang, Yihong Wu, Haiyang Xu, Shuo Zhang, Hang Zhou, Siyang Cheng, Jiayu Fan, Wei He, Qingrui Jiao, Hongguang Li, Zhiyuan Li, Runke Liu, Xi Liu, Xinchen Liu, Sinno Jialin Pan, Yi Ren, Liuyang Song, Chenyu Wang, Bei Yu, Quanlu Zhang, Xiangyu Zhang, Mengyu Zheng, Yingjie Zong
**arXiv:** [arxiv.org/abs/2609.08183](https://arxiv.org/abs/2609.08183)
**Summary:** Recursive self-improvement (RSI) requires a concrete mechanism through which an AI system observes its capabilities and converts that evidence into the next round of learning. We present NeoHorse-1, a family of agent-native models developed to explore this path through agentic post-training.
**Trending because:** 384 HuggingFace upvotes + gives recursive self-improvement a concrete agentic post-training mechanism with a routing harness

---

### 2. AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing
**Authors:** Ziyang Ma, Zhikang Niu, Wenming Tu, Tianrui Wang, Ruiqi Yan, Junxi Liu, Yanru Huo, Nickk Huang, Yang Liu, Qicong Xie, Zeyu Xie, Hui Wang, Haitao Li, Zixuan Jiang, Yalin Li, Jie Fang, Yifan Duan, Zeyue Tian, Guangzheng Li, Haina Zhu, Shuyi Wang, Jinwen Wang, Mingyu Cui, Tian Tan, Auden, Sen Liang, Steve Yves, Shan Yang, Liefeng Bo, Zilong Zheng, Kai Yu, Eng-Siong Chng, Xie Chen
**arXiv:** [arxiv.org/abs/2609.08936](https://arxiv.org/abs/2609.08936)
**Summary:** We introduce AuK, an open-source foundational model that unifies speech generation and editing through a common interface of natural-language instructions and audio context. To support this broad capability set, we construct approximately 3.03 billion instruction--audio instances and 1.95 million hours of effective supervision across five task families: speech generation, content editing, enhancement and separation, paralinguistic editing, and acoustic editing.
**Trending because:** 196 HuggingFace upvotes + open-sources a single instruction-driven model spanning speech generation and five editing task families

---

### 3. Omni Interaction Agent Technical Report
**Authors:** Orantqing, Shengpeng Ji, Junlong Tong, Jialong Zuo, Dongjie Fu, Di Cao, Yangzhuo Li, Shangda Wu, Franz, Evan, Theron Veyra, Changhao Pan, Jingyu Lu, Dongchao Yang, Zhifei Xie, Yang Tan, Xiaoyu Shen, Xiaoda Yang, Wenfu Wang, Teddysun, Steveyves, Zhou Zhao, Bryanytian
**arXiv:** [arxiv.org/abs/2609.08977](https://arxiv.org/abs/2609.08977)
**Summary:** In this work, we present Gander, an end-to-end model that unifies omni perception, realtime interaction, and agentic capabilities within a single framework. In contrast to turn-based conventional paradigms, Gander continuously receives streaming inputs across multiple modalities, including video, speech, and text, enabling natural full-duplex interaction in both everyday conversations and complex workflow-oriented agent scenarios.
**Trending because:** 125 HuggingFace upvotes + replaces turn-based interaction with a full-duplex streaming agent over video, speech, and text

---

### 4. Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation
**Authors:** Youngrok Park, Sangmin Bae, Hojung Jung, Jongwoo Ko, Yunseon Choi, Young Jin Kim, Pashmina Cameron, Aaron Courville, Se-Young Yun
**arXiv:** [arxiv.org/abs/2609.08798](https://arxiv.org/abs/2609.08798)
**Summary:** Weak-to-strong generalization asks whether stronger models can learn from weaker supervisors and surpass them. This question is particularly important for successive model generations and multi-domain consolidation, where repeating frontier-scale post-training from scratch can be prohibitively expensive.
**Trending because:** 84 HuggingFace upvotes + lets stronger models surpass weaker supervisors without repeating frontier-scale post-training

---

### 5. Show-Harness: Just a VLM Agent Can Play Robots
**Authors:** Yanzhe Chen, Zechen Bai, Zhijun Cao, Wenzheng Zeng, Kevin Qinghong Lin, Yiqi Lin, Guoqiang Liang, Kevin Yuchen Ma, Qiming Huang, Mike Zheng Shou
**arXiv:** [arxiv.org/abs/2609.10522](https://arxiv.org/abs/2609.10522)
**Summary:** Foundation vision-language models (VLMs) exhibit broad intelligence about the world, yet translating this intelligence into robot control remains challenging. We present Show-Harness, an Embodied Harness that enables VLMs to "play" robots through a compact semantic interface linking intent to action.
**Trending because:** 62 HuggingFace upvotes + turns an off-the-shelf VLM into a robot controller through a compact semantic action interface

---

### 6. OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining
**Authors:** Yuran Wang, Siqiao Huang, Mingleyang Li, Chenhao Zhang, Jiaqi Liang, Weiyang Jin, Yue Chen, Xuemin Chi, Donghao Zhou, Qize Yu, Yu-Kai Wang, Yuhan Rui, Shenzhe Yao, Zhen Yuan, Zhenhao Shen, Kefei Zhu, Zijie Zhu, Ning Gao, Xiaowei Chi, Guanqi He, Shanghang Zhang, Hao Dong, Lin Shao, Hang Zhao
**arXiv:** [arxiv.org/abs/2609.07398](https://arxiv.org/abs/2609.07398)
**Summary:** World-Action Models inherit world knowledge from video-generative priors, and channel it into executable control signals through embodied experience. Existing systems, however, are monolithic: the generative backbone, visual representation, architecture, information flow, inference procedure, and training data are tightly coupled, obscuring which design choices matter and why.
**Trending because:** 59 HuggingFace upvotes + breaks monolithic world-action models into modular parts to show which design choices actually matter

---

### 7. DriveZero: End-to-End Driving Beyond Human Demonstrations
**Authors:** Hao He, Chengcheng Hu, Zirun Su, Heng Zhang, Haisong Liu, Jinke Li, Haochen Tian, Zhenwei Shen, Hongyang Li, Zhichao Li, Yunchen Yang, Bochao Huang, Siyu Zhang, Kuangye Chen, Xiongjie Zhang, Wentao Dai, Hengchen Dai, Siyuan Liu, Zehao Huang, Naiyan Wang
**arXiv:** [arxiv.org/abs/2609.06055](https://arxiv.org/abs/2609.06055)
**Summary:** Most end-to-end autonomous-driving systems learn by imitating human driving logs, leaving their learned behavior constrained by the quality and behavioral coverage of the recorded trajectories. This report presents DriveZero, an end-to-end system that learns driving behavior beyond human demonstrations.
**Trending because:** 53 HuggingFace upvotes + learns driving behavior that is not bounded by the coverage of human demonstration logs

---

### 8. Programmable World Model
**Authors:** Zheng-Hui Huang, Guixu Lin, Jiacheng Lin, Yi-Chuan Huang, Ruihan Yu, Muyao Niu, Siqi Yang, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang, Zhixiang Wang
**arXiv:** [arxiv.org/abs/2609.10540](https://arxiv.org/abs/2609.10540)
**Summary:** Recent video world models generate increasingly realistic and interactive visual experiences, yet lack reliable mechanisms for maintaining persistent world state and enforcing programmable rules over extended interactions. We introduce Programmable World Model, a framework that decouples world-state evolution from visual observation generation.
**Trending because:** 50 HuggingFace upvotes + decouples persistent world state from visual generation so rules hold over long interactions

---

### 9. GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation
**Authors:** AgiBot Research Team, Renhang Liu, Wenzhi Zhao, Zhuo Yang, Liliang Chen, Pengfei Zhou, Shengcong Chen, Guanghui Ren, Youlun Peng, Rongjun Jin, Nan Wang, Sukai Wang, Xindong He, Jinyuan Feng, Ziyu Xiong, Linqing Zhong, Yifei Wei, Feng Han, Long Zhang, Da Huang, Nanshu Zhao, Chenghao Yin, Mo Wu, Zhaodong Yan, Kongtao Hu, Yuxiang Yan, Aogelijiang Niyazi, Yu Fang, Jia Zeng, Lizhu Meng, Daizhen Lv, Haoyu Cao, Zhiwen Hou, Lianjin Ye, Yuehan Niu, Zhikai Cai, Xuan Hu, Hui Min, Xiongfeng Cai, Yue Liao, Jing Wu, Soujanya Poria, Ye Li, Sanping Zhou, Maoqing Yao
**arXiv:** [arxiv.org/abs/2609.05588](https://arxiv.org/abs/2609.05588)
**Summary:** World-action models (WAM) predict future states to guide robot actions, enabling learning from both action-free video and action-labeled interaction. Most inherit pretrained video generators, leaving WAM pretraining and scaling underexplored.
**Trending because:** 49 HuggingFace upvotes + treats world-action pretraining and scaling as first-class instead of inheriting a video generator

---

### 10. Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation
**Authors:** Igor Pavlovic, Thiemo Wandel, Anton Obukhov, Luca Bartolomei, Andrey Davydov, Fabio Tosi, Matteo Poggi, Sabine Süsstrunk, Dengxin Dai
**arXiv:** [arxiv.org/abs/2609.08084](https://arxiv.org/abs/2609.08084)
**Summary:** Monocular depth estimation is a ubiquitous yet highly ill-posed computer vision task, with downstream applications in scene reconstruction, computational photography, and robotics, among others. Despite the field's maturity, recent models still struggle to generalize to out-of-distribution inputs and to produce sharp and detailed depth maps.
**Trending because:** 48 HuggingFace upvotes + revisits diffusion transformers to fix out-of-distribution generalization and blurry monocular depth

---

### 11. Miles v0.1: Production-Level Post-Training
**Authors:** RadixArk, Tom Chen, Mao Cheng, Shi Dong, Kangrui Du, Yanbin Jiang, Jiajun Li, Yiming Li, Tao Lin, Yusheng Su, Andy Ye, Yueming Yuan, Zhichen Zeng
**arXiv:** [arxiv.org/abs/2609.08368](https://arxiv.org/abs/2609.08368)
**Summary:** We present Miles v0.1, a full-stack, production-ready system for frontier post-training. Building upon the clean design of slime, Miles designs each stage of the reinforcement-learning (RL) training loop around a single principle: components should be verified, clean, and customizable.
**Trending because:** 48 HuggingFace upvotes + ships a production-ready RL post-training stack built for verifiable, customizable components

---

### 12. Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout
**Authors:** Zhuoran Zhao, Shengju Qian, Tongtong Liang, Xianghao Kong, Songchun Zhang, Junchao Huang, Guian Fang, Xin Wang, Pan Hui, Anyi Rao
**arXiv:** [arxiv.org/abs/2609.09123](https://arxiv.org/abs/2609.09123)
**Summary:** Autoregressive (AR) video diffusion models have shown great potential in real-time video generation. Recent methods distill pretrained bidirectional video diffusion models into causal AR students through Distribution Matching Distillation (DMD), but the generated videos often suffer from over-saturation and over-smoothing issues, resulting in limited visual quality and realism.
**Trending because:** 43 HuggingFace upvotes + attacks the over-saturation and over-smoothing that plague distilled autoregressive video diffusion

---

### 13. SceneMosaic: Efficient and Diverse Simulation-Ready Scene Generation via Hybrid Agentic Layout Evolution
**Authors:** Xingjian Ran, Xiaoye Mo, Sihao Liu, Jianyu Zhang, Li Luo, Bo Dai
**arXiv:** [arxiv.org/abs/2609.05594](https://arxiv.org/abs/2609.05594)
**Summary:** Diverse and simulation-ready indoor scenes are essential for interactive entertainment and embodied AI, yet their scalable generation remains challenging. Recent agentic text-to-3D scene pipelines that rely on vision-language models (VLMs) can generate scenes of high fidelity but require costly iterative object placement and refinement.
**Trending because:** 41 HuggingFace upvotes + cuts the cost of simulation-ready 3D scene generation via hybrid agentic layout evolution

---

### 14. AgentGrad: Intervention-guided Prompt Optimization for Multi Agent Systems
**Authors:** Jaewon Chu, Jinwoo Seo, Jaewon Cho, Jeehye Na, Yunyang Xiong, Youngdae Kim, Hyunwoo J. Kim
**arXiv:** [arxiv.org/abs/2609.08572](https://arxiv.org/abs/2609.08572)
**Summary:** Large language model (LLM)-based multi-agent systems (MAS) achieve strong performance by employing specialized multiple agents, yet their performance depends on the prompt design of each agent. For MAS prompt optimization, textual gradient methods that guide prompt updates using natural-language feedback have emerged as a leading paradigm.
**Trending because:** 40 HuggingFace upvotes + optimizes per-agent prompts in multi-agent systems using intervention-guided textual gradients

---

### 15. BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference
**Authors:** Janghyeon Kim, Minsoo Kim, Kyuhong Shim, Jungwook Choi
**arXiv:** [arxiv.org/abs/2609.04971](https://arxiv.org/abs/2609.04971)
**Summary:** Large Reasoning Models (LRMs) achieve superior problem-solving through extended Chain-of-Thought (CoT) generation, but the resulting key-value (KV) cache grows linearly with sequence length and creates severe memory bottlenecks, often exceeding GPU capacity for long reasoning traces. Existing KV cache compression methods rely on recent queries to estimate future token importance, implicitly assuming these serve as reliable proxies for future attention patterns.
**Trending because:** 32 HuggingFace upvotes + compresses the KV cache of long reasoning traces using beacon queries instead of recent-query proxies

---

### 16. Reason Through the Latent! Making Latent Visual Reasoning Necessary
**Authors:** Suhyeong Park, Junha Jung, Jaewoo Kang
**arXiv:** [arxiv.org/abs/2609.06746](https://arxiv.org/abs/2609.06746)
**Summary:** Latent visual reasoning aims to perform multimodal reasoning through hidden-state computation rather than explicit textual chains of thought. However, visual information being present in a latent state does not imply that the model actually relies on that state when producing its answer, especially when alternative image-conditioned paths remain available.
**Trending because:** 32 HuggingFace upvotes + makes latent visual reasoning load-bearing rather than an unused hidden state

---

### 17. VDiff-Bench: A Challenging Benchmark for Fine-Grained Image Difference Identification
**Authors:** Yixin Wan, Tianle Zheng, Kai-Wei Chang
**arXiv:** [arxiv.org/abs/2609.06245](https://arxiv.org/abs/2609.06245)
**Summary:** Multimodal Large Language Models (MLLMs) perform strongly on general visual understanding tasks such as visual question answering, yet they often struggle with a basic comparative skill: identifying what has changed between two similar images. We introduce VDiff-Bench, a challenging multiple-choice benchmark for fine-grained Image Difference Identification.
**Trending because:** 30 HuggingFace upvotes + exposes how badly multimodal LLMs handle fine-grained image difference identification

---

### 18. Kalman Delta Networks: Uncertainty-aware Associative Memory
**Authors:** Ngoc Bui, Tinglin Huang, Rex Ying
**arXiv:** [arxiv.org/abs/2609.07816](https://arxiv.org/abs/2609.07816)
**Summary:** Linear attention is increasingly used in frontier language models for efficient long-context inference and constant-memory decoding. Its fixed-size recurrent memory, however, requires an online decision at each token: what to write and how strongly to overwrite existing associations before knowing which information future queries will require.
**Trending because:** 27 HuggingFace upvotes + adds uncertainty awareness to linear-attention memory writes under fixed-size recurrent state

---

### 19. Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context RL Post-Training
**Authors:** Zili Wang, Zhaopeng Qiu, Yuekai Zhang, Shuang Yu, Junjie Lai
**arXiv:** [arxiv.org/abs/2609.07108](https://arxiv.org/abs/2609.07108)
**Summary:** Speculative decoding accelerates rollout generation, which dominates the cost of reinforcement learning (RL) post-training. Online co-training can further increase the draft's accuracy, yielding greater speedups.
**Trending because:** 27 HuggingFace upvotes + speeds up RL post-training rollouts by co-training the speculative draft model online

---

### 20. Steering Geometry: Validating Human Value Geometry in LLM Steering Space
**Authors:** Mohammad Mahdi Abootorabi, Armin Saghafian, Ali Bazshoushtari, Hamid Rezaei, EunJeong Hwang, Vered Shwartz, Parvin Mousavi, Purang Abolmaesumi
**arXiv:** [arxiv.org/abs/2609.06289](https://arxiv.org/abs/2609.06289)
**Summary:** As large language models (LLMs) are increasingly deployed in alignment-sensitive contexts, activation steering has emerged as a lightweight, inference-time alternative to fine-tuning methods (e.g., RLHF, DPO) for behavioral control. However, existing work typically validates steering on isolated behaviors, leaving it unclear whether steering vectors encode coherent semantic structure or merely exploit behavior-specific shortcuts.
**Trending because:** 27 HuggingFace upvotes + tests whether activation-steering vectors encode coherent value geometry or behavior-specific shortcuts
