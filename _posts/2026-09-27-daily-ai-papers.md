---
title: "Daily AI Papers — September 27, 2026"
date: 2026-09-27
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-27/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - llm-reasoning
  - ai-agents
  - multimodal-ai
---

### 1. Single-stream Policy Optimization
**Authors:** Zhongwen Xu, Zihan Ding
**arXiv:** [arxiv.org/abs/2509.13232](https://arxiv.org/abs/2509.13232)
**Summary:** Single-stream Policy Optimization replaces group-based baselines with a persistent KL-adaptive value tracker and globally normalized advantages, avoiding degenerate groups and synchronization barriers in LLM reinforcement learning. On five hard mathematics benchmarks with Qwen3-8B, it improves average maj@32 by 3.4 percentage points over GRPO while converging more smoothly and wasting less computation.

---

### 2. Self-Supervised Prompt Optimization
**Authors:** Jinyu Xiang, Jiayi Zhang, Zhaoyang Yu, Xinbing Liang, Fengwei Teng, Jinhao Tu, Fashen Ren, Xiangru Tang, Sirui Hong, Chenglin Wu, Yuyu Luo
**arXiv:** [arxiv.org/abs/2502.06855](https://arxiv.org/abs/2502.06855)
**Summary:** Self-Supervised Prompt Optimization compares model outputs with an LLM evaluator and uses an LLM optimizer to improve prompts without ground-truth answers or human references. Across closed and open-ended tasks, it matches or exceeds prior prompt-optimization methods using only three samples and 1.1% to 5.6% of their cost.

---

### 3. PyTorch Distributed: Experiences on Accelerating Data Parallel Training
**Authors:** Shen Li, Yanli Zhao, Rohan Varma, Omkar Salpekar, Pieter Noordhuis, Teng Li, Adam Paszke, Jeff Smith, Brian Vaughan, Pritam Damania, Soumith Chintala
**arXiv:** [arxiv.org/abs/2006.15704](https://arxiv.org/abs/2006.15704)
**Summary:** The paper details PyTorch DistributedDataParallel and the dependencies between gradient computation and communication that make distributed training difficult to optimize. Gradient bucketing, communication-computation overlap, and optional synchronization skipping deliver near-linear scalability when training across 256 GPUs.

---

### 4. Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction
**Authors:** Yang-Tian Sun, Tianjia Liu, Zehuan Huang, Yi-Hua Huang, Xiaoyang Lyu, Ziyi Yang, Zi-Xin Zou, Yuan-Chen Guo, Yan-Pei Cao, Xiaojuan Qi
**arXiv:** [arxiv.org/abs/2609.23796](https://arxiv.org/abs/2609.23796)
**Summary:** Mira-Scene replaces sparse object-pose regression with Canonical Coordinate Maps, dense pixel-aligned fields that pair with scene-space point clouds to recover object transformations through geometric alignment. Its multimodal diffusion transformer improves layout accuracy over SAM3D by 39.8% in 3D-IoU and 16.5% in 2D-IoU across diverse scenes.

---

### 5. Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents
**Authors:** Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Yi Nie, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, Jiaji Rao, Zhengru Fang, Changxu Wei, Yu Wang, Wenbo Ding, Chao Yu
**arXiv:** [arxiv.org/abs/2607.08448](https://arxiv.org/abs/2607.08448)
**Summary:** Harness VLA treats a frozen vision-language-action model as a retryable contact-rich primitive and combines it with analytic primitives plus memory of successes, failures, and operating ranges. Without fine-tuning the VLA, it improves success by 38.6 and 25.4 percentage points on LIBERO-Pro and RoboCasa365 and demonstrates recovery and retargeting on dual-Franka robots.

---

### 6. SAGE: Mitigating Long-Horizon Reasoning Biases via Topological Guidance
**Authors:** Xinyue Zeng, Jiawei Zhang, Yujun Yan, Dawei Zhou
**arXiv:** [arxiv.org/abs/2609.30192](https://arxiv.org/abs/2609.30192)
**Summary:** SAGE addresses exploration and compounding biases in long-horizon reasoning with algebraic sparsification of candidate branches and hyperbolic guidance that supplies depth-wise structural signals. It outperforms competing methods across 12 benchmarks and seven model families, including an eightfold improvement on the Andrews-Curtis problem.

---

### 7. Synthetic Hospital: An Open, Verifiable, Physician-Validated Longitudinal EHR Benchmark
**Authors:** Christine Park, Valerie Chen, Tim Dettmers
**arXiv:** [arxiv.org/abs/2609.30027](https://arxiv.org/abs/2609.30027)
**Summary:** Synthetic Hospital provides 1,268 fully synthetic longitudinal patients and 5,602 encounters grounded in public medical-education sources, standard clinical ontologies, and complete provenance. Physicians distinguish its records from real charts at near-chance rates, while frontier models still miss roughly half of clinically relevant findings during chart summarization.

---

### 8. Learning to Ideate for Scientific Impact
**Authors:** Shubham Kale, Aniketh Garikaparthi, Manasi Patwardhan
**arXiv:** [arxiv.org/abs/2609.29802](https://arxiv.org/abs/2609.29802)
**Summary:** The authors build a dataset from more than 100,000 computer-science papers and train a reward model to predict year-normalized citation-impact labels from research goals and proposed ideas. Reinforcement learning with that outcome-grounded signal produces ideas with higher estimated impact than both the base model and supervised fine-tuning baselines.

---

### 9. Breaking the Environment Wall: Evolving LLM Agent Environments for Recursive Self-Improvement
**Authors:** Yukai Wu, Yuanjing Yang, Le Zhou, Shaokun Han, Haoyu Wang, Zirui Tang, Weihuang Zheng, Maxm Pan, Xuanhe Zhou, Fan Wu
**arXiv:** [arxiv.org/abs/2609.29773](https://arxiv.org/abs/2609.29773)
**Summary:** Env-Rethink organizes fragmented agent environments with collection maps and event logs, learns to identify environmental noise, and creates harder virtual histories for further training. Its 27B post-trained model improves rubric pass rate by more than 15.1% across nine downstream agents on 30 tasks.

---

### 10. iCoder-27B: Recursive AI-Led Development of Frontier Industrial Coding Model
**Authors:** Cheng Yang, Jiayang Lyu, Shangyuan Liu, Guibin Zhang, Jiong Lin, Xinlei Yu, Junchi Yan, Shuicheng Yan, Weinan E, Linfeng Zhang, Linfeng Zhang, Qibing Ren
**arXiv:** [arxiv.org/abs/2609.29626](https://arxiv.org/abs/2609.29626)
**Summary:** iCoder concentrates human input into reusable research skills while an agent selects experiments, evolves data, diagnoses outcomes, and coordinates supervised fine-tuning, self-distillation, and reinforcement learning. The resulting 27B industrial coding model leads RTLLM, ranks second on CVDP and KernelBench L2, and ties the best TritonBench result among the evaluated systems.

---

### 11. Jev-Mobile: Jev as an Executor for Mobile GUI Agents
**Authors:** Linghua Zhang
**arXiv:** [arxiv.org/abs/2609.30186](https://arxiv.org/abs/2609.30186)
**Summary:** Jev-Mobile separates low-frequency vision-language-model planning from high-frequency execution by letting a typed decision model choose actions within an accessibility-tree action space. On AndroidWorld it achieves 79% success while reducing successful-run execution time by 32.7% and model API cost by 73.4% relative to a step-wise VLM baseline.

---

### 12. C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks
**Authors:** Xueshu Chen, Yan Wang, Zihao Xue, Jiefu Li, Zhenfang Liu, Jayden Chen, Zhen Bi, Jungang Lou
**arXiv:** [arxiv.org/abs/2609.29735](https://arxiv.org/abs/2609.29735)
**Summary:** C3M maintains a bounded active index over persistent text-image evidence, consolidating safe redundancy while preserving conflicting observations and source provenance. At query time, budgeted routing selects index pages and expands their linked evidence to support reliable reasoning across long-running sessions.

---

### 13. To Think or Not to Think: Allocating Reasoning Where It Helps
**Authors:** Zhengdong He, Yunfan Zhou, Jianguo Yao, Haibing Guan, Xijun Li
**arXiv:** [arxiv.org/abs/2609.29664](https://arxiv.org/abs/2609.29664)
**Summary:** The paper finds that extra reasoning mainly helps partially solvable questions, rather than benefiting all difficult questions monotonically. Its CARE reward estimates useful length adjustments from sampled responses, improving Pass@1 by up to 4% while cutting reasoning length by 37% with no extra inference cost.

---

### 14. PoEM: Predicting RL Outcomes from Existing Policies
**Authors:** Kimia Hamidieh, Giannis Daras, Antonio Torralba
**arXiv:** [arxiv.org/abs/2609.30226](https://arxiv.org/abs/2609.30226)
**Summary:** PoEM predicts the policy produced by a new reinforcement-learning reward from models already optimized for other rewards, using low-rank structure among their log-policies. Experiments across text and image modalities show that it can approximate new post-training outcomes without running another full RL process.

---

### 15. MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression
**Authors:** Youpeng Zhao, Tian Tan, Liqian Peng, Jun Wang, Alec Go
**arXiv:** [arxiv.org/abs/2609.29913](https://arxiv.org/abs/2609.29913)
**Summary:** MILO compresses many-shot key-value caches block by block and assigns low-rank budgets according to each block's information entropy. On Qwen2.5 models it reduces KV-cache memory by up to 50% and improves throughput by 1.8 times with negligible loss on classification and reasoning tasks.

---

### 16. Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases
**Authors:** Tapan Parikh
**arXiv:** [arxiv.org/abs/2609.30012](https://arxiv.org/abs/2609.30012)
**Summary:** The paper proposes frozen public stimuli and three inexpensive scoring methods for repeatedly measuring model behavior across vendors, prompts, and releases. Applied to four years of frontier and open-model releases, the assays reveal changing patterns in response convergence, resistance to leading prompts, behavioral consistency, and coding-agent compliance.

---

### 17. Artificial Societies Benchmark: A Validation Framework for Synthetic Research
**Authors:** Edoardo Chidichimo, Min Jun Jung, Felix P. S. Wallis, James K. He
**arXiv:** [arxiv.org/abs/2609.30030](https://arxiv.org/abs/2609.30030)
**Summary:** The Artificial Societies Benchmark combines 11 tests spanning internal, construct, and external validity to evaluate whether LLM-generated populations support intended research analyses. Comparisons across 20 human sources and nine language models show that synthetic respondents often over-converge, compress scales, and distort relationships between traits.

---

### 18. Sequential knowledge editing breaks a model's ability to tell good evidence from bad, without costing it accuracy
**Authors:** Atul Anand
**arXiv:** [arxiv.org/abs/2609.29587](https://arxiv.org/abs/2609.29587)
**Summary:** After 1,000 sequential edits, a conservatively tuned model retains its MMLU score but becomes markedly worse at choosing between remembered answers and conflicting retrieved evidence on untouched facts. The degradation persists across methods, models, datasets, and prompts, and retrieval accuracy falls from 0.592 to 0.46 despite conventional edit-success and locality metrics remaining strong.

---

### 19. Beyond Average Safety: Chance-Constrained LLM Fine-tuning
**Authors:** Taha Entesari, Mahyar Fazlyab
**arXiv:** [arxiv.org/abs/2609.29960](https://arxiv.org/abs/2609.29960)
**Summary:** The method constrains the fraction of safety examples whose degradation exceeds a chosen threshold, rather than controlling only average safety loss during fine-tuning. A differentiable conservative bound and constraint-aware gradient update emphasize tail failures and outperform prior safety-preserving baselines across three tasks and three models.

---

### 20. The Alignment Illusion in Multimodal Large Language Models
**Authors:** Hong-Han Wang, Yuntao Wang, Hu Ding
**arXiv:** [arxiv.org/abs/2609.30210](https://arxiv.org/abs/2609.30210)
**Summary:** Across 13 multimodal language models, four standard scalar alignment measures fail to consistently distinguish real visual tokens from Gaussian noise even when task accuracy collapses. The proposed principal-angle gap separates one-dimensional weight-induced similarity from richer visual structure and tracks performance more reliably under controlled corruption.
