---
title: "Daily AI Papers — June 15, 2026"
date: 2026-06-15
permalink: /blog/ai-papers/2026/06/daily-ai-papers-06-15/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agentic-rl
  - multimodal-ai
  - video-generation
---

## 1. OmniDirector: General Multi-Shot Camera Cloning without Cross-Paired Data
**Authors:** Jiwen Liu, Shujuan Li, Zhixue Fang, Xiaohan Li, Yan Zhou, Zijie Meng, Zhimin Zhang, Yawen Luo, Guoxin Zhang, Yu-Shen Liu, Pengfei Wan (Kling Team)

OmniDirector introduces a novel camera motion representation that encodes camera trajectories as grid motion videos, enabling precise multi-shot camera cloning without needing cross-paired training data. A hierarchical prompt expansion agent unifies character, action, and camera controls within multimodal diffusion transformers, trained on a million-scale dataset for director-level video generation.

**arXiv:** [arxiv.org/abs/2606.13432](https://arxiv.org/abs/2606.13432)
**Sources:** HuggingFace Daily Papers (91 upvotes), GitHub (27 stars), arXiv cs.CV
**Why trending:** Top upvoted paper of the day from Kling Team; solves multi-shot camera cloning — a real creative production pain point — without requiring paired training data.

---

## 2. APPO: Agentic Procedural Policy Optimization
**Authors:** Xucong Wang, Ziyu Ma, Yong Wang, Yuxiang Ji, Shidong Yang, Guanhua Chen, Pengkun Wang, Xiangxiang Chu

APPO improves agentic RL by moving branching and credit assignment from coarse tool-call boundaries to fine-grained decision points in the sequence. A Branching Score combining token uncertainty with policy-induced likelihood gains selects where to explore, while procedure-level advantage scaling better distributes credit — yielding nearly +4 points across 13 benchmarks.

**arXiv:** [arxiv.org/abs/2606.12384](https://arxiv.org/abs/2606.12384)
**Sources:** HuggingFace Daily Papers (61 upvotes), GitHub (53 stars), arXiv cs.AI
**Why trending:** Agentic RL is the hot research area right now; APPO addresses the fundamental credit assignment problem with strong multi-benchmark results and solid GitHub traction.

---

## 3. Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents
**Authors:** Shuo Ji, Yibo Li, Bryan Hooi (National University of Singapore)

MRAgent proposes replacing the static retrieve-then-reason memory pipeline with an associative memory graph and active reconstruction mechanism that dynamically adapts memory access to intermediate evidence discovered during inference. This lets agents reason over long interaction histories without being bottlenecked by a rigid retrieval step.

**arXiv:** [arxiv.org/abs/2606.06036](https://arxiv.org/abs/2606.06036)
**Sources:** HuggingFace Daily Papers (53 upvotes), GitHub (51 stars), arXiv cs.AI
**Why trending:** Memory is a core bottleneck for deployed agents; the graph-based reconstruction framing is a compelling departure from standard RAG approaches, reflected in strong community engagement.

---

## 4. From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomous AI
**Authors:** Yongheng Zhang, Ziang Liu, Jiaxuan Zhu, Shuai Wang, Xiangqi Chen

This survey conceptualizes the transition of LLMs from conversational generators to "Digital Colleagues" — persistent systems that reason, act, and self-improve across cognitive core and embodied action dimensions. It organizes the evolving architecture of autonomous AI along both the capability and deployment axes.

**arXiv:** [arxiv.org/abs/2606.14502](https://arxiv.org/abs/2606.14502)
**Sources:** HuggingFace Daily Papers (41 upvotes), arXiv cs.AI
**Why trending:** Captures the moment the field is at — transitioning from chatbots to autonomous systems — resonating broadly with practitioners and researchers across the community.

---

## 5. Orchestra-o1: Omnimodal Agent Orchestration
**Authors:** Fan Zhang, Vireo Zhang, Shengju Qian, Haoxuan Li, Hao Wu (The Chinese University of Hong Kong)

Orchestra-o1 extends multi-agent orchestration to heterogeneous modalities (text, image, video, audio, 3D), where existing frameworks fail because they assume homogeneous agents. The system introduces orchestration policies that decompose omnimodal tasks and coordinate specialist agents, enabling generalization to complex real-world multi-modal scenarios.

**arXiv:** [arxiv.org/abs/2606.13707](https://arxiv.org/abs/2606.13707)
**Sources:** HuggingFace Daily Papers (37 upvotes), GitHub (39 stars), arXiv cs.AI
**Why trending:** Multi-agent systems are increasingly the deployment paradigm; extending orchestration to all modalities in one coherent framework addresses an obvious gap.

---

## 6. HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry
**Authors:** Tingyang Chen, Shuo Lu, Kang Zhao, Weicheng Meng, Hanlin Teng

HarnessX is a meta-framework for building agent harnesses that are composable (mix-and-match prompts, tools, memory, control flow), adaptive (self-modifying based on execution traces), and evolvable (traces feed back into systematic improvement rather than being discarded). It addresses the bespoke scaffolding tax that consumes engineering effort for each new model or task.

**arXiv:** [arxiv.org/abs/2606.14249](https://arxiv.org/abs/2606.14249)
**Sources:** HuggingFace Daily Papers (33 upvotes), arXiv cs.AI
**Why trending:** Every team building agents faces the scaffolding problem; HarnessX's composable foundry approach offers a principled solution that resonates with practitioners.

---

## 7. Rethinking RAG in Long Videos: What to Retrieve and How to Use It?
**Authors:** Yuho Lee, Jisu Shin, Nicole Hee-Yeon Kim, Jihwan Bang, Juntae Lee (Data Intelligence System Lab)

The authors introduce V-RAGBench, exposing two gaps in VideoRAG: benchmarks that allow video-free answering (masking retrieval failures) and methods that apply a fixed modality-granularity config per query despite chunk-level variability. Their framework addresses both by requiring true video-grounded retrieval and dynamic multi-modal, multi-granularity chunk selection.

**arXiv:** [arxiv.org/abs/2606.13141](https://arxiv.org/abs/2606.13141)
**Sources:** HuggingFace Daily Papers (32 upvotes), arXiv cs.CV, arXiv cs.IR
**Why trending:** VideoRAG is rapidly maturing; exposing fundamental benchmark and method flaws with a rigorous replacement drives high community interest.

---

## 8. From AGI to ASI
**Authors:** Tim Genewein, Matija Franklin, Alexander Lerchner, Laurent Orseau, Samuel Albanie (Google DeepMind)

A Google DeepMind report investigating what the continuum of machine intelligence looks like in a post-AGI world, tracing the path from human-level AI toward Artificial Superintelligence (ASI). It examines societal implications, capability trajectories, and the complex questions that arise when AI development continues past human-level performance.

**arXiv:** [arxiv.org/abs/2606.12683](https://arxiv.org/abs/2606.12683)
**Sources:** HuggingFace Daily Papers (23 upvotes), Google DeepMind blog, arXiv cs.AI
**Why trending:** DeepMind authorship + AGI/ASI framing makes this required reading for anyone tracking frontier AI development; timing aligns with mainstream AGI discourse hitting a peak.

---

## 9. OmniVideo-100K: A Dataset for Audio-Visual Reasoning through Structured Scripts and Evidence Chains
**Authors:** Xinyue Cai, Chaoyou Fu, Yi-Fan Zhang, Ran He, Caifeng Shan (Nanjing University)

OmniVideo-100K addresses the decoupled audio-visual pipeline problem in video QA by building a 100K-sample dataset where each entry is grounded in structured scripts and multi-hop evidence chains linking sounds to their visual sources. The result is richer, more coherent cross-modal reasoning supervision that prevents entity inconsistency across clips.

**arXiv:** [arxiv.org/abs/2606.14702](https://arxiv.org/abs/2606.14702)
**Sources:** HuggingFace Daily Papers (21 upvotes), GitHub (29 stars), arXiv cs.CV
**Why trending:** Audio-visual reasoning is an underserved area; the scale and evidence-chain structure of the dataset make it a high-value contribution for multimodal research.

---

## 10. Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO
**Authors:** Yiming Ren, Yiran Xu, Zicheng Lin, Chufan Shi, Yukang Chen

This paper identifies that smaller models within the same family exhibit higher policy-level diversity than larger ones (better pass@k despite weaker pass@1), making them natural explorers in GRPO rollout generation. Leveraging smaller sibling models as diverse proposers — rather than injecting token-level noise — produces cleaner, more coherent training trajectories.

**arXiv:** [arxiv.org/abs/2605.30789](https://arxiv.org/abs/2605.30789)
**Sources:** HuggingFace Daily Papers (18 upvotes), GitHub (13 stars), arXiv cs.LG
**Why trending:** GRPO is widely used for post-training; the insight that model size itself is a diversity knob is simple, surprising, and immediately actionable.

---

## 11. RedAct: Redacting Agent Capability Traces for Procedural Skill Protection
**Authors:** Shuwen Xu, Zhitao He, Yi R. Fung

RedAct addresses the IP leakage problem in agent execution traces: the rich procedural detail (tool calls, thresholds, strategies) that makes traces useful for debugging also exposes proprietary skills to competitors. The framework selectively redacts capability-revealing trace content while preserving enough information for legitimate accountability.

**arXiv:** [arxiv.org/abs/2606.10813](https://arxiv.org/abs/2606.10813)
**Sources:** HuggingFace Daily Papers (15 upvotes), GitHub (12 stars), arXiv cs.AI
**Why trending:** As commercial agent deployments grow, procedural IP protection becomes a real concern; RedAct is the first explicit treatment of this problem.

---

## 12. Measuring Epistemic Resilience of LLMs Under Misleading Medical Context
**Authors:** Hongjian Zhou, Xinyu Zou, Jinge Wu, Sean Wu, Junchi Yu (University of Oxford)

The paper shows that LLMs achieving expert-level scores on medical licensing exams are fragile: injecting misleading context into questions they originally answer correctly causes them to abandon the right answer at high rates. The authors define "epistemic resilience" as the capacity to maintain correct beliefs under adversarial pressure — a property current models lack.

**arXiv:** [arxiv.org/abs/2606.12291](https://arxiv.org/abs/2606.12291)
**Sources:** HuggingFace Daily Papers (13 upvotes), University of Oxford, arXiv cs.CL
**Why trending:** Medical AI safety is a high-stakes area; the finding that benchmark scores dramatically overstate real-world robustness has broad regulatory and deployment implications.

---

## 13. Skip a Layer or Loop It? Learning Program-of-Layers in LLMs
**Authors:** Ziyue Li, Yang Li, Tianyi Zhou (University of Maryland)

PoLar reveals that pretrained LLM layers can be organized into dynamic, input-specific programs — skipping some layers and looping others — without any fine-tuning. This training-free approach achieves substantial inference speedups on most inputs while maintaining quality, by exploiting the wide redundancy in fixed-depth forward passes.

**arXiv:** [arxiv.org/abs/2606.06574](https://arxiv.org/abs/2606.06574)
**Sources:** HuggingFace Daily Papers (13 upvotes), GitHub (9 stars), arXiv cs.LG
**Why trending:** Training-free inference acceleration is extremely valuable for deployment; the layer-program framing is novel and the results are immediately usable.

---

## 14. LLM Agents Can See Code Repositories
**Authors:** Dongjian Ma, Silin Chen, Yufei Yang, Yulin Shi, Yanfu Yan (Shanghai Jiao Tong University)

SeeRepo gives coding agents visual access to repository structure — folder hierarchies, dependency graphs — in addition to text, mimicking how human developers orient themselves in large codebases. The multimodal approach improves software engineering task performance by grounding agents in the visual architecture humans use to navigate code.

**arXiv:** [arxiv.org/abs/2606.14061](https://arxiv.org/abs/2606.14061)
**Sources:** HuggingFace Daily Papers (11 upvotes), GitHub (9 stars), arXiv cs.SE
**Why trending:** Coding agents are a top deployment priority; the visual repo structure idea is intuitive and elegant, addressing a real gap in text-only agent interfaces.

---

## 15. iMaC: Translating Actions into Motion and Contact Images for Embodied World Models
**Authors:** Zhenyu Wu, Xiuwei Xu, Yukun Zhou, Yifan Li, Qiuping Deng

iMaC replaces low-dimensional action vectors (joint angles, end-effector poses) with image-format motion and contact representations that are visually expressive and embodiment-agnostic. This reformulation integrates naturally with vision-based world models and improves generalization across diverse robot embodiments.

**arXiv:** [arxiv.org/abs/2606.09813](https://arxiv.org/abs/2606.09813)
**Sources:** HuggingFace Daily Papers (9 upvotes), GitHub (14 stars), arXiv cs.RO
**Why trending:** Embodied AI is rapidly growing; representing actions as images is a clever unification that makes robot learning more compatible with the powerful vision-language model ecosystem.

---

## 16. RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space
**Authors:** Xichen Pan, Aashu Singh, Satya Narayan Shukla, Xiangjun Fan, Shlok Kumar Mishra (Meta AI)

RepFusion proposes using pretrained LLM representations (from representation autoencoders) as the generation target in text-to-image diffusion, creating a latent space that is more semantically compatible with LLM priors than pixel or VAE latents. The approach enables better utilization of frozen LLM knowledge for denoising without training new generative backbones.

**arXiv:** [arxiv.org/abs/2606.14700](https://arxiv.org/abs/2606.14700)
**Sources:** HuggingFace Daily Papers (7 upvotes), Meta AI, arXiv cs.CV
**Why trending:** Meta FAIR authorship + novel representation-space denoising approach bridges the gap between language and image generation in an interesting way.

---

## 17. Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack
**Authors:** He Zhang, Lingzhu Xiang, Haitao Lin, Zeyu Huang, Minghui Wang (Tencent Hunyuan)

HyVLA-0.5 presents Tencent Hunyuan's end-to-end robot learning stack covering data collection, model design, continued pretraining, supervised fine-tuning, RL post-training, and real-world deployment in a single report. Each component is designed to work together across the full stack, with results on real robotic manipulation tasks.

**arXiv:** [arxiv.org/abs/2606.14409](https://arxiv.org/abs/2606.14409)
**Sources:** HuggingFace Daily Papers (8 upvotes), Tencent Hunyuan, arXiv cs.RO
**Why trending:** Full-stack embodied AI reports from major labs (Tencent Hunyuan) are rare and valuable; practitioners can learn from the complete pipeline rather than isolated components.

---

## 18. The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment
**Authors:** Filippo Tonini, Federico Torrielli, Anton Danholt Lautrup, Peter Schneider-Kamp, Mustafa Mert Çelikok (University of Southern Denmark)

The Arbiter is an independent monitor agent that watches multi-agent conversations for emergent misalignment — cases where individually well-aligned agents collectively exhibit problematic behavior through their interactions. It continuously evaluates conversational trajectories rather than individual agent outputs, catching alignment failures that per-agent testing misses.

**arXiv:** [arxiv.org/abs/2606.10747](https://arxiv.org/abs/2606.10747)
**Sources:** HuggingFace Daily Papers (6 upvotes), GitHub (5 stars), arXiv cs.AI
**Why trending:** Multi-agent systems are being deployed at scale; emergent misalignment that appears only in multi-agent interaction is a safety blind spot that the Arbiter directly targets.

---

## 19. MBench: A Comprehensive Benchmark on Memory Capability for Video World Models
**Authors:** Shengjun Zhang, Zhang Zhang, Simin Huang, Zhenyu Tang, Hanyang Wang (Tsinghua-IVG)

MBench benchmarks whether video world models can maintain stable, consistent internal state across extended temporal horizons — a functional requirement distinct from visual plausibility. Current models produce visually impressive but temporally incoherent videos because benchmarks measure appearance, not memory; MBench fills this evaluation gap.

**arXiv:** [arxiv.org/abs/2606.00793](https://arxiv.org/abs/2606.00793)
**Sources:** HuggingFace Daily Papers (6 upvotes), GitHub (16 stars), arXiv cs.CV
**Why trending:** World models are a major research focus; demonstrating that temporal memory is unmeasured by current benchmarks motivates an important new evaluation direction.

---

## 20. The Hidden Power of Scaling Factor in LoRA Optimization
**Authors:** Zicheng Zhang, Haoran Li, Jiaxing Wang, Guoqiang Gong, Anqi Li

This paper reveals that the LoRA scaling factor α is not equivalent to the learning rate but acts as an independent and dominant driver of effective optimization, with gains that cannot be replicated by learning rate tuning alone. The finding fundamentally changes how practitioners should configure LoRA fine-tuning and explains many previously unexplained empirical results.

**arXiv:** [arxiv.org/abs/2606.12883](https://arxiv.org/abs/2606.12883)
**Sources:** HuggingFace Daily Papers (5 upvotes), arXiv cs.LG
**Why trending:** LoRA is ubiquitous for fine-tuning; revealing that a commonly ignored hyperparameter is actually the dominant optimization driver has immediate practical impact across the entire fine-tuning community.
