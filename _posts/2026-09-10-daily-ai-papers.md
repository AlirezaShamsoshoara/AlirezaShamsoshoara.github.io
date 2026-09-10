---
title: "Daily AI Papers — September 10, 2026"
date: 2026-09-10
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-10/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robot-learning
  - multimodal-ai
---

### 1. WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data
**Authors:** Ji Soo Lee, Xilun Chen, Pierce Chuang, Ashish Shenoy, Jason Wei, Dohwan Ko, Hyunwoo J. Kim, Benoit Corda
**arXiv:** [arxiv.org/abs/2609.05405](https://arxiv.org/abs/2609.05405)
**Summary:** Recent advances in wearable sensing enable continuous monitoring of physiological and behavioral signals, yet existing benchmarks rarely evaluate whether AI systems can reason over a real user's longitudinal wearable record. We introduce WearableQA, a benchmark comprising 4,084 10-option multiple-choice questions constructed from the wearable time series, blood biomarkers, and demographics of 200 real users, each with up to 500 days of daily measurements.
**Trending because:** 28 HuggingFace upvotes + tests health reasoning over longitudinal, real-world wearable records

---

### 2. What Did I Just Say? Self-Listening for Full-Duplex Speech Models
**Authors:** Xuanning Zhou, Junyi Ao, Xiaotong Liu, Tom Ko, Benyou Wang, Haizhou Li
**arXiv:** [arxiv.org/abs/2609.05592](https://arxiv.org/abs/2609.05592)
**Summary:** Full-duplex spoken language models can listen and speak simultaneously, enabling them to handle interruptions and backchannels in human conversation. However, text generation, speech synthesis, and audio playback proceed asynchronously.
**Trending because:** 19 HuggingFace upvotes + addresses asynchronous self-hearing in full-duplex speech models

---

### 3. Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy
**Authors:** Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos
**arXiv:** [arxiv.org/abs/2609.07470](https://arxiv.org/abs/2609.07470)
**Summary:** Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages. We study the addition of Greek to an open vision-language-action stack using only machine-rephrased instructions and no architecture changes.
**Trending because:** 19 HuggingFace upvotes + measures multilingual transfer by adding Greek to an English-trained robot policy

---

### 4. SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents
**Authors:** Pujun Zheng, Zixin Shang, Shufan Jiang, Wenhui Tian, Dongsheng Zhu, Zerun Ma, Dingbo Yuan, Qi Zhang
**arXiv:** [arxiv.org/abs/2609.08149](https://arxiv.org/abs/2609.08149)
**Summary:** SWE-Bench Pro has emerged as a standard benchmark for evaluating software engineering agents on challenging repository-level tasks. However, our analysis work show that its evaluation is undermined by two sources of unreliability: reward hacking, enabled by leakage of gold solutions or hidden evaluation information, and task quality issues, including misleading problem statements and improperly scoped tests.
**Trending because:** 18 HuggingFace upvotes + targets reliability problems in a standard benchmark for software-engineering agents

---

### 5. SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?
**Authors:** Yuqiao Tan, Shizhu He, Jun Zhao, Kang Liu
**arXiv:** [arxiv.org/abs/2609.09113](https://arxiv.org/abs/2609.09113)
**Summary:** While research on recursive self-improvement (RSI) has predominantly automated model training pipelines, reliable autonomous development demands a missing pillar: post-hoc monitoring and auditing to understand what models learn and ensure safe alignment. Mechanistic interpretability tools are essential to bridge this gap, among which Sparse Autoencoders (SAEs) serve as a cornerstone by isolating interpretable features for model inspection and steering.
**Trending because:** 16 HuggingFace upvotes + tests whether agents can autonomously conduct sparse-autoencoder interpretability research

---

### 6. Cadence: Error-Bounded Lossy Compression of Demand Time Series with a Time-Series Foundation Model
**Authors:** Roberto Tacconelli
**arXiv:** [arxiv.org/abs/2609.06008](https://arxiv.org/abs/2609.06008)
**Summary:** We present Cadence, an error-bounded lossy compressor for numeric time series pairing a 330M-parameter time-series foundation model (Google TimesFM-3) with an adaptive arithmetic coder, guaranteeing |x_t-x_t|≤τ on every sample. One negative result constrains the design space: for lossless coding a foundation model is worth nothing, because bits saved are logarithmic in predictor accuracy, Δb=log_2(MAE_{old}/MAE_{new}).
**Trending because:** 16 HuggingFace upvotes + guarantees bounded error while compressing demand time series with a foundation model

---

### 7. SynthGait-19K: A Physically Grounded Synthetic Video Dataset for Gait Parameter Estimation
**Authors:** Soroush Mehraban, Xin Lei Lin, Vida Adeli, Majid Mirmehdi, Amirhossein Dadashzadeh, Clint Hansen, Andrea Iaboni, Babak Taati
**arXiv:** [arxiv.org/abs/2609.08108](https://arxiv.org/abs/2609.08108)
**Summary:** Accurate estimation of clinically meaningful gait parameters from monocular video is important for scalable mobility assessment, yet progress is limited by the small scale, restricted viewpoints, and limited visual diversity of existing datasets. We introduce SynthGait-19k, a physically grounded synthetic video dataset containing 19,272 walking videos derived from 6,427 MoCap sequences across 437 subjects, with paired SMPL motion and annotations for six gait parameters.
**Trending because:** 16 HuggingFace upvotes + expands clinically grounded gait estimation with a large synthetic video dataset

---

### 8. Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents
**Authors:** Jingjie Ning, Shanshan Zhong, Xiaochuan Li, Ji Zeng
**arXiv:** [arxiv.org/abs/2609.09219](https://arxiv.org/abs/2609.09219)
**Summary:** AI research agents combine prior knowledge, public sources, and experimental feedback to produce useful results. The Discovery Certification Protocol (DCP) turns claims about these results into executable recovery and feedback tests.
**Trending because:** 15 HuggingFace upvotes + turns AI discovery claims into executable recovery and feedback audits

---

### 9. Encoded Early, Used Late: Where Transformers Begin to Act on an Inferred Partner's Expertise
**Authors:** Mika Okamoto, Gabriele Sarti
**arXiv:** [arxiv.org/abs/2609.07139](https://arxiv.org/abs/2609.07139)
**Summary:** A transformer can make an attribute linearly decodable in its residual stream at a depth where that attribute does not yet influence the output. This gap between where information is readable and where it is used has been shown for attributes stated directly in the input.
**Trending because:** 15 HuggingFace upvotes + pinpoints when transformers use an inferred partner's expertise rather than merely encode it

---

### 10. Harnessing CLIP and DINO: An Uncertainty-Aware Cascaded Fusion Network for Generalizable Deepfake Image Detection
**Authors:** Xuechao Zou, Yi Zhou, Kai Li, Shun Zhang, Yuhui Chen, Congyan Lang, Junliang Xing
**arXiv:** [arxiv.org/abs/2609.07670](https://arxiv.org/abs/2609.07670)
**Summary:** The growing realism and accessibility of manipulated and generated faces threaten the trustworthiness of digital media. To detect such forgeries, deepfake detectors based on vision foundation models have shown promising performance, but they typically rely on a single pretrained representation and are prone to overfitting to particular training distributions.
**Trending because:** 15 HuggingFace upvotes + combines CLIP, DINO, and uncertainty-aware fusion for generalizable deepfake detection

---

### 11. Puppeteer: Object-Grounded Posture-Aware Co-Speech Gesture Generation
**Authors:** Vida Adeli, Soroush Mehraban, Jacob Rommann, Harrison Sanborn, Cole Clifford, Babak Taati
**arXiv:** [arxiv.org/abs/2609.00369](https://arxiv.org/abs/2609.00369)
**Summary:** Generating co-speech gestures that are temporally coherent, semantically aligned with speech, and grounded with surrounding objects remains challenging. Prior speech-driven gesture models emphasize audio-gesture alignment but do not explicitly account for posture constraints or surrounding objects, failing to capture the inherent correlation between body gestures and the physical space.
**Trending because:** 15 HuggingFace upvotes + grounds co-speech gesture generation in surrounding objects and body posture

---

### 12. SQS: Bayesian DNN Compression through Sparse Quantized Sub-distributions
**Authors:** Ziyi Wang, Nan Jiang, Guang Lin, Qifan Song
**arXiv:** [arxiv.org/abs/2510.08999](https://arxiv.org/abs/2510.08999)
**Summary:** Compressing large-scale neural networks is essential for deploying models on resource-constrained devices. Most existing methods adopt weight pruning or low-bit quantization individually, often resulting in suboptimal compression rates to preserve acceptable performance drops.
**Trending because:** 15 HuggingFace upvotes + combines sparse Bayesian sub-distributions with quantization for efficient DNN compression

---

### 13. StudyBench: Can Self-Evolution Squeeze Textbooks for Olympiad Capability?
**Authors:** Yinghao Chen, Zixi Chen, Bingxiang He, Ziqing Qiao, Huan-ang Gao, Yinuo Xu, Yuxin Zuo, Zeyuan Liu, Yuhao Zhan, Chaojun Xiao
**arXiv:** [arxiv.org/abs/2609.00787](https://arxiv.org/abs/2609.00787)
**Summary:** Humans need to study only a handful of well-written textbooks to master a discipline and attempt its hardest problems. We argue that an ideal self-evolution method should share the same property, that is autonomously learning from raw training material for transferable problem-solving capability.
**Trending because:** 14 HuggingFace upvotes + tests whether self-evolving models can learn olympiad capability from a few textbooks

---

### 14. A*-Thought-V2: Efficient Latent Reasoning via Geometric Dynamics of LLM
**Authors:** Xiaoang Xu, Siyuan Liu, Shuo Wang, Junlan Feng, Fanyu Meng, Zhu Zhang, Jixun Wang, Xiaorong Wang, Zihan Zhou, Xin Li, Chaojun Xiao, Yiming Zhang, Huijia Wu, Liuyu Xiang, Peipei Li, Zhaofeng He
**arXiv:** [arxiv.org/abs/2609.07821](https://arxiv.org/abs/2609.07821)
**Summary:** Chain-of-Thought (CoT) improves the reasoning ability of Large Language Models (LLMs) but incurs substantial computation and context costs. Existing methods either lose intermediate information through hard pruning or lack a principled criterion for continuous compression.
**Trending because:** 11 HuggingFace upvotes + reduces chain-of-thought cost through geometric latent reasoning dynamics

---

### 15. SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators
**Authors:** Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang, Junyi Cao, Haoyu Zhen, Yilun Du, Chuang Gan
**arXiv:** [arxiv.org/abs/2609.09155](https://arxiv.org/abs/2609.09155)
**Summary:** World models are increasingly used as policy-in-the-loop imagination environments, where reliable rollouts require fine-grained controllability with respect to low-level robot actions. A key obstacle to scaling such models in robotics is that actions are not a universal language in pixel space: changes in visual environment, camera view, robot placement, or embodiment alter how the same numerical action manifests visually, leading to conflicting supervision under mixed training and brittle generalization at deployment.
**Trending because:** 11 HuggingFace upvotes + uses visual calibration to turn world models into zero-shot robot simulators

---

### 16. DianShi-RxnDB: A Large-Scale, Fine-Grained Organic Reaction Data Platform Built via a Fully Automated Pipeline for Researchers and AI Agents
**Authors:** Yubin Wang, Xingjian Wei, Jiang Wu, Yinfan Wang, Boyu Zhu, Lin Zhang, Jianing Yu, Huazheng Zeng, Ruiyi Ding, Junyuan Gao, Jiaxing Sun, Lingli Ge, Haote Yang, Jingchao Wang, Aijia Guo, Qian Jiang, Yurui Zhao, Wenjian Zhang, Chen Zhu, Lijun Wu, Xiaolei Yang, Haodong Chen, Junjie Yuan, Zichao Ye, Shaowei Hou, Jing Ye, Jia Yu, Shan Wang, Lijun Wu, Jiantao Qiu, Chao Xu, Yuqiang Li, Guangyu Wang, Bowen Zhou, Dahua Lin, Conghui He
**arXiv:** [arxiv.org/abs/2609.06703](https://arxiv.org/abs/2609.06703)
**Summary:** High-quality structured organic reaction data are essential for developing artificial intelligence for chemistry (AI4Chem), yet much of this knowledge remains dispersed across patent text, images, and reaction schemes. We present DianShi-RxnDB, a large-scale, fine-grained organic reaction data platform built via a fully automated extraction and normalization pipeline integrating patent text, images, and reaction schemes.
**Trending because:** 9 HuggingFace upvotes + builds a large structured reaction database for AI chemistry through an automated pipeline

---

### 17. Revisiting Complete Reasoning Traces for Post-Training
**Authors:** Jaehui Hwang, Sangdoo Yun, Byeongho Heo, Dongyoon Han
**arXiv:** [arxiv.org/abs/2609.07103](https://arxiv.org/abs/2609.07103)
**Summary:** Large language models (LLMs) are often post-trained on pre-collected reasoning trajectories to improve their reasoning capability. Such trajectories tend to be long due to complex, interwoven paths, which often include detours on the path toward the answer.
**Trending because:** 8 HuggingFace upvotes + re-examines whether complete reasoning trajectories are best for post-training

---

### 18. RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting
**Authors:** Hejun Wang, Jinxi Li, Junwei Jiang, Shiwei Mao, Hu Cheng, Shouwang Huang, Bo Yang
**arXiv:** [arxiv.org/abs/2609.07414](https://arxiv.org/abs/2609.07414)
**Summary:** Image relighting is traditionally tackled via complex inverse rendering pipelines, which suffer from ill-posed optimization, or single-image generative models that ignore crucial multi-view cues necessary for understanding 3D geometry and material interactions. To address these limitations, we introduce a feed-forward generative Transformer for direct single- and multi-view image relighting that entirely bypasses explicit intrinsic property estimation.
**Trending because:** 8 HuggingFace upvotes + uses multiview cues in a feed-forward transformer for object relighting

---

### 19. Φ-Bench: Can Large Language Models Engineer the Infrastructure That Powers Them?
**Authors:** Leilei Ding, Shumin Wang, Yuting Huang, Fanqi Wan, Yinmin Zhang, Qi Han, Yiming Xu, Feiyuan Zhang, Xiaomeng Chu, Guoliang You, Wuyang Zhang, Daxin Jiang, Yanyong Zhang
**arXiv:** [arxiv.org/abs/2609.10226](https://arxiv.org/abs/2609.10226)
**Summary:** Large language models (LLMs) have demonstrated remarkable capabilities in reasoning and code generation, raising the prospect that they could assist in developing and optimizing the very infrastructure that powers them. However, existing benchmarks mainly focus on isolated kernels, predefined operators, or pre-specified optimization targets, and therefore fail to evaluate the ability of LLMs to perform open-ended, long-horizon LLM infrastructure engineering.
**Trending because:** 7 HuggingFace upvotes + tests whether LLMs can engineer and optimize the infrastructure that powers them

---

### 20. AgenticGen: Reward-Guided Agentic Video Generation for Advertising
**Authors:** Xingyuan Bu, Chengru Song, Hao Zhou, Tao Zhou, Dong Li, Wei Li, Shilong Li, Hao Shi, Yongxin Guo, Donghao Zhou, Qiangpeng Yang, Shilei Wen
**arXiv:** [arxiv.org/abs/2609.09187](https://arxiv.org/abs/2609.09187)
**Summary:** Advertising video generation is not only a video synthesis task, but also a product-conditioned reasoning problem whose success is measured by online business metrics. Recent video foundation models can generate realistic clips from multimodal conditions, yet they do not optimize how a product should be transformed into an effective advertisement or how future generation should be improved from online business feedback.
**Trending because:** 7 HuggingFace upvotes + connects reward-guided advertising video generation to measurable business outcomes
