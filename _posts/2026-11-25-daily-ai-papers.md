---
title: "Daily AI Papers — November 25, 2026"
date: 2026-11-25
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-25/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal-agents
  - embodied-ai
  - reinforcement-learning
---

### 1. Antom 3-in-1 Transformer: A Payment Foundation Model
**Authors:** Weiyu Han, Haoyu Jiang, Jie Sheng, Youxi Pan, Xianglong Liu, Zeqi Ren, Dongquan Yi, Yinhao Liu, Ruobing Zuo, Ze Zhao, Huilin He, Nairong Zhang, Xinyi He, Xiao Tan, Jun Wang, Pan Fang, Wei Zeng, Jianan Su, Kaixin Shen, Jingtong Wu, Hao Li, Shuai Chen, Jiangming Yang, Tianyi Zhang
**arXiv:** [arxiv.org/abs/2611.25403](https://arxiv.org/abs/2611.25403)
**Summary:** Antom 3-in-1 Transformer combines sequence, tabular, and graph representations in a roughly 7B-parameter payment-risk model with about 1.7B parameters activated per task route. The authors report a 34.5% improvement in a cross-business transfer metric and a 37.88% reduction in overall loss rate relative to XGB-Online during a four-month online experiment.

---

### 2. Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe
**Authors:** Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang, Soujanya Poria
**arXiv:** [arxiv.org/abs/2611.32884](https://arxiv.org/abs/2611.32884)
**Summary:** Reinforcement Learning with Verifiable Beliefs rewards agents for gathering more evidence when a simulator's exact posterior remains ambiguous and for answering once the evidence is sufficient, without a judge or reward model. Across three vision-language models and three benchmarks, including two unseen during training, the authors report a 17.1% average improvement over the base models and a 9.3% advantage over judge-based process-reward PPO with fewer GPU-hours.

---

### 3. Rewirable Circuits in Transformers with Loom Attention
**Authors:** Da Xiao, Qingye Meng, Shengping Li, Xingyuan Yuan
**arXiv:** [arxiv.org/abs/2611.30634](https://arxiv.org/abs/2611.30634)
**Summary:** Loom attention lets Transformer heads dynamically attend to earlier head outputs as well as tokens, using a matrix-memory stream alongside the conventional vector residual stream. Across model sizes and training budgets, the authors report that LoomFormer matches conventional Transformers trained with over three times the compute and that LoomPythia-2.8B matches or surpasses Pythia-12B on the reported downstream settings.

---

### 4. Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents
**Authors:** Jiaqi Su, Jie-Jing Shao, Yichen Liu, Long-Kai Huang, Haiyan Yin
**arXiv:** [arxiv.org/abs/2611.28947](https://arxiv.org/abs/2611.28947)
**Summary:** NightWatch adds continuous interface monitoring to computer-use agents through a lightweight 0.8B-parameter watcher, without changing the main agent's model, prompt, or action space. The authors report 33% less non-reasoning wall-clock time and 53% less wasted time on OSWorld with comparable success, plus an increase from 39.5% to 44.2% success on DynaCU-Bench.

---

### 5. Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation
**Authors:** Guo Chen, Fuxiao Liu, Haoqin Tu, Yiyang Zhou, Andrew Tao, Bryan Catanzaro, Cihang Xie, Yuyin Zhou, Huaxiu Yao, Didong Lu, Zongxia Li, Guilin Liu
**arXiv:** [arxiv.org/abs/2611.31358](https://arxiv.org/abs/2611.31358)
**Summary:** Nemotron-Labs-VisualCreation unifies learned raster tokens and explicit programs through a shared generation, rendering, and visual-feedback interface for images, vector graphics, webpages, and documents. Its tokenizer improves reconstruction PSNR from 26.08 to 29.57 dB in the reported evaluation, while the agentic harness raises GenEval2 Soft-TIFA GM from 31.71 to 52.56 using the same raster generator.

---

### 6. ACAP: Asynchronous Coding Agents for Efficient Robot Control
**Authors:** Zexin He, Rui Li, Yushi Lan, Chengkai Jin, Zhi Hou, Xingang Pan
**arXiv:** [arxiv.org/abs/2611.31205](https://arxiv.org/abs/2611.31205)
**Summary:** ACAP organizes a robot into persistent coding agents for configurable control groups, with a coordinating hyper-agent managing dependencies and dynamically assigning control. Across 72 real-world rollouts covering 25 task/platform settings, the authors report a 28.2% reduction in task-balanced time cost compared with a single-agent Direct Policy and release a rollout dataset.

---

### 7. Self-Evolving Evaluation Environments for Computer-Use Agents
**Authors:** Wenhao Wang, Panrong Tong, Quyu Kong, Pengxiang Li, Haowen Yang, chenglin Cai, Siheng Chen, Yue Wang
**arXiv:** [arxiv.org/abs/2611.30962](https://arxiv.org/abs/2611.30962)
**Summary:** CUA-SEE evolves computer-use evaluation tasks and executable verifiers in a closed loop using evidence from agent rollouts. Across agents, applications, and rounds, it expands benchmark difficulty and coverage, probes agent-specific capability boundaries, and preserves process-level evidence through state-grounded checkpoints and adversarial verifier validation.

---

### 8. S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence
**Authors:** Muxin Fu, Peike Yu, Guibin Zhang, Wenrui Zhou, Runze Liu, Lang Feng, Fuchao Yang, Feng Chen, Yixuan Li, Mengao Zhang, Shiying Zhang, Wen Shen, Ling Pan, Shuicheng Yan, Bo An
**arXiv:** [arxiv.org/abs/2611.28649](https://arxiv.org/abs/2611.28649)
**Summary:** S-Mind trains compact spatial tokens to fuse multiple visual views into a coherent 3D scene and transform that representation as reasoning adopts new viewpoints. Across four spatial benchmarks, the authors report gains of up to 22.26 points over Qwen3.5 backbones, improved fusion and transformation probe accuracy, and roughly 100-fold faster inference than a same-backbone tool agent.

---

### 9. LingSante MedGuard Technical Report
**Authors:** LingSante MedGuard Team
**arXiv:** [arxiv.org/abs/2611.25509](https://arxiv.org/abs/2611.25509)
**Summary:** LingSante MedGuard combines a medical guardrail teacher and six capability experts through supervised fine-tuning followed by multi-teacher on-policy distillation. On the authors' 11-subset MedGuardBench, its 4B, 9B, and 27B models achieve mean risk-detection F1 scores of 82.3%, 82.4%, and 87.4%, with additional evaluations of retrieval-supported hallucination detection and verification components.

---

### 10. PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement
**Authors:** Yang Cao, Zhe Zhu, Yiheng Zhang, Zhengqiang Zhang, Haoyuan Li, Le Wan, Dan Xu
**arXiv:** [arxiv.org/abs/2611.32554](https://arxiv.org/abs/2611.32554)
**Summary:** PartAgent is a training-free framework that combines spatial proposals from 3D experts with multiview semantic evidence from 2D experts, then verifies and refines its part partitions through closed-loop actions. The authors report 68.41 mIoU on PartObjaverse-Tiny-WT and an average of 69.36 across four additional datasets, outperforming the strongest reported comparison means by 8.53 and 7.28 points respectively.

---

### 11. Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies
**Authors:** Xuanchen Liu, Hejun Zhang, Boxuan Dong, Ying Wu, Heshuai Li, Wen Gao, Yonghong Tian, Weihao Yu
**arXiv:** [arxiv.org/abs/2611.33010](https://arxiv.org/abs/2611.33010)
**Summary:** RoboDojo-Mirror compares robot manipulation policies in mirror-free scenes and three reflective conditions while preserving task objectives and policy checkpoints. Across five policies, the authors report average success drops of 10.8 to 56.7 percentage points, analyses showing that direct panel collisions alone do not explain the failures, and lower success in real-robot mirror experiments.

---

### 12. Interpretable Prototype-Conditioned Adaptation for Weather Forecasting
**Authors:** Zhixuan Li, Hao Jiang, Chen Hui, Kai Geng, Weisi Lin
**arXiv:** [arxiv.org/abs/2611.25848](https://arxiv.org/abs/2611.25848)
**Summary:** ProtoCast uses group-specific prototype banks and sparse mixtures of prototype-conditioned low-rank operators to adapt weather forecasts to local temporal evolution and cross-variable dependencies. Experiments on GlobalForecast and TyphoonTracking show improved forecasting accuracy, while prototype-deletion analysis links explicit local correction contributions to changes in prediction error.

---

### 13. ThinkMorph-SSL: Scaling Interleaved Multimodal Reasoning with Pretext Tasks
**Authors:** Jiawei Gu, Linjie Li, Yiming Liu, Yunzhuo Hao, Huichen Wang, Guanzheng Chen, Zhichao Peng, Luxin Xu, Xinyu Zhang, Li Luo, Disen Lan, Zican Hu, Mingyang Song, David Valente, Alex Jinpeng Wang, Yafu Li, Ganqu Cui, Zhengyuan Yang, Qizhe Xie, Yejin Choi, Ranjay Krishna, Yu Cheng
**arXiv:** [arxiv.org/abs/2611.32183](https://arxiv.org/abs/2611.32183)
**Summary:** ThinkMorph-SSL first turns visual pretext tasks such as colorization and denoising into instruction-free interleaved reasoning traces, then trains on automatically constructed question-driven demonstrations. At a matched instruction-tuning budget, pretext reasoning outperforms instruction tuning alone, and the full recipe improves the base model by an average of 11.33 accuracy points across twelve benchmarks.

---

### 14. ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds
**Authors:** Qingle Liu, Jieming Li, Pei-lin Li, Shenghan Zheng, Ruize Yang, Sunqi Fan, Deyao Hong, Huan-ang Gao, Meng-Hao Guo, Shuojin Yang
**arXiv:** [arxiv.org/abs/2611.32649](https://arxiv.org/abs/2611.32649)
**Summary:** ICLWorld evaluates inference-time rule learning across computer-use and robot-use agents using 30 environments, 630 demonstration videos, and 160 customized tasks with three rule versions each. The strongest evaluated agents reach 82% and 76% computer-use success but only 27% and 26% robot-use success, exposing gaps between understanding contextual rules and acting on them.

---

### 15. KMed-31B Technical Report
**Authors:** KMed Team
**arXiv:** [arxiv.org/abs/2611.28719](https://arxiv.org/abs/2611.28719)
**Summary:** KMed-31B trains medical-task specialists with feedback-appropriate rewards and combines them through Multi-teacher On-policy Delta Distillation for on-premises deployment. Relative to its base model, the authors report HealthBench Hard improvements from 22.95 to 41.87 in non-thinking mode and from 23.80 to 51.48 in thinking mode, while maintaining or slightly improving four multiple-choice medical benchmarks.

---

### 16. Qwen-Image-HD: Autoregressive Diffusion for High Definition Image Generation
**Authors:** Zihao Liu, Zekai Zhang, Shengming Yin, Zikai Zhou, Donghao Zhou, Chenyang Zhu, Lihan Jiang, Ningyuan Tang, Bingxuan Zhao, Yanran Zhang, Yan Shu, Zhening Liu, Jiahao Li, Jie Zhang, Kaiyuan Gao, Kun Yan, Qihang Ai, Rui Song, Shuo Cao, Xiao Xu, Xiaoyue Chen, Yuxiang Chen, Zhendong Wang, Zhouyang Li, Bo Zheng, Jun Zhou, Xiu Li, Chenfei Wu
**arXiv:** [arxiv.org/abs/2611.32736](https://arxiv.org/abs/2611.32736)
**Summary:** Qwen-Image-HD adapts Qwen-Image 2.0 to high-resolution generation through local 1K-tile training and blockwise autoregressive diffusion conditioned on neighboring tiles and a historical thumbnail. The authors report better 4K quality, lower training compute, and higher inference efficiency than full-image fine-tuning of the same backbone, and introduce a multi-GPU wavefront schedule to reduce image latency.

---

### 17. PhyCoVE: Benchmarking Physical Counterfactual Video Editing across Diverse Material Dynamics
**Authors:** Conghan Yue, Yuanjie Chen, Yunyan Xiao, Zeyu Peng, Xingsong Ye, Ya Gao, Yanglin Huang, WeiYao Zhang, Yue Han, Zhineng Chen, Yu-Gang Jiang
**arXiv:** [arxiv.org/abs/2611.29184](https://arxiv.org/abs/2611.29184)
**Summary:** PhyCoVE provides 533 physical counterfactual editing cases from 110 videos, covering rigid, elastic, and fluid dynamics plus a fidelity metric for the resulting physical changes. Evaluation of seven video-editing models finds that even the best reproduces only about one seventh of the physical change, highlighting the gap between appearance editing and correct scene dynamics.

---

### 18. CoT-Proxy: Cross-Format Transfer for Distilling Long-Horizon Policies
**Authors:** Dawid J. Kopiczko, Tijmen Blankevoort, Yuki M. Asano
**arXiv:** [arxiv.org/abs/2611.33148](https://arxiv.org/abs/2611.33148)
**Summary:** CoT-Proxy distills long-horizon policies from teacher actions without requiring hidden chain-of-thought, using empty student reasoning blocks and a replay-buffer KL loss to limit drift. The authors report that visible outputs and API reasoning summaries from GPT-5.6 Luna raise Qwen3-4B success from 7% to 48% on AppWorld and from 3% to 28% on SWE-bench Verified.

---

### 19. Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching
**Authors:** Yihong Luo
**arXiv:** [arxiv.org/abs/2611.30986](https://arxiv.org/abs/2611.30986)
**Summary:** Instantaneous Trajectory Distribution Matching addresses baseline-induced gradient drift in forward-diffusion reinforcement learning by anchoring updates at the behavior velocity tracked by an auxiliary denoiser. Across online and offline alignment evaluations, the authors report stronger performance and nearly threefold faster convergence on GenEval2, reaching 0.87 without collapse and scaling to the 5.6B FLUX.3 model.

---

### 20. LeadVLA: Learning Follower-Aware Route Execution for Robot Leading
**Authors:** Tianle Zeng, Hanjing Ye, Bingyi Xia, Yuchen Zhou, Zibo Zhang, Yufei Huang, Yonggen Ling, Hong Zhang
**arXiv:** [arxiv.org/abs/2611.30149](https://arxiv.org/abs/2611.30149)
**Summary:** LeadVLA separates a robot-leading policy into an explicit route Path, a learned progress Pace, and a follower- and scene-conditioned Residual for local adaptation. With an approximately four-million-sample training corpus and 108 held-out LeadBench episodes, it achieves the highest evaluated success rate of 39.6% and transfers to unseen real-world environments without real-world policy fine-tuning.
