---
title: "Daily AI Papers — November 06, 2026"
date: 2026-11-06
permalink: /blog/ai-papers/2026/11/daily-ai-papers-11-06/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - embodied-ai
  - inference-efficiency
---

### 1. Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents
**Authors:** Lang Mo, Xingxuan Zhang, Qi Wang, Mingchao Hao, Hao Yuan, Chunjing Gan, Wang Lu, Peng Cui
**arXiv:** [arxiv.org/abs/2611.02075](https://arxiv.org/abs/2611.02075)
**Summary:** DPDM combines a language model’s semantic representations with a shared frozen conditional predictor, using deployment history to support tool judgments, candidate preferences, and reasoning assessments without updating neural parameters. With Qwen3.5-27B and a LimiX-2 predictor, the authors report mean accuracy rising from 78.80 percent to 84.92 percent across 50 benchmarks under the respective evaluated history budgets, or 82.33 percent with matched histories and queries.

---

### 2. VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding
**Authors:** Yu-Cheng Chou, Shihao Wang, Jin Huang, Chi-Pin Huang, Chiao-An Yang, Xianzhe Fan, Jing Wang, Zhiqi Li, Yuanguo Kuang, Ruijie Zheng, Johan Bjorck, Sifei Liu, Hang Su, Abhishek Badki, Lei Zhang, Alan Yuille, Linxi "Jim'' Fan, Jan Kautz, Zhiding Yu
**arXiv:** [arxiv.org/abs/2611.08449](https://arxiv.org/abs/2611.08449)
**Summary:** VFlash predicts complete visual primitives jointly with a lightweight drafter rather than generating each coordinate autoregressively, supporting boxes and variable-length robot trajectories. The authors report lower trajectory errors, preliminary single-rollout generation approximately 25 times faster for 3D motion forecasting, and world-action-model success of 70.2 percent versus 62.6 percent across four MolmoSpaces suites.

---

### 3. Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training
**Authors:** Kangning Zhang, Wenxiang Jiao, Bowen Fang, Shuai Shao, Jiachen Zhu, Rong Shan, Shijian Wang, Hao Wang, Yuan Lu, Weiwen Liu, Weinan Zhang
**arXiv:** [arxiv.org/abs/2611.04277](https://arxiv.org/abs/2611.04277)
**Summary:** Harness-S selectively replaces failed base-harness reinforcement-learning rollouts with fresh trajectories generated under complementary sibling harnesses, routing among them using policy-aware behavior profiles. Across AppWorld, SWE-Gym, and DBBench, the resulting policy outperforms policy-only training when deployed back under the original harness, with additional gains from rank-one harness selection at inference.

---

### 4. Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand
**Authors:** George Ling, Shanshan Zhong, Lijin Yang, Hao Yang, Nanxiang Li, Zhongzhan Huang
**arXiv:** [arxiv.org/abs/2611.00883](https://arxiv.org/abs/2611.00883)
**Summary:** BestRand stabilizes benchmark compression by reducing the rare high-error tail of otherwise effective random subsets, guided by an analytical approximation of estimation-error distributions. Across more than 70 text, multimodal, and agent benchmarks, the authors report average reductions of 50.2 percent in high-error risk and 16.4 percent in estimation error at 51.3 percent of competing methods’ construction cost.

---

### 5. SLA: Scaling Spatial-Language-Action Model via Continual Pre-training
**Authors:** Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang, Junwu E, Pengwei Wang, Yan Wang, Shunbo Zhou, Haoang Li
**arXiv:** [arxiv.org/abs/2611.08373](https://arxiv.org/abs/2611.08373)
**Summary:** SLA scales spatial alignment during continual pretraining of a pi05-initialized robot policy, supervising intermediate visual embeddings with a frozen 3D perception model across heterogeneous robot datasets. Feature-dependent gates, partial geometric annotations, and probabilistic state dropout support transferable spatial learning while all auxiliary components remain training-only and the original inference architecture is preserved.

---

### 6. WeLM-Image: A Unified Image Generation Model towards Visual Intelligence
**Authors:** Canmiao Fu, Chen Li, Guohui Zhang, Hao Lu, Hongyang Wei, Huadong Wu, Huaisong Zhang, Hubery Yin, Liyuan Cui, Qixin Yan, Tong Shao, Xiaoqiang Zhou, Xinhang Leng, Ying Zhang, Zhenhai Liu, Zhipeng Huang
**arXiv:** [arxiv.org/abs/2611.07392](https://arxiv.org/abs/2611.07392)
**Summary:** WeLM-Image combines multimodal understanding, text-to-image generation, instruction-guided editing, and multi-reference synthesis through a sparse Mixture-of-Transformers and Mixture-of-Experts architecture. The authors report strong open-source benchmark comparisons at native 1536 resolution, while an eight-step guidance-free Turbo variant generates a 1024-by-1024 image in 4.98 seconds on a single NVIDIA H20 GPU.

---

### 7. TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing
**Authors:** Ruikang Li, Zixuan Chen, Jiarui Wu, Mingde Yao, Yiyuan Zhang, Yujin Wang, Hanming Deng, Lewei Lu, Tianfan Xue
**arXiv:** [arxiv.org/abs/2611.06741](https://arxiv.org/abs/2611.06741)
**Summary:** TailSteer preserves early denoising behavior while concentrating content-preservation corrections near the trajectory tail, learning from an editor’s own on-policy rollouts rather than curated editing pairs. Across FLUX, SenseNova, and Qwen model families, the authors report substantially less cumulative drift over 15 to 20 editing turns while largely retaining text-to-image and single-turn editing performance.

---

### 8. EvoMemState: Evolving Memory State for Personal Agents
**Authors:** Zhishang Xiang, Yunbo Tang, Zhongqiao Liu, Junkai Chen, Zerui Chen, Qingguo Hu, Yuxuan Zhang, William Grant, Qinggang Zhang, Jinsong Su
**arXiv:** [arxiv.org/abs/2611.03743](https://arxiv.org/abs/2611.03743)
**Summary:** EvoMemState augments persistent facts with relational states describing validity and connections, plus an RL-generated reasoning state that determines how memories apply to the current request. Experiments on long-term dialogue and memory-use benchmarks report more complete retrieval and more accurate memory-grounded responses than existing memory systems.

---

### 9. D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding
**Authors:** Baoyou Chen, Ruiqiao Mei, Guancong Lin, Tao Song, Weihao Yuan, Qun Liu, Siyu Zhu
**arXiv:** [arxiv.org/abs/2611.06425](https://arxiv.org/abs/2611.06425)
**Summary:** D3D removes a diffusion drafter’s dependence on target-model hidden states, allowing successor blocks to be drafted asynchronously while earlier blocks are verified. Across seven benchmarks, it averages 5.00-times and 5.71-times decoding speedups with Qwen3-8B and Qwen3-32B targets, exceeding the reported DFlash comparisons while layer pruning retains over 99 percent of mean acceptance length in the stated three-benchmark study.

---

### 10. VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents
**Authors:** ZhengXian Wu, Qianhao Nie, Zhuohong Chen, Junjie Gao, Yuyao Zhang, Yunyao Yu, Hangrui Xu, Cheng Cheng, Guiyu Ma, Jin Zhang, Xingzhong Xu, Kai Yang, Haoqian Wang
**arXiv:** [arxiv.org/abs/2611.04894](https://arxiv.org/abs/2611.04894)
**Summary:** VisSearch-Bench contains 204 human-written tasks across seven domains and five visual-search structures, evaluating how multimodal agents connect image evidence with external information over multiple steps. Across 16 models, the best system fully solves only 26.47 percent of tasks despite search-tool access, highlighting limitations in visual context management.

---

### 11. Towards Foundation Decision Models: Drex
**Authors:** Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev, Darkhan Akhmetov, Yash Shah, Nurmukhamed Ubaidullayev, Raman Saparkhan, Dos Baha, Abulhair Saparov
**arXiv:** [arxiv.org/abs/2611.07854](https://arxiv.org/abs/2611.07854)
**Summary:** Drex provides four open decision models that return probability distributions over supplied options without autoregressive decoding, combining supervised training with reinforcement learning from adjusted feedback. The authors report strong decision-benchmark performance, option-order robustness, and typical 183-millisecond responses for Drex Max compared with roughly two to three-and-a-half seconds for the cited frontier-model comparisons.

---

### 12. Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models
**Authors:** Juncheng Ma, Jiaxin Li, Jiankai Tu, Bo Liang, Guodong Lv, Yufan Deng, Junzhe Tang, Liangzhu Yang, Chen Bian, Shukai Gong, Yintianrun Zhang, Zicong Cao, Baohao Zhu, Jianxin Bi, Tengfei Yan, Yinyuan Zhang, Kewei Zhang, Xinglong Chen, Kaiqi Chen, Duomin Wang, Xiaotian Tang, Liang Tan, Li Li, Yuan Xu, Haosen Yang, Yuqi Wang, Jingfei Xia, Songyan Huang, Zhiyang Dou, Zhen Dong, Enze Xie, Tat-Seng Chua, Daquan Zhou
**arXiv:** [arxiv.org/abs/2611.06817](https://arxiv.org/abs/2611.06817)
**Summary:** Open-HumanWAM releases a 50,000-hour annotated egocentric video corpus and open training recipes, finding a log-linear relationship between human pretraining hours and downstream robot success. Its hybrid human–robot, visual-goal-conditioned HumanWAM-Goal model reaches 92.70 percent Clean2Clean and 84.60 percent Clean2Random success on RoboTwin 2.0 and demonstrates adaptation to unseen physical-robot visual goals without parameter updates.

---

### 13. Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents
**Authors:** Haoqing Wang, Xiaoyi Zhang, Sicheng Fan, Zhexin Zhang, Xinjie Zhang, Jiahao Li, Bin Li, Yan Lu
**arXiv:** [arxiv.org/abs/2610.41432](https://arxiv.org/abs/2610.41432)
**Summary:** Hybrid Computer Use unifies programmatic tools, accessibility-based semantic interaction, and visual GUI actions, letting agents select and combine the most suitable channel while guarding against stale-state actions. On OSWorld 2.0, the authors report the highest partial and binary scores among compared systems and improvements in both efficiency and task success across all evaluated models.

---

### 14. On the Opportunities and Challenges of Prefill-to-Autoregressive Cross-Model Transfer
**Authors:** Zhenyi Shen, Junru Lu, Wei Liu, Jiangnan Ye, Jiazheng Li, Di Yin, Xing Sun, Tameem Adel, Yali Du, Lin Gui, Yulan He
**arXiv:** [arxiv.org/abs/2611.06976](https://arxiv.org/abs/2611.06976)
**Summary:** PLatour connects frozen large and small language models through lightweight reward-trained bridges for prefill-to-autoregressive cross-model transfer, including hybrid-attention architectures. Controlled experiments show that some apparent communication gains can be reproduced with uninformative signals or receiver-only adaptation, motivating PACT-Check to isolate genuine information transfer.

---

### 15. LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers
**Authors:** Minsoo Cheong, Sungjoo Yoo
**arXiv:** [arxiv.org/abs/2611.05304](https://arxiv.org/abs/2611.05304)
**Summary:** LoopVQ jointly quantizes KV-cache channels across loop steps and fine-tunes codebooks to preserve looped-transformer outputs, achieving strong results at 0.5 bits per element and retaining much BF16 accuracy at 0.25 bits when combined with TaSQ. Its SGLang implementation nearly halves decode latency at a 32K-token context and increases peak serving throughput by up to 4.3 times and 6.1 times on the evaluated Ouro models.

---

### 16. The SIMPLE Law for Energy Cost of LLM Inference
**Authors:** Hiari Pizzini Cavagna, Andrea Proia, Daniele Cesarini, Zeynep Kiziltan, Andrea Bartolini
**arXiv:** [arxiv.org/abs/2611.03330](https://arxiv.org/abs/2611.03330)
**Summary:** SIMPLE derives an architectural energy model separating prefill, next-token computation, and KV-cache costs instead of fitting each LLM independently. Across 13 dense LLMs on H100 GPUs, it achieves 11.97 percent mean absolute percentage error and explains why longer reasoning and agent histories can drive superlinear energy growth even with prefix caching.

---

### 17. EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure
**Authors:** Kwan Yun, Minhyeok Bang, Colette Suhjung Koo, Junyong Noh
**arXiv:** [arxiv.org/abs/2611.07909](https://arxiv.org/abs/2611.07909)
**Summary:** EDGAR trains a one-step conditional diffusion refiner on real and synthetic Gaussian-avatar failure cases, combining identity features and expert routing to correct recoverable appearance artifacts. Refined multi-view images become pseudo-targets for optimizing a single avatar, with experiments reporting better perceptual quality, reconstruction, and cross-view consistency without running the refiner on every rendered frame.

---

### 18. VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing
**Authors:** Yexin Liu, Yunlong Lin, Zehan Wang, Guangxin He, Xinli Xu, Jiajun Zha, Yaofu Liu, Yueze Wang, Bowen Ping, Yuanming Li, Amie Wang, Bernard Ghanem, Bing Li, Harry Yang
**arXiv:** [arxiv.org/abs/2611.03404](https://arxiv.org/abs/2611.03404)
**Summary:** VidDub trains a video-dubbing teacher with replacement-aware audio supervision that removes conflicting source-mouth reconstruction losses, then distills it into a full-context two-step diffusion editor. The authors report a 0.833 cross-audio Sync-C improvement from masking across three seeds and strong synchronization, visual quality, identity preservation, and visual speech recognition across four benchmarks.

---

### 19. Future Representation Distillation for Imagination-free World Action Models
**Authors:** Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye, Yekyung Nah, Hojung Jung, Kimin Lee, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2611.04527](https://arxiv.org/abs/2611.04527)
**Summary:** DreamFree distills future-video representations into a predictive visual encoder that operates on the current observation, enabling robot actions without generating future videos at inference. Across real and simulated tasks, the authors report stronger success rates than compared VLAs and WAMs, 11-Hz control with a 14-billion-parameter video backbone, and learning new tasks from video demonstrations without new-task action labels.

---

### 20. Decode Before You Hear: Speculative Listening for Chunk-Interleaved Full-Duplex Speech Language Models
**Authors:** Yutong Bian, Yanglin Zhang, Yuxiang Wang, Luoyuan Zhang, Rongshen He, Zihao Wang, Junwen Qiu, Jiaqi Li, Zhizheng Wu
**arXiv:** [arxiv.org/abs/2611.06982](https://arxiv.org/abs/2611.06982)
**Summary:** Speculative Listening uses idle listening compute to draft the next speech-model chunk under an assumed silence input, maintaining branches and verifying them once actual audio arrives without changing outputs. On TickTock-Bench, the authors report 2.6-to-2.8-times faster speech chunks, up to 23.4-times faster tool-call chunks, and a 73 percent average reduction in decoding delay before responses start.
