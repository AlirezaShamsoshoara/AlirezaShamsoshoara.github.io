---
title: "Daily AI Papers — October 11, 2026"
date: 2026-10-11
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-11/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - 3d-generation
  - multimodal-models
  - ai-agents
---

### 1. Structured 3D Latents for Scalable and Versatile 3D Generation
**Authors:** Jianfeng Xiang, Zelong Lv, Sicheng Xu, Yu Deng, Ruicheng Wang, Bowen Zhang, Dong Chen, Xin Tong, Jiaolong Yang
**arXiv:** [arxiv.org/abs/2412.01506](https://arxiv.org/abs/2412.01506)
**Summary:** The method introduces Structured LATents, combining a sparse 3D grid with dense multiview foundation-model features so one representation can decode into radiance fields, 3D Gaussians, or meshes. Rectified-flow transformers trained at up to two billion parameters on 500,000 objects improve text- and image-conditioned generation while enabling flexible output formats and local editing.

---

### 2. SpatialLM: Training Large Language Models for Structured Indoor Modeling
**Authors:** Yongsen Mao, Junhao Zhong, Chuan Fang, Jia Zheng, Rui Tang, Hao Zhu, Ping Tan, Zihan Zhou
**arXiv:** [arxiv.org/abs/2506.07491](https://arxiv.org/abs/2506.07491)
**Summary:** SpatialLM adapts a standard multimodal language-model architecture to turn 3D point clouds into structured descriptions of walls, doors, windows, and semantically labeled object boxes. Training on 12,328 synthetic indoor scenes yields state-of-the-art layout estimation and competitive 3D detection, pointing toward stronger spatial reasoning for robotics and augmented reality.

---

### 3. Context Language Models
**Authors:** Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin, Yuetai Li, Minheng Wang, Hamish Ivison, Radha Poovendran, Nathan Lambert, Teng Xiao, Mike Lewis, Wen-tau Yih, Luke Zettlemoyer, Pang Wei Koh
**arXiv:** [arxiv.org/abs/2609.37725](https://arxiv.org/abs/2609.37725)
**Summary:** Context Language Models treat context as a file that the model can update directly, letting it learn what to preserve and naturally extending the mechanism to multiple agents with separate context files. Zero-shot, skill-optimized, and reinforcement-learned variants improve long-horizon task accuracy while using less compute, with suffix-cache reuse reducing serving cost further.

---

### 4. Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training
**Authors:** Shuyuan Tu, Qi Tian, Yinming Huang, Yue Wu, Xintong Han, Kaihang Pan, Weijie Kong, Jiangfeng Xiong, Jian-Wei Zhang, Zuxuan Wu, Yu-Gang Jiang
**arXiv:** [arxiv.org/abs/2610.05416](https://arxiv.org/abs/2610.05416)
**Summary:** Prism partitions joint video-audio tokens into adaptive spatiotemporal macro-zones whose sparse attention shapes respond to local visual variation and audio-visual coupling. Native 2K training runs 2.5 times faster than full attention while improving generation quality, showing that structured sparsity can preserve informative cross-modal interactions.

---

### 5. Bitnet.cpp: Efficient Edge Inference for Ternary LLMs
**Authors:** Jinheng Wang, Hansong Zhou, Ting Song, Shijie Cao, Yan Xia, Ting Cao, Jianyu Wei, Shuming Ma, Hongyu Wang, Furu Wei
**arXiv:** [arxiv.org/abs/2502.11880](https://arxiv.org/abs/2502.11880)
**Summary:** Bitnet.cpp provides an inference system and mixed-precision matrix-multiplication library for lossless, sub-two-bit deployment of BitNet b1.58 and other ternary language models. Its lookup-table and scaled-int2 kernels reach up to 6.25 times the speed of full-precision baselines and 2.32 times that of low-bit baselines on edge hardware.

---

### 6. Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning
**Authors:** Hanqiu Li Cai, Chema Garabito
**arXiv:** [arxiv.org/abs/2610.09450](https://arxiv.org/abs/2610.09450)
**Summary:** Iris-3B tests whether pixel-space diffusion provides better fine-grained priors than latent diffusion by pretraining a three-billion-parameter model and converting a latent FLUX model for matched downstream comparisons. Pixel-space models do not improve depth estimation or image restoration, but Iris-3B shows that pixel-space pretraining can scale to competitive 1024-pixel text-to-image quality.

---

### 7. MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent
**Authors:** Zekai Liu, Zhilin Wang, Xuzheng He, Yu Cheng, Yang Yang
**arXiv:** [arxiv.org/abs/2610.10355](https://arxiv.org/abs/2610.10355)
**Summary:** MIRA turns explicit and implied musical intent into independently verifiable rubric items, then searches over prompt revisions for a black-box text-to-music generator under a bounded budget. On MuRA-Bench, its iterative generation and verification loop improves intent alignment enough for an open-source generator to approach representative commercial systems.

---

### 8. Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable Agent-System Interaction
**Authors:** Yipeng Li, Ashutosh Hathidara, Jane Lo, Harshavardhan Abichandani, Gunraj Singh, Atin Ghosh
**arXiv:** [arxiv.org/abs/2610.10549](https://arxiv.org/abs/2610.10549)
**Summary:** Synthesis Through Simulation generates enterprise data by having an LLM agent operate policy-enforcing APIs inside simulated environments, guaranteeing structural validity without exposing database schemas. Its domain-agnostic Generalist Populator attains 0.88 average marginal fidelity and 100% constraint satisfaction across ten environments while remaining applicable where seed-data methods cannot run.

---

### 9. BrickBench: Evaluating Agentic Brick Design
**Authors:** Peter Kulits, Yiqing Xu, R. Kenny Jones, Cordelia Schmid, Jiajun Wu
**arXiv:** [arxiv.org/abs/2610.12452](https://arxiv.org/abs/2610.12452)
**Summary:** BrickBench asks coding agents to design text-conditioned LEGO assemblies that satisfy semantic goals, design quality, part availability, and physical buildability. Its BrickAgent environment reveals that leading agents handle many verifiable constraints but still fall short of human designs on the combined creative and structural task.

---

### 10. Native and Compact Structured Latents for 3D Generation
**Authors:** Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
**arXiv:** [arxiv.org/abs/2512.14692](https://arxiv.org/abs/2512.14692)
**Summary:** The paper introduces O-Voxel, a sparse native-3D representation that captures arbitrary topology together with texture and physically based rendering attributes. A compression VAE and four-billion-parameter flow-matching models produce efficient, high-quality geometry and materials from diverse public 3D asset data.

---

### 11. On-Policy Distillation Teaches New Skills but Not New Knowledge
**Authors:** Yixuan Tang, Yi Yang
**arXiv:** [arxiv.org/abs/2610.09639](https://arxiv.org/abs/2610.09639)
**Summary:** Controlled experiments separate factual acquisition from compositional reasoning and show that reverse-KL on-policy distillation transfers new reasoning skills but very little new factual knowledge. Forward KL restores factual transfer, while student-generated rollouts specifically improve multi-step execution, clarifying which ingredients produce each capability.

---

### 12. CARE: Certifying Acceleration for Vision-Language-Action Inference
**Authors:** Rui Liu, Tong Zheng, Jindong Gu, Zhipeng Wang
**arXiv:** [arxiv.org/abs/2610.08917](https://arxiv.org/abs/2610.08917)
**Summary:** CARE uses paired rollouts from identical initial conditions to certify that an accelerated vision-language-action policy stays within a user-specified risk of failing tasks solved by the reference policy. Across robot benchmarks it certifies 9.0-to-10.8-times speedups while preserving at least 85.8% of reference-solved episodes at 95% confidence.

---

### 13. Incidental information contaminates patient notes and disrupts clinical reasoning in large language models
**Authors:** Krithik Vishwanath, Brandon Ye, Anton Alyakin, John E. Markert, Aaron Hsieh, Michał Mańkowski, Eric K. Oermann
**arXiv:** [arxiv.org/abs/2610.08585](https://arxiv.org/abs/2610.08585)
**Summary:** Experiments with patient-clinician dialogues show that frontier models often insert small talk into clinical notes and sometimes misattribute or use those asides clinically. Background speech from another encounter also leaks into transcripts and downstream notes, motivating safeguards that block incidental contamination without impairing clinical reasoning.

---

### 14. Frozen Models, Evolving Expertise: Model-Agnostic Learning from Deployment Experience for Multimodal Medical AI
**Authors:** Yexiao He, Yucheng Tang, Pengfei Guo, Yufan He, Andriy Myronenko, Can Zhao, Ang Li, Daguang Xu, Dong Yang
**arXiv:** [arxiv.org/abs/2610.09146](https://arxiv.org/abs/2610.09146)
**Summary:** The framework lets frozen language and vision-language models learn from deployment through an external reasoning skill, evidence-backed knowledge memory, and a multimodal case base. Validation on new and earlier cases prevents regressions, producing gains of up to 34.2% on medical tasks and transferring experience across models without weight updates.

---

### 15. You Changed Your Mind, The Model Didn't: Demystifying Intent in Multi-Turn Dialogue
**Authors:** Junle Chen, Wei Chen, Zhengjun Huang, Zhoujin Tian, Yuxuan Liu, Kai Wang, Rui Chen, Xiaofang Zhou
**arXiv:** [arxiv.org/abs/2610.06496](https://arxiv.org/abs/2610.06496)
**Summary:** Intent-Eval shows that language models often treat rejected proposals and superseded requirements as still active across tool use, coding, database, and mathematics tasks. Intent-OPSD trains on full dialogues with supervision tied to the user's final decision, helping models distinguish content merely mentioned from requirements that remain in force.

---

### 16. EDiS: Edge Disjoint Subgraph Sparsification Framework for Graph Neural Networks
**Authors:** Sai Karthik Navuluru, Siddhartha Shankar Das, Franck Dernoncourt, S M Ferdous, Ryan A. Rossi, Nesreen K. Ahmed, Baris Coskunuzer, Alex Pothen, Lakshman Tamil, Mahantesh M Halappanavar
**arXiv:** [arxiv.org/abs/2610.09059](https://arxiv.org/abs/2610.09059)
**Summary:** EDiS performs one structural decomposition into cacheable edge-disjoint subgraphs, then recombines them across epochs and retention ratios without repeating expensive extraction. Across 19 node-classification benchmarks and 17 baselines, it achieves the best mean score and average rank, especially under tight edge budgets.

---

### 17. Learning to Steer, Steering to See: Unveiling the Geometry of RLVR in Large Language Models via Trainable Vectors
**Authors:** Yuchen Cai, Ding Cao, Qixiang Yin, Xin Xu, Kai Yang, Siye Wu, Pengyuan Wang, Jiaxuan Wang, Weijie Liu, Saiyong Yang, Guangzhong Sun, Guiquan Liu, Junfeng Fang
**arXiv:** [arxiv.org/abs/2609.34344](https://arxiv.org/abs/2609.34344)
**Summary:** Trainable steering vectors reveal that reinforcement learning with verifiable rewards concentrates gains in a small effective activation manifold, largely outside the principal high-variance subspace. The resulting Alpha-Stabler monitors intrusion into that subspace and removes harmful gradient components, stabilizing 2,000-step training and improving gains across models and tasks.

---

### 18. MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination
**Authors:** Joss Armstrong
**arXiv:** [arxiv.org/abs/2605.22949](https://arxiv.org/abs/2605.22949)
**Summary:** MARGIN learns model-specific confidence corrections online from recent outcomes, avoiding retraining and a held-out calibration set when heterogeneous agents report incomparable confidence. It improves post-shift calibration and raises answer-selection accuracy by 4.3 and 14.0 percentage points on two code-generation benchmarks.

---

### 19. SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery
**Authors:** Jiajun Jiang, Chunliang Hua, Zichun Chen, Yanxing Wu, Zeyuan Yang, Jie Song, Xiao Hu
**arXiv:** [arxiv.org/abs/2609.31507](https://arxiv.org/abs/2609.31507)
**Summary:** SatNav uses high-resolution satellite imagery to build 118,000 long-horizon UAV navigation episodes across 59 scenes in 18 cities without expensive reconstructed 3D environments. Its boundary, landmark, and route tasks expose persistent memory and geospatial-reasoning weaknesses, while transfer tests show that satellite-trained policies can operate on real-flight UAV imagery.

---

### 20. TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image Generation via MLLM Workflows
**Authors:** Shuai Fu, Jing Gu, Jian Zhou, Zicheng Duan, Gengze Zhou, Qi Wu
**arXiv:** [arxiv.org/abs/2610.02959](https://arxiv.org/abs/2610.02959)
**Summary:** TerraVis defines 18 object-, interaction-, and scene-level violation types for evaluating whether generated images obey real-world structure, anatomy, physics, and spatial relationships. Its multi-stage multimodal-LLM workflow correlates better with human world-consistency judgments than existing metrics and reveals failures hidden by strong aesthetics or alignment scores.

---
