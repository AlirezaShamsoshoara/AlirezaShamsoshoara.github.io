---
title: 'Daily AI Papers — April 4, 2026'
date: 2026-04-04
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-04/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - agent-systems
  - reasoning-models
  - embodied-ai
---

Top 20 trending AI papers. No new HuggingFace daily papers posted yet today (Friday), so today's report captures the settled ranking from April 3's papers after a full day of community engagement, plus new cross-platform signals.

---

## 1. DataFlex: A Unified Framework for Data-Centric Dynamic Training of LLMs
**Authors:** Hao Liang, Zhengyang Zhao, Meiyi Qiang, Mingrui Chen et al.
**Summary:** Unifies data selection, mixture optimization, and reweighting into a single consistent framework. Existing approaches are fragmented across isolated codebases with inconsistent interfaces. Open-source on GitHub with YouTube walkthrough.
**Link:** [arxiv.org/abs/2603.26164](https://arxiv.org/abs/2603.26164)
**Source:** HuggingFace daily (Apr 3, #1), YouTube explainer video, GitHub open-source (OpenDCAI/DataFlex), HuggingFace paper page
**Why trending:** Holds #1 on HF daily. Open-source tool that unifies a universal pain point. YouTube + GitHub drive real adoption.

## 2. Generative World Renderer
**Authors:** Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu et al.
**Summary:** Large-scale dynamic dataset of 4M continuous frames (720p/30fps) from AAA games using dual-screen stitched capture. Scales generative inverse and forward rendering to real-world complexity by bridging the synthetic-to-real domain gap.
**Link:** [arxiv.org/abs/2604.02329](https://arxiv.org/abs/2604.02329)
**Source:** HuggingFace daily (Apr 3, #3), alphaxiv.org, arxivlens analysis, AI Native Foundation daily digest (Apr 3)
**Why trending:** Featured in AI Native Foundation digest. Creative data strategy using AAA game footage. Multi-platform discussion continues.

## 3. SKILL0: In-Context Agentic RL for Skill Internalization
**Authors:** Zhengxi Lu, Zhiyuan Yao, Jinyang Wu, Chengcheng Han et al.
**Summary:** Runtime skill loading suffers from retrieval noise and token overhead. SKILL0 uses in-context agentic RL to internalize skills directly into model weights, eliminating inference-time loading while preserving performance.
**Link:** [arxiv.org/abs/2604.02268](https://arxiv.org/abs/2604.02268)
**Source:** HuggingFace daily (Apr 3, #4), paperium.net, arxivexplained.com, YouTube explainer
**Why trending:** Addresses a fundamental limitation of tool-augmented agents. Multi-platform coverage with YouTube explainer.

## 4. Steerable Visual Representations
**Authors:** Jona Ruthardt, Manu Gaur, Deva Ramanan, Makarand Tapaswi, Yuki M. Asano
**Summary:** Pretrained ViTs focus on salient cues with no way to redirect. Proposes steerable representations that let users direct frozen features toward specific visual concepts of interest. Bridges the gap between generic features and multimodal LLM controllability.
**Link:** [arxiv.org/abs/2604.02327](https://arxiv.org/abs/2604.02327)
**Source:** HuggingFace daily (Apr 3, #5), ICLR 2026 accepted paper list (papercopilot.com), scirate.com top papers
**Why trending:** Accepted at ICLR 2026. Deva Ramanan (CMU) co-author. Makes frozen ViT features controllable without retraining.

## 5. CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery
**Authors:** Ao Qu, Han Zheng, Zijian Zhou, Yihao Yan et al.
**Summary:** First framework for autonomous multi-agent evolution on open-ended problems. Existing LLM-based evolution methods rely on fixed heuristics and hard-coded exploration rules. CORAL removes these constraints, enabling sustained search and knowledge accumulation through autonomous agent evolution.
**Link:** [arxiv.org/abs/2604.01658](https://arxiv.org/abs/2604.01658)
**Source:** HuggingFace daily (Apr 3, #6), project website (human-agent-society.github.io/CORAL/)
**Why trending:** "First framework for autonomous multi-agent evolution" is a bold claim. Dedicated project website. Extends open-ended learning to multi-agent settings.

## 6. The Latent Space: Foundation, Evolution, Mechanism, Ability, and Outlook
**Authors:** Xinlei Yu, Zhangquan Chen, Yongbo He, Tianyu Fu et al.
**Summary:** Comprehensive survey arguing latent space is becoming the native computational substrate for language models. Many critical internal processes happen in continuous latent space, not human-readable token traces. Covers foundations through future outlook.
**Link:** [arxiv.org/abs/2604.02029](https://arxiv.org/abs/2604.02029)
**Source:** HuggingFace daily (Apr 3, #2), arxiv cs.CL
**Why trending:** Timely meta-analysis as latent reasoning gains momentum. HF #2 position reflects high community interest. Broad scope survey.

## 7. Therefore I am. I Think
**Authors:** Esakkivel Esakkiraja, Sai Rajeswar, Denis Akhiyarov, Rajagopal Venkatesaramani
**Summary:** Presents evidence that reasoning models make decisions before generating chain-of-thought. A linear probe decodes tool-calling decisions from pre-generation activations. Suggests CoT may be post-hoc rationalization, not causal reasoning. Intentional Descartes inversion in the title.
**Link:** [arxiv.org/abs/2604.01202](https://arxiv.org/abs/2604.01202)
**Source:** HuggingFace daily (Apr 3, #11), arxiv cs.AI
**Why trending:** Directly challenges the assumption that CoT drives decisions. If models decide first and rationalize second, the implications for alignment and interpretability are significant.

## 8. EgoSim: Egocentric World Simulator for Embodied Interaction Generation
**Authors:** Jinkun Hao, Mingda Jia, Ruiyan Wang, Xihui Liu et al.
**Summary:** Closed-loop egocentric simulator generating spatially consistent interaction videos while persistently updating 3D scene state. Fixes the two failure modes of existing simulators: no 3D grounding (structural drift) or static scenes (no state updates).
**Link:** [arxiv.org/abs/2604.01001](https://arxiv.org/abs/2604.01001)
**Source:** HuggingFace daily (Apr 3, #7), arxiv cs.CV
**Why trending:** Embodied AI needs closed-loop simulators. Persistent 3D state across multi-step interactions is the key missing piece.

## 9. LatentUM: Interleaved Cross-Modal Reasoning via Latent-Space Unified Model
**Authors:** Jiachun Jin, Zetong Zhou, Xiao Yang, Hao Zhang et al.
**Summary:** Goes beyond simple text-to-image or image-to-text by enabling interleaved cross-modal reasoning in latent space. Supports dense visual thinking, self-reflective generation improvement, and dynamic reasoning across modalities.
**Link:** [arxiv.org/abs/2604.02097](https://arxiv.org/abs/2604.02097)
**Source:** HuggingFace daily (Apr 3, #8), arxiv cs.CV
**Why trending:** Latent-space reasoning across modalities is harder than one-shot generation. Aligns with the broader latent space trend (see #6).

## 10. VOID: Video Object and Interaction Deletion
**Authors:** Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool et al.
**Summary:** Goes beyond appearance-level video object removal (shadows, reflections) to handle interaction-level consequences. When a removed object has collisions or physical interactions with other objects, VOID corrects those downstream effects.
**Link:** [arxiv.org/abs/2604.02296](https://arxiv.org/abs/2604.02296)
**Source:** HuggingFace daily (Apr 3, #10), arxiv cs.CV
**Why trending:** Interaction-aware video editing is meaningfully harder than pixel inpainting. Luc Van Gool co-author. Practical for video production.

## 11. Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Agent Memory
**Authors:** Jiaqi Liu, Zipeng Ling, Shi Qiu, Yanqing Liu et al.
**Summary:** Uses automated research methodology to systematically discover optimal memory configurations for multimodal agents, navigating a design space too large for manual exploration. Already on v2.
**Link:** [arxiv.org/abs/2604.01007](https://arxiv.org/abs/2604.01007)
**Source:** HuggingFace daily (Apr 3, #12), arxiv cs.AI
**Why trending:** Agent memory is the critical unsolved bottleneck. Meta-approach of using AI to research memory design.

## 12. Video Models Reason Early: Exploiting Plan Commitment for Maze Solving
**Authors:** Kaleb Newman, Tyler Zhu, Olga Russakovsky (Princeton)
**Summary:** Studies how video diffusion models internally reason during generation using maze solving as a testbed. Discovers "early plan commitment" -- models commit to a solution plan early in the diffusion process rather than refining throughout. This finding can be exploited for efficiency.
**Link:** [arxiv.org/abs/2603.30043](https://arxiv.org/abs/2603.30043)
**Source:** HuggingFace daily (Apr 3, #21), arxiv cs.CV
**Why trending:** Princeton (Olga Russakovsky). Understanding how diffusion models reason internally is fundamental. Early commitment finding has practical implications for speedup.

## 13. ASI-Evolve: AI Accelerates AI
**Authors:** Weixian Xu, Tiantian Mi, Yixiu Liu, Yang Nan et al.
**Summary:** Agentic framework for AI-for-AI research. Closes the loop through learn-deploy-evaluate cycles on the costly, long-horizon, weakly supervised research loops that drive real AI progress. Tests whether agents can handle actual research, not just benchmarks.
**Link:** [arxiv.org/abs/2603.29640](https://arxiv.org/abs/2603.29640)
**Source:** HuggingFace daily (Apr 3, #15), arxiv cs.AI
**Why trending:** Recursive AI-doing-AI-research vision. Addresses whether agentic systems can tackle real research complexity.

## 14. Apriel-Reasoner: RL Post-Training for General-Purpose Reasoning
**Authors:** Rafael Pardinas, Ehsan Kamalloo, David Vazquez, Alexandre Drouin (ServiceNow)
**Summary:** Documents challenges of joint RLVR optimization across domains with varying rollout lengths and difficulty. Provides a transparent recipe when frontier labs keep theirs secret.
**Link:** [arxiv.org/abs/2604.02007](https://arxiv.org/abs/2604.02007)
**Source:** HuggingFace daily (Apr 3, #29), ServiceNow blog (Apriel model family), researchtrend.ai
**Why trending:** ServiceNow company release. Transparency about RL training recipes when others won't share.

## 15. Investigating Autonomous Agent Contributions in the Wild
**Authors:** Razvan Mihai Popescu, David Gros, Andrei Botocan, Rahul Pandita et al.
**Summary:** First large-scale empirical study of autonomous coding agents' actual contributions to real-world projects. Analyzes activity patterns, code change quality, and effects on team dynamics over time.
**Link:** [arxiv.org/abs/2604.00917](https://arxiv.org/abs/2604.00917)
**Source:** HuggingFace daily (Apr 3, #16), arxiv cs.SE
**Why trending:** Everyone deploys coding agents but nobody has studied their real impact at scale. Data-driven answers to a pressing question.

## 16. GPA: Learning GUI Process Automation from Demonstrations
**Authors:** Zirui Zhao, Jun Hao Liew, Yan Yang, Wenzhuo Yang et al. (Salesforce)
**Summary:** Vision-based RPA from a single demo. Sequential Monte Carlo-based localization makes it more robust than traditional RPA and more deterministic than VLM-based GUI agents. From Salesforce Research (Junnan Li).
**Link:** [arxiv.org/abs/2604.01676](https://arxiv.org/abs/2604.01676)
**Source:** HuggingFace daily (Apr 3, #19), arxiv cs.AI
**Why trending:** Salesforce Research. Practical enterprise tool that's more reliable than either traditional RPA or LLM agents.

## 17. VideoZeroBench: Probing the Limits of Video MLLMs
**Authors:** Jiahao Meng, Tan Yue, Qi Xu, Haochen Wang et al.
**Summary:** Requires video MLLMs to identify precise spatio-temporal evidence supporting their answers, not just get the right answer. Exposes inflated scores that mask fine-grained understanding gaps.
**Link:** [arxiv.org/abs/2604.01569](https://arxiv.org/abs/2604.01569)
**Source:** HuggingFace daily (Apr 3, #18), arxiv cs.CV
**Why trending:** Evidence-grounded evaluation for video models. Right-answer-wrong-reason is a fundamental evaluation problem.

## 18. Executing as You Generate: Hiding Execution Latency in LLM Code Gen
**Authors:** Zhensu Sun, Zhihao Lin, Zhi Chen, Chengran Yang et al.
**Summary:** Runs partial code execution in parallel with token generation, hiding execution latency. Current agents waste time with serial generate-then-execute workflows. Simple idea with measurable latency savings.
**Link:** [arxiv.org/abs/2604.00491](https://arxiv.org/abs/2604.00491)
**Source:** HuggingFace daily (Apr 3, #32), HuggingFace paper page
**Why trending:** Directly applicable to every coding agent in production. Every developer will feel this improvement.

## 19. Gated Condition Injection for Controllable Linear-Attention Transformers
**Authors:** Yuhe Liu, Zhenxiong Tan, Yujia Hu, Songhua Liu, Xinchao Wang
**Summary:** Enables controllable diffusion models on-device without multimodal attention. Cloud-dependent generation raises privacy concerns; this paper explores efficient, private on-device alternatives using linear-attention transformers with gated conditioning.
**Link:** [arxiv.org/abs/2603.27666](https://arxiv.org/abs/2603.27666)
**Source:** HuggingFace daily (Apr 3, #14), arxiv cs.CV
**Why trending:** On-device AI + privacy is a growing concern. Linear attention makes controllable diffusion practical on mobile hardware.

## 20. Tex3D: Adversarial 3D Textures for VLA Models
**Authors:** Jiawei Chen, Simin Huang, Jiawei Du, Shuaihang Chen et al.
**Summary:** First physically realizable adversarial attack on VLA models via 3D object textures. More representative of real deployment than language perturbations or 2D patch attacks, since robots interact with textured 3D objects.
**Link:** [arxiv.org/abs/2604.01618](https://arxiv.org/abs/2604.01618)
**Source:** HuggingFace daily (Apr 3, #20), arxiv cs.CV
**Why trending:** VLA security is critical as robots deploy in the real world. 3D texture attacks are more realistic than 2D patches.

---

## Honorable Mentions

- **UniDriveVLA** (2604.02190) -- Unified perception + action for autonomous driving
- **NearID** (2604.01973) -- Identity representation via near-identity distractors
- **AutoMIA** (2604.01014) -- Agentic membership inference attacks
- **Omni123** (2604.02289) -- 3D generation from limited data
- **T5Gemma-TTS** (2604.01760) -- Encoder-decoder TTS fixing text conditioning fade
- **Brainstacks** (2604.01152) -- Frozen MoE-LoRA stacks for continual learning
- **ActionParty** (2604.02330) -- Multi-subject action binding in video games
- **Woosh** (2604.01929) -- Sound effects foundation model

---

## Methodology

| Source | URL | Signal | What Was Found |
|--------|-----|--------|---------------|
| HuggingFace Daily (Apr 4) | huggingface.co/api/daily_papers?date=2026-04-04 | Today's submissions | 0 papers (too early, Friday) |
| HuggingFace Daily (Apr 3) | huggingface.co/api/daily_papers?date=2026-04-03 | Yesterday's settled ranking | 45 papers (primary signal today) |
| AI Native Foundation | ainativefoundation.org/ai-native-daily-paper-digest-20260403/ | Curated digest | Generative World Renderer featured |
| GitHub | github.com/OpenDCAI/DataFlex | Open-source release | DataFlex framework |
| YouTube | youtube.com | Video explainers | DataFlex, SKILL0 |
| ICLR 2026 Paper List | papercopilot.com | Conference acceptance | Steerable Visual Representations |
| scirate.com | scirate.com | Top daily papers | Steerable Visual Representations |
| CORAL Project | human-agent-society.github.io/CORAL/ | Project website | CORAL multi-agent evolution |
| ServiceNow Blog | servicenow.com/blogs | Company release | Apriel-Reasoner |
| alphaxiv.org | alphaxiv.org | Cross-platform | Generative World Renderer |
| paperium.net / arxivexplained | Various | Cross-platform | SKILL0 |
| dair-ai ML Papers of the Week | github.com/dair-ai/ML-Papers-of-the-Week | Weekly curation | General weekly signal |
| Web search (Reddit, X, HN) | Various | Social media | Limited direct paper-level results |
| arxiv listings | arxiv.org/list/cs.* | Raw submissions | Abstract retrieval |

**Note:** No new HF daily papers for April 4 yet. Today's ranking reflects the settled community signal from April 3 papers after 24 hours of engagement, supplemented with new cross-platform appearances.

**Ranking criteria:** Cross-platform presence > company blog/release > conference acceptance > HF daily position > topic relevance.

*Generated by Jarvis | Next report: April 5, 2026 at 10:00 AM PT*
