---
title: "Daily AI Papers — October 22, 2026"
date: 2026-10-22
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-22/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - video-generation
  - robotics
---

### 1. StreamEval: Evaluating Interactive Streaming Video Generation Models
**Authors:** StreamEval Team
**arXiv:** [arxiv.org/abs/2610.28402](https://arxiv.org/abs/2610.28402)
**Summary:** StreamEval benchmarks interactive streaming video generation across five tasks using 300 scripted cases and ten metrics covering execution, consistency, fidelity, and audiovisual coordination. Evaluation of 37 models shows that high visual quality does not guarantee reliable request execution or sustained state consistency.

---

### 2. SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?
**Authors:** Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li
**arXiv:** [arxiv.org/abs/2610.26659](https://arxiv.org/abs/2610.26659)
**Summary:** SpatialScout evaluates VLM agents on active object-level 3D mapping across 80 indoor scenes and 3,140 target objects, requiring camera exploration and metric localization under bounded interaction budgets. The strongest evaluated model achieves 41.71% mean overlap, revealing a substantial gap between coarse layouts and complete, precise maps.

---

### 3. Cache Engineering for Agents
**Authors:** Tianyu Fu, Ruoxi Wang, Zihan Min, Zhongqi Ren, Zhihao Li, Tengxuan Liu, Shengxu Mu, Hanling Zhang, Yu Wang
**arXiv:** [arxiv.org/abs/2610.28577](https://arxiv.org/abs/2610.28577)
**Summary:** Cache engineering lets agents drop selected KV-cache states and adjust retained keys without rewriting trajectories or re-prefilling retained context, supported by the stateful AKV serving engine. A rolling-drop policy improves average benchmark scores by 1.7 points while cutting average cost by 27.7%, with AKV delivering up to 1.2-times output throughput and 1.5-times faster P95 latency.

---

### 4. DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations
**Authors:** Mingze Sun, Ziang Cao, Yuan Fei, Qiankuan Tao, Zihan Wang, Tianqi Liu, Junhao Chen, Haiwen Diao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
**arXiv:** [arxiv.org/abs/2610.29997](https://arxiv.org/abs/2610.29997)
**Summary:** DONIC learns a generalist bimanual tracker from heterogeneous human references using PPO, behavioral cloning, contact-role rewards, and successful-execution recycling, alongside the BiHOI dataset of 1,575 sequences spanning 229 objects. Without fine-tuning, one checkpoint achieves 86.79% success on unseen trajectories of training objects and 57.32% on held-out objects.

---

### 5. Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation
**Authors:** Ruopeng Gao, Yukun Huang, Jiarui Hu, Shuai Wang, Wenbo Hu, Ying Shan, Limin Wang
**arXiv:** [arxiv.org/abs/2610.29989](https://arxiv.org/abs/2610.29989)
**Summary:** Future Chunk Prediction augments teacher-forced autoregressive video denoising with an objective that predicts temporally separated chunks without intervening visual context. It improves physical plausibility with a lower overall training compute budget, needs no extra pretrained visual encoder, and leaves autoregressive inference unchanged.

---

### 6. Agent World Model in the Wild: Computer-Use Agent Environment Synthesis
**Authors:** Zhaoyang Wang, Qianhui Wu, Haorui Wang, Simon Yu, Baolin Peng, Canwen Xu, Hao Cheng, Wenlin Yao, Boyi Liu, Yite Wang, Jianfeng Gao, Huaxiu Yao
**arXiv:** [arxiv.org/abs/2610.26828](https://arxiv.org/abs/2610.26828)
**Summary:** WildAWM uses open-source models to synthesize executable computer-use environments with GUI, MCP, and command-line interfaces, applying execution-based gates to task solvability, difficulty, and verifier reliability. Its 341 long-horizon environment-task pairs support training two Qwen models that improve across eight out-of-distribution web, claw, and computer-use benchmarks.

---

### 7. PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through Decomposed Rubric Synthesis
**Authors:** Qiushi Sun, Jingyang Gong, Yang Liu, Qiaosheng Chen, Zhangyue Yin, Zixian Huang, Hanxu Hu, Jing Xiong, Fangzhi Xu, Haochen Tan, Haoli Bai, Lifeng Shang, Xiaoguang Li, Ben Kao, Qipeng Guo, Lingpeng Kong, Jiahui Gao
**arXiv:** [arxiv.org/abs/2610.20538](https://arxiv.org/abs/2610.20538)
**Summary:** PrismaForge synthesizes hierarchical rubrics that assess program correctness, construction quality, and rendered appearance, using the same criteria for data filtering and reinforcement-learning rewards. The resulting PrismaCoder-2M dataset trains released 9B and 35B models that lead the reported open multimodal coding state of the art and rival leading proprietary systems.

---

### 8. Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds
**Authors:** Kuan Zhang, Yukun Chen, Zhihao Yang, Yue Su, Xiangnan Wu, Zirong Chen, Run Luo, Jinkun Hou, Tao Tan, Yinhe Zheng, Yiming Li
**arXiv:** [arxiv.org/abs/2610.28698](https://arxiv.org/abs/2610.28698)
**Summary:** A controlled continued-pretraining study spans 120 configurations, four model sizes from 0.8B to 27B, data budgets of 50 to 1,600 hours, and five mixtures of virtual worlds. More data improves in-corpus performance and diversity helps related-world transfer, but persistent distant-world gaps indicate that richer training stages are needed beyond imitation.

---

### 9. Spectral-Spatial Interpretation
**Authors:** Haotian Ma, Ruqi Yang, Philip Townsend
**arXiv:** [arxiv.org/abs/2610.21114](https://arxiv.org/abs/2610.21114)
**Summary:** Spectral-Spatial Interpretation applies local conditional Shapley games to position-channel pairs, producing a full attribution matrix instead of separate spatial heatmaps and global channel scores. Across three datasets it leads joint deletion and insertion metrics, and on HLS Burn Scar it outperforms an MC-Owen estimator using about 6% of its evaluation budget.

---

### 10. Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills
**Authors:** Letian Zhu, Han Li, Yifan Yao, Xinping Lei, Xinyu Che, Jiahao Wang, Dianyi Wang, Yucheng Fu, Jiakai Wang, Zhiqi Bai, Wenbo Su, Jiaheng Liu
**arXiv:** [arxiv.org/abs/2610.17860](https://arxiv.org/abs/2610.17860)
**Summary:** Socratic Skill Learning interleaves expert guidance with student-operated practice and student-authored reusable skills, evaluated on SkillTransferBench with 35 task families and 408 executable cases. Issue-guided review reaches 0.805 utility on the main cohort while using 61.7% fewer educator tokens and 16.9% fewer total acquisition tokens than fixed-window review.

---

### 11. Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents
**Authors:** Jiaming Zhang, Xuan Wang, Fuyao Zhang, Yang Cao, Lingjuan Lyu, Wei Yang Bryan Lim
**arXiv:** [arxiv.org/abs/2610.11942](https://arxiv.org/abs/2610.11942)
**Summary:** LGWM is a decoder-free, action-conditioned GUI world model trained on 1.85 million real transitions to predict the next screen representation, enabling verification through vector comparison. On RSWT-BENCH it reaches 0.987 AUC at 17 ms per decision, while residual direction separates harmful from benign violations at 0.953 AUC.

---

### 12. Retrieval Augmented Generation Compositionality
**Authors:** Ido Levy, Segev Shlomov, Leshem Choshen
**arXiv:** [arxiv.org/abs/2610.29722](https://arxiv.org/abs/2610.29722)
**Summary:** LASAGNA evaluates RAG composition through 450 configurations across eight benchmarks and corpora ranging from 5,000 to 200,000 documents. Individually strong components fail to deliver their predicted combined gains, retrieval and faithfulness can conflict, and the best stack changes with corpus scale.

---

### 13. AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics
**Authors:** Xinxin Liu, Bingxin Xu, Wenrui Bao, Ming Li, Wentao Bao, Chen Chen, Yuzhang Shang
**arXiv:** [arxiv.org/abs/2610.28589](https://arxiv.org/abs/2610.28589)
**Summary:** AgenticRoboRL combines supervised fine-tuning and multi-turn reinforcement learning to post-train robot planners across VLA-skill and control-code harnesses while leaving execution components fixed. On LIBERO-PRO it raises a 9B planner from 18.1% to 71.0% success without external memory, approaching the reported 72.1% of Codex with external memory.

---

### 14. Memory-Centric Continual Learning for AI Agents
**Authors:** Dongfang Li, Zhuoen Chen, Bonian Jia, Zixuan Liu, Zhengxuan Lu, Can Deng, Yukun Shi, Yuhang Meng, Xin Zhang, Jiahe Huang, Fuhao Li, Junmai Wang, Shunyao Wen, Jingjun Sun, Jiaxu Tian, Jiangling Zhang, Zihan Wang, Liangyou Li, Yitong Yao, Shuangyong Song, Beilun Wang, Pengxu Wei, Hanlin Xu, Chang Liu, Yongxiang Li, Baotian Hu, Xiangyang Ji, Min Zhang
**arXiv:** [arxiv.org/abs/2610.29357](https://arxiv.org/abs/2610.29357)
**Summary:** Memory-Centric Continual Learning reframes agent memory as a driver of better future actions through a substrate-asset-policy taxonomy and a two-loop lifecycle for memory and management-policy updates. It proposes retention, adaptation, and transfer evaluation alongside a scaling framework relating performance to experience, storage, and compute.

---

### 15. Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research
**Authors:** Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, Xinjie Lin, Yuzhao Peng, Ruoyu Han, Youjie Zheng, Kaisen Yang, Qinhuai Na, You Fu, Calvin Xiao
**arXiv:** [arxiv.org/abs/2610.30113](https://arxiv.org/abs/2610.30113)
**Summary:** Quant-Arena benchmarks end-to-end quantitative research on real A-share data, allowing feedback only on 2022-2023 before freezing strategies for a sealed 2024 evaluation with trading constraints and costs. Nine frontier models are assessed, and although GPT-6 Astra scores highest, none beats the equal-weight market in the held-out year.

---

### 16. TraceForge: Distilling with Your Own Thinking
**Authors:** Yan Wang
**arXiv:** [arxiv.org/abs/2610.29680](https://arxiv.org/abs/2610.29680)
**Summary:** TraceForge generates reasoning traces from a context and teacher answer in the student model family's style using supervised generator training followed by adversarial refinement. With the same 5,000 questions and teacher answers, its generated traces improve HumanEval+ by 3.7 points and MBPP+ by 7.1 points relative to the compared teacher-thinking corpus.

---

### 17. DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents
**Authors:** Tianle Chen, Pushkar Singh, Ketan Todi, Biswajit Paria, Qijia He, Wenqi Wang, Yuwen Tan, Jike Zhong, Sugato Basu, Deepti Ghadiyaram, Arjun Akula
**arXiv:** [arxiv.org/abs/2610.19376](https://arxiv.org/abs/2610.19376)
**Summary:** DeLoop mines repeated actions as negative examples and later non-looping actions as positives from an agent's own rollouts, then trains with direct preference optimization without task rewards or judges. Under CodeGym history compression it reduces Qwen3-8B tasks containing loops from 57.3% to 6.1% with roughly one-third the steps, while raising Qwen3-32B task success from 37.7% to 44.8%.

---

### 18. Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use
**Authors:** Yanzhe Chen, Ziyi Yang, Jifeng Zhu, Qiming Huang, Ruihe An, Peiyao Xu, Hesen Yang, Runda Liu, Chang Gong, Zhijun Cao, Zechen Bai, Wenzheng Zeng, Yiqi Lin, Guoqiang Liang, Kevin Yuchen Ma, Kevin Qinghong Lin, Mike Zheng Shou
**arXiv:** [arxiv.org/abs/2610.30108](https://arxiv.org/abs/2610.30108)
**Summary:** PAPAV organizes multimodal embodied agents around five functions: Perceive, Anticipate, Plan, Act, and Verify, comparing computer-use and robotic systems under physical constraints. Across 64 benchmarks, only five explicitly assess anticipation and three assess verification, exposing capability gaps hidden by aggregate task success.

---

### 19. ALPS: Visual State Encoders for World Models
**Authors:** Yanqing Liu, Letian Zhang, Chengzhi Liu, Zijun Wang, Jieru Mei, Hongliang Fei, Yuyin Zhou, Cihang Xie
**arXiv:** [arxiv.org/abs/2610.30120](https://arxiv.org/abs/2610.30120)
**Summary:** ALPS pretrains a ViT-B/16 visual state encoder from still images and text to combine physical-state information, language alignment, and pixel reconstruction in one set of patch tokens. Across fifteen encoders it achieves the lowest aggregate LIBERO state-probe error among ViT-B models, and its frozen tokens reach 85.5% mean LIBERO policy success with the native text tower.

---

### 20. Harness Scaling for Generalizable Agentic Reinforcement Learning
**Authors:** Fei Bai, Huatong Song, Chuan Hao, Ran Tao, Jian Yang, Bryan Dai, Wayne Xin Zhao, Ji-Rong Wen
**arXiv:** [arxiv.org/abs/2610.29458](https://arxiv.org/abs/2610.29458)
**Summary:** Harness Scaling trains agentic RL over a factorized space of execution configurations, using balanced factorial coverage and controlled same-task variation instead of one fixed harness. Across benchmarks, model scales, and RL algorithms, the structured diversity improves transfer to unseen white-box configurations and external black-box harnesses.
