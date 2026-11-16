---
title: "Daily AI Papers — November 15, 2026"
date: 2026-11-15
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-15/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - robot-learning
  - ai-agents
  - llm-evaluation
---

### 1. Auriga Technical Report: A Task-Agnostic Agent Harness for Zero-Shot Embodied Manipulation
**Authors:** Chengcheng Wang, Yuheng Shi, Siyu Xu, Yutong Wang, Jinjing Zhao, Chenghao Xia, Jinqi Liao, Jiankun Peng, Ligong Bi, Yuechuan Ma, Jiaqi Liu, Wenbo Wang, Zijian Wang, Yuemin Wu, Minjing Dong, Xiu Su, Tao Huang, Jianyuan Guo, Chengbin Du, Yunke Wang, Chang Xu
**arXiv:** [arxiv.org/abs/2611.01112](https://arxiv.org/abs/2611.01112)
**Summary:** Auriga gives a vision-language model an explicit task belief, calibrated 3D measurements, trajectory previews, and guarded dual-arm execution for zero-shot manipulation. The frozen harness achieves 57.7% success on RoboDojo and 73.2% on RoboCasa365, more than doubling the reference harness on the same model in the former benchmark.

---

### 2. Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies
**Authors:** Chubin Zhang, Bo An
**arXiv:** [arxiv.org/abs/2611.14488](https://arxiv.org/abs/2611.14488)
**Summary:** This study shows that time-indexed memory can make vision-language-action policies mistake pauses or wrist fidgets for completed work, causing premature stopping on counting tasks. Event-indexed memory recovers at least half of the resulting performance loss without retraining, whereas removing timestamps alone does not fix the shortcut.

---

### 3. CogBattery: Human-Referenced Evaluation of Cognitive Task Behavior and Structure in Language Models
**Authors:** Dengzhe Hou, Lingyu Jiang, Fangzhou Lin, Kazunori D Yamada
**arXiv:** [arxiv.org/abs/2607.24999](https://arxiv.org/abs/2607.24999)
**Summary:** CogBattery evaluates 54 open-weight language models on text adaptations of 13 cognitive paradigms using condition-level human reference data. Matching the direction of human effects does not ensure human-like errors or confidence, and larger models are not consistently closer to human behavior.

---

### 4. All Quiet on the Neural Front: Language Models Do Not Report Injected Pain States
**Authors:** Emilio Ferrara
**arXiv:** [arxiv.org/abs/2611.10123](https://arxiv.org/abs/2611.10123)
**Summary:** The authors inject pain-related activation directions into open-weight models and compare verbal reports against sham, perturbation, and text-only controls. Although probes and trained reporters can decode these behaviorally consequential states, untrained verbal reports provide no additional evidence of access to the injected pain state.

---

### 5. Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists
**Authors:** Guowei Xu, Jiaru Zou, Mete Erdogan, Haotian Ye, Pan Lu, James Zou
**arXiv:** [arxiv.org/abs/2611.12184](https://arxiv.org/abs/2611.12184)
**Summary:** Blind Variation and Selective Retention generates scientific proposals with deliberately limited task information, then uses prior empirical outcomes to select promising candidates. Across five proposer models and 12 scientific tasks, the framework improves originality and usefulness while discarding half the candidates and retaining most top-performing proposals.

---

### 6. LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation
**Authors:** Nesta Midavaine, Floris Fok, Paulo Mendes, Joao Silva, Önder Akaçık, Dimas Lima, Zülküf Genç
**arXiv:** [arxiv.org/abs/2610.37570](https://arxiv.org/abs/2610.37570)
**Summary:** LCM-Promo fine-tunes a language model on transactional commerce data to predict intent and monotonic promotion-response curves conditioned on session context. In a production churn-reactivation A/B test, it increases conversion by 1% and reduces promotion cost by 6% relative to the Segment-EMA baseline.

---

### 7. ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control
**Authors:** Xu Luo, Jiaying Yang, Hao Wu, Junlin Xie, Zijin Hong, Ji Zhang, Lianli Gao, Jingkuan Song
**arXiv:** [arxiv.org/abs/2611.13482](https://arxiv.org/abs/2611.13482)
**Summary:** ExRL adapts long-action-chunk robot policies by learning how many timesteps of each predicted chunk to execute rather than optimizing the full high-dimensional action sequence. A lightweight off-policy reinforcement-learning adapter enables sample-efficient adaptation across simulation benchmarks and real-world robotic tasks with minimal task-specific tuning.

---

### 8. FlyHash for LLM Agent Memory: An Empirical Validation and a New Application
**Authors:** Mohan Bheemadolu, Chrisogonas O. Odhiambo
**arXiv:** [arxiv.org/abs/2611.05791](https://arxiv.org/abs/2611.05791)
**Summary:** This study applies FlyHash's sparse random projections and winner-take-all competition to language-model agent memory, validating retrieval quality under matched-bit and genuine relevance-label evaluations. Its quality advantage does not yield broad latency or memory savings: dense HNSW indexing dominates both tested hashing approaches at ordinary scales.

---

### 9. JoVox: Joint Hierarchical Flow Matching for Lightweight Voxel Generation
**Authors:** Xiangjun Tang, Jianqi Chen, Peter Wonka
**arXiv:** [arxiv.org/abs/2611.10690](https://arxiv.org/abs/2611.10690)
**Summary:** JoVox jointly models every level of a voxel hierarchy with discrete flow matching, allowing fine cells to inform and revise coarse decisions. Compared with TRELLIS.2, the authors report eightfold higher training throughput, one-fifteenth the forward-pass FLOPs, and an 11% lower Chamfer distance.

---

### 10. EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery
**Authors:** Haoran Zhang, Huizhen Sun, Hanbin Wen, Jie Leng, Jiaxin Zhu, Zhaohua Sun
**arXiv:** [arxiv.org/abs/2611.12934](https://arxiv.org/abs/2611.12934)
**Summary:** EarthRecord evaluates multimodal agents on 238 land-change questions at 56 sites using four decades of raw multi-sensor satellite imagery, leaving preprocessing to the agents. Twelve-agent evaluations show that many workflows complete end to end but remain vulnerable to sensor alterations, revealing a gap between image-grounded answers and reliable land-change inference.

---

### 11. SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable Dermatology AI
**Authors:** Jing Hao, Weinan Zhou, Zhihong Lu, Yaling Shen, Yiming Xu, Yefeng Liu, Siyuan Yan, Shuaibo Li, Ming Dai, Junjun He, Zuyi Zhu, Jinjie Gu, Lijun Wu, Jian Wang
**arXiv:** [arxiv.org/abs/2611.08935](https://arxiv.org/abs/2611.08935)
**Summary:** SkinMind uses eight hierarchical graph-probing tools to retrieve textual, relational, and visual dermatology evidence from a graph with over one million nodes and two million edges. Across six dermatology visual-question-answering benchmarks, it improves average scores over direct answering by 8.70 and 8.89 points with two evaluated policy models while outperforming competing retrieval methods.

---

### 12. FraudBench: A Legal Evaluation of AI Deception
**Authors:** Kevin Wei, Sumaya Nur Adan, Stephan Llerena, Mark Gitau, Jakob Merane, Anita Srinivasan, Colette Le Brannan, Keethan Kleiner, Alessandro Tacconelli, Michael Tiu Jr., Case Thomason, Kyle Emili, Natasza Gadowska, Alex Mark, Eric Ren, Umang Bhatt, Jatinder Singh, Jacy Reese Anthis, Doni Bloomfield, Noam Kolt
**arXiv:** [arxiv.org/abs/2611.12167](https://arxiv.org/abs/2611.12167)
**Summary:** FraudBench evaluates model recommendations, drafted messages, and autonomous actions in 159 expert-validated scenarios derived from court cases, for 477 tasks. Across 20 language models, the authors report higher rates of benchmark-scored misrepresentation or concealment as autonomy increases, from 3.0% when advising to 21.4% when acting directly.

---

### 13. RidgeFill: Training-Free Late-Layer Cache Fill for Faster Prefill
**Authors:** Dylan Johnston, Robert P. Smith
**arXiv:** [arxiv.org/abs/2611.09709](https://arxiv.org/abs/2611.09709)
**Summary:** RidgeFill accelerates prefill by using closed-form ridge-regression maps to predict late-layer inputs and populate their caches while retaining full-model decoding and selected exact prompt rows. Reported time-to-first-token speedups reach 1.25 to 1.31 times on a dense model and 1.50 to 1.60 times on a hybrid model, with measured long-context quality tradeoffs rather than a guarantee of no loss.

---

### 14. Learning to Act with World Models by Valuing What Comes Next
**Authors:** Chenghao Gao, Zhi Zhang, Dian Jin, Yihe Pan, Doudou Zhou
**arXiv:** [arxiv.org/abs/2611.12200](https://arxiv.org/abs/2611.12200)
**Summary:** WM-PPO combines world-model predictions with critic values to supply auxiliary policy advantages and value targets for actions that may not be executed. With comparable real-environment steps and no teacher or privileged information, it raises success from 63.5% to 87.5% on ALFWorld and from 39.3% to 52.9% on ScienceWorld.

---

### 15. EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video Understanding
**Authors:** Changti Wu, Ruizhe Fan, Bin Wang, Lei Zhang, Yuxiang Zhang
**arXiv:** [arxiv.org/abs/2611.13907](https://arxiv.org/abs/2611.13907)
**Summary:** EVAThink learns when to answer directly and when to reason by contrasting evidence-dense and evidence-sparse video views under identical frame budgets. Two-stage reinforcement learning on 6.7 thousand curated samples improves video-understanding performance across benchmarks while refining response efficiency and mitigating mode collapse.

---

### 16. PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing
**Authors:** Yiwen Song, Yale Song, Tomas Pfister, Jinsung Yoon
**arXiv:** [arxiv.org/abs/2604.05018](https://arxiv.org/abs/2604.05018)
**Summary:** PaperOrchestra is a multi-agent system that transforms unconstrained research materials into LaTeX manuscripts with literature synthesis and generated visuals. On PaperWritingBench and side-by-side human evaluations, it outperforms autonomous baselines with reported win-rate margins of 50% to 68% for literature-review quality and 14% to 38% for overall manuscript quality.

---

### 17. The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages?
**Authors:** Nikhil Sharma, Kelly Marchisio, Kenton Murray, Ziang Xiao
**arXiv:** [arxiv.org/abs/2611.12750](https://arxiv.org/abs/2611.12750)
**Summary:** NarrativeBench evaluates six capabilities for navigating competing multilingual narratives using 1,333 news articles, 23 publication languages, and 460 Reddit-grounded queries. Tests of 14 language models across 24 query languages expose substantial gaps in narrative coverage and information parity even when diverse perspectives are explicitly requested.

---

### 18. Predictive Surprise as Self-Grounding Concept Bottleneck for Interpretable Time Series
**Authors:** Sachith Abeywickrama, Emadeldeen Eldele, Min Wu, Xiaoli Li, Chau Yuen
**arXiv:** [arxiv.org/abs/2611.12955](https://arxiv.org/abs/2611.12955)
**Summary:** ConceptTime uses predictive surprise from a frozen forecaster to jointly locate time-series segment boundaries and build a vocabulary of interpretable dynamical concepts. Across 17 benchmarks it remains competitive with black-box accuracy, beats the evaluated interpretable baselines, and supports reliability estimation without expert annotations or language-model calls.

---

### 19. Bits or permutations? Spending a fixed inference budget on weight precision or on option-order averaging in small local language models
**Authors:** Mohammed Nayeem Khan, Logesh L, Aliyas Ahmad Misri
**arXiv:** [arxiv.org/abs/2611.14413](https://arxiv.org/abs/2611.14413)
**Summary:** This study jointly evaluates simulated weight quantization and answer-option-order averaging on two small Qwen models under a budget measured as weight bytes read times inference passes. Six-bit weights preserve accuracy in the evaluated settings, and the cost-matched analysis favors spending remaining budget on up to four cyclic option orders, with conclusions limited to the tested small models and quantizer.

---

### 20. TorchCurves: Differentiable Parametric Curves
**Authors:** Alex Shtoff
**arXiv:** [arxiv.org/abs/2611.14516](https://arxiv.org/abs/2611.14516)
**Summary:** TorchCurves provides differentiable vector-valued B-spline and Legendre curves as trainable primitives within PyTorch models, supporting gradients through both inputs and coefficients. Benchmarks cover curve evaluation and Kolmogorov-Arnold network training, identifying where the general vectorized implementation is practical and where its overhead is substantial.

---
