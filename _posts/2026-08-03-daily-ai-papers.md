---
title: "Daily AI Papers — August 03, 2026"
date: 2026-08-03
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-03/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - world-models
  - robotics
---

### 1. From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement
**Authors:** Qinsi Wang, Jing Shi, Huazheng Wang, Kun Wan, Yiran Wu, Bo Liu, Qingyun Wu, Hai Helen Li, Yiran Chen, Handong Zhao, Wentian Zhao
**arXiv:** [arxiv.org/abs/2607.23802](https://arxiv.org/abs/2607.23802)
**Summary:** RLVR drives strong LLM reasoning gains in math and coding where correctness is deterministically checkable, but open-ended tasks usually rely on noisy human/LLM judges instead. This paper transforms open-ended tasks into self-verifiable ones (RLSVR), extending verifiable-reward RL self-improvement beyond narrow, checkable domains.
**Trending because:** Top of today's HuggingFace Daily Papers with 65 upvotes — the highest of the day.

---

### 2. Mental World Modeling
**Authors:** Hao Fei, Yiran Zhao
**arXiv:** [arxiv.org/abs/2607.27201](https://arxiv.org/abs/2607.27201)
**Summary:** Existing world models predict physical scene evolution but ignore agents' hidden mental states (beliefs, desires, intentions), so they can mispredict actions even with a correctly modeled scene. The paper formulates Mental World Modeling to jointly track physical dynamics and agents' internal mental states for better action prediction.
**Trending because:** 50 upvotes on HuggingFace Daily Papers, second-highest of the day.

---

### 3. $N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens
**Authors:** NeoteAI Team, Fudan TEAI Team
**arXiv:** [arxiv.org/abs/2607.23782](https://arxiv.org/abs/2607.23782)
**Summary:** Introduces a vision-tactile-language-action foundation model for fine-grained, contact-rich manipulation, adding tactile perception via visuo-tactile pretraining and staged tactile-pathway integration on top of vision-based backbones. It also supports offline policy improvement from stored deployment data using advantage conditioning.
**Trending because:** 49 upvotes; companion paper to #5 below, part of a coordinated tactile-robotics release.

---

### 4. Meshy T2: Fast Native Mesh Generation with Flow Matching
**Authors:** Jiale Xu, Rendong Liang, Yuhao Long, Siyuan Shen, Zangyueyang Xian, Zeyi Xu, Yuanming Hu
**arXiv:** [arxiv.org/abs/2607.28675](https://arxiv.org/abs/2607.28675)
**Summary:** Standard mesh generation serializes meshes into token sequences and decodes them autoregressively, which is slow and prone to error accumulation for interactive use. Meshy T2 instead uses flow matching for fast, native mesh generation with artist-style topology suitable for film, gaming, and interactive 3D pipelines.
**Trending because:** 40 upvotes; strong interest in production-ready 3D generative tooling.

---

### 5. $N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation
**Authors:** NeoteAI Team, Fudan TEAI Team
**arXiv:** [arxiv.org/abs/2607.23783](https://arxiv.org/abs/2607.23783)
**Summary:** Presents what the authors describe as the first tactile world-action model trained at large scale, jointly predicting future vision and future contact for contact-rich manipulation. It is pre-trained on visuo-tactile demonstrations across six embodiments and 450 tasks using a unified force-based tactile representation called NeoForce.
**Trending because:** 26 upvotes; paired release with #3, signaling a push toward tactile-native robot foundation models.

---

### 6. Scaling Properties of Text Conditioning in Visual Generation
**Authors:** Zilong Chen, Chaorui Deng, Kunchang Li, Hongyi Yuan, Haoqi Fan
**arXiv:** [arxiv.org/abs/2607.29679](https://arxiv.org/abs/2607.29679)
**Summary:** Studies how diffusion training loss scales with the structure of natural-language prompts, since loss doesn't scale simply with token count. Using both a white-box likelihood metric and a black-box attribute metric, the authors find converged diffusion loss scales predictably with the amount of structured language in the prompt.
**Trending because:** 23 upvotes; addresses a fundamental scaling-law gap in text-to-image/video generation.

---

### 7. SAF-OPD: Stable Advantage Fusion for On-Policy Distillation
**Authors:** Yifan Ding, Xincheng Wei, Yoshua Y. Li, Ziheng Li, Yuquan Lu, Siyu Zhang, Dongsheng Ma, Rongxiang Weng, Xunliang Cai, Yun Chen
**arXiv:** [arxiv.org/abs/2607.29209](https://arxiv.org/abs/2607.29209)
**Summary:** Combining RLVR's response-level rewards with on-policy distillation's dense per-token teacher signal is appealing but naive fusion triggers entropy collapse from magnitude and calibration mismatches between the two signals. SAF-OPD proposes a stable fusion method that combines both advantages without destabilizing training.
**Trending because:** 22 upvotes; tackles a practical failure mode in combining two popular LLM post-training techniques.

---

### 8. Fewer Clarifications, Better Code: Benchmarking Cross-Session Personalized Ambiguity Adaptation in Coding Assistants
**Authors:** Zijian Xu, Wenshuo Zhang, Zisen Qin, Rui Sheng, Yushi Sun, Huamin Qu, Chuhan Shi
**arXiv:** [arxiv.org/abs/2607.26611](https://arxiv.org/abs/2607.26611)
**Summary:** AI coding assistants often re-ask the same clarifying questions across sessions even when a user's past resolutions reveal consistent, personal preferences. This benchmark measures whether assistants can use cross-session memory of resolved ambiguity to reduce repeated clarification requests.
**Trending because:** 19 upvotes; directly relevant to daily-use coding-assistant UX.

---

### 9. Enhancing Rubric-based RL via Self-Distillation
**Authors:** Mingxuan Xia, Yuhang Yang, Chao Ye, Shuai Zhu, Shenzhi Yang, Guangcheng Zhu, Yuhang Zhang, Cheng Peng, Haobo Wang, Siqing Wang
**arXiv:** [arxiv.org/abs/2607.18082](https://arxiv.org/abs/2607.18082)
**Summary:** In rubric-based RL, criteria that no rollout ever satisfies get no learning signal, and prior fixes that inject rubric guidance during rollout create a train-inference mismatch. This paper uses self-distillation so the policy internalizes guided behavior without needing that external guidance at inference time.
**Trending because:** 14 upvotes; addresses a known blind spot in rubric/reward-based RL training for LLMs.

---

### 10. ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction
**Authors:** Boyang Zhang, Adrian Lyjak, Eli Stewart, Zhaoqi Li, Simon Suo
**arXiv:** [arxiv.org/abs/2607.29677](https://arxiv.org/abs/2607.29677)
**Summary:** Introduces a benchmark for agentic schema-guided document extraction that jointly scores value accuracy, completeness, grounding, and cost — reportedly the first to combine all four. It spans 4,869 pages across 370 enterprise document types.
**Trending because:** 13 upvotes; fills a gap in evaluating enterprise-grade document AI agents.

---

### 11. Evaluation-Verification Reward for Consistent Multi-Reference Image Editing
**Authors:** Yingmao Miao, Pengfei Zhang, Xiaochen Lv, Meng Yu, Lei Sun, Xiangxiang Chu, Chao Shen, Chenhao Lin
**arXiv:** [arxiv.org/abs/2607.29025](https://arxiv.org/abs/2607.29025)
**Summary:** Multi-reference image editing struggles to keep visual consistency across several reference images, and RL methods lack reward models that capture multi-image relational constraints. This paper proposes an evaluation-verification reward scheme to make RL-based training practical for consistent multi-reference editing.
**Trending because:** 11 upvotes; extends RL-for-generation techniques into a harder multi-image setting.

---

### 12. ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow
**Authors:** Dongxiu Liu, Haoyi Niu, Peng Cheng, Yuan Gao, Xirui Kang, Sangli Teng, Koushil Sreenath, Xianyuan Zhan
**arXiv:** [arxiv.org/abs/2607.27924](https://arxiv.org/abs/2607.27924)
**Summary:** Most world models predict in discrete time steps despite the physical world being continuous, which limits their efficiency at capturing real dynamics. ODEWorld introduces Physical-Time Flow, a continuous latent velocity field that models sequential dynamics directly in physical time.
**Trending because:** 7 upvotes; part of a broader cluster of world-model papers trending today (alongside #2 and #14).

---

### 13. RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models
**Authors:** Derek Ming Siang Tan, Shailesh Shailesh, Srikrishna Iyer, William Wei Jie Teo, Yuanliang Ju, Qiao Gu, Guillaume Sartoretti
**arXiv:** [arxiv.org/abs/2607.26991](https://arxiv.org/abs/2607.26991)
**Summary:** VLA models degrade on out-of-domain tasks, and existing test-time steering methods apply the same intervention at every timestep regardless of context, inheriting correlated failure modes. RL$^2$-VLA proposes adaptive, context-aware latent steering with test-time scaling to fix this.
**Trending because:** 4 upvotes; addresses robustness gaps in deployed robot VLA policies.

---

### 14. One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA
**Authors:** Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov
**arXiv:** [arxiv.org/abs/2607.28443](https://arxiv.org/abs/2607.28443)
**Summary:** Asks whether every robot in a swarm can agree on the same predicted future collective state using only local observations and bandwidth-limited peer messages. CS-JEPA, a decentralized joint-embedding predictive architecture, has each robot output one shared future token field with no global pooling or targets required.
**Trending because:** 3 upvotes; novel decentralized extension of JEPA-style world modeling to multi-robot swarms.

---

### 15. Toward Robust and 3D-Aware RGB-NIR Imaging in the Dark
**Authors:** Muyao Niu, Mingze Ma, Yifan Zhan, Qingtian Zhu, Zhihang Zhong, Wei Guo, Chang Wen Chen, Yinqiang Zheng
**arXiv:** [arxiv.org/abs/2607.29684](https://arxiv.org/abs/2607.29684)
**Summary:** Existing RGB-NIR low-light fusion methods depend on carefully curated paired training data and generalize poorly across scenarios. This paper adds 3D-aware neural modeling to fuse extremely noisy RGB with NIR without requiring clean RGB supervision.
**Trending because:** 2 upvotes; practical low-light computer vision advance with no clean-data requirement.

---

### 16. SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark for UAV/UGV-Based SUrface LANDmine Detection Under Domain Shift
**Authors:** Sagar Lekhak, Prasanna Reddy Pulakurthi, Lalit Joshi, Ramesh Bhatta, Emmett J. Ientilucci
**arXiv:** [arxiv.org/abs/2607.28996](https://arxiv.org/abs/2607.28996)
**Summary:** Public RGB landmine-detection datasets are scarce and existing benchmarks lack cross-architecture and out-of-distribution testing, obscuring real-world generalization. SULAND v2 provides a refined dataset and benchmark for evaluating detector robustness on PFM-1 and PMA-2 landmines under domain shift.
**Trending because:** 2 upvotes; safety-critical humanitarian application of AI object detection.

---

### 17. Beyond Feeling Better: Capability-Sustaining Emotional Dialogue as a Longitudinal Research Paradigm
**Authors:** Ming Wang, Jiaqi Wu Young, Wenfang Wu, Daling Wang, Shi Feng
**arXiv:** [arxiv.org/abs/2607.27851](https://arxiv.org/abs/2607.27851)
**Summary:** Existing emotional-dialogue research (empathetic dialogue, emotional support conversation) optimizes for momentary comfort rather than sustained user wellbeing. The paper proposes capability-sustaining emotional dialogue, a longitudinal paradigm aimed at preserving users' emotion regulation, coping, and social-connection capacities over time.
**Trending because:** 2 upvotes; reframes a well-studied area (emotional support chatbots) around long-term user outcomes.

---

### 18. Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocation for Long-CoT Reasoning
**Authors:** Qiangqiang He, Zhongheng Wu, ZiJian Wang
**arXiv:** [arxiv.org/abs/2607.27888](https://arxiv.org/abs/2607.27888)
**Summary:** Critic-free RLVR methods like GRPO broadcast a single response-level reward uniformly across all tokens, ignoring that tokens contribute unequally to the final outcome. This paper introduces counterfactual sensitivity-based credit reallocation to give long chain-of-thought tokens differentiated training signal.
**Trending because:** 2 upvotes; part of a cluster of papers refining token-level credit assignment in RLVR today.

---

### 19. Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs
**Authors:** Pingyu Wu, Lingyao Zhu, Weiming Zhang, Nenghai Yu
**arXiv:** [arxiv.org/abs/2607.27951](https://arxiv.org/abs/2607.27951)
**Summary:** LLM safeguards typically decide whether to answer before knowing how the answer will be used, which breaks down for dual-use tasks when an attacker can copy/imitate a benign requester's interaction history. The authors derive an exact worst-case bound on attacker assistance achievable when the evidence a safeguard relies on is copyable.
**Trending because:** 1 upvote; a notable theoretical result on the limits of LLM safety-by-context approaches.

---

### 20. In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous Driving System Testing
**Authors:** Qunying Song, Yuan Gao, Johannes Betz, Dietmar Pfahl, Mohammad Reza Mousavi, Federica Sarro
**arXiv:** [arxiv.org/abs/2607.15820](https://arxiv.org/abs/2607.15820)
**Summary:** Reports an interview study with practitioners across multiple companies on how autonomous driving system (ADS) testing is actually done, finding the field still lacks standardized scenario selection, evaluation, and acceptance criteria. Offers empirical, industry-grounded insight that contrasts with academic assumptions about ADS testing maturity.
**Trending because:** 1 upvote; rare empirical/industry study format among today's papers.
