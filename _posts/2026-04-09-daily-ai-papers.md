---
title: 'Daily AI Papers — April 9, 2026'
date: 2026-04-09
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-09/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-systems
  - reasoning-models
  - video-generation
---

**Generated:** 2026-04-09 ~11:20 AM PT
**Note:** Strong day — 27 new HuggingFace papers for Apr 9, plus 20 from Apr 8. Rankings combine fresh HF engagement, cross-platform signals, and carryover papers with sustained momentum.

---

## Top 20 Trending AI/ML Papers

### 1. Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding
- **Authors:** Chaoyou Fu, Haozhi Yuan, Yuhao Dong, Yi-Fan Zhang, Yunhang Shen et al.
- **Summary:** Addresses the critical gap between inflated leaderboard scores and real-world video understanding. Existing benchmarks are saturated — Video-MME-v2 introduces rigorous robustness and faithfulness evaluation to expose where models actually fail. Successor to the widely-used Video-MME.
- **Link:** https://arxiv.org/abs/2604.05015
- **Sources:** HuggingFace #1 Apr 8 (217 upvotes — massive), video-mme.github.io project site, AI Native Foundation digest
- **Why trending:** 217 HF upvotes is exceptional. Benchmarks that expose model weaknesses get attention from both researchers and practitioners. Dedicated project website signals serious community effort.

### 2. Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents
- **Authors:** Bowen Ye, Rang Li, Qibin Yang, Yuanxin Liu, Linli Yao et al.
- **Summary:** Addresses three critical limitations of existing agent benchmarks: trajectory-opaque grading (checking only final outputs), underspecified safety evaluation, and narrow modality coverage. Introduces comprehensive evaluation of autonomous agents across multi-step workflows.
- **Link:** https://arxiv.org/abs/2604.06132
- **Sources:** HuggingFace #2 Apr 8 (102 upvotes), deeplearn.org
- **Why trending:** 102 HF upvotes. Agent evaluation is a hot topic as LLMs deploy into production workflows. Goes beyond "did it get the right answer" to "did it do it safely and correctly."

### 3. RAGEN-2: Reasoning Collapse in Agentic RL
- **Authors:** Zihan Wang, Chi Gui, Xing Jin, Qineng Wang, Licheng Liu et al. (Li Fei-Fei, Yejin Choi co-authors)
- **Summary:** Discovers that RL training of multi-turn LLM agents is inherently unstable — even with stable entropy, models collapse to fixed templates that ignore input differences. Identifies "reasoning collapse" as a fundamental failure mode of agentic RL. Open-source (mll-lab-nu/RAGEN).
- **Link:** https://arxiv.org/abs/2604.06268
- **Sources:** HuggingFace #2 Apr 9 (41 upvotes), GitHub, dedicated project website (ragen-ai.github.io/v2)
- **Why trending:** Star-studded author list (Fei-Fei Li, Yejin Choi). Reasoning collapse is a critical failure mode that affects anyone building RL-trained agents. Open-source + project website.

### 4. Think in Strokes, Not Pixels: Process-Driven Image Generation via Interleaved Reasoning
- **Authors:** Lei Zhang, Junjiao Tian, Zhipeng Fan, Kunpeng Li et al.
- **Summary:** Introduces process-driven image generation — a multi-step paradigm where the model plans a global layout, sketches a coarse draft, inspects, and refines, mimicking how humans paint. Each step is grounded in evolving visual states via interleaved reasoning.
- **Link:** https://arxiv.org/abs/2604.04746
- **Sources:** HuggingFace #1 Apr 9 (43 upvotes), emergentmind, YouTube walkthrough
- **Why trending:** Top HF paper today. The "think like a human painter" framing is compelling. YouTube walkthrough driving engagement beyond the paper itself.

### 5. Learning to Retrieve from Agent Trajectories
- **Authors:** Yuqi Zhou, Sunhao Dai, Changle Qu, Liang Pang, Jun Xu, Ji-Rong Wen
- **Summary:** IR systems have traditionally been designed for human users (clicks, dwell time). With LLM search agents, retrieval is increasingly consumed by agents, not humans. This paper rethinks retrieval for agent consumption — learning to rank based on agent trajectory signals rather than human interaction logs.
- **Link:** https://arxiv.org/abs/2604.04949
- **Sources:** HuggingFace #3 Apr 8 (61 upvotes)
- **Why trending:** Paradigm shift: retrieval systems optimized for agents, not humans. As agentic search becomes mainstream (Perplexity, SearchGPT), this reframes a foundational IR problem.

