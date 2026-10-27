---
title: "Daily AI Papers — October 27, 2026"
date: 2026-10-27
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-27/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - multimodal-generation
  - reinforcement-learning
---

### 1. Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents
**Authors:** Yihao Hu, Zhihao Wen, Yitong Lin, Siyuan Lu, Pan Wang, Wei Wu, Jiang-Ming Yang, Tao Lin
**arXiv:** [arxiv.org/abs/2610.33568](https://arxiv.org/abs/2610.33568)
**Summary:** Trajectory2Gym constructs executable tool-use interactions that cover compositional dependencies and supervises only decisions justified by the agent-visible history. Across five Qwen3 scales, it improves Tau1, Tau2, and BFCL at every tested scale, raising the equal-weight three-benchmark mean by 16.9-29.8 percentage points.

---

### 2. StreamVibe: Proactive Video Agents for Evolving User Intent
**Authors:** Chengzhi Liu, Yuxiang Lai, Yuzhe Yang, Yanqing Liu, Jiheng Hou, Yue Cao, Haonan Wang, Ruixi Fan, Lan Wang, Sheng Liu, Songyou Peng, Yale Song, Kevin Qinghong Lin, Xin Eric Wang, Jui-Hsin Lai, Youbao Tang
**arXiv:** [arxiv.org/abs/2610.34662](https://arxiv.org/abs/2610.34662)
**Summary:** StreamVibe combines an intent-focused video benchmark, a proactive streaming model, and a hierarchical-memory harness that tracks explicit, implicit, and evolving user intents. The paper reports a 10.7% improvement in response timing and answer quality for StreamVibe-VL and a further 12.3% gain in proactive interaction with its harness.

---

### 3. DynaFlow: Learning Free-Form Multi-Agent Orchestration
**Authors:** Ruhao Liu, Qi Li, Shizun Wang, Xinchao Wang
**arXiv:** [arxiv.org/abs/2610.34467](https://arxiv.org/abs/2610.34467)
**Summary:** DynaFlow lets a main agent synthesize executable, task-specific multi-agent workflows with sequential or parallel coordination, information exchange, and verification while keeping sub-agents fixed. Across six benchmarks, it reaches 88.08% overall accuracy in Forced mode, exceeding the strongest evaluated baseline by 10.90 percentage points with the same Qwen3.5-27B backbone.

---

### 4. Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution
**Authors:** Zhiyong Cao, Hengjie Zhu, Yongxin Wang, Xuchen Li, Jintao Li, Shuxia Liu, Dunqiang Liu, Bo Wang, Kairan Zhang, Cong Lin, JiangDi Yu, Siyuan Liu, Sijia Yao, Yi-Liang Wei, Lingxu Ma, Aijia Wang, Anxin Chen, Zixian Wei, Xiang Ruan, Ruizhi Xu, Ruqian Shi, Baihua Xiao, Sicheng Zhou
**arXiv:** [arxiv.org/abs/2610.32285](https://arxiv.org/abs/2610.32285)
**Summary:** TraceTrial-Bench evaluates seven components of agent-harness reliability using 95 expert-level tasks, execution tracing, evidence acquisition, and mechanism-based failure attribution. Across 3,420 runs covering four harnesses and nine models, harness scores range from 59.8% to 72.0%, and 31.1% of runs succeed at the task while failing at least one harness criterion.

---

### 5. InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants
**Authors:** Qinsi Wang, Wei Wen, Chong Zhou, Saksham Suri, Zechun Liu, Lemeng Wu, Hai Helen Li, Yiran Chen, Raghuraman Krishnamoorthi, Qi Qian
**arXiv:** [arxiv.org/abs/2610.33966](https://arxiv.org/abs/2610.33966)
**Summary:** InteractiveWorld provides a verifiable closed-loop environment in which an egocentric multimodal assistant guides an independently acting human agent, with InteractiveBench covering 120 multi-turn tasks across six categories. Tests of 12 frontier models reveal substantial reliability gaps, with the strongest evaluated model achieving at most 20% on long-horizon Guidance and 25% on Planning tasks.

---

### 6. Work Agents: Systems, Capabilities, and Optimization
**Authors:** Zishan Xu, Enjun Du, Mingqi Gao, Cheng Yang, Junhao Shen, Zirong Chen, Zhiyuan Yao, Yifu Guo, Yuquan Lu, Jinyang Huang, Zhengxi Lu, Siyi Liu, Ziyu Zheng, Yongqi Zhang, Difan Zou, Weiwen Liu
**arXiv:** [arxiv.org/abs/2610.35845](https://arxiv.org/abs/2610.35845)
**Summary:** This survey frames work agents as foundation models plus runtime harnesses that execute delegated tasks in stateful workspaces and deliver verifiable outcomes. It organizes working conditions through persistence and openness, identifies five core capability families, and reviews model, harness, joint optimization, and work-outcome evaluation.

---

### 7. WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control
**Authors:** Lei Cao, Yu Liu, Wenhua Liao, Peng Zhang, Fei Wang, Hao Zhang, Jiajun Le, Daiguo Zhou, Jian Luan, Jiayi Ma
**arXiv:** [arxiv.org/abs/2610.33135](https://arxiv.org/abs/2610.33135)
**Summary:** WorldCast uses depth-based 3D geometric guidance and Geometry-Aligned Memory Attention to preserve character geometry, appearance, and identity during large-angle camera motion. Its CLACT dataset and benchmark provide accurate camera geometry and multi-view character observations, supporting evaluation of trajectory following and world-consistent video generation.

---

### 8. Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents
**Authors:** Haoyu Zhao, Sitian Tu, Yuxuan Huang, Huichi Zhou, Zhangyue Yin, Jiahao Huang, Jingyuan Xu, Tianmiao Shi, Jin Shi, Nianxi Zhang, Yangmiao Zhang, Zhuolang Chan, Huiyan Hu, Chenchao Sheng, Yaqing Luo, Yue Chen, Huaxiu Yao, Meng Fang, Jun Wang
**arXiv:** [arxiv.org/abs/2610.33956](https://arxiv.org/abs/2610.33956)
**Summary:** Continual Learning Exam measures experience-driven agent improvement through 120 human-authored tasks arranged into 600 progressively unlocked levels spanning 89 professional roles. Across 17 harness-model configurations, diagnostic feedback and one revision yield a median 5.3-point completion gain, yet the best system clears only 47.7% of levels and completes every level in 23.3% of tasks.

---

### 9. Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion
**Authors:** Kam Man Wu, Yu Zhang, Pengjun Fang, Mingfei Chen, Weijia Chen, Zeyue Tian, Qifeng Chen
**arXiv:** [arxiv.org/abs/2610.34415](https://arxiv.org/abs/2610.34415)
**Summary:** AMBIT unifies First-Order Ambisonics generation and editing through executable ScenePlans, a shared planning-and-rendering Transfusion backbone, and a spatially aware continuous VAE. Joint on-policy self-distillation improves content and spatial quality, instruction-guided editing fidelity, and preservation of unchanged sources across speech, music, and sound evaluations.

---

### 10. AV-FABLE: Audio-Visual Manipulation Forensics in Long-Form Videos
**Authors:** Yuesheng Huang, Hoi Fan Au, Jiaqi Hou, Ruicheng Zhang, Jiarui He, Haocheng Yang, Bin Hu, Kewei Zhang, Weijian Deng, Jun Zhou, Xiu Li
**arXiv:** [arxiv.org/abs/2610.33413](https://arxiv.org/abs/2610.33413)
**Summary:** AV-FABLE benchmarks sparse audio and visual manipulations in long-form videos using 16,650 pristine-manipulated twin pairs totaling 998 hours and separate modality timelines. Although zero-shot audio-visual language-model prompting performs near chance, NFSR decodes frozen perception features with separate temporal readouts and achieves the best localization results in-domain and across three out-of-distribution settings.

---

### 11. Eat Your Precision: Precision Objective Mitigates Reward Hacking in Rubric-based RL
**Authors:** Hyun Ryu, Jong-Heon Kim, Yiqing Xie, Seungone Kim, Carolyn Rose, Eunho Yang
**arXiv:** [arxiv.org/abs/2610.33512](https://arxiv.org/abs/2610.33512)
**Summary:** FORK augments recall-oriented rubric rewards with a precision objective requiring response units to be both necessary and factually correct. It reduces verbosity while preserving similar rubric coverage, raising win rates against the base policy from 10.6% to 68.0% on RubricHub-Medical and from 22.1% to 74.1% on HealthBench.

---

### 12. Δτ-Bench: Pushing Agents Toward a Moving Capability
**Authors:** Shuofei Qiao, Xuanguang Pan, Yijun Chen, Wendi Feng, Bin Wu, Runnan Fang, Yuqi Zhu, Shumin Deng, Emine Yilmaz
**arXiv:** [arxiv.org/abs/2610.34238](https://arxiv.org/abs/2610.34238)
**Summary:** Δτ-Bench evaluates agent adaptation across six evolving tool ecosystems using 1,588 validated multi-turn tasks in 42 domains, where familiar services can disappear or more efficient alternatives emerge. The strongest evaluated model or harness reaches only 42.3% task success, while the proposed Steward manager improves adaptation through incremental skill maintenance and dynamic tool provisioning.

---

### 13. Principia: Test-Time Hypotheses to Principle Construction for Scientific Discovery
**Authors:** Dongki Kim, Sangwoo Park, Jinheon Baek, Soyeong Jeong, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2610.32195](https://arxiv.org/abs/2610.32195)
**Summary:** Principia constructs comparative causal hypotheses from observed outcomes, synthesizes recurring relationships into inductive principles, and revises that knowledge throughout test-time scientific discovery. It outperforms evaluated baselines across molecular optimization, protein engineering, gene perturbation, and molecular property prediction while producing principles consistent with the scientific literature.

---

### 14. Qwen-Image-PE: Learning Visual Design for Text-to-Image Prompt Enhancement
**Authors:** Zekai Zhang, Yanran Zhang, Shengming Yin, Yan Shu, Zhening Liu, Bingxuan Zhao, Chenyang Zhu, Donghao Zhou, Jiahao Li, Jiahao Wang, Jie Zhang, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Qihang Ai, Rui Song, Shuo Cao, Xiao Xu, Xiaoyue Chen, Yuxiang Chen, Zhendong Wang, Zhouyang Li, Zihao Liu, Zikai Zhou, Bo Zheng, Huishuai Zhang, Dongyan Zhao, Chenfei Wu
**arXiv:** [arxiv.org/abs/2610.33472](https://arxiv.org/abs/2610.33472)
**Summary:** Qwen-Image-PE learns fine-grained visual design through caption-based reverse-distillation supervised training followed by groupwise design rewards for lighting, composition, layout, and detail. Its 397B model improves Qwen-Image-Bench by 7.81 points over original requests, while the 9B model outperforms evaluated prompt-enhancement baselines and transfers to additional image-generation backbones.

---

### 15. HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction
**Authors:** Zunnan Xu, Shangchen Zhou, Yihang Luo, Chen Change Loy
**arXiv:** [arxiv.org/abs/2610.31635](https://arxiv.org/abs/2610.31635)
**Summary:** HiP3R reconciles overlapping long-video reconstructions through a hierarchical pose graph that first fixes global layout and scale with chunk-level Sim(3) optimization, then estimates one shared SE(3) camera per frame. It improves camera trajectories and 3D reconstruction across multiple benchmarks and applies to chunk-based or streaming backends without extra training or fine-tuning.

---

### 16. World-in-Context: Interactive Video World Modeling with In-Context Conditioning
**Authors:** Harold Haodong Chen, Rui Peng, Rongjin Guo, Lingteng Qiu, Kejie Qiu, Chao Xu, Zilong Dong
**arXiv:** [arxiv.org/abs/2610.33169](https://arxiv.org/abs/2610.33169)
**Summary:** World-in-Context places explicit view, action, and camera-control tokens in shared self-attention and uses Interaction-Transport RoPE to preserve continuity across execution intervals. Its 5B model matches the navigation performance of 22B EchoWM on WBench and achieves 93.8% perspective-switching success, compared with 18.8% for existing 5B baselines.

---

### 17. Trustworthy Recursive Self-Improvement in the Era of Large Models: Foundation, Risks, Evaluation and Open Challenges
**Authors:** Jiayue Pu, Ang Gao, Jinyi Bai, Qipeng Wang, Tongyu Wen, Jiahao Zhao, Keyu Qu, Junhao Zhang, Chenglei Shen, Zhongxiang Sun, Jun Xu, Xiao Zhang
**arXiv:** [arxiv.org/abs/2610.35193](https://arxiv.org/abs/2610.35193)
**Summary:** This survey defines recursive self-improvement operationally and examines how persistent changes to models, prompts, memories, tools, workflows, and improvement mechanisms can undermine trustworthiness. It organizes risks, safeguards, and evaluation evidence around improvement validity, constraint preservation, and effective oversight, emphasizing independent and longitudinal assessment.

---

### 18. miniTE: Diagnosing and Bridging the Execution Gap in Native NVFP4 Reinforcement Learning
**Authors:** Zhen Li, Mingfa Feng, Yiming Zhang, Yang Yu, Changhai Zhou, Pengxiang Li, Dongkuan Wu, Congkai Xie, Hongxia Yang
**arXiv:** [arxiv.org/abs/2610.23928](https://arxiv.org/abs/2610.23928)
**Summary:** miniTE combines execution diagnostics, cross-engine numerical alignment, and native W4A4 GEMM to stabilize low-bit LLM reinforcement learning without changing the RL objective. Long-horizon Qwen3-30B-A3B experiments approach BF16 benchmark performance, while the optimized learner reaches 33,540 tokens per second on one NVIDIA B300 GPU node, 1.39 times BF16 throughput.

---

### 19. S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning
**Authors:** Shuo Shen, Guangran Cheng, Chengqi Lyu, Xiangsen Wang, Yanan Sun, Wenwei Zhang
**arXiv:** [arxiv.org/abs/2610.35518](https://arxiv.org/abs/2610.35518)
**Summary:** S3AC introduces a practical long-chain-of-thought critic-training recipe that provides token-specific advantages and prompt-specific baselines, together with difficulty-aware prompt selection before generation. It outperforms GRPO-X across dense and mixture-of-experts models from 1.5B to 397B parameters and sustains single-rollout training at 35B where tested critic-free baselines deteriorate.

---

### 20. ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning
**Authors:** Bowen Ding, Mingda Wan, Yuhan Chen, Jiyao Yuan, Qi Zhu, Futing Wang, Heyuan Deng, Fei Mi, Lifeng Shang, Tao Lin
**arXiv:** [arxiv.org/abs/2610.18683](https://arxiv.org/abs/2610.18683)
**Summary:** ProAS uses a dynamically evolving Agentic Reference Graph to mask unreasonable incentives and redistribute penalties, giving critic-free multi-turn RL finer-grained action credit. Across Qwen2.5-1.5B and 7B experiments, it reaches peak ALFWorld success rates of 91.9% and 94.3% and WebShop rates of 66.7% and 70.8%, while accelerating convergence by up to 2.44 times.
