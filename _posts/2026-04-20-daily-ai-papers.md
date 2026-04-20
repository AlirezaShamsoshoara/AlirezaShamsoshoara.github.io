---
title: "Daily AI Papers — April 20, 2026"
date: 2026-04-20
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-20/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - inference-scaling
  - multimodal
  - agents
---

## 1. Elucidating the SNR-t Bias of Diffusion Probabilistic Models
- **Authors:** Meng Yu, Lei Sun, Jianhao Zeng, Xiangxiang Chu, Kun Zhan
- **Summary:** Identifies a systematic Signal-to-Noise Ratio vs. timestep (SNR-t) misalignment that arises only at inference in diffusion models, causing error accumulation and degraded sample quality. Proposes a corrective scheme that re-couples SNR with the timestep schedule, yielding consistent gains across image generation benchmarks without retraining.
- **arxiv:** [arxiv.org/abs/2604.16044](https://arxiv.org/abs/2604.16044)
- **Sources:** HuggingFace Daily Papers (64 upvotes — top of the day), arxiv
- **Why trending:** Highest-voted paper of the day on HF; surfaces a previously under-discussed inference-time failure mode in diffusion models with a clean, training-free fix.

## 2. Maximal Brain Damage Without Data or Optimization: Disrupting Neural Networks via Sign-Bit Flips
- **Authors:** Ido Galil, Moshe Kimhi, Ran El-Yaniv
- **Summary:** Introduces Deep Neural Lesion (DNL), a data-free, optimization-free attack that locates critical weights and catastrophically breaks DNNs by flipping just a handful of sign bits — flipping two bits in ResNet-50 collapses ImageNet accuracy. Demonstrates the vulnerability across image classification, object detection, segmentation, and reasoning LLMs.
- **arxiv:** [arxiv.org/abs/2502.07408](https://arxiv.org/abs/2502.07408)
- **Sources:** HuggingFace Daily Papers (33 upvotes), arxiv
- **Why trending:** Striking security/robustness result with broad cross-domain implications for hardware fault attacks (Rowhammer-style) on deployed models.

## 3. PersonaVLM: Long-Term Personalized Multimodal LLMs
- **Authors:** Chang Nie, Chaoyou Fu, Yifan Zhang, et al.
- **Summary:** Proposes PersonaVLM, a multimodal agent framework for long-term personalization that turns a general-purpose MLLM into an assistant that tracks evolving user preferences and personality across sessions. Goes beyond static, single-turn personalization (input augmentation, output alignment) toward continuous behavioral adaptation.
- **arxiv:** [arxiv.org/abs/2604.13074](https://arxiv.org/abs/2604.13074)
- **Sources:** HuggingFace Daily Papers (29 upvotes), arxiv
- **Why trending:** Personalized AI assistants are a hot research area; this work directly tackles the long-term memory + identity problem for multimodal models.

## 4. Web Retrieval-Aware Chunking (W-RAC) for Efficient and Cost-Effective Retrieval-Augmented Generation Systems
- **Authors:** Uday Allu, Sonu Kedia, Tanmay Odapally, et al.
- **Summary:** Presents W-RAC, a chunking framework specifically designed for web-scale RAG that decouples text extraction from chunk boundary decisions, cutting token consumption and redundant generation versus fixed-size or fully agentic chunking. Targets debuggability and scalability for production ingestion pipelines.
- **arxiv:** [arxiv.org/abs/2604.04936](https://arxiv.org/abs/2604.04936)
- **Sources:** HuggingFace Daily Papers (22 upvotes), arxiv
- **Why trending:** Practical infra-flavored RAG paper — chunking remains the highest-leverage knob for cost and quality in production retrieval systems.

## 5. Qwen3.5-Omni Technical Report
- **Authors:** Qwen Team
- **Summary:** Releases Qwen3.5-Omni, scaling the Qwen-Omni family to hundreds of billions of parameters with a 256k context, trained on heterogeneous text-vision pairs and >100M hours of audio-visual content. Reports SOTA on 215 audio and audio-visual benchmarks, claiming to surpass Gemini-3.1 Pro on omni-modal understanding.
- **arxiv:** [arxiv.org/abs/2604.15804](https://arxiv.org/abs/2604.15804)
- **Sources:** HuggingFace Daily Papers (20 upvotes), arxiv, Qwen team release channels
- **Why trending:** Major frontier-class omni-modal release from Alibaba's Qwen team with explicit Gemini-3.1 Pro comparisons; high industry attention.

## 6. Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning
- **Authors:** Jiaxi Bi, Tongxu Luo, Wenyu Du, et al.
- **Summary:** Proposes the first systematic taxonomy of path pruning for parallel reasoning in LRMs and introduces STOP (Super TOken for Pruning), a learnable internal-signal method that kills doomed reasoning paths early at the prefix level. Substantially reduces compute waste in parallel test-time scaling.
- **arxiv:** [arxiv.org/abs/2604.16029](https://arxiv.org/abs/2604.16029)
- **Sources:** HuggingFace Daily Papers (18 upvotes), arxiv
- **Why trending:** Test-time compute and parallel reasoning efficiency is the dominant inference-scaling research thread right now.

## 7. (1D) Ordered Tokens Enable Efficient Test-Time Search
- **Authors:** Zhitong Gao, Parham Rezaei, Ali Cy, et al.
- **Summary:** Investigates how token structure in autoregressive image generation affects test-time search effectiveness, hypothesizing and confirming that 1D ordered (coarse-to-fine) tokenizers enable far more efficient verifier-guided search than spatial 2D tokens. Yields large quality gains under fixed search budgets.
- **arxiv:** [arxiv.org/abs/2604.15453](https://arxiv.org/abs/2604.15453)
- **Sources:** HuggingFace Daily Papers (12 upvotes), arxiv
- **Why trending:** Reframes tokenization as a first-class lever for inference-time scaling — relevant beyond images to any AR generative system.

## 8. Repurposing 3D Generative Model for Autoregressive Layout Generation (LaviGen)
- **Authors:** Haoran Feng, Yifan Niu, Zehuan Huang, et al.
- **Summary:** Introduces LaviGen, which repurposes a 3D generative model for native-3D-space autoregressive layout generation, explicitly modeling geometric relations and physical constraints between objects. Adds a dual-guidance self-rollout distillation procedure to produce coherent and physically plausible 3D scenes from instructions.
- **arxiv:** [arxiv.org/abs/2604.16299](https://arxiv.org/abs/2604.16299)
- **Sources:** HuggingFace Daily Papers (9 upvotes), arxiv
- **Why trending:** 3D-native generative pipelines (vs. 2D-projected) are a rising direction; physical-constraint-aware layout is directly useful for sim, robotics, and games.

## 9. Where does output diversity collapse in post-training?
- **Authors:** Constantinos Karouzos, Xingwei Tan, Nikolaos Aletras
- **Summary:** Disentangles whether the well-known post-training diversity collapse stems from training data composition, training method, or generation format, by tracing diversity through three parallel post-training lineages of Olmo 3 (Think, Instruct, and a third). Provides a controlled, mechanism-level account that prior work conflated.
- **arxiv:** [arxiv.org/abs/2604.16027](https://arxiv.org/abs/2604.16027)
- **Sources:** HuggingFace Daily Papers (8 upvotes), arxiv
- **Why trending:** Diversity collapse directly threatens inference-time scaling (best-of-N, parallel sampling) and creative tasks — actionable diagnostic study using open Olmo 3 lineages.

## 10. QuantCode-Bench: A Benchmark for Evaluating LLMs on Algorithmic Trading Strategies
- **Authors:** Alexey Khoroshilov, Alexey Chernysh, Orkhan Ekhtibarov, et al.
- **Summary:** Introduces QuantCode-Bench, the first benchmark for evaluating LLMs on generating *executable* algorithmic trading strategies — combining financial domain logic, specialized API knowledge, and code that actually trades on historical data. Goes beyond standard code benchmarks by requiring end-to-end runnable strategies.
- **arxiv:** [arxiv.org/abs/2604.15151](https://arxiv.org/abs/2604.15151)
- **Sources:** HuggingFace Daily Papers (5 upvotes), arxiv
- **Why trending:** Bridges code-LLM evaluation with quantitative finance — niche but hits a real gap and attracts both ML and quant audiences.

## 11. Learning Adaptive Reasoning Paths for Efficient Visual Reasoning (AVR)
- **Authors:** Yixu Huang, Tinghui Zhu, Muhao Chen
- **Summary:** Identifies "reasoning path redundancy" as the cause of overthinking in visual reasoning models and proposes AVR, decomposing visual reasoning into perception, logical reasoning, and answer application as adaptively-invoked cognitive functions. Cuts reasoning length on easy queries while preserving accuracy on hard ones.
- **arxiv:** [arxiv.org/abs/2604.14568](https://arxiv.org/abs/2604.14568)
- **Sources:** HuggingFace Daily Papers (5 upvotes), arxiv
- **Why trending:** Adaptive/early-exit reasoning is a major sub-area of efficient inference; clean modular framing for the visual case.

## 12. Can Large Language Models Reinvent Foundational Algorithms?
- **Authors:** Jian Zhao, Haoren Luo, Yu Wang, et al.
- **Summary:** Proposes an Unlearn-and-Reinvent pipeline: surgically remove a foundational algorithm (Dijkstra's, Euclid's, etc.) from an LLM via unlearning, then test whether the model can reinvent it from first principles in a controlled setting. Probes a hard prerequisite for LLM-driven scientific discovery.
- **arxiv:** [arxiv.org/abs/2604.05716](https://arxiv.org/abs/2604.05716)
- **Sources:** HuggingFace Daily Papers (5 upvotes), arxiv
- **Why trending:** Provocative methodology connecting unlearning and innovation evaluation — likely to spark debate in the AI-for-science crowd.

## 13. TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment
- **Authors:** Bingyi Cao, Koert Chen, Kevis-Kokitsi Maninis, et al.
- **Summary:** Tackles a persistent failure of foundational vision-language models — aligning dense patch embeddings with text concepts — and shows that patch-level distillation substantially boosts dense alignment. Improves a range of downstream tasks (classification, retrieval, segmentation, depth) without sacrificing global image-text capability.
- **arxiv:** [arxiv.org/abs/2604.12012](https://arxiv.org/abs/2604.12012)
- **Sources:** HuggingFace Daily Papers (4 upvotes), arxiv
- **Why trending:** Practical recipe-style improvement to foundational VL pretraining; directly drops into many downstream pipelines.

## 14. GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows
- **Authors:** Jize Wang, Xuanxuan Liu, Yining Li, et al.
- **Summary:** Releases GTA-2, a hierarchical benchmark for general tool-using agents that spans atomic tool calls up to open-ended productivity workflows, built on real user queries, deployed tools, and multimodal contexts (no AI-generated queries or dummy tools). Aims to fix the realism gap in current tool-use benchmarks.
- **arxiv:** [arxiv.org/abs/2604.15715](https://arxiv.org/abs/2604.15715)
- **Sources:** HuggingFace Daily Papers (3 upvotes), arxiv
- **Why trending:** Tool-use / agent benchmarks are saturating; GTA-2 is one of the more rigorous attempts to evaluate end-to-end real-world workflow completion.

## 15. EdgeDetect: Importance-Aware Gradient Compression with Homomorphic Aggregation for Federated Intrusion Detection
- **Authors:** Noor Islam S. Mohammad
- **Summary:** Proposes EdgeDetect, a federated intrusion detection system for bandwidth-limited 6G-IoT environments that uses median-based statistical binarization ("gradient smartification") to compress updates to {+1,-1} (32× uplink reduction) and homomorphic aggregation to defeat gradient-inference attacks. Preserves convergence under aggressive compression.
- **arxiv:** [arxiv.org/abs/2604.14663](https://arxiv.org/abs/2604.14663)
- **Sources:** HuggingFace Daily Papers (2 upvotes), arxiv
- **Why trending:** Touches federated learning, privacy, and 6G/IoT systems — appeals to security and edge-ML communities simultaneously.

## 16. AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization
- **Authors:** Genghan Zhang, Shaowei Zhu, Anjiang Wei, et al.
- **Summary:** Presents AccelOpt, a self-improving LLM agent that autonomously optimizes kernels for emerging AI accelerators with no expert-provided hardware knowledge, using an iterative generate-and-curate loop over a memory of slow/fast kernel pairs. Introduces NKIBench, a benchmark of AWS Trainium kernels extracted from real LLM workloads.
- **arxiv:** [arxiv.org/abs/2511.15915](https://arxiv.org/abs/2511.15915)
- **Sources:** HuggingFace Daily Papers (2 upvotes), arxiv, AWS Trainium developer channels
- **Why trending:** Sits at the intersection of agentic systems and ML systems — autonomous kernel tuning is a high-value, increasingly tractable target for LLM agents.

## 17. Hierarchical Codec Diffusion for Video-to-Speech Generation (HiCoDiT)
- **Authors:** Jiaxin Ye, Gaoxiang Cong, Chenhui Wang, et al.
- **Summary:** Introduces HiCoDiT, a Hierarchical Codec Diffusion Transformer for video-to-speech that exploits the hierarchical structure of RVQ-based neural codecs to align visual features with speech at coarse (speaker-aware semantics) and fine (prosodic detail) levels. Improves over prior VTS methods that ignore speech hierarchy.
- **arxiv:** [arxiv.org/abs/2604.15923](https://arxiv.org/abs/2604.15923)
- **Sources:** HuggingFace Daily Papers (1 upvote), arxiv
- **Why trending:** Multimodal generation across silent video → speech is a niche but rising area with applications in dubbing, accessibility, and avatar systems.

## 18. TwinTrack: Post-hoc Multi-Rater Calibration for Medical Image Segmentation
- **Authors:** Tristan Kirscher, Alexandra Ertl, Klaus Maier-Hein, et al.
- **Summary:** Addresses inherent ambiguity in pancreatic ductal adenocarcinoma CT segmentation, where inter-rater disagreement reflects real uncertainty rather than noise. TwinTrack post-hoc calibrates ensemble probabilities to the empirical mean human response, producing better-calibrated, more interpretable segmentations under genuine annotator disagreement.
- **arxiv:** [arxiv.org/abs/2604.15950](https://arxiv.org/abs/2604.15950)
- **Sources:** HuggingFace Daily Papers (1 upvote), arxiv
- **Why trending:** Medical-imaging-grounded calibration paper that takes annotator disagreement seriously rather than averaging it away — relevant to clinical deployment.

## 19. NTIRE 2026 Challenge on Video Saliency Prediction: Methods and Results
- **Authors:** Andrey Moskalenko, Alexey Bryncev, Ivan Kosmynin, et al.
- **Summary:** Reports the NTIRE 2026 video saliency prediction challenge: a new 2,000-video open-license dataset with crowdsourced mouse-tracking saliency from 5,000+ assessors, evaluated on 800 test videos. Aggregates results from 20+ competing teams and surveys their methods.
- **arxiv:** [arxiv.org/abs/2604.14816](https://arxiv.org/abs/2604.14816)
- **Sources:** HuggingFace Daily Papers (1 upvote), arxiv, NTIRE/CVPR workshop channels
- **Why trending:** Benchmark/challenge reports concentrate community methods in one place and are reliable references for the saliency-prediction subfield.

## 20. PRL-Bench: A Comprehensive Benchmark Evaluating LLMs' Capabilities in Frontier Physics Research
- **Authors:** Tingjia Miao, Wenkai Jin, Muhua Zhang, et al.
- **Summary:** Introduces PRL-Bench for theoretical and computational physics, designed to evaluate not just domain knowledge and reasoning but the exploratory, long-horizon, autonomous research workflows demanded by agentic science. Targets verifiable end-to-end research tasks without requiring physical experiments.
- **arxiv:** [arxiv.org/abs/2604.15411](https://arxiv.org/abs/2604.15411)
- **Sources:** HuggingFace Daily Papers (1 upvote), arxiv
- **Why trending:** Agentic-science benchmarks with verifiable end-to-end physics workflows are increasingly important as LLMs are pushed toward research-grade autonomy.
