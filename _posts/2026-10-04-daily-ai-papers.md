---
title: "Daily AI Papers — October 04, 2026"
date: 2026-10-04
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-04/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - world-models
  - ai-agents
  - video-generation
---

### 1. OpenTumorBoard: A Real-World Benchmark of Multidisciplinary Tumor Board Discussion Trajectories
**Authors:** Anqi Li, Zhixuan Ge, Yixuan Duan, Jiarong Qian, Chi-Yu Chen, MingYu Lu, Huan-Yu Hsu, Yu Gu, Yue Guo, Sheng Wang, Wei Qiu, Hanwen Xu
**arXiv:** [arxiv.org/abs/2609.32810](https://arxiv.org/abs/2609.32810)
**Summary:** OpenTumorBoard contains 611 cancer cases and 19,157 discussion turns across ten specialist roles, extracted from more than 12,500 minutes of public multidisciplinary tumor board recordings. Fourteen frontier and medical LLMs fall well short of specialist answers and recorded board conclusions, while supervised fine-tuning and reinforcement learning improve held-out performance.

---

### 2. DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration
**Authors:** Yupeng Xie, Zhenyang Wang, Liangwei Wang, Jiayi Zhu, Zhouan Shen, Yuyu Luo
**arXiv:** [arxiv.org/abs/2609.33403](https://arxiv.org/abs/2609.33403)
**Summary:** DataMagic generates data videos from raw tables using DVSpec, a declarative representation that links charts, narration, animation, provenance, and timing, plus a generate-then-orchestrate multi-agent workflow. On 109 real examples it raises quality to 3.89 out of 5 with execution success above 95%, while a user study finds a 79.7% reduction in authoring time versus a conversational LLM workflow.

---

### 3. Removing the NEEDLE in the Haystack: Backdoor Removal in LLMs via Weight Orthogonalisation
**Authors:** Minoo Kim, Vasileios Lampos, George Drayson
**arXiv:** [arxiv.org/abs/2610.00348](https://arxiv.org/abs/2610.00348)
**Summary:** NEEDLE is a training-free defense that estimates a backdoor direction and refusal subspace from activations, then applies sequential weight orthogonalization to suppress the trigger without broadly changing benign behavior. Across model families and attack types it achieves the lowest mean attack success rate among tested defenses, including 0% on code-injection attacks, with minimal capability and safety changes.

---

### 4. RLE-Bench: A Qualifying Exam for Coding Agents as Robot Learning Engineers
**Authors:** Haitong Ma, Chenxiao Gao, Rushi Qiang, Bo Dai, Na Li
**arXiv:** [arxiv.org/abs/2609.34210](https://arxiv.org/abs/2609.34210)
**Summary:** RLE-Bench evaluates coding agents on four end-to-end robotics workflows: interactive control, policy learning, perception and estimation, and mechanical design. Its task-specific metrics and aggregate RLE Index expose how well agents build, integrate, diagnose, and improve heterogeneous physical-world artifacts under resource constraints.

---

### 5. LOCI: Spatial Linear Memory for Streaming World Models
**Authors:** Ji Xia, Tingting Liao, Xuezhi Liang, Hao Li, Guangyi Liu
**arXiv:** [arxiv.org/abs/2609.40222](https://arxiv.org/abs/2609.40222)
**Summary:** LOCI combines detailed key-value caches with recurrent linear-attention memory whose reads and writes are conditioned on projective camera geometry, enabling viewpoint-aware retrieval of earlier scenes. It improves revisit fidelity on public and recorded trajectories, cuts peak memory by about 30% versus full softmax at equal length, and can stream indefinitely with a bounded observation bank.

---

### 6. Memorizon: Training World Models Beyond Their Context Window
**Authors:** Tingting Liao, Xuezhi Liang, Hao Li, Guangyi Liu
**arXiv:** [arxiv.org/abs/2610.00544](https://arxiv.org/abs/2610.00544)
**Summary:** Memorizon trains world models on arbitrarily long temporal spans while scoring only the final chunks and retrieving a bounded bank of camera-co-visible latents instead of attending to every intervening frame. Extending training spans from 100 to 400 seconds adds only 12% step time, while retrieval and access to the first visit improve revisit consistency substantially over sliding-window training.

---

### 7. SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation
**Authors:** Mikhail Dereviannykh, Vikram Voleti, Simon Donne, Mallikarjun Byrasandra Ramalinga Reddy, Shimon Vainer, Mark Boss
**arXiv:** [arxiv.org/abs/2610.00686](https://arxiv.org/abs/2610.00686)
**Summary:** SemanTok trains a flexible video tokenizer to reconstruct frozen DINO features from every retained token prefix, making early tokens carry predictable global semantics while later tokens refine visual detail. A 201M-parameter SemanTok autoregressive model matches or beats a VideoFlexTok model 3.4 times its size and preserves semantic alignment on out-of-distribution classes.

---

### 8. VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in Video Generation
**Authors:** Yu Huang, Jungang Li, Zhiyuan Wang, Yonghua Hei, Song Dai, Jiayu Yang, Deyuan Liu, Xiang Zheng, Xiaoshuang Shi, Hao Cheng, Kaidi Xu
**arXiv:** [arxiv.org/abs/2610.01499](https://arxiv.org/abs/2610.01499)
**Summary:** VTR-Bench evaluates visual text rendering in generated video with 300 prompts across five application scenarios and an automated, human-aligned pipeline that separately scores transcription, scene, and motion requirements. Eleven leading models show widespread failures, with the best reaching a 0.250 word error rate, while a keyframe-guided agentic framework offers an iterative path to improvement.

---

### 9. Generalization Is Stability, Not Accuracy: Multi-Axis Evaluation of LLMs
**Authors:** Nagham Omar, Mahmoud Jabarin, Maya Rozenshtein, Rom Himelstein, Avi Mendelson, Amit LeVi
**arXiv:** [arxiv.org/abs/2610.01428](https://arxiv.org/abs/2610.01428)
**Summary:** The Stability-Aware Generalization Objective evaluates whether an LLM behaves consistently for semantically equivalent input variations across generation, internal activations, confidence, and response mirroring. Experiments show that no tested model generalizes uniformly, different axes reveal independent failures, and cross-dataset variation can reverse model rankings.

---

### 10. ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research
**Authors:** Sohyeon Kim, Yoonho Lee, Bo Liu, Dayoon Ko, Rulin Shao, Seungone Kim, Graham Neubig, Pang Wei Koh, Aakanksha Chowdhery, Akari Asai, Omar Khattab, Yejin Choi, Gunhee Kim, Chelsea Finn
**arXiv:** [arxiv.org/abs/2610.02202](https://arxiv.org/abs/2610.02202)
**Summary:** ScholarCatalyst uses detailed judgments from 184 lead authors of 207 recent computer science papers to test whether systems can retrieve earlier work that would have advanced a project from its initial research question. Agentic search reaches only 0.42 Recall@20 versus 0.48 for embedding retrieval, and even a strong agent reaches just 0.51, highlighting the gap in expert scientific search intuition.

---

### 11. Devils in Question Relay: Source-Conditioned Relay Steering to Mitigate Hallucinations in Audio-visual Large Language Models
**Authors:** Yu Zhang, Pingrui Zhang, Xuefeng Bai, Pengfei Zhang, Yang Xiang, Kehai Chen
**arXiv:** [arxiv.org/abs/2609.37568](https://arxiv.org/abs/2609.37568)
**Summary:** The authors identify a question-relay mechanism in audio-visual LLMs where question states carry interference from an irrelevant modality alongside evidence from the required source. Their training-free SECRET steering method redirects those states toward the requested modality and improves source-grounded accuracy by up to 18.0 and 7.1 percentage points on two benchmarks.

---

### 12. KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards
**Authors:** Pengfei Li, Naufal Suryanto, Sicheng Zhang, Muzammal Naseer
**arXiv:** [arxiv.org/abs/2610.02206](https://arxiv.org/abs/2610.02206)
**Summary:** KaliBench contains 8,504 natural-language-to-command pairs covering 1,642 Kali Linux tools, 23 capability dimensions, and five security phases, with canonicalization and execution-based verification. No open-weight model exceeds 42% exact-command accuracy without tool hints, while supervised and verifiable-reward training lets an 8B model approach a 685B mixture-of-experts model.

---

### 13. Does Native 3D Texture Generation Necessarily Require 3D Assets for Training?
**Authors:** Jiangshan Wang, Zeqiang Lai, Jiayi Guo, Xin Yang, Xin Huang, Jiarui Chen, Ziheng Ouyang, Chunchao Guo, Xiangyu Yue
**arXiv:** [arxiv.org/abs/2609.34621](https://arxiv.org/abs/2609.34621)
**Summary:** Tex-Zero trains a native 3D texture VAE and diffusion transformer without real 3D assets by turning high-quality 2D images into planar patches with randomized rotations and aggregated geometry. The resulting system reconstructs and generates detailed textures on real 3D assets despite never seeing such assets during training, suggesting a more scalable data strategy for 3D generation.

---

### 14. Explore Broadly, Reason Sharply: Push Small Models toward the Frontier via Sampling
**Authors:** Panagiotis Theodoropoulos, Nan Jiang, Xintong Duan, Ali Hasan, Yuriy Nevmyvaka, Evangelos A. Theodorou, Wei Deng
**arXiv:** [arxiv.org/abs/2609.38104](https://arxiv.org/abs/2609.38104)
**Summary:** Parallel Power Tempering runs interacting inference replicas at different sharpening levels so some chains explore diverse reasoning paths while others exploit high-likelihood answers. The method improves over single-chain power-sharpened sampling and tested reinforcement-learning post-trained models, producing stronger reasoning traces without parameter updates or external rewards.

---

### 15. Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs
**Authors:** Vincent-Daniel Yun, Woosang Lim, Haneul Yoo, Sungjoo Yoo, Murali Annavaram, Sai Praneeth Karimireddy
**arXiv:** [arxiv.org/abs/2609.32259](https://arxiv.org/abs/2609.32259)
**Summary:** HeteroFold maps a sender model's key-value cache into a frozen receiver from another model family by aligning structure and calibrating the transferred cache to preserve receiver behavior. It leads across six transfer directions and four long-context benchmarks, and at 32K context makes one Llama-to-Ministral transfer 10.7 times faster than native prefill.

---

### 16. OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport
**Authors:** Guillaume Besset, Erwann Carn, Timothée Carecchio, Valentin Tordjman-Levavasseur, Fabian Schramm, Yann de Mont-Marin, Justin Carpentier, Ajay Suresha Sathya
**arXiv:** [arxiv.org/abs/2609.36602](https://arxiv.org/abs/2609.36602)
**Summary:** OTRetarget jointly adapts humanoid and object trajectories from human demonstrations by transferring surface-interaction geometry through entropic optimal transport and optimizing constrained inverse kinematics. On OMOMO it reaches an 87% robot-object interaction Jaccard score and 8.7 mm depth error, and the retargeted references transfer to a physical G1 humanoid through reinforcement-learned whole-body policies.

---

### 17. JevSpawn: Adaptive Agentic Inference through Compositional Action Spaces
**Authors:** Haoyang Su, Weiran Huang
**arXiv:** [arxiv.org/abs/2610.00437](https://arxiv.org/abs/2610.00437)
**Summary:** JevSpawn converts natural-language tasks into finite probabilistic action spaces, then uses parallel spawning, feedback-driven branch selection, representation revision, and retained alternatives for recovery. Across eight tasks and seven agent baselines, it improves task performance and navigation speed without additional training by sharing action structure and model prefixes.

---

### 18. MemFold: Learning Compact Soft Memory for Long-Context Personalization via On-Policy Optimization
**Authors:** Jingxuan Wu, Yuzhe Yang, Yiqiao Huang, Chengzhi Liu, Qingni Wang, Chengxuan Qian, Shutong Wu, Jiawei Zhang, Xin Eric Wang
**arXiv:** [arxiv.org/abs/2609.36435](https://arxiv.org/abs/2609.36435)
**Summary:** MemFold compresses query-conditioned user history into a fixed number of continuous memory vectors and trains the reader on its own rollouts using task rewards plus confidence-gated on-policy distillation. Across three Qwen backbones it achieves the best reported PersonaMem-32K and PersonaMem-128K accuracy in the study and transfers to PrefEval and LongMemEval without target-domain training.

---

### 19. When Does Correction Become Repair? Mechanistic Auditing of Internal Interventions in Tool-Using LLMs
**Authors:** Jiayi Li, Ruizhe Li
**arXiv:** [arxiv.org/abs/2609.36138](https://arxiv.org/abs/2609.36138)
**Summary:** SAKIKO audits activation steering for tool-use decisions through directional error discovery, router-conditioned interventions, destination-resolved verification, and frozen statistical criteria. Although calibrated interventions produce direction-specific gains in five of seven models, destination analysis shows that apparently positive steering can corrupt more than half of the baseline-correct decisions it touches.

---

### 20. Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models
**Authors:** Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis
**arXiv:** [arxiv.org/abs/2610.01942](https://arxiv.org/abs/2610.01942)
**Summary:** Latent-Foresight jointly trains a latent tokenizer and flow-based generative dynamics model so compressed vision-foundation features are explicitly organized for temporal prediction rather than learned in a separate frozen stage. It produces more temporally coherent representations and consistently beats two-stage baselines across future-scene tasks and horizons, including high-resolution adaptation.
