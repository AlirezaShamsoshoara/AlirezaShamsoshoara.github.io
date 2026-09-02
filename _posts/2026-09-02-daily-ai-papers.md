---
title: "Daily AI Papers — September 2, 2026"
date: 2026-09-02
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-02/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-systems
  - multimodal-models
  - embodied-ai
---

### 1. StudentSim: Training LLM-based Student Simulators
**Authors:** Ke Yang, Chenglong Wang, Michel Galley, Chandan Singh, Jeevana Priya Inala, ChengXiang Zhai, Jianfeng Gao
**arXiv:** [arxiv.org/abs/2609.01591](https://arxiv.org/abs/2609.01591)
**Summary:** AI tutors are most useful when they adapt to each student's strengths, weaknesses, and preferred guidance, but evidence about which guidance works for which student is sparse, slow, and costly to collect from real learners. Student simulators can provide this signal as a proxy, yet existing approaches are limited: state-tracking models fit student behavior but struggle to process explanations or corrections, while LLM role-play follows guidance fluently but does not reliably match the competence of the student being imitated.
**Trending because:** 484 HuggingFace upvotes + strong interest in realistic student simulation for adaptive AI tutoring

---

### 2. Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving
**Authors:** Xin Zhou, Zongchuang Zhao, Zhibo Yang, Mingsheng Li, Humen Zhong, Shuai Bai, Du Chu, Ruizhe Chen, Zhaohai Li, Jun Tang, Qiuyue Wang, Mingkun Yang, Jiazhao Zhang, Dayiheng Liu, Dingkang Liang, Xiang Bai
**arXiv:** [arxiv.org/abs/2609.00111](https://arxiv.org/abs/2609.00111)
**Summary:** We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving. Qwen-Drive-1.0 retains the architecture of the pretrained vision-language model (VLM) and integrates 3D perception, visual question answering, and motion planning within a unified framework.
**Trending because:** 377 HuggingFace upvotes + a major vision-language foundation model for autonomous driving

---

### 3. SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers
**Authors:** Shaowen Wang, Ge Zhang, Kairong Luo, Yuhao Wu, Shaofan Liu, Jiaheng Liu, Wenhao Huang, Shen Yan, Jian Li
**arXiv:** [arxiv.org/abs/2609.01343](https://arxiv.org/abs/2609.01343)
**Summary:** Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs. We study looping on Mixture-of-Experts Transformers while closely matching per-token FLOPs, total non-embedding parameters, and KV cache.
**Trending because:** 99 HuggingFace upvotes + compute-matched scaling laws clarify the value of looped MoE architectures

---

### 4. UI-Venus-2 Technical Report
**Authors:** Venus Team, Zhuohan Cai, Haoxing Chen, Jiaxuan Chen, Weizhi Chen, Changlong Gao, Zhangxuan Gu, Yuan Guo, Yusong Hu, Jianrong Jiang, Jianguo Li, Runze Li, Jinzhen Lin, Zhenyu Ma, Changhua Meng, Han Peng, Xinyu Qiu, Shuheng Shen, Zhongyi Shui, Weiqiang Wang, Ming Wen, Zhuoer Xu, Hang Yan, Kaiwen Yang, Ruilin Yao, Nanjun Yu, Zhengwen Zeng, Lianrui Zhang, Yunzhu Zhang, Zhe Zhao, Beitong Zhou
**arXiv:** [arxiv.org/abs/2609.00028](https://arxiv.org/abs/2609.00028)
**Summary:** Multimodal GUI agents have emerged as a promising paradigm for digital task automation, yet transitioning from benchmark-oriented models to dependable real-world applications remains challenging due to limited environment coverage, brittle task construction, and unreliable reward verification. In this work, we present UI-Venus-2, a general-purpose foundation GUI agent designed to operate across mobile, web, and desktop environments through a unified closed-loop reasoning-action framework.
**Trending because:** 62 HuggingFace upvotes + cross-platform GUI agents are central to practical digital automation

---

### 5. ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training
**Authors:** Xionghao Wu, Yijun Yang, Shiyang Zhou, Haoze Sun, Jianhui Liu, Songsong Yu, Jiyao Zhang, Wenbo Li, Bo Wang, Guoqing Ma, Lin Song, Renjie Liao, Shenghe Zheng, Wei Tang, Xiaojuan Qi, Yanwei Li, Yuan Zhang, Zhuotao Tian, Haoyang Huang, Nan Duan
**arXiv:** [arxiv.org/abs/2609.00188](https://arxiv.org/abs/2609.00188)
**Summary:** Robotic manipulation faces a fundamental scaling challenge: robust generalization demands broad physical experience, yet action-labeled robot trajectories are expensive to collect and inherently limited in diversity. Egocentric videos offer a far more scalable source of embodied experience, capturing object interactions, contact dynamics, tool use, and long-horizon behaviors across diverse environments.
**Trending because:** 51 HuggingFace upvotes + scalable video pre-training targets broader robotic manipulation generalization

---

### 6. H3-World: Turning Language Understanding into World Control
**Authors:** Danze Chen, Zeqing Wang, Ziyue Lin, Xingyi Yang, Yeying Jin
**arXiv:** [arxiv.org/abs/2609.01560](https://arxiv.org/abs/2609.01560)
**Summary:** We present H3-World, an efficient framework that turns the 33B MiniMax-H3 video generator into an interactive world model. Our key finding is that, as large video generators become more capable, language is emerging as a natural interface for control.
**Trending because:** 50 HuggingFace upvotes + language-controlled interactive world models connect generation with action

---

### 7. Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question Answering
**Authors:** Jueun Kim, Sungho Park, Wook-Shin Han
**arXiv:** [arxiv.org/abs/2608.30468](https://arxiv.org/abs/2608.30468)
**Summary:** A central bottleneck in multi-hop Question Answering (QA) is that the granularity at which a question is expressed often differs from the granularity at which corpus evidence is retrievable. Existing methods address this mismatch by imposing fixed graph structures over the corpus, by iteratively reformulating the query, or by executing a generated program over it, but these strategies do not explicitly decide when a query unit is already supported by evidence and when it should be refined.
**Trending because:** 34 HuggingFace upvotes + evidence-guided query refinement addresses a core multi-hop QA bottleneck

---

### 8. From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers the Corporate Request Mix
**Authors:** Olga Tsymboi, Dmitrii Stoianov, Ramil Latypov, Danil Taranets, Daniil Dryabin, Mikhail Gashkov, Viktor Zelenkovskiy, Aleksandr Fida, Gleb Alektorov, Nikita Gulyakov, Arthur Babkin, Aleksandr Medvedev, Pavel Gein, Anatolii Potapov
**arXiv:** [arxiv.org/abs/2609.01572](https://arxiv.org/abs/2609.01572)
**Summary:** Data-residency constraints force enterprises to self-host LLMs, but continuous adoption of newer models without decommissioning their predecessors expands the serving fleet, fragmenting a finite GPU pool. We consolidate traffic from over 200 internal applications onto a single model by closing quality gaps identified through production error analysis along three axes: instruction following, function-calling, and internal task distribution.
**Trending because:** 33 HuggingFace upvotes + production-driven post-training tackles enterprise LLM fleet consolidation

---

### 9. Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching
**Authors:** Jaewoo Park, Minyoung Lee, Sukmin Seo, Moonbin Yim, Hyunwook Yoon, Dohoon Ryu, Daehee Kim, Myungseo Song, Jihyuk Byun, Seunggyu Chang, Taeho Kil, Jiseob Kim, Bado Lee, Geewook Kim
**arXiv:** [arxiv.org/abs/2609.01404](https://arxiv.org/abs/2609.01404)
**Summary:** Multimodal Large Language Models (MLLMs) are strong perceivers of images and video. We ask how far that reach extends into acting: dropping an MLLM directly into a drone's control loop, with its entire action space declared solely in the prompt.
**Trending because:** 27 HuggingFace upvotes + generalist multimodal control pushes VLMs into real drone action loops

---

### 10. Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models: From Representation, Task to System
**Authors:** Penghao Wu, Haiwen Diao, Weichen Fan, Lewei Lu, Dahua Lin, Ziwei Liu
**arXiv:** [arxiv.org/abs/2609.01607](https://arxiv.org/abs/2609.01607)
**Summary:** While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may reinforce each other, compete for capacity, or merely coexist. We investigate their relationship at the representation, task, and system levels in a controlled, structurally native setting without pretrained vision priors.
**Trending because:** 23 HuggingFace upvotes + it tests whether multimodal understanding and generation truly reinforce each other

---

### 11. DiagEvo: Diagnosis-Guided Self-Evolution via Hierarchical Error Memory
**Authors:** Xincheng Wei, Yifan Ding, Yoshua Li, Dongsheng Ma, Rongxiang Weng, Xunliang Cai, Wenjian Ding, Yao Zhang
**arXiv:** [arxiv.org/abs/2609.00768](https://arxiv.org/abs/2609.00768)
**Summary:** Self-play is an effective paradigm for language-model self-evolution, but without guidance, solver performance can plateau or decline across rounds. Unguided methods steer question generation with signals such as difficulty, learnability, or diversity.
**Trending because:** 20 HuggingFace upvotes + diagnosis-guided self-evolution aims to prevent language-model performance plateaus

---

### 12. Safin-1: Safety from Within through Memory-Native State Evolution
**Authors:** Ming Zhang, Kaisen Yang, Shu Yu, Ermo Hua, Zhekai Chen, Cheng Jin, Jingnan Zheng, Yi Zhang, Zhongtian Ma, Jiawei Zhou, Sirui Chen, Qiaosheng Zhang, Xiang Wang, Ning Ding, Xia Hu, Bowen Zhou, Youbang Sun, Chaochao Lu
**arXiv:** [arxiv.org/abs/2609.00092](https://arxiv.org/abs/2609.00092)
**Summary:** Long-horizon complex tasks require foundation models to accumulate information, maintain internal states, and adapt over extended interactions. Safety should be an intrinsic property of the model itself, rather than a behavioral constraint relying solely on external safeguards or post-hoc alignment such as supervised fine-tuning.
**Trending because:** 20 HuggingFace upvotes + memory-native safety targets intrinsic protection in long-horizon agents

---

### 13. AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling
**Authors:** Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru
**arXiv:** [arxiv.org/abs/2608.26623](https://arxiv.org/abs/2608.26623)
**Summary:** LLM judges are widely used to evaluate agentic tool-calling systems, yet their reliability on structured, dependency-driven workflows remains largely unexamined. We present AgentJudgeBench, the first benchmark to systematically study LLM-as-a-judge reliability for agentic tool-calling over workflow DAGs, as distinct from the broader LLM-as-a-judge task of open-ended text or preference evaluation.
**Trending because:** 20 HuggingFace upvotes + reliable LLM judging is essential for evaluating tool-using agents

---

### 14. Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement
**Authors:** Haoyang Yan, Min-le Su, Hangfan Zhang, Zhanhao Li, Chen Zhang, Shao Zhang, Yang Chen, Lei Bai, Shuyue Hu
**arXiv:** [arxiv.org/abs/2609.01481](https://arxiv.org/abs/2609.01481)
**Summary:** This paper studies autonomous software development, in which LLM-based coding agents transform high-level requirements into complete, functional, and usable software systems without human intervention. We introduce Harness-of-Harness (HoH), a framework that enables coding agents to continually improve software during autonomous development.
**Trending because:** 17 HuggingFace upvotes + continual improvement over multi-day coding tasks advances autonomous software agents

---

### 15. E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation
**Authors:** Wei Fan, Xinjie Shen, Xudong Guo, Jianhong Tu, Yang Su, Yinger Zhang, Lianghao Deng, Fengyu Wang, Baohua Dong, Yangqiu Song, Dayiheng Liu
**arXiv:** [arxiv.org/abs/2608.30730](https://arxiv.org/abs/2608.30730)
**Summary:** Long-horizon agentic tasks go beyond chaining short tasks over more interaction turns. Their evolving dynamic environments and long-range dependencies require Large Language Models (LLMs) to continually explore, learn from experience, and adapt their policies over thousands of steps.
**Trending because:** 16 HuggingFace upvotes + long-horizon business operation is a demanding benchmark for adaptive agents

---

### 16. EM^2Mem: Event-Centric Multimodal Memory for Large Language Models
**Authors:** Yijun Chen, Yaqi Zheng, Yanya Li, Boyi Xiao, Buqiang Xu, Shuofei Qiao, Jizhan Fang, Xinle Deng, Yunzhi Yao, Xuehai Wang, Liuxin Zhang, Hui Li, Huajun Chen, Shumin Deng
**arXiv:** [arxiv.org/abs/2609.00551](https://arxiv.org/abs/2609.00551)
**Summary:** Multimodal memory offers a scalable interface for long-video question answering, but existing methods often retrieve captions, frames, transcripts, summaries, or graph facts as isolated fragments. Although searchable, such fragments are not generation-ready: language models must reconstruct cross-modal and temporal alignments at inference time, when context is limited and attribution is difficult.
**Trending because:** 14 HuggingFace upvotes + event-centric memory improves generation-ready retrieval from long multimodal streams

---

### 17. Agents in the Large: Perception-Centered Architecture for Persistent Agents
**Authors:** Shihan Dou, Haoxiang Jia, Shichun Liu, Feng Chen, Chenhao Huang, Yujiong Shen, Shaofan Liu, Jiayi Chen, Jiahang Lin, Honglin Guo, Qianyu He, Minghao Guo, Ziyi Ye, Pluto Zhou, Tao Gui, Qi Zhang, Xuanjing Huang
**arXiv:** [arxiv.org/abs/2608.30478](https://arxiv.org/abs/2608.30478)
**Summary:** Cognitive language agents have achieved substantial progress by equipping language models with memory, tools, and decision-making procedures, enabling agents to reason and act in interactive environments. Existing frameworks largely cast these agents as systems for solving user-specified, bounded tasks.
**Trending because:** 11 HuggingFace upvotes + persistent agents require architectures beyond bounded task execution

---

### 18. Learning Where Outcomes Change:Credit-Addressable Reasoning for Multimodal Geometry
**Authors:** Jiani Guo, Junjie Wang, Jie Wu, Pengxiang Zhao, Dongdong Zhang, Shaohan Huang, Yujiu Yang, Furu Wei
**arXiv:** [arxiv.org/abs/2608.30457](https://arxiv.org/abs/2608.30457)
**Summary:** Multimodal geometry reasoning requires VLMs to extract precise visual relations and preserve them through multi-step deduction. Existing free-form traces obscure the decisions that determine the answer, and trajectory-level reinforcement learning distributes a single terminal signal across the entire response.
**Trending because:** 9 HuggingFace upvotes + credit-addressable reasoning improves supervision for multimodal geometry

---

### 19. Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall
**Authors:** Jacqueline He, Howard Yen, Shuyue Stella Li, Margaret Li, Hanqing Zeng, Yinglong Xia, Benyu Zhang, Zhuokai Zhao, Qiang Zhang, Pang Wei Koh, Luke Zettlemoyer, Wen-tau Yih
**arXiv:** [arxiv.org/abs/2609.01532](https://arxiv.org/abs/2609.01532)
**Summary:** Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the standard KD formulation--with post-trained teachers behaves fundamentally differently during mid-training, an intermediate phase of self-supervised learning on curated corpora.
**Trending because:** 8 HuggingFace upvotes + the study distinguishes distillation effects on reasoning from factual recall

---

### 20. Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs
**Authors:** Wentao Zhang, Syed Shariyar Murtaza, Junaid Ahmad Bhatti, Utkarsh Soni, Yifan Nie, Eugene Wen, Yuntian Deng
**arXiv:** [arxiv.org/abs/2609.00621](https://arxiv.org/abs/2609.00621)
**Summary:** Prompt optimization can improve multi-agent LLM systems, but the prompts being optimized often serve two entangled roles: generating task-relevant content and specifying execution-critical protocols, such as message routing, output formatting, and termination signals, on which the underlying code relies. As a result, a prompt edit intended to improve content generation can inadvertently corrupt the protocol and cause the entire agent pipeline to fail.
**Trending because:** 8 HuggingFace upvotes + separating protocol control from content stabilizes multi-agent prompt optimization

---
