---
title: "Daily AI Papers — October 30, 2026"
date: 2026-10-30
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-30/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal-ai
  - efficient-inference
  - ai-agents
---

### 1. Intrinsic Distribution Matching
**Authors:** Deyuan Liu, Yansen Han, Kaiwen Zheng, Jun Xie, Jiacheng Liu, Zhenglin Cheng, Peng Sun, Jintao Zhang, Jianguo Li, Tao Lin
**arXiv:** [arxiv.org/abs/2610.39633](https://arxiv.org/abs/2610.39633)
**Summary:** Intrinsic Distribution Matching adds explicit feature-mean and standard-deviation constraints to distribution matching distillation, using the generator's exponential-moving-average copy without an external feature encoder. At two network evaluations, it reports 94.25% and 90.20% on Chinese and English LongText-Bench, respectively, the highest scores among compared methods at that budget.

---

### 2. A-RSI: Adaptive Task Refresh for Zero-Data Multimodal Self-Improvement
**Authors:** Yu Liu, Youxing Li, Yuedong Tan, Zhiwei Yang, Zihan Su, Hanqi Feng, Shaojie Zhang, Libin Liao, Zihao Wan, Chenxu Wu, Cong Cao, Fangfang Yuan, Yanbing Liu, Ziheng Chen, Pei Fu, Radu Timofte, Zongwei Wu, Nicu Sebe, Barnabas Poczos, Jian Luan
**arXiv:** [arxiv.org/abs/2610.38568](https://arxiv.org/abs/2610.38568)
**Summary:** A-RSI uses reward variation and training accuracy to refresh a multimodal task pool when its learning signal declines, while model-authored programs generate independently checkable answers. Without external training examples or human-written answer labels, it raises the average across eleven benchmarks from 57.77 to 61.05 using 800 fresh tasks.

---

### 3. Your Benchmark Is an Empirical Measure Over Difficulty
**Authors:** Yifan Sun, Naicheng Yu, Jiawen Gong, Jingyan Shen, Huan Zhang
**arXiv:** [arxiv.org/abs/2610.29927](https://arxiv.org/abs/2610.29927)
**Summary:** This paper treats a benchmark as an empirical measure over difficulty and introduces diagnostics with theoretical guarantees for difficulty-distribution mismatch and coverage gaps. An analysis of 25 benchmarks across seven domains identifies both problems, and the proposed BenchFill algorithm reduces local coverage gaps through difficulty-targeted item rewriting.

---

### 4. Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs
**Authors:** Donghyeon Cho, Joowon Kim, Seungho Shin, Eunho Yang
**arXiv:** [arxiv.org/abs/2610.36671](https://arxiv.org/abs/2610.36671)
**Summary:** LOWN routes visual processing in diffusion vision-language models by comparing image-free predictions with the last image-conditioned predictions and reusing certified agreements. Without training or a tuned threshold, it retains 99.6% of LLaDA-V's score across ten benchmarks while using 35.3% of the decoding FLOPs on average.

---

### 5. L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory
**Authors:** Jinhyeok Choi, JoungBin Lee, Jongmin Lee, Minkyeong Jeon, Jiyoung Kim, Kaeun Han, Yoonjin Yoon, Seungryong Kim
**arXiv:** [arxiv.org/abs/2610.40614](https://arxiv.org/abs/2610.40614)
**Summary:** L3G-World alternates a video diffusion transformer with a latent 3D Gaussian memory updater, storing VAE features directly and growing memory with scene extent rather than stream length. It reports state-of-the-art generation quality and long-horizon spatial consistency at 9 FPS, with up to 38.6 times fewer 3D primitives and 359 times faster memory rendering than the most efficient prior baseline for each metric.

---

### 6. WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training
**Authors:** Ziyang Zeng, Tingyang Chen, Jia Deng, Qiyao Wang, Shuo Tang, Yike Yang, Tao Ren, Wayne Xin Zhao, Feng Chang, Jujie He, Chuan Hao, Ran Tao, Bryan Dai
**arXiv:** [arxiv.org/abs/2610.37161](https://arxiv.org/abs/2610.37161)
**Summary:** WorkFactory converts professional intents into executable agent tasks using information-support graphs, probe executions, and targeted repairs, producing 112,686 tasks across 612 occupations. Fine-tuning three Qwen model scales yields WorkPilot models that improve across four professional-work benchmarks, including an increase from 879 to 1565 Elo for WorkPilot-35B-A3B on GDPval-AA v2.1.

---

### 7. A Broader Look into MLLM's Retrieval Heads
**Authors:** Jia Wang, Yuqing Li, Jiangnan Li, Zheng Lin, Mo Yu
**arXiv:** [arxiv.org/abs/2610.32411](https://arxiv.org/abs/2610.32411)
**Summary:** Across 18 language, vision-language, and omni-modal checkpoints, this study finds that sparse retrieval heads are substantially shared across modalities and that their ablation harms retrieval and other capabilities. Training these heads with a ranking objective improves document retrieval across three model families and raises Qwen3-VL-8B page Recall@1 on MMDocIR by 6.03 points.

---

### 8. Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities
**Authors:** Yunhang Shen, Zhangquan Chen, Xiaotian Li, Zhongpeng Cai, Qing Zhou, Zekai Zhang, Kun Zhang, Zezhong Wu, Jian Hu, Haihan Gao, Heting Gao, Xin Li, Yinsong Liu, Deqian Jiang, Di Yin, Haoyu Cao, Xing Sun, Bing Liu, Yanqiu Qu, Yunfei Wu, Kun Yin, Zhixiang Wei, Yongxiang Hua, Qianyu Li, Xiaoxing Hu, Peiyuan Zhang, Lijiang Li, Dong Xu, Zhenchuan Yang, Yiliang Jiang
**arXiv:** [arxiv.org/abs/2610.39301](https://arxiv.org/abs/2610.39301)
**Summary:** Youtu-Parsing-Omni uses a shared encoder and unified schema to convert documents, images, audio, and video into structured records grounded in space and time. Its single 5B-parameter checkpoint reports 96.96 Overall on OmniDocBench v1.6 and the leading open-weight average of 75.08 on OmniParsingBench, with public code and model weights.

---

### 9. Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers
**Authors:** Jiongfan Yang, Weichen Fan, Haiwen Diao, Zhongang Cai, Ziwei Liu
**arXiv:** [arxiv.org/abs/2610.40647](https://arxiv.org/abs/2610.40647)
**Summary:** SpecSlot separates low-frequency global communication from high-frequency local detail by assigning image-anchor slots to disjoint DCT bands, keeping the generative state and loss in pixel space. It improves ImageNet-512 FID by 2.84 over a FLOPs-matched control with 3.9% fewer FLOPs and exceeds JiT-B/8 on DPG-Bench by 1.06 at 40.6% lower forward cost.

---

### 10. Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models
**Authors:** Xilin Wei, Shengyuan Ding, Xinyu Fang, Tiancheng Gu, Yuchi Wang, Zhixun Li, Ziyu Liu, Yuhang Zang, Weixiang Yu, Cheng Lu, Chonggao Sun, Tong Zhou, Dahua Lin, Hang Zhang, Shuai Bai, Dayiheng Liu
**arXiv:** [arxiv.org/abs/2610.35138](https://arxiv.org/abs/2610.35138)
**Summary:** Co-Design Bench evaluates multimodal application edits and repository revisions using 273 tasks from real coding sessions, 2,331 hidden acceptance criteria, and a judge-then-refute protocol grounded in source and browser evidence. Under a shared harness, the strongest of ten model endpoints satisfies 69.9% of criteria on average but completely solves only 26.4% of tasks.

---

### 11. VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team
**Authors:** Wenbo Hu, Ken Li, Jiazhe Wei, Yukang Cao, Weiyi Hong, Jiayi Dai, Chenjun Bai, Jiajun Liang, Yucheng Liao, Ruichuan An, Zeyu Lou, Haofan Wang, Yueming Lyu, Jingkang Yang, Ziwei Liu, Chenyang Si
**arXiv:** [arxiv.org/abs/2610.33106](https://arxiv.org/abs/2610.33106)
**Summary:** VibeGame creates complete 2D game projects from prompts and optional reference images using an AI-native structured-text engine, frame-synchronous runtime control, and eight specialized implementation and review agents. It distills accepted projects into reusable development assets without training and outperforms compared harnesses on a GameCraft-Bench subset under the same underlying model.

---

### 12. WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video
**Authors:** Chenyu Mu, Wenming Weng, Qinrui Wang, Xingsong Ye, Hao Yu, Jun He, Chong Sun, Chen Li, Jing Lyu, Erkun Yang, Cheng Deng
**arXiv:** [arxiv.org/abs/2610.38352](https://arxiv.org/abs/2610.38352)
**Summary:** WeVisCut couples a shared-state editing harness with a 9B policy trained on more than 130K executable examples recovered from 3,750 finished videos through editing inversion and verified replay. On its 100-task benchmark, it reports performance comparable to Claude Opus 5 while generating nearly 33 times fewer tokens per successful output minute.

---

### 13. HairDeck: Animation-Ready Stylized Hair Cards from a Single Image
**Authors:** Yuze He, Yixiang Wei, Wang Zhao, Chuhao Chen, Yanning Zhou, Yong-Jin Liu
**arXiv:** [arxiv.org/abs/2610.40599](https://arxiv.org/abs/2610.40599)
**Summary:** HairDeck uses set diffusion to generate stylized hair cards and their spring-bone chains from a single image, exporting directly animatable assets. On CHARM's test set, it lowers Chamfer distance by 44%, more than halves card-orientation error, and runs 33 times faster.

---

### 14. PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas
**Authors:** Haoming Li, Defu Cao, Xu Hu, Yingtao Luo, Yiyang Wang, Xianghe Xu, Jiashu He, Wanting Jiang, Yifan Zhang, Yunhan Zhao, Siyang Wu, Chen Yang, Haixin Wang, Zheyuan Deng, Taoran Li, Jingwen Zhang, Zhejian Peng, Shushu Liang, Yue Zhao, Bingzhe Li, Feng Chen, Yifan Wang, Jintao Huang, Yijun Wang, Yuexing Hao, Xiaomin Li
**arXiv:** [arxiv.org/abs/2610.22990](https://arxiv.org/abs/2610.22990)
**Summary:** PersonaCUABench fixes 74 computer-use tasks across eleven domains while varying 44 user personas, exposing agents only to the resulting dialogue rather than hidden profiles or original instructions. Across nine backbones and 3,330 runs, mean task completion falls by 36% relative to original requests, and full completion still does not consistently produce top user satisfaction.

---

### 15. IntReal: A Real-World Dataset and Benchmark for Multimodal Interleaved Generation
**Authors:** Shaohan Yu, Jie Qin, Wende Tan, Haiwen Diao, Limeng Qiao, Yueming Lyu, Chenyang Si
**arXiv:** [arxiv.org/abs/2610.38425](https://arxiv.org/abs/2610.38425)
**Summary:** IntReal introduces a real-world interleaved text-image dataset and a seven-dimension evaluation suite that reports low metric redundancy, 83.3% agreement with human judgments, and strong consistency across expert evaluators. Benchmarking and post-training experiments reveal distinct model strengths and show that modality-specific generation training can also improve interleaved generation.

---

### 16. PhysInsert: Physically Plausible Object Insertion with Geometric Priors and Bidirectional Object-Scene Interactions
**Authors:** Yue Gong, Le Zhang, Rui Chen, Song Chang, Xiaochao Qu, Luoqi Liu, Ting Liu, Yebin Liu
**arXiv:** [arxiv.org/abs/2610.40453](https://arxiv.org/abs/2610.40453)
**Summary:** PhysInsert uses strictly aligned Blender-rendered counterfactual pairs, geometry-guided adaptation, and object-scene spatial supervision to jointly adapt inserted objects and their environments. Its evaluations report improved image fidelity and user-rated gains in placement, lighting integration, perspective, and pose plausibility.

---

### 17. WebAnything: From the Wild Web to Scalable Agent Environments
**Authors:** Tianci Xie, Zikun Cai, Chaoyun Zhang, Pinxue Guo, Bingxuan Li, Rui Zheng, Hang Yan
**arXiv:** [arxiv.org/abs/2610.37786](https://arxiv.org/abs/2610.37786)
**Summary:** WebAnything automatically reconstructs source-grounded, reusable web-agent environments from real URLs using exploration, independent verification, and targeted repair, producing 244 website artifacts and 12,984 accepted tasks. Fine-tuning Qwen3.5-9B on 5,856 interaction trajectories improves REAL success by 9.9 percentage points and WebArena-Verified overall success by 13.33 percentage points under the fixed harness.

---

### 18. CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models
**Authors:** Yingzhuo Deng, Chong Li, Bingxin Liu, Yi Shu, Tianyu Peng, Can Xie, Siyao Song, Shuo Ren, Jiajun Zhang
**arXiv:** [arxiv.org/abs/2610.21143](https://arxiv.org/abs/2610.21143)
**Summary:** CoSTA decouples spoken-dialogue generation and synthesis token spaces through a post-hoc compressed vocabulary and deterministic expansion back to the original speech tokens, preserving the existing tokenizer and decoder. On bilingual benchmarks, it reports approximately 1.7 times expanded speech-token generation speed, lower full-response latency, and higher throughput while preserving response quality.

---

### 19. Glance: The Generator Is Its Own Reranker
**Authors:** Adilet Metinov, Chingiz Arziev
**arXiv:** [arxiv.org/abs/2610.40454](https://arxiv.org/abs/2610.40454)
**Summary:** Glance equips a generator with a lightweight decision adapter and pointer head to rerank passages from shared cached context, avoiding a separate resident reranking model and repeated passage prefills. Initial evaluations on two retrieval datasets and HotpotQA report stronger retrieval and answer quality than the compared cross-encoder, with approximately 0.1 GiB of extra memory per decision skill.

---

### 20. AskStream: When and What to Ask Proactively under Uncertainty in Streaming Video Understanding
**Authors:** Lu Wang, Zhuoran Jin, Longxiang Wang, Junhong Chen, Yupu Hao, Yao Xu, Daojian Zeng, Yubo Chen, Kang Liu, Guang Liu, Jun Zhao
**arXiv:** [arxiv.org/abs/2610.38678](https://arxiv.org/abs/2610.38678)
**Summary:** AskStream introduces asking for missing information as a third action alongside waiting and answering in streaming video understanding, covering video and user uncertainty with 438 videos and 2,714 annotated time windows. Across multiple-choice and open-ended settings, the strongest evaluated model reaches only 52.18% Ask-F1, exposing limitations in proactive information seeking.
