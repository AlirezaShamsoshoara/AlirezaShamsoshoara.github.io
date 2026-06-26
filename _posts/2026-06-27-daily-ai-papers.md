---
title: "Daily AI Papers — June 27, 2026"
date: 2026-06-27
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-27/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - multimodal-models
  - embodied-ai
---

## 1. Autoregressive Boltzmann Generators
**Authors:** Danyal Rehman, Charlie B. Tan, Yoshua Bengio, Avishek Joey Bose
**arxiv:** [arxiv.org/abs/2606.27361](https://arxiv.org/abs/2606.27361)

Boltzmann Generators (BGs) allow rapid generation of uncorrelated thermodynamic equilibrium samples by combining a generative model with exact likelihoods and importance sampling correction, but existing BGs rely on normalizing flows that suffer from limited expressivity or scalability. This work introduces Autoregressive Boltzmann Generators, replacing the flow backbone with a more expressive autoregressive model to overcome the representation bottleneck in equilibrium molecular sampling.

---

## 2. Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
**Authors:** Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
**arxiv:** [arxiv.org/abs/2606.26080](https://arxiv.org/abs/2606.26080)

The log-probability ratio between an RL-trained LLM policy and its reference policy provably recovers the optimal advantage function under a general Markov decision process, yielding an annotation-free, domain-agnostic step-level reward signal. Validated across test-time scaling, uncertainty quantification, and failure attribution on five benchmarks, this "progress advantage" consistently outperforms confidence baselines and surpasses dedicated trained reward models without any task-specific training.

---

## 3. RiVER: Ranking-Induced Verifiable RL without Ground-Truth Solutions
**Authors:** (University team — arxiv 2606.27369)
**arxiv:** [arxiv.org/abs/2606.27369](https://arxiv.org/abs/2606.27369)

RiVER (Ranking-induced VERifiable framework) trains LLMs on score-based optimization tasks using deterministic execution feedback as continuous-valued supervision, bypassing the need for ground-truth solutions. The method applies group-relative RL to continuous reward signals rather than binary outcomes, enabling policy improvement on tasks like design, code optimization, and other open-ended domains where correctness cannot be binary-verified.

---

## 4. CARVE: Content-Aware Recurrent with Value Efficiency for Chunk-Parallel Linear Attention
**Authors:** Sayak Dutta
**arxiv:** [arxiv.org/abs/2606.27229](https://arxiv.org/abs/2606.27229)

Standard delta-rule recurrent models decide what to erase from memory without reading the stored memory state, while also wasting parameters via a value-axis erase mask that mathematically prevents full-rank memory updates. CARVE introduces content-aware (memory-reading) gates and a joint value/erase integration with chunk-parallel execution, provably removing all three defects while maintaining linear-time inference.

---

## 5. Ask, Don't Judge: Binary Questions for Interpretable LLM Evaluation (BINEVAL)
**Authors:** Sangwoo Cho, Kushal Chawla, Pengshan Cai, Zefang Liu
**arxiv:** [arxiv.org/abs/2606.27226](https://arxiv.org/abs/2606.27226)

BINEVAL decomposes evaluation criteria into atomic binary questions and aggregates verdicts into interpretable, multi-dimensional scores, replacing opaque holistic LLM judge scores with transparent criterion-specific assessments. The framework enables both standalone LLM evaluation and self-improvement feedback loops by making quality dimensions explicit and independently auditable.

---

## 6. E-TTS: A New Embodied Test-Time Scaling Framework for Robotic Manipulation
**Authors:** Wen Ye, Peiyan Li, Tingyu Yuan, Yuan Xu
**arxiv:** [arxiv.org/abs/2606.27268](https://arxiv.org/abs/2606.27268)

E-TTS studies the scaling mechanism of reasoning for embodied policies and addresses the critical challenge that historical context is essential in long-horizon sequential tasks, making sole reliance on current observations for action scaling inadequate. The framework provides a principled approach to scaling test-time compute for robotic manipulation while preserving temporal context across interaction steps.

---

## 7. Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation
**Authors:** Ritesh Thawkar, Shravan Venkatraman, Omkar Thawakar
**arxiv:** [arxiv.org/abs/2606.27376](https://arxiv.org/abs/2606.27376)

This work proposes a self-evolving framework with three internal roles — a Proposer that generates visual questions, a Solver that answers them, and a Generator that produces images — that improve both visual understanding and generation from unlabeled images without any external supervision. The closed-loop training signal between roles enables joint improvement across both modalities autonomously.

---

## 8. Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization
**Authors:** Tianyi Men, Zhuoran Jin, Pengfei Cao, Yubo Chen
**arxiv:** [arxiv.org/abs/2606.27330](https://arxiv.org/abs/2606.27330)

Open-source MLLMs for GUI web agents suffer from weak planning and limited cross-website generalization compared to commercial models, and existing approaches lack mechanisms for agents to learn from exploration experience. This work introduces autonomous experience exploration combined with hindsight experience utilization to enable small, privacy-preserving models to accumulate planning knowledge across diverse web tasks.

---

## 9. Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy
**Authors:** Junhao Shi, Zezheng Huai, Siyin Wang, Jia Chen
**arxiv:** [arxiv.org/abs/2606.27251](https://arxiv.org/abs/2606.27251)

This work proposes a unified cyber-physical action space for persistent embodied agents that spans APIs, IoT, manipulation, and navigation in unstructured environments, paired with autonomous recovery mechanisms for the physical failures that inevitably arise during extended operation. The approach addresses memory accumulation and context-overflow failures in VLM-based planners operating over long horizons.

---

## 10. Beyond the Hard Budget: Sparsity Regularizers for More Interpretable Top-k Sparse Autoencoders
**Authors:** Nathanaël Jacquier, Maria Vakalopoulou, Mahdi S. Hosseini
**arxiv:** [arxiv.org/abs/2606.27321](https://arxiv.org/abs/2606.27321)

Standard Top-k SAEs enforce sparsity architecturally by retaining only the k most active latents per input, potentially pruning meaningful lower-ranked features during training. This paper proposes soft sparsity regularizers that replace the hard budget constraint, enabling more principled feature selection and producing more interpretable sparse decompositions of vision foundation model activations.

---

## 11. World Action Models Enable Continual Imitation Learning with Recurrent Generative Replay (REGEN)
**Authors:** Manish Kumar Govind, Dominick Reilly, Smit Patel
**arxiv:** [arxiv.org/abs/2606.27374](https://arxiv.org/abs/2606.27374)

REGEN leverages World Action Models' ability to generate future visual observations to synthesize pseudo-replay trajectories, allowing a robot policy to rehearse previously learned tasks during continual adaptation without storing the original human demonstrations. This eliminates the data storage and privacy constraints of replay-based continual learning methods.

---

## 12. DnA: Denoising Attention for Visual Tasks
**Authors:** Ron Campos, Subhajit Maity, Xin Li
**arxiv:** [arxiv.org/abs/2606.27372](https://arxiv.org/abs/2606.27372)

DnA introduces a dual-query attention mechanism where a positive query identifies image features belonging to the correct class while a negative query identifies and suppresses noise, producing sharper attention patterns without additional parameters. Applied within multihead attention, DnA improves dense prediction performance by reducing spurious activations that degrade feature quality.

---

## 13. When are Likely Answers Right? On Sequence Probability and Correctness in LLMs
**Authors:** Johannes Zenn, Jonas Geiping
**arxiv:** [arxiv.org/abs/2606.27359](https://arxiv.org/abs/2606.27359)

Many LLM decoding methods implicitly assume that higher-probability outputs are more correct, yet this assumption is rarely examined systematically. This paper analyzes when the conditional probability of a continuation actually aligns with correctness, providing principled criteria for when probability-based decoding strategies succeed or fail.

---

## 14. Don't Settle at the Mode! Mitigating Diversity Collapse in Pretrained Flow Models
**Authors:** Pradhaan S Bhat, Rishubh Parihar, Abhijnya Bhat
**arxiv:** [arxiv.org/abs/2606.27371](https://arxiv.org/abs/2606.27371)

State-of-the-art flow models generate high-quality images but suffer from diversity collapse when producing multiple samples under the same conditioning, with existing fixes requiring either heavy latent guidance or costly external reward models. This work introduces a parameter-efficient approach to restore generation diversity by modifying the flow trajectory structure itself, requiring no external components at inference time.

---

## 15. RayPE: Ray-Space Positional Encoding for 3D-Aware Video Generation
**Authors:** Minghao Yin, Jiahao Lu, Wenbo Hu
**arxiv:** [arxiv.org/abs/2606.27345](https://arxiv.org/abs/2606.27345)

RayPE replaces standard (u,v,t) RoPE in video diffusion transformers with Plucker-based positional encodings derived from camera ray pairs, capturing the true 3D geometric relation between viewpoints via the Plucker reciprocal product — which is bilinear in rays, matching the dot-product structure of Transformer attention. This enables 3D-consistent multi-view video generation without architectural changes to the underlying diffusion transformer.

---

## 16. SAM2Matting: Generalized Image and Video Matting
**Authors:** Ruiqi Shen, Guangquan Jie, Chang Liu
**arxiv:** [arxiv.org/abs/2606.27339](https://arxiv.org/abs/2606.27339)

SAM2Matting bridges the gap between SAM2's high-level frame-wise tracking and the low-level fine-grained detail extraction required for accurate alpha matte prediction in both images and videos. By reformulating matting as a guided segmentation refinement task within SAM2's architecture, the approach achieves strong generalization without relying on expensive domain-specific matting datasets.

---

## 17. How Post-Training Shapes Biological Reasoning Models
**Authors:** Lukas Fesser, Hanlin Zhang, Michelle M. Li, Eric Wang, Bryan Perozzi
**arxiv:** [arxiv.org/abs/2606.16517](https://arxiv.org/abs/2606.16517)

This paper studies how SFT, RL, and other post-training stages shape reasoning and generalization in biological reasoning models combining language models with multimodal biological data (DNA, RNA, proteins) across genomics, transcriptomics, and protein tasks. By training and evaluating over 100 models under controlled conditions, it identifies when post-training improves performance and when it induces over-specialization at the expense of generalization.

---

## 18. ABACUS: Adapting Unified Foundation Model for Bridging Image Count Understanding and Generation
**Authors:** Anindya Mondal, Sauradip Nag, Anjan Dutta
**arxiv:** [arxiv.org/abs/2606.23835](https://arxiv.org/abs/2606.23835)

ABACUS adapts a 3B-parameter unified foundation model for object counting using density-aware adaptive zooming with objectness maps, a boundary-aware count policy via GRPO to eliminate crop-boundary errors, and a cycle-consistent GRPO strategy where the understanding branch self-critiques generated outputs. It achieves state-of-the-art across seven benchmarks without benchmark-specific training, demonstrating that a single model can simultaneously understand and generate with count fidelity.

---

## 19. OpenBioRQ: Unsolved Biomedical Research Questions for Agents
**Authors:** Minbyul Jeong
**arxiv:** [arxiv.org/abs/2606.21959](https://arxiv.org/abs/2606.21959)

OpenBioRQ benchmarks agentic LLMs on genuinely unsolved biomedical research questions, revealing that while citation fabrication is rare, citation-to-wrong-paper errors occur in roughly 15.9% of cases — a failure mode invisible to benchmarks where the ground-truth source can be reproduced from the answer key. This benchmark design forces independent source retrieval rather than answer-conditioned memorization, exposing a significant reliability gap in current biomedical AI agents.

---

## 20. Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models
**Authors:** Shravan Venkatraman, Ritesh Thawkar, Omkar Thawakar
**arxiv:** [arxiv.org/abs/2606.27373](https://arxiv.org/abs/2606.27373)

Existing self-evolving LMM frameworks using multi-role self-play and self-consistency rewards optimize answer agreement without ensuring the decoder actually attends to visual content, allowing statistical shortcuts to dominate. This work proposes visual attention regularization during self-evolution to enforce genuine visual token engagement, preventing modality collapse in unsupervised multimodal self-improvement.
