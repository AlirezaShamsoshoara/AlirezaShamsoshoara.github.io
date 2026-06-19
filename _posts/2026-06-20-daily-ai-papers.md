---
title: "Daily AI Papers — June 20, 2026"
date: 2026-06-20
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-20/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-agents
  - multimodal-learning
  - retrieval-augmented-generation
---

---

## 1. DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis
**Authors:** Cheng-You Lu, Yi-Shan Hung, Wei-Ling Chi, Hao-Ping Wang
**arxiv:** [arxiv.org/abs/2604.13416](https://arxiv.org/abs/2604.13416)
**Sources:** HuggingFace Daily Papers (26 upvotes), arXiv
**Summary:** Radiance fields enable photorealistic novel view synthesis, but distractor-free methods lacked a large-scale benchmark with paired clean/cluttered images per scene. DF3DV-1K provides 1K such scenes to support comprehensive benchmarking and research progress beyond scene-specific reconstruction.
**Why trending:** Highest upvote count among today's new papers; fills a key infrastructure gap for 3D scene understanding evaluation.

---

## 2. LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents
**Authors:** Md Nayem Uddin, Amir Saeidi, Eduardo Blanco, Chitta Baral
**arxiv:** [arxiv.org/abs/2606.20529](https://arxiv.org/abs/2606.20529)
**Sources:** HuggingFace Daily Papers (5 upvotes), arXiv
**Summary:** Standard tool-calling agents conflate task state with conversation history, causing policy drift across turns. LedgerAgent maintains a structured ledger of facts, constraints, identifiers, and tool results that persists separately from the dialogue, enabling reliable policy adherence in customer-service domains.
**Why trending:** Addresses a key reliability problem in production LLM agents used in enterprise settings.

---

## 3. Freeing the Law with LOCUS: A Local Ordinance Corpus for the United States
**Authors:** Denis Peskoff, Joe Barrow, Christopher Vu, Diag Davenport
**arxiv:** [arxiv.org/abs/2606.19334](https://arxiv.org/abs/2606.19334)
**Sources:** HuggingFace Daily Papers (5 upvotes), arXiv
**Summary:** Local ordinances governing zoning, housing, business licensing, and public health are fragmented across thousands of municipalities and largely absent from machine-readable AI corpora. LOCUS provides a large-scale, structured corpus of US local ordinances to advance legal AI, regulatory compliance, and policy research.
**Why trending:** Critical infrastructure resource for legal AI; addresses an important but overlooked layer of US law.

---

## 4. Understanding the Behaviors of Environment-Aware Information Retrieval
**Authors:** Ruifeng Yuan, Chaohao Yuan, David Dai, Yu Rong
**arxiv:** [arxiv.org/abs/2606.16817](https://arxiv.org/abs/2606.16817)
**Sources:** HuggingFace Daily Papers (5 upvotes), arXiv
**Summary:** Different retrievers in RAG systems require fundamentally different query formulation strategies for optimal performance, a challenge current research largely overlooks. This paper presents the first systematic analysis of how LLMs can learn to adapt their query formulation to different retrieval environments.
**Why trending:** Actionable insights for RAG system design; relevant to any production LLM application using retrieval.

---

## 5. Adaptive Volumetric Mechanical Property Fields Invariant to Resolution
**Authors:** Rishit Dagli, Donglai Xiang, Vismay Modi, Xuning Yang
**arxiv:** [arxiv.org/abs/2606.18231](https://arxiv.org/abs/2606.18231)
**Sources:** HuggingFace Daily Papers (4 upvotes), arXiv
**Summary:** Most 3D assets lack the mechanical properties (Young's modulus, Poisson's ratio, density) required for reliable physics simulation of digital worlds. This work proposes neural fields that predict volumetric material properties invariant to mesh resolution, enabling accurate simulation of digital twins without manual annotation.
**Why trending:** Key enabler for physics-based simulation in robotics, gaming, and digital twin applications.

---

## 6. Think Again or Think Longer? Selective Verification for Budget-Aware Reasoning
**Authors:** Sajib Acharjee Dip, Dawei Zhou, Liqing Zhang
**arxiv:** [arxiv.org/abs/2606.19808](https://arxiv.org/abs/2606.19808)
**Sources:** HuggingFace Trending (3 upvotes), arXiv
**Summary:** Extra test-time reasoning is not uniformly valuable—it can repair failed attempts, waste compute on already-correct answers, or even corrupt good answers. SEVRA (Selective Verification for Reasoning Allocation) treats this as a deployment allocation problem, learning a serving-layer policy for when to re-reason and when to stop.
**Why trending:** Directly relevant to efficient LLM inference; addresses over-reasoning costs in deployed reasoning models.

---

## 7. JAMER: Project-Level Code Framework Dataset and Benchmark on Professional Game Engines
**Authors:** Jianwen Sun, Chuanhao Li, Zizhen Li, Yukang Feng
**arxiv:** [arxiv.org/abs/2606.19830](https://arxiv.org/abs/2606.19830)
**Sources:** HuggingFace Daily Papers (3 upvotes), arXiv
**Summary:** AI-driven game development has made progress in asset generation and web-based coding, but project-level code engineering on professional engines (Unity, Unreal) remains largely unevaluated. JAMER provides a realistic benchmark dataset for evaluating LLMs on project-scale game engine code tasks.
**Why trending:** Game engine coding is commercially important and an underexplored but hard frontier for LLMs.

---

## 8. Configurable Clinical Information Extraction with Agentic RAG: What Works, What Breaks, and Why
**Authors:** Osman Alperen Çinar-Koraş, Marie Bauer, Sameh Khattab, Merlin Engelke
**arxiv:** [arxiv.org/abs/2606.19602](https://arxiv.org/abs/2606.19602)
**Sources:** HuggingFace Daily Papers (3 upvotes), arXiv
**Summary:** Patient contexts span hundreds of heterogeneous documents and thousands of structured data points, yet AI systems lack the metadata needed for efficient retrieval and triage. This paper systematically diagnoses what works and what fails in agentic RAG pipelines for configurable clinical information extraction.
**Why trending:** Clinical AI is high-stakes; rigorous diagnosis of agentic RAG failure modes is practically valuable.

---

## 9. LooseControlVideo: Directorial Video Control using Spatial Blocking
**Authors:** Shariq Farooq Bhat, Niloy J. Mitra, Kalyan Sunkavalli
**arxiv:** [arxiv.org/abs/2606.19495](https://arxiv.org/abs/2606.19495)
**Sources:** HuggingFace Daily Papers (3 upvotes), arXiv
**Summary:** Precise 3D spatial orchestration in text-to-video generation is challenging for multi-object scenes where semantic layout and temporal dynamics are entangled. LooseControlVideo introduces spatial blocking as a coarse but intuitive director-style interface for controlling scene layout in video generation.
**Why trending:** Practical advancement in controllable video generation with a creative direction use case.

---

## 10. LegalHalluLens: Typed Hallucination Auditing and Calibrated Multi-Agent Debate for Trustworthy Legal AI
**Authors:** Lalit Yadav, Akshaj Gurugubelli
**arxiv:** [arxiv.org/abs/2606.18021](https://arxiv.org/abs/2606.18021)
**Sources:** HuggingFace Daily Papers (3 upvotes), arXiv
**Summary:** AI systems in legal workflows hallucinate at ~52% aggregate rates, but aggregate metrics hide where errors concentrate and in which direction they run. LegalHalluLens provides typed hallucination auditing and a calibrated multi-agent debate mechanism to surface and reduce errors in high-stakes legal AI deployments.
**Why trending:** Typed hallucination analysis is immediately actionable for legal AI practitioners; multi-agent debate as calibration is novel.

---

## 11. Selective Synergistic Learning for Video Object-Centric Learning
**Authors:** WonJun Moon, Jae-Pil Heo
**arxiv:** [arxiv.org/abs/2606.15527](https://arxiv.org/abs/2606.15527)
**Sources:** HuggingFace Daily Papers (3 upvotes), arXiv
**Summary:** Typical video object-centric learning (VOCL) relies on reconstruction-driven encoder-decoder architectures that mediate learning via two spatial maps, conflating object discovery with reconstruction quality. Selective Synergistic Learning improves slot-based frameworks by selectively coupling informative spatial signals to achieve better object representation in video.
**Why trending:** Foundational for compositional video understanding; relevant to embodied AI and autonomous systems.

---

## 12. ROSE: Benchmarking the Perception-to-Action Gap in Multimodal Models
**Authors:** Yihao Wang, Zijian He, Jie Ren, Keze Wang
**arxiv:** [arxiv.org/abs/2606.19965](https://arxiv.org/abs/2606.19965)
**Sources:** HuggingFace Trending, arXiv
**Summary:** Multimodal LLMs are expected to act on visual information, but the same scene may require different actions under different task contexts—a gap that existing benchmarks do not measure. ROSE (Reference-conditioned Oddity and Symbol Evaluation) benchmarks how reliably models translate visual evidence into context-appropriate actions.
**Why trending:** Identifies a critical blind spot in multimodal model evaluation that matters for real-world deployment.

---

## 13. World Engine: Towards the Era of Post-Training for Autonomous Driving
**Authors:** Tianyu Li, Li Chen, Caojun Wang, Haochen Liu et al.
**arxiv:** [arxiv.org/abs/2606.19836](https://arxiv.org/abs/2606.19836)
**Sources:** HuggingFace Trending, arXiv
**Summary:** End-to-end driving policies excel in routine scenarios but fail at rare safety-critical long-tail events that are scarce in real driving datasets. World Engine proposes a post-training paradigm using world model simulation to expose policies to safety-critical scenarios, improving reliability at the practical safety boundary.
**Why trending:** Safety-critical autonomous driving and scalable post-training are major active research frontiers.

---

## 14. Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users
**Authors:** Haw-Shiuan Chang, Jeffrey Gomez, Mehul Patwari, Aryan Sajith, Hamed Zamani
**arxiv:** [arxiv.org/abs/2606.20482](https://arxiv.org/abs/2606.20482)
**Sources:** HuggingFace Trending, arXiv
**Summary:** Most LLM alignment methods require expensive explicit human preference annotations that users rarely provide. This paper demonstrates that implicit user signals—mouse movements and eye gaze patterns during interaction—can be leveraged for preference learning, enabling low-cost continuous alignment from natural usage.
**Why trending:** Novel and practical approach to dramatically reducing RLHF annotation cost; directly applicable to deployed chat systems.

---

## 15. UNIEGO: Proxies as Mediators for Unified Egocentric Video Representation Learning
**Authors:** Wenhao Chi, Arkaprava Sinha, Dominick Reilly, Hieu Le, Srijan Das
**arxiv:** [arxiv.org/abs/2606.20559](https://arxiv.org/abs/2606.20559)
**Sources:** HuggingFace Trending, arXiv
**Summary:** Egocentric video understanding from wearable cameras is limited by a single viewpoint, modality, and model representation. UNIEGO uses proxy representations as mediators to unify knowledge across viewpoints, modalities, and foundation models, producing richer egocentric representations deployable from a single camera.
**Why trending:** Relevant to AR/VR, embodied AI, and assistive technology where egocentric perception is central.

---

## 16. Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems
**Authors:** Zewen Liu
**arxiv:** [arxiv.org/abs/2606.20493](https://arxiv.org/abs/2606.20493)
**Sources:** HuggingFace Trending, arXiv
**Summary:** When LLMs serve as evaluators in multi-agent systems, their systematic biases do not stay isolated—they propagate through the agent network. Contagion Networks formalizes how evaluator biases spread and compound across interacting LLM agents in a controlled 3-agent experiment, with implications for multi-agent evaluation design.
**Why trending:** Critical insight for understanding reliability of LLM-as-judge frameworks in multi-agent pipelines.

---

## 17. The Data Manifold under the Microscope
**Authors:** Marios Koulakis, Constantin Seibold
**arxiv:** [arxiv.org/abs/2606.15760](https://arxiv.org/abs/2606.15760)
**Sources:** HuggingFace Daily Papers (2 upvotes), arXiv
**Summary:** A significant gap persists between theory and practice in deep learning: generalization and approximation error bounds are often derived for simplified models and are too loose to be informative. This paper empirically examines the geometry of the data manifold to directly characterize the sources of this gap.
**Why trending:** Foundational work addressing why theoretical guarantees don't match practice; relevant to all of deep learning.

---

## 18. Duration Aware Scheduling for ASR Serving Under Workload Drift
**Authors:** Darshan Makwana, Yash Jogi, Harsh Kotta, Aayush Kubba
**arxiv:** [arxiv.org/abs/2603.11273](https://arxiv.org/abs/2603.11273)
**Sources:** HuggingFace Daily Papers (2 upvotes), arXiv
**Summary:** Scheduling in large-scale ASR serving pipelines critically impacts end-to-end latency, but widely-used engines rely on first-come-first-serve policies that are blind to audio duration. This paper proposes duration-aware scheduling with online adaptation to workload drift, achieving significantly lower latency at scale.
**Why trending:** Practical ML serving optimization relevant to any speech AI system operating at scale.

---

## 19. No Resource, No Benchmarks, No Problem? Evaluating and Improving LLMs for Code Generation in No-Resource Languages
**Authors:** Alessandro Giagnorio, Alberto Martin-Lopez, Gabriele Bavota
**arxiv:** [arxiv.org/abs/2606.16827](https://arxiv.org/abs/2606.16827)
**Sources:** HuggingFace Daily Papers (1 upvote), arXiv
**Summary:** LLMs excel at code generation in popular languages like Python but remain largely unevaluated on "no-resource" programming languages that have minimal training data representation. This paper introduces evaluation methodology and fine-tuning improvements for LLM code generation in underrepresented languages.
**Why trending:** Expands LLM utility beyond dominant programming languages; important for practitioners working with specialized or legacy languages.

---

## 20. ReSyn: A Generalized Recursive Regular Expression Synthesis Framework
**Authors:** Seongmin Kim, Hyunjoon Cheon, Su-Hyeon Kim, Yo-Sub Han
**arxiv:** [arxiv.org/abs/2603.24624](https://arxiv.org/abs/2603.24624)
**Sources:** HuggingFace Daily Papers (1 upvote), arXiv
**Summary:** Existing Programming-By-Example (PBE) systems rely on simplified benchmarks that fail to capture real-world regex complexity such as deep nesting and frequent alternation. ReSyn provides a generalized recursive synthesis framework that handles the full structural complexity of production regular expressions from examples.
**Why trending:** PBE and program synthesis are core to code intelligence; complex regex synthesis represents a hard and practically relevant benchmark.
