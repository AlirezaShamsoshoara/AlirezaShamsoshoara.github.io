---
title: "Daily AI Papers — November 16, 2026"
date: 2026-11-16
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-16/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robot-learning
  - multimodal-models
---

### 1. Envisioning Agentic Robotics: A New Era of Robotic Systems
**Authors:** Grid Robotics, Qingfeng Lan, Duo Li, Siyao Li, Yiheng Lyu, Shijian Lu, Zhenghao Qi, Shizun Wang, Xinchao Wang, Ming Yang, Zhiqin Yang, Zuhao Yang, Tao Yu
**arXiv:** [arxiv.org/abs/2611.18359](https://arxiv.org/abs/2611.18359)
**Summary:** This position paper argues that agentic robotics, in which a foundation model with an embodied harness acts as an "Embodied System 2" in a closed perception-reasoning-action loop, is replacing per-task policies. It proposes an evaluation framework covering both model capability and closed-loop system performance, plus a research roadmap toward sustained physical autonomy.

---

### 2. Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent
**Authors:** Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang, Yufei Zhang, Renrong Hu, Yi Zhang, Guiyu Ma, Tianyu Fan, Longze Chen, Hao Sun, Jiaming Li, Jiaming Yang, Xiaohao Liu, Tao Tan, Minzheng Wang, Hangtian Jia, Shuai Yuan, Lvdi Wang, Xiao Liu, Chao Ma, Yuting Zou, Yinhe Zheng, Xiaobo Xia, Dawei Jiang, Shaoqing Ren
**arXiv:** [arxiv.org/abs/2611.18397](https://arxiv.org/abs/2611.18397)
**Summary:** Gamer is a generalist agent framework pre-trained on tens of thousands of hours of device-level keyboard and mouse trajectories, then refined with sparse-thinking instruction tuning and stable multi-turn reinforcement learning. With a cloud-edge inference engine for low-latency real-time play, it generalizes across challenging 3D open-world games at near skilled-player efficiency and is competitive on 2D game benchmarks.

---

### 3. VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender
**Authors:** Yuzhe Chen, Muxi Diao, Lele Yang, Wenbin Xu, Xuyang Liu, Qile Su, Changyi Liu, Jiankang Chen, Kaiyu Jiang, Haoyu Zhang, Hongyi Fu, Jianxiong Wang, Tianke Zhang, Haonan Fan, Yingxin Li, Bingyi Li, Xu Wang, Xuanyu Zheng, Bin Wen, Tingting Gao, Wentao Zhang, Jiale Cao
**arXiv:** [arxiv.org/abs/2611.15789](https://arxiv.org/abs/2611.15789)
**Summary:** VibePrevisBench is a 242-task benchmark in which coding agents turn a brief into an executable 4D Blender scene and render a proxy video, scored by rule-based scene checks against hidden ground truth and a VLM-based screen check. Across 11 frontier coding agents, multimodal spatial and camera understanding separates the agents, and agents inspect their renders but fail to correct their errors.

---

### 4. MMFlash: Faster Speculative Decoding for Vision-Language Models
**Authors:** Sicheng Feng, Zigeng Chen, Song Wang, Gongfan Fang, Xinchao Wang
**arXiv:** [arxiv.org/abs/2611.18482](https://arxiv.org/abs/2611.18482)
**Summary:** The authors introduce a KL-based token-level visual-dependence metric and find that speculative-decoding acceptance falls from 46% to 22% as visual dependence rises. MMFlash adaptively upweights poorly drafted visually dependent tokens and adds sparse attention for long videos, achieving lossless speedups of up to 3.58x over standard decoding and outperforming EAGLE-3 and DFlash.

---

### 5. Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding
**Authors:** Zhongxing Xu, Zhonghua Wang, Zhe Qian, Shiyan Su, Ming Hu, Xiaocheng Zou, Wei Feng, Mingquan Lin, Yuyin Zhou, Yifan Peng, Hamid Rezatofighi, Zongyuan Ge
**arXiv:** [arxiv.org/abs/2611.12901](https://arxiv.org/abs/2611.12901)
**Summary:** This work observes that hallucinations in multimodal diffusion language models coincide with localized entropy spikes during iterative denoising. StepRefine is a plug-and-play decoding strategy that switches to probability-weighted latent refinement at spike steps under a stability controller, significantly reducing hallucinations across MDLMs on multimodal benchmarks.

---

### 6. MIRIX-2.0: Multi-Agent Memory System
**Authors:** Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan, Peng Xia, Yu Wang
**arXiv:** [arxiv.org/abs/2611.12068](https://arxiv.org/abs/2611.12068)
**Summary:** MIRIX-2.0 is a multi-agent memory system with six typed memory agents that keep complete records, a provenance hypergraph index, budgeted retrieval, and an offline AutoDream process that merges duplicates and distills skills. It is the most accurate compared system on four of five QA benchmarks, reaching 91.4% on LoCoMo and 72.6% on LongMemEval-S, and also leads as procedural memory on ALFWorld and WebShop without fine-tuning.

---

### 7. V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations
**Authors:** Keuntae Kim, Dongjun Kim, Yong Suk Choi
**arXiv:** [arxiv.org/abs/2611.17831](https://arxiv.org/abs/2611.17831)
**Summary:** The paper shows that video-language models built on V-JEPA ignore the dynamics their encoder captures, answering speed questions at chance while a linear probe reads speed at 87%. Using counterfactual pixel-transformation supervision on 4.53M public samples in a single stage, V-JEPA-LM models from 1B to 8B lead every size class across eleven video benchmarks.

---

### 8. DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery
**Authors:** Kailai Sun, Zijie Gao, Mingyi He, Can Rong, Alok Prakash, Baoshen Guo, Shenhao Wang, Jinhua Zhao
**arXiv:** [arxiv.org/abs/2611.17878](https://arxiv.org/abs/2611.17878)
**Summary:** DySENSE is a joint multimodal generative framework that synthesizes static urban satellite imagery together with spatially aligned dynamic monthly building energy maps, decoupling morphology from energy dynamics. Across four cities it produces high-fidelity annotated synthetic data from under 25% labeled data, boosting downstream prediction by 8% mIoU and reducing CVRMSE error by 9% to 18%.

---

### 9. Loopback Transformer: Towards a Unified View of Residual Looped Transformers
**Authors:** Xuan Ouyang, Zefan Cai, Chenlong Zhang, Cheng Luo, Ke Wan, Junjie Hu
**arXiv:** [arxiv.org/abs/2611.07226](https://arxiv.org/abs/2611.07226)
**Summary:** Taking a depth-memory view of residual connections, the authors argue looped Transformers should read individual block updates rather than full outputs, separating control of input strength, update weight, and allocation. The resulting Loopback Transformer, using geometric decay plus learned attention, beats standard Transformers on ClimbMix validation loss with 40-75% of their parameters at scales from 191M to 3B.

---

### 10. G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands
**Authors:** Yuechun Yu, Wenzheng Kong, Xiaofeng Mao, Jin Zhang
**arXiv:** [arxiv.org/abs/2611.17814](https://arxiv.org/abs/2611.17814)
**Summary:** G-CAST is a governed continual self-training system that turns daily production evidence into reward-routed, entropy-prioritized training data with governed reward evolution and checkpoint transitions. On a real production e-commerce agent, it adapts better to new demand while preserving accepted behavior than a strong autonomous post-training baseline, and it is deployed in Alibaba 1688's Yuancai procurement agent.

---

### 11. MEM-SQL: Memory-Empowered Text-to-SQL
**Authors:** Xiaoqi Wang, Wenqi Pei, Shizheng Hou, Yilai Liu, Han Chen, Boyan Li, Yuyu Luo, Hongyang Du
**arXiv:** [arxiv.org/abs/2611.18338](https://arxiv.org/abs/2611.18338)
**Summary:** The authors introduce HARE, a 1,600-request benchmark measuring how text-to-SQL systems adapt verified historical queries, and MEM-SQL, which stores query templates, reusable SQL blocks, and concept-to-schema mappings with on-demand schema linking. Across six language models, MEM-SQL raises mean execution accuracy from 37.1% to 50.0% while using 76.6% fewer input tokens and 68.8% lower latency.

---

### 12. JVT: Just Video Transformer makes pixel-space video diffusion simple
**Authors:** Jianjun Zhou, Hua Geng, Haoyu Guo
**arXiv:** [arxiv.org/abs/2611.18549](https://arxiv.org/abs/2611.18549)
**Summary:** JVT is a simple large-patch DiT-style Transformer for pixel-space video diffusion that needs no pretrained autoencoder, cascades, or U-Net skips, with systematic study of patch embeddings, registers, and adaptive normalization. It achieves quality competitive with latent diffusion baselines and naturally supports joint RGB-disparity generation that improves camera following and yields explicit geometry.

---

### 13. Aligning AI Teams
**Authors:** Siddarth Srinivasan, Morgan Jane Matthews, Jascha Sohl-Dickstein, Erik Jones
**arXiv:** [arxiv.org/abs/2611.17820](https://arxiv.org/abs/2611.17820)
**Summary:** This study investigates why alignment of individual LLM agents fails to transfer to multi-agent teams across software-engineering and consulting tasks, finding that diffusion of responsibility largely explains the safety gap. Common interventions such as peer critique do not reliably help, whereas a designated safety-lead agent or a coordinator-published safety specification restores single-agent alignment behavior.

---

### 14. GH-AWTrace: A Large-Scale Dataset of GitHub Agentic Workflow Execution Logs
**Authors:** Jasem Khelifi, Hao Li, Ali Ouni, Mohammed Sayagh, Mohamed Aymen Saied
**arXiv:** [arxiv.org/abs/2611.06866](https://arxiv.org/abs/2611.06866)
**Summary:** GH-AWTrace links 25,014 verified GitHub Agentic Workflows across 5,051 repositories to 4.1M run records and 562,877 execution log archives, preserving execution evidence alongside repository metadata and workflow configurations. Illustrative cases show the logs expose tool denials, provider failures, strategy changes, and delegation among agents.

---

### 15. WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents
**Authors:** Imene Kerboua, Fatemeh Pesaran Zadeh, Xing Han Lù, Weijian Qi, Alexander Miller, Junyi Song, Yunjia Tian, Dongjin Kang, Seyeon Choi, Marzia Nouri, Ewen Gueguen, Matteo Boglioni, Fengyuan Liu, Zeyi Liao, Mengqi Yuan, Yue Li, Alexandre Lacoste, Alexandre Drouin, Spandana Gella, Huan Sun, Gunhee Kim, Siva Reddy
**arXiv:** [arxiv.org/abs/2611.17955](https://arxiv.org/abs/2611.17955)
**Summary:** WebArena-Pro is a reproducible benchmark of 300 tasks across 20 self-hosted web applications in six domains, treating audio and video as core observations alongside text and vision. The best agents, Codex with GPT 6.1 Sol and Claude Code with Claude Opus 5.5, reach 62.3%, while the strongest generic agent configurations reach 30.3%.

---

### 16. Mobile AI Factory: Building Specialized Language Models for Your Mobile Device
**Authors:** Evan Li, Krishna Deshpande, Wen Cheng, Shyamnath Gollakota
**arXiv:** [arxiv.org/abs/2611.13509](https://arxiv.org/abs/2611.13509)
**Summary:** Mobile AI Factory is an agentic system in which an orchestrator LLM tunes hyperparameters, mines data, or generates synthetic examples to build a fine-tuned, quantized small language model for a given task and phone, guided by real on-device measurements. Across ten tasks and four Android phones, its on-device models beat two five-shot frontier models on five tasks and match them on three, while using 19x less GPU time than exhaustive training.

---

### 17. Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents
**Authors:** Subodh Lonkar
**arXiv:** [arxiv.org/abs/2611.16378](https://arxiv.org/abs/2611.16378)
**Summary:** Evidence-Governed Evolution (EGE) is a framework for deciding when autonomous agents should persistently adopt their own self-generated modifications, separating candidate generation from confirmatory adoption via fresh paired audits and non-inferiority tests. It provides evaluator-calibrated simultaneous lower bounds, reference-lineage degradation bounds, and audit-planning conditions, illustrated with a Monte Carlo stress test.

---

### 18. eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means
**Authors:** Kyudan Jung, Jihwan Kim, Minwoo Lee, Eunji Shin, Jaegul Choo
**arXiv:** [arxiv.org/abs/2611.18529](https://arxiv.org/abs/2611.18529)
**Summary:** eDIAR removes the fixed speaker-slot limit of neural streaming diarizers without retraining by clustering speaker embeddings inside a slot with the e-means algorithm once all slots are used, with bounded re-clustering windows. It remains accurate on hour-long meetings where Streaming Sortformer accumulates errors, and links speakers across large archives at k-means quality several times faster.

---

### 19. Emergent Biological Capabilities in a Foundation Model for Molecular Interactions
**Authors:** Adi Mashiach
**arXiv:** [arxiv.org/abs/2611.14504](https://arxiv.org/abs/2611.14504)
**Summary:** Bonbon is a foundation model for molecular interactions trained on about 3.2 trillion tokens of paired protein-ligand sequences, exhibiting zero-shot emergent capabilities in mechanism of action, binding-site localization, and covalent engagement. Its frozen representations achieve state-of-the-art binding and affinity prediction far faster than co-folding, and prospective wet-lab validation across nine targets yields a 61.5% dose-response hit rate on de novo compounds.

---

### 20. HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation
**Authors:** Shuai Yang, Fangyi Xu, Yishu Shen, Kecheng Zheng, Yinghao Xu
**arXiv:** [arxiv.org/abs/2611.16439](https://arxiv.org/abs/2611.16439)
**Summary:** HALO is a human-aligned data collection system for whole-body mobile manipulation that uses kinesthetic teaching and a low-resistance platform, with deployment-aligned processing that calibrates base motion and inpaints demonstrator hands. It collects demonstrations up to 2.9x faster than Mobile ALOHA and VR teleoperation, and trained policies reach 73.3% success on a six-stage long-horizon mobile manipulation task.

---
