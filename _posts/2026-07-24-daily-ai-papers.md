---
title: "Daily AI Papers — July 24, 2026"
date: 2026-07-24
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-24/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - deep-research-agents
  - video-generation
  - vision-language-action
---

## 1. AREX: Towards a Recursively Self-Improving Agent for Deep Research

**Authors:** Shuqi Lu, Chaofan Li, Kun Luo, Zhang Zhang, Hui Wang, et al.

**Summary:** Introduces AREX, a family of deep research agents that alternate between an inner loop gathering evidence toward a provisional answer and an outer loop that audits the answer constraint-by-constraint, using partially verified state to guide targeted follow-up research. Trained via agentic mid-training and long-horizon RL at 4B and 122B-A10B MoE scales, AREX substantially outperforms comparable-scale baselines on BrowseComp, WideSearch, DeepSearchQA, and Humanity's Last Exam.

**arXiv:** [arxiv.org/abs/2607.21461](https://arxiv.org/abs/2607.21461)
**Found on:** HuggingFace Daily Papers
**Why trending:** Top of today's HF board (115 upvotes) — recursive self-improvement for deep-research agents is a hot agentic-RL topic.

---

## 2. ReferTrack: Referring Then Tracking for Embodied Visual Tracking

**Authors:** Hanjing Ye, Tianle Zeng, Jiazhao Zhang, Shaoan Wang, Zibo Zhang, et al.

**Summary:** Proposes a referring-then-tracking paradigm for embodied visual tracking that first selects a target from indexed bounding boxes, then decodes tracking waypoints grounded in that image-space decision, addressing the weak supervision of abstract spatial latents in prior VLA chain-of-thought approaches. ReferTrack achieves state-of-the-art single-view results on EVT-Bench (89.4%/73.3%/74.1% across splits) and demonstrates real-world sim-to-real transfer on legged and humanoid robots.

**arXiv:** [arxiv.org/abs/2607.20061](https://arxiv.org/abs/2607.20061)
**Found on:** HuggingFace Daily Papers
**Why trending:** 41 upvotes — embodied VLA tracking with real-robot validation draws strong interest.

---

## 3. K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training Educational LLMs

**Authors:** Hao Liang, Qihan Lin, Zhaoyang Han, Xiaochen Ma, Zhen Hao Wong, et al.

**Summary:** Introduces K12-KGraph, a curriculum-aligned knowledge graph built from official K-12 textbooks across four subjects, from which the authors derive K12-Bench (a 23,640-question benchmark) and K12-Train (a graph-guided fine-tuning corpus). Current models like Gemini-3-Flash and Gemma-4-31B-IT score only 57% and 46% exact match respectively, while training on K12-Train outperforms equally-sized subsets of mainstream instruction-tuning corpora.

**arXiv:** [arxiv.org/abs/2605.09635](https://arxiv.org/abs/2605.09635)
**Found on:** HuggingFace Daily Papers
**Why trending:** 39 upvotes — curriculum-grounded educational AI benchmarking is a growing niche with clear real-world stakes.

---

## 4. Visual Contrastive Self-Distillation

**Authors:** Yijun Liang, Yunjie Tian, Yijiang Li, Yuqi Jia, Furong Huang, et al.

**Summary:** Proposes Visual Contrastive Self-Distillation (VCSD), which removes the need for an external teacher, privileged answers, or visual evidence signals in on-policy self-distillation by contrasting an EMA teacher's next-token distributions with and without image content to sharpen its training target. On Qwen3-VL, VCSD lifts a seven-benchmark aggregate from 62.27%→67.04% (2B), 71.30%→73.16% (4B), and 72.51%→76.26% (8B) with no added inference cost.

**arXiv:** [arxiv.org/abs/2607.21556](https://arxiv.org/abs/2607.21556)
**Found on:** HuggingFace Daily Papers
**Why trending:** 39 upvotes — a simple, teacher-free self-distillation recipe for VLMs with strong reported gains.

---

## 5. Show, Don't Tell: Evaluating Spatial Cognition in Generative Pixels Rather Than LLM Text

**Authors:** Xu Wang, Kaixiang Yao, Miao Pan, Xiaohe Zhou, Xuanyu Liu, et al.

**Summary:** Points out that existing spatial-reasoning benchmarks require coordinates or text answers, creating an interface mismatch for image-generation models that could otherwise express spatial judgments directly in pixels. The authors introduce ProVisE, a framework that elicits and parses protocol-constrained visual answers, plus SpatialGen-Bench, finding image-generation models competitive when allowed to answer in pixel space while text-output VLMs retain an edge on compositional reasoning.

**arXiv:** [arxiv.org/abs/2607.21072](https://arxiv.org/abs/2607.21072)
**Found on:** HuggingFace Daily Papers
**Why trending:** 34 upvotes — a novel evaluation angle bridging image generation and spatial cognition benchmarking.

---

## 6. Tencent WorkBuddy Bench: A Multi-Domain Coding-Agent Benchmark with Contamination-Resistant Task Construction

**Authors:** Tencent WorkBuddy Bench Team: Siqi Cai, Shaopeng Chen, Xiang Fei, Yong Mao, et al.

**Summary:** Introduces a multi-domain coding-agent evaluation suite spanning Code, Web, Office, and Security domains, where every task is reverse-engineered from a real commit/PR/business scenario and rewritten as a colloquial role-played request so it can't be recovered via web search, with the full dataset (task directories, environments, harness, tests) openly released for reproducibility. The suite reports a cross-model leaderboard run on two agent harnesses (CodeBuddy Code and Claude Code), noting scores aren't comparable across its four subsets.

**arXiv:** [arxiv.org/abs/2607.20911](https://arxiv.org/abs/2607.20911)
**Found on:** HuggingFace Daily Papers
**Why trending:** 17 upvotes — contamination-resistant coding-agent benchmarking from a major industry lab.

---

## 7. NVIDIA Object-Oriented Agents: Native Python Object-Oriented Agents

**Authors:** Paul Furgale, Severin Klingler, James Nolan, Matt Staats, Gaia Di Lorenzo, et al.

**Summary:** Presents NOOA, a model-agnostic Python framework where an agent is simply a Python object — methods are actions, fields are state, docstrings are prompts, and a method body of "..." is completed at runtime by an LLM agent loop while normal-bodied methods stay deterministic. The paper identifies six model-facing design ideas NOOA is first to combine on one surface and demonstrates effective use on SWE-bench Verified, Terminal-Bench 2.0, and ARC-AGI-3.

**arXiv:** [arxiv.org/abs/2607.20709](https://arxiv.org/abs/2607.20709)
**Found on:** HuggingFace Daily Papers
**Why trending:** 17 upvotes — from NVIDIA, addressing the fragmented state of agent-framework tooling.

---

## 8. Color Pass-Through via Camera-Display Coupling

**Authors:** Ruikang Li, Molin Li, Jiarui Wu, Zhe Wei, Pengpeng Liu, et al.

**Summary:** Argues that the mismatch between a captured scene and its on-screen rendering stems from calibrating cameras and displays separately and connecting them via low-dimensional color transforms, and proposes Color Pass-Through, an end-to-end learned framework that treats camera and display as one coupled system. The method achieves an average +2.0-point gain on a 5-point user study and more than 2x improvement on quantitative color-reproduction metrics versus baselines.

**arXiv:** [arxiv.org/abs/2607.12746](https://arxiv.org/abs/2607.12746)
**Found on:** HuggingFace Daily Papers
**Why trending:** 17 upvotes — a practical fix for a long-standing capture-to-display color fidelity problem.

---

## 9. LLMs Get Lost in Evolving User Intent

**Authors:** Jihoon Tack, Philippe Laban, Jennifer Neville

**Summary:** Introduces a framework that converts static single-turn tasks into multi-turn conversations where user intent is incrementally revealed, revised, and redirected, while preserving each task's original evaluation protocol so existing benchmarks can be reused without new annotation. Across multiple tasks, strong static-setting performance fails to transfer to the evolving-intent setting, revealing that today's LLMs don't yet faithfully track and act on shifting user intent.

**arXiv:** [arxiv.org/abs/2607.20734](https://arxiv.org/abs/2607.20734)
**Found on:** HuggingFace Daily Papers
**Why trending:** 14 upvotes — a clean, reusable evaluation framework exposing a real gap in collaborative-agent reliability.

---

## 10. Self-Supervised Learning of Structured Dynamics from Videos

**Authors:** Lukas Knobel, Andrew Zisserman, Yuki M. Asano

**Summary:** Proposes the Structured Dynamics Model (SDM), which separates camera motion from object motion in frozen features of a pretrained image ViT via future-feature prediction, rather than an entangled single latent, trained with self-supervision on real video plus weak synthetic (Kubric) supervision. On the new ProbeMotion evaluation suite, SDM outperforms global CLS/average-pooled backbone baselines and compares favorably to strongly supervised representations like VGGT despite much weaker supervision.

**arXiv:** [arxiv.org/abs/2607.21576](https://arxiv.org/abs/2607.21576)
**Found on:** HuggingFace Daily Papers
**Why trending:** 12 upvotes — disentangling camera vs. object motion is a persistent open problem in video representation learning.

---

## 11. SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation

**Authors:** Junsong Chen, Jincheng Yu, Yitong Li, Shuchen Xue, Haozhe Liu, et al.

**Summary:** Introduces SANA-Video 2.0, a hybrid video diffusion transformer (5B/14B) combining gated linear attention with periodic gated-softmax anchors at a 3:1 ratio, plus Block Attention Residuals that reuse anchor features across depth, matching full-softmax video DiT quality while retaining linear attention's long-sequence scaling. It hits a VBench score of 84.30 in 13.2s at 480p on one H100 and is up to 120x faster than Wan 2.2-A14B with further Sol-Engine kernel/caching optimizations.

**arXiv:** [arxiv.org/abs/2607.21553](https://arxiv.org/abs/2607.21553)
**Found on:** HuggingFace Daily Papers
**Why trending:** 12 upvotes — efficient long/high-res video generation is a fast-moving competitive area.

---

## 12. Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers

**Authors:** Sicheng Mo, Yuheng Li, Ziyang Leng, Krishna Kumar Singh, Bolei Zhou

**Summary:** Presents WorldWeaver (W^2), a streaming multi-agent video diffusion model that maintains shared world state via learnable "world state registers" — tokens tracking individual agent status and global state that are updated after each generated chunk — using a Mixture-of-Transformers design with separate weights for world-state and visual-frame modeling. Experiments on two-agent Minecraft video generation show explicit world-state modeling improves logical consistency and generation quality over prior autoregressive pipelines that just carry forward raw observation history.

**arXiv:** [arxiv.org/abs/2607.21594](https://arxiv.org/abs/2607.21594)
**Found on:** HuggingFace Daily Papers
**Why trending:** 9 upvotes — multi-agent persistent world models are an emerging frontier for interactive video generation.

---

## 13. Robostral Navigate

**Authors:** Arjun Majumdar, Avinash Sooriyarachchi, Benjamin Tibi, Chris Bamford, Elliot Chane-Sane, et al.

**Summary:** Introduces Robostral Navigate, an 8B vision-language navigation model that consumes only monocular RGB and predicts waypoints by pointing within the current camera view, trained on 2.4M simulated trajectories with a prefix-caching recipe cutting training tokens 22x. It sets new state-of-the-art results on R2R-CE (77.4% success, +10.5 over the best monocular method) and RxR-CE (75.1%) using only a single RGB camera.

**arXiv:** [arxiv.org/abs/2607.20785](https://arxiv.org/abs/2607.20785)
**Found on:** HuggingFace Daily Papers
**Why trending:** 8 upvotes — sensor-minimal, embodiment-general navigation with strong new SOTA numbers.

---

## 14. Predictive Divergence Masks for LLM RL

**Authors:** Xiangxin Zhou, Jiarui Yao, Penghui Qi, Bowen Ping, Jiaqi Tang, et al.

**Summary:** Observes that PPO-style trust-region masking for LLM RL relies on a sampled-token importance-ratio "direction criterion" that can disagree in sign with the actual change in the divergence used for the proximity criterion. The authors propose a predictive divergence mask that directly asks whether the next policy-gradient step will increase or decrease that divergence, deriving a closed-form prediction with lightweight top-K estimators that improves RL training stability across model scales.

**arXiv:** [arxiv.org/abs/2607.10848](https://arxiv.org/abs/2607.10848)
**Found on:** HuggingFace Daily Papers
**Why trending:** 8 upvotes — RL training stability for LLMs remains a heavily worked post-training problem.

---

## 15. Sample-Efficient Learning from Agent Experience

**Authors:** Chenhui Gou, Haoqin Tu, Yunhao Fang, Jianfei Cai, Hamid Rezatofighi

**Summary:** Defines "Experience Distillation," internalizing an agent's in-context interaction history into model weights without further environment interaction, addressing that in-context learning gains vanish once experience leaves the context window. On 749 software-engineering tasks and six text-adventure games, it retains at least 64.8% of in-context-learning gains (vs. 3.8% for direct supervised fine-tuning) and matches classical RL baselines with at least 9.6x fewer environment samples.

**arXiv:** [arxiv.org/abs/2607.21051](https://arxiv.org/abs/2607.21051)
**Found on:** HuggingFace Daily Papers
**Why trending:** 7 upvotes — cheap internalization of agent experience addresses a real cost bottleneck in agent training.

---

## 16. Multi-Turn On-Policy Distillation with Prefix Replay

**Authors:** Baohao Liao, Hanze Dong, Christof Monz, Xinxing Xu, Li Dong, Furu Wei

**Summary:** Identifies a "prefix trap" in multi-turn on-policy distillation for agents: making histories more student-on-policy improves relevance but can query the teacher on histories where its guidance is unreliable. The proposed ReOPD reuses pre-collected teacher trajectories as replayed prefixes with a step-decaying sampling schedule, preserving or improving accuracy while requiring zero tool calls during student training and running at least 4x faster per rollout than standard on-policy distillation.

**arXiv:** [arxiv.org/abs/2607.04763](https://arxiv.org/abs/2607.04763)
**Found on:** HuggingFace Daily Papers
**Why trending:** 7 upvotes — a practical efficiency win for distilling agentic LLM behavior at scale.

---

## 17. Recurrent Sinusoidal INRs for Efficient High-Fidelity Representation

**Authors:** Hyunmin Cho, Jaejun Yoo, Kyong Hwan Jin

**Summary:** Studies sinusoidal recurrence as a mechanism for harmonic spectral enrichment in implicit neural representations, showing sinusoidal activations induce a harmonic line spectrum that a shared, iteratively-applied sinusoidal block can exploit to enrich effective spectral support. The approach achieves higher fidelity than feed-forward INR baselines with fewer parameters and optimization steps, transferring favorably to super-resolution, NeRF, and SDF tasks.

**arXiv:** [arxiv.org/abs/2607.21485](https://arxiv.org/abs/2607.21485)
**Found on:** HuggingFace Daily Papers
**Why trending:** 6 upvotes — a parameter-efficient architectural insight for implicit neural representations.

---

## 18. TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation

**Authors:** Boyuan Wang, Yue Zhang, Xutao Xue, Xueyu Song, Yu Sun

**Summary:** Introduces TableVerse, a Real2Sim pipeline that deterministically reconstructs simulation-ready tabletop environments from unstructured internet images rather than hallucinating layouts, producing physically stable scenes with authentic clutter and topology, paired with an automated trajectory generator for pick-and-place demonstrations. The resulting TableVerse-100K dataset provides 100,000 physically consistent environments with interactive manipulation trajectories for generalizable robotic manipulation research.

**arXiv:** [arxiv.org/abs/2607.21017](https://arxiv.org/abs/2607.21017)
**Found on:** HuggingFace Daily Papers
**Why trending:** 5 upvotes — addresses the realism/scale bottleneck in synthetic manipulation training data.

---

## 19. FinanceComplexQA: Benchmarking Agentic Reasoning on Industrial-grade Financial Documents

**Authors:** Xianfu Cheng, Shiwei Zhang, Jiyu Zhao, Jian Yang, Xinyuan Wang, et al.

**Summary:** Introduces FinanceComplexQA, an open-ended generation benchmark of 2,026 deep-research tasks over 1,009 complex-layout financial documents synthesized via a "Finance-LaTeX SKILL" agent workflow, with bilingual support and Agent-as-a-Judge evaluation. Evaluating leading RAG systems and agentic reasoning tools reveals failure patterns in numerical computation, multi-hop reasoning, summarization, and industry analysis.

**arXiv:** [arxiv.org/abs/2607.19238](https://arxiv.org/abs/2607.19238)
**Found on:** HuggingFace Daily Papers
**Why trending:** 4 upvotes — agentic reasoning benchmarks for high-stakes financial document analysis are an emerging enterprise-AI focus.

---

## 20. GraphVid: Interactive Graph-Controllable Video Generation

**Authors:** Vedant Shah, Onkar Susladkar, Tushar Prakash, Kiet Nguyen, Tianjio Yu, et al.

**Summary:** Proposes GraphVid, a graph-conditioned image-to-video model that enables multi-object interaction control via structured interaction graphs instead of per-object trajectory drawing, which scales poorly and grows ambiguous under occlusion. Trained on the newly curated GraphVid-Bench dataset, it uses substantially less data and fewer parameters than prior motion-control methods while cutting FID by up to 39.9% and FVD by 37.6% versus Motion-I2V.

**arXiv:** [arxiv.org/abs/2607.21580](https://arxiv.org/abs/2607.21580)
**Found on:** HuggingFace Daily Papers
**Why trending:** 2 upvotes — structured graph-based control is a fresh interface paradigm for controllable video generation.
