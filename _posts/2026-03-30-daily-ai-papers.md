---
title: 'Daily AI Papers — March 30, 2026'
date: 2026-03-30
permalink: /blog/ai-papers/2026/03/daily-ai-papers-03-30/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-systems
  - video-generation
  - long-context
---

## 1. Composer 2 Technical Report
**Authors:** Cursor Research (Aaron Chan, Ahmed Shalaby, Alexander Wettig et al.)
**Summary:** Cursor's new model for agentic software engineering. Trained in two phases: continued pretraining for coding knowledge, then large-scale RL for agentic behavior. Demonstrates strong long-term planning and coding intelligence while staying efficient for interactive use. This is the model powering Cursor's code editor.
**Link:** [arxiv.org/abs/2603.24477](https://arxiv.org/abs/2603.24477)
**Source:** HuggingFace trending + widespread discussion on Twitter/X and Reddit
**Why trending:** Major product release from Cursor, one of the most-used AI coding tools. First detailed technical report on their proprietary model.

## 2. Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale
**Authors:** Yicheng Zou, Dongsheng Zhu, Lin Zhu, Tong Zhu, Yunhua Zhou et al.
**Summary:** The first one-trillion-parameter scientific multimodal foundation model. Delivers comprehensive enhancements across general and scientific domains with advanced agent capabilities. A major scale milestone for scientific AI.
**Link:** [arxiv.org/abs/2603.25040](https://arxiv.org/abs/2603.25040)
**Source:** HuggingFace trending (top paper on Mar 29), arxiv cs.AI
**Why trending:** First 1T-parameter scientific model. Scale milestone that drew immediate attention from the research community.

## 3. Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?
**Authors:** Richard J. Young
**Summary:** Examines whether reasoning models actually use the chain-of-thought they verbalize, or just rationalize post-hoc. Prior work found acknowledgment rates as low as 25% for certain factors. Critical paper for AI safety -- if CoT isn't faithful, it can't serve as a transparency mechanism.
**Link:** [arxiv.org/abs/2603.22582](https://arxiv.org/abs/2603.22582)
**Source:** HuggingFace trending, arxiv cs.CL
**Why trending:** Directly challenges the assumption that CoT = interpretability. High relevance to safety and alignment debates.

## 4. MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens
**Authors:** Yu Chen, Runkai Chen, Sheng Yi, Xinda Zhao, Xiaohong Li et al.
**Summary:** Tackles the holy grail of long-context: scaling to 100 million tokens. Proposes Memory Sparse Attention that overcomes the limitations of full-attention architectures (typically capped at ~1M tokens). Uses sparse attention over memory states instead of fixed-size compressed representations.
**Link:** [arxiv.org/abs/2603.23516](https://arxiv.org/abs/2603.23516)
**Source:** HuggingFace trending (Mar 29), arxiv cs.LG
**Why trending:** 100M token context is a 100x jump over current limits. Directly relevant to anyone building long-context applications.

## 5. Voxtral TTS
**Authors:** Alexander H. Liu, Alexis Tacnet, Andy Ehrenberg, Andy Lo, Chen-Yo Sun et al. (Mistral)
**Summary:** Mistral's expressive multilingual text-to-speech model. Generates natural speech from just 3 seconds of reference audio. Hybrid architecture combining autoregressive semantic tokens with flow-matching for acoustic tokens. Uses Voxtral Codec, a speech tokenizer trained from scratch.
**Link:** [arxiv.org/abs/2603.25551](https://arxiv.org/abs/2603.25551)
**Source:** HuggingFace trending (Mar 29), Mistral blog announcement
**Why trending:** Major lab (Mistral) entering TTS space. 3-second voice cloning is state-of-the-art for open models.

## 6. Learning to Commit: Generating Organic Pull Requests via Online Repository Memory
**Authors:** Mo Li, L. H. Xu, Qitai Tan, Ting Cao, Yunxin Liu
**Summary:** Addresses why LLM coding agents pass benchmarks but get rejected by real maintainers. The problem isn't functional correctness but "organicity" -- generated code ignores project conventions, duplicates existing APIs, and violates implicit architectural constraints. Proposes online repository memory for learning project-specific norms.
**Link:** [arxiv.org/abs/2603.26664](https://arxiv.org/abs/2603.26664)
**Source:** HuggingFace trending (Mar 30)
**Why trending:** Hits a pain point every developer has experienced with AI-generated PRs. Highly practical and timely.

## 7. Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills
**Authors:** Jingwei Ni, Yihao Liu, Xinpeng Liu, Yutao Sun, Mengyu Zhou et al.
**Summary:** Tackles the bottleneck of equipping LLM agents with domain-specific skills. Manual authoring doesn't scale; automated generation produces fragile results. Proposes distilling trajectory-local lessons into transferable skills that generalize beyond specific execution traces.
**Link:** [arxiv.org/abs/2603.25158](https://arxiv.org/abs/2603.25158)
**Source:** HuggingFace trending (Mar 30), arxiv cs.AI
**Why trending:** Agent skill acquisition is a hot topic. This proposes a scalable alternative to manual skill engineering.

## 8. SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks
**Authors:** Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu et al.
**Summary:** Reveals that coding agents can pass test suites but produce code that becomes progressively harder to extend. Proposes a benchmark for measuring how code quality degrades over iterative development -- a blind spot in current single-shot benchmarks.
**Link:** [arxiv.org/abs/2603.24755](https://arxiv.org/abs/2603.24755)
**Source:** HuggingFace trending (Mar 29), arxiv cs.SE
**Why trending:** Exposes a fundamental gap in how we evaluate coding agents. "Slop code" is a term that resonated widely.

## 9. Natural-Language Agent Harnesses
**Authors:** Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng
**Summary:** Agent performance increasingly depends on "harness engineering" -- the control logic around an agent. This paper externalizes harness design as a portable, executable artifact written in natural language rather than buried in controller code, making agent harnesses transferable and comparable.
**Link:** [arxiv.org/abs/2603.25723](https://arxiv.org/abs/2603.25723)
**Source:** HuggingFace trending (Mar 30)
**Why trending:** Novel framing of agent orchestration as a first-class research object. Relevant to the growing agent infrastructure ecosystem.

## 10. PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference
**Authors:** Xiaofeng Mao, Shaohao Rui, Kaining Ying, Bo Zheng, Chuanhao Li et al.
**Summary:** Tackles the core bottleneck of autoregressive video diffusion: linear KV-cache growth, temporal repetition, and compounding errors during long-video generation. Introduces a three-partition KV-cache strategy that enables training on short videos while generating long ones.
**Link:** [arxiv.org/abs/2603.25730](https://arxiv.org/abs/2603.25730)
**Source:** HuggingFace trending (Mar 30), arxiv cs.CV
**Why trending:** Practical solution to a major video generation bottleneck. Decouples training length from generation length.

## 11. ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling
**Authors:** Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu et al.
**Summary:** Enables interactive long-form video storytelling. Reformulates multi-shot video as next-shot generation conditioned on historical context, using a causal architecture for streaming generation with low latency.
**Link:** [arxiv.org/abs/2603.25746](https://arxiv.org/abs/2603.25746)
**Source:** HuggingFace trending (Mar 30)
**Why trending:** Interactive video generation is a frontier application. Causal architecture enables real-time use cases.

## 12. Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models
**Authors:** Kaijin Chen, Dingkang Liang, Xin Zhou, Yikang Ding, Xiaoqiang Liu et al.
**Summary:** Video world models treat environments as static canvases. When objects hide and re-emerge, current methods produce frozen, distorted, or vanishing subjects. Proposes Hybrid Memory for tracking visible and hidden dynamic subjects.
**Link:** [arxiv.org/abs/2603.25716](https://arxiv.org/abs/2603.25716)
**Source:** HuggingFace trending (Mar 30, #1 position)
**Why trending:** Addresses a fundamental limitation of video world models. Strong demo results.

## 13. Sommelier: Scalable Open Multi-turn Audio Pre-processing for Full-duplex Speech Language Models
**Authors:** Kyudan Jung, Jihwan Kim, Soyoon Kim, Jeongoon Kim, Jaegul Choo et al.
**Summary:** Full-duplex real-time conversation requires multi-speaker conversational data that's currently scarce. Sommelier provides a scalable pipeline for creating this data for speech language models.
**Link:** [arxiv.org/abs/2603.25750](https://arxiv.org/abs/2603.25750)
**Source:** HuggingFace trending (Mar 30)
**Why trending:** Solves a data bottleneck for the next generation of voice AI (full-duplex conversation).

## 14. MedOpenClaw: Auditable Medical Imaging Agents Reasoning over Uncurated Full Studies
**Authors:** Weixiang Shen, Yanzhu Hu, Che Liu, Junde Wu, Jiayuan Zhu et al.
**Summary:** Real clinical agents must navigate full 3D volumes across modalities, not pre-selected 2D images. MedOpenClaw is an auditable agent that reasons over uncurated, full medical imaging studies.
**Link:** [arxiv.org/abs/2603.24649](https://arxiv.org/abs/2603.24649)
**Source:** HuggingFace trending (Mar 30), arxiv cs.CV
**Why trending:** Bridges the gap between benchmark medical AI and real clinical workflows. Auditability is key for healthcare adoption.

## 15. Calibri: Enhancing Diffusion Transformers via Parameter-Efficient Calibration
**Authors:** Danil Tokhchukov, Aysel Mirzoeva, Andrey Kuznetsov, Konstantin Sobolev
**Summary:** A single learned scaling parameter can significantly improve DiT blocks. Calibri is a parameter-efficient approach that unlocks hidden potential in existing diffusion architectures without retraining.
**Link:** [arxiv.org/abs/2603.24800](https://arxiv.org/abs/2603.24800)
**Source:** HuggingFace trending (Mar 29), arxiv cs.CV
**Why trending:** Surprisingly simple technique with strong results. Low barrier to adoption.

## 16. RealChart2Code: Advancing Chart-to-Code Generation with Real Data
**Authors:** Jiajun Zhang, Yuying Li, Zhixun Li, Xingyu Guo, Jingzhuo Wu et al.
**Summary:** New large-scale benchmark (2,800+ instances) for evaluating VLMs on replicating complex, multi-panel visualizations from real-world data.
**Link:** [arxiv.org/abs/2603.25804](https://arxiv.org/abs/2603.25804)
**Source:** HuggingFace trending (Mar 30)
**Why trending:** Practical benchmark for a common use case (chart reproduction). Fills a gap in VLM evaluation.

## 17. GenMask: Adapting DiT for Segmentation via Direct Mask Generation
**Authors:** Yuhuan Yang, Xianwei Zhuang, Yuxuan Cai, Chaofan Ma, Shuai Bai et al.
**Summary:** Instead of using generative models as indirect feature extractors for segmentation, proposes directly generating masks with Diffusion Transformers. Eliminates representation misalignment.
**Link:** [arxiv.org/abs/2603.23906](https://arxiv.org/abs/2603.23906)
**Source:** HuggingFace trending (Mar 30), arxiv cs.CV
**Why trending:** Clean rethink of how to use DiTs for segmentation. Simplifies the pipeline significantly.

## 18. Know3D: Prompting 3D Generation with Knowledge from Vision-Language Models
**Authors:** Wenyue Chen, Wenjue Chen, Peng Li, Qinghe Wang, Xu Jia et al.
**Summary:** Uses VLM knowledge as structural priors to guide single-view 3D asset generation, producing more controllable results for unseen views.
**Link:** [arxiv.org/abs/2603.22782](https://arxiv.org/abs/2603.22782)
**Source:** HuggingFace trending (Mar 30), arxiv cs.CV
**Why trending:** Practical approach to a hard problem (single-view 3D). Leverages existing VLM capabilities creatively.

## 19. Diffutron: A Masked Diffusion Language Model for Turkish Language
**Authors:** Suayp Talha Kocabay, Talha Ruzgar Akkus
**Summary:** First masked diffusion language model for a morphologically rich language (Turkish). Demonstrates non-autoregressive diffusion LMs work for agglutinative languages.
**Link:** [arxiv.org/abs/2603.20466](https://arxiv.org/abs/2603.20466)
**Source:** HuggingFace trending (Mar 30)
**Why trending:** Extends diffusion language modeling beyond English/Chinese to morphologically complex languages. Niche but novel.

## 20. LongTail Driving Scenarios with Reasoning Traces: The KITScenes LongTail Dataset
**Authors:** Royden Wagner, Omer Sahin Tas, Jaime Villa, Felix Hauser, Yinzhe Shen et al.
**Summary:** Dataset for end-to-end driving focused on rare long-tail events. Includes multi-view video, trajectories, instructions, and reasoning traces for in-context learning.
**Link:** [arxiv.org/abs/2603.23607](https://arxiv.org/abs/2603.23607)
**Source:** HuggingFace trending (Mar 30), arxiv cs.CV
**Why trending:** Long-tail generalization is the key unsolved problem in autonomous driving. Reasoning traces enable new training approaches.

---

## Methodology

| Source | URL | Signal |
|--------|-----|--------|
| HuggingFace Trending | huggingface.co/papers | Community upvotes (primary ranking signal) |
| HuggingFace Daily | huggingface.co/papers?date=YYYY-MM-DD | Papers from past 2-3 days still gaining traction |
| arxiv cs.CL | arxiv.org/list/cs.CL/current | NLP/language model submissions |
| arxiv cs.LG | arxiv.org/list/cs.LG/current | General ML submissions |
| arxiv cs.AI | arxiv.org/list/cs.AI/current | AI submissions |
| Web search | Various | Major lab blogs, Twitter/X threads, Reddit r/MachineLearning |

Papers are ranked by: HuggingFace position > lab prestige > cross-platform buzz > topic relevance.

*Generated by Jarvis | Next report: March 31, 2026 at 10:00 AM PT*
