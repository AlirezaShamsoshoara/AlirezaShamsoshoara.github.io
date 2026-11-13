---
title: "Daily AI Papers — November 14, 2026"
date: 2026-11-14
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-14/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal-agents
  - agent-memory
  - robot-learning
---

### 1. Unbundling Multimodal Vision Encoding
**Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, Marjan Ghazvininejad, Luke Zettlemoyer, Lucas Beyer, Mengye Ren, Jakob Verbeek, Saining Xie, Hu Xu
**arXiv:** [arxiv.org/abs/2611.17334](https://arxiv.org/abs/2611.17334)
**Summary:** A compute-matched study separates vision pretraining, dedicated visual capacity, and the placement of that capacity within multimodal language models. Dedicated vision capacity matters more than a pretrained visual prior, and inserting vision-only modules early inside the backbone matches a conventional encoder while potentially reducing time to first token.

---

### 2. Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent Interaction
**Authors:** Yunzhe Wang, Mesut Erhan Unal, Sheng Zhang, Shabnam Ghadar, Peng Tang
**arXiv:** [arxiv.org/abs/2611.10439](https://arxiv.org/abs/2611.10439)
**Summary:** MixUA extracts lessons from user-agent trajectories and assigns them to pair, user, agent, or global memory scopes according to usefulness and privacy. On CrossLearnBench it improves pass rates by up to 16 percentage points over no memory, retains up to 90% of preferences, and exposes planted private facts in at most 0.02% of forbidden-scope probes.

---

### 3. RoboHarness: A Simple Harness Outperforms VLA and World Action Models
**Authors:** Bince Qu, Wei Chen, Bo Zhang
**arXiv:** [arxiv.org/abs/2610.14018](https://arxiv.org/abs/2610.14018)
**Summary:** RoboHarness gives coding agents a visual-geometric control panel for understanding and invoking robotic manipulation tasks without training a dedicated action-generating model. The authors report that Qwen3.8-Flash-Next using this open-source harness outperforms state-of-the-art vision-language-action models on BEHAVIOR Challenge 2025 tasks.

---

### 4. JustRUA: A Controlled Study of GPT-6 Robot-Use Agents
**Authors:** Zefan Wang, Yufan Dang, Xuanwei Shi, Mingqi Gao, Cheng Yin, SikYuen Tam, Hanyu Liu, Yasheng Wang, Yaxi Lu, Songyang Zhang, Xin Cong, Yuan Yao
**arXiv:** [arxiv.org/abs/2611.16009](https://arxiv.org/abs/2611.16009)
**Summary:** JustRUA studies robot-use agent design under a controlled framework, separating harness history, action interfaces, experience reuse, and scene geometry. A simplified official L3 harness raises RoboDojo simulation scores from 29.7 to 50.3 without a learned policy, self-improvement loop, or task-specific tuning.

---

### 5. TurtLES: A Large-Scale Benchmark for Turbulent 3D Neural PDE Surrogates
**Authors:** Jarno Platenburg, Armand Kassaï Koupaï, Paola Cinnella, Patrick Gallinari
**arXiv:** [arxiv.org/abs/2611.09567](https://arxiv.org/abs/2611.09567)
**Summary:** TurtLES provides a 14 TB benchmark of three-dimensional turbulent cylinder wakes, with 400 trajectories of 400 time steps and 3 to 11 million mesh points per frame. Neural-operator evaluations expose temporal instability, loss of small-scale energy, and difficulties handling large irregular domains during autoregressive rollouts.

---

### 6. Humanized but Still True? Auditing Facts and Detection in AI-Text Humanizers
**Authors:** Ziyuan Wang, Genliang Zhu, Xiaobo Chen
**arXiv:** [arxiv.org/abs/2611.00359](https://arxiv.org/abs/2611.00359)
**Summary:** This audit checks whether AI-text humanizers preserve numbers, names, dates, and quotations, finding that all 11 tested commercial tools altered or dropped at least one such unit in 35% to 65% of eligible documents in the main cycle. Fact retention was not clearly correlated with detector evasion, and detector comparisons reveal substantial false positives and failures on contemporary AI-styled text.

---

### 7. Consensus Capture in Reference-Based UAV Video Stabilization: A Benchmark on Dynamic Urban Scenes
**Authors:** Robert Fonod, Nikolas Geroliminis
**arXiv:** [arxiv.org/abs/2611.17190](https://arxiv.org/abs/2611.17190)
**Summary:** This UAV stabilization benchmark studies consensus capture, where coherently moving vehicles pull a reference-frame homography toward foreground motion without suspicious inlier statistics. Static and dynamic evaluations of ten pipelines show that object masking removes capture for every tested pipeline while preserving the leading stabilization methods.

---

### 8. Back to Pixels: Lifting Latent Video Diffusion into Pixel Space
**Authors:** Yanke Song, Shuo Chen, Chris Rockwell, Guande He, Nan Liu, Desai Xie, Tianpei Gu, Yong-Hyun Park, Aryan V S, Dennis Yuren Menn, Ming-Hsuan Yang, Xun Huang
**arXiv:** [arxiv.org/abs/2611.17336](https://arxiv.org/abs/2611.17336)
**Summary:** PixVid converts a pretrained latent video diffusion model into a framewise pixel generator by retaining its diffusion transformer and replacing the VAE decoder with a convolutional rendering head. Fine-tuned from Wan2.1-14B on about 1.3 million clips, it remains competitive with the latent baseline while supporting twice the resolution at the same per-frame token count and next-frame responses to actions.

---

### 9. Experience-Handoff Reinforcement Learning for Recursive Self-Improvement
**Authors:** Doyoung Kim, Byeongguk Jeon, Kailin Zhang, Sherry Yang
**arXiv:** [arxiv.org/abs/2611.16409](https://arxiv.org/abs/2611.16409)
**Summary:** This reinforcement-learning method jointly trains an agent to act, reflect, and curate task-local playbooks within a fixed Agentic Context Engineering harness. It scores experience-handoff artifacts by their effect on future rollouts and achieves higher held-out benchmark performance than the evaluated baselines.

---

### 10. HiVe-Mem: Interleaving Horizontal Memory Expansion and Vertical Evidence Composition for Multimodal Agents
**Authors:** Haozhen Zhang, Bohan Liu, Jianzhu Bao, Qingyuan Liu, Haodong Yue, Xiao Li, Zi Pong Lim, Wenya Wang
**arXiv:** [arxiv.org/abs/2611.12872](https://arxiv.org/abs/2611.12872)
**Summary:** HiVe-Mem expands retrieved memory through a graph of textual and visual anchors, then uses a trainable selector to compose query-specific evidence from summaries, captions, images, and interaction histories. Across three multimodal memory benchmarks it improves task performance across base models while reducing token consumption by about 90% relative to the most efficient competing multimodal baselines.

---

### 11. Evidence-Guided Recovery for AI Agents with Ambiguous Tool Outcomes and Partial Execution
**Authors:** Genliang Zhu, Xiaobo Chen, Ziyuan Wang, Chu Wang
**arXiv:** [arxiv.org/abs/2610.41453](https://arxiv.org/abs/2610.41453)
**Summary:** This work formulates evidence-guided recovery for agent workflows whose tool actions may have failed, committed, or remained in flight, separating actual goal satisfaction from publicly supported safe completion. In a preregistered held-out comparison under a common shield, planning advice certifies 30 completions versus nine for evidence prompting across 58 paired units, with all 116 trajectories passing independent replay.

---

### 12. Probing Transformer Representations Layer by Layer, Module by Module
**Authors:** Ambroise Odonnat, Theo Gnassounou, Laetitia Chapel, Romain Tavenard, Ievgen Redko
**arXiv:** [arxiv.org/abs/2611.11531](https://arxiv.org/abs/2611.11531)
**Summary:** More than 144,000 linear-probing evaluations show that useful transformer features depend jointly on layer depth and the module being probed, rather than depth alone. Simple fixed module-aware probes recover an average of 42% of the best-pair gains for vision and 86% for language while usually improving over final-layer residual-stream probing.

---

### 13. Module-Aware Optimization for Graph Neural Networks
**Authors:** Guy Hadad, Haggai Roitman, Moshe Eliasof, Bracha Shapira
**arXiv:** [arxiv.org/abs/2611.08379](https://arxiv.org/abs/2611.08379)
**Summary:** GraphMuon adapts Muon's matrix updates to the covariance of graph-propagated layer inputs and normalizes steps by their induced effect on representations. It reports 1.32 to 2.42 times faster validation-loss time-to-target than AdamW on three large OGB benchmarks and lower time-to-target in 13 of 15 dataset-architecture configurations.

---

### 14. Mixed Signals: Weight-Space Programming for EEG and ECG
**Authors:** Dara Varam, Taraneh Aminosharieh Najafi, David Atienza
**arXiv:** [arxiv.org/abs/2611.13758](https://arxiv.org/abs/2611.13758)
**Summary:** This study tests whether language models can inspect, repair, and write small EEG and ECG networks directly in weight space without gradient descent. One experiment matches conventional training with six times fewer subjects, but the models struggle to improve already well-trained classifiers or reliably identify a network's task from its weights alone.

---

### 15. Do Multimodal Models Decide Consistently on Equivalent Optical Spectra?
**Authors:** Ziyuan Wang, Genliang Zhu, Xiaobo Chen
**arXiv:** [arxiv.org/abs/2611.00428](https://arxiv.org/abs/2611.00428)
**Summary:** This benchmark tests multimodal decision models on equivalent optical spectra represented as tables or plots, together with incomplete spectra that require abstention. Representation changes move accuracy by up to 41 percentage points within one model, and carefully designed fine-tuning examples are needed to prevent a shortcut that treats every truncated input as unanswerable.

---

### 16. CARTBench: Rubric-Based Evaluation of Shopping Advice for Complex and Ambiguous Requests with Timelines
**Authors:** Yuqin Dai, Zhanwei Zhang, Honghui Yang, Zhouheng Yao, Yueqi Zhang, Jingyu He, Chaoyang Shi, Fanding Wei, Boyuan Pan, Kai Xu, Yao Hu, Yongliang Shen
**arXiv:** [arxiv.org/abs/2611.05862](https://arxiv.org/abs/2611.05862)
**Summary:** CARTBench evaluates shopping assistants on complex, ambiguous, time-sensitive requests using cases from 17 retail domains, 1,603 product records, and 1,328 expert-annotated criteria. Under frozen rubrics, three of ten models exceed 90% on Core criteria but none exceeds 45% on Excellence, exposing gaps in product evidence and high-quality purchase advice.

---

### 17. The Value of Thinking: Learning When to Reason in Hybrid Decision Models
**Authors:** Zhengxu Yu, Ke Xu, Meng Fang, Haitham Ammar, Weilin Luo, Jun Wang
**arXiv:** [arxiv.org/abs/2611.16961](https://arxiv.org/abs/2611.16961)
**Summary:** A hybrid decision model routes each request between a token-free single-forward-pass decision and full autoregressive reasoning by estimating the expected value of thinking. Its 4B version matches or slightly exceeds Jev on JevBench with 72.5% lower median latency, while the 27B version reduces token cost by 80.1% on MiniWoB.

---

### 18. From Large Language Models to Efficient System One Models via Adaptive Computation
**Authors:** Minh-Anh Nguyen
**arXiv:** [arxiv.org/abs/2611.16321](https://arxiv.org/abs/2611.16321)
**Summary:** This study finds that decision information concentrates in intermediate LLM layers and that the final six layers can be removed without loss in the evaluated setting. Joint self-distillation of shared-depth submodels and lightweight exit gates matches or outperforms independently trained models across seven decision benchmarks while improving adaptive accuracy-efficiency trade-offs.

---

### 19. A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents
**Authors:** Jingjing Jiang
**arXiv:** [arxiv.org/abs/2611.14256](https://arxiv.org/abs/2611.14256)
**Summary:** This survey analyzes self-evolving multimodal agents across reasoning, generation, GUI and Web navigation, and embodied manipulation using an experience-feedback-update framework. It relates asymmetric transfer of improvement mechanisms to scenario-specific resource constraints and proposes matched-budget measurements that could test its still-unverified portability judgments.

---

### 20. Structured Confidence Perturbation via Fisher Geometry for Adversarial Training
**Authors:** Chenlong Wei, Hanling Wang, Chong Zhang, Qinkai Yu, Fangyu Wu, Xiaobo Jin
**arXiv:** [arxiv.org/abs/2611.14046](https://arxiv.org/abs/2611.14046)
**Summary:** This work proposes adversarial objectives that deform predictive confidence, combining cross-entropy with KL divergence and constructing perturbations through Fisher geometry. Theory links optimal perturbations to principal Fisher eigenvectors, while an efficient implementation reports stronger robustness and robust transferability across tested datasets and architectures.

---
