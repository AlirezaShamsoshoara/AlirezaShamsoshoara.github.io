---
title: "Daily AI Papers — June 23, 2026"
date: 2026-06-23
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-23/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - terminal-agents
  - llm-efficiency
  - agentic-systems
---

## 1. Tmax: A Simple Recipe for Terminal Agents

**Authors:** Hamish Ivison, Junjie Oscar Yin, Rulin Shao, Teng Xiao, Nathan Lambert, Hannaneh Hajishirzi (AI2 / University of Washington)

**Summary:** Tmax presents the strongest open RL recipe for terminal-using agents to date, achieving 27% on Terminal-Bench 2.0 with only 9B parameters — outperforming much larger proprietary models. The recipe combines publicly sourced data generation, verified execution environments, and a clean PPO training loop, bringing open recipes significantly closer to frontier performance.

**arXiv:** [arxiv.org/abs/2606.23321](https://arxiv.org/abs/2606.23321)

**Sources:** HuggingFace Daily Papers, Nathan Lambert Substack (dedicated article), YouTube (AI Automation Research channel)

**Why trending:** Nathan Lambert wrote a dedicated Substack post about this paper, citing it as a landmark open recipe for terminal agents. The AI2/UW authorship and reproducible recipe make it a go-to reference for the RL-for-agents community.

---

## 2. Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding

**Authors:** Xuanming Zhang, Sining Zhoubian, Yuxuan Chen, Tianyi Tang, An Yang, Sean Du, Chujie Zheng, Fei Huang, Dayiheng Liu, Gao Huang, Jingren Zhou (Alibaba / Qwen Team)

**Summary:** This paper reveals a "Guess-Refine-Perturb" dynamic in autoregressive LLMs: early layers form coarse guesses, intermediate layers refine reasoning-relevant semantics, and final layers can perturb these refined predictions toward generic or alignment-preferred tokens — causing an alignment tax. Confident Decoding selectively routes to intermediate layers when final-layer confidence is low, recovering reasoning capability without retraining.

**arXiv:** [arxiv.org/abs/2606.21906](https://arxiv.org/abs/2606.21906)

**Sources:** HuggingFace Daily Papers (5 comments — highest engagement today)

**Why trending:** Most-commented paper on HuggingFace today. The Qwen team's finding that deeper layers degrade certain reasoning tasks challenges a core assumption of LLM design and has immediate practical implications.

---

## 3. PlanBench-XL: Evaluating Long-Horizon Planning of LLM Tool-Use Agents in Large-Scale Tool Ecosystems

**Authors:** Jiayu Liu, Qihan Lin, Cheng Qian, Rui Wang, Emre Can Acikgoz, Heng Ji, Dilek Hakkani-Tür (UIUC / Northwestern)

**Summary:** PlanBench-XL is an interactive benchmark of 327 retail tasks over 1,665 tools that tests whether agents can iteratively retrieve usable tools, invoke them to uncover intermediate evidence, and adapt across long horizons under retrieval-limited visibility. It fills a critical gap: existing benchmarks rarely evaluate planning when agents cannot see the full tool catalog upfront.

**arXiv:** [arxiv.org/abs/2606.22388](https://arxiv.org/abs/2606.22388)

**Sources:** HuggingFace Daily Papers (3 comments)

**Why trending:** Agentic tool-use evaluation is a hot area, and the scale (1,665 tools) and realistic retrieval constraints make this a more credible benchmark than prior work. UIUC/Northwestern authorship adds credibility.

---

## 4. EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory

**Authors:** Chang Nie, Chaoyou Fu, Junlan Feng, Caifeng Shan

**Summary:** EvoEmbedding breaks from static embedding models by maintaining a continuously updated latent memory as it sequentially processes inputs, generating embeddings that evolve with context. This makes it particularly suited for long-context scenarios where information is dynamic and sequential, enabling retrieval systems that track state rather than encode snapshots.

**arXiv:** [arxiv.org/abs/2606.21649](https://arxiv.org/abs/2606.21649)

**Sources:** HuggingFace Daily Papers (3 comments)

**Why trending:** The framing of "evolvable" embeddings taps into both the long-context retrieval and agent memory communities simultaneously, generating cross-community interest.

---

## 5. Causal Discovery in the Era of Agents

**Authors:** Yujia Zheng, Vishal Verma, Mantej Gill, Haoyue Dai, Peter Spirtes, Kun Zhang (CMU / Peking University)

**Summary:** Rather than using LLMs to directly infer causal structure, this paper argues agents should act as experiment designers and data inspectors — proposing interventions, running tests, and constraining search — while statistical algorithms handle graph estimation. The paper formalizes this role separation and demonstrates that agent-assisted causal discovery substantially outperforms purely LLM-inferred graphs.

**arXiv:** [arxiv.org/abs/2606.23608](https://arxiv.org/abs/2606.23608)

**Sources:** HuggingFace Daily Papers, arXiv cs.AI

**Why trending:** Peter Spirtes and Kun Zhang are leading figures in causal inference; their take on LLM-agent integration with principled causal discovery provides a rigorous corrective to hype-driven approaches.

---

## 6. Tapered Language Models

**Authors:** Reza Bayat, Ali Behrouz, Aaron Courville (Mila / Université de Montréal)

**Summary:** Modern LLMs uniformly allocate parameters across depth — a default inherited from the original transformer. This paper shows that later layers contribute disproportionately less to predictions, and proposes Tapered LMs where parameter capacity decreases with depth (wider early layers, narrower late layers). This achieves equivalent or better perplexity with fewer total parameters.

**arXiv:** [arxiv.org/abs/2606.23670](https://arxiv.org/abs/2606.23670)

**Sources:** HuggingFace Daily Papers, arXiv cs.LG

**Why trending:** Aaron Courville (Mila) co-authorship attracts attention; the idea of questioning the uniform-depth assumption opens a new efficiency axis distinct from sparsity or quantization.

---

## 7. CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents

**Authors:** Zhanbo Hua, Yifan Yao, Weihao Xie, Yongchi Zhao, et al.

**Summary:** CLI-Universe is a principled synthesis engine for terminal-agent training data that generates unambiguous instructions, deep execution paths, and verifiable test cases — addressing the shallow artifact problem in existing pipelines. The engine produces tasks grounded in real CLI semantics with automatically checkable correctness criteria.

**arXiv:** [arxiv.org/abs/2606.22883](https://arxiv.org/abs/2606.22883)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.AI

**Why trending:** Terminal agents are a top application area; data quality for RL training is the bottleneck everyone is hitting, making a principled synthesis engine immediately practical.

---

## 8. BioMatrix: Towards a Comprehensive Biological Foundation Model Spanning the Modality Matrix of Sequences, Structures, and Language

**Authors:** Qizhi Pei, Zhimeng Zhou, Yi Duan, Yiyang Zhao, Wei Li, Han Guo, Liang He, Chang-Yu Hsieh, Rui Yan, Lijun Wu (Microsoft Research / Peking University)

**Summary:** BioMatrix is the first decoder-only foundation model that natively integrates DNA/protein sequences, 3D structures, and natural language within a single architecture. Unlike prior models that fuse modalities for one entity type or span multiple types without structural grounding, BioMatrix handles the full modality-entity matrix — enabling joint generation and reasoning across all biological representations.

**arXiv:** [arxiv.org/abs/2606.22138](https://arxiv.org/abs/2606.22138)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.LG/q-bio

**Why trending:** Biological AI is accelerating rapidly post-AlphaFold3; a model unifying sequences, structures, and language at this scale is a milestone the bio-ML community has been waiting for.

---

## 9. World Action Models: A Survey

**Authors:** Qiuhong Shen, Shihua Zhang, Yue Liao, Qi Li, Zhenxiong Tan, Shizun Wang, Shuicheng Yan, Xinchao Wang (NUS / Sea AI Lab)

**Summary:** This survey establishes a taxonomy for World Action Models (WAMs) — embodied predictive-action models that forecast future states to ground decisions — distinguishing them from broader world models, video generators, and VLA policies. It covers both video-generation-based and language-backbone-based WAMs, providing a unified framework for a field that has grown rapidly without shared terminology.

**arXiv:** [arxiv.org/abs/2606.20781](https://arxiv.org/abs/2606.20781)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.RO/cs.CV

**Why trending:** With physical AI (Cosmos, Kairos, DreamX) dominating recent weeks, a rigorous taxonomy from the NUS/Sea AI Lab group arrives at exactly the right moment to structure the field.

---

## 10. Grouped Query Experts (GQE): Mixture-of-Experts on GQA Self-Attention

**Authors:** Vishesh Tripathi, Abhay Kumar

**Summary:** GQE places a mixture-of-experts layer on top of grouped-query attention (GQA), routing each token to a subset of specialized attention heads based on token difficulty or content, rather than applying the full head set uniformly. This reduces attention compute at long context lengths while maintaining or improving quality, offering a new axis of sparsity for transformer efficiency.

**arXiv:** [arxiv.org/abs/2606.20945](https://arxiv.org/abs/2606.20945)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.LG

**Why trending:** Combining MoE sparsity with GQA in the attention layer (rather than just FFN) is a novel angle on efficient transformers that practitioners are keen to evaluate.

---

## 11. SkillHarness: Harnessing Safe Skills for Computer-Use Agents

**Authors:** Yurun Chen, Biao Yi, Keting Yin, Shengyu Zhang (Zhejiang University)

**Summary:** SkillHarness addresses a gap in computer-use agent skill learning: existing methods assume static, safe environments and ignore adversarial risks like prompt injections or unexpected pop-ups. The system learns and applies reusable skills while maintaining safety under dynamic and adversarial conditions, with explicit adversarial skill validation before deployment.

**arXiv:** [arxiv.org/abs/2606.20636](https://arxiv.org/abs/2606.20636)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.AI

**Why trending:** As computer-use agents deploy on real desktops, adversarial robustness for skill reuse is an unsolved problem; this paper addresses it directly.

---

## 12. Self-Compacting Language Model Agents

**Authors:** Tianjian Li, Jingyu Zhang, William Jurayj, Xi Wang, Chuanyang Jin, Mehrdad Farajtabar, Eric Nalisnick, Daniel Khashabi (JHU / DeepMind)

**Summary:** SelfCompact lets the language model itself decide when and how to compress its growing trace — rather than using fixed token-threshold triggers. The model emits a compact signal at semantically meaningful boundaries, avoiding truncation mid-derivation, and produces structured summaries that preserve task-critical context while reclaiming context window space.

**arXiv:** [arxiv.org/abs/2606.23525](https://arxiv.org/abs/2606.23525)

**Sources:** HuggingFace Daily Papers, arXiv cs.CL

**Why trending:** Context window management for long-running agents is a practical pain point; a model-driven (vs. rule-driven) compaction strategy from JHU/DeepMind authors is compelling.

---

## 13. Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization via Reinforcement Learning

**Authors:** Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, Jingren Zhou (Alibaba DAMO Academy)

**Summary:** This paper introduces "Connect the Dots" (CoD), a meta-capability for long-lifecycle agents: the ability to solve sequential tasks over time while continuously learning from experience and self-updating environment context to improve on future tasks. An RL framework trains LLMs to CoD across domains, achieving progressive performance gains on later tasks in a deployment sequence.

**arXiv:** [arxiv.org/abs/2606.20002](https://arxiv.org/abs/2606.20002)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.AI

**Why trending:** Long-lifecycle (continual) agents that improve through deployment experience address a gap between episodic RL evaluation and real-world usage; Alibaba DAMO authorship signals production relevance.

---

## 14. Learning from Your Own Mistakes: Constructing Learnable Micro-Reflective Trajectories for Self-Distillation

**Authors:** Zhilin Huang, Hang Gao, Ziqiang Dong, Yuan Chen, Yifeng Luo, et al.

**Summary:** Standard self-distillation for reasoning uses uncontrolled sampling to generate training signal, producing no diagnostic insight about specific error patterns. This paper constructs "micro-reflective trajectories" — structured rollouts that explicitly identify the model's mistakes and include corrective reasoning — enabling targeted self-improvement rather than blind imitation of a privileged distribution.

**arXiv:** [arxiv.org/abs/2606.18844](https://arxiv.org/abs/2606.18844)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.LG

**Why trending:** Self-distillation for reasoning is a crowded area; the micro-reflective framing — making error patterns explicit rather than implicit — is a clean and extensible idea.

---

## 15. OpenRath: Session-Centered Runtime State for Agent Systems

**Authors:** Fukang Wen, Zhijie Wang, Ruilin Xu

**Summary:** OpenRath introduces a PyTorch-like programming model for multi-agent systems where the core abstraction is `Session` — a unified runtime object that centralizes transcripts, tool effects, memory events, workspace placement, branch provenance, and replay evidence. This makes complex agent state inspectable and reproducible, addressing the fragmentation problem in current agent frameworks.

**arXiv:** [arxiv.org/abs/2606.19409](https://arxiv.org/abs/2606.19409)

**Sources:** HuggingFace Daily Papers (2 comments)

**Why trending:** Agent debugging and reproducibility are pain points for every practitioner building agentic systems; the PyTorch-style abstraction metaphor is immediately intuitive.

---

## 16. KaLM-Reranker-V1: Fast but Not Late Interaction for Compressed Document Reranking

**Authors:** Xinping Zhao, Jiaxin Xu, Ziqi Dai, Xin Zhang (Baidu)

**Summary:** KaLM-Reranker-V1 decouples query and passage encoding in a reranking architecture, enabling independent computation and caching — unlike traditional cross-encoders that require joint encoding. It achieves near-late-interaction quality with substantially lower latency, making high-quality reranking practical at retrieval scale.

**arXiv:** [arxiv.org/abs/2606.22807](https://arxiv.org/abs/2606.22807)

**Sources:** HuggingFace Daily Papers (2 comments), arXiv cs.IR

**Why trending:** RAG pipelines are everywhere; a reranker that matches late-interaction quality without the latency cost is a drop-in upgrade that the practitioner community will immediately try.

---

## 17. Training Open Models for Agentic Phone Use (PhoneBuddy)

**Authors:** Zhengyang Tang, Xin Lai, Pengyuan Lyu, Xinyuan Wang, Tianyi Bai, Chenxin Li, Yiduo Guo, et al.

**Summary:** PhoneBuddy presents an open training recipe for phone-use agents that combines real-device environments (slow, stateful, hard to reset) with scalable mock environments for data generation, bridging the sim-to-real gap. The released model line achieves reliable performance on real Android apps across a diverse task suite.

**arXiv:** [arxiv.org/abs/2606.23049](https://arxiv.org/abs/2606.23049)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.AI

**Why trending:** Phone/mobile is the most ubiquitous agentic surface; open training recipes for this domain are scarce, making PhoneBuddy practically significant for the agent training community.

---

## 18. Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs

**Authors:** Charbel El Feghali, Arkil Patel, Nicholas Meade, Spandana Gella, Verna Dankers, Siva Reddy (McGill / Mila)

**Summary:** This paper proposes Tiered Layers — a release strategy that separates LLM capabilities into public layers (released openly) and private layers (accessible only via authenticated API). The architecture enables open scientific use of base capabilities while mediating access to sensitive capabilities through controlled inference endpoints, without suppressing capabilities for all users.

**arXiv:** [arxiv.org/abs/2606.21638](https://arxiv.org/abs/2606.21638)

**Sources:** HuggingFace Daily Papers, arXiv cs.CL

**Why trending:** Open-weight model safety is a top policy conversation in 2026; a technical architecture that allows graduated capability release rather than binary open/closed is novel and timely.

---

## 19. Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive Benchmark (PhySciBench)

**Authors:** Yigeng Jiang, Tengchao Yang, Taoyong Cui, Jiaxing Wan, Yuan Wang, et al.

**Summary:** PhySciBench introduces 200 expert-curated questions balanced between physics and chemistry, designed to evaluate LLM-based deep research agents on multi-step scientific reasoning tasks — not just single-hop Q&A. The accompanying multi-agent framework shows that specialized sub-agents (literature retrieval, hypothesis formation, calculation verification) outperform monolithic approaches on scientific research tasks.

**arXiv:** [arxiv.org/abs/2606.18648](https://arxiv.org/abs/2606.18648)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.AI

**Why trending:** AI for science is a priority research area; a rigorous benchmark that distinguishes genuine multi-step scientific reasoning from pattern-matched recall fills an important gap.

---

## 20. DailyReport: An Open-ended Benchmark for Evaluating Search Agents on Daily Search Tasks

**Authors:** Jingxuan Han, Wei Liu, Mingyang Zhu, Youpeng Wang, Ziwen Wang, Lin Qiu, Xuezhi Cao, Xunliang Cai (Microsoft Research)

**Summary:** DailyReport constructs evaluation tasks from real daily information-seeking queries, moving beyond specialized/synthetic benchmarks to assess search agents on the tasks users actually perform. It uses fine-grained rubrics covering source diversity, factual accuracy, and response completeness — providing richer interpretability than coarse task-level scoring.

**arXiv:** [arxiv.org/abs/2606.12871](https://arxiv.org/abs/2606.12871)

**Sources:** HuggingFace Daily Papers (1 comment), arXiv cs.IR

**Why trending:** Search agents are the most-deployed agentic application; a benchmark grounded in real daily tasks from Microsoft Research provides a practical evaluation standard the field has been missing.
