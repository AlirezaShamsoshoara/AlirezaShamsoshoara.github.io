---
title: "Daily AI Papers — September 11, 2026"
date: 2026-09-11
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-11/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - multimodal-ai
  - world-models
---

### 1. Scaling Automatic Research Agents via World Models
**Authors:** Xiyuan Yang, Sheikh Sarwar, Jingru Cheng, Zhan Shi, Duanshun Li, Huiyuan Chen, Haiyang Zhang, Xing Fan, Chenlei Guo, Jingrui He, Zhenyu Liao
**arXiv:** [arxiv.org/abs/2608.12564](https://arxiv.org/abs/2608.12564)
**Summary:** Automating empirical research is a long-standing direction of AI. Recent automatic research (AutoResearch) agents bring this goal within reach, as modern LLMs show the capability to independently implement solutions and learn from the execution outcomes.
**Trending because:** 434 HuggingFace upvotes + scales automated empirical research with world-model-generated experiment proposals

---

### 2. NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction
**Authors:** NCP Team, Jiaqi Cao, Chiyu Chen, Shuang Cheng, Xu Cheng, Beiya Dai, Yufan Feng, Kewen Ge, Ruijun Ge, Jiayi Huang, Yang Jiao, Dahua Lin, Zhouhan Lin, Yifan Liu, Yuliang Liu, Biqing Qi, Mowen Ruan, Junzhe Shen, Yunchong Song, Hao Sun, Zhongbo Tian, Yixuan Wang, Rubin Wei, Jiaxin Xiong, Kangyu Yang, Qian Yao, Qi Zhang, Bowen Zhou
**arXiv:** [arxiv.org/abs/2609.10715](https://arxiv.org/abs/2609.10715)
**Summary:** We introduce NCP-ArchPreview, a latent-space language model that pushes autoregressive pretraining beyond standard next-token prediction (NTP). Alongside NTP, the model learns through Next Concept Prediction (NCP) to predict discrete concepts that span multiple tokens, introducing an explicit and more challenging concept-level objective while preserving standard token-level autoregressive generation.
**Trending because:** 135 HuggingFace upvotes + introduces concept-level autoregressive pretraining beyond next-token prediction

---

### 3. SenseNova-U1.5: Towards Native Unified Visual Intelligence
**Authors:** Haiwen Diao, Jiahao Wang, Chenjing Ding, Hanming Deng, Jiangnan Chen, Ruixi Zhang, Ruohui Wang, Wenwen Tong, Xiangyu Fan, Yubo Wang, Yue Zhu, Yuwei Niu, Zhengqi Bai, Zhiqian Lin, Zhitao Yang, Zhongang Cai, Bo Yang, Chen Feng, Chengguang Lv, Guangjia Liu, Guanlin Wang, Hanyu Zhang, Haojia Yu, Hongcan Xiao, Hongli Wang, Huan Wu, Huaping Zhong, Jian Fang, Jianan Fan, Jiaqi Li, Jiefan Lu, Jing Zuo, Jingcheng Ni, Junxiang Xu, Linjun Dai, Mutian Xu, Peishen Yan, Penghao Wu, Ruijie Mao, Ruisi Wang, Shihao Bai, Shuang Yang, Shuya Yang, Shuyan Zheng, Silei Wu, Siying Li, Tao Chu, Tianbo Zhong, Tongxi Zhou, Weichao Luo, Weichen Fan, Wenhao Jia, Wenjie Gao, Xiangli Kong, Yan Li, Yang Yong, Zimo Wen, Zixuan Qian, Wenxiu Sun, Ruihao Gong, Quan Wang, Lewei Lu, Lei Yang, Ziwei Liu, Dahua Lin
**arXiv:** [arxiv.org/abs/2609.11929](https://arxiv.org/abs/2609.11929)
**Summary:** We launch SenseNova-U1.5, an 8B-MoT native unified multimodal model that understands, reasons about, and generates visual content within an encoder-free and VAE-free architecture. We strengthen its visual interface through spatially coherent patch reconstruction and scale its training with carefully curated generation and editing data, improved task formulation, structural prompt enhancement, and native resolutions of up to 4K.
**Trending because:** 112 HuggingFace upvotes + unifies visual understanding, reasoning, and generation in an 8B multimodal model

---

### 4. SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem
**Authors:** Soohyun Ryu, Sohee Kim, Eunho Yang
**arXiv:** [arxiv.org/abs/2609.07064](https://arxiv.org/abs/2609.07064)
**Summary:** Large Vision-Language Models (LVLMs) have achieved strong performance on diverse visual tasks, yet their ability to reconstruct and reason about the 3D structure of the scene depicted in 2D images -- referred to as spatial intelligence -- remains limited. Existing approaches attempt to address this gap by using real-scene spatial question answering datasets that require dense geometric annotations.
**Trending because:** 50 HuggingFace upvotes + uses synthetic block stacking to improve 3D spatial reasoning in vision-language models

---

### 5. T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks
**Authors:** Junyao Yang, Yucheng Shi, Zhongzhi Li, Ruhan Wang, Zongxia Li, Haitao Mi, Leowei Liang
**arXiv:** [arxiv.org/abs/2609.11042](https://arxiv.org/abs/2609.11042)
**Summary:** Agent usage is shifting toward long-horizon tasks such as coding and scientific discovery, among which terminal tasks are especially important. We introduce T1, a Mixture-of-Experts model of 122B total trained with reinforcement learning, operating a real shell in a cloud sandbox for up to 300+ tool-call turns per task, rewarded by executing each task's own verifier.
**Trending because:** 44 HuggingFace upvotes + trains a 122B terminal agent with reinforcement learning on 300-plus-turn tasks

---

### 6. EvoSafeHarness: Evolving Model- and Domain-Specific Harnesses for Securing Agents
**Authors:** Nanxi Li, Yingzi Ma, Yulong Cao, Edward Suh, Bo Li, Dawn Song, Chaowei Xiao
**arXiv:** [arxiv.org/abs/2609.05903](https://arxiv.org/abs/2609.05903)
**Summary:** Large Language Model (LLM) agents are turning language into real-world effects, making safety necessary against both indirect prompt injections and direct harmful requests. System-level safety harnesses add an enforcement layer beyond model-level defenses, but existing harnesses are usually designed once by experts and applied across heterogeneous models and domains.
**Trending because:** 35 HuggingFace upvotes + evolves model- and domain-specific safety harnesses for LLM agents

---

### 7. Mi-Ripple: Restoring Images Degraded by Iterative AI Editing
**Authors:** Jiayin Chen, Yicheng Xu, Muting Wang
**arXiv:** [arxiv.org/abs/2609.11317](https://arxiv.org/abs/2609.11317)
**Summary:** Iterative reference-conditioned image editing can introduce grid-like and granular textures, commonly described as digital ripple. We present Mi-Ripple, a diagnosis-guided restoration workflow that suppresses this digital ripple while protecting image structure.
**Trending because:** 20 HuggingFace upvotes + targets artifacts accumulated through iterative AI image editing

---

### 8. PARSER: Read in Parallel, Reason in Depth for Long-Context LLM Agents
**Authors:** Kun Li, Zexuan Qiu, Tianhua Zhang, Irwin King, Helen Meng
**arXiv:** [arxiv.org/abs/2609.06702](https://arxiv.org/abs/2609.06702)
**Summary:** Sequential memory agents process long documents by reading chunks one after another while maintaining a compact memory state, coupling document traversal to reasoning depth. This coupling introduces sensitivity to evidence placement and ties inference latency linearly to document length.
**Trending because:** 17 HuggingFace upvotes + parallelizes long-context reading while preserving deeper reasoning

---

### 9. X-AuT: Progressive Audio-Encoder Compression for Speech LLMs with Cross-Scale Distillation
**Authors:** Haojun Zhang, Yi Zou, Min Chen, Qize Yu, Lianrui Fan, Xini Ding, Hao Li, Shuchang Zhou, Xianming Liu, Shiyu Huang
**arXiv:** [arxiv.org/abs/2609.11412](https://arxiv.org/abs/2609.11412)
**Summary:** Reducing audio-encoder depth lowers the inference cost of speech large language models, but removing complete blocks perturbs the embeddings consumed by the decoder and can cause deletion and premature end-of-sequence errors. We introduce X-AuT, a progressive framework that selects layer combinations through short behavioral probes and restores the pruned model through representation alignment, cross-scale distillation, scheduled student-policy supervision, and LoRA finetuning.
**Trending because:** 12 HuggingFace upvotes + compresses speech-LLM audio encoders while protecting decoder behavior

---

### 10. Memory as Plans: World-Action Modeling with Memory-Grounded Planning
**Authors:** Sizhe Zhao, Haozhe Xie, Weiyu Zhao, Chenchu Zhang, Huan Wang, Chenyang Wang, Qinglin Liu, Shengping Zhang
**arXiv:** [arxiv.org/abs/2609.11561](https://arxiv.org/abs/2609.11561)
**Summary:** Mainstream robotic policies often adopt a Markovian formulation, but many complex real-world manipulation tasks are inherently non-Markovian, requiring long-horizon memory beyond the current observation. Existing memory mechanisms often rely on language summaries, growing visual windows, or their combinations, and may therefore lose fine-grained visual evidence or face a trade-off between history coverage and execution efficiency.
**Trending because:** 9 HuggingFace upvotes + grounds long-horizon robot planning in structured memory

---

### 11. Train Smarter, Not Harder: Switching Signal-Guided Training in Active Learning
**Authors:** Nagham Omar, Maya Rozenshtein, Evgeny Mishlyakov, Avigdor Gal
**arXiv:** [arxiv.org/abs/2609.06806](https://arxiv.org/abs/2609.06806)
**Summary:** Training strategy, namely whether to retrain from scratch or fine-tune from the previous checkpoint, is an overlooked decision variable in active learning. We show that this choice has exploitable structure: retraining is most useful in early rounds, when each batch can substantially reshape the labeled distribution, while fine-tuning becomes safer once the model trajectory stabilizes.
**Trending because:** 8 HuggingFace upvotes + adapts scratch training versus fine-tuning across active-learning rounds

---

### 12. SchemeArena: Factorized Stress Testing of Scheming in LLM Agents
**Authors:** Jie Ruan, Inderjeet Nair, Amy Liu, Muhammad Khalifa, Yusheng Zhou, Lu Wang
**arXiv:** [arxiv.org/abs/2609.08126](https://arxiv.org/abs/2609.08126)
**Summary:** We study scheming in LLM agents, in which agents covertly pursue misaligned goals. Our focus is to understand how scheming arises from the interaction of key factors, such as instrumental goals, environmental affordances, oversight conditions, and perceived consequences.
**Trending because:** 7 HuggingFace upvotes + factorizes how goals, environments, oversight, and consequences drive agent scheming

---

### 13. Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs
**Authors:** Killian Steunou, Yannis Tevissen, Mounîm A. El Yacoubi
**arXiv:** [arxiv.org/abs/2609.10355](https://arxiv.org/abs/2609.10355)
**Summary:** Video understanding has rapidly evolved toward video large language models (VideoLLMs): systems that couple video representations with pretrained large language models and condition generation on a textual prompt. Their strong performance on captioning, question answering, retrieval and temporal grounding comes at a computation and memory cost that grows with frame count and context length, limiting deployment in real-time, mobile and resource-constrained settings.
**Trending because:** 6 HuggingFace upvotes + surveys the computation and memory bottlenecks of video and audiovisual LLMs

---

### 14. TempCloze: Can Video-LLMs Identify the Missing Middle?
**Authors:** Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu, Jiahao Meng, Han Chen, Ziyu Wang, Hongyang Du
**arXiv:** [arxiv.org/abs/2609.01515](https://arxiv.org/abs/2609.01515)
**Summary:** Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs.
**Trending because:** 6 HuggingFace upvotes + reduces linguistic shortcuts in video temporal-reasoning evaluation

---

### 15. OracleZoom: On-Policy Self-Distillation Inspired Reference-Constrained Recursive Image Super Resolution
**Authors:** Shubhashis Roy Dipta, Sourajit Saha, Shaswati Saha, Nobin Sarwar
**arXiv:** [arxiv.org/abs/2609.06490](https://arxiv.org/abs/2609.06490)
**Summary:** Recursive Super-Resolution (SR) extends fixed-scale SR to extreme magnification by repeatedly feeding predictions back into the same model, analogous to zooming an image repeatedly. However, ground truth availability at every scale, especially at depth, remains challenging as the required source resolution grows geometrically, leaving deeper predictions unsupervised.
**Trending because:** 6 HuggingFace upvotes + extends recursive image super-resolution with reference-constrained self-distillation

---

### 16. StochBench: A Domain-Specific Benchmark for Stochastic Processes in Lean
**Authors:** Idan Davidovich, Debargha Ganguly, Vikash Singh, Vipin Chaudhary
**arXiv:** [arxiv.org/abs/2609.09264](https://arxiv.org/abs/2609.09264)
**Summary:** Leading benchmarks for formal theorem proving with large language models are small collections drawn from competition math, such as the IMO and Putnam, that poorly represent field-specific applications. We introduce StochBench, a Lean 4 benchmark of 450 graduate stochastic-processes problems at varying abstraction levels, each paired with its natural-language source.
**Trending because:** 6 HuggingFace upvotes + brings field-specific graduate stochastic-process proofs to Lean evaluation

---

### 17. Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs
**Authors:** Zhiqi Li, Yuxuan Liao, Bo Zhu
**arXiv:** [arxiv.org/abs/2609.11499](https://arxiv.org/abs/2609.11499)
**Summary:** Code world models represent worlds as executable programs, but this representation alone does not determine how to construct a complex world. We introduce Recursive Code World Models (RCWM), a framework for reconstructing complex 3D worlds in code from a single reference image.
**Trending because:** 5 HuggingFace upvotes + reconstructs complex 3D worlds as recursive executable scene programs

---

### 18. World in World: Explore the World with World Models
**Authors:** Chenxi Song, Yanming Yang, Chi Zhang
**arXiv:** [arxiv.org/abs/2609.11548](https://arxiv.org/abs/2609.11548)
**Summary:** Autoregressive video world models enable interactive, long-horizon exploration, but flexible control remains challenging. Exploring a source video from new viewpoints requires the generated rollout to remain synchronised with the recorded event, place observed content in the requested view, plausibly complete newly exposed regions, and recover previously generated appearance on revisits.
**Trending because:** 5 HuggingFace upvotes + enables controllable exploration of recorded video through a world model

---

### 19. FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation
**Authors:** Vladislav Bargatin, Alexander Yakovenko, Khaled Abud, Dmitriy Vatolin
**arXiv:** [arxiv.org/abs/2609.11486](https://arxiv.org/abs/2609.11486)
**Summary:** Optical flow methods typically rely on task-specific inductive biases, such as correlation volumes, feature warping, and iterative refinement, among others, to reach high accuracy. While effective, such biases constrain the model to predefined heuristics, which can limit its expressivity and lead to more complex pipelines and additional computational cost.
**Trending because:** 5 HuggingFace upvotes + removes task-specific inductive biases from transformer optical-flow estimation

---

### 20. Diffs vs. Whole Files: An Empirical Comparison of Iterative Edit-Based and Direct Generation for Flutter/Dart Code Models
**Authors:** Andrej Andrejev
**arXiv:** [arxiv.org/abs/2609.05779](https://arxiv.org/abs/2609.05779)
**Summary:** Large language models used for code editing can be trained and deployed in at least two output regimes: direct generation, where the model emits the entire modified file in one shot, and iterative diff-based generation ("steps"), where the model emits a sequence of localized search/replace edits applied one at a time until it signals completion or a step budget is exhausted. The diff-based regime is attractive because it mirrors how developers edit code and should require far fewer generated tokens per turn.
**Trending because:** 5 HuggingFace upvotes + empirically compares diff-based edits with whole-file code generation
