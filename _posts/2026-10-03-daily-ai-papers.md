---
title: "Daily AI Papers — October 03, 2026"
date: 2026-10-03
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-03/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - model-distillation
  - ai-agents
  - multimodal-ai
---

### 1. On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics
**Authors:** Julianna Piskorz, Antonin Berthon, Mihaela van der Schaar
**arXiv:** [arxiv.org/abs/2609.35259](https://arxiv.org/abs/2609.35259)
**Summary:** This controlled strong-to-weak distillation study independently varies rollout policy, token-level KL direction, and learning rate across Llama3 and Qwen2.5 models and several reasoning domains. The results show that KL direction and optimization settings often matter more than on-policy versus off-policy rollouts, although on-policy data helps on harder arithmetic variants before later RLVR.

---

### 2. Transformers Stop Thinking Too Early, and a Tiny LoRA Fixes It
**Authors:** Zehao Jin, Ruixuan Deng, Junran Wang
**arXiv:** [arxiv.org/abs/2609.36585](https://arxiv.org/abs/2609.36585)
**Summary:** The authors find that pretrained transformers follow only short in-context reference chains, then extend this computation by training a rank-8 LoRA at one early layer while freezing the remaining model. The intervention raises Qwen3-8B from 15.5% to 99% exact accuracy on 24-line chains, reveals a middle-layer information relay, and also improves MuSiQue performance.

---

### 3. Video Generation Models: A Survey of Post-Training and Alignment
**Authors:** Chaoyu Li, Xiaoyi Gu, Yogesh Kulkarni, Eun Woo Im, Mohammadmahdi Honarmand, Zeyu Wang, Juntong Song, Fei Du, Xilin Jiang, Kexin Zheng, Tianzhi Li, Fei Tao, Pooyan Fazli
**arXiv:** [arxiv.org/abs/2610.00812](https://arxiv.org/abs/2610.00812)
**Summary:** This survey organizes video-generation post-training into supervised fine-tuning, self-training and distillation, preference- and reward-based methods, and inference-time methods. It also reviews datasets and evaluations while highlighting unresolved issues in long-horizon consistency, reward design, safety, and the stability-expressiveness trade-off.

---

### 4. Persona Dosing: Calibrated Activation Steering for Graded Trait Control
**Authors:** Zehao Jin, Junran Wang, Ruixuan Deng, Jiahao Chen, Jingyuan Zhang, Yuxuan Zhang, Xinjie Shen
**arXiv:** [arxiv.org/abs/2609.36388](https://arxiv.org/abs/2609.36388)
**Summary:** PersonaDose conditions an activation-steering controller on trait descriptions and calibrates its flow time against measured behavioral intensity, without training on requested target intensities. Across Llama-3.1-8B, Qwen3-8B, and Gemma-3-4B, it improves trait expression over contrastive activation addition and reaches mean targeting errors of 4.7 to 6.2 points on reachable targets.

---

### 5. Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens
**Authors:** Ruiyang Si, Jianxin Bi, Shunyu Yang, Rui Ni, Wenbo Huang, Qiang Wang, Shulong Jiang, Duomin Wang, Xiuyu Li, Haiwen Feng, Zhen Dong, Daquan Zhou
**arXiv:** [arxiv.org/abs/2610.01939](https://arxiv.org/abs/2610.01939)
**Summary:** PyRUA-Lean lets a robot agent compose classical primitives and learned policies into executable Python cells with local retries and selectively requested observations. Across 700 simulated tasks, it raises success from 63.1% to 71.7% under equal call budgets and uses 65% fewer input tokens on tasks solved by both systems.

---

### 6. X-Tree: Tokenizing Reusable Experience for Efficient Agent Generalization
**Authors:** Sitao Cheng, Xunjian Yin, Zhiyuan Sun, Yuxuan Li, Ruiwen Zhou, Xiangru Jian, Victor Zhong
**arXiv:** [arxiv.org/abs/2609.32993](https://arxiv.org/abs/2609.32993)
**Summary:** X-Tree extracts reusable hierarchical action skills directly from agent trajectories by scoring and merging recurring canonicalized spans without additional LLM calls. Integrated into offline RL, online RLVR, and on-policy self-distillation, it improves matched-budget results on WebArena, ScienceWorld, and WebShop.

---

### 7. SILSA: Sliding-Window Slice Latents for Topology-Preserving High-Resolution 3D Generation
**Authors:** Tianjiao Yu, Xinzhuo Li, Yifan Shen, Ying Shen, Kiet A. Nguyen, Adheesh Sunil Juvekar, Ismini Lourentzou
**arXiv:** [arxiv.org/abs/2610.02201](https://arxiv.org/abs/2610.02201)
**Summary:** SILSA represents 3D shapes with overlapping slice latents along three canonical axes and coordinates them through a shared volumetric anchor lattice with topology-aware supervision. It improves structural fidelity while using 70% fewer tokens than the next-most compact baseline, reducing training memory and inference time.

---

### 8. Architect-Ant: Editable Automatic Furnishing of Architectural Floor Plans
**Authors:** Fedor Rodionov, Aleksandar Cvejic, Michael Birsak, John Femiani, Peter Wonka
**arXiv:** [arxiv.org/abs/2606.10953](https://arxiv.org/abs/2606.10953)
**Summary:** Architect-Ant learns editable furniture layouts from 505 professionally designed floor plans using a coordinate-based DSL, supervised fine-tuning, and GRPO with geometric and functional constraints. It combines low violation rates with high functional completeness, while preserving object-level editability and conversion to 3D scenes.

---

### 9. Decoding Looped Transformers Better for (Almost) Free
**Authors:** Weihao Liu, Huangjie Zheng, Tianrong Chen, Rohit Dilip, Richard He Bai, Yizhu Jiao, Yuyang Wang, Ruixiang Zhang
**arXiv:** [arxiv.org/abs/2610.02185](https://arxiv.org/abs/2610.02185)
**Summary:** LoopCD contrasts the final prediction of a looped transformer with an earlier recurrent state, using aligned weak and strong predictions already produced by the model. Across four model families it improves reasoning and code-generation accuracy and can halve recurrent loops while matching or exceeding full-depth baselines.

---

### 10. Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding Spaces
**Authors:** Hongyuan Tao, Xinggang Wang, Lianghui Zhu, Yongkang Li, Yunchao Wei, Bin Feng, Shaoyu Chen, Qian Zhang, Chang Huang, Kai Yu
**arXiv:** [arxiv.org/abs/2609.40362](https://arxiv.org/abs/2609.40362)
**Summary:** Multimodal Flow models text and images as ordered continuous hyperchunks and trains one chunk-causal vector field through flow matching. Its MF-1 models remain competitive with unified systems trained on much more data and outperform matched hybrid and discrete baselines.

---

### 11. CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning
**Authors:** Wenbin Hu, Huihao Jing, Haochen Shi, Yuxuan Liu, Haoran Li, Yangqiu Song
**arXiv:** [arxiv.org/abs/2609.36820](https://arxiv.org/abs/2609.36820)
**Summary:** CorrGRPO replaces covariance-scale-sensitive normalization in multi-reward GRPO with Pearson-correlation normalization while preserving the centered total reward. Tests on code generation, tool use, and agent security show improvements across models from 0.5B to 8B parameters.

---

### 12. Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows
**Authors:** Gabriel Tomitsuka, Arman Raayatsanati, Emma Xing, Duke Gand, Joseph J Ma
**arXiv:** [arxiv.org/abs/2610.02122](https://arxiv.org/abs/2610.02122)
**Summary:** Argo-Bench evaluates 210 enterprise data-agent tasks in a simulated food-delivery business exposed through a 235-table warehouse containing 7.5 billion rows. Agents must reconstruct facts and take consequential actions, and the strongest of 14 evaluated models scores at least 95 on only 34.8% of tasks.

---

### 13. Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation
**Authors:** Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana, Qinrong Cui, Erland Hilman Fuadi, Zayd M. K. Zuhri, Nanda Ryaas Absar, Ahmed Elshabrawy, Wilfried Ariel Mulyawan, Shoubin Yu, Yue Zhang, Mohit Bansal, Alham Fikri Aji
**arXiv:** [arxiv.org/abs/2610.01092](https://arxiv.org/abs/2610.01092)
**Summary:** Ego2Act introduces 2,640 videos from 110 real-world tasks to test whether video generators can simulate multi-step, goal-directed egocentric manipulation. Its reference-free judge and evaluations show that current models often skip dependent steps and fail on fine-grained physical dynamics and persistent world state.

---

### 14. Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation
**Authors:** Mohammed Irfan Kurpath, Jaseel Muhammad Kaithakkodan, Sahal Shaji Mullappilly, Ivan Laptev, Hisham Cholakkal
**arXiv:** [arxiv.org/abs/2610.02148](https://arxiv.org/abs/2610.02148)
**Summary:** Omni-Embed-Mini maps text, speech, audio, images, video, and visually rich documents into one embedding space while leaving all text-side parameters frozen. The 0.9B model preserves text retrieval quality, is substantially smaller than compared open omni-embedders, and extends alignment through dense-caption distillation and lightweight adapters.

---

### 15. PhysVista: Benchmarking Physical Intelligence in VLMs via a Perception-Reasoning-Assessment Loop
**Authors:** Xinge Peng, Yiting Lu, Tianwu Zhi, Wen Wen, Jianzhao Liu, Xin Li, Zhibo Chen
**arXiv:** [arxiv.org/abs/2610.00559](https://arxiv.org/abs/2610.00559)
**Summary:** PhysVista evaluates VLM physical intelligence as a closed loop spanning state perception, dynamics reasoning, and plausibility assessment on real and generated videos. Broad testing reveals a persistent gap between visual recognition and reliable physical understanding, especially for reasoning and authenticity judgments.

---

### 16. Smaller Models, Better Rejects: Preference Distillation Scaling
**Authors:** Rui Cai, Wenhui Zhu, Xiwen Chen, Jincheng Cao, Han Yu, Shayan Mohajer Hamidi, Zelin He, Qiyao Ma, Daiwei Chen, Xuanzhao Dong, Yuanda Xu, Jelena Markovic-Voronov, Kayhan Behdin, Zhengze Zhou, Ran He, Alborz Geramifard, Rohit Jain, Zhe Zhao
**arXiv:** [arxiv.org/abs/2609.38987](https://arxiv.org/abs/2609.38987)
**Summary:** This study finds that smaller frozen models can generate cheaper and more effective rejected responses for preference distillation than a student's own outputs. Experiments across 7B to 72B students show that task-structured, lower-likelihood rejects improve code and mathematical reasoning while reducing generation cost.

---

### 17. Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes
**Authors:** Sophia Sirko-Galouchenko, Monika Wysoczanska, Andrei Bursuc, Nicolas Thome, Spyros Gidaris
**arXiv:** [arxiv.org/abs/2610.02117](https://arxiv.org/abs/2610.02117)
**Summary:** Where-OPD gives a privileged teacher text-based spatial guidance from procedurally generated scenes, then distills the behavior into a student that sees only the image and question. Training solely on synthetic scenes improves counting, document, and chart tasks and transfers to real-world perception benchmarks with a 3.23-point average gain.

---

### 18. Better Supervision Is Nearby: Neighborhood On-Policy Self-Distillation
**Authors:** Xincheng Wei, Yifan Ding, Yoshua Li, Yuquan Lu, Ziheng Li, Yi Lu, Dongsheng Ma, Rongxiang Weng, Xunliang Cai
**arXiv:** [arxiv.org/abs/2609.39687](https://arxiv.org/abs/2609.39687)
**Summary:** Neighborhood OPSD builds a compact pool of locally perturbed frozen experts whose complementary corrections supervise student-visited states in mathematical reasoning. Across three model sizes and three competition benchmarks, it consistently improves Average@12 over standard on-policy self-distillation while requiring only the distilled student at inference.

---

### 19. AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding Agent Pipelines
**Authors:** Sumin Lee, Sukmin Cho, Suengjae Lim, Youngjin Kwon
**arXiv:** [arxiv.org/abs/2610.01108](https://arxiv.org/abs/2610.01108)
**Summary:** AgSpec augments retrieval-based speculative decoding for coding agents with session, workspace, and global corpora plus per-agent adaptive draft lengths. On repository-level multi-agent benchmarks it reaches up to 4.37 times the single-batch throughput and 4.76 times the larger-batch throughput of autoregressive decoding.

---

### 20. Benchmarking and Enhancing Skill-Level Memory for Partially Observable Robotic Manipulation
**Authors:** Yansong Shi, Jiange Yang, Xijie Yang, Shaowei Zhang, Yuhan Zhu, Tao Lu, Limin Wang
**arXiv:** [arxiv.org/abs/2609.38886](https://arxiv.org/abs/2609.38886)
**Summary:** HIDE benchmarks memory under partial observability across 15 robotic manipulation tasks involving repetition, historical-state recall, and progress tracking. SEEK combines three memory mechanisms and achieves the highest average success among evaluated configurations in simulation and real-world experiments, while showing that individual mechanisms can hurt mismatched tasks.
