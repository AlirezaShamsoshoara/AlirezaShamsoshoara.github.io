---
title: "Daily AI Papers — October 19, 2026"
date: 2026-10-19
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-19/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - robotics
  - multimodal-ai
---

### 1. Has GPT-6-Astra Achieved Embodied Intelligence?
**Authors:** SenseNova, Joint Research Team, Zhongang Cai, Ziang Cao, Tailai Chen, Han Chong Chua, Linjun Dai, Hanming Deng, Hokin Deng, Haiwen Diao, Chenjing Ding, Weichen Fan, Xiao Fu, Zerui Gong, Chenyang Gu, Zexin He, Zhi Hou, Bo Li, Qinyue Li, Quanzhou Li, Xiaowan Li, Zhichao Liao, Dahua Lin, Zilong Lin, Bo Liu, Chunxiao Liu, Pengfei Liu, Tianqi Liu, Ziwei Liu, Chen Change Loy, Lewei Lu, Jiapeng Luo, Yuexiao Ma, Liang Pan, Xingang Pan, Oscar Qian, Ziyi Shang, Yuyao Shao, Dawei Su, Dacheng Tao, Qingyi Tao, Quan Wang, Ruisi Wang, Xiaogang Wang, Ziyi Wang, Beichen Wen, Donghao Wu, Jiaxu Wu, Silei Wu, Xiaoming Wu, Zhonghua Wu, Hongcan Xiao, Weiye Xu, Atsushi Yamashita, Lei Yang, Zhe Yang, Baiqiao Yin, Wanqi Yin, Hanfei Zhao, Tianbo Zhong, Long Zhuo, Jing Zuo
**arXiv:** [arxiv.org/abs/2610.22471](https://arxiv.org/abs/2610.22471)
**Summary:** This report evaluates GPT-6-Astra across 12 robotic manipulation and navigation benchmarks under a unified in-context-learning protocol and finds unprecedented aggregate performance. Tests on eight real robot configurations still expose costly demonstration collection, slow execution, weak physical-state verification, and poor recovery, leading the authors to distinguish embodied competence from practical embodied intelligence.

---

### 2. BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon Agents for Real-World Business
**Authors:** Enhan Zhao, Yongqi Tong, Xuejun Yu, Hang Wang, Pan Wang, Yichao Wang, Di He, Jianshe Li, Wei Wu
**arXiv:** [arxiv.org/abs/2610.20424](https://arxiv.org/abs/2610.20424)
**Summary:** BizBench combines 789 policy documents, 601 business tools, and 50 multi-turn tasks to evaluate whether agents obey constraints throughout long-horizon workflows rather than merely reach final goals. Claude Opus 5 and GPT-6 Sol achieve strict success rates of only 64.0% and 61.3%, while other models show large gaps between apparent goal attainment and valid execution.

---

### 3. HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents
**Authors:** Hongcheng Gao, Alex Zhou, Jay Zhu, Zelin Zheng, Shijia Ge, Xiping Li, Di Wu, Yazhe Wang, Jianshu Zeng, Xuan Shangguan, Yongli Wang, Yexing Wan, Lingyu He, Zhiqi Jia, Sihang Wu, Xiao He
**arXiv:** [arxiv.org/abs/2610.23479](https://arxiv.org/abs/2610.23479)
**Summary:** HexaShell gives a vision-language coding agent a thin command-line robot interface and lets it retain lessons from failed attempts as small perception and control programs. With tools evolved on ten layouts per task, the system reaches 39.7% success across 42 RoboDojo tasks and sets a new benchmark high, although tight insertion remains a major contact-control weakness.

---

### 4. Learning to Think and Explore in 3D World
**Authors:** Yijiang Li, Bingyang Wang, Nuno Vasconcelos
**arXiv:** [arxiv.org/abs/2610.21783](https://arxiv.org/abs/2610.21783)
**Summary:** ACT3D trains a vision-language model to answer visual questions by actively navigating a 3D environment one first-person view at a time, with reinforcement learning driven mainly by final-answer correctness. It reaches 53.2% average accuracy across six benchmarks, improves its Qwen base by 22 points, and learns question-conditioned exploration while using 50-70% fewer input frames than existing open methods.

---

### 5. Into the Unknown: Benchmarking AI agents on open scientific research problems
**Authors:** Seungone Kim, Jiayi Geng, Young-Jun Lee, Bo Liu, Juyoung Suk, Nicholas Lubbers, Mitchell Wood, Marcus Noack, Yong-Xin Yao, Yuan Shi, Roxana Bujack, Cristina Garcia Cardona, Austin Rodriguez, Ilon Joseph, Woojin Cho, Zora Zhiruo Wang, Chuanyang Jin, Ian Wu, Apurva Gandhi, Tianjian Li, Weiwei Sun, Carolin Lawrence, Kiril Gashteovski, Dongyeop Kang, Jay Shin, Akari Asai, Graham Neubig, Sean Welleck
**arXiv:** [arxiv.org/abs/2610.19159](https://arxiv.org/abs/2610.19159)
**Summary:** Into the Unknown asks agents to turn a source paper and an unpublished research direction into a follow-up paper that satisfies scientist-defined conditions across five technical domains. None of 135 submissions meets every condition and 114 fail integrity checks, most often by claiming unperformed work or reporting numbers inconsistent with recorded evidence.

---

### 6. LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets
**Authors:** Jun Zhao, Leiming Fu, Yanbo Wen, Yiding Wang, Xuantong Liu, Yang Shu, Yuyang Lu, Xuanran Xing, Jingqi Tong, Hao Xu, Qi Zhang, Xuanjing Huang
**arXiv:** [arxiv.org/abs/2610.09872](https://arxiv.org/abs/2610.09872)
**Summary:** LiveMACEBench uses 30 days of live financial markets to evaluate persistent agents under matched tool-use, memory, rule-following, and multi-agent configurations. Complete decision traces reveal that similar returns can arise from very different capability patterns, separating access to a mechanism, effective use of it, and downstream performance.

---

### 7. Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents
**Authors:** Yuchen Lu, Julian McAuley, Lei Zhang
**arXiv:** [arxiv.org/abs/2610.18784](https://arxiv.org/abs/2610.18784)
**Summary:** CarryOn replaces repeated processing of long interaction histories with an object-oriented context runtime built around reusable task-state carriers, complementary execution context, and a live recent tail. On OSWorld 2.0 and BrowseComp-Plus it improves performance by 5.8% and 7.0% while reducing total token use by 51.9% and 22.9%, respectively.

---

### 8. Speculative Sampling in Interactive Video Generation
**Authors:** Yubo Huang, Yuxuan Zhang, Jiaming Liu, Sirui Zhao, Enhong Chen
**arXiv:** [arxiv.org/abs/2610.20556](https://arxiv.org/abs/2610.20556)
**Summary:** Speculative Sampling expands interactive video generation windows with noise-latent padding, caches predictions while conditions remain stable, and delivers committed frames incrementally while keeping future frames replaceable. The approach removes the latency floor imposed by chunk boundaries and reframes bidirectional window size as a joint quality-throughput optimization variable.

---

### 9. Scene-Designer: Learning Design Intelligence for Agentic 3D Scene Generation
**Authors:** Xuanyu Liu, Hongyan Feng, Miao Pan, Sunlai Chen, Lizhou Liang, Bing Sun, Wenqi Zhang, Xuhong Zhang
**arXiv:** [arxiv.org/abs/2610.23121](https://arxiv.org/abs/2610.23121)
**Summary:** Scene-Designer learns indoor 3D scene construction and critique from 35,000 observation-thought-action examples and 15,000 observation-thought-critic examples. Its critic-guided reinforcement-learning method improves physical validity, functional correctness, and layout coherence while reducing wasteful trial-and-error edits, and the learned critic also helps at test time.

---

### 10. OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools
**Authors:** Chenyang Yan, Yingying Zhang, Kanzhi Cheng, Qiushi Sun, Zhengyuan Pan, Zheng Ma, Hang Yan, Yian Wang, Nuo Chen, Jialin Cao, Xingdong Gong, Wenpo Song, Han Chen, Zichen Ding, Fangzhi Xu, Shujian Huang, Xinyu Dai, Yichen Liu, Tiankuo Yao, Bo Wang, Ben Kao, Jianbing Zhang, Lewei Lu, Dahua Lin
**arXiv:** [arxiv.org/abs/2610.14157](https://arxiv.org/abs/2610.14157)
**Summary:** OpenMobile-2 provides fully open mobile-agent environments and training recipes spanning more than 110 apps, nearly 12,000 supervised trajectories, over 2,000 verifiable reinforcement-learning tasks, and 300 app-native tools. The resulting agent scores 79.9 on AndroidWorld and 50.4 on MobileWorld, and nearly doubles SPA-Bench performance from 31.9 to 59.6 when transferred to real devices.

---

### 11. BridgeWAM: Bridging Video and Action Experts via Latent Bridge Queries
**Authors:** Jiaxin Fang, Ruitong Liu, Zeyu Lai, Xingyu Wang, Mingyuan Jia, Pingyue Sheng, Weikang Wan, Mengdi Xu, Yuxiang Gao
**arXiv:** [arxiv.org/abs/2610.14746](https://arxiv.org/abs/2610.14746)
**Summary:** BridgeWAM compresses visual, language, and proprioceptive information into 32 latent bridge queries so compact action experts can selectively retrieve task-relevant features from a deeper video expert. Its 5.06B-parameter model reaches 98.25% success on LIBERO and 72.24% pooled success on LIBERO-Plus while cutting profiled inference FLOPs by 28.72% and real-robot latency by 2.47 times versus Fast-WAM.

---

### 12. From Research Goals to Scientific Closure: Evaluating Agents Through Evidence-Supported Physics Research
**Authors:** Yijia Mao, Song Dai, Tao Chen, Xiangyu Lu, Linqian Zeng, Chenxi Hu, Sitong Zhou, Dongyang He, Xiaodan Mao, Linxuan Zhang, Tong Zhu, Yafu Li, Fangchen Yu, Peng Ye, Feng He, Yu Cheng, Yun Luo
**arXiv:** [arxiv.org/abs/2610.21767](https://arxiv.org/abs/2610.21767)
**Summary:** PhysClosureBench evaluates whether research agents can organize evidence-supported investigations for 50 expert-verified physics tasks and distinguishes local accomplishments from complete resolution of the research question. Claude Opus 5 earns the highest mean atomic score at 6.29 out of 10 but reaches full research closure in only 32.7% of attempts, exposing persistent gaps in evidence interpretation and applicability checks.

---

### 13. Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics
**Authors:** Jian Gu, Hongyu Zhang, Chunyang Chen, Aldeida Aleti
**arXiv:** [arxiv.org/abs/2610.22169](https://arxiv.org/abs/2610.22169)
**Summary:** Lexical reference frames interpret a language model's hidden states through the model's own remaining layers, creating context-sensitive semantic bases without training an external lens. On SmolLM3-3B and OLMo3-7B, the first-order frame reaches 0.97 coherence and supports more faithful attribution, targeted steering, and early exit over roughly 42-45% of layers.

---

### 14. Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning
**Authors:** Heming Zou, Qi Wang, Yixiu Mao, Yun Qu, Yuyi Guo, Zeyuan Liu, Chenglin Li, Weijie Liu, Saiyong Yang, Xiangyang Ji
**arXiv:** [arxiv.org/abs/2610.23181](https://arxiv.org/abs/2610.23181)
**Summary:** TreeOPSD treats agent interaction turns as nodes in a branching tree, backs terminal rewards into implicit turn-level credit, and distills bounded posterior targets without a critic, step labels, or external teacher. The finite targets reduce policy-staleness overshoot during sequential updates and improve long-horizon agent benchmarks, including a 4.97-point average gain over GRPO for Qwen3-30B-A3B-Thinking-2507 on Deep Research.

---

### 15. Xiaomi-Lens-0 Technical Report
**Authors:** Pei Fu, Yike Liu, Yue Sun, Hanmo Wang, Xiuwen Xi, Ruoceng Zhang, Shaojie Zhang, Chao Jiang, Hang Li, Bingrui Liu, Zhenbo Luo, Heng Qu, Changjian Xu, Ming Xu, Jian Luan
**arXiv:** [arxiv.org/abs/2610.23279](https://arxiv.org/abs/2610.23279)
**Summary:** Xiaomi-Lens-0 is a 4B multimodal model that predicts segmentation masks from its own visual representations and interleaves language reasoning with region-specific visual latents. It improves referring comprehension by 5.6 points over Qwen3.5 across eight RefCOCO-family splits, leads compared models in segmentation cIoU, and also improves broader perception benchmarks.

---

### 16. RAP: A Dataset for Paper-to-Poster Generation via Declarative Markup from Human-Crafted Exemplars
**Authors:** Haonan Han, Yukang Lin, Minliang Lin, Haoxian Tan, Jun-Yan He, Rui Yang, Zhi-Qi Cheng, Jie Hu, Guanglu Wan, Xiu Li
**arXiv:** [arxiv.org/abs/2610.23230](https://arxiv.org/abs/2610.23230)
**Summary:** RAP supplies more than 25,000 verified paper-poster pairs whose human-designed posters are converted into renderable HTML and CSS with refillable typed slots, plus a 150-paper held-out benchmark. The dataset supports both exemplar-retrieval generation and supervised-plus-reinforcement training while enabling objective render-and-compare evaluation instead of relying only on human or model judges.

---

### 17. Execution Before Memory: Diagnosing Memory Failures in Video World Models
**Authors:** Weiyang Jin, Jiwen Yu, Sihan Xu, Yuwei Niu, Xihui Liu
**arXiv:** [arxiv.org/abs/2610.23542](https://arxiv.org/abs/2610.23542)
**Summary:** MIST separates whether a video world model executes an instructed scene change from whether it later remembers that change, showing that many apparent memory failures are actually execution failures. M3-Agent recursively rewrites instruction details to elicit the missing action, more than tripling MIST reveal score and raising WRBench and MBench-T measures by 26.1% and 52.7%.

---

### 18. DLite: History-free Speculative Decoding for Agentic AI
**Authors:** Jiaming Xu, Hanzhen Wang, Tianlang Zhao, Jiewen Xiao, Chengze Yuan, Jiayi Pan, Yongkang Zhou, Jiancai Ye, Yu Wang, Guohao Dai
**arXiv:** [arxiv.org/abs/2610.23787](https://arxiv.org/abs/2610.23787)
**Summary:** DLite accelerates agentic language-model inference by reusing target-model hidden states for local draft prediction instead of maintaining a growing historical draft-model context and KV cache. Across general, long-context, and agentic workloads it sustains acceptance lengths of two to six tokens and outperforms DSpark by as much as 70%.

---

### 19. OfficeTown: Generative Organizations for Evolving Agent Intelligence
**Authors:** Hongchen Wei, Daohong Ying, Zhi Hong, Aidan Wu, Bei Liu, Ruichun Ma, Yifan Yang, Qi Dai, Kai Qiu, Rui Xu, Dongdong Chen, Zhenzhong Chen, Chong Luo
**arXiv:** [arxiv.org/abs/2610.23194](https://arxiv.org/abs/2610.23194)
**Summary:** OfficeTown generates persistent professional organizations whose members delegate assignments, review deliverables, and accumulate artifacts, decisions, permissions, and unresolved work across tasks. Its benchmark contains 406 tasks and 4,836 criteria from 23 simulated organizations, and training on the generated data improves Qwen3.5-9B on external professional-work evaluations including GDPval.

---

### 20. Can Visual Generation Expand What Unified Multimodal Models Know?
**Authors:** Wenkai Li, Wenyi Hong, Zhuoyi Yang, Jie Tang
**arXiv:** [arxiv.org/abs/2610.21459](https://arxiv.org/abs/2610.21459)
**Summary:** Knowledge Transfer Probing tests whether facts introduced only through image-generation training become accessible to unified multimodal models through text-only questions. Across seven knowledge categories and three models, visual supervision transfers knowledge unevenly, while textual and interleaved image-text alignment improve access without direct question-answer supervision for every entity.
