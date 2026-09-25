---
title: "Daily AI Papers — September 25, 2026"
date: 2026-09-25
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-25/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - world-models
  - ai-agents
  - video-generation
---

### 1. Training Object Permanence in World Models
**Authors:** Haotian Zhang, Fengyuan Yu, Dezhi Luo, Haoran Sun, Zehong Zhao, Qingying Gao, Yihan Li, Siyuan An, Huayi Qin, Yilan Zhang, Zhengze Jiang, Pinyuan Feng, Renrui Zhang, Ziyu Guo, Letian Wang, Mengyue Yang, Kangfu Mei, Maijunxian Wang, Ran Ji, Vikash Kumar, Freda Shi, Chandra Sripada, Vincent C. Muller, Philip Torr, Alan Yuille, Nikolaus Kriegeskorte, Felix Juefei-Xu, Lvmin Zhang, Jieneng Chen, Yilun Du, Hokin Deng
**arXiv:** [arxiv.org/abs/2609.28654](https://arxiv.org/abs/2609.28654)
**Summary:** WROP supplies 150 cognitive-science-inspired tasks, a 1.5-million-sample training corpus, and a 300-question exam for measuring object permanence in video world models. Its 16B PWM-WROP model ranked first among continuation models and third overall in a blind pairwise Elo evaluation of 14 systems.

---

### 2. Your Transformer Can Hold Two Thoughts at Once: Evidence of Linear Superposition in LLMs
**Authors:** Pavel Tikhonov, Anton Korznikov, Matvey Mikhalchuk, Nikita Dragunov, Temurbek Rahmatullaev, Polina Druzhinina, Anton Razzhigaev, Ivan Oseledets, Elena Tutubalina
**arXiv:** [arxiv.org/abs/2609.29845](https://arxiv.org/abs/2609.29845)
**Summary:** The authors find that Transformers can approximately superpose the next-token distributions of two linearly combined text streams, an architectural property they call the Superposition Linearity Hypothesis. Lightweight fine-tuning restores this behavior after pretraining weakens it, and guided decoding extracts two coherent continuations from one forward pass.

---

### 3. WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation
**Authors:** Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong
**arXiv:** [arxiv.org/abs/2609.30221](https://arxiv.org/abs/2609.30221)
**Summary:** WanPE is a 397B prompt-enhancement model trained on 1.05 million real-world videos to turn user requests into shot-level cinematic plans while preserving intent with Semantic-Consistency GRPO. When paired with Wan3.0, it improved human preference by 10.66-18.84 points for 5-15-second videos and 50.86 points in the 30-second arena.

---

### 4. OmniEcho: Spatial Audio Understanding for Embodied Agents
**Authors:** Ruixun Liu, Yuxuan Wang, Jiacheng Xie, Yuhuan You, Donghua Cai, Junming Lin, Xiong-Hui Chen, Zhifang Guo, Yunfei Chu, Qize Yang, Xize Cheng, Jin Xu, Yiwu Zhong
**arXiv:** [arxiv.org/abs/2609.23407](https://arxiv.org/abs/2609.23407)
**Summary:** OmniEchoBench evaluates spatial audio-visual perception and sound-guided navigation across 197 real scenes, 2,972 question-answer pairs, and 900 navigation samples. The OmniEcho model adds a first-order ambisonics spatial encoder to a semantic audio pathway, achieving state-of-the-art spatial perception and navigation performance close to traditional vision-language navigation.

---

### 5. Agent-Editing World Model: Rethinking World Modeling for LLM Agents
**Authors:** Shuang Sun, Guoxin Chen, Fanzhe Meng, Jia Deng, Huatong Song, Jinhao Jiang, Wayne Xin Zhao, Hongteng Xu, Ji-Rong Wen
**arXiv:** [arxiv.org/abs/2609.28416](https://arxiv.org/abs/2609.28416)
**Summary:** The Agent-Editing World Model judges actions and revises contaminated reasoning states rather than trying to reconstruct high-entropy tool responses that an agent can observe directly. Its EditAct integration improved six agent benchmarks by 3.2-6.7 points, while verified-trajectory fine-tuning beat Self-RFT by 2.2-2.6 points across three domains.

---

### 6. Parts-of-Speech as Emergent Categories in SAE Latent Space
**Authors:** Alessandro Bondielli, Lucia Passaro, Serena Auriemma, Alessandro Lenci
**arXiv:** [arxiv.org/abs/2609.29362](https://arxiv.org/abs/2609.29362)
**Summary:** Sparse-autoencoder activations make part-of-speech distinctions highly recoverable without reducing them to lexical memorization or one-latent-per-category features. Instead, grammatical categories occupy compact, stable, and partially overlapping groups of sparse latents, with different structures for open and closed classes.

---

### 7. Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents
**Authors:** Tingyu Qu, Weigao Sun, Yuecheng Liu, Yucheng Zhao, Yi Zhu, Yifeng Ding, Qiyi Wang, Sihan Cao, Pengkun Jiao, Hanlei Xie, Xiongwei Wu, Qichao Wang, Haodong Zhang, Jiajun Liu, Yuhao Wang, Yuqing Xie, Junpeng Zhao, Long Chen, Ming Ma, Sihan Yang, Ziwang Zhao, Yanhao Jia, Liangquan Gong, Feida Zhu, Yiran Zhong, Steven Hoi
**arXiv:** [arxiv.org/abs/2609.29892](https://arxiv.org/abs/2609.29892)
**Summary:** Qwen-Planner-Agent closes the loop among agent-generated mobile-task data, supervised and reinforcement-learning training, and deployment feedback through a shared action-feedback-verification contract. It led MobilePA-Bench among evaluated systems, improved tool use, memory, skills, and sub-agent coordination over its base model, and transferred gains to non-mobile agent benchmarks.

---

### 8. IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis
**Authors:** Xingyu Wu, Yuchen Yan, Zhengxi Lu, Siqi Chen, Xin ZHANG, Aiting Liu, Chao Deng, Jie Liu, Jin Ma, Jian Shao, Jun Xiao, Yongliang Shen
**arXiv:** [arxiv.org/abs/2609.29444](https://arxiv.org/abs/2609.29444)
**Summary:** IterSynth separates deep-search planning from evidence synthesis and keeps an evolving summary as persistent state, reducing role coupling and noisy context growth. Its role-specific policy optimization helped an 8B model average 50.7 across five long-horizon search benchmarks, 4.2 points above the strongest prior model of comparable size.

---

### 9. Coding Agents for Generalized Task and Motion Planning Problems
**Authors:** Matteo Merler, Bowen Li, Josh Roy, Yichao Liang, Qianwei Wang, Yixuan Huang, Tom Silver
**arXiv:** [arxiv.org/abs/2609.30233](https://arxiv.org/abs/2609.30233)
**Summary:** This study asks coding agents to synthesize reusable programs for generalized task-and-motion planning using only task descriptions, simulator access, and a fixed development budget. Across 28 environments and 98,000 held-out episodes, three agent configurations achieved 56%-95% mean success and all surpassed hand-engineered planners at 47% on the comparable subset.

---

### 10. Neural Spectral Capacity: Measuring and Designing Architectures from Network Specification Alone
**Authors:** Chenyu Zhu, Ruoyu Zhao, Zhichao Lu
**arXiv:** [arxiv.org/abs/2609.23087](https://arxiv.org/abs/2609.23087)
**Summary:** Neural Spectral Capacity is a closed-form, architecture-aware score derived from weight-matrix spectra that can be computed from a network specification without data, gradients, or model instantiation. Its exact dynamic-programming optimizer found strong Transformer designs in seconds and selected a 5.7B LLaMA pruning configuration roughly 5,900 times faster than the strongest training-free proxy baseline.

---

### 11. Rufus-Air: An Open LLM Post-Training Recipe
**Authors:** Chia-Yuan Chang, Renyuan Cheng, Rui Feng, Xiaotian Han, Yuan He, Hongye Jin, Linwei Li, Shiyang Li, Fenglin Liu, Xin Liu, Priyanka Nigam, Haoyang Wen, Zhenghao Xu, Zhuocheng Xu, Bing Yin, Qingyu Yin, Chao Zhang, Rongzhi Zhang, Zhihan Zhang, Zixuan Zhang, Zixuan Zhang, Tuo Zhao
**arXiv:** [arxiv.org/abs/2609.29421](https://arxiv.org/abs/2609.29421)
**Summary:** Rufus-Air documents an open eight-stage post-training pipeline for GLM-4.5-Air-Base spanning supervised fine-tuning, specialized reinforcement learning, agent training, and RLHF. Built from open-source components and public data, the resulting model improves on the official GLM-4.5-Air post-trained release and remains competitive with similarly sized open models.

---

### 12. ExplorationBench: Measuring AI Systems' Exploration in Verifiable Alien Worlds
**Authors:** Ming Zhang, Zhenghao Xiang, Peizhong Gao, Yujiong Shen, Yuhui Wang, Zhonghan Yue, Shihan Dou, Zhangyue Yin, Junjie Ye, Shichun Liu, Weihuang Zheng, Jiahao Chen, Jiayi Chen, Hongzhang Liu, Jiaqi Shao, Tao Gui, Qi Zhang, Xuanjing Huang, Suncong Zheng, Maxm Pan
**arXiv:** [arxiv.org/abs/2609.30199](https://arxiv.org/abs/2609.30199)
**Summary:** ExplorationBench tests whether AI systems can discover unfamiliar executable rules in AlienCode and AlienLogic worlds that conflict with memorized knowledge. Experiments with 10 systems show that leading models can acquire new rules, but exploration quality varies sharply across trajectories and can stall or reverse with continued interaction.

---

### 13. AgentKernel: The Trust-Native Agentic Operating System
**Authors:** Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Zhuotao Liu
**arXiv:** [arxiv.org/abs/2609.29647](https://arxiv.org/abs/2609.29647)
**Summary:** AgentKernel proposes an operating-system layer that places identity, input mediation, memory governance, and execution control inside a mandatory enforcement boundary. Its four-pillar design adapts classical security ideas to prompt injection, delegation abuse, memory poisoning, and privileged tool misuse across the full agent lifecycle.

---

### 14. PUBG Ally: A Conversational Embodied Agent as an AI Teammate
**Authors:** Beomsoo Kim, Byeongju Kim, Dohyun Kim, Dongwon Kim, Eunchong Kim, Hongmin Kim, Hyeojung Im, Hyeonbin Hwang, Hyeonghwan Kim, Hyoseok Seol, Insub Im, Irene Chen, Jaeseung Jeon, Jimin Hong, Kiyoon Yoo, Minkyoung Park, Seohyeon Jung, Seungjun Chung, Sue Hyun Park, Sungwoo Kim, Youngin Cho, Yujeong Son, Kangwook Lee, Hyunseung Kim
**arXiv:** [arxiv.org/abs/2609.29837](https://arxiv.org/abs/2609.29837)
**Summary:** PUBG Ally combines a language-model agent, a controlled game-information interface, and a fast control layer to act and converse as a real-time voice teammate. Training used nearly 39,000 gameplay sessions, while live-service deployment added compression, context compaction, safety training, guardrails, and memory redaction; surveyed players reported substantially more positive than negative recommendations.

---

### 15. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal
**Authors:** Yehang Zhang, Haojian Huang, Yifan Chang, Jianchong Su, Bohan Zhou, Yingjie Xu, Wosong Chen, Tianhao Zhou, Chenxu Wang, Tianyi Zhang, Yangkai Wei, Wenqian Li, Shiyuan Deng, Yinchuan Li, Ying-Cong Chen, Zexi Li
**arXiv:** [arxiv.org/abs/2609.29964](https://arxiv.org/abs/2609.29964)
**Summary:** World Action Agent lets vision-language models control robots inside a visual workspace with contact views, editable action rehearsals, correction loops, and reusable multimodal skills. It reached 75.6% average success on LIBERO-Pro, transferred learned skills to robosuite, and raised a fine-tuned 9B model's out-of-domain success from 1.7% to 43.3%.

---

### 16. AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation
**Authors:** Zhiyu Xu, Weilong Yan, Yufei Shi, Shiyang Li, Yihao Liu, Kin-Man Lam, Yuewen Cao
**arXiv:** [arxiv.org/abs/2609.29816](https://arxiv.org/abs/2609.29816)
**Summary:** AV-GRPO converts coupled audio-video preference learning into modality-specific reinforcement-learning subproblems using anchored rollouts, frozen-tower optimization, and adaptive objectives. With its difficulty-controlled 5DAV dataset, the method outperformed LTX-2.3 on generation quality, semantic alignment, and cross-modal synchronization under both LoRA and full fine-tuning.

---

### 17. DeltaWAM: Delta World Action Models for Bimanual Manipulation
**Authors:** Han Yan, Zishang Xiang, Haokai Jiang, Zeyu Zhang, Qilin Wang, Weiyu Guo, Yandong Guo, Boxin Shi, Hao Tang
**arXiv:** [arxiv.org/abs/2609.28811](https://arxiv.org/abs/2609.28811)
**Summary:** DeltaWAM predicts visual changes and robot actions instead of repeatedly reconstructing mostly static frames, while Streaming Delta Memory updates cached context with compact observed deltas. On RoboTwin it improved clean and randomized-scene success over Fast-WAM while cutting training compute and reducing one-step inference latency by 36.57%.

---

### 18. ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation
**Authors:** Zichong Meng, Chongjian Ge, Chun-Hao P. Huang, Yang Zhou, Huaizu Jiang
**arXiv:** [arxiv.org/abs/2609.28923](https://arxiv.org/abs/2609.28923)
**Summary:** ViRDM replaces teacher-and-critic video distillation with generator-only post-training against a precomputed representation distribution, using truncated clean-exit supervision and lightweight dynamics regularization. After only 20 generator updates it scored 84.87 on VBench, slightly exceeding the prior few-step causal baseline while using 16 A100 GPU-hours.

---

### 19. Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures
**Authors:** Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Lida Zhao, Yutao Wu, Simin Chen, Ying Zhang, Leo Yu Zhang
**arXiv:** [arxiv.org/abs/2609.29429](https://arxiv.org/abs/2609.29429)
**Summary:** Jev uses reinforcement learning for calibrated decisions to answer multiple typed alignment questions about one input with probabilities in a single call. Across 10 failure modes, 44 benchmarks, and five target models, a generic zero-shot question reached 0.886 median AUROC and cost 63 times less than generative LLM-judge scoring.

---

### 20. Rate-distortion optimization for full-reference image quality metrics via stochastic Hessian estimates
**Authors:** Samuel Fernández-Menduiña, Eduardo Pavez, Antonio Ortega
**arXiv:** [arxiv.org/abs/2609.30077](https://arxiv.org/abs/2609.30077)
**Summary:** The paper approximates full-reference image-quality metrics with input-dependent quadratic distortions whose Hessians are estimated through automatic-differentiation matrix-vector products. Block-diagonal and diagonal approximations enable codec rate-distortion optimization with MS-SSIM-, LPIPS-, and related perceptual objectives, delivering 14.2%-36.7% BD-rate savings under the target metric without decoder changes.

---
