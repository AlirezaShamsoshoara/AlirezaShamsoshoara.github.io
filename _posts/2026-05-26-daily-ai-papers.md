---
title: "Daily AI Papers — May 26, 2026"
date: 2026-05-26
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-26/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reinforcement-learning
  - agentic-ai
  - multimodal
---

## #1 — DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward Reinforcement Learning

**Authors:** Guochao Jiang, Jingyi Song, Guofeng Quan, Chuzhan Hao, Guohua Liu, Yuewei Zhang  
**arXiv:** [arxiv.org/abs/2605.25604](https://arxiv.org/abs/2605.25604)  
**Sources:** HuggingFace Daily Papers (116 upvotes), arXiv  
**Why trending:** Top upvoted paper on HF today — tackles a core pain point in multi-reward RLHF/GRPO training used widely in LLM post-training pipelines.

DVAO proposes a dynamic weighting scheme for multi-reward reinforcement learning that adjusts combination weights based on empirical reward variance within a rollout group, up-weighting objectives with stronger learning signals while suppressing noisy ones. The method mathematically guarantees bounded advantage magnitudes for training stability and introduces self-adaptive cross-objective regularization, outperforming baselines on Qwen3 and Qwen2.5 models across math reasoning and tool-use benchmarks.

---

## #2 — WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation

**Authors:** Kaining Ying, Hengrui Hu, Siyu Ren, Jiamu Li, Fengjiao Chen, Ziwen Wang, Xuezhi Cao, Xunliang Cai, Henghui Ding  
**arXiv:** [arxiv.org/abs/2605.25874](https://arxiv.org/abs/2605.25874)  
**Sources:** HuggingFace Daily Papers (77 upvotes), arXiv, Papers With Code  
**Why trending:** Fills a gap in world model evaluation as interactive video generation heats up; covers 20 SOTA models with 289 test cases.

WBench introduces a comprehensive multi-turn benchmark for evaluating interactive world models across five dimensions: video quality, setting adherence, interaction adherence, consistency, and physics compliance. It contains 289 test cases and 1,058 interaction turns with 22 automatic sub-metrics combining specialist vision models and LMMs, revealing that no single model excels across all dimensions.

---

## #3 — Macaron-A2UI: A Model for Generative UI in Personal Agents

**Authors:** Fancy Kong, Congjie Zheng, Murphy Zhuang, Rio Yang, Sueky Zhang, Hao Fu, Gene Jin, Song Cao, Kaijie Chen, Andrew Chen, Pony Ma  
**arXiv:** [arxiv.org/abs/2605.24830](https://arxiv.org/abs/2605.24830)  
**Sources:** HuggingFace Daily Papers (66 upvotes), arXiv  
**Why trending:** Addresses the next frontier of agentic AI: dynamic UI generation for personal agents, moving beyond plain-text chat interfaces.

Macaron-A2UI proposes a generative UI model that dynamically synthesizes controls, options, and interactive state directly from personal agent conversation context, replacing static chat interfaces with rich, context-aware UI components. The system enables personal agents to handle complex user-centric tasks through an adaptive interface layer that evolves with the interaction in real time.

---

## #4 — Foundation Protocol: A Coordination Layer for Agentic Society

**Authors:** Bang Liu, Yongfeng Gu, Jiayi Zhang, Zhaoyang Yu  
**arXiv:** [arxiv.org/abs/2605.23218](https://arxiv.org/abs/2605.23218)  
**Sources:** HuggingFace Daily Papers (56 upvotes), arXiv, Reddit r/MachineLearning  
**Why trending:** Timely systems-level paper as multi-agent deployments scale — treats agent coordination as social infrastructure, not just API calls.

Foundation Protocol proposes a coordination layer for networks of autonomous agents that addresses the bottleneck of multi-agent coordination as agents increasingly browse, purchase, deploy software, manage systems, and interact with one another. The protocol establishes shared conventions for inter-agent communication, trust, and task delegation, enabling agentic society to scale beyond the limits of raw model capability.

---

## #5 — TriSplat: Simulation-Ready Feed-Forward 3D Scene Reconstruction

**Authors:** Weijie Wang, Zimu Li, Jinchuan Shi, Zeyu Zhang  
**arXiv:** [arxiv.org/abs/2605.26115](https://arxiv.org/abs/2605.26115)  
**Sources:** HuggingFace Daily Papers (34 upvotes), arXiv, Papers With Code  
**Why trending:** Bridges the gap between Gaussian splatting and simulation-ready meshes, directly relevant to robotics and embodied AI.

TriSplat introduces a feed-forward 3D reconstruction approach that predicts simulation-ready explicit primitives directly from sparse-view images, going beyond Gaussian splatting by producing usable triangle mesh surfaces for downstream simulation. The method addresses the challenge of extracting clean meshes from sparse-view reconstruction, making it immediately applicable to robotics, games, and embodied AI simulation environments.

---

## #6 — ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning

**Authors:** Zuhao Yang, Kaichen Zhang, Sudong Wang, Keming Wu  
**arXiv:** [arxiv.org/abs/2605.20342](https://arxiv.org/abs/2605.20342)  
**Sources:** HuggingFace Daily Papers (29 upvotes), arXiv  
**Why trending:** Parallel tool calling in video RL agents is a hot topic — solving sequential bottlenecks is key for long-video understanding.

ParaVT addresses the "tool prior paradox" in agentic video RL, where existing native-RL methods dispatch video-processing tool calls sequentially (one per turn), creating a single-writer bottleneck that limits parallelism and long-video understanding. The method enables large multimodal models to invoke multiple video tools in parallel within a single turn, significantly improving throughput and long-horizon video reasoning performance.

---

## #7 — Toward Native Multimodal Modeling: A Roadmap

**Authors:** Siyu An, Junru Lu, Junnan Dong, Qiufeng Wang  
**arXiv:** [arxiv.org/abs/2605.25343](https://arxiv.org/abs/2605.25343)  
**Sources:** HuggingFace Daily Papers (28 upvotes), arXiv  
**Why trending:** Comprehensive survey and roadmap bridging the gap from late-fusion VLMs to true native multimodal architectures.

This paper presents a structured roadmap for native multimodal modeling, tracing the evolution from late-fusion approaches (encoders + frozen LLM backbones) toward architectures that natively process and reason across modalities without modality-specific wrappers. The work identifies key open challenges and design principles for unified models that achieve world-modeling-level understanding, rather than modality-agnostic reasoning.

---

## #8 — ThriftAttention: Selective Mixed Precision for Long-Context FP4 Attention

**Authors:** Joe Sharratt  
**arXiv:** [arxiv.org/abs/2605.23081](https://arxiv.org/abs/2605.23081)  
**Sources:** HuggingFace Daily Papers (22 upvotes), arXiv  
**Why trending:** FP4/low-precision attention for long-context inference is a hot engineering challenge; directly relevant to Blackwell GPU users.

ThriftAttention proposes selective mixed-precision attention that overcomes the accuracy limitations of uniform block-scaled FP4 quantization on long-context workloads for Blackwell GPUs. By identifying which attention blocks require higher precision and applying FP4 only where safe, the method achieves near-lossless inference at 4-bit precision with significant speedups over FP16 baselines.

---

## #9 — QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks

**Authors:** Jian Xie, Tianhe Lin, Zilu Wang, Yuting Ning  
**arXiv:** [arxiv.org/abs/2605.24218](https://arxiv.org/abs/2605.24218)  
**Sources:** HuggingFace Daily Papers (21 upvotes), arXiv  
**Why trending:** Open training data for deep research agents is scarce — fully synthetic tasks are a path to democratizing frontier research agent training.

QUEST addresses the training data bottleneck for deep research agents by generating fully synthetic search-and-synthesis tasks, enabling open training of agents that generalize beyond proprietary systems. The approach constructs verifiable synthetic tasks that mirror real deep research workflows (literature search, knowledge synthesis, multi-hop reasoning), producing agents that close the gap with frontier proprietary systems.

---

## #10 — AutoResearch AI: Towards AI-Powered Research Automation for Scientific Discovery

**Authors:** Guiyao Tie, Jiawen Shi, Dingjie Song, Yixiao Huang  
**arXiv:** [arxiv.org/abs/2605.23204](https://arxiv.org/abs/2605.23204)  
**Sources:** HuggingFace Daily Papers (21 upvotes), arXiv, Reddit r/MachineLearning  
**Why trending:** End-to-end AI research pipelines are a major trend; this paper tackles the full workflow from literature to experiment to revision.

AutoResearch AI presents a framework for AI-powered automation of the full scientific research workflow, spanning literature grounding, hypothesis generation, experimentation, validation, reporting, and revision — moving beyond task-level AI tools toward longer-horizon research agents. The work marks a transition from narrow AI assistance to systemic research automation that can iteratively improve hypotheses based on experimental feedback.

---

## #11 — Your Embedding Model is SMARTer Than You Think

**Authors:** Jianrui Zhang, Hyun Jung Lee, Sukanta Ganguly, Tae-Eui Kam  
**arXiv:** [arxiv.org/abs/2605.24938](https://arxiv.org/abs/2605.24938)  
**Sources:** HuggingFace Daily Papers (17 upvotes), arXiv, Papers With Code  
**Why trending:** Challenges the assumption that single-vector embeddings are inherently inferior to multi-vector approaches for dense retrieval.

SMART demonstrates that single-vector embedding models retain more fine-grained local information than commonly assumed, and proposes lightweight mechanisms to unlock this latent capacity for dense retrieval tasks without the overhead of full multi-vector approaches. The work shows that properly exploited single-vector retrievers can match or exceed multi-vector systems on standard benchmarks, closing a long-held performance gap.

---

## #12 — ControlLight: Towards Controllable, Consistent, and Generalizable Low-Light Enhancement

**Authors:** Yufeng Yang, Jianzhuang Liu, Jisheng Chu, Yuqi Peng  
**arXiv:** [arxiv.org/abs/2605.25569](https://arxiv.org/abs/2605.25569)  
**Sources:** HuggingFace Daily Papers (15 upvotes), arXiv, Papers With Code  
**Why trending:** Low-light enhancement with fine-grained control is critical for mobile photography and surveillance; strong generalization is a key gap.

ControlLight introduces a framework for low-light image enhancement that enables controllable, consistent, and generalizable enhancement across diverse lighting conditions. The method achieves user-controllable brightness and style while maintaining color consistency and generalizing to unseen degradations beyond its training distribution.

---

## #13 — Pantheon360: Taming Digital Twin Generation via 3D-Aware 360° Video Diffusion

**Authors:** Ting-Hsuan Chen, Ying-Huan Chen, Tao Tu, Jie-Ying Lee  
**arXiv:** [arxiv.org/abs/2605.25449](https://arxiv.org/abs/2605.25449)  
**Sources:** HuggingFace Daily Papers (15 upvotes), arXiv  
**Why trending:** 3D-aware 360° video generation is a key enabler for immersive digital twins and embodied AI training environments.

Pantheon360 proposes a 3D-aware diffusion framework for generating consistent 360° video for digital twins, addressing the geometric inconsistency issues that plague standard video diffusion when applied to omnidirectional video synthesis. The method leverages 3D scene structure to enforce multi-view consistency across full-sphere video frames, enabling high-quality digital twin generation for simulation and VR.

---

## #14 — CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents

**Authors:** Bowen Wang, Dunjie Lu, Junli Wang, Tianyi Bai  
**arXiv:** [arxiv.org/abs/2605.25624](https://arxiv.org/abs/2605.25624)  
**Sources:** HuggingFace Daily Papers (13 upvotes), arXiv  
**Why trending:** RLVR for computer-use agents has been bottlenecked by training data scarcity; this directly addresses that gap.

CUA-Gym tackles the scalability bottleneck in training computer-use agents (CUAs) with RLVR by providing a scalable gym of verifiable training environments with deterministic rewards across diverse computer interaction tasks. The framework scales task generation and environment construction to the point where computer-use agents can be trained with RL signals comparable to what math and code agents enjoy.

---

## #15 — Anticipate and Learn: Unleashing Idle-Time Compute in Proactive Agents

**Authors:** Haoyi Hu, Qirong Lyu, Xianghan Kong, Weiwen Liu  
**arXiv:** [arxiv.org/abs/2605.25971](https://arxiv.org/abs/2605.25971)  
**Sources:** HuggingFace Daily Papers (12 upvotes), arXiv  
**Why trending:** Idle-time compute utilization in always-on AI agents is an underexplored efficiency frontier with high practical impact.

This paper proposes proactive agents that utilize idle time between user prompts to anticipate likely future requests and pre-compute partial responses, transforming reactive AI assistants into always-learning systems that reduce perceived latency. The approach shifts agent computation from purely reactive to speculative, demonstrating significant improvements in response quality and latency for agentic workflows.

---

## #16 — On-Policy Adversarial Flow Distillation for Autoregressive Video Generation

**Authors:** Yang Luo, Shengju Qian, Xiaohang Tang, Zirui Zhu  
**arXiv:** [arxiv.org/abs/2605.26105](https://arxiv.org/abs/2605.26105)  
**Sources:** HuggingFace Daily Papers (12 upvotes), arXiv  
**Why trending:** Distilling causal video generators from black-box teachers is a key challenge for streaming/interactive video generation at scale.

This work introduces on-policy adversarial flow distillation for training autoregressive video generators from strong black-box teacher models, addressing the distribution mismatch that arises when causal students must learn under their own rollout distribution. The adversarial distillation framework produces high-quality causal video generation models suitable for streaming and interactive applications without requiring access to teacher internals.

---

## #17 — Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World

**Authors:** Yusong Lin, Xinyuan Liang, Haiyang Wang, Qipeng Gu  
**arXiv:** [arxiv.org/abs/2605.26086](https://arxiv.org/abs/2605.26086)  
**Sources:** HuggingFace Daily Papers (11 upvotes), arXiv  
**Why trending:** Always-on personal AI assistants with broad digital world access are the next frontier; this benchmark fills a critical evaluation gap.

Claw-Anything benchmarks LLM-based personal assistants that operate with access to a broad slice of the user's digital world (files, apps, communication, calendar, etc.), evaluating context-sensitive reasoning and assistance quality across realistic always-on scenarios. The work identifies the key limitations of current narrow-context systems and provides a systematic evaluation framework for broader-access agents.

---

## #18 — SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills

**Authors:** Yingtie Lei, Zhongwei Wan, Jiankun Zhang, Samiul Alam  
**arXiv:** [arxiv.org/abs/2605.24117](https://arxiv.org/abs/2605.24117)  
**Sources:** HuggingFace Daily Papers (10 upvotes), arXiv  
**Why trending:** Skill distillation from agent trajectories is a core question for long-horizon AI agents; this benchmark provides the first systematic evaluation.

SkillEvolBench introduces a diagnostic benchmark for evaluating whether LLM agents can distill rich episodic task trajectories into reusable procedural skills, testing the critical step from episodic memory to generalizable skill formation. The benchmark reveals key bottlenecks in current agent architectures' ability to extract procedural knowledge from experience, providing a roadmap for improving long-horizon agent learning.

---

## #19 — Channel-wise Vector Quantization

**Authors:** Wei Song, Tianhang Wang, Yitong Chen, Tong Zhang  
**arXiv:** [arxiv.org/abs/2605.26089](https://arxiv.org/abs/2605.26089)  
**Sources:** HuggingFace Daily Papers (8 upvotes), arXiv, Papers With Code  
**Why trending:** A novel tokenization paradigm that challenges the dominant patch-wise VQ approach for image generation and compression.

Channel-wise Vector Quantization (CVQ) proposes a fundamentally different image tokenization approach that quantizes individual feature map channels rather than patch-wise feature vectors, producing channel tokens instead of spatial tokens. This rethinking of VQ enables richer codebook utilization and better reconstruction quality by disentangling the spatial and channel dimensions of learned image representations.

---

## #20 — MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing

**Authors:** Han Chen, Zining Zhang, Wenqi Pei, Bingsheng He  
**arXiv:** [arxiv.org/abs/2605.23986](https://arxiv.org/abs/2605.23986)  
**Sources:** HuggingFace Daily Papers (8 upvotes), arXiv  
**Why trending:** Efficient long-context memory for agents is a persistent infrastructure challenge; hierarchical temporal indexing is a practical solution.

MemForest proposes a hierarchical temporal indexing approach for agent memory systems that addresses the high maintenance overhead of existing memory architectures, enabling efficient serve-and-update lifecycles across long multi-session interactions. The forest-structured memory index reduces retrieval latency and update cost while maintaining high recall, providing a practical foundation for persistent-state LLM agents.
