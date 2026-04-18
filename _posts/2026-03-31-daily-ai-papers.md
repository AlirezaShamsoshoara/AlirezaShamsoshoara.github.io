---
title: 'Daily AI Papers — March 31, 2026'
date: 2026-03-31
permalink: /blog/ai-papers/2026/03/daily-ai-papers-03-31/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-systems
  - multimodal-models
  - reasoning-models
---

Top 20 trending AI papers from the past 48 hours, ranked by community attention.

## How This Report Is Built

**Sources crawled (in order of signal strength):**
1. **HuggingFace Trending Papers** (huggingface.co/papers) -- community upvotes from researchers and practitioners. Primary ranking signal.
2. **HuggingFace Daily Papers** (huggingface.co/papers?date=YYYY-MM-DD) -- papers from the past 2-3 days to catch ones still gaining traction.
3. **Company blogs and model hubs** -- Allen AI blog, EpochX blog, AMD ROCm blog, HuggingFace model releases.
4. **Web search** -- picks up major lab announcements, social media buzz, and cross-platform discussion.
5. **arxiv recent listings** (arxiv.org/list/cs.CL/current, cs.LG, cs.AI, cs.CV) -- raw new submissions for coverage.

**Ranking criteria:**
- Position on HuggingFace trending (highest weight)
- Cross-source appearance (paper trending on multiple platforms ranks higher)
- Lab/company prestige (major lab releases get boosted)
- Relevance to current hot topics (agents, reasoning, efficiency, safety, video generation)

---

