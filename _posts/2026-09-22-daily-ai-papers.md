---
title: "Daily AI Papers — September 22, 2026"
date: 2026-09-22
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-22/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - robotics
  - video-generation
---

### 1. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses
**Authors:** Peng Xia, Rujun Han, Zifeng Wang, Yanfei Chen, Yufan Zhang, Yoonho Lee, Chengsong Huang, Han Yu, Zhongying CuiZhu, Yifei Ming, Huaxiu Yao, Burak Gokturk, Tomas Pfister, Chen-Yu Lee
**arXiv:** [arxiv.org/abs/2609.24972](https://arxiv.org/abs/2609.24972)
**Summary:** RRSI regularizes recursive harness improvement by limiting proposal size, encouraging unexplored trajectories, and filtering benchmark-specific, costly, tiny, or obsolete edits. Across eight benchmarks, it gained up to 14.1 points in-distribution and 4.7 points on five out-of-distribution benchmarks while using 30% fewer policy tokens than unregularized evolution.

---

### 2. WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory
**Authors:** Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan
**arXiv:** [arxiv.org/abs/2609.24984](https://arxiv.org/abs/2609.24984)
**Summary:** WorldCrafter uses a camera-queryable implicit 3D-aware memory that compresses multi-view history into target-view-specific tokens for video generation. It improved long-horizon consistency and camera-control accuracy while preserving visual quality during minute-scale exploration from an image or text prompt.

---

### 3. GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay
**Authors:** Yiran Wang, Xingyilang Yin, Junfu Pu, Guangzhi Wang, Kaifeng Li, Mingyu Ouyang, Huiqiang Sun, Lingen Li, Cheng Cheng, Wangbo Yu, Honghao Chen, Xiaodong Cun, Chi-Man Pun, Zhiguo Cao, Ying Shan
**arXiv:** [arxiv.org/abs/2609.25001](https://arxiv.org/abs/2609.25001)
**Summary:** GameHorizon combines an annotation pipeline, 5,000 hours of aligned gameplay from 21 games and 100 expert players, and reproducible offline and stepwise online evaluations. Evaluation of 47 models through more than one million invocations revealed a hierarchy of task difficulty and substantial differences among model capabilities.

---

### 4. Transferring the Intelligence of VLMs to Robotic Control
**Authors:** Meng-Hao Guo, Zhe-Han Mo, Jia-Jun Wang, Yi Zhang, Kejin Wang, Yi-Xuan Deng, Jia-Peng Zhang, Yongming Rao, Shi-Min Hu
**arXiv:** [arxiv.org/abs/2609.22966](https://arxiv.org/abs/2609.22966)
**Summary:** RoboDawn lets an agentic vision-language model control robots in closed loop through discrete translation, rotation, and gripper commands, with demonstrations used for in-context grounding. One demonstration raised success from 53.2% to 73.6% on RoboTwin 2.0 C2R and from 35.67% to 47.17% on RoboDojo, and the framework also transferred to real robots.

---

### 5. OmniEdu: Open Foundation Models for Learning and Teaching
**Authors:** Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang
**arXiv:** [arxiv.org/abs/2609.23088](https://arxiv.org/abs/2609.23088)
**Summary:** OmniEdu is an open family of 4B, 9B, and 27B educational models tuned on 69,999 examples organized around subject competence, curriculum grounding, diagnostic reasoning, and pedagogical action. Education-oriented tuning consistently improved curriculum grounding, K-12 problem solving, and tutoring across scales, with OmniEdu-27B reaching 85.89% on MathFish and 86.95% on EDUMATH.

---

### 6. Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion
**Authors:** Uday Allu, Abhivanth Sivaprakash, Pratik Singh, Aman Manocha
**arXiv:** [arxiv.org/abs/2609.24220](https://arxiv.org/abs/2609.24220)
**Summary:** D-RAC normalizes heterogeneous documents to PDF, converts rendered pages to retrieval-oriented Markdown with one multimodal model pass, and plans chunks over identifiers without regenerating source text. On 236 documents totaling 795 pages, it produced 1,748 chunks with zero errors while reducing chunking output tokens by 95.7%, cost by 77.8% to 85.6%, and time by 75% against agentic chunking.

---

### 7. VideoGen-Agent: Reinforcing Video Generation Agents
**Authors:** Binxu Li, Haoyi Duan, Yuhui Zhang, Yaohui Zhang, Zihao Lin, Kaituo Feng, Suozhi Huang, Xiangyi Li, Yu Li, Chunyuan Li, Shilong Liu, Mengdi Wang
**arXiv:** [arxiv.org/abs/2609.24997](https://arxiv.org/abs/2609.24997)
**Summary:** VideoGen-Agent is trained with supervised trajectories and multitask reinforcement learning to coordinate augmentation, generation, and verification tools across six video tasks. On the 600-prompt VABench, it raised its base generator's score from 56.5 to 75.6, reached 86.1 with upgraded tools without retraining, and was preferred over the strongest standalone baseline in 84.3% of human comparisons.

---

### 8. onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction
**Authors:** Lei Yang, Mengyin Liu, Jia Wang, Hangyu Guo, Liang Zhao, Zheng Ge, Kang An, Binxing Jiao, Qi Han, Daxin Jiang, Siqi Shen, Xiangyu Zhang
**arXiv:** [arxiv.org/abs/2609.24983](https://arxiv.org/abs/2609.24983)
**Summary:** onPanda lets annotators correct the first inappropriate token in a response and continue generation from the corrected prefix, preserving much of the model's sampling distribution. A small controlled study found 52% lower median annotation time than manual post-editing, while recorded corrections provide position-specific and paired positive-negative supervision.

---

### 9. Grounded Action Model: 3D Grounding as a Foundation for Robotics
**Authors:** Gehao Zhang, Weikai Huang, Shailesh Shailesh, Yiyan Peng, Jiafei Duan, Ranjay Krishna
**arXiv:** [arxiv.org/abs/2609.23863](https://arxiv.org/abs/2609.23863)
**Summary:** Grounded Action Models convert language, point, or box prompts into a shared object-centric representation containing target-focused features and metric geometry for action prediction. GAM reached 55.3% average success across 50 RoboTwin 2.0 tasks and 61% across 16 LIBERO-PRO perturbation settings, while also improving robustness and long-horizon completion on real robots.

---

### 10. HuRo: Robotizing Human Videos for Scalable VLA Pretraining
**Authors:** Jinho Jeong, Se June Joo, Jaehyun Kang, Dongyun Kim, Yena Kim, Hanjung Kim, Seon Joo Kim
**arXiv:** [arxiv.org/abs/2609.10706](https://arxiv.org/abs/2609.10706)
**Summary:** HuRo converts heterogeneous human videos into robot-aligned observations and action trajectories, yielding about 630,000 episodes and 142 million processed frames from five sources. Across four real-world manipulation tasks, scaling robotized pretraining improved overall completion from 51.5% to 80.3% and out-of-distribution completion from 34.9% to 72.2%.

---

### 11. One to More, More to One: Category-Aware Iterative Expert Training for Software Engineering Agents
**Authors:** Jie Zhao, Ziyu Jiang, Suhang Zheng, Minghui Shan, Xiaoxiao Xu, Lin Qu
**arXiv:** [arxiv.org/abs/2609.23377](https://arxiv.org/abs/2609.23377)
**Summary:** This framework trains category-specific software-engineering experts with iterative reinforcement learning and self-generated repair trajectories, then consolidates them through label-routed on-policy distillation. The final policy reached 58.04% mean resolution on Pro-618 and 59.00% on SWE-bench Multilingual, improving on the base model by 5.39 and 2.78 percentage points.

---

### 12. Harness-Zero: Harness Distillation via Agent-as-Harness
**Authors:** Haoran Ye, Yuxing Lu, Haonan Dong, Zhaochen Su, Guojie Song
**arXiv:** [arxiv.org/abs/2609.24974](https://arxiv.org/abs/2609.24974)
**Summary:** Harness-Zero uses an optimized harness to guide a harnessing agent that corrects student responses in the target harness's action space, creating demonstrations that internalize harness-induced behavior. After the specialized harness was removed, task success rose from 23.3% to 44.3%, exceeding the 41.7% achieved with that harness attached and recovering 82.3% of 28 behavior patterns.

---

### 13. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents
**Authors:** Dongming Jiang, Yi Li, Bingzhe Li
**arXiv:** [arxiv.org/abs/2609.23986](https://arxiv.org/abs/2609.23986)
**Summary:** Jev-Mem separates fast memory control from slower reasoning through a System-One controller, a multi-relational memory plane, and a System-Two reasoning plane. On LoCoMo it scored 0.777, improved 11.0% over the strongest baseline, built memory in 158 seconds at a 6.6-times speedup, and reduced average query latency to 0.93 seconds.

---

### 14. Deep Persona: A Psychologically Grounded Architecture and Evaluation Framework for Role-Playing Agents and Simulations
**Authors:** Rotem Dror, Zohar Elyoseph, Yuval Haber, Elad Refoua, Oshrat Ayalon, Adir Solomon
**arXiv:** [arxiv.org/abs/2609.22255](https://arxiv.org/abs/2609.22255)
**Summary:** Deep Persona organizes role-playing agents into three psychological layers covering observable expression, latent beliefs, and core motivational drives under scripted determinism and bounded agency. Its reference-free evaluation found high pragmatic fluency but systematic limits in emotional expression and joint attention, while case studies showed closer alignment with human conversational behavior.

---

### 15. Realtime-Venus: A full-duplex interaction system with asynchronous delegation
**Authors:** Ruixiang Zhao, Hualei Wang, Renhe Sun, Enzhi Zhou, Jincenzi Wu, Xujie Song, Kexin Shi, Zihang Liu, Pengcheng Zhu, Jiayi Zhou, Baoyue Zhang, Changhao Zhang, Zitong Wang, Jinhong Wang, Tong Niu, Jingjing Liu, Junan Lin, Haolin He, Hengshuo Chu, Yuhui Chen, Jian Liu, Yuge Huang, Junliang Xing, Yuntao Wang, Weiqiang Wang, Chun Yu, Yuanchun Shi
**arXiv:** [arxiv.org/abs/2609.13814](https://arxiv.org/abs/2609.13814)
**Summary:** Realtime-Venus uses separate 9B audio-visual and audio models as full-duplex conversational frontends, with a dual-loop runtime that continues interaction while a harness performs background reasoning and tool execution. Its audio-visual model led six of eight evaluated video benchmarks, while its audio model handled 75% of interruptions and exceeded Gemini 3.1 Live and GPT-4o on three continuation metrics.

---

### 16. CARE: Experience-Guided Atomic Corrective Execution for Vision-Language-Action Policies
**Authors:** Junlan Xiao, Junwei Jiang, Zaibin Zhang, Yifan Wang, Zhongbo Zhang, Huchuan Lu, Lijun Wang
**arXiv:** [arxiv.org/abs/2609.24118](https://arxiv.org/abs/2609.24118)
**Summary:** CARE learns stage-conditioned failure distributions from failed robot rollouts, synthesizes representative failure states and corrections, and uses 3D monitoring to trigger atomic recovery actions at inference. Across multiple VLA backbones and tasks, it improved average task success by 14.5 points in simulation and 15.9 points in real-world dual-arm settings.

---

### 17. Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention Mechanisms
**Authors:** Yueyan Li, Haibo Wang, Caixia Yuan, Xiaojie Wang
**arXiv:** [arxiv.org/abs/2609.23658](https://arxiv.org/abs/2609.23658)
**Summary:** An interpretability study links motion planning in video diffusion models to specific attention heads and finds that rotary position embeddings cause excessive spatial attention decay and premature trajectory locking. Scaling rotary frequencies across denoising steps improved physical commonsense in both training-free and training-based experiments.

---

### 18. Gricea: An Open Science Platform for Conversational AI Research
**Authors:** Nikhil Sharma, Yunlin Gong, Xinyang Cheng, Ziang Xiao
**arXiv:** [arxiv.org/abs/2609.22039](https://arxiv.org/abs/2609.22039)
**Summary:** Gricea represents conversational-AI studies as configurable and deployable artifacts that researchers can run, inspect, share, and reuse. A replication study reproduced configurations for 93% of eligible CUI 2026 papers while identifying missing information that hindered faithful replication in 96% of papers.

---

### 19. 1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation
**Authors:** Huanxin Sheng, Zhiling Ye, Haonan Wang, Jian Wang, Jinjie Gu, Jian Kang
**arXiv:** [arxiv.org/abs/2609.24432](https://arxiv.org/abs/2609.24432)
**Summary:** This work introduces an information-efficiency ratio that balances gradient signal and noise when selecting sparsely supervised tokens for on-policy distillation. On mathematical and medical reasoning tasks, adding the ratio improved existing selectors, with 0.1% to 1% token budgets matching or exceeding full on-policy distillation.

---

### 20. CADWorld: Computer-Use Benchmark for Long-Horizon Computer-Aided Design
**Authors:** Zihan Dong, Yuanzhe Liu, Zhiyuan Ma, Qishi Zhan, Dehan Kong, Guohao Li, Kaixin Li
**arXiv:** [arxiv.org/abs/2609.16251](https://arxiv.org/abs/2609.16251)
**Summary:** CADWorld contains 200 long-horizon FreeCAD tasks across 11 mechanical-design categories, with executable checks over persistent native artifacts and engineering state. The strongest of seven evaluated agents achieved 17.5% success versus an 87.0% expert pass rate, exposing failures in structural, geometric, and construction-process requirements.

---
