---
title: "Daily AI Papers — April 27, 2026"
date: 2026-04-27
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-27/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - video-generation
  - llm-safety
---

## 1. Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond

**Authors:** Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, et al.

**Summary:** Introduces a "levels × laws" taxonomy for world models in agentic AI, defining three capability levels (L1 Predictor, L2 Simulator, L3 Evolver) across four governing-law regimes (physical, digital, social, scientific). Provides a unified framework for understanding how agents model environment dynamics as they move from text generation to goal-directed interaction.

**arXiv:** [arxiv.org/abs/2604.22748](https://arxiv.org/abs/2604.22748)
**Sources:** HuggingFace Daily Papers (146 upvotes), arXiv cs.AI
**Why trending:** Highest HuggingFace upvotes of the day (146); touches the hottest topic in AI—autonomous agents and world models—with a rare taxonomic synthesis across communities.

---

## 2. Video Analysis and Generation via a Semantic Progress Function

**Authors:** Gal Metzer, Sagi Polaczek, Ali Mahdavi-Amiri, Raja Giryes, Daniel Cohen-Or

**Summary:** Proposes a one-dimensional Semantic Progress Function (SPF) that captures how meaning evolves across video frames, addressing the non-linear semantic drift in generation models where content is stable for long stretches then jumps abruptly. Enables precise video editing and generation control by operating in semantic rather than pixel space.

**arXiv:** [arxiv.org/abs/2604.22554](https://arxiv.org/abs/2604.22554)
**Sources:** HuggingFace Daily Papers (32 upvotes), arXiv cs.CV
**Why trending:** Strong HuggingFace traction; video generation control is a boiling area with wide practitioner interest.

---

## 3. DiffNR: Diffusion-Enhanced Neural Representation Optimization for Sparse-View 3D Tomographic Reconstruction

**Authors:** Shiyan Su, Ruyi Zha, Danli Shi, Hongdong Li, Xuelian Cheng

**Summary:** Proposes DiffNR, a framework that combines neural representations (NeRF / 3D Gaussians) with a single-step diffusion model (SliceFixer) to correct artifacts in sparse-view CT reconstruction. Achieves state-of-the-art results in medical imaging without requiring dense scan data.

**arXiv:** [arxiv.org/abs/2604.21518](https://arxiv.org/abs/2604.21518)
**Sources:** HuggingFace Daily Papers (26 upvotes), arXiv cs.CV
**Why trending:** Diffusion priors for 3D reconstruction is a high-impact research area; medical imaging application broadens audience beyond pure ML community.

---

## 4. LLM Safety From Within: Detecting Harmful Content with Internal Representations (SIREN)

**Authors:** Difan Jiao, Yilun Liu, Ye Yuan, Zhenwei Tang, Linfeng Du

**Summary:** Presents SIREN, a lightweight guard model that detects harmful content by mining safety-relevant features distributed across all internal layers of an LLM (not just the final layer), using linear probing to identify "safety neurons." Outperforms state-of-the-art guard models while being more efficient, showing that internal representations carry rich safety signals.

**arXiv:** [arxiv.org/abs/2604.18519](https://arxiv.org/abs/2604.18519)
**Sources:** HuggingFace Daily Papers (21 upvotes), arXiv cs.CL
**Why trending:** AI safety and content moderation remain top priorities across labs and regulators; internal-representation approach is a novel angle over prompt-based guards.

---

## 5. Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought

**Authors:** Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo

**Summary:** Introduces Abstract Chain-of-Thought (ACoT), a method enabling LLMs to reason in continuous latent space rather than generating verbose verbal reasoning steps, achieving competitive accuracy on complex tasks with significantly shorter generation lengths. Bridges the gap between token-efficient non-verbal approaches and the performance of explicit chain-of-thought reasoning.

**arXiv:** [arxiv.org/abs/2604.22709](https://arxiv.org/abs/2604.22709)
**Sources:** arXiv cs.CL, arXiv cs.LG
**Why trending:** Inference efficiency is critical as reasoning models get deployed at scale; latent reasoning is a frontier research direction following OpenAI's o-series models.

---

## 6. FlowAnchor: Stabilizing the Editing Signal for Inversion-Free Video Editing

**Authors:** Ze Chen, Lan Chen, Yuanhang Li, Qi Mao

**Summary:** Proposes FlowAnchor, a training-free framework for stable inversion-free video editing using flow-based models that anchors the editing signal across frames to prevent drift in multi-object scenes. Addresses the core failure mode of inversion-free methods when extended from images to videos.

**arXiv:** [arxiv.org/abs/2604.22586](https://arxiv.org/abs/2604.22586)
**Sources:** HuggingFace Daily Papers (10 upvotes), arXiv cs.CV
**Why trending:** Training-free video editing at high quality is a practical goal for content creators; flow-based diffusion methods are the current state-of-the-art backbone.

---

## 7. AgentSearchBench: A Benchmark for AI Agent Search in the Wild

**Authors:** Bin Wu, Arastun Mammadli, Xiaoyu Zhang, Emine Yilmaz

**Summary:** Introduces AgentSearchBench, the first benchmark designed to evaluate the ability of AI agents to find suitable sub-agents for task delegation in open-ended, "in the wild" settings where agent capabilities are compositional and execution-dependent. Reveals significant gaps between current agent discovery methods and human performance.

**arXiv:** [arxiv.org/abs/2604.22436](https://arxiv.org/abs/2604.22436)
**Sources:** HuggingFace Daily Papers (9 upvotes), arXiv cs.AI
**Why trending:** Multi-agent orchestration is a fast-growing research area; benchmarks are needed to measure progress in real deployments beyond toy setups.

---

## 8. How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks

**Authors:** Longju Bai, Zhemin Huang, Xingyao Wang

**Summary:** Systematically analyzes where AI coding agents spend tokens across different stages (planning, execution, reflection) and builds a predictive model for token budget allocation before deployment. Finds that token consumption patterns vary dramatically by task type and model, enabling cost-aware agent scheduling.

**arXiv:** [arxiv.org/abs/2604.22750](https://arxiv.org/abs/2604.22750)
**Sources:** arXiv cs.SE, arXiv cs.AI
**Why trending:** As agent usage grows, cost control is a top concern for teams shipping agentic pipelines; this directly addresses economics that practitioners care about.

---

## 9. Contexts are Never Long Enough: Structured Reasoning for Scalable QA over Long Document Sets

**Authors:** Harshit Joshi, Priyank Shethia, Jadelynn Dao, Monica S. Lam

**Summary:** Addresses the aggregation bottleneck in multi-document QA where no fixed context window is sufficient; proposes a structured reasoning pipeline that decomposes questions into sub-tasks across chunk-level outputs and synthesizes coherent answers at scale. Demonstrates robust performance even when document collections grow beyond any available context window.

**arXiv:** [arxiv.org/abs/2604.22294](https://arxiv.org/abs/2604.22294)
**Sources:** HuggingFace Daily Papers (7 upvotes), arXiv cs.CL
**Why trending:** Long-context and RAG limitations are a key unsolved problem; enterprise document QA use cases make this immediately practical.

---

## 10. Spend Less, Fit Better: Budget-Efficient Scaling Law Fitting via Active Experiment Selection

**Authors:** Sijie Li, Shanda Li, Haowei Lin

**Summary:** Proposes an active learning approach to select which pilot experiments to run when fitting scaling laws, drastically reducing the compute cost of fitting scaling laws themselves—which can rival the cost of the training runs they inform. Demonstrates accurate scaling law estimates with a fraction of the experimental budget.

**arXiv:** [arxiv.org/abs/2604.22753](https://arxiv.org/abs/2604.22753)
**Sources:** arXiv cs.LG
**Why trending:** Scaling law fitting is critical for planning multi-million-dollar training runs; reducing that meta-cost has outsized industry value.

---

## 11. Building a Precise Video Language with Human-AI Oversight

**Authors:** Zhiqiu Lin, Chancharik Mitra, Siyuan Cen, Isaac Li, Yuhan Huang

**Summary:** Defines a structured specification for video description covering subjects, scenes, motion, spatial relations, and camera dynamics, grounded in hundreds of visual primitives, and pairs it with a human-AI scalable oversight pipeline for high-precision video captioning. Releases open datasets and benchmarks for training video-language models on this vocabulary.

**arXiv:** [arxiv.org/abs/2604.21718](https://arxiv.org/abs/2604.21718)
**Sources:** HuggingFace Daily Papers (3 upvotes), arXiv cs.CV
**Why trending:** Structured video captioning is foundational for next-generation VLMs; the scalable oversight methodology is directly relevant to alignment research.

---

## 12. Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities

**Authors:** Ilana Nguyen, Harini Suresh, Thema Monroe-White

**Summary:** Examines how LLMs encode and propagate representational harms against nationalities from the Global Majority (Africa, Latin America, South/Southeast Asia) in generated narratives, including simulated interviews used in high-stakes government applications. Identifies systematic patterns of stereotype reinforcement and provides an audit framework for practitioners.

**arXiv:** [arxiv.org/abs/2604.22749](https://arxiv.org/abs/2604.22749)
**Sources:** arXiv cs.CL, arXiv cs.AI
**Why trending:** AI fairness and harm auditing are central to responsible deployment; government use cases (asylum interviews) raise the stakes significantly.

---

## 13. dWorldEval: Scalable Robotic Policy Evaluation via Discrete Diffusion World Model

**Authors:** Yaxuan Li, Zhongyi Zhou, Yefei Chen, Yaokai Xue, Yichen Zhu

**Summary:** Proposes dWorldEval, which uses a discrete diffusion world model as a scalable proxy for evaluating robotic policies across thousands of environments without physical simulation. Maps all modalities (vision, action, proprioception) into a unified discrete token space for scalable rollout generation.

**arXiv:** [arxiv.org/abs/2604.22152](https://arxiv.org/abs/2604.22152)
**Sources:** HuggingFace Daily Papers (2 upvotes), arXiv cs.RO
**Why trending:** Scalable robot evaluation is a hard open problem; diffusion world models for robotics is a frontier being actively pursued by major labs.

---

## 14. EmbodiedMidtrain: Bridging the Gap Between VLMs and VLAs via Mid-training

**Authors:** Yiyang Du, Zhanqiu Guo, Xin Ye, Liu Ren, Chenyan Xiong

**Summary:** Identifies a data distribution gap between vision-language models (VLMs) and vision-language-action models (VLAs) that limits VLA downstream performance, and proposes EmbodiedMidtrain—a mid-training stage that adapts VLMs specifically for the embodied domain before VLA fine-tuning. Demonstrates consistent gains across multiple robot manipulation benchmarks.

**arXiv:** [arxiv.org/abs/2604.20012](https://arxiv.org/abs/2604.20012)
**Sources:** HuggingFace Daily Papers (2 upvotes), arXiv cs.RO, arXiv cs.CV
**Why trending:** VLA models (like π0, RT-2) are a major research investment; closing the VLM-to-VLA gap has direct impact on robot learning pipelines.

---

## 15. CRAFT: Clustered Regression for Adaptive Filtering of Training Data

**Authors:** Parthasarathi Panda, Asheswari Swain, Subhrakanta Panda

**Summary:** Proposes CRAFT, a vectorized clustering-and-regression approach for selecting a small, high-quality subset from tens of millions of data points for fine-tuning, replacing expensive full dataset training. Achieves comparable downstream performance to full fine-tuning with a fraction of the data and compute.

**arXiv:** [arxiv.org/abs/2604.22693](https://arxiv.org/abs/2604.22693)
**Sources:** arXiv cs.LG
**Why trending:** Data selection for efficient fine-tuning is a hot practical problem as datasets grow and compute costs bite; CRAFT addresses scale that matters in production.

---

## 16. Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents

**Authors:** Seyed Moein Abtahi, Rasa Rahnema, Hetkumar Patel, Neel Patel, Majid Fekri

**Summary:** Presents Memanto, an agent memory architecture using typed semantic memory categories and information-theoretic retrieval to replace computationally expensive hybrid graph approaches. Designed for persistent, multi-session agents requiring low-latency memory access in production deployments.

**arXiv:** [arxiv.org/abs/2604.22085](https://arxiv.org/abs/2604.22085)
**Sources:** HuggingFace Daily Papers (1 upvote), arXiv cs.AI
**Why trending:** Memory is the primary bottleneck in production agentic systems; efficient retrieval architectures are in active demand.

---

## 17. Sessa: Selective State Space Attention

**Authors:** Liubomyr Horbatko

**Summary:** Proposes Sessa, a hybrid architecture that selectively combines state-space model recurrence with attention, enabling per-token routing between SSM and attention paths to balance long-context efficiency with the focused recall that attention provides. Addresses the core tradeoff that neither pure Transformers nor pure SSMs handle optimally.

**arXiv:** [arxiv.org/abs/2604.18580](https://arxiv.org/abs/2604.18580)
**Sources:** HuggingFace Daily Papers (1 upvote), arXiv cs.LG
**Why trending:** Mamba/SSM-Transformer hybrid architectures are a heavily researched alternative to pure Transformers; any architectural advance here gets traction.

---

## 18. DiagramBank: A Large-scale Dataset of Diagram Design Exemplars for RAG

**Authors:** Tingwen Zhang, Ling Yue, Zhen Xu, Shaowu Pan

**Summary:** Introduces DiagramBank, a large-scale dataset of scientific diagram exemplars with paper metadata, designed to enable retrieval-augmented generation for automated scientific figure creation in "AI scientist" pipelines. Addresses a key bottleneck—diagram generation—in end-to-end autonomous paper writing systems.

**arXiv:** [arxiv.org/abs/2604.20857](https://arxiv.org/abs/2604.20857)
**Sources:** HuggingFace Daily Papers (1 upvote), arXiv cs.CV, arXiv cs.AI
**Why trending:** AI-generated scientific papers are a growing capability area; diagram quality is the weakest link and DiagramBank provides the missing resource.

---

## 19. AgriIR: A Scalable Framework for Domain-Specific Knowledge Retrieval

**Authors:** Shuvam Banerji Seal, Aheli Poddar, Alok Mishra, Dwaipayan Roy

**Summary:** Presents AgriIR, a modular RAG framework for agriculture that decomposes information access into declarative stages (query refinement, sub-query planning, retrieval, synthesis) for grounded, domain-specific answers without large monolithic models. Demonstrates that modular RAG beats end-to-end LLM approaches in specialized, low-resource domains.

**arXiv:** [arxiv.org/abs/2604.16353](https://arxiv.org/abs/2604.16353)
**Sources:** HuggingFace Daily Papers (1 upvote), arXiv cs.IR
**Why trending:** Domain-specific RAG is a practical deployment pattern; agriculture is a high-value vertical with limited existing AI tooling.

---

## 20. Learning Evidence Highlighting for Frozen LLMs (HiLight)

**Authors:** Shaoang Li, Yanhang Shi, Yufei Li, Mingfu Liang, Xiaohan Wei

**Summary:** Introduces HiLight, an Evidence Emphasis framework that trains a lightweight Emphasis Actor to insert minimal highlights into long, noisy contexts, steering a frozen LLM's attention to decisive evidence without rewriting or compressing the input. Decouples evidence selection from reasoning, preserving input fidelity while dramatically improving answer accuracy on long-context QA.

**arXiv:** [arxiv.org/abs/2604.22565](https://arxiv.org/abs/2604.22565)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL
**Why trending:** Long-context retrieval and evidence grounding remain unsolved; the frozen-LLM + lightweight adapter design is immediately deployable without retraining.

---

*Report generated: 2026-04-27 | Papers from HuggingFace Daily Papers (primary), arXiv (cs.AI, cs.LG, cs.CL)*
