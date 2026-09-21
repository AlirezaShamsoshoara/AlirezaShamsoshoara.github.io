---
title: "Daily AI Papers — September 21, 2026"
date: 2026-09-21
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-21/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - multimodal-ai
  - efficient-language-models
---

### 1. IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts
**Authors:** Ran Cheng, Longfei Xu, Zheng Liu, Kaikui Liu, Xiangxiang Chu
**arXiv:** [arxiv.org/abs/2609.21346](https://arxiv.org/abs/2609.21346)
**Summary:** IntBMoE decouples expert participation, execution cost, and materialization cost by combining dense expert composition with sparse block execution from a learned codebook. It improves several vision, language-modeling, and recommendation baselines and reports a 2.4% relative UVCTR gain in a large-scale production recommendation deployment.
**Trending because:** 89 HuggingFace upvotes + a production-tested approach to making mixture-of-experts participation dense without dense execution cost

---

### 2. Grounded Skill Synthesis from Code at Scale for Agentic Intelligence
**Authors:** Yongqi Tong, Pan Wang, Hang Wang, Jianshe Li, Xin Zhang, Jiang-Ming Yang, Wei Wu
**arXiv:** [arxiv.org/abs/2609.05571](https://arxiv.org/abs/2609.05571)
**Summary:** Code2Skill automatically turns source-code units into verified records of atomic operations, composite workflows, and reusable patterns, producing more than one million accepted skills from 19,769 repositories. Retrieved skills improve matched agent baselines by 11.7% on average across 72 evaluations and outperform trajectory-derived skill banks on all seven shared benchmarks.
**Trending because:** 84 HuggingFace upvotes + it offers a million-scale, execution-grounded skill bank for coding and general agents

---

### 3. CodeMidas: Scaling Agentic Coding RL Environments from Code Itself
**Authors:** Bowen Ye, Lei Li, Shicheng Li, Zihao Yue, Linghao Zhang, Hanglong Lv, Yuanxin Liu, Wenhan Ma, Hao Tian, Rang Li, Jinhao Dong, Yikai Zhao, Xiangwei Deng, Hailin Zhang, Liang Zhao, Qi Liu, Lingpeng Kong, Tong Yang, Fuli Luo
**arXiv:** [arxiv.org/abs/2609.22068](https://arxiv.org/abs/2609.22068)
**Summary:** CodeMidas uses agents to convert implemented functionality in open-source codebases into executable reinforcement-learning tasks, with specifications, tests, and repeated rollout validation grounded in the original code. Its 5,545 tasks across 23 languages improve MiMo-V2.5 on issue repair, whole-program construction, and terminal-work benchmarks.
**Trending because:** 77 HuggingFace upvotes + it scales verified coding-agent RL environments without relying on issues or commits

---

### 4. EvoOntology: A Self-Evolving Ontology Layer for Data Agents
**Authors:** Meiduo Chong, Shaolei Zhang, Ju Fan, Xiaoyong Du
**arXiv:** [arxiv.org/abs/2609.15779](https://arxiv.org/abs/2609.15779)
**Summary:** EvoOntology exposes schema, content, and tool layers through an MCP server that data agents can query while operating over heterogeneous sources. A builder agent and attribution-guided evaluation loop continuously refine the ontology, yielding consistent gains across three data-agent benchmarks and four language-model backbones.
**Trending because:** 66 HuggingFace upvotes + its self-evolving MCP ontology directly addresses the agent-to-data semantic gap

---

### 5. RecreationWorld: Scalable and Verifiable Environments for Hybrid Computer-Use Agents
**Authors:** Shuai Bai, Jiayong Deng, Yikun Fu, Chang Gao, Xuhao Hu, Mianqiu Huang, Yizhen Jiang, Yuheng Jing, Dehui Kong, Keliang Li, Ning Li, Wanli Li, Dayiheng Liu, Dunjie Lu, Changwei Luo, Que Shen, Zheyuan Wang, Zijian Wang, Jie Wu, Gao Wu, Zhihui Xie, Rui Xie, Haiyang Xu, An Yang, Jiakang Yuan, Yanming Zhang, Jiajun Zhang, Xi Zhang, Zhenru Zhang, Zhuo Zhen, Mingkang Zhu, Bowen Zhou
**arXiv:** [arxiv.org/abs/2609.22000](https://arxiv.org/abs/2609.22000)
**Summary:** RecreationWorld trains and evaluates hybrid computer-use agents that interleave graphical interaction, coding, command-line work, and visual verification across Ubuntu, macOS, Windows, Android, and the web. Its 250-task RecreationBench exposes large remaining gaps in reproducing interactions and computed outputs even for the strongest tested agents.
**Trending because:** 60 HuggingFace upvotes + it provides a broad, execution-grounded benchmark for agents that must both use and build software

---

### 6. OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue
**Authors:** Haolin He, Yunfei Chu, Qi Chen, Wen Huang, Yuan Feng, Muzhi Zhu, Zheqi Dai, Haoning Xu, Dongchao Yang, Chunyat Wu, Zining Liang, Zhengxi Liu, Xiquan Li, Xie Chen, Xize Cheng, Qize Yang, Jin Xu, Qiuqiang Kong
**arXiv:** [arxiv.org/abs/2609.21465](https://arxiv.org/abs/2609.21465)
**Summary:** OmniVChat defines native dialogue in which a model jointly receives video and audio containing the user's query, without separate transcription or captioning. Its synthesis engine, benchmark, and reinforcement-learning reward improve Qwen3-Omni-Instruct on both synthetic and human-recorded audio-visual conversations.
**Trending because:** 29 HuggingFace upvotes + it unifies data generation, evaluation, and training for direct audio-visual dialogue

---

### 7. OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation
**Authors:** Wenxue Li, Peiyan Guan, Haoyang Jiang, Junxian Cai, Hualuo Liu, Chunjie Zhang, Chong Guan, Songlian Li, Taiyi Wu, Yongjian Yu, Xiaotong Zhao, Alan Zhao, Eric Liu, Xi Chen, Yu Liu, Lei Zhu
**arXiv:** [arxiv.org/abs/2609.22069](https://arxiv.org/abs/2609.22069)
**Summary:** OmniVBench evaluates reference-to-video systems across seven task families and 18 fine-grained tasks using 12,172 case-specific checks for preservation, disentanglement, binding, and instruction following. The accompanying 340,000-sample Omni-R2V Dataset supplies industrial-scale training data for diverse single- and multi-reference controls.
**Trending because:** 19 HuggingFace upvotes + it pairs unusually granular video-generation evaluation with a large public training resource

---

### 8. Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design
**Authors:** Hongyang Du, Lan Yan, Christian Flores, Asim Kadav
**arXiv:** [arxiv.org/abs/2609.22086](https://arxiv.org/abs/2609.22086)
**Summary:** Designer-RSI keeps a frontier model frozen while expanding and refining an external natural-language skill memory from successful and failed graphic-design trajectories. Across five rounds of real user briefs, the skill bank grows from 76 to 139 procedures and raises execution success from 72.7% to 99.3% without weight updates or human labels.
**Trending because:** 11 HuggingFace upvotes + it demonstrates continual agent improvement from traffic through gated procedural memory rather than retraining

---

### 9. MintAct: A Unified Visual Agent for Digital Environments
**Authors:** Mingfei Gao, Rui Tian, Haiming Gang, Bohan Zhai, Le Zhang, Yuanzheng Gong, Di Feng, Ege Özsoy, Kaixin Ma, Vishwesh Kirthivasan, Oğuzhan Fatih Kar, Roman Bachmann, Anders Boesen Lindbo Larsen, Afshin Dehghan
**arXiv:** [arxiv.org/abs/2609.22083](https://arxiv.org/abs/2609.22083)
**Summary:** MintAct is a 2B-to-8B vision-language model family trained to unify UI grounding, multi-step navigation, and visual tool use across mobile, desktop, and web environments. Its scalable asynchronous reinforcement-learning setup reaches state-of-the-art OSWorld-Verified performance at comparable model sizes while matching domain specialists across capabilities.
**Trending because:** 10 HuggingFace upvotes + it consolidates several visual-agent domains into one compact model family

---

### 10. GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills
**Authors:** Rui Sun, Zhi Zheng, Zhenkun Wang, Zhichao Lu
**arXiv:** [arxiv.org/abs/2609.21749](https://arxiv.org/abs/2609.21749)
**Summary:** GraphSkillEvo represents an agent skill as a directed workflow whose nodes contain operational guidance and whose edges encode context-dependent transitions. Population-based mutation and crossover search this structured space more effectively than unstructured self-refinement, improving average accuracy over SkillOpt on five benchmarks.
**Trending because:** 9 HuggingFace upvotes + graph structure makes agent skills more executable and their optimization more tractable

---

### 11. BI-Agent and BI-Bench: Towards Automating End-to-End Business Intelligence
**Authors:** Chuxuan Hu, Yeye He, Penny Zhou, Wee Hyong Tok, Daniel Kang, Surajit Chaudhuri
**arXiv:** [arxiv.org/abs/2609.20886](https://arxiv.org/abs/2609.20886)
**Summary:** BI-Bench measures whether language models can answer business-intelligence questions end to end over real projects, including table discovery, transformation, joins, and final analysis. Frontier models score below 50%, while the tool-augmented and post-trained BI-Agent delivers gains of up to 40 and 30 percentage points respectively.
**Trending because:** 6 HuggingFace upvotes + it establishes a realistic benchmark and specialized agent for end-to-end enterprise analytics

---

### 12. Calibrating Teacher--Student Discrepancy for On-Policy Distillation
**Authors:** Qiangqiang He, Jin Li, MingCai Chen
**arXiv:** [arxiv.org/abs/2609.21619](https://arxiv.org/abs/2609.21619)
**Summary:** Calibrated On-Policy Distillation estimates the teacher's own deviation using positive and negative privileged interventions, then retains only the discrepancy that lies beyond that region. On mathematical-reasoning benchmarks it outperforms standard on-policy distillation while using only about 52–65% of the original discrepancy as its training signal.
**Trending because:** 6 HuggingFace upvotes + it isolates useful teacher-student signal instead of copying teacher-side distortions

---

### 13. When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation
**Authors:** Sy-Tuyen Ho, Minghui Liu, Furong Huang
**arXiv:** [arxiv.org/abs/2609.20942](https://arxiv.org/abs/2609.20942)
**Summary:** Training reviewer models on mixtures containing synthetic reviews compresses rating distributions and reduces both per-paper and corpus-level semantic diversity, a failure mode the authors call scientific-judgment collapse. TrustReviewer combines curated single-stage training with paired activation steering to preserve judgment diversity and improve recommendation alignment.
**Trending because:** 5 HuggingFace upvotes + it identifies and mitigates a recursive-data risk in AI-assisted peer review

---

### 14. MoME: Mixture-of-Memory Embeddings for Context-Aware Sparse Lookup
**Authors:** Muchen Li, Leonid Sigal, Renjie Liao
**arXiv:** [arxiv.org/abs/2609.15126](https://arxiv.org/abs/2609.15126)
**Summary:** MoME replaces each token's single deterministic memory row with multiple slots selected by a hidden-state-conditioned gate, allowing different contextual senses to retrieve different embeddings. It improves over several conditional-memory baselines across multiple language-model backbones while retaining efficient training and inference.
**Trending because:** 4 HuggingFace upvotes + it gives sparse parametric memory a context-sensitive and partly interpretable retrieval mechanism

---

### 15. GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning
**Authors:** Ruiyang Wang, Hao-Lun Hsu, Swarajh Mehta, Jiwoo Kim, Zhihao Dou, Miroslav Pajic
**arXiv:** [arxiv.org/abs/2609.19315](https://arxiv.org/abs/2609.19315)
**Summary:** GAVEL uses an explicit graph of object relations, action preconditions and effects, and beliefs over hidden locations to predict, verify, and repair language-model plans before execution. On BEHAVIOR-1K it raises Qwen3-8B success from 41.2% to 91.8% for single tasks and from 19.9% to 92.6% for multi-task instructions.
**Trending because:** 3 HuggingFace upvotes + its explicit world model produces large reliability gains for long-horizon embodied planning

---

### 16. MLLMs Hallucinate when Information Distribution Drifts in Synergy Heads
**Authors:** Meng'en Qin, Junye Chen, Jucheng Liu, Youlu Xing, Song Wang, Ruize Han
**arXiv:** [arxiv.org/abs/2609.09206](https://arxiv.org/abs/2609.09206)
**Summary:** HEAL uses causal interventions and counterfactual analysis to classify multimodal attention heads and links hallucinations to information-distribution drift in cross-modal synergy heads. Dynamically calibrating those heads' value vectors reduces hallucinations across multiple multimodal language models while providing an interpretable mechanism.
**Trending because:** 3 HuggingFace upvotes + it offers a causal account and targeted intervention for multimodal hallucinations

---

### 17. Learning Foresight without Explicit Trajectories for 3D Diffusion Policies
**Authors:** Zhongbo Zhang, Zaibin Zhang, Yifan Wang, Changbo Yan, Lijun Wang, Huchuan Lu
**arXiv:** [arxiv.org/abs/2609.20669](https://arxiv.org/abs/2609.20669)
**Summary:** Movement Trend Guidance learns a compact future-oriented latent from recent observations, supervised by sparse future gripper states during training but requiring no explicit trajectory at inference. Adding only 3.52% more parameters to DP3 yields large gains across RoboTwin2.0, LIBERO-40, DexArt, and real-robot tasks.
**Trending because:** 3 HuggingFace upvotes + it adds effective foresight to 3D diffusion policies with little parameter overhead

---

### 18. DeformSmith: Physics Harness-Guided Hierarchical Generation of Deformable Assets for Robot Manipulation
**Authors:** Can Li, Jie Gu, Zishun Deng, Jingmin Chen, Lei Sun
**arXiv:** [arxiv.org/abs/2609.18620](https://arxiv.org/abs/2609.18620)
**Summary:** DeformSmith hierarchically constructs geometry, appearance, physical models, material behavior, and robot interactions for deformable assets generated from text or a single image. A shared physics-grounded harness repeatedly tests and refines the assets, improving visual quality and physical plausibility over several baselines while producing manipulation data.
**Trending because:** 3 HuggingFace upvotes + it closes the loop between generative assets, physical simulation, and robot manipulation

---

### 19. TeleAntiFraud 2.0: A Refreshable, Profile-Grounded, and Audio-Based Benchmark for Telecom Fraud Detection
**Authors:** Huiyuan Liu, Zhiming Ma, Yanxing Liu, Shun Zhang, Qifan Wang, Di Liu, Yifan Wang, Yuyang Deng, Haoyang Meng, Yijin Zhou, Yuxi Zhao, Chengxian Hu, Peidong Wang, Peng Chen
**arXiv:** [arxiv.org/abs/2609.18748](https://arxiv.org/abs/2609.18748)
**Summary:** TeleAntiFraud 2.0 builds monthly frozen Chinese audio evaluation sets with profile-grounded fraud and lawful near-domain calls generated under shared contexts. Experiments show that classifiers appearing perfect against unrelated negatives fall to 0.65–0.68 Macro-F1 against realistic sibling negatives and expose class-prior and snapshot failures.
**Trending because:** 3 HuggingFace upvotes + its refreshable near-domain design reveals shortcuts hidden by easier fraud benchmarks

---

### 20. FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud Detection
**Authors:** Chengxian Hu, Zhiming Ma, Mingjun Pan, Yifan Wang, Shun Zhang, Qifan Wang, Zhilei Zhao, Yijin Zhou, Yuxi Zhao, Huiyuan Liu, Peidong Wang, Peng Chen
**arXiv:** [arxiv.org/abs/2609.18766](https://arxiv.org/abs/2609.18766)
**Summary:** FRAUDSkill leaves an audio-language model frozen while optimizing external skill programs, route-specific policies, and rules for service identification, fraud detection, and fraud-type classification. On TeleAntiFraud it reaches 73.50% Macro-F1, improving the frozen-model baseline by 31.96% and cutting invalid outputs to 1.94%.
**Trending because:** 3 HuggingFace upvotes + it adapts structured audio-fraud decisions without modifying model weights
