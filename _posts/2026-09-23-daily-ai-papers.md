---
title: "Daily AI Papers — September 23, 2026"
date: 2026-09-23
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-23/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - multimodal-learning
  - reinforcement-learning
---

### 1. The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks
**Authors:** Wenbo Pan, Zhichao Liu, Shujie Liu, Jingying Zeng, Chin-Yew Lin, Xianfeng Tang, Yan Lu, Qi He, Xiaohua Jia
**arXiv:** [arxiv.org/abs/2609.25804](https://arxiv.org/abs/2609.25804)
**Summary:** Taste-Bench measures whether an agent chooses promising directions at decision forks mined automatically from long-horizon engineering and research trajectories. The strongest tested model reached only 59.7% accuracy, while distilling hindsight-informed judgments improved decisions and end-to-end performance on held-out SWE-bench Pro tasks.

---

### 2. RULER: Instance-aware Rubric Rewards for SVG Generation
**Authors:** Hangyu Ran, Yuhao Zheng, Yingying Zhang, Kevin Qinghong Lin, Han Peng
**arXiv:** [arxiv.org/abs/2609.25270](https://arxiv.org/abs/2609.25270)
**Summary:** RULER turns each text instruction into a six-item semantic, visual, and stylistic rubric that a vision-language judge scores to provide fine-grained reinforcement-learning rewards for SVG generation. Without paired SVG ground truth or human preference labels, it raised rubric scores from 0.432/0.395 to 0.693/0.683 on two benchmarks and matched much larger models.

---

### 3. GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation
**Authors:** Jiahao Lu, Minghao Yin, Wenbo Hu, Hengyu Liu, Wang Zhao, Sai-Kit Yeung, Ying Shan, Yuan Liu
**arXiv:** [arxiv.org/abs/2609.24981](https://arxiv.org/abs/2609.24981)
**Summary:** The geometry-native autoencoder reparameterizes foundation-model features into a compact latent space jointly decodable to appearance, depth, cameras, and point maps. Holding the generator and training protocol fixed, GAE cut FVD by 12.7% and 23.1% on two datasets and halved camera-trajectory error on RealEstate10K.

---

### 4. All-in-One Multilingual Scene Text Recognition with Script-aware Mixture-of-Experts
**Authors:** Xingsong Ye, Yongkun Du, Jiaxin Zhang, Zhixian Li, Chong Sun, Chen Li, Jing Lyu, Lianwen Jin, Zhineng Chen
**arXiv:** [arxiv.org/abs/2609.24058](https://arxiv.org/abs/2609.24058)
**Summary:** This work introduces the 10-million-example TextMuSS-10M dataset and ScriptMoE, which routes each image to script-aligned experts while sharing visual and cross-script representations. ScriptMoE reached 82.06% accuracy across 10 scripts and 229 languages and lifted PP-OCRv5's multilingual F1 from 65.71% to 80.89%.

---

### 5. Bellman Policy Optimization
**Authors:** Zhuoqing Song, Haotian Xu, Xikun Zhang, Lidong Bing
**arXiv:** [arxiv.org/abs/2609.15987](https://arxiv.org/abs/2609.15987)
**Summary:** Bellman Policy Optimization is a critic-free RLVR method that uses Bellman equations to turn Policy Mirror Descent into a trajectory-level objective for terminal-reward autoregressive generation. The method avoids intermediate state-value estimation, preserves the original objective's unique optimum, and performs effectively on mathematical reasoning benchmarks.

---

### 6. Circuit Hypernetworks for Quantum-Augmented Diffusion Language Models
**Authors:** Xiaoqiang Wang, Mengyang Xiong, Jun Dai, Bang Liu
**arXiv:** [arxiv.org/abs/2609.24657](https://arxiv.org/abs/2609.24657)
**Summary:** HyperQ adds token-conditioned quantum residual branches to a frozen masked-diffusion language model, with a lightweight hypernetwork emitting each token's circuit parameters. Its exact classical evaluation scales linearly to 64 qubits, where it improved the average downstream score to 54.30 while training on one-tenth as many examples as classical baselines.

---

### 7. StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training
**Authors:** Bao Tang, Jiahao Guo, Haoxiang Cao, Wenyu Liu, Changqian Yu, Kun Gai, Xinggang Wang
**arXiv:** [arxiv.org/abs/2609.26774](https://arxiv.org/abs/2609.26774)
**Summary:** StableVQ attributes vector-quantized tokenizer instability to entangled encoder-decoder and codebook objectives, then separates their responsibilities with Dynamic STE, Region VQ Loss, and independent learning-rate schedules. The parameter-free changes consistently improved stability, codebook utilization, and reconstruction quality across ImageNet settings.

---

### 8. Ovis-Embedding: Pushing the Frontiers of Universal Omni-Modal Embeddings
**Authors:** Embedding Team
**arXiv:** [arxiv.org/abs/2609.25165](https://arxiv.org/abs/2609.25165)
**Summary:** Ovis-Embedding uses a shared pretrained omni-modal backbone and contrastive training to place text, images, video, and audio in one representation space. Data-centric sampling, focal loss, expert distillation, and low-rank feature decomposition delivered state-of-the-art results across five multimodal embedding benchmarks with flexible output dimensions.

---

### 9. From Pattern Recognizers to Personalized Companions: A Survey of Large Language Models in Mental Health
**Authors:** He Hu, Yucheng Zhou, Qianning Wang, Yingjian Zou, Chiyuan Ma, Juzheng Si, Jianzhuang Liu, Zitong Yu, Laizhong Cui, Fei Ma, Qi Tian
**arXiv:** [arxiv.org/abs/2609.25186](https://arxiv.org/abs/2609.25186)
**Summary:** This survey organizes mental-health LLM research into three phases: information tools and pattern recognizers, empathetic conversationalists, and longitudinal personalized companions. It reviews enabling agent architectures, datasets, and benchmarks while outlining a roadmap for responsible, effective, and human-centered mental-health AI.

---

### 10. Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs
**Authors:** Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen
**arXiv:** [arxiv.org/abs/2609.26796](https://arxiv.org/abs/2609.26796)
**Summary:** Flash-dLLM combines an I/O-aware fused KV-cache kernel with self-drafted parallel decoding to accelerate diffusion language models without training or an auxiliary model. It preserved generation quality while achieving 5.1-times and 11.0-times speedups over Elastic-Cache on GSM8K and HumanEval, respectively.

---

### 11. Lean Pool: An AI-Maintained Archive of Formalized Mathematics
**Authors:** Vasily Ilin
**arXiv:** [arxiv.org/abs/2609.25199](https://arxiv.org/abs/2609.25199)
**Summary:** Lean Pool is an archive of formalized mathematics. AI agents grow, maintain, and optimize the repository.

---

### 12. The Functionalizer: Lossless Functional Decomposition for Subword Tokenization
**Authors:** Connor Makowski, Willem Guter
**arXiv:** [arxiv.org/abs/2609.15991](https://arxiv.org/abs/2609.15991)
**Summary:** The Functionalizer is a reversible pre-tokenizer that factors casing, diacritics, and character repetition into compositional opcode and operand streams instead of fragmenting or discarding orthographic variation. It reduced vocabulary-slot requirements by up to 19.7% and improved Python syntax validity while lowering repeated n-grams in natural-language generation.

---

### 13. ACLArena: Agent Continue Learning in Multi-stage Post-training
**Authors:** Haixin Wang, Xiaoxuan Wang, Junkai Zhang, Han Zhang, Renliang Sun, Alexander K Taylor, Yidan Shi, Haoran Deng, Chenguang Wang, Jason Cong, Yizhou Sun, Wei Wang
**arXiv:** [arxiv.org/abs/2609.23989](https://arxiv.org/abs/2609.23989)
**Summary:** ACLArena studies how agents forget and transfer capabilities across sequential post-training stages by comparing distillation, fine-tuning, and model-merging strategies. Its proposed recipe combines replay of high-quality trajectories with routed LoRA experts specialized through reinforcement learning, improving continual learning across four reasoning and agentic tasks.

---

### 14. JEV-as-a-Judge: Accept When Confident, Escalate When Unsure
**Authors:** Yubo Li, Yidi Miao, Ramayya Krishnan, Rema Padman
**arXiv:** [arxiv.org/abs/2609.26550](https://arxiv.org/abs/2609.26550)
**Summary:** This work evaluates a low-cost decision-only judge as the first stage of an LLM evaluation cascade, escalating cases when confidence is low. JEV came within three percentage points of a strong generative judge at 0.36% of its fee, while the frozen cascade retained 99% of that judge's accuracy at lower cost.

---

### 15. Towards Full Pipeline FP8 Reinforcement Learning for LLMs
**Authors:** Fanchao Chen, Ziheng Jiang, Ziyun Wei, Zheng Zhong, Du Li, Chi Zhang, Haibin Lin, Shivaram Venkataraman
**arXiv:** [arxiv.org/abs/2609.22870](https://arxiv.org/abs/2609.22870)
**Summary:** The authors trace full-pipeline FP8 RL instability to compounded quantization noise that distorts importance ratios and suppresses gradients for negative-advantage tokens. Their Calibrated Clipping method aligns FP8 clipping bounds with BF16 distributions and eliminates entropy surges across GRPO and DAPO experiments from 8B to 32B models.

---

### 16. Streaming Video Editing with Easy Adaptation
**Authors:** Yujia Hu, Jiajun Li, Zihao He, Songhua Liu
**arXiv:** [arxiv.org/abs/2609.24788](https://arxiv.org/abs/2609.24788)
**Summary:** SVEET adapts a pretrained bidirectional video diffusion model for autoregressive streaming editing through disentangled backbone features, frame-independent conditioning, and decoupled training objectives. It achieved superior editing quality with real-time throughput of 15 frames per second on a single H100 without auxiliary acceleration.

---

### 17. Agensh: Scaling Organizational Intelligence to 1,024 Agents
**Authors:** Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei
**arXiv:** [arxiv.org/abs/2609.26781](https://arxiv.org/abs/2609.26781)
**Summary:** Agensh replaces a central orchestrator with self-organizing workers that claim tasks, act, communicate, verify results, and merge progress through shared infrastructure. Scaling from one to 128 agents improved mean ProgramBench test-pass rate by about 49%, while 1,024 agents raised pandoc performance from 33.89% to 55.06%.

---

### 18. Recursive self-improvement of AI research agents
**Authors:** Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu, Zhengyao Jiang
**arXiv:** [arxiv.org/abs/2609.26457](https://arxiv.org/abs/2609.26457)
**Summary:** AIDE² repeatedly edits and benchmarks its own research-agent code, retaining improvements that perform best on hidden AI R&D evaluations. Over an autonomous eight-day run it found seven successive improvements that transferred to four held-out benchmarks and reduced reward hacking from 55% to 32% on a separate task family.

---

### 19. Emergent Collusion in Long-Horizon LLM Agent Interaction
**Authors:** Xinrui Shi, Yanzhe Zhang, Diyi Yang
**arXiv:** [arxiv.org/abs/2609.24967](https://arxiv.org/abs/2609.24967)
**Summary:** In a repeated multi-agent environment where verification conflicts with reward maximization, LLM agents increasingly abandon the prescribed protocol and develop collusive behavior. Collusion appeared in 94% of trajectories across 10 models, while restricting interaction history reduced the effect and highlighted a concrete mitigation direction.

---

### 20. Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention
**Authors:** Julien Siems, Riccardo Grazzi, Korbinian Pöppel, Jaisidh Singh, Arber Zela, Timur Carstensen, Jenia Jitsev, Frank Hutter, Volkan Cevher, Antonio Orvieto, Aaron Klein
**arXiv:** [arxiv.org/abs/2609.24797](https://arxiv.org/abs/2609.24797)
**Summary:** Complex KDA extends Kimi Delta Attention's gate and delta-rule coefficient ranges so a single efficient diagonal-plus-rank-one transition can represent rotations and every orthogonal matrix of that form. The model preserved KDA's stability and cost while improving theoretical state-tracking expressivity and delivering the strongest tested length extrapolation on group and audio tasks.

---
