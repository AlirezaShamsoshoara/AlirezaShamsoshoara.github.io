---
title: "Daily AI Papers — August 08, 2026"
date: 2026-08-08
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-08/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - world-models
  - agentic-ai
  - vla-robotics
---

### 1. Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory and Replay
**Authors:** Nossa Iyamu
**arXiv:** [arxiv.org/abs/2608.05784](https://arxiv.org/abs/2608.05784)
**Summary:** Computer-use agents pay full frontier inference to re-derive routines their user has already performed, because an agent's memory today records what the user said, not what the user did. We compile passively captured screen activity into agent memory with a deterministic, zero-model pipeline: it segments a local capture stream into typed activity frames, bounded episodes carrying application, site, timing, input volume, and evidence pointers back to the raw rows, with no model in the loop, so the output is byte-identical, cacheable, and mechanically auditable.
**Trending because:** 16 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 2. KVAE: Family of Tokenizers for Multimodal Generative Models
**Authors:** Andrey Shutkin, Denis Parkhomenko, Ivan Kirillov, Kirill Chernyshev, Kirill Malakhov, Ilia Vasiliev, Ilia Trushkin, Valeriya Kobenko, David Chikovani, Alexander Ivanov, Azat Saginbaev, Egor Silvestrov, Ivan Mikheev, Konstantin Zakharov
**arXiv:** [arxiv.org/abs/2608.05798](https://arxiv.org/abs/2608.05798)
**Summary:** Latent diffusion modeling (LDM), a prominent paradigm, utilizes tokenizers to map input signal to compressed representation. This dependency positions tokenizer as an integral part of generation process itself, since it affects learning speed, quality of synthesized samples and lay foundation for later applications.
**Trending because:** 14 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 3. MameLoshnLM: Yiddish Language Model and Evaluation Benchmark
**Authors:** Uri Katz, Omer Goldman, Tomasz Limisiewicz, Reut Tsarfaty, Noah A. Smith
**arXiv:** [arxiv.org/abs/2608.05850](https://arxiv.org/abs/2608.05850)
**Summary:** We present MameLoshnLM, the first open-source 8B-parameter language model built specifically for Yiddish. Despite Yiddish's rich textual tradition, its limited digital presence and the scarcity of reliable evaluation resources have constrained progress in Yiddish language modeling.
**Trending because:** 14 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 4. Continual Learning in Transition
**Authors:** Zhiyan Hou, Dan Zhang, Tao Feng, Liyuan Wang, Wei Li, Xiangzhao Hao, Hongyan An, Junfeng Fang, Haokai Ma, Zhaohui Xu, Haiyun Guo, Jinqiao Wang, Tat-Seng Chua
**arXiv:** [arxiv.org/abs/2608.06216](https://arxiv.org/abs/2608.06216)
**Summary:** Classical continual learning (CL) has primarily focused on enabling models to update and retain knowledge through parameter-centric mechanisms, e.g., training strategies, architectural designs, and weight adaptation. However, emerging paradigms are reshaping the scope of CL beyond this traditional model adaptation view.
**Trending because:** 13 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 5. ExplainBench: Evaluating Code Explanations from Agents
**Authors:** Zhiyuan Pan, Sungmin Kang, Imam Nur Bani Yusuf, Abhik Roychoudhury
**arXiv:** [arxiv.org/abs/2607.26451](https://arxiv.org/abs/2607.26451)
**Summary:** Large Language Model (LLM) agents have seen rapid adoption in software engineering. As agents take a greater role in the actual generation of code, they are making larger changes, spanning tens to hundreds of lines.
**Trending because:** 13 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 6. WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models
**Authors:** Bohai Gu, Yueyang Yuan, Taiyi Wu, Dazhao Du, Jian Liu, Xiaoyi Pang, Jie Zhang, Xiaocheng Lu, Haobin Zhong, Xiaotong Zhao, Alan Zhao, Song Guo
**arXiv:** [arxiv.org/abs/2608.04964](https://arxiv.org/abs/2608.04964)
**Summary:** Interactive video world models are essential for long-horizon planning and exploration, yet they suffer from compounding errors. Post-training methods such as reinforcement learning (RL) can improve these models, but they hit a verification bottleneck: for arbitrary action sequences, no ground-truth future state exists to measure long-term drift.
**Trending because:** 11 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 7. RestoreKV: Recovering Full-Cache Behavior Under Aggressive Query-Agnostic KV Cache Eviction
**Authors:** Changwoo Baek, Seungjun Shin, Kyeongbo Kong
**arXiv:** [arxiv.org/abs/2608.01247](https://arxiv.org/abs/2608.01247)
**Summary:** Query-agnostic KV cache eviction compresses a context once and reuses the resulting cache for arbitrary future queries, but performance can collapse under tight budgets. Existing methods primarily improve which original KV pairs are retained.
**Trending because:** 11 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 8. ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Context Routing
**Authors:** Xu Guo, Zhengxuan Wei, Xinghui Li, Hanzhuo Huang, Xinyu Liu, Xiangyang Luo, Min Wei, Yiran Zhu, Qiulin Wang, Yulong Xu, Xintao Wang, Pengfei Wan, Qi Fan, Xiangwang Hou
**arXiv:** [arxiv.org/abs/2608.04956](https://arxiv.org/abs/2608.04956)
**Summary:** Recent video models increasingly support generation, reference conditioning, and editing within a single model, yet typically expose them as separate operations over fixed inputs. Practical creation unfolds across multiple shots, requiring one model to generate from text, follow a reference, or edit source footage while maintaining shared history.
**Trending because:** 10 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 9. Invisible Shortcuts: Why Vision Encoders Know Your Camera
**Authors:** Vladan Stojnić, Ryan Ramos, Giorgos Kordopatis-Zilos, Noa Garcia, Giorgos Tolias
**arXiv:** [arxiv.org/abs/2608.05424](https://arxiv.org/abs/2608.05424)
**Summary:** Deep vision models exploit shortcuts, relying on cues that correlate with supervision signals. Prior work has focused on visible biases, such as object-background or texture correlations.
**Trending because:** 10 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 10. FinanceHarness: Autonomous Financial Deep Research Framework
**Authors:** Yijia Xiao, Rujun Han, Yanfei Chen, Zifeng Wang, Ke Jiang, Zhongying CuiZhu, Vishy Tirumalashetty, Wei Wang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee
**arXiv:** [arxiv.org/abs/2607.27853](https://arxiv.org/abs/2607.27853)
**Summary:** Powered by advances in LLMs and autonomous agents, deep research has become one of the most widely adopted agentic products. However, most deep research systems write general-purpose reports, which are inadequate for financial deep research.
**Trending because:** 10 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 11. Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for Capability-Selectable Flow Models
**Authors:** Siming Fu, Haojun Xu, Ruizhe He, Zheming Fu, Hualiang Wang, Jie Huang, Xiaoxiao Ma, Mingchen Zhong, Weihu Huang, Xiaoxuan He, Linjiang Huang, Si Liu
**arXiv:** [arxiv.org/abs/2608.04349](https://arxiv.org/abs/2608.04349)
**Summary:** Leading open text-to-image models often carry complementary strengths: one may lead on preference-aligned aesthetics while another follows compositional instructions more faithfully. However, differences in their autoencoders and noise schedules make it difficult to transfer these strengths across models.
**Trending because:** 10 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 12. OPD-V: Visual On-Policy Self-Distillation with Modality Balance
**Authors:** Aniri, Jinhe Bi, Peng Liao, Zengjie Jin, Volker Tresp, Fei Shen, Yunpu Ma, Tat-Seng Chua
**arXiv:** [arxiv.org/abs/2608.05131](https://arxiv.org/abs/2608.05131)
**Summary:** On-Policy Self-Distillation (OPSD) has become a standard post-training approach for improving visual reasoning in multimodal large language models (MLLMs). Existing methods draw privileged information from diverse input sources to guide self-distillation.
**Trending because:** 9 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 13. When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills
**Authors:** Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu
**arXiv:** [arxiv.org/abs/2608.03700](https://arxiv.org/abs/2608.03700)
**Summary:** Persona skills distill personal interaction histories into portable and executable artifacts for downstream agents. While enabling flexible personalization, this process concentrates fragmented personal signals, amplifies their impact through reuse, and challenges defenses designed for individual records or retrieval-based memory.
**Trending because:** 9 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 14. MASS: Multiplayer World Models with Authoritative Shared State
**Authors:** Ziqi Cai, Siqi Yang, Yimu Wang, Zixian Gao, Yunheng Liu, Shuchen Weng, Erwin Wu, Kaipeng Zhang, Boxin Shi
**arXiv:** [arxiv.org/abs/2608.06257](https://arxiv.org/abs/2608.06257)
**Summary:** Current video world models struggle in multiplayer environments because they entangle world state with view-dependent visual latents, leading to redundant compute, view inconsistencies, and poor scalability. We propose MAS (Multiplayer world models with Authoritative Shared State) to resolve this limitation.
**Trending because:** 8 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 15. Push-Wiper: Toward General-Purpose Robotic Cleaning across Varied Stains and Surfaces with Segmented Pushing Trajectories
**Authors:** Renhao Lu, Mingxin Wang, Chenyang Cao, Yang Yang, Guoping Pan, Kangkang Dong, Yi Cheng, Houde Liu
**arXiv:** [arxiv.org/abs/2608.00730](https://arxiv.org/abs/2608.00730)
**Summary:** Viscous stains, characterized by high viscosity and complex rheological properties, remain a major challenge for robotic surface cleaning. Conventional wiping often spreads the stain, while scrubbing provides stronger friction but risks damaging the surface.
**Trending because:** 8 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 16. Consistency-Driven Co-Evolution for Self-Supervised Cross-Representation Learning
**Authors:** Xuehang Guo, Pengyuan Li, Tom Hope, Tirthankar Ghosal, Manling Li, Qingyun Wang
**arXiv:** [arxiv.org/abs/2608.04926](https://arxiv.org/abs/2608.04926)
**Summary:** As chart images, tabular data, and visualization code play increasingly important roles across diverse domains, cross-representation understanding across these modalities poses fundamental challenges for AI systems: the relationships across representations are inherently one-to-many, supervision is ambiguous and costly, and model optimization lacks a principled signal that is both direction-adaptive and representation-generalizable beyond task-specific objectives. We introduce CoCoEvolve to improve consistency across chart, table, and code representations.
**Trending because:** 7 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 17. BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation
**Authors:** Peiyan Li, Yuze Zhu, Yixiang Chen, Qisen Ma, Yuan Xu, Jiabing Yang, He Guan, Yan Huang, Hongtao Wu, Xiao Ma, Tao Kong, Liang Wang, Tieniu Tan
**arXiv:** [arxiv.org/abs/2608.05042](https://arxiv.org/abs/2608.05042)
**Summary:** Leveraging pre-trained vision-language models (VLMs) to construct vision-language-action (VLA) models has emerged as a promising paradigm for 3D robot manipulation. However, existing 3D VLA methods remain data-hungry, exhibit limited generalization under distribution shifts, and lack explicit memory of past observations.
**Trending because:** 7 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 18. UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models
**Authors:** Haiyang Zhou, Wangbo Yu, Chaoran Feng, Xunyu Zhou, Yonghong Tian, Li Yuan
**arXiv:** [arxiv.org/abs/2608.04701](https://arxiv.org/abs/2608.04701)
**Summary:** The abundance of casually captured monocular videos and images on social media provides a valuable source for immersive content creation, where generating novel views from such sparse observations can greatly enhance user experiences. However, producing photorealistic and geometrically consistent views with precise camera control remains challenging when input coverage is extremely limited.
**Trending because:** 7 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 19. Know When to Stop: Segment-Level Credit Assignment for Reducing Overthinking
**Authors:** Chia-Hsuan Lee, Sihui Dai, Mingyang Zhou, Isha Slavin, Hsuan Su, Shi-Xiong Zhang, Sambit Sahu, William Campbell
**arXiv:** [arxiv.org/abs/2607.00482](https://arxiv.org/abs/2607.00482)
**Summary:** Reasoning language models frequently overthink: generating extended chains of behaviors such as hedging, approach abandonment, and self contradiction that consume tokens without improving answers. We show that these behaviors are not merely a consequence of length; even when controlling for response length, incorrect traces exhibit higher rates of unproductive self-reflection than correct ones.
**Trending because:** 7 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---

### 20. PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design Diversity with Editable Print-Ready Outputs
**Authors:** Haojie Hu, Chenhao Dang, Yaojia Liu, Hengrui Kang, Conghui He, Weijia Li
**arXiv:** [arxiv.org/abs/2608.02218](https://arxiv.org/abs/2608.02218)
**Summary:** Scientific poster construction compresses a long multimodal paper into a readable, editable canvas. Existing systems hide request-level failures by scoring only completed outputs; direct image generation is not element-editable, while coding-agent workflows are costly.
**Trending because:** 7 HuggingFace upvotes; among the most-upvoted fresh papers in the current feed.

---
