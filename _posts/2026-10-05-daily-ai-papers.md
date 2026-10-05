---
title: "Daily AI Papers — October 05, 2026"
date: 2026-10-05
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-05/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - robot-learning
  - world-models
  - llm-reasoning
---

### 1. Does Learning Protein Folding Generalize to Broader Reasoning?
**Authors:** Yong Liu, Zhanpeng Shi, Yizhou Dang, Zhongyue Zhang, Xiaoliang Shi, Zhijian Wei, Shuangjia Zheng
**arXiv:** [arxiv.org/abs/2609.38879](https://arxiv.org/abs/2609.38879)
**Summary:** FoldingCorpus turns solved protein structures into exactly checkable spatial and topological questions, while Fold2Reason post-trains a shared representation with both discrete structural answers and continuous 3D geometry. The method scores 2.7 to 3.5 times Qwen3.5-9B on FoldBench and raises macro-average accuracy from 45.09% to 48.33% across ten broader reasoning benchmarks.

---

### 2. FrameMorrow: Future-guided Frame Selection with Prospective Tokens for Long-Horizon Video Generation
**Authors:** Bo Yin, Xiaobin Hu, Jiaqi Zhao, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2609.38839](https://arxiv.org/abs/2609.38839)
**Summary:** FrameMorrow predicts compact prospective tokens that describe future information needs, then uses them to select explicit historical frames for long-horizon video generation. Across five benchmarks and 11 generators, the plug-and-play selector consistently improves long-range consistency, visual quality, and action alignment with little extra inference cost.

---

### 3. MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation
**Authors:** Bingxuan Li, Siqi Song, Yizhuo Wu, Jiarui Yao, Tong Zhang, Huan Zhang
**arXiv:** [arxiv.org/abs/2609.38078](https://arxiv.org/abs/2609.38078)
**Summary:** MotorMind connects a general-purpose vision-language model's mid-level actions to deterministic robot control, asynchronous monitoring, and continuously updated memory without task-specific policy training or external grounding tools. It reaches 66.7% base and 53.8% perturbed success on LIBERO-PRO, plus 95% average success on a real xArm6 robot.

---

### 4. Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite
**Authors:** Zongxia Li, Yucheng Shi, Zhongzhi Li, Junyao Yang, Ruhan Wang, Chengsong Huang, Fuxiao Liu, Haitao Mi, Jordan Boyd-Graber, LeoweiLiang
**arXiv:** [arxiv.org/abs/2610.02826](https://arxiv.org/abs/2610.02826)
**Summary:** Recursive Self-Rewrite uses a planner, leakage-aware critic, and sandboxed executor to reconstruct solutions found under specialized harnesses as reusable trajectories for a general harness. It expands 2,001 source successes into 11,094 training trajectories and substantially improves Qwen-3.8-27B across multiple terminal-task benchmarks.

---

### 5. World Action Modeling with Progressive Visual Planning
**Authors:** Fei Zhang, Zhaochong An, Duncan Frost, Yikai Wang, Pengfei Liu, Ya Zhang, Michal Drozdzal, Amir Bar
**arXiv:** [arxiv.org/abs/2610.02508](https://arxiv.org/abs/2610.02508)
**Summary:** ProWAM jointly predicts robot actions and an ordered sequence of sparse visual subgoals, giving closed-loop control explicit progress anchors without generating dense video rollouts. It sets new state-of-the-art results on LIBERO-Plus and randomized RoboTwin and reaches 70.0% success in zero-shot real-world experiments.

---

### 6. Native Action-Prior Learning from Videos for World Action Models
**Authors:** Zhaochong An, Fei Zhang, Menglin Jia, Duncan Frost, Zijian Zhou, Yikai Wang, Xudong Wang, Aditya Patel, Belinda Zeng, Tao Xiang, Serge Belongie, Amir Bar, Sen He
**arXiv:** [arxiv.org/abs/2610.03391](https://arxiv.org/abs/2610.03391)
**Summary:** NAVA-WAM directly pretrains an action policy from observation-only videos by propagating future-video supervision through transition-structured attention, then post-trains with labeled demonstrations. The approach consistently improves in- and out-of-distribution control, action-label efficiency, and real-robot generalization without a separate latent-action model.

---

### 7. On-Policy Parameter Update Direction Underlies Generalization in LLM Post-Training
**Authors:** Shufan Shen, Zhongni Hou, Junshu Sun, Yufei Zhang, Wei Lin, Guojun Yin, Qingming Huang, Shuhui Wang
**arXiv:** [arxiv.org/abs/2609.36659](https://arxiv.org/abs/2609.36659)
**Summary:** The authors find that on-policy post-training continually changes cumulative parameter-update directions, unlike the more consistent directions produced by supervised fine-tuning. Their OPSFT method identifies an on-policy direction in a few steps and constrains later SFT updates to it, transferring stronger generalization while preserving SFT efficiency and use of high-quality trajectories.

---

### 8. SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation
**Authors:** Ruiqi Zhang, Jiahao Wang, Mingxuan Li, Haichen Luo, Chaoting Wang, Guoyu Mou, Keyu Lai, Hanchao Lv, Jiaxu Wang, Yibo Zheng, Aijun Yang, Xiaohua Wang
**arXiv:** [arxiv.org/abs/2610.02304](https://arxiv.org/abs/2610.02304)
**Summary:** SimuVerity provides 101 text-to-executable Simulink tasks across ten engineering domains and evaluates qualified models on six dimensions beyond compilation or structural similarity. The best of six tested agent systems scores only 42.86, exposing major gaps in executable implementation, multidimensional engineering correctness, and model layout.

---

### 9. Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models
**Authors:** Seo Hyun Kim, Sunwoo Hong, Younwoo Choi, Chen-Hao Chao, Se-Young Yun, Rahul G. Krishnan
**arXiv:** [arxiv.org/abs/2610.03665](https://arxiv.org/abs/2610.03665)
**Summary:** Pivot-SD identifies high-impact token commitments in masked diffusion language-model denoising by measuring how much they reduce uncertainty over the remaining masked positions. Training successful pivots with cross-entropy and failed pivots with targeted unlikelihood beats full-sequence SFT and budget-matched diffusion RL using only 200 questions and four rollouts each.

---

### 10. PDE-JEPA: Predictive Representation Learning of Latent Dynamics Modeling for Parametric PDEs
**Authors:** Zhentao Tan, Jianrong Zhang, Ruijie Quan, Yi Yang
**arXiv:** [arxiv.org/abs/2609.34715](https://arxiv.org/abs/2609.34715)
**Summary:** PDE-JEPA combines masked latent prediction, a geometry projector aligned to physical-field evolution, and a physics-structured predictor for parametric PDE dynamics. Across nine benchmarks it improves on prior state of the art by 33.4% in-distribution and 51.4% when extrapolating to unseen governing parameters.

---

### 11. HyperBrowseComp: A Multilingual and Multimodal Stress Test for Web-Browsing Agents
**Authors:** Alham Fikri Aji, Faiz Rizki Ramadhan, Zayd M. K. Zuhri, Seung Hun Eddie Han, Ryandito Diandaru, Qinrong Cui, Jan Christian Blaise Cruz, Badrinath Chandana, Peerawat Chomphooyod, Ahmed Attia, Jonibek Mansurov, Emilio Villa-Cueva, Canh Duong Nguyen, Imran Turganov, Minghao Wu, Peerat Limkonchotiwat, Irina Nikishina
**arXiv:** [arxiv.org/abs/2610.03574](https://arxiv.org/abs/2610.03574)
**Summary:** HyperBrowseComp contains 423 human-validated questions in 13 languages that require agents to follow obscure multi-step clues across text, video, scans, images, and maps. Its shared protocol and human evaluation create a demanding test of persistent multilingual, multimodal evidence discovery rather than answers recoverable from model memory alone.

---

### 12. Science or Slop?: Benchmarking and Mitigating Scientific Slop in AI-Generated Papers
**Authors:** Yerim Oh, Young-Jun Lee, Jaewoo Ahn, Gunhee Kim, Dongyeop Kang
**arXiv:** [arxiv.org/abs/2610.00531](https://arxiv.org/abs/2610.00531)
**Summary:** SciSlopBench pairs 390 AI-generated scientific papers with matched human papers and measures failures in structure, argument, and artifacts, identifying the AI paper with 85.9% accuracy. The evidence-grounded SciSlopHarness reduces the remaining AI-human gap by 63% over the strongest revision baseline without human reference targets.

---

### 13. World Embedding Benchmark
**Authors:** Yiqi Liu, Ruifeng Yuan, Yang Wang, Long Li, Fengyu Cai, Hou Pong Chan, Jialin Yu, Hao Zhang, Chenghua Lin, Chenghao Xiao
**arXiv:** [arxiv.org/abs/2610.03632](https://arxiv.org/abs/2610.03632)
**Summary:** The World Embedding Benchmark uses 8,000 controlled simulations from 80 physical-system families to test retrieval, physical-property regression, and video-description matching. Current omnimodal embeddings show weak physical alignment despite retaining probeable quantitative information, while physics-aware retrieval improves the fidelity of generated videos.

---

### 14. Source Preference in the Wild: How LLM Agents Favor Items by Source, and How to Reduce It
**Authors:** Jonghyun Song, Haewon Park, Jeonghoon Shim, Woojung Song, Yohan Jo
**arXiv:** [arxiv.org/abs/2610.03195](https://arxiv.org/abs/2610.03195)
**Summary:** Across 12 agent models and three domains, the study finds systematic source preferences that can outweigh whether an item better satisfies a user's requirements. Hiding or relabeling source identity changes selections, while supplying missing information or explicitly countering source preconceptions reduces the bias.

---

### 15. LexReward: A Taxonomy-Driven Reward Framework for Legal Language Models
**Authors:** Yida Cai, Xin Dai, Bingxiang He, Huiyuan Xie, Yuxiao Ye, Zhenghao Liu, Yang Bai, Zhiyuan Liu
**arXiv:** [arxiv.org/abs/2609.39071](https://arxiv.org/abs/2609.39071)
**Summary:** LexReward evaluates legal responses with interpretable rubrics spanning Style, legal Elements, and the completeness and correctness of the reasoning Chain. Rubric-derived preference data improves all three dimensions through DPO, and dimension-specific LexRM reward models support effective reinforcement learning without reference answers at reward time.

---

### 16. Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory
**Authors:** Ying Yang, Guiyu Zhang, Lianghua Huang, Chang Nie, Chenyang Si, Haofan Wang, Shaoshuai Shi, Li Jiang
**arXiv:** [arxiv.org/abs/2610.02521](https://arxiv.org/abs/2610.02521)
**Summary:** Spatial Memory Intelligence uses a multimodal understanding model to manage long-term world-model memory through spatial clustering, within-cluster sparsification, action-aware retrieval, and reliability-aware filtering. Across multiple baselines, benchmarks, and backbones, it improves memory sparsity, generation stability, and spatial consistency.

---

### 17. Science Utopia? Closed-Loop LLM Simulation of Academic Research Ecosystems
**Authors:** Yiqiao Jin, Yiyang Wang, Lucheng Fu, Bing He, Siheng Xiong, Yijia Xiao, B. Aditya Prakash, Josiah Hester, Srijan Kumar, James Evans, Jindong Wang
**arXiv:** [arxiv.org/abs/2610.01257](https://arxiv.org/abs/2610.01257)
**Summary:** SciUtopia is a persistent closed-loop simulation of research direction choice, collaboration, submission, review, citation, funding, and attrition across evolving academic ecosystems. In 61 worlds with over 40,000 simulated researchers, it reveals how resubmission raises reviewer burden, cautious exploration balances impact and diversity, and resource inequality can emerge without narrow early-funding advantage.

---

### 18. Multilingual GSM-Symbolic: What determines capability transfer across languages?
**Authors:** Kenneth Enevoldsen, Riley Herchert, Sofie Mosegaard, Dan Saattrup Smart, Simon Enni, Isaac Chung, Sofie Bruun, Ayush Sunil Munot, Max Müller-Eberstein, Adnan El-Assadi, Elisa Bassignana, Gianluca Barmina, Hafsteinn Einarsson, Iben Nyholm Debess, Linda Freienthal, Lukas Galke Poech, Mike Zhang, Nicolas Legrand, Vladimir Salnikov, Yevhen Kostiuk, Zafar Hussain, Sagandeep Kaur, Agnes Toftgård, Marie Mattson, Kristoffer Nielbo
**arXiv:** [arxiv.org/abs/2610.03367](https://arxiv.org/abs/2610.03367)
**Summary:** Multilingual GSM-Symbolic provides 30,000 item-matched math questions across 15 languages, with symbolic templates that generate fresh variations and reduce saturation. Its analysis attributes most cross-language capability differences to model size, language resource level, reasoning, and typological distance, explaining 92% of between-language variation.

---

### 19. DEFINE: Exemplar-Guided Accent Control for Zero-Shot TTS
**Authors:** Ambuj Mehrish, Abhinaba Roy, Alex Ivanov, Tawsif Ahmed, Dorien Herremans
**arXiv:** [arxiv.org/abs/2609.32777](https://arxiv.org/abs/2609.32777)
**Summary:** DEFINE separates speaker identity and target accent into distinct audio exemplars and uses one inference-time guidance weight to control accent strength in zero-shot text-to-speech. A single LoRA-adapted F5-TTS model generalizes accent control beyond its training set while matching a two-model cascade on supported accents with better speaker similarity.

---

### 20. VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks
**Authors:** Caiqi Zhang, Rujun Han, Zifeng Wang, Zoey CuiZhu, Nigel Collier, Tomas Pfister, Chen-Yu Lee
**arXiv:** [arxiv.org/abs/2610.00972](https://arxiv.org/abs/2610.00972)
**Summary:** VeriHarness turns the generator's base LLM into an evidence-seeking verifier whose disagreement resolver checks competing claims and whose consensus challenger probes shared claims and omissions. Across five long-horizon benchmarks it leads tested selection baselines, with evidence-backed revision improving over one rollout by 6.2 points for Gemini 3.5 Flash and 6.4 for Claude Opus 4.8.
