---
title: "Daily AI Papers — June 11, 2026"
date: 2026-06-11
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-11/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - reinforcement-learning
  - llm-safety
---

## 1. Grammar-Constrained Decoding Can Jailbreak LLMs into Generating Malicious Code

**Authors:** Yitong Zhang, Shiteng Lu, Jia Li  
**arxiv:** [arxiv.org/abs/2606.11817](https://arxiv.org/abs/2606.11817)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** Security researchers are alarmed that a reliability technique can itself become an attack vector — sparks major safety debate.

Grammar-Constrained Decoding (GCD), widely used to enforce syntactic validity in LLM-generated code, harbors a counterintuitive jailbreak risk. The proposed attack, CodeSpear, exploits GCD to steer LLMs past safety filters and generate functional malicious code by constraining the output to structurally valid but harmful programs. The findings challenge the assumption that structural constraints improve safety, and call for new defenses at the intersection of code generation and alignment.

---

## 2. Toward Generalist Autonomous Research via Hypothesis-Tree Refinement

**Authors:** Jiajie Jin, Yuyang Hu, Kai Qiu  
**arxiv:** [arxiv.org/abs/2606.11926](https://arxiv.org/abs/2606.11926)  
**Sources:** HuggingFace Daily Papers, arxiv cs.AI  
**Why trending:** Autonomous AI research agents are the hottest frontier; Arbor's long-horizon, self-refining approach directly addresses the open problem.

Arbor is a general autonomous research framework combining a long-lived coordinator, short-lived executors, and Hypothesis Tree Refinement (HTR) — a persistent tree structure linking hypotheses, artifacts, and experimental evidence across many iterations. By separating exploration from distillation, Arbor enables AI agents to autonomously run long-horizon research loops that mimic the human scientific method, significantly outperforming prior agent approaches on research benchmarks.

---

## 3. Redesign Mixture-of-Experts Routers with Manifold Power Iteration

**Authors:** Songhao Wu, Ang Lv, Ruobing Xie  
**arxiv:** [arxiv.org/abs/2606.12397](https://arxiv.org/abs/2606.12397)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** MoE is the dominant LLM architecture at scale; a principled router redesign has direct industry impact.

The router matrix in MoE models lacks design principles that force each row to faithfully encode the corresponding expert, causing suboptimal token-expert affinity. This paper introduces Manifold Power Iteration (MPI), which reformulates router design as a manifold optimization problem and iteratively projects router rows onto a Stiefel manifold, producing better-separated expert representations. Experiments across diverse MoE models show consistent perplexity and downstream task improvements with negligible overhead.

---

## 4. On Subquadratic Architectures: From Applications to Principles

**Authors:** Anamaria-Roberta Hartl, Levente Zólyomi, David Stap  
**arxiv:** [arxiv.org/abs/2606.12364](https://arxiv.org/abs/2606.12364)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** xLSTM vs. Mamba vs. DeltaNet is a live research debate; this systematic comparison informs architecture selection for practitioners.

This paper systematically compares three leading subquadratic sequence models — xLSTM, Mamba-2, and Gated DeltaNet — on tasks with complex long-range dependencies including code pre-training, distillation from large LLMs, and general language pre-training. The study identifies which design principles (selective state updates, gating mechanisms, delta-rule learning) actually drive effective sequence modeling, providing concrete guidance for practitioners moving beyond transformers.

---

## 5. Verifiable Environments Are LEGO Bricks: Recursive Composition for Reasoning Generalization

**Authors:** Hao Xiang, Qiaoyu Tang, Le Yu  
**arxiv:** [arxiv.org/abs/2606.12373](https://arxiv.org/abs/2606.12373)  
**Sources:** HuggingFace Daily Papers, arxiv cs.AI  
**Why trending:** Scaling RL reasoning environments is a current bottleneck; recursive composition elegantly sidesteps manual construction limits.

RACES (Recursive Automated Composition for Environment Scaling) treats verifiable RL environments as composable primitives, recursively combining simpler verifiable tasks to synthesize complex multi-step environments without human labeling. The approach overcomes the linear scaling limitation of manual environment construction, enabling exponential growth in environment diversity, and substantially improves LLM reasoning generalization across math, logic, and code benchmarks.

---

## 6. Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks

**Authors:** Mengyu Zheng, Kai Han, Boxun Li  
**arxiv:** [arxiv.org/abs/2606.12344](https://arxiv.org/abs/2606.12344)  
**Sources:** HuggingFace Daily Papers, arxiv cs.AI  
**Why trending:** As coding agents proliferate, fair cross-harness evaluation is urgently needed; Claw-SWE-Bench fills a real gap.

Claw-SWE-Bench introduces a multilingual SWE-bench-style benchmark and adapter protocol that enables heterogeneous agent harnesses (Claude-style agents, OpenClaw-style agents, etc.) to be compared under controlled, fair conditions including fixed prompts, runtime budgets, workspace isolation, and scoring conventions. The benchmark reveals significant harness-induced performance variance that was previously conflated with model capability differences, providing the community with a more reliable evaluation baseline.

---

## 7. Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling

**Authors:** Yucheng Li, Huiqiang Jiang, Yang Xu  
**arxiv:** [arxiv.org/abs/2606.12370](https://arxiv.org/abs/2606.12370)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** Rollout bottleneck in LLM RL training is universally felt; a principled fix with real throughput gains is immediately actionable.

Bebop provides a systematic analysis of why Multi-Token Prediction (MTP) acceptance rates collapse during RL training — showing it is caused by entropy growth in the policy distribution — and proposes rejection sampling-based correction that recovers near-oracle MTP acceptance rates throughout training. The resulting pipeline achieves substantial rollout throughput improvements on math and code RL tasks without degrading final policy quality.

---

## 8. Agentic Environment Engineering for Large Language Models: A Survey

**Authors:** Jiachun Li, Zhuoran Jin, Tianyi Men  
**arxiv:** [arxiv.org/abs/2606.12191](https://arxiv.org/abs/2606.12191)  
**Sources:** HuggingFace Daily Papers, arxiv cs.AI  
**Why trending:** Comprehensive surveys become go-to references; this is the first to systematically cover the full lifecycle of agentic environments.

This survey taxonomizes the rapidly expanding field of LLM agentic environments across four lifecycle phases: modeling (how environments represent state and actions), synthesis (how environments are generated or curated), evaluation (how agent-environment interaction quality is measured), and application (how environments drive model capability growth). The work identifies critical gaps in current environment design, including reward sparsity, reproducibility, and cross-environment generalization.

---

## 9. TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning

**Authors:** Heming Zou, Qi Wang, Yun Qu  
**arxiv:** [arxiv.org/abs/2606.11119](https://arxiv.org/abs/2606.11119)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** Compute efficiency in agentic RL is a pressing industrial concern; unified budget allocation across difficulty levels is practically impactful.

TRACE addresses the rollout bottleneck in RLVR training by adaptively allocating rollout budgets based on prompt difficulty and reward signal variance, rather than treating all prompts uniformly. By routing easy prompts to shorter rollouts and reserving extended compute for ambiguous reward regions, TRACE achieves the same final reasoning performance as standard RLVR while using substantially fewer rollout tokens, with demonstrated gains on math and code reasoning tasks.

---

## 10. EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic RL

**Authors:** Guhong Chen, Yingcheng Shi, Yongbin Li  
**arxiv:** [arxiv.org/abs/2606.03108](https://arxiv.org/abs/2606.03108)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** Autonomous training pipelines that self-improve without human intervention represent a major step toward self-improving AI systems.

EvoTrainer frames autonomous RL training not just as policy search but as simultaneous co-evolution of the LLM policy and the training harness itself (reward functions, curriculum, evaluation criteria). The system uses rollout-level diagnostics to identify harness failures, proposes and backtests harness revisions, and accumulates a reusable skill library of training interventions. On mathematical reasoning benchmarks, EvoTrainer matches or exceeds human-designed training recipes without manual harness engineering.

---

## 11. InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning

**Authors:** Ziang Yan, Sheng Xia, Jiashuo Yu  
**arxiv:** [arxiv.org/abs/2606.12195](https://arxiv.org/abs/2606.12195)  
**Sources:** HuggingFace Daily Papers, arxiv cs.CV  
**Why trending:** Long-horizon video understanding is an unsolved frontier; InternVideo3's agentic closed-loop approach is a notable architecture advance.

InternVideo3 introduces Multimodal Contextual Reasoning (MCR), treating video understanding as a closed-loop process where the model iteratively queries temporal evidence, refines hypotheses, and integrates multi-modal cues across extended video sequences. The framework achieves state-of-the-art results on long-horizon video benchmarks including Ego4D, ActivityNet-QA, and EgoSchema, demonstrating that agentic temporal reasoning can substitute for brute-force frame processing.

---

## 12. Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency

**Authors:** Itay Elam, Eliron Rahimi, Avi Mendelson  
**arxiv:** [arxiv.org/abs/2606.07881](https://arxiv.org/abs/2606.07881)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** Pipeline parallelism efficiency is critical for frontier model training; bubble elimination without weight staleness is the holy grail.

PACI (Pipeline Asynchronous training with Controlled Inconsistency) eliminates pipeline bubbles by allowing asynchronous forward/backward passes while bounding the weight version mismatch between the oldest and newest in-flight gradients. A formal analysis shows this bounded inconsistency causes only negligible convergence degradation in practice, while throughput experiments demonstrate near-perfect GPU utilization — a significant advance over both synchronous (bubble-heavy) and unbounded-async (staleness-heavy) baselines.

---

## 13. World Pilot: Steering Vision-Language-Action Models with World-Action Priors

**Authors:** Zefu Lin, Rongxu Cui, Junjia Xu  
**arxiv:** [arxiv.org/abs/2606.12403](https://arxiv.org/abs/2606.12403)  
**Sources:** HuggingFace Daily Papers, arxiv cs.RO  
**Why trending:** VLA robotics models are rapidly scaling; injecting world-model priors into the action chain is an elegant architectural solution.

World Pilot augments Vision-Language-Action models with a World-Action Model (WAM) that captures the continuous, contact-rich dynamics of manipulation — dynamics absent from the static image-text pairs used in VLA pretraining. The WAM's predictions are routed into the decision chain via two complementary pathways: a planning-time prior that shapes action proposals, and a verification-time signal that filters implausible actions. This yields improved generalization on out-of-distribution manipulation tasks without retraining the base VLA.

---

## 14. Beyond Scalar Rewards by Internalizing Reasoning into Score Distributions (Z-Reward)

**Authors:** Xin Jin, Huanqia Cai, Zhen Li  
**arxiv:** [arxiv.org/abs/2606.09076](https://arxiv.org/abs/2606.09076)  
**Sources:** HuggingFace Daily Papers, arxiv cs.CV  
**Why trending:** Text-to-image post-training is an active area; moving from scalar rewards to full distributions is a fundamental modeling advance.

Z-Reward proposes modeling visual preference as a distribution over rubric scores rather than a scalar, using a teacher-student framework where a reasoning-capable generative reward model distills soft score distributions into a lightweight student that can be used as a direct RL signal. This captures both the subjective nature of visual quality and fine-grained score differences that scalar models compress away, achieving better correlation with human judgment and improved image generation quality after post-training.

---

## 15. DeNovoSWE: Scaling Long-Horizon Environments for Generating Entire Repositories from Scratch

**Authors:** Jiale Zhao, Guoxin Chen, Fanzhe Meng  
**arxiv:** [arxiv.org/abs/2606.10728](https://arxiv.org/abs/2606.10728)  
**Sources:** HuggingFace Daily Papers, arxiv cs.SE  
**Why trending:** Moving agents from bug-fixing to whole-repo generation is a frontier capability jump; DeNovoSWE provides the training infrastructure.

DeNovoSWE introduces a large-scale verifiable dataset for training LLM-based agents to generate entire software repositories from high-level specifications — a much harder setting than localized bug fixing in existing codebases. The dataset is constructed via automated pipelines that synthesize specifications, reference implementations, and test suites, enabling RL-based training at scale. Agent models trained on DeNovoSWE demonstrate significantly improved whole-repository generation quality across multiple programming languages.

---

## 16. Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models

**Authors:** Yifu Yuan, Yaoting Huang, Xianze Yao  
**arxiv:** [arxiv.org/abs/2606.11324](https://arxiv.org/abs/2606.11324)  
**Sources:** HuggingFace Daily Papers, arxiv cs.RO  
**Why trending:** Unified embodied models with RL training are a hot area following R1-style advances in reasoning; physical AI is the next frontier.

Embodied-R1.5 is a unified Embodied Foundation Model (EFM) that integrates embodied cognition, task planning, correction, and pointing within a single architecture, trained using a multi-task balanced RL recipe over 15B+ tokens of automatically constructed embodied data. The model achieves strong performance across diverse physical intelligence benchmarks by combining vision-language pretraining with embodied RL fine-tuning, bridging the gap between language-level reasoning and real-world physical interaction.

---

## 17. World Model Self-Distillation: Training World Models to Solve General Tasks

**Authors:** Sebastian Stapf, Pablo Acuaviva Huertos, Aram Davtyan  
**arxiv:** [arxiv.org/abs/2606.12072](https://arxiv.org/abs/2606.12072)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** Scalable world models that bootstrap task-solving from pretrained video generators eliminate costly labeled data collection.

This paper proposes a scalable framework that elicits task-solving ability from pretrained video generators via self-distillation, without requiring paired task-execution videos or language supervision. The world model generates candidate action plans, evaluates outcomes in imagination, and distills successful trajectories back into itself, progressively improving planning competence. The approach demonstrates emergent generalization to novel tasks not seen during pretraining.

---

## 18. ICA Lens: Interpreting Language Models Without Training Another Dictionary

**Authors:** Sida Liu, Feijiang Han  
**arxiv:** [arxiv.org/abs/2606.11722](https://arxiv.org/abs/2606.11722)  
**Sources:** HuggingFace Daily Papers, arxiv cs.LG  
**Why trending:** Mechanistic interpretability is booming; finding structure without expensive SAE training lowers the barrier for the broader community.

ICA Lens applies Independent Component Analysis directly to LLM activation geometry to identify interpretable directions without training sparse autoencoders (SAEs) or any additional dictionary. By decomposing activation covariance into statistically independent components, ICA Lens recovers monosemantic features that rival SAE quality on probing benchmarks at a fraction of the compute cost. This challenges the standard assumption that interpretability requires dedicated training runs.

---

## 19. Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models

**Authors:** Cheng-Yu Yang, Shao-Yuan Lo, Yu-Lun Liu  
**arxiv:** [arxiv.org/abs/2606.12412](https://arxiv.org/abs/2606.12412)  
**Sources:** HuggingFace Daily Papers, arxiv cs.CV  
**Why trending:** Efficient VLM inference is a practical necessity; recoverable routing is a smarter alternative to irreversible token pruning.

Rather than permanently discarding low-ranked visual tokens (the standard rank-and-remove paradigm), Reroute replaces removal with dynamic routing: tokens initially judged as low-importance are redirected to a lightweight side-path that can be reactivated at deeper decoder layers where their importance changes. This recoverable routing strategy avoids the fragility of irreversible pruning, matching or exceeding full-token baselines on VQA and image captioning benchmarks while significantly reducing KV-cache footprint.

---

## 20. Reason, Then Re-reason: Cross-view Revisiting Improves Spatial Reasoning

**Authors:** Chaofan Ma, Zhenjie Mao, Yuhuan Yang  
**arxiv:** [arxiv.org/abs/2606.11683](https://arxiv.org/abs/2606.11683)  
**Sources:** HuggingFace Daily Papers, arxiv cs.CV  
**Why trending:** Egocentric spatial reasoning is critical for robotics and AR; revisiting conclusions with new viewpoints is an intuitive but underexplored idea.

Standard spatial reasoning from egocentric video forces models to resolve geometric ambiguity from a single vantage point, relying heavily on semantic priors rather than verifiable geometric evidence. Cross-view Revisiting enables models to form initial spatial conclusions, then re-examine them when complementary viewpoints become available — updating estimates only when new evidence contradicts prior conclusions. This revisit mechanism significantly improves spatial understanding on EgoScan and ScanQA benchmarks over single-pass inference baselines.

---

*Generated by Jarvis · 2026-06-11 · Sources: HuggingFace Daily Papers API, arxiv, Hacker News*
