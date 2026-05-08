---
title: "Daily AI Papers — May 08, 2026"
date: 2026-05-08
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-08/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - agentic-systems
  - diffusion-models
---

## 1. Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning
**Authors:** Yaorui Shi, Yuxin Chen, Zhengxi Lu, Yuchun Miao, Shugui Liu, Qi GU, Xunliang Cai, Xiang Wang, An Zhang
**arXiv:** [arxiv.org/abs/2605.06130](https://arxiv.org/abs/2605.06130)
**Sources:** HuggingFace Daily Papers (#1, 51 upvotes)

**Summary:** Skill1 proposes a single RL policy that jointly learns to select, use, and distill skills into a persistent library — all from one task-outcome signal. Training on ALFWorld and WebShop, it outperforms both skill-based and RL baselines by co-evolving all three capabilities together rather than optimizing them in isolation.

**Why trending:** Tops the HF daily board. Hits a real gap in agent systems: existing skill-library approaches train selection, execution, and distillation separately, creating conflicting gradients. The single-signal formulation is elegant and the ALFWorld/WebShop results are strong.

---

## 2. Continuous Latent Diffusion Language Model (Cola DLM)
**Authors:** Hongcan Guo, Qinyu Zhao, Yian Zhao, Shen Nie, Rui Zhu, Qiushan Guo, Feng Wang, Tao Yang, Hengshuang Zhao, Guoqiang Wei, Yan Zeng
**arXiv:** [arxiv.org/abs/2605.06548](https://arxiv.org/abs/2605.06548)
**Sources:** HuggingFace Daily Papers (#2, 37 upvotes, 4 comments)

**Summary:** Cola DLM is a hierarchical latent diffusion model that separates global semantic organization from local text realization — using a Text VAE for stable encoding, a block-causal DiT for continuous latent prior modeling, and conditional decoding for output. Scaling experiments up to ~2000 EFLOPs vs. matched 2B-parameter AR and LLaDA baselines show strong scaling behavior as a principled alternative to autoregressive token-level generation.

**Why trending:** Non-autoregressive LM generation is a hot research area; Cola DLM's unified Markov-path framing and compelling scaling curves put it in direct conversation with LLaDA and other diffusion LM efforts. Four comments on HF the day of submission signals active discussion.

---

## 3. MiA-Signature: Approximating Global Activation for Long-Context Understanding
**Authors:** Yuqing Li, Jiangnan Li, Mo Yu, Zheng Lin, Weiping Wang, Jie Zhou
**arXiv:** [arxiv.org/abs/2605.06416](https://arxiv.org/abs/2605.06416)
**Sources:** HuggingFace Daily Papers (#3, 37 upvotes)

**Summary:** Inspired by cognitive science's "global ignition" model, MiA-Signature produces a compact compressed representation of the global activation pattern a query induces over a long context, using submodular concept selection optionally refined with working memory. Plugging MiA-Signatures into RAG and agentic systems yields consistent gains across multiple long-context understanding benchmarks.

**Why trending:** Long-context efficiency is a perennial hot topic; the cognitive-science motivation and the practical RAG/agent integration story make it accessible to a broad ML audience.

---

## 4. RaguTeam at SemEval-2026 Task 8: Meno and Friends — Judge-Orchestrated LLM Ensemble for Faithful Multi-Turn Response Generation
**Authors:** Ivan Bondarenko, Roman Derunets, Oleg Sedukhin, Mikhail Komarov, Ivan Chernov, Mikhail Kulakov
**arXiv:** [arxiv.org/abs/2605.04523](https://arxiv.org/abs/2605.04523)
**Sources:** HuggingFace Daily Papers (#4, 33 upvotes, 4 comments)

**Summary:** The winning system (1st/26 teams) for SemEval-2026 MTRAGEval Task B uses a heterogeneous 7-LLM ensemble with two prompting variants, arbitrated by a GPT-4o-mini judge, achieving a conditioned harmonic mean of 0.7827 vs. 0.6390 for the next-best baseline. They additionally release Meno-Lite-0.1, a 7B domain-adapted model with a strong cost-performance ratio.

**Why trending:** Competition wins reliably draw interest; the judge-orchestrated ensemble approach is a practically reusable pattern, and the 1st-place result with a 7B-class model versus much larger baselines is notable.

---

## 5. MARBLE: Multi-Aspect Reward Balance for Diffusion RL
**Authors:** Canyu Zhao, Hao Chen, Yunze Tong, Yu Qiao, Jiacheng Li, Chunhua Shen
**arXiv:** [arxiv.org/abs/2605.06507](https://arxiv.org/abs/2605.06507)
**Sources:** HuggingFace Daily Papers (#5, 32 upvotes)

**Summary:** MARBLE addresses multi-reward RLHF for diffusion models by maintaining independent advantage estimators per reward and harmonizing their policy gradients via Quadratic Programming — eliminating the need for hand-tuned weighted-sum rewards. On SD3.5 Medium with five simultaneous rewards, MARBLE improves all five dimensions at once, flips the worst-aligned reward's gradient cosine from mostly negative to consistently positive, and runs at 0.97× the speed of single-reward training.

**Why trending:** Multi-reward alignment for image generation is practically important and under-solved; the QP-based gradient harmonization is theoretically clean and the SD3.5 results are practical and reproducible.

---

## 6. When to Trust Imagination: Adaptive Action Execution for World Action Models
**Authors:** Rui Wang, Yue Zhang, Jiehong Lin, Kuncheng Luo, Jianan Wang, Zhongrui Wang, Xiaojuan Qi
**arXiv:** [arxiv.org/abs/2605.06222](https://arxiv.org/abs/2605.06222)
**Sources:** HuggingFace Daily Papers (#6, 32 upvotes)

**Summary:** World Action Models (WAMs) for robotics typically execute a fixed number of predicted actions per inference step, even when reality diverges from the imagined future. This paper introduces FFDC (Future Forward Dynamics Causal Attention), a lightweight verifier that decides when to trust the predicted rollout vs. replan, reducing WAM forward passes by 69.1% and execution time by 34% on RoboTwin while improving success rate by 35% in real-world experiments.

**Why trending:** World models for robot control are a high-interest area; the adaptive execution framing is novel and the 35% real-world success improvement is a strong empirical result.

---

## 7. Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction
**Authors:** Zhuofeng Li, Haoxiang Zhang, Cong Wei, Pan Lu, Ping Nie, Yi Lu, Yuyang Bai, Shangbin Feng, Hangxiao Zhu, Ming Zhong, Yuyu Zhang, Jianwen Xie, Yejin Choi, James Zou, Jiawei Han, Wenhu Chen, Jimmy Lin, Dongfu Jiang, Yu Zhang
**arXiv:** [arxiv.org/abs/2605.05242](https://arxiv.org/abs/2605.05242)
**Sources:** HuggingFace Daily Papers (#7, 32 upvotes)

**Summary:** Instead of routing agentic search through embedding models and vector indices, Direct Corpus Interaction (DCI) lets agents search raw corpora with shell tools (grep, file reads, lightweight scripts), requiring no offline indexing. DCI substantially outperforms strong sparse, dense, and reranking baselines on BRIGHT and BEIR datasets and reaches strong accuracy on BrowseComp-Plus and multi-hop QA — without any conventional retriever.

**Why trending:** The provocative argument that "just use grep" beats carefully tuned vector retrieval for agentic tasks challenges the dominant RAG paradigm and is backed by broad benchmark results with an impressive author list including Yejin Choi, James Zou, and Jiawei Han.

---

## 8. Continuous-Time Distribution Matching for Few-Step Diffusion Distillation (CDM)
**Authors:** Tao Liu, Hao Yan, Mengting Chen, Taihang Hu, Zhengrong Yue, Zihao Pan, Jinsong Lan, Xiaoyong Zhu, Ming-Ming Cheng, Bo Zheng, Yaxing Wang
**arXiv:** [arxiv.org/abs/2605.06376](https://arxiv.org/abs/2605.06376)
**Sources:** HuggingFace Daily Papers (#8, 20 upvotes, 3 comments)

**Summary:** CDM extends Distribution Matching Distillation (DMD) from discrete timestep anchoring to continuous-time optimization, using a dynamic random-length schedule and an off-trajectory alignment objective to match distributions at arbitrary points along sampling trajectories. On SD3-Medium and Longcat-Image, CDM achieves highly competitive few-step visual fidelity without GANs or reward models. Code available.

**Why trending:** Diffusion distillation is a top applied research area; migrating DMD to continuous time is a principled advance that removes the need for complex auxiliary losses — and the open-source code release drives immediate uptake.

---

## 9. Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration (LoPE)
**Authors:** Langlin Huang, Chengsong Huang, Jinyuan Li, Donghong Cai, Yuyi Yang, Jiaxin Huang
**arXiv:** [arxiv.org/abs/2605.05566](https://arxiv.org/abs/2605.05566)
**Sources:** HuggingFace Daily Papers (#9, 19 upvotes)

**Summary:** LoPE (Lorem Perturbation for Exploration) addresses the GRPO "zero-advantage problem" — where all rollouts fail on hard questions, zeroing out training signal — by prepending stochastic Lorem Ipsum sequences to prompts before resampling, shifting output distributions enough to unlock alternative reasoning paths. Experiments across 1.7B, 4B, and 7B models show LoPE significantly outperforms plain resampling with original prompts.

**Why trending:** The counterintuitive finding that meaningless Latin text improves LLM reasoning makes for a compelling headline; it also fills a practical gap in GRPO training that many practitioners have hit.

---

## 10. Audio-Visual Intelligence in Large Foundation Models (Survey)
**Authors:** You Qin, Kai Liu, Shengqiong Wu, Kai Wang, Shijian Deng, Yapeng Tian, Junbin Xiao, Yazhou Xing, Yinghao Ma, Bobo Li, Roger Zimmermann, Lei Cui, Furu Wei, Jiebo Luo, Hao Fei
**arXiv:** [arxiv.org/abs/2605.04045](https://arxiv.org/abs/2605.04045)
**Sources:** HuggingFace Daily Papers (#10, 15 upvotes)

**Summary:** This is the first comprehensive survey of Audio-Visual Intelligence (AVI) through the lens of large foundation models, covering understanding, generation, and interaction tasks with a unified taxonomy. It synthesizes methods from modality tokenization and cross-modal fusion to diffusion-based generation, instruction alignment, and preference optimization — contextualizing recent work like Meta MovieGen and Google Veo-3.

**Why trending:** Surveys of rapidly-moving fields attract wide readership; the framing around Meta MovieGen and Veo-3 is timely, and the unified taxonomy is practically useful for researchers entering the AVI space.

---

## 11. Auto Research with Specialist Agents Develops Effective and Non-Trivial Training Recipes
**Authors:** Jingjie Ning, Xiaochuan Li, Ji Zeng, Hao Kang, Chenyan Xiong
**arXiv:** [arxiv.org/abs/2605.05724](https://arxiv.org/abs/2605.05724)
**Sources:** HuggingFace Daily Papers (#11, 10 upvotes)

**Summary:** This paper instantiates automated ML research as a closed empirical loop where specialist agents propose hypotheses, submit code edits, and incorporate feedback (including crashes and budget overruns) to improve training recipes — with no human intervention during 1,197 headline trials. Across three tasks, the loop autonomously discovers non-trivial improvements: 0.81% reduction in validation bpb, 38.7% improvement on NanoChat-D12 CORE, and 4.59% wallclock reduction on CIFAR-10 Airbench96.

**Why trending:** AutoML and AI-for-science automation are high-interest areas; the no-human-in-the-loop claim across 1,797 total trials with independently verified outcomes is a significant empirical demonstration.

---

## 12. StraTA: Incentivizing Agentic RL with Strategic Trajectory Abstraction
**Authors:** Xiangyuan Xue, Yifan Zhou, Zidong Wang, Shengji Tang, Philip Torr, Wanli Ouyang, Lei Bai, Zhenfei Yin
**arXiv:** [arxiv.org/abs/2605.06642](https://arxiv.org/abs/2605.06642)
**Sources:** HuggingFace Daily Papers (#12, 10 upvotes)

**Summary:** StraTA introduces an explicit trajectory-level strategy — sampled from the initial task state, then used to condition all subsequent actions — into agentic RL, trained jointly with a hierarchical GRPO-style rollout. On ALFWorld (93.1%), WebShop (84.2%), and SciWorld (63.5%), StraTA outperforms both strong baselines and frontier closed-source models.

**Why trending:** State-of-the-art agent RL results across three standard benchmarks, with notable co-authors (Philip Torr, Wanli Ouyang), attract attention from the robotics and NLP communities simultaneously.

---

## 13. Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key (ScaleLogic)
**Authors:** Tianle Wang, Zhaoyang Wang, Guangchen Lan, Xinpeng Wei, Sipeng Zhang, Guanwen Qiu, Abulhair Saparov
**arXiv:** [arxiv.org/abs/2605.06638](https://arxiv.org/abs/2605.06638)
**Sources:** HuggingFace Daily Papers (#13, 7 upvotes, 3 comments)

**Summary:** ScaleLogic is a synthetic logical reasoning framework that independently controls proof depth and logical expressiveness (from simple if-then to full FOL with negation and quantification), revealing a power-law relationship T ∝ D^γ (R²>0.99) between RL training compute and reasoning depth. The scaling exponent γ grows from 1.04 to 2.60 with logical expressiveness, and more expressive training yields up to +10.66 points on downstream math/reasoning benchmarks — showing that *what* you train on matters as much as *how much*.

**Why trending:** Principled analysis of RL scaling for reasoning with clean power-law fits is exactly what the field needs right now; the "expressiveness matters" finding has immediate implications for training data curation.

---

## 14. A²TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping
**Authors:** Dingwei Chen, Zefang Zong, Zhipeng Ma, Leo Luo, Yang Li, Chengming Li, Peng Chen, Jie Jiang
**arXiv:** [arxiv.org/abs/2605.06200](https://arxiv.org/abs/2605.06200)
**Sources:** HuggingFace Daily Papers (#14, 7 upvotes, 3 comments)

**Summary:** A²TGPO addresses credit assignment in multi-turn agentic RL by using Information Gain (change in predicted probability of ground-truth) as an intrinsic turn-level signal, with three fixes: turn-group normalization (compare turns only to peers at the same depth), variance-rescaled discounted accumulation (stabilize advantage magnitude across trajectory depth), and adaptive turn-level clipping (widen updates for informative turns, narrow for uninformative ones). The result is process-level credit assignment without external reward models.

**Why trending:** Multi-turn credit assignment in agentic RL is an active and practically important problem; the Information Gain framing is principled and the three-fix decomposition is clearly motivated.

---

## 15. SkillOS: Learning Skill Curation for Self-Evolving Agents
**Authors:** Siru Ouyang, Jun Yan, Yanfei Chen, Rujun Han, Zifeng Wang, Bhavana Dalvi Mishra, Rui Meng, Chun-Liang Li, Yizhu Jiao, Kaiwen Zha, Maohao Shen, Vishy Tirumalashetty, George Lee, Jiawei Han, Tomas Pfister, Chen-Yu Lee
**arXiv:** [arxiv.org/abs/2605.06614](https://arxiv.org/abs/2605.06614)
**Sources:** HuggingFace Daily Papers (#15, 8 upvotes)

**Summary:** SkillOS trains a skill curator (with RL on grouped task streams) separately from a frozen agent executor, where earlier trajectories update an external SkillRepo and later related tasks provide evaluation signal for curation policy learning. The learned curator outperforms memory-free and strong memory-based baselines on multi-turn agentic and single-turn reasoning tasks, generalizing across executor backbones and domains.

**Why trending:** Comes from a strong author list (Jiawei Han, Tomas Pfister, Chen-Yu Lee at Google); the RL-trained curator approach is complementary to and distinct from Skill1 (#1), generating community discussion about the two approaches.

---

## 16. UniPool: A Globally Shared Expert Pool for Mixture-of-Experts
**Authors:** Minbin Huang, Han Shi, Chuanyang Zheng, Yimeng Wu, Guoxuan Chen, Xintong Yu, Yichun Yin, Hong Cheng
**arXiv:** [arxiv.org/abs/2605.06665](https://arxiv.org/abs/2605.06665)
**Sources:** HuggingFace Daily Papers (#16, 6 upvotes, 3 comments)

**Summary:** UniPool replaces per-layer expert sets in MoE Transformers with a single globally shared expert pool accessed by independent per-layer routers, with pool-level auxiliary loss and NormRouter for stable balanced training. Across five LLaMA-scale models (182M–978M) trained on 30B tokens, UniPool consistently reduces validation loss by up to 0.0386 vs. matched vanilla MoE — and reduced-pool variants using only 41.6–66.7% of vanilla expert parameters match or outperform the full baseline.

**Why trending:** MoE architecture improvements are practically impactful given widespread MoE model deployment; the sublinear-depth expert-parameter scaling result challenges a fundamental assumption of current MoE design.

---

## 17. TabEmbed: Benchmarking and Learning Generalist Embeddings for Tabular Understanding
**Authors:** Minjie Qiang, Mingming Zhang, Xiaoyi Bao, Xing Fu, Yu Cheng, Weiqiang Wang, Zhongqing Wang, Ningtao Wang
**arXiv:** [arxiv.org/abs/2605.04962](https://arxiv.org/abs/2605.04962)
**Sources:** HuggingFace Daily Papers (#17, 6 upvotes)

**Summary:** TabEmbed introduces TabBench (the first comprehensive benchmark for tabular embedding evaluation) and a generalist embedding model that unifies tabular classification and retrieval in a shared embedding space via large-scale contrastive learning with positive-aware hard negative mining. TabEmbed significantly outperforms state-of-the-art text embedding models on TabBench, establishing a new baseline for universal tabular representation learning.

**Why trending:** Tabular data is ubiquitous in enterprise settings but has lagged behind text/vision in foundation model adoption; a generalist embedding model with open-source code and datasets fills a real gap.

---

## 18. ReflectDrive-2: RL-Aligned Self-Editing for Discrete Diffusion Autonomous Driving
**Authors:** Huimin Wang, Yue Wang, Bihao Cui, Pengxiang Li, Ben Lu, Mingqian Wang, Tong Wang, Chuan Tang, Teng Zhang, Kun Zhan
**arXiv:** [arxiv.org/abs/2605.04647](https://arxiv.org/abs/2605.04647)
**Sources:** HuggingFace Daily Papers (#18, 6 upvotes)

**Summary:** ReflectDrive-2 uses a masked discrete diffusion planner that can revise trajectory tokens in-place (AutoEdit), trained with RL that propagates terminal driving reward through full decision-draft-reflect rollouts. On NAVSIM, it achieves 91.0 PDMS camera-only (94.8 oracle) with only 31.8 ms average latency on NVIDIA Thor.

**Why trending:** Discrete diffusion + RL for autonomous driving is a novel combination; the strong NAVSIM benchmark numbers and practical latency figures on shipping hardware are compelling.

---

## 19. SwiftI2V: Efficient High-Resolution Image-to-Video Generation via Conditional Segment-wise Generation
**Authors:** YaoYang Liu, Yuechen Zhang, Wenbo Li, Yufei Zhao, Rui Liu, Long Chen
**arXiv:** [arxiv.org/abs/2605.06356](https://arxiv.org/abs/2605.06356)
**Sources:** HuggingFace Daily Papers (#19, 5 upvotes)

**Summary:** SwiftI2V enables practical 2K image-to-video generation via Conditional Segment-wise Generation (CSG): a low-resolution motion reference reduces token cost, then a strongly image-conditioned 2K synthesis stage with bidirectional contextual interaction recovers fine-grained details. On VBench-I2V at 2K resolution, it matches end-to-end baselines while reducing total GPU-time by 202×, running on a single H800 or RTX 4090.

**Why trending:** 202× GPU efficiency for 2K video generation is a headline number; the consumer GPU (RTX 4090) support makes it immediately accessible to practitioners and the open-source community.

---

## 20. RemoteZero: Geospatial Reasoning with Zero Human Annotations
**Authors:** Liang Yao, Fan Liu, Shengxiang Xu, Chuanyi Zhang, Rui Min, Shimin Di, Yuhui Zheng
**arXiv:** [arxiv.org/abs/2605.04451](https://arxiv.org/abs/2605.04451)
**Sources:** HuggingFace Daily Papers (#20, 5 upvotes)

**Summary:** RemoteZero eliminates box-annotation supervision for geospatial visual grounding in remote sensing by exploiting a key asymmetry: MLLMs are better at *verifying* whether a region matches a query than at *generating* precise coordinates. This discriminative ability drives GRPO training without any annotated coordinates, enabling iterative self-evolution on unlabeled remote sensing imagery.

**Why trending:** Annotation-free geospatial AI is both scientifically interesting and practically important for Earth observation at scale; the self-verification insight is broadly applicable beyond the remote sensing domain.
