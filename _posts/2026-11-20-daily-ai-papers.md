---
title: "Daily AI Papers — November 20, 2026"
date: 2026-11-20
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-20/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal-ai
  - embodied-ai
  - generative-models
---

### 1. WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection
**Authors:** Yipeng Du, Yuxi Li, Ying Zhang, Chong Sun, Chen Li, Jing Lyu, Ying Tai
**arXiv:** [arxiv.org/abs/2611.21373](https://arxiv.org/abs/2611.21373)
**Summary:** WeVisForensics coordinates a main investigator with self-evolving visual and audio forensic sub-agents to detect AI-generated videos and localize the evidence behind its verdicts. Dual-timescale policy optimization and the ForenCue-30K dataset support joint improvement of investigation and inspection, with the authors reporting 95.2% average detection accuracy across their evaluated benchmarks.

---

### 2. Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation
**Authors:** Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang, Ziyi Xiong, Yang Li, Zhengwei Xie, Zhimin Wang, Zhen Liu, Jiazhen Huang, Yuzheng Zhang, Yuche Liu, Hongyi Yang, Chen Tang, Shixiang Tang, Hakan Aktas, Adam Wu, Duo Wu, Kangye Ji, Shuzhao Xie, Huanan Liu, Weijue Bu, Chenxin Li, Xinyuan Wang, Tianyi Bai, Yinan Mao, Jiawei Wang, Minglei Li, Heng Yu, Ehsan Adeli, Minchen Li, Yong-Lu Li, Cengiz Öztireli, Huazhe Xu, Chao Yu, Jing Zhang, Shanghang Zhang, Weitao Zhou, Wenwu Zhu, Cheng Chi, Jingyan Jiang, Zhi Wang
**arXiv:** [arxiv.org/abs/2611.26444](https://arxiv.org/abs/2611.26444)
**Summary:** Mind2Act World separates robotic cognitive reasoning, physical execution, and their closed-loop composition across 30 simulated manipulation tasks and 180 configurations. Its evaluation finds that strong individual capabilities do not reliably compose, with the strongest agent succeeding on only 12.0% of combined Mind2Act episodes.

---

### 3. WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding
**Authors:** Changli Tang, Jie Yang, Tianyi Wang, Lei Li, Daoze Zhang, Zijie Xin, Zhan Liu, Li Li, Jinchang Xu, Fengyun Rao, Chao Zhang, Jing Lyu
**arXiv:** [arxiv.org/abs/2611.26409](https://arxiv.org/abs/2611.26409)
**Summary:** WeMM-Video is a bilingual omni-modal model family that processes text, images, audio, and video in both direct-response and explicit-reasoning modes. Progressive training on approximately 1.2 trillion tokens and multi-stage post-training yield strong results across more than 120 benchmarks, with the authors releasing the models and reproduction pipeline.

---

### 4. Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models
**Authors:** Jiahao Huang, Jun Wang
**arXiv:** [arxiv.org/abs/2611.26590](https://arxiv.org/abs/2611.26590)
**Summary:** The Multimodal Concept Lens maps intermediate vision and language states into a shared vocabulary-defined semantic space to study concept accessibility, selective access, and downstream effects. Interventions and controlled training experiments reveal shared query-dependent patterns across VLM families, providing evidence about global-workspace-like functions rather than establishing consciousness.

---

### 5. Coda-DaVinci: Reimagining Video Generation with Code2Video
**Authors:** Yiyan Ji, Qixun Wang, Yang Shi, Zhuoran Zhang, Yifan Xu, Tengfei Liu, Yuqi Tang, Xiaohan Zhang, Shujie Li, Jiafu Tang, Xuanyu Zhu, Xinyu Liu, Yan He, Yushuo Guan, Zihao Wang, Xianghua Ying, Shixuan Liu, Haotian Wang, Wenjing Yang, Zhaoxiang Zhang, Yuanxing Zhang, Pengfei Wan, Jiaheng Liu
**arXiv:** [arxiv.org/abs/2611.26595](https://arxiv.org/abs/2611.26595)
**Summary:** Coda-DaVinci adapts agent-authored 3D proxy granularity, physics simulation, and proxy-grounded prompts to the requirements of a video-generation task. Controlled experiments and blinded evaluations show improved instruction following, scene consistency, and physical plausibility, while identifying remaining limits in long-video transitions and scene adherence.

---

### 6. The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation
**Authors:** Jeonghwan Cho, Minsu Kim, Junyoung Hong, Seon Joo Kim
**arXiv:** [arxiv.org/abs/2611.21383](https://arxiv.org/abs/2611.21383)
**Summary:** VODA directly supervises depth-clustered Gaussian primitives to address incomplete 3D object selections that can nevertheless render accurate two-dimensional masks. The authors introduce Removal-3D and Removal Depth Error to evaluate volumetric completeness, reporting consistent improvements across four rendering-based baselines without sacrificing established segmentation benchmarks.

---

### 7. HiUni: Harmonizing Understanding and Generation in Shared Visual Space
**Authors:** Jiahao Hu, Jingdong Du, Yichen Zhang, Yi Song, Zhenyu Zhang, Jiaxin Niu, Ruihang Li, Xiangzhao Hao, Yiqian Zhang, Yong Huang, Zefeng Zhang, Zheyuan Gu, Shuohuan Wang
**arXiv:** [arxiv.org/abs/2611.26107](https://arxiv.org/abs/2611.26107)
**Summary:** HiUni extends a pretrained VLM into a unified understanding-and-generation model by sharing its language-aligned vision encoder and dense Transformer backbone. A Pixel Diffusion Head and lightweight HiGate pathway supply generation-specific optimization and spatial detail, preserving average understanding performance while enabling competitive image generation and editing.

---

### 8. EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning
**Authors:** Yuqi Tang, Yang Shi, Yuran Wang, Tengfei Liu, Rundong Wang, Zongyang Qiu, Qixun Wang, Zhuoran Zhang, Xuanyu Zhu, Yifan Xu, Yiyan Ji, Shujie Li, Shixuan Liu, Haotian Wang, Yuanxing Zhang, Pengfei Wan, Chengwei Qin
**arXiv:** [arxiv.org/abs/2611.26380](https://arxiv.org/abs/2611.26380)
**Summary:** EgoCaptioner combines video-level overviews with precisely timed, fine-grained egocentric narration, supported by 50,000 coarse-to-fine annotated training examples. Factual and temporal rewards guide GRPO refinement, with evaluations reporting leading results among compared open-source models on caption quality, caption-conditioned question answering, and temporal alignment.

---

### 9. Posterior Matching Distillation
**Authors:** Hidir Yesiltepe, Julius Berner, Arash Vahdat, Pinar Yanardag
**arXiv:** [arxiv.org/abs/2611.26629](https://arxiv.org/abs/2611.26629)
**Summary:** Posterior Matching Distillation trains a stochastic diffusion student to recover a teacher's full clean-image posterior through exponentially tilted mean constraints rather than a mode-seeking reverse-KL objective. It supports variable sampling budgets on the trained timestep grid without an auxiliary student-score network, achieving the best reported FID among evaluated four-step methods on SDXL and FLUX.2 klein 4B.

---

### 10. Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth
**Authors:** Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, Amaël Delaunoy, Stephan R. Richter, Vladlen Koltun
**arXiv:** [arxiv.org/abs/2611.26603](https://arxiv.org/abs/2611.26603)
**Summary:** Depth Pro 2 uses a single scalable network to estimate native-resolution metric depth from both images and video. The authors report improvements in metric accuracy, boundary sharpness, temporal consistency, and runtime trade-offs, releasing a family of models with code and weights.

---

### 11. TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs
**Authors:** Xuwei Ding, Skylar Zhai, Linxin Song, Jiarui Feng, Dongqi Fu, Huajun Xi, Junnan Li, Jingcheng Liang, Jieyu Zhao, Yinglong Xia, Hong Li, Jian Kang
**arXiv:** [arxiv.org/abs/2611.25387](https://arxiv.org/abs/2611.25387)
**Summary:** TuringSpace offers 125 interactive spatial CAPTCHAs with programmatic instance generation, checkers, and oracles to evaluate perception-action feedback loops. Its analysis finds substantial model-human gaps and screenshot-perception failures, while fine-tuning on the environment improves spatial task success and transfers to seven out-of-distribution benchmarks.

---

### 12. ZeroVLN: Learning to Navigate without Supervised Fine-Tuning of the VLM Brain
**Authors:** Zixuan Huang, Yang Zhou, Guli Zhang, Sunzhu Li, Hongyan Xie, Zehao Chen, Fuzhen Zhuang, Kaixuan Wang, Xiaozhi Chen, Yikun Ban, Deqing Wang
**arXiv:** [arxiv.org/abs/2611.26414](https://arxiv.org/abs/2611.26414)
**Summary:** ZeroVLN lets a VLM navigation brain communicate semantic movement requests to an action expert without navigation-domain supervised fine-tuning of the brain. Closed-loop reinforcement learning jointly improves decisions and continuous execution, outperforming evaluated SFT-based hierarchical navigation methods while largely preserving the brain's general capabilities.

---

### 13. AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators
**Authors:** Nagham Omar, Rotem Dror, Almog Gueta, Avigdor Gal, Roi Reichart, Nitay Calderon
**arXiv:** [arxiv.org/abs/2611.26073](https://arxiv.org/abs/2611.26073)
**Summary:** AltRA-Test evaluates whether an LLM can replace a human annotator when items are labeled by different annotator subsets, using paired bootstrap panels and a non-inferiority test of agreement. Simulations and experiments with 18 LLMs across 20 multimodal datasets support task-specific replacement decisions, with roughly 100 items often sufficient and models passing in only about half of evaluated setups.

---

### 14. Accelerating Mixture of Block Attention via Dynamic Routing, KV-Centric Execution and Runtime Pipelining
**Authors:** Yingqi Shi, Junru Lu, Yun Liu, Di Yin, Xing Sun
**arXiv:** [arxiv.org/abs/2611.26268](https://arxiv.org/abs/2611.26268)
**Summary:** LightningMoBA co-designs dynamic sparse-block routing, KV-centric task ownership, and Hopper runtime pipelining to improve Mixture of Block Attention execution. At matched Top-16 retention across five checkpoints, it reports 1.20 to 1.60 times faster end-to-end generation while increasing mean RULER performance from 74.42 to 75.28.

---

### 15. WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal Loco-Manipulation
**Authors:** Junlin Long, Xu Deng, Yiran Wang, Yue Yang, Yang Zhao, Zeyu Zhang
**arXiv:** [arxiv.org/abs/2611.24011](https://arxiv.org/abs/2611.24011)
**Summary:** WAM-Policy adapts an arm-pretrained world action model to language-conditioned quadrupedal loco-manipulation, then accelerates it with on-policy self-distillation. Task-specific reinforcement learning and multi-teacher distillation raise simulated benchmark success to 85.0%, while the first-stage student samples 14 times faster and is also deployed on a real Unitree Go2 Air.

---

### 16. WM^MLLM: Turning MLLMs into World Models
**Authors:** Baiang Li, Enze Xie, Jincheng Yu, Jin Wang, Haozhe Liu, Yitong Li, Juanxi Tian, Felix Heide
**arXiv:** [arxiv.org/abs/2611.24193](https://arxiv.org/abs/2611.24193)
**Summary:** WM^MLLM maintains an external panoramic world state and revision history, using multimodal LLMs to plan and verify local edits while generators propose views. This design reproduces revisited views exactly at a fixed revision and preserves pixels outside accepted edit regions, with evaluations reporting stronger environment recovery and editing performance than compared baselines.

---

### 17. Training Vision Models for LLM-Driven Weight-Space Programming
**Authors:** Timo Ropinski, Sebastian Kranz
**arXiv:** [arxiv.org/abs/2611.26408](https://arxiv.org/abs/2611.26408)
**Summary:** This work benchmarks LLM-driven direct weight edits of vision networks across relabeling and error-correction tasks, measuring success, side effects, and accuracy loss over more than 2,600 edit processes. Edit-Ready Training rehearses closed-form weight modifications during network preparation, improving editability and producing the highest mean scores for two evaluated LLMs among the compared training methods.

---

### 18. AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher
**Authors:** Guoxin Chen, Shuang Sun, Fanzhe Meng, Xinyu Tang, Ruihua Song, Wayne Xin Zhao
**arXiv:** [arxiv.org/abs/2611.26510](https://arxiv.org/abs/2611.26510)
**Summary:** AutoMaster autonomously develops natural-language skills that shape teacher trajectories before fine-tuning, suppressing undesirable habits and eliciting more effective behaviors. With teacher, task pool, dataset size, and training recipe held fixed, it improves mean performance over unguided successful-trajectory SFT by 1.42 to 8.99 percentage points across terminal, search, and software-engineering settings.

---

### 19. On-Policy Morphing into Hybrid Attention Models
**Authors:** Disen Lan, Xuanda Wang, Jianbin Zheng, Huafeng Kuang, Wei Tang, Yu Cheng
**arXiv:** [arxiv.org/abs/2611.24809](https://arxiv.org/abs/2611.24809)
**Summary:** FlashMorph2 selects which Transformer layers retain full attention by evaluating discrete hybrid architectures on their own hidden states while jointly adapting model weights. Across Qwen3 scales and linear-attention variants, it improves on prior layer-selection methods in long-context and recall-intensive evaluations while completing selection in 0.72 to 3.57 GPU hours.

---

### 20. Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models
**Authors:** John Won, Yonghoon Dong, Jinwoo Shin
**arXiv:** [arxiv.org/abs/2611.25980](https://arxiv.org/abs/2611.25980)
**Summary:** AFFECT trains world models to match the visual consequences of temporally correlated action perturbations, targeting dynamics fidelity rather than video realism alone. Across simulation and real robotic setups, it improves rollout faithfulness, raises DROID policy-success correlation from 0.47 to 0.79, and increases planning task success by up to 8.3%.
