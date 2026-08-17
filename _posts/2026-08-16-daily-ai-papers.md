---
title: "Daily AI Papers — August 16, 2026"
date: 2026-08-16
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-16/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-memory
  - embodied-ai
---

### 1. Maglev: Sliding Recurrent Memory
**Authors:** Bo Liu, Qiang Liu
**arXiv:** [arxiv.org/abs/2608.02870](https://arxiv.org/abs/2608.02870)
**Summary:** Maglev is a recurrent Transformer architecture with fixed-size memory that generalizes sliding-window attention while remaining parallelizable during training. It couples a prefiller that leverages full attention to produce memory targets with a decoder that uses only sliding-window attention and recurrent K/V injection to produce decoder memories for next-token prediction.
**Trending because:** 9 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 2. SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models
**Authors:** Chenhao Dang, Siyuan Xiong, Conghui He, Weijia Li
**arXiv:** [arxiv.org/abs/2608.10538](https://arxiv.org/abs/2608.10538)
**Summary:** Agent skills represent a standardized format for packaging procedural knowledge and domain expertise, serving within agent harness systems as an essential mechanism to continually constrain a language model's behavior space for repeatable, high-quality task execution. However, because strong closed-source models entail high inference costs, current popular agent harnesses, such as Codex and OpenClaw, remain prohibitively expensive when deploying these skills to accomplish real-world tasks.
**Trending because:** 9 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 3. Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation
**Authors:** Hmrishav Bandyopadhyay, Xuanchi Ren, Zijian Huang, Jay Zhangjie Wu, Tianshi Cao, Ruilong Li, Bryan Chu, Sanja Fidler, Yi-Zhe Song, Zian Wang
**arXiv:** [arxiv.org/abs/2608.13391](https://arxiv.org/abs/2608.13391)
**Summary:** Interactive autoregressive video generation demands both low-latency rollouts and precise online control. Few-step distillation accelerates generation by reducing denoising steps, while online control imposes a causal constraint: frames and blocks should depend on history and controls available during generation.
**Trending because:** 9 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 4. LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation
**Authors:** Dongfang Li, Zixuan Liu, Junmai Wang, Jiahe Huang, Fuhao Li, Bonian Jia, Baotian Hu, Min Zhang
**arXiv:** [arxiv.org/abs/2608.12990](https://arxiv.org/abs/2608.12990)
**Summary:** Long-horizon LLM agents must preserve information from past interactions to support future tasks. Existing memory systems typically rely on eager consolidation, invoking LLMs after each interaction to extract, summarize, or update memories.
**Trending because:** 8 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 5. Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning
**Authors:** Xinyan Guan, Jiali Zeng, Chunlei Xin, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun, Fandong Meng
**arXiv:** [arxiv.org/abs/2607.29211](https://arxiv.org/abs/2607.29211)
**Summary:** Large language models generate computationally expensive yet semantically void reasoning on beyond-capability tasks, creating risks where plausible-sounding but incorrect derivations mislead users. We characterize this futile reasoning phenomenon through systematic analysis, revealing universal capability overreach and systematic miscalibration between capability and behavior.
**Trending because:** 7 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 6. Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing
**Authors:** Tianci Liu, Zihan Dong, Tianchun Li, Yi-Chung Chen, Qiming Cao, Xingchen Wang, Shiyang Wang, Zichen Miao, Linjun Zhang, Haoyu Wang, Jing Gao
**arXiv:** [arxiv.org/abs/2608.11660](https://arxiv.org/abs/2608.11660)
**Summary:** Large language models (LLMs) achieve remarkable performance across natural language tasks, yet they are trained on static corpora and their knowledge quickly becomes outdated in a fast-changing world. This motivates knowledge editing (KE), which updates specific knowledge in an LLM without changing unrelated others.
**Trending because:** 7 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 7. Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and Lexical Diversity
**Authors:** Irina Proskurina, Mayank Kumar, Oyindolapo O. Komolafe
**arXiv:** [arxiv.org/abs/2608.13430](https://arxiv.org/abs/2608.13430)
**Summary:** Instruction-tuned language models achieve strong performance across a range of generation tasks, but have also recently been shown to exhibit verbalized overconfidence. In question answering, verbalized model overconfidence may be associated with the consistency of the generated supporting rationales.
**Trending because:** 7 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 8. From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs
**Authors:** Yuanhe Zhang, Weiliu Wang, Jie Ren, Liang Lin, Zhenhong Zhou, Haoran Gao, Kun Wang, Chen Li, Li Sun, Sen Su
**arXiv:** [arxiv.org/abs/2608.09158](https://arxiv.org/abs/2608.09158)
**Summary:** Large audio-language models (LALMs) have demonstrated strong capabilities in understanding diverse audio inputs. This diversity includes low-frequency signals that are inaudible to humans but can still enter the model and influence its generation.
**Trending because:** 6 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 9. Specification-first convergence with an AI coding agent: a case study of dismantling a core architectural invariant across 189 files in a 717k-line codebase with no test oracle and no human code review
**Authors:** Joel Abenhaim
**arXiv:** [arxiv.org/abs/2608.12440](https://arxiv.org/abs/2608.12440)
**Summary:** This paper reports a single, fully instrumented case study of a large-scale architectural refactoring by an AI coding agent under a specification-first protocol, with no human review of the generated code and no pre-existing oracle to validate the target behaviour. The task, dismantling a central invariant across a large interdependent codebase, was assessed by the author as effectively infeasible through incremental refactoring, the kind of change that conventionally calls for a rewrite instead.
**Trending because:** 6 HuggingFace upvotes + among the more-upvoted papers in this weekend's feed.

---

### 10. Enfold: Folding World Model Imagination into Predictive Representations for Ultra-Efficient Embodied Control
**Authors:** Weili Zeng, Yitong Xing, Fulong Liu, Chengqun Yang, Antao Xiang, Feng Tian, Jingnan Gao, Jisong Cai, Xin Wang, Xiaomin Wu, Yao Mu, Xiaokang Yang, Yichao Yan
**arXiv:** [arxiv.org/abs/2607.26657](https://arxiv.org/abs/2607.26657)
**Summary:** World generative models are typically used through what they produce: a rendered future, a video-conditioned action, or latent context computed by a costly generative branch. We argue that their more reusable asset is the computation that constructs a future.
**Trending because:** 5 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 11. FATE: Frame-Level Audio-Visual Temporal Embedding
**Authors:** Kaisi Guan, Bingzi Zhang, Xihua Wang, Ying Ba, Xin Cheng, Yijing Chen, Ruihua Song
**arXiv:** [arxiv.org/abs/2608.01310](https://arxiv.org/abs/2608.01310)
**Summary:** When a dog opens its mouth and barks, humans naturally recognize what the sound is and when it occurs. Building audio-visual models with this same ability requires representations that capture both semantic and temporal alignment.
**Trending because:** 5 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 12. Adversarial Attacks for Good: A Survey of Proactive Protection across the Visual Content Lifecycle
**Authors:** Jiaming Zhang, Boyang Chen, Zherui Li, Fuyao Zhang, Xinyu Yan, Hong Xi Tae, Wenwen He, Xuan Wang, Siqi Guo, Junhao Dong, Kun Wang, Hanxun Huang, Yige Li, Xingjun Ma, Yang Cao, Lingjuan Lyu, Wei Yang Bryan Lim
**arXiv:** [arxiv.org/abs/2608.04314](https://arxiv.org/abs/2608.04314)
**Summary:** Once visual content enters an AI pipeline, its owner often retains little technical control over how it is used. Legal and regulatory remedies can address misuse, but many technical interventions must be applied earlier, when content is released or accessed.
**Trending because:** 5 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 13. OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understanding, and Interaction
**Authors:** Jiahao Huang, Zheng Lian, Jingyi Zhang, Zhide Chen, Xiaojiang Peng, Shaonan Wang
**arXiv:** [arxiv.org/abs/2608.06013](https://arxiv.org/abs/2608.06013)
**Summary:** Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in emotional intelligence. However, prevailing research predominantly focuses on task-specific specialization, often neglecting inter-task synergy and leaving latent reasoning potential underexplored.
**Trending because:** 5 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 14. Mitigating Gender Bias in English to Romanian Machine Translation
**Authors:** Ioana Grigore, Sergiu Nisioi
**arXiv:** [arxiv.org/abs/2608.08606](https://arxiv.org/abs/2608.08606)
**Summary:** Machine translation (MT) systems often fail to correctly translate gender, especially when converting from a gender-neutral language like English to a gendered target language such as Romanian. This bias results in translations that default to masculine forms or reinforce gender stereotypes.
**Trending because:** 5 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 15. Simplex Relaxation for Discrete Diffusion
**Authors:** Jinya Sakurai, Patrick Pynadath, Satoshi Hayakawa, Jaehong Yoon, Xulei Yang, Nancy F. Chen, Xun Xu
**arXiv:** [arxiv.org/abs/2608.10615](https://arxiv.org/abs/2608.10615)
**Summary:** Discrete diffusion models for categorical generation are defined by a corruption kernel, which determines the intermediate state space and the associated reverse prediction problem. We study uniform discrete diffusion and ask whether its training objective and reverse transitions can be enriched without changing the underlying categorical corruption process.
**Trending because:** 5 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 16. Poor Man's Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop
**Authors:** Igor Itkin
**arXiv:** [arxiv.org/abs/2608.11215](https://arxiv.org/abs/2608.11215)
**Summary:** Simulating societies of many large language model (LLM) agents is expensive, yet the questions asked of such simulations are usually macroscopic: phase behaviour, stylised facts, and scaling with the number of agents N, not the cognition of any single agent. We turn a statistical-physics observation into a method: replace each LLM agent by a low-parameter model fitted from a few hundred to a few thousand cheap queries, then run the society at any N on a laptop.
**Trending because:** 5 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 17. Gaze Target Estimation Anywhere with Concepts
**Authors:** Xu Cao, Houze Yang, Vipin Gunda, Zhongyi Zhou, Tianyu Xu, Adarsh Kowdle, Inki Kim, James M. Rehg
**arXiv:** [arxiv.org/abs/2608.11367](https://arxiv.org/abs/2608.11367)
**Summary:** Estimating human gaze targets from images in-the-wild is an important and formidable task. Existing approaches primarily employ brittle, multi-stage pipelines that require explicit inputs, like head bounding boxes and human pose, in order to identify the subject of gaze analysis.
**Trending because:** 5 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 18. PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just What They Say
**Authors:** Mingxuan Zhang, Jiahui Han, Dadi Guo, Songze Li, Guanchu Wang, Na Zou, Dongrui Liu, Xia Hu
**arXiv:** [arxiv.org/abs/2606.00152](https://arxiv.org/abs/2606.00152)
**Summary:** LLM-based agents are rapidly advancing, autonomously invoking external tools to complete multi-step tasks for users. However, agents often acquire more sensitive information than the task requires.
**Trending because:** 4 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 19. Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence
**Authors:** Ying Chen, Weizhen Li, Zhe Hu, Zhenjiang Li, Rui Jiang, Zhifeng Gu, Lihuang Fang, Jiangping Liu, Lei Yi, Jie Chen
**arXiv:** [arxiv.org/abs/2608.06756](https://arxiv.org/abs/2608.06756)
**Summary:** Vision-language models are increasingly serving as the reasoning core of embodied agents. Robot execution is inherently iterative: each action reshapes the scene and physical state, continually renewing what must be perceived, reasoned about, and verified.
**Trending because:** 4 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---

### 20. RibAssist 3D: Biplanar Rib-Fracture Detection, Addressing, and Selective 3D Localization from CT-Derived Projections
**Authors:** Kabila Haile Soboka
**arXiv:** [arxiv.org/abs/2608.06914](https://arxiv.org/abs/2608.06914)
**Summary:** Rib fractures are common and time-consuming to localize on computed tomography (CT). We ask whether fractures detected independently in two orthogonal CT-derived projections (anteroposterior and lateral) can be paired across views and triangulated into reliable 3D points at a controlled rate of false outputs, and we answer it with a staged diagnostic study.
**Trending because:** 4 HuggingFace upvotes + notable engagement given the weekend's lighter activity.

---
