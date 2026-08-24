---
title: "Daily AI Papers — August 24, 2026"
date: 2026-08-24
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-24/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - mixture-of-experts
  - efficient-inference
  - llm-agents
---

### 1. Let's Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Scale Mixture-of-Experts
**Authors:** Nayeon Kim, Hojin Lee, Yunju Bak, Jaesun Park, Boseop Kim
**arXiv:** [arxiv.org/abs/2608.20061](https://arxiv.org/abs/2608.20061)
**Summary:** Mixture-of-Experts (MoE) architectures significantly expand model capacity without a proportional increase in computational cost. However, optimizing their hyperparameters---particularly the learning rate---at extreme scales of both model size and token budget via sweeping remains computationally prohibitive.
**Trending because:** 31 HuggingFace upvotes + practical gains in efficient/on-device inference

---

### 2. InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter
**Authors:** Yunze Tong, Mushui Liu, Canyu Zhao, Shiyi Zhang, Didi Zhu, Peng Zhang, Wanggui He, Jinlong Liu, Ying Chen, Hao Jiang, Pipei Huang, Bo Zheng
**arXiv:** [arxiv.org/abs/2608.20910](https://arxiv.org/abs/2608.20910)
**Summary:** With large pretrained models, existing methods have effectively improved instruction-based video editing. However, most of them rely on an in-place editing assumption.
**Trending because:** 30 HuggingFace upvotes + an eye-catching result in generative video

---

### 3. Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence
**Authors:** Yuyuan Feng, Zhishang Xiang, Chaobin Yang, Qichao Ma, Zerui Chen, Yujing Zhang, Ke Huang, Chuanjie Wu, Zhaoxu Liu, Yili Wang, Xin He, Jiapu Wang, Zijin Hong, Hao Chen, Yuanchen Bei, Kun Wang, Shengyuan Chen, Ningyu Zhang, Enyan Dai, Linhao Luo, Qingyi Pan, Qi Wang, Wenqi Fan, Guangjing Wang, Na Zou, Yangqiu Song, Xin Wang, Zechao Li, Xia Hu, Qing Li, Xiao Huang, Zhihong Zhang, Jinsong Su, Qinggang Zhang, Yi Chang
**arXiv:** [arxiv.org/abs/2608.21156](https://arxiv.org/abs/2608.21156)
**Summary:** LLMs have evolved from language generators to autonomous agents capable of complex, long-horizon tasks. This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering to manage information access, Harness Engineering to organize external tools and resources, and Loop Engineering to support continual reflection and self-improvement.
**Trending because:** 29 HuggingFace upvotes + timely work on LLM agents

---

### 4. OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs
**Authors:** Xianyun Sun, Chaoyou Fu, Zhengye Zhang, Feiyang Duan, Qingyuan Cao, Yonghui Niu, Sihang Yuan, Ge Zhang, Caifeng Shan
**arXiv:** [arxiv.org/abs/2608.21360](https://arxiv.org/abs/2608.21360)
**Summary:** Recent omni-modal large language models (Omni-LLMs) show great potential as real-time video assistants, which continuously perceive environments and guide users to achieve specific goals. Unlike traditional passive video understanding, interactive assistants should actively combine visual states, user goals, and prior knowledge to provide effective help.
**Trending because:** 25 HuggingFace upvotes + a fresh benchmark drawing community attention

---

### 5. ParaTempo: Efficient Parallel Reasoning via Temporal Confidence
**Authors:** Xuteng Zhang, Wenhao Zeng, Xiaodong Gu, Chao Hu, Haotian Lin, Yuling Shi, Min Wang, Beijun Shen
**arXiv:** [arxiv.org/abs/2608.16425](https://arxiv.org/abs/2608.16425)
**Summary:** Parallel reasoning improves the accuracy and robustness of large reasoning models by exploring multiple solution paths, but its computational cost grows with reasoning depth and branch count. Existing methods for managing these parallel paths typically rely on final-answer consensus, local token confidence, or isolated intermediate probes.
**Trending because:** 25 HuggingFace upvotes + practical gains in efficient/on-device inference

---

### 6. FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills
**Authors:** Zeyu Ren, Ling Yue, Ran Li, Yishu Wang, Shengxiang Xu, Hanmo Liu, Shaowu Pan, Shimin Di
**arXiv:** [arxiv.org/abs/2607.21596](https://arxiv.org/abs/2607.21596)
**Summary:** Large language model agents can adapt to complex tasks by constructing workflows at inference time, but procedures discovered in one episode are usually discarded after execution. Existing skill libraries provide reusable executable routines, but are typically assembled offline and do not grow from the agent's own workflows.
**Trending because:** 16 HuggingFace upvotes + timely work on LLM agents

---

### 7. Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation of Large Language Models
**Authors:** Zhaoyi Li, Deyang Kong, Yuan Wei, Evan Yang, Ranran Shen, Mahardika Krisna Ihsani, Ming Yang, Wei Zhang, Chuan Hao, Jian Yang, Ran Tao, Bryan Dai, Shikun Zhang, Wei Ye, Ying Wei, Defu Lian
**arXiv:** [arxiv.org/abs/2608.16647](https://arxiv.org/abs/2608.16647)
**Summary:** On-policy distillation (OPD) transfers teacher capabilities by supervising trajectories sampled from the student's own policy, yet its generalization behavior remains poorly understood, as most studies evaluate OPD on a single domain and on benchmarks close to the training data. We present a controlled study that varies one generalization factor at a time, from in-domain distribution shifts to cross-domain transfer and the multi-teacher setting.
**Trending because:** 14 HuggingFace upvotes + a fresh benchmark drawing community attention

---

### 8. EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking
**Authors:** Enjun Du, Siyi Liu, Zirong Chen, Xinyu Zuo, Jinwen Luo, Ruiwen Tao, Lisheng Duan, Haijin Liang, Jin Ma, Junfu Pu, Yongqi Zhang
**arXiv:** [arxiv.org/abs/2608.20886](https://arxiv.org/abs/2608.20886)
**Summary:** Real-world image search queries are multimodal and compositional: ``find this shirt in pink'' specifies an entity to retain, an attribute to modify, and context to ignore. Yet existing re-rankers either compress such multifaceted relevance into an opaque embedding or rely on free-form chain-of-thought that easily omits or hallucinates fine-grained constraints.
**Trending because:** 10 HuggingFace upvotes + a strong multimodal/vision contribution

---

### 9. Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Thinking MLLMs
**Authors:** Xinming Wang, Weinong Wang, Hongming Yang, Yansong Lin, Zheng Ruan, Shangpin Peng, Qiming Peng, Nan Qiao, Fengyuan Lu, Guoqing Ma, Marito Li, Songyang Zhang, Saiyong Yang, Han Hu, Yonglong Tian, Xu-Yao Zhang
**arXiv:** [arxiv.org/abs/2608.12781](https://arxiv.org/abs/2608.12781)
**Summary:** Hybrid-thinking multimodal large language models (MLLMs) allow a single model to alternate between deliberative thinking and latency-efficient non-thinking inference. Although these modes differ in reasoning budget, their delivered responses should satisfy the same user-facing standard.
**Trending because:** 7 HuggingFace upvotes + a fresh benchmark drawing community attention

---

### 10. UniSpace: Unified Visual Representation and Scalable Multimodal Modeling
**Authors:** Jinbo Yan, Limeng Qiao, Jie Qin, Junyan He, Feize Wu, Guanglu Wan
**arXiv:** [arxiv.org/abs/2608.08676](https://arxiv.org/abs/2608.08676)
**Summary:** Semantic vision encoders have become a central visual interface for multimodal understanding and semantic conditioning in image generation. However, their final tokens discard fine-grained visual details, leading to poor pixel reconstruction and limiting their use in reconstruction-sensitive tasks such as image generation and editing.
**Trending because:** 7 HuggingFace upvotes + an eye-catching result in generative video

---

### 11. AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business Scenarios at scale
**Authors:** Minbyul Jeong, Chanwoong Yoon
**arXiv:** [arxiv.org/abs/2608.20634](https://arxiv.org/abs/2608.20634)
**Summary:** Agents learn to act through interaction with environments, yet the environments used for training are often manually constructed or synthesized around predefined tasks and benchmarks. This task-centric paradigm makes it difficult to scale environments that reflect realistic and evolving workflows where diverse tasks can naturally emerge from the underlying world.
**Trending because:** 5 HuggingFace upvotes + a fresh benchmark drawing community attention

---

### 12. Towards Faithful Simulation of Human Shopping Behavior
**Authors:** Jiakai Tang, Yan Mi, Jing Yu, Yang Zhang, See-Kiong Ng, Qi Cao, Fei Sun, Xu Chen, Wen Chen, Jian Wu, Han Zhu, Bo Zheng
**arXiv:** [arxiv.org/abs/2608.20707](https://arxiv.org/abs/2608.20707)
**Summary:** Simulating realistic user shopping behavior underpins offline evaluation and reinforcement learning in e-commerce scenarios. While recent LLM- and VLM-based simulators have made encouraging progress, reproducing a real browsing session remains difficult for two reasons.
**Trending because:** 4 HuggingFace upvotes + a distinctive applied-domain study

---

### 13. Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs
**Authors:** Luka Ribar, Jeevan Bhoot, Douglas Orr
**arXiv:** [arxiv.org/abs/2608.21134](https://arxiv.org/abs/2608.21134)
**Summary:** Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements. We present a framework for quantizing VLMs for efficient inference on resource-constrained hardware.
**Trending because:** 4 HuggingFace upvotes + practical gains in efficient/on-device inference

---

### 14. Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference
**Authors:** Christos Koutsiaris
**arXiv:** [arxiv.org/abs/2608.20210](https://arxiv.org/abs/2608.20210)
**Summary:** Small language models are usually built like large ones and then squeezed onto a CPU afterwards. We did the opposite: we fixed the target first, one user, one token at a time, 4-bit weights, ordinary CPU, and chose the architecture to suit it.
**Trending because:** 4 HuggingFace upvotes + practical gains in efficient/on-device inference

---

### 15. Human-Centric Intelligence in the Era of Foundation Models: A Survey
**Authors:** Yang Chen, Tianqi Wang, Xiaorui Jiang, Yilei Man, Yihua Shao, Mengyuan Liu, Zhi Chen, Xiaofeng Cao, Qibin Zhao, Chi Harold Liu, Albert Y. Zomaya, Nicu Sebe, Jingren Zhou, Dacheng Tao, Song Guo, Jingcai Guo
**arXiv:** [arxiv.org/abs/2608.18184](https://arxiv.org/abs/2608.18184)
**Summary:** Human-centric intelligence is evolving in the foundation-model era, with growing emphasis on scale, transferability, and general-purpose modeling. Yet it has not fully integrated with foundation models to achieve the comparable progress seen in them.
**Trending because:** 4 HuggingFace upvotes + a broad survey resonating with the field

---

### 16. Evaluating Music Context Preservation: A Multi-facet Framework for Music Editing Systems
**Authors:** Yash Vishe, Eric Xue, Xunyi Jiang, Zachary Novack, Junda Wu, Julian McAuley, Xin Xu
**arXiv:** [arxiv.org/abs/2512.14629](https://arxiv.org/abs/2512.14629)
**Summary:** Music editing plays a vital role in modern music production, with applications in film, broadcasting, and game development. Recent advances in music editing systems have enabled diverse editing tasks such as timbre transfer, instrument substitution, and genre transformation.
**Trending because:** 3 HuggingFace upvotes + an eye-catching result in generative video

---

### 17. Towards Real-Time and Adaptable LiDAR Scene Completion
**Authors:** Azhar Hussian, Martin Vossiek, Vasileios Belagiannis
**arXiv:** [arxiv.org/abs/2608.16490](https://arxiv.org/abs/2608.16490)
**Summary:** LiDAR scene completion is a key component of 3D perception in autonomous driving, where the scene must be completed in real time to be usable in downstream tasks. Existing approaches typically follow an initialize-and-refine paradigm, in which a coarse initialization of the scene is first constructed, then refined into complete 3D geometry.
**Trending because:** 3 HuggingFace upvotes + a strong multimodal/vision contribution

---

### 18. CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment
**Authors:** Chengxiao Wang, Enyi Jiang, Xiaojing Liao, Sanmi Koyejo
**arXiv:** [arxiv.org/abs/2608.21278](https://arxiv.org/abs/2608.21278)
**Summary:** Improving the safety of large language models (LLMs) often comes at the expense of utility, as globally applied safety tuning may affect model responses to both harmful and benign inputs. We propose Continuous LatEnt Adapter Routing (CLEAR), a conditional safety adaptation framework that uses a lightweight hidden-state gate to continuously control the activation strength of a safety low-rank adapter.
**Trending because:** 2 HuggingFace upvotes + a well-received recent contribution

---

### 19. Peer-Voted LLM-Agent Stress Tests Find Feed-Induced Lexical Convergence but No Reliable Matched-Exposure Advantage for Distributed Sources
**Authors:** Rana Muhammad Usman, Dominic Williamson
**arXiv:** [arxiv.org/abs/2608.20438](https://arxiv.org/abs/2608.20438)
**Summary:** Population-level behavior in large-language-model (LLM) agents cannot be characterized by single-agent benchmarks. We introduce PV-SST, a peer-voted social-platform testbed, and report a separately frozen, preregistered matched-exposure experiment spanning four topics, four unused seeds, four open-weight model families, and three prespecified larger variants.
**Trending because:** 2 HuggingFace upvotes + a fresh benchmark drawing community attention

---

### 20. Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models
**Authors:** Pardis Taghavi, Reza Langari, Gaurav Pandey
**arXiv:** [arxiv.org/abs/2608.18484](https://arxiv.org/abs/2608.18484)
**Summary:** Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sparse operator. Queries sharing a block route may have poorly overlapping supports, while retained attention mass alone does not determine the post-softmax error from skipped interactions.
**Trending because:** 2 HuggingFace upvotes + an eye-catching result in generative video

---
