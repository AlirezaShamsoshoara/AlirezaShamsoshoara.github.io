---
title: "Daily AI Papers — May 31, 2026"
date: 2026-05-31
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-31/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-safety
  - video-generation
  - retrieval-augmented-generation
---

## 1. AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security

**Authors:** Dongrui Liu, Yu Li, Zhonghao Yang, Peng Wang, Guanxu Chen et al.  
**arXiv:** [arxiv.org/abs/2605.29801](https://arxiv.org/abs/2605.29801)  
**Upvotes:** 127 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** Modern open-world agents like OpenClaw bring powerful cross-environment capabilities alongside broad new safety risks; this paper proposes a lightweight, taxonomy-guided safety alignment framework training 0.8B–8B parameter AgentDoG 1.5 variants on ~1k samples to match frontier closed-source models (e.g., GPT-5.4). The framework updates the agent safety taxonomy for Codex/OpenClaw execution scenarios, deploys as a training-free online guardrail, and reduces Docker-level environment overhead by two orders of magnitude.

**Why trending:** Top paper of the day by a wide margin; agent safety is a hot topic as agentic AI is deployed at scale, and the open-release of models + datasets draws broad community interest.

---

## 2. OmniRetrieval: Unified Retrieval across Heterogeneous Knowledge Sources

**Authors:** Jinheon Baek, Soyeong Jeong, Sangwoo Park, Woongyeong Yeo, Minki Kang et al.  
**arXiv:** [arxiv.org/abs/2605.29250](https://arxiv.org/abs/2605.29250)  
**Upvotes:** 65 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** OmniRetrieval is a unified retrieval framework that takes natural-language queries, identifies appropriate knowledge sources (unstructured text, relational tables, knowledge graphs, property graphs), and dispatches source-native queries to their native execution engines — without collapsing structural distinctions. Benchmarked across 13 datasets and 309 distinct knowledge bases, it exceeds single-source baselines while preserving each source's structural affordances.

**Why trending:** RAG and retrieval quality are central to production LLM systems; a single interface spanning heterogeneous sources addresses a persistent engineering pain point.

---

## 3. CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation

**Authors:** Fangtai Wu, Hailong Guo, Shijie Huang, Jiayi Song, Yubo Huang et al.  
**arXiv:** [arxiv.org/abs/2605.25378](https://arxiv.org/abs/2605.25378)  
**Upvotes:** 53 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** CollectionLoRA proposes a multi-teacher on-policy distillation framework that compresses up to 50 effect LoRAs plus few-step generation into a single LoRA, eliminating the parameter interference (concept bleeding, style degradation) caused by cascading multiple LoRAs with acceleration modules. Key techniques include a Probabilistic Dual-Stream Routing mechanism, an Asymmetric Orthogonal Prompting strategy for concept isolation, and a Coarse-to-Fine Distillation Objective.

**Why trending:** Practical and immediately applicable to image generation pipelines; collapsing 50 LoRAs into one with no quality loss is highly deployable and community-relevant.

---

## 4. minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models

**Authors:** Min Zhao, Hongzhou Zhu, Bokai Yan, Zihan Zhou, Yimin Chen et al.  
**arXiv:** [arxiv.org/abs/2605.30263](https://arxiv.org/abs/2605.30263)  
**Upvotes:** 49 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** minWM provides an end-to-end open-source pipeline for converting bidirectional T2V/TI2V video foundation models into camera-controllable few-step autoregressive world models suitable for real-time rollout. It covers data construction, controllable fine-tuning, AR training (Causal Forcing / Causal Forcing++), causal ODE/consistency distillation, and asymmetric DMD — instantiated on Wan2.1-T2V-1.3B and HY1.5-TI2V-8B.

**Why trending:** Interactive video world models are a frontier research direction; a full-stack open-source framework lowers the barrier to reproduction and sparks community experiments.

---

## 5. YoCausal: How Far is Video Generation from World Model? A Causality Perspective

**Authors:** You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang  
**arXiv:** [arxiv.org/abs/2605.30346](https://arxiv.org/abs/2605.30346)  
**Upvotes:** 41 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** YoCausal is a two-level benchmark inspired by the Violation of Expectation (VoE) paradigm from cognitive science that evaluates whether video diffusion models truly understand causality or merely overfit to statistical temporal patterns. By using temporally reversed real-world videos as zero-cost counterfactuals, it introduces the Reverse Surprise Index (RSI) and Causality Cognition Index (CCI), revealing that 13 state-of-the-art VDMs perceive the arrow of time without genuinely understanding causality.

**Why trending:** The "video gen = world model" claim is actively debated; this paper provides a rigorous empirical answer using an elegant, extensible protocol.

---

## 6. GenClaw: Code-Driven Agentic Image Generation

**Authors:** Junyan Ye, Jun He, Zilong Huang, Dongzhi Jiang, Xuan Yang et al.  
**arXiv:** [arxiv.org/abs/2605.30248](https://arxiv.org/abs/2605.30248)  
**Upvotes:** 31 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** GenClaw introduces a code-driven agentic image generation paradigm where an agent first conceptualizes (via search + reasoning), then renders executable visual sketches in code (SVG, HTML, Three.js), and finally applies a generative model for textures and photorealism — breaking the black-box prompt-rewrite loop. Code acts as a controllable intermediate canvas bridging linguistic reasoning and pixel synthesis.

**Why trending:** The idea of using code as a "canvas" for structured image generation is novel and aligns with the trend of agentic AI workflows; strong community interest in controllable generation.

---

## 7. EarlyTom: Early Token Compression Completes Fast Video Understanding

**Authors:** Hesong Wang, Xin Jin, Lu Lu, Chenhaowen Li, Jian Chen et al.  
**arXiv:** [arxiv.org/abs/2605.30010](https://arxiv.org/abs/2605.30010)  
**Upvotes:** 27 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** EarlyTom is a training-free token compression framework that performs compression inside the vision encoder (early-stage) rather than only after it, targeting the large fraction of time-to-first-token (TTFT) consumed by vision encoding. A decoupled spatial token selection strategy improves overall compression, achieving up to 2.65× TTFT reduction and 61% FLOPs reduction on LLaVA-OneVision-7B with no accuracy drop.

**Why trending:** TTFT is a critical production metric for video LLMs; a training-free drop-in improvement with 2.65× speedup is immediately actionable for practitioners.

---

## 8. UniSteer: Text-Guided Flow Matching in Activation Space for Versatile LLM Steering

**Authors:** Yingdong Shi, Ruiming Zhang, Changming Li, Zhiyu Yang, Kaixing Zhang et al.  
**arXiv:** [arxiv.org/abs/2605.30076](https://arxiv.org/abs/2605.30076)  
**Upvotes:** 21 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** UniSteer learns a universal conditional velocity field over LLM residual-stream activations using flow matching, conditioned on natural-language descriptions rather than fixed steering directions or task-specific modules. At inference time it partially transports source activations toward a latent state and regenerates under a target text condition, supporting behavioral control, truthfulness steering, fine-grained concept steering, multi-constraint instruction following, and activation-space classification via a single model.

**Why trending:** Activation steering for LLMs is a growing research area; a unified text-conditioned approach that handles multiple control tasks in one model is a significant advance.

---

## 9. Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic RL

**Authors:** Jiapeng Zhu, Jianxiang Yu, Yibo Zhao, Chengcheng Han, Qi Gu et al.  
**arXiv:** [arxiv.org/abs/2605.28424](https://arxiv.org/abs/2605.28424)  
**Upvotes:** 21 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** Skill0.5 proposes a novel agentic RL framework that avoids the binary choice between full skill externalization (high context overhead) and full internalization (overfitting risk) by combining general skill internalization via privileged distillation with task-specific skill utilization driven by a difficulty-aware dynamic router. Experiments on ALFWorld and WebShop show improvements over both memory-based and skill-based RL baselines in-distribution and out-of-distribution.

**Why trending:** Agentic RL generalization is a key open problem; the hybrid internalization/utilization approach is novel and results show consistent OOD gains.

---

## 10. LoMo: Local Modality Substitution for Deeper Vision-Language Fusion

**Authors:** Feng Han, Zhixiong Zhang, Zheming Liang, Yibin Wang, Jiaqi Wang et al.  
**arXiv:** [arxiv.org/abs/2605.30265](https://arxiv.org/abs/2605.30265)  
**Upvotes:** 20 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** LoMo is a lightweight, architecture-agnostic data curation paradigm that addresses "carrier sensitivity" in VLMs — the dramatic performance drop when a text question is replaced by its rendered-image equivalent — by reformulating single-modality prompts into interleaved multimodal sequences where text spans are dynamically recasted as rendered images. Evaluated on 13 multimodal benchmarks, it improves LLaVA-OneVision-1.5-8B by 2.67 points and Qwen3.5-9B by 2.82 points over standard SFT.

**Why trending:** Identifies a fundamental training-data bias in VLMs with a practical, model-agnostic fix; directly actionable for practitioners building multimodal systems.

---

## 11. Colored Noise Diffusion Sampling

**Authors:** Hadar Davidson, Noam Issachar, Sagie Benaim  
**arXiv:** [arxiv.org/abs/2605.30332](https://arxiv.org/abs/2605.30332)  
**Upvotes:** 18 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** This paper establishes a mathematical framework recasting SDE inference in diffusion models as frequency-decoupled energy transfer, exploiting the model's spectral bias (low-frequency structures resolve early, fine details late) to define Colored Noise Sampling (CNS) — a training-free stochastic solver that allocates injected noise energy toward structurally unresolved frequency bands. CNS achieves substantial FID improvements: 8.26→6.27 on SiT-XL/2 and 32.39→26.69 on JiT-B/16 on ImageNet-256.

**Why trending:** Training-free inference improvements with significant FID gains across multiple architectures (SiT, JiT, FLUX) are highly practical; plug-and-play nature drives adoption.

---

## 12. Xetrieval: Mechanistically Explaining Dense Retrieval

**Authors:** Zhixin Cai, Jun Bai, Yang Liu, Jiaqi Li, Yichi Zhang et al.  
**arXiv:** [arxiv.org/abs/2605.29507](https://arxiv.org/abs/2605.29507)  
**Upvotes:** 17 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** Xetrieval introduces an embedding-level mechanistic explainability framework for dense retrievers, combining a lightweight reasoning internalizer that approximates Chain-of-Thought reasoning in embedding space (single forward pass) with sparse, human-interpretable feature decomposition. Feature-level explanations of individual retrieval decisions uncover coherent interpretable features and support task-level feature steering.

**Why trending:** Explainability in retrieval is under-studied; mechanistic interpretability applied to embeddings is a novel angle with both research and compliance implications.

---

## 13. Is Position Bias in Dense Retrievers Built In — or Learned from Data?

**Authors:** Daegon Yu, SeungYoon Han, Woomyoung Park  
**arXiv:** [arxiv.org/abs/2605.26578](https://arxiv.org/abs/2605.26578)  
**Upvotes:** 13 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** This paper studies how training-data positional distribution — not just architecture — drives retrieval-level position bias in dense retrievers, constructing synthetic position-targeted training sets with evidence at beginning/middle/end positions across eight architecturally diverse pretrained models. Position-balanced training reduces positional sensitivity by 57–87% on position-aware benchmarks, identifying training data curation as the primary controllable lever.

**Why trending:** Position bias has practical impact on RAG quality; the training-data-as-lever insight is actionable without model architecture changes.

---

## 14. CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists

**Authors:** Junlin Yang, Dylan Zhang, Xiangchen Song, Qirun Dai, Xiao Liu et al.  
**arXiv:** [arxiv.org/abs/2605.26029](https://arxiv.org/abs/2605.26029)  
**Upvotes:** 13 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** CausaLab is a scalable synthetic laboratory environment for evaluating interactive causal discovery by LLM agents, where each episode requires an agent to recover both a causal graph and structural equations — not just predict outcomes — from a randomly sampled structural causal model (SCM). GPT-5.2-high reaches 92% task accuracy in the 6-node observational setting but only 0.471 all-edge F₁, revealing a persistent gap between predictive success and causal understanding.

**Why trending:** AI scientist and causal reasoning benchmarks are actively sought; the separation of "prediction accuracy" from "causal mechanism recovery" is a fundamental scientific contribution.

---

## 15. Towards Verifiable Multimodal Deep Research: A Multi-Agent Harness for Interleaved Report Generation

**Authors:** Chenghao Zhang, Guanting Dong, Yufan Liu, Tong Zhao, Zhicheng Dou et al.  
**arXiv:** [arxiv.org/abs/2605.29861](https://arxiv.org/abs/2605.29861)  
**Upvotes:** 10 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** Ptah is a multi-agent harness for verifiable multimodal deep research that orchestrates planning, evidence retrieval, and writing stages — maintaining source-aligned images in a Visual Working Memory and using a verifier agent to enforce factual grounding, citation fidelity, and cross-modal consistency. The companion PtahEval protocol extends existing benchmarks with image-level and presentation-level assessments.

**Why trending:** Deep research agents and multimodal report generation are fast-moving areas; verifiability (grounding + citations) addresses the reliability gap that limits practical deployment.

---

## 16. UI-KOBE: Knowledge-Oriented Behavior Exploration for Lightweight Graph-Guided GUI Agents

**Authors:** Yuxiang Chai, Han Xiao, Xinyu Fu, Jinpeng Chen, Rui Liu et al.  
**arXiv:** [arxiv.org/abs/2605.29534](https://arxiv.org/abs/2605.29534)  
**Upvotes:** 10 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** UI-KOBE improves lightweight mobile GUI agents by autonomously constructing an app-specific knowledge graph (nodes = UI states, edges = executable transitions) during exploration, then using it at runtime as external guidance so a small model can plan and execute GUI tasks without relying on large VLMs. The approach reduces the burden of end-to-end GUI planning, targeting privacy-conscious on-device deployment.

**Why trending:** On-device agents with small models are increasingly important for privacy and cost; the graph-guided approach is practical and directly competitive with large-model alternatives.

---

## 17. WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction

**Authors:** Chengzhi Liu, Yuzhe Yang, Sophia Xiao Pu, Yepeng Liu, Lin Long et al.  
**arXiv:** [arxiv.org/abs/2605.29341](https://arxiv.org/abs/2605.29341)  
**Upvotes:** 7 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** WorldMemArena formalizes multimodal agent memory as a four-stage Action-World Interaction Loop and provides 400 multi-session tasks spanning Lifelong Evolution and Agentic Execution scenarios, enabling stage-level diagnosis across long-context, manually designed, and harness-based memory agents. Key findings: better memory writing does not guarantee better performance, visual evidence is underutilized, and harness memory is flexible but costly.

**Why trending:** Long-horizon multimodal agents require robust memory; a principled benchmark that separates writing, maintenance, retrieval, and use fills a clear gap.

---

## 18. Verifiable Rewards Beyond Math and Code: Lightweight Corpus-Grounded Process Supervision for Factual QA

**Authors:** Shicheng Fan, Haochang Hao, Dehai Min, Weihao Liu, Philip S. Yu  
**arXiv:** [arxiv.org/abs/2605.29648](https://arxiv.org/abs/2605.29648)  
**Upvotes:** 6 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** CorVer (Corpus Verify) replaces expensive neural NLI verifiers and LLM judges with a corpus-grounded process reward derived from Wikipedia co-occurrence statistics, providing sentence-level credit mapped to token-level advantages via a 0.5B extractor and single corpus lookup per sentence. Across 30 (model, benchmark) cells, CorVer improves over baselines in every cell with an average +4.1 pp TriviaQA gain and 4.8–8.4× faster training.

**Why trending:** Process reward design for factual RL is an open problem; a lightweight, cheap, reliable alternative to neural verifiers with consistent gains across 6 model sizes is highly practical.

---

## 19. NeuROK: Generative 4D Neural Object Kinematics

**Authors:** Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu  
**arXiv:** [arxiv.org/abs/2605.30347](https://arxiv.org/abs/2605.30347)  
**Upvotes:** 6 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** NeuROK learns a data-driven kinematic state parameterization for object-centric physical systems using a transformer-based encoder-decoder trained on a large-scale 4D dataset, jointly learning a latent space of all possible object states and a decoder mapping latents to plausibly deformed shapes. By representing dynamics in a low-dimensional Lagrangian latent space, it enables generative simulation of realistic temporal deformations across diverse dynamic object types without predefined physical models.

**Why trending:** 4D generation and physical simulation of objects are key capabilities for building 3D world models; a generalizable, data-driven approach that avoids category-specific physical assumptions is timely.

---

## 20. AdaState: Self-Evolving Anchors for Streaming Video Generation

**Authors:** Yusuf Dalva, Pinar Yanardag  
**arXiv:** [arxiv.org/abs/2605.30349](https://arxiv.org/abs/2605.30349)  
**Upvotes:** 6 | **Sources:** HuggingFace Daily Papers, arXiv

**Summary:** AdaState replaces the static first-frame anchor in autoregressive video diffusion models with an adaptive hidden latent ("state") that the model denoises alongside content at every chunk, evolving with generated content rather than locking to the initial viewpoint. Treating time as relative (identical positional structure at every step) introduces a natural recurrence — denoising as transition function, KV cache as carrier — requiring no external module and substantially improving video dynamics.

**Why trending:** Streaming video generation quality (motion, scene progression) is a concrete deployment concern; the elegant recurrent anchor design is novel and requires no architectural changes.
