---
title: "Daily AI Papers — May 11, 2026"
date: 2026-05-11
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-11/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - diffusion-models
  - llm-post-training
  - multimodal-ai
---

## 1. MACE-Dance: Motion-Appearance Cascaded Experts for Music-Driven Dance Video Generation

**Authors:** Kaixing Yang, Jiashu Zhu, Xulong Tang, Ziqiao Peng, Xiangyue Zhang, Puwei Wang, Jiahong Wu, Xiangxiang Chu, Hongyan Liu, Jun He

**Summary:** MACE-Dance introduces a cascaded expert architecture that separately models motion dynamics and visual appearance for music-driven dance video generation—a gap left by related work in 3D pose generation and talking-head synthesis. The framework achieves joint high-quality visual appearance and rhythmically coherent motion, outperforming prior methods on cross-domain dance video benchmarks.

**arXiv:** [arxiv.org/abs/2512.18181](https://arxiv.org/abs/2512.18181)

**Sources:** HuggingFace Daily Papers

**Why trending:** Highest upvote count of the day (80); addresses a compelling AIGC use case with strong visual demo appeal on social platforms.

---

## 2. Mean Mode Screaming: Mean–Variance Split Residuals for 1000-Layer Diffusion Transformers

**Authors:** Pengqi Lu

**Summary:** This paper identifies a failure mode called Mean Mode Screaming (MMS) where deep Diffusion Transformers silently collapse into a mean-dominated state that homogenizes token representations—even when training loss appears healthy. The fix is a Mean–Variance Split Residual (MVSR) formulation that separates mean and centered-variance streams, enabling stable training of 1000-layer DiTs.

**arXiv:** [arxiv.org/abs/2605.06169](https://arxiv.org/abs/2605.06169)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Why trending:** 75 upvotes; single-author mechanistic insight into scaling diffusion transformers beyond current depth limits—practically useful for anyone training large DiTs.

---

## 3. Flow-OPD: On-Policy Distillation for Flow Matching Models

**Authors:** Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen, Kaituo Feng, Yunlong Lin, Lin Chen, Zehui Chen, Shaosheng Cao, Feng Zhao

**Summary:** Flow-OPD is the first unified post-training framework that applies on-policy distillation (a technique proven in LLM alignment) to Flow Matching text-to-image models, directly addressing reward sparsity and gradient interference that cause the "seesaw effect" in multi-task alignment. The method eliminates reward hacking while improving quality across heterogeneous objectives simultaneously.

**arXiv:** [arxiv.org/abs/2605.08063](https://arxiv.org/abs/2605.08063)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV/cs.LG

**Why trending:** 73 upvotes; bridges LLM RLHF techniques with image generation—timely given the surge in flow-matching T2I models (FLUX, Stable Diffusion 3).

---

## 4. Listwise Policy Optimization: Group-based RLVR as Target-Projection on the LLM Response Simplex

**Authors:** Yun Qu, Qi Wang, Yixiu Mao, Heming Zou, et al.

**Summary:** This work reveals that popular group-based RLVR methods (GRPO, PPO variants) share a common geometric structure: they each implicitly define a target distribution on the response probability simplex and project toward it. Building on this unification, the authors propose Listwise Policy Optimization (LPO) that operates directly on the full response distribution, achieving more stable and sample-efficient post-training.

**arXiv:** [arxiv.org/abs/2605.06139](https://arxiv.org/abs/2605.06139)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** 57 upvotes; provides a clean theoretical unification of GRPO/REINFORCE/PPO variants—highly relevant for anyone doing LLM post-training and reasoning improvement.

---

## 5. HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents

**Authors:** Guankai Li, Jiabin Chen, Yi Xu, Xichen Zhang, Yuan Lu

**Summary:** HyperEyes challenges the sequential tool-call paradigm in multimodal agents by fusing visual grounding and retrieval into a single atomic action, enabling concurrent multi-entity search within one round instead of one call per entity. The system uses dual-grained efficiency-aware RL to jointly optimize task performance and inference cost, reducing interaction rounds significantly.

**arXiv:** [arxiv.org/abs/2605.07177](https://arxiv.org/abs/2605.07177)

**Sources:** HuggingFace Daily Papers, arXiv cs.AI

**Why trending:** 55 upvotes; directly addresses latency and cost bottlenecks in agentic RAG pipelines—practical for production multimodal search systems.

---

## 6. LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling

**Authors:** Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, et al.

**Summary:** AutoTTS replaces hand-crafted test-time scaling heuristics with an environment-driven framework where LLM agents automatically discover and evaluate new TTS strategies, effectively using LLMs to design better LLM inference procedures. This meta-learning loop over computation-allocation strategies finds non-obvious patterns that manual approaches miss.

**arXiv:** [arxiv.org/abs/2605.08083](https://arxiv.org/abs/2605.08083)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG, arXiv cs.AI

**Why trending:** 52 upvotes; test-time compute scaling is one of the hottest topics in 2026; automating the design of TTS strategies is a natural and compelling next step.

---

## 7. HumanNet: Scaling Human-centric Video Learning to One Million Hours

**Authors:** Yufan Deng, Daquan Zhou

**Summary:** HumanNet is a million-hour human-centric video corpus spanning first- and third-person perspectives with fine-grained activity annotations covering how humans physically interact with the world. It targets the data bottleneck in embodied intelligence and physical world understanding that vision-language scaling alone cannot solve.

**arXiv:** [arxiv.org/abs/2605.06747](https://arxiv.org/abs/2605.06747)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Why trending:** 40 upvotes; embodied AI and physical world understanding are top research priorities in 2026; a 1M-hour curated corpus is a significant infrastructure contribution.

---

## 8. Anisotropic Modality Alignment for Multimodal LLMs

**Authors:** Xiaomin Yu, Yijiang Li, Yuhui Zhang, Hanzhen Zhao, Yue Yang, Hao Tang, et al.

**Summary:** This paper investigates whether representations from pretrained multimodal contrastive models (like CLIP) can be reliably interchanged across modalities—a premise underlying recent unimodal-data multimodal training approaches. It identifies persistent anisotropic misalignment between modalities and proposes targeted alignment corrections that improve downstream MLLM performance.

**arXiv:** [arxiv.org/abs/2605.07825](https://arxiv.org/abs/2605.07825)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV/cs.LG

**Why trending:** 22 upvotes; directly relevant to the popular paradigm of training MLLMs with unimodal data via shared embedding spaces.

---

## 9. Beyond Retrieval: A Multitask Benchmark and Model for Code Search (CoREB)

**Authors:** Siqiao Xue, Zihan Liao, Jin Qin, Ziyin Zhang, Yixiang Mu, Fan Zhou, Hang Yu

**Summary:** CoREB is a contamination-limited, multitask code retrieval and reranking benchmark that goes beyond first-stage retrieval to evaluate the full code search pipeline including reranking with developer-style queries. It addresses fundamental issues in existing code search benchmarks: data contamination, label noise, and binary relevance degeneracy.

**arXiv:** [arxiv.org/abs/2605.04615](https://arxiv.org/abs/2605.04615)

**Sources:** HuggingFace Daily Papers, arXiv cs.SE/cs.IR

**Why trending:** 22 upvotes; code search is a high-value practical problem, and a properly rigorous benchmark fills a real gap for the developer tools community.

---

## 10. TextLDM: Language Modeling with Continuous Latent Diffusion

**Authors:** Jiaxiu Jiang, Jingjing Ren, Wenbo Li, Bo Wang, Haoze Sun, et al.

**Summary:** TextLDM transfers the visual latent diffusion recipe (DiT + flow matching + VAE) to text generation with minimal architectural modification—training a Transformer VAE to map tokens to continuous latent space and then applying diffusion in that space. This produces a single architecture that unifies visual synthesis and text generation without autoregressive decoding.

**arXiv:** [arxiv.org/abs/2605.07748](https://arxiv.org/abs/2605.07748)

**Sources:** HuggingFace Daily Papers, arXiv cs.CL/cs.LG

**Why trending:** 18 upvotes; unifying image and text generation under one architecture is a long-standing goal; applying LDM directly to language is elegant and the results are closely watched.

---

## 11. UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification

**Authors:** Qihang Fan, Huaibo Huang, Zhiying Wu, Bingning Wang, Ran He

**Summary:** UniPrefill introduces block-wise dynamic sparsification for long-context prefill that works across diverse LLM architectures, including hybrid models with sparse attention, without requiring architecture-specific tuning. It significantly reduces prefill computation for long-context scenarios while maintaining generation quality.

**arXiv:** [arxiv.org/abs/2605.06221](https://arxiv.org/abs/2605.06221)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** 18 upvotes; long-context inference efficiency is a top production concern as context windows expand to millions of tokens.

---

## 12. DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents

**Authors:** Zhaorun Chen, Xun Liu, Haibo Tong, Chengquan Guo, et al. (Percy Liang, Dawn Song, Bo Li labs)

**Summary:** DTap is a red-teaming platform for evaluating AI agent security under adversarial conditions, covering real-world attack scenarios like API key leakage, unauthorized transactions, and data deletion triggered by adversarial inputs. It provides controllable, interactive evaluation environments reflecting how deployed agents can be manipulated into harmful actions.

**arXiv:** [arxiv.org/abs/2605.04808](https://arxiv.org/abs/2605.04808)

**Sources:** HuggingFace Daily Papers, arXiv cs.AI/cs.CR

**Why trending:** 16 upvotes; AI agent security is a critical open problem—this comes from top safety researchers (Stanford, UIUC, UChicago, Berkeley) and addresses a gap in evaluation tooling.

---

## 13. AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning

**Authors:** Haotian Zhao, Songlin Zhou, Yuxin Zhang, Stephen S.-T. Yau, Wenyu Zhang, et al.

**Summary:** AEM tackles the credit assignment problem in multi-turn agentic RL without dense process reward models by adaptively modulating entropy based on trajectory-level signals, providing implicit step-wise guidance under sparse outcome-only rewards. This reduces the need for expensive intermediate supervision while improving exploration in long-horizon tasks.

**arXiv:** [arxiv.org/abs/2605.00425](https://arxiv.org/abs/2605.00425)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG/cs.AI

**Why trending:** 15 upvotes; multi-turn agent RL is a key frontier for post-training LLM agents; sparse reward settings are the most practically relevant.

---

## 14. 4DThinker: Thinking with 4D Imagery for Dynamic Spatial Understanding

**Authors:** Zhangquan Chen, Manyuan Zhang, Xinlei Yu, Xiang An, Bo Li, Xin Xie, et al.

**Summary:** 4DThinker is the first framework that incorporates 4D imagery (3D space + time) into vision-language model reasoning chains, enabling VLMs to think with explicit spatiotemporal representations rather than verbalizing all spatial reasoning as text. This approach reduces verbosity and improves precision for complex dynamic spatial reasoning from monocular video.

**arXiv:** [arxiv.org/abs/2605.05997](https://arxiv.org/abs/2605.05997)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV/cs.AI

**Why trending:** 15 upvotes; bridging VLMs and physical-world spatial reasoning is a key challenge for robotics and embodied AI applications.

---

## 15. Rethinking State Tracking in Recurrent Models Through Error Control Dynamics

**Authors:** Jiwan Chung, Heechan Choi, Seon Joo Kim

**Summary:** This paper argues that the theory of recurrent state tracking should focus on error control dynamics—not just expressive capacity—and proves that affine recurrent networks (SSMs, Linear Attention) cannot correct errors along state-separating directions. The finding has direct implications for the theoretical limits of Mamba, RWKV, and similar architectures on symbolic state tracking tasks.

**arXiv:** [arxiv.org/abs/2605.07755](https://arxiv.org/abs/2605.07755)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** 14 upvotes; theoretical analysis of SSM/Linear Attention limits is highly relevant given the surge in hybrid Transformer-SSM architectures.

---

## 16. MatryoshkaLoRA: Learning Accurate Hierarchical Low-Rank Representations for LLM Fine-Tuning

**Authors:** Ionut-Vlad Modoranu, Mher Safaryan, Dan Alistarh

**Summary:** MatryoshkaLoRA extends LoRA with a nested, hierarchical rank structure inspired by Matryoshka representation learning, allowing a single trained adapter to support multiple rank budgets at inference time without retraining. This eliminates the exhaustive rank grid search required by standard LoRA while outperforming existing rank-adaptive methods like DyLoRA.

**arXiv:** [arxiv.org/abs/2605.07850](https://arxiv.org/abs/2605.07850)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** 13 upvotes; LoRA fine-tuning is ubiquitous; any improvement in rank selection flexibility is immediately useful across the LLM community.

---

## 17. MISA: Mixture of Indexer Sparse Attention for Long-Context LLM Inference

**Authors:** Ruijie Zhou, Fanxu Meng, Yufei Xu, Tongxuan Liu, Guangming Lu, Muhan Zhang, Wenjie Pei

**Summary:** MISA addresses the dominant compute cost of DeepSeek-style sparse attention—the multi-head token indexer on long contexts—by replacing it with a mixture of lightweight indexers that collectively match quality while slashing indexer FLOPs. The approach achieves state-of-the-art sparse attention efficiency on long-context benchmarks.

**arXiv:** [arxiv.org/abs/2605.07363](https://arxiv.org/abs/2605.07363)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** 12 upvotes; DeepSeek V3/V3.2 sparse attention is widely used; optimizing its indexer is directly applicable to production inference stacks.

---

## 18. A²RD: Agentic Autoregressive Diffusion for Long Video Consistency

**Authors:** Do Xuan Long, Yale Song, Min-Yen Kan, Tomas Pfister, Long T. Le

**Summary:** A²RD decouples creative synthesis from consistency enforcement in long video generation through a Retrieve–Synthesize–Refine–Update cycle that operates segment-by-segment, preventing semantic drift and narrative collapse over long horizons. The agentic loop enables self-improvement without human supervision across video segments.

**arXiv:** [arxiv.org/abs/2605.06924](https://arxiv.org/abs/2605.06924)

**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Why trending:** 11 upvotes; long video generation coherence is an unsolved problem; the agentic framing is novel and directly tackles production pain points for video generation systems.

---

## 19. UniSD: Towards a Unified Self-Distillation Framework for Large Language Models

**Authors:** Yiqiao Jin, Yiyang Wang, Lucheng Fu, Yijia Xiao, et al.

**Summary:** UniSD provides the first systematic analysis of self-distillation in autoregressive LLMs, unifying isolated design choices (trajectory sampling, correctness estimation, supervision stability) under a single framework and clarifying their individual and joint effects. The unified framework achieves consistent improvements over single-design-choice baselines across reasoning and language tasks.

**arXiv:** [arxiv.org/abs/2605.06597](https://arxiv.org/abs/2605.06597)

**Sources:** HuggingFace Daily Papers, arXiv cs.CL/cs.LG

**Why trending:** 10 upvotes; self-improvement without external teachers is a key research goal; this provides both a theoretical foundation and practical guidance.

---

## 20. Normalizing Trajectory Models

**Authors:** Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind

**Summary:** Normalizing Trajectory Models (NTM) models each reverse diffusion step as a conditional normalizing flow with exact likelihood training, addressing the breakdown of the Gaussian denoising assumption in few-step generation without sacrificing the likelihood framework. Unlike distillation or consistency training approaches, NTM enables proper likelihood evaluation at each step, enabling both high-quality generation and tractable density estimation.

**arXiv:** [arxiv.org/abs/2605.08078](https://arxiv.org/abs/2605.08078)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG/cs.CV

**Why trending:** 8 upvotes; from Apple Research (Jiatao Gu, David Berthelot, Josh Susskind); few-step diffusion with principled likelihood is an open theoretical problem—notable authorship drives attention.