### 6. MegaTrain: Full Precision Training of 100B+ Parameter LLMs on a Single GPU
- **Authors:** Zhengqing Yuan, Hanchi Sun, Lichao Sun, Yanfang Ye
- **Summary:** Memory-centric system that trains 100B+ parameter models at full precision on a single GPU. Stores parameters and optimizer states in CPU memory, treats GPUs as transient compute engines. Streams parameters in, computes gradients out, minimizing persistent device memory.
- **Link:** https://arxiv.org/abs/2604.05091
- **Sources:** HuggingFace Apr 8 (37 upvotes), emergentmind
- **Why trending:** 100B on one GPU is a democratization headline. Makes large-scale training accessible without massive GPU clusters. Practical implications for researchers with limited hardware.

### 7. MARS: Enabling Autoregressive Models Multi-Token Generation
- **Authors:** Ziqi Jin, Lei Wang, Ziwei Luo, Aixin Sun
- **Summary:** Lightweight fine-tuning method (Mask AutoRegreSsion) that teaches instruction-tuned AR models to predict multiple tokens per forward pass. No architectural modifications, no extra parameters, single model that retains original single-token capability. Pure efficiency gain.
- **Link:** https://arxiv.org/abs/2604.07023
- **Sources:** HuggingFace Apr 9 (21 upvotes)
- **Why trending:** Multi-token generation without architecture changes is the holy grail for inference speedup. The "no extra parameters" claim makes it immediately practical.

### 8. ACES: Who Tests the Tests? Leave-One-Out AUC Consistency for Code Generation
- **Authors:** Hui Sun, Yun-Ji Zhang, Zheng Xie, Ren-Biao Liu et al.
- **Summary:** Tackles the circular dependency in LLM code generation: selecting code candidates using LLM-generated tests, when the tests themselves may be incorrect. Uses leave-one-out AUC consistency to break the circularity without needing to know which codes are correct a priori.
- **Link:** https://arxiv.org/abs/2604.03922
- **Sources:** HuggingFace Apr 8 (49 upvotes)
- **Why trending:** Practical and elegant solution to a real problem every code-generating LLM faces. The "who tests the tests?" framing resonates.

### 9. Beyond Accuracy: Unveiling Inefficiency Patterns in Tool-Integrated Reasoning
- **Authors:** Qisheng Su, Shiting Huang, Zhen Fang, Ziyan Chen et al.
- **Summary:** In tool-integrated reasoning (TIR), external tool calls create pauses that evict KV-Cache, forcing recomputation. Long unfiltered tool responses inflate KV-Cache, slowing decode. This paper systematically catalogs inefficiency patterns in TIR and proposes mitigations.
- **Link:** https://arxiv.org/abs/2604.05404
- **Sources:** HuggingFace Apr 8 (36 upvotes)
- **Why trending:** Directly relevant to anyone building agents with tool use. KV-Cache inefficiency from tool calls is a real production pain point that's rarely studied.

### 10. Neural Computers
- **Authors:** Mingchen Zhuge, Changsheng Zhao, Haozhe Liu, Zijian Zhou et al.
- **Summary:** Proposes Neural Computers (NCs) — an emerging machine form that unifies computation, memory, and I/O in a learned runtime state. Unlike conventional computers (explicit programs), agents (external environments), or world models (environment dynamics), NCs make the model itself the running computer.
- **Link:** https://arxiv.org/abs/2604.06425
- **Sources:** HuggingFace Apr 9 (10 upvotes)
- **Why trending:** Bold vision paper. "The model IS the computer" is a paradigm-defining framing. Connects to neural Turing machine lineage but with modern LLM capabilities.

### 11. ThinkTwice: Jointly Optimizing LLMs for Reasoning and Self-Refinement
- **Authors:** Difan Jiao, Qianfeng Wen, Blair Yang, Zhenwei Tang, Ashton Anderson
- **Summary:** Two-phase framework using GRPO: first optimizes on solving reasoning problems, then on refining solutions to the same problems. Same binary correctness reward for both phases. Simple but effective — jointly trains both the "solve" and "check your work" capabilities.
- **Link:** https://arxiv.org/abs/2604.01591
- **Sources:** HuggingFace Apr 8 (33 upvotes), aimodels.fyi, catalyzex, arxivlens
- **Why trending:** Strong multi-platform indexing. Self-refinement is a hot capability — training it jointly with reasoning rather than separately is an elegant approach.

