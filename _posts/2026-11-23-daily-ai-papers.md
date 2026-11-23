---
title: "Daily AI Papers — November 23, 2026"
date: 2026-11-23
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-23/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - embodied-ai
  - model-efficiency
  - agent-evaluation
---

### 1. cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction
**Authors:** Haowei He, Ziwen Zhao, Chenshuo Pan, Gang Lin, Zhihao Yang, Chao Wang, Xinzhang Liu, Kaidong Yu, Han Gao, Dongfang Li, Menglin Yang, Shuangyong Song, Yongxiang Li
**arXiv:** [arxiv.org/abs/2611.27193](https://arxiv.org/abs/2611.27193)
**Summary:** cmHC geometrically contracts the space of doubly stochastic stream-mixing matrices to balance under-mixing and over-mixing in manifold-constrained hyper-connections. The authors validate the approach across dense and mixture-of-experts pretraining and report that fused Ascend NPU operators reduce hyper-connection execution latency by up to 44.8%.

---

### 2. Non-penetrating World Models
**Authors:** Yuhang Dai, Yinwei Wu, Ziyue Lin, Han Ji, Xingyi Yang
**arXiv:** [arxiv.org/abs/2611.27963](https://arxiv.org/abs/2611.27963)
**Summary:** NoPeWorld trains a small prediction head on frozen diffusion-transformer hidden states to detect obstacle-penetrating actions and replace them with safe alternatives that preserve the intended action. On the introduced NoPeBench benchmark, the authors report reducing average physical violations across six video world models from 74% to 16%, with zero-shot generalization to new imagery, viewpoints, and moving obstacles.

---

### 3. Clover-35B-A3B-Preview Technical Report
**Authors:** DiffuSpace Technical Team
**arXiv:** [arxiv.org/abs/2611.24636](https://arxiv.org/abs/2611.24636)
**Summary:** Clover is a thinking-capable mixture-of-experts diffusion language model with 35 billion total parameters and 3 billion activated parameters, combining recurrent historical memory with bidirectional attention within each generated block. The report gives scores of 73.6 on SWE-bench Verified and 51.7 on Terminal-Bench 2.1, plus a reported generation speed of 680 tokens per second on internal agent workloads using one NVIDIA GB300 GPU at BF16 and batch size one.

---

### 4. SynthDCB: World Distillation for Scalable Device Control Benchmarking
**Authors:** Zichen Zhu, Dingye Liu, Nan Jiang, Danyang Zhang, Hang Zheng, Shijie Zheng, Situo Zhang, Kunyao Lan, Yingzi Ma, Sheng Jiang, Lu Chen, Kai Yu
**arXiv:** [arxiv.org/abs/2611.18639](https://arxiv.org/abs/2611.18639)
**Summary:** SynthDCB uses world distillation to turn device behaviors, constraints, and environmental effects into executable components for verifiable device-control evaluation across Home, Car, and Phone environments. Its benchmark includes 114 device classes and 2,560 test tasks, on which the strongest of 22 evaluated models achieves 88.8% mean Pass@1.

---

### 5. Duopra: From Full-Duplex Conversation to Full-Duplex Agency
**Authors:** Chiyu Chen, Pengzhou Cheng, Yuezhao Ma, Xiaocheng Li, Can Liu, Haonan Hu, Yao Yao, Yifei Yang, Yijie Lu, Taolei Wang, Yansi Li, Muhuan Wu, Chenglu Sun, Gongshen Liu, Zhuosheng Zhang
**arXiv:** [arxiv.org/abs/2611.25773](https://arxiv.org/abs/2611.25773)
**Summary:** Duopra learns timely tool invocation and faithful request revision alongside full-duplex conversational control through protocol supervised fine-tuning, full-duplex reinforcement learning, and talker-conditioning repair. On Full-Duplex-Bench v3, the authors report increasing Pass@1 from 4.7% to 44.7% with the same backend, while direct tool calling reaches 47.7% and a DeepSeek backend reaches 49.3%.

---

### 6. Reading the Unreadable: Text-Aware Image Super-Resolution Needs Reasoning
**Authors:** Jaeseong Lee, Jinwoo Kim, Jinho Jeong, Seon Joo Kim
**arXiv:** [arxiv.org/abs/2611.15449](https://arxiv.org/abs/2611.15449)
**Summary:** ReasonText and Ground-Truth Text-Crop Accuracy expose a systematic gap in super-resolution models when degraded text requires contextual reasoning rather than local visual restoration. The proposed training-free Reasoning Transfer via Captioning plug-in uses a multimodal language model to infer text and supply a caption, improving all six evaluated text-conditioned super-resolution models.

---

### 7. MemOnce: A Scalable Memory Architecture for Large Language Models
**Authors:** Chang Nie, Chaoyou Fu, Songlin Liu, Yiqing Hu, Caifeng Shan
**arXiv:** [arxiv.org/abs/2611.27973](https://arxiv.org/abs/2611.27973)
**Summary:** MemOnce stores compact final-layer hidden states, decodes them into attention-layer KV caches on demand, and computes sparse memory-retrieval indices once across layers. When adapting Qwen3.5-4B at one-million-token context, the authors report a 1,313-fold reduction in memory-state cache, a 6.9-fold reduction in prefill latency, and a 3.5-fold throughput improvement.

---

### 8. Lost in the Hallway: Benchmarking Persistent Spatial Memory Across Revisits
**Authors:** Henry Zheng, Weibo Gong, Yang Yue, Rui Huang, Yang Zhang, Gao Huang
**arXiv:** [arxiv.org/abs/2611.21485](https://arxiv.org/abs/2611.21485)
**Summary:** ReSpaceBench evaluates persistent spatial memory with 3,244 questions across 590 scenes, including revisited rooms, similar-looking distractors, and cross-session object changes. Evaluations reveal substantial model and agent-framework limitations, while fine-tuning Qwen3-VL-8B on the separate RS-30K dataset raises overall accuracy from 35.5% to 60.4%.

---

### 9. AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control
**Authors:** Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo, Yi Xu, Xin Li, Wenbin He, Liu Ren, Chenyan Xiong
**arXiv:** [arxiv.org/abs/2611.26613](https://arxiv.org/abs/2611.26613)
**Summary:** AgentRoboCritic evaluates low-level robot actions against explicitly stated local intents, analyzing recovery, semantic grounding, and physical execution failures across 12 manipulation benchmarks. The authors release 12,844 annotated actions and a fine-tuned Muse-Glimmer-30B critic whose failure-mode accuracy improves from 32.58% to 74.24%, validated against a 400-action human-annotated benchmark.

---

### 10. StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning
**Authors:** Chi Yan, Guoyang Zhao, Wentao Yuan, Yixiao Ge, Yanning Zhou, Dan Xu
**arXiv:** [arxiv.org/abs/2611.27915](https://arxiv.org/abs/2611.27915)
**Summary:** StereoVLM learns metric 3D representations from calibrated binocular images using hierarchical supervision for correspondence, disparity, depth, and semantic spatial reasoning. StereoVLM-8B achieves 95.17% depth accuracy on Stereo3D-Bench, while geometric supervision also improves performance across five spatial benchmarks and raises RoboCasa manipulation success by 4.3 percentage points.

---

### 11. PURE: A Diagnostic Benchmark for Multi-Granularity Multimodal Identity Matching
**Authors:** Hengyu You, Xintong Wang, Jin Cao, Liang Ding
**arXiv:** [arxiv.org/abs/2611.22343](https://arxiv.org/abs/2611.22343)
**Summary:** PURE diagnoses multimodal identity matching at base and variant granularities through 1,457 expert-verified multiple-choice questions spanning perception, understanding, reasoning, and evidence-grounded judgment. Ten evaluated multimodal language models score between 47.1% and 86.0%, with weaknesses in visual difference localization and variant-level rule judgment that aggregate matching accuracy obscures.

---

### 12. AeroRSI: Recursive Self-Improvement for Aerial Vision-Language Navigation
**Authors:** Shiwei Wu, Yuwen Pan, Zhi Li, Yaowen Li, Yan Zhou, Xuemiao Xu, Yu Liu
**arXiv:** [arxiv.org/abs/2611.24077](https://arxiv.org/abs/2611.24077)
**Summary:** AeroRSI recursively improves an aerial navigation policy by collecting its failures, verifying candidate repairs through continued flight, and distilling successful repairs while preserving other behavior. On TravelUAV, three rounds improve a supervised two-billion-parameter policy from 46.4% to 67.5% success and halve collisions without additional human labels or inference cost.

---

### 13. Intent Contracts: Taking Tools Away from Agents
**Authors:** Ziyuan Wang, Genliang Zhu, Xiaobo Chen, Chu Wang
**arXiv:** [arxiv.org/abs/2611.24025](https://arxiv.org/abs/2611.24025)
**Summary:** Intent contracts remove tools from the planning model and require logged goals, user quotations, and scope fields that validated code and a trusted model use to construct tool calls. In benign-overreach evaluations, contracts improve completion of requested tasks relative to an intent-visible reviewer but do not reduce unauthorized actions or resolve wrong-target errors caused by ambiguous references.

---

### 14. Moving Generality from Model to Modeler: LLM Agents for PHM on a Deployment-Style Benchmark
**Authors:** Zhenling Chen, Zhiguo Zeng, Anne Barros
**arXiv:** [arxiv.org/abs/2611.25252](https://arxiv.org/abs/2611.25252)
**Summary:** NextUnit-Bench tests coding agents for prognostics and health management on 24 public datasets with 58 deployment-style folds that hold out equipment or operating conditions. The study finds that frontier agents outperform AutoML and many faithfully implemented published methods, but their advantage depends on data-informed task-specific designs and an implementer capable of executing them.

---

### 15. Prune to Expand: Training Prompt Enhancers with Less to Imitate
**Authors:** Tianhe Wu, Qilin Sun, Kede Ma
**arXiv:** [arxiv.org/abs/2611.27229](https://arxiv.org/abs/2611.27229)
**Summary:** Prune to Expand removes redundant sentences from dense-caption supervision while preserving explicit user requirements and informative visual structure for prompt-enhancement training. Under identical training configurations, the authors report improved human-preference alignment and visual quality across image categories and generators compared with conventional dense-caption supervised fine-tuning.

---

### 16. Search From the Start: Search-Native Pretraining for Language Models
**Authors:** Kaustubh Ponkshe, Gyung Hyun Je, Stefan Taga, Colin Raffel, Martin Jaggi
**arXiv:** [arxiv.org/abs/2611.26809](https://arxiv.org/abs/2611.26809)
**Summary:** Search-Native Pretraining augments ordinary text corpora with search queries and locally retrieved responses so QueryLM models learn to request and use evidence during pretraining. Across knowledge-intensive tasks, a 1.4-billion-parameter QueryLM consistently matches or beats a FLOP-matched 3.3-billion-parameter baseline, and the advantage persists after supervised fine-tuning.

---

### 17. Taking Apart and Putting Together: Tracking Objects Through Physical Transformations
**Authors:** Davide Gardenal, Mingxuan Liu, Flavio Vella, Quentin Guimard, Elisa Ricci
**arXiv:** [arxiv.org/abs/2611.27398](https://arxiv.org/abs/2611.27398)
**Summary:** TIPO is a training-free tracking framework that proposes object splits and merges, evaluates mask overlap, and uses a multimodal language model to verify physical transformations and label their semantics. On the new VISTA dataset of assemblies and disassemblies, the authors report state-of-the-art tracking and state-graph accuracy while operating six to fifteen times faster than prior methods.

---

### 18. Explicit Style Extraction for Personalized Long-Form Text Generation
**Authors:** Jenitha Reddy Patel, Sameeksha Kini, Amulya Rayasam, Anisa Dye, Abhinav Sharma, Sai Karthik Navuluru, Bo Ni, Li Li, Junda Wu, Tong Yu, Nedim Lipka, Xiaolei Huang, Tyler Derr, Yue Zhao, Zhengzhong Tu, Yu Wang, Hongjie Chen, Thien Huu Nguyen, Nesreen K. Ahmed, Franck Dernoncourt, Ryan A. Rossi
**arXiv:** [arxiv.org/abs/2611.27211](https://arxiv.org/abs/2611.27211)
**Summary:** StylePrism organizes 28 stylistic aspects into seven categories, and SP-Refine explicitly extracts a user’s style profile before drafting and revising long-form text twice. Across LongLaMP tasks with three language models, SP-Refine beats the retrieval-augmented baseline in 25 of 27 metric comparisons, while ablations show the profile works best as revision guidance rather than a replacement for user samples.

---

### 19. GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models
**Authors:** Bing He, Runze Wang, Fei Zha, Zhongyuan Wu, Ke Xu, Tao Zhuang, Yuxuan Xie, Zhongyuan Liu
**arXiv:** [arxiv.org/abs/2611.19247](https://arxiv.org/abs/2611.19247)
**Summary:** GameWM separates exact rules, state, camera, and world layout in a game engine from visual appearance and interaction detail generated by a video model. The system combines interaction-centered data, authored character and scene inputs, and a five-to-thirty-three-billion-parameter model family with a real-time causal variant to diversify gameplay visuals without changing engine-computed outcomes.

---

### 20. Motion-Aware Reward Modeling for Instruction-Guided Video Editing
**Authors:** Li Li, Xiangbo Gao, Bo Ni, Samyadeep Basu, Viet Dac Lai, Jing Shi, Seunghyun Yoon, Gang Wu, Yu Wang, Thien Huu Nguyen, Tyler Derr, Franck Dernoncourt, Zhengzhong Tu, Yue Zhao
**arXiv:** [arxiv.org/abs/2611.22495](https://arxiv.org/abs/2611.22495)
**Summary:** This study finds that video-editing rewards can favor motion-suppressed outputs and proposes a motion-aware reward model combining frame differences with preference training against suppressed and fabricated motion. On the VE-Bench motion ladder, the model reduces selection of motion-suppressed candidates to 0% while achieving 0.57 Spearman correlation with human quality ratings and preserving motion during reward-guided fine-tuning.
