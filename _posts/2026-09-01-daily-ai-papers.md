---
title: "Daily AI Papers — September 1, 2026"
date: 2026-09-01
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-01/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - reasoning-models
  - video-generation
  - agentic-research
---

### 1. Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement
**Authors:** Yi Ding, Ruqi Zhang
**arXiv:** [arxiv.org/abs/2608.31046](https://arxiv.org/abs/2608.31046)
**Summary:** On-policy distillation (OPD) offers dense token-level supervision as an alternative to the sparse outcome-level advantages of reinforcement learning with verifiable rewards (RLVR). However, the teacher scores student-generated trajectories that are inherently off-policy for it, so the reliability of its supervision, and hence the source of the student's improvement, remains unclear.
**Trending because:** 87 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 2. DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution
**Authors:** Jiashu Zhu, Yanhao Zheng, Ruitian Tian, Rujing Dang, Shen Zhang, Bingze Song, Jiachen Lei, Ruimin Lin, Jiahong Wu, Xiangxiang Chu
**arXiv:** [arxiv.org/abs/2608.31106](https://arxiv.org/abs/2608.31106)
**Summary:** Recent video generators often omit audio or synthesize it in a separate stage, limiting reciprocal modeling of visual dynamics and acoustic events. We present DreamX-Creator 1.0, a compact native joint audio-video generation system centered on a 7B generator.
**Trending because:** 85 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 3. Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling
**Authors:** Minghan Qin, Yuang Wang, Xiuyu Yang, Yushi Long, Yujian Zhang, Ruihuan Wang, Kai Ye, Yangang Zhang, Hang Li
**arXiv:** [arxiv.org/abs/2608.30821](https://arxiv.org/abs/2608.30821)
**Summary:** Composable scene modeling aims to recover a real indoor scene as complete, editable object assets arranged as observed, giving robot simulation and embodied AI a simulation-ready replica of the real environment whose objects can be manipulated individually. Existing pipelines decompose the task into three steps---parse the observations into instances, generate an asset for each, and place each asset back---but every step presumes an input that a cluttered capture rarely provides: accurate instance geometry, unoccluded views, and assets that accurately match the observations.
**Trending because:** 61 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 4. GenFirst: Generation Before Reconstruction for Stable End-to-End Latent Generative Modeling
**Authors:** Guangting Zheng, Yiyuan Zhang, Tao Yang, Yunpeng Chen, Rui Zhu, Jiajun Deng, Yanyong Zhang
**arXiv:** [arxiv.org/abs/2608.29335](https://arxiv.org/abs/2608.29335)
**Summary:** Latent generative models typically follow a two-stage pipeline, training a variational autoencoder for reconstruction and then a generative model on the frozen latent space. Since reconstruction-optimized latents are not necessarily generation-friendly, jointly training both models is an appealing alternative.
**Trending because:** 56 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 5. Normalized Low-Rank Adaptation
**Authors:** Jiale Kang, Ziyin Yue, Zheng Zhan, Yangyi Huang, Weiyang Liu
**arXiv:** [arxiv.org/abs/2608.31036](https://arxiv.org/abs/2608.31036)
**Summary:** While low-rank adaptation (LoRA) is widely used for parameter-efficient model adaptation, how to regularize its training dynamics for stable and effective optimization remains underexplored. Because LoRA initializes the up-projection to zero, its early optimization dynamics are largely governed by the down-projection.
**Trending because:** 35 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 6. PaperGym: Rubric-Centered Evolution for Research-Plan Generation
**Authors:** Yuhan Wang, Zhengxi Lu, Yuchen Yan, Kaitao Song, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
**arXiv:** [arxiv.org/abs/2608.31119](https://arxiv.org/abs/2608.31119)
**Summary:** Research planning is the decisive capability of AI scientists. Yet a research plan admits no verifiable answer, so reinforcement learning lacks the environment it requires: tasks paired with a critic.
**Trending because:** 34 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 7. On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability
**Authors:** Zihan Qiu, Zekun Wang, Xiao Li, Yanpeng Li, Yang Xu, Yixuan Wang, Huaqing Zhang, Rui Men, Bochao Mao, Chengruidong Zhang, Fan Zhou, Hao Luo, Haofeng Huang, Haoran Lian, Haoyan Huang, Hongqing Chen, Jianwei Zhang, Jing Xu, Junjie Wang, Langshi Chen, Liangyu Wang, Linlang Jiang, Man Yuan, Minmin Sun, Peng Jin, Siqi Zhang, Siyu Wang, Xingzhang Ren, Yakai Wang, Yi Zhang, Yiming Dong, Yizhong Cao, Yubo Ma, Yunfei Mao, Bo Zheng, Dayiheng Liu
**arXiv:** [arxiv.org/abs/2608.30320](https://arxiv.org/abs/2608.30320)
**Summary:** We describe the architecture and ablations of Qwen3.8-Flash-Next, a sparse mixture-of-experts model with 125B parameters, 6B activated per token, and additional 51B parameters of n-gram embedding tables held off the accelerator. On fourteen pre-training benchmarks the model leads the 397B-A17B predecessor on eight and trails it on the rest by at most 2.6 points, at 1/3 the activated parameters, 1/3 the training tokens, and roughly 1/9 the training FLOPs.
**Trending because:** 30 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 8. CogEvol: Towards Efficient and Reliable Learning Environment Generation
**Authors:** Shangqing Tu, Daniel Zhang-Li, Yucheng Wang, Shiyu Gan, Yanpeng Wang, Huiqiang Rong, Mofei Chen, Shen Yang, Yini Chen, Yinuo Duan, Haoxuan Li, Binglin Liu, Ye He, Danqi Zheng, Zhanxin Hao, Yuxuan Wu, Mengting Tao, Yuqiu Liu, Jifan Yu, Juanzi Li, Bin Xu, Lei Hou, Huiqin Liu, Yu Zhang
**arXiv:** [arxiv.org/abs/2608.30968](https://arxiv.org/abs/2608.30968)
**Summary:** We present CogEvol, a family of models trained specifically for Learning Environment Generation: turning a course brief into a finished learning artifact (structured-JSON slides or self-contained interactive HTML pages) in a single pass. Across 220k production requests, CogEvol completes a slide in a median of 17 seconds and an interactive page in 59, replacing minutes-long multi-turn agent scaffolding.
**Trending because:** 25 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 9. LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation
**Authors:** Shaoan Wang, Aocheng Luo, Fei Huang, Jingyi Xu, Xiaoyang Wang, Yueyu Wang, Qianli Ma, Fan Yang, Ran Mei, Jia Wei, Jiangpeng Hu, Xuhao Liu, Hongming Chen, Yuanbin Shao, Yiyang Lin, Ziliang Li, Liang Pan, Xinhang Liu, Yuntao Ma, Tingxiang Fan
**arXiv:** [arxiv.org/abs/2608.30935](https://arxiv.org/abs/2608.30935)
**Summary:** Embodied navigation requires agents to translate heterogeneous goals and visual observations into actions across tasks, environments, and robot embodiments. Modern vision-language models (VLMs) already encode spatial priors for visual grounding, spatial reasoning, and pointing, but these capabilities are rarely elicited directly for robot control.
**Trending because:** 24 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 10. SHAPE of Chain-of-Thought in Math Reasoning
**Authors:** Jonghyun Song, Sangjun Song, Minjae Oh, Haesung Pyun, Sungsik Lee, Yohan Jo
**arXiv:** [arxiv.org/abs/2608.28600](https://arxiv.org/abs/2608.28600)
**Summary:** Large language models (LLMs) achieve strong performance on mathematical reasoning benchmarks, yet the mathematically meaningful skills underlying their reasoning remain underexplored. We introduce SHAPE, a framework that analyzes Chain-of-Thought (CoT) trajectories through two lenses developed in mathematics education: (1) semantic spaces: the model's evolving mathematical interpretations of a problem (e.g., algebraic, geometric), and (2) heuristics: the specific mathematical actions taken within those spaces (e.g., simplifying the problem, working backward).
**Trending because:** 24 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 11. Super Library Agent: Joint Generation and Maintenance of Multiple Applications Beyond the Single Codebase
**Authors:** Daegyu Sung, Yukyeong Lee, Geon Park, Yumin Choi, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2608.29310](https://arxiv.org/abs/2608.29310)
**Summary:** Organizations often develop and maintain portfolios of related applications: independently deployable codebases that share substantial domain logic, interface patterns, or operational conventions. As LLM coding agents are increasingly used to generate and maintain such software, a naive application-by-application workflow duplicates shared logic across codebases and allows prolonged agentic maintenance to accumulate verbosity, dead code, and structural erosion.
**Trending because:** 22 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 12. Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence
**Authors:** Zhiqin Yang, Jingwen Fu, Yuhan Liu, Hengyu Liu, Yonggang Zhang, Kainan Cao, Zizhuo Zhang, Chenxin Li, Ruibin Yuan, Jiahao Pan, Jiankai Sun, Zhenyuan Zhang, Yibo Li, Yunlong Lin, Jing Xiong, Sida Lin, Bo Han, Wei Xue, Yike Guo
**arXiv:** [arxiv.org/abs/2608.31075](https://arxiv.org/abs/2608.31075)
**Summary:** Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can be checked automatically. Extending this progress to open-ended and agentic tasks remains difficult because reliable rewards are harder to obtain and direct human supervision cannot keep pace with the scale and complexity of model-generated experience.
**Trending because:** 21 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 13. Evaluating the Hidden Costs of Personalization in Large Language Models
**Authors:** Yumeng Wang, Yuchen Wu, Cheng Qian, Zhiyuan Fan, Hyeonjeong Ha, Shujin Wu, Jiayu Liu, Heng Ji, Ge Wang
**arXiv:** [arxiv.org/abs/2608.28833](https://arxiv.org/abs/2608.28833)
**Summary:** While Large language models (LLMs) incorporate user personalization signals to improve usability and helpfulness, they increasingly shift from providing balanced, informative responses toward optimizing for user satisfaction when conditioned on personal context such as conversation history, inferred preferences, and user profiles. Specifically, we identify three emerging risks: (1) irrelevant personalization, where models reference personal information in unnecessary contexts; (2) preference narrowing, where models reinforce informational echo chambers; and (3) sycophantic bias, where models agree excessively with user opinions.
**Trending because:** 18 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 14. Lies We Can See: Joint Verbal and Non-Verbal Deception by VLM Agents in Embodied Social Interactions
**Authors:** Jaewoo Ahn, Junseo Kim, Hyunseo Kim, Heeseung Yun, Jaehyeon Son, Zsolt Kira, Gunhee Kim
**arXiv:** [arxiv.org/abs/2608.30428](https://arxiv.org/abs/2608.30428)
**Summary:** Strategic deception by LLM and VLM agents has emerged as a central AI alignment and safety concern. Social-deduction games (where each player holds a hidden role and communicates with others to deduce identities) serve as the canonical testbed, particularly in multi-agent settings.
**Trending because:** 11 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 15. Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents
**Authors:** Xuehai Wang, Haowei Qin, Tongxin Liu, Junkai Li, Buqiang Xu, Jintian Zhang, Yijun Chen, Zirui Xue, Shumin Deng
**arXiv:** [arxiv.org/abs/2608.31076](https://arxiv.org/abs/2608.31076)
**Summary:** Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-ended research tasks often do not clearly specify the analyses, methods, and success criteria required to complete the task.
**Trending because:** 10 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 16. Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation
**Authors:** Yeonkyeong Lee, Hyunsung Go, Jongmin Kim, Sewoong Lim, Donghoon Lee
**arXiv:** [arxiv.org/abs/2608.24293](https://arxiv.org/abs/2608.24293)
**Summary:** Latent diffusion models have emerged as a dominant framework for high-fidelity image and video synthesis, operating in compact latent spaces with variational autoencoders (VAEs) to enhance computational efficiency without compromising visual quality. However, conventional VAEs are suboptimal for video data as they employ fixed compression ratios that cannot adapt to the varying complexity of spatio-temporal content.
**Trending because:** 9 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 17. Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory
**Authors:** Runjia Qian, Zile Wang, Jihai Zhang, Kai Zou, Wei Yu, Jiaxing Li, Zexiang Liu, Yaokun Li, Fei Kang, Kaichen Huang, Mengyin An, Haobo Zhang, Biao Jiang, Jiahua Wang, Haofeng Sun, Yang Liu, Yangguang Li
**arXiv:** [arxiv.org/abs/2608.29910](https://arxiv.org/abs/2608.29910)
**Summary:** Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR. Achieving stable long-horizon interactive generation, however, remains challenging, as the model must simultaneously preserve scene geometry, dynamic consistency, and camera control while supporting real-time autoregressive generation.
**Trending because:** 8 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 18. Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered
**Authors:** Aryo Pradipta Gema, Neel Rajani, Rohit Saxena, Wai-Chung Kwan, Pasquale Minervini
**arXiv:** [arxiv.org/abs/2608.29464](https://arxiv.org/abs/2608.29464)
**Summary:** Chain-of-thought (CoT) monitoring assumes that reasoning traces faithfully record the information that shapes a model's answer. Existing faithfulness tests often place explicit bias cues in the user message, while agents may encounter preferences through tool returns or raw artifacts.
**Trending because:** 8 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 19. MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents
**Authors:** Vernon Toh, Navonil Majumder, Zhengyuan Liu, Nancy F. Chen, Soujanya Poria
**arXiv:** [arxiv.org/abs/2608.31022](https://arxiv.org/abs/2608.31022)
**Summary:** AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities.
**Trending because:** 7 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---

### 20. PaperBanana-Interact: Scientific Diagram Refinement with Multi-Turn Human Feedback
**Authors:** Xueqing Wu, Ashwin Balasubramanian, Bingxuan Li, Dawei Zhu, Kai-Wei Chang, Yale Song, Yiwen Song, Rui Meng, Tomas Pfister, Nanyun Peng
**arXiv:** [arxiv.org/abs/2608.30241](https://arxiv.org/abs/2608.30241)
**Summary:** Recent efforts have aimed to automate scientific diagram generation from paper content (Lin et al., 2026; Zhu et al., 2026a). However, fully satisfying an author's visual and communicative preferences in a single turn is challenging: in our formative user study (N = 14), all participants requested further revisions after viewing an initial draft, and 86% of them rated the refined diagrams as more satisfactory.
**Trending because:** 6 HuggingFace upvotes + high-engagement paper on the HuggingFace daily/trending feed

---
