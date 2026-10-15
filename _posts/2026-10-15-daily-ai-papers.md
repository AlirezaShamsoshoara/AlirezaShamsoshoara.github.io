---
title: "Daily AI Papers — October 15, 2026"
date: 2026-10-15
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-15/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - reinforcement-learning
  - model-distillation
---

### 1. Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation
**Authors:** Wang, Weijie, Zhang, Haomin, Li, Ye, Liu, Akide, Zhang, Zeyu, Zhao, Haoyu, He, Yefei, Chen, Donny Y., Chen, Feng, Zhuang, Bohan
**arXiv:** [arxiv.org/abs/2610.20571](https://arxiv.org/abs/2610.20571)
**Summary:** ATAS compiles a screenplay into shot requests with explicit location, camera, and event-time references, then grounds generation in registered scene geometry and time-indexed event memory. Across four video generators it improves every reported cross-shot consistency measure, leads spatial-revisit and event-recapture comparisons, and earns the highest human ratings on all six criteria.

---

### 2. Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation
**Authors:** Tian, Shi-Yu, Liu, Yong, Liu, Ximan, Zhu, Tianrui, Bai, Sule, Yang, Xinwei, Liu, Ruiqi, Yu, Kun-Yang, Yang, Ming, Zhou, Zhi, Li, Yu-Feng, Sun, Yipeng, Simiu, Gu
**arXiv:** [arxiv.org/abs/2610.13521](https://arxiv.org/abs/2610.13521)
**Summary:** Road MOPD uses non-routed teachers as cross-domain critics, strengthening token corrections supported by teacher agreement while projecting away conflicting gradients. It mitigates degradation in disadvantaged domains, gains more than five percentage points under high conflict, and improves overall performance in low-conflict and three-domain settings.

---

### 3. Player-1: Learning to Play from Synthetic Experience
**Authors:** Ouyang, Mingyu, Wang, Yiran, Hu, Siyuan, Yin, Xingyilang, Sun, Huiqiang, Wang, Guangzhi, Pu, Junfu, Cheng, Cheng, Chen, Honghao, Shan, Ying, Shou, Mike Zheng, Ng, Hwee Tou
**arXiv:** [arxiv.org/abs/2610.20584](https://arxiv.org/abs/2610.20584)
**Summary:** Player-1 extends computer-use actions for game control and post-trains on 6,044 demonstrations plus reinforcement learning across sixteen synthetic 2D and 3D environments. Its 9B model reaches 38.33% success on MineDojo-300 versus 12.63% for the strongest baseline, with gains transferring to ViZDoom-10 and GameWorld.

---

### 4. Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents
**Authors:** Ge, Yuyao, Liu, Shenghua, Gao, Peizhong, Ge, Chendi, Liu, Chenxu, Wang, Yiwei, Mei, Lingrui, Bi, Baolong, Yao, Jiayu, Guo, Jiafeng, Cheng, Xueqi
**arXiv:** [arxiv.org/abs/2610.20344](https://arxiv.org/abs/2610.20344)
**Summary:** Doc2Harness directly benchmarks long-horizon harness engineering by asking models to construct a complete agent harness from an interface contract and development document, then testing it in isolated containers. Across nineteen frontier models and 328 deterministic cases, the best model reaches only 53.05%, exposing broad weaknesses in cross-cutting harness functionality.

---

### 5. More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning
**Authors:** Zhong, Linhao, Fang, Bozhen, Wang, Xuehao, Shi, Duochao, Luo, Zekai, Yao, Guangming, Yuan, Yi, Chen, Hao, Chen, Jingdong, Shen, Chunhua
**arXiv:** [arxiv.org/abs/2610.19789](https://arxiv.org/abs/2610.19789)
**Summary:** This study compares ten self-distillation methods with GRPO across four agent benchmarks, three model sizes, and 132 training runs totaling 12,124.4 H800 GPU-hours. No method consistently beats GRPO, strong final scores can conceal unstable training, and extra compute does not reliably improve performance.

---

### 6. Recovering Reliable Supervision via Critique-Guided On-Policy Distillation
**Authors:** Zhao, Kaixiang, Yu, Tianrun, Li, Shangzhe, Yang, Yuxiao, Hughes, Amanda, Zhang, Weitong, Killian, Taylor W.
**arXiv:** [arxiv.org/abs/2610.20572](https://arxiv.org/abs/2610.20572)
**Summary:** CriticOPD addresses failures in on-policy distillation where a teacher recognizes a student's error but continues from the faulty prefix instead of recovering. A teacher critique guides a rewritten solution used for training, improving two Qwen3 students across six mathematical-reasoning benchmarks with the largest gains on competition problems.

---

### 7. LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation
**Authors:** He, Zefeng, Chai, Yunkai, Chen, Xiaoyang, Zhu, Tong, Wu, Zongliang, Luo, Yun, Li, Yafu, Cheng, Yu
**arXiv:** [arxiv.org/abs/2610.19975](https://arxiv.org/abs/2610.19975)
**Summary:** LatentLoop exploits asymmetry between repeated MoE block visits by compressing the first visit's sequence, preserving full resolution in the second, and reallocating compute to a wider hidden state. Across fifteen configurations from 1.3B to 7B parameters it consistently lowers validation loss, predicts up to 19.0% compute savings, and improves nine-benchmark averages.

---

### 8. Cortex: Consolidating Context into Parametric Memory
**Authors:** Zhang, Jintian, He, Feng, Liang, Xinnian, Xu, Ziwen, Xu, Haoming, Huang, Haojing, Wu, Shuangzhi, Zhang, Ningyu
**arXiv:** [arxiv.org/abs/2610.20399](https://arxiv.org/abs/2610.20399)
**Summary:** Cortex consolidates temporary context into mergeable low-rank or structural feed-forward updates by generating prospective queries and distilling context-conditioned outputs. Across 4B to 120B text and multimodal models it usually lies on the consolidation-retention Pareto frontier, retaining 99.8% of non-target performance after fifty sequential factual edits.

---

### 9. RuleTrek: Benchmarking Agentic Rule Reasoning in Complex Scenarios
**Authors:** Yuan, Chenhao, Yu, Bohan, Xu, Yinhao, Yin, Chao, Zhou, Chenxi, Wang, Zhaoxuan, Xu, Shuwen, Huang, Shaoping, Ren, Haolin, Liu, Jiaxiang, Xu, Yao, Zhao, Jun, Liu, Kang
**arXiv:** [arxiv.org/abs/2610.19698](https://arxiv.org/abs/2610.19698)
**Summary:** RuleTrek evaluates agents on identifying, deducing, and applying domain rules when scenario evidence is distributed across interactive multi-file workspaces. Eleven frontier models top out at 62.47% for rule identification, 60.43% for deduction, and 55.29% end to end, showing substantial room for improvement.

---

### 10. ActionOPD: Distilling Decisions, Not Tokens
**Authors:** Yuan, Huining, Yi, Xiangmin, Xu, Zelai, Wang, Zixu, Chen, Xinlei, Zhang, Xiao-Ping, Wang, Yu, Yu, Chao
**arXiv:** [arxiv.org/abs/2610.19820](https://arxiv.org/abs/2610.19820)
**Summary:** ActionOPD distills black-box teachers at the level of semantic actions rather than tokens, rewarding student actions for agreement with teacher decisions at student-visited states. Qwen3-4B and 8B students gain 3.3 to 6.9 percentage points across four out-of-distribution tool-use benchmarks without shared tokenizers or teacher token probabilities.

---

### 11. Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory
**Authors:** Guo, Minghao, Jiao, Qingyue, Liu, Xiujin, Pang, Jianhong, Yang, Ruimeng, Xu, Naihao, Che, Liwei, Xue, Haochen, Wang, Ziqi, Cai, Xinying, Luo, Jiaxuan, Deng, Jiaxin, Ye, Xuesong, Qu, Jintao, Gao, Wenyao, Gu, Jingwen, Zhao, Chenyang, Liu, Shichun, Zhang, Guibin, Liu, Zefang, Wang, Siyin, Xu, Wujiang, Li, Danrui, Shi, Zeru, Yeo, Woongyeong, Liu, Shuang, Huang, Wei-Chieh, Zhang, Weizhi, Yang, Tianyu, Kim, Kangsan, Hu, Yebowen, Wen, Bowen, Jiang, Bowen, Su, Haohao, Yin, Ming, Yu, Sheldon, Zhang, Mian, Chen, Yuyan, Zhang, Hanrong, Mei, Kai, Zhang, Zihao, Jin, Mingyu, Zhu, Xi, Wang, Hengyi, Wei, Tianxin, Nan, Linyong, Liang, Zhenwen, Chu, Zhendong, Huang, Ziqi, Su, Yongye, Dong, Sixun, Liu, Shujian, Liang, Kaiqu, Han, Jiaojiao, Fei, Zhaoye, Wang, Kun, Dou, Shihan, Guo, Zhichun, Diao, Xingjian, Gu, Zeqi, Wang, Heng, Feng, Tao, Qian, Cheng, Palangi, Hamid, Xu, Silei, Yun, Xi, Zhu, Yi, Liu, Shilong, Wen, Qingsong, Hwang, Sung Ju, Wu, Zuxuan, Jiang, Yu-Gang, Shi, Yiyu, Metaxas, Dimitris N., You, Jiaxuan, McAuley, Julian, Wang, Mengdi, Han, Jiawei, Yu, Philip S., Ye, Ziyi
**arXiv:** [arxiv.org/abs/2610.19366](https://arxiv.org/abs/2610.19366)
**Summary:** This survey organizes multimodal agent memory along two axes: how heterogeneous information is represented and how memory-management policies adapt with experience. It distinguishes static, dynamic, and self-evolving memory while deriving design principles for fidelity, abstraction, temporal validity, provenance, and evidence-grounded retrieval.

---

### 12. LensErase: A Foundation Model for Erase Anything
**Authors:** Chen, Yunuo, Wu, Xiuyu, Yang, Qinhong, Zhao, Jinjing, Dong, Yanchen, Zhang, Sirui, Chen, Dong, Wei, Fangyun, Shi, Lei, Li, Ji, Chen, Dongdong, Lu, Guo, Lu, Yan, Guo, Baining
**arXiv:** [arxiv.org/abs/2610.18072](https://arxiv.org/abs/2610.18072)
**Summary:** LensErase is a general-purpose mask-based erasing foundation model trained from 101.07 million source-mask-target examples and refined with contract-guided regional rewards. Mask-Aware RoPE incorporates erase masks efficiently, while TraceFusion preserves unaffected content and helps the model outperform prior systems across six public benchmarks and LensErase-Bench.

---

### 13. Apertus 1.5: From Open Text Models to Open Multimodal Reasoners
**Authors:** Apertus, Project, Xu, Yixuan, Turki, Yassine, Sabolčec, Vinko, Pyatkin, Valentina, Chu, Tommy, Najem-Meyer, Sven, Carroll, Sean F., Smith, Robert, Kreft, Raphael, Tazza, Oscar Alessandro, Lavrovsky, Oleg, Irmiger, Nicola, Santelmo, Matteo, Schneider, Marian, Giraldo, Juan García, Yukhymenko, Hanna, Ďurech, Eduard, Melikidze, Davit, Tamayo, Dani, Messmer, Bettina, Ahadinia, Aryan, Yadav, Anunay, Huang, Allen, Fraij, Ahmad, Bombarda, Alessandro, Padula, Alex, Hägele, Alexander, Sternfeld, Alexander, Hedström, Anna, Kosovskaia, Anna, Wuhrmann, Arthur, Balasubramaniam, Arundhati, Mahouri, Badr Al, Pasztor, Barna, Szostakiewicz, Bartosz, Doan, Bich Ngoc, Schmid, Bryan, Sezen, Burak, Challier, Camille, Charmillot, Clément, Shayakhmetova, Dana, Perruchoud, Daniel, Brüggemann, David, Isztl, David, Palme, Elia, Anastassova, Emma, Bösch, Fabian, Zahiragić, Faruk, Mohamed, Fawzi Roberto, Panicali, Fiona, Kolly, Florian, Guerra, Flynn, Monti, Francesco, Lübeck, Frederike, Oliva, Gennaro, Yang, Haofeng, Shang, Haoliang, Khoury, Helen El, Mendonça, Henrique, Vamvas, Jannis, Landolt, Jérome, Lam, Jessica, Xiao, Jingchun, Coles, Jonathan, Oyebanji, Joshua, Nguyen, Khanh, Pitas, Konstantinos, Strand, Lasse B., Mi, Li, Deslarzes, Loïc, Baggi, Lorenzo, Noci, Lorenzo, Baumann, Luca, Sartori, Luca, Drescher, Lukas, De Negri, Marco, Passerini, Marco, Klein, Mark, Stojanovic, Marko, Majsec, Martin, Ansaripour, Matin, Busato, Mattea, Pellonara, Mauro, Neuwinger, Max, Graber, Michael, Tešnar, Michal, Wastl, Michelle, Gila, Miguel, Boronski, Mikolaj, Magnin, Morgane, Reihs, Moritz, Sayfiddinov, Mukhammadali, Ranchin, Nathan, Cuveillier, Nicolas, Wohlfahrt, Oscar, Zou, Qianqian, Kamysheva, Rada, Sevastjanova, Rita, Machacek, Roman, Keller, Sebastian, Matrenok, Simon, Pierre, Simon, Schuppli, Stefano, Chen, Suei-Wen, Horváth-Mikulas, Szabina, Perez, Taliesin, Spinner, Thilo, Buening, Thomas Kleine, Robinson, Tim, Kwiecinski, Tymoteusz, Zouhar, Vilém, Thoma, Vinzenz, Yao, Xiaozhe, Metz, Yannick, Fukuhara, Yuhei, Askari, Yusif, Chen, Zixuan, Ilic, Alexander, Klimovic, Ana, Krause, Andreas, Kucharavy, Andrei, Ash, Elliott, VandeVondele, Joost, Rajman, Martin, El-Assady, Mennatallah, Schulthess, Thomas, Kehrer, Timo, Hoefler, Torsten, Bosselut, Antoine, Jaggi, Martin, Schlag, Imanol
**arXiv:** [arxiv.org/abs/2610.15542](https://arxiv.org/abs/2610.15542)
**Summary:** Apertus 1.5 extends the fully open Apertus family to image and audio understanding, 262,144-token context, verifiable-reward training, and switchable thinking while keeping the architecture and text-only output head. The released 8B and 70B models improve nearly every predecessor benchmark, remain competitive with fully open multimodal systems, and publish weights, data recipes, training recipes, and evaluations.

---

### 14. KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization
**Authors:** Park, Sihwan, Kim, Sung-Yub, Jang, Doohyuk, Yang, Eunho
**arXiv:** [arxiv.org/abs/2610.14448](https://arxiv.org/abs/2610.14448)
**Summary:** KV4-RL combines calibration-free INT4 KV-cache quantization with selective INT8 protection for attention sinks and recent context to accelerate asynchronous RLVR rollouts without destabilizing learning. Over 400 GRPO iterations it delivers a 1.80-times cumulative rollout speedup and stays within 0.5 percentage points of BF16-rollout accuracy on two Qwen3 model sizes.

---

### 15. Towards Agentic Robots: Model, Data, Environment, and Harness
**Authors:** Qin, Chonghan, Wu, Dongming, Feng, Kaituo, Wang, Jiaxu, Yu, Xinlei, Sun, Peiwen, Fan, Yijia, He, Xilin, Chen, Bingao, Lian, Weitong, Ji, Ryan, Ren, Wenqi, Hu, Xiaobin, Lin, Dahua, Jiang, Yu-Gang, Yue, Xiangyu
**arXiv:** [arxiv.org/abs/2610.20442](https://arxiv.org/abs/2610.20442)
**Summary:** This survey defines agentic robots as systems that reason over instructions, interact with environments, correct execution errors, and dynamically adjust operational strategies. It organizes the field into seventeen categories spanning models, data, environments, and harnesses, connecting vision-language-action policies, world models, data curation, evaluation, and orchestration.

---

### 16. Hybrid Reasoning Agents
**Authors:** Zou, Jiaru, Qi, Yunzhe, Chen, Sirui, Bianchi, Federico, Zhu, Shang, Lu, Pan, He, Jingrui, Zou, James
**arXiv:** [arxiv.org/abs/2610.18861](https://arxiv.org/abs/2610.18861)
**Summary:** HybridAgents move dynamically between latent reasoning and text-based tool interaction using a lightweight transition module and continuous working memory. Across three model scales and eleven benchmarks they improve performance by 10.4% while reducing generated tokens by 35.5% to 54.7%, speeding inference up to 2.6 times, and cutting cost up to 3.7 times.

---

### 17. HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution
**Authors:** Jang, Kyochul, Park, Seohyeon, Kwon, Ohchul, Park, Sangjun, Choi, Junhyeok, Yi, Seungyeop, Kim, Chaeyun, Lee, Sangkyu, Szpektor, Idan, Caciularu, Avi, Park, Jongmin, Yu, Youngjae
**arXiv:** [arxiv.org/abs/2610.02089](https://arxiv.org/abs/2610.02089)
**Summary:** HumanoidToolBench jointly evaluates tool selection, manipulation, and mobile execution through eighteen tasks, while ToolBook supplies 3,100 simulated and real Unitree G1 demonstrations. Tests of seven simulated and three real-robot policies reveal a large gap between choosing an appropriate tool and successfully completing the task, especially with unseen tools.

---

### 18. Super-Resolution in The Right Latent Space: A Frozen Vision-Foundation Substrate
**Authors:** Lei, Wanzhou, Shen, Cuifeng, He, Yanjin, Li, Maohua, Yuan, Hua, Persson, Per-Olof, Lan, Tao, Liu, Kan, Tang, Hanlin
**arXiv:** [arxiv.org/abs/2610.04781](https://arxiv.org/abs/2610.04781)
**Summary:** RAESR performs real-world super-resolution in a frozen fused DINOv3 latent space where degraded images remain close to the natural-image manifold and retain both detail and semantics. A 415M one-pass decoder achieves the best fidelity-perception tradeoff on four benchmarks at 37 milliseconds per 512-by-512 image, beating the same recipe built on VAE latents.

---

### 19. The Thinking Leakage in Reinforcement Learning for LLMs
**Authors:** Zhu, Wenxuan, Liu, Shuming, An, Bang, Aliev, Aznaur, Li, Bing, Yang, Yibo, Ghanem, Bernard
**arXiv:** [arxiv.org/abs/2610.14270](https://arxiv.org/abs/2610.14270)
**Summary:** The paper argues that reinforcement-learning gains reported for Qwen3 models in NO-THINK mode largely come from reactivating reasoning already present in THINK mode rather than learning new capabilities. Weight, activation, attention-head, and gradient analyses show RL-trained models shifting toward THINK behavior, with low-dimensional activation swaps removing or transferring much of the gain.

---

### 20. Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders
**Authors:** Li, Xin, Jiang, Hao, Guo, Jinghao, Lin, Weisi, Yuen, Chau
**arXiv:** [arxiv.org/abs/2610.17771](https://arxiv.org/abs/2610.17771)
**Summary:** ReMaRk removes responder noise from GRPO recommenders by scoring each generated list against the union of valid titles across all replies and sampling each request equally. Across seven backbones and three datasets it reaches Rank-GRPO's validation recall in 25% to 53% of the steps and is never significantly worse after full training.

---
