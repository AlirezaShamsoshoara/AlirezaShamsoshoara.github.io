---
title: "Daily AI Papers — April 30, 2026"
date: 2026-04-30
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-30/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multi-agent-systems
  - multimodal-models
  - video-generation
---

## 1. From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company
**Authors:** Zhengxu Yu, Yu Fu, Zhiyuan He, Yuxuan Huang
**arXiv:** [arxiv.org/abs/2604.22446](https://arxiv.org/abs/2604.22446)
**Sources:** HuggingFace (112 upvotes), Reddit r/MachineLearning, Papers With Code
**Why trending:** Proposes a corporate org-layer metaphor for agent orchestration — resonates with growing demand for production-grade multi-agent frameworks.

Individual agent capabilities have advanced rapidly, yet multi-agent systems remain constrained by fixed team structures and session-bound learning. This work argues for a principled organisational layer governing how a workforce of heterogeneous agents is assembled, governed, and improved over time, drawing from real-world company structures to enable persistent, adaptive agent collaboration.

---

## 2. World-R1: Reinforcing 3D Constraints for Text-to-Video Generation
**Authors:** Weijie Wang, Xiaoxuan He, Youping Gu, Yifan Yang
**arXiv:** [arxiv.org/abs/2604.24764](https://arxiv.org/abs/2604.24764)
**Sources:** HuggingFace (111 upvotes), Reddit r/MachineLearning, Reddit r/LocalLLaMA, Papers With Code
**Why trending:** Applies RL (DeepSeek-R1 style) to video generation to enforce 3D consistency — a compelling convergence of RL alignment and video synthesis.

Recent video foundation models suffer from geometric inconsistencies despite impressive visual quality. World-R1 aligns video generation with 3D constraints through reinforcement learning, enabling scalable geometric consistency without expensive architectural modifications or 3D annotation pipelines.

---

## 3. GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents
**Authors:** V Team, Wenyi Hong, Xiaotao Gu, Ziyang Pan
**arXiv:** [arxiv.org/abs/2604.26752](https://arxiv.org/abs/2604.26752)
**Sources:** HuggingFace (71 upvotes), Papers With Code, Reddit r/MachineLearning
**Why trending:** Top paper on HuggingFace today; native multimodal agent model with GUI/web/video perception — direct competitor to GPT-4o and Gemini in agentic settings.

GLM-5V-Turbo presents a step toward native foundation models for multimodal agents where perception is integrated as a core component of reasoning, planning, tool use, and execution. The model is designed to perceive, interpret, and act over heterogeneous contexts including images, videos, webpages, documents, and GUIs without relying on separate encoder-decoder pipelines.

---

## 4. Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation
**Authors:** Zhiheng Liu, Weiming Ren, Xiaoke Huang, Shoufa Chen
**arXiv:** [arxiv.org/abs/2604.24763](https://arxiv.org/abs/2604.24763)
**Sources:** HuggingFace (61 upvotes), Papers With Code, Reddit r/MachineLearning
**Why trending:** Bold architectural claim — pixel embeddings outperforming dedicated vision encoders; challenges the dominant CLIP-ViT paradigm in multimodal LLMs.

Unified multimodal models typically rely on pretrained vision encoders, creating misalignment between understanding and generation tasks. Tuna-2 performs visual understanding and generation directly from pixel embeddings, enabling fully end-to-end optimization from raw pixels and demonstrating competitive or superior performance versus encoder-based approaches.

---

## 5. ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning
**Authors:** Yiming Zhang, Jiacheng Chen, Jiaqi Tan, Yongsen Mao
**arXiv:** [arxiv.org/abs/2604.24300](https://arxiv.org/abs/2604.24300)
**Sources:** HuggingFace (60 upvotes), Papers With Code
**Why trending:** Exposes systematic flaws in existing spatial benchmarks for VLMs — benchmark papers that challenge the status quo consistently trend.

Current evaluations of spatial intelligence are systematically invalid under modern VLM settings because benchmarks derive QA pairs from point-cloud-based 3D annotations with reconstruction artifacts. ReVSI rebuilds evaluation with video-native, artifact-free annotations designed to accurately test genuine 3D reasoning capabilities of VLMs.

---

## 6. Large Language Models Explore by Latent Distilling
**Authors:** Yuanhao Zeng, Ao Lu, Lufei Li, Zheng Zhang
**arXiv:** [arxiv.org/abs/2604.24927](https://arxiv.org/abs/2604.24927)
**Sources:** HuggingFace (48 upvotes), Papers With Code
**Why trending:** Novel decoding approach targeting semantic diversity for test-time scaling — relevant to reasoning model optimization.

Standard stochastic sampling yields only surface-level lexical variation, limiting semantic exploration critical for test-time scaling. Exploratory Sampling (ESamp) distills diverse latent directions at decoding time, explicitly encouraging semantic diversity by leveraging the neural network's geometry to produce meaningfully different response paths from the same prompt.

---

## 7. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms
**Authors:** Qi Li, Bo Yin, Weiqi Huang, Ruhao Liu
**arXiv:** [arxiv.org/abs/2604.23775](https://arxiv.org/abs/2604.23775)
**Sources:** HuggingFace (43 upvotes), Papers With Code
**Why trending:** Timely safety survey for embodied AI as VLA models move toward real-world robotics deployment.

Vision-Language-Action (VLA) models are emerging as a unified substrate for embodied intelligence, raising a new class of safety challenges from irreversible physical consequences, a multimodal attack surface, and real-time latency constraints. This comprehensive survey covers threats, evaluation protocols, and defense mechanisms specific to VLA systems in the wild.

---

## 8. Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models
**Authors:** Gongbo Zhang, Wen Wang, Ye Tian, Li Yuan
**arXiv:** [arxiv.org/abs/2604.26951](https://arxiv.org/abs/2604.26951)
**Sources:** HuggingFace (35 upvotes), Papers With Code
**Why trending:** First cross-architecture distillation framework for diffusion LLMs — bridges the scalability gap as dLLMs gain traction.

Diffusion LLMs offer parallel decoding and bidirectional context but require billions of parameters for competitive performance, and existing distillation methods only work within a single architecture. TIDE is the first framework for cross-architecture dLLM distillation, enabling knowledge transfer between teacher and student models with different architectures, attention mechanisms, and tokenizers.

---

## 9. ClawGym: A Scalable Framework for Building Effective Claw Agents
**Authors:** Fei Bai, Huatong Song, Shuang Sun, Daixuan Cheng
**arXiv:** [arxiv.org/abs/2604.26904](https://arxiv.org/abs/2604.26904)
**Sources:** HuggingFace (35 upvotes), Papers With Code
**Why trending:** Directly targets file-system/tool-use agents (the "Claw" paradigm), filling infrastructure gaps for training personal agents at scale.

Claw-style environments support multi-step workflows over local files, tools, and persistent workspace states, but scalable development is constrained by lack of a systematic framework for synthesizing verifiable training data. ClawGym provides the full lifecycle infrastructure for personal Claw-style agent development including data synthesis, agent training, and diagnostic evaluation.

---

## 10. RADIO-ViPE: Online Tightly Coupled Multi-Modal Fusion for Open-Vocabulary Semantic SLAM
**Authors:** Zaid Nasser, Mikhail Iumanov, Tianhao Li, Maxim Popov
**arXiv:** [arxiv.org/abs/2604.26067](https://arxiv.org/abs/2604.26067)
**Sources:** HuggingFace (32 upvotes), Papers With Code
**Why trending:** Monocular RGB-only open-vocabulary SLAM in dynamic environments — impressive setup eliminating depth sensor requirements.

RADIO-ViPE is an online semantic SLAM system enabling geometry-aware open-vocabulary grounding in dynamic environments, associating arbitrary natural language queries with localized 3D regions and objects. The system operates on raw monocular RGB video without requiring calibrated depth sensors, posed input, or pose initialization, tightly coupling multi-modal fusion at inference time.

---

## 11. ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents
**Authors:** Fanqing Meng, Lingxiao Du, Zijian Wu, Guanzheng Chen
**arXiv:** [arxiv.org/abs/2604.23781](https://arxiv.org/abs/2604.23781)
**Sources:** HuggingFace (30 upvotes), Papers With Code
**Why trending:** Addresses persistent agents working across multiple days — a uniquely realistic benchmark setup not covered by existing evals.

Existing benchmarks for language-model agents fail to capture persistent coworker scenarios where the environment changes independently over multiple working days. ClawMark evaluates agents handling arriving emails, shifting calendars, and evidence across images, PDFs, audio, video, and spreadsheets — modeling the multimodal, multi-day nature of real collaborative work.

---

## 12. SketchVLM: Vision Language Models Can Annotate Images to Explain Thoughts and Guide Users
**Authors:** Brandon Collins, Logan Bolton, Hung Huy Nguyen, Mohammad Reza Taesiri
**arXiv:** [arxiv.org/abs/2604.22875](https://arxiv.org/abs/2604.22875)
**Sources:** HuggingFace (29 upvotes), Reddit r/MachineLearning, Papers With Code
**Why trending:** Enables VLMs to draw SVG overlays on images during reasoning — intuitive and visually compelling capability.

When answering questions about images, humans naturally point and draw to explain reasoning, but modern VLMs like Gemini and GPT only respond with text. SketchVLM is a training-free, model-agnostic framework enabling VLMs to produce non-destructive, editable SVG overlays on input images, making spatial reasoning transparent and verifiable.

---

## 13. Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis
**Authors:** Zhisong Qiu, Shuofei Qiao, Kewei Xu, Yuqi Zhu
**arXiv:** [arxiv.org/abs/2604.24198](https://arxiv.org/abs/2604.24198)
**Sources:** HuggingFace (18 upvotes), Papers With Code
**Why trending:** Extends Process Reward Models from math reasoning to dynamic data analysis — bridges a key gap in agentic LLM applications.

Process Reward Models (PRMs) have succeeded in augmenting LLM reasoning on static tasks like math but struggle in dynamic data analysis settings. This paper presents an empirical study revealing why generic PRMs fail on data analysis agents and introduces specialized process-level reward modeling that supervises the scientific workflow rather than just final outcomes.

---

## 14. Why Fine-Tuning Encourages Hallucinations and How to Fix It
**Authors:** Guy Kaplan, Zorik Gekhman, Zhen Zhu, Lotem Rozner
**arXiv:** [arxiv.org/abs/2604.15574](https://arxiv.org/abs/2604.15574)
**Sources:** HuggingFace (18 upvotes), Papers With Code
**Why trending:** Explains a fundamental mechanism behind SFT-induced hallucinations and proposes continual learning fixes — highly practical for anyone fine-tuning LLMs.

Large language models are prone to hallucinating factually incorrect statements, and supervised fine-tuning (SFT) on new factual information can increase hallucinations relative to pre-training knowledge. This work frames SFT-induced hallucinations as a continual learning problem and shows that established tools from that literature can mitigate the effect, offering practical guidance for fine-tuning practitioners.

---

## 15. Diffusion Templates: A Unified Plugin Framework for Controllable Diffusion
**Authors:** Zhongjie Duan, Hong Zhang, Yingda Chen
**arXiv:** [arxiv.org/abs/2604.24351](https://arxiv.org/abs/2604.24351)
**Sources:** HuggingFace (6 upvotes), Papers With Code
**Why trending:** Addresses fragmentation across controllable diffusion methods with a backbone-agnostic plugin system — high practical value for the image generation community.

Controllable diffusion methods are typically developed as isolated, backbone-specific systems with incompatible training pipelines and parameter formats. Diffusion Templates introduces a unified plugin framework enabling reuse and composition of control modules across different diffusion backbones without retraining, substantially reducing the cost of developing new controllable generation capabilities.

---

## 16. Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding
**Authors:** Hayate Iso, Tiyasa Mitra, Sudipta Mondal, Rasoul Shafipour
**arXiv:** [arxiv.org/abs/2604.26779](https://arxiv.org/abs/2604.26779)
**Sources:** HuggingFace (3 upvotes), Papers With Code
**Why trending:** Targets the core bottleneck in RL post-training — rollout generation speed — using speculative decoding as a lossless primitive.

RL post-training of frontier language models is increasingly bottlenecked by autoregressive rollout generation. This paper studies speculative decoding as a lossless acceleration primitive for RL rollouts that preserves the on-policy distribution exactly, enabling significant throughput improvements without changing the training regime.

---

## 17. Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (X-WAM)
**Authors:** Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen
**arXiv:** [arxiv.org/abs/2604.26694](https://arxiv.org/abs/2604.26694)
**Sources:** HuggingFace (2 upvotes), Papers With Code
**Why trending:** Unifies real-time robotic action execution and 4D world synthesis (video + 3D reconstruction) in a single framework — ambitious and timely for embodied AI.

X-WAM proposes a unified 4D world model that combines real-time robotic action execution with high-fidelity 4D world synthesis within a single framework, addressing the limitations of prior models that only operate in 2D pixel-space. By leveraging strong visual priors from pretrained video diffusion models, X-WAM achieves both action efficiency and world modeling quality simultaneously.

---

## 18. A Survey on LLM-based Conversational User Simulation
**Authors:** Bo Ni, Leyao Wang, Yu Wang, Branislav Kveton
**arXiv:** [arxiv.org/abs/2604.24977](https://arxiv.org/abs/2604.24977)
**Sources:** HuggingFace (2 upvotes), Papers With Code
**Why trending:** Comprehensive survey at the intersection of LLMs and conversational simulation — foundational reference for dialogue system researchers.

User simulation has long played a vital role in computer science, supporting applications from dialogue system training to evaluation. This survey covers LLM-based approaches to conversational user simulation, cataloging methods, datasets, and evaluation protocols, and identifying open challenges in modeling realistic user behavior at scale.

---

## 19. FASH-iCNN: Making Editorial Fashion Identity Inspectable Through Multimodal CNN Probing
**Authors:** Morayo Danielle Adeyemi, Ryan A. Rossi, Franck Dernoncourt
**arXiv:** [arxiv.org/abs/2604.26186](https://arxiv.org/abs/2604.26186)
**Sources:** HuggingFace (1 upvote), Papers With Code
**Why trending:** Unusual intersection of fashion AI, interpretability, and cultural analytics — trained on 87K Vogue images across 15 fashion houses spanning three decades.

Fashion AI systems routinely encode the aesthetic logic of specific houses, editors, and historical moments without disclosing it. FASH-iCNN is a multimodal system trained on 87,547 Vogue runway images across 15 fashion houses (1991–2024) that makes this cultural logic inspectable through CNN probing, revealing what visual features signal editorial identity.

---

## 20. PSP: An Interpretable Per-Dimension Accent Benchmark for Indic Text-to-Speech
**Authors:** Venkata Pushpak Teja Menta
**arXiv:** [arxiv.org/abs/2604.25476](https://arxiv.org/abs/2604.25476)
**Sources:** HuggingFace (1 upvote), Papers With Code
**Why trending:** Addresses a gap in TTS evaluation for Indic languages — accent quality benchmarking that standard WER/MOS metrics miss entirely.

Standard TTS evaluation measures intelligibility (WER, CER) and naturalness (MOS) but does not quantify accent — a system can score well on all metrics yet sound non-native on phonemic features of the target language. PSP introduces a per-dimension accent benchmark for Indic TTS that decomposes accent fidelity into interpretable axes, enabling targeted improvement for underrepresented language communities.
