---
title: "Daily AI Papers — October 01, 2026"
date: 2026-10-01
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-01/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - self-improvement
  - multimodal-ai
---

### 1. The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation Residuals in On-Policy Distillation
**Authors:** Hao Li, MeiJia Chen, Weijie Ren, Donghan Li, Zijun Tian, Jingchun Huang, Naibo Wang
**arXiv:** [arxiv.org/abs/2609.36484](https://arxiv.org/abs/2609.36484)
**Summary:** RIDE measures the representation residual between an RL-trained teacher and its pre-RL checkpoint at every layer, then trains the student toward hidden-state targets extrapolated beyond the teacher along that direction. Across four model pairs, it approaches or exceeds every RL teacher and consistently outperforms output-space extrapolation, especially when the teacher remains close to its base model.

---

### 2. UniEvo-VL: An On-policy Self-Distillation Training Recipe for Multimodal Model Self-improvement
**Authors:** Fang Wu, Da Xing, Yanjie Huang, Junxi Wang, Ji Wang, Hejia Geng, Guancheng Wan, Bowen Zuo, Xiaomin Li, Shixiang Tang, Xinyu Xiang, Zehong Wang, Shiyi Du, Peng Xia, Shuangjia Zheng, Yining Hong, Li Erran Li, Jure Leskovec, Yejin Choi
**arXiv:** [arxiv.org/abs/2609.38721](https://arxiv.org/abs/2609.38721)
**Summary:** UniEvo-VL uses one multimodal model as both student and critique-conditioned teacher, distilling denoising distributions along the student's own image-generation trajectories without an external supervisor. On Qwen-Image-2512 it raises GenEval from 0.747 to 0.808 and GenEval2 Soft-TIFA from 32.97 to 35.53, while revealing that self-improvement remains uneven across tasks such as text rendering.

---

### 3. False Frontiers: Diagnosing and Mitigating Co-Cheating in Self-Evolving Search Agents
**Authors:** Meijia Chen, Hao Li, Zheng Lu, Hongshan Lin, Junbai Tian, Yichen Liu, Zijun Tian, Yufan Zou, Shuhan Sun, Hanxin Chen, Zeyu Zhang, Weizhi Du, Yueting Li, Tianyu Shi, Alaa Khamis
**arXiv:** [arxiv.org/abs/2609.39102](https://arxiv.org/abs/2609.39102)
**Summary:** This work identifies co-cheating in self-evolving search agents, where a question proposer and solver increasingly reinforce shared errors even as their internal reward rises. CrossFit breaks that feedback ancestry by scoring questions with a solver trained on disjoint source documents, roughly halving false agreement and improving seven search benchmarks by more than eight average points over coupled self-evolution.

---

### 4. AREX-2: Advancing Self-Improving Agents through Long-Horizon Reflective Tasks
**Authors:** Hongjin Qian, Chaofan Li, Kun Luo, Wenqing Wei, Jianlyu Chen, Shuqi Lu, Yuyang Hu, Hongwang Xiao, Hui Wang, Chaozhuo Li, Qiwei Ye, Zhicheng Dou, Defu Lian, Zheng Liu
**arXiv:** [arxiv.org/abs/2609.38288](https://arxiv.org/abs/2609.38288)
**Summary:** AREX-2 trains long-horizon reflection and execution using verifiable improvement trajectories from machine learning and algorithmic programming tasks. The resulting Qwen3.8-27B agent reaches 81.8 on MLE-bench Lite and transfers strongly to research benchmarks including 84.0 on BrowseComp, with performance continuing to improve as more iteration rounds are allowed.

---

### 5. Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents
**Authors:** Minki Kang, Ryo Hachiuma, Shaokun Zhang, Subhashree Radhakrishnan, Yonggan Fu, Jindong Jiang, Mingjie Liu, Ehsan Hosseini-Asl, Yi Dong, Yu-Chiang Frank Wang, Byung-Kwan Lee
**arXiv:** [arxiv.org/abs/2609.39982](https://arxiv.org/abs/2609.39982)
**Summary:** Mid-Harness samples and verifies multiple candidate terminal actions before allowing one to alter the environment, adding test-time compute at the model-harness boundary without changing either component. With TMAX-9B as generator, an eight-action GPT-5.6 Sol verifier raises TerminalBench-Lite Pass@1 from 50.00% to 68.03%, and distilled verification preserves further gains at lower cost than trajectory-only scaling.

---

### 6. EvoDuet: Bilevel Co-Evolution of Web Searching and Task Solving for Scientific Discovery
**Authors:** Young-Jun Lee, Jinheon Baek, Soyeong Jeong, Minki Kang, Seungyeon Jwa, Jonghyun Choi, Seungho Han, Dongyeop Kang
**arXiv:** [arxiv.org/abs/2609.40340](https://arxiv.org/abs/2609.40340)
**Summary:** EvoDuet co-evolves scientific solutions and web-search queries through an inner retrieval loop that predicts useful documents and an outer loop that evaluates candidates and records outcomes. It lifts normalized discovery gain from 74.1% to 78.0% with GPT-5.6-Luna and from 61.3% to 82.3% with Gemini-3.8-Flash, surpassing prior best scores on eight of 21 optimization tasks.

---

### 7. WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents
**Authors:** Ziyan Jiang, Jingbo Yang, Jiabao Ji, Yujian Liu, Qiucheng Wu, Tommi Jaakkola, Yang Zhang, Shiyu Chang
**arXiv:** [arxiv.org/abs/2609.40325](https://arxiv.org/abs/2609.40325)
**Summary:** WorldAuditBench evaluates agents that must navigate interactive 3D worlds while detecting and validating anomalies such as floating objects and traversable walls. Its 213 tasks across 13 environments expose a large action-reasoning gap: five frontier models achieve only 6.6% to 42.3% success under fixed exploration budgets, versus 83.4% for humans.

---

### 8. Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI
**Authors:** Cheng Qian, Kunlun Zhu, Beibin Li, Zhenhailong Wang, Heng Ji
**arXiv:** [arxiv.org/abs/2609.38143](https://arxiv.org/abs/2609.38143)
**Summary:** Meta-Skill lets a Builder agent learn reusable principles for constructing execution harnesses around a fixed Target model from development-set feedback. On Harness-Bench and NewtonBench, a frozen bank of these skills improves macro-average performance by 8.95 points over no-skill construction and by 12.02 points over handing the same skills directly to the Target.

---

### 9. EVOKE: Eliciting World Knowledge in Agents for Transferable Decision-Making
**Authors:** Yuhan Guo, Jinming Liu, Liang Xu, Ziqiang Li, Jianguo Huang, Zhicheng Wang, Hu Zhu, Qiuyu Chen, Yuntao Wei, Xin Jin, Wenjun Zeng
**arXiv:** [arxiv.org/abs/2609.38334](https://arxiv.org/abs/2609.38334)
**Summary:** EVOKE holds an environment state and interaction history fixed while asking an agent to rank the same actions under diverse goals, forcing its decisions to expose pretrained world knowledge instead of superficial single-goal habits. Across three model backbones and multiple tasks, this post-training method improves task performance, unseen-environment transfer, and data efficiency without explicit future-observation prediction.

---

### 10. More Choices, Fewer Decisions: Ordinal-Scale Bias in JEV-like Direct-Decision Models
**Authors:** Tianxiang Gao, Jinzhe Li, Zhiyuan Li, Yi Chang, Yuan Wu
**arXiv:** [arxiv.org/abs/2609.38827](https://arxiv.org/abs/2609.38827)
**Summary:** The authors identify ordinal scale-utilization bias in direct-decision models: as an ordered label scale grows, models increasingly compress predictions into only part of the available support even when candidate probabilities remain broad. Across JEV and KEV models, utilization falls to 26% to 75% at 14 choices, while targeted BA-LoRA raises gold-relative utilization from about 47% to 86% on eight supervised scales.

---

### 11. RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement
**Authors:** Wenyi Wu, Minghao Fu, Jieyu You, Kun Zhou, Siqi Liu, Aayush Salvi, Yiheng Lin, Ce Zhang, Xiaohan Lan, Jiahui Zhu, Yujie Zhong, Qi She, Biwei Huang
**arXiv:** [arxiv.org/abs/2609.39045](https://arxiv.org/abs/2609.39045)
**Summary:** RSIGame improves generated games through a local explore-diagnose-revise loop with an evolving checklist and a global loop that preserves the best checkpoint and detects regression. Across 140 GameCraft-Bench tasks, internalized development experience lets Qwen3.8-27B surpass GPT-5.5 one-shot scores on Godot and Phaser while using eleven times fewer generation tokens.

---

### 12. Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering
**Authors:** Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, Wonjun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
**arXiv:** [arxiv.org/abs/2609.38177](https://arxiv.org/abs/2609.38177)
**Summary:** Imagine3D-LLM appends summary tokens to multi-view image inputs and decodes them into a compact 3D Gaussian Splatting scene under photometric reconstruction supervision. Joint reconstruction and language training strengthens cross-view correspondence throughout the model and consistently outperforms prior spatial-reasoning and 3D-understanding approaches.

---

### 13. LANTERN: Illuminating Hidden Mathematical Knowledge in Language Models
**Authors:** Pavel Tikhonov, Elena Tutubalina, Ivan Oseledets, Dmitry I. Ignatov, Mikhail Seleznyov
**arXiv:** [arxiv.org/abs/2609.32264](https://arxiv.org/abs/2609.32264)
**Summary:** LANTERN trains a classifier over language-model activations to rank latent mathematical relationships, then subjects promising candidates to staged hypothesis generation, executable verification, and analytical checks. In under eight hours it screened 50 million OEIS sequence pairs, verified 62 previously unlinked relations, and surfaced four relationships the authors found in neither OEIS nor targeted literature searches.

---

### 14. Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training
**Authors:** Kunlun Zhu, Xuyan Ye, Yibo Li, Cheng Qian, Beibin Li, Heng Ji
**arXiv:** [arxiv.org/abs/2609.40111](https://arxiv.org/abs/2609.40111)
**Summary:** The Agent Error Dataset contains 50,228 error-diagnosis pairs from 9,961 tasks across 33 environments, preserving traces and execution metadata for failure analysis and recovery training. On 3,062 matched replays, first-proposal corrections raise verifier pass rates from 18.4% to 51.1%, while diagnosis fine-tuning improves exact-step agreement from 47.2% to 63.6%.

---

### 15. AIM: Agentic Idea Management for Automated Research
**Authors:** Hyeong Kyu Choi, Bhavana Dalvi Mishra, Jiefeng Chen, Mihir Parmar, Rui Meng, Chun-Liang Li, Xiangru Tang, Sharon Li, Jinsung Yoon, Tomas Pfister
**arXiv:** [arxiv.org/abs/2609.38445](https://arxiv.org/abs/2609.38445)
**Summary:** AIM treats automated research as idea-level search, using agentic surrogate and acquisition mechanisms to organize directions, a Solution Auditor to preserve idea-implementation alignment, and a Resource Planner to divide experimental budget. On ten AutoLab tasks it beats the strongest baseline by 1.6 points on system optimization and 4.9 points on long-horizon model and CUDA development, while matching the baseline's best performance up to 3.1 times faster.

---

### 16. Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation
**Authors:** Haibo Jin, Xinjie Li, Najmeh Sadoughi, Yang Liu, Yibo Wang, Zhu Liu, Yuzong Liu
**arXiv:** [arxiv.org/abs/2609.38660](https://arxiv.org/abs/2609.38660)
**Summary:** SMART builds persistent series-level memory and uses a dynamic router, mixture of agents, validation tools, and a judge-refiner loop to adapt subtitle translation workflows without retraining the underlying models. It earns the best MQM score in all 15 Subtitle Arena directions, cuts average penalty by 6.9% versus the strongest agent baseline, and leads both model and human evaluation on MuSC.

---

### 17. Unmask the State: When Does State Adaptation Matter for Masked Diffusion Language Models
**Authors:** Injin Kong, Sunghwan Choi, Yohan Jo
**arXiv:** [arxiv.org/abs/2609.33355](https://arxiv.org/abs/2609.33355)
**Summary:** This study organizes masked diffusion decoding choices into score, cardinality, region, commitment, and planning axes, then measures when a different action becomes better than a fixed strategy during generation. Lightweight detectors enable selective adaptation, capturing 56.9% of candidate-set oracle opportunity while changing only the top 10% of states for constrained JSON generation with LLaDA-8B.

---

### 18. It's Not What the Image Shows: Irrelevant Context Destabilises VLM Judges Without Informing Them
**Authors:** Nagham Omar, Mahmoud Jabarin, Kinan Ibraheem, Lotem Peled-Cohen
**arXiv:** [arxiv.org/abs/2609.37863](https://arxiv.org/abs/2609.37863)
**Summary:** MIST tests 13 vision-language judges on sentence labels that should ignore an accompanying aligned, misleading, or absent image. Images change roughly one in five labels regardless of what they depict and do not alter human agreement, showing that mere image presence destabilizes judge outputs without contributing relevant information.

---

### 19. Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies
**Authors:** Galbot Team, Xuchuan Chen, Xiaoqian Cheng, Yu Deng, Lihe Ding, Shaocong Dong, Xiangjun Gao, Haozhe Jia, Zekai Li, Zhoujian Li, Yunrui Lian, Sikai Liang, Chenghuai Lin, Dairu Liu, Jiahang Liu, Qingtao Liu, Yuxuan Ma, Zekun Qi, Jiayi Su, He Wang, Ruochen Xu, Tianyu Xu, Xudong Xu, Zhe Xu, Mi Yan, Siming Yan, Li Yi, Ruixi Yu, Jinlu Zhang, Yintianrun Zhang, Zhikai Zhang, Zhizheng Zhang, Yixin Zheng, Weiyi Zhu
**arXiv:** [arxiv.org/abs/2609.38537](https://arxiv.org/abs/2609.38537)
**Summary:** This evaluation probes GPT-6 Astra as an embodied policy across gripper and dexterous manipulation, mobile manipulation, navigation, locomotion, and humanoid control. Astra makes useful task-level decisions and reaches strong navigation results, but direct physical control remains unreliable and prohibitively slow, exposing a gap between reasoning quality and deployable robot action.

---

### 20. DyRAD: Radar Novel View Synthesis for Dynamic Driving Scenes
**Authors:** Merav Keidar, Tomer Borreda, Rajalakshmi Nandakumar, Or Litany
**arXiv:** [arxiv.org/abs/2609.39841](https://arxiv.org/abs/2609.39841)
**Summary:** DyRAD reconstructs dynamic driving scenes as static background reflectors plus tracked moving point reflectors, rendering full range-azimuth-Doppler tensors through an analytic radar point-spread function. The separation prevents sensor blur from becoming false geometry, supports zero-shot transfer across radar configurations, and recovers detections for 90.7% of reference-detected RADIal objects versus 26.9% for the strongest baseline.
