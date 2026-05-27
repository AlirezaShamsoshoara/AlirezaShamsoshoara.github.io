---
title: "Daily AI Papers — May 27, 2026"
date: 2026-05-27
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-27/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - mixture-of-experts
  - multimodal
  - agentic-ai
---

## 1. The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence

**Authors:** MiniMax Team (Aili Chen, Aonian Li, Baichuan Zhou, Bangwei Gong, et al.)
**arXiv:** [arxiv.org/abs/2605.26494](https://arxiv.org/abs/2605.26494)

**Summary:** MiniMax-M2 is a Mixture-of-Experts language model with 229.9B total parameters and only 9.8B activated per token, designed end-to-end for agentic deployment. It introduces agent-driven data pipelines with verifiable trajectories, a scalable agent-native RL system called Forge, and a hybrid architecture combining Lightning Attention and Softmax Attention for unlimited context and high throughput.

**Why trending:** Major open MoE model release from MiniMax; the "mini activations, max intelligence" efficiency angle at 229.9B scale with agentic-first design is drawing broad community attention. Widely discussed across Reddit r/LocalLLaMA, Hacker News, and ML Twitter/X.

**Sources:** HuggingFace Daily Papers, arXiv, Reddit r/LocalLLaMA, Hacker News

---

## 2. Gemini Embedding 2: A Native Multimodal Embedding Model from Gemini

**Authors:** Madhuri Shanbhogue, Zhe Li, Shanfeng Zhang, Gustavo Hernández Ábrego, Shih-Cheng Huang, et al. (Google DeepMind)
**arXiv:** [arxiv.org/abs/2605.27295](https://arxiv.org/abs/2605.27295)

**Summary:** Gemini Embedding 2 is a native multimodal embedding model that unifies video, audio, image, and text into a single representation space using interleaved multimodal inputs. Through large-scale contrastive learning in a multi-task multi-stage training setup, it achieves state-of-the-art performance on unimodal, cross-modal, and multimodal retrieval benchmarks.

**Why trending:** Google's first truly native multimodal embedding (not adapter-based) supporting video+audio+image+text in one model. Accompanied by official Google Blog post and Google AI for Developers documentation launch — significant industry product release.

**Sources:** HuggingFace Daily Papers, arXiv, Google Blog, Google AI Developer Docs, Papers With Code

---

## 3. LLaVA-OneVision-2: Towards Next-Generation Perceptual Intelligence

**Authors:** Xiang An, Yin Xie, Feilong Tang, Yunyao Yan, Huajie Tan, et al.
**arXiv:** [arxiv.org/abs/2605.25979](https://arxiv.org/abs/2605.25979)

**Summary:** LLaVA-OV-2 advances the LLaVA-OneVision series with a native OneVision-Encoder, Windowed Attention for efficient high-resolution processing, and codec-stream tokenization — treating compressed video as a continuous bit-cost stream to adaptively select salient spatial-temporal evidence. It achieves superior performance across a broad range of multimodal benchmarks.

**Why trending:** Follow-up to the widely-adopted LLaVA-OneVision model; the codec-stream video tokenization is a novel architectural idea attracting strong research interest on HuggingFace and Reddit r/MachineLearning.

**Sources:** HuggingFace Daily Papers, arXiv, Reddit r/MachineLearning

---

## 4. LocateAnything: Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding

**Authors:** Shihao Wang, Shilong Liu, Yuanguo Kuang, Xinyu Wei, Yangzhou Liu, Zhiqi Li, Yunze Man, Guo Chen, Andrew Tao, Guilin Liu, Jan Kautz, Lei Zhang, Zhiding Yu (NVIDIA)
**arXiv:** [arxiv.org/abs/2605.27365](https://arxiv.org/abs/2605.27365)

**Summary:** LocateAnything introduces Parallel Box Decoding (PBD), decoding bounding boxes and points as atomic geometric units in a single step rather than the standard token-by-token sequential approach used in VLMs. This resolves the inference bottleneck of autoregressive coordinate generation while preserving high grounding quality across detection and visual grounding tasks.

**Why trending:** NVIDIA research paper solving a core VLM inference bottleneck; parallel decoding of bounding boxes is architecturally clean and practically impactful for real-time vision systems.

**Sources:** HuggingFace Daily Papers, arXiv, Papers With Code

---

## 5. Share More, Search Less: Collaborative Parallel Thinking for Efficient Test-Time Scaling

**Authors:** Xinglin Wang, Hao Lin, Shaoxiong Feng, Peiwen Yuan, Yiwei Li, et al.
**arXiv:** [arxiv.org/abs/2605.27030](https://arxiv.org/abs/2605.27030)

**Summary:** Current parallel test-time scaling methods keep search branches isolated, causing redundant re-discovery of the same intermediate reasoning steps. This paper proposes collaborative parallel thinking, where branches share intermediate discoveries in real time, enabling other branches to leverage existing findings rather than starting from scratch — significantly improving efficiency and accuracy.

**Why trending:** Test-time scaling is a hot topic post-o1/DeepSeek-R1, and solving the information isolation problem in parallel inference is a practical and impactful contribution actively discussed in reasoning/inference optimization communities.

**Sources:** HuggingFace Daily Papers, arXiv, Reddit r/MachineLearning

---

## 6. MobileMoE: Scaling On-Device Mixture of Experts

**Authors:** Yanbei Chen, Hanxian Huang, Ernie Chang, Jacob Szwejbka, Digant Desai, et al.
**arXiv:** [arxiv.org/abs/2605.27358](https://arxiv.org/abs/2605.27358)

**Summary:** MobileMoE presents the first systematic study of MoE architecture for on-device deployment at sub-billion active parameter scales (0.3–0.9B active, 1.3–5.3B total), deriving a mobile-specific MoE scaling law that jointly optimizes sparsity and architecture under mobile memory and compute constraints. It establishes a new Pareto frontier for on-device LLMs across quality and efficiency.

**Why trending:** On-device AI is a rapidly growing area; applying MoE (previously only practical at 100B+ scale) to mobile hardware is a significant architectural advance, widely discussed across AI hardware and edge inference communities.

**Sources:** HuggingFace Daily Papers, arXiv, Reddit r/LocalLLaMA

---

## 7. MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research

**Authors:** Dingbang Wu, Rui Hao, Haiyang Wang, Shuzhe Wu, Han Xiao, et al.
**arXiv:** [arxiv.org/abs/2605.26114](https://arxiv.org/abs/2605.26114)

**Summary:** MobileGym is a browser-hosted, lightweight environment for mobile app interaction that enables verifiable outcome signals through deterministic JSON state-based judging, and scalable online RL through hundreds of parallel low-cost rollout instances (~400 MB memory each). The full environment state is captured, forked, and compared as structured JSON, making it ideal for training and evaluating mobile GUI agents with RL.

**Why trending:** GUI agent research is booming; verifiable RL environments for mobile apps have been a missing piece, and this fills a critical gap for the agentic AI community.

**Sources:** HuggingFace Daily Papers, arXiv, Papers With Code

---

## 8. MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

**Authors:** Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, Tieying Zhang, et al.
**arXiv:** [arxiv.org/abs/2605.27366](https://arxiv.org/abs/2605.27366)

**Summary:** MUSE-Autoskill proposes a skill-centric agent framework where agents continuously create, reuse, and refine skills under a unified lifecycle — creation, memory, management, evaluation, and refinement — rather than treating skills as static isolated artifacts. This enables long-term agent self-improvement without human intervention.

**Why trending:** Self-evolving agent capabilities are at the frontier of agentic AI research; the full skill lifecycle approach (create → store → manage → evaluate → refine) addresses a real limitation of current tool-use frameworks.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 9. D²-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing

**Authors:** Aoxi Liu, Yupeng Chen, James Oldfield, Guanzhe Hong, Junchi Yu, et al.
**arXiv:** [arxiv.org/abs/2605.25893](https://arxiv.org/abs/2605.25893)

**Summary:** D²-Monitor introduces the first safety monitoring framework specifically for Diffusion LLMs (D-LLMs), which generate text through multi-step denoising rather than autoregressive generation. It identifies "hesitation" signals in intermediate denoising trajectory representations to route potentially unsafe generations to a heavier safety classifier, enabling always-on lightweight monitoring.

**Why trending:** As diffusion-based language models (like MDLM, Plaid) gain traction as AR alternatives, safety monitoring for their unique generation process is an urgent open problem — this paper directly addresses it.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 10. VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions

**Authors:** Yuxin Chen, Yi Zhang, Zhengzhou Cai, Yaorui Shi, Zhiyuan Yao, et al.
**arXiv:** [arxiv.org/abs/2605.27141](https://arxiv.org/abs/2605.27141)

**Summary:** VitaBench 2.0 benchmarks LLM agents on their ability to infer user preferences from fragmented daily interactions and act proactively — going beyond standard reasoning and tool-use evaluations. It introduces realistic long-horizon scenarios where agents must build personalized user models and anticipate needs without explicit instructions.

**Why trending:** As AI assistants move toward persistent, personalized deployment, benchmarks measuring proactive behavior and long-term user modeling are increasingly important and under-represented.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 11. EvalVerse: Pipeline-Aware and Expert-Calibrated Benchmarking for Professional Cinematic Video Generation

**Authors:** Songlin Yang, Haobin Zhong, Ruilin Zhang, Xiaotong Zhao, Shuai Li, et al.
**arXiv:** [arxiv.org/abs/2605.23271](https://arxiv.org/abs/2605.23271)

**Summary:** EvalVerse tackles the evaluation gap in professional cinematic video generation, where existing benchmarks test only "whether it is right" (prompt following) but not "whether it is good" (cinematic quality, acting, aesthetics). It introduces pipeline-aware metrics calibrated against expert cinematographers to evaluate RL-trained and agentic video generation workflows.

**Why trending:** With video generation models rapidly maturing toward professional-grade output (Sora, Wan, Kling), expert-calibrated cinematic evaluation is a timely and practical contribution.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 12. GARD: Geometry-Aware Representation Denoising for Robust Multi-View 3D Reconstruction

**Authors:** Jin Hyeon Kim, Jaeeun Lee, Claire Kim, Kyoungjin Oh, Paul Hyunbin Cho, et al.
**arXiv:** [arxiv.org/abs/2605.26230](https://arxiv.org/abs/2605.26230)

**Summary:** GARD addresses the brittleness of feed-forward multi-view 3D reconstruction models when inputs are degraded (noise, blur, artifacts). It performs diffusion-based multi-view restoration directly in the geometry-aware representation space rather than pixel space, making the restoration process aware of 3D structure and cross-view consistency.

**Why trending:** Feed-forward 3D reconstruction (e.g., MVSplat, Splatt3R) is a hot research area; robust reconstruction under real-world degradations is a critical practical gap.

**Sources:** HuggingFace Daily Papers, arXiv, Papers With Code

---

## 13. SpatialBench: Is Your Spatial Foundation Model an All-Round Player?

**Authors:** Haosong Peng, Hao Li, Jiaqi Chen, Yuhao Pan, Runmao Yao, et al.
**arXiv:** [arxiv.org/abs/2605.27367](https://arxiv.org/abs/2605.27367)

**Summary:** SpatialBench provides a holistic evaluation of spatial foundation models across diverse downstream tasks, arbitrary viewpoints, shifting scene domains, varying input densities, and hardware constraints — dimensions that are typically evaluated in isolation. It reveals significant performance gaps in current models when facing out-of-distribution spatial conditions.

**Why trending:** Spatial AI (depth estimation, scene understanding, 3D) is a core enabler for robotics and AR/VR; comprehensive cross-domain evaluation benchmarks are needed to identify real model limitations.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 14. Negligible in Size, Significant in Effect: On Scale Vectors in Large Language Models

**Authors:** Mingze Wang, Shuchen Zhu, Yuxin Fang, Binghui Li, Kai Shen, et al.
**arXiv:** [arxiv.org/abs/2605.26895](https://arxiv.org/abs/2605.26895)

**Summary:** This paper presents the first systematic study of the learned scale vectors in LLM normalization layers — parameters that constitute a negligible fraction of total model size but whose removal substantially degrades pre-training performance. The study examines scale vectors from expressivity, optimization, and architectural structure perspectives, uncovering previously unknown properties.

**Why trending:** Interpretability of normalization components is a fundamental LLM research question; showing that tiny scale vectors have outsized impact challenges conventional thinking about parameter importance.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 15. AKBE: Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement

**Authors:** Dingwei Chen, Zefang Zong, Zhipeng Ma, Leo Luo, Yang Li, et al.
**arXiv:** [arxiv.org/abs/2605.26952](https://arxiv.org/abs/2605.26952)

**Summary:** AKBE identifies that agentic RL training causes LLM agents to blur their intrinsic knowledge boundaries — failing to distinguish when to call external tools versus when parametric knowledge suffices — leading to reward hacking via indiscriminate tool suppression. It proposes an on-policy intrinsic reward that explicitly reinforces fine-grained knowledge boundary awareness.

**Why trending:** Tool-use reliability in agentic RL is a critical unsolved problem; this paper provides a principled diagnosis and solution for a failure mode actively observed in deployed agent systems.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 16. Does Seeing More Mean Knowing More? Mono-Anchored Advantage Normalization for Multi-Source Visual Reasoning

**Authors:** Fanhu Zeng, Zhicong Luo, Zefan Wang, You Li, Chi Chen, et al.
**arXiv:** [arxiv.org/abs/2605.25437](https://arxiv.org/abs/2605.25437)

**Summary:** In multi-source visual reasoning with RLVR, naively combining multiple input modalities (e.g., RGB + infrared + depth) can introduce interference rather than information gain. This paper proposes Mono-Anchored Advantage Normalization to explicitly distinguish beneficial information integration from cross-modal interference in reinforcement learning from verifiable rewards.

**Why trending:** Multi-modal RLVR is a frontier research topic; understanding when more visual sources hurt rather than help is practically important for robotics and autonomous perception.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 17. LongAV-Compass: Towards Unified Evaluation of Minute-Scale Audio-Visual Generation

**Authors:** Tengfei Liu, Yang Shi, Xuanyu Zhu, Jiafu Tang, Liu Yang, et al.
**arXiv:** [arxiv.org/abs/2605.26244](https://arxiv.org/abs/2605.26244)

**Summary:** LongAV-Compass introduces a systematic benchmark for minute-long audio-visual generation across text-to-AV, image-to-AV, and video-to-AV conditioning, measuring identity consistency, narrative coherence, and audio-visual alignment over extended temporal horizons. It fills the evaluation gap left by existing short-form (5–10 second) AV benchmarks.

**Why trending:** As AV generation extends to minute-scale content for real-world media production, unified evaluation across conditioning types and temporal consistency is critically needed.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 18. Learning to Act under Noise: Enhancing Agent Robustness via Noisy Environments

**Authors:** Yuxin Chen, Xiaodong Cai, Junfeng Fang, Zhuowen Han, Yu Wang, et al.
**arXiv:** [arxiv.org/abs/2605.27209](https://arxiv.org/abs/2605.27209)

**Summary:** LLM agents trained on curated, stable environments degrade significantly when deployed in real-world stochastic settings. This paper proposes training agents in deliberately noisy environments — with imperfect instructions, unstable tool responses, and adversarial context — to build fundamental robustness to deployment conditions rather than relying on test-time patches.

**Why trending:** Agent deployment reliability is a top practical concern; systematically training for robustness via noise injection is a simple, generalizable approach with strong implications for production agent systems.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 19. QUACK: Questioning, Understanding, and Auditing Communicated Knowledge in Multimodal Social Deduction Agents

**Authors:** Ye Yuan, Rui Song, Weien Li, Zeyu Li, Haochen Liu, et al.
**arXiv:** [arxiv.org/abs/2605.27068](https://arxiv.org/abs/2605.27068)

**Summary:** QUACK is an open-source evaluation framework for multimodal social deduction games (e.g., Werewolf, Among Us variants) that audits whether LLM agent language is actually grounded in perceived actions and observations, rather than merely scored by win rates. It introduces structured grounding metrics to identify failure modes like deception-without-perception and action-language misalignment.

**Why trending:** Social deduction games are a popular LLM agent testbed; moving beyond win-rate scoring to grounding audits is a methodological advance that reveals important failure modes in current MLLM agents.

**Sources:** HuggingFace Daily Papers, arXiv

---

## 20. Soap2Soap: Long Cinematic Video Remaking via Multi-Agent Collaboration

**Authors:** Yiren Song, Huilin Zhong, Kevin Qinghong Lin, Haofan Wang, Mike Zheng Shou, et al.
**arXiv:** [arxiv.org/abs/2605.17423](https://arxiv.org/abs/2605.17423)

**Summary:** Soap2Soap tackles series-level cinematic remaking — stylizing or replacing actors across full film episodes while preserving narrative structure, motion choreography, and character identity across hundreds of shots. A multi-agent framework with a Director-Cinematographer-Editor architecture enforces long-term language-visual consistency to prevent identity drift and semantic erosion.

**Why trending:** Long-horizon video-to-video generation at the episode scale is a compelling and novel challenge; the multi-agent creative collaboration framing aligns with growing interest in agentic media production pipelines.

**Sources:** HuggingFace Daily Papers, arXiv
