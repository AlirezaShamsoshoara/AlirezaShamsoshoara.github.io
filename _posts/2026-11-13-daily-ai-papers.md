---
title: "Daily AI Papers — November 13, 2026"
date: 2026-11-13
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-13/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - world-models
  - video-generation
  - ai-agents
---

### 1. SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models
**Authors:** Lichen Li, Ziping Dong, Sicheng Feng, Qi Li, Xinchao Wang
**arXiv:** [arxiv.org/abs/2611.15777](https://arxiv.org/abs/2611.15777)
**Summary:** SO-Arena evaluates fast System One decision models across 11 domains and five capability families, testing both task performance and reliability under changed options or missing valid answers. Across 21 models, stronger aggregate accuracy does not guarantee reliable decisions, with the best-performing System One model ranking only seventh on reliability.

---

### 2. BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model
**Authors:** Junyoung Seo, Jaewoo Seo, Seungryong Kim, Laura Leal-Taixé, Xiuming Zhang, Seung Wook Kim
**arXiv:** [arxiv.org/abs/2611.14815](https://arxiv.org/abs/2611.14815)
**Summary:** BirdDreams jointly generates perspective and bird's-eye-view videos so a driving world model can predict surrounding-vehicle motion while following a specified ego trajectory. Starting from a single camera image without HD maps or vehicle-state inputs, it improves trajectory fidelity on PhysicalAI-AV and nuScenes and produces more realistic surrounding-vehicle behavior than a perspective-only baseline in human evaluation.

---

### 3. PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models
**Authors:** Yuxuan Chen, Xiaojie Li, Hao Chen, Juncheng Ma, Kewei Zhang, Zhongjing Du, Guoqiang Wei, Fangfang Wang, Zhen Dong, Zhiyang Dou, Liming Zhao, Yan Zeng, Jianwei Zhang, Daquan Zhou
**arXiv:** [arxiv.org/abs/2611.16748](https://arxiv.org/abs/2611.16748)
**Summary:** PhysLoop constrains and guides language models through video generation, selection, and correction to turn their physical knowledge into training data and inference-time repairs. The authors release 100K videos, generation tools, and two evaluation datasets, and assess controllable generation, localized repair, and physical behavior on an external benchmark.

---

### 4. G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation
**Authors:** Xu Huang, Ye Huang, Xiaotong Li, Zhengrong Yue, Jialv Zou, Minhao Jing, Haodong Li, Wenhao Yan, Yaxin Luo, Duomin Wang, Daquan Zhou
**arXiv:** [arxiv.org/abs/2611.13004](https://arxiv.org/abs/2611.13004)
**Summary:** G-STAR scales product-quantization group size with spatial compression and adds a semi-autoregressive decoder to preserve image quality with much shorter token sequences. Its deeply compressed models remain competitive across five text-to-image benchmarks and report a 20-fold speedup over prior discrete autoregressive models, generating a 1024-by-1024 image in 2.5 seconds on one NVIDIA H200.

---

### 5. Duo: A Reciprocal World Model for Full-Duplex Interaction
**Authors:** Hengyuan Cao, Biao Gong, Guoshan Lu, Qiyuan Zhang, Lin Liu, Yiding Tian, Yilei Jiang, Yuxin Ma, Chengzhang Wu, Kun Chen, Yiqian Xie, Ting Liu, Xin Zheng, Xijun Gu, Tianren Ma, Jiancheng Pan, Chi Zhang, Xuzhe Zheng, Siyi Li, Zhenzhong Lan
**arXiv:** [arxiv.org/abs/2611.15131](https://arxiv.org/abs/2611.15131)
**Summary:** Duo v1 is a full-duplex audiovisual world model that separates interaction reasoning, called Intent, from coherent audiovisual generation, called Realization, while synchronizing both on a causal timeline. Dual rollout distillation trains the modules on their generated histories to support continuous perception, spontaneous conversation, interruptions, and interactive audiovisual experiences.

---

### 6. Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents
**Authors:** Haochen Liu, Qianhao Zhu, Zixuan Wang, Dingming Li, Tongbo Chen, Peng Qiu, Yingqi Qu, Weiming Lu, Jun Xiao, Yongliang Shen
**arXiv:** [arxiv.org/abs/2611.17167](https://arxiv.org/abs/2611.17167)
**Summary:** This study compares decision models as actors, retrospective judges, and reinforcement-learning teachers, finding that weak action selection can coexist with useful evaluation of completed trajectories. Using JEV as a teacher raises a Qwen2.5-1.5B policy's success rate over GRPO from 72.8% to 82.9% on ALFWorld and from 56.8% to 71.4% on WebShop.

---

### 7. On the Design of Hyper-Connections: Simplification, Stability, and Scalability
**Authors:** Xiangdong Zhang, Xiaohan Qin, Sunan Zou, Tuo Dai, Bizhao Shi, Zhuo Xia, Yebin Yang, Yizhou Chen, Yuliang Liu, Yu Cheng, Junchi Yan
**arXiv:** [arxiv.org/abs/2611.05984](https://arxiv.org/abs/2611.05984)
**Summary:** SimpleHC removes residual mixing and shares memory access after an analysis finds that simpler hyper-connection interaction groups can match mHC while repeated residual-state access drives overhead. It maintains comparable performance when scaling from 15B to 30B mixture-of-experts models, adds only 2.4% end-to-end training time at the largest tested scale, and exhibits smoother gradients and stress-test stability.

---

### 8. Open Vision Banana: A Fully Open Recipe for Generative Visual Perception
**Authors:** Arpit Jadon, Valentinos Pariza, Jona Ruthardt, Ryousuke Yamada, A. Sophia Koepke, Andrei Bursuc, Yuki M. Asano
**arXiv:** [arxiv.org/abs/2611.15844](https://arxiv.org/abs/2611.15844)
**Summary:** Open Vision Banana provides public data pipelines, code, and checkpoints for adapting pretrained image generators into multi-task visual perception systems, with experiments on interacting design choices. Its models exceed Vision Banana's reported Cityscapes zero-shot score, while test-time legend ensembling improves segmentation without retraining and other segmentation tasks retain documented performance gaps.

---

### 9. Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors
**Authors:** Hao Li, Fangzhou Hong, Zhaoxi Chen, Hui En Pang, Kairui Hu, Mingze Sun, Runmao Yao, Xinhao Ji, Xiyuan Zheng, Xuanli Chen, Yalun Dai, Yap Kim Hui, Dingwen Zhang, Yuanyuan Gao, Ziang Cao, Cheng Huang Yean, Jackson Peng, Rui Duan, Yaobo Liu, Zetong Wang, Ziwei Liu
**arXiv:** [arxiv.org/abs/2611.17060](https://arxiv.org/abs/2611.17060)
**Summary:** Ropedia Xperience 2 releases 1,589 metric-scale 3D scans and 4,230 egocentric recordings covering 74 tasks and 131 hours to jointly capture physical environments and human behavior. It demonstrates converting scenes into interactive simulations, retargeting human motion to whole-body robot trajectories, and producing additional behaviors through virtual teleoperation and automated trajectory generation.

---

### 10. TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models
**Authors:** Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe, Min-Hung Chen, Yu-Chiang Frank Wang, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu, Cheng Sun
**arXiv:** [arxiv.org/abs/2611.17331](https://arxiv.org/abs/2611.17331)
**Summary:** Test-time Baking distills global cross-view attention mappings into lightweight MLPs for decoder-only novel-view synthesis instead of replacing attention wholesale. Separating camera-only rendering inputs from image-containing mapping targets addresses modality misalignment, enabling up to a 23-fold rendering speedup with quality comparable to state-of-the-art systems across several benchmarks.

---

### 11. WorldDraft: If Code Builds the World, Can Video Models Just Render It?
**Authors:** Zhiyu Hou, Wen-Jie Shu, Harold Haodong Chen, Weilin Ruan, Chenfei Liao, Liuzhou Zhang, Disen Lan, Xiaogang Xu, Qi Chen, Ser-Nam Lim
**arXiv:** [arxiv.org/abs/2611.16217](https://arxiv.org/abs/2611.16217)
**Summary:** WorldDraft benchmarks video models as renderers of code-built 4D worlds using 432 paired cases across 48 executable world families with independently controlled scaffold detail and appearance cues. Evaluations of 12 models reveal tension between preserving dynamics and realizing target appearance, while the plug-and-play WorldDraft-Primer prompting strategy improves both objectives across frozen renderers.

---

### 12. Factored One-sided Adam-Moment for Practical and Scalable SOAP
**Authors:** Jaemyung Yu, Byeongho Heo, Sangdoo Yun, Dongyoon Han
**arXiv:** [arxiv.org/abs/2611.16905](https://arxiv.org/abs/2611.16905)
**Summary:** FOAM reduces SOAP's costs by using input-only preconditioning and a factored Adam second-moment estimator, with theoretical justification under stated curvature and Fisher assumptions. Across language-model pretraining experiments from 124M to 760M parameters, it matches strong SOAP and Muon validation-loss baselines, uses half of SOAP's optimizer state, and runs at Muon-class wall-clock time.

---

### 13. UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation
**Authors:** Jiancheng Pan, Yuzheng Liu, Hengyuan Cao, Qiyuan Zhang, Yangyan Li, Biao Gong, Zheng Zhang, Ka Long Cheng, Xinyang Wang, Yujun Shen
**arXiv:** [arxiv.org/abs/2611.16517](https://arxiv.org/abs/2611.16517)
**Summary:** UniSpark combines full attention with GatedDeltaNet linear attention in a mixture-of-transformer-experts multimodal backbone to support understanding, image generation, editing, and interleaved prediction. A blockwise causal protocol separates noisy targets from clean context, while four-stage training extends synthesis to 2K and yields reported scores of 2470.3 on MME-S and 0.83 on GenEval.

---

### 14. FAME-QP: A GPU-Accelerated Quadratic-Programming Solver for Real-Time Model Predictive Control
**Authors:** Santosh Mohan Rajkumar, Debdipta Goswami, Stephanie Stockar
**arXiv:** [arxiv.org/abs/2611.13766](https://arxiv.org/abs/2611.13766)
**Summary:** FAME-QP accelerates dense quadratic programs for linear model predictive control using constraint-dependent operators, fused GPU kernels, and CUDA-graph replay. Device calibration, problem-specific timing, cached operator selection, and lazy updates reduce latency against competing GPU solvers in numerical benchmarks and simulated humanoid and quadrotor control while preserving accuracy and control performance.

---

### 15. Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis
**Authors:** Julia Herbst, Simon Roschmann, Quentin Bouniot, Zeynep Akata
**arXiv:** [arxiv.org/abs/2611.12869](https://arxiv.org/abs/2611.12869)
**Summary:** This study revisits the Platonic Representation Hypothesis by examining cross-modal alignment across model layers and dimensions and introducing unimodal and multimodal comparison baselines. It finds that the capability-alignment trend persists for newer language models with sufficiently informative captions, while cross-modal similarity remains well below same-modality alignment even when it exceeds explicitly aligned vision-language models.

---

### 16. Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement
**Authors:** Wenbo Huang, Jianxin Bi, Shunyu Yang, Ruiyang Si, Rui Ni, Qiang Wang, Shulong Jiang, Yintianrun Zhang, Feixiang Ruan, Kewei Zhang, Ye Huang, Shukai Gong, Daquan Zhou
**arXiv:** [arxiv.org/abs/2611.08318](https://arxiv.org/abs/2611.08318)
**Summary:** Controlled embodied self-improvement experiments test whether exposing benchmark success criteria teaches agents the instructed task or encourages overfitting to the verifier. Criteria exposure boosts the original benchmark score, but its advantage disappears after instruction-preserving criteria changes and learned skills transfer poorly, motivating instruction-faithful evaluation criteria.

---

### 17. Subliminal Learning in Vision-Language Models
**Authors:** Arman Hatami, Romina Aalishah, Ilya E. Monosov
**arXiv:** [arxiv.org/abs/2611.08538](https://arxiv.org/abs/2611.08538)
**Summary:** Subliminal Learning in Vision-Language Models shows that a teacher's animal or facial preferences can transfer to students through numeric outputs from an unrelated geometric-shape task. Across 2B-to-7B models, animal-preference differences reach roughly 10 percentage points, and biased students also adopt more of their teacher's explanatory wording despite the unrelated training task.

---

### 18. DeepStress: Stress-Testing Deep Search Agents
**Authors:** Ismael Rousseau, Geraldine Damnati, Frederic Bechet
**arXiv:** [arxiv.org/abs/2607.13920](https://arxiv.org/abs/2607.13920)
**Summary:** DeepStress replaces retrieval with a controlled synthetic environment that independently degrades document trustworthiness, relevance, and factuality to stress-test search agents. Evaluating 12 systems on HotpotQA and BrowseComp-Plus reveals confident answers despite credibility red flags and frequent reliance on parametric knowledge even when all retrieved documents are factually wrong.

---

### 19. Precision on Demand: Escalating Weight Bits at Uncertain Decoding Steps in a Small Local Model
**Authors:** Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri
**arXiv:** [arxiv.org/abs/2611.14418](https://arxiv.org/abs/2611.14418)
**Summary:** This small-model study simulates decoding with four-bit weights and escalating uncertain steps to eight-bit precision, finding that low-pass entropy and margin can identify many changed token choices. On 150 GSM8K problems, an entropy gate reaches 62.7% accuracy at 0.87 of all-high weight-byte cost, but the live results do not statistically separate it from either fixed-precision endpoint and do not establish hardware speedups.

---

### 20. WMIP: A Working-Memory-Inspired Programmable Probe of Cumulative State Tracking in Large Language Models
**Authors:** Dengzhe Hou, Lingyu Jiang, Deng Li, Zirui Li, Fangzhou Lin, Kazunori D Yamada
**arXiv:** [arxiv.org/abs/2603.27343](https://arxiv.org/abs/2603.27343)
**Summary:** WMIP probes cumulative state tracking with program-computed answers, three to 100 updates, and multiple query protocols across 18 language models. Accuracy falls from 84.9% on single-step arithmetic to 31.7% on short cumulative tasks, no model exceeds 10% from 50 updates onward, and explicit written-step instructions substantially change measured performance.

---
