---
title: "Daily AI Papers — September 20, 2026"
date: 2026-09-20
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-20/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - efficient-language-models
  - multimodal-ai
---

### 1. PDFMathTranslate: Scientific Document Translation Preserving Layouts
**Authors:** Rongxin Ouyang, Chang Chu, Zhikuang Xin, Xiangyao Ma
**arXiv:** [arxiv.org/abs/2507.03009](https://arxiv.org/abs/2507.03009)
**Summary:** PDFMathTranslate is open-source software that translates scientific documents while preserving their layouts, combining large language models with precise layout detection. The authors report improvements in precision, flexibility, and efficiency, and note more than 222,000 downloads of the released project.
**Trending because:** 3 HuggingFace upvotes + preserves equations and page structure while making scientific PDFs accessible across languages

---

### 2. dQwen3.5: Hybrid-Attention Diffusion Language Models
**Authors:** Anton Xue, Litu Rout, Aditya Akella, Adam Klivans, Sujay Sanghavi, Sanjay Shakkottai
**arXiv:** [arxiv.org/abs/2609.20751](https://arxiv.org/abs/2609.20751)
**Summary:** dQwen3.5 adapts hybrid attention-and-RNN Qwen3.5 backbones at four scales into diffusion language models despite the difficulty of making causal RNN layers bidirectional. The hybrid models reach a given training loss in roughly half the tokens of a full-attention control while retaining strong any-order and parallel decoding behavior.
**Trending because:** 0 HuggingFace upvotes + shows hybrid attention-RNN backbones can become efficient parallel-decoding diffusion language models

---

### 3. On-Demand Attention: Language Models Know When to Recall
**Authors:** Haibo Feng, Ruiqi Liang, Hanyang Peng, Shiqi Yu
**arXiv:** [arxiv.org/abs/2609.20734](https://arxiv.org/abs/2609.20734)
**Summary:** On-Demand Attention uses a lightweight recall head to let a pretrained language model decide when long-context decoding needs global attention rather than always rereading the full history. Across Qwen and Gemma models, it recovers most of full-attention performance while substantially reducing global reads and producing practical vLLM speedups.
**Trending because:** 0 HuggingFace upvotes + lets long-context models decide when global recall is actually worth its inference cost

---

### 4. Score Centering Stabilizes Off-policy Reinforcement Learning
**Authors:** Martin Marek, Max Ryabinin
**arXiv:** [arxiv.org/abs/2609.20807](https://arxiv.org/abs/2609.20807)
**Summary:** Score centering addresses reinforcement-learning instability caused by persistent drift between the training and inference engines used for language-model rollouts. The additive correction matches or beats importance-sampling methods under quantization from 0.6B to 30B parameters and also composes effectively with importance sampling under staleness.
**Trending because:** 0 HuggingFace upvotes + offers a simple correction for a major source of instability in agentic language-model RL

---

### 5. Can 4D Foundation Models Remember?
**Authors:** Guangzhao He, Hadar Averbuch-Elor, Wei-Chiu Ma
**arXiv:** [arxiv.org/abs/2609.20819](https://arxiv.org/abs/2609.20819)
**Summary:** PersistBench uses 360-degree video as omniscient ground truth to test 4D foundation models on object permanence, motion continuity, and appearance preservation. Its evaluations find that current models maintain only short-term consistency and degrade significantly after objects leave the field of view.
**Trending because:** 0 HuggingFace upvotes + introduces object-centric tests showing that visual perception is not yet durable visual memory

---

### 6. UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning
**Authors:** Wenjie Liao, Liangjie Zhao, Zehong Cao
**arXiv:** [arxiv.org/abs/2609.20089](https://arxiv.org/abs/2609.20089)
**Summary:** UnifiedPlayers jointly trains planning, execution, and evaluation players so tool-using agents can generate trajectories and executable verifiers without relying on fixed evaluators. Across two backbones and twelve reasoning benchmarks, it improves mathematical and general reasoning while producing a verifier with 84.2% adversarial-detection accuracy.
**Trending because:** 0 HuggingFace upvotes + co-trains task generation, tool execution, and adaptive verification for self-improving agents

---

### 7. Chronicle: Cut-Point Replay for Regression Testing of LLM Agents
**Authors:** Tisha Chawla, Susheem Koul
**arXiv:** [arxiv.org/abs/2609.20625](https://arxiv.org/abs/2609.20625)
**Summary:** Chronicle records an LLM agent's nondeterministic boundaries as immutable envelopes and can replay selected boundaries while running changed code live. Its cut-point replay turns recorded incidents into stable CI regression tests and caught every unsafe tool mutant in the reported study.
**Trending because:** 0 HuggingFace upvotes + turns nondeterministic agent failures into reproducible continuous-integration tests

---

### 8. How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents
**Authors:** Yukun Zhang, Kemu Xu, Yishen Chen
**arXiv:** [arxiv.org/abs/2609.20474](https://arxiv.org/abs/2609.20474)
**Summary:** This study isolates how task-specific plans and terminal verification contribute to stateful LLM-agent performance in retail and airline tasks. Fixed plans improved oracle-verified success by 7.17 percentage points, while a low-cost read-only verifier rejected 61% of invalid retail episodes.
**Trending because:** 0 HuggingFace upvotes + quantifies the separate value of planning guidance and release-control verification in agent harnesses

---

### 9. MM-Future: Multi-Mode Joint World-Action Modeling for Autonomous Driving
**Authors:** Shuai Liu, Hechangle Gong, Hao Jiang, Runlin He, Junxiang Zhan, Kai Huang, Sheng Yang, Shaoqing Ren
**arXiv:** [arxiv.org/abs/2609.20377](https://arxiv.org/abs/2609.20377)
**Summary:** MM-Future jointly generates multiple paired future-scene and action hypotheses for autonomous driving, co-evolving them with a modality-aware diffusion Transformer. Its compressed planning representations and proposal scorer deliver strong open-loop and zero-shot closed-loop results, outperforming single-mode and action-only variants.
**Trending because:** 0 HuggingFace upvotes + jointly models multiple plausible futures and actions for autonomous-driving decisions

---

### 10. JEPA-WAM: Connecting Generated Visual Instructions to World Action Models through JEPA Latent Representations
**Authors:** Tianbin Liu, Jian Zhu, Taiyi Su, Jianjun Zhang, Chong Ma, Zitai Huang, Yi Xu
**arXiv:** [arxiv.org/abs/2609.20277](https://arxiv.org/abs/2609.20277)
**Summary:** JEPA-WAM supplements sparse robot-language supervision with multiple generated visual instructions encoded as compact V-JEPA goal tokens. On a real-robot benchmark, it substantially outperforms π0 and Fast-WAM across in-distribution and out-of-distribution scenes and instructions.
**Trending because:** 0 HuggingFace upvotes + uses generated visual goals to strengthen robot instruction following under distribution shift

---

### 11. Paint-Anything: Unified Any-Color Control for Image Generation and Editing
**Authors:** Ji Xie, Dewei Zhou, Xinyu Huang, Zhennan Chen, Xun Wang
**arXiv:** [arxiv.org/abs/2609.20816](https://arxiv.org/abs/2609.20816)
**Summary:** Paint-Anything gives image generation and editing models a shared interface for specifying any 24-bit hex color at the object level. Trained with the Paint-500K pipeline and pure-color anchors, it markedly improves hex-color fidelity on both generation and editing benchmarks over the FLUX.2-4B base model.
**Trending because:** 0 HuggingFace upvotes + adds precise arbitrary-color control to a unified image generation and editing interface

---

### 12. D-Quant: Driftable Entropy Coding for KV Cache Quantization
**Authors:** Yi Su, Hong Liu, Guanghua Yu, Jianchen Zhu
**arXiv:** [arxiv.org/abs/2609.19880](https://arxiv.org/abs/2609.19880)
**Summary:** D-Quant compresses KV caches with entropy coding while using a drift mechanism to turn variable-length token representations into fixed-size bitstreams. This design targets the non-uniform distribution of KV values while preserving regular memory access and parallel dequantization for attention kernels.
**Trending because:** 0 HuggingFace upvotes + combines entropy-efficient KV compression with hardware-friendly fixed-size decoding

---

### 13. JustMem: Just-Enough Memory Access for Long-Term Conversations
**Authors:** Guanhua Chen, Yanting Wang, Wenjing Zhi, Lei Sha
**arXiv:** [arxiv.org/abs/2609.19877](https://arxiv.org/abs/2609.19877)
**Summary:** JustMem represents long conversations as compact atomic memories and adapts both retrieval breadth and reading fidelity to each query. Its LOOKUP, COMPOSE, and REPLAY modes achieve the highest mean accuracy and retrieval recall in the reported LoCoMo and LongMemEval-S comparisons while using fewer generative-model tokens.
**Trending because:** 0 HuggingFace upvotes + adapts conversational memory search depth and source fidelity to each question

---

### 14. To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model Signals
**Authors:** Roy Eisenstadt, Ido Cohen, Edo Cohen-Karlik, Lior Wolf, Itamar Zimerman
**arXiv:** [arxiv.org/abs/2609.20186](https://arxiv.org/abs/2609.20186)
**Summary:** SwitchSD uses lightweight probes over a target language model's internal representations to detect genuine copy intent during speculative decoding. Dynamically switching between neural drafting and context copying yields up to 15% more throughput than reported state-of-the-art baselines across Llama and Qwen models.
**Trending because:** 0 HuggingFace upvotes + uses intrinsic model signals to switch speculative-decoding strategies and improve throughput

---

### 15. Parallelism, critical windows, and separations among diffusion language models
**Authors:** Sitan Chen, Liye Wang
**arXiv:** [arxiv.org/abs/2609.20539](https://arxiv.org/abs/2609.20539)
**Summary:** This paper gives a fine-grained theoretical comparison of masked, uniform, and Gaussian diffusion language models in terms of parallel sampling. It establishes the first provable separation among the three paradigms and links the disadvantage of masked diffusion to narrower critical sampling windows.
**Trending because:** 0 HuggingFace upvotes + provides the first provable parallelism separation among major diffusion-language-model families

---

### 16. Lens: Bringing the Right Semantic Perspective into Focus for Training-Free Multimodal Representation Learning
**Authors:** Xinran Liu, Shouqian Shi, Yixian Chen, Ruizhi Chen, Xin-Wei Yao, Sheng Zhong
**arXiv:** [arxiv.org/abs/2609.20252](https://arxiv.org/abs/2609.20252)
**Summary:** Lens addresses semantic-perspective misalignment in training-free multimodal representation extraction by anchoring a task-specific readout phrase and aggregating its contextualized token states. Without parameter updates or reranking, it reaches 63.9 Precision@1 across 36 MMEB datasets, 10.2 points above the closest same-backbone training-free baseline.
**Trending because:** 0 HuggingFace upvotes + extracts task-directed multimodal embeddings from pretrained models without further training

---

### 17. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance
**Authors:** Marina Orozco González, Luis Merino
**arXiv:** [arxiv.org/abs/2609.20589](https://arxiv.org/abs/2609.20589)
**Summary:** RawSLAM is an online Gaussian SLAM framework that tracks and maps directly from single-exposure 16-bit linear HDR imagery instead of tonemapped inputs. Its logarithmic Gaussian-color parameterization and HDR-aware objective improve trajectory and reconstruction accuracy and transfer to several existing Gaussian SLAM systems.
**Trending because:** 0 HuggingFace upvotes + brings online Gaussian SLAM to raw HDR inputs for robustness under extreme lighting

---

### 18. DocAttriBench: Benchmarking Answer Grounding in Document Visual Question Answering
**Authors:** Luca De Grandis (1), Silvia Cappelletti (1), William Raccagni (1 and 2), Marcella Cornia (1), Lorenzo Baraldi (1), Rita Cucchiara (1) ((1) University of Modena and Reggio Emilia, Modena, Italy, (2) University of Pisa, Pisa, Italy)
**arXiv:** [arxiv.org/abs/2609.20574](https://arxiv.org/abs/2609.20574)
**Summary:** DocAttriBench provides element-level source attribution for document visual question answering across 237,000 documents and 296,000 question-answer pairs. Its MAPPET construction method masks layout elements to measure their effect on answer perplexity, and evaluations show that even strong multimodal models often fail to localize supporting evidence.
**Trending because:** 0 HuggingFace upvotes + scales fine-grained evidence attribution for trustworthy document question answering

---

### 19. RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents
**Authors:** Mingxuan Zhang, Xiaowen Wang, Anupma Sharan, Zhengyi Chen, Chenyu Diana Zhang, Shanshan Yang, Chittibabu Pacharu
**arXiv:** [arxiv.org/abs/2609.20754](https://arxiv.org/abs/2609.20754)
**Summary:** RAFT models closed troubleshooting cases as stateful chains and retrieves timeline entries that match an active case's intermediate state. On synthetic Windows Server cases and real Apache Jira duplicates, it improves case retrieval over vanilla RAG and GraphRAG baselines throughout case progress.
**Trending because:** 0 HuggingFace upvotes + retrieves state-matched historical trajectories rather than treating support cases as static documents

---

### 20. SCGFM-ART: Amortized Relational Transport for Structure-Centric Graph Foundation Models
**Authors:** Xiaodong He, Xincheng Wang, Zhao Kang
**arXiv:** [arxiv.org/abs/2609.20419](https://arxiv.org/abs/2609.20419)
**Summary:** SCGFM-ART aligns heterogeneous graphs to a shared relational atlas using amortized relational transport, avoiding iterative alignment at inference time. Across 14 cross-domain graph and node classification tasks, it reports state-of-the-art transferability and 44.2-to-85.1-times faster frozen target-domain inference.
**Trending because:** 0 HuggingFace upvotes + maps heterogeneous graphs into a reusable structural coordinate system with much faster transfer
