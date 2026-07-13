---
title: "Daily AI Papers — July 13, 2026"
date: 2026-07-13
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-13/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - long-horizon-agents
  - visual-pretraining
  - llm-quantization
---

## 1. Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading

**Authors:** Zongxia Li, Zhongzhi Li, Yucheng Shi, Ruhan Wang, Junyao Yang, Zhichao Liu, Xiyang Wu, Anhao Li, Yue Yu, Ninghao Liu, Lichao Sun, Haotao Mi, LeoweiLiang  
**arXiv:** [arxiv.org/abs/2607.08964](https://arxiv.org/abs/2607.08964)  
**Sources:** HuggingFace Daily Papers (42 upvotes).  
**Why Trending:** Highest-upvoted paper on HF today; agent long-horizon evaluation is one of the hottest open problems in the field, and the stark 15% pass rate is a striking, shareable result.

A new benchmark of 46 long-horizon terminal tasks (experiment reproduction, SWE, multimodal analysis, games, scientific computing) that decomposes each task into fine-grained graded subtasks for dense, partial-credit rewards instead of pass/fail. Evaluating 15 frontier models shows agents burn ~9.9M tokens and ~85 minutes per task on average, yet the best model still only hits 15.2% pass@1 at a 0.95 partial-reward threshold — exposing a big gap in long-horizon agent capability.

---

## 2. Scalable Visual Pretraining for Language Intelligence

**Authors:** Yiming Zhang, Zhonghan Zhao, Wenwei Zhang, Haiteng Zhao, Tianyang Lin, Yunhua Zhou, Demin Song, Kuikun Liu, Haochen Ye, Haian Huang, Yuzhe Gu, Haijun Lv, Qipeng Guo, Bin Liu, Gaoang Wang, Kai Chen  
**arXiv:** [arxiv.org/abs/2607.09657](https://arxiv.org/abs/2607.09657)  
**Sources:** HuggingFace Daily Papers (39 upvotes).  
**Why Trending:** Second-highest HF upvotes today; taps into the growing "text-only pretraining is leaving value on the table" narrative that's been building all year.

Argues that converting visually rich documents (figures, equations, layouts) to plain text for LLM pretraining discards information, and proposes a scalable visual-pretraining recipe that keeps document structure intact as a signal for language intelligence. Shows gains on downstream language reasoning tasks that depend on document/structural understanding, not just raw text.

---

## 3. Video Generation Models are General-Purpose Vision Learners

**Authors:** Letian Wang, Chuhan Zhang, Rishabh Kabra, Jasper Uijlings, Steven Waslander, Andrew Zisserman, Joao Carreira, Kaiming He, Misha Andriluka, Eduard Gabriel Bazavan, Andrei Zanfir, Cristian Sminchisescu  
**arXiv:** [arxiv.org/abs/2607.09024](https://arxiv.org/abs/2607.09024)  
**Sources:** HuggingFace Daily Papers (34 upvotes).  
**Why Trending:** Star-studded author list (Kaiming He of ResNet fame, Andrew Zisserman of VGG, plus DeepMind researchers) makes a big claim about the future of CV foundation models — exactly the kind of paper that lights up ML Twitter.

Argues large-scale text-to-video generation is computer vision's answer to NLP's next-token-prediction pretraining, providing spatiotemporal priors and vision-language alignment for general-purpose visual intelligence. Introduces "GenCeption," using video generation as a foundation-model pretraining paradigm rather than a narrow content-generation task.

---

## 4. Trust Region Policy Distillation

**Authors:** Zhengpeng Xie, Li Lyna Zhang, Zeke Xie, Mao Yang  
**arXiv:** [arxiv.org/abs/2607.04751](https://arxiv.org/abs/2607.04751)  
**Sources:** HuggingFace Daily Papers (17 upvotes).  
**Why Trending:** Rare paper offering rigorous convergence theory for a practical LLM post-training technique, appealing to both theory and applied RLHF/distillation crowds.

Introduces TOP-D (Trust Region Policy Distillation), which stabilizes the notoriously unstable, high-variance On-Policy Distillation by dynamically constructing a proximal teacher, with a formal global convergence proof and monotonic improvement guarantee. Positions itself as a more reliable way to break big training goals into small, provably stable steps.

---

## 5. KronQ: LLM Quantization via Kronecker-Factored Hessian

**Authors:** Donghyun Lee, Yuhang Li, Ruokai Yin, Priyadarshini Panda  
**arXiv:** [arxiv.org/abs/2607.07964](https://arxiv.org/abs/2607.07964)  
**Sources:** HuggingFace Daily Papers (12 upvotes).  
**Why Trending:** Efficient-inference/quantization work consistently draws attention from the local-LLM and edge-deployment crowd.

Challenges GPTQ-style second-order quantization methods that only use input-activation statistics by folding gradient covariance into a Kronecker-factored Hessian approximation, so the quantization loss accounts for output-channel importance too. Aims at better accuracy-per-bit for post-training LLM quantization without retraining.

---

## 6. From RGB Generation to Dense Field Readout: Pixel-Space Dense Prediction with Text-to-Image Models

**Authors:** Zanyi Wang, Xin Lin, Haodong Li, Dengyang Jiang, Yijiang Li  
**arXiv:** [arxiv.org/abs/2607.06553](https://arxiv.org/abs/2607.06553)  
**Sources:** HuggingFace Daily Papers (9 upvotes).  
**Why Trending:** Speaks to a recurring critique in the vision community about over-fitting diffusion-model tricks onto tasks that don't need them.

Argues that reusing text-to-image priors for dense prediction (depth, normals, masks) by decoding annotations as RGB-like images inherits an unnecessary generative interface. Proposes a more direct pixel-space dense-field readout that better matches the pixel-correct nature dense prediction actually needs.

---

## 7. PanoWorld: Real-World Panoramic Generation

**Authors:** Haoyuan Li, Dizhe Zhang, Yuemei Zhou, Xiangkai Zhang, Haoran Feng, Xiaofan Lin, Wenjie Jiang, Bo Du, Ming-Hsuan Yang, Lu Qi  
**arXiv:** [arxiv.org/abs/2607.09661](https://arxiv.org/abs/2607.09661)  
**Sources:** HuggingFace Daily Papers (7 upvotes).  
**Why Trending:** Panoramic/world-model generation is a fast-growing subfield feeding into VR and embodied-AI applications.

Tackles long-range memory in panoramic world models by exploiting the rotation-equivariant structure of omnidirectional views, simplifying camera trajectories to translations via fixed headings. Introduces Dense Panoramic Ray-Conditioning and Geometry-aware Memory Augmentation, trained via a three-stage pipeline.

---

## 8. Self-Guided Test-Time Training for Long-Context LLMs

**Authors:** Xinyu Zhu, Zhe Xu, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Kaushik Rangadurai, Hua Zhi, Frank Shyu, Sandeep Pandey, Luke Simon, Yu Meng, Xi Liu  
**arXiv:** [arxiv.org/abs/2607.09415](https://arxiv.org/abs/2607.09415)  
**Sources:** HuggingFace Daily Papers (7 upvotes).  
**Why Trending:** Long-context utilization ("lost in the middle"-style failures) remains one of the most practically painful LLM limitations for real deployments.

Shows that just extending context windows doesn't guarantee LLMs use long inputs well, and proposes self-guided test-time training (TTT) that adapts to the test context cheaply by selectively targeting the most relevant evidence, instead of prohibitively expensive full-context TTT.

---

## 9. Towards Mechanistically Understanding Why Memorized Knowledge Fails to Generalize in Large Language Model Finetuning

**Authors:** Lu Dai, Ziyang Rao, Yili Wang, Hanqing Wang, Hao Liu, Hui Xiong  
**arXiv:** [arxiv.org/abs/2607.08393](https://arxiv.org/abs/2607.08393)  
**Sources:** HuggingFace Daily Papers (5 upvotes).  
**Why Trending:** Mechanistic interpretability applied to a very concrete, widely-felt finetuning pain point (injecting facts that don't transfer to reasoning).

Formalizes the "Knowing–Using Gap" — LLMs memorize injected facts quickly but fail to use them in downstream reasoning — and uses a novel "self-patching" intervention to trace the internal spatial/temporal dynamics of how memorized knowledge does (or doesn't) permeate into usable representations.

---

## 10. Flow-ERD: Agent-type Aware Flow Matching with Entropy-Regularized Distillation for Diverse Traffic Simulation

**Authors:** Seulbin Hwang, Kiyoung Om, Daejung Kim, Jinhan Lee  
**arXiv:** [arxiv.org/abs/2607.06957](https://arxiv.org/abs/2607.06957)  
**Sources:** HuggingFace Daily Papers (4 upvotes).  
**Why Trending:** Traffic simulation diversity is a known bottleneck for autonomous-driving training pipelines.

Proposes a multi-agent traffic simulator that optimizes for both realism and diversity (most prior work over-indexes on realism alone), using Agent-Type Aware Flow Matching plus entropy-regularized distillation to preserve fine-grained behavioral diversity per agent type.

---

## 11. Phone Segmentation and Recognition through Phonological Activation Mapping

**Authors:** Shikhar Bharadwaj, Kwanghee Choi, Stephen McIntosh, Chin-Jou Li, Eunjung Yeo, Daisuke Saito, Nobuaki Minematsu, Shinji Watanabe, Jian Zhu, David Harwath, David R. Mortensen  
**arXiv:** [arxiv.org/abs/2607.09020](https://arxiv.org/abs/2607.09020)  
**Sources:** HuggingFace Daily Papers (2 upvotes).  
**Why Trending:** Elegant unification of two speech tasks usually modeled separately, backed by a strong multi-institution author list (CMU, Waseda, etc.).

Shows phonetic structure is already latent in self-supervised speech model representations, and introduces "SPAM" to map those representations to phonological feature activations (voicing, nasality, etc.), enabling lightweight, gradient-descent-free heads for both phone segmentation and recognition from one shared representation.

---

## 12. MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models

**Authors:** Hyunjae Kim, Dain Kim, Pan Xiao, Serina S. Applebaum, Younjoon Chung, and 20+ others  
**arXiv:** [arxiv.org/abs/2607.07673](https://arxiv.org/abs/2607.07673)  
**Sources:** HuggingFace Daily Papers (2 upvotes).  
**Why Trending:** Medical foundation models are a major applied-AI growth area, and data-scaling infrastructure papers tend to get reused widely once released.

Introduces an automated, continuously-updatable framework that mines PubMed Central's expert-authored image-text literature into high-fidelity, reproducible training data for medical multimodal foundation models — addressing the data-scarcity bottleneck in medical AI.

---

## 13. A Sovereign, Open-Source Foundation Model for German and English

**Authors:** The Soofi-Team (Benedikt Droste, David Fitzek, Ruben Härle, Lukas Helff, and others)  
**arXiv:** [arxiv.org/abs/2607.09424](https://arxiv.org/abs/2607.09424)  
**Sources:** HuggingFace Daily Papers (1 upvote).  
**Why Trending:** "AI sovereignty" (non-US/non-China open models) is a hot geopolitical/policy angle in AI right now, especially in the EU.

Presents Soofi S 30B-A3B, an open-source hybrid Mamba-Transformer Mixture-of-Experts model (3B of 30B params active per token) pretrained on ~27T tokens with German up-weighted, matching dense 14–27B models on English/German benchmarks while leading on code in both languages — pitched explicitly as European AI sovereignty infrastructure.

---

## 14. VaseMuseum: Digital Intelligent Museum for Ancient Greek Pottery

**Authors:** Jiazi Wang, Nonghai Zhang, Qiushi Xie, Zeyu Zhang, Yufeng Chen, Yang Zhao, Ling Shao, Hao Tang  
**arXiv:** [arxiv.org/abs/2607.06374](https://arxiv.org/abs/2607.06374)  
**Sources:** HuggingFace Daily Papers (0 upvotes, newest listing).  
**Why Trending:** Niche but a nice example of VLM grounding/hallucination-avoidance techniques applied to a concrete cultural-heritage use case.

Builds a VLM-based interactive digital museum for ancient Greek pottery, tackling two hard problems for cultural-heritage VLMs: grounding open-ended interpretation in specialized curatorial knowledge without unverifiable retrieval, and avoiding confident-but-wrong answers when evidence is incomplete or noisy.

---

## 15. Mach-Mind-4-Flash Technical Report

**Authors:** Foundation Model Team (Li Auto Inc)  
**arXiv:** [arxiv.org/abs/2607.09375](https://arxiv.org/abs/2607.09375)  
**Sources:** arXiv (cs.CL, new submission July 13) — not yet reflected in HF Daily Papers curation.  
**Why Trending:** New efficient-agentic-model technical reports from industry labs (here, Li Auto) reliably draw fast attention from the open-model community for benchmarking against Qwen/DeepSeek-class releases.

Technical report for Mach-Mind-4-Flash, a 35B-parameter MoE agentic model with only 3B activated parameters that matches or beats 100B-class models purely through post-training optimization (large-scale RL in scalable agentic environments) rather than more pretraining compute.

---

## 16. Statistically Undetectable Backdoors in Deep Neural Networks

**Authors:** Andrej Bogdanov, Alon Rosen, Neekon Vafa  
**arXiv:** [arxiv.org/abs/2607.09532](https://arxiv.org/abs/2607.09532)  
**Sources:** arXiv (cs.LG, new submission July 13); referenced by an MIT CSAIL research seminar — not yet reflected in HF Daily Papers curation.  
**Why Trending:** Theoretical AI-safety result with real teeth: it implies white-box auditing alone can never rule out backdoors, a topic of active concern for model-supply-chain security.

Shows an adversarial model trainer can plant backdoors in a broad class of deep feedforward networks that are statistically undetectable even given full white-box access to the weights, under standard cryptographic hardness assumptions — extending the theoretical line of work on cryptographic ML backdoors.

---

## 17. HALO: Hybrid Adaptive Latent Reasoning for Language Models

**Authors:** Micah Zhang  
**arXiv:** [arxiv.org/abs/2607.08775](https://arxiv.org/abs/2607.08775)  
**Sources:** arXiv (cs.CL, new submission July 13) — not yet reflected in HF Daily Papers curation.  
**Why Trending:** Latent/adaptive-compute reasoning (as opposed to explicit chain-of-thought tokens) is one of the fastest-moving research threads in LLM efficiency right now.

Proposes a way to add adaptive extra "thinking" compute to a frozen pretrained LLM: a coarse refinement stage over all tokens plus a selective, token-scored second refinement stage on a subset of tokens, avoiding the waste of either a too-weak single pass or an expensive full second pass everywhere.

---

## 18. A Survey on the Green Development of Large Models: From Resource-Efficient Architectures to Hardware-Software Co-Design

**Authors:** Linhui Xiao, Guiping Cao, Mingyue Guo, Xianchao Guan, Fan Yang, Ming Tao, Xin Li, Yuxin Peng, Yaowei Wang  
**arXiv:** [arxiv.org/abs/2607.09084](https://arxiv.org/abs/2607.09084)  
**Sources:** arXiv (cs.LG, new submission July 13) — not yet reflected in HF Daily Papers curation.  
**Why Trending:** AI energy consumption is under increasing scrutiny; broad surveys on "green AI" tend to get widely bookmarked and cited as reference material.

A comprehensive survey of energy/compute-efficient large-model development, covering attention-operator optimization, linear-complexity architectures, sparsification, and full-stack hardware-software co-design aimed at reducing the environmental footprint of frontier AI.

---

## 19. Training, Reading, and Editing Legible Transformers

**Authors:** Mark Oskin  
**arXiv:** [arxiv.org/abs/2607.08946](https://arxiv.org/abs/2607.08946)  
**Sources:** arXiv (cs.CL, new submission July 13) — not yet reflected in HF Daily Papers curation.  
**Why Trending:** Interpretability-by-construction is a growing alternative to post-hoc interpretability (SAEs, probing), and this offers a concrete, fixable training pathology.

Builds transformers from operators that are legible by construction — bounded, named units behaving like fuzzy-set operations rather than dense activations — and identifies a training failure mode where a naive "crispness penalty" collapses detectors into dead constants, fixing it with a per-channel variance floor.

---

## 20. Correlation-Aware Contextual Bandits with Surrogate Rewards for LLM Routing

**Authors:** Ajay Narayanan Sridhar, Ronak Singh, Mehrdad Mahdavi, Vijaykrishnan Narayanan  
**arXiv:** [arxiv.org/abs/2607.09015](https://arxiv.org/abs/2607.09015)  
**Sources:** arXiv (cs.LG, new submission July 13) — not yet reflected in HF Daily Papers curation.  
**Why Trending:** LLM routing (sending queries to the cheapest sufficient model) has become a standard cost-control technique in production LLM systems, making the underlying bandit theory practically relevant.

Studies contextual bandits with correlated arms and noisy surrogate reward signals from an ML model, directly motivated by LLM routing (picking which model to call per-query). Proposes a coupled reward-mixing approach that pools true and surrogate rewards to route more efficiently than classical independent-arm bandits.

---
