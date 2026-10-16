---
title: "Daily AI Papers — October 16, 2026"
date: 2026-10-16
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-16/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - multimodal-ai
  - spatial-reasoning
---

### 1. OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding
**Authors:** Xuyang Liu, Shihao Wang, Xinyu Wei, Minghan Li, Zeqing Wang, Zuhao Yang, Zichen Wen, Lei Zhang
**arXiv:** [arxiv.org/abs/2610.18829](https://arxiv.org/abs/2610.18829)
**Summary:** OmniCompass evaluates when, where, and what happens in video through temporal grounding, spatial grounding, and question answering, with separate vision-language and joint audio-visual tracks. Testing 50 multimodal models on manually verified data reveals persistent weaknesses in precise grounding, paired target consistency, and especially audio-visual understanding among open models.

---

### 2. Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation
**Authors:** Bingxi Hou, Guochao Jiang, Guofeng Quan, Weiqing Li, Wenfeng Feng, Guohua Liu, Yuewei Zhang
**arXiv:** [arxiv.org/abs/2610.21601](https://arxiv.org/abs/2610.21601)
**Summary:** Waypoint-OPD uses an intermediate checkpoint from a teacher's reinforcement-learning run to measure whether early and late policy shifts agree on student-visited prefixes. Gating endpoint distillation by that agreement gives the best domain-average result in all six tested mathematical and code-reasoning settings while requiring only one extra frozen-teacher scoring pass.

---

### 3. OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use
**Authors:** Hanzhang Zhou, Long Li, Quyu Kong, Lei Wang, Panrong Tong, Long Chen, Tianyu Xia, Gongjie Zhang, Xu Zhang, Chen Liu, Jianan Zhang, Chenglin Cai, Zhengwen Zeng, Steven Hoi, Yue Wang
**arXiv:** [arxiv.org/abs/2610.22200](https://arxiv.org/abs/2610.22200)
**Summary:** OpenGCUA releases an open stack for generalist computer-use agents that choose among visual and programmatic interfaces, including prompts, trajectories, a real-device harness, and a cross-device SDK. Across eight models on OSWorld-v2, its full setup raises the mean partial score by 19.6 points and cuts reported steps by 53.0% relative to batched GUI-only execution.

---

### 4. FDE-Gym: The Last Mile of AI Delivery
**Authors:** Dongxu Yang, Hongda Yan, Renxin Wang, Baoli Zhang, Haojia Zuo, Ying Zhao, Youmin Chen, Xiaojian Liao, Congming Gao, Tianyang Jiang, Yixiao Chen, Qing Wang, Zhiguo Yu, Xiaqing Li, Yuhao Zhang, Jiawen Sun, Renzhe Xu, De Mi, Tiancheng Wu, Xianya Fu, Xuanlu Zhao, Bo Feng, Meixuan Ren, Guanming Lin, Ziheng Zhou, Xinhua Wang
**arXiv:** [arxiv.org/abs/2610.22350](https://arxiv.org/abs/2610.22350)
**Summary:** FDE-Gym measures whether agents can deliver working systems from ambiguous customer needs through 95 tasks drawn from 20 scenarios and 18 sectors. In its realistic setting, the best configuration averages 0.56 and resolves only 14 tasks, showing that discovering unstated constraints and converting them into business impact remain major bottlenecks.

---

### 5. RoTA-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection Alignment
**Authors:** Qingchuan Ma, Yuexiao Ma, Xiang Meng, Yixuan Zou, Tianyu Xie, Wang Chen, Yuhui Zeng, Yuhang Wu, Xiawu Zheng, Rongrong Ji
**arXiv:** [arxiv.org/abs/2610.17665](https://arxiv.org/abs/2610.17665)
**Summary:** RoTA-Bench tests interactive 3D reasoning by asking models to rotate objects until their 2D projections match target silhouettes within a limited action budget. Its 674 tasks expose a large control gap: GPT-5.6-Sol succeeds on 17% of the test set while undergraduate participants complete it with 100% success.

---

### 6. Self-Evolving Agent Harness
**Authors:** Chuyang Wei, Haoxiang Guan, Minghang Zhu, Kexin Zhou, Jiyan He, Xiren Zhou, Huanhuan Chen, Yifei Shen
**arXiv:** [arxiv.org/abs/2610.18813](https://arxiv.org/abs/2610.18813)
**Summary:** This work formalizes self-evolving agent harnesses that persistently revise prompts, memory, workflows, tools, code, and plugins while model weights stay fixed. It develops reliability bounds and admission rules for accepted revisions, then argues that continual validation and independent safeguards are necessary as tasks, evaluators, and runtime privileges change.

---

### 7. MJev-Spatial: System One Spatial Intelligence via Native Attention Matching
**Authors:** Luozheng Qin, Yuhan Zhu, Changhai Zhou, Qian Qiao, Jun Gao, Yuhua Zhou, Harry Zhang, Xiangyu Zeng, Yuxuan Liu, Kaijie Chen, Andrew Chen, Pony Ma
**arXiv:** [arxiv.org/abs/2610.22276](https://arxiv.org/abs/2610.22276)
**Summary:** MJev-Spatial reframes choice, scalar, and point-based spatial tasks as parameter-free classification using a vision-language backbone's pretrained attention projections. The Qwen3.5-4B system leads seven of twelve benchmarks, beats its autoregressive base on all twelve, and runs 5.6 times faster by producing no answer tokens.

---

### 8. Learning Where to Split: Dynamic Band Splitting for Audio Source Separation
**Authors:** Bingzhe Zhang, Kai Li, Xiaolin Hu
**arXiv:** [arxiv.org/abs/2610.14993](https://arxiv.org/abs/2610.14993)
**Summary:** Dynamic Band Splitting learns content-conditioned frequency boundaries for each audio mixture while holding the band-token budget fixed. The method improves several separator backbones across three datasets, including a 29.0% relative average SI-SDR gain for DBS-BSRNN on DnR v2.

---

### 9. InfiniSplat v2: Analyzing and Improving Feed-Forward 3DGS from Any Views
**Authors:** Yongzhen Hu, Hao Yu, Jiawei Wang, Xianming Zeng, Jianyun Xu, Xingliang Liu, Ruizhen Hu, Xiaowei Zhou, Hujun Bao, Sida Peng
**arXiv:** [arxiv.org/abs/2610.20341](https://arxiv.org/abs/2610.20341)
**Summary:** InfiniSplat v2 improves feed-forward Gaussian scene reconstruction by freezing geometry, separating geometry from attribute prediction, aligning Gaussians with ground-truth poses during training, and supervising large-angle target views. One trained model reaches state-of-the-art mean LPIPS and DISTS across six datasets in both pose-conditioned and pose-free settings.

---

### 10. 3DCodeVerse: Exploring 3D Worlds as Code
**Authors:** Yipeng Gao, Ziyao Zeng, Jinfa Huang, Yijiang Li, Haolin Xiong, Wang Qin, Xinlei Yu, Youheng Yao, Jie Zhang, Kun-Yu Lin, Rong Liu, Yinyuan Zhao, Yajie Zhao, Meiqi Guo, Jiebo Luo, Lei Shu, Yunhao Ge, Xinyu Hu, Laurent Itti
**arXiv:** [arxiv.org/abs/2610.22341](https://arxiv.org/abs/2610.22341)
**Summary:** 3DCodeVerse combines two million executable 3D programs, an automated multi-agent coding harness, and empirical guidance for generating editable and verifiable 3D content. Fine-tuning on the dataset improves open models, while the harness uses execution, spatial, and visual checks to achieve a 90% human-evaluation win rate against Claude Design's 3D Object workflow.

---

### 11. MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training across Mobile and Computer Environments
**Authors:** Panrong Tong, Quyu Kong, Pengxiang Li, Tianyu Xia, Hanzhang Zhou, Lei Wang, Chenglin Cai, Long Li, Long Chen, Jianan Zhang, Zhengwen Zeng, Xu Zhang, Gongjie Zhang, Yue Wang, Steven Hoi
**arXiv:** [arxiv.org/abs/2610.20939](https://arxiv.org/abs/2610.20939)
**Summary:** MAI-Gym unifies GUI-agent evaluation, data collection, and online reinforcement learning across mobile, computer, and web environments with support for 20,000 parallel instances. Its 9B model reaches 78.4% on MobileWorld and 76.2% on OSWorld-Verified, while reinforcement learning in a mocked app transfers to a physical phone.

---

### 12. SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image Generation
**Authors:** Yufei Jiao, Jinfa Huang, Zeyue Xue, Tianyu Xie, Yuexiao Ma, Rongrong Ji, Xiawu Zheng, Jiebo Luo
**arXiv:** [arxiv.org/abs/2610.22264](https://arxiv.org/abs/2610.22264)
**Summary:** SCOPE groups prompt-rewriter tokens into semantic spans and shares a GRPO update coefficient within each span without adding rewards or image renders. Across three image generators, it improves over vanilla GRPO by 9.48% on GeneVal and 7.62% on T2I-CompBench.

---

### 13. Speculative Forcing for Efficient Autoregressive Video Generation
**Authors:** Hyunwook Choi, Seungryong Kim, Dongyoon Han, Sangdoo Yun
**arXiv:** [arxiv.org/abs/2610.22347](https://arxiv.org/abs/2610.22347)
**Summary:** Speculative Forcing treats intermediate video tokens as drafts, verifies when each can be accepted, and stops denoising accepted tokens while retaining their cached context. It preserves full-step quality across short video, long video, and world generation while accelerating LongLive by more than 1.5 times and Lingbot-World 2.0 by 1.35 times.

---

### 14. VLA-Δ: Learning Physical State Transition for Vision-Language-Action Models
**Authors:** Qi Lu, Jiarun Li, Ce Zhang, Miao Pan, Yi Pan, Xu Wang, Wenqi Zhang, Xuhong Zhang
**arXiv:** [arxiv.org/abs/2610.21306](https://arxiv.org/abs/2610.21306)
**Summary:** VLA-Delta explicitly trains vision-language-action models to predict the physical changes between current and future states rather than only observation-action mappings. Its large-scale state-transition supervision adds no inference overhead, matches leading results on LIBERO and RoboTwin, and beats pi-0.5 in real-robot experiments.

---

### 15. Mosaic: Multi-Session Agentic Reinforcement Learning
**Authors:** Yilong Xu, Minrui Xu, Xinyu Zhou, Xiang Long, Haochen Tan, Zhijiang Guo
**arXiv:** [arxiv.org/abs/2610.22174](https://arxiv.org/abs/2610.22174)
**Summary:** Mosaic extends agentic reinforcement learning to trajectories spanning multiple sessions, including those created by context compaction and subagent forking. Its critic-free hierarchy estimates session usage and marginal contribution, outperforming trajectory-wide advantage broadcasting on BrowseComp while using fewer sessions.

---

### 16. Intern Lumina U2: A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding and Image Generation
**Authors:** Qian Yu, Zongyang Qiu, Juncheng Yan, Hongliang Li, Qi Qin, Keqi Wang, Siqi Luo, Junkui Ju, Yapeng Mi, Tiantian Lu, Tian Liu, Pengyu Xie, Chenhao Ji, Minghui Zhang, Yiang Zhao, Siyu Yan, Haiying Xu, Yanbo Wang, Jianghan Shen, Yuandong Pu, Jiayi Lei, Borui Zhang, Jinxin Shi, Bo Zhang, Yuhang Zang, Shenglong Ye, Lixin Gu, Hongjie Zhang, Linghan Liu, Xinyuan Chen, Yuewen Cao, Lihe Zhang, Xiaohong Liu, Junjun He, Qiangwei Liu, Qi Zhang, Yu Cheng, Tianfan Xue, Hui Xiong, Chang Xu, Yu Qiao, Yihao Liu, Bin Fu
**arXiv:** [arxiv.org/abs/2610.20818](https://arxiv.org/abs/2610.20818)
**Summary:** Intern Lumina U2 represents each visual position with complementary discrete codebooks inside a diffusion language model that also handles text. Its unified backbone supports image, video, and 3D understanding and generation, and a stability-aware sampler speeds image generation by 4.45 times.

---

### 17. AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning
**Authors:** Bingxiang He, Pengqi Sun, Shihao Peng, Shaoxuan Li, Huiyu Xiao, Hongjian Shi, Zixuan Fu, Ziqing Qiao, Yuxin Zuo, Cheng Qian, Xinqiang Yu, Jiayi Li, Xiusi Chen, Yizhen Song, Xiangyang Wang, Iofai Lei, Yudong Wang, Ning Ding, Zhiyuan Liu, Xiaozhi Wang, Chaojun Xiao
**arXiv:** [arxiv.org/abs/2610.22194](https://arxiv.org/abs/2610.22194)
**Summary:** AutoSFT gives agents a broad data-engineering action space for changing proportions, pruning, repairing, replacing, and synthesizing supervised fine-tuning data. Separating execution from analysis, collecting independent proposals, and invoking synthesis yields attributable gains on instruction following and code generation over a single-agent loop.

---

### 18. DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding
**Authors:** Boyuan Sun, Deshui Miao, Wenzhao Gao, Shaoyong Jia, Shaohui Jiao, Chi Liu, Yan Shu, Derek Li, Bryan Dai, Shengsheng Qian, Qibin Hou
**arXiv:** [arxiv.org/abs/2610.19849](https://arxiv.org/abs/2610.19849)
**Summary:** DeltaStreamer records visual changes in structured memory before a query arrives, then plans retrieval and targeted replay after seeing the question. This combination recovers omitted evidence and reaches 66.07% on OVO-Bench and 59.53% on StreamingBench.

---

### 19. Orbia: Do Generated Videos Form a Consistent 3D World?
**Authors:** Dongyue Lu, Guian Fang, Hur Lim, Yonggang Wu, Yanrong Wang, Hongshan Chen, Shengju Qian, Yue Liao, Wei Chow, Lingdong Kong, Tianxin Huang, Yu Yang, Hongji Yang, Junchao Huang, Ao Liang, Yihao Wang, Zihan Wang, Rong Li, Hanlin Chen, Xin Wang, Wei Tsang Ooi, Mike Zheng Shou, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2610.20693](https://arxiv.org/abs/2610.20693)
**Summary:** Orbia systematically evaluates whether interactive video world models preserve input geometry, retain generated content, and maintain cross-view 3D consistency during exploration and revisits. Its 720 indoor and outdoor instances test 27 text-, action-, and camera-conditioned models, including minute-long trajectories for long-term consistency.

---

### 20. WorldCast: Exploring Intelligent Visual Generation in World State Prediction
**Authors:** Wenhao Yan, Haodong Li, Xiaotong Li, Yaxin Luo, Zhengrong Yue, Jialv Zou, Xu Huang, Haojin Yang, Nan Jia, Yan Feng, Peng Pei, Xunliang Cai
**arXiv:** [arxiv.org/abs/2610.20731](https://arxiv.org/abs/2610.20731)
**Summary:** WorldCast evaluates multi-step prediction of future visual world states from multimodal observations and references through 320 cases in eight categories. Tests of twelve models reveal wide gaps, with the strongest system scoring 72.8, Nano Banana Pro 42.8, and the best open model 20.1.

---
