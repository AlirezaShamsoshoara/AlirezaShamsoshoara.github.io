---
title: "Daily AI Papers — June 02, 2026"
date: 2026-06-02
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-02/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multi-agent
  - speculative-decoding
  - video-generation
---

## 1. Crafter: A Multi-Agent Harness for Editable Scientific Figure Generation from Diverse Inputs

**Authors:** Haozhe Zhao, Shuzheng Si, Zhenhailong Wang, Zheng Wang, Liang Chen, Xiaotong Li, Zhixiang Liang, Maosong Sun, Minjia Zhang  
**ArXiv:** [arxiv.org/abs/2605.30611](https://arxiv.org/abs/2605.30611)  
**GitHub:** [github.com/HaozheZhao/Crafter](https://github.com/HaozheZhao/Crafter)  
**Sources:** HuggingFace Daily Papers (#1, 105 upvotes)  
**Why Trending:** Top HuggingFace paper today by a wide margin; addresses an acute pain point for researchers — publication-quality figure generation — with a multi-agent approach that generalizes across figure types and produces editable SVGs.

Existing automated figure generation systems target single figure types under text-only input, and produce raster outputs that cannot be locally revised. Crafter is a multi-agent harness that generalizes across figure types and input conditions without architectural changes, paired with CraftEditor for SVG conversion and CraftBench for evaluation across three figure types and four input conditions.

---

## 2. On the Scaling of PEFT: Towards Million Personal Models of Trillion Parameters

**Authors:** Mind Lab, Song Cao, Vic Cao, Kaijie Chen, Bunny Fan, et al.  
**ArXiv:** [arxiv.org/abs/2606.02437](https://arxiv.org/abs/2606.02437)  
**Sources:** HuggingFace Daily Papers (#2, 55 upvotes)  
**Why Trending:** Reframes PEFT from a training shortcut to a new personalization paradigm — "a million personal models on top of one shared model" — a provocative vision that's resonating with the efficiency research community.

PEFT is typically treated as a cheaper alternative to full fine-tuning, but this paper studies a broader role: small trainable adapters as persistent local state on top of strong shared foundation models, where the base model provides shared competence while adapters carry instance-specific behavior such as preferences, skills, tool habits, and memory-like updates. The scaling analysis reveals when this adapter-as-persistent-state framing outperforms both full fine-tuning and larger shared models.

---

## 3. A Matter of TASTE: Improving Coverage and Difficulty of Agent Benchmarks

**Authors:** Tomer Keren, Nitay Calderon, Asaf Yehudai, Yotam Perlitz, Michal Shmueli-Scheuer  
**ArXiv:** [arxiv.org/abs/2605.28556](https://arxiv.org/abs/2605.28556)  
**GitHub:** [github.com/tomerkeren42/TASTE-task-synthesis-from-tool-sequence-evolution](https://github.com/tomerkeren42/TASTE-task-synthesis-from-tool-sequence-evolution)  
**Sources:** HuggingFace Daily Papers (#3, 52 upvotes)  
**Why Trending:** Agent benchmarks are a hot topic as frontier models saturate existing ones; this proposes an automated way to extend benchmark difficulty and coverage without manual annotation.

Existing agent benchmarks like τ²-Bench are becoming saturated as agent capabilities advance, yet constructing new tasks remains complex and costly. TASTE synthesizes benchmark tasks from tool-sequence evolution — starting from existing tool sequences and systematically mutating them to produce harder, more diverse scenarios — enabling coverage of long-tail tool-use patterns with minimal human effort.

---

## 4. K-BrowseComp: A Web Browsing Agent Benchmark Grounded in Korean Contexts

**Authors:** Nahyun Lee, Dongkeun Yoon, Guijin Son, Geewook Kim, Dayoon Ko  
**ArXiv:** [arxiv.org/abs/2606.02404](https://arxiv.org/abs/2606.02404)  
**GitHub:** [github.com/prometheus-eval/K-BrowseComp](https://github.com/prometheus-eval/K-BrowseComp)  
**Sources:** HuggingFace Daily Papers (#4, 42 upvotes)  
**Why Trending:** Non-English agentic benchmarks are rare; this directly exposes frontier model blind spots in Korean web navigation and is generating broad interest in multilingual agent evaluation.

Frontier model evaluation is shifting toward compositional, agentic tasks, but Korean agentic benchmarks remain scarce. K-BrowseComp introduces 400 web-browsing problems grounded in Korean cultural and linguistic contexts (300-problem verified subset), showing significant performance gaps between top English-capable and Korean-capable browsing agents.

---

## 5. Domino: Decoupling Causal Modeling from Autoregressive Drafting in Speculative Decoding

**Authors:** Jianuo Huang, Yaojie Zhang, Qituan Zhang, Hao Lin, Hanlin Xu  
**ArXiv:** [arxiv.org/abs/2605.29707](https://arxiv.org/abs/2605.29707)  
**GitHub:** [github.com/jianuo-huang/Domino](https://github.com/jianuo-huang/Domino)  
**Sources:** HuggingFace Daily Papers (#5, 26 upvotes, 29 GitHub stars)  
**Why Trending:** Speculative decoding is an active engineering battleground; Domino separates causal modeling from autoregressive drafting in a novel way that breaks the longstanding quality-vs-cost tradeoff, with strong GitHub traction.

Speculative decoding's speedup is constrained by a trade-off: autoregressive drafters model causal dependencies among draft tokens but incur sequential overhead, while parallel drafters reduce cost but weaken intra-block coherence. Domino decouples causal modeling from autoregressive drafting, using a non-autoregressive draft head for speed while maintaining causal token coherence through a separate lightweight module, yielding significant speedup improvements over EAGLE-series baselines.

---

## 6. Draft-OPD: On-Policy Distillation for Speculative Draft Models

**Authors:** Haodi Lei, Yafy Li, Haoran Zhang, Shunkai Zhang, Qianjia Cheng  
**ArXiv:** [arxiv.org/abs/2605.29343](https://arxiv.org/abs/2605.29343)  
**GitHub:** [github.com/bingyang-lei/Draft-OPD](https://github.com/bingyang-lei/Draft-OPD)  
**Sources:** HuggingFace Daily Papers (#6, 25 upvotes, 15 GitHub stars)  
**Why Trending:** Addresses a well-known ceiling in speculative decoding training — SFT plateauing — with an on-policy distillation remedy; builds directly on EAGLE3 and DFlash lineage.

Draft models for speculative decoding trained via supervised fine-tuning quickly plateau: acceptance length on test data stops improving even as training loss falls. Draft-OPD applies on-policy distillation — generating drafts from the current policy and distilling from the target model's distribution — breaking the SFT plateau and achieving higher acceptance rates than EAGLE3 and DFlash baselines across diverse target models.

---

## 7. Linear Ensembles Wash Away Watermarks: On the Fragility of Distributional Perturbations in LLMs

**Authors:** Zhihao Wu, Gracia Gong, Qinglin Zhu, Yudong Chen, Runcong Zhao  
**ArXiv:** [arxiv.org/abs/2605.30501](https://arxiv.org/abs/2605.30501)  
**Sources:** HuggingFace Daily Papers (#7, 23 upvotes)  
**Why Trending:** Raises a fundamental alarm for AI provenance efforts — a simple theoretical result showing watermarks fail as soon as users average multiple model outputs — timely given growing regulatory interest in AI content attribution.

Watermarking embeds statistical signatures in AI-generated text for detection and attribution, but this paper reveals a fundamental vulnerability: when users access multiple models (today's reality), watermarks trivially fail. Watermarks perturb output distributions away from the original, and in competitive markets these perturbations are independent across providers; averaging even two watermarked outputs provably washes the signature below detection thresholds.

---

## 8. VLMs are Good Teachers for Video Reasoning via Adaptive Test-Time Optimization

**Authors:** Junhao Cheng, Liang Hou, Tianxiong Zhong, Xin Tao, Pengfei Wan  
**ArXiv:** [arxiv.org/abs/2606.02564](https://arxiv.org/abs/2606.02564)  
**Sources:** HuggingFace Daily Papers (#8, 22 upvotes)  
**Why Trending:** The "Reasoning with Video" paradigm is a 2026 hot topic; this paper shows VLMs can supervise video generation models at test time to fix logical failures without retraining.

The "Reasoning with Video" paradigm uses Video Generation Models (VGMs) to produce visual trajectories for reasoning, but VGMs often generate visually coherent but logically incorrect trajectories. This paper proposes using VLMs as adaptive test-time teachers that score and select generated trajectories on-the-fly, providing optimization signals to VGMs without model retraining, significantly improving reasoning accuracy on physics and causal tasks.

---

## 9. NITP: Next Implicit Token Prediction for LLM Pre-training

**Authors:** Xiangdong Zhang, Debing Zhang, Shaofeng Zhang, Xiaohan Qin, Yu Cheng  
**ArXiv:** [arxiv.org/abs/2605.24956](https://arxiv.org/abs/2605.24956)  
**GitHub:** [github.com/aHapBean/NITP](https://github.com/aHapBean/NITP)  
**Sources:** HuggingFace Daily Papers (#9, 21 upvotes, 23 GitHub stars)  
**Why Trending:** Challenges the decades-old next-token prediction objective at pre-training time — adding implicit latent supervision — with solid experimental backing and growing GitHub interest.

Standard next-token prediction (NTP) supervises language models solely through discrete one-hot labels in the output logit space, leaving the latent representation space under-constrained and allowing hidden states to drift into degenerate, anisotropic configurations. NITP adds a next implicit token prediction objective that supervises the hidden state space directly using continuous targets derived from the embedding of future tokens, improving downstream task performance across language modeling benchmarks.

---

## 10. X-Stream: Exploring MLLMs as Multiplexers for Multi-Stream Understanding

**Authors:** Peiwen Sun, Xudong Lu, Huadai Liu, Yang Bo, Dongming Wu  
**ArXiv:** [arxiv.org/abs/2606.02482](https://arxiv.org/abs/2606.02482)  
**GitHub:** [github.com/PeiwenSun2000/X-Stream](https://github.com/PeiwenSun2000/X-Stream)  
**Sources:** HuggingFace Daily Papers (#10, 21 upvotes, 18 GitHub stars)  
**Why Trending:** Targets real-world multi-stream applications (live sports, autonomous driving, multi-screen) currently unsupported by single-stream VLM benchmarks; strong community response.

Existing video understanding benchmarks are confined to single-stream paradigms, but real-world applications like live sports broadcasting, autonomous driving, and multi-screen collaboration demand continuous multi-stream reasoning. X-Stream treats MLLMs as multiplexers that interleave and jointly reason over multiple simultaneous video streams, introducing new benchmarks and baselines for this challenging but practically critical setting.

---

## 11. VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion

**Authors:** Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay  
**ArXiv:** [arxiv.org/abs/2605.30351](https://arxiv.org/abs/2605.30351)  
**GitHub:** [github.com/yesiltepe-hidir/VideoMLA](https://github.com/yesiltepe-hidir/VideoMLA)  
**Sources:** HuggingFace Daily Papers (#11, 20 upvotes)  
**Why Trending:** Long-form video diffusion is a key frontier; applying Multi-Head Latent Attention (MLA) — proven in language models — to reduce KV cache memory in video diffusion is a clean engineering insight.

Long-rollout causal video diffusion has converged on fixed-size sliding-window KV caches, but the per-head KV layout remains a dominant contributor to streaming memory and latency. VideoMLA applies low-rank latent KV compression (analogous to DeepSeek's MLA in transformers) to video diffusion's temporal attention, enabling minute-scale video generation with dramatically reduced memory footprint without quality degradation.

---

## 12. SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories

**Authors:** Zhuoyun Yu, Xin Xie, Wuguannan Yao, Chenxi Wang, Lei Liang  
**ArXiv:** [arxiv.org/abs/2606.01311](https://arxiv.org/abs/2606.01311)  
**Sources:** HuggingFace Daily Papers (#12, 20 upvotes)  
**Why Trending:** Skill-based LLM agents are a major 2026 trend; step-level attribution for skill refinement is a clean improvement over session-level approaches that many practitioners find too coarse.

Existing training-free skill adaptation pipelines update skills from full trajectories or session-level feedback, making failure attribution coarse and producing unstable or overly broad revisions. SkillAdaptor operates at the step level, identifying precisely which skill invocation failed and why, then applying targeted refinements that produce more stable and generalizable skill updates across interactive benchmark tasks.

---

## 13. Where to Look: Can Foundation Models Reach a Target Viewpoint Through Active Exploration?

**Authors:** Liyang Li, Muzhi Zhu, Zhiyue Zhao, Hengyu Zhao, Ke Liu  
**ArXiv:** [arxiv.org/abs/2606.01247](https://arxiv.org/abs/2606.01247)  
**GitHub:** [github.com/aim-uofa/TVRBench](https://github.com/aim-uofa/TVRBench)  
**Sources:** HuggingFace Daily Papers (#13, 19 upvotes, 13 GitHub stars)  
**Why Trending:** Tests a genuinely new capability — active viewpoint reproduction — that bridges embodied AI and spatial intelligence in foundation models, sparking debate on what "spatial understanding" really means.

Foundation models' spatial intelligence has mostly been studied as passive understanding of pre-collected observations, but humans can actively reproduce viewpoints through physical motion. This paper introduces Target Viewpoint Reproduction (TVR): a task where an agent adjusts its position in a 3D environment until its observation matches a given target image, revealing large gaps between current foundation models and human-level active spatial reasoning.

---

## 14. Which Pretraining Paradigm Better Serves Spatial Intelligence? VLM vs. VGM

**Authors:** Haozhan Shen, Tiancheng Zhao, Kangjia Zhao, Jianwei Yin  
**ArXiv:** [arxiv.org/abs/2605.28132](https://arxiv.org/abs/2605.28132)  
**GitHub:** [github.com/om-ai-lab/Probing-VLM-VGM](https://github.com/om-ai-lab/Probing-VLM-VGM)  
**Sources:** HuggingFace Daily Papers (#14, 17 upvotes)  
**Why Trending:** The VLM-vs-VGM debate for spatial tasks is a recurring discussion; this provides systematic empirical evidence that is frequently cited in ongoing community debates.

Two major pre-training schemes serve as backbones for spatial intelligence tasks: Vision-Language Models (VLMs) using language supervision for semantic alignment, and Video Generation Models (VGMs) learning from temporal and geometric structure. This systematic comparison across depth estimation, scene understanding, and 3D reasoning reveals complementary strengths — VLMs excel at semantic spatial tasks while VGMs are superior for geometric and structural reasoning.

---

## 15. When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs

**Authors:** Yifan Zeng, Yiran Wu, Yaolun Zhang, Wentian Zhao, Kun Wan  
**ArXiv:** [arxiv.org/abs/2605.24202](https://arxiv.org/abs/2605.24202)  
**GitHub:** [github.com/XHMY/marl-llm-workflows](https://github.com/XHMY/marl-llm-workflows)  
**Sources:** HuggingFace Daily Papers (#15, 13 upvotes)  
**Why Trending:** As MARL for LLMs becomes mainstream, the community needs systematic guidance on when it actually helps; this paper fills that gap with practical scaling and architecture insights.

Multi-agent LLM workflows route inference through specialized roles to improve end-task accuracy, but jointly training those roles with RL is unstable in poorly understood ways. This study compares Shared-Policy vs. Isolated-Policy training of multi-agent workflows, identifying conditions under which multi-agent RL beats its base models and the role of workflow complexity, scale, and policy-sharing in determining outcome.

---

## 16. ESPO: Early-Stopping Proximal Policy Optimization

**Authors:** Zihang Li, Rui Zhou, Yingcheng Shi, Wenhan Yu, Zhewen Tan  
**ArXiv:** [arxiv.org/abs/2605.29860](https://arxiv.org/abs/2605.29860)  
**Sources:** HuggingFace Daily Papers (#16, 13 upvotes)  
**Why Trending:** PPO waste on failed reasoning trajectories is a well-known problem in RLHF; ESPO's early-stopping heuristic is simple to implement and shows strong gains, driving replication interest.

When an LLM under RL commits a wrong reasoning step early in a trajectory, standard PPO forces it to keep generating until the maximum horizon — wasting compute on tokens that never receive positive reward and polluting advantage estimates with post-failure noise. ESPO detects trajectory failure early and stops generation, reattributing advantage and significantly improving sample efficiency and final policy quality on math and coding RL benchmarks.

---

## 17. LVSA: Training-Free Sparse Attention for Long Video Diffusion

**Authors:** Gael Glorian, Ioannis Lamprou, Zhen Zhang, Yujie Yuan, Hongsheng Liu  
**ArXiv:** [arxiv.org/abs/2605.31057](https://arxiv.org/abs/2605.31057)  
**GitHub:** [github.com/JiusiServe/LongVideoSparseAttention](https://github.com/JiusiServe/LongVideoSparseAttention)  
**Sources:** HuggingFace Daily Papers (#17, 12 upvotes)  
**Why Trending:** Training-free efficiency improvements for video diffusion are highly practical; LVSA solves both the quadratic attention bottleneck and the "frozen frame" quality problem beyond training horizon simultaneously.

Dense self-attention in long video diffusion grows quadratically with sequence length, and beyond the training horizon the model collapses to near-static "frozen" repetitive frames. LVSA applies training-free sparse attention patterns specifically designed for video diffusion's temporal structure, enabling long-form generation with linear attention complexity while resolving the frozen-frame failure mode.

---

## 18. MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Environment Simulation

**Authors:** Wenhao Wang, Peizhi Niu, Gongyi Zou, Xiyuan Yang, Jingxing Wang  
**ArXiv:** [arxiv.org/abs/2606.02470](https://arxiv.org/abs/2606.02470)  
**GitHub:** [github.com/wwh0411/MCP-Persona](https://github.com/wwh0411/MCP-Persona)  
**Sources:** HuggingFace Daily Papers (#18, 12 upvotes)  
**Why Trending:** MCP (Model Context Protocol) is a hot standard in 2026; this is among the first benchmarks specifically targeting MCP-connected personal application agents, filling an obvious evaluation gap.

The Model Context Protocol (MCP) has been rapidly adopted across personal applications and development platforms, but existing benchmarks focus on generic information-seeking tools and fail to capture challenges of personal social apps (email, calendar, messaging) with complex state and privacy requirements. MCP-Persona simulates real-world personal application environments and benchmarks LLM agent performance across tasks requiring multi-app coordination, state tracking, and user-preference alignment.

---

## 19. Masking Stale Observations Helps Search Agents — Until It Doesn't: A Regime Map and Its Mechanism

**Authors:** Haoxiang Zhang, Qixin Xu, Zhuofeng Li, Lei Zhang, Pengcheng Jiang  
**ArXiv:** [arxiv.org/abs/2606.00408](https://arxiv.org/abs/2606.00408)  
**GitHub:** [github.com/i-DeepSearch/observation-masking](https://github.com/i-DeepSearch/observation-masking)  
**Sources:** HuggingFace Daily Papers (#19, 12 upvotes)  
**Why Trending:** Context management for long-horizon agents is an open engineering question; this paper provides a concrete regime map — when masking helps vs. hurts — which practitioners can directly apply.

Long-horizon search agents accumulate large amounts of retrieved content across many tool calls, and masking stale observations is a minimal intervention to manage context budgets. Through systematic sweeps over agent types, task lengths, and masking schedules, this paper maps the conditions under which observation masking helps vs. degrades performance, identifying the mechanism behind both effects and providing actionable guidelines.

---

## 20. LongLive-RAG: A General Retrieval-Augmented Framework for Long Video Generation

**Authors:** Qixin Hu, Shuai Yang, Wei Huang, Song Han, Yukang Chen  
**ArXiv:** [arxiv.org/abs/2606.02553](https://arxiv.org/abs/2606.02553)  
**GitHub:** [github.com/qixinhu11/LongLive-RAG](https://github.com/qixinhu11/LongLive-RAG)  
**Sources:** HuggingFace Daily Papers (#20, 11 upvotes)  
**Why Trending:** Long video generation is a top research priority in 2026; applying RAG-style retrieval to video diffusion to fix identity drift is a creative cross-domain idea gaining traction.

Autoregressive video diffusion enables variable-length synthesis, but long-horizon generation suffers from accumulated errors and identity drift as sliding-window attention loses earlier context. LongLive-RAG introduces a retrieval-augmented framework that maintains a memory bank of past generated frames and retrieves relevant past context at each generation step, substantially reducing drift and improving consistency in minute-scale video generation.
