---
title: "Daily AI Papers — September 16, 2026"
date: 2026-09-16
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-16/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-agents
  - multimodal-ai
  - efficient-ai
---

### 1. LongCat-Video Technical Report
**Authors:** Meituan LongCat Team, Xunliang Cai, Qilong Huang, Zhuoliang Kang, Hongyu Li, Shijun Liang, Liya Ma, Siyu Ren, Xiaoming Wei, Rixu Xie, Tong Zhang
**arXiv:** [arxiv.org/abs/2510.22200](https://arxiv.org/abs/2510.22200)
**Summary:** Video generation is a critical pathway toward world models, with efficient long video inference as a key capability. Toward this end, we introduce LongCat-Video, a foundational video generation model with 13.6B parameters, delivering strong performance across multiple video generation tasks.
**Trending because:** 41 HuggingFace upvotes + introduces a 13.6B foundation model aimed at efficient long-video generation

---

### 2. Learning to Solve Hard Problems in RL for LLMs by Never Giving Up
**Authors:** Michael Noukhovitch, Hamish Ivison, Nathan Lambert, Aaron Courville
**arXiv:** [arxiv.org/abs/2609.13443](https://arxiv.org/abs/2609.13443)
**Summary:** We demonstrate that training LLMs with RL does not improve performance equally across a dataset. RL shows large improvements on easy problems that an LLM is already good at solving, but small improvements on hard problems.
**Trending because:** 8 HuggingFace upvotes + targets hard-problem RL for LLMs by preventing difficult examples from being abandoned

---

### 3. Pick Your Poison: Learning to Select Poison Sets for Stronger LLM Backdoor Attacks
**Authors:** Aashiq Muhamed, Mona T. Diab, Virginia Smith, Andrew Ilyas, Matthew Jagielski
**arXiv:** [arxiv.org/abs/2609.15029](https://arxiv.org/abs/2609.15029)
**Summary:** Backdoor poisoning attacks add poisoned examples to otherwise-clean finetuning data, pairing a trigger with a target behavior that the model learns to produce when the trigger appears. Existing evaluations typically fix the number of poisoned examples and sample them at random from a candidate pool.
**Trending because:** 7 HuggingFace upvotes + learns which poison sets make LLM backdoor attacks stronger

---

### 4. Dynin-Robotics: Omnimodal Unified Diffusion Vision-Language-Action Model
**Authors:** Hoeun Lee, Jaeik Kim, Jusang Oh, Jinhyeok Kim, Geon Choi, Hyeonggeun Kim, Jaeyoung Do
**arXiv:** [arxiv.org/abs/2609.13053](https://arxiv.org/abs/2609.13053)
**Summary:** Visual goal and dynamics prediction can provide language-conditioned robot policies with both a target outcome and a representation of action-dependent scene changes. We bring these predictions into action generation and selection through a shared trajectory model.
**Trending because:** 6 HuggingFace upvotes + unifies visual goals, dynamics prediction, and robot action generation

---

### 5. Expert-Space Exploration in MoE Reinforcement Learning
**Authors:** Hongyi He, Zhenghao Lin, Xiao Liu, Peng Cheng, Yan Lu, Yeyun Gong
**arXiv:** [arxiv.org/abs/2609.13058](https://arxiv.org/abs/2609.13058)
**Summary:** Reinforcement learning (RL) has become central to post-training of large language models. Recent advances in RL for Mixture-of-Experts (MoE) models have primarily focused on improving optimization stability and training efficiency, while treating the expert selection as a fixed component.
**Trending because:** 5 HuggingFace upvotes + opens expert routing itself to exploration during MoE reinforcement learning

---

### 6. Enabling Creative Exploration for Vibe Design Agents
**Authors:** Yifan Zhang, Nghi D. Q. Bui, Georgios Evangelopoulos, Arnaud Benard
**arXiv:** [arxiv.org/abs/2609.15078](https://arxiv.org/abs/2609.15078)
**Summary:** Vibe design agents turn natural-language briefs into rendered interfaces and frontend code. Yet a useful design agent should do more than produce one valid page: it should help users explore coherent alternatives.
**Trending because:** 5 HuggingFace upvotes + helps design agents explore coherent alternative interfaces instead of producing only one

---

### 7. Root-Cause Attribution Is a Search Problem: Continual Search for Long-Horizon Agent Failures
**Authors:** Harsh Raj, David Lee, Anas Mahmoud, Renxiong Wang, Razvan-Gabriel Dumitru, Chenguang Wang, Tong Zhao, Yunzhong He, Darvin Yi, Vipul Gupta
**arXiv:** [arxiv.org/abs/2609.13463](https://arxiv.org/abs/2609.13463)
**Summary:** The increasing deployment of AI agents in long-horizon tasks yields massive execution logs. Diagnosing failures within these records is crucial for reliability, as it transforms outcome-level signals into actionable interventions.
**Trending because:** 3 HuggingFace upvotes + frames root-cause attribution in long agent traces as continual search

---

### 8. Building a Production Greek-English Speech Recognizer
**Authors:** Christos Petrocheilos, Cleopatra Papadopoulou, Chris Porikis, Ioakeim Perros, Ayoub Kirouane, Themistoklis Nikolis
**arXiv:** [arxiv.org/abs/2609.13498](https://arxiv.org/abs/2609.13498)
**Summary:** We report a multi-month engineering program to build Sophea, a production bilingual Greek-English automatic speech recognition system. We evaluate the system against nine production gates covering Greek and English word error rate, language identification, and hallucinations on non-speech audio.
**Trending because:** 3 HuggingFace upvotes + documents a production bilingual Greek-English speech recognition system

---

### 9. Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement
**Authors:** Hongyao Tang, Yi Ma, Pengyi Li, Yifu Yuan
**arXiv:** [arxiv.org/abs/2609.13406](https://arxiv.org/abs/2609.13406)
**Summary:** When we speak of recursive self-improvement (RSI), are we speaking of a phenomenon, a mechanism, or a prospect? Towards autonomous and evolving intelligence, RSI is being claimed at many scales, while no single framework that formally describes these emerging instances exists.
**Trending because:** 2 HuggingFace upvotes + formalizes iterative policy improvement and recursive self-improvement in one framework

---

### 10. LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence
**Authors:** Xingxuan Zhang, Gang Ren, Hao Yuan, Hao Zou, Hongze Tan, Hui Wang, Jianhao Song, Jiansheng Li, Jiayao Zhang, Jinghan Zhang, Kaifang Li, Lang Mo, Li Mao, Mingchao Hao, Nuo Xu, Rui Ding, Ruiji Zhang, Shuyang Li, Siyu Mei, Tianyang Zhang, Weiyang Mu, Yancheng Dong, Yongxian Wei, Yuan Xue, Yuanrui Wang, Yue He, Zijia Yang, Ziyun Li, Dongzhe Li, Fuqiang Wang, Jiandong Liu, Jiawei Chen, Jiaxin Du, Kaijie Cheng, Kehan Li, Lei Sun, Linjun Zhou, Ningbo Dai, Qi Wang, Renzhe Xu, Shaoxing Du, Shumeng Yang, Wang Lu, Wenjing Chu, Xiannan Huang, Xiaoyu Lin, Xing Ai, Xinyan Han, Xuanyue Li, Xuanyue Su, Xukun Zhang, Yan Lu, Yaxin Zhang, Yi Qin, Yifei Huang, Yihan Xu, Yongle Lv, Yuanyuan Jiang, Yushan Han, Peng Cui
**arXiv:** [arxiv.org/abs/2609.17488](https://arxiv.org/abs/2609.17488)
**Summary:** We introduce LimiX-2, a new model in the LimiX family, developed through model and data scaling guided by our previously established scaling laws. LimiX-2 adopts the Contextual Mechanism Networks (CMNs) paradigm and is pretrained with Context-Conditional Masked Modeling (CCMM).
**Trending because:** 2 HuggingFace upvotes + scales contextual mechanism networks toward general structured-data intelligence

---

### 11. E2A-Bench: Benchmarking Evidence-to-Action Reliability in Financial Chart Reasoning
**Authors:** Xiaoya Wang, Yutong Xu, Junjie Wang
**arXiv:** [arxiv.org/abs/2609.14302](https://arxiv.org/abs/2609.14302)
**Summary:** Can financial vision-language models (VLMs) turn chart evidence into reliable action recommendations? Existing hallucination evaluations are mostly claim-centric; they assess whether generated statements are supported, but not whether evidence remains traceable through rationale, confidence, and final action.
**Trending because:** 2 HuggingFace upvotes + tests whether financial VLM evidence remains traceable through rationales and actions

---

### 12. Thought without systematicity? Evaluating reasoning models on rule induction tasks
**Authors:** Simon Schug, Brenden M. Lake
**arXiv:** [arxiv.org/abs/2609.13948](https://arxiv.org/abs/2609.13948)
**Summary:** A central tenet of human cognition is systematicity, the principle that understanding one concept is inherently tied to understanding close variations of that concept. Do reasoning models robustly exhibit such systematicity?
**Trending because:** 2 HuggingFace upvotes + probes systematicity in reasoning models through rule induction

---

### 13. Learning Sparse Decision Trees via Transformer Variational Auto-Encoders
**Authors:** Giacomo Fidone, Alessio Cascione, Riccardo Guidotti
**arXiv:** [arxiv.org/abs/2609.01430](https://arxiv.org/abs/2609.01430)
**Summary:** Decision trees are among the most widely used models in machine learning, largely due to their transparent decision logic, making them well-suited for high-stakes decision-making contexts. However, most existing learning algorithms focus on predictive performance, overlooking the joint optimization of other desirable properties, such as structural sparsity.
**Trending because:** 2 HuggingFace upvotes + jointly targets interpretable decision trees and structural sparsity

---

### 14. RelateAnything: Real-Time Open-Vocabulary Relation Prediction From Any Inputs
**Authors:** Maëlic Neau
**arXiv:** [arxiv.org/abs/2609.12552](https://arxiv.org/abs/2609.12552)
**Summary:** Open-vocabulary detection accepts any class list at inference, and promptable segmentation returns regions without class names: the taxonomy has left the model and become an input. Relation prediction has not.
**Trending because:** 1 HuggingFace upvotes + brings open-vocabulary prompting to relation prediction

---

### 15. Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models through Capability Composition
**Authors:** Yecheng Wu, Song Han, Han Cai
**arXiv:** [arxiv.org/abs/2609.14708](https://arxiv.org/abs/2609.14708)
**Summary:** A core goal of efficient reasoning is to improve the accuracy-efficiency frontier. However, jointly improving reasoning accuracy and inference efficiency can be challenging, as the two objectives can favor different reasoning behaviors.
**Trending because:** 1 HuggingFace upvotes + composes reasoning capabilities to improve the accuracy-efficiency frontier

---

### 16. OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy Learning
**Authors:** Xu Xu, Jinxiu Liu, Zhangbo Qiao, Jiaxing Lu, Xiangyu Zhang, Yubin Gu, Fangwei Ning, Yan Shi
**arXiv:** [arxiv.org/abs/2609.16057](https://arxiv.org/abs/2609.16057)
**Summary:** Unified multimodal large language models (MLLMs) and multi-agent systems have advanced visual generation. However, three limitations remain.
**Trending because:** 1 HuggingFace upvotes + uses symbolic policy learning to generalize visual-generation workflows

---

### 17. ModaLens: Measuring Image Sensitivity in Report-Conditioned Medical VLMs
**Authors:** Sebastián Andrés Cajas Ordóñez, Maximin Lange, Quang Bui, Anqi Peter Li, Felipe Ocampo Osorio, Rafi Al Attrach, Kushul Reddy Palakala, Sahil Kapadia, Zakaria Laouabdia Sellami, Xinyue Zhang, Ashley Zhang, Leo Anthony Celi
**arXiv:** [arxiv.org/abs/2609.15635](https://arxiv.org/abs/2609.15635)
**Summary:** A radiology report can already answer a clinical question, so it is hard to tell whether a vision-language model also uses the image. ModaLens, a paired image-swap audit, measures how report availability changes image sensitivity: MedGemma-27B on 3,199 paired MIMIC-CXR cases from 293 patients, all 14 questions per case (13 finding-specific and one composite), each image replaced by one from another study, usually of the same patient, with question and report fixed.
**Trending because:** 1 HuggingFace upvotes + audits whether medical VLMs truly use images when reports are available

---

### 18. JustFit: 200K-Token LLM Serving on a 24 GiB Laptop with Just-in-Time State Management
**Authors:** Yuhua Chen
**arXiv:** [arxiv.org/abs/2609.17475](https://arxiv.org/abs/2609.17475)
**Summary:** Capable open-weight models make local coding and reasoning attractive, but their context and execution state strain laptop memory. We present JustFit, an MLX-based inference runtime that combines KVExec for compressed KV execution, PhaseSwap for component residency, and StateTrans for state-preserving serving transitions.
**Trending because:** 0 HuggingFace upvotes + serves 200K-token contexts on a 24 GiB laptop through just-in-time state management

---

### 19. OPEN-1B: A Fully Auditable Training Run
**Authors:** John Donaghy, Brian Wilcox, Oğuzhan Ersoy, Shikhar Rastogi, Adam St Arnaud, Alexey Titov, Jordan Greenberg, Ben Fielding, Harry Grieve
**arXiv:** [arxiv.org/abs/2609.17380](https://arxiv.org/abs/2609.17380)
**Summary:** Open-source language models have a reproducibility problem. Despite releasing weights, training data, and recipes, none of them are provably reproducible due to the non-associativity of floating-point arithmetic.
**Trending because:** 0 recorded HuggingFace upvotes + publishes a fully auditable language-model training run focused on reproducibility

---

### 20. When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control
**Authors:** Ali Şenol
**arXiv:** [arxiv.org/abs/2609.17516](https://arxiv.org/abs/2609.17516)
**Summary:** Large language models can produce fluent answers when their factual support is weak. This paper introduces Chain-of-Self-Questioning (CoSQ), a prompt-only framework that makes answer commitment conditional on an explicit assessment of the information required to answer a question.
**Trending because:** 0 recorded HuggingFace upvotes + adds prompt-only self-questioning so LLMs can abstain when factual support is weak
