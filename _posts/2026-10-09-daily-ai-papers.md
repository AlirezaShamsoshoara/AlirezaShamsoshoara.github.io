---
title: "Daily AI Papers — October 09, 2026"
date: 2026-10-09
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-09/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robotics
  - world-models
---

### 1. AgentGarten: Code Worlds for Evolving Agents
**Authors:** Jiawei Chi, Shangchen Miao, Zhiyuan Shi, Kailu Wu, Hanyang Wang, Weiliang Chen, Qiyu Dai, Jinshan Ren, Jun Gao, Mingsheng Long, Yueqi Duan, Jiangran Lyu, Jialong Wu, Fangfu Liu
**arXiv:** [arxiv.org/abs/2610.12374](https://arxiv.org/abs/2610.12374)
**Summary:** AgentGarten couples persistent simulator or game-engine state with a shared neural renderer to create realistic, real-time interactive worlds that agents can explore. Its Adversarial Forcing renderer and inherited playbooks let agents learn in four rounds, compared with millions of interactions for the conventional reinforcement-learning counterpart.

---

### 2. TokenRouter: Efficient Serving System for Token-Level LLM Routing
**Authors:** Tianyu Fu, Tengxuan Liu, Ruoxi Wang, Yixin Dong, Yi Ge, Yichen You, Yu Wang
**arXiv:** [arxiv.org/abs/2610.12242](https://arxiv.org/abs/2610.12242)
**Summary:** TokenRouter presents token-level LLM routing through a request-centric programming model backed by asynchronously dispatched per-model subservers. Its delayed-batching scheduler, tuned with a throughput model, delivers 2.01 to 64.15 times higher decoding throughput than existing systems across varied algorithms, workloads, and model pairs.

---

### 3. SuperNav: An Agentic Navigation System for Any Task in Any Scene
**Authors:** Jinkai Zhang, Jingyi Xu, Yuanhong Yu, Jiarui Guo, Ruizhen Hu, Hujun Bao, Xiaowei Zhou, Sida Peng
**arXiv:** [arxiv.org/abs/2610.12126](https://arxiv.org/abs/2610.12126)
**Summary:** SuperNav keeps a pretrained multimodal language model focused on interpreting requests and scenes while a specialized harness handles navigation skills, physical tools, and task progress. A visual-point interface connects decisions to motion, helping the system beat four baselines and transfer across HM3D environments and a real quadruped robot.

---

### 4. MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement
**Authors:** Core Team, Zongming Qiao, Ziyue Hua, Zirui Ou, Zihao Yue, Zihan Jiang, Zhuo Huang, Zhiyang Chen, Zhixian Zheng, Zhipeng Xu, Zhengrui Ma, Yuyang Hu, Yuhang Dong, Yuechen Zhang, Yudong Wang, Yuanxin Liu, Yixin Yang, Yishuo Cai, Yikai Zhao, Yihan Yan, Yifan Zhang, Yifan Song, Xiyu Wei, Xing Zhang, Xin Zhang, Xiaoqian Liu, Xiaodong Ji, Xiangwei Deng, Xueyu Guo, Wenhan Ma, Weimin Xiong, Weikun Wang, Weiji Zhuang, Shuo Liu, Shuhuai Ren, Shuhao Gu, Shimao Chen, Shijie Cao, Shihua Yu, Shicheng Li, Shengjie Zhou, Shaolei Zhang, Rang Li, Qiying Wang, Qingkai Fang, Qianli Chen, Minzheng Wang, Liwen Wang, Linli Yao, Linghao Zhang, Liangyu Cheng, Liang Zhao, Lei Li, Jinhao Dong, Jinyu Xiang, Jianyu Wei, Jiangshan Duo, Huaqiu Liu, Huanjie Fan, Hongyi Guan, Hongshen Xu, Hao Tian, Hanyu Li, Hailin Zhang, Gang Wang, Fuli Luo, Feng Wei, Dong Zhang, Dawei Zhu, Chiheng Lou, Chenhong He, Chenhao He, Chenghua Liu, Bowen Ye, Bowen Shen, Boshen Xu, Bo Yang, Bingquan Xia, Bangjun Xiao, Baixuan Xu, Zhouxiang Mao, Zhiyang Zhang, Zhixiang Xu, Zhenru Lin, Zhengju Tang, Zhaojun Huang, Yuzhe Weng, Yuxing Xiang, Yuxiao Li, Yuheng Yang, Yuhang Wang, Yuchen Liu, Yuanyuan Tian, Yuanliang Dong, Yu Cheng, Yongzhe He, Yongshun Liang, Yong Wang, Yiyan Wang, Yitian Gong, Yijie Zhang, Yanshu Xin, Xun Zhang, Xingjian Zhao, Wenyu Yang, Wenshan Huang, Wenhao Li, Tingwei Huang, Tianyu Yu, Tianyang Lu, Taoyu Yang, Sinan Du, Shutong Tian, Shulin Du, Shengfan Wang, Shanchuan Fang, Qihao Zhang, Qibin Yang, Qian Yu, Qian Tu, Pengrong Xie, Peipei Wang, Peidian Li, Minkun Guo, Mingchen Shao, Luohan Gao, Lijie Wang, Liang Shi, Kaiqi Chen, Kaiming Liu, Kaifei Wang, Kai Yang, Jinlong Xue, Jiechen Zhang, Jiaxuan Liu, Hongxu An, Hao Peng, Hanglong Lü, Guonan Wang, Feiyu Yang, Fanyu Cao, Fangyue Liu, Fan Cui, Cong Wang, Chun Chen, Chenxu Bai, Chengxuan Zhu, Chenghua Wang, Boyi Zeng
**arXiv:** [arxiv.org/abs/2610.11959](https://arxiv.org/abs/2610.11959)
**Summary:** MiMo-V2.6 scales agentic reinforcement learning through larger asynchronous batches, contexts up to one million tokens, diverse code, visual, general, and cyber environments, and more capable grading. The system freezes its mixture-of-experts router and adds defenses against reward hacking while releasing training dynamics, environments, and infrastructure for reproducible model self-improvement.

---

### 5. From Traces to Agentic Worlds: Agentic Language World Models for Interactive Environment Simulation
**Authors:** Quanyu Long, Xiao Chen, Jianda Chen, Haozhen Zhang, Qisheng Hu, Jianzhu Bao, Wenya Wang
**arXiv:** [arxiv.org/abs/2610.06100](https://arxiv.org/abs/2610.06100)
**Summary:** Trace2Env reconstructs historical interaction traces into a reusable worldbook of schemas, evidence, behavioral knowledge, and persistent episodic state, allowing an agent to simulate an unavailable environment. Across nine environments, it improves next-observation fidelity and long-horizon consistency, and actions learned in its simulations replay successfully in real systems more often.

---

### 6. In-context Robot Learning Made Simple: A Democratized Recipe for Manipulation Tasks
**Authors:** Minxing Li, Minghao Han, Weizhi Zhao, Hanwen Wang, Xiangshuo Liu, Shuyao Shang, Jingxiang Zhou, Mingchao Sun, Hongyu Pan, Mu Xu, Yu Liu, Lue Fan, Zhaoxiang Zhang
**arXiv:** [arxiv.org/abs/2609.38173](https://arxiv.org/abs/2609.38173)
**Summary:** SimpleICL clarifies what a robot should infer from visual demonstrations and pairs that definition with a minimal visual prompt encoder and inexpensive data-collection protocol. Without massive pretraining or specialized infrastructure, it achieves strong simulation and real-world manipulation results while exposing how robots discriminate actions, semantics, compositions, and affordances.

---

### 7. Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction
**Authors:** Dahyun Chung, Siyoon Jin, Hyunwook Choi, Honggyu An, Junyoung Seo, Hyunsung Kim, Seung Wook Kim, Seungryong Kim
**arXiv:** [arxiv.org/abs/2610.12299](https://arxiv.org/abs/2610.12299)
**Summary:** ME-World generates synchronized first-person streams for multiple agents by jointly denoising their views, conditioning on every agent's pose, and grounding them in shared environment memory. New shared-world metrics and experiments show better action control, identity preservation, video quality, and consistency of environments and interaction-driven updates.

---

### 8. DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training
**Authors:** Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang
**arXiv:** [arxiv.org/abs/2610.12468](https://arxiv.org/abs/2610.12468)
**Summary:** DreamTrue improves robot video prediction with geometric calibration that aligns action trajectories to images and counterfactual post-training that expands action and contact coverage. A human-trained embodied video reward model guides reinforcement learning, cutting the assessed interaction-defect rate on AgiBot from 48.12% to 6.25% while achieving state-of-the-art action following.

---

### 9. OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs
**Authors:** You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu
**arXiv:** [arxiv.org/abs/2610.12461](https://arxiv.org/abs/2610.12461)
**Summary:** OuroWorld turns static 3D Gaussian Splatting scenes into viewpoint-consistent 3D cinemagraphs with diverse motion that loops seamlessly. Its Fourier-based periodic deformation and drift correction handle imperfect multi-view supervision, outperforming baselines and winning 70.8% to 99.0% of user-study comparisons across 39 scenes.

---

### 10. Foundations of Large Language Models
**Authors:** Tong Xiao, Jingbo Zhu
**arXiv:** [arxiv.org/abs/2501.09223](https://arxiv.org/abs/2501.09223)
**Summary:** This book organizes the foundations of large language models into six chapters covering pretraining, generative models, prompting, alignment, inference, and reasoning. It targets students, NLP professionals, and practitioners who need a conceptual reference rather than an exhaustive catalog of frontier techniques.

---

### 11. Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?
**Authors:** Yibo Li, Jinhang Qiu, Zhi Zheng, Qianyun Guo, Jiaying Wu, Shuo Ji, Bryan Hooi
**arXiv:** [arxiv.org/abs/2610.08215](https://arxiv.org/abs/2610.08215)
**Summary:** Learn2Play Bench uses unfamiliar or counterintuitive text games to test whether agents actually learn from interaction instead of relying on pretrained knowledge of the rules. Experiments find that full experience records beat compressed strategies, humans explore more effectively than agents, and harness changes can improve scores while lowering estimated inference cost.

---

### 12. MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers
**Authors:** Jiarui Chen, Zeqiang Lai, Jiangshan Wang, Ziheng Ouyang, Ye Huang, Xiangyu Yue, Cewu Lu, Chunchao Guo
**arXiv:** [arxiv.org/abs/2610.06801](https://arxiv.org/abs/2610.06801)
**Summary:** MC-Sparse attributes quality loss in sparse diffusion-transformer attention to grouping constraints, selection errors, and discarded contributions, then caches exact-probability token choices and dense-to-sparse residuals across denoising steps. The training-free method stays close to dense outputs while speeding denoising by 1.80 times on Minimax-H3-Base and 2.32 times for 3D generation with negligible quality loss.

---

### 13. TestPrism: Rethinking Test Evaluation Beyond a Single Reference
**Authors:** Han Li, Lingxiang Hu, Jiacheng Huang, Ziqian Jiang, Jingkai Luo, Wei Gao, Yunfan Tan, Zun Wang, Jiaheng Liu
**arXiv:** [arxiv.org/abs/2610.12289](https://arxiv.org/abs/2610.12289)
**Summary:** TestPrism evaluates generated tests against many valid and invalid implementations rather than one reference, using 300 tasks, 3,000 candidate programs, and a strict Joint Success Function. Fourteen coding-agent configurations reach only 28.00% under that metric versus 59.67% with single-reference scoring, while the TestHelix synthesis and peer-validation method improves strict success by 8.67 to 9.00 points.

---

### 14. Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards
**Authors:** Yuanhao Ban, I-Hung Hsu, Anastasios Angelopoulos, Wei-Lin Chiang, Ion Stoica, Cho-Jui Hsieh
**arXiv:** [arxiv.org/abs/2610.02967](https://arxiv.org/abs/2610.02967)
**Summary:** This work post-trains text-to-image models by composing broad human-preference rewards with rubric rewards for prompt faithfulness and safeguards against reward hacking. Its composition strategy beats naive weighted averaging, raising Flux2dev by 69 Arena Elo points and taking post-trained Ideogram-4 to 1223.5 Elo on the reported leaderboard snapshot.

---

### 15. U-Space: Uncovering When and Why Uncertainty Arises in Language Models
**Authors:** Tobias Braun, Nils Loose, Alexander Herzog, Virginia Ceccatelli, Marcus Rohrbach, Thomas Eisenbarth, Lorenzo Cavallaro
**arXiv:** [arxiv.org/abs/2610.09087](https://arxiv.org/abs/2610.09087)
**Summary:** U-Space maps semantic directions for doubt and certainty into a low-dimensional residual-stream basis, producing token-level uncertainty traces through the U-Lens. It needs no correctness labels, repeated generations, or training, yet outperforms established baselines under standard and length-controlled reasoning evaluations and transfers more reliably than supervised estimators.

---

### 16. Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks
**Authors:** Haoyu Zhao, Zhengxu Yu, Zhiyuan He, Meng Fang, Rasul Tutunov, Haitham Bou-Ammar, Weilin Luo, Jun Wang
**arXiv:** [arxiv.org/abs/2610.11794](https://arxiv.org/abs/2610.11794)
**Summary:** Memento 3 lets a frozen LLM continually revise a natural-language rulebook, compile it into executable world-model code, and accept updates only after semantic and exact-replay verification. The single-model agent clears every level of all 25 public ARC-AGI-3 games with 100.0 mean relative human action efficiency and 44% of the human action count, while a learned Pong controller wins three games 21 to 0.

---

### 17. SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference
**Authors:** Qitong Wang, Xinwei Niu, Mingluo Su, Shanwei Zhao, Shiai Zhu, Huan Wang
**arXiv:** [arxiv.org/abs/2610.12327](https://arxiv.org/abs/2610.12327)
**Summary:** SparseDecoding calibrates pruning on activations from the model's own autoregressive decoding rather than natural-text inputs, removing a distribution mismatch that harms generated outputs. Its optimized N:M sparse matrix-vector kernel improves long-form accuracy over fixed-text calibration and provides up to 1.48 times end-to-end decoding speedup on A100 GPUs.

---

### 18. LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation
**Authors:** Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim
**arXiv:** [arxiv.org/abs/2610.12442](https://arxiv.org/abs/2610.12442)
**Summary:** LEGO replaces depth lifting and point-cloud reprojection with a learned transformer that directly synthesizes structurally aligned egocentric conditions from an exocentric video. Confidence-aware masking and diffusion guidance restore details in uncertain regions, outperforming the explicit state-of-the-art pipeline and generalizing to other datasets without retraining.

---

### 19. Reasoning-Informed Visual Editing
**Authors:** Xue Yang, Peiyuan Zhang, Yilun Zhu, Qihao Yang, Mingxin Liu, Xiangyu Zhao, Ziqian Fan, Zhaokai Wang, Yan Li, Yifan Yang, Xu Yang, Xiaosong Jia, Yue Zhou, Zhihang Zhong, Junchi Yan
**arXiv:** [arxiv.org/abs/2610.12343](https://arxiv.org/abs/2610.12343)
**Summary:** RISEBench++ evaluates reasoning-informed visual editing with 1,000 bilingual cases spanning six reasoning dimensions, 12 subcategories, 65 task types, and multi-image or multi-turn inputs. Its training-free RISE-Agent combines planning, tools, and verifier-guided refinement to beat most strong approaches, while the best evaluated editor still reaches only 56.6% accuracy.

---

### 20. OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video
**Authors:** Hongyu Li, Manyuan Zhang, Kaituo Feng, Shu Chen, Dian Zheng, Hao Li, Hao Yu, Zhangquan Chen, Zoey Guo, Ray Zhang, Shaofei Huang, Tianrui Hui, Linjiang Huang, Si Liu
**arXiv:** [arxiv.org/abs/2610.12419](https://arxiv.org/abs/2610.12419)
**Summary:** OneSearch-VL uses a Visually Grounded Evidence Graph to preserve links among visual anchors, entity relations, retrieved sources, and answer-producing operations across image and video research. VGEG-derived training data, rewards, and benchmarks lift the 8B model over Qwen3-VL-8B with tools by 20.2 and 17.6 points on its multi-image and video benchmarks and also improve seven image benchmarks plus VideoDR.

---
