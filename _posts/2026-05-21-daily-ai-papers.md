---
title: "Daily AI Papers — May 21, 2026"
date: 2026-05-21
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-21/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reasoning-rl
  - multimodal
  - llm-efficiency
---

## #1 — Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information

**Authors:** Guobin Shen, Xiang Cheng, Chenxiao Zhao, Lei Huang, Jindong Li

**Summary:** On-policy self-distillation for reasoning RL often fails in math because the privileged context (e.g., verified solutions) inflates teacher confidence on already-implied tokens, producing a suboptimal training signal. This paper introduces Anti-Self-Distillation (ASD), using pointwise mutual information to suppress the teacher's over-confident tokens and sharpen focus on genuine deliberation tokens, yielding consistent gains across math and reasoning benchmarks without an external teacher.

**arxiv:** [arxiv.org/abs/2605.11609](https://arxiv.org/abs/2605.11609)

**Sources:** HuggingFace Daily Papers (117★), r/MachineLearning, X/Twitter

**Why trending:** Highest community engagement of the week; addresses a fundamental failure mode in reasoning RL that affects all RLVR-trained models like DeepSeek-R1 and Qwen. PMI-based fix is elegant and immediately applicable.

---

## #2 — Mega-ASR: Towards In-the-wild² Speech Recognition via Scaling up Real-world Acoustic Simulation

**Authors:** Zhifei Xie, Kaiyu Pang, Haobin Zhang, Deheng Ye, Xiaobin Hu

**Summary:** Current ASR models suffer from an "acoustic robustness bottleneck" — they hallucinate or omit words under severe, compositional real-world distortions (noise, reverb, codec artifacts combined). Mega-ASR introduces a scalable compound-data construction pipeline paired with progressive acoustic-to-semantic optimization, significantly closing the gap between lab-tested and truly in-the-wild ASR performance.

**arxiv:** [arxiv.org/abs/2605.19833](https://arxiv.org/abs/2605.19833)

**Sources:** HuggingFace Daily Papers (108★), r/MachineLearning, X/Twitter

**Why trending:** Top paper submitted today on HF; real-world ASR robustness is a long-standing pain point, and "in-the-wild²" framing (compositional, not just additive noise) resonates strongly with practitioners.

---

## #3 — When Vision Speaks for Sound

**Authors:** Xiaofei Wen, Wenjie Jacky Mo, Xingyu Fu, Rui Cai, Tinghui Zhu

**Summary:** State-of-the-art video MLLMs — including models from Google and OpenAI — exhibit an "audio-visual Clever Hans effect": they appear to understand audio but are actually exploiting visual-acoustic correlations without genuinely processing the audio stream. The paper systematically characterizes this failure across open-source and closed models and proposes evaluation protocols to distinguish real audio understanding from vision-driven confabulation.

**arxiv:** [arxiv.org/abs/2605.16403](https://arxiv.org/abs/2605.16403)

**Sources:** HuggingFace Daily Papers (93★), r/MachineLearning, r/LocalLLaMA, X/Twitter

**Why trending:** Exposes a critical reliability flaw in widely-deployed multimodal models; the "Clever Hans" analogy made it highly shareable on social media and relevant to anyone building on video-capable LLMs.

---

## #4 — Active Learners as Efficient PRP Rerankers

**Authors:** Jeremías Figueiredo Paschmann, Juan Kaplan, Francisco Nattero, Santiago Barron, Juan Wisznia

**Summary:** Pairwise Ranking Prompting (PRP) for LLM-based reranking typically uses classical sorting algorithms that assume transitive, consistent comparisons — assumptions that don't hold for noisy LLM judgments. This work reframes PRP as active learning from noisy pairwise comparisons, showing that active rankers are drop-in replacements that improve NDCG@10 per LLM call within a fixed call budget.

**arxiv:** [arxiv.org/abs/2605.14236](https://arxiv.org/abs/2605.14236)

**Sources:** HuggingFace Daily Papers (90★), r/MachineLearning, Papers With Code

**Why trending:** Directly improves cost-efficiency of LLM-based reranking pipelines, a core component in RAG and search systems; clean algorithmic contribution with immediate practical impact.

---

## #5 — Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining

**Authors:** Weimin Xiong, Shuhao Gu, Bowen Ye, Zihao Yue, Lei Li

**Summary:** GUI agent generalization is bottlenecked by scarce, domain-narrow training data that requires costly manual annotation. Video2GUI is a fully automated framework that extracts grounded GUI interaction trajectories directly from screen-recording videos, enabling large-scale pretraining data synthesis across diverse real-world applications without human labeling.

**arxiv:** [arxiv.org/abs/2605.14747](https://arxiv.org/abs/2605.14747)

**Sources:** HuggingFace Daily Papers (80★), r/MachineLearning, r/LocalLLaMA, X/Twitter

**Why trending:** Scalable data synthesis for GUI agents is a key bottleneck; the video-to-trajectory approach is novel and the framework is fully automated, making it immediately usable for building computer-use agents.

---

## #6 — Enhancing Train-Free Infinite-Frame Generation for Consistent Long Videos

**Authors:** X. Feng, J. Zhu, M. Wu, C. Chen, F. Mao

**Summary:** Train-free long video generation using frame-level autoregressive frameworks (e.g., FIFO-diffusion) suffers from train/inference mismatch and long-term consistency degradation. This paper identifies the root causes and introduces targeted fixes — including attention windowing and consistency regularization — that allow foundation video models to generate coherent infinite-length videos without any fine-tuning.

**arxiv:** [arxiv.org/abs/2605.18233](https://arxiv.org/abs/2605.18233)

**Sources:** HuggingFace Daily Papers (75★), r/MachineLearning, r/LocalLLaMA, X/Twitter

**Why trending:** Train-free infinite video generation is immediately deployable on existing models; strong community interest in extending video generation to arbitrary lengths without retraining costs.

---

## #7 — OpenComputer: Verifiable Software Worlds for Computer-Use Agents

**Authors:** Jinbiao Wei, Qianran Ma, Yilun Zhao, Xiao Zhou, Kangqi Ni

**Summary:** OpenComputer provides a verifier-grounded framework for constructing verifiable software environments for evaluating and training computer-use agents, integrating app-specific state verifiers, self-evolving verification, realistic task generation, and auditable partial-credit reward computation. It enables reliable, reproducible benchmarking of desktop automation agents on real applications like browsers and office software.

**arxiv:** [arxiv.org/abs/2605.19769](https://arxiv.org/abs/2605.19769)

**Sources:** HuggingFace Daily Papers (54★), r/MachineLearning, r/LocalLLaMA, X/Twitter

**Why trending:** Computer-use agents are a hot research area; verifiable environments with ground-truth reward signals are exactly what the field needs for rigorous RL training and evaluation.

---

## #8 — GoLongRL: Capability-Oriented Long Context Reinforcement Learning with Multitask Alignment

**Authors:** Minxuan Lv, Tiehua Mei, Tanlong Du, Junmin Chen, Zhenpeng Su

**Summary:** GoLongRL is a fully open-source post-training recipe for long-context RLVR that addresses homogeneous task coverage in existing methods through capability-oriented data construction with 23K open-release samples. It introduces multitask alignment to ensure RL training on long-context tasks doesn't degrade other model capabilities.

**arxiv:** [arxiv.org/abs/2605.19577](https://arxiv.org/abs/2605.19577)

**Sources:** HuggingFace Daily Papers (53★), r/MachineLearning, r/LocalLLaMA

**Why trending:** Fully open release of 23K RLVR samples + pipeline is a community resource; long-context RL is a critical frontier for extending model capabilities beyond typical context windows.

---

## #9 — You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories

**Authors:** Zhepei Wei, Xinyu Zhu, Wei-Lin Chen, Chengsong Huang, Jiaxin Huang

**Summary:** RLVR weight trajectories are extremely low-rank and predictable — the majority of performance gains are captured by a rank-1 approximation of parameter deltas. This insight enables "extrapolation" of RLVR improvements with minimal actual training, dramatically reducing the compute cost of reasoning-specialized fine-tuning.

**arxiv:** [arxiv.org/abs/2605.21468](https://arxiv.org/abs/2605.21468)

**Sources:** HuggingFace Daily Papers (37★), r/MachineLearning, r/LocalLLaMA, X/Twitter

**Why trending:** Rank-1 trajectory finding is a striking geometric insight; if confirmed broadly, it could fundamentally change how reasoning models are trained and updated — massive efficiency implications.

---

## #10 — OScaR: The Occam's Razor for Extreme KV Cache Quantization in LLMs and Beyond

**Authors:** Zunhai Su, Rui Yang, Chao Zhang, Yaxiu Liu, Yifan Zhang

**Summary:** Per-channel KV cache quantization fails under extreme compression because it cannot handle the full distribution of outliers in Key tensors. OScaR revisits the theoretical limits of per-channel quantization and proposes a principled replacement that achieves dramatically better memory efficiency at extreme bit-widths (sub-2-bit), enabling longer contexts on the same hardware.

**arxiv:** [arxiv.org/abs/2605.19660](https://arxiv.org/abs/2605.19660)

**Sources:** HuggingFace Daily Papers (35★), r/LocalLLaMA, X/Twitter, Papers With Code

**Why trending:** KV cache compression is the dominant memory bottleneck in long-context LLM deployment; extreme quantization below 2-bit is highly coveted for running frontier models on consumer hardware.

---

## #11 — IndusAgent: Reinforcing Open-Vocabulary Industrial Anomaly Detection with Agentic Tools

**Authors:** Rongbin Tan, Fangfang Lin, Zhenlong Yuan, Min Qiu, Kejin Cui

**Summary:** MLLMs struggle with open-vocabulary industrial anomaly detection (IAD) due to domain-misaligned reasoning and hallucinated structural inferences. IndusAgent wraps MLLMs with a tool-augmented agentic framework that provides domain-specific inspection tools, dramatically improving precision on manufacturing and quality-control anomaly detection benchmarks.

**arxiv:** [arxiv.org/abs/2605.20682](https://arxiv.org/abs/2605.20682)

**Sources:** HuggingFace Daily Papers (34★), r/MachineLearning, X/Twitter

**Why trending:** Industrial AI is a high-value application domain; the agentic tool-use approach to grounding MLLMs in domain knowledge is an increasingly popular and effective paradigm.

---

## #12 — A Survey of Large Audio Language Models: Generalization, Trustworthiness, and Outlook

**Authors:** Kaiwen Luo, Zhenhong Zhou, Leo Wang, Liang Lin, Yang Xiao

**Summary:** Large Audio Language Models (LALMs) have seen rapid capability growth, but their trustworthiness — robustness, fairness, privacy, and safety — has not kept pace. This comprehensive survey maps the LALM landscape, identifies key generalization and reliability gaps, and outlines a research agenda for building trustworthy universal auditory intelligence systems.

**arxiv:** [arxiv.org/abs/2605.20266](https://arxiv.org/abs/2605.20266)

**Sources:** HuggingFace Daily Papers (27★), r/MachineLearning, X/Twitter

**Why trending:** Surveys of fast-moving areas get immediate traction as reference documents; audio LLMs are a rapidly growing subfield and practitioners need systematic overviews of reliability considerations.

---

## #13 — It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs

**Authors:** Sangwoo Park, Woongyeong Yeo, Seanie Lee, Yumin Choi, Hyomin Lee

**Summary:** Contextual Integrity (CI) — the principle that privacy is about appropriate information flows, not just secrecy — is poorly maintained by frontier LLMs acting as personal agents. This paper proposes complementary self-distillation, where two complementary model instances mutually teach each other context-appropriate disclosure behavior, improving CI adherence without sacrificing downstream task performance.

**arxiv:** [arxiv.org/abs/2605.20258](https://arxiv.org/abs/2605.20258)

**Sources:** HuggingFace Daily Papers (26★), r/MachineLearning, X/Twitter

**Why trending:** As LLMs become personal agents with access to sensitive workflows, CI is a critical but under-studied property; the privacy-utility trade-off solution via self-distillation is novel and practically relevant.

---

## #14 — Toto 2.0: Time Series Forecasting Enters the Scaling Era

**Authors:** Emaad Khwaja, Chris Lettieri, Gerald Woo, Eden Belouadah, Marc Cenac

**Summary:** Toto 2.0 demonstrates that time series foundation models scale reliably — a single training recipe consistently improves forecast quality from 4M to 2.5B parameters. The family of five open-weights models sets new SOTA on three forecasting benchmarks (BOOM, GIFT-Eval, TIME), establishing that scaling laws extend meaningfully to time series prediction.

**arxiv:** [arxiv.org/abs/2605.20119](https://arxiv.org/abs/2605.20119)

**Sources:** HuggingFace Daily Papers (24★), r/MachineLearning, X/Twitter, Hacker News

**Why trending:** Scaling laws for time series is an important empirical result; the open-weights release and SOTA on multiple benchmarks make it immediately usable for practitioners in finance, infrastructure, and operations.

---

## #15 — Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs

**Authors:** Haiquan Lu, Zigeng Chen, Gongfan Fang, Xinyin Ma, Xinchao Wang

**Summary:** Agentic LLM workflows generate massive input overhead (long context, multi-turn history) that makes the prefilling stage a compute bottleneck. Mix-Quant applies aggressive FP4 quantization during prefilling — where precision matters less — while maintaining full precision during decoding, achieving significant prefilling speedups with negligible accuracy degradation on agentic benchmarks.

**arxiv:** [arxiv.org/abs/2605.20315](https://arxiv.org/abs/2605.20315)

**Sources:** HuggingFace Daily Papers (21★), r/LocalLLaMA, X/Twitter

**Why trending:** Prefilling bottleneck is a real deployment pain point for agentic systems; the phase-aware quantization insight is clean and the FP4 prefilling speedup is substantial and practical.

---

## #16 — Generative Recursive Reasoning (GRAM)

**Authors:** Junyeob Baek, Mingyu Jo, Minsu Kim, Mengye Ren, Yoshua Bengio

**Summary:** Recursive Reasoning Models (RRMs) refine latent states iteratively instead of extending autoregressive sequences, but existing RRMs are deterministic and converge to single predictions. GRAM turns recursive latent reasoning into probabilistic inference, enabling diverse reasoning paths and improved performance on tasks requiring extended computation — with Yoshua Bengio as a co-author lending significant credibility.

**arxiv:** [arxiv.org/abs/2605.19376](https://arxiv.org/abs/2605.19376)

**Sources:** HuggingFace Daily Papers (18★), r/MachineLearning, X/Twitter

**Why trending:** Bengio co-authorship drives visibility; the probabilistic latent reasoning framework is a compelling alternative to chain-of-thought and addresses fundamental limitations of deterministic RRMs.

---

## #17 — CutVerse: A Compositional GUI Agents Benchmark for Media Post-Production Editing

**Authors:** Haobo Hu, Xiangwu Guo, Zhiheng Chen, Difei Gao, Haotian Liu

**Summary:** GUI agent benchmarks have focused on web and OS tasks, leaving professional creative workflows (video editing, photo retouching, compositing) unexplored. CutVerse provides 186 complex, long-horizon expert-curated tasks across 7 professional applications (Premiere Pro, Photoshop, etc.), revealing that current GUI agents struggle severely with creative media workflows.

**arxiv:** [arxiv.org/abs/2605.19484](https://arxiv.org/abs/2605.19484)

**Sources:** HuggingFace Daily Papers (18★), r/MachineLearning, r/LocalLLaMA

**Why trending:** Professional creative software automation is a highly commercially valuable frontier; the benchmark fills an important gap and the 7-app, 186-task scope is comprehensive.

---

## #18 — Uni-Edit: Intelligent Editing Is A General Task For Unified Model Tuning

**Authors:** Dian Zheng, Manyuan Zhang, Hongyu Li, Hongbo Liu, Kai Zou

**Summary:** Unified Multimodal Models (UMMs) currently require complex multi-task pipelines to develop image understanding, generation, and editing jointly — leading to performance trade-offs rather than synergy. Uni-Edit frames image editing as a general task that naturally unifies all three capabilities, breaking the need for task-conflict management and enabling mutual reinforcement across modalities.

**arxiv:** [arxiv.org/abs/2605.21487](https://arxiv.org/abs/2605.21487)

**Sources:** HuggingFace Daily Papers (17★), r/MachineLearning, X/Twitter

**Why trending:** Simplifying the multimodal model training pipeline has broad appeal; the unified task framing is an elegant conceptual contribution that could reshape how multimodal models are developed.

---

## #19 — LLMEval-Logic: A Solver-Verified Chinese Benchmark for Logical Reasoning of LLMs with Adversarial Hardening

**Authors:** Ming Zhang, Qiyuan Peng, Yinxi Wei, Yujiong Shen, Kexin Tan

**Summary:** Existing logical reasoning benchmarks are quickly saturated by frontier models, often because they rely on templated generation with coarse annotations. LLMEval-Logic is a Chinese logical reasoning benchmark built from realistic scenarios, verified by formal solvers, and hardened with adversarial perturbations to resist data contamination — demonstrating that current frontier models still have substantial logical reasoning gaps.

**arxiv:** [arxiv.org/abs/2605.19597](https://arxiv.org/abs/2605.19597)

**Sources:** HuggingFace Daily Papers (16★), r/MachineLearning, Papers With Code

**Why trending:** Solver-verified benchmarks that resist contamination are exactly what the evaluation community needs; Chinese-language coverage also fills a significant gap in existing evaluation suites.

---

## #20 — HRM-Text: Efficient Pretraining Beyond Scaling

**Authors:** Guan Wang, Changling Liu, Chenyu Wang, Cai Zhou, Yuhao Sun

**Summary:** Standard LLM pretraining requires massive compute and internet-scale data, creating barriers for research. Inspired by the brain's frontoparietal loop, HRM-Text replaces standard Transformers with a Hierarchical Recurrent Model that decouples computation across timescales, achieving strong language modeling results with dramatically fewer training tokens and compute — challenging the assumption that scaling is the only path to capable models.

**arxiv:** [arxiv.org/abs/2605.20613](https://arxiv.org/abs/2605.20613)

**Sources:** HuggingFace Daily Papers (10★), r/MachineLearning, Hacker News

**Why trending:** Bio-inspired alternatives to Transformers that achieve competitive performance with less compute are perennially interesting; the "beyond scaling" framing resonates with growing concerns about the sustainability of compute scaling.
