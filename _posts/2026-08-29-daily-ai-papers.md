---
title: "Daily AI Papers — August 29, 2026"
date: 2026-08-29
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-29/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - video-generation
  - test-time-scaling
---

### 1. MARS: Multi-Specialist LLM Relay System for Competitive Programming
**Authors:** Andrei Mikhailov, Mikhail Burtsev, Alsu Sagirova
**arXiv:** [arxiv.org/abs/2608.23918](https://arxiv.org/abs/2608.23918)
**Summary:** Large Language Models excel at code generation, yet competitive programming exposes a persistent failure mode: existing multi-agent pipelines distribute work over generic planner, coder, and debugger roles and delegate the choice of algorithmic technique to the backbone alone. We present MARS (Multi-Agent Relay of Specialized LLMs), a prompt-only framework in which each agent is a topic specialist---dynamic programming, graphs, strings, geometry, and so on---grounded by retrieval-augmented generation over an algorithm-theory corpus.
**Trending because:** 8 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 2. AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace
**Authors:** Seonglae Cho, Donghyun Lee
**arXiv:** [arxiv.org/abs/2608.23740](https://arxiv.org/abs/2608.23740)
**Summary:** Concurrent multi-agent coding promises division of labor across modules, robustness through redundancy, and parallel exploration at the natural granularity of multi-file projects. Realtime collaborative editing protocols solve this coordination problem for human teams via Conflict-free Replicated Data Types (CRDTs), but the LLMs underneath generate one token at a time and existing multi-agent coding systems inherit this serial limit: they either sequence agents through phase handoffs or pool independent samples without coordination, and a single agent abandons up to half of hard tasks with a one-file stub-and-exit.
**Trending because:** 7 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 3. Luce: Relightable Gaussians for 3D Asset Generation
**Authors:** Mayank Singh, Michele Stoppa, Alvise Memo, Rui Yu, Harsha Kalli, Srimanth Gunturi, Muhammad Ahmed Riaz, Behrooz Shahsavari, Waleed Abdulla, David E. Jacobs
**arXiv:** [arxiv.org/abs/2608.23943](https://arxiv.org/abs/2608.23943)
**Summary:** High-fidelity image-to-3D generation requires a 3D representation that captures both geometry and appearance. To support relighting and integration into standard rendering pipelines, the representation should include physically based rendering (PBR) modalities such as albedo, metallic-roughness, and surface normals.
**Trending because:** 7 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 4. CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes
**Authors:** Yufan Wu, Yinghui He, Zhengyi Hu, Lang Wei, Ruichen Li, Qifan Yang, Ting Zhu
**arXiv:** [arxiv.org/abs/2608.27455](https://arxiv.org/abs/2608.27455)
**Summary:** Recent advances in inference-time scaling have significantly improved the reasoning performance of large language models (LLMs). However, these methods typically rely on repeated generation or external verification.
**Trending because:** 6 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 5. When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows
**Authors:** Yiheng Sun, Huifei Wang, Yancheng Zhu, Zhenyu Li, Zebin Zhao, Yifan Yuan
**arXiv:** [arxiv.org/abs/2608.24569](https://arxiv.org/abs/2608.24569)
**Summary:** Large language model (LLM) agents coordinate complex tasks through multi-role and multi-stage workflows. Upstream state is repeatedly transformed into intermediate language artifacts, such as summaries, plans, tickets, memories, and handoff notes, from which downstream components act.
**Trending because:** 6 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 6. CAFE: Self-Improving Search Agents Need Co-Evolving Feedback
**Authors:** Boyang Liu, Senjie Jin, Peixin Wang, Zhangyue Yin, Yibo Wang, Yuhao Zhou, Xinbing Liang, Shizheng Zhu, Yuhui Wang, Jingqi Tong, Zhiheng Xi, Jiazheng Zhang, Clive Bai, Clarenceai, Blaze Chen, Tao Gui, Qi Zhang, Xuanjing Huang
**arXiv:** [arxiv.org/abs/2608.24794](https://arxiv.org/abs/2608.24794)
**Summary:** Outcome-supervised search agents learn when and how to retrieve evidence, but terminal rewards neither localize intermediate errors nor redirect an ongoing trajectory before those errors compound. Treating corrective feedback as a learned in-trajectory intervention couples the two roles: the agent must decide when to request and use feedback, while the critic must infer useful corrections from outcome-confounded rollouts whose failure patterns shift as the agent improves.
**Trending because:** 5 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 7. CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval
**Authors:** Zhiyuan Li, Linyuan Gao, Xuechun Ding, Hongwei Chen, Yuan Wu, Yi Chang
**arXiv:** [arxiv.org/abs/2608.25500](https://arxiv.org/abs/2608.25500)
**Summary:** Reusable skill libraries allow large language model (LLM) agents to reuse procedural knowledge across tasks, but they also turn memory access into a challenging retrieval problem. Full-library prompting preserves coverage at high context cost, vector retrieval returns compact neighborhoods but treats skills as independent text, and graph-based retrieval can recover workflow context only when the edges that carry relevance are reliable.
**Trending because:** 5 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 8. DREAM Technical Report
**Authors:** Bin Zhang, Bowen Zheng, Chao Yi, Chengyu Lai, Dian Chen, Dimin Wang, Gaoyang Guo, Jialin Zhu, Jian Wu, Jing Yu, Jiuning Lin, Lingqing Zhang, Lingyun Zheng, Mao Zhang, Mingming Pan, Ruiquan Lan, Shuai Zhong, Wen Chen, Wendong Zhang, Xiaodong Zhu, Xuan Chen, Xunke Xi, Yifan Lu, Yiheng Wang, Yue Zeng, Yujie Luo, Yuning Jiang, Zhe Hu, Zhibo Xiao, Zihong Huang, Binbin Cao, Bo Zheng, Danning Wang, Dixuan Wang, Ge Fan, Haixia Wu, Han Zhu, Hao Fang, Haoming Chen, Huiping Chu, Jian Wang, Jianjun Wu, Jiawei Wu, Jiaxin Yu, Jingwen Liu, Jinzhe Shan, Kai Meng, Kai Zhang, Keqin Xu, Kewei Zhu, Lang Tian, Leihui Chen, Li Chen, Licheng Xu, Lide Xiao, Ruitong Zhang, Shiyao Peng, Silu Zhou, Tao Wang, Wei Shi, Wenjun Yang, Xiang Chen, Xiang Gao, Xiao Ren, Xu Liu, Xuwen Wang, Yang Li, Yeqiu Yang, Yi Hu, Yichen Yuan, Yinnan Song, Yipeng Yu, Yuan Liu, Yunqi Gao, Zhiliang Huang, Zhujin Gao, Zongyuan Wu
**arXiv:** [arxiv.org/abs/2608.09408](https://arxiv.org/abs/2608.09408)
**Summary:** Industrial recommender systems commonly use cascaded retrieval, ranking, and re-ranking pipelines. Although efficient, these pipelines fragment information and objectives across modules, rely on rigid rules, and have limited awareness of real-time intent, leaving session-level shifts among browsing, comparison, and purchase insufficiently addressed.
**Trending because:** 5 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 9. Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models
**Authors:** Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh
**arXiv:** [arxiv.org/abs/2608.19556](https://arxiv.org/abs/2608.19556)
**Summary:** Streaming autoregressive diffusion models enable real-time, long-horizon video generation, but their training objectives optimize local frame prediction rather than the geometry and dynamics of a coherent world: long rollouts accumulate geometric drift and degrade into static or unnatural motion. Recent bidirectional approaches address this problem using rewards signals built upon 3D Gaussian-Splatting reconstruction.
**Trending because:** 5 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 10. Super Star: Towards Streaming Real-time Interactive Agents for Digital Humans
**Authors:** Wentao Jiang, Youchen Xie, Haidi Fan, Yajing Chen, Xin Wang, Ye Shi, Jingya Wang
**arXiv:** [arxiv.org/abs/2608.24909](https://arxiv.org/abs/2608.24909)
**Summary:** Existing co-speech gesture generation methods are predominantly studied in offline settings, where gestures are synthesized from complete speech segments. However, interactive digital humans in real-world scenarios are required to generate speech-synchronous gestures online, using only currently available response audio under strict latency constraints.
**Trending because:** 5 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 11. TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback
**Authors:** Jianbo Zhou, Boyuan Zhao, Yuzheng Zhang, Yiyang Chen, Wenxin Chen, Qiuyue Li, Xiangyang Gu, Yuhan Cao, Xiao Xia, Yanzhe Hu, Zhijie Deng
**arXiv:** [arxiv.org/abs/2608.25798](https://arxiv.org/abs/2608.25798)
**Summary:** Contact-rich manipulation requires adapting to contact states that can evolve substantially within an action horizon. However, chunk-based vision-language-action models predict complete action chunks from observations collected before execution, leaving tactile conditioning stale during execution.
**Trending because:** 5 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 12. Automata from Agent Traces: Failure and Next-Step Prediction
**Authors:** Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed, Zekun Wu, Kleyton Da Costa, Ilham Wicaksono, Adriano Koshiyama
**arXiv:** [arxiv.org/abs/2608.23670](https://arxiv.org/abs/2608.23670)
**Summary:** LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 13. Length-Adaptive Decoding for Masked Diffusion Machine Translation
**Authors:** Yan Zhan, Mengkai Hou, Wanting Zhang, Zhijun Gao
**arXiv:** [arxiv.org/abs/2608.22274](https://arxiv.org/abs/2608.22274)
**Summary:** Machine translation tests masked diffusion language models (dLLMs) because every source token must be rendered faithfully, while fixed canvas decoding must choose target length before denoising. Existing masked diffusion decoding work mainly studies token unmasking order, leaving this length decision under-explored despite its direct effect on coverage and redundancy.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 14. Prefix Sliding for efficient test-time scaling
**Authors:** Niklas Muennighoff, Zhengyang Wang, Zeyi Chen, Weijia Shi, Binyuan Hui, John Yang, Dapeng Jiang, Mika Senghaas, Fares Obeid, Johannes Hagemann, Sami Jaghouar, Ludwig Schmidt, Percy Liang, Jason Wei, Andrew Y. Ng, Luke Zettlemoyer, Yejin Choi, Mike Lewis
**arXiv:** [arxiv.org/abs/2608.26070](https://arxiv.org/abs/2608.26070)
**Summary:** Test-time scaling uses extra test-time compute to improve performance, such as letting language models reason longer when solving a problem. As models keep the entire reasoning trace in memory via full attention, hard tasks that need long thinking can be prohibitively expensive.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 15. Skill Issue: Are Skills Language-Invariant in LLMs?
**Authors:** Bobby Cheng, Adam Gaber, Zhengyuan Liu, Catherine Arnett, Omer Goldman, Cheston Tan, Leshem Choshen
**arXiv:** [arxiv.org/abs/2608.25832](https://arxiv.org/abs/2608.25832)
**Summary:** Large language models access knowledge inconsistently across languages, but to what extent do they differ in their skill sets when interacting with different languages? This work quantifies cross-lingual skill inconsistency orthogonally from knowledge and general benchmark performance.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 16. Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning
**Authors:** Chenyang Wu, Fuchen Long, Binyuan Huang, Xinlong Sun, Xi Chen, Chun-Le Guo, Chongyi Li
**arXiv:** [arxiv.org/abs/2608.26809](https://arxiv.org/abs/2608.26809)
**Summary:** While generative AI has significantly advanced video editing, existing methods primarily focus on single-shot or short video clips. Editing long videos with multiple instructions remains a formidable challenge.
**Trending because:** 4 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 17. Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal Reasoning
**Authors:** Hengyuan Xu, Wei Cheng, Yumeng Ji, Xuanyang Zhang, Xianfang Zeng, Gang Yu, Xingjun Ma
**arXiv:** [arxiv.org/abs/2608.26993](https://arxiv.org/abs/2608.26993)
**Summary:** Explicit visual intermediates can help multimodal large language models (MLLMs) externalize spatial evidence and updated visual states, but their utility depends on whether an image editor can faithfully realize the required transformation. We introduce Aphanta, an automated task-discovery and closed-loop diagnostic framework for the MLLM -> image editor -> MLLM pipeline.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 18. EditaLive! Unified Character Video Editing for Live Streaming
**Authors:** Zhiyuan Li, Chi-Man Pun, Peng-Tao Jiang, Bo Li, Xiaodong Cun
**arXiv:** [arxiv.org/abs/2608.27123](https://arxiv.org/abs/2608.27123)
**Summary:** Conventional video editing primarily focuses on scene-level content, whereas live streaming places greater emphasis on the human subject. However, directly applying existing video-editing methods to human-centric live streaming remains challenging, as they may introduce facial-expression inconsistencies and typically depend on multiple offline inference steps, making them unsuitable for real-time interaction.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 19. FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling
**Authors:** Peiyuan Zhang, Xiangyu Zhao, Hongbo Liu, Xiaoxing Hu, Mingxin Liu, Shuran Ma, Yunhang Shen, Jian Hu, Haihan Gao, Haoyu Cao, Xue Yang
**arXiv:** [arxiv.org/abs/2608.21839](https://arxiv.org/abs/2608.21839)
**Summary:** Reliable reward models are essential for text-to-video evaluation and alignment. However, the trade-off between evaluation accuracy and inference efficiency places high demands on the quality of training supervision.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
### 20. MoTE: Mixture of Task Experts for Multi-Task Video Understanding
**Authors:** Muhammad Asad Ali, Umar Khan, Nadia Robertini, Didier Stricker
**arXiv:** [arxiv.org/abs/2608.24763](https://arxiv.org/abs/2608.24763)
**Summary:** Procedural video-language models must solve heterogeneous tasks from the same visual evidence, including action recognition, forecasting, and procedure prediction. Dense transformer decoders share the same feed-forward networks across tasks, which can entangle task behavior and make controlled capability expansion difficult.
**Trending because:** 3 HuggingFace upvotes + surfaced on the HuggingFace trending feed for its topical relevance

---
