---
title: "Daily AI Papers — May 07, 2026"
date: 2026-05-07
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-07/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal
  - video-generation
  - reasoning
---

## 1. MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction

**Authors:** Junbo Cui, Bokai Xu, Chongyi Wang, Tianyu Yu, Weiyue Sun et al.
**arXiv:** [arxiv.org/abs/2604.27393](https://arxiv.org/abs/2604.27393)
**Sources:** HuggingFace Daily Papers, GitHub (OpenBMB/MiniCPM-o), Reddit r/LocalLLaMA

**Summary:** MiniCPM-o 4.5 addresses the two key bottlenecks in multimodal LLMs — alternating perception/response cycles and fragmented modality integration — by introducing a real-time full-duplex omni-modal interaction paradigm. The model enables simultaneous audio, video, and text understanding with continuous streaming I/O, rivaling Gemini 2.5 Flash in multimodal interaction benchmarks at a fraction of the compute cost.

**Why trending:** Full-duplex real-time multimodal interaction is the next frontier after GPT-4o; the open-source release of a competitive model has driven heavy community discussion on r/LocalLLaMA and GitHub.

---

## 2. Stream-T1: Test-Time Scaling for Streaming Video Generation

**Authors:** Yijing Tu, Shaojin Wu, Mengqi Huang, Wenchuan Wang, Yuxin Wang et al.
**arXiv:** [arxiv.org/abs/2605.04461](https://arxiv.org/abs/2605.04461)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Summary:** Stream-T1 applies test-time scaling (TTS) — the paradigm popularized by reasoning models — to streaming video generation, addressing the twin problems of exorbitant candidate exploration costs and lack of temporal guidance in diffusion-based video generators. By shifting focus to the chunked structure of streaming video and leveraging temporal coherence as a guidance signal, the method achieves significant quality improvements without retraining.

**Why trending:** TTS has dominated NLP; this is one of the first principled attempts to bring the concept to video generation, a highly anticipated research direction.

---

## 3. OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents

**Authors:** Shuang Chen, Kaituo Feng, Hangting Chen, Wenxuan Huang, Dasen Dai et al.
**arXiv:** [arxiv.org/abs/2605.05185](https://arxiv.org/abs/2605.05185)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL, Papers With Code

**Summary:** OpenSearch-VL provides a fully open recipe for training state-of-the-art multimodal search agents capable of active search, evidence verification, and multi-step reasoning over images and text. The work releases high-quality training data, trajectory synthesis pipelines, and detailed training procedures — directly addressing the reproducibility gap that has kept top multimodal search agents proprietary.

**Why trending:** Reproducibility of frontier multimodal agents is a major pain point; this open recipe drew attention from the AI research community and practitioners building RAG + vision pipelines.

---

## 4. When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning

**Authors:** Jiaqi Wei, Xuehang Guo, Pengfei Yu, Xiang Zhang, Wanli Ouyang et al.
**arXiv:** [arxiv.org/abs/2605.03314](https://arxiv.org/abs/2605.03314)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL, Reddit r/MachineLearning

**Summary:** This paper formalizes the "silence tax" problem in autoregressive reasoning models: coupling deliberation with token commitment forces a trade-off between latency and reasoning quality. The authors propose Side-by-Side (SxS) Interleaving, a learned disclosure policy that separates internal chain-of-thought from streamed output, allowing models to reason privately before selectively committing tokens.

**Why trending:** Directly relevant to the design of production reasoning systems (o3, Claude Sonnet thinking) — resolving the tension between streaming UX and reasoning quality is a hot open problem.

---

## 5. RLDX-1 Technical Report

**Authors:** Dongyoung Kim, Huiwon Jang, Myungkyu Koo, Suhyeok Jang, Taeyoung Kim et al.
**arXiv:** [arxiv.org/abs/2605.03269](https://arxiv.org/abs/2605.03269)
**Sources:** HuggingFace Daily Papers, arXiv cs.RO, Reddit r/MachineLearning

**Summary:** RLDX-1 is a Vision-Language-Action (VLA) model designed to overcome the limitations of existing VLA systems in complex real-world tasks — specifically targeting motion awareness, memory, and goal-conditioned generalization. The model inherits broad scene understanding from pre-trained VLMs while adding functional capabilities through a novel reinforcement learning framework tailored for dexterous manipulation.

**Why trending:** Embodied AI and robot foundation models are a top research priority in 2026; VLA models are the intersection of LLM generalization and physical world grounding.

---

## 6. Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation

**Authors:** Bin Wu, Mengqi Huang, Shaojin Wu, Weinan Jia, Yuxin Wang et al.
**arXiv:** [arxiv.org/abs/2605.03849](https://arxiv.org/abs/2605.03849)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Summary:** Stream-R1 challenges the standard approach in video diffusion distillation (DMD) that treats all rollouts and frames as equally reliable supervision signals. By introducing reliability-perplexity aware reward distillation, it selectively emphasizes high-signal supervision, significantly improving the student model's output quality and temporal consistency at equivalent inference cost.

**Why trending:** The R1-style reward learning paradigm applied to video generation is a natural extension of the reasoning model revolution; the "Stream" series has attracted significant attention as a two-paper release.

---

## 7. Awaking Spatial Intelligence in Unified Multimodal Understanding and Generation (JoyAI-Image)

**Authors:** Lin Song, Wenbo Li, Guoqing Ma, Wei Tang, Bo Wang et al.
**arXiv:** [arxiv.org/abs/2605.04128](https://arxiv.org/abs/2605.04128)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV, Papers With Code

**Summary:** JoyAI-Image introduces a unified multimodal foundation model coupling a spatially enhanced MLLM with a Multimodal Diffusion Transformer (MMDiT) for visual understanding, text-to-image generation, and instruction-guided image editing in a single architecture. The shared multimodal interface enables bidirectional interaction between perception and generation, yielding a model that understands spatial relationships while generating spatially coherent images.

**Why trending:** Unifying perception and generation in a single coherent framework is an active research frontier; spatial intelligence has been identified as a key missing capability in current MLLMs.

---

## 8. The First Token Knows: Single-Decode Confidence for Hallucination Detection

**Authors:** Mina Gabriel
**arXiv:** [arxiv.org/abs/2605.05166](https://arxiv.org/abs/2605.05166)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL

**Summary:** This paper demonstrates that the confidence signal encoded in the first generated token of an LLM response is highly predictive of hallucination risk, enabling hallucination detection without repeated sampling or external inference models. The method sidesteps the cost of self-consistency and semantic clustering approaches, offering a near-zero overhead alternative for production deployment.

**Why trending:** Hallucination detection at inference time with zero overhead is directly actionable for anyone deploying LLMs; single-decode confidence is a clever, counterintuitive finding.

---

## 9. CreativityBench: Evaluating Agent Creative Reasoning via Affordance-Based Tool Repurposing

**Authors:** Cheng Qian, Hyeonjeong Ha, Jiayu Liu, Jeonghwan Kim, Jiateng Liu et al.
**arXiv:** [arxiv.org/abs/2605.02910](https://arxiv.org/abs/2605.02910)
**Sources:** HuggingFace Daily Papers, arXiv cs.AI, Reddit r/MachineLearning

**Summary:** CreativityBench introduces a novel evaluation framework for large language model agents focused on creative problem-solving through affordance-based tool repurposing — using objects for purposes beyond their canonical function by reasoning about attributes and properties. The benchmark reveals a significant gap between current LLMs' strong performance on conventional reasoning tasks and their limited creative flexibility.

**Why trending:** Creativity and out-of-distribution generalization in agents is an underexplored dimension of capability evaluation; the affordance-based framing brings cognitive science grounding to LLM benchmarking.

---

## 10. Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems

**Authors:** Yilun Zhao, Jinbiao Wei, Tingyu Song, Siyue Zhang, Chen Zhao et al.
**arXiv:** [arxiv.org/abs/2605.04018](https://arxiv.org/abs/2605.04018)
**Sources:** HuggingFace Daily Papers, arXiv cs.IR, Papers With Code

**Summary:** This work addresses the gap in evaluation and training frameworks for retrievers operating in agentic, multi-step search pipelines, where the goal is supporting downstream reasoning rather than topical similarity matching. The authors propose new benchmarks and training approaches that explicitly account for the iterative search-and-synthesis loop characteristic of modern AI agents.

**Why trending:** Agentic RAG systems are ubiquitous; the realization that existing retrieval benchmarks (BRIGHT, etc.) don't capture reasoning-intensive needs has sparked significant community interest.

---

## 11. PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual Worlds

**Authors:** Yunhan Yang, Chunshi Wang, Junliang Ye, Yang Li, Zanxin Chen et al.
**arXiv:** [arxiv.org/abs/2605.05163](https://arxiv.org/abs/2605.05163)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV, Papers With Code

**Summary:** PhysForge tackles the bottleneck of synthesizing interactive 3D assets that respect physical laws, proposing a decoupled two-stage pipeline grounded in functional logic and hierarchical physics simulation. Unlike prior work focused on static geometry, PhysForge generates assets with physically accurate properties essential for embodied AI training and interactive virtual world construction.

**Why trending:** Embodied AI simulation data generation is a critical bottleneck; physics-grounded synthetic assets directly enable the training of more capable physical world models.

---

## 12. SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies

**Authors:** Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi
**arXiv:** [arxiv.org/abs/2605.04637](https://arxiv.org/abs/2605.04637)
**Sources:** HuggingFace Daily Papers, arXiv cs.SE, Reddit r/MachineLearning

**Summary:** SWE-WebDevBench introduces evaluation infrastructure for "vibe coding" platforms — AI systems that translate natural language descriptions into full-stack applications — assessing them holistically as virtual software agencies rather than at the code-level only. The benchmark covers business requirement understanding, architectural decision-making, production code quality, and end-to-end feature delivery.

**Why trending:** The explosion of AI coding platforms (Cursor, Lovable, Devin) has outpaced rigorous evaluation; this benchmark directly addresses how to measure the end-to-end capabilities of these systems.

---

## 13. Lightning Unified Video Editing via In-Context Sparse Attention

**Authors:** Shitong Shao, Zikai Zhou, Haopeng Li, Yingwei Song, Wenliang Zhong et al.
**arXiv:** [arxiv.org/abs/2605.04569](https://arxiv.org/abs/2605.04569)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Summary:** This work addresses the quadratic attention bottleneck in In-Context Learning (ICL)-based video editing by introducing In-context Sparse Attention (ISA), a near-lossless sparse attention framework that leverages the finding that context tokens exhibit significantly lower salience than query tokens. ISA achieves dramatic speedups in video editing pipelines without perceptible quality degradation.

**Why trending:** ICL-based video editing is an emerging paradigm; making it computationally tractable for long videos is a key enabling capability.

---

## 14. ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning

**Authors:** Zihan Lin, Xiaohan Wang, Jie Cao, Jiajun Chai, Li Wang et al.
**arXiv:** [arxiv.org/abs/2605.00380](https://arxiv.org/abs/2605.00380)
**Sources:** HuggingFace Daily Papers, arXiv cs.CL

**Summary:** ResRL addresses the diversity collapse problem in RLVR (RL with Verifiable Rewards) training — where over-incentivizing correct answers suppresses semantic exploration — by introducing negative sample projection residuals that penalize the shared distribution between positive and negative samples rather than the full negative distribution. This preserves generation diversity while maintaining accuracy gains.

**Why trending:** RLVR is the dominant paradigm for improving LLM reasoning post-DeepSeek-R1; addressing its known failure modes (mode collapse, diversity loss) is highly relevant to practitioners.

---

## 15. D-OPSD: On-Policy Self-Distillation for Continuously Tuning Step-Distilled Diffusion Models

**Authors:** Dengyang Jiang, Xin Jin, Dongyang Liu, Zanyi Wang, Mingzhe Zheng et al.
**arXiv:** [arxiv.org/abs/2605.05204](https://arxiv.org/abs/2605.05204)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Summary:** D-OPSD addresses the challenge of fine-tuning few-step distilled diffusion models (like FLUX.1-schnell, Z-Image-Turbo) where standard supervised fine-tuning degrades the efficiency gains from distillation. The on-policy self-distillation approach allows continuous adaptation of step-distilled models without reverting to slow multi-step sampling during training.

**Why trending:** Few-step diffusion models are the practical standard for image generation; enabling efficient fine-tuning of these models unlocks broad customization use cases.

---

## 16. HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation

**Authors:** Xin Zhou, Dingkang Liang, Xiwu Chen, Feiyang Tan, Dingyuan Zhang et al.
**arXiv:** [arxiv.org/abs/2604.28196](https://arxiv.org/abs/2604.28196)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Summary:** HERMES++ unifies future scene generation and 3D scene understanding in a single driving world model by integrating LLM reasoning capabilities with geometric evolution prediction. The model bridges the gap between scene generation (which lacks understanding) and LLM-based reasoning (which lacks geometric prediction), enabling comprehensive autonomous driving simulation.

**Why trending:** Autonomous driving world models are a major investment area; a model that simultaneously understands and generates 3D scenes addresses a fundamental limitation of existing approaches.

---

## 17. Diffusion Model as a Generalist Segmentation Learner

**Authors:** Haoxiao Wang, Antao Xiang, Haiyang Sun, Peilin Sun, Changhao Pan et al.
**arXiv:** [arxiv.org/abs/2604.24575](https://arxiv.org/abs/2604.24575)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV, Papers With Code

**Summary:** This paper demonstrates that the denoising trajectories of pre-trained diffusion models encode rich, spatially aligned visual priors that can be leveraged for text-conditioned semantic and open-vocabulary segmentation without task-specific architectural changes. The resulting framework generalizes across segmentation tasks (semantic, open-vocabulary, referring) using a single diffusion backbone.

**Why trending:** Re-purposing the rich representations in generative models for discriminative tasks is an active and productive research direction; segmentation as a target showcases the breadth of diffusion priors.

---

## 18. MedSkillAudit: A Domain-Specific Audit Framework for Medical Research Agent Skills

**Authors:** Yingyong Hou, Xinyuan Lao, Huimei Wang, Qianyu Yao, Wei Chen et al.
**arXiv:** [arxiv.org/abs/2604.20441](https://arxiv.org/abs/2604.20441)
**Sources:** HuggingFace Daily Papers, arXiv cs.AI

**Summary:** MedSkillAudit develops and evaluates a domain-specific audit framework for modular AI agent skills deployed in medical research contexts, addressing safety requirements beyond general-purpose evaluation — including scientific integrity, methodological validity, reproducibility, and boundary safety. The framework targets the growing deployment of AI agent pipelines in biomedical research workflows.

**Why trending:** Regulatory scrutiny of AI in healthcare is intensifying; domain-specific safety auditing frameworks for medical AI agents fill a critical gap.

---

## 19. APEX: Large-scale Multi-task Aesthetic-Informed Popularity Prediction for AI-Generated Music

**Authors:** Jaavid Aktar Husain, Dorien Herremans
**arXiv:** [arxiv.org/abs/2605.03395](https://arxiv.org/abs/2605.03395)
**Sources:** HuggingFace Daily Papers, arXiv cs.SD

**Summary:** APEX addresses popularity prediction for AI-generated music — an entirely new landscape distinct from human-created music, where traditional signals like artist reputation and label backing are absent. The multi-task model integrates aesthetic quality metrics with engagement prediction, trained on large-scale data from AI music platforms.

**Why trending:** AI music generation platforms (Suno, Udio) have created a new content ecosystem; understanding what makes AI-generated music popular has commercial and research significance.

---

## 20. Parameter-Efficient Multi-View Proficiency Estimation: From Discriminative Classification to Generative Feedback

**Authors:** Edoardo Bianchi, Antonio Liotta
**arXiv:** [arxiv.org/abs/2605.03848](https://arxiv.org/abs/2605.03848)
**Sources:** HuggingFace Daily Papers, arXiv cs.CV

**Summary:** This paper targets action proficiency estimation — assessing how well (not just what) a person performs an action — across multi-view video, addressing the challenge of subtle timing, balance, and body mechanics differences distributed across views. The work moves beyond discriminative classification toward generative feedback generation, enabling actionable coaching outputs.

**Why trending:** Automated coaching and rehabilitation assessment using AI video models is a high-value application; the shift from "classify skill level" to "generate coaching feedback" represents a meaningful capability jump.
