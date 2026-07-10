---
title: "Daily AI Papers — July 10, 2026"
date: 2026-07-10
permalink: /blog/ai-papers/2026/07/daily-ai-papers-07-10/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - video-generation
  - agent-benchmarks
  - linear-attention
---

## 1. Vidu S1: A Real-Time Interactive Video Generation Model

**Authors:** Jintao Zhang, Kai Jiang, Jintao Chen, Xu Wang, Yang Luo, et al. (ShengShu Technology)  
**arXiv:** [arxiv.org/abs/2607.03118](https://arxiv.org/abs/2607.03118)  
**Sources:** HuggingFace Daily Papers (106 upvotes, 6 comments — top paper today); press coverage via TMTPost ("rival to OpenAI's Sora and Google's Veo"), Interesting Engineering, Daily AI Brief, TechNode, and wide PR-newswire syndication.  
**Why Trending:** By far the most upvoted paper on HuggingFace today, and one of the rare research drops with genuine cross-platform media pickup — tech outlets are framing it as China's answer to Sora/Veo for real-time, voice-controllable video generation.

ShengShu introduces Vidu S1, a real-time interactive video generation model that lets users steer digital characters via voice instructions mid-generation. Built on TurboDiffusion and TurboServe, it produces infinite-length 540p video at up to 42 fps without the blurring, drift, or distortion that plague earlier streaming video generators.

---

## 2. Video-Oasis: Rethinking Evaluation of Video Understanding

**Authors:** Geuntaek Lim, Sungjune Park, Jaeyun Lee, Inwoong Lee, Taeoh Kim, et al.  
**arXiv:** [arxiv.org/abs/2603.29616](https://arxiv.org/abs/2603.29616)  
**Sources:** HuggingFace Daily Papers (42 upvotes, 1 comment).  
**Why Trending:** Second-highest HuggingFace traction today; tackles a widely-felt pain point — that Video-LLM benchmark scores conflate visual perception, linguistic reasoning, and knowledge priors rather than isolating true video understanding.

Rather than adding yet another benchmark, the authors step back to define shared criteria for what "video understanding" should actually measure, disentangling whether a model's score reflects genuine temporal/visual reasoning or leakage from language priors and world knowledge.

---

## 3. Why Can't I Open My Drawer? Mitigating Object-Driven Shortcuts in Zero-Shot Compositional Action Recognition

**Authors:** Geo Ahn, Inwoong Lee, Taeoh Kim, Minho Shim, Dongyoon Wee, et al.  
**arXiv:** [arxiv.org/abs/2601.16211](https://arxiv.org/abs/2601.16211)  
**Sources:** HuggingFace Daily Papers (40 upvotes, 1 comment).  
**Why Trending:** Third-highest HuggingFace traction; a memorable title paired with a genuinely useful diagnosis of why zero-shot action recognition models cheat.

The paper shows models solving Zero-Shot Compositional Action Recognition tend to predict verbs by latching onto the labeled object class rather than actual temporal/motion evidence. It proposes training adjustments that force verb-object learning to stay balanced, closing the object-driven shortcut.

---

## 4. UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

**Authors:** Zhekai Chen, Chengqi Duan, Kaiyue Sun, Bohao Li, Yuqing Wang, et al.  
**arXiv:** [arxiv.org/abs/2607.08768](https://arxiv.org/abs/2607.08768)  
**Sources:** HuggingFace Daily Papers (21 upvotes, 1 comment).  
**Why Trending:** Strong same-day HuggingFace traction; part of a fast-growing "ClawBench" family of agent benchmarks, reflecting the field's pivot from single-turn sandboxed agent evals to proactive, real-world, multi-turn evaluation.

Existing agent benchmarks mostly rely on sandboxed environments and single-turn tasks that don't reflect how proactive agents actually need to operate everyday tools. UniClawBench proposes a more realistic, real-world evaluation paradigm for LLM/multimodal agents that must act proactively rather than just respond.

---

## 5. Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation

**Authors:** Yifan Zhou, Qihao Yang, Yan Li, Donggang Li, Xiru Hu, et al.  
**arXiv:** [arxiv.org/abs/2607.08758](https://arxiv.org/abs/2607.08758)  
**Sources:** HuggingFace Daily Papers (20 upvotes, 3 comments).  
**Why Trending:** Highest comment count relative to upvotes today, suggesting active discussion; introduces a novel framing of scientific ideation as an "inheritance" problem, adjacent to but distinct from prior idea-generation benchmarks.

The authors present IdeaGene-Bench, testing whether AI systems can trace how scientific ideas inherit mechanisms and repair the limitations of earlier work — much like biological genomes — rather than generating ideas from a blank slate.

---

## 6. LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models

**Authors:** Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, et al.  
**arXiv:** [arxiv.org/abs/2607.08770](https://arxiv.org/abs/2607.08770)  
**Sources:** HuggingFace Daily Papers (19 upvotes, 1 comment).  
**Why Trending:** Solid same-day HuggingFace traction for a niche but technically dense contribution — fine-tuning video diffusion priors for the event-camera domain, a fast-growing sub-area of computational imaging.

LongE2V leverages pretrained video diffusion priors to jointly reconstruct, predict, and interpolate video from sparse event-camera streams, addressing both the texture blur of regression methods and the long-term instability of prior generative approaches.

---

## 7. Enhancing In-context Panoramic Generation via Geometric-aware Pretraining

**Authors:** Haoran Feng, Ruiyang Zhang, Longyi Zhang, Dizhe Zhang, Lu Qi  
**arXiv:** [arxiv.org/abs/2607.08765](https://arxiv.org/abs/2607.08765)  
**Sources:** HuggingFace Daily Papers (14 upvotes, 1 comment).  
**Why Trending:** Notable HuggingFace uptake for a fairly specialized generation task, driven by a new 1M-sample dataset (Canvas360Dataset) that fills a real data gap in panoramic generation.

Canvas360 is a two-stage framework combining geometry-aware pretraining with task-specific fine-tuning for in-context panoramic generation (style transfer, inpainting, outpainting), backed by a new large-scale paired panoramic dataset.

---

## 8. CineMobile: On-Device Image-to-Video Diffusion for Cinematic Camera Motion Generation

**Authors:** Xuyao Huang, Zelai Deng, Xu Wang, Xizhong Xiao, Zhijie Deng  
**arXiv:** [arxiv.org/abs/2607.03803](https://arxiv.org/abs/2607.03803)  
**Sources:** HuggingFace Daily Papers (8 upvotes, 1 comment).  
**Why Trending:** Rides the same wave of interest as Vidu S1 (image/video generation on-device) — practical relevance for shipping cinematic camera effects (bullet time, dolly zoom, slow motion) directly on phones.

CineMobile targets efficient on-device image-to-video generation with cinematic camera motion effects, addressing the heavy compute cost of Diffusion Transformers that normally blocks mobile deployment of such effects.

---

## 9. Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE

**Authors:** Haozhan Tang, Zerui Wang, Yuxian Gu, Song Han, Han Cai  
**arXiv:** [arxiv.org/abs/2607.07740](https://arxiv.org/abs/2607.07740)  
**Sources:** HuggingFace Daily Papers (7 upvotes, 1 comment).  
**Why Trending:** Co-authored by Song Han's efficient-AI lab (MIT HAN Lab), a name that reliably draws attention in the long-context/efficient-inference community; targets a very practical deployment problem — zero-shot context extension for open-weight models.

Jet-Long proposes a dynamic "bifocal" RoPE scheme for zero-shot long-context extension, aimed at agentic workflows and repo-level coding tasks whose accumulated context routinely blows past the pretraining window of open-weight LLMs.

---

## 10. OpenCoF: Learning to Reason Through Video Generation

**Authors:** Xinyan Chen, Ziyu Guo, Renrui Zhang, Dongzhi Jiang, Hongsheng Li  
**arXiv:** [arxiv.org/abs/2607.08763](https://arxiv.org/abs/2607.08763)  
**Sources:** HuggingFace Daily Papers (6 upvotes, 0 comments).  
**Why Trending:** Part of an emerging line of work (Chain-of-Frame reasoning) proposing video generation itself as a reasoning substrate, an alternative to text-based Chain-of-Thought that's gaining traction alongside other 2026 CoF papers.

OpenCoF explores "Chain-of-Frame" reasoning, where a video generator's temporally-connected frames serve as the reasoning trace instead of textual Chain-of-Thought, and open-sources training recipes to push generators beyond generic video synthesis toward reasoning tasks.

---

## 11. DrugGen 2: A Disease-Aware Language Model for Enhancing Drug Discovery

**Authors:** Ali Motahharynia, Mohammadreza Ghaffarzadeh-Esfahani, Mahsa Sheikholeslami, Navid Mazrouei, Matin Irajpour, et al.  
**arXiv:** [arxiv.org/abs/2607.08404](https://arxiv.org/abs/2607.08404)  
**Sources:** HuggingFace Daily Papers (5 upvotes, 1 comment).  
**Why Trending:** Steady HuggingFace interest in the AI-for-drug-discovery niche; extends the original DrugGen with disease-context conditioning, a gap most target-conditioned molecule generators ignore.

DrugGen-2 generates small molecules conditioned jointly on disease ontology and target protein, addressing how disease context shapes target behavior and therapeutic outcomes — a dimension largely neglected by prior target-only generative drug design models.

---

## 12. Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing

**Authors:** Tommaso Cerruti, Tim Rieder, George Rowlands, Lingfeng Jin, Imanol Schlag  
**arXiv:** [arxiv.org/abs/2607.07953](https://arxiv.org/abs/2607.07953)  
**Sources:** HuggingFace Daily Papers (5 upvotes, 1 comment).  
**Why Trending:** A timely comparative survey (DeltaNet, Gated DeltaNet, Kimi Delta Attention, Gated DeltaNet-2) landing right as linear-attention architectures (following Kimi Linear and similar releases) are becoming a hot alternative to quadratic softmax attention for long-context LLMs.

The paper unifies four recent recurrent linear-attention mechanisms under a common recurrence formulation, comparing their trade-offs against softmax attention and proposing cross-layer routing to combine their strengths.

---

## 13. UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma

**Authors:** Chongyu Fan, Pengfei Liu, Jingjia Huang, Sijia Liu, Yi Lin  
**arXiv:** [arxiv.org/abs/2607.06987](https://arxiv.org/abs/2607.06987)  
**Sources:** HuggingFace Daily Papers (2 upvotes, 1 comment).  
**Why Trending:** Addresses a core, widely-discussed pain point in LLM RL training — the exploration-stability trade-off in importance-sampling-based RL — relevant to anyone tuning RLHF/RLVR pipelines.

UP proposes an unbounded positive asymmetric optimization scheme to break the exploration-stability dilemma that plagues importance-sampling-based RL for LLM reasoning, where standard clipping trades away exploration to gain stability.

---

## 14. PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution

**Authors:** Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, et al.  
**arXiv:** [arxiv.org/abs/2607.06238](https://arxiv.org/abs/2607.06238)  
**Sources:** HuggingFace Daily Papers (2 upvotes, 1 comment).  
**Why Trending:** Niche medical-imaging traction; notable for explicitly modeling the physics coupling between spatial resolution and SNR in MRI acquisition, rather than treating super-resolution as a purely deterministic mapping.

PhyMRI-SR reframes MRI super-resolution as a physics-aware problem, since a given low-resolution scan is only one of many possible acquisitions once the resolution/SNR coupling inherent to MRI physics is accounted for.

---

## 15. Flash-BoN: Instant Drafts for Inference-Time Scaling in Diffusion Models

**Authors:** Ruchit Rawal, Reza Shirkavand, Sayak Paul, Yuxin Wen, Heng Huang, et al.  
**arXiv:** [arxiv.org/abs/2607.04461](https://arxiv.org/abs/2607.04461)  
**Sources:** HuggingFace Daily Papers (2 upvotes, 1 comment).  
**Why Trending:** Relevant to the fast-moving inference-time-scaling-for-diffusion literature; co-authored by Sayak Paul (well-known in the diffusers/Hugging Face community), which tends to draw extra attention from that audience.

Flash-BoN speeds up Best-of-N sampling for text-to-image diffusion by making the draft-generation step itself cheap, rather than only optimizing when and how often intermediate denoising steps get verified.

---

## 16. A Quantized Native Runtime for On-Device Semantic Audio Generation

**Authors:** Matteo Spanio, Antonio Rodà  
**arXiv:** [arxiv.org/abs/2607.08526](https://arxiv.org/abs/2607.08526)  
**Sources:** HuggingFace Daily Papers (1 upvote, 3 comments).  
**Why Trending:** Disproportionately high comment count for its upvote count, suggesting the "runs Stable Audio 3 on a Raspberry Pi 5 with zero Python/DL-framework dependency" pitch is sparking discussion among on-device/edge-AI practitioners.

The authors present "aria," a dependency-free native runtime that runs the full text-to-music pipeline of Stable Audio 3 on ordinary CPUs and even a Raspberry Pi 5, with no Python or deep-learning framework required at inference time.

---

## 17. CausalDS: Benchmarking Causal Reasoning in Data-Science Agents

**Authors:** Andrej Leban, Yuekai Sun  
**arXiv:** [arxiv.org/abs/2607.08093](https://arxiv.org/abs/2607.08093)  
**Sources:** HuggingFace Daily Papers (1 upvote, 1 comment).  
**Why Trending:** Fills a specific, cited gap between symbolic causal-reasoning benchmarks and realistic data-analysis benchmarks — relevant as LLM data-science agents become more common in production tooling.

CausalDS benchmarks LLM data-science agents on causal reasoning grounded in realistic data-analysis workflows, an area prior benchmarks either abstracted away into pure symbolic logic or evaluated without a principled causal generating structure.

---

## 18. A Sparse and Truncated State Vector Simulator for Peaked Circuits

**Authors:** Diogo R. Ferreira  
**arXiv:** [arxiv.org/abs/2607.07816](https://arxiv.org/abs/2607.07816)  
**Sources:** HuggingFace Daily Papers (1 upvote, 1 comment).  
**Why Trending:** Quantum-computing crossover paper drawing interest from the ML/HPC-adjacent HuggingFace crowd, given the quantum simulation and sampling angle.

For "peaked" quantum circuits, whose output distribution has a sharp spike on the most likely bitstring, the paper shows a truncated, sparse state-vector simulator using only a fraction of the full probability mass can efficiently recover that peak.

---

## 19. SAM-MT: Real-Time Interactive Multi-Target Video Segmentation

**Authors:** Ruiqi Shen, Chang Liu, Henghui Ding  
**arXiv:** [arxiv.org/abs/2607.08688](https://arxiv.org/abs/2607.08688)  
**Sources:** HuggingFace Daily Papers (0 upvotes, 1 comment).  
**Why Trending:** Builds directly on the SAM lineage (Segment Anything), a name that reliably draws niche interest even at low upvote counts; tackles the FPS collapse that occurs when naively replicating single-target SAM pipelines per object.

SAM-MT extends real-time interactive video object segmentation to the multi-target setting without the frame-rate collapse and unbounded latency growth that comes from simply replicating single-target processing per tracked object.

---

## 20. Can Dialects Be Steered Like Languages? Sparse Neurons and Distributed Directions in Arabic LLMs

**Authors:** Kareem Elozeiri, Mervat Abassy, Omar Kallas, Fahim Dalvi, Preslav Nakov, et al.  
**arXiv:** [arxiv.org/abs/2607.03936](https://arxiv.org/abs/2607.03936)  
**Sources:** HuggingFace Daily Papers (0 upvotes, 1 comment).  
**Why Trending:** Interpretability angle on a persistent, well-known weak spot of multilingual LLMs — dialectal Arabic generation — co-authored by Preslav Nakov, a recognizable name in Arabic/multilingual NLP.

The paper investigates where dialectal features are encoded inside Arabic LLMs, using sparse neurons and distributed directions to explain why models default to Modern Standard Arabic and testing whether that encoding can be steered to produce accurate dialectal output.
