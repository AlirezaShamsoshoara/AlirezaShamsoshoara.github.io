---
title: "Daily AI Papers — September 12, 2026"
date: 2026-09-12
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-12/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-reasoning
  - multimodal-ai
  - ai-systems
---

### 1. An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics
**Authors:** Ivan Moshkov, Stephen Ge, George Armstrong, Wei Du, Sadegh Mahdavi, Igor Gitman
**arXiv:** [arxiv.org/abs/2609.10712](https://arxiv.org/abs/2609.10712)
**Summary:** We study how model post-training and test-time inference design affect natural-language proof generation for hard olympiad mathematics. Starting from Nemotron 3 Ultra, we train two specialist checkpoints using supervised fine-tuning and reinforcement learning, and evaluate checkpoint choice, verification, and refinement.
**Trending because:** 22 HuggingFace upvotes + demonstrates an open natural-language proof pipeline that reaches the IMO 2026 gold-medal threshold

---

### 2. MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes
**Authors:** Remco Hendriks
**arXiv:** [arxiv.org/abs/2609.10016](https://arxiv.org/abs/2609.10016)
**Summary:** We introduce MetroLLM-Bench, a 955-case benchmark for testing language models as the policy layer of a transit kiosk. It covers six real metro systems, ranging from 37 to 414 stations, and eleven categories that include routing, fare calculation, disruptions, accessibility, and adversarial input.
**Trending because:** 19 HuggingFace upvotes + tests language models as policy runtimes across realistic transit-kiosk tasks

---

### 3. Studying Image Tokenizers as Visual Languages in Unified Multimodal Models
**Authors:** Siting Li, Zhengyang Wang, Simon Shaolei Du, Xi Chen, Yang Liu
**arXiv:** [arxiv.org/abs/2609.09143](https://arxiv.org/abs/2609.09143)
**Summary:** Image tokenizers define the ``visual language'' of unified multimodal models, yet are commonly studied through isolated metrics or generation-/understanding-only evaluations. These evaluations do not fully capture how visual tokens behave when modeled jointly with text.
**Trending because:** 18 HuggingFace upvotes + treats image tokenizers as visual languages inside unified multimodal models

---

### 4. Negative Self-Distillation: Learning to Reason by Avoiding Flaws
**Authors:** Rongcan Pei, Zhepei Wei, Shuyao Xu, Xinyu Zhu, Wei-Lin Chen, Yu Meng
**arXiv:** [arxiv.org/abs/2609.11699](https://arxiv.org/abs/2609.11699)
**Summary:** On-Policy Self-Distillation (OPSD) has emerged as a popular paradigm for large language model (LLM) self-improvement, allowing models to act as their own teachers by leveraging privileged information such as ground-truth solutions. However, recent findings indicate that OPSD can severely degrade the performance of LLMs on complex reasoning tasks: By forcing the student to imitate an artificially confident reasoning trace conditioned on privileged information, OPSD inadvertently suppresses expressions of uncertainty and penalizes the exploratory, self-corrective behaviors required to solve challenging problems.
**Trending because:** 17 HuggingFace upvotes + improves reasoning by training models to avoid flawed self-distillation traces

---

### 5. HyQuant: Hybrid-Precision Quantization for LLM Attention
**Authors:** Jiatong Ding, Bingxin Xing, Yu Zhang, Dian Ding, Xiaodong Yi, Xianbin Ouyang, Feihu Zhou, Kun Zhang, Zhenyu Guo, Hao Pan, Guangtao Xue, Yiming Zhang
**arXiv:** [arxiv.org/abs/2608.27875](https://arxiv.org/abs/2608.27875)
**Summary:** Quantization has been widely adopted in LLM training and inference to reduce cost and improve efficiency. However, low-bit quantization of the attention module often introduces large errors at very low bit-widths, causing performance degradation.
**Trending because:** 17 HuggingFace upvotes + targets the accuracy losses caused by very-low-bit attention quantization

---

### 6. Building Multilingual Bridges: Data Mixing as the Pillar of Generalization for In-Language Reasoning
**Authors:** Mehrnaz Mofakhami, Ananya Sahu, Alejandro R. Salamanca, Daniel D'souza, Alexandre Berard, Thomas Euyang, Marzieh Fadaee, Julia Kreutzer
**arXiv:** [arxiv.org/abs/2609.10445](https://arxiv.org/abs/2609.10445)
**Summary:** Reasoning language models have made substantial advances on a variety of complex tasks, yet their capabilities remain overwhelmingly English-centric: models primarily reason in English regardless of the language they are prompted in. This is inaccessible for non-English-speaking users, risks losing the intent of the original question, and forgoes knowledge more readily expressed in the target language.
**Trending because:** 16 HuggingFace upvotes + examines data mixing as the foundation for multilingual in-language reasoning

---

### 7. Generative Late-Interaction Embeddings For Visual Document Retrieval
**Authors:** Mohamed Eltahir, Talal Aloushan, Rose Khairoalsendi, Jana Shata, Mohammed Alhassan, Leen Alrehaili, Tanveer Hussain, Naeemullah Khan
**arXiv:** [arxiv.org/abs/2609.11808](https://arxiv.org/abs/2609.11808)
**Summary:** Late-interaction retrieval is the state-of-the-art for visual document search, but it pays for its accuracy in storage. Existing compression methods retain a subset or local average of the N~1,000 vectors per page.
**Trending because:** 14 HuggingFace upvotes + reduces the storage burden of late-interaction visual document retrieval

---

### 8. UniH^3: Unifying Hierarchical Homogeneity and Heterogeneity for All-in-One Medical Image Restoration
**Authors:** Zhiwen Yang, Jiayin Li, Chengyu Liu, Hui Zhang, Bingzheng Wei, Yan Xu
**arXiv:** [arxiv.org/abs/2609.11156](https://arxiv.org/abs/2609.11156)
**Summary:** All-in-One medical image restoration (MedIR) aims to address diverse tasks across modalities and degradation types using a single universal model. Existing methods typically prioritize modeling inter-task heterogeneity (e.g., distinct data distributions and degradation types).
**Trending because:** 14 HuggingFace upvotes + unifies medical image restoration across modalities and degradation types

---

### 9. Beyond Solver Verdicts: Generative Reward Models for Autoformalization
**Authors:** Vikash Singh, Debargha Ganguly, Aman Goel, Ali Torkamani, Xiaoxue Han, Joseph Lilien, Ferhat Erata, Vipin Chaudhary
**arXiv:** [arxiv.org/abs/2609.11085](https://arxiv.org/abs/2609.11085)
**Summary:** Neurosymbolic systems rely on mathematical solvers to guarantee reasoning correctness, yet solvers are fundamentally blind to whether a formal translation maintains strict reference-equivalence to a designated formalization. We formalize this vulnerability as Verdict-Preserving-Unfaithfulness (VPU): a failure mode where an incorrect encoding executes successfully and matches the expected verdict.
**Trending because:** 13 HuggingFace upvotes + audits verdict-preserving but unfaithful translations in autoformalization

---

### 10. CARDEA: Auditable Reasoning Grounded in Spatial Evidence for End-to-End Coronary Angiography Interpretation
**Authors:** Jia-Jen Lee, Shih-Yen Hou, Kee Koon Ng, Wei-Chun Wang, Shih-Sheng Chang
**arXiv:** [arxiv.org/abs/2609.06931](https://arxiv.org/abs/2609.06931)
**Summary:** Invasive coronary angiography (CAG) is the gold standard for diagnosing coronary artery disease, but interpretation varies substantially among observers. Existing AI systems can improve consistency but lack auditable decision processes and are limited in comprehensive open-ended assessment, undermining clinician trust and clinical adoption readiness.
**Trending because:** 13 HuggingFace upvotes + grounds coronary angiography interpretation in auditable spatial evidence

---

### 11. IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications
**Authors:** Yiling Ma, Yilun Zhao, Sihong Wu, Manasi Patwardhan, Arman Cohan
**arXiv:** [arxiv.org/abs/2609.10539](https://arxiv.org/abs/2609.10539)
**Summary:** A research idea may be novel, coherent, and scientifically plausible, yet its proposed method may remain insufficiently specified for faithful implementation. We study the codification readiness of implementation-facing research-method specifications, defined by whether they provide sufficient methodological information for a competent implementer or coding agent to construct the intended method without unsupported assumptions.
**Trending because:** 12 HuggingFace upvotes + benchmarks whether research ideas are specified well enough for faithful implementation

---

### 12. ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable Peer Review Generation
**Authors:** Yiling Ma, Yilun Zhao, Sihong Wu, Ziyu Chen, Manasi Patwardhan, Arman Cohan
**arXiv:** [arxiv.org/abs/2609.09076](https://arxiv.org/abs/2609.09076)
**Summary:** As LLMs are increasingly used for pre-submission self-review, there is growing demand for feedback that not only identifies weaknesses but also guides authors toward concrete revisions. We study this as Actionable Peer-review Generation and decompose it into two subtasks: diagnostic claim generation and revision suggestion generation.
**Trending because:** 12 HuggingFace upvotes + trains language models to generate concrete, actionable peer-review revisions

---

### 13. Think Before You Link: Rarity, Reasoning, and Retrieval in Multilingual Entity Linking
**Authors:** Parinthapat Pengpun, Simran Khanuja, Graham Neubig
**arXiv:** [arxiv.org/abs/2609.10745](https://arxiv.org/abs/2609.10745)
**Summary:** Multimodal entity linking grounds entity mentions in text and images to knowledge-base entries. These systems degrade on rare entities, but prior work measures rarity primarily through popularity-based metrics such as pageviews.
**Trending because:** 12 HuggingFace upvotes + studies rarity-aware reasoning and retrieval for multilingual entity linking

---

### 14. DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning for Cooperative Air Combat
**Authors:** Junlin Liu, Chengwei Li, Yang Gao, Hui Chang, Xinchen Zhang, Zhijun Zhao, Hao Zhao
**arXiv:** [arxiv.org/abs/2609.11155](https://arxiv.org/abs/2609.11155)
**Summary:** Multi-Agent Reinforcement Learning (MARL) has emerged as a pivotal paradigm for complex decision-making in autonomous systems and air combat. While MARL has demonstrated significant potential in air combat, achieving sophisticated tactical coordination remains a non-trivial challenge.
**Trending because:** 12 HuggingFace upvotes + uses dynamic role graphs for coordinated multi-agent air combat

---

### 15. Adaptive Bridge: A Proxy-Based Decoupling Layer for Mitigating DDS Backpressure in ROS 2
**Authors:** Kaushalraj Puwar, B. Thangaraju
**arXiv:** [arxiv.org/abs/2608.15380](https://arxiv.org/abs/2608.15380)
**Summary:** In systems built on Robot Operating System 2 (ROS 2) and using Data Distribution Service (DDS), a single network-impaired or throttled subscriber on a RELIABLE topic can cause backpressure that degrades throughput and latency for all other subscribers, including safety-critical ones sharing the publisher, because the publisher's DDS writer can no longer accept new samples. We present Adaptive Bridge, a proxy-based layer that decouples critical subscribers from degraded or noncritical ones, thereby isolating the critical path through topic splitting and dynamic rate control.
**Trending because:** 12 HuggingFace upvotes + isolates safety-critical ROS 2 subscribers from DDS backpressure

---

### 16. A Three-Layer Caching Architecture for Low-Latency LLM Web Search on Commodity CPU Hardware
**Authors:** Ayushman Bhattacharya, Nihal Gazi
**arXiv:** [arxiv.org/abs/2609.05463](https://arxiv.org/abs/2609.05463)
**Summary:** AI-powered search products such as ChatGPT search, Google's AI Overviews, and Perplexity provide LLM-synthesized answers grounded in live web results. We developed OreoLook (formerly lixSearch), an open-source answer engine using automated browser agents and provider-routed LLM inference.
**Trending because:** 8 HuggingFace upvotes + uses layered caching to lower LLM web-search latency on commodity CPUs

---

### 17. Co-Evolving Harnesses and Models: On-Policy Correction Helps Weaker Models Catch Up Where Imitation Fails
**Authors:** Zhou Yu, Bin Bi, Shiva Kumar Pentyala, Shubham Mehrotra, Sougata Chaudhuri, Shilpa Bhagavath, Zeyuan Chen, Ran Xu, Phil Mui, James Zhu, Sitaram Asur
**arXiv:** [arxiv.org/abs/2609.09134](https://arxiv.org/abs/2609.09134)
**Summary:** Agent harnesses (the system prompt, tool set, execution hooks, and context-management scaffolding around a model) are a critical determinant of agentic task success. Automated harness evolution can enable smaller models to perform well on domain-specific tasks at a fraction of frontier-model cost.
**Trending because:** 7 HuggingFace upvotes + co-evolves agent harnesses and models through on-policy correction

---

### 18. PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in Autonomous Driving
**Authors:** Yuan Gao, Sebastian Müller, Mattia Piccinini, Marc Kaufeld, Yuchen Zhang, Finn Rasmus Schäfer, Qunying Song, Johannes Betz
**arXiv:** [arxiv.org/abs/2609.08965](https://arxiv.org/abs/2609.08965)
**Summary:** Ensuring the safety of autonomous driving is a critical challenge. Scenario-based testing is a systematic process used to validate Autonomous Driving Systems (ADSs), but it remains a fragmented modular pipeline in which scenario generation, retrieval, modification, ADS execution, and results analysis are performed by separate tools with little interaction.
**Trending because:** 5 HuggingFace upvotes + applies LLM agents to scenario-based testing of autonomous-driving motion planners

---

### 19. The Semantic Bottleneck: Leveraging Semantic Representations for Non-Invasive Speech Decoding
**Authors:** Gilad D. Landau, Dulhan Jayalath, Oiwi Parker Jones
**arXiv:** [arxiv.org/abs/2609.10296](https://arxiv.org/abs/2609.10296)
**Summary:** Non-invasive speech decoding remains constrained by the low signal-to-noise ratio of neural recordings, which makes fine-grained reconstruction of phonemes or individual words difficult. Motivated by neuroscientific evidence that high-level semantic representations are distributed across cortical regions and evolve over slower temporal scales, we hypothesize that semantic content may provide a more suitable target for non-invasive decoding than low-level acoustic or lexical features.
**Trending because:** 5 HuggingFace upvotes + uses high-level semantic targets for non-invasive speech decoding

---

### 20. DF26: We Cannot Tell Fake From Real Anymore
**Authors:** Severyn Shykula, Andrii Yermakov, Ivan Samarskyi, Dmytro Mishkin, Jan Cech, Anastasiia Mishchuk
**arXiv:** [arxiv.org/abs/2609.07369](https://arxiv.org/abs/2609.07369)
**Summary:** We introduce DF26, a novel benchmark for detecting AI-generated videos containing fully synthetic clips produced by recent text-to-video and image-to-video models. The videos capture single-person public-speaking scenarios, spanning direct-to-camera recordings, official statements, and studio interviews - 271 real and 2,420 synthetic videos generated by seven modern video models.
**Trending because:** 4 HuggingFace upvotes + shows how difficult modern AI-generated videos are to distinguish from real footage
