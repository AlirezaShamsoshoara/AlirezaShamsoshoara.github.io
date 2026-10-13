---
title: "Daily AI Papers — October 13, 2026"
date: 2026-10-13
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-13/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - visual-grounding
  - ai-agents
  - reinforcement-learning
---

### 1. GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives
**Authors:** Yu, Qize, Fan, Lianrui, Chen, Boyu, Liang, Jiaqi, Ding, Xini, Chen, Yue, Song, Zetian, Wang, Yuran, Zou, Yi, Wang, Kaixuan, Chen, Tianxing, Song, Wenxuan, Zhou, Bohan, Li, Mingleyang, Huang, Siqiao, Ye, Yuqi, Jiang, Caigao, Wei, Wei, Wu, Ruihai, Zhang, Hang, Ge, Yixiao, Zhou, Shuchang, Liu, Shilong, Liu, Xianming, Luo, Ping, Huang, Shiyu
**arXiv:** [arxiv.org/abs/2609.39601](https://arxiv.org/abs/2609.39601)
**Summary:** GroundingPI is a 4B grounding foundation model that emits points and boxes as quantized coordinates after multimodal and spatial pretraining, supervised fine-tuning, and GRPO. It sets a 73.68% average across 34 grounding benchmarks and improves downstream robotic manipulation and autonomous-driving results, including out-of-distribution gains of up to 24.8% on RoboTwin 2.0.

---

### 2. Thinking Inertia: LLMs Keep Thinking When Told Not To
**Authors:** Lei, Dianqiao, Lin, Kevin Qinghong, Lu, Pan, Torr, Philip, Zou, James
**arXiv:** [arxiv.org/abs/2610.11765](https://arxiv.org/abs/2610.11765)
**Summary:** This study introduces metrics that distinguish answer-only output, relevant but non-inferential text, and visible explicit inference when language models are instructed not to think. Across six models, tasks, and prompting interventions, explicit reasoning persists under strict controls and becomes more common as the answer space opens, a behavior the authors call Thinking Inertia.

---

### 3. AgentSWE: Can Coding Agents Build the Agent You Actually Want?
**Authors:** Wang, Jiahao, Qian, Hongjin, Hu, Yuyang, Zhang, Jiajun, Liu, Zheng
**arXiv:** [arxiv.org/abs/2610.13361](https://arxiv.org/abs/2610.13361)
**Summary:** AgentSWE benchmarks whether coding agents can create, edit, and optimize production agents that satisfy natural-language requirements on held-out acceptance cases. Tests across models and harnesses find a large gap between demonstrated and delivered behavior, with recurring failures from visible-case overfitting, hollow runtimes, and unsupported completion claims.

---

### 4. Scaling Agentic Data for Long-Horizon Terminal Intelligence
**Authors:** Zou, Shun, Ma, Ziyu, Zou, Yi, Wang, Yong, Chen, Lin, Chen, Zehui, Chen, Guanhua, Chu, Xiangxiang, Zhao, Feng
**arXiv:** [arxiv.org/abs/2610.13166](https://arxiv.org/abs/2610.13166)
**Summary:** TerminalHorizon is an automated synthesis engine that reconstructs long-horizon terminal tasks so agents must genuinely explore, implement, verify, and improve their work. Training Qwen3.5-27B on 1,500 synthesized environments yields gains across 12 coding, production-agent, and reasoning benchmarks, while 12-hour case studies show continued self-improvement beyond initial solutions.

---

### 5. VIS-Ground: Video Interactive Storytelling with Contextual Grounding
**Authors:** Li, Bingxuan, Song, Yiwen, Wu, Xueqing, Pan, Yanzhou, Li, Yang, Su, Kuang, Liu, Jingyun, Ko, Sebastian, Zhang, Huan, Zhang, Tong, Peng, Nanyun, Pfister, Tomas, Song, Yale
**arXiv:** [arxiv.org/abs/2610.09326](https://arxiv.org/abs/2610.09326)
**Summary:** VIS-Ground turns a video's source material, rendered history, and viewer request into executable constraints for interactive continuation. Across three video-generation backbones, its abstraction, constraint induction, planning, verification, revision, and rendering pipeline improves the strongest baseline's composite score by an average of 10.3 points.

---

### 6. GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed
**Authors:** Yu, Qize, Fan, Lianrui, Ping, Bowen, Ding, Xini, Song, Zetian, Niu, Junbo, Wang, Kaixuan, Chen, Tianxing, Chen, Yue, He, Minghua, Wang, Yuran, Huang, Jie, Zhang, Haojun, Chen, Min, Li, Hao, Song, Wenxuan, Wu, Ruihai, Liu, Xianming, Liu, Shilong, Zhou, Shuchang, Luo, Ping, Huang, Shiyu
**arXiv:** [arxiv.org/abs/2609.39600](https://arxiv.org/abs/2609.39600)
**Summary:** GroundAnything recasts visual grounding as parallel evidence extraction and uses bidirectional diffusion with blockwise denoising to jointly refine spatial predictions. Its 4B model reaches state-of-the-art grounding accuracy at its scale, while an optional self-speculative mode delivers a 4.51-times speedup over the autoregressive counterpart for only a 0.74-point COCO F1mIoU drop.

---

### 7. Multi-Stream Attention Residuals
**Authors:** Qin, Xiaohan, Zhang, Xiangdong, Dai, Tuo, Zou, Sunan, Wu, Huaijin, Yang, Yebin, Xia, Zhuo, Yao, Lin, Liu, Yuliang, Yan, Junchi
**arXiv:** [arxiv.org/abs/2610.13630](https://arxiv.org/abs/2610.13630)
**Summary:** Multi-Stream Attention Residuals extends depth-wise attention with multiple contextual streams produced by multi-scale causal convolutions and lightweight adaptive mixing. At 18B and 28B mixture-of-experts scales it beats standard residuals, Hyper-Connections, and Attention Residuals on all 12 benchmarks, with a 1.58-times iso-loss compute speedup over standard residuals.

---

### 8. Relevance Does Not Imply Applicability: Experience Activation for Personal GUI Agents
**Authors:** Zhang, Fuyao, Wang, Xuan, Li, Zherui, Zhang, Jiaming, Huang, Longtao, Lim, Wei Yang Bryan
**arXiv:** [arxiv.org/abs/2609.33304](https://arxiv.org/abs/2609.33304)
**Summary:** ExpActivator treats personalization for GUI agents as activating history only when it applies to the current screen or recurring situation, rather than appending all task-relevant experience. Across four GUI backbones it raises within-trajectory step success by 28% on average, uses about one-fifth as many history tokens, and more than doubles the strongest proactive baseline's Matthews correlation coefficient.

---

### 9. CrossTimeEdit: A Decade-Spanning Cross-View Dataset and Reward-Guided Editing for Historical Street-View Generation
**Authors:** Lu, Hanwen, He, Jun, Yang, Mingjia, Wei, Hao, Huang, Jinhao, Lin, Yi, Zhang, Xiang
**arXiv:** [arxiv.org/abs/2609.36616](https://arxiv.org/abs/2609.36616)
**Summary:** CrossTimeEdit uses recent street views for viewpoint and persistent content, plus temporal satellite differences as evidence, to reconstruct plausible historical street scenes. Trained on the 43,653-location VIGOR-his dataset with supervised learning and multi-reward online reinforcement learning, it improves the three editing criteria by 17.12% over its pretrained baseline.

---

### 10. SpatialASM: Internalizing Active Mentalization for Spatial Reasoning
**Authors:** Liu, Yuhong, Wu, Shenxi, Chi, Junyi, Zhang, Beichen, Dai, Xuanlang, Wang, Jiaqi, Zang, Yuhang, Lin, Dahua
**arXiv:** [arxiv.org/abs/2610.13832](https://arxiv.org/abs/2610.13832)
**Summary:** SpatialASM trains vision-language models to plan viewpoints and mentally reconstruct scenes using an allocentric novel-view generator, explicit active-mentalization trajectories, and perspective-taking tasks. The method improves four model backbones across seven spatial benchmarks while preserving their general visual capabilities, offering scalable supervision for cross-view reasoning.

---

### 11. PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic Reinforcement Learning
**Authors:** Li, Muyang, Yang, Jie, Fang, Zhengyu, Zhu, Junchao, Xiao, Zhengkun, Deng, Ruining, Jiang, Zhe, Chen, Shigang
**arXiv:** [arxiv.org/abs/2609.36642](https://arxiv.org/abs/2609.36642)
**Summary:** PR-OPD has an agent generate a hindsight skill, reread its response with that skill as a stop-gradient teacher, and align hidden representations at every layer alongside the reward objective. Without an external teacher or inference overhead, it improves over GRPO by up to 4.7 points on ALFWorld success and 14.0 points on WebShop accuracy.

---

### 12. Systematic Multi-Agent Vision-and-Language Navigation: Formulation, Benchmark, and Method
**Authors:** Xu, Yunzhe, Liu, Zhe
**arXiv:** [arxiv.org/abs/2609.35965](https://arxiv.org/abs/2609.35965)
**Summary:** MAVLN formalizes multi-agent vision-and-language navigation as coordination under dependency and resource constraints, with 11,724 episodes across 145 scenes for teams of up to four agents. Its TRISS baseline combines LLM scheduling, shared topological memory, and conflict-aware execution, revealing substantial remaining challenges in scheduling, planning, and coordinated navigation.

---

### 13. T3lescope: Arbitrary-Resolution High-Fidelity Generative Surface Reconstruction from Images
**Authors:** Noguchi, Atsuhiro, Xu, Tianhan, Liang, Yiming, Kikuchi, Yuta, Ishiyama, Masahiro, Takagi, Shintaro, Murai, Hitoshi, Matsumoto, Eiichi
**arXiv:** [arxiv.org/abs/2610.03308](https://arxiv.org/abs/2610.03308)
**Summary:** T3lescope reconstructs meshes from posed multi-view images through an inference-time coarse-to-fine cascade that shares one fixed-resolution generator across scene scales. It handles objects through city-scale environments without per-scene optimization, outperforming feed-forward and generative baselines while recovering fine, glossy, and transparent surfaces.

---

### 14. ARCS: Towards Precise Text-to-SQL via Structured Disambiguation
**Authors:** Hu, Yihao, Feng, Yanlin, Otani, Naoki, Bhutani, Nikita
**arXiv:** [arxiv.org/abs/2610.09396](https://arxiv.org/abs/2610.09396)
**Summary:** ARCS introduces structured disambiguation and a text-to-SQL corpus that fully annotates naturally occurring ambiguities, valid interpretations, and SQL queries over real databases. The benchmark exposes a major deployment gap: the strongest evaluated closed model reaches only 51% end-to-end execution accuracy and no open model exceeds 27%.

---

### 15. Learning More by Training Less: Uncertainty-Guided Progressive Contraction for Efficient Reasoning Post-Training
**Authors:** Yang, Suorong, Wang, Jiaxin, Su, Jiaming, Yue, Chentao, Shen, Furao, Ye, Peng, Poria, Soujanya
**arXiv:** [arxiv.org/abs/2610.12933](https://arxiv.org/abs/2610.12933)
**Summary:** This framework builds Monte Carlo reasoning trees around intermediate states to identify uncertain supervision, then progressively contracts both the teacher corpus and student optimization toward the most useful trajectories. Across model families and reasoning benchmarks, it maintains or improves performance with as little as 0.22% of the full-data supervised fine-tuning optimization budget.

---

### 16. Branching On-Policy Distillation
**Authors:** Chen, Dongyang, Liu, Shudong, Li, Shubo, Tang, Duoxun, Liang, Jinwei, Wu, Zehuan, Lu, Lewei
**arXiv:** [arxiv.org/abs/2610.13481](https://arxiv.org/abs/2610.13481)
**Summary:** BranchOPD selects uncertain or teacher-disagreed decision points, reuses shared prefixes, and distills teacher supervision into multiple student-policy continuations. It beats vanilla and seven-rollout on-policy distillation across the tested math and agent benchmarks while reducing generated-token costs by roughly 19% on ALFWorld and 31% on WebShop.

---

### 17. Initialization Improves LLM-Driven Discovery
**Authors:** Sakarvadia, Mansi, Ciccone, Marco, Raffel, Colin
**arXiv:** [arxiv.org/abs/2610.00707](https://arxiv.org/abs/2610.00707)
**Summary:** A study of 12 modular harnesses across five LLM-driven discovery tasks finds brittle results and frequent mode collapse as iterate diversity disappears. Initial parallel exploration reliably improves the starting population and subsequent iterative optimization, producing more consistent gains than state-of-the-art harnesses or later diversity interventions.

---

### 18. Evaluating LLM Creativity through Long-Tail Performance
**Authors:** Wang, Yichen, Huang, Tenghao, Padmakumar, Vishakh, Lee, Mina
**arXiv:** [arxiv.org/abs/2610.12998](https://arxiv.org/abs/2610.12998)
**Summary:** The authors formalize creativity as task quality in the long tail of a reference input-output distribution and test the idea across 15 benchmarks and 26 open-weight models. Higher-tail subsets align model rankings more closely with human creativity judgments, motivating q@Tail as a lower-cost diagnostic for measuring useful novelty.

---

### 19. Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality Gaps
**Authors:** Zhang, Jiaxin, Peng, Xiangyu, Chen, Qinglin, Li, Yu, Hayashi, Hiroaki, Wu, Chien-Sheng
**arXiv:** [arxiv.org/abs/2610.02740](https://arxiv.org/abs/2610.02740)
**Summary:** Prospective Hindsight augments retrospective reinforcement learning with surprise from the gap between an agent's pre-feedback prediction and post-feedback evaluation. Its stop-gradient, surprise-weighted advantage improves task performance and calibration across single-turn and multi-turn tasks, model scales, GRPO, on-policy distillation, and their combination.

---

### 20. Same Output, Different Gold: Measuring How Reference Choice Moves a Multilingual Benchmark Score
**Authors:** Kulshreshtha, Parth, Dalmia, Shivali, Mukherji, Abhishek
**arXiv:** [arxiv.org/abs/2610.03825](https://arxiv.org/abs/2610.03825)
**Summary:** Holding model outputs fixed while swapping among independently produced references moves multilingual benchmark scores by up to 7.55 F1 points in one language and can alter system comparisons. The analysis traces the sensitivity to an undocumented aggregation default and proposes reporting a reference-sensitivity band alongside benchmark scores.

---
