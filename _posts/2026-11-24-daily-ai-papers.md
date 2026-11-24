---
title: "Daily AI Papers — November 24, 2026"
date: 2026-11-24
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-24/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - embodied-ai
  - world-models
  - multimodal-agents
---

### 1. Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control
**Authors:** Yue Huang, Tianshan Zhang, Zeyu Zhang, Jayeon Kang, Akide Liu, Sungjoon Choi, Dacheng Tao, Hao Tang
**arXiv:** [arxiv.org/abs/2611.29897](https://arxiv.org/abs/2611.29897)
**Summary:** Motion Mamba 2.0 combines recurrent Mamba states, local attention, and persistent content memory to generate controllable humanoid motion over long horizons. The authors report rollouts up to 39.52 seconds, a 6.138-fold median paired inference speedup on an RTX 4090 with identical tested outputs, and real-world evaluation on the Unitree G1.

---

### 2. Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness
**Authors:** Xiao-Ming Wu, Kang Liao, Yuexiao Ma, Taolin Zhang, Mingqian Zhou, Nuo Chen, Ziming Li, Yihang Luo, Rui Li, Zhonghua Wu, Tianyu Xie, Xiawu Zheng, Zhongang Cai, Zhi Hou, Chen Change Loy
**arXiv:** [arxiv.org/abs/2611.31201](https://arxiv.org/abs/2611.31201)
**Summary:** Embo-Harness systematically studies prompting, planning, action execution, and tool use when frontier multimodal models serve directly as closed-loop robot policies. Its resulting recipe reaches 83.3% success on RoboLab-120 and succeeds in 15 of 20 zero-shot real-world trials, with interventions identifying accurate spatial target estimation as especially important.

---

### 3. WorldLeague: Benchmarking Physical Agency
**Authors:** Xinyang Zhou, Qi Li, Xinchao Wang
**arXiv:** [arxiv.org/abs/2611.30989](https://arxiv.org/abs/2611.30989)
**Summary:** WorldLeague evaluates physical agency across 60 simulated robot tasks and six capability dimensions, accommodating vision-language, vision-language-action, and world-action models through their respective controls. Across 13 systems, the strongest achieves 13 of the 60 goals, while correctly answered final questions still accompany zero physical progress in 71.8% of the evaluated VLM episodes.

---

### 4. 3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets
**Authors:** Bohan Zeng, Kaixin Zhu, Yifan Yang, Dongge Yu, Zihao Wu, Yifan Dai, Zhou Liu, Junbo Niu, Xiaochen Ma, Shiran Ge, Zimo Meng, Junzhu Liang, Huanyao Zhang, Jinhang Liu, Tianqi Xiao, Jinhao Zhang, Tianyi Bai, Zhixiong Zeng, Penghao Zhao, Yuanbo Peng, Key Zhang, Wentao Zhang
**arXiv:** [arxiv.org/abs/2611.30013](https://arxiv.org/abs/2611.30013)
**Summary:** DivDynBench tests rigging and instruction-controlled motion generation across six morphology categories, including coordinated multi-phase movements and explicit timing or trajectory constraints. The proposed agentic framework writes compact skeleton and motion programs for a deterministic executor, improving rigging reliability and motion accuracy while reducing generation overhead.

---

### 5. WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce
**Authors:** Binhui Xie, Jinmin Li, Haomiao Tang, Guangting Wang, Song Jin, Jianwei Zhu, Fengyun Rao, Jing Lyu
**arXiv:** [arxiv.org/abs/2611.30662](https://arxiv.org/abs/2611.30662)
**Summary:** WeMM-Ecom is a five-size family of multimodal models trained through domain-focused continued pretraining and hybrid-thinking post-training with on-policy distillation and reinforcement learning. The authors evaluate 28 e-commerce and 64 public general-purpose benchmarks, report advantages over relevant comparison models, and release weights and code for domain-specialized multimodal research.

---

### 6. Let the Fixer Decide: Training a Code Localizer from the Fixer's Likelihood
**Authors:** Khalil Hennara, Muhammad Hreden, Zeina Aldallal, Sara Chrouf, Safwan AlModhayan
**arXiv:** [arxiv.org/abs/2611.12164](https://arxiv.org/abs/2611.12164)
**Summary:** Fixer-Guided Localization trains a code localizer using a frozen fixer's likelihood of verified patches rather than reference edit locations, applying weighted supervised fine-tuning without tests or reinforcement learning during that training. The authors report comparable bug-localization utility with 27.5% less code and a single small agent solving up to 11 of 78 tasks compared with eight for the base model.

---

### 7. A Glimpse of Training VLMs as Foundation Models for Robotic Manipulation
**Authors:** Meng-Hao Guo, Yi Zhang, Zhe-Han Mo, Han-Zheng Wang, Jia-Jun Wang, Xin-Sheng Chen, Jiaxi Song, Yi-Xuan Deng, Jia-Ning Li, Xuanyu Chu, Hengrui Zhang, Huan-ang Gao, Yongming Rao, Shi-Min Hu
**arXiv:** [arxiv.org/abs/2611.29338](https://arxiv.org/abs/2611.29338)
**Summary:** nanoAstra combines semantic action primitives with capability-preserving supervised fine-tuning to adapt vision-language models for robotic manipulation using more than 5,000 hours of robot data and general visual-question-answering data. The 9B model reaches 17.8% zero-shot success on randomized RoboTwin 2.0 and uses overlapping inference and execution on one H20 GPU to reduce robot idle time from 35.0% to 6.9%.

---

### 8. ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step
**Authors:** Kaiwen Zhang, Yiming Gao, Zeqi Xiao, Xintao Wang, Pengfei Wan, Kun Gai, Xingang Pan
**arXiv:** [arxiv.org/abs/2611.26389](https://arxiv.org/abs/2611.26389)
**Summary:** ViDecide trains video diffusion models as causal sequences of state-transition decisions with explicit stopping, while Corrective Fine-tuning maps failed-decision noise to successful continuations without policy-gradient optimization. Across games, planning tasks, and multi-step robot planning, the authors report 83.8% average strict success compared with 23.3% for standard fine-tuning and 67.8% for the strongest prior method.

---

### 9. AutoPILOT: A Visual Agent Harness for Real-Time Gameplay
**Authors:** Mark Zhao, Pengcheng Wang, Rui Yang, Jiarui Yao, Xirui Jiang, Yuxi Chen, Bingxuan Li, Hanyang Chen, Ke Yang, Manling Li, Tong Zhang, Huan Zhang
**arXiv:** [arxiv.org/abs/2611.28202](https://arxiv.org/abs/2611.28202)
**Summary:** AutoPILOT lets a visual gameplay agent issue primitive actions, open-loop macros, or closed-loop screen-based controllers that continue acting between model calls. On the 120-game AFK-Bench, it reaches 68.6% real-time success against 38.3% for VISTA under matched budgets, and reaches VISTA's final success rate at one-fifth of its API cost.

---

### 10. Plan4D: Generative Plannable 4D Worlds
**Authors:** Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
**arXiv:** [arxiv.org/abs/2611.26516](https://arxiv.org/abs/2611.26516)
**Summary:** Plan4D predicts future RGB video together with depth, camera parameters, point clouds, and scene flow from scene context and text-specified actions. By stitching Depth Anything 3 to LongCat-Video and adding a scene-flow head, the authors report improved visual fidelity and geometric accuracy across synthetic and real-world generative 4D evaluations.

---

### 11. World Models as Native Latent Action Models
**Authors:** Qinyue Li, Weijie Qiao, Qingyi Tao, Zerui Gong, Zhe Yang, Quanzhou Li, Taolin Zhang, Jinglin He, Zhonghua Wu, Chen Change Loy
**arXiv:** [arxiv.org/abs/2611.30898](https://arxiv.org/abs/2611.30898)
**Summary:** Native LAM uses one pretrained video diffusion transformer as both inverse- and forward-dynamics models, with compact learnable registers extracting latent actions from counterfactual temporal pairs. The accompanying PAWlicy robot-policy pretraining method reaches 93.6% average RoboTwin 2.0 success with a 3.8B model trained on domain-randomized demonstrations and improves over the reported real-robot baseline on both tested tasks.

---

### 12. Composable Soft-Prompt Distillation of RL Experts: Toward Continual Post-Training
**Authors:** Zhen Zhang, Changyi Yang, Xuehai He, Chengzhi Liu, Yutong Yin, Ziyue Liu, Zhuoran Yin, Yangmin Li, Zhihan Liu, Jisen Li, Mingyu Jin, Chuhan Li, Zhaotian Weng, Ruoyu He, Wenyao Gao, Jiaxin Deng, Chenwei Wu, Hui Shen, Wenhao Chai, Chenyang Zhao, Zhuofan Ying, Kieran Liu, Andrew Chen, Pony Ma, Zhaoran Wang, Alkesh Patel, Zhe Gan, Xin Eric Wang
**arXiv:** [arxiv.org/abs/2611.27376](https://arxiv.org/abs/2611.27376)
**Summary:** Composable Soft-Prompt Distillation freezes a pre-RL backbone, distills each RL expert into an independent soft prompt, and combines experts by concatenating prompts without joint training. It recovers at least 90% of teacher gains in 22 of 23 settings, matches multi-teacher on-policy distillation in the evaluated composition, and keeps throughput within 1.5% of the unadapted backbone.

---

### 13. RUIBench: What Makes a Good Robot-Use Interface?
**Authors:** Yanzhe Chen, Zhijun Cao, Zechen Bai, Wenzheng Zeng, Kevin Yuchen Ma, Yiqi Lin, Guoqiang Liang, Xiaokang Liu, Ke Sun, Kevin Qinghong Lin, Mike Zheng Shou
**arXiv:** [arxiv.org/abs/2611.31115](https://arxiv.org/abs/2611.31115)
**Summary:** RUIBench evaluates 30 robot manipulation tasks, while RUIKit compares 13 robot-use interfaces under shared perception and control. Changing only the interface shifts success from 45% to 81% for a frontier agent and from 13% to 47% for a fine-tuned 4B model, while exposing a gap between agents' success declarations and observable task completion.

---

### 14. ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild
**Authors:** Yuxi Wang, Yufei Liu, Chengkai Jin, Qingyue Chen, Wenqi Ouyang, Tianyi Wei, Kerui Ren, Siyuan Huang, Zhiqi Shen, Hongsheng Li, Xingang Pan
**arXiv:** [arxiv.org/abs/2611.30597](https://arxiv.org/abs/2611.30597)
**Summary:** ViDiHand2 combines video diffusion priors with fine-grained geometric lifting, clip-level ray fitting, and confidence-gated fusion to reconstruct metric 3D hand motion from unconstrained videos. Across seven datasets and 18 baselines, the authors report 42% lower in-the-wild absolute joint error and 8.82-fold fewer detection failures than the best respective baselines, while running at 57 frames per second.

---

### 15. Distilling Visual Agents from Limited Interaction Experience
**Authors:** Siyu Zhou, Jing Jiang, Chengqi Zhang, Guodong Long
**arXiv:** [arxiv.org/abs/2611.28618](https://arxiv.org/abs/2611.28618)
**Summary:** This work distills visual agents from a small set of representative trajectories selected by skill-context coverage and ordered visual-decision similarity. Four fixed trajectories raise a 4B student's success from 49.17% to 82.08% on standard Navigation and from 60.16% to 85.55% on Sokoban, recovering over 90% of the measured gap to a 27B teacher on those panels.

---

### 16. DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings
**Authors:** Ben Kang, Junda Wang, Yuxuan Yuan, Hang Li, Yuhan Liu, Xin Chen, Wanting Geng, Tong Lin, Pei Fu, Dong Wang, Jian Luan, Huchuan Lu
**arXiv:** [arxiv.org/abs/2611.25419](https://arxiv.org/abs/2611.25419)
**Summary:** DiLE learns compact multimodal embeddings using task-guided latent queries, shared-private expert adaptation, and on-policy hard-negative distillation from a teacher's relevance judgments. The authors report state-of-the-art performance on MMEB-v2, UVRB, and MRMR across four configurations spanning two backbone generations.

---

### 17. Open Vision Banana: An Open Framework for Unified Visual Perception through Generation in RGB Space
**Authors:** Xu Lin, Ruilin Yao, Haoran Xu, Zixiang Wang, Ming Ma, Yu Zhao, Pu Miao, Chonghan Liu
**arXiv:** [arxiv.org/abs/2611.28489](https://arxiv.org/abs/2611.28489)
**Summary:** Open Vision Banana adapts a 7B Qwen image diffusion generator into one RGB-output perception model for depth and multiple segmentation tasks using a shared low-rank adapter and public data. Its controlled evaluations reveal unstable absolute depth scale, competition between depth and segmentation, and validation-loss reductions that do not reliably select better perception checkpoints.

---

### 18. Polytropos: What Do Vision-Language Model Descriptions Make of a Cultural Object?
**Authors:** Yuechen Jiang, Enze Zhang, Yuyan Wang, Mohsinul Kabir, Chenying Lin, Sijia Li, Qianqian Xie, Stavroula Golfomitsou, Konstantinos Arvanitis, Sophia Ananiadou
**arXiv:** [arxiv.org/abs/2611.29355](https://arxiv.org/abs/2611.29355)
**Summary:** Polytropos measures what vision-language descriptions preserve about individual cultural objects by reconstructing images from the descriptions and comparing them with original photographs. On 374 museum objects, 1,870 model descriptions, and 230 curator descriptions, reconstructions more often convey a recognizable recorded culture but are identified as the specific object in only 0.49% of cases.

---

### 19. UUBench: Understanding the Unspoken toward Full-Duplex Multimodal Interaction
**Authors:** Ye Pan, Chenfei Liao, Bin Ren, Hanqian Li, Haocong He, Jialei Chen, Jinlin He, Kunyu Peng, Mengyu Jin, Shijie Li, Wenqian Cui, Yuanqi Yao, Yuqian Fu, Kailong Ruan, Yuan Gao, Wei Wang, Xuming Hu, Irwin King, Nicu Sebe, Xu Zheng
**arXiv:** [arxiv.org/abs/2611.30157](https://arxiv.org/abs/2611.30157)
**Summary:** UUBench evaluates whether full-duplex multimodal systems infer implicit communicative needs from prosody, facial expressions, gestures, and context and respond appropriately. Its process-oriented and outcome-oriented scoring, supported by timestamped audiovisual evidence, separates intent fulfillment from the naturalness and appropriateness of the generated reply.

---

### 20. DexDuet: Learning Contact-Preserving Bimanual Dexterity from Human Demonstrations
**Authors:** Haoran Zhang, Haokai Ding, Han Zhou, Zuxing Lu, Heng Zhang, Xingxing Zuo
**arXiv:** [arxiv.org/abs/2611.30495](https://arxiv.org/abs/2611.30495)
**Summary:** DexDuet learns bimanual robot dexterity from one human demonstration using contact-preserving rewards, weight-sharing per-hand policies, and an adaptive assisted reference-state curriculum. Across four benchmarks, three simulators, and five robot embodiments, it improves object-tracking ADD-AUC by 11 to 41 points and preserves human contacts better in 117 of 122 paired runs with comparable tracking accuracy.
