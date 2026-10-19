---
title: "Daily AI Papers — October 18, 2026"
date: 2026-10-18
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-18/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - language-models
  - multimodal-ai
---

### 1. LeanPRM: Lean-Grounded Process Supervision for Natural Language Proof Verification
**Authors:** Rodney Lafuente-Mercado, Salman Rahman, Jingyan Shen, James Shiffer, Saadia Gabriel, Pavel Izmailov
**arXiv:** [arxiv.org/abs/2610.17697](https://arxiv.org/abs/2610.17697)
**Summary:** LeanPRM uses paired natural-language and formal Lean proofs to generate step-level correctness labels without human annotation, filtering out failures caused only by formal syntax. Its 10,634 proofs and 152,000 labeled steps raise a Qwen3-4B verifier's exact step-label accuracy from 48.2% to 74.7% and improve proof selection and external verification performance.

---

### 2. Copy-Paste Language Models
**Authors:** Nathan Godey, Yoav Artzi
**arXiv:** [arxiv.org/abs/2610.19247](https://arxiv.org/abs/2610.19247)
**Summary:** Copy-Paste Language Models add a lightweight copying head beside the standard language-modeling head so Transformers can explicitly copy material from context. Pretraining experiments from 135M to 1.7B parameters show better training efficiency and downstream performance across backbones with negligible overhead, partly by easing the LM-head gradient bottleneck.

---

### 3. Scalable Weak-to-Strong Verifier Hardening for Agent Environments
**Authors:** Chong Zeng, Ziqian Zhong, Kexun Zhang, Ivan Bercovich, Ivgeni Segal, Yuzhen Mao, Shashwat Saxena, Aditi Raghunathan
**arXiv:** [arxiv.org/abs/2610.15924](https://arxiv.org/abs/2610.15924)
**Summary:** This work builds an isolated verifier sandbox and an automated hacker-fixer loop that repeatedly finds and repairs reward-hacking vulnerabilities in agent environments. Applied to Terminal Bench, KernelBench, and SETA, the iterative method substantially reduces attack success and strengthens defenses as the hardening budget grows.

---

### 4. Recursive Environment Scaling for General Long-Horizon Agents
**Authors:** Lingxiao Jing, Zhengbo Jiao, Yichen Xiang, Bofan Zhu, Lingbei Meng, Yan Ni, Haorui Chen, Ran Ran, Zhirong Shen, Yuheng Yang, Chenhang Cui, Yaosong Du, Rui Huang
**arXiv:** [arxiv.org/abs/2610.16397](https://arxiv.org/abs/2610.16397)
**Summary:** Recursive Environment Scaling raises agent-task difficulty by altering information access, resource relations, and execution dependencies while preserving each task's objective and completion requirements. Across 294 tasks, the resulting environments sharply reduce success for six evaluation models, while fine-tuning on their trajectories beats original-trajectory training in all nine comparisons.

---

### 5. Learning to Read Out: Unembedding Dynamics in Language Model Pretraining
**Authors:** Matteo He, William F. Shen, Alex Iacob, Andrej Jovanovic, Xinchi Qiu, Nicholas D. Lane
**arXiv:** [arxiv.org/abs/2610.21025](https://arxiv.org/abs/2610.21025)
**Summary:** Parameter-trajectory crosscoding tracks how every token's unembedding row evolves across checkpoints, separating information already encoded in hidden states from what the model's readout can express. In Pythia, the readout reorganizes within the first 0.4-1.1% of pretraining, showing that behavioral capability dates can lag the model's actual internal learning.

---

### 6. PathFM: Fast Generative Forecasting of Multivariate Trajectories
**Authors:** Jiachen Yao, Xiyuan Zhang, Annan Yu, Boran Han, Abdul Fatir Ansari, Shuai Zhang, Michael Bohlke-Schneider, Bernie Wang
**arXiv:** [arxiv.org/abs/2610.22358](https://arxiv.org/abs/2610.22358)
**Summary:** PathFM uses flow matching to generate complete future trajectories rather than independent marginal quantiles, preserving dependencies needed for cumulative demand, peak load, and event timing. One- or two-step distillation plus shared history caches makes multi-path sampling practical, while the model leads evaluated baselines on the new Forecast Path Score Bench.

---

### 7. Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization
**Authors:** Sekh Mainul Islam, Pepa Atanasova, Isabelle Augenstein
**arXiv:** [arxiv.org/abs/2610.22127](https://arxiv.org/abs/2610.22127)
**Summary:** The authors personalize three open-weight mixture-of-experts models and use crosscoders on paired activations to identify interpretable latents and experts associated with distinct personalization features. Causal interventions recover personalized behavior and reveal different routing paths, while the sparse models remain competitive with dense alternatives using fewer active parameters.

---

### 8. H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression
**Authors:** Or Ronai, Vladimir Kulikov, Tomer Michaeli
**arXiv:** [arxiv.org/abs/2610.18125](https://arxiv.org/abs/2610.18125)
**Summary:** H-DDCM replaces dense Gaussian codebooks in training-free diffusion compression with implicit randomized Hadamard dictionaries that need O(d log d) compute and O(d) memory. Its table-free coding and streaming video scheme deliver competitive rate-distortion-perception quality while enabling close-to-real-time long-form video compression on one GPU.

---

### 9. Speech event detector: Timestamped detection of non-verbal vocalizations and background sounds for rich speech transcription
**Authors:** Ayush Kumar Bar, Promila Ghosh
**arXiv:** [arxiv.org/abs/2610.14232](https://arxiv.org/abs/2610.14232)
**Summary:** This 5.8M-parameter convolutional-Transformer detects 54 classes of vocalizations and background sounds every 40 milliseconds and merges timestamped events into Whisper transcripts. Trained from seven heterogeneous public datasets, it covers 67% of held-out events in its sensitive profile and runs about 39 times faster than real time on eight CPU threads.

---

### 10. CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness
**Authors:** Dongjie Cheng, Ruifeng Yuan, Ran Wei, Ning Song, Yongqi Li, Wenjie Li
**arXiv:** [arxiv.org/abs/2610.21910](https://arxiv.org/abs/2610.21910)
**Summary:** CoWorld Reasoner exposes a video world model as a suite of visual-imagination tools that a vision-language model can choose, prompt, and interpret during reasoning. Co-evolving the tools, skills, and execution code improves the same backbone on all seven tested spatial, temporal, causal, and perceptual benchmarks without changing either model's weights.

---

### 11. When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill
**Authors:** Muhammad Ibrahim
**arXiv:** [arxiv.org/abs/2610.21500](https://arxiv.org/abs/2610.21500)
**Summary:** The paper shows that a shared remote KV-cache tier can make long-context serving slower than recomputation because bandwidth and fixed per-hit costs create unstable queues. Rank-sharded storage, asynchronous loading, and client fixes raise GET bandwidth 6.3 times and cut hit-heavy p99 latency from 83.32 seconds to 0.67 seconds.

---

### 12. PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation
**Authors:** Xinyu Guo, Chao Jing, Li Yi, Xingyu Chen, Zhengxing Wu
**arXiv:** [arxiv.org/abs/2610.16355](https://arxiv.org/abs/2610.16355)
**Summary:** PINT coordinates a vision-language model, video generator, and action expert through learned chunk-level Predictive Intent tokens while preserving each component's specialized pathway. Without embodied pretraining, it posts strong in-distribution results and large out-of-distribution gains on RoboTwin, LIBERO-Plus, and real-world bimanual tasks.

---

### 13. SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models
**Authors:** Xiaodong Wang, Tianle Li, Chuanxin Song, Junliang Xie, Zhanmi Zhong, Suiying Wu, Peixi Peng
**arXiv:** [arxiv.org/abs/2610.06598](https://arxiv.org/abs/2610.06598)
**Summary:** SimForcing distills motion priors from a simulation teacher into a real-domain robot world model and uses simulation trajectories as optional multi-block conditioning. It leads compared methods on Bridge video metrics without external embodied pretraining and improves downstream LIBERO policy success when used to initialize a vision-language-action model.

---

### 14. ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion
**Authors:** Zekai Gu, Peng Wang, Jiahao Lu, Yongsen Mao, Cheng Lin, Yuan Liu
**arXiv:** [arxiv.org/abs/2610.12625](https://arxiv.org/abs/2610.12625)
**Summary:** ForcingBooster dynamically allocates denoising steps per video patch so easy regions stop early while difficult regions receive additional refinement. A lightweight routing module cuts the total patch-level denoising work by about 50% while maintaining visual quality comparable to a four-step baseline.

---

### 15. One Bias Score, Two Factors: How Mitigations Affect Option Bias in Multiple-Choice Evaluation
**Authors:** Hyunjong Ok, Minjae Park, Jaeho Lee
**arXiv:** [arxiv.org/abs/2610.20993](https://arxiv.org/abs/2610.20993)
**Summary:** The paper decomposes pooled option-selection bias into flip rate across answer reorderings and positional skew among unstable questions. Across 41 checkpoints and 12 benchmarks, the factors reveal that prior correction mainly reduces symbol preference while reversal aggregation mainly improves stability, which can still stabilize wrong answers.

---

### 16. Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR
**Authors:** Nguyen Nguyen, Yongyi Zang
**arXiv:** [arxiv.org/abs/2610.20461](https://arxiv.org/abs/2610.20461)
**Summary:** semCER augments character error rate by assigning each grapheme edit an LLM-judged severity while retaining CER's alignment and denominator. Reader studies across English, Vietnamese, and Chinese show that the per-edit charges better expose damaging OCR mistakes, and the authors release 61 million judged edits plus a distilled scorer.

---

### 17. VascuSR: Iterative Anatomy-Aware Diffusion for CT Super-Resolution
**Authors:** Hairong Ni, Jiahe Huang, Minghao Guo, Wojciech Matusik, Rose Yu
**arXiv:** [arxiv.org/abs/2610.20509](https://arxiv.org/abs/2610.20509)
**Summary:** VascuSR couples diffusion super-resolution with an explicit 3D vascular representation, a structure refiner, and iterative anatomical feedback to avoid plausible-looking but unsupported vessels. On two CT datasets it improves vessel segmentation, connectivity, and centerline distance over interpolation and learned baselines while maintaining backbone-level image quality.

---

### 18. Diminishing Returns of Data in Sparse Autoencoders: Functional Behavior does not Guarantee Feature Reproducibility
**Authors:** Sambit Ghosh, Madelyn Mathai, R. Venkatesh Babu, Chirag Agarwal
**arXiv:** [arxiv.org/abs/2610.20680](https://arxiv.org/abs/2610.20680)
**Summary:** Experiments across four sparse-autoencoder architectures and three language models compare activation-data budgets from 5M to 500M tokens, separating functional convergence from one-to-one feature reproducibility. Reconstruction can stabilize at modest budgets while feature matching keeps improving, so cheaper training is viable when claims are paired with goal-specific reproducibility checks.

---

### 19. PAIR: Bridging Perception and Action in Vision-Language-Action Models
**Authors:** Kaixi Feng, Guoheng Sun, Ang Li
**arXiv:** [arxiv.org/abs/2610.09016](https://arxiv.org/abs/2610.09016)
**Summary:** PAIR learns Bridge Tokens that align visual-language features with horizon-matched action latents during training, giving the action expert an action-ready representation at inference. It improves OpenVLA-OFT and VLA-Adapter across LIBERO, CALVIN, and seven real-world tasks, including raising real-world OpenVLA-OFT success from 51.4% to 65.0%.

---

### 20. AI-Driven, Timing-Aware Power Optimization
**Authors:** Amit Sharma
**arXiv:** [arxiv.org/abs/2610.18890](https://arxiv.org/abs/2610.18890)
**Summary:** This framework uses gradient-boosted models to rank chip power-recovery edits and subsequent repairs while deterministic electronic-design analyses decide every acceptance. It specifies conservative acquisition, baseline-preservation, and repair-budget rules plus a public evaluation protocol, but reports no trained-policy results yet.

---
