---
title: 'Daily AI Papers — April 11, 2026'
date: 2026-04-11
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-11/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-systems
  - reinforcement-learning
  - multimodal-models
---

## 1. SkillClaw: Let Skills Evolve Collectively with Agentic Evolver
- **Authors:** Ziyu Ma, Shidong Yang, Yuxiang Ji, Xucong Wang, Yong Wang, Yiming Hu, Tongwen Huang, Xiangxiang Chu
- **arxiv:** [2604.08377](https://arxiv.org/abs/2604.08377)
- **Summary:** SkillClaw introduces a framework for collective skill evolution in multi-user LLM agent ecosystems. It aggregates trajectories from user interactions and uses an autonomous evolver to identify recurring patterns, refining existing skills or extending them with new capabilities. Skills are shared across users, enabling cross-user knowledge transfer without additional effort.
- **Sources:** HuggingFace (207⬆), arxiv, EmergentMind, YouTube, SkillClaw.org, X/Twitter
- **Why Trending:** Highest upvoted paper on HuggingFace. Addresses a critical gap in agentic AI — making skills improve collectively from real-world usage rather than remaining static post-deployment. Strong cross-platform buzz with dedicated website and video explainer.

---

## 2. Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability
- **Authors:** Qihan Ren, Peng Wang, Ruikun Cai, Shuai Shao, Dadi Guo, Yuejin Xie, Yafu Li, Quanshi Zhang, Xia Hu, Jing Shao, Dongrui Liu (AI45Research)
- **arxiv:** [2604.06628](https://arxiv.org/abs/2604.06628)
- **Summary:** Challenges the prevailing narrative that SFT memorizes while RL generalizes. Shows that reasoning SFT cross-domain generalization is conditional — shaped by optimization dynamics, data quality, and base-model capability. Reveals a "dip-and-recovery" pattern where short training underestimates generalization, and that reasoning gains come at the cost of safety degradation.
- **Sources:** HuggingFace (176⬆), arxiv, GitHub (74⭐)
- **Why Trending:** Directly challenges a core assumption in LLM post-training. The finding that SFT can generalize under the right conditions reshapes how the community thinks about training recipes. GitHub repo gaining rapid traction.

---

## 3. HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents
- **Authors:** Tencent Robotics X, HY Vision Team, Xumin Yu, Zuyan Liu, Ziyi Wang, He Zhang, Yongming Rao, Fangfu Liu et al.
- **arxiv:** [2604.07430](https://arxiv.org/abs/2604.07430)
- **Summary:** A family of foundation models for real-world embodied agents featuring Mixture-of-Transformers architecture. Designed to bridge the gap between general VLMs and embodied intelligence needs, enhancing spatial/temporal visual perception alongside advanced embodied reasoning for prediction, interaction, and planning.
- **Sources:** HuggingFace (139⬆), arxiv, Tencent Research Blog
- **Why Trending:** Major industry release from Tencent Robotics X. Embodied AI is a hot frontier, and this represents one of the first open foundation model families purpose-built for real-world robot agents with strong visual grounding.

---

## 4. When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models (NUMINA)
- **Authors:** Zhengyang Sun, Yu Chen, Xin Zhou et al.
- **arxiv:** [2604.08546](https://arxiv.org/abs/2604.08546)
- **Summary:** NUMINA is a training-free framework that fixes a persistent problem in text-to-video models: generating the correct number of objects. It identifies prompt-layout inconsistencies using discriminative attention heads, derives countable latent layouts, and guides regeneration via attention modulation.
- **Sources:** HuggingFace (107⬆), arxiv
- **Why Trending:** Addresses a well-known and frustrating failure mode of generative video models (wrong object counts). Training-free approach makes it immediately applicable. Clean, practical contribution.

---

## 5. ClawBench: Can AI Agents Complete Everyday Online Tasks?
- **Authors:** Yuxuan Zhang, Yubo Wang, Yipeng Zhu et al.
- **arxiv:** [2604.08523](https://arxiv.org/abs/2604.08523)
- **Summary:** A comprehensive evaluation framework with 153 real-world tasks across 144 live platforms spanning 15 categories (purchases, bookings, job applications, etc.). Tests whether AI agents can actually automate routine aspects of digital life, providing a realistic and challenging testbed for next-gen agents.
- **Sources:** HuggingFace (98⬆), arxiv
- **Why Trending:** Fills a major gap in agent evaluation — moving from synthetic benchmarks to real-world, live-platform tasks. The scale (144 platforms) and practical focus make it immediately relevant for agent developers.

---

## 6. MegaStyle: Constructing Diverse and Scalable Style Dataset via Consistent Text-to-Image Style Mapping
- **Authors:** Junyao Gao, Sibo Liu, Jiaxing Li et al.
- **arxiv:** [2604.08364](https://arxiv.org/abs/2604.08364)
- **Summary:** Introduces a scalable data curation pipeline for building intra-style consistent, inter-style diverse datasets. Leverages the consistent text-to-image style mapping of large generative models with 170K style prompts and 400K content prompts. Proposes style-supervised contrastive learning for effective style representation.
- **Sources:** HuggingFace (83⬆), arxiv
- **Why Trending:** Style transfer and consistent stylization remain hot topics in creative AI. The massive scale of the curated dataset (170K+ prompts) and the practical pipeline make this valuable for both researchers and practitioners.

---

## 7. Think in Strokes, Not Pixels: Process-Driven Image Generation via Interleaved Reasoning
- **Authors:** Lei Zhang, Junjiao Tian, Zhipeng Fan et al.
- **arxiv:** [2604.04746](https://arxiv.org/abs/2604.04746)
- **Summary:** Introduces process-driven image generation — decomposing synthesis into iterative steps of textual planning, visual drafting, textual reflection, and visual refinement. Mimics how humans paint incrementally, with each step grounded in evolving visual states. Uses step-wise supervision for interleaved reasoning trajectories.
- **Sources:** HuggingFace (59⬆), arxiv
- **Why Trending:** A paradigm shift in image generation — moving from single-shot pixel prediction to human-like iterative reasoning. The interleaved text-vision approach opens new possibilities for controllable and interpretable generation.

---

## 8. RAGEN-2: Reasoning Collapse in Agentic RL
- **Authors:** Zihan Wang, Chi Gui, Xing Jin et al.
- **arxiv:** [2604.06268](https://arxiv.org/abs/2604.06268)
- **Summary:** Identifies "template collapse" — a hidden failure mode in multi-turn RL-trained LLM agents where models rely on fixed templates that look diverse but are input-agnostic. Standard entropy metrics miss this entirely. Proposes mutual information proxies and SNR-aware filtering to detect and mitigate reasoning collapse.
- **Sources:** HuggingFace (52⬆), arxiv, RAGEN project site, GitHub
- **Why Trending:** Critical finding for anyone training agentic LLMs with RL. Template collapse is invisible to standard metrics, making this a wake-up call for the community. Practical mitigation strategies included.

---

## 9. LPM 1.0: Video-based Character Performance Model
- **Authors:** Ailing Zeng, Casper Yang, Chauncey Ge et al.
- **arxiv:** [2604.07823](https://arxiv.org/abs/2604.07823)
- **Summary:** A large-scale multimodal model for real-time conversational character performance generation. Tackles the "performance trilemma" — jointly achieving high expressiveness, real-time inference, and long-horizon identity stability. Enables interactive, infinite-length video synthesis while maintaining character identity.
- **Sources:** HuggingFace (38⬆), arxiv
- **Why Trending:** Character animation and performance generation are key for gaming, film, and digital humans. Real-time capability with identity consistency represents a significant advance over existing methods.

---

## 10. OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks
- **Authors:** Wenbo Hu, Xin Chen, Yan Gao-Tian et al.
- **arxiv:** [2604.08539](https://arxiv.org/abs/2604.08539)
- **Summary:** Introduces Gaussian GRPO to address extreme variance in reward topologies across diverse visual tasks. Achieves distributional matching for gradient equity and stable RL training, enabling improved perception-reasoning balance in open-source multimodal generalist models.
- **Sources:** HuggingFace (37⬆), arxiv
- **Why Trending:** Pushes open-source multimodal reasoning forward with a practical fix for a key RL training challenge. Balancing fine-grained perception with multi-step reasoning is a core unsolved problem.

---

## 11. DMax: Aggressive Parallel Decoding for dLLMs
- **Authors:** Zigeng Chen, Gongfan Fang, Xinyin Ma et al.
- **arxiv:** [2604.08302](https://arxiv.org/abs/2604.08302)
- **Summary:** A new paradigm for efficient diffusion language models that reformulates decoding as progressive self-refinement from mask to token embeddings. Uses On-Policy Uniform Training to enable aggressive decoding parallelism while preserving generation quality, significantly reducing error accumulation.
- **Sources:** HuggingFace (35⬆), arxiv
- **Why Trending:** Diffusion LLMs are an emerging alternative to autoregressive models. DMax makes them practically faster with a clean training strategy, potentially accelerating the dLLM research trajectory.

---

## 12. KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation
- **Authors:** Tongbo Chen, Zhengxi Lu, Zhan Xu et al.
- **arxiv:** [2604.08455](https://arxiv.org/abs/2604.08455)
- **Summary:** Evaluates personalized mobile agents on their ability to infer user preferences through interaction and decide when to intervene, seek consent, or remain silent. Tests proactive assistance in live GUI environments — a capability no prior benchmark has measured.
- **Sources:** HuggingFace (35⬆), arxiv
- **Why Trending:** As mobile AI assistants become mainstream, evaluating proactive and personalized behavior is critical. First benchmark to test interactive preference elicitation in real GUI contexts.

---

## 13. Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering
- **Authors:** Chenyu Zhou, Huacan Chai, Wenteng Chen et al.
- **arxiv:** [2604.08224](https://arxiv.org/abs/2604.08224)
- **Summary:** Comprehensive review of how LLM agents are built less by changing model weights and more by reorganizing runtime — externalizing capabilities into memory stores, reusable skills, interaction protocols, and surrounding harness. Frames this through the lens of cognitive artifacts and externalization.
- **Sources:** HuggingFace (33⬆), arxiv
- **Why Trending:** Timely survey that captures the paradigm shift in agent building. As the field moves from model-centric to system-centric approaches, this review provides a unifying framework.

---

## 14. Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models
- **Authors:** Shilin Yan, Jintao Tong, Hongwei Xue et al.
- **arxiv:** [2604.08545](https://arxiv.org/abs/2604.08545)
- **Summary:** Addresses "blind tool invocation" in agentic models — the tendency to reflexively call tools even when queries are resolvable from visual context alone. Introduces HDPO (a decoupled optimization framework) for teaching agents when NOT to use tools, improving efficiency and accuracy.
- **Sources:** HuggingFace (29⬆), arxiv
- **Why Trending:** Meta-cognition in AI agents (knowing what you know) is an under-explored but crucial capability. This paper tackles a real pathological behavior with a practical training solution.

---

## 15. MolmoWeb: Open Visual Web Agent and Open Data for the Open Web
- **Authors:** Tanmay Gupta, Piper Wolters, Zixian Ma et al.
- **arxiv:** [2604.08516](https://arxiv.org/abs/2604.08516)
- **Summary:** An open-source web agent that navigates and executes tasks on the web using only visual information — no HTML or accessibility tree required. Introduces MolmoWebMix, a large diverse training dataset, and achieves state-of-the-art on browser-based tasks among open models.
- **Sources:** HuggingFace (29⬆), arxiv
- **Why Trending:** A strong open-source alternative to proprietary web agents. Operating without HTML/a11y tree access is a significant constraint that makes this more robust to real-world web diversity.

---

## 16. MARS: Enabling Autoregressive Models Multi-Token Generation
- **Authors:** Ziqi Jin, Lei Wang, Ziwei Luo et al.
- **arxiv:** [2604.07023](https://arxiv.org/abs/2604.07023)
- **Summary:** MARS (Mask AutoRegreSsion) is a lightweight fine-tuning method that teaches instruction-tuned AR models to predict multiple tokens per forward pass. Requires no architectural changes, no extra parameters, and the fine-tuned model remains fully compatible with standard AR inference.
- **Sources:** HuggingFace (29⬆), arxiv
- **Why Trending:** Multi-token prediction is a hot efficiency topic. MARS stands out because it's a pure fine-tuning approach with zero architectural overhead — a practical path to faster inference for existing models.

---

## 17. Neural Computers
- **Authors:** Mingchen Zhuge, Changsheng Zhao, Haozhe Liu et al.
- **arxiv:** [2604.06425](https://arxiv.org/abs/2604.06425)
- **Summary:** Proposes Neural Computers (NCs) — a new computing paradigm where the model itself becomes the running computer, unifying computation, memory, and I/O in a learned runtime state. Distinct from agents (which act over external environments) and world models (which learn dynamics). Long-term vision: the Completely Neural Computer (CNC).
- **Sources:** HuggingFace (18⬆), arxiv, alphaXiv, METAUTO.ai
- **Why Trending:** Bold, paradigm-defining vision paper from a well-known research group. The concept of "model as computer" sparks deep theoretical discussion about the future of computation itself.

---

## 18. OpenSpatial: A Principled Data Engine for Empowering Spatial Intelligence
- **Authors:** Jianhui Liu, Haoze Sun, Wenbo Li et al.
- **arxiv:** [2604.07296](https://arxiv.org/abs/2604.07296)
- **Summary:** An open-source data engine for spatial reasoning using 3D bounding boxes. Creates a large-scale dataset and achieves state-of-the-art on spatial perception benchmarks. Addresses the critical gap of principled, open-source spatial data generation for spatial intelligence research.
- **Sources:** HuggingFace (28⬆), arxiv
- **Why Trending:** Spatial understanding is fundamental for embodied AI, robotics, and AR/VR. An open data engine for this is a significant infrastructure contribution.

---

## 19. INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling
- **Authors:** InSpatio Team, Donghui Shen, Guofeng Zhang et al.
- **arxiv:** [2604.07209](https://arxiv.org/abs/2604.07209)
- **Summary:** A real-time framework for generating high-fidelity, dynamic interactive scenes from single videos using spatiotemporal autoregressive architecture and joint distribution matching distillation. Enables seamless navigation in complex 3D environments with spatial consistency.
- **Sources:** HuggingFace (26⬆), arxiv
- **Why Trending:** World simulators are a key building block for autonomous systems and gaming. Real-time 4D generation from single video is a compelling capability with broad applications.

---

## 20. Combee: Scaling Prompt Learning for Self-Improving Language Model Agents
- **Authors:** Hanchen Li, Runyuan He, Qizheng Zhang et al.
- **arxiv:** [2604.04247](https://arxiv.org/abs/2604.04247)
- **Summary:** Enables scalable parallel prompt learning for self-improving agents using parallel scans, augmented shuffle mechanisms, and dynamic batch size control. Overcomes the limitations of existing methods that are restricted to single-agent or low-parallelism settings.
- **Sources:** HuggingFace (24⬆), arxiv
- **Why Trending:** Self-improvement at scale is a key challenge for deployed agents. Combee provides practical infrastructure for learning from large sets of agent traces efficiently.

---

## Honorable Mentions

| Paper | ID | Upvotes | Key Idea |
|---|---|---|---|
| SEVerA: Verified Synthesis of Self-Evolving Agents | 2603.25111 | 24⬆ | Formally verified agentic code generation |
| FP4 Explore, BF16 Train (Sol-RL) | 2604.06916 | 13⬆ | FP4 quantization for diffusion RL training |
| Graph of Skills (GoS) | 2604.05333 | 17⬆ | Dependency-aware skill retrieval for agents |
| Flux Attention | 2604.07394 | 9⬆ | Context-aware hybrid attention for LLM inference |
| Graph-Based CoT Pruning | 2604.05643 | 8⬆ | Pruning redundant reasoning in LLMs |

---

*Report generated: April 11, 2026 10:00 PDT*
*Sources checked: HuggingFace Daily Papers API, arxiv, Reddit, X/Twitter, Hacker News, Papers With Code, Company Blogs*
