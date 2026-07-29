---
title: "Daily AI Papers — July 29, 2026"
date: 2026-07-29
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-29/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - robot-manipulation
  - agentic-search
  - coding-agents
---

## 1. HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone

**Authors:** Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, et al. (Simple AI)

**Summary:** Introduces a portable UMI (universal manipulation interface) data-capture rig with head-mounted stereo-inertial SLAM and dual wide-angle cameras that reaches 3mm end-effector accuracy without external tracking. Policies post-trained solely on this "robot-free" data match real-robot teleoperation performance across three VLA/world-action-model backbones, removing the need for a real-robot data "anchor."

**arXiv:** [arxiv.org/abs/2607.25895](https://arxiv.org/abs/2607.25895)
**Sources:** HuggingFace Daily Papers
**Why trending:** Top-voted paper of the day (110 upvotes) — tackles the costly bottleneck of scaling robot manipulation data and open-sources a 2,000-hour dataset (HiFi-UMI-2K).

---

## 2. A New Role for Relevance: Guiding Corpus Interaction in Agentic Search

**Authors:** Jiangnan Li, Yuqing Li, Mo Yu, Jinchao Zhang, Jie Zhou

**Summary:** Argues that document-level relevance alone can't localize or verify evidence for complex questions, and proposes using relevance signals to guide fine-grained grep-style corpus exploration ("Direct Corpus Interaction") instead of just top-k filtering. This narrows search faster and surfaces useful evidence earlier in agentic retrieval pipelines.

**arXiv:** [arxiv.org/abs/2607.24223](https://arxiv.org/abs/2607.24223)
**Sources:** HuggingFace Daily Papers
**Why trending:** Second-highest engagement (78 upvotes) — directly relevant to the fast-growing agentic-search/RAG space.

---

## 3. ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition

**Authors:** Jooyeol Yun, Jintae Park, Hyesu Lim, Junha Hyung, Hyungjin Chung, Jaegul Choo

**Summary:** Presents an agentic framework that reconstructs editable design files (typography, vector geometry, colors, layering) from a raster image by composing specialized tools with a "graceful verification" step that prevents error accumulation. Introduces the Figma Edit Replay Benchmark (909 files, ~14.8K edit instructions) and beats layered-decomposition baselines on editability.

**arXiv:** [arxiv.org/abs/2607.25565](https://arxiv.org/abs/2607.25565)
**Sources:** HuggingFace Daily Papers
**Why trending:** 53 upvotes — strong practical appeal for design tooling/agentic workflows.

---

## 4. Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory

**Authors:** Ruizhe Li, Mingxuan Du, Benfeng Xu, Zhendong Mao

**Summary:** Identifies a failure mode in long-term memory systems where retrieval assumes a stored memory textually resembles the query needing it (e.g., a tree-nut allergy note won't surface for a macaron request despite the almond-flour link). Introduces a benchmark to measure this "implicit-association blind spot" in agent memory architectures.

**arXiv:** [arxiv.org/abs/2607.24368](https://arxiv.org/abs/2607.24368)
**Sources:** HuggingFace Daily Papers
**Why trending:** 23 upvotes — surfaces a subtle, underexplored gap in the fast-growing agent-memory subfield.

---

## 5. CodeNib: A Multi-View Data System for Serving Repository Context to Coding Agents

**Authors:** Zhongming Yu, Hengjia Yu, Boqin Yuan, Shuting Zhao, et al.

**Summary:** Builds reusable lexical, dense, and structural indexes per repository commit to serve ranked search, symbol navigation, and bounded context to coding agents through a single runtime, avoiding disconnected/rebuilt indexes. Shows 8.7x–25.4x faster incremental updates and 50–87% fewer trajectory tokens versus grep/read baselines across five models.

**arXiv:** [arxiv.org/abs/2607.25431](https://arxiv.org/abs/2607.25431)
**Sources:** HuggingFace Daily Papers
**Why trending:** 22 upvotes — coding-agent infrastructure is a hot topic alongside the related Agent Retrieval Bench paper (#19) released the same window.

---

## 6. Pass the Baton: Trajectory-Relayed On-Policy Distillation

**Authors:** Haolei Xu, Xiaowen Xu, Haiwen Hong, Zixuan Ni, Hongxing Li, Yiwen Qiu, Weiming Lu, Yongliang Shen

**Summary:** Diagnoses "prefix failure" in on-policy distillation, where a student that commits to a wrong reasoning path keeps building on that error. Proposes Relay-OPD, which lets the teacher briefly take over at detected failure points before handing control back to the student, improving Qwen3 students by up to +5.73% on math benchmarks while cutting training trajectory length over 50%.

**arXiv:** [arxiv.org/abs/2607.26057](https://arxiv.org/abs/2607.26057)
**Sources:** HuggingFace Daily Papers
**Why trending:** 21 upvotes — practical, cheap improvement to a widely-used distillation recipe for reasoning models.

---

## 7. Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model

**Authors:** Senqiao Yang, Kaichen Zhang, Zhaoyang Jia, Jinghao Guo, et al.

**Summary:** Targets "Moravec's paradox" in VLMs — strong offline visual reasoning but weak/inefficient streaming perception — with a codec-native tokenizer (Mage-ViT) that selectively encodes motion/entropy-rich regions, cutting visual tokens over 75%. The 4B model matches Qwen3-VL-4B on static tasks while beating a 15B baseline on video/spatial reasoning with up to 3.5x inference speedup.

**arXiv:** [arxiv.org/abs/2607.24904](https://arxiv.org/abs/2607.24904)
**Sources:** HuggingFace Daily Papers
**Why trending:** 21 upvotes — efficient real-time multimodal streaming is a key direction for on-device/agentic vision systems.

---

## 8. Novel Claim or Déjà Vu? Rethinking "Contamination-Free" Dynamic Evaluation for Multimodal Automated Fact-Checking

**Authors:** Haorui He, Xinwen Chen, Dacheng Wen, Reynold Cheng, Francis C. M. Lau, Yupeng Li

**Summary:** Shows that static fact-checking benchmarks risk contamination since claims are often verifiable from an LLM's internal knowledge, inflating scores. Proposes rethinking "dynamic" benchmark construction so claims genuinely require external, up-to-date evidence to test multimodal automated fact-checking systems fairly.

**arXiv:** [arxiv.org/abs/2607.23514](https://arxiv.org/abs/2607.23514)
**Sources:** HuggingFace Daily Papers
**Why trending:** 12 upvotes — timely critique of benchmark validity as fact-checking systems get deployed more widely.

---

## 9. Shieldstral

**Authors:** Antonia Calvi, Avinash Sooriyarachchi, Giada Pistilli, Guillaume Lample, Maarten Buyl, et al. (Mistral)

**Summary:** A 3B-parameter policy-adaptive multimodal safety classifier that reformulates content moderation as a single binary yes/no task, unifying heterogeneous moderation taxonomies under one training framework built from ~54.1M samples. It matches or beats models nearly 7x its size on text safety and sets a new SOTA on multimodal safety classification.

**arXiv:** [arxiv.org/abs/2607.25857](https://arxiv.org/abs/2607.25857)
**Sources:** HuggingFace Daily Papers
**Why trending:** 10 upvotes — from Mistral's safety team (Guillaume Lample among authors), notable for small-model efficiency in trust & safety.

---

## 10. Wonder: Video World Model Done Better

**Authors:** Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei

**Summary:** Presents a real-time, camera-controllable video world model that lets users interactively explore a "playable world" generated from an image or video, with a dense coordinate-field camera conditioning scheme and sparse-attention memory for long-horizon coherence. Synthesizes diverse minute-scale videos at 16 FPS while preserving geometry and dynamics across long rollouts.

**arXiv:** [arxiv.org/abs/2607.26037](https://arxiv.org/abs/2607.26037)
**Sources:** HuggingFace Daily Papers
**Why trending:** 9 upvotes — video world models for interactive exploration are a hot generative-video research direction.

---

## 11. PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models

**Authors:** Zichao Lin, Yifeng Xie, Bowen Qu, Haiming Wang, et al. (large multi-org author list)

**Summary:** Builds a bottom-up benchmark isolating ten "atomic" visual perception capabilities from reasoning/knowledge, using 3,000 verified short-answer questions derived from diagnosing failure points across 42 existing benchmarks. Finds no frontier MLLM exceeds 60% accuracy and that perception-related hallucination is the weakest capability across the board.

**arXiv:** [arxiv.org/abs/2607.24957](https://arxiv.org/abs/2607.24957)
**Sources:** HuggingFace Daily Papers
**Why trending:** 9 upvotes — a sobering, well-constructed benchmark showing basic visual perception is still unsolved in top MLLMs.

---

## 12. MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities

**Authors:** Mingqiao Ye, Zhaochong An, Zhitong Gao, Xian Liu, François Fleuret, et al.

**Summary:** Investigates decoder-only any-to-any multimodal modeling that treats every modality symmetrically as both input and output within one network, letting the model reuse strong pre-trained decoder-only priors instead of training encoder-decoder/diffusion architectures from scratch. Supports chained generation through intermediate modalities and self-verification by cross-checking its own outputs.

**arXiv:** [arxiv.org/abs/2607.25948](https://arxiv.org/abs/2607.25948)
**Sources:** HuggingFace Daily Papers
**Why trending:** 8 upvotes — pushes any-to-any multimodal architecture toward reusing decoder-only LLM priors, a meaningfully different design choice.

---

## 13. Visual prompt engineering for video models

**Authors:** Robert Geirhos, Yuxuan Li, Thaddäus Wiedemer, Neha Kalibhat, Zi Wang, Mani Malek, Oyvind Tafjord, Kevin Swersky, Been Kim, Priyank Jaini

**Summary:** Asks whether video foundation models benefit from "visual prompt engineering" — automatically modifying the input image/scene rather than the text prompt — and finds it improves video reasoning performance, sometimes more than classic text prompt engineering or test-time scaling. Demonstrated on visual physics reasoning tasks where converting sketch-like scenes to photorealistic ones boosts accuracy.

**arXiv:** [arxiv.org/abs/2607.25537](https://arxiv.org/abs/2607.25537)
**Sources:** HuggingFace Daily Papers
**Why trending:** 7 upvotes — notable author list (Been Kim, Robert Geirhos) and a fresh, low-cost technique as video models become reasoning foundation models.

---

## 14. Parallel Decoding Distillation for Fast Image and Video Generation

**Authors:** Neta Shaul, Chao Liu, Arash Vahdat, Julius Berner

**Summary:** Introduces Parallel Decoding Distillation (PDD), a trajectory-based distillation method that predicts multiple denoising steps per network evaluation without the instability of variational score distillation or adversarial losses. Achieves SOTA 4–8 NFE generation on LTX-2.3, Wan 14B, and Qwen-Image while notably preserving video diversity where VSD-based methods suffer mode collapse.

**arXiv:** [arxiv.org/abs/2607.26004](https://arxiv.org/abs/2607.26004)
**Sources:** HuggingFace Daily Papers
**Why trending:** 6 upvotes — practical few-step generation speedup (NVIDIA authors) addressing a known diversity-collapse weakness in prior distillation methods.

---

## 15. OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs

**Authors:** Haoyang Huang, Wenjie Huang, Tianqi Xu, Hongyaoxing Gu, et al.

**Summary:** Tackles token-budget allocation (not just token selection) for compressing long audio-video sequences in omni-modal LLMs, showing raw query-to-media similarity is unreliable for allocating budget across modalities. The training-free method reallocates budget using skill pools and local complexity/redundancy, cutting GPU memory 22% and achieving 1.64x speedup at 25% token retention.

**arXiv:** [arxiv.org/abs/2607.25669](https://arxiv.org/abs/2607.25669)
**Sources:** HuggingFace Daily Papers
**Why trending:** 5 upvotes — addresses a practical inference-cost bottleneck for omni-modal models as audio-video LLMs proliferate.

---

## 16. Where Quality Breaks in Compressed Short-Text Generation: Staged Bottleneck Localization

**Authors:** Alexey Gavrilov, Alan-Barsag Gazzaev, Sergey Muravyov

**Summary:** Studies whether quality loss in compressed-latent text generators comes from the codec discarding information or from the latent generator producing weak codes, using a controlled TinyStories case study with a hierarchical VQ-VAE-2 codec and masked discrete diffusion generator. Proposes a staged validation protocol to separate these failure modes so researchers spend compute fixing the right component.

**arXiv:** [arxiv.org/abs/2607.24176](https://arxiv.org/abs/2607.24176)
**Sources:** HuggingFace Daily Papers
**Why trending:** 3 upvotes — a focused diagnostic methodology relevant to anyone building latent-space text generators.

---

## 17. Towards Robust Reinforcement Learning for Small-Scale Language Model Agents

**Authors:** Md Rezwanul Haque, Md. Milon Islam, Fakhri Karray

**Summary:** Systematically investigates why PPO-based RL alignment is unstable for small (70–500M parameter) language models, identifying three concrete failure modes: silent LoRA freezing, bfloat16 overflow in importance ratios, and reward-model-driven policy collapse. Proposes fixes (adapter merge-reinitialize, float32 PPO updates, reward whitening/importance guarding/weight rollback) that stabilize training and beat instruction-tuned baselines with less data.

**arXiv:** [arxiv.org/abs/2607.25091](https://arxiv.org/abs/2607.25091)
**Sources:** HuggingFace Daily Papers
**Why trending:** 3 upvotes — actionable, reproducible engineering fixes for small-model RL, useful for resource-constrained fine-tuning.

---

## 18. Mapping CVEs to MITRE ATT&CK Techniques: A Curated Gold-Set Classifier and the Limits of LLM-Assisted Label Expansion

**Authors:** Cédric Bonhomme, Alexandre Dulaunoy

**Summary:** Builds a reproducible classifier mapping CVE descriptions directly to MITRE ATT&CK techniques, trained on a curated 1,207-CVE gold set, roughly doubling recall@5 versus zero-shot embedding similarity. Critically, a careful replication study shows LLM-assisted label expansion provides no reliable improvement and can hurt rare-technique coverage — the earlier apparent gain was an evaluation artifact from noisy checkpoint selection.

**arXiv:** [arxiv.org/abs/2607.25572](https://arxiv.org/abs/2607.25572)
**Sources:** HuggingFace Daily Papers
**Why trending:** 2 upvotes — a rigorous negative result on LLM-assisted data labeling, relevant caution for anyone using LLMs to expand training sets.

---

## 19. Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents

**Authors:** Bowen Qin, Yi Xie

**Summary:** Introduces a 427-sample, 25-repository benchmark isolating the upstream context-acquisition stage of coding agents (finding the right files before patch generation), covering four positive-retrieval tasks plus a no-gold/counterfactual selective-retrieval subset. Finds no single retrieval method dominates across tasks and that logged agent trajectories miss every gold file on 27–35% of samples, exposing a real bottleneck upstream of patch quality.

**arXiv:** [arxiv.org/abs/2607.24882](https://arxiv.org/abs/2607.24882)
**Sources:** HuggingFace Daily Papers
**Why trending:** 2 upvotes — complements CodeNib (#5) in probing coding-agent context retrieval, a fast-growing evaluation gap.

---

## 20. VisualPatchWorld: Code World Models as Latent Structured Representations for Planning

**Authors:** Jiaxin Bai, Jiaxuan Xiong

**Summary:** Proposes representing world dynamics as inspectable, editable code rather than opaque neural weights or hand-built physics engines, selecting a qualitative dynamical form via active probes and fitting its parameters from state-action traces. Achieves 69.0% mean planning success, beating the strongest code-based world-model baseline by 23.5 points, with the largest gains where choosing correct dynamics form matters most.

**arXiv:** [arxiv.org/abs/2607.25236](https://arxiv.org/abs/2607.25236)
**Sources:** HuggingFace Daily Papers
**Why trending:** 1 upvote — a distinctive "world-model-as-code" angle bridging neural and symbolic approaches to planning.
