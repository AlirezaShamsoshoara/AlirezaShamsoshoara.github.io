---
title: "Daily AI Papers — October 20, 2026"
date: 2026-10-20
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-20/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robotics
  - multimodal-ai
---

### 1. Scaling Parameter-Efficient Fine-Tuning for Brain Encoding
**Authors:** Zhuofan Josh Ying, Guanglong Sun, Nolan Ho, Kieran Liu, Rui Yang, Andrew Chen, Nikolaus Kriegeskorte, Pony Ma, Hossein Adeli
**arXiv:** [arxiv.org/abs/2610.26802](https://arxiv.org/abs/2610.26802)
**Summary:** BrainLoRA uses parameter-efficient low-rank adaptation and causal multi-timepoint prediction to tune multimodal backbones as large as 104B parameters for brain encoding. It improves results across nine backbones, reaches the best published Algonauts 2025 performance on Qwen3-Omni, and enables a 200-plus-model ensemble through a shared multi-LoRA kernel.

---

### 2. MemT-1.0: Towards Memory-Native Evolution
**Authors:** Zhiyu Li, Zeyu Zhang, Linyun Liu, Yiwei Bu, Chenyang Xi, Xichong Zhang, Yi Yu, Yu Yu, Zhichen Liu, Yuxiao Yi, Chunyu Li, Haoran Liu, Zhenkai Ding, Le Zhou, Juncheng Zhang, Boyu Chen, Zehao Lin, Guorui Li, Renyu Fu, Ji Li, Youyang Xia, Jiajun Shen, Harvey Li, Jingsong Zhou, Helan Hu, Tong Shen, Tianxiao Xu, Chenye Han, Weijie Li, Zhongquan Zhou, Hongming Xu, Yuekeng Li, Erenkai Zhu, Peng Yu, Wenhao Li, Jingyi Kang, Xixuan Hao, Xuzhou Zhu, Can Chen, Jiawei Liu, Chen Jiang, Tao Jiang, Fangwei Xiang, Zepeng Yao, Kai Chen, Guang Yang, Mingfei Lu, Chunhui Li, Zhengxuan Jiang, Bo Tang, Shiyu Zhan, Yihang Sun, Jie Chu, Wenjun Xiong, Zhenxiang Hua, Chen Lin, Detong Su, Dongyu Deng, Qiuping Ding, Guofeng Ding, Si Chen, Guohua Wen, Xu Chen, Zhi-Qin John Xu, Ying-Cong Chen, Ningyu Zhang, Haofen Wang, Muning Wen, Haotian Chen, Wentao Zhang, Xuanhe Zhou, Rita Zhang, Junchi Yan, Feiyu Xiong
**arXiv:** [arxiv.org/abs/2610.26825](https://arxiv.org/abs/2610.26825)
**Summary:** MemT-1.0 makes memory part of foundation-model computation through Gated DeltaNet-2, stable token-level updates, and a Mixture-of-Storage design trained on 34B tokens. At 128K history length, its Nano model reports about 1.86 times faster end-to-end inference and 66 times less persistent storage than a full-context KV cache while improving agent success with internalized procedural experience.

---

### 3. Learning from Fleet Experience: A Collective Learning Paradigm for Robots
**Authors:** Chao Yu, Shu'ang Yu, Hao Lin, Hongzhi Zang, Yuxiang Yan, Chenxi Jiang, Zhen Guo, Chuankang Li, Yihao Chen, Xin Xu, Xu Fu, Jiakai Zhou, Liangzhi Shi, Hongyi Ren, Yiwei Liu, Jing Wu, Yuanqing Wang, Chen Wu, Bo Dai, Chunyu Yang, Hongliang Huang, Shuoyu Yue, Weiqi Yin, Yinuo Chen, Ruihua Chen, Chunyang Zhu, Han Xiao, Yanghao Li, Ruipu Wu, Zhikai Cai, Xiu Chen, Xu Tan, Yuchen Yan, Jialin Zhang, Wen Zeng, Yiming Zhou, Zixiao Huang, Guanghui Ren, Quanlu Zhang, Boxun Li, Maoqing Yao, Yu Wang
**arXiv:** [arxiv.org/abs/2610.25736](https://arxiv.org/abs/2610.25736)
**Summary:** Collective experience learning lets deployed robots pool successful execution traces, while failure-guided retrieval fine-tuning uses relevant fleet segments as supervision without new expert corrections. Across five real manipulation tasks it reaches 93.3-99.2% success, including an increase from 79.2% to 98.3% on phone packaging when learning from 96 robots.

---

### 4. Holi-World: Building Holistic World Intelligence from Human-Ego Experience
**Authors:** Hao Li, Xiyuan Zheng, Yuanyuan Gao, Yalun Dai, Xinhao Ji, Xuan-Li Chen, Jing Zhao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
**arXiv:** [arxiv.org/abs/2610.26549](https://arxiv.org/abs/2610.26549)
**Summary:** HOLI-WORLD links egocentric capture, automated static and dynamic world records, grounded training data, model learning, and independent evaluation in one ecosystem. Its roughly 80,000 QA pairs improve a 4B vision-language model's spatial and temporal reasoning, while evaluations show strong static perception and dynamic tracking across multiple datasets.

---

### 5. EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience
**Authors:** Xinhao Ji, Hui En Pang, Hao Li, Kairui Hu, Jiner Wang, Mingze Sun, Ziang Cao, Yalun Dai, Thang Luu, Qin Ma, Hongyi Chen, Yukang Cao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
**arXiv:** [arxiv.org/abs/2610.26625](https://arxiv.org/abs/2610.26625)
**Summary:** EgoXperience jointly reconstructs camera motion, scene geometry, hands, and objects from monocular egocentric video in a shared metric world frame. Its automatic annotation engine produces a 50-hour, six-million-scale dataset, and the resulting model cuts camera, hand, and depth errors by 68.9%, 65.6%, and 42.9% against the strongest evaluated baselines.

---

### 6. OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners
**Authors:** Peisong Wang, Feixue Liu, Yize Meng, Bowen Liu, Ruoyu Chen, Gaoyang Dai, Xing He, Aiqian Li, Fengchi Yuan, Aochuan Chen, Chenyi Zi, Yuhan Li, Hongchuan Zeng, Yimo Yan, Nuo Chen, Jie Fu, Zuo-Jun Max Shen, Yong-Hong KUO, Jia Li
**arXiv:** [arxiv.org/abs/2610.24087](https://arxiv.org/abs/2610.24087)
**Summary:** OR-License evaluates coding agents on 31 de-identified operations-research engagements worth $3.68 million, preserving original client materials, data, deliverable formats, and information boundaries. Although several models exceed experts on conditional objective quality, none matches expert deployment-adjusted quality; the strongest primary Claude Code setup attains 88.39% strict feasibility and a 0.87 DAQ.

---

### 7. ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation
**Authors:** Yihui Yang, Yuanhong Yu, Jiawei Wang, Zhongrui Yu, Jia Shi, Kun Zhan, Ruizhen Hu, Xiaowei Zhou, Yu Liu, Sida Peng
**arXiv:** [arxiv.org/abs/2610.25690](https://arxiv.org/abs/2610.25690)
**Summary:** ScaleNav pretrains goal-directed visual dynamics on Internet egocentric video, aligns those dynamics with simulated robot actions, and jointly fine-tunes the full navigation system. It reaches 86.5% success on a Short-Horizon OVON adaptation and 94.9% on HabitatGS-LN, with real-quadruped experiments supporting transfer to physical navigation.

---

### 8. SpecMRL: Redesign Matryoshka Representation Learning within Parametric Spectrum
**Authors:** Zhongxin Chen, Songhao Wu, Heng Cui, Cong Li, Xiao Zhou, Rui Yan
**arXiv:** [arxiv.org/abs/2610.26824](https://arxiv.org/abs/2610.26824)
**Summary:** SpecMRL reorganizes Matryoshka representations in a learned, parameter-derived spectral basis ordered by feature importance so short prefixes retain more useful information. On MTEB it beats standard MRL at every reduced dimension tested and surpasses full-dimensional MRL while using only half the embedding dimensions.

---

### 9. OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory
**Authors:** Yu Zhou, Cheng-Fu Yang, Rui Sun, Di Wu, Sibo Peng, Mingyang Zhang, Zhen Yang, Ruiyi Zhang, Nanyun Peng, Zhe Gan, Kai-Wei Chang
**arXiv:** [arxiv.org/abs/2610.26860](https://arxiv.org/abs/2610.26860)
**Summary:** OpenVLHarness gives multimodal models a consistent capability layer for heterogeneous tools plus persistent memory for images, structured data, and web evidence that generated programs can combine. Across 22 benchmarks and eight backbones it improves average scores by 9.7-12.6 points, and its GPT-6 Luna configuration beats higher-effort alternatives while using at most 37% of their model-token cost.

---

### 10. Self-Evolving Coding Agents via Harness-Policy Optimization
**Authors:** Zhepei Wei, Wenlin Yao, Baolin Peng, Danqing Wang, Qianhui Wu, Hao Cheng, Yu Meng, Jianfeng Gao
**arXiv:** [arxiv.org/abs/2610.22791](https://arxiv.org/abs/2610.22791)
**Summary:** Self-HPO recursively alternates between policy-proposed harness improvements and reinforcement-learning updates to the coding policy, using newly hard tasks to focus the next search round. It raises Qwen3.5-35B-A3B's average resolve rate from 57.8% to 64.8%, with gains in both reliability and capability that exceed optimizing either component alone.

---

### 11. CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents
**Authors:** Zhongwei Xie, Yiming Du, Jiaxin Bai, Baixuan Xu, Chunyang Li, Xiyu Ren, Wei Fan, Tianshi Zheng, Weizhi Du, Jingqiao Yu, Xingsu Li, Zhaowei Wang, Yangqiu Song
**arXiv:** [arxiv.org/abs/2610.24960](https://arxiv.org/abs/2610.24960)
**Summary:** CoworkEnv synthesizes coherent, executable training environments for long-horizon AI coworkers from workflow requirements, programmatic validation, repaired specifications, and teacher demonstrations. Supervised fine-tuning raises Qwen3-VL-8B-Instruct's mean Claw-Eval score from 46.6 to 64.1, including a 31.9-point gain on multi-turn tasks, while reinforcement-learning runs provide early evidence of further policy improvement.

---

### 12. MT Forcing: Towards Stable and Consistent Multi-Turn Image Editing with Autoregressive Diffusion
**Authors:** Houyuan Chen, Fanzhou Wang, Xiangyu Fan, Zesong Qiu, Yukun Wei, Songlin Yang, Zhitao Yang, Lvmin Zhang, Pei Yang, Hao Zhao, Lei Yang, Anyi Rao
**arXiv:** [arxiv.org/abs/2610.25404](https://arxiv.org/abs/2610.25404)
**Summary:** MT Forcing stabilizes autoregressive-diffusion image editing across multiple instructions by distilling single-turn cumulative edits and adding teacher-forced guidance on reference trajectories. The combination limits recursive artifact buildup and unintended changes to preserved regions, producing better visual quality and cross-turn consistency.

---

### 13. Interlock: From Local Correctness to Task Completion in Long-Horizon Agents
**Authors:** Linji Hao, Yanji He, Zihan Wang, Hansi Yang, Jiayuan Zhang, Hongyan Hao, Qi Gu, Yan Feng, Han Wu
**arXiv:** [arxiv.org/abs/2610.19686](https://arxiv.org/abs/2610.19686)
**Summary:** Interlock represents long-horizon tasks as typed completion graphs whose edges connect evidence, decisions, joint constraints, and every required downstream effect. After validating generated workspaces and retaining fully verified agent trajectories, fine-tuning improves task completion across AutomationBench, JobBench, and Harvey LAB on two Qwen3.6 backbones.

---

### 14. AnyGoal: On World Model Generalization Beyond Expert Rollouts
**Authors:** Heejeong Nam, Divyat Mahajan, Quentin Le Lidec, Randall Balestriero, David Klindt
**arXiv:** [arxiv.org/abs/2610.26844](https://arxiv.org/abs/2610.26844)
**Summary:** AnyGoal tests whether world models can recombine familiar state and action factors into valid dynamics for goal-shifted tasks that were underrepresented in expert rollouts. Across several environments and model families, current systems consistently fail these compositional generalization cases, revealing a gap between fitting expert trajectories and supporting reliable new planning objectives.

---

### 15. Kronecker Delta Rule for Long Context Linear Attention
**Authors:** Anamaria-Roberta Hartl, Levente Zólyomi, Michael List, Günter Klambauer, Sebastian Böck, Sepp Hochreiter
**arXiv:** [arxiv.org/abs/2610.26834](https://arxiv.org/abs/2610.26834)
**Summary:** KronLSTM applies a Kronecker Delta Rule to revise targeted associations along a single matrix-space direction, reducing interference with previously stored information. Its memory dynamics remain bounded without extra normalization, and experiments show competitive or stronger results than existing linear-attention systems, especially on long-context benchmarks.

---

### 16. RoAR-VAE: Improving Latent Diffusability through Robust Prediction
**Authors:** Yang Yue, Fangyun Wei, Yitong Wang, Jinjing Zhao, Henry Zheng, Dong Chen, Gao Huang
**arXiv:** [arxiv.org/abs/2610.26216](https://arxiv.org/abs/2610.26216)
**Summary:** RoAR-VAE trains visual latents so semantic features and clean images remain recoverable after corruption, preserving both high-level structure and fine detail for downstream diffusion. Under matched budgets it improves average generation benchmarks by 2.19 points over the strongest tokenizer baseline and raises small-text reconstruction accuracy by 16.93 points over FLUX.1-VAE.

---

### 17. AdaExploreBench: Benchmarking LLM Agents for Proactive Exploration and Test-time Adaptation in Evolving Environments
**Authors:** Rui Wang, Zishen Lai, Jiayu Liu, Cheng Qian, Jeonghwan Kim, Heng Wang, Xuejun Zhang, Jiateng Liu, Bingxuan Li, Shujin Wu, Qing Zong, Tianshi Zheng, Chunyang Li, Qihan Lin, Chen Li, Dadi Guo, Xiusi Chen, Yangqiu Song
**arXiv:** [arxiv.org/abs/2610.25950](https://arxiv.org/abs/2610.25950)
**Summary:** AdaExploreBench hides environment rules and changes them without notice to test whether agents proactively gather evidence, detect stale knowledge, and adapt at inference time. GPT-6 Sol reaches only 61.9% calibrated accuracy, while sufficient evidence or removal of rule drift improves average performance by nearly 10%, identifying exploration rather than reasoning as the main bottleneck.

---

### 18. MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents
**Authors:** Haozhen Zhang, Haodong Yue, Quanyu Long, Jianzhu Bao, Qingyuan Liu, Tao Feng, Bohan Liu, Weida Liang, Wenya Wang
**arXiv:** [arxiv.org/abs/2610.06830](https://arxiv.org/abs/2610.06830)
**Summary:** MemPilot trains a multi-step policy to choose between ordinary retrieval and query-specific curation of raw multimodal history by heterogeneous language and vision models. By controlling evidence volume, instructions, model choice, and visual access under separate performance, cost, and latency objectives, it produces broader trade-off frontiers on five agent-memory benchmarks than existing baselines.

---

### 19. HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs
**Authors:** Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen, Honglin Lin, Junru Lu, Zhongxia Chen, Shuo Yang, H. Vicky Zhao, Jie Tang
**arXiv:** [arxiv.org/abs/2610.26770](https://arxiv.org/abs/2610.26770)
**Summary:** HarnessPro recursively improves agent harnesses with LLM-generated tests and specialized diagnosis, planning, and implementation agents, then selects lite, balanced, and heavy variants along a performance-cost frontier. On three coding benchmarks, its heavy mode with GPT-5.5 and Codex gains 2.0 pass-rate points while reducing per-task cost by 26.1% relative to RHO.

---

### 20. InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation
**Authors:** Yi-Chuan Huang, Hao-Jen Chien, Zheng-Hui Huang, Yu-Lun Liu, Kaipeng Zhang, Zhixiang Wang
**arXiv:** [arxiv.org/abs/2610.26853](https://arxiv.org/abs/2610.26853)
**Summary:** InfiniDream combines symbolically constrained asset generation with semantic scene planning and deterministic frustum-guided placement to create editable, seed-diverse photorealistic 3D worlds. Evaluations on 100 object and 20 scene tasks show gains across four perceptual metrics, with ablations, diversity analysis, and human preferences supporting the full pipeline.
