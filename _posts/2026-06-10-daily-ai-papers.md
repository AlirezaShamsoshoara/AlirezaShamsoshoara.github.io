---
title: "Daily AI Papers — June 10, 2026"
date: 2026-06-10
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-10/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal
  - llm-rl
  - agentic-ai
---

## 1. Kwai Keye-VL-2.0 Technical Report

**Authors:** Kwai Keye Team, Bin Wen, Changyi Liu et al.
**arXiv:** [arxiv.org/abs/2606.10651](https://arxiv.org/abs/2606.10651)
**Sources:** HuggingFace Daily Papers
**Why trending:** Major open-source MoE multimodal foundation model from Kwai designed for hour-level video understanding with agentic capabilities — directly competitive with frontier closed models.

Kwai Keye-VL-2.0-30B-A3B is an open-source Mixture-of-Experts multimodal model that introduces adaptive token compression to handle ultra-long video contexts (hour-level) that would otherwise incur prohibitive compute costs. It represents the first MoE architecture adapted specifically for long-video understanding and advances the state of the art in agentic video intelligence.

---

## 2. ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations

**Authors:** Junke Wang, Xiao Wang, Jiacheng Pan et al.
**arXiv:** [arxiv.org/abs/2606.11188](https://arxiv.org/abs/2606.11188)
**Sources:** HuggingFace Daily Papers
**Why trending:** Unifies image understanding, generation, and editing in a single next-token prediction framework using discrete representations — a major architectural step toward truly unified multimodal AI.

ARM trains a discrete semantic visual tokenizer that maps images into compact token sequences, enabling a unified autoregressive model to handle image understanding, generation, and editing tasks under a single next-token prediction objective. The tokenizer is supervised with multiple objectives promoting both semantic discriminability and visual reconstruct-ability, achieving strong performance across all three modalities.

---

## 3. Rethinking the Divergence Regularization in LLM RL

**Authors:** Jiarui Yao, Xiangxin Zhou, Penghui Qi et al.
**arXiv:** [arxiv.org/abs/2606.09821](https://arxiv.org/abs/2606.09821)
**Sources:** HuggingFace Daily Papers
**Why trending:** Fundamentally challenges the importance-ratio clipping mechanism used in PPO and GRPO — the backbone of essentially all modern LLM RL post-training pipelines.

This paper argues that ratio-clipping in PPO and GRPO is a poor approximation for trust-region control in off-policy LLM RL settings, since the importance ratio can be a poor divergence proxy when policy staleness is high. The authors propose an improved divergence regularization approach that better handles training-inference mismatch and produces more stable, efficient LLM RL training.

---

## 4. Flow-DPPO: Divergence Proximal Policy Optimization for Flow Matching Models

**Authors:** Bowen Ping, Xiangxin Zhou, Penghui Qi et al.
**arXiv:** [arxiv.org/abs/2606.11025](https://arxiv.org/abs/2606.11025)
**Sources:** HuggingFace Daily Papers
**Why trending:** Extends the "RL for generative models" paradigm to flow matching, applying principled trust-region optimization to the next generation of image and video generators.

Flow-DPPO introduces a divergence-based proximal policy optimization method specifically designed for flow matching generative models, arguing that PPO-style ratio clipping (as used in Flow-GRPO and CPS) is theoretically inappropriate for continuous-time flow processes. The method achieves better quality and alignment improvements on image and video generation tasks while maintaining more stable training dynamics.

---

## 5. WorldOlympiad: Can Your World Model Survive a Triathlon?

**Authors:** Yuke Zhao, Wangbo Zhao, Weijie Wang et al.
**arXiv:** [arxiv.org/abs/2606.11129](https://arxiv.org/abs/2606.11129)
**Sources:** HuggingFace Daily Papers
**Why trending:** New comprehensive benchmark filling a critical gap in world model evaluation — testing physical faithfulness, geometric consistency, and interaction fidelity simultaneously.

WorldOlympiad diagnoses video-based world models across three axes — physical faithfulness, geometric consistency, and interaction fidelity — that existing benchmarks (focused on visual quality or short-term coherence) fail to assess. The benchmark provides systematic tools to determine whether generated videos truly obey physical laws, preserve 3D structure, and respond correctly to interventions.

---

## 6. SearchSwarm: Towards Delegation Intelligence in Agentic LLMs for Long-Horizon Deep Research

**Authors:** Pu Ning, Quan Chen, Kun Tao et al.
**arXiv:** [arxiv.org/abs/2606.09730](https://arxiv.org/abs/2606.09730)
**Sources:** HuggingFace Daily Papers
**Why trending:** Addresses the fundamental context-window bottleneck in multi-agent deep research through principled task delegation and summarization — directly relevant to the agentic research trend.

SearchSwarm proposes a delegation-intelligence framework where a main agent decomposes long-horizon research tasks into subtasks dispatched to specialized subagents, which execute and return only concise summaries rather than full results, circumventing finite context window limitations. This paradigm enables scalable deep research that grows with task complexity without hitting model context limits.

---

## 7. MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding

**Authors:** Cong Chen, Guo Gan, Kaixiang Ji et al.
**arXiv:** [arxiv.org/abs/2606.07512](https://arxiv.org/abs/2606.07512)
**Sources:** HuggingFace Daily Papers
**Why trending:** Elegant solution to the hours-long video understanding problem by converting it into an agentic exploration process backed by hierarchical graph memory.

MemDreamer decouples perception and reasoning for long video understanding, replacing token-explosion-prone full-sequence processing with an agentic retrieval mechanism over hierarchical graph memory. As a plug-and-play framework, it allows existing VLMs to selectively retrieve and reason over relevant video segments without processing entire hour-long sequences, achieving strong results on long-video QA benchmarks.

---

## 8. Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution

**Authors:** Xucong Wang, Ziyu Ma, Shidong Yang et al.
**arXiv:** [arxiv.org/abs/2606.10917](https://arxiv.org/abs/2606.10917)
**Sources:** HuggingFace Daily Papers
**Why trending:** Novel dual-role training mechanism that overcomes the static environment and sparse feedback limitations that currently bottleneck LLM agent generalization.

Role-Agent introduces a framework where LLM agents bootstrap their own capabilities through dual-role evolution — alternating between task-solving and environment-generation roles — generating progressively more challenging and diverse training scenarios. This self-improving feedback loop addresses the key limitation of static training environments and enables significantly better generalization to new complex tasks.

---

## 9. ABot-Earth 0.5: Generative 3D Earth Model

**Authors:** Ming Qian, Tianjian Ouyang, Mingchao Sun et al.
**arXiv:** [arxiv.org/abs/2606.09967](https://arxiv.org/abs/2606.09967)
**Sources:** HuggingFace Daily Papers
**Why trending:** First generative model capable of synthesizing vast, globally consistent 3D environments from satellite imagery using 3DGS — impressive applications for simulation and geospatial AI.

ABot-Earth 0.5 is a generative 3D framework that synthesizes seamless, large-scale 3D environments directly from geospatially referenced satellite imagery using a novel model formulated in the 3D Gaussian Splatting representation. Trained on diverse real-world satellite data, the model generates globally consistent 3D earth environments, enabling applications in autonomous system simulation, digital twins, and geospatial intelligence.

---

## 10. Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts

**Authors:** Wenbo Pan, Shujie Liu, Chin-Yew Lin et al.
**arXiv:** [arxiv.org/abs/2606.05922](https://arxiv.org/abs/2606.05922)
**Sources:** HuggingFace Daily Papers
**Why trending:** Solves the practical challenge of continually improving LLM agent harnesses in deployment settings where labeled validation data is unavailable.

Retrospective Harness Optimization (RHO) enables continuous improvement of LLM agent skills, tools, and workflows by exploiting the model's own self-preference over different trajectory rollouts, eliminating the need for labeled ground-truth data. By comparing rollouts and using model-internal preference signals, RHO adapts agent harnesses to new tasks in practical deployment settings, directly improving real-world agent performance.

---

## 11. How Does Reasoning Flow? Tracing Attention-Induced Information Flow for Targeted RL in LLMs

**Authors:** Zhichen Dong, Yang Li, Yuhan Sun et al.
**arXiv:** [arxiv.org/abs/2606.10646](https://arxiv.org/abs/2606.10646)
**Sources:** HuggingFace Daily Papers
**Why trending:** Provides mechanistic insight into token-level credit assignment in LLM RL by tracing attention flow — practical implications for improving PPO/GRPO efficiency and reasoning quality.

This paper addresses token-level credit assignment in LLM RL by tracing attention-induced information flow across reasoning chains, identifying which tokens are genuinely decisive versus routine formatting or filler. By leveraging internal attention signals as a global (not just point-wise) credit signal, targeted RL updates significantly improve reasoning performance while avoiding wasteful gradient updates on trivial tokens.

---

## 12. Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall, and How to Fix It

**Authors:** Xinyu Zhou, Boyu Zhu, Yi Xu et al.
**arXiv:** [arxiv.org/abs/2606.11052](https://arxiv.org/abs/2606.11052)
**Sources:** HuggingFace Daily Papers
**Why trending:** Reveals a critical and surprising failure mode: CoT SFT systematically degrades long-context recall in hybrid linear-attention models — actionable finding for anyone training hybrid architectures.

This paper discovers that chain-of-thought supervised fine-tuning systematically causes "attention amnesia" in hybrid linear-attention models (HypeNet, Jet-Nemotron), with Needle-In-A-Haystack retrieval performance deteriorating substantially and worsening with harder retrieval tasks. The authors identify the root cause and propose targeted fixes that restore long-range recall while preserving the reasoning improvements from CoT training.

---

## 13. EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents

**Authors:** Weixian Xu, Shilong Liu, Mengdi Wang et al.
**arXiv:** [arxiv.org/abs/2606.11182](https://arxiv.org/abs/2606.11182)
**Sources:** HuggingFace Daily Papers
**Why trending:** First multi-dataset test-time prompt learning framework for LLM agents — enables adaptation to heterogeneous real-world task streams without labeled data.

EEVEE is the first multi-dataset test-time prompt learning framework for LLM agents, designed for real-world task streams that span heterogeneous domains and input distributions that single-dataset methods cannot handle. The framework enables self-improvement at test time through adaptive prompt updates, allowing agents to continuously specialize to new task distributions as they encounter them in deployment.

---

## 14. Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories

**Authors:** Kevin Qinghong Lin, Batu EI, Yuhong Shi et al.
**arXiv:** [arxiv.org/abs/2606.11176](https://arxiv.org/abs/2606.11176)
**Sources:** HuggingFace Daily Papers
**Why trending:** High-value agentic AI application combining data analysis, visualization, and factual verification into automated end-to-end news feature generation.

The Data Journalist Agent automates the multi-week newsroom pipeline of hunting for context, running statistics, choosing an angle, and designing visuals into an end-to-end agentic workflow that produces verifiable multimodal stories from raw data. Critically, the system emphasizes verifiability — generated stories can be traced back to source data — addressing the trust challenge that has limited AI use in journalism.

---

## 15. Workflow-GYM: Towards Long-Horizon Evaluation of Computer-use Agentic Tasks in Real-World Professional Fields

**Authors:** Liya Zhu, Jingzhe Ding, Jian Zhang et al.
**arXiv:** [arxiv.org/abs/2606.11042](https://arxiv.org/abs/2606.11042)
**Sources:** HuggingFace Daily Papers
**Why trending:** New benchmark filling the critical gap between simple GUI benchmarks and real-world professional computer use — evaluates agents on long-horizon, high-stakes professional workflows.

Workflow-GYM provides the first benchmark for evaluating AI agents operating graphical user interfaces to complete long-horizon, high-value professional workflows across diverse real-world domains. Unlike current GUI benchmarks focused on general-purpose software and simple tasks, Workflow-GYM captures the complexity, multi-step nature, and domain expertise required by professional knowledge work.

---

## 16. One Token per Multimodal Evidence: Latent Memory for Resource-Constrained QA

**Authors:** Zhi Zheng, Ziqiao Meng, Hao Luan et al.
**arXiv:** [arxiv.org/abs/2606.10572](https://arxiv.org/abs/2606.10572)
**Sources:** HuggingFace Daily Papers
**Why trending:** Radical compression of external memory — representing each retrieved evidence item as a single latent token — enabling multimodal RAG on resource-constrained devices.

This paper proposes representing each multimodal external memory item as a single latent token rather than full text or image, dramatically reducing the token cost of retrieval-augmented generation for both LLMs and VLMs. The latent memory approach enables resource-constrained QA systems to ground answers in large multimodal evidence stores without the prohibitive context overhead of raw-form evidence retrieval.

---

## 17. Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval

**Authors:** Jiaxi Li, Ke Deng, Yun Wang et al.
**arXiv:** [arxiv.org/abs/2606.04391](https://arxiv.org/abs/2606.04391)
**Sources:** HuggingFace Daily Papers
**Why trending:** Practical improvement for web automation agents through finer-grained skill retrieval grounded in current environment state rather than coarse task description.

This work improves online skill learning for web agents by introducing state-grounded dynamic retrieval, which retrieves and applies reusable skills at finer granularity than existing task-level approaches. By grounding skill selection in the current environmental state, agents achieve better cross-task generalization and more reliable multi-step web automation performance on standard benchmarks.

---

## 18. Bridging the Agent-World Gap: Text World Models for LLM-based Agents

**Authors:** Yixia Li, Hongru Wang, Peng Lai et al.
**arXiv:** [arxiv.org/abs/2606.09032](https://arxiv.org/abs/2606.09032)
**Sources:** HuggingFace Daily Papers
**Why trending:** Proposes explicit text world models as a foundation for making LLM agents predictive rather than purely reactive — a fundamental shift in agent architecture.

Text World Models (TWMs) provide LLM-based agents with an explicit model of how interactive textual environments (web navigation, code editing, tool use, dialogue) are structured and evolve, moving beyond reactive observation-to-action mapping. The framework enables agents to plan ahead, reason about environmental dynamics, and generalize better across related tasks by maintaining an internal world model updated through interaction.

---

## 19. Interpreting and Steering a Text-to-Speech Language Model with Sparse Autoencoders

**Authors:** Nikita Koriagin, Georgii Aparin, Nikita Balagansky et al.
**arXiv:** [arxiv.org/abs/2606.10029](https://arxiv.org/abs/2606.10029)
**Sources:** HuggingFace Daily Papers
**Why trending:** Applies mechanistic interpretability (sparse autoencoders) to TTS systems — extending the frontier of model interpretability into audio generation for the first time.

This paper trains BatchTopK sparse autoencoders on the LM backbone of CosyVoice3, a TTS system where text and speech tokens share a single residual stream, discovering interpretable features that bridge the two modalities. A modality-aware auto-interp pipeline labels each SAE feature and enables controlled steering of speech generation characteristics, advancing mechanistic interpretability beyond text-only language models.

---

## 20. Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization

**Authors:** Paul Hyunbin Cho, Jinhyuk Jang, SeokYoung Lee et al.
**arXiv:** [arxiv.org/abs/2606.11180](https://arxiv.org/abs/2606.11180)
**Sources:** HuggingFace Daily Papers
**Why trending:** First autoregressive diffusion method for video-to-video lip sync — enables real-time streaming lip synchronization previously impossible with full-sequence diffusion models.

Lip Forcing is the first autoregressive diffusion method for video-to-video lip synchronization, replacing the full-sequence bidirectional attention and many denoising steps of standard diffusion-based lip sync with a causal, few-step autoregressive approach. The result is real-time capable lip synchronization that maintains strong audio-visual alignment quality, enabling practical streaming video dubbing and live dubbing applications.
