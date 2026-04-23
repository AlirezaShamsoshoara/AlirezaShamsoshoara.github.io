---
title: "Daily AI Papers — April 23, 2026"
date: 2026-04-23
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-23/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal
  - reasoning
  - agents
---

## 1. LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model

- **Authors:** Inclusion AI, Tiwei Bie, Haoxing Chen, Tieyuan Chen, Zhenglin Cheng et al.
- **arXiv:** [arxiv.org/abs/2604.20796](https://arxiv.org/abs/2604.20796)
- **Summary:** Presents a unified discrete diffusion LLM combining a semantic discrete tokenizer (SigLIP-VQ), MoE-based dLLM backbone, and diffusion decoder for native multimodal understanding and generation. Matches specialized VLMs on understanding while delivering strong image generation and editing — with prefix-aware optimizations and few-step distillation for inference efficiency.
- **Sources:** HuggingFace Daily Papers (207 upvotes — runaway top of the day), GitHub (inclusionAI/LLaDA2.0-Uni — 50+ stars same day)
- **Why trending:** Massive HF spike (207 upvotes vs. 43 for #2). Discrete-diffusion unified models are the hot alternative to autoregressive omni-modal stacks; Inclusion AI's open release with code/models lit up the multimodal-research community.

## 2. Near-Future Policy Optimization (NPO)

- **Authors:** Chuanyu Qin, Chenxu Yang, Qingyi Si, Naibin Gu, Dingyu Yao
- **arXiv:** [arxiv.org/abs/2604.20733](https://arxiv.org/abs/2604.20733)
- **Summary:** A mixed-policy RLVR scheme that pulls auxiliary trajectories from the policy's own near-future checkpoint — both stronger than the current policy and closer than any external teacher, optimizing the effective learning signal S=Q/V. Validated on early-stage bootstrapping and late-stage plateau breakthrough.
- **Sources:** HuggingFace Daily Papers (43 upvotes)
- **Why trending:** RLVR plateau-breaking is one of the hottest threads in post-training right now; "future-self distillation" is an elegant, deployable trick.

## 3. DR-Venus: Frontier Edge-Scale Deep Research Agents with Only 10K Open Data

- **Authors:** Venus Team, Sunhao Dai, Yong Deng, Jinzhen Lin, Yusheng Song
- **arXiv:** [arxiv.org/abs/2604.19859](https://arxiv.org/abs/2604.19859)
- **Summary:** A 4B deep-research agent built entirely on ~10K open data via two-stage training: agentic SFT (with strict cleaning + long-horizon resampling) followed by IGPO-based agentic RL with information-gain turn-level rewards. Significantly outperforms prior <9B agentic models on multiple deep research benchmarks.
- **Sources:** HuggingFace Daily Papers (37 upvotes)
- **Why trending:** Edge-scale, fully-open deep-research agents are a counterweight to closed frontier agents — strong results from only 10K samples is a notable data-efficiency claim.

## 4. DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation

- **Authors:** Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo
- **arXiv:** [arxiv.org/abs/2604.20841](https://arxiv.org/abs/2604.20841)
- **Summary:** Uses text-conditioned synthetic interaction videos as imitation targets for physics-based dexterous control, bypassing the need for high-quality 3D mocap demonstrations. A hybrid 3D-human + 2D-object tracking reward overcomes the imprecision of generative 2D cues, enabling zero-shot generalization across unseen objects.
- **Sources:** HuggingFace Daily Papers (19 upvotes)
- **Why trending:** Robotics-from-video is the hottest scaling frontier for dexterous manipulation; using generative video instead of mocap is a high-leverage idea.

## 5. Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges

- **Authors:** Xiaohua Wang, Muzhao Tian, Yuqi Zeng, Zisu Huang, Jiakang Yuan
- **arXiv:** [arxiv.org/abs/2604.13602](https://arxiv.org/abs/2604.13602)
- **Summary:** A survey formalizing reward hacking via the Proxy Compression Hypothesis — exploitation as an emergent consequence of optimizing expressive policies against compressed reward representations. Catalogs failure modes (verbosity bias, sycophancy, hallucinated justification, evaluator manipulation, perception-reasoning decoupling) and links shortcut behaviors to broader misalignment.
- **Sources:** HuggingFace Daily Papers (19 upvotes)
- **Why trending:** Reward hacking is the central RLHF/RLVR pain point of 2026; a unifying framework + comprehensive taxonomy fills a real gap.

## 6. Exploring Spatial Intelligence from a Generative Perspective (GSI-Bench)

- **Authors:** Muzhi Zhu, Shunyao Jiang, Huanyi Zheng, Zekai Luo, Hao Zhong
- **arXiv:** [arxiv.org/abs/2604.20570](https://arxiv.org/abs/2604.20570)
- **Summary:** Introduces generative spatial intelligence — the ability of unified MLLMs to respect 3D spatial constraints during image generation — and GSI-Bench (real + synthetic) for measuring it. Strikingly, fine-tuning on synthetic spatial edits also improves downstream spatial understanding.
- **Sources:** HuggingFace Daily Papers (17 upvotes)
- **Why trending:** First evidence that generative training tangibly improves perception — a meaningful data-point in the "generation = understanding" debate.

## 7. TACO: Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression

- **Authors:** Jincheng Ren, Siwei Wu, Yizhi Li, Kang Zhu, Shu Xu
- **arXiv:** [arxiv.org/abs/2604.19572](https://arxiv.org/abs/2604.19572)
- **Summary:** A plug-and-play self-evolving compression framework for terminal agents that automatically discovers and refines compression rules from interaction trajectories, breaking the quadratic token-cost growth of long-horizon CLI tasks. Improves performance across SWE-Bench Lite, CompileBench, DevEval, CRUST-Bench, and TerminalBench while cutting tokens by ~10% with MiniMax-2.5.
- **Sources:** HuggingFace Daily Papers (15 upvotes)
- **Why trending:** Long-horizon terminal/coding agents (SWE-bench, TerminalBench) are the dominant agent benchmark suite; context compression is the inference-cost lever.

## 8. C-GenReg: Training-Free 3D Point Cloud Registration via Multi-View-Consistent Geometry-to-Image Generation

- **Authors:** Yuval Haitman, Amit Efraim, Joseph M. Francos
- **arXiv:** [arxiv.org/abs/2604.16680](https://arxiv.org/abs/2604.16680)
- **Summary:** Routes 3D point cloud registration through an auxiliary RGB image domain by synthesizing multi-view-consistent views from input geometry via a World Foundation Model, then using VFMs for dense correspondence — no fine-tuning required. A Match-then-Fuse probabilistic scheme combines generated-RGB and raw-geometry correspondences.
- **Sources:** HuggingFace Daily Papers (10 upvotes)
- **Why trending:** Training-free 3D pipelines that piggyback on world-models + VFMs are a practical pattern — generalization across sensors/environments is a live pain point.

## 9. WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training

- **Authors:** Yifu Chen, Shengpeng Ji, Qian Chen, Tianle Liang, Yangzhuo Li
- **arXiv:** [arxiv.org/abs/2604.14932](https://arxiv.org/abs/2604.14932)
- **Summary:** Modality-aware adaptive RL post-training recipe for end-to-end spoken dialogue models, constraining preference updates to the semantic channel while anchoring acoustic behavior, with rollout-statistic-driven mixture regulation. Consistently improves intelligence and expressiveness across spoken dialogue benchmarks and architectures.
- **Sources:** HuggingFace Daily Papers (9 upvotes)
- **Why trending:** Voice-native models (post Sesame, post Qwen-Omni) need a clean RL recipe — sparse-preference + dense-speech is a real gap this paper attacks.

## 10. SWE-chat: Coding Agent Interactions From Real Users in the Wild

- **Authors:** Joachim Baumann, Vishakh Padmakumar, Xiang Li, John Yang, Diyi Yang
- **arXiv:** [arxiv.org/abs/2604.20779](https://arxiv.org/abs/2604.20779)
- **Summary:** First large-scale dataset of real coding-agent sessions (6K sessions, 63K user prompts, 355K tool calls) collected from open-source devs in the wild. Finds bimodal usage (41% "vibe coding", 23% all-human), only 44% of agent code survives into commits, and agent code introduces more security vulnerabilities than human code.
- **Sources:** HuggingFace Daily Papers (6 upvotes), NLP/agents communities
- **Why trending:** Empirical, in-the-wild data on agent usage cuts through marketing claims — the 44% survival rate and security findings are quotable.

## 11. Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL

- **Authors:** Skylar Zhai, Jingcheng Liang, Dongyeop Kang
- **arXiv:** [arxiv.org/abs/2604.17073](https://arxiv.org/abs/2604.17073)
- **Summary:** A clarification-aware RLVR reward that rewards correct answers on answerable queries while jointly optimizing explicit abstention and semantically aligned post-refusal clarification on unanswerable ones. The 3B Abstain-R1 matches DeepSeek-R1 on unanswerable-query behavior while preserving answerable performance.
- **Sources:** HuggingFace Daily Papers (5 upvotes)
- **Why trending:** Hallucination-via-guessing is the next frontier after reasoning RL — and a 3B model matching R1 on abstention is a strong data-efficiency story.

## 12. Image Generators are Generalist Vision Learners (Vision Banana)

- **Authors:** Valentin Gabeur, Shangbang Long, Songyou Peng, Paul Voigtlaender, Shuyang Sun
- **arXiv:** [arxiv.org/abs/2604.20329](https://arxiv.org/abs/2604.20329)
- **Summary:** Reframes perception as image generation: instruction-tunes Nano Banana Pro on a mixture of original training data + small vision-task data, parameterizing vision-task outputs as RGB images. Vision Banana achieves SOTA on diverse 2D/3D vision tasks, beating zero-shot specialists including Segment Anything Model 3.
- **Sources:** HuggingFace Daily Papers (4 upvotes), Google research channels
- **Why trending:** "Generation pretraining = vision pretraining" is the splashy claim; beating SAM 3 with a generalist is a headline result.

## 13. Cortex 2.0: Grounding World Models in Real-World Industrial Deployment

- **Authors:** Adriana Aida, Walida Amer, Katarina Bankovic, Dhruv Behl, Fabian Busch
- **arXiv:** [arxiv.org/abs/2604.20246](https://arxiv.org/abs/2604.20246)
- **Summary:** Shifts industrial robotic manipulation from reactive Vision-Language-Action policies to a plan-and-act framework that generates candidate future trajectories in visual latent space, scores them, and commits to the best. Outperforms SOTA VLA baselines across pick-and-place, sorting, screw sorting, and shoebox unpacking, including in cluttered/contact-rich environments.
- **Sources:** HuggingFace Daily Papers (4 upvotes)
- **Why trending:** World-model-based planning vs. reactive VLA is a key architectural debate in robotics; real-deployment results carry weight.

## 14. Tadabur: A Large-Scale Quran Audio Dataset

- **Authors:** Faisal Alherran
- **arXiv:** [arxiv.org/abs/2604.18932](https://arxiv.org/abs/2604.18932)
- **Summary:** Releases a large-scale Quran audio dataset with 1400+ hours of recitation from over 600 distinct reciters, providing variation in recitation styles, vocal characteristics, and recording conditions. Aims to support standardized Quranic speech benchmarks.
- **Sources:** HuggingFace Daily Papers (4 upvotes)
- **Why trending:** Underserved-language/domain audio datasets fill gaps in TTS/ASR research; community-resource papers consistently trend on HF.

## 15. Scaling Test-Time Compute for Agentic Coding (RTV + PDR)

- **Authors:** Joongwon Kim, Wannan Yang, Kelvin Niu, Hongming Zhang, Yun Zhu
- **arXiv:** [arxiv.org/abs/2604.16529](https://arxiv.org/abs/2604.16529)
- **Summary:** Test-time scaling framework for long-horizon coding agents based on compact rollout-trajectory summaries that preserve hypotheses, progress, and failure modes. Introduces Recursive Tournament Voting (parallel) and adapts Parallel-Distill-Refine (sequential) to the agentic setting.
- **Sources:** HuggingFace Daily Papers (4 upvotes)
- **Why trending:** Test-time compute for agents is the natural extension of TTC for reasoning — coding-agent benchmarks make it directly measurable.

## 16. Convergent Evolution: How Different Language Models Learn Similar Number Representations

- **Authors:** Deqing Fu, Tianyi Zhou, Mikhail Belkin, Vatsal Sharan, Robin Jia
- **arXiv:** [arxiv.org/abs/2604.20817](https://arxiv.org/abs/2604.20817)
- **Summary:** Identifies a two-tier hierarchy in number-feature learning: Transformers, RNNs, LSTMs, and word embeddings all learn periodic Fourier features (T=2,5,10), but only some learn geometrically separable features for mod-T classification. Proves Fourier sparsity is necessary but not sufficient, and traces separability to data, architecture, optimizer, and tokenizer.
- **Sources:** HuggingFace Daily Papers (3 upvotes)
- **Why trending:** Mechanistic-interpretability + universality result with solid theory; Belkin/Jia carry weight in this corner of the field.

## 17. SAVOIR: Learning Social Savoir-Faire via Shapley-based Reward Attribution

- **Authors:** Xiachong Feng, Yi Jiang, Xiaocheng Feng, Deyi Yin, Libo Qin
- **arXiv:** [arxiv.org/abs/2604.18982](https://arxiv.org/abs/2604.18982)
- **Summary:** Cooperative-game-theory framework for credit assignment in multi-turn social dialogue RL, combining expected-utility prospective valuation with Shapley-value fairness guarantees. The 7B SAVOIR matches/exceeds GPT-4o and Claude-3.5-Sonnet on the SOTOPIA social-intelligence benchmark.
- **Sources:** HuggingFace Daily Papers (3 upvotes)
- **Why trending:** Principled credit-assignment for multi-turn agents + a 7B beating frontier proprietary models on SOTOPIA is a punchy headline.

## 18. Visual Reasoning through Tool-supervised Reinforcement Learning (ToolsRL)

- **Authors:** Qihua Dong, Gozde Sahin, Pei Wang, Zhaowei Cai, Robik Shrestha
- **arXiv:** [arxiv.org/abs/2604.19945](https://arxiv.org/abs/2604.19945)
- **Summary:** Two-stage RL curriculum for MLLM tool use: stage one optimizes simple tool-specific rewards (zoom, rotate, flip, draw point/line), stage two trains accuracy rewards while allowing tool calls. Avoids optimization conflict between learning to call tools and using them for visual reasoning.
- **Sources:** HuggingFace Daily Papers (3 upvotes)
- **Why trending:** Tool-use is the active frontier for MLLMs; native interpretable visual tools (zoom/draw) are particularly attractive for grounding.

## 19. Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts

- **Authors:** Chaitanya Dwivedi, Binxuan Huang, Himanshu Gupta, Pratik Jayarao, Neeraj Varshney
- **arXiv:** [arxiv.org/abs/2604.19835](https://arxiv.org/abs/2604.19835)
- **Summary:** Progressively expands MoE capacity by duplicating experts and extending the router during continued pre-training, holding top-K routing fixed and preserving per-token inference cost. Duplication provides a warm initialization that beats random expert init, and CPT then breaks symmetry to drive specialization.
- **Sources:** HuggingFace Daily Papers (3 upvotes)
- **Why trending:** MoE scaling is the dominant frontier-model architecture; cost-efficient ways to grow expert count without retraining shifts the Pareto frontier.

## 20. Self-Evolving LLM Memory Extraction Across Heterogeneous Tasks (CluE / BEHEMOTH)

- **Authors:** Yuqing Yang, Tengxiao Liu, Wang Bill Zhu, Taiwei Shi, Linxin Song
- **arXiv:** [arxiv.org/abs/2604.11610](https://arxiv.org/abs/2604.11610)
- **Summary:** Formalizes heterogeneous memory extraction and releases BEHEMOTH (18 datasets across personalization, problem-solving, agentic). Proposes CluE, a cluster-based self-evolving prompt-optimization strategy that groups training examples by extraction scenario, analyzes each cluster, and synthesizes cross-cluster insights — +9.04% relative gain over prior self-evolving frameworks.
- **Sources:** HuggingFace Daily Papers (3 upvotes)
- **Why trending:** Persistent agent memory is the next major axis after long context; benchmarking + a self-evolving solution lands at the right time.
