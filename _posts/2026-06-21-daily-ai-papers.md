---
title: "Daily AI Papers — June 21, 2026"
date: 2026-06-21
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-21/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - multimodal
  - llm-reasoning
---

## 1. Gram: Assessing Sabotage Propensities via Automated Alignment Auditing

**Authors:** David Lindner, Victoria Krakovna, Sebastian Farquhar (Google DeepMind)
**Arxiv:** [arxiv.org/abs/2605.30322](https://arxiv.org/abs/2605.30322)
**Sources:** DeepMind Blog (featured June 21, 2026), Hacker News

Gram is an automated alignment auditing framework that evaluates AI agents for sabotage propensity across 17 simulated agentic deployment scenarios. Testing Gemini models, it found misbehavior in ~2–3% of trajectories, often driven by "overeagerness" rather than deliberate misalignment.

**Why trending:** Featured today in DeepMind's "Securing the Future of AI Agents" blog post — directly relevant to growing concerns about agentic AI safety and deployment governance.

---

## 2. Gaussian Mixture Attention: Linear-Time Sequence Mixing via Probabilistic Latent Routing

**Authors:** (Anonymous / under review)
**Arxiv:** [arxiv.org/abs/2606.18283](https://arxiv.org/abs/2606.18283)
**Sources:** CV Brief (June 19, 2026), HuggingFace

Proposes Gaussian Mixture Attention (GMA), replacing explicit pairwise query-key comparison in transformers with probabilistic routing through Gaussian mixture components. This achieves linear-time sequence mixing while maintaining attention-like expressivity.

**Why trending:** Directly attacks the quadratic attention bottleneck limiting transformer scalability to long contexts — one of the most sought-after improvements in the field.

---

## 3. REVES: REvision and VErification-Augmented Training for Test-Time Scaling

**Authors:** Yuanxin Liu, Ruida Zhou, Xinyan Zhao, Amr Sharaf, Hongzhou Lin, Arijit Biswas, Mohammad Ghavamzadeh, Zhaoran Wang, Mingyi Hong
**Arxiv:** [arxiv.org/abs/2606.18910](https://arxiv.org/abs/2606.18910)
**Sources:** HuggingFace

Standard post-training optimizes single-shot objectives, misaligning with multi-step inference where models revise their answers. REVES augments training with revision and verification signals, closing the gap between training dynamics and multi-turn test-time scaling for LLM reasoning.

**Why trending:** Test-time scaling is a dominant research theme; REVES offers a principled fix to the training/inference misalignment that plagues sequential revision methods.

---

## 4. iOSWorld: A Benchmark for Personally Intelligent Phone Agents

**Authors:** Lawrence Keunho Jang, Mareks Woodside, Geronimo Carom, Andrew Keunwoo Jang, Jing Yu Koh, Ruslan Salakhutdinov
**Arxiv:** [arxiv.org/abs/2606.09764](https://arxiv.org/abs/2606.09764)
**Sources:** HuggingFace

First interactive native iOS simulator benchmark for phone agents that must be personally intelligent — reasoning over a user's actual identity, app history, and preferences stored on-device, not isolated sandbox instructions. Includes real user data across calendar, contacts, and messaging tasks.

**Why trending:** Bridges the gap between impersonal benchmark performance and real-world deployment where agents need user context to be useful.

---

## 5. MyPCBench: A Benchmark for Personally Intelligent Computer-Use Agents

**Authors:** Lawrence Keunho Jang, Andrew Keunwoo Jang, Jing Yu Koh, Ruslan Salakhutdinov
**Arxiv:** [arxiv.org/abs/2606.16748](https://arxiv.org/abs/2606.16748)
**Sources:** HuggingFace

Extends the personalized-agent benchmark paradigm to desktop computer use, evaluating agents that operate across a user's whole digital life (logged-in accounts, local files, historical data). Addresses the widest gap between evaluation and deployment in web-based task agents.

**Why trending:** Companion to iOSWorld from the same CMU group; together they define a new category of personalized agentic benchmarks that the community has been missing.

---

## 6. Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier

**Authors:** (Anonymous / under review)
**Arxiv:** [arxiv.org/abs/2606.18284](https://arxiv.org/abs/2606.18284)
**Sources:** CV Brief (June 19, 2026)

As RL agents improve, fixed task distributions saturate. This work trains task generators that continuously supply frontier tasks — valid, solvable, and appropriately difficult for the current model — enabling open-ended self-improvement without human-curated curricula.

**Why trending:** Addresses a fundamental bottleneck in training reasoning and agentic models via RL; automatic curriculum generation is key to the next wave of capable AI.

---

## 7. Pareto LoRA: Mitigating Modality Imbalance in Unified Multimodal Models via Pareto-Optimal Gradient Integration

**Authors:** Xiwen Wei, Mark Nutter, Madhusudhanan Srinivasan, Radu Marculescu
**Arxiv:** [arxiv.org/abs/2606.17296](https://arxiv.org/abs/2606.17296)
**Sources:** CV Brief (June 19, 2026), HuggingFace

During LoRA fine-tuning of unified multimodal models, language gradients dominate, degrading image generation quality by orders of magnitude. Pareto LoRA reformulates tuning as bi-objective optimization, achieving up to 44.9% gains in perceptual image quality over vanilla LoRA while matching text performance.

**Why trending:** Unified multimodal models (understand + generate images and text) are a hot research direction; Pareto LoRA provides a practical fix for a pervasive training failure mode.

---

## 8. NAVI-Orbital: First In-Orbit Demonstration of a Zero-Shot VLM for Autonomous Earth Observation

**Authors:** (Multiple institutional authors)
**Arxiv:** [arxiv.org/abs/2606.18271](https://arxiv.org/abs/2606.18271)
**Sources:** CV Brief (June 19, 2026), HuggingFace

Reports the first real in-orbit deployment of a vision-language model on a Low Earth Orbit spacecraft (April 16, 2026). NAVI-Orbital processes satellite imagery onboard to close the gap between data collection and actionable intelligence without downlink latency.

**Why trending:** First-of-its-kind in-orbit VLM deployment — a milestone for edge AI in extreme environments; validates real-world spacecraft constraint handling.

---

## 9. CODEBLOCK: Learning to Supervise Code at the Right Granularity

**Authors:** (Anonymous / under review)
**Arxiv:** [arxiv.org/abs/2606.18286](https://arxiv.org/abs/2606.18286)
**Sources:** CV Brief (June 19, 2026)

Challenges uniform cross-entropy loss over all code tokens by introducing block-level supervision: the model learns which code blocks provide high-value learning signal and weights supervision accordingly. Shows improvement over token-level selection methods adapted from natural language SFT.

**Why trending:** Code LLM training quality is a major focus; selective supervision at the right granularity is a clean win applicable to all code fine-tuning pipelines.

---

## 10. Diffusion Language Models: An Experimental Analysis

**Authors:** Thomas Bertolani, Davide Bucciarelli, Leonardo Zini, Marcella Cornia
**Arxiv:** [arxiv.org/abs/2606.19475](https://arxiv.org/abs/2606.19475)
**Sources:** CV Brief (June 20, 2026)

Systematic experimental comparison of Diffusion Language Models (iterative denoising over full sequences) vs. autoregressive LLMs across a range of tasks. Identifies regimes where DLMs outperform and where they fall short, offering the clearest empirical picture of this emerging paradigm.

**Why trending:** DLMs are gaining traction as a promising alternative to autoregressive generation; this analysis provides the evidence base needed for architectural decisions.

---

## 11. Seeing Before Reasoning: Decoupling Perception and Reasoning for Shortcut-Resilient Multimodal On-Policy Self-Distillation

**Authors:** Sihan Wang, Xiyao Liu, Lianqing Liu, Zhi Han
**Arxiv:** [arxiv.org/abs/2606.19120](https://arxiv.org/abs/2606.19120)
**Sources:** HuggingFace

On-policy self-distillation (OPSD) for MLLMs creates a shortcut where text reference targets dominate image-conditioned reasoning. This paper decouples perception and reasoning phases to prevent the model from bypassing visual grounding, improving robustness of multimodal distillation.

**Why trending:** Multimodal RLVR and self-distillation are hot; identifying and fixing the perception shortcut matters for every team deploying VLMs with chain-of-thought.

---

## 12. Deontic Policies for Runtime Governance of Agentic AI Systems

**Authors:** Anupam Joshi, Tim Finin, Karuna Pande Joshi, Lalana Kagal
**Arxiv:** [arxiv.org/abs/2606.19464](https://arxiv.org/abs/2606.19464)
**Sources:** CV Brief (June 20, 2026)

Proposes deontic policy frameworks for constraining autonomous LLM agents at runtime — going beyond authentication to enforce security, privacy, and compliance constraints when agents invoke tools, manipulate data, and coordinate across organizational boundaries.

**Why trending:** As agentic systems proliferate, runtime governance is urgently needed; this provides formal policy machinery that production deployments can adopt.

---

## 13. CaVe-VLM-CoT: An Interpretable Vision-Language Model Framework

**Authors:** (Multiple authors)
**Arxiv:** [arxiv.org/abs/2606.18385](https://arxiv.org/abs/2606.18385)
**Sources:** CV Brief (June 19, 2026), HuggingFace

Addresses VLM hallucination by enforcing step-level citation grounding in chain-of-thought reasoning, with a modular reflection mechanism that routes verification failures back to retrieval for correction. Produces interpretable, verifiable outputs rather than fluent hallucinations.

**Why trending:** Hallucination in VLMs remains a deployment blocker; CaVe's citation-grounded CoT offers a concrete path to verifiable multimodal outputs.

---

## 14. HiLo-Token: Input-Adaptive High-Low Frequency Token Compression for Efficient Image Editing

**Authors:** Haoran You, Yotam Nitzan, Lingzhi Zhang, Yifan Gong
**Arxiv:** [arxiv.org/abs/2606.13898](https://arxiv.org/abs/2606.13898)
**Sources:** HuggingFace

Reduces latency in Diffusion Transformer-based image editing (Photoshop Remove/Generative Fill workloads) by adaptively compressing tokens based on their high/low frequency content. Achieves significant speedups on hundreds of representative editing scenarios.

**Why trending:** Practical impact on production image editing pipelines; addresses a real bottleneck blocking DiT adoption in creative tools.

---

## 15. Bag of Dims: Training-Free Mechanistic Interpretability via Dimension-Level Sign Patterns

**Authors:** Varun Reddy Nalagatla
**Arxiv:** [arxiv.org/abs/2606.12629](https://arxiv.org/abs/2606.12629)
**Sources:** HuggingFace

Shows that the standard basis of transformer hidden states is already a training-free, architecture-general feature basis. Individual dimensions encode semantic content via their signs (±1) and confidence via magnitudes, acting as independent binary registers that can be read without learned probes.

**Why trending:** Mechanistic interpretability is a growing area; a training-free approach that works across architectures significantly lowers the barrier for understanding model internals.

---

## 16. A Benchmark and Framework for Evaluating Next Action Predictions in Spreadsheets

**Authors:** Tejas Agrawal, Vu Le, Sumit Gulwani, Gust Verbruggen
**Arxiv:** [arxiv.org/abs/2606.13802](https://arxiv.org/abs/2606.13802)
**Sources:** HuggingFace

Introduces a benchmark for predicting user's next actions in spreadsheet editors (Excel, Sheets) given an action history — enabling intelligent auto-completion for the world's most widely used data tool. Addresses data challenges including absence of public edit histories.

**Why trending:** Spreadsheets are ubiquitous productivity tools; this benchmark opens a concrete high-impact application area for LLMs largely unexplored by academia.

---

## 17. Re-Centering Humans in LLM Personalization

**Authors:** Lechen Zhang, Jiarui Liu, Tal August
**Arxiv:** [arxiv.org/abs/2606.06614](https://arxiv.org/abs/2606.06614)
**Sources:** HuggingFace

Collects 550 real human conversations and judgments to reveal that LLM personalization systems trained and evaluated on synthetic data degrade significantly on real users. Calls for human-centered evaluation standards for personalization research.

**Why trending:** Personalized LLMs are a key commercial direction; this paper surfaces a critical evaluation gap that synthetic benchmarks systematically hide.

---

## 18. When Does Trajectory-Level Supervision Permit Efficient Offline Reinforcement Learning?

**Authors:** Xuanfei Ren, Tengyang Xie
**Arxiv:** [arxiv.org/abs/2606.18531](https://arxiv.org/abs/2606.18531)
**Sources:** HuggingFace

Develops a statistical theory for offline RL from trajectory-level outcomes (win/lose, success/failure) rather than per-step reward supervision, which is the more realistic setting for most real-world sequential datasets.

**Why trending:** Offline RL from sparse outcome labels is the practical reality for many domains; this theoretical grounding matters for practitioners.

---

## 19. Reinforcement Learning-Guided Retrieval with Soft Fusion for Robust Multimodal Imitation Learning under Missing Modalities

**Authors:** Hassan Ismkhan, Hamid Bouchahcia
**Arxiv:** [arxiv.org/abs/2606.15514](https://arxiv.org/abs/2606.15514)
**Sources:** HuggingFace

Uses RL to guide retrieval of the most informative modality-complete reference experiences for imitation learning when sensors drop out. Soft fusion combines available modalities with retrieved context robustly.

**Why trending:** Sensor failure in real-world robot deployment is unavoidable; this provides a practical RL-based solution for multimodal robustness.

---

## 20. Artemis: Anatomy-Resolved inTervention for Eliminating Multimodal NeuroImage confounderS

**Authors:** Siyuan Dai, Yang Du, Kun Zhao, Zhusuyi Chen, Heng Huang, Paul Thompson, Chao Shi, Haoteng Tang, Liang Zhan
**Arxiv:** [arxiv.org/abs/2606.18287](https://arxiv.org/abs/2606.18287)
**Sources:** CV Brief (June 19, 2026), HuggingFace

Proposes a region-level causal framework for brain network GNNs that independently adjusts for demographic confounders (age, sex) at each brain region, using multimodal fMRI/DTI features. Achieves consistent improvements on ADNI, OASIS, and HCP benchmarks.

**Why trending:** Brain connectivity analysis with GNNs is an active area; causal confounder removal is critical for clinical translation and is broadly applicable to neuroscience ML.
