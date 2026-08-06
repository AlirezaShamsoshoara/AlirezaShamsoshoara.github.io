---
title: "Daily AI Papers — August 06, 2026"
date: 2026-08-06
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-06/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-agents
  - benchmarks
  - world-models
---

### 1. ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment
**Authors:** Yijun Lu, Rui Ye, Jiajun Wang, Yuwen Du, Tian Jin, Songhua Liu, Siheng Chen
**arXiv:** [arxiv.org/abs/2608.05102](https://arxiv.org/abs/2608.05102)
**Summary:** Long-horizon search agents must make multiple sequential actions (steps) to search, retrieve, verify, and integrate evidence to reach a final answer. However, existing methods for training these agents typically treat all steps within a trajectory uniformly during both supervised fine-tuning (SFT) and reinforcement learning (RL), failing to distinguish useful actions from erroneous or redundant ones.
**Trending because:** 52 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 2. ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image Generation
**Authors:** Jiahao Zhao, Xiaomin Yu, Zhongxiang Sun, Fengwei Teng, Chengwei Qin, Xiaobin Hu, Jun Xu, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2608.04436](https://arxiv.org/abs/2608.04436)
**Summary:** Text-to-image (T2I) models can produce visually compelling images, yet they remain limited on open-world tasks that require complex semantic understanding, multi-step reasoning, and the integration of external world knowledge. Existing efforts introduce agent capabilities into image generation, but they either prescribe a fixed workflow or place only a subset of the open-world image generation process under agent control.
**Trending because:** 45 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 3. The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads
**Authors:** Yushi Sun, Yanjie Zhang, Rui Sheng
**arXiv:** [arxiv.org/abs/2608.04570](https://arxiv.org/abs/2608.04570)
**Summary:** Personalized LLMs with persistent memory are increasingly deployed, yet the faithfulness of their user models remains unexamined. We study over-inference (OI): the phenomenon where LLMs fabricate user attributes beyond what evidence supports.
**Trending because:** 37 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 4. Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality Synergy, Early Unification, and Recipes
**Authors:** Junlin Han, Shengbang Tong, David Fan, Minghao Chen, Philip Torr, Filippos Kokkinos, Mike Lewis
**arXiv:** [arxiv.org/abs/2608.05000](https://arxiv.org/abs/2608.05000)
**Summary:** Vision offers a critical axis for advancing foundation models, driving a shift towards natively unified multimodal pretraining. Despite this momentum, the design space and the fundamental mechanisms of how modalities interact during unified training remain underexplored.
**Trending because:** 37 HuggingFace upvotes; among the most-upvoted fresh papers in today's feed.

---

### 5. OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents
**Authors:** Jingsheng Zheng, Xinyuan Fang, Jintian Zhang, Zhengke Gui, Huajun Chen, Ningyu Zhang
**arXiv:** [arxiv.org/abs/2608.05013](https://arxiv.org/abs/2608.05013)
**Summary:** LLM agents are increasingly applied to open-ended everyday requests that span work, study, and life. These tasks are long-horizon, cross-environment, and multimodal, forcing the agent to preserve goals and constraints across many steps while navigating heterogeneous tools and attachments.
**Trending because:** 27 HuggingFace upvotes; solid community engagement on today's feed.

---

### 6. GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks
**Authors:** Leijun Zhou, Zhihao Liu, Xiang Qu, Chenxu Liu, Yifei Liu, Yanke Yu, Jingzhe Xu, Xuejun Wu, Buyue Qian, Xi Chen, Yaowei Zheng, Junhao Hu
**arXiv:** [arxiv.org/abs/2608.03764](https://arxiv.org/abs/2608.03764)
**Summary:** Agent self-evolution updates an agent's persistent state from prior experience and reuses it to solve related tasks more effectively. Evaluating self-evolution is difficult: existing benchmarks provide limited coverage of economically valuable task domains, do not always design training and test tasks such that test-time gains can be attributed to training experience, and remain vulnerable to data contamination.
**Trending because:** 21 HuggingFace upvotes; solid community engagement on today's feed.

---

### 7. Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning
**Authors:** Yinghui He, Ling Yang, Jiarui Liu, Yongjin Yang, Lechen Zhang, Yingcheng Wu, Zhenfei Yin, Mengdi Wang, Sanjeev Arora
**arXiv:** [arxiv.org/abs/2608.05139](https://arxiv.org/abs/2608.05139)
**Summary:** Long-horizon reasoning in recent LLMs demands that the model switch between distinct skills inside a reasoning chain, such as first doing a math derivation, then using the result to plan a schedule. We call such problems cross-skill long-horizon tasks: multi-step tasks whose steps require different reasoning skills and depend on earlier outputs.
**Trending because:** 20 HuggingFace upvotes; solid community engagement on today's feed.

---

### 8. When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation
**Authors:** Yinuo Jiang, Yongjie Ye, Zhou Tao, Xiang Zhuang, Qiang Zhang, Huajun Chen, Tiankai Li
**arXiv:** [arxiv.org/abs/2608.03632](https://arxiv.org/abs/2608.03632)
**Summary:** On-Policy distillation (OPD) transfers teacher capabilities by supervising student-sampled trajectories with dense token-level teacher signals. Recent selective OPD methods improve this process by prioritizing signals that are confident, informative, or learnable.
**Trending because:** 18 HuggingFace upvotes; solid community engagement on today's feed.

---

### 9. Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data
**Authors:** Ye Wang, Pei Lin, Xiong-Hui Chen, Haoqi Yuan, Zhixuan Liang, Yiyang Huang, Anzhe Chen, Zixing Lei, Jie Zhang, Tao Zhang, Haoyang Li, Tong Zhang, Chenxi Xiao, Ziyuan Jiao, Qin Jin
**arXiv:** [arxiv.org/abs/2608.02580](https://arxiv.org/abs/2608.02580)
**Summary:** Learning generalizable robot manipulation policies requires large-scale and diverse demonstration data. Egocentric human manipulation videos offer rich scene and task diversity, and prior work has shown that retargeting and rendering such videos into robot-format data can yield effective per-task policies at small scale.
**Trending because:** 16 HuggingFace upvotes; solid community engagement on today's feed.

---

### 10. NOLLI: A Difficulty-Calibrated Puzzle Benchmark for Diagnosing the English-Korean Performance Gap
**Authors:** Dasol Choi, Joonyong Park, Daegon Yu, Soo Yong Kim, Youngsook Song, Seunghyeok Hong
**arXiv:** [arxiv.org/abs/2608.04397](https://arxiv.org/abs/2608.04397)
**Summary:** We introduce NOLLI, a procedurally generated English-Korean puzzle benchmark designed to diagnose where Korean performance gaps arise. It comprises 15 puzzle types (25 tasks; 7,500 items), with every instance seed-regenerable, verified to have a unique solution, and scored deterministically.
**Trending because:** 16 HuggingFace upvotes; solid community engagement on today's feed.

---

### 11. AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities
**Authors:** Yuqing Wen, Yukai Huang, Qianqian Xie, Jiangtao Wu, Yibin Lin, Yikai Gu, Jialu Chen, Yuanxing Zhang, Jiaheng Liu
**arXiv:** [arxiv.org/abs/2607.24821](https://arxiv.org/abs/2607.24821)
**Summary:** While instruction-based video editing has advanced rapidly, real-world videos contain tightly coupled audio and visual signals, and editing one modality often requires coordinated changes in the other. Existing benchmarks primarily evaluate visual transformations on silent clips or isolated audio editing, leaving complex audio-visual editing and cross-modal consistency underexplored.
**Trending because:** 15 HuggingFace upvotes; solid community engagement on today's feed.

---

### 12. Decoding Children's Gait Behavior
**Authors:** Yifan Shen, Boyi Li, Meihuan Huang, Yuanzhe Liu, Xu Cao, Jinyang Jin, Zhengyuan Li, Anglin Liu, Junho Kim, Jingyuan Zhu, Lan Fangzhou, Jianguo Cao, Jintai Chen, Ismini Lourentzou, James Matthew Rehg
**arXiv:** [arxiv.org/abs/2608.00371](https://arxiv.org/abs/2608.00371)
**Summary:** We introduce a new problem domain for human action recognition: the fine-grained analysis of children's gait behaviors from standard RGB video. We specifically target the ambulatory patterns of children aged 3-17 years.
**Trending because:** 13 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---

### 13. MiniWorld: Democratizing the Training of Video World Models from Scratch
**Authors:** Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang, Jie Chen
**arXiv:** [arxiv.org/abs/2608.01127](https://arxiv.org/abs/2608.01127)
**Summary:** Video world models predict future observations conditioned on historical observations and control signals, enabling long-horizon generation through autoregressive state transitions. Unlike conventional video generation models that primarily capture visual appearance and motion, video world models learn the underlying dynamics governing environment evolution under agent actions, providing a foundation for embodied AI and interactive simulation.
**Trending because:** 13 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---

### 14. When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents
**Authors:** Yushi Sun, Yanjie Zhang
**arXiv:** [arxiv.org/abs/2608.04574](https://arxiv.org/abs/2608.04574)
**Summary:** Memory-augmented VLM agents act on persistent spatial knowledge, yet that knowledge silently goes stale as the environment changes. We ask what happens when an agent must reconcile a confident memory claim with a contradicting observation, and whether current models can catch the conflict before it becomes a safety-relevant mistake.
**Trending because:** 12 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---

### 15. ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?
**Authors:** Tianyi Guan, Yiding Wang, Haotong Yang, Siyuan Cao, Shirui Liu, Yi Hu, Jiaqi Li, Muhan Zhang
**arXiv:** [arxiv.org/abs/2608.03874](https://arxiv.org/abs/2608.03874)
**Summary:** Modern agent frameworks equip large language models with external skill libraries to solve complex tasks. However, it remains unclear whether these systems can effectively evolve their skills and whether the resulting skills improve task-solving capabilities.
**Trending because:** 11 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---

### 16. Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups from Adaptive Teacher Guidance
**Authors:** Zhuowen Han, Jinwei Xiao, Zhengxi Lu, Renren Jin, Zhiyuan Yao, Yuxin Liu, Hongyan Hao, Yueqing Sun, Yu Yang, Qi GU, Xunliang Cai, Deyi Xiong
**arXiv:** [arxiv.org/abs/2608.00782](https://arxiv.org/abs/2608.00782)
**Summary:** Reinforcement learning with verifiable rewards (RLVR) has become a standard paradigm for post-training large language models (LLMs). While Group Relative Policy Optimization (GRPO) is widely adopted, it suffers from sparse reward signals and loses gradients entirely when all responses within a group receive identical rewards.
**Trending because:** 11 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---

### 17. K-EXAONE 2.0 Technical Report
**Authors:** Eunbi Choi, Kibong Choi, Sehyun Chun, Seokhee Hong, Junwon Hwang, Hyojin Jeon, Ahra Jo, Hyunjik Jo, Yeonsik Jo, Minhyeok Jung, Doyoung Kim, Heegyu Kim, Joonkee Kim, Seonghwan Kim, Soyeon Kim, Sunkyoung Kim, Yireun Kim, Yongil Kim, Byungoh Ko, Changhun Lee, Dohaeng Lee, Haeju Lee, Jinsik Lee, Kyungmin Lee, Minwoo Lee, Wonkee Lee, Sangha Park, Sungjune Park, Kwangrok Ryoo, Kijung Seo, Minju Seo, Yongwoo Song, Sejong Yang, Heuiyeen Yeen, Stanley Jungkyu Choi, and collaborators
**arXiv:** [arxiv.org/abs/2608.04505](https://arxiv.org/abs/2608.04505)
**Summary:** This technical report presents K-EXAONE 2.0, an open-weight multilingual foundation model developed by LG AI Research as a step in our effort toward global frontier-scale foundation models. Rather than training from scratch, we upcycle K-EXAONE and expand its architecture, yielding a Mixture-of-Experts (MoE) model with 750B total parameters and approximately 37B activated per token---more than three times the capacity of its predecessor.
**Trending because:** 11 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---

### 18. Are the Financial Reasoning from LLMs Credible? A Real World Test over Long-Horizon Statements
**Authors:** Xinke Tong, Xuanming Zhang, Tianyi Tang, An Yang, Jiatu Hu, Guojie Lin, Zhenzhen Shi, Lingfeng Zeng, Boyu Yang, Bing Zhao, Hu Wei, Lin Qu, Dayiheng Liu
**arXiv:** [arxiv.org/abs/2607.28661](https://arxiv.org/abs/2607.28661)
**Summary:** Do Large Language Models (LLMs) possess genuine structural reasoning, or merely rely on surface-level pattern matching? The financial domain, demanding numerical precision and multi-step logic over long contexts, is an ideal testbed.
**Trending because:** 10 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---

### 19. FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory
**Authors:** Zhuoran Zhang, Bowen Li, Jingcheng Ju, Yang Shi, Qixun Wang, Haotian Wang, Wei Chen, Tengjiao Wang
**arXiv:** [arxiv.org/abs/2608.04530](https://arxiv.org/abs/2608.04530)
**Summary:** GUI agents must remember both useful experience from earlier tasks and unfinished progress in the current interaction. Latent memory offers a compact solution by compressing multimodal trajectories into a few continuous tokens.
**Trending because:** 10 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---

### 20. HelloWorld: Enabling Socially Interactive Characters in Video World Models
**Authors:** Liangyang Ouyang, Ruicong Liu, Xuangeng Chu, Kaipeng Zhang, Yoichi Sato
**arXiv:** [arxiv.org/abs/2608.05070](https://arxiv.org/abs/2608.05070)
**Summary:** Despite the remarkable recent progress of video world models, social interaction between users and the characters within these worlds remains unsupported. To fill this gap, we present HelloWorld, a video world model that enables social interaction with in-world characters.
**Trending because:** 10 HuggingFace upvotes; a fresh paper gaining traction in today's feed.

---
