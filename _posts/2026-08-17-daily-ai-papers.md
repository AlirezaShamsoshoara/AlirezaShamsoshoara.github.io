---
title: "Daily AI Papers — August 17, 2026"
date: 2026-08-17
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-17/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - on-policy-distillation
  - evaluation-benchmarks
---

### 1. Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A Systematic Evaluation of Detectors, Generators and Social Dissemination
**Authors:** Shuo Liang, Yixing Ma, Pengfei Zhou, Xingyan Chen, Zihan Mei, Manting Li, Feihan Chen, Zhiwen Wang, Bin Xu, Haotian Zhang, Jiajun Song, Shiya Su, Run Liu, Zhenghang Ni, Yifa Yu, Jintao Hong, Bolong Feng, Yifei Liu, Zirui Zhang, Jingxuan Zhang, Songlin Zhao, Yifan Bai, Kang Tan, Yizhe Liu, Junhao Du, Yongtao Ge, Zhaopan Xv, Xinyuan Zhang, Mengru Ma, Chunhua Shen, Wei Wang, Yang You, Zheng Zhu, Kaipeng Zhang, Wangbo Zhao
**arXiv:** [arxiv.org/abs/2608.14391](https://arxiv.org/abs/2608.14391)
**Summary:** Recent video generators can fabricate realistic depictions of wars, disasters, public emergencies, and other real-world crises, creating substantial risks of misinformation. Existing benchmarks, however, provide limited evidence on detector and generator behavior in such settings, including how detectability varies with generation conditions, how people perceive generated videos, and whether detectors remain reliable during social dissemination.
**Trending because:** 255 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 2. Self-Supervised Visual On-Policy Distillation
**Authors:** Yijiang Li, Yijun Liang, Yunjie Tian, Bingyang Wang, Ke Zhang, Zhenfei Yin, Di Fu, Philip Torr, Nuno Vasconcelos
**arXiv:** [arxiv.org/abs/2608.14144](https://arxiv.org/abs/2608.14144)
**Summary:** Visual on-policy distillation relies heavily on an informative teacher-student asymmetry, through either a larger, stronger teacher or privileged supervision, such as reference answers or ground-truth regions of interest. This raises a fundamental question: where can informative asymmetry come from when nothing privileged is available?
**Trending because:** 139 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 3. Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development
**Authors:** Yiwei Li, Wanli Yang, Hexiang Tan, Xiangzhou Huang, Zhengyu Chen, Ziran Li, Borun Chen, Shanglin Lei, Huaisheng Zhu, Hao Tian, Fei Sun, Xunliang Cai, Jingang Wang
**arXiv:** [arxiv.org/abs/2608.13417](https://arxiv.org/abs/2608.13417)
**Summary:** Autonomous agents are increasingly capable of improving models, systems, and other technical artifacts through long-horizon experimentation. To understand the current state of this capability, however, evaluation must go beyond final scores, which neither reveal where progress is gained or lost nor indicate whether accumulated experience improves later decisions.
**Trending because:** 38 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 4. Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning
**Authors:** Kai Chen, Jifeng Ding, Ning Ding, Jiaye Ge, Lixin Gu, Yicheng Gu, Qipeng Guo, Ermo Hua, Haian Huang, Haozheng Hou, Jie Hou, Xiangyu Hong, Che Jiang, Minxi Jin, Cheng Liang, Dahua Lin, Dawei Liu, Kuikun Liu, Chengqi Lv, Haijun Lv, Han Lv, Ningsheng Ma, Biqing Qi, Jianmin Qian, Shiya Su, Youbang Sun, Huanze Tang, Zhongbo Tian, Hanjing Wang, Rui Wang, Ting Wang, Yi Wang, Baiting Wu, Jun Xu, Bowen Yang, Hui Wang, Weida Wang, Haochen Ye, Jiashuo Yu, Shan Yu, Xiaoyi Yu, Qirui Zeng, Qi Zhang, Ming Zhang, Wenwei Zhang, Bowen Zhou, Xinyu Zhou
**arXiv:** [arxiv.org/abs/2608.14290](https://arxiv.org/abs/2608.14290)
**Summary:** We introduce Mobius-v0, an architecture that comprises a globally shared Memory (FFN) that stores knowledge vectors and multiple Reasoners (Self-Attn) that iteratively achieve compositional reasoning. Using hidden states as cache and carrier, reasoners repeatedly query memory for required knowledge-vectors, while the knowledge is transmitted back to reasoning operators.
**Trending because:** 29 HuggingFace upvotes + a foundation-model release with broad applicability

---

### 5. Marionette: Predicting World States, Rendering Geometry, Painting Appearance
**Authors:** Zian Meng, Zhen Li, Chuanhao Li, Qiang Li, Kaipeng Zhang
**arXiv:** [arxiv.org/abs/2608.14530](https://arxiv.org/abs/2608.14530)
**Summary:** Interactive game world models typically autoregress visual observations directly in pixel or latent space, forcing structured properties such as pose, geometry, and occlusion to be implicitly maintained by the same generative sequence. Over long horizons, errors in these latent world properties accumulate, making consistency and controllability fragile.
**Trending because:** 22 HuggingFace upvotes + addressing an urgent real-world safety concern

---

### 6. MobileMem: Learning from a Year of Mobile Experiences
**Authors:** Xinle Deng, Yida Xue, Xiangyuan Ru, Haoming Xu, Shuofei Qiao, Mengru Wang, Yijun Chen, Buqiang Xu, Chen Jiang, Yuchen Eleanor Jiang, Lizhong Wang, Jianfeng Wang, Li Zeng, Haofen Wang, Guilin Qi, Huajun Chen, Ningyu Zhang
**arXiv:** [arxiv.org/abs/2608.13606](https://arxiv.org/abs/2608.13606)
**Summary:** The next generation of AI agents is increasingly moving beyond systems that answer isolated questions toward persistent personal assistants that can understand, remember, and continuously learn from users' experiences. Such assistants require long-term memory to accumulate and leverage user-specific experiences over time, yet existing benchmarks remain inadequate for realistic mobile settings, where experiences are heterogeneous, multimodal, evolving, and deeply personal.
**Trending because:** 20 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 7. SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Reasoning
**Authors:** Haonan He, Haodi Lei, Yun Luo, Haoran Zhang, Shunkai Zhang, Yizhuo Li, Shengji Tang, Zhilin Wang, Runzhe Zhan, Lei Bai, Ganqu Cui, Fangchen Yu, Yafu Li, Peng Ye, Ning Ding, Yu Cheng
**arXiv:** [arxiv.org/abs/2608.14277](https://arxiv.org/abs/2608.14277)
**Summary:** On-policy distillation (OPD) offers a promising way to transfer reasoning capabilities from stronger teacher models, but applying it to long-context reasoning teachers and short-context students introduces practical challenges, including tokenizer mismatch, teacher-student distribution mismatch, response length explosion, and training instability. In this work, we study this setting by transferring proof-reasoning capabilities from the long-context reasoning model SU-01 to short-context student models.
**Trending because:** 19 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 8. DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data
**Authors:** Peter Schneider-Kamp, Jacob Nielsen, Gianluca Barmina, Kenneth Enevoldsen, Lukas Galke Poech
**arXiv:** [arxiv.org/abs/2608.13517](https://arxiv.org/abs/2608.13517)
**Summary:** Current large language model development relies on massive, often non-permissible datasets, creating a high barrier for researchers committed to open-source and ethically sourced data. We introduce Mimir v1, a 1-billion-parameter language model based on the Hierarchical Reasoning Model (HRM) architecture, that is trained from scratch and delivers highly competitive performance for English and sets a new state of the art for Danish using only permissible post-training data.
**Trending because:** 18 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 9. Apodex Discovery: Reality Benchmarks and Environments for Evaluating and Building Discoverative Artificial Intelligence
**Authors:** Brian Wang, Bin Feng, Xiaoman Pan, Chenyang An, Felix Liu, Tangqi Fang, Gongbo Sun, Lingfeng Shen, Ning Wang, Handuo Zhang, Feng Chen, Fuchao Yang, Xiang Wang, Jiacheng Lin, Siting Li, Zixuan Liu, Chi Han, Zhenhailong Wang, Kunlun Zhu, Lawrence Zhao, Yueqi Guo, Kailong Wen, Feng Xing, Yiling Guo, Lidong Bing, David Tan, Bo An, Heng Ji, Sheng Wang
**arXiv:** [arxiv.org/abs/2608.11341](https://arxiv.org/abs/2608.11341)
**Summary:** Apollo did not reach the Moon merely because its engineers could solve difficult equations. It succeeded by turning a distant ambition into a mission architecture of explicit objectives, simulation, verification, and repeated correction.
**Trending because:** 15 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 10. HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark
**Authors:** Dairu Liu, Zekun Qi, Jiayu Zeng, Ruixi Yu, Yu Guan, Yintianrun Zhang, Xuchuan Chen, Sikai Liang, Zekai Li, Chenghuai Lin, Xinqiang Yu, Wenyao Zhang, He Wang, Li Yi
**arXiv:** [arxiv.org/abs/2608.13555](https://arxiv.org/abs/2608.13555)
**Summary:** Humanoid motion tracking is central to teleoperation and whole-body imitation, yet evaluation often disagrees with what people perceive in videos. Kinematic errors average per-frame pose differences but miss the physical artifacts that matter most, particularly unstable support and incorrect contacts such as foot skating and mistimed touch-downs.
**Trending because:** 15 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 11. CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Image Editing
**Authors:** Qinye Zhou, Jun Zheng, Yongchao Du, Yuan Wang, Zhengrui Chen, Zuan Gao, Taihang Hu, Chao Lin, Yefeng Shen, Xingjian Wang, Zhao Wang, Zhengtao Wu, Xiaoli Xu, Zhengze Xu, Hao Yan, Denghui Yang, Yuhang Yu, Huayu Zhang, Mingzhou Zhang, Mengting Chen
**arXiv:** [arxiv.org/abs/2608.14546](https://arxiv.org/abs/2608.14546)
**Summary:** With the rapid advancement of image editing models and their widespread application across various domains, there is an increasingly urgent need to deploy these model capabilities directly into real-world scenarios. However, existing benchmarks remain confined to simple single-image tasks, suffering from limited coverage dimensions and an inability to effectively differentiate performance among diverse models.
**Trending because:** 12 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 12. Claim-Level Reliability Assessment for Efficient Test-Time Reasoning
**Authors:** Sen Xu, Wei Wang, Shixi Liu, Jixin Min, Yingwei Dai, Zhibin Yin, Yirong Chen, Junlin Zhang
**arXiv:** [arxiv.org/abs/2608.11994](https://arxiv.org/abs/2608.11994)
**Summary:** We propose claim-level falsification as a principle for test-time scaling and instantiate it through Claim-Level Reliability Assessment (CLR), a training-free framework that reallocates test-time compute from additional solution sampling to targeted verification. Since whole-trace evaluation often obscures decisive errors due to signal dilution from routine tokens, CLR condenses each reasoning trace into a compact set of decision-critical claims, thereby isolating its logical anchors.
**Trending because:** 9 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 13. Latent On-Policy Self-Distillation
**Authors:** Guibin Zhang, Jiayang Lyu, Ran Sun, Xinlei Yu, Haoyu Zhao, Qibing Ren, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2608.13040](https://arxiv.org/abs/2608.13040)
**Summary:** Enabling agents to learn from experience and internalize it into their policy has become a central problem in self-evolving AI. On-policy self-distillation (OPSD) offers an effective pathway by using a privileged self-teacher to provide dense supervision on the student's own trajectories; however, existing methods still rely heavily on designer-specified privileged artifacts (e.g., answers, feedback, skills, or trajectories), limiting the end-to-end learnability and scalability required for continual self-improvement.
**Trending because:** 9 HuggingFace upvotes + advancing on-policy distillation, a hot training paradigm

---

### 14. PRM-as-a-Judge 1.5: A Toolkit for Robot Process Assessment
**Authors:** Yuyang Liu, Yanqing Shen, Ruike Chen, Jifan Zhao, Yuxuan Tian, Yichi Zhang, Tianfeng Long, Zixuan Yin, Yipu Wang, Ziheng Qin, Wenxing Tan, Yang Shi, Mingyu Cao, Runze Xiao, Ziqi Wang, Zhixin Yin, Shiwei Chu, Yi-Fan Zhang, Yao Mu, Yuheng Ji, Yihao Wang, Jun Yan, Zhongyuan Wang, Pengwei Wang, Xiaolong Zheng
**arXiv:** [arxiv.org/abs/2608.14284](https://arxiv.org/abs/2608.14284)
**Summary:** Fine-grained robotic evaluation matters for understanding embodied models, going beyond binary success rates and rule-based process scores. We present PRM-as-a-Judge 1.5, a toolkit for robot process assessment that turns rollout videos into dense progress curves and derives multiple fine metrics.
**Trending because:** 9 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 15. CW-BASS v2: Saturation-Aware Pseudo-Label Selection for Semi-Supervised Segmentation under Foundation-Model Teachers
**Authors:** Ebenezer Tarubinga
**arXiv:** [arxiv.org/abs/2608.12773](https://arxiv.org/abs/2608.12773)
**Summary:** Semi-supervised semantic segmentation has long turned on one question, which pseudo-labels to trust, and a generation of selection rules, dynamic thresholds, per-class curricula, soft confidence weights, answered it for the noisy, under-confident ResNet teachers of their day. Self-supervised foundation encoders change the regime: with a DINOv2 teacher, confidence saturates, so the filtering that helped a weak teacher can hurt a strong one.
**Trending because:** 8 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 16. Modular Cognitive Architecture Emerges in Large Language Models
**Authors:** Pengrui Han, Jacob Andreas, Evelina Fedorenko, Andrea Gregor de Varda
**arXiv:** [arxiv.org/abs/2608.13567](https://arxiv.org/abs/2608.13567)
**Summary:** The human brain exhibits a striking degree of functional specialization, with distinct networks supporting language, formal reasoning, reasoning about other minds, and reasoning about the physical world. Is this modular organization a fundamental principle of how intelligent systems must be built, or an evolutionary accident specific to biological brains?
**Trending because:** 8 HuggingFace upvotes + pushing on reasoning, a central LLM research frontier

---

### 17. TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation with Operational Validity Enforcement
**Authors:** Karim Aly, Alexei Sharpanskykh, Jacco Hoekstra
**arXiv:** [arxiv.org/abs/2608.11951](https://arxiv.org/abs/2608.11951)
**Summary:** Extreme events in air transport, such as severe arrival delays and abnormal air times, cause cascading network disruptions with substantial operational, economic, and safety costs. Such events are rare in historical records, leaving insufficient training signal for machine learning models.
**Trending because:** 8 HuggingFace upvotes + a notable contribution generating community discussion

---

### 18. Forecast Collapse in Time-Series Foundation Models
**Authors:** Shu Wan, Miles Ma, Hank Zhu, Guangqi Liu, Stephen Wang, Qingsong Wen, Huan Liu
**arXiv:** [arxiv.org/abs/2608.14106](https://arxiv.org/abs/2608.14106)
**Summary:** When forecasting hourly returns for 1,000 US equities, we observe an unexpected phenomenon: predictions become nearly flat and show poor stock ranking, as measured by cross-sectional correlation. We call this forecast collapse.
**Trending because:** 7 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 19. Multimodal Model Diffing for Feature Discovery and Control
**Authors:** Hunar Batra, Lachin Naghashyar, Ashkan Khakzar, Philip Torr, Christian Schroeder de Witt, Constantin Venhoff, Ronald Clark
**arXiv:** [arxiv.org/abs/2608.09928](https://arxiv.org/abs/2608.09928)
**Summary:** Multimodal Large Language Models (MLLMs) exhibit strong visual understanding, yet the internal features that cause these behaviors remain difficult to identify, audit, or control. While applicable to post-hoc inspection, hidden states that are decomposed into interpretable feature directions using sparse autoencoders (SAEs) neither readily isolate which features are changed by multimodal training, nor are they directly useful for targeted control.
**Trending because:** 7 HuggingFace upvotes + a notable contribution generating community discussion

---

### 20. PixSDS: Why Latent SDS Makes Noisy Pixels
**Authors:** Vsevolod Skorokhodov
**arXiv:** [arxiv.org/abs/2608.12997](https://arxiv.org/abs/2608.12997)
**Summary:** Score Distillation Sampling (SDS) enables text-to-3D generation by optimizing rendered images with a pretrained diffusion prior, but latent SDS often produces structured color artifacts and high-frequency texture noise. We identify a failure mode of latent SDS caused by VAE-induced pixel drift: the optimized image can move along pixel-space directions that are weakly constrained by the VAE encoder, so its latent representation remains clean and semantically meaningful while the image itself accumulates visible artifacts.
**Trending because:** 7 HuggingFace upvotes + advancing on-policy distillation, a hot training paradigm

---
