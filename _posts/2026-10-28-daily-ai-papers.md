---
title: "Daily AI Papers — October 28, 2026"
date: 2026-10-28
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-28/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - world-models
  - agent-memory
---

### 1. The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents
**Authors:** Weidong Tang, Ruiheng Wang, Jingxuan Zhang, Hexin Wang, Haoyuan Chen, Zhengfeiyang Zhang, Yixing Ma, Zichen Jiang, Ziyu Guo, Haodong Li, Zhengbo Jiao, Zhiqing Cui, Xinxiang Yin, Shuo Liang, Zhenglin Wan, Hongzhan Lin, Wangbo Zhao Kaipeng Zhang, Pengfei Zhou, Odin Zhang, Yang You
**arXiv:** [arxiv.org/abs/2610.36077](https://arxiv.org/abs/2610.36077)
**Summary:** The Trinity couples world generation and agent-harness evolution through a capability tree, reusable modules, and a capability-aware router. Its evolved harnesses improve mean performance by 34 points across 28 training benchmarks and 26 points across 18 unseen benchmarks, including two real-world embodied tasks.

---

### 2. ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence
**Authors:** Yihao Hu, Yitong Lin, Pan Wang, Zhihao Wen, Hang Wang, Yiwen Zhao, Deyuan Liu, Yutong Li, Mingda Wan, Yuchen Mao, Tao Lin
**arXiv:** [arxiv.org/abs/2610.34283](https://arxiv.org/abs/2610.34283)
**Summary:** ChronoReplay trains streaming spatial vision-language models using chronologically ordered episodes that retain heterogeneous spatial targets and balance supervision across task families. A single checkpoint improves all three evaluated benchmarks, including a 13.41-point gain on OST-Bench, while adaptive frame selection adds inference-time gains at lower visual cost.

---

### 3. PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations
**Authors:** Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin, Wentao Zhang, Zenan Zhou, Youzheng Wu
**arXiv:** [arxiv.org/abs/2610.37381](https://arxiv.org/abs/2610.37381)
**Summary:** PDRVLA conditions robot actions on physical tokens learned by predicting future RGB, depth, and optical-flow features, avoiding online video generation in the control loop. Trained entirely on public data, it reports success rates of 99.3% on LIBERO, 89.9% on LIBERO-Plus, 93.6% on RoboTwin 2.0, and 81.5% on SimplerEnv.

---

### 4. Multiscale Policy Optimization for Long-Horizon LLM Agents
**Authors:** Tao Ren, Hui Yang, Jia Deng, Tingyang Chen, Qiyao Wang, Shuo Tang, Ziyang Zeng, Yuhua Jiang, Guanghao Li, Huatong Song, Yining Li, Yifan Luo, Kunbao Ding, Feng Chang, Chuan Hao, Ran Tao, Bryan Dai, Jiafeng Liang, Jinyang Jiang
**arXiv:** [arxiv.org/abs/2610.35013](https://arxiv.org/abs/2610.35013)
**Summary:** Multiscale Policy Optimization aligns long-horizon agent credit assignment and policy updates with assistant turns while retaining finer token-level credit allocation. Experiments on search, tool-use, and automation tasks with 4B and 30B-A3B models show consistent gains over strong reinforcement-learning baselines.

---

### 5. VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation
**Authors:** Muxi Diao, Wenbin Xu, Lele Yang, Xuyang Ma, Yuzhe Chen, Jiankang Chen, Kaiyu Jiang, Changyi Liu, Haoyu Zhang, Hongyi Fu, Jianxiong Wang, Tianke Zhang, Haonan Fan, Yingxin Li, Bingyi Li, Xu Wang, Xuanyu Zheng, Bin Wen, Tingting Gao, Han Li, Wentao Zhang, Weiran Xu, Kongming Liang, Zhanyu Ma
**arXiv:** [arxiv.org/abs/2610.35864](https://arxiv.org/abs/2610.35864)
**Summary:** VibeVideoBench evaluates code-driven video-generation agents on 239 English and Chinese tasks requiring a finished video with sound within one hour. Across nine systems and 2,151 scored rollouts, the strongest system satisfies every core requirement on 76.3% of tasks, while missing final renders reveal a separate delivery-planning failure mode.

---

### 6. Hy-Nomas: Towards Free-form Interactive World Generation
**Authors:** Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng, Tiankai Hang, Ji Hou, Jiaqi Li, Yifan Liu, Tao Lu, Junshu Tang, Yu Tang, Yao Teng, Yu Tian, Heng Wang, Weizhi Wang, Xiyao Wang, Xilun Wu, Mingyu Yang, Yangbin Yu, Rui Zhao, Longjun Cao, Linghao Chen, Haoyi Duan, Jiaming Han, Mingji Han, Enhua Jiang, Shunkai Li, Yanzhe Liang, Qinwei Ma, Cong Wang, Lei Wang, Bing Wu, Ke Xing, Ray Ying, Zhentao Yu, Key Zhang, Yuan Zhou, Zhengguang Zhou, Kai Zou
**arXiv:** [arxiv.org/abs/2610.36729](https://arxiv.org/abs/2610.36729)
**Summary:** Hy-Nomas is an 8B diffusion video world model supporting successive free-form text instructions, continuous camera control, and variable-length generation conditioned on cached history. Structured captions and action-aware causal attention preserve context while restricting commands to their intended temporal windows, with human evaluations reporting stronger performance than existing world models.

---

### 7. Memory Tax: Dissecting the Net Value of Agent Memory
**Authors:** Xuan He, Sining Zhoubian, Ruozhen Yang, Yuhao Wen, Zhineng Wang, Yuyang Hu, Ke Yang, Yuyu Zhang, Ping Nie, Jiawei Han, ChengXiang Zhai
**arXiv:** [arxiv.org/abs/2610.34073](https://arxiv.org/abs/2610.34073)
**Summary:** Memory Tax evaluates the net value of dedicated agent memory against direct retrieval from raw interaction history and finds that many memory systems underperform naive RAG. It separates memory benefits from losses caused by reorganizing information, highlighting how memory processing and evaluation can obscure or remove useful evidence.

---

### 8. Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?
**Authors:** Jialv Zou, Xiaotong Li, Zhengrong Yue, Xu Huang, Yaxin Luo, Wenhao Yan, Haodong Li, Wenyu Liu, Xinggang Wang
**arXiv:** [arxiv.org/abs/2610.37662](https://arxiv.org/abs/2610.37662)
**Summary:** This paper finds that effective discrete-token bit budgets predict multimodal understanding better than quantization error and introduces Factorized Vector Quantization to reduce semantic saturation. At industrial training scale, its discrete representations match continuous representations in multimodal understanding and outperform UniAR and Emu3-Chat by 22.8% and 59.2% on a nine-metric average.

---

### 9. HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory
**Authors:** Junming Zhang, Rubin Wei, Xu Cheng, Hao Sun, Jiarui Wang, Ruoxi Cheng, Xiquan Wang, Peisong Wu, Mingsong Chen, Zhouhan Lin
**arXiv:** [arxiv.org/abs/2610.24520](https://arxiv.org/abs/2610.24520)
**Summary:** HABIT-Bench evaluates whether agent memory systems infer user habits from weak evidence across hundreds of sessions and apply them correctly despite exceptions and changing preferences. Across eight memory methods and four domains, the best method reaches only 33.61% macro accuracy, exposing a gap between retaining interactions and appropriately using habits.

---

### 10. Representation Redistribution in Sparse Autoencoders
**Authors:** Ziye Mei, Haotian Ma
**arXiv:** [arxiv.org/abs/2610.21240](https://arxiv.org/abs/2610.21240)
**Summary:** The redistribution sensitivity score identifies sparse-autoencoder feature changes that recur across prompt transformations and separates those changes from their downstream effects. Across 27 autoencoders and eight language models, recurring redistribution is reproducible, while combining sparse-support erosion with the clean margin predicts failures in two frozen safety readouts with AUROCs of 0.935 and 0.958.

---

### 11. Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery?
**Authors:** Yepeng Liu, Shengmai Chen, Xuandong Zhao, Chengzhi Liu, Dawn Song, Xin Eric Wang, Yuheng Bu
**arXiv:** [arxiv.org/abs/2610.32046](https://arxiv.org/abs/2610.32046)
**Summary:** Test-Time Memory Evolution adapts scientific-discovery agents by distilling experience into external memory without updating model weights. Under the same discovery framework, it outperforms test-time training on all five evaluated mathematical tasks while reducing FLOPs by 82.8-84.6% and runtime by 47.7-58.4%.

---

### 12. Rollback: Experience Backtracking in World Models for Policy Improvement
**Authors:** Jiayi Luo, Yang Zhang, Liliang Chen, Nan Wang, Chen Gao, Boxiang Qiu, Zhuoxuan Li, Baorui Peng, Chuankang Li, Yuxiang Yan, Si Liu, Qingyun Sun, Shuicheng Yan, Maoqing Yao, Jianxin Li, Guanghui Ren
**arXiv:** [arxiv.org/abs/2610.36068](https://arxiv.org/abs/2610.36068)
**Summary:** Rollback rewinds action-conditioned world models to critical decisions, explores counterfactual actions, and distills outcome comparisons into action-level supervision while grounding dynamics with real-robot experience. It improves success over the strongest baseline by 10.67, 11.11, and 11.85 percentage points on three real-world tasks and surpasses average human success on ball tossing and tabletop curling within eight hours.

---

### 13. CodeCap-Bench: Can Code Serve as a Good Video Caption?
**Authors:** Jiafu Tang, Yifan Xu, Eric Tang, Junjie Zhao, Shipeng Luo, Te Sun, Haoxuan Hu, Yiyan Ji, Xinlong Chen, Zihao Wang, Yang Shi, Yuanxing Zhang, Pengfei Wan, Jiaheng Liu
**arXiv:** [arxiv.org/abs/2610.37341](https://arxiv.org/abs/2610.37341)
**Summary:** CodeCap-Bench studies executable programs as complementary video captions and finds advantages over natural-language captions in question answering and video reconstruction. Its benchmark contains 323 structured 2D videos across five categories, revealing persistent difficulty capturing complex temporal dynamics and a substantial gap between proprietary and open-source models.

---

### 14. ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning
**Authors:** Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, Fu-En Yang
**arXiv:** [arxiv.org/abs/2610.37666](https://arxiv.org/abs/2610.37666)
**Summary:** ThinkWorld represents robot action reasoning as discrete Chain-of-Dynamics motion tokens and reinforces those tokens through imagined futures that match observed state transitions. This allows unlabeled human and robot videos to refine a shared action-reasoning space, with simulation and real-robot experiments showing human-to-robot transfer and generalization to unseen tasks and environments.

---

### 15. OvisOCR3 Technical Report
**Authors:** Yu Xia, Yinglun Li, Yuhui Chen, Jinlong Huang, Yuyang Wanyan, Shengze Shi, Yifei Song, Yue Duan, Shubo Lin, Jianshan Zhao, En Lin, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo
**arXiv:** [arxiv.org/abs/2610.33066](https://arxiv.org/abs/2610.33066)
**Summary:** OvisOCR3 is a 0.8B model unifying document parsing, OCR, key information extraction, document figure captioning, and cross-page table reconstruction. Domain-balanced training, multi-teacher distillation, and task-specific reinforcement learning produce strong results across these task families, including a 96.74 overall score on OmniDocBench v1.6.

---

### 16. LociArt: A Unified Paradigm for Free-Style Local Video Stylization
**Authors:** Yuxuan Chen, Feng Xie, Jiagao Hu, Fuhao Li, Zepeng Wang, Fei Wang, Daiguo Zhou
**arXiv:** [arxiv.org/abs/2610.36456](https://arxiv.org/abs/2610.36456)
**Summary:** LociArt enables region-specific video stylization through style-aware masks and complementary representation-geometry conditioning while preserving non-target content. It introduces 100K training pairs and a benchmark covering 168 stylization cases, with experiments reporting stronger regional style quality and spatial control alongside temporal consistency.

---

### 17. Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation
**Authors:** Xuyuan Xiong, Siyu Chen, Zihan Shao, Yue Su, Weiyang Jin, Ping Luo, Zhuoran Yang, Xihui Liu
**arXiv:** [arxiv.org/abs/2610.26030](https://arxiv.org/abs/2610.26030)
**Summary:** A scaling study spanning nearly 600 training runs jointly varies model size, token budgets, and forward and backward loop counts to evaluate truncated backpropagation in looped transformers. Full backpropagation through fewer loops wins at matched compute, and the compute-optimal two-loop setting achieves lower validation loss than a non-looped model with about 27% fewer non-embedding parameters and 8% more training compute.

---

### 18. On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction
**Authors:** Eliezer Shlomi, Eliron Rahimi, Avi Mendelson, Chaim Baskin
**arXiv:** [arxiv.org/abs/2610.22543](https://arxiv.org/abs/2610.22543)
**Summary:** SPOT predicts the order in which diffusion language models commit tokens and proposes candidate continuation trees that the target verifies exactly in one pass. Experiments on SDAR-8B reduce target passes by up to 6.8 times and reach up to 3.4 times standard-decoding throughput, while the SPOT-Sets variant adds 59% average throughput over dynamic threshold decoding.

---

### 19. Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception
**Authors:** Lai Wei, Yatai Li, Liangbo He, Jun Lan, Renjie Gu, Linhan Cao, Junkai Lin, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang
**arXiv:** [arxiv.org/abs/2610.37037](https://arxiv.org/abs/2610.37037)
**Summary:** EvidenceConnect synthesizes questions requiring comparison, aggregation, and chaining of visual evidence from related image regions, using agreement and region-ablation checks for quality control. Training vision-language models on these data with verifiable-reward reinforcement learning produces ZwZ2, improving spatial perception, multimodal long-context understanding, agent tasks, and general visual reasoning without benchmark-specific synthesis.

---

### 20. RSI Arena: Towards Recursive Self-Improvement with Human Feedback
**Authors:** Yue Huang, Yanbo Wang, Lichi Li, Yuanyuan Chen, Andreas Haupt, Xiaonan Luo, Zheyuan Liu, Jihye Choi, Felix Juefei-Xu, Xiangliang Zhang, Radha Poovendran, Misha Sra, Ying Liu, Ben Burtenshaw, Thomas Wolf, Alex Pentland, Zichen Chen, Zhangchen Xu
**arXiv:** [arxiv.org/abs/2610.33624](https://arxiv.org/abs/2610.33624)
**Summary:** RSI Arena studies ten agents autonomously post-training language models and then refining them using blind human comparison feedback. All agents produce working assistants and eight improve their style-adjusted relative ratings in the second stage, but benchmark gains remain modest and one model exhibits increased harmful compliance.
