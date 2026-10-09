---
title: "Daily AI Papers — October 10, 2026"
date: 2026-10-10
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-10/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robotics
  - computer-vision
---

### 1. Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching
**Authors:** Luping Liu, Bingyi Kang, Yifan Wang, Dong Xu
**arXiv:** [arxiv.org/abs/2610.12421](https://arxiv.org/abs/2610.12421)
**Summary:** FreeMatching combines generative and semantic foundation representations with heterogeneous supervision to match dense correspondences even when image editing or reference-guided generation breaks ordinary motion and geometry assumptions. A single model improves difficult identity-preserving matches while remaining competitive on classical benchmarks, and its scores correlate with human judgments of identity preservation.

---

### 2. Pumpire: Unified Benchmark for Metric Distance Estimation
**Authors:** Siyu Chen, Zehan Wang, Jiayang Xu, Yihan Wu, Jialei Wang, Junming Chen, Ziang Zhang, Yutong Ying, Zhou Zhao
**arXiv:** [arxiv.org/abs/2610.12423](https://arxiv.org/abs/2610.12423)
**Summary:** Pumpire directly evaluates point-to-point metric distance estimation in image- and video-level 3D foundation models instead of scoring depth, camera intrinsics, or point-cloud similarity separately. Its pumpire-6k dataset covers 100 real scenes, 6,400 frames, and physically measured distances, supporting comparison across 29 representative model configurations.

---

### 3. Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement
**Authors:** Kairui Hu, Siyuan Hu, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
**arXiv:** [arxiv.org/abs/2610.12369](https://arxiv.org/abs/2610.12369)
**Summary:** Code-Only-as-Policy represents robot, environment, and task state in reusable code so decisions can run without a vision-language model or vision-language-action model in the test-time control loop. A coding agent can recursively extend the shared library, which reaches 70.24% success across RoboDojo's 42 bimanual tasks while remaining explicit, fast, and controllable.

---

### 4. SparseEngine: Sparse-First Inference Engine
**Authors:** Jitai Hao, Quansheng Gu, Qiang Huang, Jun Yu
**arXiv:** [arxiv.org/abs/2609.39068](https://arxiv.org/abs/2609.39068)
**Summary:** SparseEngine provides a shared lifecycle contract that lets sparse-attention methods control their own key-value representations and computation while using common serving infrastructure. Across 15 methods, it reports more than 10 times higher throughput with KV eviction, over 2.5 times faster decoding than vLLM at matched concurrency, and over 2 times end-to-end speedup on agent benchmarks.

---

### 5. OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning
**Authors:** Zhongyu Yang, Jiale Tao, Ruitao Chen, Zuhao Yang, Yingfang Yuan, Xueliang Zhao, Auden, Kai Wang, Shuai Shao, Biao Wang, Steve Yves, Qinglin Lu
**arXiv:** [arxiv.org/abs/2610.12458](https://arxiv.org/abs/2610.12458)
**Summary:** OmniCapBench replaces whole-caption scoring with atomic, verifiable units covering entity references, visual shots, and audio events, combining deterministic checks with localized semantic comparisons. Tests on 786 densely annotated videos reveal that frontier multimodal models have strong local perception but weak long-horizon reasoning, especially for identity consistency and cross-modal alignment.

---

### 6. Do LLMs Understand Sequential Structure? A Controlled Study of Inference and Generation
**Authors:** Jerry Wang, Zhengxiang Wang, Ting Yu Liu, Hsin-Ling Hsu, Yi-Cheng Lai, Tengfei Ma
**arXiv:** [arxiv.org/abs/2610.04977](https://arxiv.org/abs/2610.04977)
**Summary:** Controlled Rock-Paper-Scissors and stochastic n-gram tasks test whether language models recover latent sequential rules rather than merely matching marginal action frequencies. Longer context does not improve identification, correct recognition does not guarantee faithful simulation, and higher-order dependencies sharply degrade rule recovery.

---

### 7. Opera: A Verbal Critic Framework for Long-horizon Coding Agents
**Authors:** Kai Mei, Zhiyuan Hu, Yutong Dai, Juntao Tan, Yifan Zhang, Dingjie Song, Dimitris N. Metaxas, Silvio Savarese, Ran Xu, Zeyuan Chen
**arXiv:** [arxiv.org/abs/2609.33987](https://arxiv.org/abs/2609.33987)
**Summary:** Opera treats each critique as a persistent note, auditing it against evidence and following the coding agent until the underlying problem is actually resolved. It improves resolve rates across Terminal-Bench 2.1, SWE-Bench Pro, and DeepSWE, while its guided rollouts also provide effective approximately on-policy fine-tuning data.

---

### 8. A GPU-Parallel Framework for Heterogeneous Multi-Task Reinforcement Learning
**Authors:** Rui Zhang, Qiwei Wu, Zhengyu Zhang, Tao Li, Hongyu Zhou, Xiang Li, Yunrong Guo, Junjie Lai, Renjing Xu, Weihua Zhang
**arXiv:** [arxiv.org/abs/2606.03335](https://arxiv.org/abs/2606.03335)
**Summary:** Hebero is an Isaac Lab benchmark for jointly training one policy across 40 heterogeneous robot-manipulation tasks with GPU-parallel simulation. Its demonstration-guided IW-ABC method reaches 90.1% mean success from state inputs and 93.5% from visual inputs, and one simulation-trained policy transfers to four tasks on a physical Piper robot.

---

### 9. ReSPO: Reshaped Sequence Policy Optimization for Gradient Starvation in Off-Policy Learning
**Authors:** Yihang Chen, Yuanhao Ban, Cho-Jui Hsieh
**arXiv:** [arxiv.org/abs/2609.35433](https://arxiv.org/abs/2609.35433)
**Summary:** ReSPO addresses sign-dependent gradient starvation caused by clipped policy optimization when reinforcement learning reuses rollouts from older policies. Its smooth two-branch sequence-level kernel preserves learning signals from under-generated positive trajectories and suppresses over-generated negatives, improving optimization and held-out results on dense and mixture-of-experts Qwen3 models.

---

### 10. Mara Chain: Rethinking Failure as a Stepping Stone for AI System Auto-Evolution
**Authors:** Yubin Lyu, Fu Li, Jiawei Fei, Yang Zhao, Weixing Mei, Yinan Wu
**arXiv:** [arxiv.org/abs/2609.35855](https://arxiv.org/abs/2609.35855)
**Summary:** Mara Chain retains rejected prompt, skill, harness, and code configurations and iteratively refines them using evidence from earlier failures instead of discarding them. Across AppWorld, TerminalBench 2.1, and MuSiQue, it improves task performance with fewer rollouts and substantially outperforms several artifact-optimization baselines.

---

### 11. Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station
**Authors:** Wenyu Du, Stephen Chung
**arXiv:** [arxiv.org/abs/2610.08927](https://arxiv.org/abs/2610.08927)
**Summary:** Station places multiple agents in an open-world scientific ecosystem and adds supervision plus periodic meta-reflection to sustain exploration when intermediate metrics are absent. On tasks derived from three ICLR oral papers, it rediscovers 62.7% of withheld findings on average, far above the reported multi-agent and AI Scientist baselines.

---

### 12. REMORY: Learning Residual Memory for Context Compaction
**Authors:** Hanchen Xia, Baoyou Chen, Yutang Ge, Naihao Deng, Senqiao Yang, Zilong Dong, Weihao Yuan, Siyu Zhu
**arXiv:** [arxiv.org/abs/2610.11287](https://arxiv.org/abs/2610.11287)
**Summary:** REMORY augments a textual history summary with a bounded sequence of learned soft memory tokens that help a frozen language model approximate full-context continuations. It approaches the full-context SummHay score with only 5.2% of the input positions and reduces repeated tool outputs and tool errors on long-horizon agent benchmarks.

---

### 13. A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization
**Authors:** Ming Chen, Rong-Xi Tan, Ke Xue, Yu-Jie Zhou, Taiye Lu, Zhi-Xuan Gao, Peng Xie, Zijun Shen, Chen Lu, Haopu Shang, Chao Qian
**arXiv:** [arxiv.org/abs/2610.12183](https://arxiv.org/abs/2610.12183)
**Summary:** AgenticBBO-Bench compares language-model agents under one finite-budget protocol across synthetic functions, hyperparameter optimization, database tuning, chip design, and molecular design. Agentic approaches beat direct language-model methods in all five domains and the best numerical optimizer in four, while ablations clarify the roles of tools, task semantics, priors, and model-driven search.

---

### 14. SpaceFlow: Locally Controllable 3D Generation
**Authors:** Neil De La Fuente, Joan Lafuente, Mukhammadali Sayfiddinov, Felicia Scharitzer, Marc Pollefeys, Ata Celen, Sayan Deb Sarkar, Elisabetta Fedele
**arXiv:** [arxiv.org/abs/2610.12399](https://arxiv.org/abs/2610.12399)
**Summary:** SpaceFlow is a training-free pipeline that assigns local geometry-control levels and text or image cues to primitive parts of a generated 3D object. It preserves strict geometry where requested, allows plausible completion elsewhere, and limits appearance leakage between parts while retaining competitive overall quality.

---

### 15. WorldGuide: Goal-Directed Video World Model for Procedural Task Execution
**Authors:** Ankan Deria, Komal Kumar, Hisham Cholakkal, Fahad Shahbaz Khan, Salman Khan
**arXiv:** [arxiv.org/abs/2610.12459](https://arxiv.org/abs/2610.12459)
**Summary:** WorldGuide closes the loop between planning and generation by predicting an atomic action, generating its video outcome, and using that result to choose the next action or stop. Trained on a new benchmark of roughly 59,000 step-annotated videos, it improves task success over a strong video model even when that baseline receives reference action plans.

---

### 16. Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models
**Authors:** Hongxing Li, Yixin Li, Dingming Li, Zixuan Wang, Yuchen Yan, Wenqi Zhang, Weiming Lu, Yongliang Shen
**arXiv:** [arxiv.org/abs/2610.12355](https://arxiv.org/abs/2610.12355)
**Summary:** Geometry-Privileged Distillation routes compact depth, semantic, and bird's-eye-view cues to a teacher during on-policy training while leaving the deployed vision-language model RGB-only. Applied only to incorrect trajectories, the privileged loss improves spatial reasoning over both GRPO and answer-privileged self-distillation across several benchmarks.

---

### 17. SpecFold: Folding Multi-Branch Redundancy for Faster Speculative Decoding in Diffusion Language Models
**Authors:** Chung-En Ho, Weiyu Sun, Cheng-Jhih Shih, He Li, Yong Liu, Yingyan Celine Lin
**arXiv:** [arxiv.org/abs/2610.04875](https://arxiv.org/abs/2610.04875)
**Summary:** SpecFold exploits hidden-state similarity among speculative draft branches in diffusion language models using token-level residual gating and selective reuse of parent attention and feed-forward computation. A Triton implementation delivers up to 1.64 times the throughput of Spiffy and 1.99 times vanilla decoding across two model families while preserving comparable task performance.

---

### 18. Incremental Open-Ended Deep Research with Structured Harness
**Authors:** Meilin Chen, Hongyuan Bao
**arXiv:** [arxiv.org/abs/2610.11566](https://arxiv.org/abs/2610.11566)
**Summary:** Incremental-OEDR treats a report as evolving research state, using a structured harness of outlines, sections, retrieval, and persistent evidence to update only what new information changes. Across ten-year evaluation chains, it maintains competitive quality while improving continuity and cutting token use by up to 33% and search calls by 61% relative to rebuilding reports from scratch.

---

### 19. One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts
**Authors:** Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
**arXiv:** [arxiv.org/abs/2610.12448](https://arxiv.org/abs/2610.12448)
**Summary:** reViT repeatedly applies one Transformer block while programming each recurrent depth as a convex combination of a small shared feed-forward expert bank. It matches strong full-depth vision encoders with about 70% fewer stored parameters, transfers across vision tasks, and can run one checkpoint at multiple resampled depths.

---

### 20. Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict
**Authors:** Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu, Jingyu Zhang, Jie Gao, Mark Dredze, Daniel Khashabi
**arXiv:** [arxiv.org/abs/2610.12360](https://arxiv.org/abs/2610.12360)
**Summary:** This work evaluates whether agents identify, resolve, and communicate uncertainty when retrieved evidence conflicts with parametric knowledge or other sources. Four agents often detect conflicts early but fail to preserve or disclose unresolved uncertainty later, and interventions that improve epistemic humility can reduce task accuracy.

---
