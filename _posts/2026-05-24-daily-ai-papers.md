---
title: "Daily AI Papers — May 24, 2026"
date: 2026-05-24
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-24/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - llm-reasoning
  - multimodal
---

## #1 — DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards

**Authors:** Kaiyi Zhang, Wei Wu, Yankai Lin

**Summary:** DelTA introduces a discriminator view of RLVR updates, showing that the policy-gradient update direction implicitly acts as a linear discriminator over token-gradient vectors, revealing which tokens actually benefit from rewards. By using this insight to assign fine-grained token-level credit, DelTA significantly improves LLM reasoning performance beyond standard RLVR baselines.

**arXiv:** [arxiv.org/abs/2605.21467](https://arxiv.org/abs/2605.21467)
**Sources:** HuggingFace (192 upvotes), arXiv cs.LG
**Why trending:** Highest-upvoted HF paper of the week; directly addresses one of the core open questions in RLVR — how reward signals propagate to individual tokens — with strong empirical results on reasoning benchmarks.

---

## #2 — TransitLM: A Large-Scale Dataset and Benchmark for Map-Free Transit Route Generation

**Authors:** Hanyu Guo, Jiedong Yang, Chao Chen, Longfei Xu, Kaikui Liu

**Summary:** TransitLM presents a dataset of over 13 million transit route planning records from four Chinese cities (120,845 stations, 13,666 lines) to train LLMs for map-free public transit navigation. Experiments show an LLM trained on this corpus can generate valid routes without relying on structured map infrastructure or routing engines.

**arXiv:** [arxiv.org/abs/2605.22355](https://arxiv.org/abs/2605.22355)
**Sources:** HuggingFace (167 upvotes), arXiv cs.CL
**Why trending:** Massive scale, novel task framing (LLM-native transit planning), and implications for deploying AI navigation in underserved areas without expensive map infrastructure.

---

## #3 — Perception or Prejudice: Can MLLMs Go Beyond First Impressions of Personality?

**Authors:** Caixin Kang, Tianyu Yan, Sitong Gong, Mingfang Zhang, Liangyang Ouyang

**Summary:** This paper introduces Grounded Personality Reasoning (GPR), a new task requiring MLLMs to infer Big Five personality traits from behavioral evidence rather than surface patterns, exposing whether models genuinely perceive personality or rely on superficial bias. Evaluation reveals that current MLLMs largely fall back on visual stereotypes rather than behavioral reasoning, highlighting a fundamental gap in multimodal understanding.

**arXiv:** [arxiv.org/abs/2605.22109](https://arxiv.org/abs/2605.22109)
**Sources:** HuggingFace (162 upvotes), arXiv cs.CV, Reddit r/MachineLearning
**Why trending:** Raises important questions about bias and reliability of MLLMs in high-stakes human-facing applications; the behavioral-evidence framing is a novel and important benchmark design choice.

---

## #4 — π-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows

**Authors:** Haoran Zhang, Luxin Xu, Zhilin Wang, Runquan Gui, Shunkai Zhang

**Summary:** π-Bench introduces a benchmark specifically for evaluating proactive assistance in personal agent workflows, capturing long-horizon, underspecified user tasks where agents must identify unstated needs and act before being asked. The benchmark reveals that even frontier LLM-based agents fail significantly on proactive, multi-step workflows, pointing to a critical gap in current agentic capabilities.

**arXiv:** [arxiv.org/abs/2605.14678](https://arxiv.org/abs/2605.14678)
**Sources:** HuggingFace (91 upvotes), arXiv cs.AI, Reddit r/LocalLLaMA
**Why trending:** Strong relevance to the booming personal agent ecosystem; proactivity is an under-studied yet critical capability, and this benchmark gives the community a rigorous evaluation target.

---

## #5 — Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps

**Authors:** Yanke Zhou, Yiduo Li, Hanlin Tang, Maohua Li, Kan Liu

**Summary:** This work demonstrates that full-attention LLMs are already intrinsically sparse, and that trained dense models can be converted into highly sparse attention models with only ~100 fine-tuning steps — no native sparse training required. The resulting sparse models match full-attention performance at a fraction of the long-context inference cost, eliminating the usual efficiency/accuracy trade-off.

**arXiv:** [arxiv.org/abs/2605.16928](https://arxiv.org/abs/2605.16928)
**Sources:** HuggingFace (85 upvotes), arXiv cs.LG, Papers With Code
**Why trending:** Practical and impactful: eliminates the need to retrain from scratch for sparse attention, making long-context inference cheaper for existing deployed models.

---

## #6 — ACC: Compiling Agent Trajectories for Long-Context Training

**Authors:** Qisheng Su, Zhen Fang, Shiting Huang, Yu Zeng, Yiming Zhao

**Summary:** ACC proposes using agent problem-solving trajectories (tool calls + environment observations spanning many turns) as a natural source of long-context training data, compiling scattered evidence into coherent training examples. Training LLMs on ACC-compiled data substantially improves long-context reasoning without requiring expensive document curation or synthetic context construction.

**arXiv:** [arxiv.org/abs/2605.21850](https://arxiv.org/abs/2605.21850)
**Sources:** HuggingFace (56 upvotes), arXiv cs.CL
**Why trending:** Elegant solution to the long-context training data bottleneck by repurposing what agents already produce; bridges agentic AI and long-context LLM research.

---

## #7 — PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects

**Authors:** Ziang Cao, Yinghao Liu, Haitian Li, Runmao Yao, Fangzhou Hong

**Summary:** PhysX-Omni presents the first unified framework for generating simulation-ready 3D assets across rigid, deformable, and articulated object categories, with physically accurate properties estimated from a novel geometry-aware representation. Unlike prior work limited to one category, PhysX-Omni handles the full diversity of real-world objects applicable to robotics and game simulation.

**arXiv:** [arxiv.org/abs/2605.21572](https://arxiv.org/abs/2605.21572)
**Sources:** HuggingFace (46 upvotes), arXiv cs.CV, Reddit r/MachineLearning
**Why trending:** Robotics and simulation communities have been hungry for physically grounded 3D generation; covering all three object types in one system is a clear step-change over prior art.

---

## #8 — LatentOmni: Rethinking Omni-Modal Understanding via Unified Audio-Visual Latent Reasoning

**Authors:** Yifan Dai, Zhenhua Wu, Bohan Zeng, Daili Hua, Jialing Liu

**Summary:** LatentOmni argues that text-based chain-of-thought in multimodal models is lossy — compressing continuous audio-visual signals into discrete tokens weakens temporal grounding and over-relies on language priors. Instead, the paper proposes reasoning in a unified audio-visual latent space, achieving stronger omni-modal understanding without token-level language mediation.

**arXiv:** [arxiv.org/abs/2605.22012](https://arxiv.org/abs/2605.22012)
**Sources:** HuggingFace (40 upvotes), arXiv cs.CV
**Why trending:** Challenges the dominant text-CoT paradigm in multimodal reasoning; the latent reasoning approach is architecturally novel with strong benchmark results.

---

## #9 — SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers

**Authors:** Javad Rajabi, Kimia Shaban, Koorosh Roohi, David B. Lindell, Babak Taati

**Summary:** SEGA addresses the resolution extrapolation problem in DiTs by using spectral-energy signals to guide attention scaling in a content-aware, frequency-specific way, rather than applying uniform RoPE extrapolation. The method enables training-free high-resolution generation beyond the model's training range with significantly improved visual quality.

**arXiv:** [arxiv.org/abs/2605.22668](https://arxiv.org/abs/2605.22668)
**Sources:** HuggingFace (34 upvotes), arXiv cs.CV
**Why trending:** Resolution extrapolation is a persistent pain point for DiT-based T2I models; training-free approaches that actually work are highly practical for the community.

---

## #10 — Forecasting Scientific Progress with Artificial Intelligence

**Authors:** Sean Wu, Pan Lu, Yupeng Chen, Jonathan Bragg, Yutaro Yamada

**Summary:** The authors introduce CUSP (Cutoff-conditioned Unseen Scientific Progress), a benchmark for evaluating AI's ability to forecast future scientific developments under controlled knowledge cutoffs, spanning feasibility assessment, mechanism prediction, and impact estimation. Results show current AI systems struggle with genuine scientific forecasting, revealing an important gap between retrieval/summarization and anticipation of novel discoveries.

**arXiv:** [arxiv.org/abs/2605.22681](https://arxiv.org/abs/2605.22681)
**Sources:** HuggingFace (34 upvotes), arXiv cs.AI, Hacker News
**Why trending:** Meta-level question about AI's role in science with a rigorous evaluation methodology; timely given the surge in AI-for-science investment.

---

## #11 — WorldKV: Efficient World Memory with World Retrieval and Compression

**Authors:** Jung Yi, Minjae Kim, Paul Hyunbin Cho, Wooseok Jang, Sangdoo Yun

**Summary:** WorldKV tackles the KV-cache explosion problem in autoregressive video diffusion world models by introducing a selective retrieval-and-compression mechanism that maintains long-term scene consistency without unbounded memory growth. The approach enables persistent world generation (revisiting prior viewpoints with consistent content) at real-time speeds.

**arXiv:** [arxiv.org/abs/2605.22718](https://arxiv.org/abs/2605.22718)
**Sources:** HuggingFace (33 upvotes), arXiv cs.CV
**Why trending:** World model consistency is a key unsolved challenge for interactive AI environments; addresses the fundamental memory-efficiency tension head-on.

---

## #12 — Spreadsheet-RL: Advancing LLM Agents on Realistic Spreadsheet Tasks via Reinforcement Learning

**Authors:** Banghao Chi, Yining Xie, Mingyuan Wu, Jingcheng Yang, Jize Jiang

**Summary:** Spreadsheet-RL applies reinforcement learning to train LLM agents for realistic, multi-step spreadsheet manipulation tasks in Excel and Google Sheets, moving beyond prompting-based baselines that fail on complex operations. RL-trained agents significantly outperform prompted LLMs on a new realistic benchmark capturing real enterprise spreadsheet workflows.

**arXiv:** [arxiv.org/abs/2605.22642](https://arxiv.org/abs/2605.22642)
**Sources:** HuggingFace (33 upvotes), arXiv cs.AI, Reddit r/LocalLLaMA
**Why trending:** Spreadsheets are ubiquitous in enterprise workflows; combining RL with computer-use agents for structured data manipulation is a natural next step with immediate practical implications.

---

## #13 — SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation

**Authors:** Xiaolong Zhou, Yifei Liu, Ziyang Gong, Jiarui Li, Qiyue Zhao

**Summary:** SpaceDG is a benchmark that stress-tests MLLM spatial reasoning under real-world visual degradations — motion blur, low light, adverse weather, lens distortion, and compression — that existing spatial benchmarks ignore. Results show dramatic performance drops across leading MLLMs under degraded conditions, revealing a critical robustness gap for deployment.

**arXiv:** [arxiv.org/abs/2605.22536](https://arxiv.org/abs/2605.22536)
**Sources:** HuggingFace (24 upvotes), arXiv cs.CV
**Why trending:** Real-world deployment conditions are rarely ideal; this robustness-focused benchmark fills a genuine blind spot in MLLM evaluation.

---

## #14 — Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving

**Authors:** Jiahao Wang, Bo Sun, Yijing Bai, Vincent Casser, Songyou Peng

**Summary:** Sensor2Sensor learns to convert dashcam footage (cheap, abundant, diverse) into the sensor modalities used by AV fleets (LiDAR, structured cameras), enabling large-scale diverse data to be used for AV training and validation without proprietary sensor collection. The cross-embodiment translation bridges the data gap between consumer and AV-grade sensors.

**arXiv:** [arxiv.org/abs/2605.22809](https://arxiv.org/abs/2605.22809)
**Sources:** HuggingFace (24 upvotes), arXiv cs.CV
**Why trending:** Data diversity is a top bottleneck for AV safety; reusing the vast dashcam data ecosystem is a pragmatic and high-impact direction.

---

## #15 — FlowLong: Inference-time Long Video Generation via Manifold-constrained Tweedie Matching

**Authors:** Jangho Park, Geon Yeong Park, Gihyun Kwon, Jong Chul Ye

**Summary:** FlowLong introduces a manifold-constrained Tweedie matching framework for training-free long video generation that avoids the drift/repetition problems of autoregressive approaches and the architecture coupling of bidirectional extensions. The method produces temporally consistent long videos of arbitrary length at inference time without fine-tuning the base diffusion model.

**arXiv:** [arxiv.org/abs/2605.20910](https://arxiv.org/abs/2605.20910)
**Sources:** HuggingFace (24 upvotes), arXiv cs.CV
**Why trending:** Long video generation without retraining is highly sought after; the Tweedie matching formulation is theoretically principled and architecture-agnostic.

---

## #16 — Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

**Authors:** Ali Hatamizadeh, Yejin Choi, Jan Kautz

**Summary:** Gated DeltaNet-2 proposes a new linear attention architecture that explicitly decouples the erase and write operations in recurrent state updates, using separate learned gates for each to avoid the association-scrambling problem in existing delta-rule models. The design closes the performance gap with softmax attention on language modeling while preserving O(1) memory decoding.

**arXiv:** [arxiv.org/abs/2605.22791](https://arxiv.org/abs/2605.22791)
**Sources:** HuggingFace (21 upvotes), arXiv cs.LG
**Why trending:** Linear attention architectures are rapidly advancing; NVIDIA authorship signals production relevance, and the erase/write decoupling is a principled improvement.

---

## #17 — Q-ARVD: Quantizing Autoregressive Video Diffusion Models

**Authors:** Siao Tang, Xinyin Ma, Gongfan Fang, Xingyi Yang, Xinchao Wang

**Summary:** Q-ARVD is the first systematic study of quantization for autoregressive video diffusion models (ARVDs), identifying unique challenges from their temporal KV-cache reuse and multi-step denoising structure. The proposed quantization-aware calibration strategy achieves near-lossless compression at W4A8, significantly reducing inference cost for streaming video generation.

**arXiv:** [arxiv.org/abs/2605.21072](https://arxiv.org/abs/2605.21072)
**Sources:** HuggingFace (19 upvotes), arXiv cs.CV
**Why trending:** ARVDs are the architecture behind cutting-edge real-time video and world model systems; practical quantization is essential for deployment, and this fills a gap no prior work addressed.

---

## #18 — Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles

**Authors:** Jinyang Wu, Guocheng Zhai, Ruihan Jin, Yuhao Shen, Zhengxi Lu

**Summary:** Maestro uses RL to train an orchestrator that dynamically selects the best LLM and skill combination for each subtask within a hierarchical agent framework, exploiting the complementary strengths of diverse models and tools. Compared to monolithic LLM agents, Maestro achieves substantially better performance on multi-domain agent benchmarks while reducing unnecessary large-model calls.

**arXiv:** [arxiv.org/abs/2605.22177](https://arxiv.org/abs/2605.22177)
**Sources:** HuggingFace (18 upvotes), arXiv cs.AI
**Why trending:** Model/skill routing is an increasingly important systems problem as agents access growing LLM and tool ecosystems; RL-based orchestration is a principled approach with clear scaling benefits.

---

## #19 — GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation

**Authors:** Sixiang Chen, Zhaohu Xing, Tian Ye, Xinyu Geng, Yunlong Lin

**Summary:** GenEvolve enables image generation agents to self-improve over time by distilling visual experience from tool-orchestrated trajectories — combining the model's internal generative capability with external tools — into reusable knowledge. The framework continuously evolves agent performance across diverse generation challenges without requiring human annotation of new training examples.

**arXiv:** [arxiv.org/abs/2605.21605](https://arxiv.org/abs/2605.21605)
**Sources:** HuggingFace (10 upvotes), arXiv cs.CV
**Why trending:** Self-evolving agents for visual generation is a novel paradigm; the trajectory distillation approach is generalizable and aligns with broader interests in autonomous agent improvement.

---

## #20 — KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving

**Authors:** Zedong Liu, Xinyang Ma, Dejun Luo, Hairui Zhao, Bing Lu

**Summary:** KVServe addresses the KV cache communication bottleneck in disaggregated LLM serving (prefill/decode separation) by introducing dynamic, service-aware compression that adapts to real-time workload mix, available bandwidth, and SLO requirements. The system reduces KV transfer overhead by up to 4× with negligible quality degradation, improving end-to-end serving throughput.

**arXiv:** [arxiv.org/abs/2605.13734](https://arxiv.org/abs/2605.13734)
**Sources:** HuggingFace (10 upvotes), arXiv cs.DC
**Why trending:** Disaggregated serving is the dominant production architecture for large LLMs; practical KV compression that respects SLOs is a high-value engineering contribution.
