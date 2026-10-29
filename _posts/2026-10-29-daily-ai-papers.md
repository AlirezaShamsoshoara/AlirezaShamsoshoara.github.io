---
title: "Daily AI Papers — October 29, 2026"
date: 2026-10-29
permalink: /blog/ai-papers/2026/10/daily-ai-papers-10-29/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - multimodal-ai
  - efficient-inference
  - ai-agents
---

### 1. Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes
**Authors:** Wendi Sang, Kai Li, Yifan Li, Jianqiang Huang, Xiaolin Hu
**arXiv:** [arxiv.org/abs/2610.32749](https://arxiv.org/abs/2610.32749)
**Summary:** Falcon performs causal audio-visual target speaker extraction with a single-pass multi-scale separator and an encoder-space speaker contrastive loss, while RealSSA adds realistic simulated and recorded evaluation scenes. Relative to causal AV-TFGridNet, the paper reports 91.9% fewer parameters, 20.2 times less computation, and 11.1 times lower GPU inference latency while achieving state-of-the-art extraction quality on the evaluated benchmarks.

---

### 2. OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images
**Authors:** Junyeong Ahn, Geonwoo Kim, Kinam Kim, Gihwi Kim, Hoonjin Jung, Hyojin Jang, Jaegul Choo
**arXiv:** [arxiv.org/abs/2610.35684](https://arxiv.org/abs/2610.35684)
**Summary:** OmniShowcase combines geometry-driven synthetic training videos with surface-normal conditioning reconstructed from multiple reference views to preserve a subject across changing camera viewpoints. The authors release Showcase-4K and ShowcaseBench and report state-of-the-art subject identity and 3D consistency while maintaining competitive video quality and motion.

---

### 3. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success
**Authors:** Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
**arXiv:** [arxiv.org/abs/2610.31670](https://arxiv.org/abs/2610.31670)
**Summary:** Sensorimotor Alignment is a training-free offline metric measuring how sensory representations align with the geometry of physical motion. It correlates with downstream robot task success across model families and can help prioritize vision-language backbones before costly adaptation and closed-loop evaluation.

---

### 4. EmbeddingGemma 2: Unified and Efficient Multimodal Representations
**Authors:** Henrique Schechter Vera, Sahil Dua, Jovan Andonov, Sara Smoot, Sebastian Russo, Ivan Llanos, Max Matveev, Jae Hyeon Yoo, Kat Black, Shih-Cheng Huang, Josiah Aklilu, Maarten Grootendorst, Omar Sanseviero, Chandramouli Amarnath, Ian Ballantyne, Zhe Li, Daniel Salz, Ibrahim Alabdulmohsin, Ilya Philippov, Kristen Quan, Glenn Cameron, Edouard Yvinec, Luciano Martins, Doug Reid, Sindhu Raghuram Panyam, Weiyi Wang, Hengxuan Ying, Madhuri Shanbhogue, Tanmaya Dabral, Shanfeng Zhang, Juyeong Ji, Renjie Wu, Joe Zou, Xu Chen, Yunan Zhang, Yu-Hui Chen, Matthew Soulanille, Vinod Mamillapalli, Yi-Chun Kuo, Wai Hon Law, Matt Kreileder, Alice Zheng, Suril Shah, Mogan Shieh, Pooja Consul, Alberto Montes, Andreas Hess, Andres Sevilla, Babak Samari, Brendan McCloskey, Brian Potetz, Daniel Cer, Georgios Kathareios, Gustavo Hernández Ábrego, Hesen Zhang, Ji Ma, Jiaxing Wu, Keegan Mosley, Paul Suganthan, Rui Meng, Shen Gao, Shengcao Cao, Yi-Ting Chen, Yichang Chen, Zhongli Ding, Kendra Byrne, Cormac Brick, Olivier Lacombe, Qin Yin, Tris Warkentin, Armand Joulin, Tom Duerig, Mojtaba Seyedhosseini
**arXiv:** [arxiv.org/abs/2610.37364](https://arxiv.org/abs/2610.37364)
**Summary:** EmbeddingGemma 2 represents text, images, audio, video, and mixed-modality inputs in a unified embedding space using simplified per-layer embeddings and a progressive training curriculum. The paper reports a new quality-efficiency Pareto frontier and supports selective modality loading, adjustable vision token budgets, truncatable dimensions, and quantized weights.

---

### 5. Channel Selection for Mixture-of-Experts Decoding Needs No Calibration Data
**Authors:** Geunhyoung Kim, Sung Ju Hwang
**arXiv:** [arxiv.org/abs/2610.37386](https://arxiv.org/abs/2610.37386)
**Summary:** This paper shows that top-k channel selection can replace calibrated thresholds in mixture-of-experts decoding while fixing each token's read budget and avoiding observed repetition-loop failures. A weight-derived reader retains 98.1% of full-model accuracy at 17.8% of routed-expert reads, with Triton kernels accelerating MoE blocks by 1.60 to 1.90 times over optimized vLLM at batch one.

---

### 6. MatAnyone-E: Sparse Memory Propagation for Efficient High-Resolution Video Matting
**Authors:** Shuyun Wang, Shangchen Zhou, Peiqing Yang, Yuekun Dai, Xin Yu, Chen Change Loy
**arXiv:** [arxiv.org/abs/2610.35724](https://arxiv.org/abs/2610.35724)
**Summary:** MatAnyone-E identifies uncertain regions and useful memory candidates at low resolution, then restricts expensive high-resolution matching to those regions while using a lightweight decoder. At 4K it reports comparable matting quality, an estimated 7.4-times inference speedup, and peak GPU memory at 7.6% of MatAnyone 2, reaching 28.62 FPS with compilation on an NVIDIA H200.

---

### 7. h1: A Taste of the Bitter Lesson in Automated Theorem Proving
**Authors:** Skander Moalla, Ahmad Rammal, Niket Patel, Remi Munos, Julia Kempe
**arXiv:** [arxiv.org/abs/2610.35962](https://arxiv.org/abs/2610.35962)
**Summary:** h1 is a simple theorem-proving harness that gives a model an efficient Lean 4 interface and scales execution feedback and self-reflection without prescribing decomposition or search. It achieves state-of-the-art results on three formal-mathematics benchmarks, settles eight open FormalConjectures problems, and shows that interface efficiency strongly affects cost and solve rate.

---

### 8. TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving
**Authors:** Shuhuai Li, Shengdong Ye, Dongdong Ge, Yinyu Ye, Jianghao Lin
**arXiv:** [arxiv.org/abs/2610.37230](https://arxiv.org/abs/2610.37230)
**Summary:** TAO jointly schedules and places agent sessions using tool-return readiness, time-decayed cache credit, and token footprint under GPU capacity constraints. Across 12 model-workload-concurrency settings, it reports up to 26.8% lower latency, 36.3% lower mean time to first token, and 29.5% higher decode throughput relative to the best evaluated baseline for each metric.

---

### 9. RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents
**Authors:** Yunqi Liu, Peiyu Wang, Bingli Wang, Leo Luo, Xuanwu Song, Xudong Ma, Hongxin Li, Yaxin Du, Weicheng Gu, Fanglin Xu, Yi Xing, XiangLong Liu, Jujie He, Zhange Zhang, Huatong Song, Zhaoyi Li, Deyang Kong, Chuan Hao, Peihao Wu, Mingjie Tang, Ran Tao, Jian Yang, Wayne Xin Zhao, Bryan Dai
**arXiv:** [arxiv.org/abs/2610.22507](https://arxiv.org/abs/2610.22507)
**Summary:** REALCLI pairs complete-specification CLI tasks with scripted runtime collaboration to measure both execution and human-agent interaction across five dimensions. The strongest evaluated configuration reaches only 49.2% average score and 37.6% joint collaboration score, exposing gaps in steerability, trust calibration, and safety boundary management.

---

### 10. Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous Omnimodal Streams
**Authors:** Yinsong Yan, Ling Wang, Yuxuan Wang, Yifan Yang, Ruiyang Xu, Junming Lin, Qi Chen, Meng Gao, Minghao Han, Yunfei Chu, Qize Yang, Xize Cheng, Jin Xu, Jibin Wu
**arXiv:** [arxiv.org/abs/2610.35439](https://arxiv.org/abs/2610.35439)
**Summary:** Omni-InteractScope evaluates proactive streaming assistants on 1,479 human-annotated interactions with 1,790 temporal targets across eight task groups. Across 12 models, on-time first responses cover at most 40% of tool-invocation targets, joint timing-and-tool accuracy peaks at 32.0%, and query-free reminder recall never exceeds 23.0%.

---

### 11. Beyond the Estimate: Wiener-Informed Decoding for Easier Training of Pixel-Space Flow Models
**Authors:** Ziqiao Wang, Yang You
**arXiv:** [arxiv.org/abs/2610.36192](https://arxiv.org/abs/2610.36192)
**Summary:** Wiener-informed Decoding uses image statistics to initialize a trainable prediction path and coefficient interfaces that ease velocity learning in pixel-space flow models. It improves training speed and generation quality across architectures, with PixelDiT-XL reaching FID 1.53 on ImageNet 256 by 256 after 500 epochs, matching comparable PixelDiT quality with 37.5% fewer epochs.

---

### 12. Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation
**Authors:** Hyunwoong Bae, Jisu Han, Jiyeon Choi, Dohoon Kim, Taesup Moon
**arXiv:** [arxiv.org/abs/2610.34674](https://arxiv.org/abs/2610.34674)
**Summary:** OSMA-Bench compares spatially matched household-navigation scenarios that differ only in obstacle type, using a Semantic Sensitivity Index to assess safety-conditioned motion. Evaluated VLM and VLA policies recognize safety-relevant distinctions but fail to consistently translate them into clearance and speed, while an explicit parameter-inference step improves adaptation for VLM-based policies.

---

### 13. RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions
**Authors:** Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li
**arXiv:** [arxiv.org/abs/2610.36791](https://arxiv.org/abs/2610.36791)
**Summary:** RynnWorld-Latent uses 3D-grounded universal latent actions to train a controllable video world model across human videos, robot demonstrations, and simulation rollouts. Pretrained on approximately 553.5 million frames from 23 datasets, it improves evaluated video prediction and uses synthetic demonstrations to improve policy success on simulation benchmarks and two real-robot platforms.

---

### 14. Timestral
**Authors:** Adrien Petralia, Alexandre Gavaudan, Artjom Joosen, Etienne Goffinet, Richard Kurle, Yassine El Ouahidi, Yassir Bendou, Abdelaziz Bounhar, Abhijeet Somani, Aditi Kabra, Adrian Valente, Adrien Sadé, Ahmed Djermani, Alan Jeffares, Albert Jiang, Alberto Bietti, Aleksandr Timashov, Alexandre Cahill, Alexandre Laval, Alexandre Sablayrolles, Alexandros Sanchez Vassopoulos, Amélie Héliou, Amos You, André Jonasson, Andreas Fürst, Andrew Bai, Andrew Ehrenberg, Andrew Zhao, Andy Lo, Angele Lenglemetz, Anmol Agarwal, Antonia Calvi, Arata Suzuki, Arjun Majumdar, Arthur Fournier, Ashwani Kumar, Augustin Lombard, Avinash Sooriyarachchi, Aylin Guliz Akkus, Aysenur Karaduman, Baptiste Bout, Baptiste Rozière, Barna Pásztor, Baudouin De Monicault, Benjamin Holzschuh, Benjamin Tibi, Benno Stein, Bernhard Stadlbauer, Bhargavi Bhaskar, Binbing Hou, Błażej Osiński, Boris van Breugel, Camille Le Scao, Chaoran Yu, Charlotte Cronjäger, Chen-Yo Sun, Chris Bamford, Christian Wallenwein, Christophe Renaudin, Clémence Lanfranchi, Colin Bonatti, Corentin Barreau, Corentin Sautier, Cristiana-Diana Diaconu, Cyprien Courtot, Daniel Lopes, Daniel Marczak, Darius Dabert, Diego de las Casas, Dominik Nuss, Dylan Rubini, Dzmitry Soupel, Elizaveta Demyanenko, Elliot Chane-Sane, Emilien Fugier, Emmanuel Gottlob, Erik Aas, Etienne Duchesne, Fabian Paischer, Fabian Schlager, Faruk Ahmed, Federico Baldassarre, Félix Rosseeuw, Filip Szatkowski, Filippo Vicentini, Florian Wiesner, Gabrielle Berrada, Gaëtan Ecrepont, Gaspard Blanchet, Gaspard Donada-Vidal, Gaurav Mahajan, Gauthier Guinet, Genevieve Hayes, Georgii Novikov, Georgios Christoglou, Giada Pistilli, Gonzague de Carpentier, Graeme Nail, Guillaume Breton, Guillaume Kunsch, Guillaume Lample, Guillaume Martin, Guillaume Raille, Guillaume Richard, Guillem Simeon, Gunjan Dhanuka, Gunshi Gupta, Hamza Senhaji Rhazi, Han Zhou, Hédi Hadiji, Himanshu Jaju, Hope McGovern, Hubert de Parseval, Hugo Cisneros, Hugo Germain, Hugo Thimonier, Hugo Venturini, Hyeonju Lee, Hyunwoo Oh, Iliass Lasri, Ilyas Oulkadda, Jacques Sun, Jan Ludziejewski, Jason Rute, Jean de Becdelièvre, Jean Quentin, Jean-Malo Delignon, Jessica Chudnovsky, Jianchao Li, Jie Zhang, Jin Bin Ou, Joachim Studnia, Joep Barmentlo, Johannes Brandstetter, John Harvill, Jonas Amar, Jonas Schweizer, Jonathan Roberts, Joséphine Delas, Josselin Somerville, Jules Depersin, Julien Denize, Julien Tauran, Julien Verlaguet, Kartik Khandelwal, Khyathi Raghavi Chandu, Kilian Tep, Konstantin Mishchenko, Kris Szczepaniak, Kush Jain, Larissa Laich, Laura Calem, Laurence Aitchison, Laurent Callot, Laurent Fainsin, Léo Cotteleer, Léonard Blier, Loïc Chadoutaud, Loïck Chambon, Lorenzo Proietti, Louis Faucon, Louis Martin, Louis Serrano, Lu Li, Luc Boudier, Lucas Fernandes Martins, Lucas Mebille, Lucile Saulnier, Ludovic Ho Fuh, Luis Montero, Łukasz Borchmann, Maarten Buyl, Malik Hassan Raza, Manon Chossegros, Marcin Możejko, Margaret Jennings, Markus Hennerbichler, Martin Alexandre, Mathieu Poirée, Mathieu Schmitt, Mathilde Guillaumin, Mathis Felardos, Matthieu André, Matthieu Dinot, Matthieu Futeral, Maurits Bleeker, Mauro Comi, Max Mynter, Maxim Berman, Maxime Darrin, Maxime Langelier, Maxime Louis, Maximilian Augustin, Maximilian Müller, Mehdi Bouaziz, Melina Jingting Laimon, Mert Unsal, Mia Chiquier, Michael Pilcer, Michał Pietruszka, Michał Zając, Mickaël Seznec, Mikhail Biriuchinskii, Minh-Quang Pham, Minwoo Kang, Mircea Lica, Morgane Rivière, Namit Katariya, Natasha Ørregaard Klingenbrunn, Nathan Bout, Nathan Grinsztajn, Nathan Simpson, Neeraj Aggarwal, Neil Ashton, Neil Mallinar, Nick Bührer, Nicolas Moreau, Nicolò Lucchesi, Ola Mysiak, Oliver Leicht, Olivier Bousquet, Olivier Koch, Parag Jain, Patricia Wang, Patrick Blies, Patrick von Platen, Patryk Saffer, Paul Jacob, Paul Teiletche, Paul Wambergue, Paula Kurylowicz, Pavan Kumar Reddy, Pavel Kuksa, Philippe Formont, Philippe Pinel, Philomène Chagniot, Pierre Glandon, Pierre Stock, Pierre-André Savalle, Piotr Miłoś, Poojan Shah, Prateek Gupta, Pravesh Agrawal, Pui Ki Chan, Quentin Desreumaux, Quentin Selle, Quentin Torroba, Quentin Wargnier, Quercus Hernandez, Ram Ramrakhya, Randall Isenhour, Ranjit Parva, Raphaël Balouka, Raphaël Rialland, Raul Perez Pelaez, Reinhard Sonnleitner, Remi Delacourt, Rishi Shah, Rob Romijnders, Rohan Shah, Rohin Arora, Romain Sauvestre, Roman Soletskyi, Ronan Riochet, Rosalie Millner, Rupert Menneer, Sagar Vaze, Samuel Barry, Samuel Belkadi, Samuel Humeau, Samuele Papa, Sanchit Gandhi, Sandeep Cranganore, Sandeep Subramanian, Sarthak Mittal, Saskia Adaime, Scott Matthews, Sean Cha, Sebastian Kaltenbach, Seungjae Jung, Shashwat Verma, Sherif Waly, Shrimai Prabhumoye, Siddhant Waghjale, Siddharth Gandhi, Simon Lepage, Simon Sorg, Soham Ghosh, Sophie Marbach, Srijan Mishra, Stanislas Lange, Steve Hong, Sumukh Aithal, Szymon Antoniak, Tarun Kumar Vangani, Teddy Turquet, Teven Le Scao, Théo Cachet, Thibaut Lavril, Thomas Chabal, Thomas Coste, Thomas Defard, Thomas Foubert, Thomas Loux, Thomas Robert, Thomas Wang, Tianyu Zhang, Tim Lawson, Timothée Lacroix, Timothy Wallis, Tobias Kronlachner, Tom Bewley, Tom Edwards, Tomas Hodan, Triantafyllos Afouras, Tuhin Das, Tyler Wang, Udit Saxena, Ulrick Blé, Umar Jamil, Umberto Tomasini, Valentin Macé, Van Phung, Venkata Reddy, Vibha Masti, Victor Jouault, Victor Letzelter, Victor Paltz, Victor Poucheret, Vincent Maladière, Vincent Pfister, Virgile Richard, Vladislav Bataev, Wassim Bouaziz, Wen Ding Li, William Flanagan, William Havard, William Marshall, Witold Jędrzejewski, Xinghui Li, Xingran Guo, Xinyu Yang, Xuanyu Zhang, Yann Dreze, Yann Viegas, Yannic Neuhaus, Yassine Turki, Yessin Moakher, Yi He, Yihan Wang, Yimu Pan, Yuying Zhu, Yves Martin des Taillades, Zaccharie Ramzi, Zhenlin Xu, Zsófia Csákány
**arXiv:** [arxiv.org/abs/2610.37585](https://arxiv.org/abs/2610.37585)
**Summary:** Timestral introduces four probabilistic time-series foundation models with 5M to 209M parameters, combining Decoupled Horizon Forecasting, known-future covariates, and synthetic-first training. The 209M and 123M variants take the top two positions on every reported metric across GIFT-Eval, TIME, and fev-bench, with weights and inference code released.

---

### 15. The Lexical Imprint of Pre-training Data
**Authors:** Jeonghoon Kim, Woojin Chung, Woomin Song, Cheonbok Park, Nako Sung, Jinwoo Shin
**arXiv:** [arxiv.org/abs/2602.10657](https://arxiv.org/abs/2602.10657)
**Summary:** This paper uses tokenizer-agnostic unigram cross-entropy to measure lexical alignment between pretraining corpora and benchmark targets without running a model. Controlled training across four corpora, three model scales, and ten benchmarks shows that alignment tracks zero-shot accuracy, while document selection and domain-drafter routing turn the signal into accuracy and throughput gains.

---

### 16. TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using Conversational Agents
**Authors:** Krishanu Adhikary, Prashant Devadiga
**arXiv:** [arxiv.org/abs/2610.30161](https://arxiv.org/abs/2610.30161)
**Summary:** TauIndianBankBench evaluates tool-using conversational agents on 1,000 Indian retail-banking tasks by checking required procedure steps and unrequested changes as well as final records. End-state-only evaluation incorrectly accepts 6.5 to 12.0% of sessions for every tested model, demonstrating that outcome checks can miss procedural failures.

---

### 17. Your Policy Is Secretly a Harness: The Decision Geometry of Agent Interfaces
**Authors:** Jian Mu, Ruibo Shen, Yao Shu
**arXiv:** [arxiv.org/abs/2610.37255](https://arxiv.org/abs/2610.37255)
**Summary:** This paper separates an agent harness's attainable return ceiling from the trained policy's mismatch, showing that fixed-model comparisons can conflate interface quality and learned preferences. In MiniWoB++, reversing observation-field order drops success from 85.0% to 19.2% despite unchanged optimal decisions, while retraining under rejected but higher-ceiling harnesses outperforms the original agent.

---

### 18. Vision-Language-Action or World-Action? Just Action Models
**Authors:** Yonghao Yu, Lang Huang, Runyi Li, Toshihiko Yamasaki
**arXiv:** [arxiv.org/abs/2610.37219](https://arxiv.org/abs/2610.37219)
**Summary:** Just Action Model decouples backbone initialization, future-observation supervision, and inference machinery, training an action expert with a foresight head that is discarded after training. Its policies improve over matched FastWAM and ImageWAM baselines, with LIBERO-Plus success rising from 55.3% to 64.5% versus FastWAM and estimated online training FLOPs reduced by 73% when foresight targets are cached.

---

### 19. MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model
**Authors:** Brian Ko, Han Wang, Hejia Geng, Li Erran Li, Sherry Yang
**arXiv:** [arxiv.org/abs/2610.37175](https://arxiv.org/abs/2610.37175)
**Summary:** MLE-World predicts training logs, error traces, and validation scores from an ML program and data description, using confidence to decide when real execution is needed. On 17 MLE-bench Lite tasks it matches held-out terminal outputs on 77.9% of programs and enables test-time search policies with up to 22.1% higher observed mean performance and less real execution.

---

### 20. Learning and Reasoning with Geometry: How Generation Helps Spatial Understanding
**Authors:** Rui Yang, Yanwei Li, Sili Chen, Jingjia Huang, Yi Lin, Hengshuang Zhao
**arXiv:** [arxiv.org/abs/2610.36022](https://arxiv.org/abs/2610.36022)
**Summary:** GeoUG unifies geometric generation and spatial understanding through depth and multi-view supervision, then adaptively generates evidence to confirm or revise an initial answer. Reinforcement learning balances accuracy against generation cost, achieving circular accuracies of 97.9%, 90.8%, and 94.2% on CV-Bench-3D, 3DCueBench, and DA-2K with fewer generation calls than always generating.
