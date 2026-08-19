---
title: "Daily AI Papers — August 19, 2026"
date: 2026-08-19
permalink: /blog/ai-papers/2026/08/daily-ai-papers-08-19/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-ai
  - evaluation-benchmarks
---

### 1. StateM: Reaching 95.3% Raw Accuracy, or a $15 Frontier Run, on Terminal-Bench 2.1 via Harness Scaling
**Authors:** Ziheng Qin, Yaxin Lu, Zhangyang Atlas Wang, Kai Wang
**arXiv:** [arxiv.org/abs/2608.15089](https://arxiv.org/abs/2608.15089)
**Summary:** Long-horizon agents can fail even when their underlying models can solve the constituent steps. They may lose track of mutable state, fail to reactivate lessons from earlier executions, skip known procedures, or stop prematurely.
**Trending because:** 284 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 2. Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements
**Authors:** Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, Wee Sun Lee
**arXiv:** [arxiv.org/abs/2608.17310](https://arxiv.org/abs/2608.17310)
**Summary:** Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branching interactions and sparse rewards, exposing several limitations of RL: its heavyweight backpropagation-based training stack makes it impractical to fine-tune larger LLMs, and longer-horizon trajectories make credit assignment in RL substantially harder.
**Trending because:** 89 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 3. Demystifying Agent Skills: Why They Work-Until They Don't
**Authors:** Zhiyuan Jiang, Fangrui Huang, Hanwen Xing, Xander Wu, Yipeng Gao, Rui Cao, Mengdi Wang, Shilong Liu, Yijiang Li
**arXiv:** [arxiv.org/abs/2608.14036](https://arxiv.org/abs/2608.14036)
**Summary:** Skills have emerged as a practical and effective approach for enhancing LLM agents at inference time through structured packages of knowledge. However, existing evaluations largely measure whether skills improve aggregated task success, leaving a more fundamental question underexplored: \textbf{When do skills help, why do they work, and where do they fail?} Through controlled experiments across various benchmarks, agent harnesses and LLMs, we isolate the effects of representation, outcome annotation, retrieval difficulty, and cross-framework robustness of skills.
**Trending because:** 82 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 4. ASI-Bench: At the Dawn of Artificial Superintelligence
**Authors:** Junwei Zhou, Zhen Sun, Binyu Li, Jiangyu Zhou, Yuexi Pan, Hengyu Wang, Honghe Ren, Xiaohan Jia, Xueyang Zhou, Xiaoyu Cao, Yongchao Chen, Yuanning Feng, Junhao Wu, Cheng Zhang, Sijia Chen, Haoyu Xue, Chengsong You, Huan Wang, Koutian Wu, Peigan Gao, Jiakun Wu, Wenzhe Li, Ergan Shang, Qingyuan Zheng, Jingjing Zhou, Ruixuan Jia, Yan Xu, Hongrui Zhang, Xiao-Han Ma, Zhengxiang Cheng, Yuexing Hao, Liting Mai, Xianglin Ji, Wenjun Zhang, Zhuofan Chen, Yixiao Huang, Chi Wang, Wenyue Hua, Yilun Hao, Yuantao Zhai, Ziyan Zhao, Jingyan Xie
**arXiv:** [arxiv.org/abs/2608.17271](https://arxiv.org/abs/2608.17271)
**Summary:** Artificial superintelligence (ASI) requires AI to move beyond mastering existing knowledge toward exploring the unknown, creating new knowledge, and turning new ideas into verifiable results. However, the capabilities of today's AI systems are still largely built on learning, compressing, and applying existing human knowledge.
**Trending because:** 51 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 5. Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation
**Authors:** Hongyan Feng, Sunlai Chen, Xuanyu Liu, Miao Pan, Yangfan Xie, Yuxiang Cui, Zhongxiang Zhou, Rong Xiong, Wenqi Zhang, Jianwei Yin, Yueting Zhuang, Xuhong Zhang
**arXiv:** [arxiv.org/abs/2608.17512](https://arxiv.org/abs/2608.17512)
**Summary:** Although Large Vision-Language Models (VLMs) have significantly advanced embodied navigation, their direct deployment remains challenging, as existing methods often force VLMs into unnatural action spaces that misalign with their 2D pre-training priors, compounded by rigid reasoning schedules and inefficient memory management. To overcome these limitations, we propose TAMP-Nav, a unified framework for efficient embodied navigation.
**Trending because:** 42 HuggingFace upvotes + addressing efficiency bottlenecks in real deployment

---

### 6. FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution
**Authors:** Shuo Yang, Xiaoze Fan, Melissa Pan, Haocheng Xi, Zhe Wang, Shanlin Sun, Kurt Keutzer, Song Han, Matei Zaharia, Chenfeng Xu, Ion Stoica
**arXiv:** [arxiv.org/abs/2608.16157](https://arxiv.org/abs/2608.16157)
**Summary:** Frontier open-weight models are increasingly available, but serving them still largely assumes datacenter infrastructure. We present FreeToken, an edge-native MoE serving system that treats a personal machine not as a small GPU, but as a unified, elastic inference platform.
**Trending because:** 41 HuggingFace upvotes + addressing efficiency bottlenecks in real deployment

---

### 7. EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing
**Authors:** Jiayi Song, Shijie Huang, Fangtai Wu, Yubo Huang, Zhenxiong Tan, Songhua Liu, Jiaming Liu, Ruihua Huang
**arXiv:** [arxiv.org/abs/2608.18063](https://arxiv.org/abs/2608.18063)
**Summary:** High-resolution image editing is increasingly demanded in professional workflows, yet existing diffusion-based models remain constrained to resolutions below 1K due to quadratic attention complexity and prohibitive memory requirements. A prevalent workaround employs a two-stage pipeline: editing at low resolution followed by independent super-resolution.
**Trending because:** 20 HuggingFace upvotes + riding strong momentum in generative vision research

---

### 8. HarmProfile: Characterizing Harmful Distributions in Frontier LLMs
**Authors:** Zhouyuan Ma, Yutao Wu, Hanxun Huang, Xiang Zheng, Xiao Liu, Yixin Cao, Zuxuan Wu, Xingjun Ma, Yu-Gang Jiang
**arXiv:** [arxiv.org/abs/2608.14577](https://arxiv.org/abs/2608.14577)
**Summary:** Frontier large language models (LLMs) safety evaluation has largely treated harmful generation as an attack outcome rather than as an object of analysis. Consequently, little is known about the harmful outputs produced during model misbehavior, partly because large-scale, high-quality collections of frontier-LLM misbehavior are difficult to obtain.
**Trending because:** 19 HuggingFace upvotes + resonating with current LLM research priorities

---

### 9. Agent Lightning v1.0: Towards Harnessed Agentic RL
**Authors:** Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo
**arXiv:** [arxiv.org/abs/2608.17528](https://arxiv.org/abs/2608.17528)
**Summary:** Modern agents operate inside agent harnesses that manage tools, context, and control flow, making the harness a critical part of the agent system. Our original Agent Lightning introduced a disaggregated architecture that connects arbitrary agents to RL training through an LLM endpoint proxy, an approach later adopted by frameworks such as verl Uni-Agent, AReaL 2.0, slime, and Polar.
**Trending because:** 15 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 10. V-RAE: Rethinking Video Latent Spaces for Generation
**Authors:** Minghui Guo, Shengqiong Wu, Hao Fei
**arXiv:** [arxiv.org/abs/2608.13556](https://arxiv.org/abs/2608.13556)
**Summary:** Latent video generation relies on autoencoders to define a compact space in which generative models operate. Although video autoencoder architectures have evolved substantially, their latent spaces are still optimized primarily for pixel-level reconstruction and provide limited high-level semantic organization.
**Trending because:** 15 HuggingFace upvotes + riding strong momentum in generative vision research

---

### 11. CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Guided Video Editing
**Authors:** Fuchen Long, Cong Wang, Zitao Gao, Wenhao Zhong, Yu Cheng, Xiaolu Hou, Yan Li, Xiao Cao, Xinlong Sun, Xi Chen, Yu Liu
**arXiv:** [arxiv.org/abs/2608.17566](https://arxiv.org/abs/2608.17566)
**Summary:** The quality and diversity of instruction-based video editing datasets are steadily improving, yet existing datasets mainly focus on single editing operations and fall short in supporting compositional instruction-guided video editing. In particular, multiple editing intents must be jointly understood and faithfully executed within the same video.
**Trending because:** 13 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 12. DiSCO: Defending text-to-image generation through distribution-guided contrastive prompt optimization
**Authors:** Tong Zhang, Motasem Alfarra, Carlos Hinojosa, Christos Louizos, Bernard Ghanem
**arXiv:** [arxiv.org/abs/2608.17067](https://arxiv.org/abs/2608.17067)
**Summary:** As text-to-image generative models advance, they raise critical safety concerns, particularly the generation of Not-Safe-For-Work (NSFW) content such as violence and nudity, further exacerbated by red-teaming adversarial attacks. Existing defenses predominantly operate under white-box assumptions, relying on text encoder optimization, weight editing, or inference-time intervention, and fundamentally cannot scale to proprietary models.
**Trending because:** 13 HuggingFace upvotes + riding strong momentum in generative vision research

---

### 13. Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents
**Authors:** Wei-Chieh Huang, Weizhi Zhang, Yuchen Wu, Yankai Chen, Eric Hanchen Jiang, Wooseong Yang, Yiwei Yang, Henry Peng Zou, Hanrong Zhang, Ying Nian Wu, Haolun Wu, Kai-Wei Chang, Philip S. Yu, Xue Liu, Aylin Caliskan
**arXiv:** [arxiv.org/abs/2608.15008](https://arxiv.org/abs/2608.15008)
**Summary:** Memory is becoming core infrastructure for long-horizon LLM agents, yet existing evaluations offer limited guidance on which memory substrate, namely the underlying medium in which memory is represented and stored, should be used under different operating regimes. We present a controlled harness evaluation of memory substrates for memory-augmented agents, covering dense and sparse indices, text records, structural stores, hierarchical stores, refinement-based memories, parametric updates, and activation-compatible context mechanisms.
**Trending because:** 11 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 14. From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation
**Authors:** Xingjian Wang, Zhao Wang, Taihang Hu, Jun Zheng, Qing Jin, Qinye Zhou, Zhengtao Wu, Yongchao Du, Zuan Gao, Chao Lin, Yefeng Shen, Xiaoli Xu, Zhengze Xu, Hao Yan, Yuhang Yu, Mingzhou Zhang, Mengting Chen
**arXiv:** [arxiv.org/abs/2608.18076](https://arxiv.org/abs/2608.18076)
**Summary:** Large-scale image generation has benefited from advances in data scale, quality, rebalancing, and recaptioning, yet conventional pipelines typically optimize task-specific datasets in isolation. A central challenge is not only how to curate each task-specific corpus, but also how to organize heterogeneous supervision according to the dependencies among generative capabilities.
**Trending because:** 9 HuggingFace upvotes + riding strong momentum in generative vision research

---

### 15. StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End Workflows
**Authors:** Liya Zhu, Xin Ma, Tao Liu, Haodong Wang, Ge Zhang, Jingzhe Ding, Qingshui Gu, Yongjie Zhong, Jinxiang Meng, Yuan Gao, Yunqiu Zhou, Hao Zhu, Jifeng He, Yongzhi Liao, Xinyi Zhang, Chaoxin Li, Yi Zhu, Xi Lin, Duju Zeng, Xiang Gao, Wen Zhang, Yunyang Wang, Duo Wang, Huan Zhou, Zuo Wang, Jin Chen, Kaiyuan Zhang, Chuqian Yu, Tianhao Yu, Longxiang Liu, Jianbo Xue, Huimin Che, Jiahao Wang, Yujia Qin, Jiaheng Liu, Shen Yan, Xiaolong Chang, Wenhao Huang
**arXiv:** [arxiv.org/abs/2608.17800](https://arxiv.org/abs/2608.17800)
**Summary:** Recent advances in Large Language Models(LLMs) and agents have substantially improved the ability of AI systems to execute complex tasks. Yet existing benchmarks largely rely on researcher-selected tasks, leaving uncertain whether such progress extends to the work that real-world users actually demand from AI systems.
**Trending because:** 8 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 16. Energy-Guided Flow Matching
**Authors:** Haoyang Tong, Yu He, Fang Li, Lichen Ma, Jingling Fu, Dong Chen, Zhen Chen, Junshi Huang, Jie Cao
**arXiv:** [arxiv.org/abs/2608.05811](https://arxiv.org/abs/2608.05811)
**Summary:** Pixel-space generative models bypass lossy latent compression, yet necessitate joint learning of global structure and fine-grained details in a high-dimensional space. Standard flow matching interpolates noise toward a fixed clean-image endpoint, leaving the spectral evolution to be learned implicitly.
**Trending because:** 8 HuggingFace upvotes + resonating with current LLM research priorities

---

### 17. HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety
**Authors:** Yajing Bai, Jinhao Duan, Jie Peng, Xianfeng Wu, Sijia Liu, Song Wang, Tianlong Chen
**arXiv:** [arxiv.org/abs/2608.17597](https://arxiv.org/abs/2608.17597)
**Summary:** Large language models are increasingly deployed through agent harnesses that manage tools, extensions, persistent state, permissions, and external actions. Existing safety benchmarks mainly target individual attack mechanisms or a limited subset of operational settings, making it difficult to compare how safety failures emerge across different harness responsibilities.
**Trending because:** 7 HuggingFace upvotes + a timely benchmark drawing evaluation-focused attention

---

### 18. Abra: Scaling Diffusion Image Training
**Authors:** Kyle Chickering, Wei-An Lin, Swayam Bhanded, Dan Saunders, Akshat Tripathi, Jiaming Song, Shyamal Buch, Xinchen Yan
**arXiv:** [arxiv.org/abs/2608.17286](https://arxiv.org/abs/2608.17286)
**Summary:** Compute-optimal scaling laws guide the training of frontier language models yet remain largely unexplored for visual generation. We present a systematic scaling law study for text-to-image diffusion models using Abra, a controlled family of flow-matching transformers trained across three orders of magnitude worth of compute (10^{19} to 10^{22} FLOPs), reaching significantly larger compute budgets than previous works.
**Trending because:** 6 HuggingFace upvotes + riding strong momentum in generative vision research

---

### 19. From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents
**Authors:** Zhengzhao Ma. Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun
**arXiv:** [arxiv.org/abs/2608.16002](https://arxiv.org/abs/2608.16002)
**Summary:** Reliable uncertainty quantification (UQ) is essential for deploying large language model (LLM) agents in complex interactive environments. Existing UQ methods largely rely on local signals, such as token probabilities, predictive entropy, or per-step confidence, and therefore overlook the long-range dependencies through which errors accumulate across an execution trajectory.
**Trending because:** 6 HuggingFace upvotes + tapping the surging interest in autonomous agents

---

### 20. Dynamic Multi-Byte Prediction With Hierarchical Language Models
**Authors:** Abraham Toluwase Owodunni, Chibuzor Okocha, Christan Grant, Tomasz Limisiewicz, Sachin Kumar
**arXiv:** [arxiv.org/abs/2608.15454](https://arxiv.org/abs/2608.15454)
**Summary:** Byte-level hierarchical language models (LMs) have recently emerged as a robust alternative to their popular counterparts that use subword tokenization. However, generating one byte at a time remains a bottleneck for inference speed.
**Trending because:** 6 HuggingFace upvotes + resonating with current LLM research priorities

---
