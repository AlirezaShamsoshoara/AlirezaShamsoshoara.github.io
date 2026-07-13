---
title: "Daily AI Papers — July 12, 2026"
date: 2026-07-12
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-12/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - robotics
  - medical-imaging
  - agent-safety
---

## 1. Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models

**Authors:** Hongyu Li, Wanjia Fu, Xiaoyan Cong, Zekun Li, Binghao Huang, Hanxiao Jiang, et al.  
**arXiv:** [arxiv.org/abs/2607.05390](https://arxiv.org/abs/2607.05390)  
**Sources:** HuggingFace Daily Papers (9 upvotes, 2 comments — top score of the cycle).  
**Why Trending:** Leading engagement on HF this cycle; addresses a real gap in robotics world-modeling by systematically comparing 2D-pixel vs 3D-geometric approaches to deformable-object dynamics, backed by a large new multi-view visuotactile dataset.

Deform360 introduces a massive multi-view visuotactile dataset for studying deformable-object dynamics, a notoriously hard case for robotic world models due to high-dimensional state spaces and complex material behavior. The authors use it to systematically compare 2D pixel-space and 3D geometric world-modeling paradigms, clarifying their relative strengths for manipulation.

---

## 2. PraMem: Practice-derived Experiential Memory for Long-horizon Behavior Prediction

**Authors:** Zhuoqun Li, Boxi Cao, Jiawei Chen, Hanshu Zhou, Ruoxi Xu, Guiping Jiang, et al.  
**arXiv:** [arxiv.org/abs/2607.02881](https://arxiv.org/abs/2607.02881)  
**Sources:** HuggingFace Daily Papers (9 upvotes, 2 comments).  
**Why Trending:** Tied for top HF engagement this cycle; tackles a core weakness of LLM-based behavior prediction — memory that compresses context but loses the latent behavioral patterns needed for long-horizon inference.

PraMem proposes a practice-derived experiential memory mechanism for predicting a user's next action from long historical sequences, moving beyond the context-compression paradigm used by prior memory-management methods. The approach targets LLMs' struggles with latent behavioral-pattern induction and intrinsic cognitive biases on long-horizon prediction tasks.

---

## 3. Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability Reproduction

**Authors:** Mingzhe Du, Luu Anh Tuan, Tianyi Wu, Renyang Liu, Zhijiang Guo, Dong Huang, et al.  
**arXiv:** [arxiv.org/abs/2607.01764](https://arxiv.org/abs/2607.01764)  
**Sources:** HuggingFace Daily Papers (8 upvotes, 2 comments).  
**Why Trending:** Strong HF pickup for reframing agentic vulnerability reproduction around strategy learning rather than full action-trajectory imitation — relevant to the fast-growing "LLM agents for security" niche.

Mastermind targets repository-scale vulnerability reproduction, where an agent must inspect a codebase, infer the input grammar reaching a vulnerable path, build a proof-of-concept, and confirm the crash disappears post-patch. The paper argues that learning the right high-level strategy — not the entire action trajectory — is what separates agents that succeed from those that fail despite a sound approach.

---

## 4. CONFLUX: A Latent Diffusion Model for 3D Chest-CT Synthesis with RL Post-Training

**Authors:** Max Van Puyvelde, Halil Ibrahim Gulluk, Wim Van Criekinge, Olivier Gevaert  
**arXiv:** [arxiv.org/abs/2607.02998](https://arxiv.org/abs/2607.02998)  
**Sources:** HuggingFace Daily Papers (6 upvotes, 4 comments — highest comment count in the cycle).  
**Why Trending:** Drew the most discussion (relative to upvotes) on HF; a natively-3D latent diffusion model for chest CT that stays faithful to structured clinical conditioning, refined with RL post-training.

CONFLUX is a latent diffusion model for controllable 3D chest CT synthesis, using a 3D variational autoencoder to compress volumes and a rectified-flow transformer to generate in the latent space. Generation is conditioned on 18 structured radiological attributes, and the model is further refined with reinforcement-learning post-training for clinical fidelity.

---

## 5. AI Wizards at EXIST 2026: Hierarchical Soft-Label Learning for Multimodal Sexism Identification in Memes

**Authors:** Matteo Fasulo, Antonio Gravina, Luca Tedeschini, Luca Babboni  
**arXiv:** [arxiv.org/abs/2607.04410](https://arxiv.org/abs/2607.04410)  
**Sources:** HuggingFace Daily Papers (7 upvotes, 2 comments).  
**Why Trending:** Competition-winning shared-task submission (ranked 1st on Task 2.3) drawing attention for its lightweight architecture — a Gated MLP on frozen Gemini vision-language embeddings beating heavier pipelines.

This is the AI Wizards team's submission to EXIST 2026 for multimodal sexism identification in memes, modeling the task's three increasingly hard subtasks as hierarchical conditional soft-label prediction over empirical annotator distributions. Mapping fixed Gemini Embedding 2 representations through a lightweight Gated MLP trained with KL divergence and uncertainty weighting, the system ranked first on Task 2.3 and fourth across other subtasks.

---

## 6. Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification

**Authors:** Yunhao Feng, Ruixiao Lin, Ming Wen, Qinqin He, Yanming Guo, Yifan Ding, et al.  
**arXiv:** [arxiv.org/abs/2607.01793](https://arxiv.org/abs/2607.01793)  
**Sources:** HuggingFace Daily Papers (7 upvotes, 2 comments).  
**Why Trending:** Feeds directly into the ongoing agent-safety debate — proposes automated, evolvable safety testing for LLM agents in place of costly expert-designed violation sets and hard-coded evaluation rules.

The paper presents Vera, an end-to-end automated safety-testing framework for LLM agents that adapts software-engineering testing principles to non-deterministic agents through a three-stage pipeline. It moves safety evaluation away from static, expert-authored violation sets toward evidence-grounded verification that can scale as agents evolve.

---

## 7. GORGO: Online Tuning for Cross-Region Network-Aware LLM Serving

**Authors:** Alessio Ricci Toniolo, Rome Thorstenson, Abinaya Dinesh  
**arXiv:** [arxiv.org/abs/2602.11688](https://arxiv.org/abs/2602.11688)  
**Sources:** HuggingFace Daily Papers (7 upvotes, 2 comments).  
**Why Trending:** Relevant to every lab running globally distributed inference — addresses uneven load and KV-cache concentration caused by load balancers that ignore network latency between regions.

GORGO is a proxy architecture for LLM inference serving that jointly optimizes KV-cache locality, replica load, and cross-region network latency, factors existing systems typically consider only in part. By holistically modeling these costs, it reduces the uneven load and cache concentration that hurt latency and time-to-first-token in globally distributed deployments.

---

## 8. Transition-Aware best-of-N sampling for Longitudinal Chest X-ray Reports

**Authors:** Halil Ibrahim Gulluk, Max Van Puyvelde, Wim Van Criekinge, Olivier Gevaert  
**arXiv:** [arxiv.org/abs/2606.28393](https://arxiv.org/abs/2606.28393)  
**Sources:** HuggingFace Daily Papers (6 upvotes, 2 comments).  
**Why Trending:** First training-free best-of-N scheme aware of longitudinal clinical context, addressing a documented blind spot in chest X-ray report generation — most systems ignore how a report should describe change from a prior exam.

The paper introduces a training-free best-of-N sampling scheme for pretrained chest X-ray report generators that is explicitly aware of the transition between a patient's prior exam and the current one. Reports are split into sentences and embedded so the sampling process can select candidates that best reflect genuine longitudinal change rather than treating each exam in isolation.

---

## 9. MuseBench: Benchmarking Intent-Level Audiovisual Arts Understanding in MLLMs

**Authors:** Yuxuan Fan, Gyusik Seo, Jing Hao, Jaemin Cho, Mohit Bansal, Jaehong Yoon  
**arXiv:** [arxiv.org/abs/2606.30026](https://arxiv.org/abs/2606.30026)  
**Sources:** HuggingFace Daily Papers (6 upvotes, 2 comments).  
**Why Trending:** Pushes multimodal LLM evaluation past surface-level description toward artistic intent — reasoning about *why* a creative choice (framing, silence, close-ups) produces a specific emotional effect.

MuseBench is a benchmark for evaluating whether multimodal LLMs understand audiovisual art at the level of intent — reasoning about why particular creative choices (e.g., claustrophobic framing to amplify fear) produce their effect, not just recognizing what is depicted. It spans cinema, visual arts, stage performance, and game design to probe this deeper artistic reasoning.

---

## 10. ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation

**Authors:** Kaifeng Zhao, Mathis Petrovich, Haotian Zhang, Tingwu Wang, Siyu Tang, Davis Rempe  
**arXiv:** [arxiv.org/abs/2607.08741](https://arxiv.org/abs/2607.08741)  
**Sources:** HuggingFace Daily Papers (6 upvotes, 1 comment).  
**Why Trending:** Targets the classic speed-vs-controllability tradeoff in human motion generation, aiming for real-time synthesis without giving up the text-driven control that offline methods offer.

ARDY combines autoregressive diffusion with a hybrid motion representation to generate realistic 3D human motion in real time for interactive applications like animation and humanoid robotics. It aims to close the gap between offline methods, which offer precise text- and kinematic-based control but are too slow for interactive use, and online methods, which are fast but struggle with complex language and long-horizon goals.

---

## 11. SIEVE: Structure-Aware Data Selection for Imitation Learning with VLA Models

**Authors:** Changti Wu, Bin Yu, Zhaolong Shen, Shijie Lian, Xiaopeng Lin, Cong Huang, et al.  
**arXiv:** [arxiv.org/abs/2607.06442](https://arxiv.org/abs/2607.06442)  
**Sources:** HuggingFace Daily Papers (5 upvotes, 2 comments).  
**Why Trending:** Speaks to a growing concern in robot learning — that scaling VLA training data isn't enough when it's redundant or noisy — by selecting for reusable sub-behavior structure instead of just trajectory- or state-level quality.

SIEVE is a structure-aware data selection method for training Vision-Language-Action models via imitation learning, targeting the reusable sub-structures that compose long-horizon behaviors. Unlike prior selection methods that score demonstrations at the trajectory or state-action level, SIEVE aims to reduce redundancy and noise while preserving the building blocks policies need to generalize.

---

## 12. Bibby AI: An Editor-Native Agentic Platform for Academic Research, Writing, and Publishing

**Authors:** Nilesh Jain  
**arXiv:** [arxiv.org/abs/2607.05435](https://arxiv.org/abs/2607.05435)  
**Sources:** HuggingFace Daily Papers (5 upvotes, 2 comments).  
**Why Trending:** An "agentic platform" pitch for academia itself — collapsing literature discovery, reference management, LaTeX writing, formatting, and submission into one editor-native tool, cutting the tool-switching tax researchers pay.

Bibby AI is proposed as an editor-native agentic platform that unifies the fragmented academic writing toolchain — literature discovery, reference management, LaTeX drafting, venue formatting, and submission — into a single workflow. The goal is to eliminate the context switches and manual conversions that currently consume researcher time outside of actual research.

---

## 13. GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

**Authors:** Kaiyuan Chen, Shuangyu Xie, Letian Fu, Justin Yu, William Pacini, Sandeep Bajamahal, et al.  
**arXiv:** [arxiv.org/abs/2607.05369](https://arxiv.org/abs/2607.05369)  
**Sources:** HuggingFace Daily Papers (5 upvotes, 2 comments).  
**Why Trending:** Bridges agentic coding systems and model-free robot policies for "Variational Automation" — industrial tasks with more geometric/pose variation than fixed automation, where reliability gaps have been hard to close.

GaP proposes a graph-as-policy, multi-agent self-learning harness that combines interpretable robot programming with the open-world adaptability of model-free policies for "Variational Automation" tasks. It targets commercial and industrial settings where object geometry and pose vary more than in fixed automation, a regime where model-free policies alone often fail to reach the reliability bar required for persistent deployment.

---

## 14. RoboTALES: Learning Reasoning-Guided Robot Policies via Task-Aligned Simulated Futures

**Authors:** Hanan Gani, Tejal Kulkarni, Madhoolika Chodavarapu, Nicklas Hansen, Manmohan Chandraker  
**arXiv:** [arxiv.org/abs/2607.06018](https://arxiv.org/abs/2607.06018)  
**Sources:** HuggingFace Daily Papers (5 upvotes, 2 comments).  
**Why Trending:** Addresses a well-known failure mode of using video generative models for robot planning — imagined futures that drift from task intent — with a hierarchical LLM-based planner that keeps rollouts action-conditional.

RoboTALES is a single-stage framework that trains robot policies on task-aligned simulated futures generated by pretrained video models, fixing the tendency of such imagined rollouts to drift from actual task intent. It introduces a hierarchical LLM-based planning component so the generated futures stay reliably action-conditional and usable for policy extraction.

---

## 15. Teaching LLMs a Low-Resource Language: Enhancing Code Completion in Pharo

**Authors:** Kilian Kier, Alessandro Giagnorio, Omar AbedelKader, Oleksandr Zaitsev, Robert Peharz, Romain Robbes, et al.  
**arXiv:** [arxiv.org/abs/2607.04939](https://arxiv.org/abs/2607.04939)  
**Sources:** HuggingFace Daily Papers (5 upvotes, 2 comments).  
**Why Trending:** A concrete case study in LLM equity for low-resource programming languages — Pharo developers currently only get single-token completions while mainstream languages get full LLM-grade tooling.

The paper tackles the gap in code-completion quality for low-resource programming languages, using Pharo — a Smalltalk-inspired language whose IDE currently supports only single-token completion — as its test case. The authors adapt LLMs to substantially improve Pharo code completion despite the language's scarce training data.

---

## 16. OmniTacTune: Policy-Agnostic Real-World RL for Tactile Residual Adaptation of Visual Policies

**Authors:** Kelin Yu, Haode Zhang, Harish Ravichandar, Yunhai Han, Ruohan Gao  
**arXiv:** [arxiv.org/abs/2607.03723](https://arxiv.org/abs/2607.03723)  
**Sources:** HuggingFace Daily Papers (5 upvotes, 2 comments).  
**Why Trending:** Tackles a persistent robotics gap — visual policies trained on human/teleop video fail at contact-rich manipulation — with a real-world RL pipeline that's agnostic to the base visual policy and sensor hardware.

OmniTacTune is a policy-agnostic, real-world reinforcement-learning pipeline that adapts tactile feedback onto pretrained visual policies to improve contact-rich manipulation. It addresses visual policies' well-known weakness in tasks depending on local force and contact geometry, while working around the cost and poor cross-sensor generalization of tactile data.

---

## 17. Where to cut, how deep: BPE and Unigram-LM on chemistry SMILES

**Authors:** Hunter Heidenreich  
**arXiv:** [arxiv.org/abs/2607.05691](https://arxiv.org/abs/2607.05691)  
**Sources:** HuggingFace Daily Papers (4 upvotes, 2 comments).  
**Why Trending:** A rare deep look at tokenizer choice for chemical language models — questions the field's unexamined inheritance of byte-pair encoding from NLP and shows Unigram-LM builds structurally different chemistry vocabularies.

This paper runs a controlled comparison of byte-pair encoding (BPE) and Unigram-LM tokenization for chemical language models reading SMILES strings, over a fixed 165-token chemistry base vocabulary. It finds that the vocabulary-structure contrast known between these two schemes in natural language also holds in chemistry, particularly at the small vocabulary sizes where token embeddings remain learnable.

---

## 18. Layer-wise Cross-Lingual Depression Detection from Speech: Analysis with Contrastive Alignment

**Authors:** Anisha Pattanayak, Hanie Kang, Huang-Cheng Chou, Shrikanth Narayanan, Sudarsana Reddy Kadiri  
**arXiv:** [arxiv.org/abs/2607.02920](https://arxiv.org/abs/2607.02920)  
**Sources:** HuggingFace Daily Papers (4 upvotes, 2 comments).  
**Why Trending:** Flags a methodological flaw in prior cross-lingual depression-detection work — identity leakage from random segment-level splits — and fixes it with a contrastive alignment framework, CLeaD.

The paper introduces CLeaD, a supervised contrastive alignment framework that maps WavLM speech embeddings from English and other languages into a shared space for cross-lingual depression detection. It addresses a key flaw in prior work: segment-level random splits without speaker grouping, which leaks speaker identity across train/test sets and inflates reported accuracy.

---

## 19. SynCity 3000: Bootstrapping Scene-Scale 3D Diffusion

**Authors:** Paul Engstler, Iro Laina, Christian Rupprecht, Andrea Vedaldi  
**arXiv:** [arxiv.org/abs/2607.05392](https://arxiv.org/abs/2607.05392)  
**Sources:** HuggingFace Daily Papers (4 upvotes, 2 comments).  
**Why Trending:** Extends single-object image-to-3D generation to full scene scale by turning the generator into a convolutional operator — a scaling trick for globally coherent, fine-grained-controllable 3D scenes.

SynCity 3000 generates globally coherent 3D scenes with fine-grained layout control by extending image-to-3D asset generators to operate convolutionally across an entire scene. The model is fine-tuned on scene-like data from a new synthetic data engine built specifically to bridge single-object generation and scene-scale generation.

---

## 20. Speaker-Aware Temporal Aggregation Strategies on Segment Representations for Depression Detection in Dyadic Interaction: A Benchmark Study

**Authors:** Anisha Pattanayak, Huang-Cheng Chou, Shrikanth Narayanan, Sudarsana Reddy Kadiri  
**arXiv:** [arxiv.org/abs/2607.02904](https://arxiv.org/abs/2607.02904)  
**Sources:** HuggingFace Daily Papers (4 upvotes, 2 comments).  
**Why Trending:** Companion benchmark to the day's other depression-detection paper, isolating temporal aggregation — a step usually left unexamined — as its own variable across six architectures and six frozen speech backbones.

The paper introduces DEPOOL, a controlled benchmark isolating temporal aggregation — how segment-level speech features get compressed into one speaker-level decision — as a variable in its own right for depression detection. It compares six aggregation architectures across six frozen self-supervised speech backbones on English and Mandarin dyadic-interaction datasets, showing that reported gains often reflect the aggregation choice rather than the encoder.

---
