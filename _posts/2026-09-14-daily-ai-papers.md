---
title: "Daily AI Papers — September 14, 2026"
date: 2026-09-14
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-14/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-agents
  - efficient-ai
  - robotics
---

### 1. DataFlex-RL: An Evaluation Platform for RLVR Data Policies
**Authors:** Hao Liang, Mingrui Chen, Hengyi Feng, Meiyi Qiang, Wentao Zhang
**arXiv:** [arxiv.org/abs/2609.06107](https://arxiv.org/abs/2609.06107)
**Summary:** Data policies for reinforcement learning with verifiable rewards (RLVR) determine which rollouts are used, how strongly they are weighted, and which domains contribute to subsequent training batches. We introduce DataFlex-RL, an evaluation platform for comparing these choices under a common GRPO recipe.
**Trending because:** 95 HuggingFace upvotes + tests whether sophisticated RLVR data policies reliably outperform uniform sampling

---

### 2. Feyospace-v1: How the Cyber Mercury Seven Trained Frontier Cyber Models
**Authors:** Zongjie Li, Alan Z. W, John Nicolas J, Walter H. F, Scott Donald L, Gordon Y. P, Deke X Jr
**arXiv:** [arxiv.org/abs/2609.08418](https://arxiv.org/abs/2609.08418)
**Summary:** Training capable cyber agents is often treated primarily as a problem of model scale, yet open-weight post-training is constrained more directly by the cost of executable environments, reliable multi-turn supervision, and access to strong teachers. We present a data-centric framework that addresses these bottlenecks through five complementary systems: Choulea analyzes hidden reasoning signatures, SkyReal reduces teacher-sampling cost, Hongzwang bypasses API restrictions on teacher execution, PSBreakup restores capabilities weakened by model merging, and Kreator converts expert interventions into trainable reasoning.
**Trending because:** 74 HuggingFace upvotes + shows a small team training competitive open-weight cyber agents with execution-verified data

---

### 3. Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation
**Authors:** Koutian Wu, Junjie Zhou, Ergan Shang, Jiayu Wang, Pengqian Han, Junkai Wang, Wanghan Xu
**arXiv:** [arxiv.org/abs/2609.11115](https://arxiv.org/abs/2609.11115)
**Summary:** Benchmark researchers and developers of large language models (LLMs) and other AI systems need to find relevant evaluations, locate their benchmark datasets and code, and understand the settings behind reported scores. We present Benchmark Radar, a living database and search engine for retrieval and discovery of AI benchmarks, covering LLM evaluation, agentic and tool-use benchmarks, coding, reasoning, safety, and domain-specific evaluations.
**Trending because:** 71 HuggingFace upvotes + builds a living search engine for tracking AI benchmarks and evaluation practice

---

### 4. Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models
**Authors:** Jianman Lin, Shailesh Shailesh, Zhongyi Luo, Jiafei Duan
**arXiv:** [arxiv.org/abs/2609.12641](https://arxiv.org/abs/2609.12641)
**Summary:** Robot foundation models achieve strong in-distribution performance but often degrade under visual distribution shifts. When learning to generate actions from pretrained visual representations, models may exploit task-irrelevant visual cues that correlate with demonstrated actions within the training distribution.
**Trending because:** 61 HuggingFace upvotes + targets better robotics generalization by breaking direct vision-action shortcuts

---

### 5. SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking
**Authors:** Zhiwei Li, Lei Zhu, Hao Gu, Xiang Hu, Yan Wang, Haitao Mi, Sirui Han, Leo Liang, Zhijiang Guo
**arXiv:** [arxiv.org/abs/2609.13141](https://arxiv.org/abs/2609.13141)
**Summary:** Post-training attention sparsification reduces the quadratic cumulative attention cost of pretrained Transformers by selecting a small set of context units (tokens or blocks) for each query. Existing trainable methods usually use a lightweight selector to score context units, followed by hard Top-K selection that blocks gradients from the language modeling loss.
**Trending because:** 49 HuggingFace upvotes + learns sparse attention through end-to-end context ranking

---

### 6. COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization
**Authors:** Pingchen Lu, Xiangyi Wang, Xiang Li, Jie Mao, Zikun Qu, Junfeng Luo, Yao Shu, Bryan Kian Hsiang Low, Zhongxiang Dai
**arXiv:** [arxiv.org/abs/2609.11682](https://arxiv.org/abs/2609.11682)
**Summary:** Large language model (LLM) agents can benefit from reusable skills distilled from prior task experience, yet existing skill optimization methods often rely on costly execution-based evaluation and substantial task data. We introduce COBRA-Skills, an efficient framework that formulates skill optimization as budgeted sequential optimization over a dynamically evolving candidate space.
**Trending because:** 29 HuggingFace upvotes + uses contextual bandits to evolve and select stronger agent skills

---

### 7. StepAudio 3 Gen Technical Report
**Authors:** Bin Lin, Bo Zhao, Boyang Wang, Boyang Zhang, Boyong Wu, Chao Yan, Chen Geng, Chen Wu, Cheng Yi, Chengli Feng, Chenglin Zhu, DanNi Wan, Daxin Jiang, Dongqing Pang, Fei Tian, Feng Tian, Future Li, Gang Yu, Guanglong Yang, Jia Peng, Jiahao Song, Jiamin Fan, Jiangjie Zhen, Jianzheng Gao, Jun Chen, Li Xie, Lifang Zhang, Lingli Ji, Liying Shi, Lun Cai, Min Xu, Na Wang, Peilin Li, Peng Yang, Pengfei Tan, Qingjian Lin, Ruijie Xiong, Runze Li, Shenghua Hu, Shi Qiu, Siqi Tu, Siyi Zhou, Tianjiao Deng, Wanying Lu, Weiming Niu, Wen Sun, WenWen Qu, Xiangyu Zhang, Xianwei Zhang, XiaoSu Su, Xing Chen, Xinyu Liu, Xuerui Yang, Yang Li, Yang Yang, Yechang Huang, Yibo Zhu, Yifan Zhang, Yiyang Xu, Yu Fu, Yu Luo, Yu Zhou, Yumang Wang, Yunzhou Ju, Yuxiang Yang, Zekai Liu, Zengwei Yao, Zhenwei Mou, Zheqi Dai, Zhiyue Wu, Zichao Zhou
**arXiv:** [arxiv.org/abs/2609.12945](https://arxiv.org/abs/2609.12945)
**Summary:** We introduce StepAudio 3 Gen, a general-purpose audio generation model that supports zero-shot text-to-speech (TTS), voice design, vocal generation, sound effects, music, vibe speech, and mixtures of multiple audio types within a unified framework. At its core, StepAudio 3 Gen is a discrete autoregressive generator that models audio directly over residual vector quantization (RVQ) tokens, departing from the diffusion Transformer-based continuous generation paradigm prevalent in recent general audio models.
**Trending because:** 28 HuggingFace upvotes + advances unified speech generation with the StepAudio model family

---

### 8. PLC-DPO: Posterior Label Correction in Noisy and Ambiguous Preference Optimization
**Authors:** Boryeong Cho, Sumyeong Ahn, Se-Young Yun
**arXiv:** [arxiv.org/abs/2608.30597](https://arxiv.org/abs/2608.30597)
**Summary:** Direct Preference Optimization (DPO) simplifies alignment through pairwise comparisons but assumes all observed preferences are reliable. Real data often violates this assumption, leading to reversed, weak, or ambiguous labels that cause harmful policy updates.
**Trending because:** 23 HuggingFace upvotes + improves preference optimization under noisy and ambiguous labels

---

### 9. Online Learning with LLM Experts from Limited Feedback
**Authors:** Wang Wei, Soumyabrata Pal, Koyel Mukherjee, Franck Dernoncourt, Ryan A. Rossi, Branislav Kveton, Hoda Eldardiry
**arXiv:** [arxiv.org/abs/2609.05820](https://arxiv.org/abs/2609.05820)
**Summary:** We study adaptive routing of prompts to large language model (LLM) experts to maximize response quality in an online setting with limited feedback. We formulate it as a bandit problem with K actions that represent experts and d features that encode prompts, over a horizon of T rounds.
**Trending because:** 4 HuggingFace upvotes + studies online learning from LLM experts when feedback is scarce

---

### 10. Beyond Top-$k$ Skill Retrieval: Diversity-Aware Skill Routing for LLM Agents
**Authors:** Wang Wei, Tiankai Yang, Samyadeep Basu, Hongjie Chen, Yue Zhao, Zhengzhong Tu, Xiyang Hu, Franck Dernoncourt, Ryan A. Rossi, Hoda Eldardiry
**arXiv:** [arxiv.org/abs/2609.05824](https://arxiv.org/abs/2609.05824)
**Summary:** Large language model (LLM) agents increasingly rely on external skills, but routing user requests over large skill registries is difficult because many skills are functionally redundant while complex tasks often require complementary skill sets. Existing skill routers typically rank candidates independently by query relevance, which can waste context budget on redundant skills.
**Trending because:** 4 HuggingFace upvotes + moves agent skill routing beyond similarity-only top-k retrieval

---

### 11. SNAP3D: Physically Grounded 3D Parts for Assembly from a Single Image
**Authors:** Yu-Rou Tuan, Hao-Tang Tsui, Nicolas Ugrinovic, Kris Kitani, Xiaoxuan Ma
**arXiv:** [arxiv.org/abs/2609.13146](https://arxiv.org/abs/2609.13146)
**Summary:** Part-aware 3D asset generation enables applications such as editing, articulation, simulation, and fabrication, yet existing methods can generate visually complete individual parts without ensuring that they form a valid physical assembly. Consequently, generated neighboring parts may interpenetrate, lack valid connections, or collapse under gravity.
**Trending because:** 3 HuggingFace upvotes + generates physically grounded, assembly-ready 3D parts from one image

---

### 12. ActionSplice: In-Flight Action Editing for Interactive World Models
**Authors:** Pardis Taghavi, Tingyu Guo, Jonas Lossner, Gaurav Pandey, Reza Langari
**arXiv:** [arxiv.org/abs/2609.08230](https://arxiv.org/abs/2609.08230)
**Summary:** Chunk-autoregressive video world models typically condition each generated chunk on one action. An action received during sampling must therefore wait for the next chunk, condition future solver evaluations on a state produced under the previous action, or trigger rollback that repeats completed evaluations.
**Trending because:** 2 HuggingFace upvotes + enables users to edit actions while interactive world-model rollouts are in progress

---

### 13. Building and Evaluating Fixed-Voice Thai TTS from Synthetic Speech
**Authors:** Kunat Pipatanakul, Potsawee Manakul, Warit Sirichotedumrong, Sittipong Sripaisarnmongkol, Pakorn Nathong, Phatrasek Jirabovonvisut
**arXiv:** [arxiv.org/abs/2609.03502](https://arxiv.org/abs/2609.03502)
**Summary:** In low-resource settings, deploying TTS typically requires choosing between a large voice-cloning model with costly inference or a compact fixed-voice system that requires a speaker-specific corpus. We study a third route: using a large voice-cloning model as a programmable data source to turn a short voice reference (e.g., 15 seconds) into a compact fixed-voice student trained entirely on synthetic speech.
**Trending because:** 1 HuggingFace upvotes + evaluates a synthetic-data route to fixed-voice Thai text-to-speech

---

### 14. How Far Can Synthetic Data Take Thai OCR?
**Authors:** Kunat Pipatanakul
**arXiv:** [arxiv.org/abs/2609.03595](https://arxiv.org/abs/2609.03595)
**Summary:** We investigate what makes synthetic OCR supervision transfer to real Thai documents and use the resulting insights to build Wayu-Paxa-OCR-Zero, a Thai OCR model adapted without OCR labels from real Thai document pages. Synthetic data provide exact labels at scale, but "realism" conflates source domain, page context, typography, spatial structure, and glyph variation.
**Trending because:** 1 HuggingFace upvotes + measures how far synthetic data can carry low-resource Thai OCR

---

### 15. Ambient @ EgoProactive 2026 : Proactive Egocentric Assistance with Visually Grounded Supervision
**Authors:** Logesh Kumar Umapathi
**arXiv:** [arxiv.org/abs/2609.07099](https://arxiv.org/abs/2609.07099)
**Summary:** We present our submission to the EgoProactive track of the ECCV 2026 Wearable AI Challenge, which ranked first in the large-model division and second in the <=2B division. The task requires a wearable assistant to decide after each eight-second segment of egocentric video whether to intervene or remain silent.
**Trending because:** 1 HuggingFace upvotes + uses visually grounded supervision for proactive wearable assistance

---

### 16. Ambient @ EgoLongQA 2026: Distilling Long-Video perception into a Sub-2B Model
**Authors:** Logesh Kumar Umapathi
**arXiv:** [arxiv.org/abs/2609.07154](https://arxiv.org/abs/2609.07154)
**Summary:** We describe our entry to the EgoLongQA track of the Wearable-AI Challenge in ECCV 2026, which placed first in the <=2B parameter division with 0.8279 on the held-out test set. Our system is a single 2B vision-language model that answers multiple-choice questions about ten-minute egocentric videos in one greedy forward pass; It is obtained by distilling the junior perception module of a tool-using agentic pipeline, not the agent itself into a small student, using teacher traces filtered to those that answered correctly.
**Trending because:** 1 HuggingFace upvotes + distills long-video perception into a sub-2B vision-language model

---

### 17. Studying Without a Syllabus: Task-Agnostic Environment Preprocessing
**Authors:** Vinay Samuel, Varun Ursekar, Vijay S. Kalmath, Apaar Shanker, Veronica Chatrath, Yuan Xue
**arXiv:** [arxiv.org/abs/2609.10824](https://arxiv.org/abs/2609.10824)
**Summary:** Before an LLM agent tackles tasks in a new environment, it can inspect available corpora and tools and construct reusable resources such as indices, scripts, or procedural guidance. Most automated adaptation methods, however, rely on task examples, trajectories, or evaluation feedback to decide what to build.
**Trending because:** 1 HuggingFace upvotes + investigates task-agnostic environment preprocessing for autonomous agents

---

### 18. TRACE: Trajectory-robust Admission with Evidence Ordering for Efficient GUI Agents
**Authors:** Yuhao Wang, Mu Qiao, Xindong Zhang, Yunzhi Zhuge, Lei Zhang, Huchuan Lu
**arXiv:** [arxiv.org/abs/2609.10297](https://arxiv.org/abs/2609.10297)
**Summary:** GUI agents accumulate high-resolution screenshots as the trajectory unfolds, increasing inference latency and memory usage. Training-free visual token pruning can reduce this cost, but cache reuse introduces a fundamental constraint.
**Trending because:** 0 HuggingFace upvotes + improves GUI-agent efficiency with evidence-ordered trajectory admission

---

### 19. Rethinking Heterogeneous System Disaggregation for Subquadratic Attention
**Authors:** Arya Tschand, Yaosheng Fu, Vikram Sharma Mailthody, Nicolai Oswald, Po-An Tsai, Ritchie Zhao, Oreste Villa, Vijay Janapa Reddi, Karu Sankaralingam
**arXiv:** [arxiv.org/abs/2609.13134](https://arxiv.org/abs/2609.13134)
**Summary:** Frontier language models are more aggressively using subquadratic attention to reduce the memory footprint and compute requirements during inference while still delivering frontier accuracy. While existing systems make dense attention-centric disaggregated serving decisions, we show that disaggregating inference around the unique arithmetic intensity and memory footprint of subquadratic attention LLMs can achieve significant throughput and energy efficiency gains on emerging DRAM-based and SRAM-only heterogeneous systems.
**Trending because:** 0 HuggingFace upvotes + proposes system disaggregation tailored to subquadratic attention workloads

---

### 20. Skill Issue: Lessons from Optimizing Repository SKILLs for Coding Agents
**Authors:** Mykhailo Kozyrev, Andrei Kozyrev, Anton Podkopaev
**arXiv:** [arxiv.org/abs/2609.12742](https://arxiv.org/abs/2609.12742)
**Summary:** Coding agents increasingly read repository knowledge from SKILLs --- plain \texttt{.md} files versioned alongside the code. Recent work synthesizes these files automatically, by optimizing the document against a benchmark.
**Trending because:** 0 HuggingFace upvotes + provides empirical lessons for optimizing repository skills used by coding agents
