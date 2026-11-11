---
title: "Daily AI Papers — November 11, 2026"
date: 2026-11-11
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-11/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robot-learning
  - world-models
---

### 1. Tree-Ising: Repairing Language Models with Bit-Level Ising Edits
**Authors:** Hadi Salloum, Ammar Ali
**arXiv:** [arxiv.org/abs/2611.14210](https://arxiv.org/abs/2611.14210)
**Summary:** Tree-Ising repairs reasoning loops in a language model by casting weight edits as sparse discrete optimization over its own BF16 bits, decomposed exactly into per-row QUBO (Ising) problems solved on GPU. It beats a frontier agent's weight-space repair on Qwen3.5-0.8B (54.6% vs 51.7% on MATH-500) with fewer bit flips, only four forward-pass requests, and about $0.90 of GPU time.

---

### 2. World In-Context Learning for Agentic Robot Manipulation
**Authors:** Heng Fang, Zehui Guo, Yuehan Zhang, Mingyang Du, Dingkang Liang, Xiang Bai
**arXiv:** [arxiv.org/abs/2611.12885](https://arxiv.org/abs/2611.12885)
**Summary:** World In-Context Learning lets a frozen model start from one demonstration, rehearse the task in a simulator, and write the feedback into its context rather than its weights. The RoboScript implementation reaches 83.4% mean success on all 50 RoboTwin 2.0 tasks with no gradient updates, beating the strongest trained policy by over 20 points and transferring to a real dual-arm robot.

---

### 3. Few-Step Streaming Video Generation via Condition Shifting
**Authors:** Deyuan Liu, Jungang Li, Kaiwen Zheng, Kai Jiang, Jintao Chen, Yaole Wang, Ming Lin, Tao Lin, Jianfei Chen, Jun Zhu, Jintao Zhang
**arXiv:** [arxiv.org/abs/2611.14033](https://arxiv.org/abs/2611.14033)
**Summary:** APEX extends few-step streaming video generation by using condition shifting to estimate the generated distribution's velocity field within the generator itself, removing DMD's separate fake-score network. On 180-second videos it improves instruction fulfillment and visual aesthetics over S2-Avatar while cutting peak GPU memory by 4.4% and iteration time by 9.2% versus DMD.

---

### 4. Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents
**Authors:** Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2611.14320](https://arxiv.org/abs/2611.14320)
**Summary:** WikiTrace stores each agent-memory lesson as a concise insight linked to a summary of why its trajectory succeeded or failed and to the raw trajectory itself. Agents descend through these links to verify or correct lessons before acting, outperforming existing memory approaches on five agentic benchmarks while reducing memory-induced degradation.

---

### 5. OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer
**Authors:** Feng Cheng, Yu-Hsuan Huang, Fengyi Wang, Chaofan Zhou, Zhennan Zhu, Huan He, Bo Zhang, Ruoqi Zhang, Zhanfeng Mo, Ziwei Liu, Lanyi Li, Yifeng Pan, Junhua Long, Ziqiu Zhou, Yue Lin, Shaowei Liu
**arXiv:** [arxiv.org/abs/2611.04720](https://arxiv.org/abs/2611.04720)
**Summary:** OneTrans-GSR reformulates industrial reranking and mix-ranking as one learning problem, using a single decoder-only policy trained with a slate-level reward model to generate the exposure slate end to end. Deployed at scale, it improves GMV per user by 2.63% and advertiser value by 2.06% while cutting reranking and mix-ranking latency by 13%.

---

### 6. dNaViT: Discrete Codes are General-Purpose Visual Representations
**Authors:** Xiaotong Li, Zhengrong Yue, Xu Huang, Jialv Zou, Minhao Jing, Wenhao Yan, Haodong Li, Hai Huang, Bo Zhao, Yan Feng, Peng Pei, Xunliang Cai
**arXiv:** [arxiv.org/abs/2611.12426](https://arxiv.org/abs/2611.12426)
**Summary:** dNaViT is a discrete native-resolution vision transformer that turns a frozen pretrained encoder into a tokenizer producing language-like visual tokens via residual modulation and grouped product quantization. It matches or exceeds task-specific baselines across 12 understanding benchmarks, 4 generation benchmarks, and an image editing benchmark.

---

### 7. Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra Optimization
**Authors:** Zhengyu Hu, Zheyuan Xiao, Yike Wang, Hamish Ivison, Haoyu Wang, Yige Yuan, Rulin Shao, Yuetai Li, Niqi Lyu, Yicheng Ding, Shu Yang, Zhichen Zeng, Banghua Zhu, Jiaxin Pei, Kaize Ding, Pradeep Dasigi, Dan Roth, Hannaneh Hajishirzi, Noah A. Smith, Teng Xiao, Radha Poovendran
**arXiv:** [arxiv.org/abs/2611.11995](https://arxiv.org/abs/2611.11995)
**Summary:** Infrathon is a benchmark of long-horizon AI infrastructure optimization tasks, evaluated with six models over 150 runs of 24 hours each and more than 10,000 GPU-hours. Model rankings shift with horizon, 135 of 150 runs keep improving in the second half, and agents sometimes beat human-designed baselines, such as raising KV-cache compression from 6.82% to 19.86%.

---

### 8. MMDM: Measuring Massive Multitask Decision Making
**Authors:** Junhao Shen, Qing Zong, Yue Guo, Zhanqiu Zhang, Yiwen Guo, Hong Cheng
**arXiv:** [arxiv.org/abs/2611.14309](https://arxiv.org/abs/2611.14309)
**Summary:** MMDM is a benchmark of 5,448 questions across 16 categories for System-1 decision models that pick among query-specified options in a single forward pass, with option spaces up to 1,024 and inputs up to 64,817 tokens. Evaluating 28 decision models shows strong world-knowledge performance but weak handling of interdependent options, constraints, and multi-select tasks.

---

### 9. DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight
**Authors:** Zhongxi Chen, Yi Yang, Xinyi Chen, Mingzhe Ye, Yaping Li, Zhihong Liu, Congsheng Xu, Haonan Wang, Zhijie Deng
**arXiv:** [arxiv.org/abs/2611.11166](https://arxiv.org/abs/2611.11166)
**Summary:** DexForesight learns spatial foresight implicitly by aligning a dexterous policy's latents with a frozen action-conditioned world model that predicts 3D hand-point motion and visual feature changes. At deployment only the RGB policy is kept, raising success on 11 DexJoCo tasks from 49.4% to 60.5% and reaching 58.3% on real-robot tasks versus 50.0% for the strongest baseline.

---

### 10. SWAM: Scaling World Action Models with Cross-Modal Alignment
**Authors:** Yu Zhou, Xinyuan Xia, Xuankun Yang, Yinghao Yang, Wendi Chen, Bowen Liu, Jianhan Ma, Weicheng Duan, Jun Lv, Cewu Lu, Yanwei Li
**arXiv:** [arxiv.org/abs/2611.12870](https://arxiv.org/abs/2611.12870)
**Summary:** SWAM systematically studies how language-video and language-video-action supervision affect world action models, using about 47,000 hours of general, egocentric, UMI, and robot videos. The resulting recipe reaches 88.10% and 61.56% success on RoboTwin Easy and Hard settings and 40.00% on real-world tasks, and the data, code, and weights are released.

---

### 11. MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations
**Authors:** Lorenz K. Muller, Philippe Bich, Chiara Boretti, Hyun-Min Chang, Jiawei Zhuang, Lukas Cavigelli
**arXiv:** [arxiv.org/abs/2611.10649](https://arxiv.org/abs/2611.10649)
**Summary:** MACaQ is an MXFP4 W4A4 post-training quantization method that treats each linear layer independently, applying online per-channel scaling and block-Hadamard transforms plus a Hessian-aware Flip-Refinement step. It adds only 2.3% overhead over pure MXFP4 in vLLM, beats DuQuant++ and MR-GPTQ on perplexity, and quantizes a 122B model in 64 minutes with 32.5GB of GPU memory.

---

### 12. FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance
**Authors:** Yupeng Cao, Xueqing Peng, Lingfei Qian, Haohang Li, Yangyang Yu, Anke Xu, Wenbo Cao, Yan Wang, Yuechen Jiang, Yuyan Wang, Zhuohan Xie, Yankai Chen, Zehan Li, Jimin Huang, Xue Liu, Jian-Yun Nie, Sophia Ananiadou
**arXiv:** [arxiv.org/abs/2611.07464](https://arxiv.org/abs/2611.07464)
**Summary:** FINCOSMOS is an open-world evaluation paradigm where financial agents must elicit a hidden user strategy, acquire Web data, and build point-in-time backtests whose results are verified by programs. Across 150 sessions with four coding agents and a tool-less model, no session is accepted, though an agent with persistent memory learned all ten tasks using FINCOSMOS feedback.

---

### 13. How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time
**Authors:** Ku Onoda, Haruto Kawano, Shota Takashiro, Kohei Hayashi
**arXiv:** [arxiv.org/abs/2611.12324](https://arxiv.org/abs/2611.12324)
**Summary:** Using ARC-AGI-3 games, the paper introduces MechEval to measure how many exposures a world model needs to learn new game mechanics, and builds WARC, a 35M-parameter ViT that updates its parameters after every transition. WARC learns four in five held-out mechanics to at least 80% accuracy, and pairing it with an explorer triples the official efficiency score from 0.15 to 0.46.

---

### 14. ProTEUS: A mutation-resolved world model for closed-loop protein evolution
**Authors:** Yikun Zhang, Minghao Guo, Guangxue Xu, Peter Yichen Chen, Wojciech Matusik, Wengong Jin, Jingjing Chai, Kaiyi Jiang
**arXiv:** [arxiv.org/abs/2611.13348](https://arxiv.org/abs/2611.13348)
**Summary:** ProTEUS is a mutation-resolved world model for protein evolution that represents variants as latent states and mutations as actions, combining a MutationFormer architecture with a physics-constrained all-atom predictor over 10 times faster than AlphaFold3. In two closed-loop experimental campaigns it produced enzyme variants with more than 10-fold higher activity than wild type.

---

### 15. WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning
**Authors:** Sang-Hoon Lee, Ha-Yeong Choi
**arXiv:** [arxiv.org/abs/2611.12527](https://arxiv.org/abs/2611.12527)
**Summary:** WaveGen is a fully end-to-end diffusion text-to-waveform model that uses Spectral Forcing to learn an internal spectral trajectory jointly with the target waveform, without codecs, vocoders, duration predictors, or self-supervised features. Scaled from 0.1B to 0.6B parameters with one-stage training on open data, it reaches a WER of 1.47 and SIM of 0.75 on Seed-en.

---

### 16. DepthGraft: Structural Regularization through Hierarchical Cross-Layer KV Reconstruction
**Authors:** Xiaohan Qin, Xiangdong Zhang, Yu Wang, Huaijin Wu, Zhuo Xia, Yebin Yang, Junchi Yan
**arXiv:** [arxiv.org/abs/2611.03142](https://arxiv.org/abs/2611.03142)
**Summary:** DepthGraft revisits cross-layer KV sharing as an implicit structural regularizer and reconstructs deep-layer KV from stride-aligned shallow-middle source pairs, cutting KV cache by roughly one third. Across dense and MoE models from 0.5B to 16B it improves downstream results, including a 7.0-point MMLU-Pro gain on the 16B MoE model.

---

### 17. MotionGraphicsBench: Evaluating Motion Graphics Generation with Programmatic Verification
**Authors:** Jiaju Ma, Ashvini Kumar Jindal, Chuhua Wang, Sumithra Bhakthavatsalam
**arXiv:** [arxiv.org/abs/2611.10592](https://arxiv.org/abs/2611.10592)
**Summary:** MotionGraphicsBench is an expert-curated benchmark of 100 tasks for animating a static SVG from a motion edit prompt, each paired with a deterministic verification program built from real Lottie designs. Its programs agree with human judgments 93.3% of the time, and across 47 configurations from 32 LLMs pass@1 ranges from 6.0% to 67.7%.

---

### 18. PhysOPSD: Code as Privilege for Physically Plausible Video Generation
**Authors:** Harold Haodong Chen, Rui Peng, Lingteng Qiu, Kejie Qiu, Chao Xu, Zilong Dong
**arXiv:** [arxiv.org/abs/2611.12411](https://arxiv.org/abs/2611.12411)
**Summary:** PhysOPSD uses executable simulation code as privileged context for on-policy self-distillation of video generators, translating real physical scenarios into verifiable programs. With dual-level physical privilege and controlled physical variations, it improves physical plausibility across backbones with only 3K samples while preserving general video quality.

---

### 19. PhyRubric: Rubric-Grounded Diagnostic Evaluation of Physical Commonsense in Text-to-Video Generation
**Authors:** Huiyi Chen, Weitai Kang, Shicheng Fan, Xinshuo Wang, Zhixiang Shen, Yan Yan, Philip S. Yu, Baoxin Li
**arXiv:** [arxiv.org/abs/2611.13576](https://arxiv.org/abs/2611.13576)
**Summary:** PhyRubric evaluates physical commonsense in text-to-video models by building a caption-specific rubric of semantic and physical items and scoring item-level verdicts grounded in timestamped evidence. Results across ten T2V models show physical commonsense is far from solved, and the open PhyRubric-Judge tracks human judgments better than existing open-source judges.

---

### 20. e-means: outperforming k-means (in one-tenth the epochs)
**Authors:** Swann Bessa, Pierre-Emmanuel Mazaré, Gergely Szilvasy, Hugo Touvron, David Picard, Matthijs Douze, Hervé Jégou
**arXiv:** [arxiv.org/abs/2611.09501](https://arxiv.org/abs/2611.09501)
**Summary:** e-means is a mini-batch k-means variant driven by an exponential moving average, with scaling laws that set decay rate and batch size without hyperparameter sweeps. It beats Lloyd k-means' 25-epoch loss in 1.4 to 2.6 epochs, giving 10-45x GPU wall-clock speedups, and clusters 10 billion DINO embeddings into 16 million clusters in 2.5 epochs.
