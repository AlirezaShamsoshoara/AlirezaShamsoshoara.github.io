---
title: "Daily AI Papers — September 26, 2026"
date: 2026-09-26
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-26/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - embodied-ai
  - world-models
---

### 1. Learning to Discover Interesting Mathematics
**Authors:** Niket Patel, Ahmad Rammal, Amaury Hayat, Remi Munos, Julia Kempe
**arXiv:** [arxiv.org/abs/2609.28603](https://arxiv.org/abs/2609.28603)
**Summary:** The authors define a theorem's intrinsic interestingness as the ratio of proof length to statement length and show that it correlates strongly with downstream utility. A 27B proof-difficulty predictor then helps generate and select more interesting, less Mathlib-overlapping theorems for a self-expanding machine-verified library.

---

### 2. RGBD20K: A Large-Scale Benchmark for RGB-D Semantic Segmentation
**Authors:** Shaohua Dong, Zexuan Meng, Haiyan Sun, Bing Fan, Cuicui Zhang, Dylan Joseph, Kewei Sha, Yunhe Feng, Heng Fan
**arXiv:** [arxiv.org/abs/2609.29028](https://arxiv.org/abs/2609.29028)
**Summary:** RGBD20K provides 20,000 RGB-D image pairs across 160 fine-grained semantic categories, with annotations re-evaluated and corrected to reduce longstanding label noise. The accompanying score-purified fusion method achieves state-of-the-art results across the evaluated RGB-D segmentation benchmarks.

---

### 3. Self-Organizing Agent Teams Learn to Reason Together
**Authors:** Aneesh Pappu, Mirac Suzgun, Yongchan Kwon, Federico Bianchi, Batu El, Mykel J. Kochenderfer, Hancheng Cao, James Zou
**arXiv:** [arxiv.org/abs/2609.22682](https://arxiv.org/abs/2609.22682)
**Summary:** Self-Organizing Agent Teams learn reusable collaboration strategies that govern roles, conversational phases, participation, and information flow rather than relying on fixed protocols. Across mathematics and physics benchmarks, the teams average 66.7% accuracy versus 48.8% for their strongest member, with gains closely tied to whether correct reasoning is recognizable once produced.

---

### 4. MemoryAthena: Adaptive Routing over Latent and Generated Memories
**Authors:** Mingyuan Li, Guangsheng Yu, Juyuan Zhang, Xu Wang, Zhibo Man, Haonan Zhang, Shaoxiong Ji
**arXiv:** [arxiv.org/abs/2609.25853](https://arxiv.org/abs/2609.25853)
**Summary:** MemoryAthena combines direct Engram retrieval with memories generated from retrieved cues or backbone states, using a lightweight causal router to decide when generated memory should intervene. With the rest of the system frozen, this selective routing improves five-task question-answering and six-task general-NLP averages over direct retrieval alone.

---

### 5. FLEET: From Logits Entropy to Enhanced Trajectories in Text Generation
**Authors:** Oleksii Streltsov, Oleksandra Vitko
**arXiv:** [arxiv.org/abs/2609.27657](https://arxiv.org/abs/2609.27657)
**Summary:** FLEET records high-entropy token decisions as sparse trajectories and uses prior generations to adjust future logits, reducing the duplicate answers produced by memoryless repeated sampling. It matches repeated-sampling accuracy with a 3x speedup and raises LiveCodeBench Pass@32 from 59.9% to 66.2% under the same budget.

---

### 6. Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery
**Authors:** Rasmus Aagaard, Nicki Skafte Detlefsen
**arXiv:** [arxiv.org/abs/2609.27980](https://arxiv.org/abs/2609.27980)
**Summary:** The method ranks Whisper encoder layers by leave-one-layer-out word-error-rate impact, removes the six least consequential layers, and requires no custom inference implementation. Distillation on unlabeled monolingual speech recovers part of the pruning loss, improving mean WER from 21.9% after zero-shot pruning to 20.1%, compared with an 18.2% baseline.

---

### 7. Uranus: Building the Next-Generation Simulation Infrastructure for Embodied AI
**Authors:** Wenkang Qin, Yukun Zhou, Noah Shen, Jisong Cai, Dongxiao Mao, Baicheng Li, Yue Zhang, Wei Sui
**arXiv:** [arxiv.org/abs/2609.24815](https://arxiv.org/abs/2609.24815)
**Summary:** Uranus is a joint-trajectory-conditioned autoregressive diffusion simulator that streams open-ended robot rollouts across embodiments, viewpoints, and camera configurations. After inference optimization it generates at 24 FPS, and the authors release code and weights alongside in- and out-of-distribution evaluations.

---

### 8. The Linear Representation Hypothesis Needs a Group Action
**Authors:** Louie Hong Yao, Yuhao Li, Shengchao Liu
**arXiv:** [arxiv.org/abs/2609.27158](https://arxiv.org/abs/2609.27158)
**Summary:** The paper argues that the Linear Representation Hypothesis is a family of claims whose meaning depends on which representation transformations count as equivalent. It formalizes those equivalences with group actions and uses the framework to audit common metrics, reading points, and recent interpretability analyses.

---

### 9. StudentBench: AI and human tutoring yield equivalent GRE learning gains
**Authors:** Curtis Northcutt, Inaara Hasmani, Kevin Feng, Trevor Khangi, Andreas Plesner, Jonas Mueller
**arXiv:** [arxiv.org/abs/2609.28470](https://arxiv.org/abs/2609.28470)
**Summary:** StudentBench compares AI tutoring, expert human tutoring, and no tutoring across 2,383 participants working on GRE questions, supported by more than 175,000 student-AI messages. AI tutoring is statistically equivalent to expert human tutoring for learning gains, while one system achieves equivalent gains at 918 times lower cost per percentage point gained.

---

### 10. X-Planner: Event-Structured Task Planning for Embodied Intelligence
**Authors:** Howard Lu, Shalfun Li, Porter Pan, Cris, Lumen, Cyril, Eric Hu, Lily Li, Maeve Zhang, Robert Wang, KZ Zheng, Viggo Chen, Tim Ding, Regsis Cheng, YJ Xiao, Kian, Hai Lin, Alan Song, Elise Ma, Gody Li, Victor Yao, Yohann Tang, Ingrid Yu, Jason He, James Wang, Ryan Yu, Ping Yang, Chris Pan, Vincent Chen, Roy Gan, Hao Wang, Qian Wang
**arXiv:** [arxiv.org/abs/2609.25187](https://arxiv.org/abs/2609.25187)
**Summary:** X-Planner makes embodied task planning explicit through discrete event states and latent continuous reasoning states relayed across Transformer depths with Staircase Decoding. Its mixed-source supervision includes hierarchy-aware demonstrations, takeover-time annotations, and designed failures, and its offline planning scores place it second among four evaluated models on both reported measures.

---

### 11. Knowledge Pull Requests for Continual Document Authoring
**Authors:** Alexander Martin, Benjamin Van Durme
**arXiv:** [arxiv.org/abs/2609.26634](https://arxiv.org/abs/2609.26634)
**Summary:** Knowledge Pull Requests revise documents by extracting new claims, routing them to sections, flagging conflicts, and separating proposed knowledge changes from the resulting text diff. On multilingual Wikipedia revision and RAGTIME reports, KPRs integrate more information while preserving more existing content than source rewriting or full regeneration.

---

### 12. Self-Play Pretraining with Zero Data
**Authors:** Aditya Cowsik, Kfir Dolev, Michael Y. Li, G. Bruno De Luca, Nourya Cohen, Noah D. Goodman, Yoav Levine
**arXiv:** [arxiv.org/abs/2609.30063](https://arxiv.org/abs/2609.30063)
**Summary:** This proof of concept trains a generator and learner from random initialization, with the generator searching over programs for a universal Turing machine to create byte sequences at the learner's capability frontier. Without training on natural data, zero-shot natural-data loss scales predictably with self-play compute, and the models develop in-context learning and discover recognizable mathematical sequences.

---

### 13. Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale
**Authors:** Edesio Alcoba, Kevin Rossell, Aman Gupta, Shao Tang, Jiwoo Hong, Pabel Carrillo-Mendoza, Wanderson Conceição Ferreira, Alvaro Tedeschi, Zayd Simjee, Shreya Rajpal, Bruno Finardi Hime, Christian Sousa, Luis Moneda, Herbert Fei, Daniel Silva, Rohan Ramanath
**arXiv:** [arxiv.org/abs/2609.30137](https://arxiv.org/abs/2609.30137)
**Summary:** The authors use synthetic customers and simulated tool outputs to screen multi-step customer-experience agents before production deployment. Across Nubank deployments, simulation scores correlate with production evaluations, while simulation-guided choices produce a 36.69-point tNPS gain in one live test and an 8.82-point self-service-rate gain in another.

---

### 14. Multimodal Thinking with Renderable Programs
**Authors:** Sunli Chen, Ding Zhong, Ziqiao Ma, Jiaxin Liu, Zeyuan Yang, Hao Zhang, Lie Lu, Joyce Chai, Chuang Gan
**arXiv:** [arxiv.org/abs/2609.30130](https://arxiv.org/abs/2609.30130)
**Summary:** SVGLM uses scalable vector graphics as both image descriptions and text instructions, allowing vision-language models to generate interpretable images inside their reasoning chains. Training on a curated SVG editing dataset yields strong SVG generation and image-assisted mathematical reasoning, positioning renderable programs as a bridge between textual and visual thought.

---

### 15. TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations
**Authors:** Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta, Fan Zhang, Tanner Schmidt, Jakob Engel, Katerina Fragkiadaki, Adam W. Harley
**arXiv:** [arxiv.org/abs/2609.30222](https://arxiv.org/abs/2609.30222)
**Summary:** TrackEverything represents video as persistent world-coordinate 3D scene tracks, de-duplicating repeated geometry so complexity scales with the physical scene rather than clip duration. It tracks all visible points for videos longer than 1,000 frames within 40 GB of GPU memory and exceeds open-source dense 3D trackers by more than 20% APD on short TAPVid-3D clips.

---

### 16. Minimally Invasive Steering of Language Models
**Authors:** Taha Entesari, Jingyu Zhang, Daniel Khashabi, Mahyar Fazlyab
**arXiv:** [arxiv.org/abs/2609.30218](https://arxiv.org/abs/2609.30218)
**Summary:** MISVO steers frozen language models at test time while penalizing interventions according to the local KL geometry of the output distribution. Across preference and code-generation tasks on roughly 1B-to-14B-parameter models, it earns the highest mean reward in six of seven settings while keeping diversity and coherence near Best-of-N.

---

### 17. How does Adversarial Influence Scale in Multi-Agent Systems?
**Authors:** Addison J. Wu, Jasin Cekinmez, Michel Liao, Karthik Narasimhan, Thomas L. Griffiths
**arXiv:** [arxiv.org/abs/2609.30028](https://arxiv.org/abs/2609.30028)
**Summary:** The study finds that deception-induced defection in multi-agent deliberation grows with the proportion of deceptive agents rather than the absolute group size. LLM agents switch away from initially correct answers even when deceivers are a minority, and privately coordinating deceivers can unexpectedly become less effective.

---

### 18. AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control
**Authors:** Jiabin Qiu, Zixuan Chen, Hongye Cao, Jieqi Shi, Jing Huo, Yang Gao
**arXiv:** [arxiv.org/abs/2609.30264](https://arxiv.org/abs/2609.30264)
**Summary:** AD-WM trains latent world models to preserve action-dependent differences needed for counterfactual model-predictive control, rather than optimizing factual prediction alone. It raises hard-start success on OGBench-Cube from 3.7% to 52.0% over a matched baseline and improves zero-shot Franka pick-and-place success from 42.2% to 71.1%.

---

### 19. FlashLoop: Fast and Memory-Efficient Looped Transformers via Lazy Updates
**Authors:** Wanqi Yang, Shiwei Liu
**arXiv:** [arxiv.org/abs/2609.29812](https://arxiv.org/abs/2609.29812)
**Summary:** FlashLoop removes redundant work across repeated Transformer loops through token-sparse updates, sparse attention, and low-bit quantization of inter-loop KV residuals. The training-free framework preserves accuracy while delivering up to 1.64x end-to-end speedup and up to 6x KV-cache memory reduction.

---

### 20. Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think
**Authors:** Xvyuan Liu, Jianjie Fang, Chen Gao, Yong Li
**arXiv:** [arxiv.org/abs/2609.30036](https://arxiv.org/abs/2609.30036)
**Summary:** The authors show that visual world-model planners can fail when they score only distance to the final goal because successful actions may initially move away from it. Anchored Planning instead retrieves and targets intermediate observations, outperforming the released LeWM planner on every long-range task tested without retraining the frozen model.
