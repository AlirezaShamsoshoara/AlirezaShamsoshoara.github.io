---
title: "Daily AI Papers — September 7, 2026"
date: 2026-09-07
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-07/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - multimodal-learning
  - model-alignment
---

### 1. Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of Reasoning Operations in LLMs
**Authors:** Seogyeong Jeong, Jaehui Hwang, Dongyoon Han, Geonmo Gu, Alice Oh, Taekyung Kim
**arXiv:** [arxiv.org/abs/2609.04753](https://arxiv.org/abs/2609.04753)
**Summary:** Reasoning in large language models unfolds through diverse functional operations, such as problem formulation, goal decomposition, and deduction. Although these operations are explicitly distinguished in text, little is known about how they are geometrically organized in representation spaces.
**Trending because:** 13 HuggingFace upvotes + mechanistic evidence about how LLMs represent reasoning operations

---

### 2. UniMate: One Unified Model to Animate Diverse Skeletons
**Authors:** Linzhan Mou, Jiahui Lei, Zhiyang Dou, Chenyue Cai, Chaoyue Song, Adam Finkelstein, Szymon Rusinkiewicz
**arXiv:** [arxiv.org/abs/2609.05415](https://arxiv.org/abs/2609.05415)
**Summary:** Recent advances in automatic rigging now deliver animation-ready 3D assets at scale, yet generating the motion to drive them remains a bottleneck. Existing learned animators are topology-constrained: they rely on category-specific templates or require per-skeleton fine-tuning and reference motions at inference.
**Trending because:** 13 HuggingFace upvotes + one animation model generalizes across arbitrary skeleton topologies

---

### 3. MaxKernel: Agentic Kernel Generation for TPUs
**Authors:** Shangkun Wang, Nina Cai, Charles Hoong, Julian Walker, Gerson Kroiz, George Vanica, Deepak Patil, Andi Gavrilescu, Hassan Sipra, Sethu Sankaran
**arXiv:** [arxiv.org/abs/2609.04523](https://arxiv.org/abs/2609.04523)
**Summary:** Designing and authoring high-performance custom kernels for accelerators is a complex task that requires deep hardware-level expertise. Large Language Models (LLM) can be leveraged together with real-time compiler feedback to build agentic systems for kernel generation.
**Trending because:** 12 HuggingFace upvotes + agentic compiler feedback automates high-performance TPU kernels

---

### 4. EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents
**Authors:** Wei Wang, Wenqiao Zhang, Yutong Lin, Yuqian Yuan, Tianwei Lin, Jinhao Mao, Zhenxuan Fan, Mingjian Gao, Yang Dai, Wentong Li, Zheqi Lv, Zheng Dong, Yingjie Niu, Jiaqi Zhu, Jun Xiao, Chao Li, Yueting Zhuang
**arXiv:** [arxiv.org/abs/2609.01281](https://arxiv.org/abs/2609.01281)
**Summary:** Vision-language-action (VLA) models map visual observations and language instructions directly to robot actions, but long-horizon tasks require more than action prediction. An agent must coordinate perception, planning, execution, progress verification, and recovery as the physical state evolves.
**Trending because:** 10 HuggingFace upvotes + closed-loop orchestration makes VLA robot skills inspectable and trainable

---

### 5. RISE: Recursive Improvement via Self-Extrapolating Policy Distillation
**Authors:** Yang Li, Semih Yavuz, Shafiq Joty
**arXiv:** [arxiv.org/abs/2609.05295](https://arxiv.org/abs/2609.05295)
**Summary:** On-policy distillation (OPD) provides dense, per-token supervision for language model post-training, but its effectiveness is bottlenecked by teacher quality: external teachers suffer from distribution mismatch, while self-distillation with privileged conditioning is limited by in-context learning capacity. We propose RISE (Recursive Improvement via Self-Extrapolating Policy Distillation), which constructs a synthetic teacher directly from the model's own RLVR training trajectory.
**Trending because:** 9 HuggingFace upvotes + self-generated teachers enable recursive policy improvement

---

### 6. Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning
**Authors:** Yijun Yang, Shenghe Zheng, Wenbo Li, Jianhui Liu, Haoze Sun, Yanbing Zhang, Jiaxiu Jiang, Lin Song, Haoyang Huang, Nan Duan, Lei Zhu
**arXiv:** [arxiv.org/abs/2609.03729](https://arxiv.org/abs/2609.03729)
**Summary:** Despite the remarkable prowess of Vision-Language Models (VLMs) in general multimodal tasks, they remain fundamentally “flat” when reasoning about the physical world. We argue that this spatial bottleneck stems from a profound dimensional mismatch: while VLMs are trained to interpret 2D projections, true spatial reasoning demands the recovery of latent 3D geometry and temporal continuity.
**Trending because:** 8 HuggingFace upvotes + factorized reinforcement learning targets 4D spatial reasoning

---

### 7. τ^τ-Bench: An Environment for End-To-End, Realistic Agent Construction
**Authors:** Quan Shi, Keshav Dhandhania, Karthik Narasimhan, Victor Barres
**arXiv:** [arxiv.org/abs/2609.04611](https://arxiv.org/abs/2609.04611)
**Summary:** LLM agents are rapidly becoming production software, deployed to handle customer service, adjudicate disputes, and operate internal systems. Notably, the work of building them is increasingly handed to coding agents, yet existing benchmarks say little about whether an AI system can deliver one under the conditions of a real client engagement.
**Trending because:** 7 HuggingFace upvotes + a realistic benchmark measures end-to-end production-agent construction

---

### 8. Group Adaptive Clipping Policy Optimization
**Authors:** Sheng Jia, Xiao Wang, Shiva Prasad Kasiviswanathan, Rein Houthooft
**arXiv:** [arxiv.org/abs/2609.00444](https://arxiv.org/abs/2609.00444)
**Summary:** Group relative policy optimization for reinforcement learning with verifiable rewards (RLVR) typically uses a fixed importance-sampling (IS) ratio clipping boundary across all rollouts. We identify a key limitation: rare correct rollouts on harder problems and abundant correct rollouts on easier problems are clipped at comparable rates, despite contributing very different learning signals.
**Trending because:** 7 HuggingFace upvotes + adaptive clipping preserves hard-example RLVR learning signals

---

### 9. When Models Edit Too Much: On the Fidelity of Minimal Code Edits
**Authors:** Tongyao Zhu, Wei Hern Lim, Min-Yen Kan
**arXiv:** [arxiv.org/abs/2609.04061](https://arxiv.org/abs/2609.04061)
**Summary:** Large language models (LLMs) are increasingly used to edit existing code, but correctness alone is not enough: useful repairs should also be minimal, reviewable, and faithful to the original implementation. We study over-editing, the tendency of a model to rewrite code beyond what is required to fix a bug.
**Trending because:** 6 HuggingFace upvotes + code-edit fidelity is measured separately from functional correctness

---

### 10. One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Editing
**Authors:** Adheesh Sunil Juvekar, Onkar Kishor Susladkar, Kiet A. Nguyen, Muntasir Wahed, Nabeel Bashir, Xiaona Zhou, Tianjiao Yu, Vedant Shah, Ismini Lourentzou
**arXiv:** [arxiv.org/abs/2609.04190](https://arxiv.org/abs/2609.04190)
**Summary:** Video editing spans diverse editing paradigms, yet achieving high-quality instruction-guided and subject-guided editing within a single unified framework remains challenging. We introduce EditVid, a training-free framework combining sparse causal memory for local coherence, correspondence-based post-attention token injection for long-range identity preservation, and soft latent blending for edit locality.
**Trending because:** 6 HuggingFace upvotes + training-free editing preserves video identity across diverse edits

---

### 11. To See a World in a Living Context: Unified Indoor-Outdoor Urban World Generation
**Authors:** Xiaobin Huang, Zilong Huang, Yang Luo, Hongchao Fan, Yiping Chen, Ting Han
**arXiv:** [arxiv.org/abs/2608.05879](https://arxiv.org/abs/2608.05879)
**Summary:** Text-driven 3D generation has advanced rapidly in creating large-scale outdoor environments and detailed indoor scenes, but these domains are usually synthesized independently, lacking the correspondence required for a coherent urban world. We present HoloWorld, a unified indoor-outdoor urban world generation framework built on a continuously updated cross-scale world context.
**Trending because:** 6 HuggingFace upvotes + indoor and outdoor generation are unified into coherent 3D cities

---

### 12. Knowing What Not to Answer: Selective Non-Compliance in Vision-Language Models
**Authors:** Minji Kim, Jihyoung Jang, Hyounghun Kim
**arXiv:** [arxiv.org/abs/2609.04720](https://arxiv.org/abs/2609.04720)
**Summary:** Vision-language models (VLMs) are expected to respond helpfully to appropriate requests while withholding compliance with requests that are incorrect, unsafe, infeasible, or unanswerable. However, existing benchmarks predominantly evaluate non-compliance at the level of the query as a whole, assuming that each request either warrants compliance or requires withholding compliance.
**Trending because:** 4 HuggingFace upvotes + selective VLM non-compliance is tested at component level

---

### 13. Refuse without Refusal: A Structural Analysis of Safety-Tuning Responses for Reducing False Refusals in Language Models
**Authors:** Minji Kim, Hyounghun Kim
**arXiv:** [arxiv.org/abs/2609.04714](https://arxiv.org/abs/2609.04714)
**Summary:** Striking a balance between helpfulness and safety remains a fundamental challenge in aligning large language models. To achieve this balance, models should refuse harmful queries (e.g., “How do I shoot someone?”) while remaining responsive to benign inputs, even those superficially resembling harmful queries (e.g., “Where can I shoot a good photo?”).
**Trending because:** 4 HuggingFace upvotes + rationale-only safety tuning reduces false refusals

---

### 14. When Quantization Breaks Memory: Recurrent-State Write-Back in Low-Precision Temporal Inference
**Authors:** Ismail Erbas, Xavier Intes, Vikas Pandey
**arXiv:** [arxiv.org/abs/2609.04490](https://arxiv.org/abs/2609.04490)
**Summary:** Quantization is widely used to reduce the computational and memory demands of neural-network inference. In recurrent networks, however, the quantized state is stored and returned at the next time step, so the rule used to store that state can alter subsequent computations.
**Trending because:** 4 HuggingFace upvotes + low-precision recurrent state storage exposes major memory failures

---

### 15. Training-Free Speech-Centric Omni Understanding with Frozen VLMs
**Authors:** Ankan Deria, Hanoona Rasheed, Xilin He, Fahad Shahbaz Khan, Salman Khan
**arXiv:** [arxiv.org/abs/2609.04242](https://arxiv.org/abs/2609.04242)
**Summary:** Audio-visual understanding remains challenging because models must jointly interpret spoken content, visual events, and their temporal relationships. Existing omni models typically introduce dedicated audio encoders and rely on expensive audio-video-text training, tightly coupling omni capability to specific VLM backbones and potentially weakening their existing visual and reasoning abilities.
**Trending because:** 4 HuggingFace upvotes + frozen VLMs gain multilingual speech understanding without retraining

---

### 16. AdaptVPR: Route-Aware Hard Positive Generation for Robust Visual Place Recognition
**Authors:** Shunpeng Chen, Jingyi Zhang, Changwei Wang, Shengpeng Xu, Yukun Song, Xingtian Pei, Jinzhou Lin, Li Guo, Shibiao Xu
**arXiv:** [arxiv.org/abs/2609.04369](https://arxiv.org/abs/2609.04369)
**Summary:** Visual Place Recognition (VPR) localizes a query image by retrieving database images of the same or nearby place, yet its robustness is often degraded by domain shifts arising from illumination, weather, seasonal changes, and dynamic occlusions. One contributing factor is the limited appearance diversity of the same place in existing training data.
**Trending because:** 4 HuggingFace upvotes + verified hard positives improve visual localization under domain shift

---

### 17. ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding
**Authors:** Jitai Hao, Ke Yang, Qiang Huang, Jun Yu
**arXiv:** [arxiv.org/abs/2609.02780](https://arxiv.org/abs/2609.02780)
**Summary:** Streaming video understanding is a critical capability for real-world applications, including embodied intelligence, autonomous driving, industrial monitoring, surveillance and early warning, and wearable assistants. However, processing continuous video streams with multimodal large language models (MLLMs) is computationally expensive.
**Trending because:** 3 HuggingFace upvotes + shallow-layer indexes sharply reduce streaming-video inference cost

---

### 18. HarvestBench: Measuring Whether LLM Agents Will Pay to Avoid Killing Animals
**Authors:** Jasmine Brazilek, Miles Tidmarsh, Matthias Endres, Anshuman Singh, Jeremiah Miller
**arXiv:** [arxiv.org/abs/2609.04444](https://arxiv.org/abs/2609.04444)
**Summary:** Benchmarks for the side effects an agent causes on the way to a goal already exist, but HarvestBench is the first to put a price on avoiding the side effect and to name that side effect as a living creature. It is a farm simulation: LLM sub-agents drive a crew of two tractors through a cooperative corn harvest, with animals in the field.
**Trending because:** 3 HuggingFace upvotes + a reproducible benchmark quantifies agents' harm-avoidance tradeoffs

---

### 19. Real-World Knowledge-Guided Change Data Synthesis for Remote Sensing
**Authors:** Yaoyi Qi, Xingxing Weng, Chao Pang, Yongkang Cui, Xiangyu Hao, Xiaokang Zhang, Guibo Zhu, Gui-Song Xia
**arXiv:** [arxiv.org/abs/2608.24263](https://arxiv.org/abs/2608.24263)
**Summary:** Change data synthesis provides a cost-effective solution for expanding training data and improving the performance of change detection models. However, existing synthesis methods typically rely on handcrafted rules to simulate changes, where limited coverage of class transitions restricts the diversity of synthesized data, while predefined transition designs limit their flexibility in accommodating varied change types.
**Trending because:** 3 HuggingFace upvotes + vision-language knowledge guides realistic remote-sensing changes

---

### 20. The 2026 PNPL Competition: Word Classification and Efficient Cross-Subject Generalisation in LibriBrain100
**Authors:** Francesco Mantegna, Gereon Elvers, Dulhan Jayalath, Gilad Landau, Tasha Kim, Miran Özdogan, Luisa Kurth, Teyun Kwon, SungJun Cho, Benjamin Ballyk, Alex Fung, Anna Greer, Pratik Somaiya, Christian Herff, Yorguin Mantilla Ramos, Hamza Abdelhedi, Karim Jerbi, Greg Farquhar, Brendan Shillingford, Mark Woolrich, Oiwi Parker Jones
**arXiv:** [arxiv.org/abs/2609.03231](https://arxiv.org/abs/2609.03231)
**Summary:** The ambition of the 2025 PNPL competition (Landau et al., 2025) was to launch a multi-year curriculum for non-invasive speech decoding. Designed to progress from foundational tasks toward the linguistic complexity required for a practical brain-computer interface (BCI), it set the stage with speech detection and phoneme classification tasks.
**Trending because:** 2 HuggingFace upvotes + cross-subject non-invasive speech decoding moves toward practical BCIs

---
