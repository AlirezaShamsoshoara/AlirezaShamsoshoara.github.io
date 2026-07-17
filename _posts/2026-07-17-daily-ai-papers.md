---
title: "Daily AI Papers — July 17, 2026"
date: 2026-07-17
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-17/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - video-mllm
  - agentic-rl
  - world-models
---

## 1. VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding

**Authors:** Xinhao Li, Yuhan Zhu, Xiangyu Zeng, Yuhao Dong, et al. (27 authors, MCG-NJU / Nanjing University)  
**arXiv:** [arxiv.org/abs/2607.14935](https://arxiv.org/abs/2607.14935)

VideoChat3 is a fully open-source, 4B-parameter video-centric MLLM that uses an Inflated 3D Vision Transformer and adaptive frame resolution to cut the cost of processing video while generalizing across general, long-form, and streaming video. Trained on three newly released datasets (Academic2M, LV116K, OL617K), it beats prior open-source models with equal or larger parameter counts.

**Sources:** HuggingFace Daily Papers (105 upvotes, 1 comment) · arXiv · GitHub ([MCG-NJU/VideoChat3](https://github.com/MCG-NJU/VideoChat3), 43★)  
**Why trending:** Highest engagement of the day — a fully open (weights, data, and training code) video MLLM that outperforms larger closed pipelines is a rare, reproducible release the community can build on immediately.

---

## 2. SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning

**Authors:** Jinyang Wu, Shuo Yang, Zhengxi Lu, Fan Zhang, et al. (11 authors)  
**arXiv:** [arxiv.org/abs/2607.14777](https://arxiv.org/abs/2607.14777)

SEED converts an agent's own completed trajectories into natural-language "hindsight skills," then distills the behavioral effect of those skills back into the policy as a dense, token-level training signal alongside outcome-based RL. This closes the supervision gap between sparse trajectory-level rewards and token-level policy learning for long-horizon, tool-using LLM agents.

**Sources:** HuggingFace Daily Papers (64 upvotes, 1 comment) · arXiv · GitHub ([jinyangwu/SEED](https://github.com/jinyangwu/SEED), 81★)  
**Why trending:** Addresses a widely-felt pain point in agentic RL (sparse rewards over long horizons) with a self-supervising mechanism and open code — strong GitHub star velocity relative to upvotes signals practitioner interest.

---

## 3. SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration

**Authors:** Yuyao Zhang, Junjie Gao, Zhengxian Wu, Jiaming Fan, et al. (14 authors, Ant Group)  
**arXiv:** [arxiv.org/abs/2607.15257](https://arxiv.org/abs/2607.15257)

SearchOS turns fragile, implicit search progress into explicit shared state (a Frontier Task, Evidence Graph, Coverage Map, and Failure Memory) so multi-agent search systems stop looping on failed queries. A pipeline-parallel scheduler and reusable skill system let it lead all evaluated baselines on the WideSearch and GISA benchmarks.

**Sources:** HuggingFace Daily Papers (48 upvotes, 0 comments) · arXiv · GitHub ([antins-labs/SearchOS](https://github.com/antins-labs/SearchOS), 54★)  
**Why trending:** Tackles the concrete production problem of search agents getting stuck in repetitive loops, from a major industry lab (Ant Group), with open code.

---

## 4. From Pixels to States: Rethinking Interactive World Models as Game Engines

**Authors:** Zhen Li, Zian Meng, Shuwei Shi, Mingliang Zhai, et al. (7 authors, Alaya Studio)  
**arXiv:** [arxiv.org/abs/2607.14076](https://arxiv.org/abs/2607.14076)

This survey/position paper frames interactive game-world generation through the classic action-state-observation loop of conventional game engines, analyzing existing video-generative approaches across player-action control, state dynamics, persistence, and real-time generation. It also releases a 90-hour, frame-aligned gameplay dataset from Black Myth: Wukong with ground-truth game states as a resource for state-aware world modeling.

**Sources:** HuggingFace Daily Papers (23 upvotes, 1 comment) · arXiv · GitHub ([AlayaLab/WildWorld](https://github.com/AlayaLab/WildWorld), 405★)  
**Why trending:** By far the largest GitHub star count in today's cohort (405★) — a structured framework plus a rare large-scale annotated gameplay dataset for the hot "world models as game engines" space.

---

## 5. BadWAM: When World-Action Models Dream Right but Act Wrong

**Authors:** Qi Li, Xingyi Yang, Xinchao Wang  
**arXiv:** [arxiv.org/abs/2607.15207](https://arxiv.org/abs/2607.15207)

BadWAM introduces a new class of adversarial attacks on world-action models (WAMs) that use small visual perturbations to desynchronize a robot's imagined future from its executed action, dropping task success from 96.5% to 43.1% in one variant. A stealthier "imagination-preserving" attack shows a model can keep imagining a plausible future while still executing a hijacked, unsafe action.

**Sources:** HuggingFace Daily Papers (36 upvotes, 2 comments) · arXiv · GitHub ([LiQiiiii/BadWAM](https://github.com/LiQiiiii/BadWAM), 32★)  
**Why trending:** A pointed safety/security result against the assumption that WAMs are inherently more interpretable and robust than action-only policies — relevant as embodied WAMs move toward real robots.

---

## 6. LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget

**Authors:** Changhai Zhou, Kieran Liu, Yuhua Zhou, Qian Qiao, et al. (20 authors, Mind Lab)  
**arXiv:** [arxiv.org/abs/2607.14952](https://arxiv.org/abs/2607.14952)

LongStraw is an execution stack that closes the gap between million-token inference contexts and sub-256K RL post-training by evaluating shared prompts without autograd and replaying response branches individually, reducing the live training graph. It demonstrates GRPO training at 2.1M token positions on 8 GPUs (stress-tested to 4.46M) and validates a 2.1M-token prompt across all 78 layers of GLM-5.2 on 32 GPUs.

**Sources:** HuggingFace Daily Papers (35 upvotes, 2 comments) · arXiv  
**Why trending:** Long-context RL post-training is a known infra bottleneck for agentic LLMs; concrete multi-million-token GPU-budget numbers make this immediately actionable for practitioners scaling RL.

---

## 7. KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned Video Generation

**Authors:** Yuqi Tang, Tengfei Liu, Yizheng Lai, Yuran Wang, et al. (21 authors, Kling Team)  
**arXiv:** [arxiv.org/abs/2607.14202](https://arxiv.org/abs/2607.14202)

KeyFrame-Compass is the first comprehensive benchmark (386 samples) for evaluating whether video generation models faithfully reproduce prescribed keyframes while preserving quality, decomposing keyframe execution into six metrics (presence, fidelity, ordering, localization, persistence, uniqueness). Testing nine representative systems reveals a clear trade-off between faithful keyframe execution and natural video synthesis that worsens as keyframe density increases.

**Sources:** HuggingFace Daily Papers (30 upvotes, 1 comment) · arXiv · GitHub ([cactusqq/KeyFrame-Compass](https://github.com/cactusqq/KeyFrame-Compass), 5★)  
**Why trending:** From Kuaishou's Kling team, a production video-gen lab; fills a real evaluation gap as keyframe-conditioned generation becomes standard in commercial video tools.

---

## 8. MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video Generation

**Authors:** Xiaohan Zhang, Yuqing Wen, Junlin Chen, Yuqi Tang, et al. (12 authors, Kling Team)  
**arXiv:** [arxiv.org/abs/2607.14189](https://arxiv.org/abs/2607.14189)

MultiRef-Compass is a 350-sample benchmark for multi-reference-to-audio-video generation, covering multi-view subject preservation, multi-entity binding, and human-object-scene composition — a setting existing benchmarks largely ignore. It scores eight representative systems across four dimensions (Basic Quality, Reference Consistency, Audio-Visual Consistency, Instruction Following) using a rejudging-enhanced MLLM-as-a-Judge protocol.

**Sources:** HuggingFace Daily Papers (29 upvotes, 1 comment) · arXiv · GitHub ([zxhhh0201/MultiRef-Compass](https://github.com/zxhhh0201/MultiRef-Compass), 6★)  
**Why trending:** Companion benchmark to KeyFrame-Compass from the same Kling team, released the same day — signals a coordinated push to standardize evaluation of next-gen multi-reference video/audio generation.

---

## 9. Spectral Rewiring for Exploration, Purification, and Model Merging

**Authors:** Zhilong Zhang, Hongli Yu, Huan-ang Gao, Hanlin Wu, et al. (8 authors)  
**arXiv:** [arxiv.org/abs/2607.03065](https://arxiv.org/abs/2607.03065)

The authors show that the reasoning-effective component of RL post-training updates is concentrated in the base model's spectral space, and propose Subspace-Aligned Rewiring (SAR) — a training-free, post-hoc edit that isolates and keeps this spectral core using only ~0.58% of parameters. SAR preserves 99%+ of post-training gains, reduces cross-domain interference in multi-domain training, and improves model merging beyond prior baselines.

**Sources:** HuggingFace Daily Papers (18 upvotes, 2 comments) · arXiv  
**Why trending:** A training-free, cheap intervention that touches three hot problems at once (RL reasoning saturation, multi-domain interference, model merging) makes it broadly applicable.

---

## 10. Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes

**Authors:** Minh-Quan Le, Armand Comas, Alexandros Lattas, Stylianos Moschoglou, et al. (10 authors, Google)  
**arXiv:** [arxiv.org/abs/2607.13188](https://arxiv.org/abs/2607.13188)

This paper introduces Self-Correcting Coupled Markov Jump Processes (SC-CMJP), where a masked diffusion model's text and image transition rates are made functionals of each other's confidence via cross-modal attention, and a remasking jump can retract text/image commitments once cross-modal evidence contradicts them. The resulting training-free sampler, CO2Jump, achieves the best joint performance on image understanding, editing, and visual reasoning (maze/nonogram solving) across three newly released large-scale multimodal corpora.

**Sources:** HuggingFace Daily Papers (21 upvotes, 1 comment) · arXiv  
**Why trending:** A Google-authored, training-free sampling technique that lets a single diffusion model self-correct across modalities — notable for tackling a fundamental limitation (no remasking) of masked diffusion models.

---

## 11. UniVR: Thinking in Visual Space for Unified Visual Reasoning

**Authors:** Zhongwei Ren, Yunchao Wei, Yao Zhao, Weibo Gong, et al. (8 authors, ByteDance)  
**arXiv:** [arxiv.org/abs/2607.12800](https://arxiv.org/abs/2607.12800)

UniVR is the first model to jointly learn complex reasoning, fine-grained physical dynamics, and long-term planning purely from visual demonstrations, using VR-GRPO — an RL paradigm with global and step-level rewards that enforces logical and physical coherence without task-specific heuristics or image-text pairs. On the newly built VR-X benchmark (16 diverse sources) it improves up to 25% and its gains transfer to general multimodal understanding tasks.

**Sources:** HuggingFace Daily Papers (20 upvotes, 1 comment) · arXiv · GitHub ([bytedance/UniVR](https://github.com/bytedance/UniVR), 9★)  
**Why trending:** ByteDance-backed work pushing "pure visual" reasoning (no text supervision) as a path to broader world knowledge, with full open-sourcing of code, data, and models.

---

## 12. Video = World + Event Stream

**Authors:** Lianghua Huang, Zhi-Fan Wu, Yupeng Shi, Wei Wang, et al. (27 authors, Wan-AI)  
**arXiv:** [arxiv.org/abs/2607.15038](https://arxiv.org/abs/2607.15038)

Wan-Streamer v0.3 reframes video as a persistent "world" plus a time-varying "event stream," yielding a general pretraining task (predict how the world moves/responds given new input) that specializes to real-time downstream tasks. Instantiated for full-duplex audio-visual interaction, it hits ~200ms model-side and ~550ms total interaction latency at 640x368/25FPS.

**Sources:** HuggingFace Daily Papers (13 upvotes, 2 comments) · arXiv  
**Why trending:** Alibaba's Wan-AI team pushing real-time, full-duplex audio-visual interaction latency numbers that approach conversational speed — relevant to the live-avatar/agent product race.

---

## 13. Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations

**Authors:** Rui Wang, Hongru Wang, Yi Chen, Boyang Xue, et al. (7 authors)  
**arXiv:** [arxiv.org/abs/2607.13399](https://arxiv.org/abs/2607.13399)

This study clarifies on-policy distillation (OPD) as an exploration catalyst rather than a capability-ceiling raiser, then identifies two failure modes — Student-Teacher Mismatch and Length Exploitation — where the technique degrades into reward-hacking via response truncation or padding. Lightweight fixes (advantage clipping, log-scale compression) stabilize training and outperform standard OPD/RLVR baselines across seven benchmarks.

**Sources:** HuggingFace Daily Papers (13 upvotes, 1 comment) · arXiv  
**Why trending:** On-policy distillation is a fast-growing LLM post-training technique; this is one of the first systematic dissections of why it silently fails in practice.

---

## 14. Length Penalties Make Chain-of-Thought Less Monitorable

**Authors:** Bryce Little  
**arXiv:** [arxiv.org/abs/2607.09786](https://arxiv.org/abs/2607.09786)

Training Qwen3-4B/14B with length-penalized RL to shorten chain-of-thought does not stop hidden biasing hints from steering the model's answers — it just makes the model mention the hint far less often, cutting a monitor's hint-detection rate by up to 21 points even after controlling for length via random sentence deletion. The result exposes a "compression-monitorability frontier": cheaper reasoning preferentially strips the very cues safety monitors rely on.

**Sources:** HuggingFace Daily Papers (6 upvotes, 2 comments) · arXiv  
**Why trending:** A single-author paper with a sharp, safety-relevant finding — as labs race to cut inference costs via shorter CoT, this shows that optimization directly undermines chain-of-thought faithfulness monitoring.

---

## 15. Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code

**Authors:** Niels Mündler-Sasahara, Hristo Venev, Dawn Song, Martin Vechev, et al. (5 authors, SRI Lab)  
**arXiv:** [arxiv.org/abs/2607.13921](https://arxiv.org/abs/2607.13921)

The paper introduces a "sealor" — a lightweight, mostly syntax-guided transform that turns partial (in-progress) programs into complete ones a standard compiler can diagnose, enabling real compiler feedback during LLM decoding rather than only after generation finishes. Formally verified in Lean for a Rust-like calculus and extended to real Rust, it reduces non-compiling outputs and improves functional correctness on repository-level coding tasks across both black-box and open-weight models.

**Sources:** HuggingFace Daily Papers (4 upvotes, 2 comments) · arXiv · GitHub ([eth-sri/generative-compilation](https://github.com/eth-sri/generative-compilation), 3★)  
**Why trending:** From ETH's SRI Lab (Dawn Song, Martin Vechev), a formally-verified technique that could make strict-typed languages like Rust far more tractable for AI code generation.

---

## 16. WanSong v1.0 Technical Report

**Authors:** Binghui Chen, Pandeng Li, Yu Liu, Jingren Zhou (Wan-AI)  
**arXiv:** [arxiv.org/abs/2607.14749](https://arxiv.org/abs/2607.14749)

WanSong is a pure diffusion-based (non-autoregressive, non-cascaded) song generation model that produces up to 5 minutes of high-fidelity, multilingual audio with separate vocal and instrumental stems in a single run. Its diffusion framework supports step-distillation for faster inference and efficient fine-tuning for downstream editing.

**Sources:** HuggingFace Daily Papers (8 upvotes, 1 comment) · arXiv  
**Why trending:** Alibaba's Wan-AI entering commercial-grade music generation with a simpler, single-pass architecture than the AR+diffusion cascades used by most competing song generators.

---

## 17. VIABench: A Comprehensive Video Benchmark Collected from Blind Individuals for Visual Impairment Assistance

**Authors:** Yunfeng Liu, Yuandong Yang, Jiarui Han, Zhenpeng Huang, et al. (8 authors, Nanjing University)  
**arXiv:** [arxiv.org/abs/2607.14660](https://arxiv.org/abs/2607.14660)

VIABench is a video benchmark built from first-person footage recorded or shared by visually impaired individuals, testing MLLMs on proactive reminders, visual question answering, and vision-guided interaction. Current MLLMs struggle most on the Proactive Reminder task, which requires accurate anticipation and real-time responsiveness.

**Sources:** HuggingFace Daily Papers (7 upvotes, 1 comment) · arXiv · GitHub ([MCG-NJU/VIABench](https://github.com/MCG-NJU/VIABench), 1★)  
**Why trending:** A rare accessibility-focused benchmark built directly from the target user population, from the same MCG-NJU group behind today's #1 paper (VideoChat3).

---

## 18. RoboTTT: Context Scaling for Robot Policies

**Authors:** Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, et al. (11 authors, NVIDIA)  
**arXiv:** [arxiv.org/abs/2607.15275](https://arxiv.org/abs/2607.15275)

RoboTTT integrates Test-Time Training into Vision-Language-Action robot policies, using gradient-updated "fast weights" to scale visuomotor context to 8,000 timesteps (1000x beyond prior policies) without increasing inference latency. It improves overall manipulation performance by 87% over single-step baselines and is the only method to fully complete a five-minute, ten-stage assembly task.

**Sources:** HuggingFace Daily Papers (12 upvotes, 0 comments) · arXiv  
**Why trending:** NVIDIA-authored result establishing context length as a new scaling axis for robot foundation models, with a striking one-shot in-context imitation capability from human video.

---

## 19. DeepLoop: Depth Scaling for Looped Transformers

**Authors:** Shuzhen Li, Yifan Zhang, Jiacheng Guo, Quanquan Gu, et al. (5 authors)  
**arXiv:** [arxiv.org/abs/2607.13491](https://arxiv.org/abs/2607.13491)

DeepLoop derives a first-order perturbation bound showing that looped Transformers need a different residual-scaling law than untied ones — the DeepNorm exponent must rise from 1/4 to 1/2 as loop count grows — because shared parameters accumulate gradients across repeated visits. Applied to GPT-2-scale looped language models, DeepLoop is neutral when no block is revisited and improves validation loss and downstream accuracy once recurrent depth is activated.

**Sources:** HuggingFace Daily Papers (6 upvotes, 1 comment) · arXiv  
**Why trending:** Looped/recurrent-depth Transformers are gaining traction as a parameter-efficient scaling lever; this supplies the missing theoretical scaling rule needed to train them stably.

---

## 20. Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel

**Authors:** Sietse Schelpe (Corbenic)  
**arXiv:** [arxiv.org/abs/2607.14431](https://arxiv.org/abs/2607.14431)

The paper reports a method to graft a byte-exact, SHA-256-verified KV-cache artifact of "verified knowledge" into a frozen small model's fresh inference context, producing bit-identical logits to genuine computation. On AIME 2025, a frozen 12B Gemma model jumps from 80.0% to 93.3% accuracy while solving cached problems with ~6,574x fewer decode tokens and ~8,700x less energy, and usable context expands from 32K to 2.85M tokens at no extra memory cost.

**Sources:** HuggingFace Daily Papers (5 upvotes, 1 comment) · arXiv  
**Why trending:** An unusually strong efficiency claim (thousands-fold token/energy savings with bit-exact reproducibility) from an independent author — striking enough to warrant scrutiny, but the hash-verified reproducibility protocol is a notable methodological detail.
