---
title: "Daily AI Papers — September 4, 2026"
date: 2026-09-04
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-04/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - multimodal-generation
  - efficient-llms
---

### 1. Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments
**Authors:** Jie Wu, Zhenru Zhang, Beichen Zhang, Xuwu Wang, Yuhui Su, Mouxiang Chen, Peng Wang, Zhihai Wang, Que Shen, Hao Zhou, An Yang, Fei Huang, Yujiu Yang, Dayiheng Liu
**arXiv:** [arxiv.org/abs/2609.04148](https://arxiv.org/abs/2609.04148)
**Summary:** As terminal-based code agents become prevalent, agent trajectories have accumulated at scale, while realistic, executable environments remain scarce. However, environments are what agent post-training actually requires: each can be re-queried into many verifiable tasks and provides execution feedback, whereas a trajectory is a single frozen demonstration.
**Trending because:** 288 HuggingFace upvotes + reconstructing reusable terminal environments could scale verifiable agent training

---

### 2. LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes
**Authors:** Chuyan Chen, Haoxing Chen, Kun Chen, Zhenglin Cheng, Long Cui, Ruishan Fang, Zhangxuan Gu, Zhicheng Huang, Zhenzhong Lan, Yuanting Lei, Haoquan Li, Jianguo Li, Rongchuan Li, Sidu Li, Tao Lin, Deyuan Liu, Jiacheng Liu, Lin Liu, Yuxuan Lou, Zhisheng Lu, Yuxin Ma, Shuheng Shen, Peng Sun, Chaoyang Wang, Hongjun Wang, Xiaomei Wang, Yongxin Wang, Chengzhang Wu, Hongru Wu, Jun Xie
**arXiv:** [arxiv.org/abs/2609.03796](https://arxiv.org/abs/2609.03796)
**Summary:** We introduce LLaDA-Image, a unified framework that pairs a 6B Diffusion Transformer (DiT) trained from scratch with a frozen vision-language understanding module built on the LLaDA2.0-Mini diffusion language model backbone. Instead of relying heavily on paired image-text data from the beginning, we first build a strong visual generative prior through image-only pre-training and mid-training.
**Trending because:** 231 HuggingFace upvotes + its fully open recipe advances high-quality image generation and editing

---

### 3. Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning
**Authors:** Heng Wang, Jielin Qiu, Wenting Zhao, Cheng Qian, Liangwei Yang, Jiawei Han, Heng Ji, Silvio Savarese, Shelby Heinecke, Huan Wang
**arXiv:** [arxiv.org/abs/2609.03430](https://arxiv.org/abs/2609.03430)
**Summary:** Large language models achieve superior performance on tasks that require extended reasoning, but long chains of thought make the KV cache a severe memory bottleneck. Existing KV cache compression methods share one paradigm: score each cached token by some estimate of how much it will matter later, and keep the top-scoring ones.
**Trending because:** 170 HuggingFace upvotes + random eviction challenges assumptions about efficient long-context reasoning

---

### 4. Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training
**Authors:** Tingyun Li, Wenfeng Feng, Weiqing Li, Abudukelimu Wuerkaixi, Guohua Liu, Yuewei Zhang
**arXiv:** [arxiv.org/abs/2608.26730](https://arxiv.org/abs/2608.26730)
**Summary:** Large language models offer broad capabilities, but adapting them to evolving domains, tools, and requirements often entails repeated post-training. Autonomous systems automate parts of this process by proposing updates, training candidates, and using evaluation feedback to select subsequent proposals.
**Trending because:** 150 HuggingFace upvotes + safer experience reuse matters for autonomous LLM post-training

---

### 5. LatentPress: Context Compression Beyond Text and Vision
**Authors:** Zhengze Zhou, Hejian Sang
**arXiv:** [arxiv.org/abs/2609.01507](https://arxiv.org/abs/2609.01507)
**Summary:** Compressed context is usually carried as human-readable text or as rendered images that must be decoded, even when its consumer is a language model. We introduce LatentPress, which writes conversational histories and long documents into a third representation: continuous memory tokens that a frozen decoder reads directly through its input-embedding interface, with no text reconstruction at inference.
**Trending because:** 113 HuggingFace upvotes + continuous memory tokens offer a fast alternative to textual context compression

---

### 6. Rethinking On-Policy Distillation of Large Language Models II: One Training Example
**Authors:** Zixuan Fu, Bingxiang He, Yuxin Zuo, Haohuan Huang, Jinqian Zhang, Ruhang Xiao, Cheng Qian, Qinyu Luo, Huan-ang Gao, Yudong Wang, Zhiyuan Liu, Ning Ding, Chaojun Xiao
**arXiv:** [arxiv.org/abs/2609.04172](https://arxiv.org/abs/2609.04172)
**Summary:** On-policy distillation (OPD) combines student-generated rollouts with dense token-level supervision from a teacher. Existing work has mainly studied its algorithmic behavior, leaving the role of training data unclear.
**Trending because:** 83 HuggingFace upvotes + single-example distillation exposes surprising data efficiency in LLM post-training

---

### 7. Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM
**Authors:** Sergii Kozyrev, Davyd Maiboroda
**arXiv:** [arxiv.org/abs/2609.04098](https://arxiv.org/abs/2609.04098)
**Summary:** Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially its decay and write-strength gates -- on the intuition that errors in a recurrence accumulate over long contexts.
**Trending because:** 78 HuggingFace upvotes + full 4-bit quantization could make hybrid LLM inference smaller and faster

---

### 8. Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States
**Authors:** Kang Liao, Yihang Luo, Xiao-Ming Wu, Linyi Jin, Size Wu, Chunyu Lin, Yao Zhao, Fei Wang, Wei Li, Chen Change Loy
**arXiv:** [arxiv.org/abs/2609.04196](https://arxiv.org/abs/2609.04196)
**Summary:** We propose Puffin-World, a unified multimodal architecture that integrates physical understanding, spatial simulation, and 3D world generation and reconstruction without relying on external offline modules. To reliably construct and interact with 3D worlds, our framework jointly models three native world states: physics (gravity field and latitude), geometry (depth), and appearance (image), together with a unified Omni-Camera representation that supports diverse tasks and flexible motions.
**Trending because:** 66 HuggingFace upvotes + native physical and geometric states advance unified 3D world modeling

---

### 9. Editable Visual Design
**Authors:** Junyan Ye, Wei Liu, Dongzhi Jiang, Zichen Wen, HaoDong Li, Zhutao Lv, Jiaxin Lin, Jinhua Yu, Jun He, Zilong Huang, Rui Chen, Weijia Li
**arXiv:** [arxiv.org/abs/2609.04034](https://arxiv.org/abs/2609.04034)
**Summary:** While diffusion base models such as GPT-Image-2 and Nano-Banana exhibit remarkable visual expressiveness, their end-to-end generation inherently yields flattened bitmaps with error-prone text, precluding layer-wise post-editing. Conversely, code-based visual generation via Coding Agents provides precise layout control and decoupled layers, yet remains constrained by a lack of global aesthetic intuition and the difficulty of coding complex visual assets.
**Trending because:** 42 HuggingFace upvotes + combining coding agents with image generation makes visual artifacts editable

---

### 10. The Missing Temporal Link: Temporal Context Routing for Script-Driven Audio-Video Generation
**Authors:** Yichen Liu, Quanwei Zhang, Haozhe Wang, Donghao Zhou, Xiaojie Li, Yang Shi, Jiaming Liu, Ruihua Huang, Yingtian Zou, Daquan Zhou
**arXiv:** [arxiv.org/abs/2609.02367](https://arxiv.org/abs/2609.02367)
**Summary:** Joint audio-video generation models have made substantial progress in visual quality and audio-visual synchronization. However, they still provide limited control over when shot transitions occur and dialogue is spoken.
**Trending because:** 33 HuggingFace upvotes + explicit timeline control improves script-driven audio-video generation

---

### 11. Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding
**Authors:** Hongyu Qu, Guangming Yao, Ling Xing, Xiaobin Hu, Rongxing Ding, Guibin Zhang, Fan Zhang, Yi Yuan, Xiangbo Shu, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2609.04131](https://arxiv.org/abs/2609.04131)
**Summary:** Streaming video understanding requires multimodal large language models (MLLMs) to process continuous visual inputs and respond to user queries under strict causality and bounded memory. Existing approaches typically compress historical observations into an external memory bank and retrieve query-relevant evidence as additional visual context.
**Trending because:** 31 HuggingFace upvotes + evolving latent memory targets bounded-memory streaming video understanding

---

### 12. RealSWE: A Compositional Evaluation of Coding Agents under Realistic User Requests
**Authors:** Gyuhyeong Kim, Hyojung Gwon, Jeonghyeon Kim, Kyuhong Shim, Sunjae Lee
**arXiv:** [arxiv.org/abs/2608.27831](https://arxiv.org/abs/2608.27831)
**Summary:** Coding agents are now commonly evaluated on the SWE-bench family of benchmarks, whose tasks are built from curated GitHub issues: long, structured, and information-rich. Real user requests, however, are typically far shorter and less structured.
**Trending because:** 31 HuggingFace upvotes + realistic user prompts reveal gaps in coding-agent benchmarks

---

### 13. WorldReward: Reward Modeling for Camera-Conditioned World Models
**Authors:** Yibin Wang, Zehan Wang, Junshu Tang, Zhimin Li, Yujie Zhou, Jiazi Bu, Pengyang Ling, Feng Han, Zhixiong Zhang, Long Xing, Shengyuan Ding, Ziang Li, Cheng Jin, Yuhang Zang, Jiaqi Wang, Tianyu Pang
**arXiv:** [arxiv.org/abs/2609.03952](https://arxiv.org/abs/2609.03952)
**Summary:** Camera-conditioned world models generate interactive videos in which commanded actions should induce the expected scene changes while appearance, geometry, and temporal dynamics remain coherent. Existing rewards assess these requirements separately: geometry-based rewards estimate trajectory execution but cannot judge the visual quality of the executed motion, whereas image-based rewards measure frame quality without capturing action execution or temporal dynamics.
**Trending because:** 25 HuggingFace upvotes + unified reward modeling improves action fidelity and visual quality in world models

---

### 14. CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation
**Authors:** Tingyu Song, Mingxin Li, Yanzhao Zhang, Dingkun Long, Chu Liu, Pengjun Xie, Yilun Zhao, Shu Wu
**arXiv:** [arxiv.org/abs/2609.04083](https://arxiv.org/abs/2609.04083)
**Summary:** MLLM-based embedding models remain limited in compositional retrieval, often failing to distinguish scenes containing the same concepts but different attribute-object bindings. Yet the same backbone can resolve such distinctions when used as a cross-attentive reranker, motivating us to distill its compositional judgments into the embedding model.
**Trending because:** 25 HuggingFace upvotes + reranker distillation strengthens compositional multimodal retrieval

---

### 15. PACE: Towards Surfacing Hidden Conflicts in User Requests
**Authors:** Yoojin Kim, Jihyoung Jang, Hyounghun Kim
**arXiv:** [arxiv.org/abs/2609.03293](https://arxiv.org/abs/2609.03293)
**Summary:** Personalized assistants should not only comply with user requests but also assess whether those requests are appropriate given the user's current circumstances. However, prior work has primarily focused on accurately executing requests, overlooking the need for assistants to account for context and engage in conflict-based refusal.
**Trending because:** 24 HuggingFace upvotes + personalized assistants need to surface implicit conflicts before complying

---

### 16. Environment Evolution for Terminal Agents
**Authors:** Zhiyuan Fan, Tinghao Yu, Yuanjun Cai, Jiang Zhou, Jiangtao Guan, Jincheng Liu, Yun Yang, Dingxin Hu, Zhuo Han, Xing Wu, Feng Zhang, Lilin Wang
**arXiv:** [arxiv.org/abs/2609.04128](https://arxiv.org/abs/2609.04128)
**Summary:** Scaling interactive and verifiable environments is critical for training terminal agents. As frontier models become more capable, environments synthesized from scratch become less challenging and thus provide limited learning signals.
**Trending because:** 20 HuggingFace upvotes + off-policy environment evolution provides harder training tasks for terminal agents

---

### 17. FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow
**Authors:** Byeongjun Park, Byung-Hoon Kim, Hyungjin Chung
**arXiv:** [arxiv.org/abs/2609.03563](https://arxiv.org/abs/2609.03563)
**Summary:** We present FlashRender, a few-step generative rendering framework that retakes a source video along a target camera trajectory in seconds. We identify sampling-step-dependent camera control as a prominent manifestation of discretization error in existing multi-step generative rendering models and show that resolving this inconsistency substantially lowers denoising trajectory curvature, facilitating subsequent step distillation.
**Trending because:** 19 HuggingFace upvotes + few-step rendering delivers large speedups while preserving camera control

---

### 18. Principia: Relational Physics Tests for Video Models
**Authors:** Varun Varma Thozhiyoor, Shivam Tripathi, Venkatesh Babu Radhakrishnan, Anand Bhattad
**arXiv:** [arxiv.org/abs/2609.04200](https://arxiv.org/abs/2609.04200)
**Summary:** Evaluating physical reasoning in video models is difficult because absolute motion measurements depend on frame rate, object scale, and camera calibration, all of which are often ambiguous or unavailable in generated video. We propose a different approach.
**Trending because:** 16 HuggingFace upvotes + calibration-independent tests expose weak physical consistency in video models

---

### 19. Percolation Dynamics in Optimization : Variance Cascades and Discrete Scale Invariance
**Authors:** Sai Niranjan Ramachandran, Suvrit Sra
**arXiv:** [arxiv.org/abs/2609.02373](https://arxiv.org/abs/2609.02373)
**Summary:** We study the dynamics of Stochastic Gradient Descent (SGD), which is known to steer deep neural networks toward invariant sets that correspond to simpler subnetworks. How this steering unfolds over time remains poorly understood.
**Trending because:** 14 HuggingFace upvotes + a percolation view links optimizer dynamics to discrete subnetwork transitions

---

### 20. Let Confidence Change, Not the Prediction: Prediction-Preserving Repair for Post-hoc Calibration
**Authors:** Daehwan Kim, Haejun Chung, Ikbeom Jang
**arXiv:** [arxiv.org/abs/2609.01072](https://arxiv.org/abs/2609.01072)
**Summary:** Post-hoc calibration corrects reported confidence, yet a multiclass calibrator can also change the associated top-1 prediction. Accuracy captures only the net effect of these changes on correctness, not how often predictions change; the Top-1 Prediction Change Rate (TPCR) instead measures this frequency.
**Trending because:** 13 HuggingFace upvotes + exact prediction preservation improves confidence calibration without changing decisions

---
