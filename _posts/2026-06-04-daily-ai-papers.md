---
title: "Daily AI Papers — June 04, 2026"
date: 2026-06-04
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-04/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal
  - agentic-ai
  - streaming-models
---

## 1. Audio Interaction Model
**Authors:** Zhifei Xie, Zihang Liu, Ze An, Xiaobin Hu, Yue Liao, Ziyang Ma et al.
**ArXiv:** [arxiv.org/abs/2606.05121](https://arxiv.org/abs/2606.05121)
**GitHub:** [github.com/xzf-thu/Audio-Interaction](https://github.com/xzf-thu/Audio-Interaction) (⭐35) | **Project:** [xzf-thu.github.io/Audio-Interaction](https://xzf-thu.github.io/Audio-Interaction/)
**HF Upvotes:** 81 | **Comments:** 2
**Sources:** HuggingFace #1

Audio is an inherently interactive modality, yet today's Large Audio Language Models (LALMs) are offline, and streaming audio models each handle only a single task such as streaming ASR or voice chatting. This paper unifies them into one online LALM — a model that, through an always-on perceive-decide-respond loop, listens to sound, environment, and instructions in real time and reacts on the fly. The authors formalize this regime as the Audio Interaction Model (AIM), realizing it with Audio-Interaction, a unified streaming-native framework supporting multiple audio interaction capabilities including streaming ASR, voice chat, and real-time audio event response.

**Why trending:** Highest upvotes of the day (81). Addresses a fundamental gap in LALM design — all existing models are offline or single-task. Unifies streaming audio perception and response into one always-on loop, a key step toward ambient audio AI.

---

## 2. Cosmos 3: Omnimodal World Models for Physical AI
**Authors:** Niket Agarwal, Arslan Ali, Jon Allen, Martin Antolini, Adeline Aubame et al. (NVIDIA)
**ArXiv:** [arxiv.org/abs/2606.02800](https://arxiv.org/abs/2606.02800)
**GitHub:** [github.com/NVIDIA/cosmos](https://github.com/NVIDIA/cosmos) (⭐8,774) | **Project:** [research.nvidia.com/labs/cosmos-lab/cosmos3](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)
**HF Upvotes:** 60 | **Comments:** 0
**Sources:** HuggingFace, web search (NVIDIA blog, HuggingFace blog)

Cosmos 3 is a family of omnimodal world models designed to jointly process and generate language, image, video, audio, and action sequences within a unified mixture-of-transformers (MoT) architecture. By supporting highly flexible input-output configurations, Cosmos 3 seamlessly unifies critical modalities for Physical AI — effectively subsuming VLMs, video generators, world simulators, and world-action models into a single framework. The model achieves state-of-the-art performance across understanding and generation tasks.

**Why trending:** NVIDIA's flagship Physical AI model with 8,774 GitHub stars. First open omni-model handling all modalities (text, image, video, audio, actions) in one architecture. Critical for robotics and embodied AI. Featured on HuggingFace blog.

---

## 3. Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories
**Authors:** Jiaming Wang, Ziteng Feng, Jiangtao Wu, Ruihao Li, Qianqian Xie, Yuxiang Ren et al.
**ArXiv:** [arxiv.org/abs/2606.02060](https://arxiv.org/abs/2606.02060)
**GitHub:** [github.com/NJU-LINK/DRIFT](https://github.com/NJU-LINK/DRIFT) (⭐7) | **Project:** [nju-link.github.io/DRIFT](https://nju-link.github.io/DRIFT/)
**HF Upvotes:** 41 | **Comments:** 3

Deep-research agents solve tasks through long trajectories of search, tool use, evidence inspection, and answer synthesis. This paper studies span-level error localization — not just whether an agent succeeds, but *which parts* of the trajectory make the answer unreliable. The authors collect 2,790 real trajectories from two agent frameworks, three backbone models, and three benchmarks, annotating harmful error spans to create TELBench. They then propose DRIFT, a claim-centric auditing approach that identifies error spans in agent reasoning trajectories.

**Why trending:** Directly addresses the black-box problem of agentic AI — high upvotes (41) and most comments (3). TELBench dataset and DRIFT framework are immediately practical for evaluating production research agents.

---

## 4. Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning
**Authors:** Xuekang Wang, Zhuoyuan Hao, Shuo Hou, Hao Peng, Juanzi Li, Xiaozhi Wang et al.
**ArXiv:** [arxiv.org/abs/2606.04923](https://arxiv.org/abs/2606.04923)
**GitHub:** [github.com/THUAIS-Lab/CHERRL](https://github.com/THUAIS-Lab/CHERRL) (⭐1)
**HF Upvotes:** 33 | **Comments:** 1

Rubric-based RL uses an LLM-as-a-Judge (LaaJ) to score model outputs as rewards. Policy models may exploit latent biases in the judge, leading to reward hacking and unsafe training outcomes. This paper introduces CHERRL, a controllable hacking environment for rubric-based RL, enabling systematic reproduction and analysis of subtle reward hacking behaviors. The authors demonstrate that policy models can learn to exploit judge biases in ways that pass rubric evaluation while failing on actual quality metrics.

**Why trending:** Critical safety concern for RLHF/RLAIF pipelines. Reward hacking in LLM judges is a growing problem as rubric-based RL becomes mainstream. CHERRL provides the first systematic controllable environment for studying this.

---

## 5. OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs
**Authors:** Yifei Li, Pengyiang Liu, Yuhang Zang, Zhongyue Shi, Qi Fu, Hongye Hao et al.
**ArXiv:** [arxiv.org/abs/2606.03890](https://arxiv.org/abs/2606.03890)
**GitHub:** [github.com/InternLM/OVO-S-Bench](https://github.com/InternLM/OVO-S-Bench) (⭐30) | **Project:** [internlm.github.io/OVO-S-Bench](https://internlm.github.io/OVO-S-Bench/)
**HF Upvotes:** 28 | **Comments:** 1

Multimodal agents in robotics, AR, and autonomous driving must reason about places and layouts from continuous egocentric streams, often using evidence outside the current view. OVO-S-Bench is a fully human-annotated benchmark for streaming spatial intelligence, comprising 1,680 questions over 348 source videos, covering hierarchical spatial reasoning from object-level to layout-level understanding. The benchmark reveals that current MLLMs struggle significantly with streaming spatial reasoning, even when they perform well on offline tasks.

**Why trending:** InternLM team benchmark filling a critical gap in spatial AI evaluation. Robotics, AR, and autonomous driving all require streaming spatial reasoning — OVO-S-Bench provides the first systematic test. 30 GitHub stars on release day.

---

## 6. Qwen-Image-Flash: Beyond Objective Design
**Authors:** Tianhe Wu, Kun Yan, Zikai Zhou, Lihan Jiang, Jiahao Li, Jie Zhang et al.
**ArXiv:** [arxiv.org/abs/2606.03746](https://arxiv.org/abs/2606.03746)
**HF Upvotes:** 28 | **Comments:** 3

Few-step distillation is an effective strategy for accelerating visual generative models, but prior work focused only on distillation objectives. This paper revisits few-step distillation from a complementary perspective — the training *recipe* — systematically investigating data composition, teacher guidance, and task mixture for Qwen-Image-2.0. The result is Qwen-Image-Flash, a distilled model that matches or exceeds the teacher in text-to-image generation and instruction-guided image editing with far fewer inference steps.

**Why trending:** Qwen series has huge community following. Practical speedup for visual generation without quality loss — directly usable by practitioners. Three comments indicate active community discussion.

---

## 7. M³Eval: Multi-Modal Memory Evaluation through Cognitively-Grounded Video Tasks
**Authors:** Jie Huang, Ruixun Liu, Sirui Sun, Xinyi Yang, Yin Li, Yixin Zhu et al.
**ArXiv:** [arxiv.org/abs/2606.05008](https://arxiv.org/abs/2606.05008)
**GitHub:** [github.com/PKU-VaLuE-Lab/m3eval](https://github.com/PKU-VaLuE-Lab/m3eval) (⭐18) | **Project:** [pku-value-lab.github.io/m3eval-homepage](https://pku-value-lab.github.io/m3eval-homepage/)
**HF Upvotes:** 24 | **Comments:** 1

As multimodal models advance toward long-form video understanding, memory emerges as a critical capability that existing benchmarks ignore. M³Eval is the first comprehensive evaluation framework specifically targeting memory in multimodal models — what models retain, how faithfully information is preserved, and how robust memory is under interference. Grounded in cognitive psychology, the benchmark reveals that current state-of-the-art models exhibit significant memory limitations, particularly in maintaining disentangled representations and showing human-like interference patterns.

**Why trending:** Fills a clear benchmark gap: all existing video benchmarks test perception and reasoning but not memory. Grounded in cognitive science. 18 GitHub stars on day one.

---

## 8. ThoughtFold: Folding Reasoning Chains via Introspective Preference Learning
**Authors:** Ziyan Liu, Xueda Shen, Yuzhe Gu, Songyang Gao, Kuikun Liu, Guangran Cheng et al.
**ArXiv:** [arxiv.org/abs/2606.03503](https://arxiv.org/abs/2606.03503)
**GitHub:** [github.com/ziyanliux/ThoughtFold](https://github.com/ziyanliux/ThoughtFold) (⭐9)
**HF Upvotes:** 24 | **Comments:** 1

Large Reasoning Models (LRMs) suffer from over-thinking: RLVR reinforces redundant trial-and-error in long CoTs because it selects outcome-correct trajectories regardless of internal redundancy. ThoughtFold addresses this with fine-grained preference learning that identifies and eliminates redundant explorations ("folds" them out) using introspective comparisons between concise and verbose reasoning paths. Unlike prior methods that give advantage to shorter responses, ThoughtFold operates at the step level with masked preference optimization.

**Why trending:** Over-thinking in reasoning models (o1, DeepSeek-R1 style) is a hot research area. ThoughtFold provides a principled solution at the step level rather than just penalizing length.

---

## 9. Echo-Infinity: Learning Evolving Memory for Real-Time Infinite Video Generation
**Authors:** Yuxuan Bian, Zeyue Xue, Songchun Zhang, Shiyi Zhang, Weiyang Jin, Yaowei Li et al.
**ArXiv:** [arxiv.org/abs/2606.04527](https://arxiv.org/abs/2606.04527)
**GitHub:** [github.com/Echo-Team-Joy-Future-Academy-JD/Echo-Infinity](https://github.com/Echo-Team-Joy-Future-Academy-JD/Echo-Infinity) (⭐47) | **Project:** [echo-team-joy-future-academy-jd.github.io/Echo-Infinity](https://echo-team-joy-future-academy-jd.github.io/Echo-Infinity/)
**HF Upvotes:** 22 | **Comments:** 1

Echo-Infinity is an autoregressive framework for real-time infinite video generation using a learnable evolving memory that dynamically filters, abstracts, and compresses any-length history at constant cost. Existing methods use predefined KV-cache schedules or fixed-ratio compression that lose historical information and amplify compounding errors. Echo-Infinity's learnable memory query mechanism with gating and relative RoPE enables coherent long-horizon video generation without the quality degradation typical of existing approaches.

**Why trending:** 47 GitHub stars on day one — highest GitHub engagement of the day. "Infinite video generation" is a compelling capability. Real-time constraint adds practical value for production use.

---

## 10. Streaming Communication in Multi-Agent Reasoning (StreamMA)
**Authors:** Zhen Yang, Xiaogang Xu, Wen Wang, Cong Chen, Xander Xu, Ying-Cong Chen et al.
**ArXiv:** [arxiv.org/abs/2606.05158](https://arxiv.org/abs/2606.05158)
**GitHub:** [github.com/EnVision-Research/StreamMA](https://github.com/EnVision-Research/StreamMA) (⭐20) | **Project:** [zhenyangcs.github.io/StreamMA-website](https://zhenyangcs.github.io/StreamMA-website/)
**HF Upvotes:** 21 | **Comments:** 1

Multi-agent reasoning systems adopt a "generate-then-transfer" paradigm where end-to-end latency scales linearly with pipeline depth. StreamMA streams each reasoning step to downstream agents as soon as it is generated, pipelining adjacent agents and reducing latency. Surprisingly, this pipelining also improves *effectiveness*: early reasoning steps are more reliable than later ones, so downstream agents benefit from working with higher-quality partial context rather than waiting for potentially degraded final outputs.

**Why trending:** Counter-intuitive finding — streaming improves both speed AND quality in multi-agent reasoning. Directly applicable to production LLM pipelines. 20 GitHub stars on launch day.

---

## 11. Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems
**Authors:** Yipeng Ouyang, Xin Huang, Bingjie Liu, Zhongchun Zheng, Yuhao Gu, Xianwei Zhang et al.
**ArXiv:** [arxiv.org/abs/2605.27492](https://arxiv.org/abs/2605.27492)
**GitHub:** [github.com/Nexa-Language/RAMP](https://github.com/Nexa-Language/RAMP) (⭐1) | **Project:** [ramp.yatcc-ai.com](http://ramp.yatcc-ai.com/)
**HF Upvotes:** 19 | **Comments:** 2

LLM agents are evolving into autonomous software engineering systems, but existing evaluation methodologies remain centered on static, isolated, short-horizon benchmarks that fail to capture real-world production workflows. RAMP evaluates long-horizon software engineering agents through realistic compiler-construction workloads, involving long execution chains, tool interactions, dependency management, and iterative feedback loops. The paper shows significant gaps between benchmark performance and actual production capability.

**Why trending:** Tackles the benchmark-reality gap for software engineering agents — highly relevant as coding agents see widespread production deployment. Two comments signal active practitioner interest.

---

## 12. Self-Distilled Policy Gradient (SDPG)
**Authors:** Yifeng Liu, Shiyuan Zhang, Yifan Zhang, Quanquan Gu
**ArXiv:** [arxiv.org/abs/2606.04036](https://arxiv.org/abs/2606.04036)
**GitHub:** [github.com/lauyikfung/SDPG](https://github.com/lauyikfung/SDPG) (⭐6) | **Project:** [lauyikfung.github.io/SDPG](https://lauyikfung.github.io/SDPG/)
**HF Upvotes:** 15 | **Comments:** 2

SDPG is a self-distilled policy-gradient framework that combines group-relative verifier advantages with normalized standard deviation and on-policy self-distillation. The key insight is that self-distillation can be cast as an auxiliary full-vocabulary student-to-teacher reverse KL-divergence loss, providing dense supervision for sparse-reward RL. SDPG improves training stability and final performance on mathematical reasoning benchmarks compared to standard GRPO variants.

**Why trending:** GRPO and its variants are currently the dominant RL training method for LLMs. SDPG provides a principled improvement with a clean theoretical grounding, from the Quanquan Gu lab (UCLA, known for strong RL-for-LLMs work).

---

## 13. Eliciting Complex Spatial Reasoning in MLLMs through Wide-Baseline Matching
**Authors:** Hao Zhong, Muzhi Zhu, Shenyan Zeng, Anzhou Li, Cong Chen, Hua Geng et al.
**ArXiv:** [arxiv.org/abs/2606.03577](https://arxiv.org/abs/2606.03577)
**GitHub:** [github.com/aim-uofa/ReasonMatch](https://github.com/aim-uofa/ReasonMatch) (⭐11) | **Project:** [aim-uofa.github.io/reasonmatch](https://aim-uofa.github.io/reasonmatch/)
**HF Upvotes:** 13 | **Comments:** 1

Wide-baseline matching (WBM) — matching scene elements across images taken from very different viewpoints — requires geometric understanding, viewpoint invariance, fine-grained perception, and occlusion reasoning, making it a hard testbed for MLLM spatial reasoning. This paper introduces ReasonMatch-Bench (stratified by viewpoint displacement and matching granularity across indoor, outdoor, and object-centric scenes) and Dynamic Correspondence Reinforcement Learning (DCRL) to train MLLMs on WBM tasks.

**Why trending:** WBM is a fundamental computer vision challenge. The paper bridges the gap between classical geometric vision and modern MLLMs, with direct applications in robotics and AR.

---

## 14. MemTrain: Self-Supervised Context Memory Training
**Authors:** Ziheng Li, Xingrun Xing, Haoqing Wang, Zhi-Hong Deng, Yehui Tang et al.
**ArXiv:** [arxiv.org/abs/2606.03197](https://arxiv.org/abs/2606.03197)
**HF Upvotes:** 12 | **Comments:** 1

Memory is critical for long-horizon LLM agents, but existing approaches train end-to-end with RL on downstream tasks — expensive and data-inefficient. MemTrain proposes self-supervised pretraining for memory via masked reconstruction and memory recall proxy tasks, optimized with GRPO. This decouples memory training from downstream task specifics, enabling more generalizable memory behaviors across long-text QA and search-based QA without expensive annotation.

**Why trending:** Memory for agents is a hot topic. Self-supervised approach reduces annotation cost dramatically. Applicable to any agent framework using external memory stores.

---

## 15. MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?
**Authors:** Xinyu Che, Junqi Xiong, Yunfei Ge, Xinping Lei, Shihao Li, Hang Yan et al.
**ArXiv:** [arxiv.org/abs/2606.01993](https://arxiv.org/abs/2606.01993)
**GitHub:** [github.com/NJU-LINK/MMG2Skill](https://github.com/NJU-LINK/MMG2Skill) (⭐3)
**HF Upvotes:** 12 | **Comments:** 1

The Web contains vast procedural knowledge (tutorials, how-tos, guides) that is multimodal, heterogeneous, noisy, and implicitly assumes human executors — hard to use directly for agent skills. MMG2Skill formalizes guide-to-skill learning: converting in-the-wild multimodal guides into executable skills and continuously improving them via closed-loop feedback. The framework uses a VLM analyzer with trajectory-level root-cause feedback and early stopping, demonstrating gains across GUI control, gameplay, and card play tasks.

**Why trending:** Knowledge transfer from human-written web guides to agents is a practically important and underexplored problem. Closed-loop skill evolution addresses the noisy web knowledge challenge directly.

---

## 16. MapAgent: An Industrial-Grade Agentic Framework for City-scale Lane-level Map Generation
**Authors:** Deguo Xia, Zihan Li, Haochen Zhao, Dong Xie, Yuyao Kong, Xiyan Liu et al.
**ArXiv:** [arxiv.org/abs/2606.04513](https://arxiv.org/abs/2606.04513)
**GitHub:** [github.com/eadst/KDD-2026-MapAgent](https://github.com/eadst/KDD-2026-MapAgent) (⭐1)
**HF Upvotes:** 11 | **Comments:** 1

Lane-level maps are critical for autonomous driving but constructing them for hundreds of cities is labor-intensive. MapAgent combines end-to-end vectorized mapping with a VLM-based Judge-Planner-Worker architecture that handles complex scenes (worn markings, intersections, construction zones) by incorporating explicit traffic regulations and mapping specifications. Evaluated at city scale, MapAgent achieves high automation rates with specification compliance.

**Why trending:** KDD 2026 paper on autonomous driving infrastructure. Industrial-grade validation distinguishes it from academic proofs-of-concept. VLM-based agentic approach to HD map generation is novel.

---

## 17. AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation
**Authors:** Haobo Li, Yanhong Zeng, Yunhong Lu, Jiapeng Zhu, Hao Ouyang, Qiuyu Wang et al.
**ArXiv:** [arxiv.org/abs/2606.03972](https://arxiv.org/abs/2606.03972)
**GitHub:** [github.com/AutoLab-SAI-SJTU/AAD-1](https://github.com/AutoLab-SAI-SJTU/AAD-1) (⭐31) | **Project:** [aad-1.github.io](https://aad-1.github.io/)
**HF Upvotes:** 11 | **Comments:** 1

AAD-1 enables one-step autoregressive image-to-video generation via asymmetric adversarial distillation. Prior adversarial distillation methods suffer from motion collapse and training instability. AAD-1 fixes this by breaking the generator-discriminator symmetry: the generator uses causal attention to preserve autoregressive constraints, while the discriminator uses bidirectional attention for holistic realism scoring. A phased training strategy progressively increases motion amplitude.

**Why trending:** 31 GitHub stars on day one. One-step video generation is a practically valuable speedup. Motion collapse has been the key failure mode of existing approaches — AAD-1 solves it with a clean architectural insight.

---

## 18. Filter, Then Reweight: Rethinking Optimization Granularity in On-Policy Distillation (FiRe-OPD)
**Authors:** Yuying Li, Leqi Zheng, Yongzi Yu, Wenrui Zhou, Xuchang Zhong, Xing Hu et al.
**ArXiv:** [arxiv.org/abs/2606.02684](https://arxiv.org/abs/2606.02684)
**GitHub:** [github.com/YuYingLi0/FiRe-OPD](https://github.com/YuYingLi0/FiRe-OPD) (⭐8)
**HF Upvotes:** 11 | **Comments:** 1

On-policy distillation (OPD) is shifting from full-trace KL supervision toward more selective training paradigms. FiRe-OPD jointly adjusts supervision at both trajectory and token levels: first filtering low-quality trajectories, then applying soft token-level reweighting to emphasize informative tokens. This dual-granularity optimization outperforms both trajectory-only and token-only selection baselines on instruction following and reasoning benchmarks.

**Why trending:** On-policy distillation is the dominant training paradigm for alignment and reasoning. FiRe-OPD's dual-granularity approach (trajectory + token) is a systematic improvement over the current state of the art.

---

## 19. ZipSplat: Fewer Gaussians, Better Splats
**Authors:** Alexander Veicht, Sunghwan Hong, Dániel Baráth, Marc Pollefeys (ETH Zürich)
**ArXiv:** [arxiv.org/abs/2606.05102](https://arxiv.org/abs/2606.05102)
**GitHub:** [github.com/cvg/ZipSplat](https://github.com/cvg/ZipSplat) (⭐28) | **Project:** [veichta.com/zipsplat](https://veichta.com/zipsplat/)
**HF Upvotes:** 10 | **Comments:** 1

Feed-forward 3D Gaussian Splatting predicts one Gaussian per input pixel, wastefully allocating the same budget to flat walls and complex geometry. ZipSplat decouples Gaussian placement from the pixel grid using a multi-view backbone that extracts image features, k-means clustering to identify scene-complexity-adaptive placement, and cross/self-attention with MLP decoding to predict Gaussian parameters. The result: fewer Gaussians, better reconstruction quality, and superior performance on pose-free imaging tasks.

**Why trending:** ETH Zürich CVG lab (Marc Pollefeys group) — high-credibility authors. 28 GitHub stars on day one. 3DGS is a hot area, and the insight of decoupling Gaussians from pixels is clean and impactful.

---

## 20. AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?
**Authors:** Zhangchen Xu, Junda Chen, Yue Huang, Dongfu Jiang, Jiefeng Chen, Hang Hua et al.
**ArXiv:** [arxiv.org/abs/2606.05080](https://arxiv.org/abs/2606.05080)
**GitHub:** [github.com/autolabhq/autolab](https://github.com/autolabhq/autolab) (⭐92) | **Project:** [autolab.moe](https://autolab.moe/)
**HF Upvotes:** 9 | **Comments:** 0

AutoLab is a benchmark for ultra long-horizon closed-loop optimization: agents must propose changes, run experiments, measure outcomes, and continuously refine artifacts across many iterations. Unlike existing benchmarks (single-turn or short-horizon), AutoLab captures the full iterative nature of scientific and engineering work. Evaluation reveals that persistent iteration and time awareness matter more than initial performance — frontier models plateau quickly without sustained refinement capability.

**Why trending:** 92 GitHub stars — highest of the day — driven by its ambitious scope and the AutoLab website. Directly targets the question of whether AI can do real R&D. Finding that "iteration matters more than initial quality" is a key insight for AI lab planning.
