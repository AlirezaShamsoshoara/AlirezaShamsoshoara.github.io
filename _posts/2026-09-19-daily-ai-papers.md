---
title: "Daily AI Papers — September 19, 2026"
date: 2026-09-19
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-19/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - embodied-ai
  - agentic-ai
  - efficient-ai
---

### 1. SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics
**Authors:** Mustafa Shukor, Dana Aubakirova, Francesco Capuano, Pepijn Kooijmans, Steven Palma, Adil Zouitine, Michel Aractingi, Caroline Pascal, Martino Russi, Andres Marafioti, Simon Alibert, Matthieu Cord, Thomas Wolf, Remi Cadene
**arXiv:** [arxiv.org/abs/2506.01844](https://arxiv.org/abs/2506.01844)
**Summary:** In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger.
**Trending because:** 166 HuggingFace upvotes + makes capable vision-language-action robotics trainable on one GPU and deployable on consumer hardware

---

### 2. Agent Lightning: Train ANY AI Agents with Reinforcement Learning
**Authors:** Xufang Luo, Yuge Zhang, Zhiyuan He, Zilong Wang, Siyun Zhao, Dongsheng Li, Luna K. Qiu, Yuqing Yang
**arXiv:** [arxiv.org/abs/2508.03680](https://arxiv.org/abs/2508.03680)
**Summary:** We present Agent Lightning, a flexible and extensible framework that enables Reinforcement Learning (RL)-based training of Large Language Models (LLMs) for any AI agent. Experiments across text-to-SQL, retrieval-augmented generation, and math tool-use tasks demonstrate stable, continuous improvements, showcasing the framework's potential for real-world agent training and deployment.
**Trending because:** 142 HuggingFace upvotes + decouples reinforcement learning from agent execution so existing agents can train with almost no code changes

---

### 3. Cache-to-Cache: Direct Semantic Communication Between Large Language Models
**Authors:** Tianyu Fu, Zihan Min, Hanling Zhang, Jichao Yan, Guohao Dai, Wanli Ouyang, Yu Wang
**arXiv:** [arxiv.org/abs/2510.03215](https://arxiv.org/abs/2510.03215)
**Summary:** Thus, we propose Cache-to-Cache (C2C), a new paradigm for direct semantic communication between LLMs. C2C uses a neural network to project and fuse the source model's KV-cache with that of the target model to enable direct semantic transfer.
**Trending because:** 99 HuggingFace upvotes + replaces text-only inter-model communication with direct semantic transfer through KV caches

---

### 4. Paper2Agent: Reimagining Research Papers As Interactive and Reliable AI Agents
**Authors:** Jiacheng Miao, Joe R. Davis, Yaohui Zhang, Jonathan K. Pritchard, James Zou
**arXiv:** [arxiv.org/abs/2509.06917](https://arxiv.org/abs/2509.06917)
**Summary:** We introduce Paper2Agent, an automated framework that converts research papers into AI agents. It systematically analyzes the paper and the associated codebase using multiple agents to construct a Model Context Protocol (MCP) server, then iteratively generates and runs tests to refine and robustify the resulting MCP.
**Trending because:** 45 HuggingFace upvotes + turns papers and their codebases into tested, interactive MCP research agents

---

### 5. GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface
**Authors:** Urchade Zaratiana, Gil Pasternak, Oliver Boyd, George Hurn-Maloney, Ash Lewis
**arXiv:** [arxiv.org/abs/2507.18546](https://arxiv.org/abs/2507.18546)
**Summary:** We present GLiNER2, a unified framework that enhances the original GLiNER architecture to support named entity recognition, text classification, and hierarchical structured data extraction within a single efficient model. Our experiments demonstrate competitive performance across extraction and classification tasks with substantial improvements in deployment accessibility compared to LLM-based alternatives.
**Trending because:** 41 HuggingFace upvotes + unifies several information-extraction tasks in a compact, schema-driven, CPU-efficient model

---

### 6. Verifiable Social Reasoning for LLM Assistants
**Authors:** Amir Taubenfeld, Zorik Gekhman, Avigail Grinstein-Dabush, Itay Laish, Ariel Goldstein, Marian Croak, Avinatan Hassidim, Yossi Matias, Amir Feder
**arXiv:** [arxiv.org/abs/2609.17496](https://arxiv.org/abs/2609.17496)
**Summary:** To address these challenges, we introduce Fuse, a multi-agent simulation framework for studying user-mediated social reasoning. We apply Fuse to 12 LLMs and demonstrate its analytical utility by systematically isolating key factors, showing that (i) user mediation compounds the inherent difficulty of social reasoning; (ii) LLMs exhibit systematic sensitivity to biased user framing; (iii) models can require more details than humans need to reach a correct prediction; and (iv) longer conversations do not always improve performance despite providing opportunities for clarifying questions.
**Trending because:** 32 HuggingFace upvotes + creates verifiable ground truth for studying how assistants reason about subjective social situations

---

### 7. In-Context Robot Learning with VLM Agents
**Authors:** Dongzhou Cheng, Taoran Yi, Ye Fang, Xingwu Zhang, Fan Feng, Yixuan Li, Gengxiong Zhuang, Rongze Wang, Shuai Yang, Wei Song, Weizhi Xue, Minyan Wu, Jie Gui, Jiaqi Wang, Tong Wu
**arXiv:** [arxiv.org/abs/2609.19138](https://arxiv.org/abs/2609.19138)
**Summary:** We introduce GPT-Policy, a general-agent framework for in-context robot learning. In real-robot trials, human video demonstrations improve task completion even without robot action labels, while aligned action references yield further gains on contact-sensitive tasks.
**Trending because:** 16 HuggingFace upvotes + uses demonstrations and interaction feedback for robot learning without gradient updates

---

### 8. Sample Count Is Not Enough: Candidate-Generation Strategy Shapes the Energy and Performance of LLM Test-Time Scaling
**Authors:** Mobina Kashaniyan, Ali Jannesari
**arXiv:** [arxiv.org/abs/2609.19499](https://arxiv.org/abs/2609.19499)
**Summary:** We therefore fix N = 8 and compare four generation schedules: 1x8, 2x4, 4x2, and 8x1, where axb denotes a generation calls with b candidates per call. On A100 GPUs, eight serial calls use 4.64-4.86x as much gross GPU-device energy and have 5.77-6.12x the P95 latency of one batched call with eight candidates.
**Trending because:** 16 HuggingFace upvotes + shows that generation scheduling can multiply energy use and tail latency at the same candidate count

---

### 9. FLAT: Resampling Image and Text into 1D Flexible-Length Aligned Transmodal Tokens for Retrieval and Generation
**Authors:** Guangyu Sun, Shlok Kumar Mishra, Wentao Bao, Robert Zhenheng Yang, Xiao Wang, Xiyuan Wang, Yujunrong Ma, Chen Yuan, Max Xiangjun Fan, Jun Xiao, Jianpeng Cheng
**arXiv:** [arxiv.org/abs/2609.16591](https://arxiv.org/abs/2609.16591)
**Summary:** We present FLAT (Flexible-Length Aligned Transmodal representations), a representation pre-training framework that jointly optimizes a shared multimodal encoder alongside downstream text-to-image (T2I) and image-to-text (I2T) decoders. Task-specific fine-tuning aligns model performance with state-of-the-art baselines: 83.1 GenEval on T2I generation; 40.5 BLEU-4 and 138.6 CIDEr on MS-COCO image captioning; and Recall@5 scores of 86.8 (I2T) / 75.8 (T2I) on MS-COCO alongside 98.3 (I2T) / 93.6 (T2I) on Flickr30K.
**Trending because:** 14 HuggingFace upvotes + learns flexible-length multimodal representations that support both retrieval and generation

---

### 10. Srijika: OpenType-Layout-Reusing Font Restyling for Nine Indic Scripts
**Authors:** Anil Pai
**arXiv:** [arxiv.org/abs/2609.05661](https://arxiv.org/abs/2609.05661)
**Summary:** We present Srijika, a system for producing installable OpenType fonts for nine Brahmic scripts: Devanagari, Tamil, Bengali, Telugu, Kannada, Malayalam, Gujarati, Gurmukhi, and Odia. All pass the OpenType Sanitizer, while HarfBuzz and CoreText reproduce the template glyph-ID sequences on conjunct-heavy probes.
**Trending because:** 14 HuggingFace upvotes + produces complete fonts for nine Indic scripts while preserving complex OpenType shaping behavior

---

### 11. VākQA: A Benchmark and Evaluation Study for Telugu Spoken Factoid Question Answering
**Authors:** Bhavana Akkiraju, Ravi Sastry Kolluru, Sri Charan D, Srihari Bandarupalli, Santosh Kesiraju, Anil Vuppala
**arXiv:** [arxiv.org/abs/2609.19879](https://arxiv.org/abs/2609.19879)
**Summary:** We introduce VākQA, a Telugu SQA benchmark of 2,001 factoid question-answer pairs across six domains, with 2.53 hours of speech audio, bilingual transcriptions, and human-verified reference answers. We observe that Telugu phrasing retains cultural specificity that is lost in translation, speech input introduces phonetic confusions that alter question meaning, and cascaded ASR-MT errors compound progressively.
**Trending because:** 12 HuggingFace upvotes + introduces the first Telugu spoken factoid QA benchmark and audits automatic evaluation reliability

---

### 12. Flattening Every Memory Peak in Long-Context Mixture-of-Experts Training
**Authors:** Shrey Pandit, Xuan-Phi Nguyen, Yiran Zhao, Shafiq Joty
**arXiv:** [arxiv.org/abs/2609.14306](https://arxiv.org/abs/2609.14306)
**Summary:** We bound all four with schedules whose GPU working set is fixed at launch: PipelinedLLEP extends least-loaded expert parallelism with a cap on the tokens each source contributes to a dispatch chunk, Ring-DTP circulates activations or weight shards around a ring at the vocabulary projection and folds each block of logits into an online log-sum-exp, Selective checkpoint offload (SCO) keeps the one long-lived tensor of each checkpoint boundary in CPU memory, and OffloadStreamAdamW turns the serial CPU Adam update of optimizer offload into a bucket pipeline. Composed on MoE models from 120B to 667B parameters, they train at 1M context length, 8--32times the reach of a tuned FSDP2 baseline, and up to 10.4times its throughput.
**Trending because:** 10 HuggingFace upvotes + bounds four distinct memory peaks to enable million-token training of very large MoE models

---

### 13. PANORAMA: Panoptic Grounded Captioning via Mask Proposal Selection
**Authors:** Sara Pieri, Evangelos Kazakos, Shizhe Chen, Josef Sivic, Cordelia Schmid
**arXiv:** [arxiv.org/abs/2609.19143](https://arxiv.org/abs/2609.19143)
**Summary:** Second, we formulate phrase grounding as selection from a phrase-conditioned pool of mask proposals and introduce PANORAMA, a VLM that conditions a pretrained segmenter on contextualized phrase representations to obtain candidate masks and learns to select those corresponding to each phrase. Third, PANORAMA achieves the best overall grounding on PanoCaps and matches or exceeds specialized models across several pixel-level grounding tasks.
**Trending because:** 10 HuggingFace upvotes + pairs detailed captions with precise phrase-level pixel masks across foreground and background regions

---

### 14. The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction
**Authors:** Yu Lin, Yiming Wang, Runyuan Cai, Hanze Liu, Xiaodong Zeng
**arXiv:** [arxiv.org/abs/2609.18063](https://arxiv.org/abs/2609.18063)
**Summary:** We present Edge0, a streaming MoE inference engine that closes the gap with a prerouter: a per-layer head predicts the next layer's routing one token ahead, and the prediction is consumed as the routing itself, so the staged expert set equals the routed set and nothing is dropped. On a single 24GB machine, Edge0 serves a 35B MoE at 20tok/s inside 3GiB of peak active memory, within a few points of its fp16 teacher on average across five public benchmarks.
**Trending because:** 10 HuggingFace upvotes + streams a 35B MoE from SSD at 20 tokens per second on a single 24GB machine

---

### 15. GLiClass: Generalist Lightweight Model for Sequence Classification Tasks
**Authors:** Ihor Stepanov, Mykhailo Shtopko, Dmytro Vodianytskyi, Oleksandr Lukashov, Alexander Yavorskyi, Mykyta Yaroshenko
**arXiv:** [arxiv.org/abs/2508.07662](https://arxiv.org/abs/2508.07662)
**Summary:** We propose GLiClass, a novel method that adapts the GLiNER architecture for sequence classification tasks. Our approach achieves strong accuracy and efficiency comparable to embedding-based methods, while maintaining the flexibility needed for zero-shot and few-shot learning scenarios.
**Trending because:** 9 HuggingFace upvotes + offers efficient zero-shot and few-shot classification without generative-LLM overhead

---

### 16. CERA-MoA: Co-Evolving Routing Mechanisms with Continually Learning LLM Agents
**Authors:** Jiaxuan Jiang, Liyuan He, Zhixuan Fang
**arXiv:** [arxiv.org/abs/2609.18779](https://arxiv.org/abs/2609.18779)
**Summary:** To resolve this, we introduce CERA-MoA (Co-Evolving Router with continually learning Agents for Mixture-of-Agents), an iterative reinforcement learning framework where the dynamic router and independent agent policies co-evolve. Extensive experiments across various domains demonstrate that CERA-MoA outperforms state-of-the-art static-agent routing and fix-workflow fine-tuning baselines.
**Trending because:** 5 HuggingFace upvotes + co-evolves agent specialization and routing rather than optimizing them separately

---

### 17. Register Tokens for Bounded-State Reasoning in Diffusion Language Models
**Authors:** Albert Ge, Chandan Singh, Yufan Zhuang, Xiaodong Liu, Jianfeng Gao, Frederic Sala
**arXiv:** [arxiv.org/abs/2609.16372](https://arxiv.org/abs/2609.16372)
**Summary:** We implement this state as a small number of register tokens: dedicated fixed-position tokens whose continuous hidden states are trained to carry reasoning progress across generation chunks. In our main comparisons on LLaDA and Dream, registers outperform discrete-text carry on every benchmark, with gains of up to 8.5 points on math and 19.5 points on code.
**Trending because:** 5 HuggingFace upvotes + carries diffusion-model reasoning across cleared chunks using a fixed-size continuous state

---

### 18. Assessing nnU-Net Generalization across Brain Tumor Populations in BraTS-GoAT 2026
**Authors:** Tristan Kirscher, Vivian Metzger, Philippe Meyer, Xavier Coubez
**arXiv:** [arxiv.org/abs/2609.15524](https://arxiv.org/abs/2609.15524)
**Summary:** We trained a conventional 3D nnU-Net on 1,351 labeled cases using five-fold cross-validation and 1,000 epochs per fold. Under matched fold-0 inference, mean regional Dice decreased from 0.9058 on source out-of-fold (OOF) cases to 0.8310 on pooled validation (difference--0.0747).
**Trending because:** 2 HuggingFace upvotes + quantifies how a standard medical segmentation model generalizes across heterogeneous tumor populations

---

### 19. Fathom: Per-Query Read Depth for Sparse Decoding over Offloaded KV Caches
**Authors:** Vivek Kalyanarangan
**arXiv:** [arxiv.org/abs/2609.17652](https://arxiv.org/abs/2609.17652)
**Summary:** We present Fathom, a key scan in which each query decides how many bits of each key channel to read. At one million tokens on Qwen3-8B a decode step is 1.67x faster in GPU time than with the 136-bit scans of Double Sparsity, Loki and SparQ r=32, and in the same GPU time as SparQ's 68-bit read (r=16) Fathom reads 18% fewer bytes with lower attention error on six of seven model and context settings.
**Trending because:** 2 HuggingFace upvotes + adapts KV-cache scan precision per query to accelerate million-token agent sessions

---

### 20. Fingers as Legs: Learning Self-Supported Locomotion and Manipulation with an Anthropomorphic Hand
**Authors:** Amirhossein Kazemipour, Hehui Zheng, Robert Katzschmann
**arXiv:** [arxiv.org/abs/2609.17172](https://arxiv.org/abs/2609.17172)
**Summary:** We show how an anthropomorphic hand can learn these skills while retaining its finger design and position controller. While supporting its own weight, the hand also executes successive keyboard commands without vision and pushes an object to targets using overhead visual feedback.
**Trending because:** 1 HuggingFace upvotes + reuses an anthropomorphic hand’s fingers for both untethered locomotion and manipulation
