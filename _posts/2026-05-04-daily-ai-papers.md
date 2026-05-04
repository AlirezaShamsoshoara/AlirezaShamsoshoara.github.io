---
title: "Daily AI Papers — May 04, 2026"
date: 2026-05-04
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-04/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - video-generation
  - multi-agent
  - llm-reasoning
---

## 1. UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors

**Authors:** Houyuan Chen, Hong Li, Xianghao Kong, Tianrui Zhu, Shaocong Xu, Weiqing Xiao, Yuwei Guo, Chongjie Ye, Lvmin Zhang, Hao Zhao, Anyi Rao

**Summary:** UniVidX repurposes video diffusion model (VDM) priors for diverse multimodal graphics tasks within a single unified framework, eliminating the need for task-specific models. Three key designs drive it: Stochastic Condition Masking (SCM) for omni-directional conditional generation, Decoupled Gated LoRA (DGL) for modality-specific adaptation, and Cross-Modal Self-Attention (CMSA) for inter-modal alignment. The system achieves SOTA performance on intrinsic video decomposition (albedo, irradiance, normal) and RGBA layer extraction using fewer than 1,000 training videos.

**arXiv:** [arxiv.org/abs/2605.00658](https://arxiv.org/abs/2605.00658)
**Sources:** HuggingFace Daily Papers (#1, 66 upvotes)
**Why trending:** Dominant paper today on HuggingFace; unified multimodal video generation with strong results on minimal data impresses the community.

---

## 2. Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction

**Authors:** Yuxuan Huang, Yihang Chen, Zhiyuan He, Yuxiang Chen, Ka Yiu Lee, Huichi Zhou, Weilin Luo, Meng Fang, Jun Wang

**Summary:** Web2BigTable is a multi-agent framework tackling both broad (structured aggregation across many entities) and deep (complex reasoning over single targets) web search. A bi-level architecture pairs an upper orchestrator with parallel lower-level workers who coordinate via shared workspace and a closed-loop run–verify–reflect process. It reaches an Avg@4 Success Rate of 38.50 on WideSearch — 7.5× the previous best — and 73.0% accuracy on XBench-DeepSearch.

**arXiv:** [arxiv.org/abs/2604.27221](https://arxiv.org/abs/2604.27221)
**Sources:** HuggingFace Daily Papers (#2, 25 upvotes), GitHub
**Why trending:** 7.5× SOTA improvement on WideSearch is an extraordinary gap; multi-agent web extraction is a hot research area.

---

## 3. RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format

**Authors:** Zhehao Huang, Yuhang Liu, Baijiong Lin, Yixin Lou, Zhengbao He, Hanling Tian, Tao Li, Xiaolin Huang

**Summary:** RAIN-Merging closes the gap between large reasoning models (LRMs) that excel at chain-of-thought reasoning but fail at instruction following. It projects instruction-tuned model task vectors onto the null space of forward features at reasoning-critical tokens, preserving structured thinking while adding instruction adherence — all without gradient updates. Evaluated across four instruction-following and nine reasoning benchmarks, gains are consistent across model scales.

**OpenReview:** [openreview.net/forum?id=PO2iULmu5e](https://openreview.net/forum?id=PO2iULmu5e)
**Sources:** ICLR 2026 Oral, papers.cool (#3 trending)
**Why trending:** ICLR 2026 Oral paper; solving instruction-following in reasoning models (o1/R1-style) is a pressing practical challenge.

---

## 4. MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science

**Authors:** Ran Xu, Yuchen Zhuang, Yishan Zhong, Yue Yu, Zifeng Wang, Xiangru Tang, Hang Wu, May Dongmei Wang, Peifeng Ruan, Donghan Yang, Tao Wang, Guanghua Xiao, Xin Liu, Carl Yang, Yang Xie, Wenqi Shi

**Summary:** MedAgentGym provides 72,413 task instances across 129 biomedical categories from 12 real-world scenarios in executable sandbox environments with verifiable ground truth. Med-Copilot trained on it achieves +43.02% from offline RL and +45.28% from online RL, becoming competitive with GPT-4o while remaining privacy-preserving and cost-efficient.

**arXiv:** [arxiv.org/abs/2506.04405](https://arxiv.org/abs/2506.04405)
**Sources:** ICLR 2026 Oral, HuggingFace
**Why trending:** ICLR 2026 Oral; large-scale agentic training environment with dramatic RL gains is a blueprint for other domains.

---

## 5. Map2World: Segment Map Conditioned Text to 3D World Generation

**Authors:** Jaeyoung Chung, Suyoung Lee, Jianfeng Xiang, Jiaolong Yang, Kyoung Mu Lee

**Summary:** Map2World enables user-controlled 3D world generation by conditioning on segment maps of arbitrary shapes and scales, solving the grid-layout and scale-inconsistency problems of prior methods. A supplementary detail enhancer network adds fine-grained visual details without disrupting global scene coherence, leveraging strong priors from asset generators for cross-domain generalization.

**arXiv:** [arxiv.org/abs/2605.00781](https://arxiv.org/abs/2605.00781)
**Sources:** HuggingFace Daily Papers (#3, 11 upvotes)
**Why trending:** Controllable large-scale 3D world generation is critical for game development, autonomous driving simulation, and metaverse applications.

---

## 6. Prox-E: Fine-Grained 3D Shape Editing via Primitive-Based Abstractions

**Authors:** Etai Sella, Hao Phung, Nitay Amiel, Or Litany, Or Patashnik

**Summary:** Prox-E addresses the limitations of 2D-centric 3D editing pipelines — which struggle with structural changes like size, position, and geometry — by representing shapes with primitive-based abstractions. This enables fine-grained, geometrically precise 3D edits that go beyond appearance-only modifications supported by 2D image editing models.

**arXiv:** [arxiv.org/abs/2604.23774](https://arxiv.org/abs/2604.23774)
**Sources:** HuggingFace Daily Papers (#4, 10 upvotes)
**Why trending:** Fine-grained 3D editing without relying on 2D priors addresses a fundamental limitation in the field.

---

## 7. Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies

**Authors:** Yi Wang, Xinchen Li, Pengwei Xie, Pu Yang, Buqing Nie

**Summary:** This work bridges the gap between offline pretraining and real-world robot deployment by enabling generalist robot policies to learn continuously during fleet-scale operation. The framework captures distribution shifts, long-tail failures, task variations, and human corrections as training signals, allowing robots to improve without returning to the lab.

**arXiv:** [arxiv.org/abs/2605.00416](https://arxiv.org/abs/2605.00416)
**Sources:** HuggingFace Daily Papers (#5, 9 upvotes)
**Why trending:** Fleet-scale online RL for robots is a significant step toward self-improving robotic systems; directly relevant to deployment challenges in physical AI.

---

## 8. Let ViT Speak: Generative Language-Image Pre-training (GenLIP)

**Authors:** Yan Fang, Mengcheng Lan, Zilong Huang, Weixian Lei, Yunqing Zhao

**Summary:** GenLIP is a minimalist generative pretraining framework that trains Vision Transformers (ViTs) to generate language tokens directly, aligning them with the autoregressive nature of large language models. This eliminates the mismatch between contrastive vision encoders and autoregressive LLMs in multimodal systems.

**arXiv:** [arxiv.org/abs/2605.00809](https://arxiv.org/abs/2605.00809)
**Sources:** HuggingFace Daily Papers (#6, 9 upvotes)
**Why trending:** Alignment between vision encoders and LLMs is a foundational challenge for MLLMs; a minimalist solution that works well draws attention.

---

## 9. Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance

**Authors:** Minchan Kwon, Sunghyun Baek, Minseo Kim, Jaemyung Yu, Dongyoon Han

**Summary:** Stable-GFlowNet leverages Generative Flow Networks (GFNs) for LLM red-teaming, using Contrastive Trajectory Balance to simultaneously achieve diversity and effectiveness in attack generation. Unlike prior methods that trade off one for the other, this approach finds a broad distribution over effective adversarial prompts.

**arXiv:** [arxiv.org/abs/2605.00553](https://arxiv.org/abs/2605.00553)
**Sources:** HuggingFace Daily Papers (#7, 9 upvotes)
**Why trending:** LLM safety and automated red-teaming remain top priorities; GFN-based approach offers a theoretically grounded diversity guarantee.

---

## 10. From Skill Text to Skill Structure: The Scheduling-Structural-Logical Representation for Agent Skills

**Authors:** Qiliang Liang, Hansi Wang, Zhong Liang, Yang Liu

**Summary:** This paper introduces the Scheduling-Structural-Logical (SSL) representation for agent skills, moving beyond text-heavy SKILL.md-style artifacts. SSL explicitly encodes scheduling dependencies, structural control flow, logical constraints, and tool calls in a machine-readable format that enables more reliable agent execution.

**arXiv:** [arxiv.org/abs/2604.24026](https://arxiv.org/abs/2604.24026)
**Sources:** HuggingFace Daily Papers (#8, 8 upvotes)
**Why trending:** As agentic AI systems proliferate, principled skill representation is becoming a critical infrastructure problem.

---

## 11. When Do Diffusion Models Learn to Generate Multiple Objects?

**Authors:** Yujin Jeong, Arnas Uselis, Iro Laina, Seong Joon Oh, Anna Rohrbach

**Summary:** This work rigorously investigates why text-to-image diffusion models fail at multi-object generation despite strong single-object fidelity. By disentangling data-level from model-level causes, the authors identify when multi-object learning emerges during training and what data conditions are necessary.

**arXiv:** [arxiv.org/abs/2605.00273](https://arxiv.org/abs/2605.00273)
**Sources:** HuggingFace Daily Papers (#9, 4 upvotes)
**Why trending:** Multi-object generation failure is a persistent and well-known problem; rigorous causal analysis advances understanding beyond empirical workarounds.

---

## 12. Trees to Flows and Back: Unifying Decision Trees and Diffusion Models

**Authors:** Sai Niranjan Ramachandran, Suvrit Sra

**Summary:** This paper establishes a crisp mathematical correspondence between hierarchical decision trees (discrete, hierarchical) and diffusion processes (continuous, dynamic) in appropriate limiting regimes. The unification provides theoretical tools that flow bidirectionally — insights from diffusion theory illuminate tree structure and vice versa.

**arXiv:** [arxiv.org/abs/2605.00414](https://arxiv.org/abs/2605.00414)
**Sources:** HuggingFace Daily Papers (#10, 3 upvotes)
**Why trending:** Novel theoretical unification of two foundational model classes; opens new avenues for interpretable generative modeling.

---

## 13. End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer

**Authors:** Wenda Chu, Bingliang Zhang, Jiaqi Han, Yizhuo Li, Linjie Yang

**Summary:** This paper introduces an end-to-end training pipeline that jointly optimizes the visual tokenizer and the autoregressive image generator, enabling direct supervision from generation losses to flow back to the tokenizer. This contrasts with the standard two-stage approach where tokenizer and generator are trained independently.

**arXiv:** [arxiv.org/abs/2605.00503](https://arxiv.org/abs/2605.00503)
**Sources:** HuggingFace Daily Papers (#11, 2 upvotes)
**Why trending:** End-to-end optimization of tokenizer+generator is a natural next step for autoregressive image generation; simplifies the training pipeline.

---

## 14. Online Self-Calibration Against Hallucination in Vision-Language Models

**Authors:** Minghui Chen, Chenxu Yang, Hengjie Zhu, Dayan Wu, Zheng Lin

**Summary:** This paper proposes an online calibration mechanism for Large Vision-Language Models (LVLMs) that detects and reduces hallucinations without depending on stronger teacher models like GPT. The self-supervised online approach avoids the limitations of offline preference alignment and adapts to new inputs at inference time.

**arXiv:** [arxiv.org/abs/2605.00323](https://arxiv.org/abs/2605.00323)
**Sources:** HuggingFace Daily Papers (#12, 1 upvote)
**Why trending:** LVLM hallucination is a critical deployment problem; teacher-free self-calibration is more practical and scalable than distillation-based approaches.

---

## 15. Themis: Training Robust Multilingual Code Reward Models for Flexible Multi-Criteria Scoring

**Authors:** Indraneil Paul, Glavaš Glavas, Iryna Gurevych

**Summary:** Themis fills the gap in reward model research for code generation, where most work relies solely on execution-based feedback. The framework trains multilingual code reward models that support flexible multi-criteria scoring (correctness, style, efficiency) across diverse programming languages.

**arXiv:** [arxiv.org/abs/2605.00754](https://arxiv.org/abs/2605.00754)
**Sources:** HuggingFace Daily Papers (#14, 1 upvote)
**Why trending:** Code reward models are increasingly important for RLHF in coding assistants; multilingual support and multi-criteria scoring address real deployment needs.

---

## 16. Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling

**Authors:** Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang

**Summary:** Talker-T2AV introduces a two-stage autoregressive diffusion process that first generates semantic tokens for cross-modal coherence and then generates low-level audio-visual details separately. This decoupling avoids the over-entangled modality coupling of pervasive cross-attention in prior joint generation models.

**arXiv:** [arxiv.org/abs/2604.23586](https://arxiv.org/abs/2604.23586)
**Sources:** HuggingFace Daily Papers (#16, 1 upvote)
**Why trending:** Joint audio-video generation is commercially valuable for digital humans, dubbing, and avatar synthesis; the two-stage decoupling is architecturally elegant.

---

## 17. Learning to Act and Cooperate for Distributed Black-Box Consensus Optimization

**Authors:** Zi-Bo Qin, Feng-Feng Wei, Tai-You Chen, Wei-Neng Chen

**Summary:** This work replaces handcrafted update rules in distributed black-box consensus optimization with learned policies that dynamically adapt cooperation patterns among agents. Using only local objective queries and limited neighbor communication, the learned agents outperform static rule-based methods on diverse multi-agent optimization problems.

**arXiv:** [arxiv.org/abs/2605.00691](https://arxiv.org/abs/2605.00691)
**Sources:** HuggingFace Daily Papers (#13, 1 upvote)
**Why trending:** Learned optimization for multi-agent systems is relevant to decentralized AI training and distributed infrastructure.

---

## 18. Better Models, Faster Training: Sigmoid Attention for Single-Cell Foundation Models

**Authors:** Vijay Sadashivaiah, Georgios Dasoulas, Judith Mueller, Soumya Ghosh

**Summary:** This paper demonstrates that sigmoid attention is a drop-in replacement for softmax attention in single-cell foundation models, achieving 25% higher cell-type separation across six diverse single-cell datasets with faster convergence. The improvement is attributed to sigmoid attention's ability to handle sparse biological expression patterns more effectively.

**arXiv:** [arxiv.org/abs/2604.27124](https://arxiv.org/abs/2604.27124)
**Sources:** HuggingFace Daily Papers (#18)
**Why trending:** Simple architectural swap with substantial gains in computational biology; relevant to the growing intersection of foundation models and life sciences.

---

## 19. AnalogRetriever: Learning Cross-Modal Representations for Analog Circuit Retrieval

**Authors:** Yihan Wang, Lei Li, Yao Lai, Jing Wang, Yan Lu

**Summary:** AnalogRetriever introduces cross-modal representation learning to enable retrieval across heterogeneous analog circuit representations — SPICE netlists, schematics, and functional descriptions — which were previously only searchable within a single modality. The approach enables effective IP reuse in analog circuit design workflows.

**arXiv:** [arxiv.org/abs/2604.23195](https://arxiv.org/abs/2604.23195)
**Sources:** HuggingFace Daily Papers (#17, 1 upvote)
**Why trending:** EDA (Electronic Design Automation) is increasingly adopting ML; cross-modal retrieval for circuit design is a novel application domain.

---

## 20. LASE: Language-Adversarial Speaker Encoding for Indic Cross-Script Identity Preservation

**Authors:** Venkata Pushpak Teja Menta

**Summary:** LASE trains speaker encoders adversarially to be invariant to script and accent while preserving speaker identity, enabling consistent voice cloning across English, Hindi, Telugu, and Tamil. The adversarial objective explicitly penalizes language-dependent features in the speaker embedding space.

**arXiv:** [arxiv.org/abs/2605.00777](https://arxiv.org/abs/2605.00777)
**Sources:** HuggingFace Daily Papers (#15, 1 upvote)
**Why trending:** Multilingual voice cloning for Indic languages is underserved; adversarial speaker encoding for cross-script identity is a practical and technically interesting solution.
