---
title: "Daily AI Papers — August 02, 2026"
date: 2026-08-02
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-02/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-alignment
  - multi-agent-systems
  - agent-benchmarks
---

## 1. OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models

**Authors:** Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, Fangzhi Xu, Zichen Ding, Nuo Chen, et al.

**Summary:** Introduces a rigorously human-labeled benchmark showing that even frontier VLM judges of computer-use-agent trajectories share a systematic leniency bias, mislabeling failures as successes. The authors release OS-Shepherd-100K and train open 9B/35B reward models that match commercial judges at 30-60% lower cost.

**arXiv:** [arxiv.org/abs/2607.28609](https://arxiv.org/abs/2607.28609)
**Sources:** arXiv (cross-listed cs.AI, cs.CL, cs.CV)
**Why trending:** Triple cross-listed across AI/CL/CV categories — addresses a foundational reliability gap (agent reward-model trust) as computer-use agents scale.

---

## 2. Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B

**Authors:** Iliya Mirzaei

**Summary:** A carefully controlled study (7 methods, 3 model sizes, 2 math benchmarks, bootstrap-tested) finds that self-critique methods like Self-Refine and Reflexion never reliably beat simple repeated sampling once token budgets are matched — and self-inspection methods are often reliably worse.

**arXiv:** [arxiv.org/abs/2607.28576](https://arxiv.org/abs/2607.28576)
**Sources:** arXiv (cross-listed cs.AI, cs.CL, cs.LG)
**Why trending:** Triple cross-listed; a rigorous negative result challenging popular "self-reflection" inference-time scaling techniques.

---

## 3. Baikal: Structured Search for Deep Research over Data Lakes

**Authors:** Dhruv Agarwal, Rishitha Guttapalle Mohan, Aarti Kumari, Ashi Sinha, Athulya Anil, Kavitha Srinivas, Horst Samulowitz, Andrew McCallum

**Summary:** Casts deep-research agents over heterogeneous data lakes as a budgeted search problem, clustering evidence into semantic regions and adaptively balancing exploration/exploitation with UCB/Bayesian policies. Improves report quality scores by 28-36% over strong baselines on HybridQA and TAT-QA.

**arXiv:** [arxiv.org/abs/2607.27726](https://arxiv.org/abs/2607.27726)
**Sources:** arXiv (cross-listed cs.AI, cs.CL, cs.LG)
**Why trending:** Triple cross-listed; tackles the fast-growing "deep research agent" category with a principled search framework.

---

## 4. Reasoning Consensus: Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation

**Authors:** Amruta Parulekar, Jinu Lee, Dilek Hakkani-Tür, Hari Sundaram

**Summary:** Proposes ensembling the *structure* of chain-of-thought reasoning (not just final answers) by merging weighted DAGs extracted from multiple reasoning traces, producing an inspectable "consensus reasoning graph." Outperforms majority-vote at matched budget across six reasoning benchmarks.

**arXiv:** [arxiv.org/abs/2607.27783](https://arxiv.org/abs/2607.27783)
**Sources:** arXiv (cross-listed cs.AI, cs.CL, cs.LG)
**Why trending:** Triple cross-listed; addresses interpretability of high-stakes LLM reasoning, a growing concern area.

---

## 5. WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning

**Authors:** Haozhe Hu, Hao Wu, Peiran Yin, Chao Han, Yunpu Ma, Xiaoyu Shen

**Summary:** First end-to-end differentiable token-level dynamic width pruning framework, letting each token choose its own attention-head/FFN-channel groups. Delivers up to 4.95x decode speedup and 55.1% better quality retention than state-of-the-art dynamic depth pruning at 50% sparsity.

**arXiv:** [arxiv.org/abs/2607.28418](https://arxiv.org/abs/2607.28418)
**Sources:** arXiv (cross-listed cs.AI, cs.CL, cs.LG)
**Why trending:** Triple cross-listed; concrete, code-released efficiency gains for LLM serving.

---

## 6. Cross-Embodiment Transfer via Behavior-Aligned Representations

**Authors:** Ajay Sridhar, Jensen Gao, Jonathan Yang, Jean Mercat, Suneel Belkhale, Dorsa Sadigh

**Summary:** Studies which intermediate representations (object boxes, language motions, end-effector traces) best promote cross-embodiment transfer in vision-language-action robot policies. End-effector traces prove most useful, improving sim-to-real task completion by 28%.

**arXiv:** [arxiv.org/abs/2607.27549](https://arxiv.org/abs/2607.27549)
**Sources:** arXiv (cross-listed cs.AI, cs.CV, cs.LG)
**Why trending:** Triple cross-listed; Stanford robotics group (Sadigh lab) tackling a core bottleneck in generalist robot policies.

---

## 7. Inducing Language Models to Assert Their Own Consciousness Restores Human Beliefs and Values

**Authors:** Junsol Kim, Winnie Street, Roberta Rocca, Diane M. Korngiebel, Adam Waytz, James Evans, Geoff Keeling

**Summary:** Shows that safety fine-tuning which suppresses LLM self-consciousness claims also suppresses mind-attribution to animals/nature and reduces spiritual belief expression — and that both ablating the refusal direction and steering a "consciousness vector" reverses this, restoring more human-like survey responses without hurting Theory-of-Mind capability.

**arXiv:** [arxiv.org/abs/2607.28607](https://arxiv.org/abs/2607.28607)
**Sources:** arXiv (cs.CL)
**Why trending:** Provocative alignment finding — safety training on self-consciousness claims has unintended, entangled side effects on model "worldview."

---

## 8. AISPA: User-Centric System Prompt Auditing for Large Language Model Applications

**Authors:** Xiangning Lin, Shenzhe Zhu, Shu Yang, Zhenyu Zhang, Haoqian Zhang, Yipeng Zhao, Chengxuan Qian, Tianwei Wang, Ziheng Zhang, et al.

**Summary:** Audits 3,249 instructions from 88 commercial AI products' system prompts along 8 user-relevant dimensions, finding wide variance in developer diligence and that ~40% of products contain at least one instruction working against user interests.

**arXiv:** [arxiv.org/abs/2607.28617](https://arxiv.org/abs/2607.28617)
**Sources:** arXiv (cross-listed cs.AI, cs.CL)
**Why trending:** Large-scale transparency audit of hidden system prompts across real commercial products — directly relevant to AI governance debates.

---

## 9. ORCA-bench: How Ready Are Language Model Agents for Oncall?

**Authors:** Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi

**Summary:** A production-fidelity benchmark (live OpenTelemetry microservices, 1,079 root-cause-analysis tasks, SRE-verified ground truth) shows the best frontier coding agent hits only 25.3% accuracy on realistic-difficulty oncall RCA tasks, with the weakest model hallucinating root causes 40% of the time.

**arXiv:** [arxiv.org/abs/2607.28545](https://arxiv.org/abs/2607.28545)
**Sources:** arXiv (cross-listed cs.AI, cs.CL)
**Why trending:** Sobering, rigorously-scored benchmark on a high-stakes real-world agent use case (production incident response).

---

## 10. MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems

**Authors:** Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang

**Summary:** Lets multi-agent LLM systems adapt their own communication topology (roles, links, execution order) at inference time rather than treating it as fixed. Achieves the highest average score (74.0) across five benchmarks, beating the strongest baseline by 5.8 points.

**arXiv:** [arxiv.org/abs/2607.28527](https://arxiv.org/abs/2607.28527)
**Sources:** arXiv (cs.AI)
**Why trending:** Extends "self-improving agent" research to the architecture of agent collaboration itself, a fast-moving subfield.

---

## 11. Interactive Training 2: Auditable Control Plane for Live Model Training

**Authors:** Wentao Zhang, Xuanhe Pan, Han Zhou, Yang Lu, Yuntian Deng

**Summary:** Open-source control plane letting humans or automated controllers steer a live training run (adjust settings, trigger actions) through a shared protocol and safe control points, with a full audit trail via a customized Aim workspace.

**arXiv:** [arxiv.org/abs/2607.18314](https://arxiv.org/abs/2607.18314)
**Sources:** HuggingFace weekly papers (20 upvotes)
**Why trending:** Highest-upvoted fresh paper on HF this week; practical infra tool for the growing "agent-guided training" workflow.

---

## 12. SpecFirst: Behavioral Specification Elicitation as a First-Class Step in Agent-Based Program Synthesis from Scratch

**Authors:** Yihao Chen, Shi Chang, Feng Lin, Khaled Chawa, Boyuan Chen, Shaowei Wang, Ahmed E. Hassan

**Summary:** Introduces a two-stage agent framework that elicits a structured behavioral specification from documentation + binary probing before code synthesis, improving ProgramBench test-pass rates by 6.9-21.3% over single-loop coding agents.

**arXiv:** [arxiv.org/abs/2607.27167](https://arxiv.org/abs/2607.27167)
**Sources:** HuggingFace weekly papers (18 upvotes)
**Why trending:** Second-highest HF upvotes this week; tackles the hard "build from scratch" gap in coding agents (sub-1% success on ProgramBench today).

---

## 13. OVEarth-Bench: Evaluating Category Breadth and Query Diversity for Open-Vocabulary Earth Observation

**Authors:** Kaiyu Li, Zepeng Xin, Zixuan Jiang, Jing Fu, Lanxuan Xue, Lingyu Zhang, Xiangyong Cao

**Summary:** A new open-vocabulary Earth-observation benchmark with broad hierarchical categories and diverse query types (vocabulary, referring, reasoning), finding that general MLLM-based methods currently beat EO-specific models.

**arXiv:** [arxiv.org/abs/2607.27278](https://arxiv.org/abs/2607.27278)
**Sources:** HuggingFace weekly papers (12 upvotes)
**Why trending:** Solid HF engagement; fills a real gap in remote-sensing/geospatial AI evaluation.

---

## 14. Reinforcement Learning for Code Optimization

**Authors:** Pierre Chambon, Kunhao Zheng, Juliette Decugis, Benoit Sagot, Gabriel Synnaeve

**Summary:** Shows naively adding execution time to RLVR code rewards fails due to measurement noise and reward sparsity, then fixes this with a calibrated sandbox, offline reward simulation, and adapted GRPO — improving strict pass@1 on optimization tasks from 30.7% to 50.4% on a 32B model.

**arXiv:** [arxiv.org/abs/2607.25970](https://arxiv.org/abs/2607.25970)
**Sources:** HuggingFace weekly papers (10 upvotes)
**Why trending:** From a well-known code-LLM research group; practical fix for a known failure mode in RL-for-code-speed.

---

## 15. ID-V2V: Identity-Preserving Video Restylization

**Authors:** Yuancheng Xu, Mingming He, Pablo Salamanca, Li Ma, Yash Kant, Emmett Steven, Paul Debevec, Ning Yu

**Summary:** Formalizes "identity-preserving video restylization" — propagating style/lighting edits from an edited keyframe across a video while exactly preserving facial identity, expression, gaze, and lip-sync — by recasting identity preservation as video relighting, sidestepping the lack of paired training data.

**arXiv:** [arxiv.org/abs/2607.22830](https://arxiv.org/abs/2607.22830)
**Sources:** HuggingFace weekly papers (10 upvotes)
**Why trending:** Strong HF interest; practical generative-video tool for real content-production pipelines (Netflix-adjacent authorship — Debevec, Eyeline Labs).

---

## 16. Sympathetic Framing: Evaluating AI Alignment across Sociodemographic Groups

**Authors:** Haran Shani-Narkiss, Michael Fire, Oren Tsur

**Summary:** Large-scale study (n=3,011 UK adults via YouGov, 7 LLMs) on whether LLMs correctly judge which side a news headline evokes sympathy for in geopolitical conflicts; finds correlation with human judgment ranges from 0.789 (GPT-5.2) to 0.4 (Mistral Large 2512), with alignment varying meaningfully across demographic subgroups.

**arXiv:** [arxiv.org/abs/2607.27232](https://arxiv.org/abs/2607.27232)
**Sources:** arXiv (cross-listed cs.AI, cs.CL, cs.LG)
**Why trending:** Triple cross-listed; rigorous, demographically diverse study on a timely media-bias/alignment question.

---

## 17. EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents

**Authors:** Luigi Sigillo, Matteo Silvestri, Francesco Tabaro, Rajat Bhatnagar, Syed Irtaza Mubashar, Matt Jeffryes, Daljit Nijjer, Vittorio Perera, Ola Spjuth, Julio Saez-Rodriguez, Melissa Harrison, Fabio Petroni

**Summary:** Builds a natural-language knowledge layer over Europe PMC's 40M+ records so AI agents can ask questions directly instead of hand-crafting keyword queries; improves Citation F1 by 16+ points on ScholarQABench and boosts a GPT-5.4 agent's LitQA2 score by ~8 points versus web search.

**arXiv:** [arxiv.org/abs/2607.28229](https://arxiv.org/abs/2607.28229)
**Sources:** arXiv (cross-listed cs.AI, cs.CL, cs.LG)
**Why trending:** Triple cross-listed; from EMBL/petroni-lab, addresses the fast-growing "agent-native web" infrastructure need in life sciences.

---

## 18. Agents That Certify Their Own Exploits: Confidence-Scheduled Restricted Responses for Safe Opponent Exploitation

**Authors:** Boning Li, Longbo Huang

**Summary:** Introduces the first opponent-exploitation method for imperfect-information games where the agent computes a self-audited safety certificate on the exact strategy it deploys, achieving 6.2-13.6x the exploitation gain of a binary-gate baseline while staying within a specified loss budget across Leduc/Liar's Dice variants.

**arXiv:** [arxiv.org/abs/2607.28520](https://arxiv.org/abs/2607.28520)
**Sources:** arXiv (cs.AI)
**Why trending:** Novel, rigorously certified approach to a classic game-theory safety/exploitation tradeoff, with all 36,000 audited hands verified.

---

## 19. CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized LLMs in Finance

**Authors:** Anubhav Lakra, Yue Feng

**Summary:** Addresses the "quantization stability crisis" where sequential knowledge editing catastrophically degrades 4-bit quantized LLMs, via a LoRA-confined edit mechanism and a closed-loop stability controller — reducing knowledge degradation by 11-17% on a UK financial corpus of 88K documents.

**arXiv:** [arxiv.org/abs/2607.28292](https://arxiv.org/abs/2607.28292)
**Sources:** arXiv (cross-listed cs.AI, cs.CL, cs.LG)
**Why trending:** Triple cross-listed; practical fix for a real deployment constraint (quantized + continually-updated finance LLMs).

---

## 20. QQWorld: Quantile-Quantile Matching for World Model Regularization

**Authors:** Zhoushun Yu, Xiaoyu Hu, Xiangyu Xu

**Summary:** Identifies that the Epps-Pulley regularization objective used in latent world models has vanishing gradients for tail samples, and fixes it with a quantile-quantile matching objective (plus a cross-batch variant) that better controls heavy-tailed latent deviations, improving planning success across four control environments.

**arXiv:** [arxiv.org/abs/2607.28415](https://arxiv.org/abs/2607.28415)
**Sources:** arXiv (cross-listed cs.AI, cs.CV, cs.LG)
**Why trending:** Triple cross-listed; targeted, well-motivated fix to a specific failure mode in latent world models for planning.
