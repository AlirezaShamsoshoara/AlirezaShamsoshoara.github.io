---
title: "Daily AI Papers — May 19, 2026"
date: 2026-05-19
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-19/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - video-generation
  - multimodal
---

## 1. SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution

**Authors:** Hongyi Liu, Haoyan Yang, Tao Jiang, Bo Tang, Feiyu Xiong, Zhiyu Li (Memtensor Research Group / IAAR-Shanghai)

**Summary:** SkillsVote is a lifecycle-governance framework that treats agent experiences as structured "skills" — pairing executable scripts with procedural guidance — and manages them from collection through recommendation and evidence-gated evolution. It profiles a million-scale open-source corpus for environment requirements and verifiability, then decomposes post-execution trajectories to credit outcomes to specific skills, admitting only successful discoveries into the skill library. Evaluated on Terminal-Bench 2.0 (offline +7.9 pp) and SWE-Bench Pro (online +2.6 pp), showing that governed skill libraries improve frozen agents without any model updates.

**Link:** [arxiv.org/abs/2605.18401](https://arxiv.org/abs/2605.18401)

**Sources:** HuggingFace Daily Papers (#1, 89 upvotes), GitHub (201 ⭐)

**Why trending:** Top-voted HF paper of the day; addresses a critical unsolved problem in agentic AI — governing reusable experience across long-horizon agents without model retraining.

---

## 2. LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation

**Authors:** Yukang Chen, Luozhou Wang, Wei Huang, Shuai Yang, Bohan Zhang, Yicheng Xiao, Ruihang Chu, et al. (NVIDIA)

**Summary:** LongLive-2.0 is the first NVFP4 (4-bit floating-point) training and inference system for long video generation, introducing sequence-parallel autoregressive (Balanced SP) training that pairs clean-history and noisy-target temporal chunks per GPU rank. Unlike prior Self-Forcing methods requiring ODE initialization and DMD distillation, it directly tunes a diffusion model into a long multi-shot autoregressive diffusion model, achieving 45.7 FPS inference on a 5B model with up to 2.15× training speedup and 1.84× inference speedup on Blackwell GPUs.

**Link:** [arxiv.org/abs/2605.18739](https://arxiv.org/abs/2605.18739)

**Sources:** HuggingFace Daily Papers (#2, 86 upvotes), GitHub (1,270 ⭐ — highest of the day)

**Why trending:** NVIDIA paper with 1,270 GitHub stars — by far the most-starred paper today. First NVFP4 video gen system, directly relevant to Blackwell GPU deployments.

---

## 3. Lance: Unified Multimodal Modeling by Multi-Task Synergy

**Authors:** Fengyi Fu, Mengqi Huang, Shaojin Wu, Yunsheng Jiang, Yufei Huo, Hao Li (ByteDance Research)

**Summary:** Lance is a lightweight unified model supporting multimodal understanding, generation, and editing for both images and videos without model capacity scaling or text-image-dominant designs. It employs unified context modeling and decoupled capability pathways via collaborative multi-task training, trained from scratch with a dual-stream mixture architecture that enables cross-modal synergy across tasks like captioning, generation, and editing within a single model.

**Link:** [arxiv.org/abs/2605.18678](https://arxiv.org/abs/2605.18678)

**Sources:** HuggingFace Daily Papers (#3, 59 upvotes), GitHub (259 ⭐)

**Why trending:** ByteDance's answer to unified multimodal modeling — practical multi-task approach without scaling compute, strong community interest with 259 stars same day.

---

## 4. AI for Auto-Research: Roadmap & User Guide

**Authors:** Lingdong Kong, Xian Sun, Wei Chow, Linfeng Li, Kevin Qinghong Lin, Xuan Billy Zhang

**Summary:** A comprehensive survey and roadmap of fully automated AI research systems, noting that papers can now be generated for as little as $15 while long-horizon agents execute experiments, draft manuscripts, and simulate peer review. The paper maps the integrity failures of frontier LLMs in this context — result fabrication, missed errors, unreliable novelty judgment — and provides an end-to-end guide covering developments through April 2026.

**Link:** [arxiv.org/abs/2605.18661](https://arxiv.org/abs/2605.18661)

**Sources:** HuggingFace Daily Papers (#4, 47 upvotes), GitHub (45 ⭐)

**Why trending:** Timely meta-research on autonomous scientific AI — the "$15 paper" framing resonates strongly with ongoing debates about LLM integrity in academia.

---

## 5. Code-as-Room: Generating 3D Rooms from Top-Down View Images via Agentic Code Synthesis

**Authors:** Yixuan Yang, Zhen Luo, Wanshui Gan, Jinkun Hao, Junru Lu, Jinghao Yan (Shanghai AI Lab)

**Summary:** Code-as-Room converts top-down floor plan images into full 3D room layouts by having an MLLM agent synthesize structured code (scene description language) rather than directly predicting object placements, circumventing instability and infinite looping seen in existing image-conditioned generation agents. The code-mediated representation enforces spatial constraints natively and is interpretable and editable, enabling functional room synthesis for interior design, VR, and embodied AI applications.

**Link:** [arxiv.org/abs/2605.18451](https://arxiv.org/abs/2605.18451)

**Sources:** HuggingFace Daily Papers (#5, 34 upvotes), GitHub (22 ⭐)

**Why trending:** Creative code-as-intermediate-representation approach to a hard spatial reasoning problem; Shanghai AI Lab provenance draws attention.

---

## 6. KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration

**Authors:** Ruicheng Zhang, Kaixi Cong, Jun Zhou, Zhizhou Zhong, Zunnan Xu, Shuiyang Mao (Tsinghua University)

**Summary:** KVPO addresses the challenge of aligning streaming autoregressive video generators with human preferences, where existing RL methods use noise-based exploration mismatched to the deterministic ODE dynamics of distilled AR models. It introduces an ODE-native online GRPO approach that explores in KV-cache semantic space rather than noise space, steering high-level storyline coherence rather than low-level pixel appearance in long-horizon video generation.

**Link:** [arxiv.org/abs/2605.14278](https://arxiv.org/abs/2605.14278)

**Sources:** HuggingFace Daily Papers (#6, 33 upvotes), GitHub (12 ⭐)

**Why trending:** Novel RLHF approach specifically designed for autoregressive video models — timely given the push toward real-time interactive video generation.

---

## 7. OProver: A Unified Framework for Agentic Formal Theorem Proving

**Authors:** David Ma, Kaijing Ma, Shawn Guo, Yunfeng Shi, Enduo Zhao, Jiajun Shi (Multimodal Art Projection)

**Summary:** OProver unifies agentic and training-time formal theorem proving in Lean 4, where failed proof attempts are iteratively revised using retrieved compiler-verified proofs and Lean compiler feedback during both training and inference. The framework uses continued pretraining followed by iterative post-training with agentic search loops, closing the gap between inference-only agentic methods and models trained on static proof corpora.

**Link:** [arxiv.org/abs/2605.17283](https://arxiv.org/abs/2605.17283)

**Sources:** HuggingFace Daily Papers (#7, 28 upvotes), GitHub (5 ⭐)

**Why trending:** Formal verification + LLM agents is a hot frontier; integrating agentic search into training (not just inference) is a meaningful architectural advance.

---

## 8. CHI-Bench: Can AI Agents Automate End-to-End, Long-Horizon, Policy-Rich Healthcare Workflows?

**Authors:** Haolin Chen, Deon Metelski, Leon Qi, Tao Xia, Joonyul Lee, Steve Brown (actAVA AI)

**Summary:** χ-Bench (CHI-Bench) introduces a benchmark of long-horizon healthcare workflow tasks stressing three underrepresented capabilities: high policy density (grounding decisions in large medical/insurance rule libraries), multi-role composition (single task requiring multiple role handoffs), and multilateral interaction (multi-turn dialogs like peer review and patient outreach). Current frontier models are benchmarked against realistic end-to-end clinical automation scenarios.

**Link:** [arxiv.org/abs/2605.16679](https://arxiv.org/abs/2605.16679)

**Sources:** HuggingFace Daily Papers (#8, 27 upvotes)

**Why trending:** Healthcare AI benchmark filling a real gap — policy-dense, multi-role workflows are absent from standard agent benchmarks like GAIA or AgentBench.

---

## 9. Post-Trained MoE Can Skip Half Experts via Self-Distillation

**Authors:** Xingtai Lv, Li Sheng, Kaiyan Zhang, Yichen You, Siyan Gao, Xueheng Luo (Tsinghua University)

**Summary:** ZEDA (the method) enables dynamic expert skipping in already fully-trained Mixture-of-Experts language models without pre-training from scratch, using self-distillation to convert a static MoE into a dynamic one that can skip up to 50% of experts for easy tokens. This directly reduces inference FLOPs of deployed MoE models like Mixtral and DeepSeek-MoE without any labeled data or task-specific adaptation.

**Link:** [arxiv.org/abs/2605.18643](https://arxiv.org/abs/2605.18643)

**Sources:** HuggingFace Daily Papers (#9, 25 upvotes), GitHub (13 ⭐)

**Why trending:** Practical inference efficiency for MoE models — skipping half the experts via post-training is immediately deployable on existing models like DeepSeek.

---

## 10. Code as Agent Harness

**Authors:** Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei

**Summary:** This survey introduces "code as agent harness" — a unified view of code not just as LLM output but as the operational substrate for agent reasoning, acting, environment modeling, and execution-based verification. It systematically maps how code functions as the control layer in agentic systems across tool use, memory, planning, and multi-agent coordination, providing a taxonomy and roadmap for the field.

**Link:** [arxiv.org/abs/2605.18747](https://arxiv.org/abs/2605.18747)

**Sources:** HuggingFace Daily Papers (#10, 24 upvotes), GitHub (24 ⭐)

**Why trending:** Conceptual framing paper that clarifies a paradigm shift in how code is used in AI systems — useful reference for the agentic AI community.

---

## 11. LiteFrame: Efficient Vision Encoders Unlock Frame Scaling in Video LLMs

**Authors:** Jihwan Kim, Nikhil Parthasarathy, Danfeng Qin, Junhwa Hur, Deqing Sun, Bohyung Han (Google DeepMind)

**Summary:** LiteFrame identifies that the primary latency bottleneck in Video LLMs is the per-frame vision encoder (not the LLM itself) after post-hoc token reduction, and proposes using lightweight/efficient vision encoders to drastically reduce per-frame encoding cost, enabling processing of far more frames per video. The approach unlocks frame-count scaling that improves long-video understanding without increasing LLM context burden.

**Link:** [arxiv.org/abs/2605.17260](https://arxiv.org/abs/2605.17260)

**Sources:** HuggingFace Daily Papers (#11, 19 upvotes, 3 comments — most discussed in this cohort), GitHub (9 ⭐)

**Why trending:** Google DeepMind paper with a clean insight that shifts the bottleneck analysis for Video LLMs; 3 comments on HF is the highest engagement in this group.

---

## 12. Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models

**Authors:** Dehai Min, Giovanni Vaccarino, Huiyi Chen, Yongliang Wu, Gal Yona, Lu Cheng (University of Illinois Chicago)

**Summary:** PUMA addresses reasoning model "overthinking" — where LRMs like o1/DeepSeek-R1 continue generating chain-of-thought after the answer has stabilized — using semantic-level convergence detection rather than answer-level confidence signals. By monitoring when the semantic content of reasoning stops changing rather than when an answer appears consistent, PUMA exits earlier without degrading accuracy, saving tokens and reducing latency.

**Link:** [arxiv.org/abs/2605.17672](https://arxiv.org/abs/2605.17672)

**Sources:** HuggingFace Daily Papers (#12, 18 upvotes), GitHub (3 ⭐)

**Why trending:** Inference efficiency for reasoning models is a top priority right now; semantic convergence is a more principled exit criterion than existing methods.

---

## 13. Measuring Maximum Activations in Open Large Language Models

**Authors:** Luxuan Chen, Han Tian, Xinran Chen, Rui Kong, Fang Wang, Jiamin Chen (Baidu)

**Summary:** A systematic empirical study of activation magnitude across modern open LLMs (post-2024 LLaMA boom era), establishing how large activations get and how this varies across model families — a first-order constraint for low-bit quantization and stable inference. The findings update the community's picture of outlier features and massive activations that was calibrated on pre-2024 LLaMA-style models, directly informing quantization stack design.

**Link:** [arxiv.org/abs/2605.15572](https://arxiv.org/abs/2605.15572)

**Sources:** HuggingFace Daily Papers (#13, 15 upvotes)

**Why trending:** Practical quantization paper with deployment implications — understanding activation ranges in modern LLMs is essential for INT4/FP8 deployments.

---

## 14. StableVLA: Towards Robust Vision-Language-Action Models without Extra Data

**Authors:** Yiyang Fu, Chubin Zhang, Shukai Gong, Yufan Deng, Kaiwei Sun, Qiyang Min (Peking University)

**Summary:** StableVLA systematically studies robustness failures in state-of-the-art Vision-Language-Action models under unseen visual disturbances (lighting changes, occlusions, sensor noise), finding significant performance drops without any training data containing such disturbances. It proposes robustification techniques that improve VLA model stability without requiring additional training data, making robotics deployments more practical.

**Link:** [arxiv.org/abs/2605.18287](https://arxiv.org/abs/2605.18287)

**Sources:** HuggingFace Daily Papers (#14, 13 upvotes)

**Why trending:** VLA robustness is critical for real-world robotics; the "no extra data" constraint makes this immediately applicable to deployed systems like π0 and OpenVLA.

---

## 15. EndPrompt: Efficient Long-Context Extension via Terminal Anchoring

**Authors:** Han Tian, Luxuan Chen, Xinran Chen, Rui Kong, Fang Wang, Jiamin Chen (Baidu)

**Summary:** EndPrompt achieves effective long-context window extension using only short training sequences by "terminal anchoring" — preserving long-range relative positional distances at sequence ends without constructing full-length inputs, exposing the model to the critical position indices without quadratic memory costs. This sidesteps the expensive RoPE scaling or full-length training required by prior long-context extension methods.

**Link:** [arxiv.org/abs/2605.14589](https://arxiv.org/abs/2605.14589)

**Sources:** HuggingFace Daily Papers (#15, 12 upvotes)

**Why trending:** Cheap long-context extension is highly practical; terminal anchoring is a clever trick that avoids the cost of training on long sequences.

---

## 16. Where Should Diffusion Enter a Language Model? Geometry-Guided Hidden-State Replacement

**Authors:** Injin Kong, Hyoungjoon Lee, Yohan Jo (HOLI-LAB)

**Summary:** DiHAL identifies the optimal transformer layers for diffusion injection using geometry-based proxy scores, replacing the lower transformer prefix with a diffusion bridge while retaining the upper autoregressive layers — addressing why continuous diffusion LMs lag behind AR transformers by operating in poorly-suited embedding spaces. The geometry-guided layer selection avoids the trial-and-error of manual architecture design for diffusion-transformer hybrids.

**Link:** [arxiv.org/abs/2605.14368](https://arxiv.org/abs/2605.14368)

**Sources:** HuggingFace Daily Papers (#16, 12 upvotes)

**Why trending:** Diffusion vs. autoregressive LMs debate is active; this offers a principled hybrid design that explains and partially resolves the performance gap.

---

## 17. Model-Adaptive Tool Necessity Reveals the Knowing-Doing Gap in LLM Tool Use

**Authors:** Yize Cheng, Chenrui Fan, Mahdi JafariRaviz, Keivan Rezaei, Soheil Feiz (University of Maryland)

**Summary:** This paper exposes a "knowing-doing gap" in LLM tool use: models often know whether they need a tool (correct classification) but fail to act accordingly (wrong execution), and tool necessity is model-dependent rather than a fixed property of queries. The study introduces model-adaptive tool necessity annotation and reveals that current benchmarks overestimate agent capability by using model-agnostic necessity labels.

**Link:** [arxiv.org/abs/2605.14038](https://arxiv.org/abs/2605.14038)

**Sources:** HuggingFace Daily Papers (#17, 11 upvotes), GitHub (6 ⭐)

**Why trending:** Diagnostic paper that reframes how we evaluate tool-using agents — knowing-doing gap is an underexplored failure mode with practical implications for agent reliability.

---

## 18. CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection

**Authors:** Jiwon Song, Dongwon Jo, Beomseok Kang, Jae-Joon Kim (Seoul National University VLSI Lab)

**Summary:** CompactAttention addresses the attention bottleneck in chunked prefill serving for long-context LLMs, where existing sparse attention methods (designed for one-shot prefill) lose efficiency when the query is limited to chunk size. It introduces Block-Union KV selection that amortizes KV pattern search across chunks and constructs compact union-of-block attention masks, maintaining sparse attention efficiency throughout chunked prefill without repeated full-cache scans.

**Link:** [arxiv.org/abs/2605.16839](https://arxiv.org/abs/2605.16839)

**Sources:** HuggingFace Daily Papers (#18, 10 upvotes), GitHub (2 ⭐)

**Why trending:** LLM serving efficiency is a core infra concern; chunked prefill + sparse attention is the frontier of production inference optimization.

---

## 19. From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating Full-Stack Web Applications from Requirements

**Authors:** Yuxuan Wan, Tingshuo Liang, Jiakai Xu, Jingyu Xiao, Yintong Huo, Michael R. Lyu (The Chinese University of Hong Kong)

**Summary:** TDDev introduces a multi-agent test-driven development pipeline for generating full-stack web applications that are actually deployable and functionally correct, not just syntactically runnable. The system deploys generated apps in browser environments, runs simulated interactions to catch functional failures, and translates failures into repair signals — addressing the >70% failure rate on functional requirements observed in prior coding agent benchmarks.

**Link:** [arxiv.org/abs/2605.17242](https://arxiv.org/abs/2605.17242)

**Sources:** HuggingFace Daily Papers (#19, 9 upvotes), GitHub (10 ⭐)

**Why trending:** Coding agents for full-stack web apps is an active product area (Cursor, Devin, Claude Code); TDD integration with browser-based testing is a meaningful step toward production-ready agent outputs.

---

## 20. Targeted Neuron Modulation via Contrastive Pair Search

**Authors:** Sam Herring, Jake Naviasky, Karan Malhotra (NousResearch)

**Summary:** Contrastive Neuron Attribution (CNA) identifies the 0.1% of MLP neurons whose activations most distinguish harmful from benign prompts using only forward passes (no gradients or auxiliary models), then modulates those specific neurons to steer model behavior. Unlike residual-stream steering vectors that degrade output coherence at high intervention strength, CNA achieves targeted refusal/compliance steering while preserving fluency, offering a more surgical interpretability-aligned safety tool.

**Link:** [arxiv.org/abs/2605.12290](https://arxiv.org/abs/2605.12290)

**Sources:** HuggingFace Daily Papers (#20, 8 upvotes)

**Why trending:** NousResearch's interpretability work on safety mechanisms is closely watched; surgical neuron-level steering without gradient computation is a practical advance for alignment research.
