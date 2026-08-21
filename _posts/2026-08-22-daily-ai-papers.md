---
title: "Daily AI Papers — August 22, 2026"
date: 2026-08-22
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-22/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-evolution
  - benchmarks
  - video-understanding
---

### 1. PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments
**Authors:** Yuhao Zhan, Bingxiang He, Zecong Tang, Chaojun Xiao
**arXiv:** [arxiv.org/abs/2608.14441](https://arxiv.org/abs/2608.14441)
**Summary:** Self-evolving agents improve future behavior from interaction experience, yet existing evaluations typically optimize under fixed execution conditions and do not test recovery after those conditions change. To address this gap, we introduce PACE-Bench (Physics Adaptation via Code Evolution), a simulator-grounded benchmark of 144 source-to-target adaptation pairs across six physics domains.
**Trending because:** 27 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 2. Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses
**Authors:** Tailin Zhou
**arXiv:** [arxiv.org/abs/2608.08466](https://arxiv.org/abs/2608.08466)
**Summary:** Modern LLM agents are often improved by modifying prompts, tools, or workflows manually, while the executable scaffold surrounding the model---the harness---is typically treated as a fixed artifact after deployment. This work studies an alternative where the harness is task-specific and continuously evolvable: each task family maintains its own harness, which is hot-swapped across iterations through a fixed task-injection seam and rewritten using environment feedback.
**Trending because:** 9 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 3. NARU: A Benchmark for NARrative Evolution and Cultural Nuance Understanding in Japanese Extreme Long Video
**Authors:** Yuheng Huang, Jianlang Chen, Jiayang Song, Hua Qi, Aza Kai, Vincent Markert, Edison Marrese-Taylor, Jianjun Zhao, Lei Ma
**arXiv:** [arxiv.org/abs/2608.13210](https://arxiv.org/abs/2608.13210)
**Summary:** Long-form video understanding encompasses tasks that go beyond retrieving isolated events, including tracking an evolving narrative and interpreting social meaning that may remain implicit. However, existing benchmarks rarely evaluate these capabilities jointly, particularly in high-context, non-English media.
**Trending because:** 8 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 4. TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity
**Authors:** Armin Steinhauser
**arXiv:** [arxiv.org/abs/2608.15767](https://arxiv.org/abs/2608.15767)
**Summary:** We introduce TinyCast, an attention-free zero-shot forecaster that emits a predictive distribution from 146,505 parameters, on the premise that at this size the periodic structure of a context is worth computing rather than learning. A zero-parameter spectral detector supplies the dominant periods, the context is folded on their phase, and a dilated convolutional encoder and a block-autoregressive quantile decoder model the rest.
**Trending because:** 8 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 5. τ_0-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation
**Authors:** Xiaowei Cai, Yunuo Cai, Bingao Chen, Jingxiao Chen, Zhi Chen, Siyuan Feng, Tengyu Hou, Jingshun Huang, Han Jiang, Runkun Ju, Dong Li, Mingxiang Li, Shaowei Li, Xinchen Li, Yifan Li, Yi Liu, Zhongyuan Liu, Jianlan Luo, Junwen Miao, Ruiqi Ni, Buqing Nie, Mingjie Pan, Xinlin Ren, Jianheng Song, Jiaxu Wang, Peiqi Wang, Sen Wang, Xiaoyan Wang, Dafeng Wei, Dongming Wu, Pengwei Xie, Pu Yang, Hangjian Ye, Xiangyu Yue, Jinyu Zhang, Qinglin Zhang, Xueyong Zhao, Pengfei Zhou, Yue Zhou
**arXiv:** [arxiv.org/abs/2608.16885](https://arxiv.org/abs/2608.16885)
**Summary:** Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. Most hierarchical vision-language-action (VLA) models make each such decision with a single forward pass, leaving no mechanism to allocate additional computation to difficult or consequential choices.
**Trending because:** 8 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 6. StreamOPD: A Post-Training Recipe with Spatio-Temporal Cue Gating for Streaming Video Understanding
**Authors:** Keming Wu, Baoyi Wang, Kaichen Zhang, Xiang An, Zuhao Yang, Sudong Wang, Haowei Zhu, Tingxuan Huang, Hongcheng Gao, Bin Wang
**arXiv:** [arxiv.org/abs/2608.16320](https://arxiv.org/abs/2608.16320)
**Summary:** Streaming video understanding demands direct responses from the causally observed prefix of an unfolding video. Existing systems add inference-time memory, retrieval, and compression, yet a training-free sliding-window baseline already matches them.
**Trending because:** 8 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 7. AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation Model
**Authors:** Kwan Yun, Serin Yoon, Sunjin Jung, Jung Eun Yoo, Inyup Lee, Junyong Noh
**arXiv:** [arxiv.org/abs/2608.16143](https://arxiv.org/abs/2608.16143)
**Summary:** We present AnyTalk, a novel method for generating 3D speech animations for arbitrary characters without requiring any animation data. While existing audio-driven 3D speech animation methods rely on character-specific training data or laborious rigging/re-meshing, AnyTalk circumvents these limitations by leveraging recent video diffusion models trained on extensive video datasets.
**Trending because:** 8 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 8. The Embedder's Dilemma: LLMs Are Better, but at What Cost?
**Authors:** Adnan El Assadi, Niklas Muennighoff, Jinhyuk Lee
**arXiv:** [arxiv.org/abs/2608.12875](https://arxiv.org/abs/2608.12875)
**Summary:** Should you replace your text-embedding pipeline with a large language model? We answer this with a controlled, cost-aware comparison of ten LLMs across six families and 26 embedding models (118M to 14B parameters) on 37 tasks spanning classification, semantic textual similarity (STS), clustering, pair classification, and retrieval.
**Trending because:** 7 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 9. QuoteBench: How Matched Scores Can Hide Command-Path Failures
**Authors:** Shangao Li, Yao Zhang, Volker Tresp, Yuanyuan Yang
**arXiv:** [arxiv.org/abs/2608.13547](https://arxiv.org/abs/2608.13547)
**Summary:** LLM coding agents issue Bash commands through interfaces that may serialize, wrap, and reparse model output. Matched execution scores alone cannot distinguish command-generation errors from failures introduced after generation.
**Trending because:** 7 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 10. Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning
**Authors:** Xiaoyu Zhu, Xinke Deng, Suresh Taddewadikar, Arnab Kumar Mondal, Zhongyu Jiang, Ian Fasel, Joerg Liebelt
**arXiv:** [arxiv.org/abs/2608.15869](https://arxiv.org/abs/2608.15869)
**Summary:** Multimodal large language models increasingly use visual chain-of-thought (Visual CoT) to reason about spatial, temporal, and embodied environments. By generating intermediate reasoning images, Visual CoT provides an intuitive mechanism for visual foresight but introduces substantial inference overhead, which is particularly problematic for proactive video reasoning.
**Trending because:** 7 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 11. PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents
**Authors:** Seongjae Kang, Taehyung Yu, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2608.19861](https://arxiv.org/abs/2608.19861)
**Summary:** Customer-service LLM agents must follow organizational policy when acting on a user's behalf. Compliance failures arise from either forbidden actions, such as granting an ineligible change, or omitted procedural requirements, such as identification or confirmation.
**Trending because:** 7 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 12. ENTLORE: A Graph-Grounded Benchmark for Latent Organizational Reasoning in Enterprise Question Answering
**Authors:** Akrin Zheng, Alexander Wu, Alaia Liu
**arXiv:** [arxiv.org/abs/2608.10679](https://arxiv.org/abs/2608.10679)
**Summary:** Enterprise question answering is framed as retrieving internal documents and generating grounded answers. Routine enterprise records, however, are work by-products in which required organizational relations remain implicit across heterogeneous sources.
**Trending because:** 6 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 13. ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment in Visual Document Retrieval
**Authors:** Peng Chunyi, Xu Zhipeng, Yan Yukun, Liu Zhenghao, Yu Shi, Mei Sen, Sun Yubo, Zhang Yongheng, Zhou Jie, Gu Yu, Yu Ge, Sun Maosong
**arXiv:** [arxiv.org/abs/2608.15698](https://arxiv.org/abs/2608.15698)
**Summary:** Visual document retrieval is a critical component of multimodal retrieval-augmented generation, aiming to identify query-relevant pages from document collections where evidence is distributed across text, layout, charts, and visual structures. Recent efforts toward finer-grained supervision primarily rely on textual descriptions or localized visual regions as evidence proxies.
**Trending because:** 6 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 14. GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation
**Authors:** Julien Merand, Boris Meden, Mathieu Grossard, Liming Chen
**arXiv:** [arxiv.org/abs/2608.19759](https://arxiv.org/abs/2608.19759)
**Summary:** Multifingered grasping is a crucial robotic skill, but current deep-learning grasp planners often struggle to generalize to new objects because they are trained on limited, object-specific datasets. We introduce a fundamentally different approach, grounded in the observation that the gripper and the object share identical surface geometry at their mutual contact points.
**Trending because:** 6 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 15. CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning
**Authors:** Julien Merand, Boris Meden, Liming Chen, Mathieu Grossard
**arXiv:** [arxiv.org/abs/2608.19776](https://arxiv.org/abs/2608.19776)
**Summary:** Current dexterous grasp planners primarily optimize for physical stability, focusing on whether an object can be grasped rather than how it should be grasped to support downstream functional tasks. However, conditioning grasp synthesis on specific human grasp taxonomies typically requires prohibitively expensive, object-annotated datasets.
**Trending because:** 6 HuggingFace upvotes + one of the highest-upvoted fresh papers in the recent HuggingFace window

---

### 16. NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents
**Authors:** Peng Cai, Zhaofan Zou, Shifa Liu, Yikun Wang, Jiawei Tang, Kaicheng Yang, Meng Tong, Zhongjiang He, Hao Sun
**arXiv:** [arxiv.org/abs/2608.12898](https://arxiv.org/abs/2608.12898)
**Summary:** Document parsing aims to transform unstructured documents into structured and machine-readable representations. Recent advances in Vision-Language Models (VLMs) have significantly advanced document parsing.
**Trending because:** 5 HuggingFace upvotes + notable topical significance in the current HuggingFace papers feed

---

### 17. Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learners
**Authors:** Umberto Cappellazzo, Xubo Liu, Stavros Petridis, Maja Pantic
**arXiv:** [arxiv.org/abs/2608.19863](https://arxiv.org/abs/2608.19863)
**Summary:** Self-supervised learning (SSL) has driven substantial progress in audio representation learning, though existing methods have increasingly relied on elaborate pre-training recipes to reach competitive performance. A markedly different pre-training philosophy underpins the most influential progress in language modeling and, more recently, in visual representation learning: rather than train encoders as static feature extractors, models are trained to predict the next element, a discrete token or a continuous embedding, from the preceding context.
**Trending because:** 5 HuggingFace upvotes + notable topical significance in the current HuggingFace papers feed

---

### 18. DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs
**Authors:** Zeyu Cao, Xuan Guo, Cheng Zhang, Cheuk Hang Lau, Ilia Shumailov, Yiren Zhao
**arXiv:** [arxiv.org/abs/2608.14614](https://arxiv.org/abs/2608.14614)
**Summary:** As AI datacenters retire functional GPUs, vast quantities of still capable accelerators enter secondary markets. This paper investigates whether these retired GPUs can find a productive afterlife to form a DumpsterCluster that can serve modern LLM inference, and under what conditions such repurposing is economically viable and environmentally sustainable.
**Trending because:** 4 HuggingFace upvotes + notable topical significance in the current HuggingFace papers feed

---

### 19. Gathered, Not Admitted: How Attention Brings a Latent Variable into Verbalizable Form
**Authors:** Parsa Mazaheri
**arXiv:** [arxiv.org/abs/2608.15022](https://arxiv.org/abs/2608.15022)
**Summary:** Language models hold latent quantities in a form they can report on, and more of a quantity is present in that form when the task requires reusing it flexibly. What causes a representation to enter that form is open, and the word workspace invites an admission story: a gate that decides what gets in.
**Trending because:** 4 HuggingFace upvotes + notable topical significance in the current HuggingFace papers feed

---

### 20. Unifying Graph Neural Networks Through a Common Layer Equation
**Authors:** Sai Karthik Navuluru, Siddhartha Shankar Das, Bo Ni, Hongjie Chen, Yu Wang, Baris Coskunuzer, Nesreen K. Ahmed, Franck Dernoncourt, Mahantesh Halappanavar, Tyler Derr, Ryan A. Rossi, Lakshman Tamil
**arXiv:** [arxiv.org/abs/2608.16097](https://arxiv.org/abs/2608.16097)
**Summary:** Graph neural networks are commonly described through family-specific equations whose notation obscures shared computations and structural differences. We introduce a common layer equation that represents covered architectures through seven components: an update domain, channel set, propagation bank, per-channel message maps, channel-fusion operator, ego/residual map, and update map.
**Trending because:** 4 HuggingFace upvotes + notable topical significance in the current HuggingFace papers feed

---
