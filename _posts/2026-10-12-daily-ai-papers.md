---
title: "Daily AI Papers — October 12, 2026"
date: 2026-10-12
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-12/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - multimodal-models
  - ai-agents
---

### 1. DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models
**Authors:** Wan, Zhenglin, Chen, Jiayu, Zhang, Zhengfeiyang, Zhou, Pengfei, Zhao, Wangbo, Kong, Fangyuan, Wan, Pengfei, Gai, Kun, You, Yang
**arXiv:** [arxiv.org/abs/2610.12572](https://arxiv.org/abs/2610.12572)
**Summary:** DiffusionART aggregates each prompt's rewards into a shared reward-improving direction for reverse-process states, eliminating a hidden consistency force while using drift-adaptive restoration without EMA tuning. Across image and video generation it trains stably with fewer samples, and on HunyuanVideo-13B reaches competing late-stage reward levels with roughly 12 times fewer GPU hours.

---

### 2. S-Space: Exploring Spatial Workspace in Multimodal Language Models
**Authors:** Shi, Zhiyuan, Li, Xiang, Guo, Xingzhuo, Miao, Shangchen, Chen, Weiliang, Dai, Qiyu, Ren, Jinshan, Lyu, Jiangran, Liu, Fangfu, Long, Mingsheng, Wu, Jialong
**arXiv:** [arxiv.org/abs/2610.13527](https://arxiv.org/abs/2610.13527)
**Summary:** The authors identify S-Space, an intrinsic linear subspace in multimodal language models that encodes object coordinates along horizontal, vertical, and distance axes and changes under viewpoint transformations. Causal interventions and diagnostic readouts show that models can form useful spatial representations but remain bottlenecked by the transformations needed for reliable reasoning across viewpoints.

---

### 3. Reflex: Visually Grounded Reactive Humanoid Control
**Authors:** Jia, Taoyang, Huang, Weikai, Song, Linxin, Darlington, Jared, Zhao, Jieyu, Wang, Yue, Duan, Jiafei, Ren, Zhongzheng, Krishna, Ranjay
**arXiv:** [arxiv.org/abs/2610.12772](https://arxiv.org/abs/2610.12772)
**Summary:** Reflex decomposes visually grounded humanoid catching into state-based whole-body control, inference of moving-object dynamics from partial observations, and an egocentric RGB-D encoder that recovers the same compact dynamics representation. It reaches 85.7% catch success in simulation and enables a real Unitree G1 to catch human-thrown boxes at distances of 2.5 and 5 meters.

---

### 4. SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments
**Authors:** Jin, Tian, Wang, Wenhao, Kang, Jing, Shi, Haoting, Ye, Rui, Lu, Yijun, Chen, Siheng
**arXiv:** [arxiv.org/abs/2610.12611](https://arxiv.org/abs/2610.12611)
**Summary:** SoftwareGym automatically synthesizes diverse runnable GUI applications, then evaluates and iteratively repairs them to create reliable computer-use-agent training environments. Its 182 applications average a 91.5% GUI task pass rate, and training on collected trajectories raises out-of-domain OSWorld Pass@3 from 41.39% to 56.97%.

---

### 5. EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents
**Authors:** Huang, Jie, Chen, Yanan, Liu, Ruixun, He, Kaichen, He, Xinyi, Huang, Rui, Zheng, Zilong, Zhang, Zhenliang, Zhong, Yiwu
**arXiv:** [arxiv.org/abs/2610.13021](https://arxiv.org/abs/2610.13021)
**Summary:** EmbodiedCLBench evaluates whether self-evolving embodied agents can learn basic tasks continually and recombine those skills to solve complex unseen tasks in simulation. Experiments show that prior experience consistently helps, but current agents fail to extract proportional value from additional learning samples as task complexity grows.

---

### 6. VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs
**Authors:** Feng, Yuan, Yang, Qize, Chen, Ruizhe, Song, Sibo, He, Haolin, Zhu, Muzhi, Liu, Zihan, Chu, Yunfei, Cheng, Xize, Wang, Yuxuan, Xu, Jin, Xie, Xike
**arXiv:** [arxiv.org/abs/2610.07987](https://arxiv.org/abs/2610.07987)
**Summary:** VisionWeave learns end to end where to allocate coarse or fine visual tokens using a gated spatial pooler and content-adaptive granularity router within a shared coordinate system. On Qwen3.8-27B it saves 43.0% of visual tokens while retaining 98.9% of native performance, delivering 2.3 times higher serving throughput with lower latency.

---

### 7. Hear the World in Stereo: Learning Dynamic Spatial Correspondence for Immersive Joint Video-Audio Generation
**Authors:** Chen, Hanmo, Liu, Chengcheng, Chen, Tianxiao, Zhang, Zheyu, Zheng, Siming, Chen, Jinwei, Yang, Xu, Deng, Cheng, Li, Bo, Jiang, Peng-tao
**arXiv:** [arxiv.org/abs/2609.38748](https://arxiv.org/abs/2609.38748)
**Summary:** StereoBind connects visual source motion to stereo sound generation through visual motion binding, an absolute-position track encoder, and relative-motion modeling. Using the new StereoWorld-29K dataset and StereoWorldBench, it substantially improves dynamic audiovisual spatial alignment while preserving overall generation quality.

---

### 8. ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents
**Authors:** Yang, Chengyi, Bao, Renxu, Hou, Jue, Teng, Zongpei, Wang, Ziheng, Lin, Yujie, Huang, Chengsong, Zhu, Junnan, Qiu, Delai, Wang, Yining, Liu, Shengping, Long, Fei, Su, Jinsong
**arXiv:** [arxiv.org/abs/2610.13395](https://arxiv.org/abs/2610.13395)
**Summary:** ProgramGym builds verifiable training environments from repositories and pairs them with a role-isolated agent workflow for long-horizon program reproduction across C, C++, Go, and Rust. Its 1,648 environments improve a Qwen3.8-27B model from 34.87% to 42.84% on ProgramBench, while the full agent workflow lifts performance above 55%.

---

### 9. Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition
**Authors:** Yang, Kaisen, Liu, Qingle, Wang, Kejin, Zhao, Yicheng, Li, Jieming, Zheng, Shenghan, Yang, Ruize, Yang, Bojun, Gong, Heng, Gao, Xiang, Zhang, Lanyue, Zhong, Kaiyu, Liu, Zhuo, Li, Shaoxuan, Li, Chengxi, Yan, Yong, Zhang, Weixuan, Luo, Tianwei, Wang, Situ, Zheng, Youjie, Zhao, Sihan, Wang, Shengyuan, Gao, Huan-ang, Xu, Jiazheng, Xie, Xiaohui, Han, Wentao, Wang, Hongning
**arXiv:** [arxiv.org/abs/2610.12341](https://arxiv.org/abs/2610.12341)
**Summary:** The paper formalizes Adversarial Heuristic Learning, where fixed-weight AI agents improve executable game policies by selecting opponents, analyzing replays, and revising code. On the 12-game AAArena benchmark, leading configurations win only half of the human ladders, exposing persistent weaknesses in rule understanding and long-horizon strategy development.

---

### 10. Continually Post-training Small Models via Synthetic Self-distillation
**Authors:** Koh, Woosung, Lee, Hyunsoo, Lee, Kyungjae, Park, Haeju, Lee, Dahyun, Hwang, Dasol, Lee, Moontae
**arXiv:** [arxiv.org/abs/2610.13113](https://arxiv.org/abs/2610.13113)
**Summary:** Synthetic Self-Distillation enables continual post-training of small models by outsourcing in-distribution rewriting to a slightly larger same-family aligner and combining it with off-policy supervision and rejection sampling. Across four acquisition datasets and 14 retention benchmarks, it consistently improves the balance between learning new capabilities and preserving prior knowledge over six competing methods.

---

### 11. Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction
**Authors:** Huang, Yuqi, Li, Hui, Cao, Yifei, Cai, Zikun, Xie, Tianci, Gao, Yangfan, Guo, Pinxue, Zhang, Chaoyun, Li, Bingxuan, Zheng, Rui, Yan, Hang, Liao, Ning
**arXiv:** [arxiv.org/abs/2610.12984](https://arxiv.org/abs/2610.12984)
**Summary:** Work2Skill records synchronized screens, input events, and accessibility data from human GUI demonstrations, then induces reusable skills that capture workflow rules, dependencies, and completion checks. Its 350-demonstration dataset and evidence-driven induction method improve four execution models by up to 10.54 points on MyPCBench and 7.50 points on OSWorld-Verified.

---

### 12. SepGen: Multi-Stem Audio-Video Separation and Generation in a Single Model
**Authors:** Dahan, Aviad, Khatib, Rajaei, Bitton, Yonatan, Szpektor, Idan, Wolf, Lior, Giryes, Raja
**arXiv:** [arxiv.org/abs/2610.11361](https://arxiv.org/abs/2610.11361)
**Summary:** SepGen extends a pretrained audio-video generator to emit video, a mixed soundtrack, and separate waveforms for each captioned source in one sampling run. The same model supports both source-controlled generation and free-text separation, outperforming language-conditioned separators most clearly on speech recordings.

---

### 13. SoloQ: Calibration-Free Quantization for Diffusion Language Models
**Authors:** Lee, Donghyun, Ghosh, Arkapravo, Manjunath, Varun, Rhee, Bumjoon Kyle, Kook, Hyunho, Xiao, Shiting, Kim, Youngeun, Panda, Priyadarshini
**arXiv:** [arxiv.org/abs/2610.07121](https://arxiv.org/abs/2610.07121)
**Summary:** SoloQ rotates and rescales diffusion-language-model weights and activations into a predictable distribution, enabling calibration-free low-bit quantization and commit-time KV-cache compression. It preserves accuracy across full-sequence and block-diffusion models while NVFP4 reduces peak memory by up to 2.61 times and speeds end-to-end inference by up to 2.24 times.

---

### 14. RSI-Anything: Unlocking Recursive Self-Improvement with World Models
**Authors:** Cui, Taoyong, Zeng, Pinxian, Xu, Wanghan, Xiao, Hao, Xue, Shuhan, Gao, Qiang, Ouyang, Wanli, Heng, Pheng Ann, Yin, Zhenfei, Wu, Yingcheng, Yang, Ling
**arXiv:** [arxiv.org/abs/2610.13912](https://arxiv.org/abs/2610.13912)
**Summary:** RSI-Anything uses predictive world models to guide actions and training-data selection, adapting policies and models from observed feedback while retaining only compatible updates. Across code repair, GUI tasks, laboratory planning, reaction optimization, and immune science, the framework produces persistent improvements under fixed feedback or experiment budgets.

---

### 15. PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence
**Authors:** GuangJian Team, Huang, Kaili, Zhang, Yongshuo, Fu, Bingtao, Jiang, Changjiang, Qu, Chenfan, Zhang, Chenfeng, Cui, Fangming, Zhang, Gaoyang, Xie, Jiangwei, Li, Jianshu, Huang, Jing, Bai, Jingwen, Fang, Mingqi, Fang, Tao, Zhang, Weihong, Du, Wenbo, Bai, Xiongfei, Zhu, Xuekang, Xia, Yinan, Wang, Zhenming, Liu, Jian, Liu, Jingjing, Qi, Xiang, Wang, Weiqiang
**arXiv:** [arxiv.org/abs/2609.37712](https://arxiv.org/abs/2609.37712)
**Summary:** PolyOCR is a family of unified OCR foundation models trained with a quality-verified data engine and a shared instruction-following framework spanning recognition, localization, parsing, and reasoning. Its competence-guided optimization routes between verifier-based policy optimization and on-policy distillation, achieving state-of-the-art or competitive results across five OCR benchmarks.

---

### 16. Contextual Correction of Parallel Draftsfor Speculative Decoding
**Authors:** Eisenstadt, Roy, Lidar, Harel, Gonen, Tal, Luxembourg, Omer, Zimerman, Itamar, Wolf, Lior, David, Eli, Naiman, Ilan
**arXiv:** [arxiv.org/abs/2610.12570](https://arxiv.org/abs/2610.12570)
**Summary:** DCOCO restores missing intra-block dependencies in diffusion-based speculative decoding by retaining multiple token candidates and scoring their contextual compatibility in parallel. Across four verifier backbones and ten benchmarks it delivers the highest average throughput in every tested configuration, including gains of 6% to 23% over the strongest competitor under concurrent serving.

---

### 17. Learning Representations to Guide Pixel Diffusion Transformers
**Authors:** Pan, Zihao, Chen, Mengting, Shi, Cheng, Hu, Taihang, Yue, Zhengrong, Wang, Zikang, Wang, Yuan, Li, Wei, Yang, Sibei
**arXiv:** [arxiv.org/abs/2610.12978](https://arxiv.org/abs/2610.12978)
**Summary:** Representation Guidance compresses generation-relevant information into an internal bottleneck and explicitly uses the resulting representation to guide a plain pixel diffusion transformer. The approach scales efficiently and reaches an FID of 1.55 on ImageNet at 256 pixels while also extending strongly to 512-pixel and text-to-image generation.

---

### 18. Inducing Process Supervision from Outcome-Only Reinforcement Learning
**Authors:** Fan, Shengda, Cong, Xin, Zhang, Zhong, Chen, Haotian, Lin, Yankai
**arXiv:** [arxiv.org/abs/2609.36641](https://arxiv.org/abs/2609.36641)
**Summary:** TIPS trains a generative process reward model using only final-outcome labels, allowing outcome-based reinforcement learning to induce useful step-level verification without explicit process supervision. With 3,200 labeled trajectories, its Qwen3-4B variant reaches 85.2 F1 on ProcessBench and surpasses all evaluated trained process reward models.

---

### 19. SWE-Duel: Towards a Self-Scaling Arena for Coding Agents
**Authors:** Minn, Wei, Sun, Zhensu, Shar, Lwin Khin, Lo, David
**arXiv:** [arxiv.org/abs/2610.12569](https://arxiv.org/abs/2610.12569)
**Summary:** SWE-Duel is a self-scaling coding-agent arena where agents author solvable repository bugs and sealed tests for opponents, then swap roles to repair each other's tasks. A tournament of 11 model-harness combinations across 15 repositories shows distinct strengths in solving and task authoring, with newer agents producing substantially harder defects.

---

### 20. InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators
**Authors:** Dai, Xuanlang, Bu, Jiazi, Zhou, Yujie, Liu, Yuhong, Zhang, Beichen, Yang, Penghui, Liu, Ziyu, Zang, Yuhang
**arXiv:** [arxiv.org/abs/2610.13944](https://arxiv.org/abs/2610.13944)
**Summary:** InstantFusion learns model-specific latent autoencoders that translate intermediate states from heterogeneous frozen image generators through a shared latent space. Aligning states and local denoising velocities enables seamless cross-model handoffs for acceleration, preference composition, distillation, and cross-model generation without a separate mapper for every pair.

---
