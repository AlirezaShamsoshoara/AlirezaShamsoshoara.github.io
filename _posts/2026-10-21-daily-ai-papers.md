---
title: "Daily AI Papers — October 21, 2026"
date: 2026-10-21
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-21/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - world-models
  - ai-agents
  - robotics
---

### 1. Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds
**Authors:** Jihai Zhang, Runjia Qian, Kaiqin Kong, Biao Jiang, Puyi Wang, Siru Chen, Tianle Li, Guanjie Chen, Junyi Wu, Chubin Chen, Yuanhang Li, Kaichen Huang, Haobo Zhang, Yangguang Li, Wei Yu, Guibin Chen, Yu Cheng, Yahui Zhou
**arXiv:** [arxiv.org/abs/2610.27999](https://arxiv.org/abs/2610.27999)
**Summary:** Matrix-Game 4.0 separates executable game state and rules from an autoregressive video renderer, using a coding agent to turn natural-language ideas into game code and dynamic scene captions. Its distilled causal generator delivers 480p gameplay at 60 FPS with 112 ms key-press-to-display latency on one RTX 5090 while supporting customizable shooter and driving games.

---

### 2. Focused Omni-Modal GUI Agents
**Authors:** Fuyao Zhang, Wenwen He, Jiaming Zhang, Yurong Hao, Xuan Wang, Guowei Guan, Che Wang, Longtao Huang, Wei Yang Bryan Lim
**arXiv:** [arxiv.org/abs/2610.26203](https://arxiv.org/abs/2610.26203)
**Summary:** FocusGUI addresses sequential distraction in GUI agents by dynamically selecting step-relevant evidence from screenshots, audio, video, interaction history, and device state. The lightweight adapter trains only from action supervision and raises average Type Match by 33.2 points and Exact Match by three times across four frozen omni-modal backbones.

---

### 3. PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking
**Authors:** Pan Wang, Yihao Hu, Guangyuan Dong, Yitong Lin, Hang Wang, Zimi Liu, Zhihao Wen, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong
**arXiv:** [arxiv.org/abs/2610.27628](https://arxiv.org/abs/2610.27628)
**Summary:** Progress-Aligned Recurrence trains each recurrent iteration to predict the state after the corresponding number of operations while anchoring recurrent-state norms to prevent scale drift. A Qwen2.5-0.5B model trained on at most 32 swaps reaches 95.5% full-state accuracy at 512 swaps, demonstrating 16-times length extrapolation.

---

### 4. Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience
**Authors:** Tianqi Liu, Hanfei Zhao, Qifeng Liang, Hui En Pang, Jiarui Xu, Sayang Mu, Penghao Qiu, YingSheng Zhang, Jun Wang, Ziang Cao, Mingze Sun, Yukang Cao, Fangzhou Hong, Zhaoxi Chen, Ziwei Liu
**arXiv:** [arxiv.org/abs/2610.26855](https://arxiv.org/abs/2610.26855)
**Summary:** Ropedia W0 is an egocentric world foundation model that learns locomotion and manipulation across human and robot embodiments from 10,000 hours of human video and 3,000 hours of robot data. It leads five cross-embodiment benchmarks, benefits from scaling human pretraining data, and supports real-time minute-long rollouts after distillation.

---

### 5. S-Agent 2.0: Spatial Reasoning with a General Coding Agent
**Authors:** Rui Gong, Ruoyu Wang, Yalun Dai, Hao Li, Sidi Yang, Qihao Zhao, Hongyu Li, Zeyang Guan, Fangzhou Hong, Zhaoxi Chen, Kim-Hui Yap, Ziwei Liu
**arXiv:** [arxiv.org/abs/2610.28354](https://arxiv.org/abs/2610.28354)
**Summary:** S-Agent 2.0 equips a general coding agent with command-line 3D perception tools and persistent scene memory so it can acquire, retain, and interpret grounded spatial evidence. The toolkit improves Qwen3.8-27B by 13.9 and 20.5 points on MMSI-Bench and ReVSI and works across harnesses including Codex and Claude Code.

---

### 6. Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition
**Authors:** Wenjie Lou, Tianshuo Peng, Shiyang Feng, Shengji Tang, Runmin Ma, Ruizhe Chen, Jinxin Shi, Haoyang Peng, Fangchen Yu, Zhijie Zhong, Yuhao Zhou, Yue Fan, Yixin Chen, Yiming Wu, Yiheng Wang, Yigeng Jiang, Yichen Jiang, Yi Xie, Xu Guo, Xiaohan He, Tao Hu, Songtao Huang, Siyu Zhou, Shuaiyu Zhang, Shangheng Du, Qinglong Cao, Kun Li, Jingqi Ye, Hongbin Zhou, Guohang Yan, Zongsheng Cao, Ziyi Wang, Zhuo Liu, Zhiyin Yu, Zhiwang Zhou, Zelin Tan, Yuqing Zhu, Yaoze Zhang, Yang Chen, Xuming He, Xiuliang Liang, Xingjian Guo, Xiang Zhuang, Weiping Shen, Weida Wang, Tianyuan Zhou, Tianlin Ye, Tengyuan Fan, Siyu Yan, Shuo Li, Shuchen Pu, Shengyuan Xu, Shao Zhang, Ran Wei, Qinyuan Qin, Qingyu Yang, Nianchen Deng, Meng Dai, Kuikun Liu, Kaitao Chen, Juncheng Xiao, Jiangning Liu, Jianbiao Mei, Jia Yu, Haonan He, Hangfan Zhang, Cheng Yang, Chen Zhang, Bihao Zhan, Benteng Cheng, Yuqiang Li, Yihao Liu, Yang Yang, Xujun Fu, Xiaosong Wang, Xiangyu Yue, Wenwei Zhang, Shuyue Hu, Pinlong Cai, Mianxin Liu, Lei Bai, Jie Zhou, Jie Hou, Jiamin Wu, Hui Wang, Haijun Li, Guangyu Wang, Dongzhan Zhou, Chunfeng Song, Chao Yang, Biqing Qi, Xing Xie, Dahua Lin, Bowen Zhou, Xiangchao Yan, Wenlong Zhang, Shufei Zhang, Peng Ye, Bo Zhang
**arXiv:** [arxiv.org/abs/2610.28578](https://arxiv.org/abs/2610.28578)
**Summary:** Sage-A1.5 is a 35B mixture-of-experts agent model that composes subagent delegation, parallel work, progress checking, evidence validation, and reflective strategy revision for long-horizon tasks. It extends these capabilities to open scientific exploration, producing interactive analyses and inspectable research artifacts rather than only answering predefined questions.

---

### 7. VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse
**Authors:** Sicheng He, Yi Pan, Qiuting Yu, Jiaming Huang, Qi Lu, Shuyan Wu, Hongyan Feng, Xuanyu Liu, Jun Zhang, Jie Zhang, Wenqi Zhang, Xuhong Zhang, Jianwei Yin
**arXiv:** [arxiv.org/abs/2610.25043](https://arxiv.org/abs/2610.25043)
**Summary:** VLA-Rolling reuses the unexecuted tail of a vision-language-action model's previous action chunk, then allocates renoising and denoising according to per-action confidence. Across 16 model-benchmark pairs it reduces inference cost everywhere, reaches up to 1.48-times speedup, and improves success in 14 pairs by as much as 15.08 percentage points.

---

### 8. CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?
**Authors:** Jiaqi Su, Guibin Zhang, Jie-Jing Shao, Cong Pang, Tiankuo Yao, Ivor Tsang, Haiyan Yin, Shuicheng Yan
**arXiv:** [arxiv.org/abs/2610.25078](https://arxiv.org/abs/2610.25078)
**Summary:** CoEvo-RSI addresses mismatches between evolving agent harnesses and the model capabilities needed to use them through bidirectional historical inheritance. A meta-agent coordinates harness development, checkpoint selection or merging, and model adaptation, making Qwen3.5-9B competitive with larger systems across failure attribution, text-to-SQL, and smart-home tasks.

---

### 9. SolarRenderer: Few-Step Generative Reference Rendering
**Authors:** Guian Fang, Shengju Qian, Dongyue Lu, Junchao Huang, Lutao Jiang, Xin Wang, Yiren Song, Li Jiang, Mike Zheng Shou
**arXiv:** [arxiv.org/abs/2610.28630](https://arxiv.org/abs/2610.28630)
**Summary:** SolarRenderer adapts a frozen 33B video backbone with two lightweight LoRAs to render realistic video from arbitrary structural references supplied by engines, simulators, or coding agents. It generates in four steps at 12.3 times the speed of 50-step sampling, supports real-time 768p streaming, and generalizes to 11 unseen structural representations.

---

### 10. Learning the 4D World through Point Trajectory Forecasting
**Authors:** Byungwoo Jeon, Sunghwan Hong, Dohyeon Kim, Jonghoon Lee, Jungwoo Park, Inhee Lee, Doosan Baek, Jinil Kim, Taehyun Lim, Hanbyul Joo, Marc Pollefeys, Saining Xie, Jinwoo Shin
**arXiv:** [arxiv.org/abs/2610.28594](https://arxiv.org/abs/2610.28594)
**Summary:** The Video-Point Model jointly predicts multi-view future video and persistent 3D point trajectories, anchoring all camera views to a shared account of physical motion. Point supervision improves video fidelity and motion accuracy on 4D benchmarks and raises manipulation success when robot actions are jointly denoised as another token modality.

---

### 11. Correction Training for Diffusion Models
**Authors:** Donghoon Ahn, Runqian Wang, Alexei A. Efros, Taesung Park, Yash Belhe
**arXiv:** [arxiv.org/abs/2610.14136](https://arxiv.org/abs/2610.14136)
**Summary:** Correction training reduces diffusion exposure bias by learning a corrector on the base denoiser's own imperfect predictions and applying it repeatedly during sampling. It substantially improves unguided and unconditional generation across DiT, SiT, and JiT, combines well with classifier-free guidance, and can be distilled back into the base model to remove extra inference cost.

---

### 12. SWIFT: Self-guided Weak-to-strong dIFfusion models via Target extrapolation
**Authors:** Yanjin He, Cuifeng Shen, Wanzhou Lei, Maohua Li, Tao Lan, Kan Liu, Hanlin Tang, Qing Qu
**arXiv:** [arxiv.org/abs/2610.25844](https://arxiv.org/abs/2610.25844)
**Summary:** SWIFT uses a frozen early checkpoint to extrapolate clean training targets away from weak predictions, emphasizing components the stronger diffusion model has not yet learned. It beats matched standard training with no added inference path, surpasses one ImageNet-256 baseline's best FID at roughly half the compute, and reaches FID 1.15 without guidance on RAEv2.

---

### 13. MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records
**Authors:** Seohyun Lee, Jongha Kim, Dohwan Ko, Ji Soo Lee, Seoung Choi, Jayun Ku, Hyunwoo J. Kim
**arXiv:** [arxiv.org/abs/2610.27911](https://arxiv.org/abs/2610.27911)
**Summary:** MMEnterprise-Bench contains 1,613 questions over simulated workplace projects whose documents, chats, and figures accumulate revisions, conflicts, and missing evidence. Tests of 10 multimodal models show persistent failures on cross-source and temporal conflicts, while higher retrieval recall does not consistently improve answer accuracy.

---

### 14. LLM2R: From Large Language Models to 3D Reassemblers
**Authors:** Zhouhan Zhong, Qiuhong Shen, Xingyi Yang, Jinyi Xu, Xinchao Wang
**arXiv:** [arxiv.org/abs/2610.18604](https://arxiv.org/abs/2610.18604)
**Summary:** LLM2R compresses each 3D part into geometric tokens, processes the full set with a LoRA-adapted decoder-only language model, and predicts all poses in one non-autoregressive pass. It leads multiple part-assembly benchmarks, with its advantage growing to more than 29 accuracy points over strong baselines on 100-part objects.

---

### 15. Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs
**Authors:** Noam Rotstein, Yoad Tewel, Chen Tessler, Haggai Maron, Gal Chechik, Or Litany, Yoni Kasten, Yuval Atzmon
**arXiv:** [arxiv.org/abs/2610.28632](https://arxiv.org/abs/2610.28632)
**Summary:** This system connects an arbitrary-skeleton 3D motion model to a pretrained video generator through compact cross-attention layers and recovers a camera that registers the motion in the scene. Trained on nearly 200,000 pairs, it co-generates scene-aware video and replayable rig motion while also supporting video-to-motion, motion-to-video, and keyframe control.

---

### 16. Specter: Fast MoE Inference via Quantization-Enabled Multi-Step Speculative Offloading
**Authors:** Wenfeng Wang, Xiaofeng Hou, Xinfeng Xia, Xinkai WAng, Mingxuan Zhang, Peng Tang, Jiacheng Liu, Chao Li
**arXiv:** [arxiv.org/abs/2511.14102](https://arxiv.org/abs/2511.14102)
**Summary:** Specter runs a lightweight quantized draft model on the accelerator to predict several steps of future expert routing and prefetch offloaded mixture-of-experts weights from host memory. For single-request inference it improves time per output token by 1.50 times on average and up to 1.88 times, making memory-constrained MoE serving more practical on one commodity GPU.

---

### 17. EvaOmni: An Evidence-Grounded Benchmark for Audio-Visual Reasoning
**Authors:** Xiaoxing Hu, Wenxi Yao, Chaoyuan Shi, Ziqi Ye, Xiaorong Guo, Peixuan Li, Zhuoran Sun, Ziyang Gong, Peiyuan Zhang, Mingxin Liu, Shuran Ma, Hongbo Liu, Xiaomin Yu, Yu Tian, Wentao Wang, Zhenjie Yang, Jian Hu, Yunhang Shen, Haoyu Cao, Xue Yang
**arXiv:** [arxiv.org/abs/2610.28444](https://arxiv.org/abs/2610.28444)
**Summary:** EvaOmni evaluates both answers and the supporting audio and visual time intervals across 1,027 human-annotated questions, reducing textual and unimodal shortcuts. Even the strongest tested model reaches 79.1% accuracy on complex reasoning but only a 12.3% bottleneck grounded score, exposing weak localization of decisive multimodal evidence.

---

### 18. Evolving Agent Interfaces
**Authors:** Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega, Bhuvan Chandra Koduru, Chih-Lun Li, Jiachen Yang, Ang Li, Xin Eric Wang
**arXiv:** [arxiv.org/abs/2610.28601](https://arxiv.org/abs/2610.28601)
**Summary:** Agent S4 treats interface design as an agent capability, using a meta-agent to analyze task trajectories and evolve reusable interfaces plus guidance without success labels. Its Qwen3.8-27B configuration reaches a 21.3% binary score on OSWorld V2, 3.8 times the same model with fixed interfaces and above two frontier-model baselines at much lower cost.

---

### 19. Breaking Diffusion: Parallel Reasoning with Draft Refinement
**Authors:** Jaesang Yu, Seoyeon Byun, Yun Wang, Yan Lu, Juho Kim
**arXiv:** [arxiv.org/abs/2610.26542](https://arxiv.org/abs/2610.26542)
**Summary:** Draft Refinement Language Models use one denoiser to propose parallel token revisions and score complete candidate drafts with a cavity energy that removes self-token evidence. A 6M-parameter model reaches 44.4% on Countdown-5 and 93.9% on Sudoku-Extreme, outperforming autoregressive and discrete-diffusion baselines without reverse diffusion.

---

### 20. PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning
**Authors:** Yuanhang Lei, Baofei Liu, Xingxuan Li, Tao Cheng, Zixuan Wang, Boming Zhao, Yujun Shen, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
**arXiv:** [arxiv.org/abs/2610.26067](https://arxiv.org/abs/2610.26067)
**Summary:** PhysSkin++ learns continuous, shape-dependent neural skinning fields from static geometry through physics-informed self-supervision, avoiding per-object training and simulation trajectories. The compact deformation subspaces generalize across shapes and support real-time controlled, collision-aware, and rig-complementary animation for meshes, point clouds, and 3D Gaussians.
