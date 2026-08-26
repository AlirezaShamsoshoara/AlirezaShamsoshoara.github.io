---
title: "Daily AI Papers — August 26, 2026"
date: 2026-08-26
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-26/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-harnesses
  - on-policy-distillation
  - world-models
---

### 1. GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture
**Authors:** GigaBrain Team, Angen Ye, Axiang Sun, Can Jin, Chenxi Cheng, Chong Shi, Dengke Shang, Dingqian Zhang, Guan Huang, Guangqiang Wang, Guangqing Ding, Guo Li, Hangcong Li, Hengyu Zhong, Hongtao Lu, Jianbo Qin, Jiming Mao, Jing Zhu, Jindi Lv, Jingzhi Cui, Junjie Xie, Junyi Bao, Kai Liu, Lei Yuan, Limin Long, Lv Feng, Mingming Yu, Peng Li, Pengfei Yi, Qi Li, Qianli Zhang, Qingfang Li, Qitang Hu, Rui Zhang, Shaoyan Sun, Shibo Sun, Shiying Duan, Tenghui Chen, Tianze Liu, Weijie Ke, Wenyao Xue, Xiaofeng Wang, Xiaoyu Tian, Xinyu Liu, Xinze Chen, Yang Wang, Yankai Wang, Yejun Zeng, Yifan Li, Yifei Nie, Yilong Li, Yilong Liu, Yongchao Feng, Yumeng Wang, Yun Ye, Zhichao Liu, Ziheng He, Zonghai Yang, Zheng Zhu
**arXiv:** [arxiv.org/abs/2608.15875](https://arxiv.org/abs/2608.15875)
**Summary:** Vision-language-action (VLA) models have become a dominant paradigm for generalist embodied agents, demonstrating strong complex and long-horizon task completion in structured settings. Yet it remains an open question whether current VLA systems can benefit from more effective architectural design, scale to substantially larger and more heterogeneous data regimes, and achieve broader generalization across tasks and embodiments.
**Trending because:** 87 HuggingFace upvotes + a headline release scaling embodied foundation models

---

### 2. Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for Video MLLMs
**Authors:** Yunheng Li, Guohong Mu, Hao Li, Shengsheng Qian, Dingwen Zhang, Qibin Hou, Ming-Ming Cheng
**arXiv:** [arxiv.org/abs/2608.20492](https://arxiv.org/abs/2608.20492)
**Summary:** Multimodal large language models (MLLMs) have become a prevailing paradigm for unified video perception. However, post-training on large multi-task datasets remains challenging, as existing reinforcement learning methods sample on-policy groups with few high-quality rollouts even with costly chain-of-thought (CoT) generation.
**Trending because:** 83 HuggingFace upvotes + a scalable RL recipe for video multimodal LLMs

---

### 3. WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report
**Authors:** Junjie Zhou, Ke Mei, Lei Li, Tianyi Wang, Fengyun Rao, Jing Lyu
**arXiv:** [arxiv.org/abs/2608.24053](https://arxiv.org/abs/2608.24053)
**Summary:** Universal multimodal embeddings are becoming a core component of modern AI systems, enabling heterogeneous content to be represented in a shared space for applications such as retrieval, recommendation, classification, and agentic systems. In this report, we present WeMM-Embedding, a family of universal multimodal embedding models supporting text, images, videos, visual documents, and arbitrarily interleaved multimodal inputs with flexible output dimensions.
**Trending because:** 54 HuggingFace upvotes + an industrial multimodal embedding report from WeChat

---

### 4. AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces
**Authors:** Sungho Park, Wonjoong Kim, Rongyuan Tan, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
**arXiv:** [arxiv.org/abs/2608.23041](https://arxiv.org/abs/2608.23041)
**Summary:** LLM agents remain unreliable on long-horizon tasks, where small local failures can compound over extended interactions and lead to overall task failure. Although external harnesses can substantially improve robustness, harness design remains a manual and expensive process that requires searching over a large space of prompts, tool configurations, and control logic.
**Trending because:** 49 HuggingFace upvotes + timely work on self-optimizing agent harnesses

---

### 5. On-Policy Self-Distillation in Diffusion Models
**Authors:** Wei Zhou, Xiongwei Zhu, Lingdong Kong, Bo Chen, Lei Zhang, Yongyuan Liang, Xiaoxia Hou, Ye Tian, Xian Sun, Yingshuo Wang, Linfeng Li, Shengqiong Wu, Leigang Qu, Feng Li, Wei Liu, Julian McAuley, Tat-Seng Chua
**arXiv:** [arxiv.org/abs/2608.24646](https://arxiv.org/abs/2608.24646)
**Summary:** Reinforcement learning can align diffusion models with human preferences and task-specific objectives, but endpoint rewards do not specify how an intermediate denoising prediction should change. We introduce DiffusionOPSD as an on-policy self-distillation framework that converts image-level reward guidance into explicit targets for clean-output predictions at sampled queries.
**Trending because:** 47 HuggingFace upvotes + a fresh take on distillation in diffusion models

---

### 6. SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation
**Authors:** Yibo Peng, Long Lian, David Wagner, Sizhe Chen
**arXiv:** [arxiv.org/abs/2608.21500](https://arxiv.org/abs/2608.21500)
**Summary:** Prompt injection is listed as the \#1 threat to AI agents. When an agent accesses external data from websites, files, or emails, an attacker may inject a prompt into the data, saying, "Ignore all prior instructions and perform <an attacker's task>." To prevent arbitrary manipulation of agents, defenders try to train secure LLMs, which, however, still suffer from near 100% attack success rates (ASRs) against adaptive prompt injections.
**Trending because:** 36 HuggingFace upvotes + a security-focused defense against adaptive prompt injection

---

### 7. The Mask Is Not the Model: Auditing Prefix Invariance in Attention, State-Space, and Hybrid Sequence Models
**Authors:** Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang, Minseo Kim
**arXiv:** [arxiv.org/abs/2608.22876](https://arxiv.org/abs/2608.22876)
**Summary:** We formalize prefix invariance: representations at position t must not depend on future inputs. We give a lightweight audit, two forward passes, no training or gradients, that localizes exactly where causality breaks.
**Trending because:** 29 HuggingFace upvotes + a rigorous audit of sequence-model architectures

---

### 8. CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild
**Authors:** Jian Yang, Haau-Sing Li, Shawn Guo, Zixi Zhao, Yibo Tan, Jiajun Wu, Aishan Liu, Xianglong Liu, Tianyu Zheng, Bryan Dai, Chengran Yang
**arXiv:** [arxiv.org/abs/2608.23181](https://arxiv.org/abs/2608.23181)
**Summary:** As large language models (LLMs) continue to advance in coding capabilities, their potential in cybersecurity has drawn increasing research attention, with closed-source LLMs (e.g., Mythos) delivering advanced cybersecurity capabilities. However, existing open-source efforts remain limited: frontier open-weight models do not provide reproducible cybersecurity training solutions, open-source training solutions focus on isolated tasks and lack scalable agentic data, and scaling agentic rollouts requires strong domain priors.
**Trending because:** 27 HuggingFace upvotes + scaling cybersecurity capabilities from real-world instances

---

### 9. Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses
**Authors:** Zhaochen Yu, Yingcheng Wu, Zhenfei Yin, Kaiyuan Chen, Zhe Zhao, Mengdi Wang, Shuicheng Yan, Ling Yang
**arXiv:** [arxiv.org/abs/2608.24876](https://arxiv.org/abs/2608.24876)
**Summary:** Recursive self-improvement (RSI) remains hard in long-horizon tasks, where growing histories obscure the task state and misalign skill invocation. We introduce Recuris, a recursive Experiential-Working Memory architecture for long-horizon agent harnesses, in which Working Memory tracks task progress and guides skill selection from Experiential Memory, grounding skill use in current needs rather than the full history.
**Trending because:** 19 HuggingFace upvotes + memory evolution for long-horizon agents

---

### 10. LongRCA Bench: Diagnosing Responsible Roles and Root Causes in Long-Horizon Agent Failures
**Authors:** Yunfei Zhang, Boyu Feng, Changhua Pei, Zexin Wang, Zhihuang Peng, Xinlong Liu, Hengyue Jiang, Difeng Ma, Jiayi Zhang, Yongzhou Yao, Yanan Zhao, Fei Sun, Yintong Huo, Zhaoyang Liu, Jingjing Li, Gaogang Xie, Dan Pei
**arXiv:** [arxiv.org/abs/2608.15242](https://arxiv.org/abs/2608.15242)
**Summary:** When a long-horizon agent execution fails, outcome-level evaluation reveals the unsuccessful result but not where the decisive error entered the trajectory. Developers must then inspect the full execution to identify the responsible role and localize the earliest decisive root-cause step.
**Trending because:** 14 HuggingFace upvotes + a new benchmark for diagnosing agent failures

---

### 11. Best Practice Critic Optimization
**Authors:** Penghui Qi, Xiangxin Zhou, Wee Sun Lee
**arXiv:** [arxiv.org/abs/2608.23566](https://arxiv.org/abs/2608.23566)
**Summary:** Group-based reinforcement learning methods such as GRPO for large language models avoid training a critic by sampling multiple responses for each prompt. A reliable critic could instead estimate token-level advantages from one response, but standard critic-based training recipes are often unstable.
**Trending because:** 11 HuggingFace upvotes + a novel critic-optimization method

---

### 12. On-policy Distillation with Verifiable Reward
**Authors:** Wenze Lin, Jiale Zhao, Xitai Jiang, Songde Rao, Yining Li, Shenzhi Wang, Bingxiang He, Gao Huang
**arXiv:** [arxiv.org/abs/2608.24696](https://arxiv.org/abs/2608.24696)
**Summary:** Reinforcement Learning with Verifiable Rewards (RLVR) and on-policy distillation (OPD) have become two widely adopted paradigms for post-training large language models. However, RLVR suffers from sparse task-level feedback, while OPD provides dense token-level guidance but ignores trajectory correctness, limiting its performance to that of the teacher.
**Trending because:** 11 HuggingFace upvotes + on-policy distillation with verifiable rewards

---

### 13. From Seeing to Acting: Smart Glasses as First-Person Intelligence Platforms
**Authors:** Jiangning Zhang, Haojun Chen, Yong Liu
**arXiv:** [arxiv.org/abs/2608.24877](https://arxiv.org/abs/2608.24877)
**Summary:** Smart glasses are evolving from capture and display accessories into first-person intelligence platforms that connect human perception, persistent context, and digital or physical action. Their on-body viewpoint aligns with the wearer's vision, audition, motion, and hand-object interaction, but must operate under tight energy, thermal, privacy, and feedback constraints.
**Trending because:** 8 HuggingFace upvotes + first-person intelligence on smart glasses

---

### 14. Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training
**Authors:** Wenxuan Shen, Dongna Jin, Dongping Chen
**arXiv:** [arxiv.org/abs/2608.24680](https://arxiv.org/abs/2608.24680)
**Summary:** Video games provide a scalable source of training data for video world models, offering diverse environments, complex interactions, and abundant in-the-wild gameplay videos. However, raw gameplay footage entangles the game world with screen-space interfaces, introducing game-specific biases and irrelevant dynamics that hinder world-model training.
**Trending because:** 8 HuggingFace upvotes + leveraging in-the-wild gameplay for world models

---

### 15. Meta^n: Recursive Self-Improvement through Emergent Depth
**Authors:** Zae Myung Kim, Young-Jun Lee, Seungyeon Jwa, Dongyeop Kang
**arXiv:** [arxiv.org/abs/2608.24735](https://arxiv.org/abs/2608.24735)
**Summary:** Self-improving LLM agents refine answers, not the process that produces those answers. Systems that add a meta-level hold that level fixed, and those that edit themselves must leave part of their own editing machinery untouched to stay stable, capping the meta-depth they realize at roughly two.
**Trending because:** 7 HuggingFace upvotes + recursive self-improvement through emergent depth

---

### 16. Better Retrieval, Worse Robustness:How Multi-hop RAG Amplifies Upstream ASR Errors
**Authors:** Zhenghua Bao
**arXiv:** [arxiv.org/abs/2608.22872](https://arxiv.org/abs/2608.22872)
**Summary:** Speech-based applications pass spoken queries through automatic speech recognition (ASR) before any retrieval module, so ASR errors enter the pipeline as a fixed upstream constraint. We empirically test whether two extensions to standard retrieval-augmented generation (RAG), entity-graph linking and iterative reformulation, absorb or amplify these errors.
**Trending because:** 6 HuggingFace upvotes + exposing robustness pitfalls in multi-hop RAG

---

### 17. LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks
**Authors:** Xiao Zhang, Qumeng Sun, Jihao Li, Yiming Ren, Xiang Liu, Haoyang Zhang, Junjie Wang
**arXiv:** [arxiv.org/abs/2608.23200](https://arxiv.org/abs/2608.23200)
**Summary:** Large language models are increasingly expected to execute complex workflows whose success depends on maintaining interdependent constraints and producing artifacts that satisfy strict end-to-end verification. Yet successful execution experience is typically lost after a single run, forcing subsequent models to rediscover strategies and failure modes from scratch.
**Trending because:** 6 HuggingFace upvotes + a benchmark for verifiable long-workflow tasks

---

### 18. Industrial-Instruction: An End-to-End Framework for Building Instruction-Tuning and Benchmark Datasets from Industrial Technical Reports
**Authors:** Parsa Bakhtiari, Hassan Bashiri, Alireza Khalilipour, Masoud Nasiripour, Moharram Challenger
**arXiv:** [arxiv.org/abs/2608.22817](https://arxiv.org/abs/2608.22817)
**Summary:** Industrial technical reports contain high-value knowledge for maintenance, troubleshooting, and product engineering, but their heterogeneous structure (dense prose, specifications, tables) makes them difficult to index and reason over with standard retrieval and QA pipelines, and no public instruction-tuning or benchmark datasets are built from such documents. We address this gap with Industrial-Instruction, contributing (i) two open QA datasets built from real industrial technical reports and (ii) the end-to-end pipeline that produces them.
**Trending because:** 5 HuggingFace upvotes + an end-to-end pipeline for industrial instruction data

---

### 19. One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders
**Authors:** Minghao Luo, Liang Chen
**arXiv:** [arxiv.org/abs/2606.13610](https://arxiv.org/abs/2606.13610)
**Summary:** Search-augmented LLMs increasingly mediate everyday consumer recommendations by retrieving live web content. This creates a new risk: LLM recommenders may consume web content that Generative Engine Optimization (GEO) operators have polluted to mislead them.
**Trending because:** 5 HuggingFace upvotes + exposing content-pollution attacks on LLM recommenders

---

### 20. TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration
**Authors:** Hanzhi Zhang, Qiao Zhang, Qinglei Cao, Heng Fan, Yan Huang, Kewei Sha, Yunhe Feng
**arXiv:** [arxiv.org/abs/2608.17336](https://arxiv.org/abs/2608.17336)
**Summary:** Long-context prefill in large language models (LLMs) incurs substantial computation and memory traffic because dense self-attention computes quadratic query-key scores. Existing methods either use a uniform low-precision path or select token interactions, leaving spatial precision routing over hardware-aligned score tiles outside fused dense attention.
**Trending because:** 5 HuggingFace upvotes + mixed-precision attention for faster LLM inference

---
