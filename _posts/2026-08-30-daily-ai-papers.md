---
title: "Daily AI Papers — August 30, 2026"
date: 2026-08-30
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-30/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - rag-retrieval
  - agent-benchmarks
  - world-models
---

### 1. What AstroPT knows about galaxies, and what that can teach us about LLMs
**Authors:** UniverseTBD, Kshitij Duraphe, Aman Kumar, Michael J. Smith, Shashwat Sourav
**arXiv:** [arxiv.org/abs/2608.22614](https://arxiv.org/abs/2608.22614)
**Summary:** Interpretability research increasingly asks when concepts emerge during training and whether linear probes recover real structure, but in language models these claims are hard to validate because language offers little ground-truth ordering of concepts or relationships among them. We propose the use of astronomical ground truth through AstroPT, a transformer trained on millions of galaxy images, as a calibration testbed.
**Trending because:** 5 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 2. PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration
**Authors:** Chen-Yu Lin, Jing-Wen Chen, Hsueh-En Chang, Hung-An Chen, Sheng-Hsun Chang, Chi-Pin Huang, Fu-En Yang, Min-Hung Chen, Yi-Ting Chen, Yu-Chiang Frank Wang, Shao-Hua Sun
**arXiv:** [arxiv.org/abs/2608.21031](https://arxiv.org/abs/2608.21031)
**Summary:** We present PhysCaP, a Physics-Informed Code-as-Policy agent for active perception in robotic manipulation. While vision-language-action policies excel at imitating demonstrations, they rely on passive observation and fail to infer latent physical properties critical for manipulation.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 3. The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration in Generative Search
**Authors:** Peiyang Liu, Xi Wang, Di Liang, Wei Ye
**arXiv:** [arxiv.org/abs/2608.23252](https://arxiv.org/abs/2608.23252)
**Summary:** As Retrieval-Augmented Generation (RAG) shifts toward diverse portfolio generation, it is stymied by two critical bottlenecks: flawed measurement of evidence utilization, and suboptimal context budget allocation. We resolve both sequentially.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 4. Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer Churn in Retrieval-Augmented QA
**Authors:** Jingjie Ning, Xueqi Li
**arXiv:** [arxiv.org/abs/2608.22856](https://arxiv.org/abs/2608.22856)
**Summary:** A retrieval-augmented QA system can return different answers after an index expansion even when its requested model identifier, prompt, retrieval policy, evidence depth, rendering, and exposed generation controls are held fixed. Aggregate accuracy may hide these changes when gains and losses cancel, while ordinary generation variability makes one-shot comparisons overstate update effects.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 5. From Generation to Simulation: How Far Are World Models from Being True Simulators?
**Authors:** Tong Wang, Huan Deng, Mucheng Yang, Yang He, Xiaohui Kuang, Gang Zhao
**arXiv:** [arxiv.org/abs/2608.23070](https://arxiv.org/abs/2608.23070)
**Summary:** With the rapid progress of diffusion models and large-scale video generation, generative world models are increasingly expected to replace traditional simulators, including physics engines, game engines, and reinforcement-learning environments. Yet the remaining distance from generation to simulation lacks a systematic assessment.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 6. ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts
**Authors:** YuanHang Xiao
**arXiv:** [arxiv.org/abs/2608.22510](https://arxiv.org/abs/2608.22510)
**Summary:** Agent benchmarks often evaluate only final answers even when agents run on stateful runtimes. We argue this under-specifies what is being evaluated: the proper unit is a declared model-plus-runtime configuration whose failures can occur in evidence acquisition, runtime routing, safety boundaries, or repeated execution.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 7. TorchMorph: CUDA-accelerated Morphological Transforms
**Authors:** Kai Zhao
**arXiv:** [arxiv.org/abs/2608.24738](https://arxiv.org/abs/2608.24738)
**Summary:** Morphological transforms are long-standing tools for shape and mask processing, but the de facto reference implementation in the Python ecosystem, i.e. scipy.ndimage, is CPU-only, single-array, and therefore unusable inside a GPU training loop without an expensive device-to-host round trip.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 8. PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX
**Authors:** Genghan Zhang, Yixin Dong, Chengze Fan, Zhichen Zeng, Yueming Yuan, Shaowei Zhu, Kunle Olukotun
**arXiv:** [arxiv.org/abs/2608.17379](https://arxiv.org/abs/2608.17379)
**Summary:** We introduce PTXBench, a benchmark for evaluating and adapting large language models (LLMs) to use architecture-specific PTX for GPU kernel optimization. PTXBench measures functional correctness, whether selected target instructions execute at runtime, and speedup over frontier libraries across GEMM and attention workloads on H100 and B200 GPUs.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 9. FlavourBench: Ranking Frontier Language Models with Executable Culinary Ground Truth
**Authors:** Josef Chen, Erim Hayretci
**arXiv:** [arxiv.org/abs/2608.20574](https://arxiv.org/abs/2608.20574)
**Summary:** Open-ended language-model benchmarks usually inherit a judge: a human preference panel, another model, or a brittle exact-match key. We introduce FlavourBench, an automated benchmark in which a versioned culinary system supplies dense, executable ground truth.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 10. RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling
**Authors:** Ziyuan Wang, Bohao Tang, Fei Zhang, Shuo Han, Pengfei Liu
**arXiv:** [arxiv.org/abs/2608.22849](https://arxiv.org/abs/2608.22849)
**Summary:** Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution. We present RIBOSPAN, a 1.61-billion-parameter bidirectional RNA foundation model natively pretrained with context lengths up to 10,240 nt.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 11. Tomatoes, Potatoes, and Onions: Questioning the Need for Faces in Face Presentation Attack Detection
**Authors:** Guray Ozgur, Fadi Boutros, Naser Damer
**arXiv:** [arxiv.org/abs/2608.21455](https://arxiv.org/abs/2608.21455)
**Summary:** Face presentation attack detection (PAD) is traditionally formulated as a face-specific problem, although many of the visual artifacts introduced by print, replay, and recapture processes are not inherently tied to facial appearance. In this work, we investigate whether transferable PAD representations can be learned without using faces during downstream PAD training.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 12. Hybrid Quantum-inspired Kolmogorov-Arnold Networks for Privacy-Aware Federated Biosignal Learning
**Authors:** Chun-Hua Lin, Samuel Yen-Chi Chen, Yu-Chao Hsu, Kuo-Chung Peng, Jiun-Cheng Jiang, Chi-Sheng Chen, Tai-Yue Li, Nan-Yow Chen, En-Jui Kuo, Hsi-Sheng Goan
**arXiv:** [arxiv.org/abs/2608.13914](https://arxiv.org/abs/2608.13914)
**Summary:** Electrocardiogram (ECG) recordings are sensitive biomedical data, limiting the ability of hospitals and wearable devices to share raw signals for centralized model training. Federated learning addresses this practical privacy constraint by enabling collaborative model training while keeping raw biosignal data at their respective sources.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 13. RetrievalRouter: Joint Modality and Architecture Selection for Document Retrieval
**Authors:** Emre Kuru, Mehmet Onur Keskin, Reza Farahbakhsh, Noel Crespi
**arXiv:** [arxiv.org/abs/2608.25625](https://arxiv.org/abs/2608.25625)
**Summary:** Document retrieval increasingly supports high-stakes information access in finance, healthcare, and law. Modern retrieval pipelines vary both in modality (text or multimodal) and in retrieval architecture (dense or late-interaction).
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 14. What Does an Evaluation License? A Commit-Bound Census of Claim-Relative Inference in Inspect Evals
**Authors:** Xi Qin
**arXiv:** [arxiv.org/abs/2608.19269](https://arxiv.org/abs/2608.19269)
**Summary:** Evaluation artifacts specify a forward computation: a task, scorer, and reported metric. They do not necessarily license the claim attached to that metric because the historical evidence and alternative semantics needed to replay it may be unbound.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 15. Drive, Pack, Fly: The Travelling Thief Problem with Drone
**Authors:** Kabir Murjani, Abhay Sobhanan
**arXiv:** [arxiv.org/abs/2608.16435](https://arxiv.org/abs/2608.16435)
**Summary:** In collection operations, accumulating payload progressively slows the vehicle, imposing a cumulative penalty on routing efficiency. An onboard drone can offset this penalty by retrieving outlying items, thereby shortening the makespan and increasing operational profit.
**Trending because:** 2 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 16. WorldRover: A Scalable Synthetic Video Data Engine for World Exploration with Rich Annotations
**Authors:** Xiaojie Xu, Zhengyuan Lin, Runyi Li, Yihao Liu, Kaipeng Zhang, Yongtao Ge
**arXiv:** [arxiv.org/abs/2608.15659](https://arxiv.org/abs/2608.15659)
**Summary:** Learning to generate or reconstruct explorable worlds requires video paired with more than RGB: camera motion, scene geometry, temporal correspondence and, for interactive models, control signals. Real capture can provide some of these signals, but dense geometry and long-range correspondence usually rely on estimation or specialised instrumentation.
**Trending because:** 2 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 17. Accuracy and Order Sensitivity Diverge Under Label-Free Strategies
**Authors:** Karl Hanna, Chen Feng
**arXiv:** [arxiv.org/abs/2608.11947](https://arxiv.org/abs/2608.11947)
**Summary:** Multiple-choice benchmarks are widely used to evaluate large language models, but MCQ scores conflate knowledge with sensitivity to option order, which makes them unreliable measures of model knowledge. In this paper, we test whether preventing a model from seeing option labels while committing to an answer removes positional influence and, in turn, improves performance.
**Trending because:** 2 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 18. When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse
**Authors:** Yingtao Ren, Ziyi Zhao, Yiwei Fu, Xiao Luo, Yu-Cheng Chang, Chin-Teng Lin
**arXiv:** [arxiv.org/abs/2608.06947](https://arxiv.org/abs/2608.06947)
**Summary:** Retrieval-augmented generation (RAG) is indispensable for enhancing large language models. However, RAGs are increasingly susceptible to poisoning attacks, in which adversarial documents are injected to manipulate generator outputs.
**Trending because:** 2 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 19. Position: AI Agents in Scientific Teams Should Be Studied as Human-Agent Systems
**Authors:** Patrick Emami, Sameera Horawalavithana, Truc Nguyen, Gihan Panapitiya, Bruno Jacob, Siddhisanket Raskar, Saumya Sinha, Jared D. Willard, Andrew Glaws, Nithin Somasekharan, Ling Yue, Brian Lu, Shaowu Pan, Jason Eisner
**arXiv:** [arxiv.org/abs/2608.14667](https://arxiv.org/abs/2608.14667)
**Summary:** Large language model-based agents are increasingly deployed as collaborators in scientific discovery yet most current work focuses on the autonomous capabilities of "AI Scientists". We argue that this overlooks the social aspects of scientific teamwork, and that studying AI Scientists as human-agent systems (HAS)--where the unit of analysis is the human-agent pair--is both underexplored and undervalued.
**Trending because:** 2 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 20. Valid Per-Field Selective Risk Control for Document Extraction: Three Failure Modes, a Validity Ladder, and When Conditioning Pays
**Authors:** Bhaskar Gurram
**arXiv:** [arxiv.org/abs/2608.14639](https://arxiv.org/abs/2608.14639)
**Summary:** Per-field accept/review with selective risk at most alpha -- accept a field only if the error rate among accepted fields is controlled -- is the trust contract document-extraction systems need, and the natural procedure silently violates it on real documents. On 13,859 genuine claude-sonnet-5 fields from 800 CORD receipts (49.0% correct) we diagnose three failure modes: document clustering (design effect 1.84-2.45), score-refit leakage (coverage 0.416 at risk 0.127, violating alpha=0.10 in 95% of splits), and a tie-mass pathology (a degenerate score collapses the threshold grid, 0.030 to 0.001).
**Trending because:** 2 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance
