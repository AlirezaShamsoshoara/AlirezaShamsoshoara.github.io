---
title: "Daily AI Papers — November 03, 2026"
date: 2026-11-03
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-03/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - video-generation
  - embodied-ai
---

### 1. Wave Forcing: Towards Speed-of-Light Streaming Video Generation
**Authors:** Yijie Jin, Yuxuan Liu, Jiajun Xu, Ye Huang, Chuzhi Wang, Jiayang Li, Ruiyang Chen, Chenling Hong, Xu Wang, Zhijie Deng
**arXiv:** [arxiv.org/abs/2611.00859](https://arxiv.org/abs/2611.00859)
**Summary:** Wave Forcing co-designs causal denoising, training, and a pipelined runtime to emit continuous video chunks while preserving appearance and motion over long rollouts. The authors report 134.8 end-to-end frames per second for four-step generation on eight H200 GPUs, with five-step generation maintaining overall quality comparable to Rolling Forcing.

---

### 2. CUA-Master: Scaling Computer-use Agents through Open-World Recursive Improvements
**Authors:** Xinlei Yu, Gen Li, Ji Zhao, Zhangquan Chen, Congcong Wang, Shuai Dong, Zelin Peng, Yuqi Xu, Hongrui Wu, Kaiwen Tuo, Cheng Yang, Kaituo Feng, Yifan Wu, Jiayi Zhang, Dongming Wu, Wenqi Shao, Jiaqi Wang, Xiangyu Yue
**arXiv:** [arxiv.org/abs/2611.03126](https://arxiv.org/abs/2611.03126)
**Summary:** CUA-Master uses nested recursive-improvement loops that turn instructional videos into reusable task primitives and collect verified computer-use trajectories with feedback-guided snapshot rollback. Its 27B model reports scores of 80.2 on OSWorld Verified and 36.9 on OSWorld 2.0, alongside continued gains across recursive iterations.

---

### 3. CoworkOS:Scaling Agent Coworkers for Real-world Automation
**Authors:** Jiajie Jin, Guanting Dong, Chengjun Pan, Xin Deng, Zhuohui Sheng, Guoqiang Wang, Tao Gui, Yutao Zhu, Yujia Chen, Shihong Yi, Binze Hu, Zhixiong Yang, Zhichao Sun, Rui Wang, Han Han, Mingyu Ma, Junhao Huang, Xiaotao Wang, Huicheng Jiang, Yuyang Hu, Xinyu Yang, Wanghan Xu, Yajie Yang, Zhecan Wang, Honglin Guo, Xiaoyu Xing, Xiaoqian Zhang, Yulun Zhu, Xiaoxi Li, Jiahang Lin, Shaofan Liu, Shihan Dou, Zhiheng Xi, Qi Zhang, Yu-Gang Jiang, See-Kiong Ng, Yang Zhang, Tat-Seng Chua, Ji-Rong Wen, Zhicheng Dou
**arXiv:** [arxiv.org/abs/2611.03178](https://arxiv.org/abs/2611.03178)
**Summary:** CoworkOS separates agent strategy from execution management, combining asynchronous delegation, shared editable artifacts, hierarchical workspaces, and persistent memory for long-horizon automation. The authors evaluate it across twelve benchmarks and six application categories, and report a sustained post-training case study that improves average performance across eight benchmarks from 33.19 to 42.95 over five rounds.

---

### 4. Advances in Agentic Computer Graphics
**Authors:** Hengyu Liu, Jihyeon Je, Ruiqi Wang, Mingxuan Wu, Haven Feng, Qixing Huang, Georgios Pavlakos, Hao Zhang, Jiajun Wu, Maneesh Agrawala, Leonidas Guibas, R. Kenny Jones, Shangzhe Wu, Guandao Yang
**arXiv:** [arxiv.org/abs/2611.01860](https://arxiv.org/abs/2611.01860)
**Summary:** This report introduces a unified taxonomy for LLM-agent systems that generate and refine code across diverse computer-graphics tasks, together with an agentic literature-analysis system. It maps emerging trends and challenges in tool coordination, human-agent interfaces, long-horizon refinement, and reliable evaluation of interactive graphics systems.

---

### 5. Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement
**Authors:** Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu, Weijia Mao, Rui Zhao, Weijia Wu, Guian Fang, Yanzhe Chen, Zeyu Zhu, Yuxin Jiang, Yiren Song, Yuchao Gu, Junchao Yi, Qi Hu, Dan Kong, Alex Jinpeng Wang, Kevin Qinghong Lin, Mike Zheng Shou, Wei Liu
**arXiv:** [arxiv.org/abs/2610.40191](https://arxiv.org/abs/2610.40191)
**Summary:** This report examines agent harnesses as runtimes that coordinate context, tools, state, feedback, and budgets around video-generation models and interactive world models. It connects agentic video production, hybrid programmable world control, and recursive self-improvement, while identifying challenges in memory, evaluation, provenance, and cost accounting.

---

### 6. Democratizing Robot-Use Agents: A Unified Harness with Open Models
**Authors:** Jiarui Yuan, Yuxin Zuo, Xiaoyu Huang, Wenbo Zhang, Kwanyoung Park, Junlin Yang, Tianxiang Zhang, Ruoqu Chen, Yutao Ouyang, Bingxiang He, Xingtai Lv, Hongjin Wu, Jiajun Liu, Jiahao Zhao, Tianwei Luo, Haozhan Li, Cheng Qian, Jiaxin Ge, Huan-ang Gao, Kaisen Yang, Jiaqi Deng, Qixin Xu, Siqiao Huang, Bowen Zhou, Mengdi Xu, Zhiyuan Liu, Pieter Abbeel, Ning Ding
**arXiv:** [arxiv.org/abs/2611.01560](https://arxiv.org/abs/2611.01560)
**Summary:** The uni-robot-agent harness enables open-weight robot-use agents to perform zero-shot manipulation without privileged inputs and supports further training. An out-of-the-box Qwen3.8-Flash-Next reaches a RoboDojo score of 31.39 and performs competitively on nineteen real-world tasks, while analysis links effective robot use to four general capabilities.

---

### 7. SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training
**Authors:** Ziming Li, Lu Yu, Jiatan Huang, Qing Cui, Jun Zhou, Chuxu Zhang
**arXiv:** [arxiv.org/abs/2611.02074](https://arxiv.org/abs/2611.02074)
**Summary:** SWE-Trail uses earlier coding trajectories to guide checkpointed exploration and select subsequent collection routes without exposing historical advice to the coding agent. Training a 124B student on its collected data improves mean resolution over independent sampling by 2.33 percentage points on SWE-bench Multilingual and 1.60 points on SWE-bench Pro.

---

### 8. NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale
**Authors:** Chaoyun Zhang, Bingxuan Li, Pinxue Guo, Yangfan Gao, Zikun Cai, Tianci Xie, Hui Li, Yuqi Huang, Yifei Cao, Bo Mao, Tian Tang, Qichang Zheng, Tongtong Liu, Xiaoxing Wang, Jinxiu Liu, Lizhi Lin, Zhou Shao, Maosen Zhou, Miao Zheng, Shuo Zhang, Yangji He, Kepeng Lei, Ning Zhao, Wei Shen, Zhenjiang Jin, Xinyue Zhang, Peng Sun, Zhenhua Han, Rui Zheng, Hang Yan
**arXiv:** [arxiv.org/abs/2611.02102](https://arxiv.org/abs/2611.02102)
**Summary:** NorthCUA closes an experience flywheel between executable task generation, a long-horizon harness, verified trajectory curation, staged learning, and joint desktop-web reinforcement learning. The authors report leading open-source results for its Nano, Mini, and Pro models under their evaluation settings, with an Ultrafast variant offering a measured web-workflow quality-latency tradeoff.

---

### 9. Follow the Gradient: Tracing Safety Degradation Back to Training Data
**Authors:** Saket Reddy, Amro Abbas, Anshuman Suri, Ari Morcos, David Schwab, Pratyush Maini
**arXiv:** [arxiv.org/abs/2610.37481](https://arxiv.org/abs/2610.37481)
**Summary:** SimpleLoRIF identifies apparently benign fine-tuning examples whose gradients align with unsafe behavior, using low-rank embeddings and backpropagation restricted to the final four transformer blocks. Removing the most unsafe-aligned twenty percent of Tulu 3 examples produces SafeTulu, which reduces reported GCG attack success by up to 22 percent while largely preserving or improving capability.

---

### 10. Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay
**Authors:** Byeonghun Bang, Sangwoo Park, Jinheon Baek, Kangsan Kim, Youngwan Lee, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2610.27954](https://arxiv.org/abs/2610.27954)
**Summary:** ReTrace evaluates computer-use-agent recovery by injecting controlled errors and checking whether goal-oriented action replay yields the same downstream outcomes as the target state. Its study finds that current agents underuse their latent recovery capabilities and that accurate model-based recovery can improve end-to-end task completion.

---

### 11. PhotoGuider: Composition-Aware Cropping and 360$^{\circ}$ View Framing with Explainable Photographic Assessments
**Authors:** Yuan-Kang Lee, Kuan-Lin Chen, Chia-Che Chang, Yu-Lun Liu
**arXiv:** [arxiv.org/abs/2611.02897](https://arxiv.org/abs/2611.02897)
**Summary:** PhotoGuider combines learned composition-aware scorers with a multimodal explainer to select viewing directions in panoramic scenes and refine image crops with photographic assessments. It reports the highest average intersection-over-union on two cropping benchmarks and first-place preferences in 53.2 percent of a blind panoramic-framing study.

---

### 12. Reviso: Not All Visual Evidence Deserves Equal Attention in Video Captioning
**Authors:** Tengfei Liu, Yang Shi, Yuran Wang, Yuqi Tang, Yizhuo Jia, Zhuoran Zhang, Qixun Wang, Shujie Li, Xuanyu Zhu, Xinyu Liu, Minghui Guo, Shixuan Liu, Haotian Wang, Yuanxing Zhang, Pengfei Wan
**arXiv:** [arxiv.org/abs/2611.03602](https://arxiv.org/abs/2611.03602)
**Summary:** Reviso plans hierarchical video observations from a global preview, then selectively revisits segments and uses tools to gather evidence for important caption facts. Verification-guided trajectory construction and GRPO rewards improve performance over evaluated open-source baselines across four captioning benchmarks, while the generated captions also support downstream video question answering.

---

### 13. When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?
**Authors:** Anton Hristov, Aleksandar Slavov, Vasil Vasilev
**arXiv:** [arxiv.org/abs/2611.01815](https://arxiv.org/abs/2611.01815)
**Summary:** This paper separates physical information in frozen video representations from the factors that drive native prediction error across IntPhys2, Physion++, and simulated Kubric events. It finds that appearance changes, static clips, and ordinary prediction difficulty can confound error signals, so representing physical information does not make prediction error a reliable measure of physical surprise.

---

### 14. From Fragmentation to Fusion: A Survey and Roadmap for Omnimodal Embeddings
**Authors:** Ziyin Zhang, Yuyu Guo, Ying Zhang, Siqiao Xue, Zihan Liao, Jin Qin, Wenjie Yang, Siyuan Yang, Shijie Li, Cheng Chen, Hao Wu, Zhaoyang Zhu, Ruipeng Li, Zhaokun Jiang, Lei Lei, Rui Wang, Hang Yu, Rui Wang
**arXiv:** [arxiv.org/abs/2611.00172](https://arxiv.org/abs/2611.00172)
**Summary:** This position paper argues that embedding research across modalities is converging around shared learning principles despite fragmented communities and modality-specific challenges. It proposes coverage, comparability, and compositionality as progressively harder capabilities, mapping transformation, alignment, and joint embedding onto a roadmap toward omnimodal representations.

---

### 15. CrossSWE: Benchmarking Cross-Repository Joint Development for Coding Agents
**Authors:** Silin Chen, Yuling Shi, Heng Lian, Zihan Zhang, Xiaodong Gu, Haotian Lin, Zhensu Sun
**arXiv:** [arxiv.org/abs/2611.01484](https://arxiv.org/abs/2611.01484)
**Summary:** CrossSWE benchmarks coordinated software changes across interdependent repositories using 171 real-world instances covering 165 repositories, twenty domains, and thirteen programming languages. Among five evaluated LLMs, the strongest reaches 58.48 percent Pass@1, with cross-repository inconsistencies accounting for the most prevalent failure mode.

---

### 16. Diagnosing the Reference Gap: What Visual Scaffolds Can and Cannot Fix in Multimodal Reasoning
**Authors:** Guizhen Chen, Weiwen Xu, Wotao Yin, Anh Tuan Luu, Hou Pong Chan
**arXiv:** [arxiv.org/abs/2610.39419](https://arxiv.org/abs/2610.39419)
**Summary:** ReGap-Bench isolates a reference gap in multimodal reasoning by holding visual scenes, questions, and answers fixed while varying external references such as object numbering. Task-matched references improve accuracy by up to 25 percent, whereas mismatched scaffolds offer little benefit or can hurt, suggesting a training-free visual skill distinct from better perception.

---

### 17. Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents
**Authors:** Zheng Wu, Xinbei Ma, Yao Yao, Zhaoyuan Huang, Haowen Hu, Yijie Lu, Taolei Wang, Yifei Yang, Wuyue Xiong, Pengzhou Cheng, Zhuosheng Zhang
**arXiv:** [arxiv.org/abs/2611.03092](https://arxiv.org/abs/2611.03092)
**Summary:** Avatar Intelligence proposes persistent personal agents that represent user goals, values, and constraints across contexts while preserving human control over consequential decisions. The paper introduces an Agentic Oversight Index and a maturity roadmap, emphasizing continuous personalization, user-situated evolution, and accountable safety mechanisms.

---

### 18. FLAMIA: FLAsh MIcroscaling Attention for Fast and Causally Safe Training on Blackwell
**Authors:** Fedor Velikonivtsev, Mikhail Koltakov, Denis Kuznedelev
**arXiv:** [arxiv.org/abs/2611.03344](https://arxiv.org/abs/2611.03344)
**Summary:** FLAMIA provides Blackwell attention kernels with MXFP8 and mixed NVFP4/FP8 paths, combining reusable token-block scaling, causal-leakage safeguards, consistent gradients, and packed-document scheduling. Its MXFP8 path reports combined forward-and-backward speedups of 1.10 to 1.40 times on B200 and 1.06 to 1.42 times on B300 against the fastest evaluated workload baselines, with training stability validated on Llama-style pretraining.

---

### 19. Order-Only On-Policy Distillation
**Authors:** Guangzeng Han, Yu Wu, Xiaolei Huang
**arXiv:** [arxiv.org/abs/2611.02112](https://arxiv.org/abs/2611.02112)
**Summary:** Order-Only On-Policy Distillation trains students to reproduce the ordering of a teacher's top candidate tokens rather than its probability values, making the objective invariant to teacher temperature. Across six teacher-student pairs it beats conventional on-policy distillation on average over three math benchmarks in every pair, with gains up to 2.9 points.

---

### 20. IdeaTaste: Do LLMs Share the Research Taste of Human Researchers?
**Authors:** Shanshan Zhong, Chen Xu, Jingjie Ning, Zhengzhong Liu, Aviral Kumar, Chenyan Xiong
**arXiv:** [arxiv.org/abs/2611.03424](https://arxiv.org/abs/2611.03424)
**Summary:** IdeaTaste compares LLM research proposals from a frozen literature snapshot with the papers that human communities subsequently publish, spanning six models, four areas, and more than ninety thousand proposals. Agents reach about 26 percent of the human citation-matching level and 18 percent of idea matching, revealing a larger weakness in concrete research approaches than in identifying broad directions.
