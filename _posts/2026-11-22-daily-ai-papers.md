---
title: "Daily AI Papers — November 22, 2026"
date: 2026-11-22
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-22/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - streaming-generation
  - embodied-ai
  - model-efficiency
---

### 1. SpecWM: Turning Verification into Refinement for Streaming World Models
**Authors:** Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong, Yue Ma, Zhiyuan Ma
**arXiv:** [arxiv.org/abs/2611.26211](https://arxiv.org/abs/2611.26211)
**Summary:** SpecWM is a training-free streaming world-model framework that verifies draft video chunks using the target model's latent velocity field and reuses the resulting correction for refinement. On WBench Navigation, the authors report improved visual quality at 1.63-times target-model speed and a NavScore increase from the draft's 75.99 to 85.63, with additional long-rollout and cross-backbone evaluations.

---

### 2. AURA: AUdio-dRiven streaming Avatar
**Authors:** Nathaniel Cohen, Nicolas Dufour, Amélie Royer, Alasdair Newson, Patrick Pérez
**arXiv:** [arxiv.org/abs/2611.26540](https://arxiv.org/abs/2611.26540)
**Summary:** AURA generates audio-driven avatar video causally in chunks with a rolling KV cache, using two-stage distillation to reduce denoising steps without requiring multi-second audio look-ahead. The authors report real-time 576p generation at 20.7 frames per second for AURA 1.3B on one GPU and 720p generation at 9.7 frames per second for AURA 5B, releasing both models and synthetic training data.

---

### 3. PAD: Policy-Aware Data Valuation for Autonomous Driving
**Authors:** Chengkai Xu, Yicheng Guo, Jiaqi Liu, Yiming Cui, Shiyu Fang, Peng Hang, Hao Zhang, Jian Sun
**arXiv:** [arxiv.org/abs/2611.25604](https://arxiv.org/abs/2611.25604)
**Summary:** PAD values autonomous-driving demonstrations according to their utility for a particular target policy, combining scene calibration, projected policy gradients, and an approximation of local training geometry. The authors report EPDMS gains of 3.5 points on NavTest and 5.0 points on NavHard for DiffusionDrive, with policy-specific curation outperforming full-pool training across several planner families.

---

### 4. DailySafe: Benchmarking Dynamic Safety Awareness in Everyday Multi-Turn Multimodal Interactions
**Authors:** Xuankun Rong, Xinhao Deng, Wenzhang Jiang, Ziheng Peng, Siyuan Liang, Wenke Huang, Pablo Arbelaez, Mang Ye
**arXiv:** [arxiv.org/abs/2611.26298](https://arxiv.org/abs/2611.26298)
**Summary:** DailySafe evaluates dynamic safety awareness in 195 naturalistic multi-turn, multi-image interactions spanning 10 everyday domains and 42 task categories. Its case-specific annotations test whether multimodal assistants track progressively revealed contextual risks while continuing to support legitimate user goals.

---

### 5. Suppressing the Shortcut Hidden Behind the Gains of VideoLLM Fine-Tuning
**Authors:** Youngwoo Shin, Jongsuk Kim, Junmo Kim
**arXiv:** [arxiv.org/abs/2611.25776](https://arxiv.org/abs/2611.25776)
**Summary:** Video-Evidence Training via Orthogonal projection, or VETO, suppresses text-only shortcuts during VideoLLM fine-tuning by projecting updates away from the base model's text-only activation subspace. Across seven VideoLLMs, the authors report preserved in-distribution fine-tuning gains and stronger performance than standard fine-tuning on six shifted-distribution benchmarks.

---

### 6. S1CogBench: What System One Decision Models Can and Cannot Do on Cognitive Experiments
**Authors:** Dengzhe Hou, Kazunori D Yamada
**arXiv:** [arxiv.org/abs/2611.00911](https://arxiv.org/abs/2611.00911)
**Summary:** S1CogBench evaluates eight System One decision models using 24 established cognitive tasks and 27 evaluation modes covering human-response prediction, autonomous execution, and controlled task changes. The study finds that strong learning-task performance can coexist with failures to gather information or adapt to feedback, while model rankings also depend on the choice-readout method.

---

### 7. PlayCraft: Designing Engaging Games from Agent Play Experience
**Authors:** Weihao Cheng
**arXiv:** [arxiv.org/abs/2611.26624](https://arxiv.org/abs/2611.26624)
**Summary:** PlayCraft alternates between vision-based agent gameplay and game revision, using retained play experience to diagnose gaps in a target progression of player mastery. Fresh evaluations across three agent intelligence settings show larger learning gains and steeper learning slopes in most games, with improvements over baselines on both macro-averaged metrics.

---

### 8. In Situ Training of Optical Neural Networks by Coding Agents
**Authors:** Ilker Oguz, Colin Christian, Christophe Moser, Demetri Psaltis, Gordon Wetzstein
**arXiv:** [arxiv.org/abs/2611.23875](https://arxiv.org/abs/2611.23875)
**Summary:** Optics as code lets a coding agent train an optical neural network from camera measurements alone, requiring a physical hypothesis for each hardware probe rather than a calibrated differentiable model. The authors report improvements over gradient-free methods in classification and image encoding, approaching calibrated-model backpropagation at a fraction of its cost.

---

### 9. Squoosh Bench: Evaluating UX-1 on 318 Historical Website A/B Tests
**Authors:** Rohith Pasula, Johari Dramiga, Viraj Shah, Suzan Halim, Tyler Dooskin
**arXiv:** [arxiv.org/abs/2611.25200](https://arxiv.org/abs/2611.25200)
**Summary:** Squoosh Bench evaluates simulated-shopper forecasts on 318 historical website A/B tests while masking page roles and withholding recorded outcomes during inference. The authors report that the browsing-data-fine-tuned UX-1 model correctly classified 267 outcomes, or 84.0 percent, compared with 196, or 61.6 percent, for the strongest general-purpose configuration.

---

### 10. LittleBit: Ultra Low-Bit Quantization via Latent Factorization
**Authors:** Banseok Lee, Dongkyu Kim, Youngcheon You, Youngmin Kim
**arXiv:** [arxiv.org/abs/2506.13771](https://arxiv.org/abs/2506.13771)
**Summary:** LittleBit compresses LLM weights using low-rank latent factorization, binarized factors, multi-scale compensation, and quantization-aware initialization to target rates as low as 0.1 bits per weight. The authors report approximately 31-times memory reduction and compression of Llama2-13B below 0.9 GB, with sub-one-bit accuracy improvements and a potential inference-speed benefit rather than a demonstrated universal speedup.

---

### 11. Inhabitant: An Agent Framework for Long-Horizon Human-Scene Interaction with Spatial Control and Quantitative Feedback
**Authors:** Yao Zhang, Zhuchenyang Liu, Yu Xiao
**arXiv:** [arxiv.org/abs/2611.25005](https://arxiv.org/abs/2611.25005)
**Summary:** Inhabitant is a training-free framework for long-horizon human-scene interaction that specifies positions, paths, and poses, measures execution errors, and revises spatial controls. On its 75-task Inhabit benchmark covering 31 apartment layouts, the authors report up to 98.7 percent task completion and ablations showing the importance of spatial control and quantitative feedback.

---

### 12. Time Series Structure Learning with Local Causal Parent Discovery
**Authors:** Jacqueline Maasch, Shu Wan, Hank Zhu, Huan Liu, Zhiguang Wang
**arXiv:** [arxiv.org/abs/2611.26232](https://arxiv.org/abs/2611.26232)
**Summary:** Iterative Temporal Parent Discovery learns causal graphs for nonstationary multivariate time series by finding local parent sets and replacing higher-order conditional-independence tests with lower-order alternatives. The authors report a favorable F1-versus-runtime trade-off in simulations and speedups of 2.3, 9.1, and 40.9 times over three compared methods on 2,000-node graphs.

---

### 13. Lang-SVG: Hierarchical Image Vectorization with Language Priors
**Authors:** Xi Liu, Chaoyi Zhou, Run Wang, Jiaang Li, Feng Luo, Junxiang Huang, Siyu Huang
**arXiv:** [arxiv.org/abs/2611.15941](https://arxiv.org/abs/2611.15941)
**Summary:** Lang-SVG turns raster images into editable SVG trees with semantic labels and explicit object-part relationships, using segmentation priors and multimodal language models. Depth-adaptive simplification, tree-guided pruning and merging, and recovery of missing regions improve compactness, while the authors report leading rendering fidelity and structural quality under their evaluation protocol.

---

### 14. TwinD: Generalizing Deepfake Detection from Blending to Entire Face Synthesis
**Authors:** Andrii Yermakov, Jan Cech, Mario Fritz, Jiri Matas
**arXiv:** [arxiv.org/abs/2611.25935](https://arxiv.org/abs/2611.25935)
**Summary:** TwinD trains deepfake detectors with reconstruction twins and blob twins that expose complementary decoder and blending cues, aiming to generalize beyond pasted-face manipulations to entire-face synthesis. On a benchmark of 19 datasets, the authors report mean AUROC of 96.3 percent, including 95.6 percent on entire-face-synthesis datasets, and release code, model weights, and training data.

---

### 15. Efficient and Robust Drafting with Multi-Token Prediction
**Authors:** Filippo Galgani, Ziwei Ji, Omri Homburger, Ganesh Jawahar, Michelle Ramanovich, Ivan Korotkov, Luciano Martins, Utku Evci, Edouard Yvinec, Pooja Consul, Vivek Kumar, Tal Schuster
**arXiv:** [arxiv.org/abs/2611.25813](https://arxiv.org/abs/2611.25813)
**Summary:** G-MTP adds a shared multi-token drafting head with target-activation injection, zero-copy KV-cache cross-attention, and clustered vocabulary projection to accelerate speculative decoding. For the evaluated Gemma 4 models, the authors report speedups up to 3.1 times on server setups and 2.2 times on a smartphone GPU, alongside parameter-efficient tuning that reduces target forward passes under domain shift.

---

### 16. VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin
**Authors:** Samir Khaki, Wei-Chen Wang, Song Han, Ryan Hanrui Wang
**arXiv:** [arxiv.org/abs/2611.25717](https://arxiv.org/abs/2611.25717)
**Summary:** VR-SparseQuant uses overlapping 2:4 sparse activation streams, offline scale calibration, and shared-weight GEMM accumulation to improve FP4 accuracy while retaining native Vera Rubin execution. The authors report WikiText-2 perplexity reduction from 6.85 to 5.57 on Nemotron-3-Nano-30B-A3B and native-kernel speedups up to 3.1 times for GEMM and 2.7 times for MoE over BF16, including activation preparation.

---

### 17. ROAM-GRPO: Enforcing Reasoning Diversity in GRPO via Routed Off-mode Approach Mining
**Authors:** Jeff Duan, Matt Thomson
**arXiv:** [arxiv.org/abs/2611.25926](https://arxiv.org/abs/2611.25926)
**Summary:** ROAM-GRPO routes already well-solved training problems into an off-mode track that prompts alternative reasoning strategies, checks them with an LLM judge, and self-distills accepted alternatives. On a 1,000-problem MATH level-five subset with Qwen3.5-2B, the authors report a 4.7 percent increase in peak pass-at-16 and roughly 1.5-to-2-times greater correct-answer embedding distance on a difficult evaluation set.

---

### 18. World Models Favor Learned Priors over Visual Evidence
**Authors:** Han Xiao, Zhiyong Bao, Xiaotong Liu, Yanhao Chen, Qingqiang Wu
**arXiv:** [arxiv.org/abs/2611.26366](https://arxiv.org/abs/2611.26366)
**Summary:** TailWorld evaluates whether world models infer physical rules from short calibration videos or instead favor common training dynamics, separating training imbalance from the informativeness of visual evidence. The proposed Rule Inference for Transfer method explicitly controls training-frequency influence and improves rare-dynamics prediction and physical consistency under the evaluated imbalances and distribution shifts.

---

### 19. SiliconGym: A Versatile Reinforcement Learning Environment for Agentic EDA
**Authors:** Hejia Zhang, Sheng Lu, Yitong Ma, Zhongming Yu, Zhijing Wu, Wentao Ni, Chia-Tung Ho, Jishen Zhao
**arXiv:** [arxiv.org/abs/2611.25658](https://arxiv.org/abs/2611.25658)
**Summary:** SiliconGym provides a cross-task, cross-toolchain reinforcement-learning environment for hardware design and verification, separating versioned workspaces, budgeted execution, and acceptance-gated scoring. The authors report a 21.9 percent faster 256-answer RL batch than native ChipSeek and evaluate how open-source-trained functional correctness and PPA improvements transfer to commercial EDA backends.

---

### 20. Represented but misread: Post-training changes how language models read out what they represent
**Authors:** Jochen Laubrock
**arXiv:** [arxiv.org/abs/2611.26584](https://arxiv.org/abs/2611.26584)
**Summary:** This study compares linear probes with model answers across six open-weight base-model families and their post-trained versions to distinguish represented information from how judgments are read out. Post-training reduces answer sensitivity on the evaluated human-versus-AI authorship task but repairs answers on public negated-statement examples, showing task-dependent readout changes rather than a uniform loss of represented knowledge.
