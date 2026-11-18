---
title: "Daily AI Papers — November 18, 2026"
date: 2026-11-18
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-18/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robot-learning
  - efficient-models
---

### 1. TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks
**Authors:** Xingchen AGI Lab, Baotian Hu, Bingkai Yang, Boyang Wang, Changzai Pan, Chao Lyu, Chao Wang, Chen Li, Chenshuo Pan, Chenyu Lin, Chenyuan Zhang, Chongming Liu, Dawei Fan, Di Wu, Dong Guo, Dong Li, Dongfang Li, Enlin Liu, Fanye Xiao, Fengkai Li, Fubei Yao, Gang Lin, Han Gao, Hanming Wu, Haowei He, Huapeng Liu, Hua Wang, Huinan Xu, Jiahong Xiong, Jiaxin Peng, Jianxiang Ma, Jianxing Zhuge, Jie Zhang, Ji Xiong, Jinglin Chen, Jingqi Li, Jingxuan Li, Jiwang Ye, Junchen Li, Junbiao Li, Junyang Wu, Kaidong Yu, Kaipeng Jia, Kehai Chen, Kuai Li, Laobin Liu, Lei Li, Libo Qin, Lingling Shi, Luwen Pu, Menghao Xu, Mengjiao Bao, Mengqi Chen, Min Zhang, Mingrui Wang, Naying Wang, Peicong Han, Peiming Guo, Pengfei Li, Qiang Feng, Qi Wang, Qingjun Zhu, Qingli Li, Qitai Ding, Qiyi Xie, Quanchao Zhao, Rongbao Han, Rui Xue, Ruiyu Fang, Ruiting Song, Shijie Li, Shiquan Wang, Shuangyong Song, Sishi Xiong, Teng Su, Wankang Bao, Weijie Zhang, Wei Mao, Weiwei Fu, Weiyang Huang, Wenmin Deng, Wenqing Hu, Wujie Zhong, Xi Yu, Xiaohui Hu, Xiaomin Fang, Xiaomeng Huang, Xiaoqiong Shi, Xiaotong Shang, Xiaoyu Li, Xinglei Xu, Xin Jiang, Xin Wang, Xin Zhang, Xinzhang Liu, Xue Liu, Xuefeng Bai, Xuewei He, Yahan Li, Yanhan Zhang, Yanlei Xue, Yanzhang Wu, Yang Yu, Yi Liu, Yin Zhang, Yingyan Li, Yitong Yao, Yixuan Li, Yongqiang Xia, Yongxiang Li, Yinzhou Zhu, Yu Zhao, Yuhao Jiang, Yunpeng Zhang, Yuting Lin, Yuxuan Wu, Yuyao Huang, Yuyi Wang, Zebo Peng, Zhenwu Pei, Zhenxiong Li, Zhao Wang, Zhaoxi Zhang, Zhihao Yang, Zhiqiang Dong, Zhiwei Yan, Zhilong Lu, Zhonghao Guo, Zhongheng Wu, Zhongjiang He, Zhongqiu Li, Zhu Yuan, Zhuoru Jiang, Zhuoyi Wei, Zijia Guo, Zilu Huang, Zhipeng Guo, Zirui Li, Zihan Wang
**arXiv:** [arxiv.org/abs/2611.22115](https://arxiv.org/abs/2611.22115)
**Summary:** Xing 4 extends the TeleChat model line with architecture and training-infrastructure work on Ascend hardware, including pretraining a 285B-parameter model on 8,192 Ascend 910C cards via MindSpore HyperParallel. For post-training it introduces TeleGym, a unified agent platform using disaggregated asynchronous execution and partial rollouts to connect execution, evaluation, and trajectory construction to policy optimization.

---

### 2. AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs
**Authors:** AI Training Platform Team, Bingwei Zhang, Jing Li, Amir Abdullin, Sihang Chen, Xin Chen, Liangjun Feng, Yingmeng Gao, Tao Guo, Junjie Huang, Dongfang Li, Zhanglian Lin, Jiajun Liu, Zekun Liu, Zhengxuan Lu, Xiaodong Luo, Jian Meng, Ivan Nosov, Linyuan Qiu, Weijian Sun, Wanrui Yan, Binfan Zheng, Zhicheng Zhou, Baotian Hu, Min Zhang, Haizhou Li, Zhiquan Luo
**arXiv:** [arxiv.org/abs/2611.17621](https://arxiv.org/abs/2611.17621)
**Summary:** AscendGYM is a benchmark of 48 kernels at three difficulty levels whose test cases use data types and tensor shapes drawn from real Ascend NPU training and inference workloads, measuring how well agents optimize existing kernels. It supports model and model-harness evaluation modes and proposes the Speedup-Token Score, which weighs kernel speedups against the token cost of obtaining them.

---

### 3. Weight-Space Programming Doesn't Need Transformers
**Authors:** Hyunjong Ok, Jaeho Lee
**arXiv:** [arxiv.org/abs/2611.22055](https://arxiv.org/abs/2611.22055)
**Summary:** When frontier LLMs write neural network weights by hand without gradient descent, given freedom to design the architecture they converge on sparse lookup tables rather than Transformers, reaching up to 54.4% test accuracy. An LLM-designed model beats the best Transformer the same LLM wrote with about 1,800x fewer parameters, motivating an associative-memory model up to 17x faster on GPUs than a same-sized Transformer.

---

### 4. Multi-Branch Transformer
**Authors:** Gaotang Li, Lingjie Chen, Chunyuan Deng, Zhiwei Xu, Hongzheng Chen, Christopher De Sa, Jingrui He, Yingheng Wang, Hanghang Tong
**arXiv:** [arxiv.org/abs/2611.19800](https://arxiv.org/abs/2611.19800)
**Summary:** The Multi-Branch Transformer scales models by running independently parameterized branches of Transformer blocks in parallel between shared initial and final layers, outperforming sequential Transformers at matched parameters and compute across 0.8B to 2.1B MoE scales. With a shared Joint-KV cache, the final recipe cuts KV-cache storage by up to 34% and raises decoding throughput by up to 51.4% on a single H200.

---

### 5. ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models
**Authors:** Ke Sun, Kevin Yuchen Ma, Yike Zhang, Yanzhe Chen, Mike Zheng Shou
**arXiv:** [arxiv.org/abs/2611.21099](https://arxiv.org/abs/2611.21099)
**Summary:** ForceHarness lets frozen, API-only multimodal models use contact force for robot manipulation without demonstrations or finetuning, via self-terminating force primitives and a physics translation layer that turns force traces into physical quantities. On a real arm without a wrist force sensor it raises GPT-6 Astra's zero-shot success from 3.3% to 90.0%, and it adds large gains on ForceBench and the new HiddenPhys benchmark.

---

### 6. Beyond Answering: Learning to Speak First and Act in Streaming Video
**Authors:** Shuhan Li, Huankang Guan, Xintong Guo, Yang Bo, Yuyang He, Dunyuan Xu, Jingyan Chen, Fang Liu, Tsz Kin Wan, Jinpeng Chen, Zhenqi He, Yuxuan Hu, Wenbo Li, Han Gao, Qijun Li, Long Chen, Hongsheng Li, Rui Liu
**arXiv:** [arxiv.org/abs/2611.17048](https://arxiv.org/abs/2611.17048)
**Summary:** AURA 2.0 is a streaming video LLM that can initiate conversations about events in a video stream without a user query, call external tools based on what it sees, and ground objects with frame-aligned bounding boxes. Trained on a dedicated streaming interaction dataset with a three-stage scheme and long-horizon interaction memory, it reports leading results among open-source streaming models.

---

### 7. Breath-Dx: A Time Series Classification Benchmark for Disease Screening with eNose
**Authors:** Ivan Poddiakov, Ivan Kruzhilov, Galina Zubkova, Svetlana Erofeeva, Andrey Savchenko, Pavel Blinov
**arXiv:** [arxiv.org/abs/2611.15348](https://arxiv.org/abs/2611.15348)
**Summary:** Breath-Dx is a benchmark for electronic-nose disease screening built on the public Scent of Health dataset of 1,234 patients across nine diagnostic groups, with temporal train/test splits that account for sensor drift. Across 10 time series methods, all lose 0.05 to 0.12 AUC under temporal validation, with the best reaching ROC AUC 0.74 to 0.76 for some lung conditions while others stay near chance.

---

### 8. Self-Improvement Memory Enables Continual Recursive Self-Improvement
**Authors:** Xin Yu, Fei Xia, Jiaqi Pan, Youbao Tang, Chengzhi Liu, Adams Yu, Sicong Jiang, Yanfei Chen, Lingzhou Xue, Ting Yu
**arXiv:** [arxiv.org/abs/2611.18856](https://arxiv.org/abs/2611.18856)
**Summary:** This work studies Continual Recursive Self-Improvement, continuing harness optimization across benchmarks or policy models, and proposes Self-Improvement Memory that records edit rationales, predicted and observed outcomes, and evaluation context for the optimizer. Across four domains, it beats harness-only and root-cause-only continuation, improving coding scores by an average of 2.36 points over harness-only continuation across ten source runs.

---

### 9. TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation
**Authors:** Haosong Peng, Xiangyang Liu, Zhengshen Zhang, Yunfeng Fan, Tianyu Qi, Xin Xia, Yufeng Zhan, Wenchao Xu
**arXiv:** [arxiv.org/abs/2611.23143](https://arxiv.org/abs/2611.23143)
**Summary:** TCP4D uses a shared 4D scene representation to track tool-center-point poses and gripper states from monocular robot videos and to generate future TCP trajectories conditioned on observations and language. Its tracker reaches 7.60 and 16.07 mm trajectory error on DROID and RoboLab, the generator hits 69.19% mean success on RoboTwin, and cross-embodiment augmentation improves target-robot success by 41.5%.

---

### 10. Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration
**Authors:** Ting-Hsuan Chen, Siheng Zhao, Han Jiang, Qi Pan, Louison Lu, Jiaheng Luo, Henghui Bao, Yiyu Chen, Quan Nguyen, Yue Wang
**arXiv:** [arxiv.org/abs/2611.22275](https://arxiv.org/abs/2611.22275)
**Summary:** Heave-Ho is a decentralized framework for long-horizon multi-humanoid loco-manipulation, pairing a multi-agent post-trained whole-body tracking controller with a vision-language planner and speech-based leader-follower coordination. Trained with two identical humanoids, it scales to teams of up to ten robots and heterogeneous teams without retraining, outperforming baselines on the new 12-task HH-Bench.

---

### 11. LynnReal-Hand: Unlocking World Interaction with Hand Control
**Authors:** Shaohao Rui, Chaoyang Zhang, Xiaofeng Mao, Weijie Ma
**arXiv:** [arxiv.org/abs/2611.21479](https://arxiv.org/abs/2611.21479)
**Summary:** LynnReal-Hand is a hand-controlled video world model trained on 100K curated interaction clips with hand-aware supervision, a causal flow map for few-step generation, and region-aware score distillation. With a compact Ultra-Fast-VAE decoder, it streams 540p video at 18.03 FPS on a single H200 while leading HandBench on hand-following accuracy and visual quality.

---

### 12. FastFrames: Video Generation at Interactive Latency
**Authors:** Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan Richter, Vladlen Koltun
**arXiv:** [arxiv.org/abs/2611.23226](https://arxiv.org/abs/2611.23226)
**Summary:** FastFrames is a family of autoregressive video diffusion models that reach interactive latency by replacing VAE decoding and KV cache updates, found to cause over half of end-to-end latency, with lightweight alternatives. Its 1.3B model runs at 36 ms per frame on one B200 while matching a state-of-the-art model nearly 8x slower, and its 14B model runs at 45 ms per frame on an 8x B200 node with better quality.

---

### 13. VideoNexus: Video Perception Beyond the Reasoning Context
**Authors:** Yancheng Long, Xuanyu Zheng, Wei Chen, Luoyuan Zhang, Haoyang Xu, Bin Wen, Tingting Gao
**arXiv:** [arxiv.org/abs/2611.21392](https://arxiv.org/abs/2611.21392)
**Summary:** VideoNexus is a training-free framework for long-video understanding that separates evidence-driven planning from detailed perception, delegating native audio-video inspection to sub-agents that return compact, temporally grounded evidence. With Gemini 3.8 Flash it reaches 88.6% on full LVBench, beating same-backbone baselines at 44% of the agentic baseline's API cost, and improves 8.5 points over the Video-GAIA ReAct harness with Kimi K3.

---

### 14. π^4: A Foundation Model for 4D Scene Geometry and Motion
**Authors:** Yifan Wang, Weiguang Zhao, Ni Yang, Haoyu Guo, Junting Dong, Weinan Zhang, Chunhua Shen
**arXiv:** [arxiv.org/abs/2611.23144](https://arxiv.org/abs/2611.23144)
**Summary:** π^4 is a roughly 0.5B-parameter foundation model that recovers dense geometry, camera poses, metric scale, 2D/3D point tracks, and moving-object masks from uncalibrated images or videos in a single forward pass. It achieves the best overall average rank in geometry evaluation and competitive tracking and segmentation, scaling to scenes with thousands of images despite training on at most 64 views.

---

### 15. FMT: Lossless Image Compression in a Fixed Number of Parallel Steps
**Authors:** Ammar Ali
**arXiv:** [arxiv.org/abs/2611.23108](https://arxiv.org/abs/2611.23108)
**Summary:** FMT is a lossless image format that stores an image as a coarse-to-fine tree of independent steps decoded in parallel rANS lanes, so any image decodes in a fixed number of sequential steps. Without a network it beats NVIDIA's HTJ2K on size and speed, and with a large network it decodes Kodak photos 9 to 61x faster than learned codecs on the same A100 at equal or smaller size.

---

### 16. From Repositories to Training Environments: Scaling Long-Horizon Coding Agents with Environment Evolution Loop
**Authors:** Yang Tian, Tianyu Zheng, Xiyuan Yang, Yaxin Du, Chengran Yang, Bo Zhao, Jian Yang, Bryan Dai
**arXiv:** [arxiv.org/abs/2611.21152](https://arxiv.org/abs/2611.21152)
**Summary:** RepoFactory converts real repositories into 10,159 verifiable environments across 17 software domains where agents build complete projects from a language specification, using an Environment Evolution Loop driven by proxy feedback. Training Qwen3.5-35B-A3B on them yields RepoHorizen-35B-A3B, gaining 22.6 points on NL2Repo-Bench and 8.5 points on average across five long-horizon coding and agentic benchmarks.

---

### 17. MedJev: A System One Vision-Language Decision Model for Fast and Effective Medical Image Understanding
**Authors:** Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Dongfu Yin, Qingsong Wen, Pheng-Ann Heng
**arXiv:** [arxiv.org/abs/2611.20992](https://arxiv.org/abs/2611.20992)
**Summary:** MedJev is a System One vision-language decision model that maps medical images, questions, and candidate answers to a decision in a single forward pass, dropping upper language layers and autoregressive generation. Built on Qwen3.5-4B, it gains 7.93% absolute accuracy with a 6.04x end-to-end speedup across four medical benchmarks and leads 4B to 9B general and medical VLMs.

---

### 18. Correcting Persistent Failures in Point-Cloud Grasping Policies using Human Demonstrations in Virtual Reality
**Authors:** Achyuthan Unni Krishnan, Karthik Rengarajan, Bharath Narasimhan, Chris von Csefalvay
**arXiv:** [arxiv.org/abs/2611.18919](https://arxiv.org/abs/2611.18919)
**Summary:** This paper adds a human-in-the-loop loop to point-cloud grasping, automatically mining grasps an RL policy keeps failing and collecting corrective human grasp points in virtual reality. In simulation, RL raises unseen-object success from 55% to 83%, and 58 human demonstrations nearly double success on persistently failed cases from 24% to 45% without hurting general performance.

---

### 19. Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model
**Authors:** William Xingxu Chen, Alexi Gladstone, Zeyu Michael Li, Heng Ji, Yilun Du
**arXiv:** [arxiv.org/abs/2611.08977](https://arxiv.org/abs/2611.08977)
**Summary:** Energy-Based Reasoners learn an energy function over latent reasoning states and treat looped model updates as gradient descent on that energy, which also supplies a stopping signal, trained with exploration to shape the energy landscape. Across four algorithmic benchmarks they match or beat prior recurrent reasoners, reaching 99.9% on Sudoku-Extreme with 345x less inference compute than the next-best model.

---

### 20. Agentic On-Policy Distillation Implicitly Reshapes LLMs' ReAct Patterns
**Authors:** Deyang Kong, Zhaoyi Li, Sijian Ren, Yuan Wei, Ying Wei, Defu Lian, Shikun Zhang, Wei Ye
**arXiv:** [arxiv.org/abs/2611.19244](https://arxiv.org/abs/2611.19244)
**Summary:** This study examines how on-policy distillation reshapes LLM agents' ReAct reasoning, actions, and observation gathering across mathematics, ALFWorld, and tau^2-bench, finding both positive and strongly negative cross-domain transfer. ALFWorld supervision drops tau^2-bench accuracy from 41.5% to 6.6%, and a selective distillation scheme guided by teacher preference shifts raises it from 11.5% to 29.9% with a source-learning trade-off.
