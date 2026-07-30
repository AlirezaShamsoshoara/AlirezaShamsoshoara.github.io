---
title: "Daily AI Papers — July 30, 2026"
date: 2026-07-30
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-30/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - robot-manipulation
  - agentic-rl
  - ai-security
---

## 1. TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM

**Authors:** Hengyi Xie, Chenfei Yao, Xianjin Wu, Xuanyang Xi, Yiping Tang, Di Xu, et al.

**Summary:** TurboVLA reformulates the conventional vision→language→action pipeline used by robotics foundation models into a direct vision+language→action mapping, cutting out the heavy LLM-centric decoding step. This lets it run robot control policies at 32 Hz on a single consumer RTX 4090 while using under 1 GB of VRAM, dramatically lowering the hardware bar for real-time embodied AI.

**arXiv:** [arxiv.org/abs/2607.27205](https://arxiv.org/abs/2607.27205)
**Sources:** HuggingFace Daily Papers (117 upvotes, top-ranked today), GitHub ([H-EmbodVis/TurboVLA](https://github.com/H-EmbodVis/TurboVLA), 64 stars)
**Why trending:** Highest upvote count of the day by a wide margin; strong community interest in making VLA robotics models cheap and consumer-hardware friendly.

---

## 2. CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization

**Authors:** Bo-Wen Zhang, Junwei He, Wen Wang, Song-Lin Lv, Wentao Ma, Rongyi Lin, et al. (ByteDance)

**Summary:** CoRT tackles a known weakness in GRPO-style RL for LLMs, where rubric-based rewards collapse into a single scalar broadcast uniformly across every generated token, losing fine-grained credit assignment. It introduces counterfactual replay to attribute rewards at the token level, aligning specific spans and formatting decisions with the rubric criteria that judged them.

**arXiv:** [arxiv.org/abs/2607.25659](https://arxiv.org/abs/2607.25659)
**Sources:** HuggingFace Daily Papers (72 upvotes), ByteDance research org
**Why trending:** Second-highest upvotes; addresses a widely-discussed limitation of rubric/GRPO-based RLHF pipelines.

---

## 3. HumanCLAW: Can Vision-Language Models Act Through a Body?

**Authors:** Siyao Li, Jiawei Gu, Shuai Liu, Kairui Hu, Zekun Li, Linjie Li, et al. (Meta Research)

**Summary:** HumanCLAW is an evaluation framework that decouples a VLM's high-level decision-making from a separate low-level motor controller, so failures can be attributed to bad choices versus execution errors (e.g., losing balance). It provides a cleaner benchmark for measuring embodied reasoning in humanoid-style agents independent of controller quality.

**arXiv:** [arxiv.org/abs/2607.27180](https://arxiv.org/abs/2607.27180)
**Sources:** HuggingFace Daily Papers (64 upvotes), Meta Research org, GitHub ([Human-CLAW/HumanCLAW](https://github.com/Human-CLAW/HumanCLAW), 32 stars)
**Why trending:** Strong upvotes plus Meta FAIR authorship; timely contribution to embodied-agent evaluation methodology.

---

## 4. DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space

**Authors:** Jiangwang Chen, Zixin Song, Junlin Liu, Shuaiyu Zhou, Haiyan Wu, Haihan Shi, et al. (Qwen Business Unit)

**Summary:** DecoEvo optimizes LLMs by co-evolving both the "solver" and the "rubric-generator" in natural-language (text-space) form rather than model weights, keeping both interpretable and inspectable. It targets the bottleneck where a fixed rubric stops rewarding improvements once the solver has saturated the criteria it measures.

**arXiv:** [arxiv.org/abs/2607.25675](https://arxiv.org/abs/2607.25675)
**Sources:** HuggingFace Daily Papers (53 upvotes), Qwen Business Unit (Alibaba)
**Why trending:** High upvotes; part of a cluster of rubric/text-space optimization papers trending together today, signaling a hot subfield.

---

## 5. CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition

**Authors:** Lai Wei, Chengqi Li, Jiapeng Li, Ruina Hu, Yue Wang, Weiran Huang

**Summary:** CLBench-V introduces a benchmark for "context learning" — a model's ability to learn from task-specific context rather than pretrained knowledge alone — extended to multimodal inputs like figures, tables, and maps. It covers a spectrum from basic visual grounding up to knowledge acquisition from mixed-modality context.

**arXiv:** [arxiv.org/abs/2607.25294](https://arxiv.org/abs/2607.25294)
**Sources:** HuggingFace Daily Papers (40 upvotes), GitHub ([IamLihua/CLBench-V](https://github.com/IamLihua/CLBench-V))
**Why trending:** Solid upvote count; fills an evaluation gap as multimodal in-context learning becomes more central to agentic systems.

---

## 6. CAST: Game Solvers as Turn-Level Teachers for LLM Agents

**Authors:** Yu Wang, Yi-Kai Zhang, Wentao Shi, Ziang Ye, Yuchun Miao, Yueqing Sun, et al. (LongCat/Meituan)

**Summary:** CAST uses classical game solvers to supply dense, turn-level credit signals to LLM agents training on long-horizon games, replacing the sparse final-reward-only signal typical of RLVR. Changes in the solver's state-value function indicate whether an agent's action moved it closer to or further from winning.

**arXiv:** [arxiv.org/abs/2607.25308](https://arxiv.org/abs/2607.25308)
**Sources:** HuggingFace Daily Papers (27 upvotes), GitHub ([Wloner0809/CAST](https://github.com/Wloner0809/CAST))
**Why trending:** Notable engagement; addresses the sparse-reward problem central to agentic RL research.

---

## 7. SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution

**Authors:** Zhiyuan Yao, Yuxin Chen, Zhengxi Lu, Zishan Xu, Yueqing Sun, Yifu Guo, et al.

**Summary:** SkillRise is a unified RL framework that lets LLM agents extract and reuse skills across related but distinct tasks, rather than treating every task episode independently. It unifies skill extraction, retrieval, and execution into a single training loop instead of separate disjoint stages.

**arXiv:** [arxiv.org/abs/2607.26784](https://arxiv.org/abs/2607.26784)
**Sources:** HuggingFace Daily Papers (18 upvotes), GitHub ([Within-yao/SkillRise](https://github.com/Within-yao/SkillRise))
**Why trending:** Growing community interest in transferable agentic skills as a step toward more general-purpose LLM agents.

---

## 8. StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation

**Authors:** Zijun Lin, Zeqing Wang, Cheston Tan, Bihan Wen, Yeying Jin

**Summary:** StatePlay adds explicit internal game-state tracking (health points, skill meters, timers) to interactive game world models, which today mostly generate visually plausible but mechanically inconsistent gameplay. This keeps generated game rollouts consistent with the actual rules governing health loss, skill activation, and termination.

**arXiv:** [arxiv.org/abs/2607.26754](https://arxiv.org/abs/2607.26754)
**Sources:** HuggingFace Daily Papers (12 upvotes), GitHub ([Jimntu/StatePlay](https://github.com/Jimntu/StatePlay))
**Why trending:** Part of a broader wave of interest in controllable, playable generative world models.

---

## 9. Can AI agents conduct open-ended AI research? Early evidence from two case studies

**Authors:** Peter Kirgis, Sayash Kapoor, Andrew Schwartz, Stephan Rabanser, David Africa, Konstantinos Voudouris, et al.

**Summary:** This paper proposes a new methodology for measuring progress toward automated AI R&D — sidestepping both narrow verifiable-task benchmarks and noisy blind peer review — by having agents take on genuinely open-ended research projects and assessing them directly. It reports early case-study evidence on how far current agents get toward independent AI research.

**arXiv:** [arxiv.org/abs/2607.27191](https://arxiv.org/abs/2607.27191)
**Sources:** HuggingFace Daily Papers (9 upvotes)
**Why trending:** Directly addresses one of the most consequential open questions in AI safety/forecasting circles: whether agents can automate AI research itself.

---

## 10. OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding

**Authors:** Jingbo Zhou, Yusai Zhao, Qi Bao, Jingjia Cao, Zhenghai Chen, Chang Gao, et al. (Baidu Frontier Research)

**Summary:** OmegaUse-OfficeVal benchmarks LLM agents on 100 realistic, long-horizon office-suite workflows (documents, spreadsheets, presentations) derived from practitioner requests, adding explicit economic/cost grounding to each task. It targets whether agents can complete real productivity work at a reasonable operating cost, not just whether they can complete it at all.

**arXiv:** [arxiv.org/abs/2607.27155](https://arxiv.org/abs/2607.27155)
**Sources:** HuggingFace Daily Papers (7 upvotes), GitHub ([baidu-frontier-research/OmegaUse-OfficeVal](https://github.com/baidu-frontier-research/OmegaUse-OfficeVal))
**Why trending:** Relevant to the enterprise-agent evaluation wave; economic grounding is a fresh angle other office benchmarks lack.

---

## 11. Explicit Layer Modeling for Video Object Insertion and Layer Decomposition

**Authors:** Kyujin Han, Seungjoo Shin, Sunghyun Cho

**Summary:** This work introduces TriLayer, a large-scale triplet video dataset with aligned composite/foreground/background layers, to give video editing models explicit layered supervision that's been missing. This enables more realistic object insertion, object reuse, and layer decomposition in video editing pipelines.

**arXiv:** [arxiv.org/abs/2607.25802](https://arxiv.org/abs/2607.25802)
**Sources:** HuggingFace Daily Papers (5 upvotes), GitHub ([KyujinHan/DBL-Diffusion](https://github.com/KyujinHan/DBL-Diffusion)), POSTECH Computer Graphics Lab
**Why trending:** Fills a concrete dataset gap in generative video editing, an active applied-research area.

---

## 12. Memory for Large Language Models

**Authors:** Sining Zhoubian, Dan Zhang, Evgeny Kharlamov, Jie Tang (Tsinghua KEG)

**Summary:** This is a systematic survey of LLM memory mechanisms, unifying transient attention, recurrent state dynamics, parameter-efficient adaptation, and scalable lookup storage into a single architecture-centric taxonomy. It aims to bring order to what the authors describe as a highly fragmented research landscape around LLM memory.

**arXiv:** [arxiv.org/abs/2607.25380](https://arxiv.org/abs/2607.25380)
**Sources:** HuggingFace Daily Papers (4 upvotes), Tsinghua Knowledge Engineering Group
**Why trending:** Survey papers on LLM memory are in high demand as agentic systems increasingly need long-term persistent memory (directly relevant to memory-architecture debates happening across the field).

---

## 13. GPT-Red: Automated Red Teaming via Self-Play at Scale

**Authors:** Eric Wallace, Christopher A. Choquette-Choo, Nikhil Kandpal, Sam Toyer, Dylan Hunn, Stephanie Lin, et al. (OpenAI)

**Summary:** GPT-Red is an automated red-teaming agent trained via large-scale self-play to discover novel prompt-injection attacks against frontier LLMs. OpenAI used it to adversarially harden GPT-5.6 against prompt injection, reporting it as their most robust model to date against this attack class.

**arXiv:** [arxiv.org/abs/2607.26115](https://arxiv.org/abs/2607.26115)
**Sources:** HuggingFace Daily Papers (4 upvotes), OpenAI research org
**Why trending:** OpenAI authorship and direct relevance to production LLM security against prompt injection — a top concern for anyone deploying agents.

---

## 14. CADENCE: Closing the Reasoning Gap via Coverage-Adaptive On-Policy Distillation

**Authors:** Satyam Kumar, Saurabh Jha

**Summary:** CADENCE improves on-policy knowledge distillation from large reasoning models to compact students by fixing three failure modes: cold-start collapse, state-agnostic KL-divergence scheduling, and binary reward sparsity. It adapts the distillation signal based on the student's current coverage state rather than using a fixed schedule.

**arXiv:** [arxiv.org/abs/2607.16955](https://arxiv.org/abs/2607.16955)
**Sources:** HuggingFace Daily Papers (3 upvotes)
**Why trending:** Practical relevance to teams distilling reasoning models into smaller, cheaper deployable models.

---

## 15. StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents

**Authors:** Ads Dawson, Adrian Wood

**Summary:** StealthBench measures whether autonomous offensive-security agents can operate without revealing their presence, capabilities, or collected intelligence — the tradecraft that separates elite human operators from detectable ones. It benchmarks agents across scenarios designed to test operational stealth rather than just task completion.

**arXiv:** [arxiv.org/abs/2607.26314](https://arxiv.org/abs/2607.26314)
**Sources:** HuggingFace Daily Papers (2 upvotes), GitHub ([GangGreenTemperTatum/stealthbench](https://github.com/GangGreenTemperTatum/stealthbench))
**Why trending:** Timely as autonomous red-team/offensive-security agents become more capable; relevant to defensive security researchers tracking this threat surface.

---

## 16. Grading the Narrators: An Isnad-Rijal Framework for Claim-Level Provenance in Multi-Agent Knowledge Systems

**Authors:** Ali Zahid Raja

**Summary:** This paper adapts the classical Islamic scholarly Isnad-Rijal framework (used to grade the reliability of hadith transmission chains) into a computational method for tracking claim-level provenance across multi-agent knowledge systems. It attaches graded, per-domain transmitter reliability scores to chains of autonomous knowledge transformations, going beyond simple execution-trace logging.

**arXiv:** [arxiv.org/abs/2607.24117](https://arxiv.org/abs/2607.24117)
**Sources:** HuggingFace Daily Papers (2 upvotes), GitHub ([alizahidraja/isnad](https://github.com/alizahidraja/isnad), 21 stars)
**Why trending:** Notable for its novel, interdisciplinary framing — applying centuries-old epistemological tooling to modern multi-agent trust/provenance problems.

---

## 17. SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response

**Authors:** Lehan Wang, Boli Chen, Ruixue Ding, Pengjun Xie, Jinwei Huang, Zhendong Liu, et al. (Alibaba-NLP)

**Summary:** SecRespond is the first benchmark focused on the post-compromise setting for LLM security agents — i.e., after an attacker already has a foothold — rather than the clean pre-compromise environments most cybersecurity benchmarks use. It evaluates agents' ability to investigate, contain, and respond to real-world incident-response scenarios via CLI access.

**arXiv:** [arxiv.org/abs/2607.26791](https://arxiv.org/abs/2607.26791)
**Sources:** HuggingFace Daily Papers (1 upvote), Alibaba-NLP org
**Why trending:** Addresses a clear evaluation gap in AI-for-security-operations, complementary to StealthBench's offensive-side focus.

---

## 18. πR²: Reactive Real-time Flow Policies

**Authors:** Sungjae Park, Shubham Tulsiani (Carnegie Mellon University)

**Summary:** πR² addresses the reactivity gap in action-chunking flow policies for robot manipulation, where large backbones and multi-step denoising make replanning too slow to react to mid-execution sensory input. It proposes a faster reactive flow-policy design that can replan frequently enough to stay responsive during execution.

**arXiv:** [arxiv.org/abs/2607.26055](https://arxiv.org/abs/2607.26055)
**Sources:** HuggingFace Daily Papers (1 upvote), GitHub ([pi-r2-flow/pi-r2-flow](https://github.com/pi-r2-flow/pi-r2-flow)), CMU School of Computer Science
**Why trending:** Speaks to a core limitation (latency vs. reactivity) in the fast-moving generalist-manipulation-policy space alongside TurboVLA.

---

## 19. Voice Memory for Agentic Speech Recognition

**Authors:** Chao-Han Huck Yang, Zih-Ching Chen, Piotr Zelasko, Zhehuai Chen, Jagadeesh Balam, Boris Ginsburg (NVIDIA)

**Summary:** Voice Memory is an inference-only scheme where a frozen "corrector" model reads a small per-domain memory file to decide, per utterance, whether to correct or abstain from correcting an ASR hypothesis. A separate score-gated optimizer asynchronously edits that memory file, accepting only edits that provably improve a held-out score — a listener-thinker split inspired by classical ASR-LM architectures.

**arXiv:** [arxiv.org/abs/2607.26410](https://arxiv.org/abs/2607.26410)
**Sources:** HuggingFace Daily Papers (0 upvotes, freshly posted), GitHub ([huckiyang/voice-memory-notebook](https://github.com/huckiyang/voice-memory-notebook)), NVIDIA org
**Why trending:** NVIDIA authorship and a novel, lightweight take on agentic memory applied specifically to speech recognition rather than text.

---

## 20. Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?

**Authors:** Perry Dong, Ron Polonsky, Dorsa Sadigh, Chelsea Fin (Stanford)

**Summary:** This paper systematically studies whether pretraining the Q-function actually helps when fine-tuning a pretrained policy with online RL, challenging the conventional assumption that it should. It finds that online RL starting from a randomly-initialized Q-function can, in several settings, match or exceed the performance of pretrained-Q-function pipelines.

**arXiv:** [arxiv.org/abs/2607.27203](https://arxiv.org/abs/2607.27203)
**Sources:** arXiv cs.AI recent listing (not yet on HuggingFace Daily Papers as of this report)
**Why trending:** Directly challenges established practice in value-based RL fine-tuning from well-known Stanford robotics/RL researchers (Sadigh, Finn labs); topically significant even without an engagement-signal footprint yet, since it questions a widely-assumed best practice.
