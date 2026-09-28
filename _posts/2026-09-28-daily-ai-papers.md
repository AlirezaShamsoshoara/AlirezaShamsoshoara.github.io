---
title: "Daily AI Papers — September 28, 2026"
date: 2026-09-28
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-28/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - representation-learning
  - efficient-ai
  - ai-agents
---

### 1. FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders
**Authors:** Hongyang Du, Yunfei Xie, Junjie Ye, Jiawei Yang, Xiaoyan Cong, Haodong Zhang, Yongchao Huang, Haiyu Wu, Zongxia Li, Shihang Gui, Dawei Liu, Runhao Li, Jingcheng Ni, Chen Wei, Randall Balestriero, Yue Wang
**arXiv:** [arxiv.org/abs/2609.31620](https://arxiv.org/abs/2609.31620)
**Summary:** FuseReg trains representation autoencoders over random subsets of visual-encoder layers, penalizing sensitivity to cross-layer disagreement and allowing one decoder to reconstruct from full, sparse, or single-layer fusions. On ImageNet-256, it improves reconstruction flexibility and cuts unguided gFID by 27% with decoder replacement alone and 29% when regularizing both decoder and diffusion training.

---

### 2. RayOrch: Programming and Executing Lineage-Controlled Multi-Grain Dataflows for Foundation-Model Data Preparation
**Authors:** Xiaochen Ma, Zimo Meng, Junzhu Liang, Youhe Jiang, Yue Cheng, Hao Liang, Bohan Zeng, Dengchun Li, Lu Ma, Zhengyang Zhao, Zhen Hao Wong, Runming He, Meiyi Qiang, Jiangtao Guan, Binhang Yuan, Wentao Zhang
**arXiv:** [arxiv.org/abs/2609.18703](https://arxiv.org/abs/2609.18703)
**Summary:** RayOrch is a programming model and distributed engine that preserves parent-child lineage, child ordering, completion state, and result routing while batching variable-cardinality foundation-model data preparation. On NVIDIA H20 GPUs, it scales MinerU by 15.14 times and a video pipeline by 7.82 times, while reducing end-to-end time against Ray Data and Daft.

---

### 3. Block Sparse Attention with Log-Linear Complexity
**Authors:** Bohao Tang, Zhen Qin, Yuqi Pan, Zheng Li, Pengfei Liu
**arXiv:** [arxiv.org/abs/2609.31093](https://arxiv.org/abs/2609.31093)
**Summary:** PISA selects block-sparse attention keys through a coarse-to-fine pyramid, reducing the selection bottleneck from quadratic to log-linear complexity. Hardware-aware Triton kernels avoid materializing the full score matrix and match baseline commonsense performance while improving retrieval results.

---

### 4. InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data
**Authors:** Xingyu Miao, Zizun Li, Baole Fang, Kaiwen Song, Tenghui Wang, Hanxue Zhang, Yating Wang, Xudong Li, Yuping He, Xueyuan Wei, Chao Gao, Xijie Yang, Yingxiang Xu, Kerui Ren, Wenqi Guo, Jianjun Zhou, Xinzhe Wang, Weiguang Zhao, Ni Yang, Zetao Cai, Yufei Xue, Hengjie Li, Zeyu He, Yuanzhen Zhou, Rong Fu, Jianyang Zhang, Siwei Cui, Fuxian Huang, Yunsong Zhou, Xing Gao, Yifei Yao, Qiaojun Yu, Kailin Li, Ming Zhou, Mu Huang, Xinyue Li, Wenze Cui, Bingqi Jiang, Xueyue Zhu, Junting Dong, Haoyu Guo, Tao Lu, Mulin Yu, Bowen Zhou, Bin Zhao, Tianfan Xue, Weinan Zhang, Chunhua Shen
**arXiv:** [arxiv.org/abs/2609.31394](https://arxiv.org/abs/2609.31394)
**Summary:** InternW0-Δ combines pretrained video dynamics, semantic guidance, 4D geometry and motion priors, and action generation in a Mixture-of-Transformers world action model. Pretraining on more than 20,000 hours of aligned robot and human demonstrations produces strong results across simulation benchmarks and real-robot platforms.

---

### 5. Tactile-JEPA: Topology-Aware Self-Supervised Representation Learning for Distributed Tactile Sensors
**Authors:** Elizaveta Kovtun, Matvey Konovalov, Andrey Sakhovskiy, Semen Budennyy
**arXiv:** [arxiv.org/abs/2609.24385](https://arxiv.org/abs/2609.24385)
**Summary:** Tactile-JEPA learns topology-aware representations for sparse, irregular electronic skin by predicting masked sensor embeddings with graph-guided dual-scale masking. Across three tactile datasets, it reduces force-estimation error by 6.3% and in-hand orientation error by 20.8% over prior state of the art, with gains in policy learning as well.

---

### 6. Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem
**Authors:** Guoming Ling, Muen Xue, Zijian Ye
**arXiv:** [arxiv.org/abs/2609.30216](https://arxiv.org/abs/2609.30216)
**Summary:** This study analyzes 2,170 public GitHub projects to characterize how the low-cost Jev decision model is used for choices, judgments, and scores. It finds rapid ecosystem growth and broad reuse as a workflow component, while public attention concentrates on routing and interface agents rather than tracking project volume.

---

### 7. Enhancing Photogrammetric Digital Surface Models with Pretrained Diffusion Models and Multimodal Conditioning
**Authors:** Antoine Lorentz, Stéphane May, Valentine Bellet, Dawa Derksen, Bastien Nespoulous
**arXiv:** [arxiv.org/abs/2609.31199](https://arxiv.org/abs/2609.31199)
**Summary:** The authors adapt Stable Diffusion 3 with a pruned text stream and patch-wise normalization to refine noisy photogrammetric digital surface models using satellite imagery and LiDAR supervision. Multimodal conditioning lowers dense-urban elevation RMSE from 6.00 to 3.45 meters in seen cities and from 4.16 to 2.77 meters in held-out Bordeaux.

---

### 8. FoMo: Forking Moment in Generative Trajectory as a Perceptual Distance
**Authors:** Jaihyun Lew, Mingi Jung, Minjun Park, Wooseok Song, Sungroh Yoon
**arXiv:** [arxiv.org/abs/2609.25716](https://arxiv.org/abs/2609.25716)
**Summary:** FoMo uses the point at which two diffusion trajectories fork as an automatically generated pointwise label of perceptual distance between images. Models trained on these labels outperform human-annotated datasets across multiple image-quality benchmarks without requiring manual judgments.

---

### 9. AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-agent LLMs
**Authors:** Raphael Shu, Yusen Zhang, Young Min Cho, Jin Mo Yang, Yuan Yuan, Wenliang Zheng, Sharath Chandra Guntuku, Lyle Ungar, Zhou Yu, Rui Zhang
**arXiv:** [arxiv.org/abs/2609.31590](https://arxiv.org/abs/2609.31590)
**Summary:** AgentWorld evaluates genuine long-horizon collaboration with 100 human-annotated tasks requiring 3–20 independently acting agents to coordinate for more than 50 rounds in an MMORPG sandbox. Even the best tested model reaches only 52.0% task success, with recurring failures in communication, role assignment, and shared-plan maintenance.

---

### 10. SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL
**Authors:** Yan Zhan, Shaobo Liu, Qiunan Liu, Yuanjun Shi, Siqi Xu, WeiYi Hou, Xiang Xu, Zekang Li, Weizhou Pan, Jiahong Yan
**arXiv:** [arxiv.org/abs/2609.29050](https://arxiv.org/abs/2609.29050)
**Summary:** SLCA-GRPO separates credit assignment for tool-call tokens and user-facing summary tokens, preventing trajectory-level advantages from contaminating heterogeneous output segments. On a 7B model, it converges faster than standard GRPO and improves results by 2.53 points in-domain, 1.36 points on BFCL, and 9.15 points on τ²-Bench under equal budgets.

---

### 11. Game Arena: Strategic LLM Evaluation in Competitive Environments
**Authors:** Bovard Doerschuk-Tiberi, Yao Yan, Justin Chiu, Hann Wang, Timothy Chung, Martyna Plomecka, John Schultz, Jon Lipovetz, Clayton Drazner, Yuchen Zhuang, Jaimie Hwang, Nate Keating, Riley Jones, Andrew Lee, Oran Kelly, Ian Gemp, Michael Aaron, Laurel Prince, Kate Larson, Jeff Moser, Harrison Jobe, Chad Woodford, Siqi Liu, Andrew Wang, Bo Chang, Christopher D'Mello, Diane Chaleff, Addison Howard, Johnny Yip, Chuck Sugnet, Antonio Gulli, Meghan O'Connell, Will Cukierski, Nenad Tomasev, Dima Yeroshenko, Kinjal Parekh, Roxanne Daniel, Marc Lanctot, Domino Weir, Elsa Dong, Daniel Hennes, Melissa Nalubwama, Robert Fraser, Ryan Trostle, Jun Peng, Tom Mason, Lloyd Hightower, Chiamaka Chukwuka, Yuexiang Zhai, Phoebe Kirk, Yi Su, Yuting Han, Jie Ren, Chris Prichard, Sahand Sharifzadeh, Karim Hakimzadeh, DJ Sterling, Meg Risdal, Kate Olszewska, Ya Xu, Orhan Firat, Minmin Chen
**arXiv:** [arxiv.org/abs/2609.31473](https://arxiv.org/abs/2609.31473)
**Summary:** Kaggle Game Arena is an open evaluation platform where language models compete head to head in structured games rather than saturating static benchmarks. Its initial Chess, Poker, and Werewolf environments test strategic planning, adaptation, and robustness across perfect-information, imperfect-information, and multiplayer settings.

---

### 12. CARD: Cluster-level Adaptation with Reward-guided Decoding for Personalized Text Generation
**Authors:** Yutong Song, Jiang Wu, Weijia Zhang, Chengze Shen, Shaofan Yuan, Weitao Lu, Jian Wang, Yu Wang, Nikil Dutt, Amir M. Rahmani
**arXiv:** [arxiv.org/abs/2601.06352](https://arxiv.org/abs/2601.06352)
**Summary:** CARD clusters users by stylistic patterns, learns group-level LoRA adapters, and then captures individual differences through implicit preference learning without manual labels. At inference it keeps the base model frozen and applies lightweight preference vectors and low-rank logit corrections, improving quality and scalability on LaMP and LongLaMP.

---

### 13. Do Implicit Personalization and Explicit Styles Conflict? PsPLUG: A Lightweight Plug-in for Balancing Personalization and Style in Customized LLMs
**Authors:** Yutong Song, Jiang Wu, Shaofan Yuan, Chengze Shen, Jian Wang, Yu Wang, Nikil Dutt, Amir M. Rahmani
**arXiv:** [arxiv.org/abs/2601.06362](https://arxiv.org/abs/2601.06362)
**Summary:** PsPLUG addresses personalization collapse, where explicit style instructions suppress the user-specific traits that personalized language models are meant to preserve. Its lightweight residual plug-in accounts for requested style and lets users tune personalization strength at inference, improving the balance between preference preservation and style adherence.

---

### 14. IndicBankBench: Evaluating Safety and Reliability of Language Model Assistants in Indian Retail Banking
**Authors:** Suvradip Paul, Chandra Bhushan, Harsh Sharma, Nitin Kukreja, Yatharth Dedhia, Keyur Doshi, Prashant Devadiga
**arXiv:** [arxiv.org/abs/2609.29167](https://arxiv.org/abs/2609.29167)
**Summary:** IndicBankBench evaluates banking assistants at four stages—safety, tool use, response adequacy, and advisory quality—across 799 Indian retail-banking cases. Eleven models achieve only 43.7% to 58.2% strict three-run reliability, showing that at-least-once success substantially overstates dependable behavior.

---

### 15. TRACE: Temporal Audit and Condition-aware Evaluation of Streaming Video Understanding
**Authors:** Yibo Ma, Qianqian Zhang, Peng Liu, Tiancheng Zhao
**arXiv:** [arxiv.org/abs/2609.30670](https://arxiv.org/abs/2609.30670)
**Summary:** TRACE audits when streaming-video evidence becomes valid, how visual history is processed, and when systems emit responses rather than reporting only aggregate task scores. Across 1,240 records from 517 videos, it shows that similar QA accuracy can hide large differences in completion, validity, workload, delay, false alarms, and missed response windows.

---

### 16. ZooWork-ShopRanker: An Open, Preference-Aligned E-Commerce Reranker
**Authors:** Siqiao Xue, Shuxuan Liu, Ning Hu
**arXiv:** [arxiv.org/abs/2609.31002](https://arxiv.org/abs/2609.31002)
**Summary:** ZooWork-ShopRanker trains 0.6B, 4B, and 8B e-commerce rerankers on position-debiased preference labels from a panel of reasoning models, then distills the largest aligned model into smaller variants. All aligned models beat their unaligned bases on the new roughly 10,000-pair ShopRank-Bench, and the 4B and 8B models outperform the strongest open reranker baseline.

---

### 17. VLA-Precision: Asymmetric Co-Bootstrapping for Efficient Real-World Online RL of Vision-Language-Action Models
**Authors:** Chenyu Su, Zhaolong Shen, Yuan Qian, Chen Qian, Rui Zhang, Feng Yan, Weixing Chen, Fei Zhang, Jiamin Wang, Shuang Cong, Weiwei Shang
**arXiv:** [arxiv.org/abs/2609.04355](https://arxiv.org/abs/2609.04355)
**Summary:** VLA-Precision combines asymmetric co-bootstrapping with a streaming experience-policy architecture to stabilize and accelerate real-world online reinforcement learning for vision-language-action models. Across nine high-precision chemistry tasks and four robot embodiments, it reaches 98.3% mean success in 45.8 minutes per task while improving throughput and computational efficiency by up to 10.9 times.

---

### 18. Depth-adaptive Inference of Looped Language Models via Continuous Depth Batching
**Authors:** Kristian Schwethelm, Daniel Rueckert, Georgios Kaissis
**arXiv:** [arxiv.org/abs/2608.09444](https://arxiv.org/abs/2608.09444)
**Summary:** Continuous depth batching dynamically regroups tokens between recurrent loop steps so looped language models can vary computation by token without losing efficient batching. On Ouro 1.4B and Huginn 3.5B, the scheduler realizes up to 99% of the estimated maximum speedup available from depth-adaptive inference.

---

### 19. MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation
**Authors:** Tianze Xu, Yanzhao Zheng, Zhentao Zhang, Yuanqiang Yu, Chao Ma, Jihuai Zhu, Lelun Wu, Lyumanshan Ye, Pengfei Liu, Baohua Dong, Hangcheng Zhu, Ruohui Huang, Gang Yu
**arXiv:** [arxiv.org/abs/2609.30837](https://arxiv.org/abs/2609.30837)
**Summary:** MOPD-Router chooses and weights supervision from multiple teachers at every token without domain labels or a separately trained routing model. Its ExpertAlign metric delivers the strongest results in four evaluated settings, improving unlabeled-data performance by 12.3% over mean aggregation and labeled-data performance by 7.8% over standard MOPD.

---

### 20. CodeGraph: Open-Taxonomy Knowledge Graph for Source Code with Wikidata Grounding
**Authors:** Federico Pennino, Andrea Gurioli, Stefano Zacchiroli, Maurizio Gabbrielli, Paolo Ferragina
**arXiv:** [arxiv.org/abs/2609.29474](https://arxiv.org/abs/2609.29474)
**Summary:** CodeGraph uses a code-specialized language model and Wikidata grounding pipeline to extract algorithms, paradigms, patterns, and domains from source files into an open-taxonomy knowledge graph. Applied to 167 million Stack-Edu files, it produces about 158 million nodes and one billion typed edges across 14 programming languages.