### 12. INSPATIO-WORLD: A Real-Time 4D World Simulator
- **Authors:** InSpatio Team (Donghui Shen, Guofeng Zhang et al.)
- **Summary:** Real-time 4D world simulator via spatiotemporal autoregressive modeling. Addresses spatial persistence and visual realism for seamless navigation in complex environments. Open-source (inspatio/worldfm on GitHub).
- **Link:** https://arxiv.org/abs/2604.07209
- **Sources:** HuggingFace Apr 9 (16 upvotes), GitHub, aifilms.ai coverage, theresanaiforthat.com
- **Why trending:** Open-source 4D world model with GitHub code, multi-platform media coverage. Real-time interactivity is a key differentiator.

### 13. SEVerA: Verified Synthesis of Self-Evolving Agents
- **Authors:** Debangshu Banerjee, Changming Xu, Gagandeep Singh
- **Summary:** Framework for synthesizing self-evolving agents with formal verification guarantees. Addresses the safety concern of agents that modify their own behavior — ensures evolved agents maintain verified properties.
- **Link:** https://arxiv.org/abs/2603.25111
- **Sources:** HuggingFace Apr 9 (17 upvotes), alphaxiv, catalyzex
- **Why trending:** Self-evolving agents are exciting but terrifying — formal verification brings much-needed safety guarantees. Timely as autonomous agents proliferate.

### 14. The Depth Ceiling: On the Limits of LLMs in Discovering Latent Planning
- **Authors:** Yi Xu, Philipp Jettkant, Laura Ruis
- **Summary:** Tests whether LLMs can discover multi-step planning strategies without supervision on intermediate steps and execute them latently within a single forward pass. Directly relevant to CoT monitoring — if models can plan latently, CoT monitoring for safety is insufficient.
- **Link:** https://arxiv.org/abs/2604.06427
- **Sources:** HuggingFace Apr 9 (4 upvotes)
- **Why trending:** Companion to "Therefore I am. I Think" from last week — both investigate whether reasoning happens in CoT or latently. Critical for AI safety and alignment.

### 15. Watch Before You Answer: Learning from Visually Grounded Post-Training
- **Authors:** Yuxuan Zhang, EunJeong Hwang, Huaisong Zhang et al.
- **Summary:** Finds that commonly reported long video understanding benchmarks contain 40-60% of questions answerable without watching the video. Proposes visually grounded post-training to force models to actually use visual information.
- **Link:** https://arxiv.org/abs/2604.05117
- **Sources:** HuggingFace Apr 8 (27 upvotes)
- **Why trending:** Devastating finding: most video benchmarks don't test video understanding. Echoes "VLMs Need Words" from last week — growing evidence that multimodal models aren't truly multimodal.

### 16. FP4 Explore, BF16 Train: Diffusion RL via Efficient Rollout Scaling
- **Authors:** Yitong Li, Junsong Chen, Shuchen Xue et al. (Song Han co-author)
- **Summary:** Scales RL-based alignment for text-to-image diffusion models (e.g., FLUX.1-12B) by using FP4 precision for exploration rollouts and BF16 for training. Mixed-precision approach dramatically reduces compute for RL alignment of large diffusion models.
- **Link:** https://arxiv.org/abs/2604.06916
- **Sources:** HuggingFace Apr 9 (8 upvotes), alphaxiv
- **Why trending:** Song Han co-author. Practical mixed-precision trick for RL alignment of diffusion models — directly applicable to production image generation systems.

### 17. MedGemma 1.5 Technical Report
- **Authors:** Andrew Sellergren, Chufan Gao, Fereshteh Mahvar et al. (Google DeepMind)
- **Summary:** Technical report for Google DeepMind's medical AI model MedGemma 1.5. Built on the Gemma architecture, specialized for medical applications including clinical text, medical imaging, and health-related reasoning.
- **Link:** https://arxiv.org/abs/2604.05081
- **Sources:** HuggingFace Apr 8 (9 upvotes), Google DeepMind official page, arxiv HTML
- **Why trending:** Google DeepMind official release. Medical AI is a high-stakes application domain — MedGemma represents a major company's investment in healthcare AI.

