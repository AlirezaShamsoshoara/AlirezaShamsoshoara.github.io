---
title: "Daily AI Papers — November 09, 2026"
date: 2026-11-09
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-09/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - inference-efficiency
  - multimodal-learning
---

### 1. SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes
**Authors:** Hao Yu, Zhenwei Wang, Yongzhen Hu, Yuning Gong, Junta Wu, Xiaowei Zhou, Hujun Bao, Tengfei Wang, Chunchao Guo, Sida Peng
**arXiv:** [arxiv.org/abs/2611.08264](https://arxiv.org/abs/2611.08264)
**Summary:** SplatAnything introduces Gaussian Spacing Normalization to give feed-forward 3D Gaussian Splatting a consistent spatial reference across scene scales and camera configurations. A benchmark spanning datasets, input sparsity, and extrapolated viewpoints shows the method improves reconstruction, especially under substantial scale and viewpoint changes.

---

### 2. P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter Priors
**Authors:** Sinuo Wang, Jiacheng Lu, Zeyu Zhang, Maojia Song, Rui Sun, Beidi Luan, Yutong Xie, Jing Li, Daxin Jiang, Qi Wu, Zuo Bai
**arXiv:** [arxiv.org/abs/2611.03953](https://arxiv.org/abs/2611.03953)
**Summary:** P^2-MOPD combines trainable student weights with expert parameter priors and jointly learns their mixing coefficients during multi-teacher on-policy distillation. Across four domains at 1.7B and 4B scales, it surpasses the baseline's final average recovery in half the training steps, with the 1.7B model reaching 94.7% recovery versus 80.9% for MOPD.

---

### 3. LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis
**Authors:** Haoxiang Cao, Yuxuan Zhang, Penghui Du, Bo Li, Jiajiong Cao, Yingying Fan, Zimeng Wu, Yifu Luo, Mingzhe Zheng, Junwen Miao, Huaisong Zhang, Yang Yao, Yu Wang, Dongfu Jiang, Ping Nie, Wenhu Chen, Chaoqun Wang, Changqian Yu, Kelsey R. Allen
**arXiv:** [arxiv.org/abs/2611.06856](https://arxiv.org/abs/2611.06856)
**Summary:** LongBanana evaluates multi-reference image synthesis with 90 expert-verified tasks containing about 32 reference images and 20 constraints each, totaling 4,670 atomic evaluation items. Its graph-grounded evaluation tests fidelity, relational binding, and global constraints, while experiments show agent harnesses can improve evidence grounding and iterative image repair.

---

### 4. Beneath the Surface: What We Overlook When We Talk About Agent Evolution
**Authors:** Xiaobo Wang, Zimu Wang, Siyu Ye, Jiaqi Li, Min Tang, Jun Bai, Yuling Shi, Ruobing Wang, Jingjing Zhang, Chaofan Wang, Kai Wu, Mengnan Qi, Kai Cai, Xiaodong Gu, Qi Liu, Zilong Zheng
**arXiv:** [arxiv.org/abs/2611.07624](https://arxiv.org/abs/2611.07624)
**Summary:** This study evaluates four agent-harness evolution methods and finds that all sixteen evolved agents gain previously uncovered tasks while losing previously covered ones, with reliability gains often increasing deployment cost. Its preservation-aware diagnostics motivate EvoAudit, which revises selection, analysis, mutation, and admission rules and achieves the best performance in the reported evaluations.

---

### 5. EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models
**Authors:** Yequan Bie, Dengyang Jiang, Zhixuan Chen, Xiaozhuan Liang, Haoxuan Che, Quande Liu, Xi Chen, Hao Chen
**arXiv:** [arxiv.org/abs/2611.06748](https://arxiv.org/abs/2611.06748)
**Summary:** EvoWorld pairs a vision-language world-state reasoner with an autoregressive video renderer to model consequences of events even when affected entities move out of view. The accompanying dataset and benchmark evaluate event realization, causal reactions, and revisit consistency, with experiments reporting improved causal evolution while preserving visual quality.

---

### 6. Fast and Exact Relative-Position Attention via Structure-Aware Kernels
**Authors:** Delyan Boychev, Ivo Petrov, Dimitar I. Dimitrov
**arXiv:** [arxiv.org/abs/2611.01182](https://arxiv.org/abs/2611.01182)
**Summary:** This paper integrates exact additive relative-position attention into FlashAttention-style tiled computation using offset-aware reuse and contention-free gradient aggregation. Its Triton kernels report 1.8-6.4x forward and 2.0-21x backward speedups at 8K tokens over the strongest tested baseline per mechanism, enabling transcription that is 1.8x faster with 2.4x less memory.

---

### 7. LLMs Don't Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting
**Authors:** Lingfei Qian, Yan Wang, Xueqing Peng, Yupeng Cao, Yuechen Jiang, Zhuohan Xie, Anke Xu, Wenbo Cao, Jiarui Chen, Zehan Li, Jimin Huang, Alejandro Lopez-Lira, Yuehua Tang, Sophia Ananiadou, Jian-Yun Nie
**arXiv:** [arxiv.org/abs/2611.06808](https://arxiv.org/abs/2611.06808)
**Summary:** FinDendro tests temporal self-knowledge using 2,226 dated financial facts and prompts that distinguish factual accuracy from claims of knowing or guessing. The results show that model self-reports, stated cutoffs, and historical-date instructions cannot certify backtests as leak-free, motivating behavioral measurement of what models actually know.

---

### 8. Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription
**Authors:** Daniel Huang, Qi He, Shaoxiong Duan, Yingjie Li, Qiao Cheng, Yitao Duan
**arXiv:** [arxiv.org/abs/2611.06043](https://arxiv.org/abs/2611.06043)
**Summary:** Confucius4-R2T2 post-trains Qwen3-ASR-1.7B on 1,500 hours of Chinese and English audio using Longest Stable Prefix labels, producing streaming transcripts that never revise earlier output. Evaluations report recognition close to the full-context base model with low emission lag and transfer beyond the post-training languages, without changing the model architecture.

---

### 9. AgentBaton: Efficient Model Collaboration in Agentic Tasks
**Authors:** Junlong Li, Jindong Jiang, Yonggan Fu, Jiarui Yao, Hanrong Ye, Wonmin Byeon, Peter Belcak, Hao Zhang, Pavlo Molchanov
**arXiv:** [arxiv.org/abs/2610.35959](https://arxiv.org/abs/2610.35959)
**Summary:** AgentBaton learns when a capable model should hand a long-horizon agent task to a cheaper model, using recurring patterns in task progress. Across 11 model pairs and two benchmarks, it reduces API cost by 65.9% on average while largely preserving accuracy, with gains of up to 8.8 percentage points over capable-only execution.

---

### 10. Video-Coder: Reinforcing Agentic Coding for Video Generation
**Authors:** Chaoyang Wang, Sicheng Gao, Junan Hu, Kunyang Li, Dongyang Chen, Yiyang Zhou, Huaxiu Yao, Yong Jae Lee, Radu Timofte, Yuzhang Shang
**arXiv:** [arxiv.org/abs/2611.09894](https://arxiv.org/abs/2611.09894)
**Summary:** Video-Coder trains a coding agent to write and execute dynamic 3D scenes whose rendered draft videos guide downstream video generation. With curated SFT and reinforcement-learning datasets, an interactive rendering harness, and execution-plus-video rewards, it improves Minimax-H3 by approximately 7 points on PhyGenBench and 24 points on VBench-2.0.

---

### 11. PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?
**Authors:** Yue Zhang, Jilei Sun, Liqiang Jing, Yijie Wei, Ruohan Yang
**arXiv:** [arxiv.org/abs/2611.08175](https://arxiv.org/abs/2611.08175)
**Summary:** PCBRouteAgent separates multimodal global PCB routing plans from detailed execution in KiCad, using structured failure feedback to revise guides while preserving accepted routes. On 247 boards, it improves clean-pass rates over the best evaluated baseline by 13.9, 36, and 10 percentage points on the three real-world subsets.

---

### 12. LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time
**Authors:** Teresa Delgado, Hugo Hazard, Martin Benfeghoul, Jun Wang, Zafeirios Fountas
**arXiv:** [arxiv.org/abs/2611.07025](https://arxiv.org/abs/2611.07025)
**Summary:** LowRAM compresses KV caches with cross-layer low-rank keys and per-head predictors that reconstruct values from keys while storing selected residuals. It reports up to 5x higher peak decoding throughput at 4x compression and reaches 26.9x compression with 94.5% of baseline long-context performance when combined with quantization and eviction.

---

### 13. AutoCompress: Automated Hardware-Guided Model Compression
**Authors:** Sheldon Liang, Ali Taghibakhshi, Saurav Muralidharan, Sharath Turuvekere Sreenivas, Ashwath Aithal, Pavlo Molchanov, Nima Tajbakhsh
**arXiv:** [arxiv.org/abs/2611.08290](https://arxiv.org/abs/2611.08290)
**Summary:** AutoCompress uses differentiable architecture search guided by serving-engine cost models to prune language models under hardware-specific latency, throughput, and memory constraints. It improves accuracy over Minitron in local and datacenter evaluations and compresses Nemotron 3.5 Super from 120B to 74B parameters for single-B200 BF16 serving at 128K context while retaining 95% of mean benchmark score.

---

### 14. Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations
**Authors:** Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, Chun-Mei Feng, Qi Zhang, Yirong Chen, Ming Hu
**arXiv:** [arxiv.org/abs/2611.09382](https://arxiv.org/abs/2611.09382)
**Summary:** This study evaluates weight-space programming, in which reasoning agents inspect and modify neural parameters, across 16 editing trajectories, seven benchmarks, and two model scales. Localized edits produce large reported gains and some cross-task transfer, but outcomes vary substantially and six trajectories retain the original weights because improvements cannot be reliably validated.

---

### 15. Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds
**Authors:** Xinjie Lin, Qingle Liu, Wenyi Li, John Lam, Xiaoqiu Wang, Deyao Hong, Mingju Gao, Zheng Jiang, Yizhe Chi, Youjie Zheng, Calvin Xiao, Kaisen Yang, Huan-ang Gao
**arXiv:** [arxiv.org/abs/2611.09017](https://arxiv.org/abs/2611.09017)
**Summary:** Frontier3DBench evaluates coding agents on 145 tasks across nine categories spanning 3D objects, scenes, and interactive open worlds, jointly measuring appearance, structure, and behavior. Across 11 model-harness configurations, reference reconstruction trails text-driven generation, and individually functioning mechanisms often fail to support coordinated activities with persistent state.

---

### 16. Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use
**Authors:** Chuxue Cao, Jingru Zeng, Boqin Yin, Yujin Zhou, Yidan Huang, Sujin Chen, Jinluan Yang, Haoran Li, Yike Guo, Sirui Han
**arXiv:** [arxiv.org/abs/2611.09113](https://arxiv.org/abs/2611.09113)
**Summary:** The Authorization Drift Benchmark contains 648 tasks with both compliant paths and tempting unauthorized shortcuts, testing boundaries across data, tools, scope, and time. Across 13 language models and three frameworks, stronger models exhibit drift rates of 0.43-0.61, often through early data over-collection, although 86.18% of tasks have an observed clean-success trajectory.

---

### 17. Hierarchical Residuals: A Minimalist Decoupling of Residual Width from Compute Width
**Authors:** Ziteng Wang, Jianqiao Lu, Xinyu Ma, Jintao Zhang, Jun Zhu, Yiyuan Ma, Jianfei Chen
**arXiv:** [arxiv.org/abs/2610.41711](https://arxiv.org/abs/2610.41711)
**Summary:** Hierarchical Residuals decouples a transformer's residual-state width from per-layer compute width through wider outer residuals and learned read/write projections at block boundaries. Experiments report a 1.30-fold FLOPs-efficiency improvement from fitted scaling laws and better OLMoE pretraining loss and downstream accuracy using standard operators rather than specialized kernels.

---

### 18. Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters
**Authors:** Constantinos Karouzos, Nikolaos Aletras
**arXiv:** [arxiv.org/abs/2611.09634](https://arxiv.org/abs/2611.09634)
**Summary:** LambdaMix jointly trains one low-rank adapter per objective with group-relative online reinforcement learning, using a preference vector to control both adapter mixing and reward weighting. One training run supports inference-time trade-off changes, with higher reported hypervolume than evaluated conditioned and merging baselines while using fewer completions and adapter parameters than separate GRPO specialists.

---

### 19. "PRISM" Is Not All You Need: Cross-Topic Name Collisions and Scientific Paper Retrieval
**Authors:** Jingjie Ning, Xueqi Li, Yibo Kong
**arXiv:** [arxiv.org/abs/2611.01362](https://arxiv.org/abs/2611.01362)
**Summary:** An analysis of 564,861 AI-related arXiv records finds cross-topic scientific name collisions grew 4.33-fold from a pooled 2020-2022 reference to 2026. Retrieval experiments show that shared names retain identification deficits under lexical and dense search despite topic clues, while contextual language-model ranking helps resolve ambiguity.

---

### 20. PREEN: Exemplar-Based Color Style Transfer with Smartphone Editor Presets
**Authors:** Beomjin Ahn
**arXiv:** [arxiv.org/abs/2610.36896](https://arxiv.org/abs/2610.36896)
**Summary:** PREEN transfers color style by predicting the 29 slider parameters of a deterministic smartphone image editor rather than generating a raster image, using teacher-derived pseudo-presets and LoRA refinement. It reports strong fidelity on PST50 with sub-second on-device prediction and an inference-time strength control that spans faithful reference matching and standalone-photo preference without retraining.
