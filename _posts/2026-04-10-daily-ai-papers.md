---
title: 'Daily AI Papers — April 10, 2026'
date: 2026-04-10
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-10/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-systems
  - embodied-ai
  - video-generation
---

## 1. SkillClaw: Let Skills Evolve Collectively with Agentic Evolver
- **Authors:** Ziyu Ma, Shidong Yang, Yuxiang Ji et al.
- **ArXiv:** [arxiv.org/abs/2604.08377](https://arxiv.org/abs/2604.08377)
- **Summary:** Introduces a framework for collective skill evolution in multi-user LLM agent ecosystems, treating cross-user interactions as the primary signal for improving reusable agent skills. SkillClaw enables skills to continuously improve post-deployment rather than remaining static.
- **Sources:** HuggingFace (139 upvotes, #1), ArXiv, EmergentMind, blog coverage (blakecrosley.com)
- **Why trending:** Addresses a key pain point in LLM agent systems — static skills. High community engagement and cross-platform visibility with blog discussion.

## 2. Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability
- **Authors:** Qihan Ren, Peng Wang, Ruikun Cai et al.
- **ArXiv:** [arxiv.org/abs/2604.06628](https://arxiv.org/abs/2604.06628)
- **Summary:** Challenges the prevailing narrative that SFT memorizes while RL generalizes for LLM reasoning. Reveals a "dip-and-recovery" pattern where cross-domain performance degrades before recovering with extended training, suggesting prior reported failures may be under-optimization artifacts.
- **Sources:** HuggingFace (124 upvotes, #2), ArXiv, OpenReview
- **Why trending:** Directly challenges dominant assumptions in the LLM post-training community with rigorous conditional analysis. Important implications for training pipelines.

## 3. HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents
- **Authors:** Tencent Robotics X, HY Vision Team, Xumin Yu et al.
- **ArXiv:** [arxiv.org/abs/2604.07430](https://arxiv.org/abs/2604.07430)
- **Summary:** A family of foundation models for real-world embodied agents from Tencent, featuring 2B (edge) and 32B (complex reasoning) variants. Uses Mixture-of-Transformers (MoT) architecture for fine-grained spatial/temporal perception and embodied reasoning.
- **Sources:** HuggingFace (105 upvotes, #3), ArXiv, EmergentMind, HuggingFace model hub (tencent/HY-Embodied-0.5)
- **Why trending:** Major industry release from Tencent with open model weights. Bridges the gap between VLMs and embodied AI with practical deployment focus.

## 4. When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models (NUMINA)
- **Authors:** Zhengyang Sun, Yu Chen, Xin Zhou et al.
- **ArXiv:** [arxiv.org/abs/2604.08546](https://arxiv.org/abs/2604.08546)
- **Summary:** Introduces NUMINA, a training-free framework that fixes object counting errors in text-to-video diffusion models by identifying prompt-layout inconsistencies via self-/cross-attention heads. Improves counting accuracy by up to 7.4% on Wan2.1 models.
- **Sources:** HuggingFace (104 upvotes, #4), ArXiv, EmergentMind, nexu.io blog coverage
- **Why trending:** Solves a highly visible and frustrating problem in video generation. Training-free approach makes it immediately applicable.

## 5. MegaStyle: Constructing Diverse and Scalable Style Dataset via Consistent Text-to-Image Style Mapping
- **Authors:** Junyao Gao, Sibo Liu, Jiaxing Li et al.
- **ArXiv:** [arxiv.org/abs/2604.08364](https://arxiv.org/abs/2604.08364)
- **Summary:** Presents a novel pipeline for curating large-scale style datasets (MegaStyle-1.4M) by leveraging consistent text-to-image style mapping. Proposes style-supervised contrastive learning and trains a FLUX-based style-driven generation model.
- **Sources:** HuggingFace (79 upvotes, #5), ArXiv
- **Why trending:** Addresses the data bottleneck for style transfer with a scalable approach. 1.4M sample dataset is a significant resource for the creative AI community.

## 6. ClawBench: Can AI Agents Complete Everyday Online Tasks?
- **Authors:** Yuxuan Zhang, Yubo Wang, Yipeng Zhu et al.
- **ArXiv:** [arxiv.org/abs/2604.08523](https://arxiv.org/abs/2604.08523)
- **Summary:** An evaluation framework of 153 real-world tasks across 144 live platforms (purchasing, booking, job applications). Tests demanding capabilities like document understanding, multi-step workflows, and form-filling that go beyond existing agent benchmarks.
- **Sources:** HuggingFace (52 upvotes, #6), ArXiv, BenchLM.ai, ClawBench.com
- **Why trending:** Fills a critical gap in agent evaluation with real-world, not simulated, tasks. Multiple benchmark platforms already tracking it.

## 7. LPM 1.0: Video-based Character Performance Model
- **Authors:** Ailing Zeng, Casper Yang, Chauncey Ge et al.
- **ArXiv:** [arxiv.org/abs/2604.07823](https://arxiv.org/abs/2604.07823)
- **Summary:** A Large Performance Model for single-person full-duplex audio-visual conversational performance. Addresses the "performance trilemma" of expressiveness, real-time inference, and long-horizon identity stability in video character generation.
- **Sources:** HuggingFace (35 upvotes, #7), ArXiv, AI Flash Report
- **Why trending:** Tackles a fundamental challenge in digital characters/avatars. Full-duplex conversational performance is key for interactive applications.

## 8. KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation
- **Authors:** Tongbo Chen, Zhengxi Lu, Zhan Xu et al.
- **ArXiv:** [arxiv.org/abs/2604.08455](https://arxiv.org/abs/2604.08455)
- **Summary:** An online benchmark for personalized mobile agents on Android emulation covering 192 tasks. Unlike prior work that treats preferences as static, KnowU-Bench requires agents to interactively elicit preferences and decide when to intervene or stay silent.
- **Sources:** HuggingFace (33 upvotes, #8), ArXiv, AlphaXiv
- **Why trending:** Benchmarks the next frontier of mobile agents — proactive personalization. Novel interactive evaluation paradigm.

## 9. Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering
- **Authors:** Chenyu Zhou, Huacan Chai, Wenteng Chen et al.
- **ArXiv:** [arxiv.org/abs/2604.08224](https://arxiv.org/abs/2604.08224)
- **Summary:** A comprehensive review arguing that modern LLM agent capabilities are increasingly built by reorganizing runtime infrastructure (memory, skills, protocols) rather than changing model weights. Frames this through the lens of cognitive artifact externalization.
- **Sources:** HuggingFace (30 upvotes, #9), ArXiv
- **Why trending:** Timely survey that captures the paradigm shift in agent engineering. Useful framing for researchers and practitioners building agent systems.

## 10. DMax: Aggressive Parallel Decoding for dLLMs
- **Authors:** Zigeng Chen, Gongfan Fang, Xinyin Ma et al.
- **ArXiv:** [arxiv.org/abs/2604.08302](https://arxiv.org/abs/2604.08302)
- **Summary:** A new paradigm for efficient diffusion language models (dLLMs) that reformulates decoding as progressive self-refinement. Introduces On-Policy Uniform Training and Soft Parallel Decoding for aggressive parallelism while maintaining generation quality.
- **Sources:** HuggingFace (28 upvotes, #10), ArXiv, EmergentMind
- **Why trending:** Diffusion-based LLMs are gaining traction as an alternative to autoregressive models. DMax makes their parallel decoding practical.

## 11. OpenSpatial: A Principled Data Engine for Empowering Spatial Intelligence
- **Authors:** Jianhui Liu, Haoze Sun, Wenbo Li et al.
- **ArXiv:** [arxiv.org/abs/2604.07296](https://arxiv.org/abs/2604.07296)
- **Summary:** An open-source data engine for generating high-quality spatial understanding data across five foundational tasks (measurement, relationships, camera perception, multi-view consistency). Uses 3D bounding boxes as fundamental primitives.
- **Sources:** HuggingFace (26 upvotes, #11), ArXiv
- **Why trending:** Spatial intelligence is a hot area with robotics and embodied AI growth. Fills the void of a principled open-source spatial data generation system.

## 12. Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models
- **Authors:** Shilin Yan, Jintao Tong, Hongwei Xue et al.
- **ArXiv:** [arxiv.org/abs/2604.08545](https://arxiv.org/abs/2604.08545)
- **Summary:** Addresses the "blind tool invocation" problem in multimodal agents where models reflexively call tools even when queries are answerable from visual context. Proposes a decoupled reward framework to balance internal reasoning vs. external tool use.
- **Sources:** HuggingFace (25 upvotes, #12), ArXiv
- **Why trending:** Targets a practical inefficiency in deployed agent systems. Meta-cognitive arbitration between internal knowledge and tool use is an emerging research direction.

## 13. OmniJigsaw: Enhancing Omni-Modal Reasoning via Modality-Orchestrated Reordering
- **Authors:** Yiduo Jia, Muzhi Zhu, Hao Zhong et al.
- **ArXiv:** [arxiv.org/abs/2604.08209](https://arxiv.org/abs/2604.08209)
- **Summary:** A self-supervised RL post-training framework for omni-modal models using temporal reordering of shuffled audio-visual clips. Proposes three cross-modal integration strategies and a two-stage data filtering pipeline.
- **Sources:** HuggingFace (16 upvotes, #13), ArXiv
- **Why trending:** Novel approach to extending RL post-training beyond text to audio-visual reasoning. Creative proxy task design.

## 14. Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills
- **Authors:** Dawei Li, Zongxia Li, Hongyang Du et al.
- **ArXiv:** [arxiv.org/abs/2604.05333](https://arxiv.org/abs/2604.05333)
- **Summary:** An inference-time structural retrieval layer for large agent skill libraries. Constructs executable skill graphs offline and retrieves bounded, dependency-aware skill bundles to avoid context window saturation and reduce hallucination.
- **Sources:** HuggingFace (16 upvotes, #14), ArXiv
- **Why trending:** Practical solution to the scaling problem of agent skill libraries. Complements the SkillClaw paper (#1) in the agent skills ecosystem.

## 15. Structured Distillation of Web Agent Capabilities Enables Generalization (Agent-as-Annotators)
- **Authors:** Xing Han Lù, Siva Reddy
- **ArXiv:** [arxiv.org/abs/2604.07776](https://arxiv.org/abs/2604.07776)
- **Summary:** A framework that distills frontier LLM web agent capabilities into small open-weight models using structured synthetic trajectory generation. A 9B student model achieves 41.5% on WebArena, surpassing Claude 3.5 Sonnet (36.0%) and GPT-4o (31.5%).
- **Sources:** HuggingFace (13 upvotes, #15), ArXiv, papers.fzhiy.net daily
- **Why trending:** Remarkable result: a 9B model beating frontier closed-source models on web navigation. Key advancement for open-weight agent models.

## 16. OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks
- **Authors:** Wenbo Hu, Xin Chen, Yan Gao-Tian et al.
- **ArXiv:** [arxiv.org/abs/2604.08539](https://arxiv.org/abs/2604.08539)
- **Summary:** Introduces Gaussian GRPO (G²RPO), a novel RL training objective using non-linear distributional matching to force advantage distributions to converge to standard normal. Enables training a generalist multimodal reasoning model across diverse visual tasks.
- **Sources:** HuggingFace (13 upvotes, #16), ArXiv
- **Why trending:** Advances the state of open-source multimodal reasoning models. Novel RL objective design addresses reward variance across heterogeneous tasks.

## 17. FIT: A Large-Scale Dataset for Fit-Aware Virtual Try-On
- **Authors:** Johanna Karras, Yuanhao Wang, Yingwei Li et al.
- **ArXiv:** [arxiv.org/abs/2604.08526](https://arxiv.org/abs/2604.08526)
- **Summary:** First dataset providing precise garment and body size information for virtual try-on, including "ill-fit" cases. Addresses the overlooked dimension of garment fit accuracy — how an XL shirt looks on an XS person.
- **Sources:** HuggingFace (12 upvotes, #17), ArXiv, Paperium
- **Why trending:** Solves a key gap in virtual try-on research. Practical e-commerce applications make this commercially relevant.

## 18. Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference
- **Authors:** Quantong Qiu, Zhiyi Hong, Yi Yang et al.
- **ArXiv:** [arxiv.org/abs/2604.07394](https://arxiv.org/abs/2604.07394)
- **Summary:** A context-aware framework that dynamically optimizes attention computation at the layer level, combining Full Attention and Sparse Attention with a lightweight Layer Router. Addresses the scalability bottleneck of standard attention for long-context LLMs.
- **Sources:** HuggingFace (9 upvotes, #18), ArXiv
- **Why trending:** Long-context efficiency is a critical infrastructure problem. Dynamic layer-level sparsity is a pragmatic middle ground between full and sparse attention.

## 19. Automating Database-Native Function Code Synthesis with LLMs (DBCooker)
- **Authors:** Wei Zhou, Xuanhe Zhou, Qikang He et al.
- **ArXiv:** [arxiv.org/abs/2604.06231](https://arxiv.org/abs/2604.06231)
- **Summary:** An LLM-based system for automatically synthesizing database native functions, handling the complexity of multi-unit registration, internal reference linking, and logic implementation that generic code generation tools struggle with.
- **Sources:** HuggingFace (9 upvotes, #19), ArXiv
- **Why trending:** Niche but impactful — LLM-driven automation for database kernel development. Addresses a real pain point in database systems engineering.

## 20. ViVa: A Video-Generative Value Model for Robot Reinforcement Learning
- **Authors:** Jindi Lv, Hao Li, Jie Li et al.
- **ArXiv:** [arxiv.org/abs/2604.08168](https://arxiv.org/abs/2604.08168)
- **Summary:** Repurposes a pretrained video generator for value estimation in robot manipulation RL. Jointly predicts future proprioception and state values, leveraging spatiotemporal priors to handle partial observability and delayed feedback.
- **Sources:** HuggingFace (8 upvotes, #20), ArXiv
- **Why trending:** Creative intersection of video generation and robot RL. Uses video priors to solve the long-horizon value estimation problem in manipulation.

---

## Key Themes Today
1. **Agent Skills & Infrastructure** (#1, #6, #9, #12, #14): Agent systems are maturing beyond model capability into skill management, retrieval, and evolution.
2. **Reasoning & Generalization** (#2, #16): The SFT vs RL debate for reasoning continues with nuanced findings.
3. **Embodied AI** (#3, #11, #20): Robotics foundation models gaining momentum with practical deployment focus.
4. **Video Generation** (#4, #7): Text-to-video alignment and character performance remain active areas.
5. **Efficient Inference** (#10, #18): Parallel decoding and attention optimization for production LLMs.

*Report generated 2026-04-10 10:00 PDT*
