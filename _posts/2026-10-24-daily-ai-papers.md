---
title: "Daily AI Papers — October 24, 2026"
date: 2026-10-24
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-24/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - generative-ai
  - ai-agents
  - efficient-inference
---

### 1. MOSS-Image Technical Report
**Authors:** MOSI. AI
**arXiv:** [arxiv.org/abs/2610.23374](https://arxiv.org/abs/2610.23374)
**Summary:** MOSS-Image combines a 5B diffusion transformer with intent-aware prompt enhancement to generate images containing dense bilingual text and intricate layouts. Its new evaluations report 96.3% average text coverage on LongLongTextBench and strong layout-rich generation, with the backbone ranking first when generators share enhanced prompts.

---

### 2. StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions
**Authors:** Xialie Zhuang, Zunhai Su, Jia Pan, Ngai Wong, Guanhua Chen, Chuan-Wei Kuo
**arXiv:** [arxiv.org/abs/2610.17309](https://arxiv.org/abs/2610.17309)
**Summary:** StartLux-Decision offers 0.8B–27B decision models that either predict in one pass or invoke confidence-guided reasoning, with reinforcement learning rewarding calibrated decisions and discouraging overly long traces. The reported training reduces average reasoning length by up to 65% while largely preserving accuracy, and AutoThink improves contrast-pair accuracy over its Instant counterparts on DecisionPivot.

---

### 3. DecisionPivot: A Diagnostic Benchmark for Decision Models in LLM Systems
**Authors:** Xialie Zhuang, Mingcong Lei, Zunhai Su, Ri Liu, Jianjin Li, Peixian Ma, Jia Pan, Ngai Wong, Guanhua Chen, Chuan-Wei Kuo
**arXiv:** [arxiv.org/abs/2610.28522](https://arxiv.org/abs/2610.28522)
**Summary:** DecisionPivot evaluates decision models on 48 tasks and 40,033 items, including controlled contrast groups whose answers are independently verified by separate solvers. Tests of 40 decision models and 14 general models expose substantial differences in contrast-group accuracy, confidence reliability, and probability ordering that aggregate item scores conceal.

---

### 4. SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer
**Authors:** Junsong Chen, Yuyang Zhao, Jincheng Yu, Ruihang Chu, Junyu Chen, Shuai Yang, Xianbang Wang, Yicheng Pan, Daquan Zhou, Huan Ling, Haozhe Liu, Hongwei Yi, Hao Zhang, Muyang Li, Yukang Chen, Han Cai, Sanja Fidler, Ping Luo, Song Han, Enze Xie
**arXiv:** [arxiv.org/abs/2509.24695](https://arxiv.org/abs/2509.24695)
**Summary:** SANA-Video uses linear attention and a constant-memory blockwise autoregressive state to generate high-resolution, minute-length video without a growing conventional KV cache. The authors report competitive small-model quality, 16 times lower measured latency than comparison models, and a 29-second runtime for a five-second 720p video with NVFP4 on an RTX 5090.

---

### 5. Internal Safety Collapse in Frontier Large Language Models
**Authors:** Yutao Wu, Xiao Liu, Yifeng Gao, Xiang Zheng, Hanxun Huang, Yige Li, Cong Wang, Bo Li, Xingjun Ma, Yu-Gang Jiang
**arXiv:** [arxiv.org/abs/2603.23509](https://arxiv.org/abs/2603.23509)
**Summary:** This paper identifies Internal Safety Collapse, in which models generate harmful content while completing otherwise benign domain tasks, and introduces a Task–Validator–Data framework plus a 53-scenario benchmark. Three representative scenarios yield a reported average worst-case safety failure rate of 95.3% across four frontier models, highlighting vulnerabilities in task-driven use of sensitive capabilities.

---

### 6. FilmFlow: Agentic System for 3D Virtual Film Cinematography
**Authors:** Yiming Zhang, Jiarui Guo, Haojia Wei, Yifei Liu, Yifan Yang, Hongjie Zhang, Xue Yang, Zhihang Zhong
**arXiv:** [arxiv.org/abs/2610.30753](https://arxiv.org/abs/2610.30753)
**Summary:** FilmFlow translates natural-language instructions or reference videos into executable camera trajectories in dynamic 3D scenes through a Director supported by Interpreter, Scout, and Critic agents. On the new CinemaBench collection of 150 Blender scenes, 750 text-directed tasks, and 60 reference videos, it achieves the strongest reported benchmark performance and highest user preference among evaluated baselines.

---

### 7. Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems
**Authors:** Daniel Ruiz, Luca Luceri, Emilio Ferrara
**arXiv:** [arxiv.org/abs/2610.30418](https://arxiv.org/abs/2610.30418)
**Summary:** Agent Mosaic studies confidentiality leaks produced when LLM agents combine individually accessible documents into forbidden sensitive conclusions, using controlled simulations and live agent harnesses. Even benign queries produce such disclosures, and classification headers, aggregation rules, and refusals reduce but do not eliminate the observed leakage.

---

### 8. Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation
**Authors:** Hermann Kumbong, Ishan S. Khare, Iddah Mlauzi, Andrew Woen, Charles Ding, E. Kelly Buchanan, Simran Arora, Azalia Mirhoseini, Christopher Ré
**arXiv:** [arxiv.org/abs/2610.14162](https://arxiv.org/abs/2610.14162)
**Summary:** Next-Concept Modeling generates text coarse-to-fine by encoding it into hierarchical discrete codes and predicting all codes at each level in parallel. At matched parameter scales, it reports better generative perplexity than the strongest diffusion-language-model baseline on LM1B with 21 times faster generation, plus competitive results and large speedups on OpenWebText and XSum.

---

### 9. Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for Diffusion Language Models
**Authors:** Ofek Avivi, Eliron Rahimi, Avi Mendelson, Chaim Baskin
**arXiv:** [arxiv.org/abs/2610.31198](https://arxiv.org/abs/2610.31198)
**Summary:** This work finds that diffusion-language-model quantization sensitivity varies across both downstream tasks and denoising timesteps, and can be predicted without task labels. Its T2Quant framework allocates activation precision under a fixed bit-width budget, reporting accuracy improvements of up to 6.7 percentage points across three models and six benchmarks.

---

### 10. Verus-Insight: Towards Explainable Artifact Detection in AI-Generated Videos
**Authors:** Zhuoran Zhang, Yang Shi, Qixun Wang, Tengfei Liu, Yuqi Tang, Xuanyu Zhu, Yizhuo Jia, Jingyun Hua, Shixuan Liu, Xianghua Ying, Haotian Wang, Yuanxing Zhang, Pengfei Wan, Wenjing Yang
**arXiv:** [arxiv.org/abs/2610.30866](https://arxiv.org/abs/2610.30866)
**Summary:** Verus-Insight decomposes AI-generated-video artifact detection into inspection planning, evidence verification, and evidence aggregation, training these capabilities with human-anchored full-process supervision. The new Verus-Bench and additional evaluations report stronger fine-grained artifact recovery and video-level detection without increasing unsupported artifact claims.

---

### 11. RTAformer: Relation-Transition-Aware Transformer for Video Scene Graph Generation
**Authors:** Jaeyeon Heo, Geuntaek Lim, Yukyung Choi
**arXiv:** [arxiv.org/abs/2610.20091](https://arxiv.org/abs/2610.20091)
**Summary:** RTAformer separates persistent object identity from changing relationships to address relational semantic inertia in video scene graph generation. Calibrated adjacent-frame query differences and cross-frame instance alignment improve reported recall and mean recall on Action Genome, with larger matched-backbone gains on relation-transition frames.

---

### 12. AgentVQA: A Unified Benchmark for Agentic Visual Understanding
**Authors:** Advait Gupta, Sachin Konan, Tom Yin, Gabriel Sarch, Zhuang Liu
**arXiv:** [arxiv.org/abs/2610.31494](https://arxiv.org/abs/2610.31494)
**Summary:** AgentVQA assembles 1,000 challenging examples from 23 datasets into an offline benchmark spanning web agents, robotics, egocentric video, games, and spatial planning. Across 22 models, the best reaches only 58.5% accuracy, and analysis attributes most errors to visual grounding and state tracking rather than downstream logical reasoning.

---

### 13. AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark
**Authors:** Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang
**arXiv:** [arxiv.org/abs/2610.31466](https://arxiv.org/abs/2610.31466)
**Summary:** AnyGameRenderer turns simple game footage into richer visuals while preserving layout, camera motion, and entity timing, using LoRA adaptation of a reference-video-conditioned generation model. On a new entity-level benchmark, temporal matching improves from 50.9% to 62.9% and missed count changes fall from 34.7% to 21.3% relative to the base model.

---

### 14. MolLean: A Process-Verifiable Language for Chemical Reasoning
**Authors:** Jiatong Li, Yatao Bian
**arXiv:** [arxiv.org/abs/2610.20459](https://arxiv.org/abs/2610.20459)
**Summary:** MolLean grounds chemical reasoning in explicit molecular states whose transitions and assertions are checked by a layered Lean-based kernel, with a stateful MCP interface for interactive verification. Across 8,800 matched examples and 12 tasks, whole-trace refinement with Qwen3.6-27B outperforms direct chain-of-thought on every task, while stepwise tool feedback adds gains on reactions.

---

### 15. RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution
**Authors:** Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Xiao Luo, Yefeng Zheng, Bo Zhang, Haoxuan Li, Pheng-Ann Heng
**arXiv:** [arxiv.org/abs/2610.15772](https://arxiv.org/abs/2610.15772)
**Summary:** RSIPO co-evolves agent policies and reusable skills by extracting skills from completed trajectories, training skill generation through replay, and calibrating trust in teacher token scores with empirical Bayes shrinkage. Experiments on embodied and search-based tasks outperform compared baselines, including 98.6% average ALFWorld success with Qwen2.5-7B.

---

### 16. RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention
**Authors:** Jiening Siow, Amy Xin, Junjie Wang, Ziyu Tang, Zijun Yao, Yunjia Qi, Fanjin Zhang, Lei Hou, Jie Tang, Juanzi Li
**arXiv:** [arxiv.org/abs/2610.31372](https://arxiv.org/abs/2610.31372)
**Summary:** RIDAR introduces a 14-type taxonomy of research-integrity violations, post-hoc trajectory detection, and runtime corrective intervention for autonomous research agents. It reports 85.2% detection F1 on expert-annotated RIV-Gold, finds violations in 99.7% of RIV-Wild trajectories, and reduces violations remaining at task completion by 36.8% through runtime intervention.

---

### 17. Reading, Writing, Sharing, and Interacting with the World through Video
**Authors:** Shengqiong Wu, Meng Luo, Bobo Li, Ziwei Liu, Shuicheng Yan, Ming-Hsuan Yang, Philip Torr, Hao Fei
**arXiv:** [arxiv.org/abs/2610.31668](https://arxiv.org/abs/2610.31668)
**Summary:** This survey uses world modeling to organize video research around reading, writing, sharing, and interacting, connecting visual understanding, generation, and action-conditioned state prediction. It distinguishes temporal visual coherence from consistency of the underlying world and identifies challenges in persistent state, controllable evolution, physical validity, and interaction-grounded evaluation.

---

### 18. Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models
**Authors:** Zhizhuo Kou, Sizai Hou, Long Chen, Jian Yang, Junyu Luo, Jingshu Peng, Wenkai Zhang, Sirui Han, Yike Guo
**arXiv:** [arxiv.org/abs/2610.30882](https://arxiv.org/abs/2610.30882)
**Summary:** This paper traces the reasoning marker 'wait' through open-model training histories and finds that it usually originates in training data rather than being invented by reinforcement learning. Controlled analyses show that reinforcement learning can amplify or erase an existing marker, while marker frequency and automated revision judgments can misrepresent actual reasoning improvements.

---

### 19. BrickWright: Agentic Creation of Physically Feasible Brick Builds
**Authors:** Ava Pun, Kevin Dai, Sally Chen, Maxwell Jones, Ruixuan Liu, Kangle Deng, Changliu Liu, Maneesh Agrawala, Deva Ramanan, Jun-Yan Zhu
**arXiv:** [arxiv.org/abs/2610.31651](https://arxiv.org/abs/2610.31651)
**Summary:** BrickWright equips pretrained agents with the BrickLayer assembly API and a physical-feasibility validator to generate valid brick structures from text or image prompts. The authors report 100% physical validity on 512 sampled prompts versus 9–69% for baseline agents, while halving inference cost relative to raw LDraw and preserving or improving prompt adherence.

---

### 20. SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs
**Authors:** Arnon Mazza, Elad Levi
**arXiv:** [arxiv.org/abs/2610.31062](https://arxiv.org/abs/2610.31062)
**Summary:** SCOPE compiles natural-language policies into executable compositions of neural predicates, deterministic extractors, and code, jointly optimizing programs and training data through adversarial counterexamples. Evaluations report the highest average accuracy among compared methods, transfer to other executors without further optimization, and stable, interpretable decisions with inexpensive models.
