---
title: "Daily AI Papers — October 06, 2026"
date: 2026-10-06
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-06/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - diffusion-models
  - multimodal-ai
---

### 1. Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation
**Authors:** Team Kandinsky, Julia Agafonova, Bulat Akhmatov, Mikhail Aksyutin, Grigorii Alekseenko, Anastasia Aliaskina, Olga Androsova, Vladimir Arkhipkin, Anna Averchenkova, Alexander Belykh, Serafima Bocharova, Sofiya Bogakovskaya, Anton Bukashkin, Mark Bulygin, Kirill Buzygin, Irina Cheremnykh, Kirill Chernyshev, Mikhail Chernyshov, Vladimir Chernyy, David Chikovani, Georgy Daniltsev, Denis Dimitrov, Anna Dmitrienko, Vladimir Dokholyan, Sergey Emelyanov, Dmitry Ermilov, Georgii Fedorov, Polina Gavrilova, Nikolai Gerasimenko, Aleksandr Gordeev, Andrey Inozemtsev, Andrei Ivaniuta, Alexander Ivanov, Mikhail Karaev, Anastasiia Kargapoltseva, Ivan Kirillov, Nikita Kiselev, Valeria Kobenko, Yury Kolabushin, Denis Koposov, Anatoly Korobov, Vladimir Korviakov, Kirill Kozlov, Denis Krzhivokolskiy, Konstantin Kuklev, Alexander Kunitsyn, Sergey Kuzin, Vladislav Lakhtionov, Alexey Letunovskiy, Maxim Litvinov, Alexander Lyulkov, Georgy Makarov, Kirill Malakhov, Egor Malykh, Mikhail Mamaev, Dmitrii Mikhailov, Polina Mikhailova, Ivan Mikheev, Elizaveta Muromtseva, Nikolai Nazarkin, Tatiana Nikulina, Lev Novitskiy, Stanislav Onuchin, Nikita Osterov, Denis Parkhomenko, Anatoliy Parpara, Vladimir Polovnikov, Konstantin Reznikov, Azat Saginbaev, Nikita Samsonov, Alexander Sentsov, Nikita Shaimov, Artem Sherstyuk, Andrey Shutkin, Egor Silvestrov, Bulat Suleimanov, Matvey Suprunov, Sergey Taranov, Irina Tolstykh, Tatiana Trofimuk, Ilya Trushkin, Aleksandra Tsybina, Olga Varlashina, Viacheslav Vasilev, Ilya Vasiliev, Eugeny Vilisov, Sergey Yakubson, Konstantin Zakharov
**arXiv:** [arxiv.org/abs/2610.05608](https://arxiv.org/abs/2610.05608)
**Summary:** Kandinsky 6.0 Video introduces 3B- and 29B-parameter diffusion models that generate five-second video with synchronized 44 kHz audio in text- and image-conditioned modes, plus Full-HD super-resolution. Its dual-stream CrossDiT and staged audio-video training outperform Kandinsky 5.0 in human evaluation and remain competitive with leading audio-video generators, with code and checkpoints released under MIT.

---

### 2. ALoDLM: Adaptively Looped Diffusion Language Models
**Authors:** Liancheng Fang, Zhuowei Li, Youngeun Kim, Tianchen Zhao, Rajat Koner, Jiaye Wu, Linghan Xu, Xuanbai Chen, Xiang Xu, Zheng Zhang, Jakub Zablocki, Nishant Sankaran, Yifan Xing
**arXiv:** [arxiv.org/abs/2610.04198](https://arxiv.org/abs/2610.04198)
**Summary:** ALoDLM replaces uniform diffusion-language-model computation with token-adaptive latent recurrence, committing easy tokens while giving harder positions additional refinement passes. At 1.7B and 8B parameters it beats all evaluated diffusion models and corresponding autoregressive baselines across eleven benchmarks while retaining fast parallel decoding.

---

### 3. Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy
**Authors:** Ruqing Ning, Haibo Meng, Zhishang Xiang, Zerui Chen, Jinsong Su, Xin Wang, Qinggang Zhang
**arXiv:** [arxiv.org/abs/2610.05162](https://arxiv.org/abs/2610.05162)
**Summary:** MemAdapter counters memory-induced sycophancy by using counterfactual induction to expose risk, context-aware reflection to calibrate each memory's influence, and evidence-based final reasoning. Experiments on three benchmarks show that it improves the reliability of long-term-memory agents even when stored memories are objectively correct but contextually misleading.

---

### 4. In-Distribution Forcing for Long Video Generation at Test Time
**Authors:** Jeongwoo Shin, Youngyoon Choi, Sangwoo Jo, Hyunmog Kim, Sungjoon Choi, Joonseok Lee, Jaewoong Choi, Jaemoo Choi
**arXiv:** [arxiv.org/abs/2610.03120](https://arxiv.org/abs/2610.03120)
**Summary:** In-Distribution Forcing addresses long-video drift by aligning both key-value caching and conditioning with the model's training setup, using self-caching to prevent out-of-distribution cache entries. The test-time method extends short-horizon autoregressive video diffusion models to minute-scale generation and substantially reduces visual and motion drift in metrics and user studies.

---

### 5. LMBuild: Evaluating LLM Agents for Generating Buildable and Functional Structures
**Authors:** Jiateng Liu, Rushi Wang, Cheng Qian, Xuejun Zhang, Sun Li, Jiayu Liu, Yifan Shen, Xu Cao, Jiarui Yao, Bingxuan Li, Ruhi Sarikaya, Heng Ji
**arXiv:** [arxiv.org/abs/2610.04292](https://arxiv.org/abs/2610.04292)
**Summary:** LMBuild evaluates whether LLM agents can create structures that are not only geometrically plausible but also buildable and functional, using an interactive construction environment and metrics for soundness, affordance, design, and realization. Tests of 30 systems show that frontier models largely overcome soundness and alignment bottlenecks, while functional operability and novel component design remain difficult.

---

### 6. Foundations of Proactive Agents: Principles, Technical Layers, and Proactivity-Gym
**Authors:** Jio Oh, Seunghyun Do, Young-Jun Lee, Steven Euijong Whang, Dongyeop Kang
**arXiv:** [arxiv.org/abs/2609.37267](https://arxiv.org/abs/2609.37267)
**Summary:** This work frames proactive agents around Task Capability, Temporal Allocation, and Trust, then introduces PROACTIVITY-GYM with multi-day scenarios, stateful environments, and persona-conditioned users. Evaluation of 23 model-harness configurations and a 30-person study finds large gaps across these goals, including sharp trust declines when interventions are misaligned despite correct outcomes.

---

### 7. Self-Generated Feedback Destabilizes Test-Time Training: A Causal Decomposition of Long-Horizon Adaptation
**Authors:** Cheng Luo, Bing Li, Bernard Ghanem
**arXiv:** [arxiv.org/abs/2610.05076](https://arxiv.org/abs/2610.05076)
**Summary:** The study shows that test-time training on a model's own generated text creates a feedback loop that degrades prediction on independent human-written text, even though the same update mechanisms help on real text. Causal comparisons isolate generation drift and update conflict, while a Settlement check on independent evidence nearly eliminates endpoint damage while preserving real-text adaptation.

---

### 8. Optimizing the Optimizer: Language Models Discover Faster Molecular Relaxation
**Authors:** Artem Tsypin, Vladimir Deshchenya, Kuzma Khrabrov, Denis Potapov, Maxim Radchenko, Artur Kadurin, Michael G. Medvedev
**arXiv:** [arxiv.org/abs/2610.06577](https://arxiv.org/abs/2610.06577)
**Summary:** An autoresearch agent rewrites the Sella molecular-geometry optimizer under gates that reject premature stopping and changes that fail to generalize, producing the AutoSella family. On held-out molecules and unseen potentials, its best variant uses only 40.2% to 77.2% of Sella's force calls at the r2SCAN-3c DFT level while achieving the same energy reduction.

---

### 9. CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG
**Authors:** Hyojeong Yun, Jueun Kim, Wook-Shin Han
**arXiv:** [arxiv.org/abs/2610.00923](https://arxiv.org/abs/2610.00923)
**Summary:** CANOPY compresses multimodal RAG evidence by scoring hierarchical regions and selecting different granularities without LLM calls for node-level pruning, while a critic requests targeted retrieval when evidence is insufficient. Across five QA benchmarks over a 33-million-item corpus it improves average accuracy, and in one Qwen3-VL setting cuts reader evidence tokens by 14.2% to 27.7% with comparable accuracy.

---

### 10. Towards Looped Models Done Right, Part II: Rethinking at Fixed Points
**Authors:** Benhao Huang, Chufan Shi, Junlin Chen, Shicheng Wen, Zhengzhong Liu, Eric Xing, Xuezhe Ma
**arXiv:** [arxiv.org/abs/2610.06833](https://arxiv.org/abs/2610.06833)
**Summary:** The paper exploits fixed-point behavior in looped language models to enable truncated training, terminal KV sharing, up to 1.79-times faster distilled prefill, and reinforcement-learning updates that are twice as fast. A learned depth prior and orthogonal input injection lower perplexity from 100M to 1.6B parameters, with the 1.6B model matching fixed-depth downstream performance using a three-times smaller KV cache.

---

### 11. OSWorld-Pro: Process-based Evaluation for Computer Use Agents
**Authors:** Zhilin Wang, Shaokun Zhang, Yifan Zhang, Hao Zhang, Jin Xu, Binfeng Xu, Jian Hu, Yunheng Zou, Karan Sapra, Andrew Tao, Jan Kautz, Yi Dong
**arXiv:** [arxiv.org/abs/2609.24890](https://arxiv.org/abs/2609.24890)
**Summary:** OSWorld-Pro adds process-level evaluation to computer-use agents with more than 300 tasks, 2,800 subgoals, and 67,000 human annotations judged by human-aligned LLM evaluators. It reveals distinct procedural failures hidden by end-state scoring, with the strongest reported model reaching 75.7% versus 83.4% on the original OSWorld evaluation.

---

### 12. Data Unlearning via Inverse Distillation
**Authors:** Aleksei Leonov, Nikita Kornilov, Zhenhe Zhang, Evgeny Burnaev, Iaroslav Koshelev, Alexander Korotin
**arXiv:** [arxiv.org/abs/2609.36099](https://arxiv.org/abs/2609.36099)
**Summary:** Inverse Distillation Unlearning jointly turns a multi-step flow or diffusion teacher into a one-step generator while suppressing a designated forget subset. The method needs only the pretrained teacher and forget-set examples, and experiments on MNIST and CIFAR-10 reduce forgotten-class generation while preserving quality on retained classes.

---

### 13. ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience
**Authors:** Haodong Lu, Dong Gong
**arXiv:** [arxiv.org/abs/2610.05303](https://arxiv.org/abs/2610.05303)
**Summary:** ASCENT performs online agentic test-time training by having a frozen initial model reinterpret verified deployment trajectories as privileged supervision, then distilling that signal into persistent LoRA fast weights. Across ALFWorld, WebShop, and AppWorld it improves success and interaction efficiency as experience accumulates, without external solutions, stronger teachers, or retrieval-based memory.

---

### 14. Representation-Space MMD for Diffusion Language Models
**Authors:** Ilya Drobyshevskiy, Ilia Sudakov, Maksim Semenov, Denis Kuznedelev, Maksim Ignatov, Pavel Temirchev, Nikita Balagansky, Viacheslav Meshchaninov, Nikita Gushchin, Dmitry Baranchuk
**arXiv:** [arxiv.org/abs/2610.06648](https://arxiv.org/abs/2610.06648)
**Summary:** This method post-trains diffusion language models by minimizing Maximum Mean Discrepancy between generated and reference distributions in a frozen model's representation space, reusing token-level features for efficient estimation. It lowers generative perplexity on OpenWebText, improves GSM8K accuracy-computation trade-offs, and increases decoding parallelism on 16B DMax-LLaDA2.0 models without sacrificing math and code accuracy.

---

### 15. OmniReasoning: Pushing the Limits of Audio-Visual Joint Reasoning
**Authors:** Junming Lin, Yuxuan Wang, Zhenxin Lei, Yuxin Liu, Ruixun Liu, Yinsong Yan, Ling Wang, Minghao Han, Yunfei Chu, Shun Lei, Xueyao Zhang, Qize Yang, Jin Xu, Yiwu Zhong
**arXiv:** [arxiv.org/abs/2609.39490](https://arxiv.org/abs/2609.39490)
**Summary:** OmniReasoning contributes a benchmark where audio and vision are jointly necessary, an evidence-grounded data engine, and modality-factored self-distillation for token-level cross-modal credit assignment. Its 30B-A3B model improves its Qwen3-Omni base by 12.8 points on OmniVideoBench and 9.3 points on OmniReasoningBench while also gaining on general and long-video tests.

---

### 16. SearchJev: A Fast and Calibrated System-1 Model for Search Agents
**Authors:** Congfeng Cao, Lipeng Zuo, Konstantinos Papakostas, Qiwei Xu, Songwei Xu, Lun Zhou, Zhaochun Ren, Yougang Lyu, Xiaohui Yan
**arXiv:** [arxiv.org/abs/2610.05107](https://arxiv.org/abs/2610.05107)
**Summary:** SearchJev directly scores legal search-agent decisions without autoregressive generation and uses soft-label learning to calibrate uncertainty before delegating difficult judgments to a System-2 model. It makes decisions 5.2 to 5.3 times faster with 41% to 74% lower calibration error, while dual-system agents speed active search by 3.7 to 4.7 times and raise BrowseComp-Plus accuracy from 45% to as much as 54%.

---

### 17. RobotUse: Allocating Computation, Context, and Decisions
**Authors:** Junhoo Lee, Injun Baek, Seungyeon Kim, Suhyun Jeon, Minkyu Kim, Baekseung Kim, Nojun Kwak
**arXiv:** [arxiv.org/abs/2610.04929](https://arxiv.org/abs/2610.04929)
**Summary:** RobotUse lets agents visually specify and revise robot targets and poses while a harness manages geometry, motion planning, control, subgoal context, and a persistent execution playbook. It reaches 45% success on RoboLab, 6.7 points above CaP-X, and shows that lessons from imperfect real-world feedback can transfer to later tasks.

---

### 18. Certification of Real Images through Calibrated Content Authentication
**Authors:** Sarim Hashmi, Abdelrahman Elsayed, Mohammed Talha Alam, Samuele Poppi, Nils Lukas
**arXiv:** [arxiv.org/abs/2610.05870](https://arxiv.org/abs/2610.05870)
**Summary:** A study of twenty deepfake detectors finds that accuracy drops from 99.5% to 76% on newer generators and below 2% under adversarial perturbations, motivating a reconstruction-based test of whether authenticity is plausibly deniable. The proposed calibrated detector bounds wrongly certified generated content at 1% in its tested setting and can preserve that bound against evaluated bounded-perturbation attacks where baseline detectors fail.

---

### 19. When to Switch: Reliable Action-Chunk Extension for Vision-Language-Action Models
**Authors:** Seonghoon Yu, Dongwon Kim, HyungRok Jung, Yoonjae Baek, Byung-kwan Lee, Suha Kwak, Jeany Son
**arXiv:** [arxiv.org/abs/2610.05719](https://arxiv.org/abs/2610.05719)
**Summary:** RACE extends vision-language-action chunks by predicting subskill transition timing with an auxiliary one-step denoising pass and conditioning action generation on that signal. In simulation it supports longer chunks with stronger reliability, and on a real robot four-times longer chunks reduce stop-and-go idle time about fivefold while outperforming same-length fine-tuning in success rate.

---

### 20. Noise Out, Bias In: Targeted Bias Injection in Diffusion Language Models via Closed-Loop Activation Steering
**Authors:** Sarim Hashmi, Mukul Ranjan, Abdelrahman Elsayed, Muhammad Umer Sheikh, Fahad Shamshad, Nils Lukas
**arXiv:** [arxiv.org/abs/2610.05894](https://arxiv.org/abs/2610.05894)
**Summary:** The paper identifies diffusion denoising trajectories as a control channel for targeted bias injection, using a proportional-integral controller to adjust activation steering toward an adversary-selected demographic answer. On LLaDA-8B-Instruct it raises targeted choices on ambiguous BBQ questions from 1.8 to 16.7 percentage points and stigmatizing SocialStigmaQA answers from 17.6% to 58.1%, outperforming fixed-strength steering with less output corruption.
