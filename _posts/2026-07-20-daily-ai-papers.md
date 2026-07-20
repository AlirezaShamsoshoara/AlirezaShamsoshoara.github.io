---
title: "Daily AI Papers — July 20, 2026"
date: 2026-07-20
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-20/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-coding
  - reinforcement-learning
  - vision-language-action
---

## 1. Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models

**Authors:** Yubo Wang, Jiarong Liang, Yuxuan Zhang, Xuye Liu, Cong Wei, Yuyu Zhang, Ping Nie, Wenhu Chen

Coding agents must integrate external tool returns into ongoing reasoning, a capability standard left-to-right code pretraining only exposes in the forward direction. The authors note the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, and propose a function-aware fill-in-the-middle mid-training objective (exploiting this pattern at internet scale in ordinary code) to better prime foundation models for agentic coding.

**arXiv:** [arxiv.org/abs/2607.12463](https://arxiv.org/abs/2607.12463)
**Sources:** HuggingFace (trending/recent daily papers, 106 upvotes)
**Why trending:** Highest engagement of any paper surfaced today; addresses a core bottleneck (tool-call reasoning) in coding-agent pretraining, a hot topic given the current push toward agentic coding models.

---

## 2. RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM

**Authors:** Mikhail Komarov, Ivan Bondarenko, Stanislav Shtuka, Oleg Sedukhin, Roman Shuvalov, Yana Dementyeva, Matvey Solovyov, Nikolay O. Nikitin

RAGU is an open-source modular GraphRAG engine that separates knowledge-graph extraction from consolidation, using two-stage typed extraction, DBSCAN-backed deduplication, LLM summarization, and Leiden community detection to reduce the noisy entities and brittle retrieval typical of single-pass GraphRAG systems. The compact domain-adapted LLM at its core allows the pipeline to run efficiently while improving retrieval quality.

**arXiv:** [arxiv.org/abs/2607.11683](https://arxiv.org/abs/2607.11683)
**Sources:** HuggingFace Daily Papers (103 upvotes)
**Why trending:** Top of today's HF Daily Papers leaderboard; GraphRAG remains one of the most actively iterated RAG architectures, and an open-source, modular engine is immediately useful to practitioners.

---

## 3. RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal Resources

**Authors:** Yijia Fan, Zonglin Di, Zimo Wen, Yifan Yang, Mingxi Cheng, Qi Dai, Bei Liu, Kai Qiu, Yue Dong, Ji Li, Chong Luo

RESOURCE2SKILL distills tutorial videos, repositories, articles, and other multimodal human-created resources into executable, reusable skills for software agents, addressing the fact that most existing skill libraries are hand-written or derived only from agent traces. This taps a largely unused data source (human tutorials) to scale up agentic skill libraries.

**arXiv:** [arxiv.org/abs/2606.29538](https://arxiv.org/abs/2606.29538)
**Sources:** HuggingFace Daily Papers (92 upvotes)
**Why trending:** Strong community interest in agent "skill" abstractions and how to bootstrap them cheaply from existing human content rather than costly agent rollouts.

---

## 4. Loop the Loopies!

**Authors:** Zitian Gao, Yilong Chen, Yihao Xiao, Xinyu Yang, Ran Tao, Joey Zhou, Bryan Dai

Introduces Loopie, described as the most powerful looped Transformer to date, released as two MoE variants (20B total/2B active and 6B total/0.6B active parameters). The paper tackles the long-standing finding that looping a model N times underperforms simply scaling parameters by N, presenting ablations showing how Loopie closes that gap.

**arXiv:** [arxiv.org/abs/2607.16051](https://arxiv.org/abs/2607.16051)
**Sources:** HuggingFace Daily Papers (53 upvotes)
**Why trending:** Looped/recurrent-depth Transformers are a hot efficiency research direction; a competitive open MoE loop model with strong ablations draws attention from the compute-efficiency crowd.

---

## 5. Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories

**Authors:** Xiaomi Robotics Team (Jun Guo, Piaopiao Jin, Jason Li, et al. — 30+ authors)

Xiaomi-Robotics-1 is a foundational vision-language-action (VLA) model that follows diverse language instructions for mobile manipulation in unseen environments and adapts efficiently to new tasks with minimal fine-tuning, trained via a two-stage pre-training/post-training recipe on over 100,000 hours of real-world trajectories. It's a successor to the earlier Xiaomi-Robotics-0 model.

**arXiv:** [arxiv.org/abs/2607.15330](https://arxiv.org/abs/2607.15330)
**Sources:** HuggingFace Daily Papers (51 upvotes)
**Why trending:** Large industrial VLA release with an unusually massive real-world trajectory dataset; part of the ongoing wave of big-tech foundation robotics models.

---

## 6. xHC: Expanded Hyper-Connections

**Authors:** Xiangdong Zhang, Xiaohan Qin, Sunan Zou, Tuo Dai, Xiaoming Shi, Huaijin Wu, Yebin Yang, Zhuo Xia, Shaofeng Zhang, Lin Yao, Yuliang Liu, Yu Cheng, Junchi Yan

Hyper-Connections (HC) expand a Transformer's residual stream into N parallel streams for extra memory scaling; this paper investigates why existing HC methods (including Manifold-Constrained HC) stall around N=4 with diminishing returns, and proposes xHC to push residual-stream expansion further as a viable scaling axis.

**arXiv:** [arxiv.org/abs/2607.14530](https://arxiv.org/abs/2607.14530)
**Sources:** HuggingFace Daily Papers (45 upvotes)
**Why trending:** Follows up on the widely-discussed Hyper-Connections line of work on architectural scaling axes beyond width/depth.

---

## 7. Cura 1T: Specialized Model for Agentic Healthcare

**Authors:** actAVA AI (Haolin Chen, Leon Qi, Steve Brown, et al.)

Cura 1T is a healthcare-specialized LLM trained to jointly handle patient consultation, clinical reasoning over text and images, interactive diagnosis, and EHR tool use — capabilities that typically degrade each other when tuned independently. The paper presents a training approach designed to avoid this cross-task interference.

**arXiv:** [arxiv.org/abs/2607.15314](https://arxiv.org/abs/2607.15314)
**Sources:** HuggingFace Daily Papers (38 upvotes)
**Why trending:** Vertical/specialized "agentic healthcare" LLMs are an emerging category, and the multi-capability trade-off framing resonates with practitioners building domain-specific medical AI.

---

## 8. RecGPT-V3 Technical Report

**Authors:** Bowen Zheng, Chao Yi, Dian Chen, Gaoyang Guo, Han Zhu, et al. (Taobao/Alibaba team)

RecGPT-V3 is the third generation of Taobao's production recommender LLM, moving from user-intent-centric modeling (V1) and coordinated multi-agent reasoning (V2) to address challenges around statelessness at scale. It reports continued deployment gains in both user experience and commercial outcomes at Taobao's scale.

**arXiv:** [arxiv.org/abs/2607.15591](https://arxiv.org/abs/2607.15591)
**Sources:** HuggingFace Daily Papers (24 upvotes)
**Why trending:** Rare production-scale technical report on LLM-based recommendation systems with a documented deployment lineage (V1→V3).

---

## 9. On-Policy Delta Distillation

**Authors:** Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han

Proposes a new "delta signal" distillation reward for on-policy RL post-training that gives token-level supervision from a teacher model without directly imitating the teacher's output distribution, addressing limitations of reward-model-constrained on-policy distillation.

**arXiv:** [arxiv.org/abs/2607.15161](https://arxiv.org/abs/2607.15161)
**Sources:** HuggingFace Daily Papers (24 upvotes)
**Why trending:** On-policy distillation is a fast-growing post-training technique (following Google/Anthropic-style approaches); a new reward formulation targets its underexplored fundamentals.

---

## 10. From Human-Centric to Agentic Code Review: The Impact of Different Generations of Generative AI Technology on Review Quality

**Authors:** Suzhen Zhong, Shayan Noei, Bram Adams, Ying Zou

An empirical study on how the shift from human-only code review to AI-supported review — with LLM reviewers and autonomous agent reviewers alongside humans — affects review quality and reviewer workload. The paper provides evidence on this transition that has so far lacked rigorous empirical grounding.

**arXiv:** [arxiv.org/abs/2607.13196](https://arxiv.org/abs/2607.13196)
**Sources:** HuggingFace Daily Papers (23 upvotes)
**Why trending:** Directly relevant to the fast-moving "agentic code review" tooling space (Copilot, Cursor, Devin-style reviewers); empirical rather than product-driven evidence is notable.

---

## 11. Qwen-Music Technical Report

**Authors:** Jin Xu, Kangdi Wang, Ruibin Yuan, Shun Lei, Xiong Wang, et al. (Qwen team, Alibaba)

Qwen-Music is a music generation model producing highly musical, high-fidelity songs with full vocal singing, supporting both text-to-music generation (from text/lyrics/attributes) and cover-song generation that reinterprets existing songs in new styles and voices.

**arXiv:** [arxiv.org/abs/2607.11699](https://arxiv.org/abs/2607.11699)
**Sources:** HuggingFace Daily Papers (16 upvotes)
**Why trending:** Another entry in Alibaba's rapidly-expanding Qwen omni-modal family, extending into music/audio generation shortly after Qwen-Audio-VAE and Qwen3-Omni releases.

---

## 12. Recursive Harness Self-Improvement

**Authors:** Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Matei Zaharia, Yujin Tang

Frames agent harnesses (scaffolds) not just as inference-time wrappers but as data-generating components whose execution traces shape future model training, introducing "harness-in-the-loop learning" that optimizes harnesses for both immediate performance and the quality of future training data.

**arXiv:** [arxiv.org/abs/2607.15524](https://arxiv.org/abs/2607.15524)
**Sources:** HuggingFace Daily Papers (11 upvotes)
**Why trending:** Co-authored by Matei Zaharia (Databricks/Spark); pushes the model–harness co-evolution idea that's gaining traction in agent research circles.

---

## 13. Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy Optimization

**Authors:** Weiwen Xu, Jia Liu, Hou Pong Chan, Long Li, Deng Cai, Min Chen, Hao Zhang

Notes that entropy-based advantage shaping in RLVR cannot distinguish useful uncertainty from detrimental confusion, and proposes Contrastive Policy Optimization (CPO), using token-level contrastive disagreement between reference-guided and vanilla generation distributions as a better correctness signal.

**arXiv:** [arxiv.org/abs/2607.14614](https://arxiv.org/abs/2607.14614)
**Sources:** HuggingFace Daily Papers (8 upvotes)
**Why trending:** Addresses a well-known weakness of entropy-based RLVR advantage shaping, a technique underpinning many current reasoning-model training recipes.

---

## 14. VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders

**Authors:** Zhihao Xie, Junfeng Wu, Xinting Hu, Junchao Huang, Li Jiang

Investigates whether frozen representations from strong video-understanding foundation models (V-JEPA 2, VideoMAEv2) — normally optimized for understanding, not pixel reconstruction — can be turned into compact, reconstruction-capable latents for video generative modeling, as an alternative to conventional 3D-VAEs.

**arXiv:** [arxiv.org/abs/2607.14088](https://arxiv.org/abs/2607.14088)
**Sources:** HuggingFace Daily Papers (7 upvotes)
**Why trending:** Bridges the video-understanding (JEPA-style) and video-generation communities, an increasingly popular crossover research direction.

---

## 15. Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex Videos

**Authors:** Sreyan Ghosh, Arushi Goel, Kaousheik Jayakumar, Lasha Koroshinadze, et al. (NVIDIA)

AV-Flamingo is a fully open audio-visual LLM for joint understanding and reasoning over audio, images, and long-form video, extending NVIDIA's Audio Flamingo lineage beyond short clips into long, complex real-world videos via a new large-scale "Audio-Visual-Skills" training collection.

**arXiv:** [arxiv.org/abs/2607.16107](https://arxiv.org/abs/2607.16107)
**Sources:** HuggingFace Daily Papers (5 upvotes); confirmed as part of NVIDIA's Audio Flamingo research line ([research.nvidia.com/labs/adlr](https://research.nvidia.com/labs/adlr))
**Why trending:** Extends a well-established, widely-used open NVIDIA model family (Audio Flamingo 1–3) into the harder long-video regime.

---

## 16. S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation

**Authors:** Jiahao Zhao, Junyi Liu, Lifeng Xu, Nan Xu, Qingli Wang, et al.

S1-Omni consolidates fragmented AI-for-Science capabilities — domain-specific models, tool-augmented LLMs, scientific language models — into a single coherent model for joint understanding, prediction, and generation across heterogeneous scientific data, laws, and expert knowledge.

**arXiv:** [arxiv.org/abs/2607.15686](https://arxiv.org/abs/2607.15686)
**Sources:** HuggingFace Daily Papers (5 upvotes)
**Why trending:** Part of the growing "AI for Science" unification trend, consolidating previously siloed scientific-AI capabilities into one omni-modal model.

---

## 17. REBASE: Reference-Background Subspace Elimination for Training-Free In-Context Segmentation

**Authors:** Mantha Sai Gopal, Jaison Saji Chacko, Harsh Nandwana, Sandesh Hegde, Debarshi Banerjee, Uma Mahesh

Improves training-free in-context segmentation (introducing new object categories at inference from a single annotated reference image) by addressing the limiting factor in prior vision-foundation-model + SAM pipelines: noisy cross-image similarity maps caused by shared contextual background features.

**arXiv:** [arxiv.org/abs/2607.09082](https://arxiv.org/abs/2607.09082)
**Sources:** HuggingFace Daily Papers (4 upvotes)
**Why trending:** Practical, training-free improvement to a popular SAM-based segmentation workflow, appealing to practitioners who want gains without retraining.

---

## 18. See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models

**Authors:** Byungkun Lee, Dongyoon Hwang, Dongjin Kim, Hojoon Lee, Minho Park, Jaegul Choo

Identifies a frame mismatch in VLA models: actions are defined in the robot's own 3D coordinate frame, but VLAs typically observe the scene in the camera frame, hurting generalization as training data aggregates across viewpoints. Proposes robot-centric pointmaps to align observation and action frames.

**arXiv:** [arxiv.org/abs/2607.11498](https://arxiv.org/abs/2607.11498)
**Sources:** HuggingFace Daily Papers (2 upvotes)
**Why trending:** Targets a subtle but fundamental representation issue in VLA models, complementing the broader wave of VLA scaling papers (e.g., #5 above).

---

## 19. Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning

**Author:** Vladislav Beliaev

Notes that RLVR (e.g., GRPO) grades only final answers, incentivizing longer outputs rather than better reasoning since the trace itself is never graded. Agon has two competing models grade each other's reasoning traces in alternating drafting/critiquing roles, creating an implicit reward signal for the reasoning process itself.

**arXiv:** [arxiv.org/abs/2607.07690](https://arxiv.org/abs/2607.07690)
**Sources:** HuggingFace Daily Papers (2 upvotes)
**Why trending:** A single-author paper proposing a creative fix (adversarial cross-model grading) to the well-known "reward only the final answer" limitation of RLVR reasoning training.

---

## 20. Behavioral Privacy Leakage in Agentic Negotiation: Formalizing and Mitigating Inference Attacks via Randomized Policies

**Author:** Barkha Rani

Studies "behavioral privacy leakage" in autonomous negotiation agents (deployed in insurance, procurement, etc.), where an adversary infers private constraint values not from disclosed data but from observable negotiation dynamics like concession trajectories and timing — a threat cryptographic protections don't address — and proposes randomized-policy mitigations.

**arXiv:** [arxiv.org/abs/2607.06815](https://arxiv.org/abs/2607.06815)
**Sources:** HuggingFace Daily Papers (2 upvotes)
**Why trending:** Raises an underexplored privacy/security risk specific to autonomous negotiation agents, a growing agentic-AI deployment category.
