---
title: "Daily AI Papers — September 29, 2026"
date: 2026-09-29
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-29/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - efficient-attention
  - multimodal-learning
---

### 1. YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality
**Authors:** Ruibin Yuan, Jiahao Pan, Junyan Jiang, Zhiyue Wu, Ziya Zhou, Jiankai Sun, Yizhi Li, Ge Zhang, Yicheng Gu, Zeyue Tian, Junyu Dai, Hanfeng Lin, Kai Li, Shangda Wu, Xuanjie Liu, Jiaming Wang, Zihan Liu, Yue Wang, Yinghao Ma, Hanzhi Yin, Kangrui Chen, Xinyue Zhang, Ziyang Ma, Mengqi Liao, Hejia Zhao, Guowei Huang, Chao Yan, Lei Ke, Jianwei Yu, Bei Liu, Joe Guo, Liumeng Xue, Gus Xia, Wei Xue, Yike Guo
**arXiv:** [arxiv.org/abs/2609.33757](https://arxiv.org/abs/2609.33757)
**Summary:** YuE2 uses a single autoregressive/non-autoregressive Mixture-of-Transformers to plan a readable score, expand it into semantic music tokens, and render full-song audio. It beats evaluated public baselines on WildSongBench, approaches proprietary systems in expert listening, and supports score-guided edits and zero-shot covers from the same checkpoint.

---

### 2. Post-Training Leaves Behavioral Shadows on Unrelated Decisions
**Authors:** Ziyang Zhang, Yubin Jing, Yuanhao Zeng, Yuyao Li, Haofan Wang, Yichen Gong
**arXiv:** [arxiv.org/abs/2609.29233](https://arxiv.org/abs/2609.29233)
**Summary:** Active Taskless Distillation transfers capabilities through task-unrelated prompt-word pairs, using only one ordinary word from a post-trained teacher per prompt and no target-task examples, logits, or teacher parameters. In its primary coding experiment, the method raises HumanEval+ by 5.34 percentage points over a nuisance-matched control and also transfers knowledge and reasoning capabilities across model families and scales.

---

### 3. Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation
**Authors:** Xin Li, Hao Jiang, Xin Gao, Annan Wang, Yuchen Xie, Jinghao Guo, Xingwei Qu, Yichi Zhang, Chau Yuen
**arXiv:** [arxiv.org/abs/2609.35347](https://arxiv.org/abs/2609.35347)
**Summary:** Domain-Normalized MOPD rescales each specialist teacher's token feedback by its measured spread so that high-variance instruction-following feedback does not dominate a shared student. Across three Qwen3.5 model sizes and six benchmarks, it consistently improves over standard multi-teacher on-policy distillation and recovers most of the mathematics specialist's lost gain.

---

### 4. VisionHOPE: Visual Backbones as Self-Modifying Learning Systems
**Authors:** Siran Peng, Tianshuo Zhang, Tianyu Fu, Weisong Zhao, Haoyuan Zhang, Jiankuo Zhao, Minghui Wu, Ping Jiang, Xiangyu Zhu, Chenxu Zhao, Zhen Lei
**arXiv:** [arxiv.org/abs/2609.33325](https://arxiv.org/abs/2609.33325)
**Summary:** VisionHOPE casts a visual backbone as a self-modifying system whose five coupled memories jointly store content, form key/value representations, and control learning and retention within each image. A stability-matched update rule makes the memory dynamics non-expansive, while the resulting backbone remains competitive on ImageNet-1K, COCO, and ADE20K.

---

### 5. Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence
**Authors:** Hongcheng Gao, Jingjing Zhou, Zelin Zheng, Shijia Ge, Jay Zhu, Yazhe Wang, Jianshu Zeng, Xuan Shangguan, Di Wu, Lingyu He, Zhiqi Jia, Sihang Wu, Xiao He
**arXiv:** [arxiv.org/abs/2609.35432](https://arxiv.org/abs/2609.35432)
**Summary:** Physical Coding represents world state and robot execution as explicit code, and HexaAnything uses perception, planning, control, and VLA/WAM tools to verify results and recover from failures. The system improves unseen-task performance on RoboCasa365, completes physics and tabletop tasks on real robots, and turns verified traces into reusable data and memory.

---

### 6. Duplex-MPE: Benchmarking Multi-Party Interaction in Full-Duplex Dialogue
**Authors:** Chengqian Ma, Wenhao Feng, Weixuan Jin, Gaole Dai, Tianyu Xie, Yuexiao Ma, Zhaolu Kang, Xiangyu Zhao, Xiawu Zheng, Fei Chao
**arXiv:** [arxiv.org/abs/2609.31948](https://arxiv.org/abs/2609.31948)
**Summary:** Duplex-MPE evaluates whether a full-duplex speech assistant should answer, stay silent, or stop speaking across 2,000 multi-party scenarios with continuous audio and no supplied transcripts or turn boundaries. Tests of five open-weight speech systems reveal substantial weaknesses, especially in distinguishing explicit from implicit requests and preserving appropriate silence.

---

### 7. Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL
**Authors:** Jinhao Dong, Liang Zhao, Zihao Yue, Wenhan Ma, Linghao Zhang, Lei Li, Shicheng Li, Yifan Song, Bowen Ye, Fuli Luo
**arXiv:** [arxiv.org/abs/2609.32577](https://arxiv.org/abs/2609.32577)
**Summary:** GAGAR jointly grades test-passing code-agent trajectories in a shared workspace, downweights weaker implementations, and redistributes their advantages while preserving the group's total credit. Industrial-scale experiments with 310B- and 1.02T-parameter MiMo checkpoints improve code-agent performance, restrain trajectory growth, and stabilize reinforcement learning.

---

### 8. MassAlloc Attention: Let Attention Allocate Its Own Compute
**Authors:** Jingze Shi, Zhangyang Peng, Xianduo Li, Yanlin Qi, Xiaotian Lin, Haoxian Chen, Liangdong Wang, Guang Liu, Yuyu Luo
**arXiv:** [arxiv.org/abs/2609.32712](https://arxiv.org/abs/2609.32712)
**Summary:** MALA preserves access to every legal causal attention score but allocates post-score computation according to normalized attention mass, using a common tolerance in training and inference. It closely tracks full attention across scaling and long-context tasks while cutting 128K-token training attention latency by 2.2 times forward and 3.0 times backward, plus 1.6 times in decoding.

---

### 9. CoWindow Attention: Full Causal Coverage Is a Collective Property
**Authors:** Jingze Shi, Zhangyang Peng, Xianduo Li, Yanlin Qi, Xiaotian Lin, Haoxian Chen, Liangdong Wang, Guang Liu, Yuyu Luo
**arXiv:** [arxiv.org/abs/2609.32704](https://arxiv.org/abs/2609.32704)
**Summary:** CoWA partitions distant causal-history windows across KV heads while sharing local and prefix-sink windows, so the head ensemble retains full coverage without every head duplicating it. At 128K tokens it reduces training attention latency by 7.4 times forward and 8.6 times backward and lowers decoding memory 7.6 times while remaining close to full attention on quality.

---

### 10. TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces
**Authors:** Dehai Min, Daoan Zhang, Yiming Zeng, Huayi Zhang, Ziyi Chen, Yan Zhang, Qinbo Bai, Mengyuan Chao, Jing Ning, Qiyue Hua, Huiyi Chen, Hanrong Zhang, Henry Peng Zou, Jie Yang, Wei Xu, Philip S. Yu
**arXiv:** [arxiv.org/abs/2609.33295](https://arxiv.org/abs/2609.33295)
**Summary:** TraceDance converts real deployment traces into targeted agent-behavior benchmarks through programmable retrieval, model confirmation, and decision-point continuation scoring. From 252,557 sessions it builds 107 benchmarks with 4,125 instances, where nine frontier models average only a 26.7% pass rate.

---

### 11. How Far Are We from Removing the Visual Encoder? Scaling Laws for Encoder-Free Multimodal Pretraining
**Authors:** Lin Chen, Bolin Ni, Qi Yang, Lan Jiang, Kun Ding, Xiaoran Fan, Hower Yang, Ying Wang, Shiming Xiang
**arXiv:** [arxiv.org/abs/2609.35457](https://arxiv.org/abs/2609.35457)
**Summary:** The study derives scaling laws for multimodal models trained directly from pixels and predicts that encoder-free systems can close their multimodal-loss gap at roughly 10^22 training FLOPs. Its analysis shows the language model increasingly assumes the visual encoder's role through earlier visual processing, bidirectional visual-token interactions, and concentrated expert routing.

---

### 12. Improving Test-Time Scaling with Adaptive Looped Transformers
**Authors:** Yichen You, Tianyu Fu, Aosong Feng, Xingtai Lv, Xuefei Ning, Ning Ding, Yu Wang
**arXiv:** [arxiv.org/abs/2609.35748](https://arxiv.org/abs/2609.35748)
**Summary:** TaH2 trains an iteration decider with lookahead depth supervision so looped transformers spend extra latent computation only on tokens that benefit from it. On AIME it improves the accuracy-compute slope by 53%, exceeds the non-looped model's peak by about 3.4 points at matched compute, and keeps improving as maximum loop depth grows.

---

### 13. Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning
**Authors:** Yijia Fan, Ziqi Huang, Zhongang Cai, Yan Li, Zimo Wen, Wanqi Yin, Haiwen Diao, Ziwei Liu
**arXiv:** [arxiv.org/abs/2609.35767](https://arxiv.org/abs/2609.35767)
**Summary:** UMM-Reflection applies one trajectory-level reinforcement signal to both textual reflection and flow-based image revisions inside a unified multimodal model. It improves GenEval by 12.05 points over supervised fine-tuning and transfers gains to WISE, OneIG-Bench, and T2I-CompBench++ without requiring a verifier at inference.

---

### 14. Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge
**Authors:** Chanuk Lee, Minki Kang, Sangwoo Park, Woongyeong Yeo, Jinheon Baek, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2609.34327](https://arxiv.org/abs/2609.34327)
**Summary:** FlyBy teaches small reasoning models to distinguish execution bottlenecks, where more reflection can help, from knowledge bottlenecks that warrant querying a stronger model. Its 4B model reaches 45.96% pass@8 on 1,158 hard problems, beating Qwen3-14B at 2.7 times lower serving cost, while the 8B version reaches 51.81%.

---

### 15. EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied Tasks
**Authors:** Lizhou Liang, Xinyu Zhong, Miao Pan, Xiaohe Zhou, Xuanyu Liu, Qinfeng Li, Peng Li, Jintao Chen, Xuhong Zhang, Wenqi Zhang
**arXiv:** [arxiv.org/abs/2609.28236](https://arxiv.org/abs/2609.28236)
**Summary:** EmbodiedMemory-Bench contains 2,554 interactive episodes that test fine-grained visual memory, dynamic state tracking, outcome-derived state updates, and generalization across four task families. The accompanying Embodied-Memorizer organizes spatial, event, and scene memories and outperforms evaluated memory systems under matched backbones, though current models remain broadly weak.

---

### 16. CompoWorld: Compositional Environment Scaling for General Agents
**Authors:** Xiao-Wen Yang, Weiyi Xu, Wen Da, Hang Xu, Canwei Li, Hong-Jie You, Pusen Dong, Yucheng Zeng, Zhaokai Luo, Yu-Feng Li, Yao Hu, Mu Chuan
**arXiv:** [arxiv.org/abs/2609.33665](https://arxiv.org/abs/2609.33665)
**Summary:** CompoWorld composes reusable, typed services into dependency-linked environments so agents learn workflows that move information and actions across multiple tools. Using 448 services and 10,130 tools, its SFT and rubric-guided RL recipe improves Qwen3.6-35B-A3B by 9.17 points on average across eight benchmarks and leads comparable agent-specialized models on AutomationBench.

---

### 17. Recursive Harness Distillation across Agents for Robot Manipulation
**Authors:** Seungyeon Kim, Junhoo Lee, Minkyu Kim, Baekseung Kim, Nojun Kwak
**arXiv:** [arxiv.org/abs/2609.33378](https://arxiv.org/abs/2609.33378)
**Summary:** Recursive Harness Distillation has a strong agent turn intervention experience into a playbook for a lighter agent, then refine that guidance using the light agent's execution feedback. Without updating model parameters, the playbook raises real-world manipulation success from 37.3% to 64.0% and also improves both light and strong agents in SimplerEnv Bridge.

---

### 18. Surprising Success, Repeated Failure: Entropy-Guided Credit Assignment for Exploration in LLM Reasoning
**Authors:** Woongyeong Yeo, Minki Kang, Chanuk Lee, Sangwoo Park, Jinheon Baek, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2609.33781](https://arxiv.org/abs/2609.33781)
**Summary:** Entropic Advantage Policy Optimization assigns stronger rewards to high-entropy decisions behind surprising successes and stronger penalties to low-entropy decisions behind repeated failures. It derives token-level credit from existing rollouts without extra supervision and improves overall reasoning performance, exploration coverage, and answer diversity across model backbones.

---

### 19. DepthBench: Measuring How Residual Connections Enable More Computational Depth
**Authors:** Keyu Wang, Yangyi Huang, Jiale Kang, David González-Martínez, Weiyang Liu, Shiwei Liu
**arXiv:** [arxiv.org/abs/2609.32534](https://arxiv.org/abs/2609.32534)
**Summary:** DepthBench holds model size and pretraining fixed while varying Transformer width-to-depth ratios across ten architectures to measure whether added layers create effective computation. Standard Pre-LN and most normalization variants gain little or degrade at extreme depth, whereas HC and Full AttnRes consistently exploit deeper, narrower designs.

---

### 20. QwenGyre: An Elastic Reinforcement Learning Framework for Training xLong-Horizon Agents
**Authors:** Weiqi Wang, Yuxin Zhou, Mouxiang Chen, Siyuan Zhang, Yi Zhang, Yuyan Luo, Zhiyu Yin, Chencan Wu, Jiemin Jiang, Wentao Yao, Chujie Zheng, JianWei Zhang
**arXiv:** [arxiv.org/abs/2609.33848](https://arxiv.org/abs/2609.33848)
**Summary:** QwenGyre elastically reallocates GPUs between live rollouts and training while reconstructing branching histories, scoring partial progress, and deduplicating redundant trajectories for extremely long-horizon agent RL. At 700K tokens per rollout it improves NL2RepoBench by 6.0 points in 48 steps and reports up to 1.85 times and 1.78 times speedups over colocated and asynchronous baselines.
