---
title: "Daily AI Papers — May 28, 2026"
date: 2026-05-28
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-28/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multi-agent
  - reinforcement-learning
  - agentic-reasoning
---

## 1. Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

**Authors:** Fangfu Liu, Kai He, Tianchang Shen, Tianshi Cao, Sanja Fidler, Yueqi Duan, Jun Gao, Igor Gilitschenski, Zian Wang, Xuanchi Ren
**arXiv:** [arxiv.org/abs/2605.28816](https://arxiv.org/abs/2605.28816)

**Summary:** World models for interactive video generation have largely focused on single-agent settings, but many real-world environments require multiple agents acting simultaneously. Gamma-World introduces a principled multi-agent design where agents remain independently controllable, permutation-symmetric, and support efficient inference while maintaining consistency across time and perspectives.

**Why trending:** Top-ranked paper on HuggingFace today with 154 upvotes; extends world models from single/two-player to arbitrary multi-agent settings — a key open challenge in embodied AI and game simulation.

**Sources:** HuggingFace Daily Papers (#1, 154 upvotes), arXiv

---

## 2. ProRL: Effective Reinforcement Learning for Proactive Recommendation via Rectified Policy Gradient Estimation

**Authors:** Hongru Hou, Tiehua Mei, Denghui Geng, Jinhui Huang
**arXiv:** [arxiv.org/abs/2605.28293](https://arxiv.org/abs/2605.28293)

**Summary:** Proactive Recommender Systems aim to guide user preference shift toward target items via sequential intermediate recommendations. ProRL applies rectified policy gradient estimation to resolve the instability of naively applying RL to this sequential decision problem, capturing both short-term acceptance and long-term guidance.

**Why trending:** Strong community interest in applying RL to recommendation beyond bandit settings; bridges RL theory and practical recommender system deployment.

**Sources:** HuggingFace Daily Papers (75 upvotes), arXiv

---

## 3. Agent Explorative Policy Optimization for Multimodal Agentic Reasoning (AEPO)

**Authors:** Minki Kang, Shizhe Diao, Ryo Hachiuma, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2605.28774](https://arxiv.org/abs/2605.28774)

**Summary:** Vision-language models with extended reasoning succeed on complex problems but struggle when external tools are needed. AEPO addresses the structural asymmetry between internal thinking and high-variance tool use by introducing exploration-driven policy optimization that balances the two behaviors in agentic reasoning.

**Why trending:** Directly tackles the tool-use vs. reasoning asymmetry problem central to building reliable multimodal agents — highly relevant as tool-augmented LLMs proliferate.

**Sources:** HuggingFace Daily Papers (67 upvotes), arXiv

---

## 4. From Pixels to Words — Towards Native One-Vision Models at Scale

**Authors:** Haiwen Diao, Jiahao Wang, Penghao Wu, Yuhao Dong
**arXiv:** [arxiv.org/abs/2605.28820](https://arxiv.org/abs/2605.28820)

**Summary:** Current VLMs stitch separate image encoders and language decoders via multi-stage alignment, fragmenting pixel-level signals across frames. This paper proposes native one-vision models that integrate pixel-word processing from the ground up, scaling to multi-image and video understanding tasks.

**Why trending:** Challenges the dominant encoder-decoder paradigm for VLMs; native architectures for vision-language are a hot research direction following similar work in multimodal foundation models.

**Sources:** HuggingFace Daily Papers (52 upvotes), arXiv

---

## 5. Self-Improving Language Models with Bidirectional Evolutionary Search

**Authors:** Guowei Xu, Zhenting Qi, Huangyuan Su, Weirui Ye
**arXiv:** [arxiv.org/abs/2605.28814](https://arxiv.org/abs/2605.28814)

**Summary:** Best-of-N sampling and tree search for self-improving LLMs suffer from sparse verification signals and purely autoregressive candidate construction. This work proposes bidirectional evolutionary search that generates candidates through both forward expansion and backward refinement, guided by dense verification signals.

**Why trending:** Self-improvement without human labels is a central challenge in scaling LLMs; the bidirectional search framing offers a novel alternative to tree search methods like MCTS.

**Sources:** HuggingFace Daily Papers (43 upvotes), arXiv

---

## 6. DenoiseRL: Bootstrapping Reasoning Models to Recover from Noisy Prefixes

**Authors:** Caijun Xu, Changyi Xiao, Zhongyuan Peng, Yixin Cao
**arXiv:** [arxiv.org/abs/2605.28421](https://arxiv.org/abs/2605.28421)

**Summary:** Most RL-based reasoning methods require stronger teacher models or curated datasets. DenoiseRL replaces external supervision with recovery-oriented optimization — training models to reason through corrupted or noisy prefixes — enabling scalable self-improvement without teacher dependency.

**Why trending:** Addresses the scalability bottleneck of RL-based reasoning improvement; the recovery-from-noise framing is a creative alternative to standard RLHF/RLAIF pipelines.

**Sources:** HuggingFace Daily Papers (39 upvotes), arXiv

---

## 7. ResearchMath-14K: Scaling Research-Level Mathematics via Agents

**Authors:** Guijin Son, Seungyeop Yi, Minju Gwak, Hyunwoo Ko
**arXiv:** [arxiv.org/abs/2605.28003](https://arxiv.org/abs/2605.28003)

**Summary:** The frontier of mathematics consists of unsolved problems, yet no large-scale dataset exists for this regime. ResearchMath-14K introduces 14,056 problems curated from academic sources via a multi-agent framework, investigating whether LLMs can meaningfully engage with frontier mathematics without human intervention.

**Why trending:** Benchmarking LLMs on genuinely unsolved math is a frontier problem; this dataset fills a critical gap above competition math benchmarks like AIME and IMO.

**Sources:** HuggingFace Daily Papers (36 upvotes), arXiv

---

## 8. MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems

**Authors:** Xinle Deng, Ruobin Zhong, Hujin Peng, Xiaoben Lu
**arXiv:** [arxiv.org/abs/2605.28732](https://arxiv.org/abs/2605.28732)

**Summary:** Memory systems for LLMs enable long-horizon reasoning but remain unreliable and opaque. MemTrace studies the new problem of error tracing and attribution in LLM memory, proposing methods to understand how information is synthesized, propagated, or corrupted dynamically over time.

**Why trending:** As LLM agent memory systems grow more complex, debugging and attribution become critical engineering challenges; this is one of the first systematic studies of the problem.

**Sources:** HuggingFace Daily Papers (33 upvotes), arXiv

---

## 9. GEM: Generative Supervision Helps Embodied Intelligence

**Authors:** Ruowen Zhao, Bangguo Li, Zuyan Liu, Yinan Liang
**arXiv:** [arxiv.org/abs/2605.28548](https://arxiv.org/abs/2605.28548)

**Summary:** Embodied VLMs excel at semantic tasks but lack the low-level spatial and physical knowledge needed for real robot execution. GEM introduces generative supervision signals to bridge this gap within Vision-Language-Action frameworks, improving both planning quality and physical grounding.

**Why trending:** Robotics + VLM integration is one of the hottest areas; GEM directly addresses the semantic-physical gap that limits current VLA models in real-world deployment.

**Sources:** HuggingFace Daily Papers (33 upvotes), arXiv

---

## 10. Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use Agents

**Authors:** Suji Kim, Kangsan Kim, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2605.28775](https://arxiv.org/abs/2605.28775)

**Summary:** Large computer-use agents excel but are too expensive to deploy per-domain. This paper automates domain specialization for small open agents by identifying domain-specific failures and synthesizing targeted training data, making small agents competitive without requiring large per-domain experts.

**Why trending:** Practical path to deploying capable computer-use agents at low cost; automated specialization addresses the scalability problem in enterprise AI deployment.

**Sources:** HuggingFace Daily Papers (32 upvotes), arXiv

---

## 11. ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence

**Authors:** Rui Meng, Bhavana Dalvi Mishra, Jiefeng Chen, Chun-Liang Li
**arXiv:** [arxiv.org/abs/2605.26340](https://arxiv.org/abs/2605.26340)

**Summary:** Autonomous research agents produce impressive-looking outputs but contain verifiability failures: fabricated citations, unreproducible scores, and implementation/description divergence. ScientistOne introduces Chain-of-Evidence (CoE), a verifiability framework that audits research agent outputs beyond surface-level metrics.

**Why trending:** AI scientist agents are proliferating rapidly, and trust/verifiability is the key open question; CoE offers a concrete evaluation framework.

**Sources:** HuggingFace Daily Papers (25 upvotes), arXiv

---

## 12. AI Research Agents Narrow Scientific Exploration

**Authors:** Yixuan Tang, Yi Yang
**arXiv:** [arxiv.org/abs/2605.27905](https://arxiv.org/abs/2605.27905)

**Summary:** AI research agents can generate ideas, run experiments, and draft papers, but this paper finds they tend to concentrate exploration around existing popular ideas rather than broadening the frontier. The study raises important questions about whether AI-assisted ideation homogenizes or diversifies scientific discovery.

**Why trending:** Provocative finding with direct implications for how AI is used in research; the "narrowing" effect echoes concerns about algorithmic echo chambers in scientific ideation.

**Sources:** HuggingFace Daily Papers (20 upvotes), arXiv

---

## 13. Rethinking Memory as Continuously Evolving Connectivity (FluxMem)

**Authors:** Jizhan Fang, Buqiang Xu, Zhixian Wang, Haoliang Cao
**arXiv:** [arxiv.org/abs/2605.28773](https://arxiv.org/abs/2605.28773)

**Summary:** Existing memory-augmented LLM agents treat memory as a static repository with fixed retrieval pipelines, which is brittle in dynamic agentic environments. FluxMem proposes a connectivity-evolving memory system where representations and connections adapt continuously based on feedback and task variation.

**Why trending:** Dynamic memory is a fundamental challenge for long-lived agents; the graph-connectivity framing is a compelling departure from static vector store approaches.

**Sources:** HuggingFace Daily Papers (18 upvotes), arXiv

---

## 14. Triplet-Block Diffusion RWKV

**Authors:** Ke Lin, Yiyang Luo, Zhaolong Su, Yunya Song
**arXiv:** [arxiv.org/abs/2605.25969](https://arxiv.org/abs/2605.25969)

**Summary:** Causal Transformers have quadratic attention cost, while diffusion models require bidirectional attention incompatible with causal models. B³D-RWKV unifies both architectures in a triplet-block design that enables efficient parallel decoding while retaining the quality benefits of discrete diffusion.

**Why trending:** Efficient architecture design combining RWKV's linear complexity with diffusion-style generation is a novel approach to the inference efficiency problem.

**Sources:** HuggingFace Daily Papers (17 upvotes), arXiv

---

## 15. OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and RL

**Authors:** Yunyang Ge, Xianyi He, Zezhong Zhang, Bin Lin
**arXiv:** [arxiv.org/abs/2605.28691](https://arxiv.org/abs/2605.28691)

**Summary:** Diffusion Transformers produce high-quality video but suffer from quadratic attention cost. OSP-Next integrates hybrid full-sparse attention, sequence parallelism, HiF8 quantization, and reinforcement learning fine-tuning to achieve efficient high-quality text-to-video generation at scale.

**Why trending:** Video generation efficiency is critical for practical deployment; the combination of sparse attention + quantization + RL fine-tuning represents a comprehensive systems approach.

**Sources:** HuggingFace Daily Papers (16 upvotes), arXiv

---

## 16. Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization

**Authors:** Hao Jiang, Shurui Li, Tianpeng Bu, Bowen Xu
**arXiv:** [arxiv.org/abs/2605.28109](https://arxiv.org/abs/2605.28109)

**Summary:** Online RL for LLMs often exhibits imbalanced exploration-exploitation, leading to unstable optimization. IB-Score uses Information Bottleneck theory to quantify this imbalance and guides tree-based policy optimization to maintain a stable balance throughout training.

**Why trending:** Principled approach to a persistent instability problem in LLM RL training; Information Bottleneck theory offers rigorous grounding for what has been a heuristic practice.

**Sources:** HuggingFace Daily Papers (16 upvotes), arXiv

---

## 17. Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving

**Authors:** Kewei Zhang, Jin Wang, Sensen Gao, Chengyue Wu
**arXiv:** [arxiv.org/abs/2605.23163](https://arxiv.org/abs/2605.23163)

**Summary:** End-to-end autonomous driving via VLA models requires balancing trajectory quality and inference efficiency. Fast-dDrive uses block diffusion to avoid the memory-bandwidth bottleneck of AR-VLAs and the KV-cache issues of full-sequence diffusion, enabling edge-deployable autonomous driving models.

**Why trending:** Autonomous driving is a high-stakes application of VLA models; the edge inference efficiency angle is directly relevant to real deployment constraints.

**Sources:** HuggingFace Daily Papers (15 upvotes), arXiv

---

## 18. GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation

**Authors:** Boxiang Qiu, Liliang Chen, Yue Liao, Nan Wang
**arXiv:** [arxiv.org/abs/2605.27491](https://arxiv.org/abs/2605.27491)

**Summary:** GE-Sim 2.0 is a closed-loop video world simulator for robotic manipulation trained on thousands of hours of real-world robot data including teleoperation, contact-rich interaction, and on-robot policy deployment. It advances the Genie Envisioner framework toward comprehensive simulation fidelity for robot learning.

**Why trending:** World simulators for robot learning are essential for scaling data collection; real-robot training data at this scale is rare and impactful.

**Sources:** HuggingFace Daily Papers (13 upvotes), arXiv

---

## 19. SAERL: Guiding LLM Post-training Data Engineering with Model Internals from Sparse Autoencoders

**Authors:** Yi Jing, Zao Dai, Jinwu Hu, Zijun Yao
**arXiv:** [arxiv.org/abs/2605.27354](https://arxiv.org/abs/2605.27354)

**Summary:** Post-training data engineering for LLM RL typically relies on external signals while ignoring rich intrinsic model signals. SAERL uses sparse autoencoders to surface model internals — diversity, difficulty, and alignment — as explicit signals to guide RL data selection and curation.

**Why trending:** Sparse autoencoders (SAEs) are a rapidly growing interpretability tool; applying them to guide training data selection is an elegant bridge between interpretability and training efficiency.

**Sources:** HuggingFace Daily Papers (12 upvotes), arXiv

---

## 20. LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

**Authors:** HuiMing Fan, Xiao Wang, Zheng Chu, Qianyu Wang
**arXiv:** [arxiv.org/abs/2605.28721](https://arxiv.org/abs/2605.28721)

**Summary:** This paper studies whether LLM-based search agents genuinely retrieve new information or use web search to confirm pre-existing parametric knowledge. Three diagnostic methods reveal Intrinsic Knowledge Dependence (IKD) — agents answer up to X% of queries from internal knowledge even with full web access.

**Why trending:** Fundamental question for evaluating search-augmented agents; IKD challenges the assumption that tool access = genuine retrieval, with implications for RAG evaluation.

**Sources:** HuggingFace Daily Papers (11 upvotes), arXiv
