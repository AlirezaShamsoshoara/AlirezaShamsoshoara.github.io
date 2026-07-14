---
title: "Daily AI Papers — July 14, 2026"
date: 2026-07-14
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-14/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - weak-to-strong-distillation
  - embodied-ai
  - world-models
---

## 1. Weak-to-Strong Generalization via Direct On-Policy Distillation

**Authors:** Shiyuan Feng, Huan-ang Gao, Haohan Chi, Hanlin Wu, Zhilong Zhang, Zheng Jiang, Bingxiang He, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou  
**arXiv:** [arxiv.org/abs/2607.05394](https://arxiv.org/abs/2607.05394)

Proposes Direct-OPD, which reuses the policy shift an RL run induces in a small "teacher" model as a dense implicit reward signal, transferring it to a stronger "student" model instead of running expensive RL rollouts on the big model directly. It boosts Qwen3-1.7B from 48.3% to 58.3% on AIME 2024 in just 4 hours on 8 A100 GPUs, outperforming step-matched direct RL.

**Sources:** HuggingFace Daily Papers (88 upvotes) · arXiv  
**Why trending:** Top-upvoted paper of the day on HF; offers a cheap way to scale RLVR post-training gains to larger models without expensive rollouts, a widely-discussed bottleneck.

---

## 2. ABot-N1: Toward a General Visual Language Navigation Foundation Model

**Authors:** Ruiyan Gong, Yingnan Guo, Junjun Hu, Jintao Kong, Xiaoxu Leng, Tianlun Li, and 34 others  
**arXiv:** [arxiv.org/abs/2607.10383](https://arxiv.org/abs/2607.10383)

Decouples "slow" chain-of-thought vision-language reasoning from a "fast" action expert that turns pixel-space goals into continuous navigation waypoints, unifying point-goal, object-goal, instruction-following, and person-following tasks. It sets new state-of-the-art urban-scale navigation results, lifting POI arrival rate by 35 points to 77.3% and reaching 95%+ success in complex indoor/outdoor scenes.

**Sources:** HuggingFace Daily Papers (78 upvotes) · arXiv  
**Why trending:** Second-highest HF upvotes; part of a large coordinated "ABot" foundation-model suite release (alongside AgentOS and 3DWorld, below) drawing significant embodied-AI attention.

---

## 3. ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory

**Authors:** Jiayi Tian, Shiao Liu, Yuting Xu, Jia Lu, Zihao Guan, and 24 others  
**arXiv:** [arxiv.org/abs/2607.10350](https://arxiv.org/abs/2607.10350)

Proposes an "Agent OS" runtime layer above low-level robot controllers that handles scene-conditioned planning, tool use, multi-stage verification, and a persistent Universal Multi-modal Graph Memory across long-horizon tasks. A failure-driven self-evolution loop converts diagnosed memory failures into reusable runtime improvements, boosting scores on LoCoMo, OpenEQA, and Mem-Gallery benchmarks.

**Sources:** HuggingFace Daily Papers (66 upvotes) · arXiv  
**Why trending:** Companion release to ABot-N1; strong upvotes reflect interest in "operating system"-style abstractions for embodied agents.

---

## 4. ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space

**Authors:** Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, and 31 others  
**arXiv:** [arxiv.org/abs/2607.11673](https://arxiv.org/abs/2607.11673)

Presents a universal 3D world model that lifts text, image, or video into a compact "Spatial Generative Primitive" (a panorama plus a spatial point cloud), then generates a 3D-consistent panoramic video and reconstructs it into an explorable 3D Gaussian Splatting world. It claims state-of-the-art results among open-source methods and stronger scene fidelity than Marble on rich multimodal inputs.

**Sources:** arXiv (fresh submission; same-day companion to ABot-N1/AgentOS, not yet on HF Daily Papers)  
**Why trending:** Third paper in the same-day "ABot" foundation-model suite release, riding the wave of attention on the other two highly-upvoted ABot papers.

---

## 5. 4D Human-Scene Reconstruction from Low-Overlap Captures (StudioRecon)

**Authors:** Minhyuk Hwang, Sangmin Kim, Seunguk Do, Daneul Kim, Jaesik Park  
**arXiv:** [arxiv.org/abs/2607.09125](https://arxiv.org/abs/2607.09125)

StudioRecon reconstructs dynamic 4D human scenes from sparse, low-overlap camera rigs by decoupling background from humans, using a video diffusion model to densify background views and deformable Gaussians with cross-view keypoint fitting for people. It achieves state-of-the-art novel-view synthesis on four real-world datasets and enables applications like novel trajectory rendering and human replacement.

**Sources:** HuggingFace Daily Papers (40 upvotes) · arXiv  
**Why trending:** High upvotes reflect interest in making high-fidelity volumetric capture practical with cheap, sparse camera rigs instead of dense studio arrays.

---

## 6. LightMem-Ego: Your AI Memory for Everyday Life

**Authors:** Yijun Chen, Boyi Xiao, Yixian Zhao, Haoting Xia, Buqiang Xu, and 8 others  
**arXiv:** [arxiv.org/abs/2607.11487](https://arxiv.org/abs/2607.11487)

A lightweight streaming multimodal memory system for wearables/smartphones that continuously captures egocentric audio/video, aligns it on a shared timeline, and organizes it into current/short-term/long-term memory tiers for query answering. It supports object finding, conversation recall, life summarization, and routine discovery, and is open-sourced for smartphone and AI-glasses deployment.

**Sources:** HuggingFace Daily Papers (32 upvotes) · arXiv · GitHub (code release)  
**Why trending:** Directly relevant to the fast-growing "AI glasses" wearable-memory product category; the open-source release adds to its visibility.

---

## 7. AdvancedMathBench: A Benchmark Suite for Advanced Mathematical Proof Generation and Verification

**Authors:** Lingkai Kong, Zijian Wu, Yuzhe Gu, Haiteng Zhao, Wenyong Huang, and 8 others  
**arXiv:** [arxiv.org/abs/2607.11849](https://arxiv.org/abs/2607.11849)

Introduces a benchmark suite for advanced (undergraduate/doctoral-qualifying-exam-level) mathematical proof generation and verification, including ProverBench (296 problems) and an automatic verification pipeline trained on large-scale expert annotations. Even the best model, GPT-5.5-xhigh, scores only 75.8/66.1 on proof generation and 65.1 balanced-F1 on proof verification, showing substantial headroom remains.

**Sources:** HuggingFace Daily Papers (18 upvotes) · arXiv  
**Why trending:** Benchmarks that expose frontier-model math-reasoning limits consistently draw strong community engagement.

---

## 8. Metacognition in LLMs: Foundations, Progress, and Opportunities

**Authors:** Gabrielle Kaili-May Liu, Areeb Gani, Jacqueline Lu, Jordan Thomas, Mark Steyvers, Arman Cohan  
**arXiv:** [arxiv.org/abs/2607.11881](https://arxiv.org/abs/2607.11881)

A comprehensive survey taxonomizing the emerging field of LLM metacognition, covering methods and benchmarks for measuring metacognitive ability, techniques to elicit and improve it, and open research questions. The authors maintain a companion GitHub reading list to track the fast-growing literature.

**Sources:** HuggingFace Daily Papers (12 upvotes) · arXiv · GitHub (paper list)  
**Why trending:** Timely survey on a topic (LLM self-awareness and confidence calibration) increasingly tied to reliability and safety discussions.

---

## 9. Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias

**Authors:** Zixiang Xu, Sixian Li, Huaxing Liu, Xiang Wang, Shuai Li, Zirui Song, Xiuying Chen  
**arXiv:** [arxiv.org/abs/2607.11871](https://arxiv.org/abs/2607.11871)

Studies LLM-as-judge scoring bias at the representation level rather than the usual input-output level, finding that biased judging inputs are displaced along a low-dimensional, bias-type-specific subspace in the judge's hidden states. The team shows this subspace can be causally steered to induce or remove bias, and that a simple linear projection onto it predicts judge failures on unseen benchmarks.

**Sources:** arXiv (fresh submission; not yet on HF Daily Papers)  
**Why trending:** LLM-as-judge reliability is a hot topic given how widely judges are used for evals and RLHF, and the mechanistic framing offers actionable bias-detection tools.

---

## 10. EgoSteer: A Full-Stack System Towards Steerable Dexterous Manipulation from Egocentric Videos

**Authors:** Yifan Zhong, Zhang Chen, Tianrui Guan, Fanlian Zeng, Yuyao Ye, and 11 others  
**arXiv:** [arxiv.org/abs/2607.09701](https://arxiv.org/abs/2607.09701)

A full-stack system that pre-trains a vision-language-action model on 9.6K hours of curated egocentric human video, then fine-tunes it on real robots with human-in-the-loop correction. EgoSteer robustly executes free-form instructions across 40+ diverse tasks and few-shot adapts to long-horizon tasks like box folding with 75%+ success.

**Sources:** HuggingFace Daily Papers (8 upvotes) · arXiv · GitHub (open-source release)  
**Why trending:** Large-scale egocentric-video pretraining for dexterous manipulation is a hot direction in embodied AI and robotics research.

---

## 11. Proxy Exploration and Reusable Guidance: A Modular LLM Post-Training Paradigm via Proxy-Guided Update Signals

**Authors:** Daocheng Fu, Rong Wu, Yu Yang, Xuemeng Yang, Jianbiao Mei, Licheng Wen, Pinlong Cai, Yong Liu, Botian Shi, Yu Qiao  
**arXiv:** [arxiv.org/abs/2607.11505](https://arxiv.org/abs/2607.11505)

PUST decouples policy exploration from distribution alignment in LLM post-training by having a lightweight proxy model discover high-reward behaviors, then transferring the proxy's relative pre/post-RL improvement as a reusable update signal to a stronger primary model. This enables weak-to-strong post-training gains that can be asynchronously generated, cached, and reused across models.

**Sources:** HuggingFace Daily Papers (7 upvotes) · arXiv  
**Why trending:** Echoes the same weak-to-strong distillation theme as today's #1 paper, suggesting a broader trend toward decoupling costly RL exploration from target-model training.

---

## 12. NeuroCogMap Reveals Cognitive Organization of Large Language Models

**Authors:** Zhongxiang Sun, Haolang Lu, Qiang Ma, Qi Li, Qipeng Wang, and 9 others  
**arXiv:** [arxiv.org/abs/2607.00397](https://arxiv.org/abs/2607.00397)

Proposes a cognitive-neuroscience-inspired framework that maps LLM internal features into functional "parcels" linked to interpretable cognitive capabilities, showing these parcels are stable across models and correspond to failure modes like hallucination, bias, and sycophancy. The framework also improves prediction of human cortical responses during language comprehension, tying LLM internals to biological cognition.

**Sources:** HuggingFace Daily Papers (5 upvotes) · arXiv  
**Why trending:** Bridges interpretability and cognitive neuroscience, appealing to both AI-safety and neuroscience audiences.

---

## 13. Latent-Identity Tuning in Text-to-Image Personalization Models

**Authors:** Daniel Garibi, Ronen Kamenetsky, Hadar Averbuch-Elor, Daniel Cohen-Or, Or Patashnik  
**arXiv:** [arxiv.org/abs/2607.11885](https://arxiv.org/abs/2607.11885)

Explores the latent space of a frozen, pre-trained text-to-image personalization encoder to enable fine-grained, training-free facial identity edits, identifying latent directions tied to specific facial regions and semantics. This allows localized, semantically coherent edits while preserving overall identity consistency across generated images.

**Sources:** HuggingFace Daily Papers (3 upvotes) · arXiv  
**Why trending:** Precision identity editing is a persistent pain point in personalized image generation, and the training-free approach lowers the barrier to adoption.

---

## 14. Motion4Motion: Motion Transfer Across Subjects at Inference

**Authors:** Ling-Hao Chen, Zixin Yin, Duomin Wang, Xianfang Zeng, Gang Yu  
**arXiv:** [arxiv.org/abs/2607.11644](https://arxiv.org/abs/2607.11644)

A training-free framework for cross-species/cross-character motion transfer that models a video's motion flow directly instead of relying on a predefined skeleton, letting motion transfer between very different characters (e.g., humans to animals). It outperforms skeleton-based baselines and generalizes to diverse characters without extra labeled training data.

**Sources:** HuggingFace Daily Papers (3 upvotes) · arXiv  
**Why trending:** Removes a long-standing skeleton-data bottleneck in animation and motion-transfer pipelines, appealing to digital-content-creation audiences.

---

## 15. CtrlVTON: Controllable Virtual Try-On via Visual-Instance-Prompt Segmentation

**Authors:** Seungyong Lee, Hyun Jun Jang, Sangoh Kim, Sungjoon Park  
**arXiv:** [arxiv.org/abs/2607.09362](https://arxiv.org/abs/2607.09362)

Introduces VIP-SAM for instance-level garment segmentation from a flatlay reference, and CtrlVTON, a controllable virtual try-on framework that uses segmentation masks as pixel-level control over garment size, style, and placement. It generates try-on images that follow user-provided layouts more faithfully than the strongest proprietary editing systems while matching them on garment fidelity.

**Sources:** HuggingFace Daily Papers (3 upvotes) · arXiv  
**Why trending:** Virtual try-on has strong commercial (e-commerce) relevance, and beating proprietary systems on controllability draws attention.

---

## 16. Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model

**Authors:** Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, and 19 others  
**arXiv:** [arxiv.org/abs/2607.11643](https://arxiv.org/abs/2607.11643)

A 38-billion-parameter multimodal autoregressive "world foundation model" from Xiaomi that jointly handles text-to-image generation, image editing, and embodied scene/video generation and transfer for robotics, preserving pre-trained visual knowledge while adapting to embodied settings. It outperforms GPT-Image-2.0 on embodied scene generation and transfer in human evaluations, and boosts a real-world manipulation policy's out-of-distribution success rate from 36.9% to 63.2%.

**Sources:** HuggingFace Daily Papers (2 upvotes) · arXiv  
**Why trending:** A major consumer-electronics company (Xiaomi) entering large-scale embodied foundation models draws industry attention.

---

## 17. MET: Theory-Grounded and Culture-Aware Multilingual Moral Reasoning

**Authors:** Ayoung Lee, Ryan Kwon, Yunxiang Zhang, Yuxuan Liu, Peter Railton, Lu Wang  
**arXiv:** [arxiv.org/abs/2607.11736](https://arxiv.org/abs/2607.11736)

Proposes MET, a theory-grounded, two-step prompting method for multilingual moral reasoning that has models select culture-specific ethical grounds (from psychology and philosophy) before reasoning in the user's native language, plus MET-D, a self-distillation variant needing no external supervision. It improves macro-F1 by several points across model sizes and families, and substantially increases native-language reasoning.

**Sources:** HuggingFace Daily Papers (2 upvotes) · arXiv  
**Why trending:** Addresses growing concern about English-centric bias in LLM moral/ethical reasoning as models are deployed globally.

---

## 18. LATO.2: Factorized 3D Mesh Generation with Vertex and Topology Flow

**Authors:** Hang Long, Tianhao Zhao, Junkai Lin, Youjia Zhang, Huipeng Guo, and 5 others  
**arXiv:** [arxiv.org/abs/2607.10623](https://arxiv.org/abs/2607.10623)

LATO.2 factorizes 3D mesh generation into a vertex flow followed by a connectivity flow conditioned on the realized vertices, both anchored to a shared voxel scaffold, avoiding the drifting vertices and broken surfaces common in joint vertex/topology latent models. This factorization enables higher-resolution part-wise mesh generation and topology-adaptive editing without re-optimization.

**Sources:** HuggingFace Daily Papers (2 upvotes) · arXiv  
**Why trending:** Improves practical 3D-asset generation quality and editability, a widely-watched area for game, VFX, and 3D-content pipelines.

---

## 19. From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence

**Authors:** Yuanzhi Liang, Xufeng Zhan, Haibin Huang, Chi Zhang, Xuelong Li  
**arXiv:** [arxiv.org/abs/2607.11689](https://arxiv.org/abs/2607.11689)

A roadmap paper reviewing the fragmented landscape of World Action Models and proposing an "embodied brain" target architecture that unifies multimodal context, intervention comparison, and closed-loop post-training into a modular physical-intelligence stack. It aims to standardize action spaces, datasets, and system interfaces across the embodied-AI field.

**Sources:** arXiv (fresh submission; not yet on HF Daily Papers)  
**Why trending:** High-profile senior author (Xuelong Li) and a unifying framework for the fast-fragmenting embodied-AI/world-model space typically attract strong readership.

---

## 20. A Theory of Contrastive Learning with Natural Images

**Authors:** Antonio Torralba, Yair Weiss  
**arXiv:** [arxiv.org/abs/2607.07470](https://arxiv.org/abs/2607.07470)

Analytically derives the optimal representation for contrastive learning under simple augmentations, showing it is realized by a CNN whose first-layer filters are sinusoids, followed by a pointwise nonlinearity, global average pooling, and partial whitening. The authors confirm empirically that CNNs trained with SGD on real image datasets do learn sinusoidal first-layer filters and partial whitening, matching the theory.

**Sources:** HuggingFace Daily Papers (1 upvote) · arXiv  
**Why trending:** A rare, fully analytical theory explaining *why* contrastive learning works, from well-known vision researchers (MIT's Torralba), appeals to the theory-hungry ML community despite modest upvotes so far.
