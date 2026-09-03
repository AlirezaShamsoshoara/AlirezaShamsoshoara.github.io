---
title: "Daily AI Papers — September 3, 2026"
date: 2026-09-03
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-03/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-harnesses
  - multimodal-models
  - reinforcement-learning
---

### 1. Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills
**Authors:** Jianlyu Chen, Yuyang Hu, Hongjin Qian, Jiawei Liu, Wenqing Wei, Xiaolong Chen, Defu Lian, Zhicheng Dou, Chaozhuo Li, Qiwei Ye, Zheng Liu
**arXiv:** [arxiv.org/abs/2609.02749](https://arxiv.org/abs/2609.02749)
**Summary:** The authors identify operational knowledge embedded in repositories and papers as a missing layer for autonomous machine-learning research agents. Their DisCo agent distills this knowledge into reusable skills, producing a library of more than 5,000 verified skills and substantial gains across four research benchmarks under fixed model and execution budgets.
**Trending because:** 533 HuggingFace upvotes + major interest in reusable repository-derived skills for AI research agents

---

### 2. HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?
**Authors:** Yuhao Wu, Jingyuan Zhang, Jiajun Shi, Xinping Lei, Qingshui Gu, Yuxuan Zhang, Zexuan Wang, Chen He, Chen Huang, Maojia Song, Zhiyuan Zeng, Shaowen Wang, Jinkai Liu, Yunfeng Shi, Jiaheng Liu, Shen Yan, Wenhao Huang, Ge Zhang, Wenxuan Zhang
**arXiv:** [arxiv.org/abs/2609.01437](https://arxiv.org/abs/2609.01437)
**Summary:** HarnessDev evaluates whether language models can create complete agent execution systems and improve them from downstream feedback. Generated harnesses approach or exceed selected human references in writing and ML experimentation but lag in coding and research, while evolutionary gains remain unstable and transfer poorly across models.
**Trending because:** 259 HuggingFace upvotes + strong interest in agents that build and evolve their own execution harnesses

---

### 3. Aspire: Can Models Self-Evolve from Vague Goals?
**Authors:** Yuhao Wu, Jingyuan Zhang, Jiajun Shi, Yuxuan Zhang, Xinping Lei, Junting Zhou, Zexuan Wang, Yuchen Wu, Huan Zhou, Duo Wang, Yinzhu Piao, Yongchang Peng, Yunfeng Shi, Jin Chen, Zuo Wang, Jinkai Liu, Jiaheng Liu, Wenxuan Zhang, Shen Yan, Wenhao Huang, Ge Zhang
**arXiv:** [arxiv.org/abs/2608.31111](https://arxiv.org/abs/2608.31111)
**Summary:** ASPIRE tests whether agents can turn vague capability goals into self-directed data selection, training, validation, and harness changes without seeing downstream evaluation tasks. Current agents complete these loops, but weight-level gains are sparse and unstable, and even the strongest evolved harness remains below an engineered reference.
**Trending because:** 225 HuggingFace upvotes + attention on self-evolving models guided only by vague capability goals

---

### 4. SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models
**Authors:** Junchao Huang, Guian Fang, Shengju Qian, Xianghao Kong, Zhuoran Zhao, Wei Huang, Yihua Du, Zixin Zhang, Justin Cui, Yuchao Gu, Yukang Chen, Xinting Hu, Tianyu He, Shaoshuai Shi, Zhuotao Tian, Xin Wang, Mike Zheng Shou, Li Jiang
**arXiv:** [arxiv.org/abs/2609.02886](https://arxiv.org/abs/2609.02886)
**Summary:** SolarWM provides an open data engine, adaptation framework, and training recipe for interactive long-horizon video world models across heterogeneous datasets and model backbones. Its four causal models support real-time rollouts lasting minutes to hours after training only on five-second sequences, with the data, pipeline, recipes, weights, and framework released for reproducibility.
**Trending because:** 144 HuggingFace upvotes + interest in open long-horizon interactive video world models

---

### 5. EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction
**Authors:** Yuling Shi, Zhensu Sun, Junsen Dong, Chengcheng Wan, David Lo, Xiaodong Gu
**arXiv:** [arxiv.org/abs/2609.02783](https://arxiv.org/abs/2609.02783)
**Summary:** EarlyEval predicts agent success or failure from intermediate behavior so expensive benchmark runs can stop before completion. Across SWE-bench Verified, TerminalBench, and Toolathlon, it removes 13–26% of agent steps and up to 44.1% of input tokens while maintaining 89–97% prediction accuracy and nearly unchanged resolve rates.
**Trending because:** 116 HuggingFace upvotes + practical cost reductions for repeated agent benchmarking

---

### 6. It Takes Two to Match: Co-Evolving Generative Retriever with Reinforcement Learning
**Authors:** Runpeng Dai, Kaili Huang, Changsung Kang, Ciya Liao
**arXiv:** [arxiv.org/abs/2609.00638](https://arxiv.org/abs/2609.00638)
**Summary:** CoGR trains language models to generate compact keyword representations for both queries and items, which are matched through a conventional inverted index. Alternating reinforcement learning co-evolves both generators and improves F1 over the strongest baseline by 10.9% on an internal marketplace dataset and 36.1% on WANDS.
**Trending because:** 72 HuggingFace upvotes + a reinforcement-learning approach to co-evolving query and item retrieval

---

### 7. Language Models Can Control Their Own Attention
**Authors:** Namgyu Ho, Huzama Ahmad, Woosung Koh, Se-Young Yun, Tal Schuster, Cicero Nogueira dos Santos
**arXiv:** [arxiv.org/abs/2609.02737](https://arxiv.org/abs/2609.02737)
**Summary:** Declarative Attention lets a language model explicitly choose global, focused, or local attention regions while generating, allowing the inference engine to skip most KV-cache reads. Zero-shot tests on 15 long-context tasks reduce attended tokens by 31.1–52.0% with accuracy drops of only 1.27–2.75 percentage points.
**Trending because:** 66 HuggingFace upvotes + a model-directed route to reducing long-context attention cost

---

### 8. S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?
**Authors:** Jiajun Shi, Siyuan Tao, Yuhao Wu, Zexuan Wang, Jingyuan Zhang, Jiaheng Liu, Xinping Lei, Xinrong Zhang, Siyuan Fang, Zhewen Tan, Tianle Cai, Junhao Fang, Jiameng Huang, Yueyang Wang, Jinkai Liu, Yuxuan Zhang, Jian Yang, Zhoujun Li, Shen Yan, Wenhao Huang, Ge Zhang
**arXiv:** [arxiv.org/abs/2608.31100](https://arxiv.org/abs/2608.31100)
**Summary:** S3Gym evaluates whether language-model agents can test their own behavior, judge the resulting experience, and turn it into improved policies across seven executable text games. History, summary memory, and parameter training can each help, but their effectiveness depends strongly on task structure and may suffer unstable gains or negative transfer.
**Trending because:** 38 HuggingFace upvotes + a benchmark for turning agent experience into reliable self-improvement

---

### 9. On the Design Fundamentals of Pixel Text Representation Learning
**Authors:** Chaohao Yuan, Ruifeng Yuan, Zhuoxu Huang, Yu Rong, Hong Cheng, Hou Pong Chan, Chenghao Xiao
**arXiv:** [arxiv.org/abs/2609.01147](https://arxiv.org/abs/2609.01147)
**Summary:** This study identifies variable resolutions, natural image-text grounding, layout-aware rendering, and a multilingual curriculum as key ingredients for pixel-based text representation learning. The resulting Pixel Linguist II encoder sets new results on visual semantic similarity and document retrieval tasks while remaining robust under 80% visual-token compression.
**Trending because:** 32 HuggingFace upvotes + new design guidance for multilingual pixel-text encoders

---

### 10. WHALE: A Simple Recipe for Joint Harness-Weight Optimization
**Authors:** Haechan Kim, Yoonho Lee, Gisang Lee, Chelsea Finn, Kangwook Lee
**arXiv:** [arxiv.org/abs/2609.00196](https://arxiv.org/abs/2609.00196)
**Summary:** WHALE alternates model-weight updates with executable harness search so neither component remains a fixed bottleneck for agent performance. On search, mathematics, and chess tasks with Qwen3.5 agents, the method beats weight-only, harness-only, and Fast-Slow Training baselines by 4.15–24.38 percentage points in best mean-at-eight accuracy.
**Trending because:** 31 HuggingFace upvotes + joint optimization of agent weights and executable harness code

---

### 11. Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering
**Authors:** Hangrui Xu, Zhengxian Wu, Yunyao Yu, Zhuohong Chen, Rui Cong, Xiangwen Deng, Zhifang Liu, Peng Jiao, Haoqian Wang
**arXiv:** [arxiv.org/abs/2608.21450](https://arxiv.org/abs/2608.21450)
**Summary:** KBMR replaces CLIP-style visual similarity retrieval with a multimodal-language-model embedding space designed to preserve entity identity for knowledge-based visual question answering. A semantic discriminator supplies continuous entity-consistency weights, yielding up to 14.7% higher Recall@1 and 9.4% higher end-to-end VQA accuracy than CLIP baselines.
**Trending because:** 29 HuggingFace upvotes + entity-aware multimodal retrieval for knowledge-grounded VQA

---

### 12. NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for Efficient Fine-Tuning and Inference
**Authors:** Aurélien Lac, Tony Wu
**arXiv:** [arxiv.org/abs/2609.01657](https://arxiv.org/abs/2609.01657)
**Summary:** NeoMME is a family of 260M- and 800M-parameter single-tower bidirectional encoders that jointly process multilingual text and raw image patches. Its retrieval variants achieve strong ViDoRe v3 results, higher page-encoding throughput than a comparable baseline, and 255-fold embedding compression while retaining over 95% of baseline retrieval quality.
**Trending because:** 26 HuggingFace upvotes + efficient single-tower multilingual multimodal encoders

---

### 13. ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes
**Authors:** Mingda Lin, Weijie Wang, Zeyu Zhang, Bowen Cui, Yefei He, Haoyu Zhao, Yuanyu He, Donny Y. Chen, Feng Chen, Bohan Zhuang
**arXiv:** [arxiv.org/abs/2609.01740](https://arxiv.org/abs/2609.01740)
**Summary:** ZipTok3D organizes object geometry into progressively informative global-token prefixes and reconstructs fine detail through iterative decoding. It matches a 32-token baseline on ShapeNet with one token and on TRELLIS with four tokens, cutting sequence lengths by 32-fold and eight-fold respectively.
**Trending because:** 25 HuggingFace upvotes + extreme compression for high-fidelity 3D tokenization

---

### 14. Cliff: Learning Process Rewards from the First Mistake
**Authors:** Peixuan Han, Runhui Wang, Ketan Ramaneti, Jie Hao, Gerald Friedland, Chris Kong
**arXiv:** [arxiv.org/abs/2609.02817](https://arxiv.org/abs/2609.02817)
**Summary:** Cliff uses a teacher language model to identify the first mistake in a reasoning rollout, rewarding the valid prefix and applying negative feedback afterward. Across 12 scenarios, this simple process-level shaping improves reasoning performance by 15% over on-policy distillation and 7% over standard GRPO.
**Trending because:** 18 HuggingFace upvotes + fine-grained reward shaping from the first reasoning error

---

### 15. A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss
**Authors:** Suryaansh Jain, Rahasya Barkur, Vishal G, Ryan Rossi, Franck Dernoncourt, Jack Wang, Koustava Goswami, Nedim Lipka, Puneet Mathur, Samyadeep Basu, Seunghyun Yoon
**arXiv:** [arxiv.org/abs/2609.00591](https://arxiv.org/abs/2609.00591)
**Summary:** SimLoss aligns a captioning model's hidden representation with a frozen image embedding, providing dense visual supervision before text decoding without reference captions. Its differentiable variant delivers the strongest precision and nearly matches a multi-stage method's F1 while preserving single-pass inference and running about 20 times faster.
**Trending because:** 17 HuggingFace upvotes + single-pass detailed captioning with dense visual supervision

---

### 16. Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation
**Authors:** Run Yang, Runpeng Dai, Jie Sun, Jielei Zhang, Fan Zhou, Hongtu Zhu, Peiyi Li, Longwen Gao
**arXiv:** [arxiv.org/abs/2608.29846](https://arxiv.org/abs/2608.29846)
**Summary:** The paper traces diversity loss in sampled-token on-policy distillation to entropy-contracting update positions using a first-order local influence measure. IDA-OPD preserves entropy-expanding updates and shrinks harmful ones, improving pass-at-k while maintaining pass-at-one and avoiding full-vocabulary teacher probabilities.
**Trending because:** 16 HuggingFace upvotes + preserving reasoning diversity during on-policy distillation

---

### 17. VibeVoice-ASR-Streaming Technical Report
**Authors:** Yujie Tu, Zhiliang Peng, Jianwei Yu, Li Dong, Songchen Xu, Yaoyao Chang, Wenhui Wang, Zilong Wang, Zehua Wang, Yan Xia, Jiajun Zhang, Xie Chen, Furu Wei
**arXiv:** [arxiv.org/abs/2609.02812](https://arxiv.org/abs/2609.02812)
**Summary:** VibeVoice-ASR-Streaming unifies low-latency speech recognition and speaker attribution in an end-to-end language-model system that processes chunked audio with limited lookahead. Its 7B model achieves the best average transcription error across five datasets and the best or tied-best speaker attribution in 12 of 13 settings, with 1.5B and 7B weights released.
**Trending because:** 16 HuggingFace upvotes + streaming speaker-attributed ASR for real-time assistants

---

### 18. Institutional Newspapers Pipeline: Deriving billions of high quality tokens from historical newspapers
**Authors:** Matteo Cargnelutti, Catherine Brobston, Eben English, Jake Sadow, Kacie Bailey, Greg Leppert, Amanda Watson, Jessica Chapel, Jonathan Zittrain
**arXiv:** [arxiv.org/abs/2608.18972](https://arxiv.org/abs/2608.18972)
**Summary:** The Institutional Newspapers Pipeline converts difficult historical newspaper scans into structured, searchable datasets through segmentation, OCR, classification, entity recognition, language detection, and embeddings. Applied to Boston Public Library holdings, it produced 16.3 billion tokens from 83.1 million crops across more than 1.47 million public-domain scans.
**Trending because:** 11 HuggingFace upvotes + an open pipeline unlocking billions of historical-news tokens

---

### 19. Post-Training Language Models for Gold-Medal Performance in Coding Competitions
**Authors:** Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi, Somshubra Majumdar, Boris Ginsburg
**arXiv:** [arxiv.org/abs/2609.02849](https://arxiv.org/abs/2609.02849)
**Summary:** The authors combine curated competition problems, synthetic reasoning traces, supervised fine-tuning, reinforcement learning, and iterative test-time correction to specialize language models for competitive programming. Their Ultra-CC system scored 535.4 out of 600 under IOI 2026 constraints, exceeding both the gold threshold and the top human score.
**Trending because:** 10 HuggingFace upvotes + language models exceeding top human performance under IOI constraints

---

### 20. MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information Retrieval
**Authors:** Seokwon Song, Sohyeon Kim, Gunhee Kim
**arXiv:** [arxiv.org/abs/2608.30949](https://arxiv.org/abs/2608.30949)
**Summary:** Multi3IR benchmarks retrieval for open-ended queries whose relevant perspectives span multiple domains and modalities, using 104,900 Stack Exchange questions with perspective annotations. The accompanying SPIN method learns lightweight noise vectors that improve perspective coverage and generalize to unseen open-ended retrieval benchmarks.
**Trending because:** 8 HuggingFace upvotes + multi-perspective retrieval across domains and modalities

---
