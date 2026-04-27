---
title: "Daily AI Papers — April 26, 2026"
date: 2026-04-26
permalink: /blog/ai-papers/2026/04/daily-ai-papers-04-26/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal
  - rag
  - moe
---

## 1. RAG-Anything: All-in-One RAG Framework
- **Authors:** Zirui Guo, Xubin Ren, Lingrui Xu, Jiahao Zhang, Chao Huang, et al.
- **arxiv:** [arxiv.org/abs/2510.12323](https://arxiv.org/abs/2510.12323)
- **Sources:** Papers With Code (#3 trending), arXiv cs.IR
- **Summary:** Proposes a unified RAG framework that ingests heterogeneous knowledge — text, tables, images, code, KGs — through a single multimodal indexing+retrieval pipeline, eliminating the patchwork of modality-specific retrievers most production stacks ship today. Reports SOTA on multimodal QA benchmarks while keeping the API surface to a single `query()` call.
- **Why trending:** Production RAG fragmentation is the loudest pain point in the agentic-app space right now, and "all-in-one" is exactly what infra teams want to ship.

## 2. Kronos: A Foundation Model for the Language of Financial Markets
- **Authors:** Yu Shi, Zongliang Fu, Shuo Chen, Bohan Zhao, Wei Xu
- **arxiv:** [arxiv.org/abs/2508.02739](https://arxiv.org/abs/2508.02739)
- **Sources:** Papers With Code (#2 trending), arXiv cs.LG
- **Summary:** Builds a transformer foundation model pre-trained on a 12B-token corpus of financial K-line (candlestick) data spanning 45 global exchanges, with a tokenizer adapted to OHLCV quintuples. Beats supervised baselines on price-direction, volatility, and regime-shift forecasting in zero-shot settings.
- **Why trending:** First credible "GPT for markets" with permissive code release; quant Twitter and HN both lit up over it this week.

## 3. PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model
- **Authors:** Cheng Cui, Ting Sun, Suyin Liang, Tingquan Gao, Zelun Zhang, et al.
- **arxiv:** [arxiv.org/abs/2510.14528](https://arxiv.org/abs/2510.14528)
- **Sources:** Papers With Code (#12 trending), arXiv cs.CV
- **Summary:** A 0.9B-parameter document VLM combining a NaViT-style dynamic-resolution encoder with ERNIE-4.5-0.3B; covers 100+ languages and beats much larger models on layout, table, and formula extraction. Released with permissive license and runs on a single consumer GPU.
- **Why trending:** Tiny VLMs that match or beat 7B+ document models are eating the OCR-VL leaderboard; immediately useful for invoice/PDF pipelines.

## 4. MinerU2.5: A Decoupled Vision-Language Model for Efficient High-Resolution Document Parsing
- **Authors:** Junbo Niu, Zheng Liu, Zhuangcheng Gu, Bin Wang, Linke Ouyang, et al.
- **arxiv:** [arxiv.org/abs/2509.22186](https://arxiv.org/abs/2509.22186)
- **Sources:** Papers With Code (#11 trending), arXiv cs.CV
- **Summary:** A 1.2B doc-parsing VLM that decouples global layout analysis from local content recognition via a coarse-to-fine two-stage pipeline, reaching SOTA accuracy at a fraction of the FLOPs of monolithic VLMs. Open weights and a CLI ship together.
- **Why trending:** Direct rival to PaddleOCR-VL; the two are framing a "tiny doc-VLM" arms race that's blowing up across PWC and HF spaces.

## 5. VibeVoice Technical Report
- **Authors:** Zhiliang Peng, Jianwei Yu, Wenhui Wang, Yaoyao Chang, Yutao Sun, et al.
- **arxiv:** [arxiv.org/abs/2508.19205](https://arxiv.org/abs/2508.19205)
- **Sources:** Papers With Code (#6 trending), arXiv cs.SD
- **Summary:** Long-form, multi-speaker speech synthesis using **next-token diffusion** — autoregressively generating continuous latent vectors via a diffusion head — to produce hours-scale podcasts and dialogues with consistent voices. Introduces a new continuous tokenizer that compresses speech 80× while preserving prosody.
- **Why trending:** Next-token-diffusion is the hottest unification trick of the season; voice clone communities are already remixing the released checkpoints.

## 6. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory
- **Authors:** Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav
- **arxiv:** [arxiv.org/abs/2504.19413](https://arxiv.org/abs/2504.19413)
- **Sources:** Papers With Code (#17 trending), arXiv cs.AI
- **Summary:** Mem0 is a memory-centric agent architecture that extracts, consolidates, and retrieves persistent facts across sessions, sidestepping LLM context-window limits. Reports 26% lower latency and 91% lower token cost vs OpenAI Memory on the LOCOMO benchmark while beating quality.
- **Why trending:** "Agent memory" went from niche to table-stakes this quarter; the open-source repo just crossed major star milestones, drawing fresh attention.

## 7. Recursive Language Models
- **Authors:** Alex L. Zhang, Tim Kraska, Omar Khattab
- **arxiv:** [arxiv.org/abs/2512.24601](https://arxiv.org/abs/2512.24601)
- **Sources:** Papers With Code (#10 trending), arXiv cs.CL
- **Summary:** Treats long prompts as an external environment and lets the LLM programmatically peek, slice, and recurse on them — effectively turning context handling into an inference-time tool-use loop. Outperforms long-context models on multi-document reasoning at a fraction of the cost.
- **Why trending:** Reframes the long-context debate as an algorithmic one rather than an architectural one; the Khattab/DSPy crowd is championing it.

## 8. SmolDocling: An ultra-compact vision-language model for end-to-end multi-modal document conversion
- **Authors:** Ahmed Nassar, Andres Marafioti, Matteo Omenetti, Maksym Lysak, Nikolaos Livathinos
- **arxiv:** [arxiv.org/abs/2503.11576](https://arxiv.org/abs/2503.11576)
- **Sources:** Papers With Code (#19 trending), arXiv cs.CV, HuggingFace ecosystem
- **Summary:** A sub-billion-parameter VLM that converts arbitrary document pages into a new **DocTags** markup capturing layout, tables, formulas, and figures in one decode pass. Designed by IBM Research and HF together, with easy fine-tuning recipes.
- **Why trending:** Trio of tiny doc-VLMs (this + PaddleOCR-VL + MinerU2.5) is reshaping the doc-AI stack; SmolDocling is the most HF-native of the three.

## 9. OmniFlatten: An End-to-end GPT Model for Seamless Voice Conversation
- **Authors:** Qinglin Zhang, Luyao Cheng, Chong Deng, Qian Chen, Wen Wang
- **arxiv:** [arxiv.org/abs/2410.17799](https://arxiv.org/abs/2410.17799)
- **Sources:** Papers With Code (#23 trending), arXiv cs.CL
- **Summary:** A full-duplex voice GPT that handles overlapping speech and natural turn-taking by **flattening** speech and text streams into a single autoregressive sequence. Hits human-like sub-200ms latency without a separate VAD or ASR module.
- **Why trending:** Full-duplex voice agents are the next interface frontier — and this is the cleanest fully-end-to-end recipe so far.

## 10. TradingAgents: Multi-Agents LLM Financial Trading Framework
- **Authors:** Yijia Xiao, Edward Sun, Di Luo, Wei Wang
- **arxiv:** [arxiv.org/abs/2412.20138](https://arxiv.org/abs/2412.20138)
- **Sources:** Papers With Code (#5 trending), arXiv cs.AI
- **Summary:** Decomposes algorithmic trading into role-played LLM agents (analyst, researcher, trader, risk manager) that debate, vote, and refine positions, mirroring a real trading-desk workflow. Reports significant alpha over single-agent and rule-based baselines on equity and crypto backtests.
- **Why trending:** Pairs naturally with Kronos (#2) — the "AI fund" narrative is back, and these two papers are the canonical references this week.

## 11. LightRAG: Simple and Fast Retrieval-Augmented Generation
- **Authors:** Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, Chao Huang
- **arxiv:** [arxiv.org/abs/2410.05779](https://arxiv.org/abs/2410.05779)
- **Sources:** Papers With Code (#18 trending), arXiv cs.IR
- **Summary:** Combines a graph-structured knowledge index with dual-level retrieval (entity + topic) to deliver GraphRAG-quality answers at a fraction of the indexing cost. Same lab as RAG-Anything (#1); LightRAG is the lean cousin focused on speed and incremental updates.
- **Why trending:** Most production teams want GraphRAG quality without the GraphRAG bill — LightRAG is the pragmatic answer that keeps trending months later.

## 12. A Comprehensive Survey of Mixture-of-Experts: Algorithms, Theory, and Applications
- **Authors:** Siyuan Mu, Sen Lin
- **arxiv:** [arxiv.org/abs/2503.07137](https://arxiv.org/abs/2503.07137)
- **Sources:** Papers With Code (#13 trending), arXiv cs.LG
- **Summary:** A 100+-page sweep of MoE — routing algorithms, load-balancing losses, system-side primitives, theoretical convergence/expressivity results, and a taxonomy of every major MoE LLM/VLM/diffusion variant shipped to date. The current go-to MoE reference.
- **Why trending:** With every frontier release going MoE (Qwen3-Omni, DeepSeek-V3.x, etc.), this survey is the cliff-notes the community keeps reaching for.

## 13. A decoder-only foundation model for time-series forecasting (TimesFM)
- **Authors:** Abhimanyu Das, Weihao Kong, Rajat Sen, Yichen Zhou
- **arxiv:** [arxiv.org/abs/2310.10688](https://arxiv.org/abs/2310.10688)
- **Sources:** Papers With Code (#15 trending), arXiv cs.LG
- **Summary:** Google Research's decoder-only forecasting foundation model trained on 100B+ time points, with patched-tokens and a long-context decoder. Zero-shot accuracy approaches supervised SOTA across Monash, Darts, and ETT benchmarks.
- **Why trending:** Time-series foundation models are having their "GPT moment" — TimesFM keeps re-emerging on PWC as benchmark refreshes drop.

## 14. OpenHands: An Open Platform for AI Software Developers as Generalist Agents
- **Authors:** Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, et al.
- **arxiv:** [arxiv.org/abs/2407.16741](https://arxiv.org/abs/2407.16741)
- **Sources:** Papers With Code (#16 trending), arXiv cs.SE
- **Summary:** Open-source platform (formerly OpenDevin) where coding agents browse, edit, run code, and call tools through a sandboxed runtime, with a unified evaluation harness across SWE-bench, WebArena, GAIA. Now the de facto reference impl for SWE agents.
- **Why trending:** With every frontier lab claiming SWE-bench wins, OpenHands is the open scaffold researchers actually compare against.

## 15. AutoDev: Automated AI-Driven Development
- **Authors:** Michele Tufano, Anisha Agarwal, Jinu Jang, Roshanak Zilouchian Moghaddam, Neel Sundaresan
- **arxiv:** [arxiv.org/abs/2403.08299](https://arxiv.org/abs/2403.08299)
- **Sources:** Papers With Code (#14 trending), arXiv cs.SE
- **Summary:** Microsoft's framework where the AI gets full IDE primitives — file edits, build, test, git, terminal — under a permission model that mirrors human dev workflows. Demonstrates strong autonomous task completion on enterprise repos.
- **Why trending:** As Copilot Workspace and Cursor-style agents proliferate, AutoDev is the academic write-up the industry keeps citing.

## 16. LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models
- **Authors:** Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo
- **arxiv:** [arxiv.org/abs/2403.13372](https://arxiv.org/abs/2403.13372)
- **Sources:** Papers With Code (#25 trending), arXiv cs.CL
- **Summary:** A unified UI+CLI for fine-tuning 100+ open LLMs with LoRA/QLoRA/DPO/PPO/RM, plus a no-code WebUI for non-engineers. Has become the most-starred Chinese OSS LLM project and the default training stack for many Asia-based labs.
- **Why trending:** With Qwen3.5, Yi, and DeepSeek series releases this week, LlamaFactory's ranking jumped because everyone is fine-tuning *something*.

## 17. GigaWorld-Policy: An Efficient Action-Centered World–Action Model
- **Authors:** Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, et al.
- **arxiv:** [arxiv.org/abs/2603.17240](https://arxiv.org/abs/2603.17240)
- **Sources:** Papers With Code (#31 trending), arXiv cs.RO
- **Summary:** Decouples future-frame prediction from policy generation in a video-pretrained World-Action Model, slashing rollout cost while keeping the world-modeling generalization gain. Beats prior WAMs on real-robot manipulation suites.
- **Why trending:** World-action models are the robotics community's hot frontier; "decoupled" recipes are the way the field is converging.

## 18. LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels
- **Authors:** Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero
- **arxiv:** [arxiv.org/abs/2603.19312](https://arxiv.org/abs/2603.19312)
- **Sources:** Papers With Code (#24 trending), arXiv cs.LG
- **Summary:** A pixel-to-latent JEPA that trains end-to-end without EMA targets, frozen encoders, or auxiliary losses — clean enough that representation collapse is provably avoided. LeCun's lab leaning hard into the "world-model from raw pixels" thesis.
- **Why trending:** Yann LeCun byline + a clean JEPA recipe = guaranteed Twitter weekend.

## 19. DFlash: Block Diffusion for Flash Speculative Decoding
- **Authors:** Jian Chen, Yesheng Liang, Zhijian Liu
- **arxiv:** [arxiv.org/abs/2602.06036](https://arxiv.org/abs/2602.06036)
- **Sources:** Papers With Code (#20 trending), arXiv cs.LG
- **Summary:** Replaces the autoregressive draft model in speculative decoding with a tiny **block-diffusion** drafter that proposes K tokens in parallel via a few denoising steps, lifting acceptance rates and total wall-clock speedup. Plug-in to any HF or vLLM stack.
- **Why trending:** Speculative-decoding remains the lowest-hanging fruit for serving cost — diffusion drafters are this year's twist on the recipe.

## 20. Temporally Extended Mixture-of-Experts Models
- **Authors:** Zeyu Shen, Peter Henderson
- **arxiv:** [arxiv.org/abs/2604.20156](https://arxiv.org/abs/2604.20156)
- **Sources:** HuggingFace daily papers, arXiv cs.LG
- **Summary:** Argues that token-level expert switching causes pathological cache churn once a model outgrows GPU memory, and proposes a temporal-MoE that holds an expert active across spans of tokens. Recovers training+inference throughput without quality regressions.
- **Why trending:** Hits the exact failure mode every team scaling MoE past single-node has run into; Henderson's name brings the policy/efficiency crowd along.

---

## Key Themes Today
- **Doc-AI tiny-VLM arms race** — PaddleOCR-VL, MinerU2.5, and SmolDocling are converging on the sub-1.5B "good enough" frontier.
- **Voice goes end-to-end** — VibeVoice (synthesis) + OmniFlatten (full-duplex dialog) signal the death of cascaded ASR→LLM→TTS pipelines.
- **Finance LLM moment** — Kronos + TradingAgents is the "AI quant fund" pairing the week converged on.
- **MoE everywhere** — survey, temporal-MoE, and downstream MoE references reflect that every frontier release is now sparse.
- **RAG matures** — RAG-Anything and LightRAG (same lab) frame the future of retrieval as multimodal-graph by default.
