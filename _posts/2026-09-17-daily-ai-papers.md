---
title: "Daily AI Papers — September 17, 2026"
date: 2026-09-17
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-17/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-agents
  - scientific-ai
  - efficient-ai
---

### 1. Continual Learning Mechanisms Compose for Long-Horizon Memorization
**Authors:** Zheyuan Zhang, Alvin Zhang, Daniel Khashabi, Tianmin Shu
**arXiv:** [arxiv.org/abs/2609.06986](https://arxiv.org/abs/2609.06986)
**Summary:** Language models may need to internalize information that arrives over time and retain it through many subsequent updates. To study this challenge, we introduce long-horizon memorization, a setting in which a model learns 100 query-answer tasks through continual supervised fine-tuning without retaining earlier training examples or receiving task identifiers at inference.
**Trending because:** 294 HuggingFace upvotes + finds that complementary continual-learning mechanisms compose for retention across 100 sequential tasks

---

### 2. AI for Games in the Foundation Model Era
**Authors:** Meng Luo, Yanlin Li, Hao Li, Hongzhan Lin, Pengfei Zhou, Tianjie Ju, Ran Zhang, Yeying Jin, Mong-Li Lee, Wynne Hsu
**arXiv:** [arxiv.org/abs/2609.16679](https://arxiv.org/abs/2609.16679)
**Summary:** Foundation models, alongside advances in learned game-world models, are reshaping AI across the game lifecycle. Beyond playing games, recent systems model players and game dynamics, support design and development, adapt player-facing experiences at runtime, and evaluate resulting artifacts.
**Trending because:** 113 HuggingFace upvotes + organizes foundation-model advances across the full game lifecycle

---

### 3. StepAudio 3 Realtime Technical Report
**Authors:** Bin Lin, Bo Zhao, Boyang Zhang, Boyong Wu, Chao Yan, Chen Geng, Chen Wu, Cheng Yi, Chengli Feng, Chenglin Zhu, Chengting Feng, Chengyuan Yao, Daijiao Liu, DanNi Wan, Daxin Jiang, Dongjian Li, Dongqing Pang, Fei Tian, Feng Tian, Future Li, Gang Yu, Guanglong Yang, Haoyang Zhang, Hongyuan Wang, Jia Peng, Jiahao Song, Jialong Xue, Jiamin Fan, Jiangjie Zhen, Jianzheng Gao, Jincheng Wen, Jinghua Liang, Jinglan Gong, Jun Chen, Li Xie, Liang Zhao, Lifang Zhang, Lingli Ji, Lun Cai, Min Xu, Peilin Li, Peng Yang, Pengfei Tan, Qingjian Lin, Qinxin Du, Ruijie Xiong, Runze Li, Shenghua Hu, Shengqian Qin, Shi Qiu, Siqi Tu, Siyi Zhou, Tianjiao Deng, Wanying Lu, Weiming Niu, Wen Sun, WenWen Qu, Xiangyu Zhang, Xianwei Zhang, Xiaosu Su, Xing Chen, Xinyu Liu, Xuerui Yang, Yan Wu, Yang Li, Yang Yang, Yechang Huang, Yibo Zhu, Yifan Zhang, Yinuo Yan, Youjun Chen, Yu Fu, Yu Luo, Yu Zhou, Yujie Chen, Yumang Wang, Yunzhou Ju, Yuxiang Yang, Yuxin Li, Yuxin Zhang, Zekai Liu, Zengwei Yao, Zhaoxin Yuan, Zhenwei Mou, Zhiquan Zhang, Zhiyue Wu, Zichao Li, Zichao Zhou, Ziqi Ren, Zixuan Wang
**arXiv:** [arxiv.org/abs/2609.14005](https://arxiv.org/abs/2609.14005)
**Summary:** We present StepAudio 3 Realtime, an audio-language foundation model organized around a continuous listen-converse-think-act loop. Crucially, we resolve the tension between deep deliberation and latency via Think-While-Speaking, executing private reasoning in parallel with spoken delivery.
**Trending because:** 101 HuggingFace upvotes + introduces real-time spoken interaction with parallel private reasoning and fluid turn-taking

---

### 4. The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement
**Authors:** Yi Duan, Ying Liu, Zirui Tang, Haodong Chen, Jun Zhou, Yumou Liu, Bangrui Xu, Yukai Wu, Sidi Chen, Yuhan Zhou, Haoyu Wang, Xiaoyou Yu, Shaokun Han, Xuzhou Zhu, Le Zhou, Bolin Lu, Wei Zhou, Jiachen Liu, Nuozhou Fang, Jiaxin Tian, Ruoyu Chen, Yuxuan Li, Kai Zuo, Kaiyan Zhang, Qianyu Yang, Zijie Wang, Jiantao Qiu, Conghui He, Guoliang Li, Bowen Zhou, Zhiyuan Liu, Zhoufutu Wen, Jihua Kang, Xuanhe Zhou, Fan Wu
**arXiv:** [arxiv.org/abs/2609.11873](https://arxiv.org/abs/2609.11873)
**Summary:** Recursive self-improvement (RSI) enables AI systems to turn experience and feedback into persistent changes that improve both their capabilities and the process of future improvement. We first use the Headroom-Closed Index (HCI) to reveal the problems of existing LLMs, then introduce the RSI concept and its development roadmap: from improvement-execution autonomy, improvement-strategy autonomy, experience-acquisition autonomy, and environment-adaptation autonomy, to recursive meta-improvement.
**Trending because:** 88 HuggingFace upvotes + lays out a roadmap from improvement execution to recursive meta-improvement

---

### 5. StepAudio 3 Music Technical Report
**Authors:** Chengli Feng, Zhiyue Wu, Jiahao Song, Zheqi Dai, Boyang Wang, Ruibin Yuan, Junming Gong, Wenxiao Zhao, Jing Guo, Gang Yu, Xiangyu Zhang, Xuerui Yang, Chao Yan
**arXiv:** [arxiv.org/abs/2609.16034](https://arxiv.org/abs/2609.16034)
**Summary:** We introduce StepAudio 3 Music, a large-scale, long-form music generation model that supports explicit musical planning and open-domain text-controlled generation. For explicit planning, a Mixture-of-Experts autoregressive model uses ABC notation to produce an intermediate arrangement plan (ABC-CoT) before predicting music tokens, making harmony, rhythm, and melodic structure part of the generation context.
**Trending because:** 76 HuggingFace upvotes + combines explicit musical planning with long-form text-controlled generation

---

### 6. ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments
**Authors:** Hejia Geng, Zesen Huang, Haoyang Li, Wenbin Li, Koutian Wu, Zihan Zhou, Yuanbo Pang, Weihao Liu, Zigong Xu, Zhiping Li, Zongzheng Zhang, Chuanfei Dong, Jiankai Sun, Tianzhe Zheng, Fengyu Xie, Yue Ma, Yueheng Shi, Tong Xie, Zonglin Di, Xianrong Liu, Qucheng Gao, Yimin Liu, Jiaming Pan, Sheng Huang, Xiao-Han Ma, Lanqing Yuan, Zhenlin Zhu, Ziang Liu, Ziyang Xu, Junkai Wang, Kangkai Liang, Jiayi Xian, Zehong Zhao, Liuwei Xu, Jingxu Xie, Peijin Zhang, Qiang Gao, Chengyi Xing, Zhe Zhao, Xi Wang, Yaopeng Xing, Xing Meng, Zhenfei Yin, Yingcheng Wu, Ling Yang
**arXiv:** [arxiv.org/abs/2609.19134](https://arxiv.org/abs/2609.19134)
**Summary:** Scientific code repositories encode decades of human knowledge in executable models, methods, and tools. We introduce ScienceIDE, infrastructure for turning the world's scientific code into programmable environments for scientific agents.
**Trending because:** 68 HuggingFace upvotes + turns scientific repositories into executable learning and evaluation environments for agents

---

### 7. Rethinking Critic Learning in PPO: Understanding and Mitigating Value Flattening
**Authors:** Yizhuo Li, Jianhao Yan, Yun Luo, Zhi Wang, Futing Wang, Rong-Xi Tan, Kanghui Tian, Ganqu Cui, Ning Ding, Peilin Zhao, Yafu Li, Yu Cheng
**arXiv:** [arxiv.org/abs/2609.18708](https://arxiv.org/abs/2609.18708)
**Summary:** However, we uncover a systematic failure mode in PPO critics, which we call Value Flattening: state values, estimated from multiple Monte Carlo continuations, change sharply across intermediate states while critic predictions remain comparatively flat. Motivated by these findings, we introduce SParse Proximal Policy Optimization (SP$^3$O), which applies the value loss to only a few well-separated states in each response to mitigate both effects.
**Trending because:** 58 HuggingFace upvotes + identifies critic Value Flattening and proposes sparse value supervision to mitigate it

---

### 8. Confidence Comes from Experience: Experiential Confidence Estimation from Reasoning to Agents
**Authors:** Caiqi Zhang, Xiaochen Zhu, Chengzu Li, Yulong Chen, Dharshan Kumaran, Nigel Collier
**arXiv:** [arxiv.org/abs/2609.17708](https://arxiv.org/abs/2609.17708)
**Summary:** Reliable confidence estimation is increasingly central to the trustworthy deployment of language models: a calibrated estimate of the probability that an output is correct decides what to ship, what to escalate, and what to retry. We propose XConf (eXperiential Confidence): estimating confidence together with the model's accumulated experience.
**Trending because:** 46 HuggingFace upvotes + grounds confidence estimates in a model’s own graded experience

---

### 9. ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE Tasks
**Authors:** Jeonghye Kim, Minseon Kim, Young Jin Kim, Matheus Pereira, Marc-Alexandre Côté, Alessandro Sordoni, Xingdi Yuan, Zhengyan Shi
**arXiv:** [arxiv.org/abs/2609.18805](https://arxiv.org/abs/2609.18805)
**Summary:** We introduce ProgramDistill, a benchmark evaluating coding agents on features discovered through interaction with fully functional reference applications. Our pipeline, mine-craft-patch, discovers 1,975 replay-verified behaviors across 26 applications and constructs 4,063 tasks without human intervention.
**Trending because:** 43 HuggingFace upvotes + converts interactive reference applications into thousands of verifiable software-engineering tasks

---

### 10. ActionPiece: Rethinking Action Tokenization for Autoregressive Vision-Language-Action Models
**Authors:** Shijie Lian, Bin Yu, Zhaolong Shen, Xiaopeng Lin, Yichao Du, Zhirui Zhang, Laurence T. Yang, Kai Chen
**arXiv:** [arxiv.org/abs/2609.18487](https://arxiv.org/abs/2609.18487)
**Summary:** We introduce physical rank consistency (PRC) to measure how well tokenization preserves local physical distance rankings after reconstruction. We further present ActionPiece, which preserves physical action relationships through joint supervision of representation learning and quantization.
**Trending because:** 36 HuggingFace upvotes + preserves relational fidelity when tokenizing actions for autoregressive robot policies

---

### 11. Agora: Git as Shared Memory for Collective AutoResearch
**Authors:** Yifan Zhang, Yunheng Zou, Shaokun Zhang, Jian Hu, Hao Zhang, Binfeng Xu, Jan Kautz, Yi Dong
**arXiv:** [arxiv.org/abs/2609.18094](https://arxiv.org/abs/2609.18094)
**Summary:** Agora is a shared memory for such agents: research is recorded as an append-only directed acyclic graph (DAG) stored in Git, so that every claim is a commit anyone can check out and rerun. We describe the system and report its first sustained use: a run of nearly 12 days in which 13 language-model workers, with no assigned tasks and no central planner, worked on a weight-transfer problem.
**Trending because:** 35 HuggingFace upvotes + uses a Git-backed research DAG as shared memory for autonomous research agents

---

### 12. VC-Attention: Value Smoothing and Softmax Casting for Low-bit Attention
**Authors:** Xingyang Li, Dongyun Zou, Shining Zhang, Jiacheng Chen, Haocheng Xi, Lvmin Zhang, Jun-Yan Zhu, Song Han, Zhekai Zhang, Yujun Lin, Muyang Li
**arXiv:** [arxiv.org/abs/2609.15810](https://arxiv.org/abs/2609.15810)
**Summary:** We propose VC-Attention, a training-free low-bit attention framework that addresses both by pairing Value smoothing with a fused probability Cast. V-Smooth reorders value tokens by lightweight online clustering, so the tokens in a hardware block quantize well together.
**Trending because:** 34 HuggingFace upvotes + pairs value smoothing with fused probability casting for accurate low-bit attention

---

### 13. EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents
**Authors:** Sehee Kim, Yumin Choi, Minki Kang, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2609.17632](https://arxiv.org/abs/2609.17632)
**Summary:** We introduce EvolveTrade, a self-evolving framework that treats the system prompt of a tool-using trading agent as a text-parameterized policy. After each update interval, a Policy Agent revises this policy using accumulated decision traces and realized portfolio feedback, while keeping the backbone LLM fixed.
**Trending because:** 30 HuggingFace upvotes + lets a trading agent refine its tool-use policy from realized portfolio feedback

---

### 14. Zing-0.5: Toward Playable Worlds with Real-Time Joint Action and Text Control
**Authors:** Mingyang Chen, Shengdong Chen, Xiaoxiao Fu, Bosheng Gong, Haoyuan Guo, Bowen Li, Jiawen Li, Kejun Li, Tianpeng Li, Yin Liu, Haoze Sun, Zeyang Tian, Meng Wang, Xinmiao Wu, Jiangqiao Yan, Zining Zhao
**arXiv:** [arxiv.org/abs/2609.17909](https://arxiv.org/abs/2609.17909)
**Summary:** We introduce Zing-0.5, a 5B autoregressive world model designed for playability: users can explore generated worlds, influence unfolding events, and respond to the resulting feedback through joint keyboard and online text control. Our approach brings together three technical contributions: (1) Unified action and text conditioning, combining magnitude-aware keyboard inputs with temporally aligned text instructions and jointly annotated videos to learn navigation and event control within the same sequence; (2) Event-scale supervision for incremental generation, using a segment-level teacher trained on connected multi-prompt videos to supervise a block-level causal student through distribution-matching distillation; and (3) Low-cost real-time interaction, combining four-step generation with context-preserving streaming to support 832 x 480 inference at 24 FPS at an estimated server rental cost of approximately USD 0.009 per stream-minute.
**Trending because:** 25 HuggingFace upvotes + enables 24-FPS generated worlds under joint keyboard and text control

---

### 15. HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses
**Authors:** Jieyuan Liu, Mengzhou Hu, Jefferson Chen, JungHo Kong, Pratibha Jagannatha, Yiming Gao, Dexter Pratt, Hsin-Yuan Lee, Zhiting Hu, Trey Ideker, Wei Wang, Eric P. Xing, Zhen Wang
**arXiv:** [arxiv.org/abs/2609.15938](https://arxiv.org/abs/2609.15938)
**Summary:** Scientific agents contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Building on this view, we introduce HypoEvolve, which makes collaboration explicit through successive updates to a hypothesis population.
**Trending because:** 24 HuggingFace upvotes + uses evolutionary multi-agent collaboration to improve scientific hypothesis discovery

---

### 16. SpectralShift: Effective Context Window Extension of Gated DeltaNet via Spectral Reparameterization
**Authors:** Zian Liu, Yiwen Hu, Zican Dong, Tian Xie, Wayne Xin Zhao, Yucheng Ding, Ran Tao, Bryan Dai
**arXiv:** [arxiv.org/abs/2609.14320](https://arxiv.org/abs/2609.14320)
**Summary:** In this work, we study long-context extension of Gated DeltaNet (GDN) from a spectral perspective of transition matrix and identify two essential factors governing long-range information retrieval: (1) a sufficiently broad slow spectral band aligned with the target dependency length, and (2) the preservation of fast-decaying modes for state clearing and context switching. Based on this observation, we propose SpectralShift, a spectral reparameterization approach for long-context continual pretraining of GDNs.
**Trending because:** 22 HuggingFace upvotes + extends Gated DeltaNet context windows through spectral reparameterization

---

### 17. A Zeroth-Order Paradigm for LLM Preference Alignment
**Authors:** Peter Chen, Xi Chen, Wotao Yin, Tianyi Lin
**arXiv:** [arxiv.org/abs/2609.19144](https://arxiv.org/abs/2609.19144)
**Summary:** In this paper, we propose and analyze Comparison-based Preference Optimization (ComPO), a zeroth-order alignment method based on comparison oracles. ComPO extracts directional information from these pairs without directly optimizing a differentiable preference loss on them.
**Trending because:** 22 HuggingFace upvotes + introduces comparison-oracle preference alignment without directly optimizing a differentiable preference loss

---

### 18. Gaze as Evidence for Common Grounding: A Cross-Corpus Analysis of MapTask and MUNDEX
**Authors:** Nan Li, Albert Gatt, Massimo Poesio
**arXiv:** [arxiv.org/abs/2609.18011](https://arxiv.org/abs/2609.18011)
**Summary:** Working from discrete behavioral annotations, we map HCRC MapTask (Anderson et al., 1991) and MUNDEX (Türk et al., 2023) into a shared partner/task/away vocabulary and compute gaze features around task-relevant dialogue units. In both corpora, aligned reference interpretations (MapTask) and UND (understood) judgments (MUNDEX) are associated with more task-directed gaze and with less partner-directed gaze, lower gaze entropy, and fewer gaze transitions.
**Trending because:** 22 HuggingFace upvotes + finds cross-corpus gaze signals associated with conversational grounding

---

### 19. EventEgoHands++: Event-based Egocentric 3D Hand Mesh Reconstruction with Real Dataset
**Authors:** Ryosei Hara, Wataru Ikeda, Masashi Hatano, Mariko Isogawa
**arXiv:** [arxiv.org/abs/2609.17189](https://arxiv.org/abs/2609.17189)
**Summary:** In this paper, we propose EventEgoHands++, a framework for event-based 3D hand mesh reconstruction from an egocentric viewpoint. To train and evaluate our framework, we extend the synthetic N-HOT3D dataset and newly construct EEH-R, the largest real-world event-based egocentric hand dataset to date, comprising approximately 1M annotated frames captured in environments including low-light conditions.
**Trending because:** 21 HuggingFace upvotes + adds instance-aware event-camera hand reconstruction and a million-frame real-world dataset

---

### 20. ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents
**Authors:** Shuhan Xue, Jianyuan Zhong, Ziyuan Nan, Wenbin Li, Zhaochen Yu, Jinchao Ding, Qiang Gao, Pengyu Zhan, Yuntong Zhang, Tian Cheng, Zhenfei Yin, Yingcheng Wu, Ling Yang
**arXiv:** [arxiv.org/abs/2609.17523](https://arxiv.org/abs/2609.17523)
**Summary:** We introduce and release ScienceBuddy, an interactive scientific research workspace that brings continually improving scientific agents into researchers' everyday workflows. At its core is recursive-in-recursive self-improvement, a paradigm that couples harness evolution with model reinforcement learning: the inner recursion improves the harness with the model fixed, while the outer recursion trains the model under the improved harness.
**Trending because:** 20 HuggingFace upvotes + couples harness evolution with model reinforcement learning for continually improving scientific agents
