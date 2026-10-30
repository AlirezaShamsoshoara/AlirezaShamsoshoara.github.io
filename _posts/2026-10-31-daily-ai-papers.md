---
title: "Daily AI Papers — October 31, 2026"
date: 2026-10-31
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-31/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - efficient-training
  - embodied-ai
---

### 1. Proving and Improving the Platonic Representation Hypothesis with JEPAs
**Authors:** Randall Balestriero, Yann LeCun
**arXiv:** [arxiv.org/abs/2610.39302](https://arxiv.org/abs/2610.39302)
**Summary:** This paper proves that separately trained JEPAs learn representations aligned up to a rotation when their positive pairs are valid observations of the same scene, and bounds misalignment for other pairings. Experiments report that good-view training needs 42 times fewer samples than next-token prediction to reach the same alignment, with a 109M-parameter text JEPA outperforming evaluated language models up to 72B parameters on encoder alignment.

---

### 2. Recurrent Looped Transformer
**Authors:** Yifan Zhang, Jichen Feng, Shihan Qin, Sun-Yuan Kung, Mengdi Wang
**arXiv:** [arxiv.org/abs/2610.07591](https://arxiv.org/abs/2610.07591)
**Summary:** The Recurrent Looped Transformer combines a parallel causal encoder with a recurrent decoder that carries the previous token's final state forward at fixed per-token cost. On algorithmic state-tracking tasks, it generalizes parity from training sequences of at most 40 bits to 256 bits with 100% accuracy and reaches 97% permutation-tracking accuracy at eight times the training length, while the matched Transformer remains near chance.

---

### 3. Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players
**Authors:** Changlian Ma, Limin Wang
**arXiv:** [arxiv.org/abs/2610.33845](https://arxiv.org/abs/2610.33845)
**Summary:** AutoTavern uses specialized LLM research agents, shared structured memory, verification gates, and live-game feedback to build a simulator and PPO-trained Hearthstone Battlegrounds policy. The resulting TavernAgent rises from a rating of 6,000 to about 15,000 and solves 91% of TavernBench play tasks, compared with at most 63% for frontier LLMs.

---

### 4. Zero-Mem: Zero-Token Memory Operations for LLM Agents
**Authors:** Yilin Xiao, Zhehan Zhu, Yujing Zhang, Jin Chen, Zijin Hong, Luyao Zhuang, Qinggang Zhang, Shengyuan Chen, Xiaocao Ouyang, Lingfei Ren, Xiao Huang
**arXiv:** [arxiv.org/abs/2607.29377](https://arxiv.org/abs/2607.29377)
**Summary:** Zero-Mem preserves original interaction traces and retrieves through an entity-context graph and temporal hierarchy without invoking an LLM for memory operations. With the same final-answer reader and context budget, it reports competitive long-memory question-answering performance and 57.6% lower memory-operation time than the fastest compared baseline, while accounting for encoder computation separately.

---

### 5. Multi-Token Prediction Done Right
**Authors:** Jayden Teoh
**arXiv:** [arxiv.org/abs/2610.38331](https://arxiv.org/abs/2610.38331)
**Summary:** Soft Multi-Token Prediction removes a noisy residual from the standard multi-token training gradient and retains its useful KL self-distillation signal through straight-through gradient routing. Across models from 167M to 1.2B parameters, it improves next-token perplexity, speculative decoding speed, and zero-shot accuracy without additional parameters or measurable overhead.

---

### 6. Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?
**Authors:** Huangfei Jiang, Anning Hu, Kai Sheng, Yuchen Cai, Rui Ge, Xiangyu Kong, Jianghao Lin, Shuzi Chen, Jiyi Weng, Junchi Yan
**arXiv:** [arxiv.org/abs/2610.38342](https://arxiv.org/abs/2610.38342)
**Summary:** Investor's Last Exam evaluates equity-research agents using decision-time information, a versioned financial database, professional deliverables, and expert scoring tied to sources and assumptions. Across 86 assignments, the leading model scores 68.1 overall but only 52.5 on forecasting and modeling, exposing a gap between research quality and predictive investment performance.

---

### 7. EditAgent: Rethinking Agentic Image Editing
**Authors:** Haiyang Xu, Tianyu Wang, Jialu Li, Jiteng Mu, Yuanjun Xiong, Jianming Zhang, Zhuowen Tu, Mingze Xu
**arXiv:** [arxiv.org/abs/2610.39664](https://arxiv.org/abs/2610.39664)
**Summary:** EditAgent expands image-editing agents' tool choices and gives visual judges verification records, then generates candidates in parallel for one listwise judgment. Experts prefer this approach to sequential refinement in 78.5% of decided comparisons with no more than half the judge calls, and it improves two open-weight editors across three benchmarks.

---

### 8. Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps
**Authors:** Peitong Duan, Khashayar Gatmiry, Jeffrey Nichols, Samy Bengio, Emmanuel Abbe
**arXiv:** [arxiv.org/abs/2610.39264](https://arxiv.org/abs/2610.39264)
**Summary:** This framework trains planning and UI-grounding agents directly on live iOS apps using dense step-level and terminal rewards, PPO, and neighbor-conditioned value estimation. Its 8B agents outperform supervised and terminal-only reinforcement-learning baselines, achieving nearly sevenfold better Android generalization than the supervised baseline and matching Gemini-3.1-Pro on real iOS applications.

---

### 9. Training Foundation Models with a Single Algorithm
**Authors:** Yuda Song, Alvin Zhang, Fahim Tajwar, Daman Arora, Jeff Schneider, Daniel Khashabi, Ruslan Salakhutdinov, J. Andrew Bagnell, Aarti Singh, Andrea Zanette
**arXiv:** [arxiv.org/abs/2610.40564](https://arxiv.org/abs/2610.40564)
**Summary:** Unified training expresses pretraining, midtraining, supervised fine-tuning, and suitable reinforcement-learning objectives through one likelihood-based algorithm. A single trainer mixes static data and model-generated targets, improving the accuracy-compute tradeoff and task coverage in controlled and real-world experiments while preserving broader capabilities.

---

### 10. SO-101 Bench: Accessible Spatial Manipulation
**Authors:** Truman Hickok
**arXiv:** [arxiv.org/abs/2610.36420](https://arxiv.org/abs/2610.36420)
**Summary:** SO-101 Bench provides an Isaac Lab digital twin for language-conditioned spatial manipulation, with 138 objects, 916 evaluation episodes, and 3,629 simulated demonstrations. Five policies retain their exact simulation ranking on a real arm despite simulation overestimating success, while an LLM agent with learned grasping scores 83.2% compared with roughly 61% for the best learned policies.

---

### 11. Amortizing Sequential Experimental Design in Reasoning LLMs
**Authors:** Anita Kriz, Antonin Berthon, Nicolás Astorga, Mihaela van der Schaar
**arXiv:** [arxiv.org/abs/2610.20832](https://arxiv.org/abs/2610.20832)
**Summary:** This work trains reasoning LLMs to choose sequential experiments using information-gain rewards from an independently specified generative model. On Twenty Questions, the learned policies beat training- and inference-time Bayesian experimental-design baselines at lower computational cost, generalize to unseen categories, and transfer positively to the Medi-Q clinical dialogue benchmark.

---

### 12. Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation risks
**Authors:** Yao Huang, Zhiyuan Zeng, Yu Wang, Zhitong Zhu, Dingcheng Duan, Hao Li, Shangzhi Xu, Yifan Wang, Jinzhe Tu, Shukun Xiong, Yihe Zang, Han Yan, Hongchang Yang, Fuyu Gu, Wei Xu, Yinpeng Dong, Xiaojian Li
**arXiv:** [arxiv.org/abs/2610.35671](https://arxiv.org/abs/2610.35671)
**Summary:** This independent evaluation tests DeepSeek V4.1 Flash-1017 across 34 benchmarks covering evaluation integrity, loss of control, and harmful manipulation. It reports improvements over the V4 generation but continuing concerning behaviors, and emphasizes incremental-release evaluation, reasoning-and-action observability, and private benchmarks.

---

### 13. LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data
**Authors:** Zhennan Wan, Jianfei Chen
**arXiv:** [arxiv.org/abs/2610.30132](https://arxiv.org/abs/2610.30132)
**Summary:** LongZero improves long-context reasoning without external data by first generating compact questions, answers, and supporting evidence, then expanding the evidence into long multi-document contexts. Combining self-generated multi-hop reasoning and multi-round retrieval tasks with GRPO, it outperforms the evaluated baselines across two LLMs and five long-context reasoning benchmarks.

---

### 14. Xiaomi-OCR-0 Technical Report
**Authors:** Xin Chen, Anan Du, Feng Feng, Pei Fu, Jian Luan, Longwei Xu, Shaojie Zhang, Hang Li, Heng Qu, Cheng Tan
**arXiv:** [arxiv.org/abs/2609.36136](https://arxiv.org/abs/2609.36136)
**Summary:** Xiaomi-OCR-0 is a unified 0.8B model for document parsing and OCR-centric understanding, trained with an automated corpus of approximately 170M samples and a progressive pretraining and mixed-task reinforcement-learning recipe. It reports 95.24 on Real5-OmniDocBench, 96.83 on OmniDocBench v1.6, 87.94 on Wild-OmniDocBench, and an average of 83.2 across five OCR-oriented visual-question-answering benchmarks.

---

### 15. TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents
**Authors:** Aaron J. Li, Weijia Xu, Chandan Singh, Zixiao Chen, Jeevana Priya Inala, Charlotte Siska, Acar Tamersoy, Bin Yu, Ion Stoica, Michel Galley, Jianfeng Gao
**arXiv:** [arxiv.org/abs/2610.22732](https://arxiv.org/abs/2610.22732)
**Summary:** TokenEconomizer is an external controller that reduces recurring coding-agent costs by injecting operational micro-skills, pruning irrelevant tools, and interrupting unproductive failure loops. Across Claude Code, Codex, and GitHub Copilot CLI, it reduces average token cost by 18.4% to 30.9% with comparable task success, with additional savings in sequential web development and security auditing.

---

### 16. Broken on Arrival: Non-Functional Quantized LLM Artifacts in Public Model Registries and How to Catch Them
**Authors:** Aditi Patodiya
**arXiv:** [arxiv.org/abs/2609.05881](https://arxiv.org/abs/2609.05881)
**Summary:** This audit screens 305 eligible code-capable GGUF tags in the official Ollama library and 22 popular HuggingFace community files, then retests suspects on HumanEval+. Seven official tags solve at most six of 164 tasks, and calibrated rebuilds show that exactly reproducible low-bit files can still be non-functional, motivating functional screening before publication.

---

### 17. OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation
**Authors:** Junli Liu, Zhongrui You, Chenhui Li, Zhen Li, Yuyang Tian, Qizhen Chen, Delin Qu, Haoming Song, Dong Wang, Xuelong Li, Zhigang Wang, Bin Zhao
**arXiv:** [arxiv.org/abs/2610.39287](https://arxiv.org/abs/2610.39287)
**Summary:** OpenFlyV2 shares a vision-language representation across aerial perception, spatial reasoning, and a compact action expert, using temporal memory and action priors for efficient onboard control. It generates 12-waypoint action chunks at 10 Hz on a Jetson Orin NX and transfers from simulation to physical quadrotors with 48% navigation success across four environments without real-world aerial training data.

---

### 18. AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers
**Authors:** Bin Xu, Mo Zhang, Zhengfeiyang Zhang, Xinfeng Yang, Yixing Ma, Wei Wang, HeXin Wang, Pengfei Zhou, Wangbo Zhao
**arXiv:** [arxiv.org/abs/2610.39663](https://arxiv.org/abs/2610.39663)
**Summary:** AB-Attention approximates dense video-diffusion attention using intra-block clustering, inclusion-probability-weighted block sampling, and a kernel that packs small key-value blocks into tensor-core tiles. On Wan2.1 and HunyuanVideo, it skips 89% to 92% of attention while improving PSNR by up to 4.4 dB over the strongest baseline and reaching up to 2.23 times end-to-end speedup.

---

### 19. Your LR Schedule May Not Be Principled: Effective Learning Rate Scheduling in Weight-Normalized Training
**Authors:** Qifan Yu, Xinyu Ma, Xingyan Bin, Di He
**arXiv:** [arxiv.org/abs/2610.40362](https://arxiv.org/abs/2610.40362)
**Summary:** This paper finds that effective learning-rate trajectories explain most reported training-loss gains from weight normalization, and proposes Affine Inverse-square-Root decay to control those trajectories. In 128B-token mixture-of-experts pretraining, the schedule improves loss, downstream performance, and hyperparameter robustness, reducing terminal loss by approximately 0.01 relative to cosine at matched cumulative learning rate.

---

### 20. Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents
**Authors:** Zhenning Shi, Liang Pang, Yongqi Li
**arXiv:** [arxiv.org/abs/2610.34298](https://arxiv.org/abs/2610.34298)
**Summary:** MICA compares MCP and CLI interfaces built from the same semantic action contract and runtime, showing substantial behavioral and cost differences across six models and three environments. Its DART repair method preserves validated semantic decisions while correcting interface-specific realization, improving benchmark scores by up to 9.0 points and reducing MCP token cost by up to 27.1k tokens per task.
