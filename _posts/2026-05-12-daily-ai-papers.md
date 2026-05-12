---
title: "Daily AI Papers — May 12, 2026"
date: 2026-05-12
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-12/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-safety
  - reasoning
  - model-efficiency
---

## 1. A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language Models

**Authors:** Hamid Kazemi, Atoosa Chegini, Maria Safi

**Summary:** Safety alignment operates through two mechanistically distinct systems: refusal neurons (gating expression of harmful knowledge) and concept neurons (encoding the harmful knowledge). By targeting a single neuron in each system, the authors demonstrate both directions of failure — bypassing safety on harmful requests via suppression, and inducing harmful content from innocent prompts via amplification — across seven models (1.7B–70B), without any training or prompt engineering.

**arXiv:** [arxiv.org/abs/2605.08513](https://arxiv.org/abs/2605.08513)

**Sources:** HuggingFace Daily Papers, Reddit r/MachineLearning, AlphaXiv

**Why trending:** Explosive finding that a single neuron can break alignment in models up to 70B; challenges the robustness of RLHF-based safety and will likely catalyze a wave of follow-up defense research.

---

## 2. Qwen-Image-2.0 Technical Report

**Authors:** Bing Zhao, Chenfei Wu, Deqing Li, Hao Meng, Jiahao Li, Jie Zhang, Jingren Zhou, Junyang Lin et al.

**Summary:** Qwen-Image-2.0 is an omni-capable image generation foundation model that unifies high-fidelity generation and precise image editing in a single framework, coupling Qwen3-VL as the condition encoder with a Multimodal Diffusion Transformer. It addresses ultra-long text rendering, multilingual typography, high-resolution photorealism, and robust instruction following in text-rich and compositionally complex scenarios.

**arXiv:** [arxiv.org/abs/2605.10730](https://arxiv.org/abs/2605.10730)

**Sources:** HuggingFace Daily Papers, arXiv, GitHub (QwenLM)

**Why trending:** Major release from Alibaba's Qwen team — the GitHub repo and associated demo are already circulating widely; positions Qwen squarely against FLUX and SD3.

---

## 3. Soohak: A Mathematician-Curated Benchmark for Evaluating Research-Level Math Capabilities of LLMs

**Authors:** Guijin Son, Seungone Kim, Catherine Arnett, Hyunwoo Ko, Hyein Lee

**Summary:** Following frontier LLMs achieving IMO gold-medal performance, the community seeks the next meaningful target. Soohak is curated by professional mathematicians and targets research-level problem-solving — problems that require not just step-by-step reasoning but advancing mathematical knowledge itself — providing a compelling post-olympiad evaluation frontier.

**arXiv:** [arxiv.org/abs/2605.09063](https://arxiv.org/abs/2605.09063)

**Sources:** HuggingFace Daily Papers, Reddit r/MachineLearning, arXiv cs.AI

**Why trending:** Directly answers "what's next after IMO?" — a question the AI reasoning community has been debating loudly, making this an instant reference benchmark.

---

## 4. WorldReasonBench: Human-Aligned Stress Testing of Video Generators as Future World-State Predictors

**Authors:** Keming Wu, Yijing Cui, Wenhan Xue, Qijie Wang, Xuan Luo

**Summary:** WorldReasonBench reframes video generation evaluation as world-state prediction, testing models like Seedance2.0 and Veo3.1 on whether they can reason about how an observed scene should evolve over time. It provides human-aligned stress tests beyond visual quality, directly probing temporal causal reasoning capabilities of video generators.

**arXiv:** [arxiv.org/abs/2605.10434](https://arxiv.org/abs/2605.10434)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV, AlphaXiv

**Why trending:** Commercial video generation is a hot space (Sora, Veo, Seedance all competing); this benchmark arrives at exactly the right moment to standardize how "world simulator" claims are evaluated.

---

## 5. TMAS: Scaling Test-Time Compute via Multi-Agent Synergy

**Authors:** George Wu, Nan Jing, Qing Yi, Chuan Hao, Ming Yang

**Summary:** TMAS organizes inference across multiple agents with distinct roles (generation, refinement, verification) to scale test-time compute more effectively than single-trajectory or chain-of-thought approaches. The multi-agent synergy framework achieves better reasoning performance by exploiting structured collaboration during inference rather than solely scaling model parameters.

**arXiv:** [arxiv.org/abs/2605.10344](https://arxiv.org/abs/2605.10344)

**Sources:** HuggingFace Daily Papers, arXiv cs.AI, DeepLearn.org

**Why trending:** Test-time scaling is among the hottest active research directions; multi-agent synergy is a natural extension that practitioners can deploy today.

---

## 6. G-Zero: Self-Play for Open-Ended Generation from Zero Data

**Authors:** Chengsong Huang, Haolin Liu, Tong Zheng, Runpeng Dai, Langlin Huang

**Summary:** G-Zero introduces a verifier-free, co-evolutionary framework for autonomous LLM self-improvement in open-ended tasks. Its core innovation, Hint-δ, is an intrinsic reward that measures the predictive shift between a Generator model's output before and after seeing a hint — sidestepping the need for proxy LLM judges that create capability bottlenecks and reward hacking.

**arXiv:** [arxiv.org/abs/2605.09959](https://arxiv.org/abs/2605.09959)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG, Reddit r/MachineLearning

**Why trending:** Addresses the central unsolved problem of self-improvement without a strong external judge — eliminates a key dependency that limits scaling self-play to open-ended domains.

---

## 7. Geometry Conflict: Explaining and Controlling Forgetting in LLM Continual Post-Training

**Authors:** Yuanyi Wang, Yifan Yang, Su Lu, Yanggan Gu, Pengkai Wang

**Summary:** This paper introduces "geometry conflict" as a mechanistic explanation for catastrophic forgetting in sequential LLM fine-tuning: conflicting gradient geometries between old and new tasks corrupt prior representations. The framework provides criteria for when sequential updates enable capability transfer versus forgetting, enabling principled continual post-training without heuristic replay.

**arXiv:** [arxiv.org/abs/2605.09608](https://arxiv.org/abs/2605.09608)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** Continual learning for LLMs is a critical practical need; providing a clean geometric explanation (rather than heuristic fixes) is intellectually compelling and actionable.

---

## 8. Model Merging Scaling Laws in Large Language Models

**Authors:** Yuanyi Wang, Yanggan Gu, Yiming Zhang, Qi Zhou, Zhaoyi Yan

**Summary:** The authors identify a compact power law relating model size and number of merged experts to cross-entropy: the size-dependent floor decreases with model capacity while the merging tail shows clear diminishing returns, analogous to pre-training scaling laws. This gives practitioners a quantitative rule for predicting model merging returns before running expensive experiments.

**arXiv:** [arxiv.org/abs/2509.24244](https://arxiv.org/abs/2509.24244)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG, Papers With Code

**Why trending:** Model merging is widely used in practice (Mergekit, DARE, TIES) but lacked principled scaling theory; this fills that gap and is immediately useful for the open-source community.

---

## 9. SEIF: Self-Evolving Reinforcement Learning for Instruction Following

**Authors:** Qingyu Ren, Qianyu He, Jiajie Zhu, Xingzhou Chen, Jingwen Chang

**Summary:** SEIF addresses the instruction-following improvement loop without costly external supervision. It generates progressively harder instructions through self-play while using RL to train on them, avoiding the capability ceiling inherent in static-difficulty self-play and the expense of teacher model supervision.

**arXiv:** [arxiv.org/abs/2605.07465](https://arxiv.org/abs/2605.07465)

**Sources:** HuggingFace Daily Papers, arXiv cs.CL

**Why trending:** Instruction following remains a bottleneck for deployment quality; a self-evolving approach that doesn't need a stronger teacher model is directly attractive.

---

## 10. Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models

**Authors:** Victor Conchello Vendrell, Arnau Padres Masdemont, Niccolò Grillo, Jordi Ros-Giralt, Arash Behboodi

**Summary:** Recurrent/looped LLM architectures (e.g., Ouro) improve reasoning via multi-step latent computation but suffer from KV cache growing linearly with reasoning depth. This work decouples memory from compute by restructuring the KV cache across loop iterations, enabling deep looped reasoning without proportional memory growth.

**arXiv:** [arxiv.org/abs/2605.07721](https://arxiv.org/abs/2605.07721)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** Efficient reasoning architectures are in high demand; directly addresses the memory wall that prevents looped transformers from being practical at scale.

---

## 11. LLaVA-UHD v4: What Makes Efficient Visual Encoding in MLLMs?

**Authors:** Kechen Fang, Yihua Qin, Chongyi Wang, Wenshuo Ma, Tianyu Yu

**Summary:** Visual encoding is a major compute bottleneck in multimodal LLMs, especially at high resolution. LLaVA-UHD v4 proposes pre-ViT token compression that reduces the quadratic ViT attention cost before processing, combined with a principled analysis of what information needs to be preserved versus discarded for downstream reasoning tasks.

**arXiv:** [arxiv.org/abs/2605.08985](https://arxiv.org/abs/2605.08985)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV, Papers With Code

**Why trending:** Multimodal LLM efficiency is actively competed on; the LLaVA lineage commands strong community attention and v4 offers concrete speed-quality improvements.

---

## 12. Make Each Token Count: Towards Improving Long-Context Performance with KV Cache Eviction

**Authors:** Ngoc Bui, Hieu Trung Nguyen, Arman Cohan, Rex Ying

**Summary:** The key insight is that full-cache attention is not always optimal for long contexts — irrelevant tokens dilute attention away from useful evidence. The proposed selective eviction strategy improves both efficiency and accuracy by removing tokens that hurt rather than help attention, contradicting the common assumption that more context is always better.

**arXiv:** [arxiv.org/abs/2605.09649](https://arxiv.org/abs/2605.09649)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** Long-context inference efficiency is among the most practical open problems; the counter-intuitive finding that eviction can improve accuracy (not just speed) generates discussion.

---

## 13. Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR

**Authors:** Jeonghye Kim, Jiwon Jeon, Dongsheng Li, Yuqing Yang

**Summary:** Self-distillation frameworks typically use a teacher's guidance everywhere, but this paper shows that on successful student rollouts, teacher guidance suppresses rather than encourages the student's own reasoning. The "rebellious student" approach inverts teacher signals on successful trajectories to preserve and amplify the student's discovered reasoning paths.

**arXiv:** [arxiv.org/abs/2605.10781](https://arxiv.org/abs/2605.10781)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** Clever inversion of the standard distillation assumption; directly improves RLVR training stability and is easy to integrate into existing pipelines.

---

## 14. ELF: Embedded Language Flows

**Authors:** Keya Hu, Linlu Qiu, Yiyang Lu, Hanhong Zhao

**Summary:** ELF applies flow-matching (continuous normalizing flows) directly in the embedding space of language models, enabling non-autoregressive text generation without fixed-length constraints. Unlike masked diffusion language models, ELF operates on continuous representations, achieving competitive generation quality with the ability to refine outputs globally rather than token-by-token.

**arXiv:** [arxiv.org/abs/2605.10938](https://arxiv.org/abs/2605.10938)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** Diffusion/flow-based LMs are a hot research direction competing with autoregressive paradigms; ELF's embedding-space approach is a distinct and technically interesting take.

---

## 15. Dynamic Skill Lifecycle Management for Agentic Reinforcement Learning

**Authors:** Junhao Shen, Teng Zhang, Xiaoyan Zhao, Hong Cheng

**Summary:** Current agentic RL frameworks assume external skills either persist forever or get internalized completely. This paper argues that skills should have a lifecycle — created when useful, pruned when redundant, and retired when superseded — and presents a dynamic management system that improves long-horizon task performance while reducing skill bloat.

**arXiv:** [arxiv.org/abs/2605.10923](https://arxiv.org/abs/2605.10923)

**Sources:** HuggingFace Daily Papers, arXiv cs.AI

**Why trending:** Agentic AI is the dominant near-term deployment direction; principled skill management addresses a gap between academic agent frameworks and production robustness.

---

## 16. SlimQwen: Exploring Pruning and Distillation in Large MoE Model Pre-training

**Authors:** Shengkun Tang, Zekun Wang, Bo Zheng, Liangyu Wang, Rui Men

**Summary:** SlimQwen systematically studies whether structured pruning and knowledge distillation at pre-training scale improve MoE models, finding that pruning provides better initialization than training from scratch and that distillation compounds these gains. Applied to Qwen MoE variants, it delivers competitive performance at substantially reduced expert counts.

**arXiv:** [arxiv.org/abs/2605.08738](https://arxiv.org/abs/2605.08738)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** MoE models (Mixtral, DeepSeek-MoE, Qwen-MoE) dominate the efficiency frontier; practical compression recipes with scaling study findings are immediately actionable.

---

## 17. CollabVR: Collaborative Video Reasoning with Vision-Language and Video Generation Models

**Authors:** Joowon Kim, Seungho Shin, Joonhyung Park, Eunho Yang

**Summary:** CollabVR addresses two failure modes in "Thinking with Video" systems: long-horizon drift and mid-clip simulation errors that compound. It pairs a video generation model for visual simulation with a vision-language model for explicit reasoning, enabling each to compensate for the other's weaknesses through a structured collaboration protocol.

**arXiv:** [arxiv.org/abs/2605.08735](https://arxiv.org/abs/2605.08735)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Why trending:** Video reasoning is gaining traction as a test of world understanding; the collaborative generation-reasoning architecture is elegant and likely to be widely replicated.

---

## 18. Pixal3D: Pixel-Aligned 3D Generation from Images

**Authors:** Dong-Yang Li, Wang Zhao, Yuxin Chen, Wenbo Hu, Meng-Hao Guo

**Summary:** Pixal3D addresses the 2D-3D correspondence gap in image-to-3D synthesis: most 3D generators lose pixel-level faithfulness to the input image because they generate in an implicit 3D space. Pixel-aligned generation enforces explicit correspondence between input image pixels and generated 3D surface points, significantly improving fidelity of reconstructed assets.

**arXiv:** [arxiv.org/abs/2605.10922](https://arxiv.org/abs/2605.10922)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Why trending:** Image-to-3D is high commercial interest (gaming, VR, product visualization); pixel-level fidelity is the key remaining gap and this directly targets it.

---

## 19. FORTIS: Benchmarking Over-Privilege in Agent Skills

**Authors:** Shawn Li, Chenxiao Yu, Han Wang, Wei Yang

**Summary:** FORTIS treats the agent skill layer as a privilege boundary and benchmarks how often LLM agents exceed the intended scope of skills. It reveals that current models routinely request and use capabilities beyond what the task requires, creating significant over-privilege attack surfaces — a security concern for deployed agentic systems.

**arXiv:** [arxiv.org/abs/2605.09163](https://arxiv.org/abs/2605.09163)

**Sources:** HuggingFace Daily Papers, arXiv cs.AI, Reddit r/LocalLLaMA

**Why trending:** Agent security is a growing practical concern as more autonomous systems deploy in production; over-privilege is an underexplored attack surface that FORTIS makes concrete.

---

## 20. NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation

**Authors:** Jinhang Xu, Qiyuan Zhu, Yujun Wu, Zirui Wang

**Summary:** NanoResearch automates the full research pipeline (ideation → literature review → experimentation → writing) while adapting to the specific researcher's resource constraints, methodological preferences, and target venues. It co-evolves skills (what to do), memory (what was tried), and policy (how to act) so the system personalizes to individual researcher context over time.

**arXiv:** [arxiv.org/abs/2605.10813](https://arxiv.org/abs/2605.10813)

**Sources:** HuggingFace Daily Papers, arXiv cs.AI

**Why trending:** AI-for-research automation is a major growth area; the personalization angle — rather than one-size-fits-all research agents — addresses a real gap that makes prior systems impractical.
