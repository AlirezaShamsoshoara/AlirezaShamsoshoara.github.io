---
title: "Daily AI Papers — November 01, 2026"
date: 2026-11-01
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-01/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - efficient-training
  - visual-generation
---

### 1. Scaling Lean Theorem Proving for Real-World Code Verification
**Authors:** Debargha Ganguly, Divya Raghunathan, Dejan Jovanović, Vikash Singh, Soonho Kong, Aaron Tomb, Aman Goel, Ferhat Erata, Sam Bayless
**arXiv:** [arxiv.org/abs/2610.38174](https://arxiv.org/abs/2610.38174)
**Summary:** EasyProver combines recursive Lean agents, asynchronous search, parallel tactic probing, and elastic elaboration to tackle mathematical proofs and code verification without extra model training. The accompanying Aegis pipeline produces 2,045 validated Rust-Lean program pairs and 11,533 specifications, with EasyProver proving 52.7% of a 2,000-statement sample within 30 minutes per statement.

---

### 2. CausGround: Causal Interaction Grounding for Adaptive Embodied Planning
**Authors:** Yijun Shen, Diqi He, Jinbang Guo, Wanyue Zhang, Jiaming Mi, Huan Yang, Zhongyuan Wang, Zhiwei Yu, Kai Zhang
**arXiv:** [arxiv.org/abs/2610.29702](https://arxiv.org/abs/2610.29702)
**Summary:** CausGround turns interaction experience into reusable knowledge of action preconditions and effects, grounding it in current observations for embodied planning without parameter updates. It raises average VirtualHome task success from 24.9% to 53.3% and RoboCasa closed-loop success from 43.0% to 57.0%, with additional interaction-reasoning and real-robot evaluations.

---

### 3. PreView: Enhancing GUI Grounding with Preprocessed Views and Cues
**Authors:** Wenjun Hou, Kaishuai Xu
**arXiv:** [arxiv.org/abs/2610.33645](https://arxiv.org/abs/2610.33645)
**Summary:** PreView uses a lightweight auxiliary model to prepare zoomed task-relevant screenshot views and visual or textual cues for a frozen GUI-grounding model. Across five benchmarks, these inputs improve average grounding accuracy for Qwen3-VL-2B, OS-Atlas-4B, and Qwen3-VL-4B without further training the grounding models.

---

### 4. Instruction Capacity: Behavior and Degradation of Language Models under Controlled Load
**Authors:** Hennadii Kutomanov
**arXiv:** [arxiv.org/abs/2610.36095](https://arxiv.org/abs/2610.36095)
**Summary:** This paper measures instruction-following capacity using independent word-replacement rules with computable reference answers and a statistical model of increasing prompt load. In 2,958 GPT-4o mini requests covering 642,430 trials, it estimates capacity at roughly 37-38 rules for a 95% correct-replacement rate, falling to about 18-19 rules at full replacement density.

---

### 5. LOB-Impact Benchmark: Emergent Market Impact in Generative Limit Order Book Models
**Authors:** George Nigmatulin, Valentin Mohl, Sascha Frey, Kang Li, Aramis Marti-Shahandeh, Mihai Cucuringu, Anisoara Calinescu, Jakob Foerster, Stefan Zohren
**arXiv:** [arxiv.org/abs/2610.27100](https://arxiv.org/abs/2610.27100)
**Summary:** LOB-Impact benchmarks generative limit-order-book models by injecting execution-style orders and measuring price impact and subsequent relaxation rather than only matching historical distributions. Across five autoregressive models and five NASDAQ stocks, it finds emergent impact exponents of 0.63-1.21 but no observed impact decay in the tested models.

---

### 6. Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion
**Authors:** Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
**arXiv:** [arxiv.org/abs/2610.25276](https://arxiv.org/abs/2610.25276)
**Summary:** Holo4D reconstructs 3D trajectories from a source video and projects their geometry and appearance into target camera views to guide pretrained video diffusion. This scaffold supports camera-controlled novel-view generation while letting the generative prior complete unseen regions, and it accepts different 4D reconstructors without retraining the video generator.

---

### 7. ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics
**Authors:** Xiaohang Yu, Hejia Geng, William Knottenbelt
**arXiv:** [arxiv.org/abs/2610.23656](https://arxiv.org/abs/2610.23656)
**Summary:** ABF-Bench converts real laundering activity into interactive blockchain-forensics tasks in which every claimed fund movement must cite retrieved ledger evidence. Its working-memory agent harness reaches 75% edge recall versus 47% for Codex with the same model and 10% for Claude Code, while early stopping still limits recall on larger tasks.

---

### 8. Weaken to Strengthen: Weakening-Induced On-Policy Self-Distillation for Large Reasoning Models
**Authors:** Yecheng Wu, Song Han, Han Cai
**arXiv:** [arxiv.org/abs/2610.38681](https://arxiv.org/abs/2610.38681)
**Summary:** Weakening-Induced On-Policy Self-Distillation contrasts a reasoning model with a quantized or pruned weaker counterpart to generate training signals from unlabeled prompts without privileged teacher information. Across mathematical and coding benchmarks, quantization and pruning improve average accuracy over the original models by 4.0 and 5.5 percentage points respectively.

---

### 9. Know, then Draw: A New Learning Paradigm for Visual Generation
**Authors:** Yucheng Mao, Chongjian Ge, Zhuowen Tu, Hao Tan, Hanwen Jiang
**arXiv:** [arxiv.org/abs/2610.37626](https://arxiv.org/abs/2610.37626)
**Summary:** Know, then Draw separates semantic knowledge acquisition through autoregressive pretraining from high-fidelity rendering through diffusion post-training, using a purely semantic tokenizer and compute-optimal scaling laws. The authors train a 3B-parameter text-to-image model in 6,600 H100 GPU-hours and report scores of 86 on GenEval and 87 on DPG-Bench.

---

### 10. Unlocking Any-Order Generation in Pretrained Autoregressive Image Models
**Authors:** Rishav Pramanik, Marco Pedersoli, Zhaozheng Yin
**arXiv:** [arxiv.org/abs/2610.39293](https://arxiv.org/abs/2610.39293)
**Summary:** This work adapts pretrained raster-scan autoregressive image models into any-order generators using future-aware positional embeddings and an ordering curriculum while retaining the standard autoregressive inference stack. Across four base models, it enables inpainting, outpainting, and editing at 13-33% additional compute beyond pretraining, with ImageNet inpainting FID of 6.21 versus 10.44 for MaskGIT.

---

### 11. EPSBench: Benchmarking LLM Agents for Earnings Forecasting
**Authors:** Yanbin Yin, Chuyu Xu, Liqin Ye, Jing Peng, Chao Zhang
**arXiv:** [arxiv.org/abs/2610.38293](https://arxiv.org/abs/2610.38293)
**Summary:** EPSBench evaluates earnings-forecasting agents on 149 firm-quarters from 86 US companies using fixed financial evidence and a shared accounting calculator that converts cited driver estimates into diluted earnings per share. Three of six models show no detectable paired point-error difference from analyst consensus, but nominal 80% prediction intervals cover reported earnings in only 37-70% of interval-returning runs.

---

### 12. After One-Click Video: The Inflow of Service-Type Content, the Failure of the Recommendation Pool Mechanism, and the BoLe System
**Authors:** Bo Zou, Chao Xu
**arXiv:** [arxiv.org/abs/2610.37695](https://arxiv.org/abs/2610.37695)
**Summary:** This paper argues that AI-generated one-click explainer videos increase service-type content faster than expressive work-type content, straining recommendation systems that consume a fixed attention budget. A simplified model predicts recommendation-pool failure beyond a growth threshold, motivating a proposed BoLe system that separates machine-screened service content from human-judged expressive work.

---

### 13. FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet Loss
**Authors:** Hina Otake, Shinei Arakawa, Keitaro Tanaka, Yoshihiro Fukuhara, Hirokatsu Kataoka, Shigeo Morishima
**arXiv:** [arxiv.org/abs/2610.39423](https://arxiv.org/abs/2610.39423)
**Summary:** FDSML uses image-generation parameter distances to define triplet supervision for synthetic vision pretraining, pairing a refined fractal dataset with parameter-aware metric learning. With ResNet-50, it improves retrieval Recall@1 over FDSL pretraining from 65.6% to 74.0% on Stanford Online Products and from 56.2% to 78.4% on Stanford Cars.

---

### 14. Differentiable Data Augmentation with Kornia
**Authors:** Jian Shi, Edgar Riba, Dmytro Mishkin, Francesc Moreno, Anguelos Nicolaou
**arXiv:** [arxiv.org/abs/2011.09832](https://arxiv.org/abs/2011.09832)
**Summary:** This paper reviews Kornia's differentiable data-augmentation module for spatial 2D and volumetric 3D tensors and its integration with PyTorch autograd and optimization components. It also benchmarks augmentation frameworks and surveys approaches that use Kornia's differentiable augmentation capabilities.

---

### 15. world2vec: Mechanistic world models through latent dynamics learning
**Authors:** Tobias Schmidt, Rodrigo Gonzalez Laiz, Krisztián Szuppinger, Steffen Schneider
**arXiv:** [arxiv.org/abs/2610.40637](https://arxiv.org/abs/2610.40637)
**Summary:** World2vec learns reward-free latent dynamics from observations and actions to build mechanistic world models that preserve system behavior over long prediction horizons. The authors report strong pixel-based continuous control and accurate identification across 71 attractors while using at least an order of magnitude fewer parameters than DreamerV3, TD-MPC2, and LeWM.

---

### 16. How to Loop Your Transformer: Loop Scaling, Specialization, and Parallel Inference
**Authors:** Chanakya Ekbote, Artidoro Pagnoni, Devendra Singh Sachan, Shruti Bhosale, Mike Lewis, Maryam Fazel-Zarandi, Shashank Rajput, Sujan Kumar Gonugondla
**arXiv:** [arxiv.org/abs/2610.40325](https://arxiv.org/abs/2610.40325)
**Summary:** This study compares transformer looping designs under parameter, training-compute, and inference constraints, finding that full-model looping favors fixed-size budgets while middle-block looping better uses constrained training FLOPs. Small loop-specific adapters improve deeper looping, and revised parallel inference preserves current-token embeddings with separate normalization to recover stronger quality across tested scales and budgets.

---

### 17. Multi-View MoE: Letting Every Router Shape Expert Computation
**Authors:** Zelin Zhao, Tianchi Ma, Junyuan Shang, Shuohuan Wang, Dianhai Yu
**arXiv:** [arxiv.org/abs/2610.40577](https://arxiv.org/abs/2610.40577)
**Summary:** Multi-View MoE combines independently initialized routers and reuses their preferences to mix learned latent views into each selected expert's input without changing active-expert count, expert FLOPs, or all-to-all communication volume. A 24-layer 10B-A1B model trained on 708B tokens improves its nine-task downstream mean by 1.18 percentage points over the baseline.

---

### 18. VeriCUA: Verification as Agentic Exploration for Computer-Using Agents
**Authors:** Qiushi Sun, Da Yu, Alexander Knop, Amer Sinha, Lingpeng Kong, Ben Kao, Ravi Kumar, Pritish Kamath
**arXiv:** [arxiv.org/abs/2610.40578](https://arxiv.org/abs/2610.40578)
**Summary:** VeriCUA verifies computer-using agents through active evidence gathering, constructing a task rubric and choosing GUI or code checks to resolve unsupported completion requirements. Experiments across online and offline settings show better agreement with reference labels than compared baselines, including stronger rejection of false online completion claims.

---

### 19. Elucidating the Design Space of LM Data Attribution
**Authors:** Steven Yu, Sheng-Yu Wang, Kimia Hamidieh, Antonio Torralba, David Bau
**arXiv:** [arxiv.org/abs/2610.40655](https://arxiv.org/abs/2610.40655)
**Summary:** The Controlled Attribution Benchmark fine-tunes language models on fictitious knowledge to isolate how redundancy and lexical distractors affect training-data attribution. Negative log-odds gradients and top-token aggregation improve ground-truth recall by 35-72 percentage points across diagnostic baselines, with counterfactual retraining gains of up to 4.9 times on FTRACE-TREX.

---

### 20. SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization
**Authors:** Derong Jin, Xiyi Chen, Ming C. Lin, Ruohan Gao
**arXiv:** [arxiv.org/abs/2610.40640](https://arxiv.org/abs/2610.40640)
**Summary:** SonoWorld4D converts a monocular video into an explorable dynamic audio-visual scene by reconstructing moving sound sources and synchronizing audio diffusion across a physically grounded sound field. The resulting scene supports real-time novel-view visuals and spatial audio, with real-scene evaluations and a user study reporting perceptual realism and consistency with scene geometry.
