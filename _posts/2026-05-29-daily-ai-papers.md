---
title: "Daily AI Papers — May 29, 2026"
date: 2026-05-29
permalink: /blog/ai-papers/2026/05/daily-ai-papers-05-29/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-safety
  - vision-language-action
  - lora-optimization
---

## 1. AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security

**Authors:** Dongrui Liu, Yu Li, Zhonghao Yang, Peng Wang, Guanxu Chen, Yuejin Xie, et al.
**arXiv:** [arxiv.org/abs/2605.29801](https://arxiv.org/abs/2605.29801)

**Summary:** Advanced frontier AI models are lowering attack barriers against agentic systems, making existing alignment frameworks insufficient. AgentDoG 1.5 proposes a taxonomy-guided training approach using minimal samples and efficient deployment mechanisms — including influence-function purification — to align open-world agents against emergent safety and security threats.

**Why trending:** Highest-upvoted paper today; addresses the timely and pressing challenge of agent safety as agentic frameworks become mainstream, resonating strongly with the AI safety community.

**Sources:** HuggingFace Daily Papers (79 upvotes), arXiv

---

## 2. Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments

**Authors:** Qiuyue Wang, Mingsheng Li, Jian Guan, Jinhui Ye, Sicheng Xie, Yitao Liu, et al.
**arXiv:** [arxiv.org/abs/2605.30280](https://arxiv.org/abs/2605.30280)

**Summary:** Embodied intelligence has long been fragmented across specialized models for manipulation, navigation, and other tasks. Qwen-VLA extends the Qwen vision-language stack with a DiT-based action decoder and embodiment-aware prompt conditioning to unify heterogeneous robot decision-making within a single foundation model.

**Why trending:** From the Qwen team; unifying robotics under a single VLA model is a major milestone. Strong cross-platform presence with interest from embodied AI and robotics researchers.

**Sources:** HuggingFace Daily Papers (64 upvotes), arXiv

---

## 3. OmniRetrieval: Unified Retrieval across Heterogeneous Knowledge Sources

**Authors:** Jinheon Baek, Soyeong Jeong, Sangwoo Park, Woongyeong Yeo, Minki Kang, Patara Trirat, et al.
**arXiv:** [arxiv.org/abs/2605.29250](https://arxiv.org/abs/2605.29250)

**Summary:** Real-world RAG systems struggle because different knowledge repositories (unstructured text, relational tables, knowledge graphs, property graphs) require incompatible query languages. OmniRetrieval identifies appropriate repositories and dispatches source-native queries to their respective execution engines, outperforming single-source retrievers across diverse benchmarks.

**Why trending:** Directly addresses a pain point in production RAG and enterprise search systems; the framework's practical applicability drives high community interest.

**Sources:** HuggingFace Daily Papers (50 upvotes), arXiv

---

## 4. CollectionLoRA: Collecting 50 Effects in 1 LoRA via Multi-Teacher On-Policy Distillation

**Authors:** Fangtai Wu, Hailong Guo, Shijie Huang, Jiayi Song, Yubo Huang, Mushui Liu, et al.
**arXiv:** [arxiv.org/abs/2605.25378](https://arxiv.org/abs/2605.25378)

**Summary:** Deploying many customized image-editing LoRAs is expensive due to storage overhead and parameter interference when cascaded with acceleration modules. CollectionLoRA uses multi-teacher on-policy distillation with a Probabilistic Dual-Stream Routing mechanism to compress up to 50 visual effects into a single LoRA, enabling efficient deployment without quality loss.

**Why trending:** Highly practical for LoRA-heavy diffusion model workflows; the 50-in-1 compression result caught the attention of the image generation and fine-tuning communities.

**Sources:** HuggingFace Daily Papers (48 upvotes), arXiv

---

## 5. minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models

**Authors:** Min Zhao, Hongzhou Zhu, Bokai Yan, Zihan Zhou, Yimin Chen, Wenqiang Sun, et al.
**arXiv:** [arxiv.org/abs/2605.30263](https://arxiv.org/abs/2605.30263)

**Summary:** Converting bidirectional video diffusion models into real-time interactive world models requires solving controllability, causality, and latency simultaneously. minWM provides a complete open-source pipeline — spanning data construction, controllable fine-tuning, autoregressive training, few-step distillation via causal Forcing/ODE, and streaming inference — to achieve low-latency interactive world models.

**Why trending:** Full-stack open-source release for interactive world models is rare; the engineering completeness and real-time capability drew strong community interest.

**Sources:** HuggingFace Daily Papers (36 upvotes), arXiv

---

## 6. YoCausal: How Far is Video Generation from World Model? A Causality Perspective

**Authors:** You-Zhe Xie, Yu-Hsuan Li, Jie-Ying Lee, Kaipeng Zhang, Yu-Lun Liu, Zhixiang Wang, et al.
**arXiv:** [arxiv.org/abs/2605.30346](https://arxiv.org/abs/2605.30346)

**Summary:** Video diffusion models exhibit arrow-of-time perception but lack true causal understanding, relying on statistical temporal patterns rather than genuine physical reasoning. YoCausal introduces a two-level benchmark inspired by the cognitive-science Violation of Expectation paradigm, using temporally reversed real-world videos to measure causal cognition in video generation models.

**Why trending:** Poses a fundamental and provocative question about the gap between world models and video generators; the VoE-inspired evaluation methodology is novel and thought-provoking.

**Sources:** HuggingFace Daily Papers (30 upvotes), arXiv

---

## 7. GenClaw: Code-Driven Agentic Image Generation

**Authors:** Junyan Ye, Jun He, Zilong Huang, Dongzhi Jiang, Xuan Yang, Rui Chen, et al.
**arXiv:** [arxiv.org/abs/2605.30248](https://arxiv.org/abs/2605.30248)

**Summary:** Existing multimodal image generation agents are constrained by black-box model interfaces and repetitive prompt-rewriting cycles with no direct canvas manipulation. GenClaw introduces a code-driven agentic framework with three stages — conceptualization, sketching, coloring — that enables LLMs to directly control image construction via programmatic logic and tool invocation.

**Why trending:** Novel code-driven paradigm for image generation agents; resonates with the growing agentic coding trend and offers a principled alternative to prompt-rewriting loops.

**Sources:** HuggingFace Daily Papers (24 upvotes), arXiv

---

## 8. EarlyTom: Early Token Compression Completes Fast Video Understanding

**Authors:** Hesong Wang, Xin Jin, Lu Lu, Chenhaowen Li, Jian Chen, Qiang Liu, et al.
**arXiv:** [arxiv.org/abs/2605.30010](https://arxiv.org/abs/2605.30010)

**Summary:** Video LLMs are slowed by massive visual token volumes, and most compression approaches act too late (at the LLM input stage) to reduce time-to-first-token. EarlyTom is a training-free framework that compresses visual tokens early within the vision encoder, achieving faster inference while maintaining accuracy comparable to full-token baselines.

**Why trending:** Training-free efficiency gains for video LLMs are immediately deployable; the early-compression approach is a clean, practical insight with direct production impact.

**Sources:** HuggingFace Daily Papers (22 upvotes), arXiv

---

## 9. UniSteer: Text-Guided Flow Matching in Activation Space for Versatile LLM Steering

**Authors:** Yingdong Shi, Ruiming Zhang, Changming Li, Zhiyu Yang, Kaixing Zhang, Jingyi Yu, et al.
**arXiv:** [arxiv.org/abs/2605.30076](https://arxiv.org/abs/2605.30076)

**Summary:** Existing activation-based LLM steering relies on fixed steering directions or task-specific modules, limiting adaptability to compositional or fine-grained behavioral constraints. UniSteer learns a universal conditional velocity field in activation space via text-guided flow matching, enabling flexible steering of LLM behaviors — including persona, style, and classification — from natural language descriptions alone.

**Why trending:** Elegant unification of activation steering with flow matching; highly relevant for LLM alignment and controllability research.

**Sources:** HuggingFace Daily Papers (19 upvotes), arXiv

---

## 10. How LoRA Remembers? A Parametric Memory Law for LLM Finetuning

**Authors:** Ziwen Xu, Haiwen Hong, Linsong Yu, Benglei Cui, Longtao Huang, Hui Xue, et al.
**arXiv:** [arxiv.org/abs/2605.30260](https://arxiv.org/abs/2605.30260)

**Summary:** Despite widespread use of LoRA for continual LLM knowledge updates, the quantitative memory capacity limits of LoRA remain poorly understood. This work establishes a power-law relationship between LoRA rank and parametric memory capacity and derives a threshold-guided optimization framework for efficient continual finetuning.

**Why trending:** Brings scientific rigor to LoRA capacity analysis — directly useful for practitioners who tune LoRA rank hyperparameters and for researchers studying continual learning.

**Sources:** HuggingFace Daily Papers (19 upvotes), arXiv

---

## 11. Native Audio-Visual Alignment for Generation (NAVA)

**Authors:** Longbin Ji, Guan Wang, Xuan Wei, Chenye Yang, Xiangrui Liu, Zhenyu Zhang, et al.
**arXiv:** [arxiv.org/abs/2605.30073](https://arxiv.org/abs/2605.30073)

**Summary:** Joint audio-video generation requires fine-grained temporal synchronization that dual-tower and fully unified tri-modal architectures struggle to achieve without coupling semantic conditioning with low-level signals. NAVA introduces native audio-visual alignment with context-conditioned denoising to improve synchronization and controllability in joint generation.

**Why trending:** Multimodal generation with tight audio-video sync is a hot frontier; NAVA's principled alignment approach addresses a key limitation of existing open-source methods.

**Sources:** HuggingFace Daily Papers (18 upvotes), arXiv

---

## 12. LoMo: Local Modality Substitution for Deeper Vision-Language Fusion

**Authors:** Feng Han, Zhixiong Zhang, Zheming Liang, Yibin Wang, Jiaqi Wang, et al.
**arXiv:** [arxiv.org/abs/2605.30265](https://arxiv.org/abs/2605.30265)

**Summary:** Vision-Language Models suffer "carrier sensitivity" — replacing a text question with its image rendering causes dramatic performance degradation — due to biases in large-scale training data. LoMo introduces a Local Modality Substitution data curation strategy that improves cross-modal representation alignment and reduces this sensitivity.

**Why trending:** Identifies and addresses a subtle but significant VLM robustness issue; the curation-based fix is both elegant and practical.

**Sources:** HuggingFace Daily Papers (17 upvotes), arXiv

---

## 13. LaRA: Layer-wise Representation Analysis for Detecting Data Contamination in RL Post-Training

**Authors:** Minju Gwak, Minseo Kwak, Dongseok Lee, Guijin Son, Alan Ritter, Jaehyung Kim, et al.
**arXiv:** [arxiv.org/abs/2605.29888](https://arxiv.org/abs/2605.29888)

**Summary:** Data contamination in RL post-training (RLHF/GRPO) is hard to detect because output-level signals like likelihood and entropy become unreliable after RL training. LaRA detects contaminated training data by analyzing geometric deviations in representations across model layers, exploiting perturbation sensitivity as a contamination signal.

**Why trending:** Timely as RL post-training (GRPO, RLHF) becomes standard practice; a principled contamination detection method directly impacts evaluation reliability.

**Sources:** HuggingFace Daily Papers (15 upvotes), arXiv

---

## 14. Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic RL

**Authors:** Jiapeng Zhu, Jianxiang Yu, Yibo Zhao, Chengcheng Han, Qi Gu, Xunliang Cai, et al.
**arXiv:** [arxiv.org/abs/2605.28424](https://arxiv.org/abs/2605.28424)

**Summary:** Skill-based agentic RL forces a rigid choice between fully externalizing skills (context overhead) or fully internalizing them (rigidity), limiting OOD generalization. Skill0.5 combines general skill internalization with task-specific skill utilization through a dynamic, difficulty-aware router and privileged distillation to achieve strong OOD performance.

**Why trending:** Agentic RL generalization is a key unsolved problem; the hybrid internalization/utilization approach offers a principled middle ground.

**Sources:** HuggingFace Daily Papers (15 upvotes), arXiv

---

## 15. Xetrieval: Mechanistically Explaining Dense Retrieval

**Authors:** Zhixin Cai, Jun Bai, Yang Liu, Jiaqi Li, Yichi Zhang, Taichuan Li, et al.
**arXiv:** [arxiv.org/abs/2605.29507](https://arxiv.org/abs/2605.29507)

**Summary:** Dense retrieval decisions are made through opaque high-dimensional embeddings, and existing explanations relying on surface signals (lexical matches, token alignments) miss the latent factors driving relevance. Xetrieval enhances sentence embeddings with chain-of-thought reasoning information and decomposes them into interpretable sparse features for mechanistic retrieval explanation.

**Why trending:** Interpretability of retrieval systems is increasingly important for production RAG; the mechanistic explanation approach bridges the gap between dense retrieval performance and transparency.

**Sources:** HuggingFace Daily Papers (14 upvotes), arXiv

---

## 16. When Should Models Change Their Minds? Contextual Belief Management in LLMs

**Authors:** Haoming Xu, Weihong Xu, Zongrui Li, Mengru Wang, Yunzhi Yao, Chiyu Wu, et al.
**arXiv:** [arxiv.org/abs/2605.30219](https://arxiv.org/abs/2605.30219)

**Summary:** Long-horizon interactions require LLMs to know when to update, preserve, or ignore accumulated information — a challenge formalized here as Contextual Belief Management (CBM). The paper introduces BeliefTrack, a closed-world benchmark spanning rule discovery and dynamic settings, and shows that RL and representation-level steering significantly improve CBM performance.

**Why trending:** Addresses the fundamental challenge of stateful reasoning in long-context agents; the BeliefTrack benchmark provides a concrete evaluation framework for the community.

**Sources:** HuggingFace Daily Papers (13 upvotes), arXiv

---

## 17. Colored Noise Diffusion Sampling

**Authors:** Hadar Davidson, Noam Issachar, Sagie Benaim
**arXiv:** [arxiv.org/abs/2605.30332](https://arxiv.org/abs/2605.30332)

**Summary:** Standard diffusion SDE solvers inject uniform white noise throughout sampling, ignoring the spectral bias of generative trajectories that resolve low-frequency structure first. Colored Noise Sampling dynamically allocates noise energy based on frequency-dependent schedules, better matching the model's generative dynamics and improving image synthesis quality.

**Why trending:** Clean theoretical insight with direct practical impact on diffusion model sampling; no additional training required, making adoption straightforward.

**Sources:** HuggingFace Daily Papers (11 upvotes), arXiv

---

## 18. Is Position Bias in Dense Retrievers Built In or Learned from Data?

**Authors:** Daegon Yu, SeungYoon Han, Woomyoung Park
**arXiv:** [arxiv.org/abs/2605.26578](https://arxiv.org/abs/2605.26578)

**Summary:** Dense retrievers are known to favor documents where query-relevant information appears at the beginning, but the cause — architectural inductive bias vs. training data distribution — has been unclear. This work constructs synthetic training sets with controlled positional distributions and shows balanced training reduces positional bias by up to 87% while maintaining retrieval performance, pointing to data as the dominant cause.

**Why trending:** Practically actionable finding for RAG practitioners; knowing positional bias is data-driven means it can be mitigated at training time.

**Sources:** HuggingFace Daily Papers (11 upvotes), arXiv

---

## 19. AsyncTool: Evaluating Asynchronous Function Calling Capability under Multi-Task Scenarios

**Authors:** Kou Shi, Ziao Zhang, Shiting Huang, Avery Nie, Zhen Fang, Qiuchen Wang, et al.
**arXiv:** [arxiv.org/abs/2605.27995](https://arxiv.org/abs/2605.27995)

**Summary:** LLM-based tool-use evaluations overlook the temporal dimension — specifically the impact of tool response latency in multi-task concurrent settings. AsyncTool introduces a benchmark for evaluating whether agents can coordinate idle time across concurrent tool calls, exposing significant gaps in current LLMs' asynchronous execution capabilities.

**Why trending:** As agentic tool use matures, async multi-task execution becomes critical; the benchmark fills a clear evaluation gap.

**Sources:** HuggingFace Daily Papers (9 upvotes), arXiv

---

## 20. CausaLab: A Scalable Environment for Interactive Causal Discovery Toward AI Scientists

**Authors:** Junlin Yang, Dylan Zhang, Xiangchen Song, Qirun Dai, Xiao Liu, Yuen Chen, et al.
**arXiv:** [arxiv.org/abs/2605.26029](https://arxiv.org/abs/2605.26029)

**Summary:** Existing causal discovery benchmarks evaluate prediction accuracy but not whether the underlying causal mechanism was faithfully recovered. CausaLab places LLM agents in synthetic laboratory episodes where they must intervene on causal systems and both predict outcomes and recover the true causal graph structure.

**Why trending:** Bridges causal reasoning and AI-for-science; the dual evaluation criterion (prediction + mechanism recovery) is a more rigorous standard that pushes toward genuine scientific reasoning in LLMs.

**Sources:** HuggingFace Daily Papers (8 upvotes), arXiv
