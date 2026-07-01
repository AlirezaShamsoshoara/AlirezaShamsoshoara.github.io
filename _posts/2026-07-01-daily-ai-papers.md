---
title: "Daily AI Papers — July 01, 2026"
date: 2026-07-01
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-01/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - world-models
  - agentic-ai
  - inference-acceleration
---

## 1. Orca: The World is in Your Mind

**Authors:** Yihao Wang, Yuheng Ji, Mingyu Cao, Yanqing Shen, Runze Xiao, Huaihai Lyu, Senwei Xie, Euan Liu, Klara Tian, Tianfeng Long, Yichi Zhang, Zhengliang Cai, Ruike Chen, Jifan Zhao, Ruochuan Shi, Zihan Tang, Jing Lyu, Wenxing Tan, Ningbo Zhang, Yangtao Hu, et al.

**Summary:** Orca is a general world foundation model that learns a unified world latent space from multimodal signals via two complementary paradigms: unconscious learning (dense natural state transitions from 125K hours of video) and conscious learning (sparse meaningful transitions via language-described events and VQA). Rather than optimizing isolated next-token or next-frame prediction, it proposes Next-State-Prediction modeling and demonstrates that stronger world latent enables stronger downstream readouts including text generation, image prediction, and embodied action generation.

**arXiv:** [arxiv.org/abs/2606.30534](https://arxiv.org/abs/2606.30534)
**Sources:** HuggingFace Daily Papers (#1, 174 upvotes), arXiv cs.AI
**Why trending:** Top paper of the day by a wide margin — ambitious world model unifying video, language, and embodied AI in a single latent space.

---

## 2. Dockerless: Environment-Free Program Verifier for Coding Agents

**Authors:** Wenhao Zeng, Yuling Shi, Xiaodong Gu, Chao Hu, Chaofan Wang, Yuhao Cui, Hongting Zhou, Mengnan Qi, Jianqiao Wangni, Zhaojian Yu, Shuzheng Gao, Kai Cai, Shilin He

**Summary:** Dockerless is an environment-free agentic patch verifier that evaluates code patches without executing them, using agentic repository exploration to gather correctness evidence rather than running unit tests in Docker containers. The resulting fully environment-free post-training pipeline achieves 62.0% on SWE-bench Verified, surpassing the Qwen3.5-9B baseline by 2.4 points while matching environment-based training.

**arXiv:** [arxiv.org/abs/2606.28436](https://arxiv.org/abs/2606.28436)
**Sources:** HuggingFace Daily Papers (#2, 81 upvotes), arXiv cs.SE
**Why trending:** Practical breakthrough for coding agent training — eliminating expensive Docker environment setup from the RL/SFT pipeline.

---

## 3. DOPD: Dual On-policy Distillation

**Authors:** Xinlei Yu, Gen Li, Qingyi Si, Guibin Zhang, Yuqi Xu, Congcong Wang, Shuai Dong, Kaiwen Tuo, Xiangyu Zeng, Kaituo Feng, Qunzhong Wang, Yang Shi, Xiaobin Hu, Xiangyu Yue, Jiaqi Wang, Shuicheng Yan

**Summary:** DOPD introduces an advantage-aware dual distillation paradigm that addresses "privilege illusion" — the conflation of transferable capability gaps and information asymmetry gaps in on-policy distillation with privileged information. It dynamically routes token-level supervision between privileged teacher and student policies based on their advantage gap, with each token receiving supervision of different strength, objective, and strategy.

**arXiv:** [arxiv.org/abs/2606.30626](https://arxiv.org/abs/2606.30626)
**Sources:** HuggingFace Daily Papers (#3, 73 upvotes), arXiv cs.LG
**Why trending:** Strong results on LLM and VLM distillation, with validation on stability, robustness, continual learning, and OOD tasks.

---

## 4. BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding

**Authors:** Hao Zhang, Yiming Hu, Yong Wang, Mingqiao Mo, Xin Xiao, Xiangxiang Chu

**Summary:** BlockPilot identifies that fixed block sizes in diffusion-based speculative decoding are suboptimal, as the optimal block size varies per sample — and proposes a lightweight policy to predict the optimal block size from the prefilling representation. It achieves an acceptance length of 5.92 and 4.20× speedup on Qwen3-4B at temperature T=1, integrated seamlessly with a single prefilling-stage prediction.

**arXiv:** [arxiv.org/abs/2606.31315](https://arxiv.org/abs/2606.31315)
**Sources:** HuggingFace Daily Papers (#4, 67 upvotes), arXiv cs.LG
**Why trending:** State-of-the-art inference speedup with a plug-and-play approach; directly relevant to production LLM deployment.

---

## 5. Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from Unposed Views

**Authors:** Mijin Yoo, In Cho, Subin Jeon, Jiwoo Lee, Eunbyung Park, Seon Joo Kim

**Summary:** This paper proposes a feed-forward framework that directly outputs instance-structured 3D token groups from unposed multi-view images, decomposing scenes into compact object-centric units rather than dense unstructured Gaussians or point clouds. Reconstruction, segmentation, and manipulation all follow from these object-centric representations without post-hoc processing.

**arXiv:** [arxiv.org/abs/2606.29513](https://arxiv.org/abs/2606.29513)
**Sources:** HuggingFace Daily Papers (#5, 31 upvotes), arXiv cs.CV
**Why trending:** Fundamental rethink of 3D scene representation — object-centric from the start rather than primitive-centric.

---

## 6. GEAR: Guided End-to-End AutoRegression for Image Synthesis

**Authors:** Bin Lin, Zheyuan Liu, Chenguo Lin, Sixiang Chen, Yunyang Ge, Yunlong Lin, Jianwei Zhang, Miles Yang, Zhao Zhong, Liefeng Bo, Li Yuan

**Summary:** GEAR jointly trains a VQ tokenizer and autoregressive generator end-to-end, guided by representation alignment, breaking the conventional two-stage pipeline where the tokenizer is frozen and unaware of what the generator needs. This co-training improves both reconstruction quality and generation coherence for image synthesis.

**arXiv:** [arxiv.org/abs/2606.32039](https://arxiv.org/abs/2606.32039)
**Sources:** HuggingFace Daily Papers (#6, 27 upvotes), arXiv cs.CV
**Why trending:** Challenges the dominant paradigm of decoupled tokenizer-generator training; strong image synthesis results.

---

## 7. Multi-Block Diffusion Language Models

**Authors:** Yijie Jin, Jiajun Xu, Yuxuan Liu, Chenkai Xu, Yi Tu, Jiajun Li, Dandan Tu, Xiaohui Yan, Kai Yu, Pengfei Liu, Zhijie Deng

**Summary:** Multi-Block Diffusion (MultiBD) extends single-block diffusion language models to decode consecutive blocks concurrently for inter-block parallelism, addressing the training-inference gap that arises when models trained under teacher forcing encounter multi-block generation. The work provides training recipes to bridge this gap and enable scalable diffusion-based text generation.

**arXiv:** [arxiv.org/abs/2606.29215](https://arxiv.org/abs/2606.29215)
**Sources:** HuggingFace Daily Papers (#7, 21 upvotes), arXiv cs.CL
**Why trending:** Advances diffusion-based language modeling toward practical parallel inference, a key challenge for competitive deployment.

---

## 8. SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History

**Authors:** Zhiwei Li, Yong Hu

**Summary:** SkillHone is a harness for continual agent skill evolution that maintains persistent decision history — retaining not just final skill artifacts but also the evaluations, rejected alternatives, and revision rationale that subsequent agents need. This enables more principled and interpretable skill improvement over time compared to approaches that discard the decision trail.

**arXiv:** [arxiv.org/abs/2606.08671](https://arxiv.org/abs/2606.08671)
**Sources:** HuggingFace Daily Papers (#8, 21 upvotes), arXiv cs.AI
**Why trending:** Addresses a key gap in agentic systems: skills that evolve continuously in changing environments need historical context to improve reliably.

---

## 9. Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks

**Authors:** Young-Jun Lee, Seungone Kim, Minki Kang, Alistair Cheong Liang Chuen, Zerui Chen, Seungho Han, Taehee Jung, Dongyeop Kang

**Summary:** Evolution Fine-Tuning trains LLMs within evolutionary search scaffolds across 371 diverse optimization tasks — spanning GPU kernel design, mathematical conjectures, scientific law discovery, and combinatorial puzzles — enabling cross-domain discovery transfer. Unlike prior work that targets one task at a time, this approach builds general evolutionary reasoning ability that generalizes to new problems without task-specific scaffolding.

**arXiv:** [arxiv.org/abs/2606.29082](https://arxiv.org/abs/2606.29082)
**Sources:** HuggingFace Daily Papers (#9, 21 upvotes), arXiv cs.LG
**Why trending:** Bridges LLM post-training and automated scientific discovery at scale, with impressive breadth across 371 tasks.

---

## 10. MemLearner: Learning to Query Context Memory for Video World Models

**Authors:** Jiwen Yu, Jianxiong Gao, Jianhong Bai, Yiran Qin, Kaiyi Huang, Quande Liu, Xintao Wang, Pengfei Wan, Kun Gai, Xihui Liu

**Summary:** MemLearner introduces a learning-based adaptive context query method for video world models that overcomes the inconsistency problem in extended video generation caused by lack of memory. Unlike rule-based context frame retrieval, it generalizes to scenes with occlusions and dynamic objects by learning which context frames to retrieve conditioned on user actions and current state.

**arXiv:** [arxiv.org/abs/2606.31734](https://arxiv.org/abs/2606.31734)
**Sources:** HuggingFace Daily Papers (#10, 18 upvotes), arXiv cs.CV
**Why trending:** Solves a fundamental limitation in long-duration video world models; relevant for autonomous agents and game simulation.

---

## 11. Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation

**Authors:** Julia Belikova, Rauf Parchiev, Evgeny Egorov, Grigorii Davydenko, Gleb Gusev, Andrey Savchenko, Maksim Makarenko

**Summary:** Introduces AFTER, a benchmark of 382 realistic enterprise tasks spanning six professional roles and 22 procedural skills, designed to evaluate how procedural memory skills transfer across tasks, roles, and model backbones. The benchmark includes controlled settings for local improvement, cross-task transfer, cross-role transfer, and continual adaptation.

**arXiv:** [arxiv.org/abs/2606.23127](https://arxiv.org/abs/2606.23127)
**Sources:** HuggingFace Daily Papers (#11, 17 upvotes), arXiv cs.CL
**Why trending:** Rigorous evaluation of procedural memory for enterprise AI agents — fills an important gap in agent benchmarking.

---

## 12. DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation

**Authors:** Siyu Yan, Yizhen Gao, Yilin Wang, Dongxing Mao, Alex Jinpeng Wang

**Summary:** DataEvolver breaks the static crawl-filter-freeze data pipeline by introducing self-evolving multi-agent construction that learns from rejected samples rather than discarding them. Multiple specialized agents collaboratively construct, evaluate, and iteratively refine training data for text-rich image generation, continuously improving data quality.

**arXiv:** [arxiv.org/abs/2606.31537](https://arxiv.org/abs/2606.31537)
**Sources:** HuggingFace Daily Papers (#12, 16 upvotes), arXiv cs.CV
**Why trending:** Novel approach to data-centric AI for a notoriously hard problem (text rendering in images); self-evolving data pipelines are gaining traction.

---

## 13. Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs

**Authors:** Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona, Idan Szpektor, Arman Cohan

**Summary:** This work uses reinforcement learning with metacognitive feedback to train LLMs to monitor and regulate their own uncertainty, directly addressing the systemic deficiencies where models hallucinate with high confidence and fail to recognize knowledge boundaries. RL-based metacognitive training elicits faithful uncertainty expression that improves trustworthiness and reliability.

**arXiv:** [arxiv.org/abs/2606.32032](https://arxiv.org/abs/2606.32032)
**Sources:** HuggingFace Daily Papers (#13, 14 upvotes), arXiv cs.CL
**Why trending:** Hallucination and calibration are critical safety issues; RL-based metacognitive training is a fresh angle with strong results.

---

## 14. RedVox: Safety and Fairness Gaps in Speech Models Across Languages

**Authors:** Beatrice Savoldi, Sara Papi, Wafa Aissa, Matteo Negri, Luisa Bentivogli

**Summary:** RedVox is a multilingual safety and fairness benchmark for speech and audio models built on real voices, covering unsafe and biased content across diverse languages. A survey of state-of-the-art speech model releases finds that only 8% document any multilingual safety analysis, exposing a critical gap in responsible AI deployment.

**arXiv:** [arxiv.org/abs/2606.26968](https://arxiv.org/abs/2606.26968)
**Sources:** HuggingFace Daily Papers (#14, 12 upvotes), arXiv cs.CL
**Why trending:** Safety red-teaming for speech models is underexplored; the finding that 92% of releases skip multilingual safety analysis is alarming.

---

## 15. Little Brains, Big Feats: Exploring Compact Language Models

**Authors:** Dari Baturova, Elena Bruches, Ivan Chernov, Roman Derunets, Arsenii Fomin, Andrey Kostin

**Summary:** This study investigates how smaller language models perform as generators in Retrieval-Augmented Generation (RAG) systems, benchmarking across open-source and proprietary datasets covering diverse subject areas and question types. The findings challenge the assumption that scale always wins, showing compact models can be competitive in specific RAG configurations.

**arXiv:** [arxiv.org/abs/2606.30062](https://arxiv.org/abs/2606.30062)
**Sources:** HuggingFace Daily Papers (#15, 10 upvotes), arXiv cs.CL
**Why trending:** Practical relevance for cost-efficient RAG deployments; compact models are increasingly competitive with frontier models.

---

## 16. Are We Measuring Strategy or Phrasing? The Gap Between Surface- and Approach-Level Diversity in LLM Math Reasoning

**Authors:** Sangmook Lee, Minbeom Kim, Jeonghye Kim, Dohyung Kim, Sojeong Rhee, Kyomin Jung

**Summary:** This paper introduces approach-level diversity — variation in strategies across correct solutions to the same problem — and demonstrates that common diversity metrics mostly capture surface-level phrasing differences rather than genuine problem-solving strategy differences. A human-calibrated LLM judge framework reveals that prior measures are unreliable proxies, with implications for math reasoning benchmarking and training.

**arXiv:** [arxiv.org/abs/2606.29985](https://arxiv.org/abs/2606.29985)
**Sources:** HuggingFace Daily Papers (#16, 9 upvotes), arXiv cs.CL
**Why trending:** Fundamental critique of how diversity is measured in LLM reasoning research; affects evaluation methodology broadly.

---

## 17. QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents

**Authors:** Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina, Joschka Strüber, Ameya Prabhu, Matthias Bethge

**Summary:** QVal provides a cost-efficient framework for evaluating dense intermediate supervision signals in long-horizon LLM agent trajectories, addressing the challenge that outcome-only rewards are too sparse when trajectories span hundreds of actions. It enables evaluation of intermediate step quality without expensive downstream training runs.

**arXiv:** [arxiv.org/abs/2606.32034](https://arxiv.org/abs/2606.32034)
**Sources:** HuggingFace Daily Papers (#17, 8 upvotes), arXiv cs.AI
**Why trending:** Dense reward signal evaluation is critical for RL-trained agents; cheap evaluation is a practical enabler for scaling.

---

## 18. PolyFlow: Continuous Topology Embedding Flow Matching for Artist-style Mesh Generation

**Authors:** Chunshi Wang, Haohan Weng, Junliang Ye, Biwen Lei, Yang Li, Zibo Zhao, Zeqiang Lai, Kaiyi Zhang, Yunhan Yang, Zhuo Chen, Chunchao Guo, Yawei Luo

**Summary:** PolyFlow introduces continuous topology embedding flow matching for generating high-quality 3D meshes in diverse artistic styles, bridging the gap between neural generation and artist-quality mesh production. The continuous topology embedding enables smooth interpolation across mesh topologies while preserving artistic style characteristics.

**arXiv:** [arxiv.org/abs/2606.30673](https://arxiv.org/abs/2606.30673)
**Sources:** HuggingFace Daily Papers (#18, 8 upvotes), arXiv cs.CV
**Why trending:** 3D content creation for games and animation is a hot area; artist-style mesh generation has direct commercial applications.

---

## 19. Xiaomi-GUI-0 Technical Report

**Authors:** Wanxia Cao, Chengzhen Duan, Pei Fu, Pengzhi Gao, Niu Lian, Fazhan Liu, Hui Liu, Heng Qu, Qinzhuo Wu, Zhehao Yu, et al.

**Summary:** Xiaomi-GUI-0 is a GUI agent built on vision-language models for end-to-end task completion in real mobile applications through tapping, swiping, text entry, and navigation actions. It specifically addresses the substantial gap between offline benchmark training and real-world deployment where interface layout, interaction logic, and abnormal-state distributions differ significantly.

**arXiv:** [arxiv.org/abs/2606.31410](https://arxiv.org/abs/2606.31410)
**Sources:** HuggingFace Daily Papers (#19, 7 upvotes), arXiv cs.AI
**Why trending:** Major hardware OEM releasing a GUI agent model signals industry-wide adoption of agentic phone control; mobile GUI agents are a competitive space.

---

## 20. Unlocking the Visual Record of Materials Science: A Large-Scale Multimodal Dataset from Scientific Literature

**Authors:** Subham Ghosh, Shubham Tiwari, Mohammad Ibrahim, Abhishek Tewari

**Summary:** MatMMExtract is an end-to-end open-source pipeline that unlocks the visual knowledge encoded in materials science literature by decomposing compound figures into individual sub-panels with accurate captions. This solves the core difficulty of compound figures where a single caption describes multiple sub-panels, enabling large-scale multimodal AI for materials discovery.

**arXiv:** [arxiv.org/abs/2606.29667](https://arxiv.org/abs/2606.29667)
**Sources:** HuggingFace Daily Papers (#20, 7 upvotes), arXiv cs.CV, cs.IR
**Why trending:** AI for science is a major growth area; unlocking decades of visual experimental data from PDFs is a high-value enabling dataset.

---

*Generated: 2026-07-01 | Data from HuggingFace Daily Papers API, arXiv*
