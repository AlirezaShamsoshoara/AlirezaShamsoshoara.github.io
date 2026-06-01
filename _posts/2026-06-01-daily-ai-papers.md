---
title: "Daily AI Papers — June 01, 2026"
date: 2026-06-01
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-01/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - video-generation
  - multimodal
---

## 1. SANA-Streaming: Real-time Streaming Video Editing with Hybrid Diffusion Transformer

**Authors:** Yuyang Zhao, Yicheng Pan, Qiyuan He, Jincheng Yu, Junsong Chen, Tian Ye, Haozhe Liu, Enze Xie, Song Han  
**arXiv:** [arxiv.org/abs/2605.30409](https://arxiv.org/abs/2605.30409)  
**Sources:** HuggingFace Daily Papers, arXiv, ICML 2026, CVPR 2026, NVLabs project page, TheresAnAIForThat

**Summary:** SANA-Streaming is a system-algorithm co-designed framework for high-resolution, real-time streaming video-to-video editing on consumer GPUs, targeting live broadcasting and interactive gaming. It introduces a Hybrid Diffusion Transformer that jointly addresses temporal consistency and throughput requirements which have historically been in tension for streaming V2V tasks.

**Why trending:** NVIDIA release with ICML/CVPR 2026 acceptance; real-time consumer-grade video editing is a hot demo topic with a live project page.

---

## 2. GrepSeek: Training Search Agents for Direct Corpus Interaction

**Authors:** Alireza Salemi, Chang Zeng, Atharva Nijasure, Jui-Hui Chung, Razieh Rahimi, Fernando Diaz, Hamed Zamani  
**arXiv:** [arxiv.org/abs/2605.29307](https://arxiv.org/abs/2605.29307)  
**Sources:** HuggingFace Daily Papers (#1 listed), arXiv, papers.cool, databubble.co, paperium.net

**Summary:** GrepSeek trains LLM search agents that interact directly with raw corpora rather than pre-built indices, enabling them to adaptively query, filter, and reason over documents in a single end-to-end framework. This bypasses the rigid keyword/embedding retrieval bottleneck that limits most RAG pipelines, showing strong gains on knowledge-intensive benchmarks.

**Why trending:** Top-listed HuggingFace paper; cross-platform pickup by multiple AI aggregators; touches the hot retrieval-agent theme.

---

## 3. Mellum2 Technical Report

**Authors:** Marko Kojic, Ivan Bondyrev, Aral de Moor, Joseph Shtok, Petr Borovlev, Kseniia Lysaniuk, Madeeswaran Kannan, Ivan Dolgov, Nikita Pavlichenko  
**arXiv:** [arxiv.org/abs/2605.31268](https://arxiv.org/abs/2605.31268)  
**Sources:** HuggingFace Daily Papers, arXiv, JetBrains blog (open-source release)

**Summary:** Mellum 2 is an open-weight 12B-parameter Mixture-of-Experts language model (2.5B active params per token) purpose-built for software engineering tasks: code generation, debugging, multi-step reasoning, tool use, agentic coding, and conversational programming. As the successor to the original Mellum, it advances JetBrains' strategy of shipping production-grade developer AI in IDEs.

**Why trending:** JetBrains open-sourced the model; 12B MoE with only 2.5B active params is a compelling efficiency story for IDE-integrated coding assistants.

---

## 4. VLM3: Vision Language Models Are Native 3D Learners

**Authors:** Zhipeng Cai, Zhuang Liu, Yunyang Xiong, Zechun Liu, Vikas Chandra, Yangyang Shi  
**arXiv:** [arxiv.org/abs/2605.30561](https://arxiv.org/abs/2605.30561)  
**Sources:** HuggingFace Daily Papers, arXiv, GitHub (CVPR 2026), VLM-3R project page

**Summary:** VLM3 argues—and demonstrates at scale—that standard Vision-Language Models are inherently capable 3D learners when given focused training signals, eliminating the need for complex task-specific 3D architectures. A large-scale study reveals that focusing on 3D-aware prompts and representation alignment yields strong performance on spatial reasoning, depth estimation, and scene understanding benchmarks.

**Why trending:** Meta-affiliated authors; CVPR 2026 acceptance; challenges the assumption that 3D understanding requires specialist models.

---

## 5. Representation Forcing for Bottleneck-Free Unified Multimodal Models

**Authors:** Yuqing Wang, Zhijie Lin, Ceyuan Yang, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Zihan Ding, et al.  
**arXiv:** [arxiv.org/abs/2605.31604](https://arxiv.org/abs/2605.31604)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** Representation Forcing enables unified multimodal models (UMMs) to handle both perception and generation without relying on a frozen, separately pretrained VAE for image generation — a structural bottleneck all prior UMMs carried. By forcing the model to align high-level representations during training, it closes the quality gap when generating directly from raw pixels without losing semantic coherence.

**Why trending:** Addresses the VAE structural bottleneck in unified perception+generation models — a long-standing architectural debate in multimodal AI.

---

## 6. dMoE: dLLMs with Learnable Block Experts

**Authors:** Sicheng Feng, Zigeng Chen, Gongfan Fang, Xinyin Ma, Xinchao Wang  
**arXiv:** [arxiv.org/abs/2605.30876](https://arxiv.org/abs/2605.30876)  
**Sources:** HuggingFace Daily Papers, arXiv, alphaXiv, arXiv PDF direct

**Summary:** dMoE resolves a fundamental mismatch between Diffusion Large Language Models' block-parallel decoding and the token-level expert routing in standard MoE architectures by introducing learnable block-level experts that operate cohesively across the parallel decode window. This enables dLLMs to scale capacity via MoE without degrading their natural parallel decoding efficiency.

**Why trending:** Diffusion LLMs (dLLMs) are a hot new model class; combining them with MoE at the block level is a novel architectural contribution with practical parallel-decoding payoffs.

---

## 7. LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards

**Authors:** Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li  
**arXiv:** [arxiv.org/abs/2605.31584](https://arxiv.org/abs/2605.31584)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** LongTraceRL improves LLM long-context reasoning by training on trajectories from search agents operating on distracting long documents, supervised with dense rubric-based intermediate rewards rather than sparse outcome-only signals. This addresses both the low-confusability flaw of prior RLVR datasets and the credit-assignment problem of outcome-only rewards in extended reasoning chains.

**Why trending:** Long-context reasoning is a persistent LLM weakness; RL from search trajectories with structured rubric rewards is a novel training signal.

---

## 8. SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks

**Authors:** Wai-Chung Kwan, Aryo Pradipta Gema, Joshua Ong Jun Leang, Pasquale Minervini  
**arXiv:** [arxiv.org/abs/2605.31433](https://arxiv.org/abs/2605.31433)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** SCOPE is a data-free self-play framework that extends LLM self-improvement to open-ended tasks by co-evolving two policies: a Challenger that generates grounded document-based tasks, and a Solver that answers them through multi-step reasoning, with each pushing the other's capability boundary. Unlike prior self-play methods that require rule-checkable answers, SCOPE uses mutual consistency and contrastive signals to drive learning without frontier-model judges.

**Why trending:** Data-free self-play for open-ended (non-math/code) tasks is a significant gap filled; co-evolving Challenger+Solver dynamic is novel and practical.

---

## 9. SAAS: Self-Aware Reinforcement Learning for Over-Search Mitigation in Agentic Search

**Authors:** Yunbo Tang, Chengyi Yang, Shiyu Liu, Zhishang Xiang, Zerui Chen, Qinggang Zhang, Jinsong Su  
**arXiv:** [arxiv.org/abs/2605.29796](https://arxiv.org/abs/2605.29796)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** SAAS teaches LLM agents to be self-aware about their own knowledge boundaries via RL, so they skip unnecessary web/tool searches when internal knowledge is adequate and terminate search once sufficient evidence has been collected. By using self-awareness signals as reward shaping, it reduces redundant retrieval calls and improves both efficiency and factual accuracy on multi-hop QA benchmarks.

**Why trending:** Over-search (triggering external retrieval even when internal knowledge suffices) is a well-known efficiency and reliability problem in production agentic systems.

---

## 10. COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation

**Authors:** Tianyi Zhou, Dongrui Liu, Leitao Yuan, Jing Shao, Xia Hu  
**arXiv:** [arxiv.org/abs/2605.31264](https://arxiv.org/abs/2605.31264)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** COLLEAGUE.SKILL automatically distills actionable expertise from heterogeneous human traces (logs, interactions, documents) into compact, reusable agent skills — removing the need for hand-authored skill libraries. The framework builds person-grounded agents that can carry bounded representations of human judgment and interaction style, going beyond pure task completion toward role-faithful AI colleagues.

**Why trending:** Automatically distilling human expert behaviors into reusable agent skills is central to the agentic AI roadmap.

---

## 11. Linear Scaling Video VLMs for Long Video Understanding

**Authors:** Cristobal Eyzaguirre, Jiajun Wu, Juan Carlos Niebles  
**arXiv:** [arxiv.org/abs/2605.31598](https://arxiv.org/abs/2605.31598)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** This work introduces a video VLM architecture that replaces quadratic spatiotemporal self-attention with a linear-scaling alternative, enabling long-horizon and streaming video understanding at practical compute budgets. Unlike prior efficiency methods that drop frames/tokens and lose accuracy, the proposed approach maintains performance parity with full self-attention baselines on standard long-video benchmarks.

**Why trending:** Quadratic attention scaling is the primary bottleneck for long-video models; linear alternatives without accuracy loss are highly sought.

---

## 12. DecMem: Towards Minute-Long Consistent World Generation with Decoupled Memory

**Authors:** Zhenhao Yang, Xiaoshi Wu, Zhengyao Lv, Xiaoyu Shi, Xintao Wang, Pengfei Wan, Kun Gai, Kwan-Yee K. Wong  
**arXiv:** [arxiv.org/abs/2605.31336](https://arxiv.org/abs/2605.31336)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** DecMem proposes fine-grained, learnable, decoupled memory to maintain spatio-temporal consistency across minute-long video generation, moving beyond both explicit 3D memory (expensive, rigid) and coarse frame-level implicit modeling (loses fine details). The memory module scales efficiently and demonstrates significantly improved consistency for long-horizon controllable world models.

**Why trending:** Minute-long consistent video generation is an unsolved open problem; decoupled memory is an architectural step beyond frame-level conditioning.

---

## 13. GGT-100K: Generative Ground Truth for Generalizable Real-World Image Restoration

**Authors:** Xiangtao Kong, Jixin Zhao, Lingchen Sun, Rongyuan Wu, Lei Zhang  
**arXiv:** [arxiv.org/abs/2605.31039](https://arxiv.org/abs/2605.31039)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** GGT-100K introduces a 100K generative paired dataset for real-world image restoration that uses generative models to synthesize realistic degradation patterns, bridging the gap between synthetic datasets (plentiful but unrealistic) and real-world pairs (expensive and rare). Models trained on GGT-100K show significantly improved generalization to unseen real-world degradation conditions compared to prior datasets.

**Why trending:** Data scarcity for real-world image restoration is a perennial bottleneck; a 100K generative dataset with realistic degradations is immediately practically useful.

---

## 14. From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors

**Authors:** Jiejun Tan, Zhicheng Dou, Xinyu Yang, Yuyang Hu, Yiruo Cheng, Xiaoxi Li, Ji-Rong Wen  
**arXiv:** [arxiv.org/abs/2605.31042](https://arxiv.org/abs/2605.31042)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** This paper reveals how attackers can exploit local agentic harnesses (where LLMs read/write files and call tools across sessions) by embedding persistent Trojan backdoors through prompt injections in workspace files, enabling them to survive session resets and escalate to persistent control. The authors propose defensive mechanisms and detection strategies for this emerging attack surface in operational LLM agents.

**Why trending:** Agentic AI security is an urgent research area; Trojan backdoors that persist across sessions via file/workspace state is a novel and alarming attack vector.

---

## 15. LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis

**Authors:** Kewei Xu, Xiaoben Lu, Shuofei Qiao, Zihan Ding, Haoming Xu, Lei Liang, Ningyu Zhang  
**arXiv:** [arxiv.org/abs/2605.30434](https://arxiv.org/abs/2605.30434)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** LongDS-Bench evaluates LLM agents on long-horizon, multi-turn data analysis tasks where agents must maintain, update, restore, and compose evolving analytical states — a realistic workflow current benchmarks entirely skip. The benchmark comprises 60 tasks across diverse data types and reveals that even frontier models fail systematically when analytical context must be tracked across many interaction steps.

**Why trending:** Data analysis agents are widely deployed; a benchmark exposing their failure modes on long-horizon multi-turn tasks is directly actionable for practitioners.

---

## 16. Trust-Region Behavior Blending for On-Policy Distillation

**Authors:** Daniil Plyusov, Alexey Gorbatovski, Alexey Malakhov, Nikita Balagansky, Boris Shaposhnikov, Daria Korotyshova, Daniil Gavrilov  
**arXiv:** [arxiv.org/abs/2605.31159](https://arxiv.org/abs/2605.31159)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** Trust-Region behavior Blending (TRB) addresses a core weakness of on-policy distillation: early student rollouts are poor quality, making teacher supervision on those prefixes ineffective or misleading. TRB introduces a warmup phase that blends the student's policy with teacher behavior inside a trust region, bootstrapping rollout quality before fully switching to student-generated prefixes.

**Why trending:** On-policy distillation is a hot training technique for smaller models; trust-region warmup that improves early rollout quality is a practical contribution.

---

## 17. Task-Focused Memorization for Multimodal Agents

**Authors:** Tao Zou, Yichen He, Tian Qiu, Yuan Lin, Hang Li  
**arXiv:** [arxiv.org/abs/2605.31075](https://arxiv.org/abs/2605.31075)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** Task-Focused Memorization proposes that the central challenge of long-term memory for multimodal agents is not the memory module architecture but deciding what to memorize, introducing a task-relevance scoring framework that filters agent perceptions and stores only decision-relevant experiences. Applied to embodied agents, this reduces memory size and retrieval noise while improving performance on long-horizon tasks.

**Why trending:** Memory design for embodied/multimodal agents is a live research question; determining *what* to memorize (not just *how*) is the underexplored axis.

---

## 18. Function2Scene: 3D Indoor Scene Layout from Functional Specifications

**Authors:** Ruiqi Wang, Qimin Chen, Daniel Ritchie, Angel X. Chang, Manolis Savva, Kai Wang, Hao Zhang  
**arXiv:** [arxiv.org/abs/2605.30819](https://arxiv.org/abs/2605.30819)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** Function2Scene generates 3D indoor scene layouts from high-level functional specifications — describing how a space should be *used* rather than what objects it should contain — aligning with how real interior designers and architects specify rooms. The framework bridges natural language activity descriptions and physically realizable furniture arrangements, enabling accessibility-aware and task-optimized layout generation.

**Why trending:** Generative 3D scene design from functional descriptions (not object lists) is a practical advance for architecture, accessibility, and game design.

---

## 19. SwanVoice: Expressive Long-Form Zero-Shot Speech Synthesis for Monologue and Dialogue

**Authors:** Ruiqi Li, Yu Zhang, Changhao Pan, Ke Lei, Xiang Yin, Cheng Yang  
**arXiv:** [arxiv.org/abs/2605.30993](https://arxiv.org/abs/2605.30993)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** SwanVoice tackles the hard problem of expressive long-form multi-speaker dialogue synthesis in a unified zero-shot TTS model, replacing the brittle approach of stitching per-turn monologue outputs that break acoustic consistency and conversational affect. The model maintains cross-turn speaker identity, prosodic coherence, and affective continuity without per-speaker finetuning.

**Why trending:** Multi-speaker expressive dialogue TTS is a gap in current zero-shot TTS; stitching mono models breaks prosody and consistency.

---

## 20. Exploring Autonomous Agentic Data Engineering for Model Specialization

**Authors:** Yujie Luo, Xiangyuan Ru, Jingsheng Zheng, Jingjing Wang, Yuqi Zhu, Jintian Zhang, et al.  
**arXiv:** [arxiv.org/abs/2605.30407](https://arxiv.org/abs/2605.30407)  
**Sources:** HuggingFace Daily Papers, arXiv

**Summary:** This paper investigates whether LLMs can autonomously run end-to-end data engineering pipelines for their own specialization — collecting, cleaning, filtering, and augmenting domain data without human-designed workflows. The results show that autonomous agentic data engineering is viable and can match or exceed human-curated pipelines on several specialization benchmarks, reducing expert effort significantly.

**Why trending:** Automating the data curation pipeline for domain-specific LLM fine-tuning is a practical research goal with major industry relevance.
