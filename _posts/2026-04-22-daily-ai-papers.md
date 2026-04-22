---
title: "Daily AI Papers — April 22, 2026"
date: 2026-04-22
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-22/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agents
  - multimodal
  - generative-models
---

## 1. Tstars-Tryon 1.0: Robust and Realistic Virtual Try-On for Diverse Fashion Items

- **Authors:** Mengting Chen, Zhengrui Chen, Yongchao Du, Zuan Gao, Taihang Hu et al.
- **arXiv:** [arxiv.org/abs/2604.19748](https://arxiv.org/abs/2604.19748)
- **Summary:** A commercial-scale virtual try-on system from Taobao/Tmall that holds up under extreme poses, lighting, and motion blur while preserving fine garment texture and material. Supports up to 6 reference images across 8 fashion categories with near real-time inference, deployed at industrial scale to millions of users.
- **Sources:** HuggingFace Daily Papers (226 upvotes — runaway #1), HF dataset (TaobaoTmall-AlgorithmProducts/Tstars-VTON)
- **Why trending:** Massive 226-upvote spike, far ahead of #2 (80) — a fully-deployed, production virtual try-on system with a public benchmark is rare and strikes both research and e-commerce communities.

## 2. CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation

- **Authors:** Xiangyang Luo, Xiaozhe Xin, Tao Feng, Xu Guo, Meiguang Jin et al.
- **arXiv:** [arxiv.org/abs/2604.19636](https://arxiv.org/abs/2604.19636)
- **Summary:** End-to-end DiT-based framework for human-object interaction video synthesis conditioned on person, product, text, and speech. Introduces a Human-Aware Mixture-of-Experts that routes tokens to region-specialized experts (hands, faces) plus a structural co-generation module to avoid hand-object interpenetration.
- **Sources:** HuggingFace Daily Papers (80 upvotes)
- **Why trending:** HOI video synthesis with physical plausibility is a long-standing pain point for ad/e-commerce video gen; the Human-Aware MoE design is broadly applicable.

## 3. AgentSPEX: An Agent SPecification and EXecution Language

- **Authors:** Pengcheng Wang, Jerry Huang, Jiarui Yao, Rui Pan, Peizhi Niu et al.
- **arXiv:** [arxiv.org/abs/2604.13346](https://arxiv.org/abs/2604.13346)
- **Summary:** A domain-specific language and runtime for LLM agent workflows with explicit control flow, typed steps, branching, loops, parallelism, and reusable modules — decoupling agent logic from Python and addressing the maintainability issues of LangGraph/DSPy/CrewAI.
- **Sources:** HuggingFace Daily Papers (53 upvotes)
- **Why trending:** Agent orchestration fatigue is real — a clean, language-level abstraction over Python-glued frameworks resonates with practitioners shipping agents to production.

## 4. SmartPhotoCrafter: Unified Reasoning, Generation and Optimization for Automatic Photographic Image Editing

- **Authors:** Ying Zeng, Miaosen Luo, Guangyuan Li, Yang Yang, Ruiyang Fan et al.
- **arXiv:** [arxiv.org/abs/2604.19587](https://arxiv.org/abs/2604.19587)
- **Summary:** Reformulates photo editing as a tightly coupled reasoning-to-generation process: an Image Critic module identifies quality deficiencies, then a Photographic Artist module performs targeted enhancements — eliminating the need for users to articulate aesthetic intent.
- **Sources:** HuggingFace Daily Papers (41 upvotes)
- **Why trending:** "Auto-editing" is the natural next step after instruction-based image editing, and removing the prompt-engineering burden is highly user-relevant.

## 5. AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model

- **Authors:** Yutian Chen, Shi Guo, Renbiao Jin, Tianshuo Yang, Xin Cai et al.
- **arXiv:** [arxiv.org/abs/2604.19747](https://arxiv.org/abs/2604.19747)
- **Summary:** Scalable sparse-view 3D reconstruction that conditions a video diffusion model on arbitrarily many unordered input views via a persistent global scene memory (capture view cache) plus geometry-aware conditioning, removing temporal compression to maintain frame-level correspondence.
- **Sources:** HuggingFace Daily Papers (35 upvotes)
- **Why trending:** Video-diffusion-as-3D-reconstructor is the dominant new paradigm; supporting arbitrary view counts (vs. fixed 1-2) is a meaningful generalization.

## 6. TEMPO: Scaling Test-time Training for Large Reasoning Models

- **Authors:** Qingyang Zhang, Xinke Kong, Haitao Wu, Qinghua Hu, Minghao Wu et al.
- **arXiv:** [arxiv.org/abs/2604.19295](https://arxiv.org/abs/2604.19295)
- **Summary:** A test-time training framework that interleaves policy refinement on unlabeled questions with periodic critic recalibration on labeled data, formalized via Expectation-Maximization. Prevents the diversity collapse and reward drift that plague existing TTT methods, sustaining gains with more compute.
- **Sources:** HuggingFace Daily Papers (28 upvotes)
- **Why trending:** TTT for reasoning LLMs is the hot post-o1 frontier; an EM-grounded fix for the plateau problem is exactly what the field needs.

## 7. PlayCoder: Making LLM-Generated GUI Code Playable

- **Authors:** Zhiyuan Peng, Wei Tao, Xin Yin, Chenhao Ying, Yuan Luo et al.
- **arXiv:** [arxiv.org/abs/2604.19742](https://arxiv.org/abs/2604.19742)
- **Summary:** Introduces PlayEval, a repository-aware benchmark of 43 multilingual GUI applications (Python/TS/JS) covering interactive games and event-driven UIs, plus PlayCoder — a multi-agent framework that improves functional correctness via iterative repair on actual interaction flows rather than pass/fail tests.
- **Sources:** HuggingFace Daily Papers (24 upvotes)
- **Why trending:** Code-gen evals have long under-tested interactive systems; benchmarking actual playability is a step-change for evaluating coding agents.

## 8. ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning

- **Authors:** Xianming Li, Zongxi Li, Tsz-fung Andrew Lee, Jing Li, Haoran Xie et al.
- **arXiv:** [arxiv.org/abs/2604.19254](https://arxiv.org/abs/2604.19254)
- **Summary:** A centralized PEFT framework that performs layer-level refinement through a depth-shared shadow module, evolving a parallel shadow state at each transformer layer — replacing LoRA's distributed weight perturbations with a shared multi-layer adaptation pathway.
- **Sources:** HuggingFace Daily Papers (23 upvotes)
- **Why trending:** First serious architectural alternative to LoRA's local low-rank perturbation in a while; depth-shared shadow paths are an interesting structural prior for PEFT.

## 9. Chat2Workflow: A Benchmark for Generating Executable Visual Workflows with Natural Language

- **Authors:** Yi Zhong, Buqiang Xu, Yijun Wang, Zifei Shan, Shuofei Qiao et al.
- **arXiv:** [arxiv.org/abs/2604.19667](https://arxiv.org/abs/2604.19667)
- **Summary:** A benchmark for generating executable visual workflows directly from natural language, drawn from real-world industrial deployments, plus a robust agentic framework to mitigate recurrent execution errors. Reveals significant gaps between current LLMs and industrial-grade workflow automation.
- **Sources:** HuggingFace Daily Papers (16 upvotes)
- **Why trending:** Visual workflow builders (n8n, Dify, ComfyUI-style) are everywhere in industry — automating their construction is high-leverage.

## 10. AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation

- **Authors:** Wentao Shi, Yu Wang, Yuyang Zhao, Yuxin Chen, Fuli Feng et al.
- **arXiv:** [arxiv.org/abs/2604.18240](https://arxiv.org/abs/2604.18240)
- **Summary:** A 155-task / 516-trajectory benchmark across search, data systems, and GUI domains for evaluating Agent-as-a-Judge — judges that interact with environments and tools to gather verifiable evidence rather than relying on rule-based or LLM-as-a-Judge scoring.
- **Sources:** HuggingFace Daily Papers (14 upvotes)
- **Why trending:** As RL agent training scales, evaluation reliability becomes the bottleneck — Agent-as-a-Judge is the natural next step beyond LLM-as-a-Judge.

## 11. SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks

- **Authors:** Shanshan Zhong, Yi Lu, Jingjie Ning, Yibing Wan, Lihan Feng et al.
- **arXiv:** [arxiv.org/abs/2604.20087](https://arxiv.org/abs/2604.20087)
- **Summary:** First benchmark for continual skill learning in LLM agents, comprising 20 verified skill-dependent tasks across 15 sub-domains, evaluated at three levels (skill quality, execution trajectory, task outcome). Finds that continual gains depend more on task structure and feedback than on model scale.
- **Sources:** HuggingFace Daily Papers (11 upvotes)
- **Why trending:** Skills (Anthropic-style or otherwise) are the de facto agent customization layer in 2026 — measuring how to learn them automatically is overdue.

## 12. CityRAG: Stepping Into a City via Spatially-Grounded Video Generation

- **Authors:** Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng et al.
- **arXiv:** [arxiv.org/abs/2604.19741](https://arxiv.org/abs/2604.19741)
- **Summary:** A video generative model for navigable city-scale environments, grounded in geo-registered data corpora to maintain physical consistency under varying weather and dynamic objects. Trained on temporally unaligned data to teach the model to generate plausible motion across real geography.
- **Sources:** HuggingFace Daily Papers (11 upvotes)
- **Why trending:** City-scale navigable video gen is the convergence point of world models, AV simulation, and 3D scene reconstruction — a flagship use case for 2026.

## 13. Understanding and Enforcing Weight Disentanglement in Task Arithmetic

- **Authors:** Shangge Liu, Yuehan Yin, Lei Wang, Qi Fan, Yinghuan Shi et al.
- **arXiv:** [arxiv.org/abs/2604.17078](https://arxiv.org/abs/2604.17078)
- **Summary:** Introduces Task-Feature Specialization (TFS) — a model's ability to allocate distinct internal features to different tasks — as the fundamental cause of weight disentanglement in task arithmetic. Proves TFS is sufficient and proposes OrthoReg to enforce it via orthogonal weight updates during fine-tuning.
- **Sources:** HuggingFace Daily Papers (11 upvotes)
- **Why trending:** Task arithmetic / model merging is a heavily-used but theoretically shaky tool — a principled explanation plus a regularizer is impactful.

## 14. Dual-View Training for Instruction-Following Information Retrieval

- **Authors:** Qingcheng Zeng, Puxuan Yu, Aman Mehta, Fuheng Zhao, Rajhans Samdani
- **arXiv:** [arxiv.org/abs/2604.18845](https://arxiv.org/abs/2604.18845)
- **Summary:** A dual-view data synthesis strategy based on polarity reversal: given a query, an instruction-relevant document, and a hard negative, an LLM generates a complementary instruction under which the two documents swap relevance. Trains retrievers to distinguish topical relevance from instruction compliance.
- **Sources:** HuggingFace Daily Papers (10 upvotes)
- **Why trending:** Most retrievers ignore explicit instructions; polarity-reversal data synthesis is a clean, generalizable trick for instruction-following IR.

## 15. Code-Switching Information Retrieval: Benchmarks, Analysis, and the Limits of Current Retrievers

- **Authors:** Qingcheng Zeng, Yuheng Lu, Zeqi Zhou, Heli Qi, Puxuan Yu et al.
- **arXiv:** [arxiv.org/abs/2604.17632](https://arxiv.org/abs/2604.17632)
- **Summary:** Introduces CSR-L, a human-annotated benchmark of mixed-language queries, and shows that code-switching is a fundamental performance bottleneck across statistical, dense, and late-interaction retrievers — even strong multilingual models suffer due to embedding-space divergence between pure and code-switched text.
- **Sources:** HuggingFace Daily Papers (10 upvotes)
- **Why trending:** Code-switching is ubiquitous in global user queries but systematically under-evaluated; a clean benchmark + diagnosis is overdue.

## 16. UniMesh: Unifying 3D Mesh Understanding and Generation

- **Authors:** Peng Huang, Yifeng Chen, Zeyu Zhang, Hao Tang
- **arXiv:** [arxiv.org/abs/2604.17472](https://arxiv.org/abs/2604.17472)
- **Summary:** A unified framework for 3D mesh tasks featuring a Mesh Head that bridges diffusion-based image generation with implicit shape decoders, a Chain of Mesh module for iterative semantic editing, and a self-reflection mechanism for error correction.
- **Sources:** HuggingFace Daily Papers (9 upvotes)
- **Why trending:** Mesh-native unified models are still rare compared to point-cloud or image-based 3D — Chain of Mesh is a nice take on iterative refinement.

## 17. Speculative Decoding for Autoregressive Video Generation

- **Authors:** Yuezhou Hu, Jintao Zhang
- **arXiv:** [arxiv.org/abs/2604.17397](https://arxiv.org/abs/2604.17397)
- **Summary:** SDVG adapts speculative decoding to block-based autoregressive video diffusion by replacing token verification with an image-quality router: a 1.3B drafter proposes blocks via four denoising steps, scored by ImageReward with worst-frame aggregation, achieving significant speedup with maintained visual quality.
- **Sources:** HuggingFace Daily Papers (8 upvotes)
- **Why trending:** Streaming video generation is becoming compute-critical; carrying over the LLM-world's speculative-decoding wins to video diffusion is high-impact.

## 18. Target-Oriented Pretraining Data Selection via Neuron-Activated Graph

- **Authors:** Zijun Wang, Haoqin Tu, Weidong Zhou, Yiyang Zhou, Xiaohuan Zhou et al.
- **arXiv:** [arxiv.org/abs/2604.15706](https://arxiv.org/abs/2604.15706)
- **Summary:** NAG-based Ranking is a training-free, interpretable framework for target-oriented pretraining data selection. Each input is characterized by a sparse set of high-impact neurons in any off-the-shelf LLM, ranked by Neuron-Activated Graph similarity to target examples — outperforming representation-based selection across 6 benchmarks.
- **Sources:** HuggingFace Daily Papers (8 upvotes)
- **Why trending:** Pretraining data selection is one of the highest-leverage research areas; neuron-graph ranking is interpretable and training-free, which is rare.

## 19. UDM-GRPO: Stable and Efficient Group Relative Policy Optimization for Uniform Discrete Diffusion Models

- **Authors:** Jiaqi Wang, Haoge Deng, Ting Pan, Yang Liu, Chengyuan Wang et al.
- **arXiv:** [arxiv.org/abs/2604.18518](https://arxiv.org/abs/2604.18518)
- **Summary:** First framework integrating Uniform Discrete Diffusion with RL via GRPO. Treats the final clean sample as the action for stable optimization signals, reconstructs trajectories via the diffusion forward process, and adds Reduced-Step + CFG-Free strategies — achieving SOTA on text-to-image and OCR.
- **Sources:** HuggingFace Daily Papers (5 upvotes)
- **Why trending:** GRPO is dominating LLM RL; porting it to discrete diffusion (a hot generative paradigm) opens a new line of work.

## 20. RDP LoRA: Geometry-Driven Identification for Parameter-Efficient Adaptation in Large Language Models

- **Authors:** Yusuf Çelebi, Yağız Asker, Özay Ezerceli, Mahmoud ElHussieni, Selva Taş et al.
- **arXiv:** [arxiv.org/abs/2604.19321](https://arxiv.org/abs/2604.19321)
- **Summary:** Models hidden-state evolution as a high-dimensional geometric trajectory and uses the Ramer-Douglas-Peucker algorithm — a parameter-free polygon simplification — to identify critical breakpoint layers for LoRA adaptation, outperforming full and random layer-selection baselines.
- **Sources:** HuggingFace Daily Papers (4 upvotes)
- **Why trending:** Layer-selection for PEFT is usually heuristic; a geometric, training-free criterion grounded in trajectory simplification is a clean idea.
