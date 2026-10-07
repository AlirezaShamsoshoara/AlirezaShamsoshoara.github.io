---
title: "Daily AI Papers — October 07, 2026"
date: 2026-10-07
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-07/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - model-efficiency
  - robotics
---

### 1. Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability
**Authors:** Bingxi Hou, Guochao Jiang, Guofeng Quan, Weiqing Li, Wenfeng Feng, Guohua Liu, Yuewei Zhang
**arXiv:** [arxiv.org/abs/2610.08448](https://arxiv.org/abs/2610.08448)
**Summary:** Cross-tokenizer on-policy distillation works surprisingly well using only strictly aligned 1:1 token groups, and a student-selected top-16 shared-vocabulary subset matches full shared-vocabulary training across math and code tasks. Adding span-level supervision for mismatched groups reduces accuracy because its gradients often conflict with the strict objective, favoring reliable compact supervision over maximal alignment coverage.

---

### 2. DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation
**Authors:** Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue
**arXiv:** [arxiv.org/abs/2610.03543](https://arxiv.org/abs/2610.03543)
**Summary:** DuoMatching augments joint video-distribution matching with frame-level marginal supervision from an image generator, using LatentBridge and temporal sampling to transfer visual and semantic priors across latent spaces. It improves composition, visual quality, and semantic alignment while largely preserving motion, earning more than 80% preference against every evaluated baseline in human studies.

---

### 3. TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models
**Authors:** Xin Wang, Hao Yu, Zhengyang Zhuge, Bochao Mao, Zheng Li, Junda Feng, Yuyan Luo, Yi Zhang, Yizhong Cao, Mi Zhang, Dayiheng Liu, Jianwei Zhang
**arXiv:** [arxiv.org/abs/2610.07767](https://arxiv.org/abs/2610.07767)
**Summary:** TRACE makes FP4 reinforcement learning for mixture-of-experts language models align training-side rounding with rollout-side quantization outcomes, while selectively caching deeper-layer quantization information. Across four large MoE models it matches BF16 rollout performance with FP4 weights, activations, and KV caches while delivering up to a 5.4-times rollout speedup.

---

### 4. CheckerBench: Can Long-Horizon Agents Synthesize Static-Analysis Checkers?
**Authors:** Hang He, Li Wang, Hao Chen, Yuchen Shao, Yuling Shi, Lisheng Wang, Peiyang Liu, Goose Lin, Zaiyuan Wang, Haiying Sun, Ting Su, Chengcheng Wan
**arXiv:** [arxiv.org/abs/2610.07557](https://arxiv.org/abs/2610.07557)
**Summary:** CheckerBench evaluates whether coding agents can build static-analysis checkers end to end through 300 tasks drawn from 297 CVEs, 167 repositories, and five language ecosystems. Across 21 model-harness configurations, mean Pass@1 is 32.30% and the best reaches 45.33%, showing that reusable checker synthesis remains difficult.

---

### 5. EVISKILL: Grounding Skill Evolution in Replayable Evidence
**Authors:** Yan Zhou, Yili Wang, Yiwei Dai, Qinggang Zhang, Xin Wang
**arXiv:** [arxiv.org/abs/2610.05030](https://arxiv.org/abs/2610.05030)
**Summary:** EVISKILL evolves reusable agent skills by preserving execution observations as Replayable Evidence Cards and linking each proposed edit to the context that supports it. Targeted replay verifies changes before persistence, while evidence and provisionally supported edits carry across epochs for further refinement.

---

### 6. From Evidence to Action: How Tool-Using Agents Fail
**Authors:** Hongzhan Lin, Shidong Cao, Ziyang Luo, Wenhao Chai, Mong-Li Lee, Wynne Hsu
**arXiv:** [arxiv.org/abs/2610.07753](https://arxiv.org/abs/2610.07753)
**Summary:** SafeActBench traces evidence-to-action failures across 656 cases spanning static judgments, investigated non-action, and single- or multi-action workflows. Ten model-harness configurations show that agents often stop investigating too early or act before establishing evidence, while dependent workflows add unresolved prerequisites and incomplete execution.

---

### 7. AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents
**Authors:** Dongki Kim, Namkyeong Lee, Surag Nair, Carl Edwards, Xiner Li, Edward De Brouwer, Jenna Lynn Collier, Sung Ju Hwang, Gabriele Scalia, Ehsan Hajiramezanali
**arXiv:** [arxiv.org/abs/2610.05140](https://arxiv.org/abs/2610.05140)
**Summary:** AutoSciBench represents scientific tasks as high-level concepts plus executable low-level recipes, then uses solver trajectories and judge feedback to close shortcuts and iteratively strengthen evaluation. In computational biology and materials science, its generated benchmarks lower average solver accuracy by 22.4 and 25.5 percentage points while receiving higher quality ratings across three domains.

---

### 8. World Action Learning via Interaction-Centric Spectral Latent Guidance
**Authors:** Zhiming Liu, Yikun Miao, Ying Chen, Hongrui Yin, Fangqi Zhu, Xiaoyi Pang, Quanxin Shou, Zhengyang Yan, Haodong Wang, Song Guo
**arXiv:** [arxiv.org/abs/2610.03607](https://arxiv.org/abs/2610.03607)
**Summary:** WING transfers interaction knowledge from egocentric video to robot policies by separating camera motion from hand-object dynamics and distilling the latter into latent actions. Spectral guidance aligns slowly varying task semantics across human and robot embodiments, producing strong simulation and real-world manipulation results.

---

### 9. Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing
**Authors:** Sohyun Lee, Yoonjae Baek, Jaesang Won, Jinnyeong Kim, Kang Hyunwoo, Seung-Hwan Baek, Ivan Laptev, Suha Kwak
**arXiv:** [arxiv.org/abs/2609.37334](https://arxiv.org/abs/2609.37334)
**Summary:** Self-compensating VLA adapts at deployment by using the residual between commanded and executed robot motion, requiring neither task rewards nor labels. On RoboStress and two physical arms with different wear histories, it outperforms base and training-time robustness methods and raises real-robot success by more than 30 percentage points per arm.

---

### 10. HuatuoGPT-3: RL-Only Domain Adaptation from Base Models
**Authors:** Junying Chen, Xinyuan Xie, Ziniu Li, Wenyuan Gu, Jianquan Li, Xiang Wan, Guangjun Yu, Ruoyu Sun, Haizhou Li, Benyou Wang
**arXiv:** [arxiv.org/abs/2610.05966](https://arxiv.org/abs/2610.05966)
**Summary:** OnePO enables RL-only domain adaptation by strengthening updates on informative low-probability teacher tokens early and retiring teacher outputs once the student surpasses them. Its HuatuoGPT-3 medical models reach 67.2 on HealthBench with 20,000 training samples, while the open 27B model reaches 70.1 overall and 71.4 on HealthBench Professional.

---

### 11. UNREAL: Unifying Retrieval and Long-Context with a Single Model
**Authors:** Edan Kinderman, Elad Hoffer, Yochai Blau, Brian Chmiel, Ron Banner, Daniel Soudry, Boris Ginsburg
**arXiv:** [arxiv.org/abs/2610.08463](https://arxiv.org/abs/2610.08463)
**Summary:** UNREAL derives retrieval queries from a frozen language model's internal representations and uses fewer than 500,000 trainable parameters to select evidence across both corpora and long prompts. It substantially improves multi-hop retrieval and long-context accuracy while reducing compute and time to first token from roughly 32,000 input tokens onward.

---

### 12. AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented Generation
**Authors:** Giulio Zeloni, Enrico Lo Conte, Salvatore Rionero, Giuseppe Santoro, Alessandro Rastelli, Fabio Sorrentino
**arXiv:** [arxiv.org/abs/2610.01218](https://arxiv.org/abs/2610.01218)
**Summary:** AGO is an evidence-first quality gate for retrieval-augmented generation that makes missing data and judge errors explicit, layers deterministic and model-based checks, and estimates regression risk probabilistically. Public RAGBench tests show that apparently well-formed judge output can still have weak discrimination, supporting mandatory per-engagement judge validation before release decisions.

---

### 13. Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents
**Authors:** Feiyu Gavin Zhu, Xiaoyu Zhu, Jiqi Yang, Rui Yang, Arnab Kumar Mondal, Yancheng Wang, Xinke Deng, Jean Oh, Reid Simmons, Joerg Liebelt, Xiang Kong, Zhongyu Jiang
**arXiv:** [arxiv.org/abs/2610.01892](https://arxiv.org/abs/2610.01892)
**Summary:** Selection-based Structured Reasoning replaces open-ended reasoning with parallel likelihood scoring over reusable natural-language candidates, sharing the context KV cache across choices. On seven multimodal search benchmarks with 2B and 4B models, it preserves competitive success while cutting per-turn reasoning latency by more than 90% and total inference latency by 28% to 54%.

---

### 14. MiniCorp: The Last Mile of the AI Agent Firm
**Authors:** Jingying Zeng, Zhenwei Dai, Jinning Li, Changho Shin, Dylan Zhang, Yuxuan Lu, Qi He, Dakuo Wang, Kai-Wei Chang
**arXiv:** [arxiv.org/abs/2610.05912](https://arxiv.org/abs/2610.05912)
**Summary:** MiniCorp simulates an e-commerce firm whose agents observe events, deliberate, make strategic decisions, and receive persistent feedback from dynamic customers and competitors. Checkpointed counterfactual replays produce longitudinal enterprise data unavailable from static archives and support studies of multi-agent coordination and long-term strategy.

---

### 15. Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment
**Authors:** Yihuai Hong, Shauli Ravfogel, Chen Zhao, Eunsol Choi
**arXiv:** [arxiv.org/abs/2609.38972](https://arxiv.org/abs/2609.38972)
**Summary:** CoT-Interpretability Alignment measures agreement between a model's written chain of thought and internal strategies detected by interpretability tools. Three models achieve only 44.8% to 75.9% alignment across three tasks, while post-training on accuracy and parametric-faithfulness rewards improves faithfulness without sacrificing task performance.

---

### 16. EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation
**Authors:** Yikai Qin, Yifei Deng, Mingjian Liang, Wenxuan Song, Zepeng Lin, Zhiyi Jiang, Jiajun Fu, Qiao Sun, Huashuo Lei, Xicheng Gong, Jiayi Chen, Han Zhao, Shuanghao Bai, Pengxiang Ding, Pengwei Wang, Haoang Li
**arXiv:** [arxiv.org/abs/2610.07969](https://arxiv.org/abs/2610.07969)
**Summary:** EmbodiedSmith recursively co-refines simulated assets, scenes, and tasks so scene generation anticipates task needs and task generation requests targeted scene changes. It supports complex embodiments, deformable objects, and fluids, while experiments show greater data diversity improves downstream policy generalization.

---

### 17. GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution
**Authors:** Geyi Yang, Zikun Qu, Xiang Li, Zhiyong Wang, Min Zhang, Shipei Zeng, Zhongxiang Dai
**arXiv:** [arxiv.org/abs/2610.00948](https://arxiv.org/abs/2610.00948)
**Summary:** GUI-HARVEST improves frozen-model GUI agents by grounding diagnosis in before-and-after screenshots, comparing repeated executions, and turning recurring failures into bounded harness edits with predicted effects. It delivers held-out gains across six backbone models, including 12.33 points on OSWorld-Verified and a 13.87-point transfer gain for GPT-5 on WindowsAgentArena.

---

### 18. DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation
**Authors:** Karn Tiwari, Varnith Chordia, Prathosh A P
**arXiv:** [arxiv.org/abs/2610.04596](https://arxiv.org/abs/2610.04596)
**Summary:** DiffGate combines group-relative reinforcement learning with bounded teacher guidance applied only to failed trajectories and scaled by group difficulty. Across two Qwen3 student sizes it improves code coverage and pass@8 over matched GRPO while preserving math average performance and improving math pass@8.

---

### 19. SlimWise: Decoupling Expert Pruning Across Prefill and Decode for Efficient MoE Serving
**Authors:** Gunho Park, Kyoungho Jeun, Juntaek Oh, Byeongjun Shin, Baeseong Park, Minsoo Rhu
**arXiv:** [arxiv.org/abs/2609.34117](https://arxiv.org/abs/2609.34117)
**Summary:** SlimWise keeps the full mixture-of-experts model for compute-bound prefill but uses a pruned expert pool for bandwidth-bound decoding, directly reusing the full model's KV cache. Its optional low-cost distillation narrows residual quality gaps, and a vLLM implementation improves decode throughput by up to 1.81 times at 50% expert pruning.

---

### 20. Adaptive Latent Capacity for World Models
**Authors:** Idan Achituve, Lior Dikstein, Idit Diamant, Arnon Netzer, Hai Victor Habi
**arXiv:** [arxiv.org/abs/2609.32921](https://arxiv.org/abs/2609.32921)
**Summary:** Adaptive LeWorldModel learns to place the most prediction-relevant information in early prefixes of a wide latent representation and samples how much capacity each sequence needs. Its MixSIGReg objective prevents collapse while organizing coordinates by importance, yielding higher visual-control success than tuned fixed-width models with lower average planning capacity.