## 1. TAPS: Task Aware Proposal Distributions for Speculative Sampling
**Authors:** Mohamad Zbib, Mohamad Bazzi, Ammar Mohanna, Hasan Abed Al Kader Hammoud, Bernard Ghanem
**Summary:** Studies how the draft model's training distribution affects speculative decoding quality. Lightweight HASS and EAGLE-2 drafters trained on domain-specific data (MathInstruct, ShareGPT) significantly outperform generic drafters. Shows that task-aware proposal distributions can meaningfully improve speculative sampling without changing the target model.
**Link:** [arxiv.org/abs/2603.27027](https://arxiv.org/abs/2603.27027)
**Source:** HuggingFace trending (#1 on Mar 31)
**Why trending:** Speculative decoding is a key inference optimization. This paper shows a simple, actionable insight: match your drafter to your task for better acceptance rates.

## 2. Towards a Medical AI Scientist
**Authors:** Hongtao Wu, Boyun Zheng, Dingjie Song, Yu Jiang, Jianfeng Gao et al.
**Summary:** First autonomous research framework tailored to clinical medicine. Unlike domain-agnostic AI Scientist systems, this one is grounded in medical evidence and handles specialized data modalities. End-to-end pipeline from hypothesis generation to manuscript drafting for medical research.
**Link:** [arxiv.org/abs/2603.28589](https://arxiv.org/abs/2603.28589)
**Source:** HuggingFace trending (#2 on Mar 31), arxiv cs.AI
**Why trending:** AI Scientist papers are hot, and this is the first one specialized for medicine. Jianfeng Gao (Microsoft Research) is a co-author.

## 3. Gen-Searcher: Reinforcing Agentic Search for Image Generation
**Authors:** Kaituo Feng, Manyuan Zhang, Shuang Chen, Yunlong Lin, Kaixuan Fan et al.
**Summary:** First attempt to train a search-augmented image generation agent. Performs multi-hop reasoning and web search to collect textual knowledge needed for knowledge-intensive prompts that stump frozen image generation models. Uses RL to train the search agent.
**Link:** [arxiv.org/abs/2603.28767](https://arxiv.org/abs/2603.28767)
**Source:** HuggingFace trending (#3 on Mar 31), related to Search-o1 line of work
**Why trending:** Novel intersection of retrieval-augmented generation and image synthesis. Addresses the fundamental limitation of frozen knowledge in image models.

## 4. Emergent Social Intelligence Risks in Generative Multi-Agent Systems
**Authors:** Yue Huang, Yu Jiang, Wenjie Wang, Haomin Zhuang, Xiaonan Luo et al.
**Summary:** Pioneer study of failure modes that emerge when multiple generative agents interact -- risks that cannot be reduced to individual agent behavior. Studies negotiation, resource allocation, and planning in multi-agent systems. Identifies collective failure patterns unique to multi-agent settings.
**Link:** [arxiv.org/abs/2603.27771](https://arxiv.org/abs/2603.27771)
**Source:** HuggingFace trending (#4 on Mar 31), arxiv cs.AI
**Why trending:** Multi-agent safety is under-studied compared to single-agent alignment. Timely as agent deployments scale.

## 5. EpochX: Building Infrastructure for Emergent Agent Civilization
**Authors:** Huacan Wang, Chaofa Yuan, Xialie Zhuang, Tu Hu, Shuo Zhang et al.
**Summary:** A credits-native marketplace infrastructure for human-agent production. Argues the binding constraint has shifted from raw AI capability to how work is delegated, verified, and rewarded at scale. Builds infrastructure for agent-to-agent and human-to-agent economic coordination.
**Link:** [arxiv.org/abs/2603.27304](https://arxiv.org/abs/2603.27304)
**Source:** HuggingFace trending (#5 on Mar 31), project website (epochx.cc), blog post (epochx.cc/blog)
**Why trending:** Bold vision paper with working infrastructure. Agent marketplaces are an emerging category.

## 6. GEditBench v2: A Human-Aligned Benchmark for General Image Editing
**Authors:** Zhangqi Jiang, Zheng Sun, Xianfang Zeng, Yufeng Yang, Xuanyang Zhang et al.
**Summary:** Comprehensive benchmark with 1,200 real-world image editing tasks spanning six core tasks. Current benchmarks suffer from narrow task coverage and metrics that fail to capture visual consistency. GEditBench v2 provides human-aligned evaluation across generation, editing, single and multiple references.
**Link:** [arxiv.org/abs/2603.28547](https://arxiv.org/abs/2603.28547)
**Source:** HuggingFace trending (#6 on Mar 31), arxiv cs.CV
**Why trending:** Image editing benchmarks are crucial as editing models mature rapidly. Fills a clear evaluation gap.

## 7. Kernel-Smith: A Unified Recipe for Evolutionary Kernel Optimization
**Authors:** He Du, Qiming Ge, Jiakai Hu, Aijun Yang, Zheng Cai et al.
**Summary:** Framework for high-performance GPU kernel generation combining evolutionary search agents with post-training recipes. Maintains a population of executable kernel candidates and iteratively improves them using execution feedback on compilation, correctness, and speedup. Practical tool for GPU optimization.
**Link:** [arxiv.org/abs/2603.28342](https://arxiv.org/abs/2603.28342)
**Source:** HuggingFace trending (#13 on Mar 31), alphaxiv.org, AMD ROCm blog discusses related GEAK-Triton agents
**Why trending:** GPU kernel optimization is a bottleneck for AI infrastructure teams. Evolutionary agent approach is novel and practical. Cross-platform discussion.

## 8. On Token's Dilemma: Dynamic MoE with Drift-Aware Token Assignment for Continual Learning
**Authors:** Chongyang Zhao, Mingsong Li, Haodong Lu, Dong Gong
**Summary:** Addresses forgetting in MoE-based continual learning of large vision-language models. Identifies "routing-drift" as the root cause: old-task tokens get misassigned as new experts are added. Proposes drift-aware token assignment to maintain routing consistency across tasks.
**Link:** [arxiv.org/abs/2603.27481](https://arxiv.org/abs/2603.27481)
**Source:** HuggingFace trending (#7 on Mar 31), arxiv cs.CV
**Why trending:** MoE architectures are everywhere now. Understanding and fixing their failure modes in continual learning is immediately relevant.

## 9. PRBench: End-to-end Paper Reproduction in Physics Research
**Authors:** Shi Qiu, Junyi Deng, Yiwei Deng, Haoran Dong, Jieyu Fu et al.
**Summary:** Benchmark of 30 expert-curated tasks spanning 11 subfields of physics, testing whether AI agents can reliably perform end-to-end reproduction from real scientific papers. Each task requires comprehending methodology and producing verifiable results.
**Link:** [arxiv.org/abs/2603.27646](https://arxiv.org/abs/2603.27646)
**Source:** HuggingFace trending (#8 on Mar 31), arxiv cs.AI
**Why trending:** Scientific reproducibility is a key test for AI agents. Physics provides hard, verifiable ground truth.

## 10. Make Geometry Matter for Spatial Reasoning
**Authors:** Shihua Zhang, Qiuhong Shen, Shizun Wang, Tianbo Pan, Xinchao Wang
**Summary:** Shows that naively fusing geometry tokens from 3D foundation models into VLMs via standard fine-tuning leaves geometric cues underutilized. Proposes methods to make geometry information actually matter for spatial reasoning in both static scenes and dynamic videos.
**Link:** [arxiv.org/abs/2603.26639](https://arxiv.org/abs/2603.26639)
**Source:** HuggingFace trending (#9 on Mar 31), arxiv cs.CV
**Why trending:** Spatial reasoning is a known weakness of VLMs. This paper provides a concrete diagnosis and fix.

## 11. MolmoPoint: Better Pointing for VLMs with Grounding Tokens
**Authors:** Christopher Clark, Yue Yang, Jae Sung Park, Zixian Ma, Jieyu Zhang et al. (Allen AI)
**Summary:** Instead of generating coordinates as text (which requires learning a complex coordinate system), proposes pointing tokens that directly select visual tokens containing the target concept via cross-attention. More intuitive and efficient grounding mechanism for VLMs. Models released on HuggingFace.
**Link:** [arxiv.org/abs/2603.28069](https://arxiv.org/abs/2603.28069)
**Source:** HuggingFace trending (Mar 31), Allen AI blog (allenai.org/blog/molmopoint), HF model releases (MolmoPoint-8B, MolmoPoint-Vid-4B)
**Why trending:** Allen AI release with open models. Fundamentally simpler approach to visual grounding that outperforms coordinate-based methods.

## 12. On-the-fly Repulsion in the Contextual Space for Rich Diversity in Diffusion Transformers
**Authors:** Omer Dahary, Benaya Koren, Daniel Garibi, Daniel Cohen-Or
**Summary:** Modern T2I diffusion models achieve great semantic alignment but converge on narrow visual solutions -- "typicality bias." Identifies a fundamental trade-off in current diversity approaches and proposes on-the-fly repulsion in contextual space to generate diverse outputs without costly optimization.
**Link:** [arxiv.org/abs/2603.28762](https://arxiv.org/abs/2603.28762)
**Source:** HuggingFace trending (#10 on Mar 31), arxiv cs.CV
**Why trending:** Addresses a real pain point in production image generation: every prompt gives the same-looking output. Clean solution.

## 13. MuSEAgent: A Multimodal Reasoning Agent with Stateful Experiences
**Authors:** Shijian Wang, Jiarui Jin, Runhao Fu, Zexuan Yan, Xingjian Wang et al.
**Summary:** Extends research agents beyond trajectory-level retrieval by proposing a stateful experience learning paradigm. Abstracts interaction data into atomic decision patterns that can be retrieved and applied across different reasoning contexts, enhancing multimodal decision-making.
**Link:** [arxiv.org/abs/2603.27813](https://arxiv.org/abs/2603.27813)
**Source:** HuggingFace trending (#12 on Mar 31), arxiv cs.AI
**Why trending:** Agent memory and experience accumulation is a key unsolved problem. Stateful experiences is a compelling abstraction.

## 14. Marco DeepResearch: Unlocking Efficient Deep Research Agents via Verification-Centric Design
**Authors:** Bin Zhu, Qianghuai Jia, Tian Lan, Junyang Ren, Feng Gu et al.
**Summary:** Deep research agents fail on long-horizon tasks because they lack explicit verification during data synthesis, trajectory construction, and test-time scaling. Proposes verification-centric design that catches errors early rather than compounding them through multi-step reasoning chains.
**Link:** [arxiv.org/abs/2603.28376](https://arxiv.org/abs/2603.28376)
**Source:** HuggingFace trending (#15 on Mar 31), HuggingFace DeepResearch Bench Leaderboard space, blog discussion (fuchsfranklin.github.io)
**Why trending:** Deep research is a hot capability. Verification is the key missing piece -- this paper addresses it directly. Cross-platform discussion.

## 15. ImagenWorld: Stress-Testing Image Generation Models with Explainable Human Evaluation
**Authors:** Samin Mahdizadeh Sani, Max Ku, Nima Jamali, Matina Mahdizadeh Sani et al.
**Summary:** Benchmark of 3,600 condition sets spanning six core image generation/editing tasks. Unlike existing benchmarks that give opaque scores, ImagenWorld explains failure modes. Covers generation, editing, single/multiple references with human-aligned evaluation.
**Link:** [arxiv.org/abs/2603.27862](https://arxiv.org/abs/2603.27862)
**Source:** HuggingFace trending (#11 on Mar 31), arxiv cs.CV
**Why trending:** Explainable evaluation for image generation is sorely needed. 3.6K conditions across six tasks is comprehensive.

## 16. HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention
**Authors:** Yufei Xu, Fanxu Meng, Fan Jiang, Yuxuan Wang, Ruijie Zhou et al.
**Summary:** Token-level sparse attention (like DeepSeek Sparse Attention) achieves fine-grained key selection but the indexer still scans the entire prefix for every query -- O(L^2) bottleneck. HISA proposes hierarchical indexing that eliminates this bottleneck while maintaining selection quality.
**Link:** [arxiv.org/abs/2603.28458](https://arxiv.org/abs/2603.28458)
**Source:** HuggingFace trending (Mar 31), arxiv cs.CL
**Why trending:** Directly extends DeepSeek's sparse attention architecture. Addresses a concrete O(L^2) bottleneck that limits long-context scaling.

## 17. ResAdapt: Adaptive Resolution for Efficient Multimodal Reasoning
**Authors:** Huanxuan Liao, Zhongtao Jiang, Yupu Hao, Yuqiao Tan, Shizhu He et al.
**Summary:** MLLMs scale visual understanding by increasing input fidelity, but visual token growth makes high resolution + long temporal context prohibitive. ResAdapt learns how much visual budget each frame needs, adapting resolution at the input side rather than compressing post-encoding representations.
**Link:** [arxiv.org/abs/2603.28610](https://arxiv.org/abs/2603.28610)
**Source:** HuggingFace trending (#14 on Mar 31), arxiv cs.CV
**Why trending:** Practical efficiency gain for multimodal models. Input-side adaptation is a cleaner approach than post-hoc compression.

## 18. DreamLite: A Lightweight On-Device Unified Model for Image Generation and Editing
**Authors:** Kailai Feng, Yuxiang Wei, Bo Chen, Yang Pan, Hu Ye et al.
**Summary:** Compact 0.39B parameter diffusion model that supports both text-to-image generation and text-guided image editing on-device. Existing on-device models focus only on generation. DreamLite unifies both capabilities in a single lightweight model.
**Link:** [arxiv.org/abs/2603.28713](https://arxiv.org/abs/2603.28713)
**Source:** HuggingFace trending (#16 on Mar 31), arxiv cs.CV
**Why trending:** On-device AI is growing fast. A unified generation + editing model at 0.39B parameters is immediately practical for mobile deployment.

## 19. KAT-Coder-V2 Technical Report
**Authors:** Fengxiang Li, Han Zhang, Haoyang Huang, Jinghui Wang et al. (Kuaishou KwaiKAT Team)
**Summary:** Agentic coding model using a "Specialize-then-Unify" paradigm: decomposes coding into five expert domains (SWE, WebCoding, Terminal, WebSearch, General), each with independent SFT and RL, before consolidation via on-policy distillation. Built KwaiEnv infrastructure sustaining tens of thousands of concurrent environments.
**Link:** [arxiv.org/abs/2603.27703](https://arxiv.org/abs/2603.27703)
**Source:** HuggingFace trending (Mar 31), arxiv cs.SE
**Why trending:** Major company (Kuaishou) release. Novel multi-domain expert approach to agentic coding. KwaiEnv infrastructure is a notable engineering contribution.

## 20. HandX: Scaling Bimanual Motion and Interaction Generation
**Authors:** Zimu Zhang, Yucheng Zhang, Xiyan Xu, Ziyin Wang, Sirui Xu et al.
**Summary:** Synthesizing realistic hand motion and bimanual interaction remains underexplored. HandX provides a unified foundation spanning data, annotation, and evaluation for dexterous bimanual behavior -- finger articulation, contact timing, and inter-hand coordination.
**Link:** [arxiv.org/abs/2603.28766](https://arxiv.org/abs/2603.28766)
**Source:** HuggingFace trending (#18 on Mar 31), arxiv cs.CV
**Why trending:** Fills a clear gap in motion generation research. Hand/finger motion is one of the hardest unsolved problems in character animation.

---

## Honorable Mentions

Papers that didn't make the top 20 but are worth watching:

- **Story2Proposal** (2603.27065) -- Contract-governed multi-agent framework for scientific manuscript generation
- **Density-aware Soft Context Compression** (2603.25926) -- Dynamic compression ratios for long-context LLMs
- **SEAR** (2603.26728) -- Schema-based evaluation and routing for LLM gateways
- **AdaptToken** (2603.28696) -- Entropy-based adaptive token selection for long video understanding
- **Superintelligence and Law** (2603.28669) -- Legal analysis of AI superintelligence implications
- **MOOZY** (2603.27048) -- Patient-first foundation model for computational pathology
- **Surgical AI Comparative Study** (2603.27341) -- Datasets, foundation models, and barriers to Med-AGI

---

## Methodology

| Source | URL | Signal | Papers Found |
|--------|-----|--------|-------------|
| HuggingFace Trending | huggingface.co/papers | Community upvotes (primary ranking signal) | 30 papers |
| HuggingFace Daily (Mar 31) | huggingface.co/papers?date=2026-03-31 | Papers from today | 30 papers (same as trending) |
| HuggingFace Daily (Mar 30) | huggingface.co/papers?date=2026-03-30 | Papers still gaining traction | 15 papers |
| Allen AI Blog | allenai.org/blog/molmopoint | Lab announcement | MolmoPoint release + open models |
| EpochX Blog | epochx.cc/blog | Project announcement | EpochX infrastructure paper |
| AMD ROCm Blog | rocm.blogs.amd.com | Related work | GEAK-Triton agent (related to Kernel-Smith) |
| alphaxiv.org | alphaxiv.org | Cross-platform discussion | Kernel-Smith discussion |
| HF DeepResearch Bench | huggingface.co/spaces/muset-ai | Leaderboard | Marco DeepResearch context |
| Web search (Reddit, X, HN) | Various | Social media buzz | Limited direct results; cross-referenced topics |
| arxiv cs.CL/LG/AI/CV | arxiv.org/list/ | Raw submissions | Used for abstract retrieval |

Papers are ranked by: HuggingFace position > cross-platform presence > lab prestige > topic relevance.

*Generated by Jarvis | Next report: April 1, 2026 at 10:00 AM PT*
