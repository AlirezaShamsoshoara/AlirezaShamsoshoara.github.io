---
title: "Daily AI Papers — October 23, 2026"
date: 2026-10-23
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-23/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal-ai
  - ai-agents
  - world-models
---

### 1. WeVisOne-VL: Unified Visual Perception from Objects to Pixels
**Authors:** Tianming Liang, Junyi Pan, Yuxi Li, Canmiao Fu, Zhipeng Huang, Chong Sun, Chen Li, Jing Lyu
**arXiv:** [arxiv.org/abs/2610.31329](https://arxiv.org/abs/2610.31329)
**Summary:** WeVisOne-VL unifies object-level and pixel-level perception through structured token prediction and a lightweight pixel decoder, supporting detection, localization, counting, OCR, segmentation, and matting. Three-stage supervised training followed by mixed-task reinforcement learning produces leading reported results across more than 30 benchmarks while preserving rejection of queries about absent objects.

---

### 2. Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation
**Authors:** Songlin Yang, Zhe Wang, Xiaotong Zhao, Xi Wang, Ran Zhang, Shuai Li, Taiyi Wu, Songlian Li, Eric Liu, Alan Zhao, Anyi Rao
**arXiv:** [arxiv.org/abs/2610.30926](https://arxiv.org/abs/2610.30926)
**Summary:** Factor-Aware Predictive Learning grounds a video diffusion transformer in MLLM latents, then trains factor-specific edits and temporal inference from limited inputs through complementary objectives. Experiments report consistent improvements over baselines in sparse-to-video generation, factor-aware editing, and multi-shot generation, with better temporal control and coordination of character, scene, action, and camera.

---

### 3. Deep Search in Real-World Web Environments
**Authors:** Xiaomin Yu, Hongliang Chen, Zhe Huang, Shilin Yan, Shao-Rong Su, Xuqiao Ma, Feiyang Wang, Jiayu Chen, Jiwei Fang, Yu Yan, Yini Huang, Chen Chen, Ruoxi Cheng, Yuzhi He, Yuhui Zhang, Xiaoxing Hu, Chen Liu, Jianbo Lin, Yijiang Li, Xiaobin Hu, Menglong Li, Zhuoran Lu, Weishi Wang, Zhongqi Yue, Chengwei Qin
**arXiv:** [arxiv.org/abs/2610.30181](https://arxiv.org/abs/2610.30181)
**Summary:** OpenDS-World benchmarks live-web deep search with 200 human-verified tasks requiring agents to combine search, browser interaction, and evidence processing across heterogeneous sources and formats. Across 12 frontier models, the strongest achieves 39.0% accuracy, while analysis exposes persistent challenges in tool coordination, failure recovery, and long-horizon research management.

---

### 4. Editing Images into Reusable Layers via Compositional Edit-Prior Distillation
**Authors:** Wen Xue, Yong Liu, Xueheng Li, Si Wu, Yong Xu, Yipeng Sun, Yan Li, Simiu Gu
**arXiv:** [arxiv.org/abs/2610.24738](https://arxiv.org/abs/2610.24738)
**Summary:** LayerEditor couples instruction-guided image editing with reusable RGBA-layer generation through joint RGB-alpha token modeling and compositional distillation of a pretrained editing prior. The work introduces LayerEditor-100K and dedicated layered-editing benchmarks, reporting strong editing fidelity and accurate layers that support local manipulation and multi-layer decomposition.

---

### 5. IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems
**Authors:** A. Jian Yang, An Huang, Bo Dan, Chen Mu, Chengran Yang, Chuan Shi, Feng Chang, Hongxin Li, Hongyuan Tao, Jinxing Zhang, Jujie He, Kun Wang, Lin Jing, Ming Yang, Qicheng Hu, Renyuan Li, Shark Liu, Shawn Guo, Shi Qing, Shi Zhong, Tianyu Zheng, Wei Liu, Wei Zhang, Wenrui Cai, Wenxiao Chen, Xuxing Chen, Yan Xing, Yi Xing, Yifan Luo, Yiran Xing, Yizhi Li, Yongsheng Kang, Yucheng Ding, Yue Song, Yun Qing, Yunqi Liu, Zelong Huang, Zhengmao Ye, Zhentao Fan, Zhiteng Li, Ziling Huang, Bihong Tang, Bingli Wang, Ce Jun, Changhao Chen, Chen Hu, Chen Xiao, Chi Liu, Chunjiang Ge, Danyang Li, Deyang Kong, Dian Qi, Ding Tan, Evan Yang, Fanglin Xu, Fei Bai, Gang Liu, Guochang Li, Hao Tang, Haoran Feng, Haowen Wang, Huahao Hu, Huanjin Yao, Huatong Song, Jia Deng, Jiajun Wu, Jialiang Cheng, Jiayi Liang, Jiayi Wu, Jie Deng, Jiejun Tan, Jing Yang, Jingda Xu, Junhang Cheng, Junxiao Liu, Kai Lv, Kaixiang Pan, Kecheng Lu, Kun Zeng, Kun Zheng, Kunbo Ding, Liang Qiu, Lingyi Sun, Luan Zhang, Mengxiao Lv, Ning Dong, Pei Wang, Peng Zhang, Qingsong Cai, Qixiang Yin, Qiyao Wang, Renbiao Liu, Renfei Dang, Ruihang Li, Ruirui Huang, Shanhui Yin, Shen Jian, Shengjie Fang, Shikai Li, Shinan Zhang, Shiqi Chen, Shuai Liu, Shuangqi Li, Shuo Tang, Shuqing Deng, Sijin Hao, Siwei Wu, Siyue Wang, Tao Hai, Tao Ren, TingYang Chen, Wei Shao, Weicheng Gu, Weihan Peng, Wenlong Miao, Xavier Yu, Xiangyuan Ji, Xiaocheng Li, Xiaodong Huang, Xiaohan Ge, Xiaoxiang Shi, Xiaoyang Zhang, Xiaoyu Yang, Xidong Wang, Xin Li, Xinyu Tang, Xiyuan Yang, Xudong Ma, Ya Tong, Yachao Wang, Yang Tian, Yaxin Du, Yeli Ruan, Yi Wang, Yi Yu, Yibin Feng, Yibo Tan, Yihang Wang, Yiming Ju, Yinda Chen, Yinda Chen, Yingjie Du, Yiwei Liu, Yizhi Zhou, Yuan Wei, Yuli Chen, Yuqi Zhu, Yuwen Li, Yuxi Dong, Yuxuan Zhang, Yuyang Song, Zhange Zhang, Zhaohan Zhang, Zhaoyi Li, Zhen Zhang, Zhengbo Zhang, Zhihang Hu, Zhiwei Yu, Zhixin Xie, Zhiyu Chen, Zhizhao Luo, Zhongyuan Wu, Zhou Fang, Zhu Lin, Zhuocheng Gong, Zixi Zhao, Ziyang Zeng, Ziyi Wang, Ziyu Zhao, Ran Tao, Mingjie Tang, Chuan Hao, Peihao Wu, Jianzhou Wang, Nan Jiang, Yuan Zhi, Bryan Dai
**arXiv:** [arxiv.org/abs/2610.30949](https://arxiv.org/abs/2610.30949)
**Summary:** IQuest-Q1 is an open sparse mixture-of-experts foundation model with 320B total parameters and 15B activated parameters, designed for agentic CLI systems. Its development combines stable pretraining, context-extending mid-training, multi-scaffold supervised and reinforcement-learning post-training, and model merging to strengthen coding and general capabilities.

---

### 6. Toward Recursive Self-Improvement in Physical AI
**Authors:** Meng Luo, Zechen Bai, Shanqing Xu, Yanlin Li, Kaixin Li, Mengchen Qian, Weifeng Lu, Ran Zhang, Yingtian Zou, Ziyang Luo, Wei Chen, Hongzhan Lin
**arXiv:** [arxiv.org/abs/2610.29677](https://arxiv.org/abs/2610.29677)
**Summary:** This position paper traces paths toward recursive self-improvement in robot learning, examining how physical experience can improve capabilities and the procedures that produce them. The reviewed physical studies demonstrate behavioral and procedure improvements but have not isolated gains attributable to recursion, motivating evaluation principles centered on transferable feedback, safety, and affordable trials.

---

### 7. Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks
**Authors:** Ivan Listopadov, Maksim Nakhodnov, Aibek Alanov
**arXiv:** [arxiv.org/abs/2610.28889](https://arxiv.org/abs/2610.28889)
**Summary:** Policy-Mask learns a budget-conditioned policy that jointly selects diffusion timesteps, network blocks, and channel subsets, using cardinality normalization to stabilize the three selection heads. At matched budgets it improves segmentation, classification, and semantic correspondence over fixed extraction and feature-filter baselines, and the framework also adapts to diffusion-transformer hidden dimensions.

---

### 8. Deep Fusion Memory: A Chunk-Level Parametric Memory for Large Language Models
**Authors:** Rubin Wei, Siyuan Sun, Hao Sun, Yuliang Liu, Xiang Shi, Jiarui Wang, Junming Zhang, Zhouhan Lin
**arXiv:** [arxiv.org/abs/2610.25100](https://arxiv.org/abs/2610.25100)
**Summary:** Deep Fusion Memory predicts chunk-level parametric memory from preceding context and injects it into frozen-backbone hidden states through gated cross-attention, requiring no explicit retrieval at inference. Compared with token-level parametric-memory construction, it uses 32 times fewer retrieval queries and 2,048 times fewer retrieved items while improving reported performance across six QA tasks and domain-adaptation evaluations.

---

### 9. What Generation Knows: Unlocking Fine-Grained Understanding in Unified Multimodal Models
**Authors:** Tengju Ru, Weitong Lian, Zecong Tang, Zhiheng Liu, Lingyi Meng, Haoran Li, Kaixuan Wang, Bohao Li, Xihui Liu
**arXiv:** [arxiv.org/abs/2610.23987](https://arxiv.org/abs/2610.23987)
**Summary:** GAFU compresses native generation-side visual representations into compact tokens that the understanding pathway can retrieve for fine-grained visual reasoning. Across unified multimodal architectures and understanding tasks, it improves over same-data supervised-fine-tuning baselines, with maximum relative gains of 20.00%, 17.94%, and 8.62% on VStar-Bench, OmniSpatial, and VSR-Bench respectively.

---

### 10. LaLa-World: Scaling Latent World Models with Natural Language Actions
**Authors:** Junha Song, Geonmo Gu, Jeongeun Park, Heejeong Nam, Lucas Maes, Byeongho Heo, Dongyoon Han, Sangdoo Yun
**arXiv:** [arxiv.org/abs/2610.27851](https://arxiv.org/abs/2610.27851)
**Summary:** LaLa-World uses natural-language descriptions of numerical actions and visual changes to train one latent future predictor across simulation, robot trajectories, and broader image and video data. In a matched comparison with a video-generation baseline, it reaches comparable planning performance with six times less training cost and 13.9 times faster planning, and its policy extension offers up to 5.5 times faster inference than Cosmos Policy.

---

### 11. Meta Expert: Cross-Layer Expert Sharing for Storage- and Retrieval-Efficient MoE
**Authors:** Ermo Hua, Xiangyu Hong, Baiting Wu, Che Jiang, Haozheng Hou, Yicheng Gu, Hanjing Wang, Qirui Zeng, Ming Zhang, Ning Ding, Qipeng Guo, Youbang Sun, Biqing Qi, Bowen Zhou
**arXiv:** [arxiv.org/abs/2610.27598](https://arxiv.org/abs/2610.27598)
**Summary:** Meta Expert shares mixture-of-experts components across layers to reduce redundancy and provide more flexible residual pathways for information retrieval. With activated quantity and expert granularity held fixed, the proposed model matches vanilla MoE performance using only 70–80% of its experts and shows lower cross-entropy loss and higher downstream accuracy in empirical comparisons.

---

### 12. Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V
**Authors:** Zhenghan Chen, Zekai Shao, Xin Lin, Leting Cheng, Siming Chen
**arXiv:** [arxiv.org/abs/2610.28416](https://arxiv.org/abs/2610.28416)
**Summary:** Code2Video-Compass evaluates general-purpose code-based text-to-video, image-to-video, and video-to-video generation with 2,104 tasks across 10 categories and 24 subtypes. A dual-level framework with 12 objective and five subjective metrics evaluates 15 multimodal models, revealing persistent difficulty producing complete coherent videos as construction, animation, and state-dependency complexity increase.

---

### 13. Self-Distilling Future Video Representations for World Action Models
**Authors:** Huiwon Jang, Suhyeok Jang, Hyeonmo Kang, Seungku Kim, Jinwoo Shin, Sihyun Yu
**arXiv:** [arxiv.org/abs/2610.30320](https://arxiv.org/abs/2610.30320)
**Summary:** FRED trains world action models to predict useful future video representations from noise in a single denoising step through self-distillation and historical visual context. It improves real-world manipulation, long-horizon generalization, and human-to-robot transfer, reaching 50.0% success on tasks demonstrated only in human videos versus 19.4% for the strongest competing world action model.

---

### 14. Heartbeat Thinking: Speculative Reasoning and Tool Execution While Listening in Realtime Voice Agents
**Authors:** Zhenyu Zhang, Kewei Fu, Yongqi Tong, Chenzhi Zheng, Wei Wu, Jiang-Ming Yang, Jianshe Li
**arXiv:** [arxiv.org/abs/2610.26233](https://arxiv.org/abs/2610.26233)
**Summary:** Heartbeat Thinking lets voice-agent reasoning invocations and dispatched tools finish while periodic new invocations consume updated speech transcripts and shared completed results. Across three benchmarks it improves speculative tool coverage or retrieval reuse, and on FDBench v3 it raises coverage by 16 percentage points and cuts mean final-response latency by 36.4%, with benchmark-dependent effects on final quality.

---

### 15. RouteWeaver: Weaving Mode Selection and Execution into Unified LLM Routing
**Authors:** Xiaohan Wang, Haozhen Zhang, Qingyuan Liu, Tao Feng, Wenya Wang
**arXiv:** [arxiv.org/abs/2610.19705](https://arxiv.org/abs/2610.19705)
**Summary:** RouteWeaver learns to choose between single-round, multi-round, and agentic routing and select models within each mode using coordinated mode-execution GRPO and progressive exploration. Across five task domains it reaches 61.4% average accuracy, an 11.03% relative improvement over the strongest baseline, while ablations show routing collapses to single-round execution without progressive exploration.

---

### 16. Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports
**Authors:** Jiahao Meng, Qize Yang, Yuxuan Wang, Yunfei Chu, Wensi Dai, Jin Xu, Yunhai Tong
**arXiv:** [arxiv.org/abs/2610.31158](https://arxiv.org/abs/2610.31158)
**Summary:** OmniDR-Bench evaluates video-centered deep research through 50 Chinese and English tasks across 19 subcategories, using interactive reports and audited rubric trees containing 6,414 criteria. Across 18 agent configurations the best scores 63.3 out of 100, exposing gaps in audiovisual grounding, multimodal evidence coverage, causal analysis, and citation support.

---

### 17. RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting
**Authors:** Injae Kim, Minseok Joo, Jihwan Park, Sehyung Kim, Minseong Bae, Hyunwoo J. Kim
**arXiv:** [arxiv.org/abs/2610.27712](https://arxiv.org/abs/2610.27712)
**Summary:** RLSplat directly allocates and decodes exactly the requested number of 3D Gaussians, making representation size, inference latency, and peak memory decrease linearly with the budget. In zero-shot evaluations it outperforms prior budget-controllable methods at every budget, exceeds the strongest baseline with four times fewer Gaussians, and achieves up to 4.1 times faster inference with 9.6 times less peak memory at low budgets.

---

### 18. Is Complex Agentic Memory Always Needed? Naive RAG Is Stronger Than We Thought
**Authors:** Zhengye Bao, Shengtao Zhang, Haokai Zhang, Shiqi Lou, Muning Wen, Minnan Luo
**arXiv:** [arxiv.org/abs/2610.30755](https://arxiv.org/abs/2610.30755)
**Summary:** Raw-RAG retrieves and reranks raw conversational history for a reader LLM without the mutation and structural machinery of complex agentic-memory systems. Across four memory benchmarks it ranks first in six of seven benchmark-model settings, with evidence analysis showing that preserving raw information and dependency paths can outweigh lower evidence utilization.

---

### 19. Cola2: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic Compression and Balanced Discrete Generation
**Authors:** Hongcan Guo, Yian Zhao, Feng Wang, Shen Nie, Guoqiang Wei, Yan Zeng, Hengshuang Zhao
**arXiv:** [arxiv.org/abs/2610.31305](https://arxiv.org/abs/2610.31305)
**Summary:** Cola2 combines dynamically segmented semantic compression with a block-causal masked diffusion decoder, balancing reconstruction, generation, and continuous-discrete co-adaptation. Experiments validate competitive scaling, and an unconverged checkpoint trained on 346.03 billion source tokens reaches a 60.10 average across eight tasks and surpasses Llama-3-8B on HellaSwag and StoryCloze.

---

### 20. Rethinking Sequence Compression with Test-time Regression
**Authors:** Sihan Yang, Jie Huang, Hanxuan Li, Yifan Guo, Weigao Sun, Yiran Zhong, Weiyang Liu
**arXiv:** [arxiv.org/abs/2610.31574](https://arxiv.org/abs/2610.31574)
**Summary:** TTR-Compressor treats sequence compression as an end-to-end-learned regression problem whose fitted coefficients are computed in closed form during the forward pass. It improves RULER results when used in block-wise sparse attention and consistently beats standard MLP visual-token merging, matching the merger's performance with 55.6% fewer visual tokens.
