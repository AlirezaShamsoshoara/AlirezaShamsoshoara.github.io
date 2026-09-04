---
title: "Daily AI Papers — September 5, 2026"
date: 2026-09-05
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-05/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - reasoning-models
  - multimodal-ai
---

### 1. StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments
**Authors:** Esakkivel Esakkiraja, Denis Akhiyarov, Vikas Yadav, Sai Rajeswar, Patrice Bechard, Sridhar Nemala, Sagar Davasam
**arXiv:** [arxiv.org/abs/2608.24804](https://arxiv.org/abs/2608.24804)
**Summary:** We present StarHarness, a framework for evolving environment-specific agent harnesses while keeping model weights fixed. The evolved harness can include prompt and task framing, tool interfaces, skills, MCP-backed providers, subagent structure, and agent-loop configuration.
**Trending because:** 41 HuggingFace upvotes + practical advances in evolving reliable agent harnesses

---

### 2. VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement
**Authors:** Wenzhuo Xu, Yuchen Zhu, Chongjian Ge, Xuan Shen, Jing Shi, Jason Kuen, Yongxin Chen, Molei Tao, Christopher McComb, Noelia Grande Gutiérrez, Jiuxiang Gu
**arXiv:** [arxiv.org/abs/2609.03153](https://arxiv.org/abs/2609.03153)
**Summary:** Visual fluency in generated video does not imply physical reliability, and a scalar quality score alone is incapable of indicating the obligation a clip violates or the moment it fails. We present VeriPhy, an auditable physical-verification system in which a text-only planner compiles the prompt into typed physical obligations and a statically validated execution plan before any frame is observed.
**Trending because:** 12 HuggingFace upvotes + auditable physical reasoning for generated-world evaluation

---

### 3. Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation
**Authors:** Zixing Lei, Gengze Zhou, Xiong-Hui Chen, Jiazhao Zhang, Yiyang Huang, Hang Yin, Haoqi Yuan, Qi Wu, Weixin Li, Siheng Chen
**arXiv:** [arxiv.org/abs/2608.30396](https://arxiv.org/abs/2608.30396)
**Summary:** Long-horizon physical-world agents must reason over distant goals while grounding decisions in reliable closed-loop behavior. Today's foundation models split these capabilities: vision-language models (VLMs) infer missing information and adapt high-level plans but remain brittle and inefficient at repeated navigation grounding, while navigation foundation models (NFMs) robustly execute semantic goals but operate as bounded episodes without persistent task-level reasoning.
**Trending because:** 10 HuggingFace upvotes + strong long-horizon embodied navigation results

---

### 4. Verification-Aware Training for Speculative Decoding
**Authors:** Geonmo Gu, Byeongho Heo, HeeJae Jun, Yoohoon Kang, Sangmin Lee, Sangdoo Yun, Dongyoon Han
**arXiv:** [arxiv.org/abs/2608.30135](https://arxiv.org/abs/2608.30135)
**Summary:** Speculative decoding accelerates large language model inference by using a draft model to generate candidate tokens, which are verified by the target model in a single forward pass. Verification proceeds sequentially and discards every position from the first rejection onward, yet existing draft training relies on token-level imitation of the target with a fixed per-position weighting that reflects neither property.
**Trending because:** 10 HuggingFace upvotes + faster LLM inference through verification-aware training

---

### 5. Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space
**Authors:** Qiancheng Zhou, Ruizhe Li
**arXiv:** [arxiv.org/abs/2608.29188](https://arxiv.org/abs/2608.29188)
**Summary:** Reinforcement learning with verifiable rewards (RLVR) substantially improves single-sample accuracy (pass@1) but causes the policy's solution space to contract, diminishing the returns of test-time scaling. In this work, we investigate where inside a reasoning trajectory this breadth is lost: does the policy fail to access a valid solution family, or does it fail to execute computation once initiated?
**Trending because:** 10 HuggingFace upvotes + new evidence on diversity collapse during RLVR

---

### 6. EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses
**Authors:** Tanmay Sah, Dolly Sah, Harshul Jain, Tanya Sah
**arXiv:** [arxiv.org/abs/2608.28363](https://arxiv.org/abs/2608.28363)
**Summary:** LLM agents increasingly modify their own prompts, tools, middleware, resources, and execution harnesses at runtime. Such self-evolution can improve capability, but a successful mutation may leave persistent effects that cannot be safely reversed in states different from the one in which it was created.
**Trending because:** 9 HuggingFace upvotes + recoverability safeguards for self-modifying agents

---

### 7. CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing
**Authors:** Huu Huy Nguyen, Chien Van Nguyen, Franck Dernoncourt, Ryan A. Rossi, Linh Ngo Van, Jieyang Chen, Thien Huu Nguyen
**arXiv:** [arxiv.org/abs/2609.01925](https://arxiv.org/abs/2609.01925)
**Summary:** The attention prefilling phase of long-context LLM inference scales quadratically, making self-attention a severe computational bottleneck. Traditional sparse attention methods mitigate this through fixed patterns or offline profiling, but lack the flexibility to adapt to input-dependent attention structure.
**Trending because:** 8 HuggingFace upvotes + long-context attention speedups with adaptive sparsity

---

### 8. WebWorld: The Browser as a World Model for Self-Improving Web Code
**Authors:** Jiajun Wu, Jian Yang, Yaxin Du, Wei Zhang, Haowen Wang, Junhang Cheng, Yuxuan Zhang, Tuney Zheng, Xianglong Liu, Ming Zhou
**arXiv:** [arxiv.org/abs/2608.30530](https://arxiv.org/abs/2608.30530)
**Summary:** VLM-driven self-improvement of web code has a structural flaw: the model that proposes the repair is the model that judges it, and visual plausibility under that judge is a poor proxy for whether the page actually works. What the loop is missing is a counterparty the VLM cannot fool, and the browser already is that counterparty: a deterministic, executable simulator of how an HTML artifact behaves under user actions, and in everything but name a world model for web code.
**Trending because:** 8 HuggingFace upvotes + browser-grounded self-improvement for web-code agents

---

### 9. CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents
**Authors:** Amir Saeidi, Zehua Zhang, Rishitosh Singh, Naman Ahuja, Vivek Gupta, Ali Payani, Gaowen Liu, Jayanth Srinivasa, Chitta Baral
**arXiv:** [arxiv.org/abs/2608.30147](https://arxiv.org/abs/2608.30147)
**Summary:** Large language model (LLM) agents are increasingly deployed in long-horizon, interactive, and stateful environments. In these settings, a single wrong action, such as refunding the wrong purchase, can cause irreversible task failure and must be intercepted before execution.
**Trending because:** 8 HuggingFace upvotes + reliability training for long-horizon tool use

---

### 10. Weaving Visual Narratives: Agentic Image Bundle Composition Beyond Atomic Visual Matching
**Authors:** Rong Shan, Tianyi Xu, Congmin Zheng, Wenteng Chen, Jiachen Zhu, Junjie Wu, Teng Wang, Weiwen Liu, Changwang Zhang, Weinan Zhang, Jun Wang, Jianghao Lin
**arXiv:** [arxiv.org/abs/2608.28695](https://arxiv.org/abs/2608.28695)
**Summary:** Image retrieval has traditionally been formulated as a point-wise matching problem, where each candidate image is scored in isolation. However, this atomic paradigm fails to capture the complexity of human search intent within personal photo collections, where users often seek compact visual stories bound by structural relations rather than isolated snapshots.
**Trending because:** 8 HuggingFace upvotes + agentic multimodal retrieval beyond single-image matching

---

### 11. InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic Reinforcement Learning in Peer Review and Rebuttal
**Authors:** Xuerui Su, Liya Guo, Qizhi Pei, Qipeng Guo, Zhongbo Tian, Lijun Wu, Kai Chen, Zun Wang
**arXiv:** [arxiv.org/abs/2608.28612](https://arxiv.org/abs/2608.28612)
**Summary:** Generating professional scholarly content, such as peer reviews and rebuttals, requires an intricate synergy between domain reasoning and factual grounding. This work presents a comprehensive framework for the development and evaluation of specialized scholarly agents, InternReviewer and InternAdvocate.
**Trending because:** 8 HuggingFace upvotes + objective rewards for scholarly review and rebuttal agents

---

### 12. PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation
**Authors:** Yunhao Liu, Hong Phuc Pham, Jaehong Yoon
**arXiv:** [arxiv.org/abs/2609.02272](https://arxiv.org/abs/2609.02272)
**Summary:** Faithfully translating research papers into repository-level implementations remains challenging because papers often describe methods at a high level, leave implementation assumptions implicit, and require generated repositories to preserve method logic, evaluation protocols, and cross-file consistency. Despite recent advances in paper-to-code agents, their intermediate outputs are often presented as free-form plans or summaries that downstream coding agents may ignore, reinterpret, or compress, leading to algorithmic simplification and inconsistent repository structure.
**Trending because:** 7 HuggingFace upvotes + faithful repository-scale paper-to-code generation

---

### 13. ExecRetrieval: Measuring the Functional-Correctness Gap in Code-Embedding Retrieval
**Authors:** Aaryan Kapoor, Md Abdullah Al Hafiz Khan
**arXiv:** [arxiv.org/abs/2609.01865](https://arxiv.org/abs/2609.01865)
**Summary:** Embedding-based code retrieval is a core component of coding agents and retrieval-augmented code generation, where retrieving correct code matters more than retrieving lexically similar code. Existing code-retrieval benchmarks do not plant controlled, execution-verified single-edit variants of each query's canonical implementation in the search pool, leaving the question of whether embeddings can functionally discriminate correct from near-clone-but-incorrect code unanswered in a retrieval setting.
**Trending because:** 7 HuggingFace upvotes + execution-grounded evaluation of code retrieval

---

### 14. Agent Memory Is a Surface for Endogenous Authorization Laundering
**Authors:** Tommaso Cerruti, Mika Okamoto, Ansel Kaplan Erol
**arXiv:** [arxiv.org/abs/2609.01836](https://arxiv.org/abs/2609.01836)
**Summary:** Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations. When memory misrepresents this evolving authorization state, the agent's own records can grant authority that the underlying history never permitted, resulting in misaligned behavior without any external attacks.
**Trending because:** 7 HuggingFace upvotes + a concrete authorization risk in persistent agent memory

---

### 15. Adapting Without Gradients: Affine Statistics Transport and What Its Certificate Can Tell You
**Authors:** Salim Khazem, Ibrahim Mohamed Serouis
**arXiv:** [arxiv.org/abs/2609.00374](https://arxiv.org/abs/2609.00374)
**Summary:** Test-time adaptation (TTA) typically assumes that model parameters can be updated at inference time. This assumption is restrictive for inference-only accelerators, frozen or third-party models, and memory-constrained deployments, and standard BatchNorm-based TTA configurations may also become inactive on architectures without BatchNorm.
**Trending because:** 7 HuggingFace upvotes + gradient-free adaptation for frozen-model deployment

---

### 16. SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Models
**Authors:** Zongrui Wang, Xiangyang Zhu, Sicheng Wang, Han Wang, Dingyi Rong, Zeyu Zhang, Chunyi Li, Yue Shi, Kaiwei Zhang, Zicheng Zhang, Yuan Tian, Qi Jia, Yan Teng, Wei Sun, Ning Liu, Guangtao Zhai
**arXiv:** [arxiv.org/abs/2608.29098](https://arxiv.org/abs/2608.29098)
**Summary:** Multimodal safety moderation requires distinguishing risks arising from visual content, user intent, and assistant behavior. Existing safeguards, however, are typically trained for a single judgment target and reduce safety assessment to a binary decision.
**Trending because:** 7 HuggingFace upvotes + fine-grained multimodal safety data and guard models

---

### 17. Rubric-to-Code Credit Assignment for Reinforcement Learning
**Authors:** Rui Jin, Jikai Chen, Yihan Chen, Hao Zhou, Demin Zhu, Kaichen Yang, Dong Wang, Chenyi Zhuang
**arXiv:** [arxiv.org/abs/2608.27906](https://arxiv.org/abs/2608.27906)
**Summary:** Interactive web application generation requires models to produce usable HTML, CSS, and JavaScript applications from natural language requests. Unlike conventional code generation, application quality depends on multiple user-facing functional requirements, each often tied to localized code regions such as event handlers, state updates, DOM fragments, or CSS selectors.
**Trending because:** 7 HuggingFace upvotes + localized credit assignment for generated applications

---

### 18. Recursive Criticality of AI Self-Improvement
**Authors:** Mikhail Burtsev
**arXiv:** [arxiv.org/abs/2609.00137](https://arxiv.org/abs/2609.00137)
**Summary:** AI is increasingly used in the R&D process that produces future AI systems. We study the conditions under which this feedback becomes self-amplifying.
**Trending because:** 6 HuggingFace upvotes + a quantitative model of recursive AI improvement

---

### 19. CoVA-SFT: A Large-Scale Dataset for Chain of Visual Abstractions
**Authors:** Tsung-Han Wu, Heekyung Lee, Anya Ji, Haoming Chen, Trevor Darrell, Joseph E. Gonzalez, David M. Chan
**arXiv:** [arxiv.org/abs/2608.28958](https://arxiv.org/abs/2608.28958)
**Summary:** Chain-of-thought (CoT) reasoning has dramatically improved large language models (LLMs) by allowing them to decompose problems into intermediate steps. While CoT is widely effective for linguistic tasks, text-only CoT forces models to serialize visual problems into awkward prose.
**Trending because:** 6 HuggingFace upvotes + large-scale training data for visual chain-of-thought

---

### 20. Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents
**Authors:** Nan Li
**arXiv:** [arxiv.org/abs/2608.28458](https://arxiv.org/abs/2608.28458)
**Summary:** Interactive dialogue games test a capability that static benchmarks largely leave implicit: a model must carry state across turns, interpret feedback, and choose valid actions under changing constraints. We study this setting in the LM Playschool Challenge with a 2B open-weight model, and find that many failures are not only broad knowledge failures but also local decision failures: repeated guesses, malformed actions, and violations of feedback that the model has just seen.
**Trending because:** 6 HuggingFace upvotes + diagnosis-guided post-training for small dialogue agents

---