### 18. GBQA: A Game Benchmark for Evaluating LLMs as Quality Assurance Engineers
- **Authors:** Shufan Jiang, Chios Chen, Zhiyang Chen et al.
- **Summary:** Novel benchmark using games to evaluate LLMs as QA engineers. Tests whether LLMs can find bugs, verify behavior, and ensure quality — a practical skill for software engineering applications.
- **Link:** https://arxiv.org/abs/2604.02648
- **Sources:** HuggingFace Apr 8 (39 upvotes)
- **Why trending:** Games as QA testbed is creative. LLM-as-QA-engineer is an immediately practical application that companies care about.

### 19. General Multimodal Protein Design Enables DNA-Encoding of Chemistry
- **Authors:** Jarrid Rector-Brooks, Théophile Lambert, Marta Skreta et al.
- **Summary:** Multimodal protein design framework that enables encoding chemical information into DNA. Bridges protein engineering and chemistry through generative design — a significant step for synthetic biology.
- **Link:** https://arxiv.org/abs/2604.05181
- **Sources:** HuggingFace Apr 8 (23 upvotes), AI Native Foundation digest
- **Why trending:** Cross-disciplinary AI for biology. DNA-encoding of chemistry via protein design has transformative implications for drug discovery and synthetic biology.

### 20. Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs
- **Authors:** Hongyuan Yuan, Xinran He, Run Shao et al.
- **Summary:** Addresses the verbosity problem in reasoning LLMs — redundant reflections and repetitive CoT steps that waste compute. Uses graph-based pruning to identify and remove redundant reasoning steps while maintaining accuracy.
- **Link:** https://arxiv.org/abs/2604.05643
- **Sources:** HuggingFace Apr 9 (6 upvotes)
- **Why trending:** Practical efficiency improvement for reasoning models. Everyone running o1/R1-style models pays for redundant CoT tokens — pruning them is directly cost-saving.

---

## Honorable Mentions

- **Paper Circle** (2604.06170) — Open-source multi-agent research discovery framework. HF 20 upvotes.
- **How Well Do Agentic Skills Work in the Wild** (2604.04323) — Benchmarking LLM skill usage in realistic settings. HF 29 upvotes.
- **ClawsBench** (2604.05172) — Evaluating LLM productivity agents in simulated workspaces. HF 18 upvotes.
- **DARE: Diffusion LLM Alignment** (2604.04215) — RL executor for diffusion LLMs. HF 18 upvotes.
- **In-Place Test-Time Training** (2604.06169) — Efficient TTT without separate adaptation. HF 18 upvotes.
- **Vanast: Virtual Try-On** (2604.04934) — Human image animation for virtual try-on. HF 35 upvotes.
- **TC-AE: Token Capacity for Deep Compression** (2604.07340) — Unlocking token capacity in autoencoders. HF 9 upvotes.

---

## Methodology

| Source | Status | Notes |
|--------|--------|-------|
| HuggingFace Daily Papers | ✅ 27 papers (Apr 9) + 20 papers (Apr 8) | Top: Video-MME-v2 (217), Claw-Eval (102) |
| Reddit r/MachineLearning | ✅ Searched | General ML papers-of-the-week results |
| Reddit r/LocalLLaMA | ✅ Searched | Landing page + YouTube digest |
| X/Twitter | ✅ Searched via web | Cross-platform signals captured |
| Company Blogs | ✅ Google DeepMind (MedGemma 1.5) | No new Anthropic/OpenAI/Meta FAIR posts this cycle |
| arxiv | ✅ Direct abstract extraction (15 papers) | Via proxy |
| Papers With Code | ✅ Searched | Redirected to arxiv |
| Hacker News | ✅ Searched | General AI papers results |
| GitHub | ✅ RAGEN-2, INSPATIO-WORLD | Open-source releases verified |
| AI Native Foundation | ✅ Apr 8 digest referenced | Video-MME-v2, Protein Design featured |

**Ranking criteria:** Cross-platform presence > company blog/announcement > fresh HF upvotes > open-source release > conference acceptance > topic relevance to AI/ML community.
