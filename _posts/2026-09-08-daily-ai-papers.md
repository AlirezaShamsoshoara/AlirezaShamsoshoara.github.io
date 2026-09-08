---
title: "Daily AI Papers — September 08, 2026"
date: 2026-09-08
permalink: /blog/ai-papers/2026/09/daily-ai-papers-09-08/
categories:
  - ai-paper-summary
tags:
  - daily-digest
  - ai-agents
  - multimodal-ai
  - efficient-llms
---

### 1. Compile by Training: Turning Natural-Language Specifications into Local Neural Functions
**Authors:** Yuntian Deng, Pengyu Nie, Stuart Shieber
**arXiv:** [arxiv.org/abs/2609.04199](https://arxiv.org/abs/2609.04199)
**Summary:** Many recurring text functions are easy to describe but difficult to implement with rules, while calling a large remote model for every input introduces repeated cost, latency, and dependency on a provider. We present compile by training, which turns a natural-language specification into a reusable neural function.
**Trending because:** 377 HuggingFace upvotes + turns reusable natural-language specifications into local neural functions that cut repeated model cost and latency

---

### 2. Dr. Claw: An AI Scientist Workspace for Vibe Research
**Authors:** Dingjie Song, Hanrong Zhang, Dawei Liu, Yixin Liu, Zongxia Li, Zhengqing Yuan, Siqi Zhang, Henry Peng Zou, Zhiling Yan, Yuxuan Zhang, Yanfang Ye, Philip S. Yu, Lichao Sun
**arXiv:** [arxiv.org/abs/2609.00365](https://arxiv.org/abs/2609.00365)
**Summary:** Command-line coding agents (e.g., Claude Code, Gemini CLI) can already read and write files and sustain long sessions, yet end-to-end research still fragments across chat tools, IDEs, terminals, and writing environments, and the decisions that make it auditable are rarely preserved. We present Dr. Claw, an open-source workspace that wraps existing coding-agent executors in a controllable and auditable human-in-the-loop workflow rather than introducing another autonomous agent.
**Trending because:** 123 HuggingFace upvotes + offers an auditable human-in-the-loop workspace for end-to-end AI research

---

### 3. Bilevel Coordinated Reflection: A Game-Theoretic Approach to Multi-Agent LLM Systems
**Authors:** Yihang Chen, Yuxiang Chen, Yuxuan Huang, Meng Fang, Weilin Luo, Jun Wang
**arXiv:** [arxiv.org/abs/2609.02750](https://arxiv.org/abs/2609.02750)
**Summary:** Multi-agent LLM systems commonly use an orchestrator to decompose a task for a team of workers and then improve through textual reflection. Despite strong empirical results, these systems lack a unified account of coordination, memory improvement, and the role of external verification.
**Trending because:** 119 HuggingFace upvotes + connects coordination, reflection, memory, and verification in multi-agent LLM systems

---

### 4. RoboTok: An Internet-Scale Data Engine for Human Demonstration Retrieval and Dexterous Manipulation Learning
**Authors:** Howard Qian, Yiting Chen, Yunfei Xie, Kejia Ren, Podshara Chanrungmaneekul, Gaotian Wang, Bowen Wen, Chen Wei, Kaiyu Hang
**arXiv:** [arxiv.org/abs/2609.03199](https://arxiv.org/abs/2609.03199)
**Summary:** Robot learning increasingly depends on broad and diverse demonstrations, yet collecting robot data remains expensive and poorly suited to covering the long tail of real-world tasks. To address this bottleneck, we introduce RoboTok, an internet-scale data engine that, given a query human manipulation video, retrieves manipulation-relevant human demonstrations from web videos for training dexterous robot policies.
**Trending because:** 116 HuggingFace upvotes + uses web-scale human demonstrations to attack the robot-data bottleneck

---

### 5. Unlocking Lossless Speedups in LLMs via Discrete Diffusion
**Authors:** Subham Sekhar Sahoo, Lingjie Chen, Khiem Pham, Jonathan Geuter, Chaitanya Dwivedi, Varad Pimpalkhute, Yash Akhauri, Alexander Moreno, Mikhail Yurochkin, Zhenting Wang, Mostafa Elhoushi, Nolan Dey, Shane Bergsma, Joel Hestness, John Thickstun, Eric Xing, Zhengzhong Liu
**arXiv:** [arxiv.org/abs/2609.04010](https://arxiv.org/abs/2609.04010)
**Summary:** Large Language Models (LLMs) owe much of their success to next-token prediction (NTP), but their autoregressive (AR) structure requires slow, sequential token generation. To overcome this bottleneck, we introduce diffusion-augmented LLMs, a new class of models that defines an AR model distribution while using diffusion to draw multiple tokens in parallel from that distribution.
**Trending because:** 56 HuggingFace upvotes + promises parallel decoding speedups while preserving an autoregressive model distribution

---

### 6. Iris: Climbing to the Search Frontier
**Authors:** Ziyuan Liu, Hengqi Liu, Zichuan Wang, Yang Qin, Jiachen Liang, Xu Chu, Shaowei Chen, Yuantao Gu, Mu Chuan
**arXiv:** [arxiv.org/abs/2609.04304](https://arxiv.org/abs/2609.04304)
**Summary:** We present Iris-mini and Iris-pro, two search agents trained at the 35B-A3B and 397B-A17B scales, together with the data pipeline and training recipe behind them. Tasks are reverse-constructed from the hyperlink structure of a web corpus: we author multi-hop chains over an entity graph distilled from a seed page and its out-links, rewrite every non-answer entity into a descriptive reference so that no clue can be resolved by string matching, and admit only questions that a reference model fails closed-book yet solves once the supporting evidence is supplied.
**Trending because:** 53 HuggingFace upvotes + trains search agents on hard multi-hop questions that require retrieved evidence

---

### 7. Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction
**Authors:** Chin-Yang Lin, Yang-Che Sun, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu
**arXiv:** [arxiv.org/abs/2609.04201](https://arxiv.org/abs/2609.04201)
**Summary:** Online 3D reconstruction models perform poorly on long videos. This happens because regressing poses relative to a fixed first-frame anchor forces extrapolation far beyond the training distribution.
**Trending because:** 46 HuggingFace upvotes + targets efficient online 3D reconstruction over long videos

---

### 8. FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience
**Authors:** Zixun Huang, Kishan Panaganti, Haitao Mi, Leowei Liang
**arXiv:** [arxiv.org/abs/2609.03241](https://arxiv.org/abs/2609.03241)
**Summary:** A reasoning model can improve from its own on-policy experience, but this inner loop is fragile: terminal verifiers provide reliable yet sparse supervision, while dense same-model guidance can reinforce false confidence or overconcentrate learning on a narrow solution mode. We introduce FlowBalance, a verifier-grounded self-improvement method that learns a normalized distribution over complete responses.
**Trending because:** 40 HuggingFace upvotes + combines sparse verifier rewards with stable dense guidance for reasoning self-improvement

---

### 9. Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue
**Authors:** Chengqian Ma, Wei Tao, Haoyu Zhang, Yiwen Guo
**arXiv:** [arxiv.org/abs/2609.04250](https://arxiv.org/abs/2609.04250)
**Summary:** An avatar that holds a conversation should decide what to say and to move while saying it, yet these abilities live in separate model families: spoken dialogue models produce speech without motion, and co-speech motion models produce motion only from audio handed to them. The standard remedy is a cascade that first generates the spoken response and then runs a motion model over the finished audio, which requires a second full inference pass and precludes any joint optimisation between the two.
**Trending because:** 38 HuggingFace upvotes + jointly generates conversational speech and full-body motion in one model

---

### 10. Last Translation Benchmark
**Authors:** Vilém Zouhar, Niyati Bafna, Mukund Choudhary, Maike Züfle, Sara Rajaee, Pinzhen Chen, Jannis Vamvas, Sara Papi, Ona de Gibert, Bhavitvya Malik, Eliya Habba, Orfeas Menis Mastromichalakis, Patrícia Schmidtová, Michelle Wastl, Sheriff Issaka, Leshem Choshen, Stella Biderman, Antonis Anastasopoulos, Jan Niehues, Rico Sennrich, Mrinmaya Sachan, Ondřej Bojar, Kenton Murray, Jörg Tiedemann, Alham Fikri Aji, Philipp Koehn, Christof Monz, Alexandra Birch, Sowmya Vajjala, Chalamalasetti Kranti, Cristina España-Bonet, Nobin Sarwar, David Kaczér, Shunta Asano, Malik Marmonier, Daban Q. Jaff, Vaisakhi Mishra, Hend Al- Khalifa, Gabriele Sarti, Sourajit Saha, Nils Rehlinger, Juan Daniel Cuervo Villa, Jonathan Tonglet, Saugata Purkayastha, Dominik Macháček, Jagannathan Ramanujam, Heejin Do, Zuzana Nadova, Fred Philippy, Fabian Retkowski, Maria Lymperaiou, Silvia Casola, Hanna Yukhymenko, Shubhashis Roy Dipta, Sangwon Ryu, Andrés Jerez, Ron Keinan, Shuaib Shuaib Yusuf, Avantica Vempati, Maria Carmen Staiano, Sukannya Purkayastha, Adrian Cosma, Vitalii Babenko, Erivan Inan, Aviral Nigam, Wafa Aissa, Fatima Haouari, Venkata Prasanth Kumar Gummadi, Mehdi Jafarzadeh, Valentin Scourneau, Lukas Edman, Kaiser Sun, Shaomu Tan, Mohammad Sadegh Gholizadeh, Johannes-Rudolf David, Dipankar Srirag, Javier García Gilabert, Ruta Binkyte, Manar Ali, Ana-Maria Bucur, Sabry E. Farrag, Youssef Saber, Yihong Liu, Jean Maillard, Cojocaru Nicoleta, Xiaochuang Yuan, Sina Ahmadi, Philipp Mondorf, Kaustubh Dhole, Roman Wixinger, Shenbin Qian, Manuel Tuor, Sergey Troshin, Jonathan Yahav, Fida Mohammad Thoker, Amir Arsalan Rezapour, Lance Calvin Lim Gamboa, Manon Reusens, Kätriin Kukk, Koel Dutta Chowdhury, Giuseppe Gallipoli, Christian Hoang, Shaswati Saha, Seth Aycock, Jan Kocoń, Bo Chen, Linh Vu, Vatsal Venkatkrishna, Arafat Ahsan, Luan Thanh Nguyen, Hassan Soliman, Daryna Dementieva, Theresia Veronika Rampisela, Ngoc Quynh Tram Do, Marius Huber, Kazuki Egashira, Azmine Toushik Wasi, Vladislav Poritski, Mike Zhang, Deep Shah, Paul Gavrikov, Luis Frentzen Salim, David Africa, R. Damanhuri, Bello Umar Bello, Anumit Garg, Gengyu Rao, Pawan Sasanka Ammanamanchi, Kamile Dementaviciute, Andrianos Michail, L D M S Sai Teja, Dawei Zhu, Yi Fan, Wei Liu, Farhan Farsi, Elias Herranen, Sankalan Pal Chowdhury, Karen Sanchez, Farzad Shami, Ashok Urlana, Zimu Wang, Tomasz Limisiewicz, Priyaranjan Pattnayak, Marii Ojastu, Hongbin Na, Emilian Radoi, Chenyi Zhao, Carlos Hinojosa, Andrea Gregor de Varda, Zaid Alyafeai, Reem Alzahrani, Nehal Kathrotia, Alex Flückiger, Ulysses Sekai Tully Carr, Jimson Paulo Layacan, Guy Kaplan, Ritwik Tiwari, Rishit Dagli, Oksana Volchek, Isaac R Caswell, Bowen Yi, Blanka Kövér, Amir Hossein Yari, Aicha Chorana, Zhengxiang Wang, Selja Keränen, Samuel Simko, Joy Olusanya, Jenny Chim, Enzo Doyen, Vivek Harsha Lakkamaneni, Sophia Conrad, Pouya Sadeghi, Panayiotis Panayiotou, Luis Lara, Jannatul Nayem, Eran Yahav, Debanshu Das, Antonia Karamolegkou, Anmol Goel, Aishik Mandal, Tommaso Cerruti, Raoyuan Zhao, Mykola Haltiuk, Thura Aung, Naser Almousa, Amir Hossein Kargaran, Rachel Bawden, Qiaoyuan Zheng, Mateusz Lango, Beni Egressy, Fidel Rodríguez Velásquez, Natchapon Jongwiriyanurak, Minh Ngoc Do, Marco Gaido, Lena Libon, Dzmitry Kuzmin, Badal Nyalang, Antoine Taroni, Andrei Niculae, Abdulaziz Nura Kani, Rushikesh Zawar, Marek Šuppa, Beatrice Savoldi, Andreas Simons, Rayyan Merchant, Ilai Yaron Levy, Francesco Pinto, Ziyi Yang, Yolanda Xavier, Samuel Frontull, Muhammad Ravi Shulthan Habibi, Kenneth Enevoldsen, Harris Abdul Majid, Francesca Padovani, Tim Graf, Tatiana Bielakova, Sharifa Djurabaeva, Shaoxiong Ji, Raia Abu Ahmad, Pavel Stepachev, Jirui Qi, Ayush Sunil Munot, Alireza Pakniat, Ayla Rigouts Terryn, Yuxing Lu, Yurii Paniv, Xiyan Fu, Tosin Adewumi, Sunisth Kumar, Stéphane J. P. S. Thunus, Shree Harsha Bokkahalli Satish, Shayan Bali, Prakhar Gupta, Papa Abdou Karim Karou Diallo, Matija Akrap, Marko Culjak, Kristýna Onderková, Joseph Attieh, Esrael Teferi Tensay, Elisabeth Fittschen, Benoît Sagot, Jingwei Ni, Yu Fan
**arXiv:** [arxiv.org/abs/2609.04173](https://arxiv.org/abs/2609.04173)
**Summary:** For scientific progress, we need benchmarks that test the limits of state-of-the-art models, and evaluation methods that inform us about failure cases. As models get stronger, standard benchmarks for machine translation are approaching saturation.
**Trending because:** 33 HuggingFace upvotes + focuses evaluation on the hard cases left as standard machine-translation benchmarks saturate

---

### 11. The Attention Triangle in Audio-Video Models
**Authors:** Sagi Polaczek, Noa Kraicer, Gal Metzer, Zhuo Ning, Ali Mahdavi-Amiri, Daniel Cohen-Or, Raja Giryes
**arXiv:** [arxiv.org/abs/2609.03586](https://arxiv.org/abs/2609.03586)
**Summary:** Audio-video diffusion models rely on cross-modal attention to coordinate text, sound, and visual content, yet this same mechanism can introduce subtle and systematic semantic leakage. We study these models by probing and analyzing the ``attention triangle,'' comprising the three cross-attention edges connecting the text, audio, and video streams, and examine how semantic information is routed across modalities during generation.
**Trending because:** 28 HuggingFace upvotes + reveals how cross-modal attention can leak semantics across audio and video streams

---

### 12. DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training
**Authors:** Shubham Gandhi, Saurabh Goyal, Kiran Kate, Yara Rizk
**arXiv:** [arxiv.org/abs/2609.04094](https://arxiv.org/abs/2609.04094)
**Summary:** Reinforcement Learning from Verifiable Rewards works well when a task has a programmatic checker, but most long-horizon agent domains have none. We work in the outcome-blind setting, where ground-truth success signals are not available.
**Trending because:** 26 HuggingFace upvotes + uses dynamic rubrics for fine-grained credit assignment in long-horizon agents

---

### 13. WorldSculpt: Generating Compositional Worlds from Grounded Videos
**Authors:** Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
**arXiv:** [arxiv.org/abs/2609.05416](https://arxiv.org/abs/2609.05416)
**Summary:** We study the problem of generating a compositional 3D representation of a cluttered scene containing hundreds of objects. The goal is to represent the scene as a collection of individual object meshes placed in a shared world frame, as required by downstream applications such as gaming, AR/VR, simulation, and robotics.
**Trending because:** 21 HuggingFace upvotes + builds object-level compositional 3D worlds from cluttered video

---

### 14. Enoki: Efficient Multi-Level Hallucination Detection
**Authors:** Elisei Rykov, Timur Ionov, Nikolay Ivanov, Maksim Savkin, Maksim Makarenko, Alexander Panchenko, Vasily Konovalov, Julia Belikova
**arXiv:** [arxiv.org/abs/2609.00581](https://arxiv.org/abs/2609.00581)
**Summary:** Ensuring factuality remains a critical challenge for deploying LLMs in high-stakes settings. Existing hallucination detectors usually operate at a single level: claim-level methods provide interpretable factual units, while span-level methods localize unsupported text.
**Trending because:** 19 HuggingFace upvotes + combines interpretable claim-level and localized span-level hallucination detection

---

### 15. Using Grounded Theory for Agent Behavior Analysis at Scale
**Authors:** Zhuoran Lu, Yangyang Yu, Zhuoyan Li, Yibo Meng, Nan Jiang, Chengxi Zang, Jie Gao, Ziang Xiao
**arXiv:** [arxiv.org/abs/2608.30391](https://arxiv.org/abs/2608.30391)
**Summary:** Understanding agent behavior requires methods that scale to thousands of trajectories and surface new patterns in long, often unfamiliar tasks where pre-built classifiers fall short. We propose to bring grounded theory into agent trajectory analysis: a six-decade-old qualitative method from the social sciences, with a principled saturation criterion and an auditable trail from data to theory.
**Trending because:** 19 HuggingFace upvotes + adapts grounded theory to discover and audit behavior patterns across large agent traces

---

### 16. Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference
**Authors:** Mostafa Elhoushi, Alex Pretko, Nolan Dey, Bin Claire Zhang, Gavia Gray, Gurpreet Gosal, Abdulrahman Mahmoud, Shane Bergsma, Joel Hestness
**arXiv:** [arxiv.org/abs/2609.05275](https://arxiv.org/abs/2609.05275)
**Summary:** Layer dropout (a.k.a. stochastic depth) has been shown to enable faster training, higher accuracy, and robustness to zero-shot layer pruning in both language and vision transformers. However, as models and datasets have scaled, dropout - particularly layer dropout - has largely disappeared from large language models (LLMs) pre-training recipes.
**Trending because:** 17 HuggingFace upvotes + revisits layer dropout as a route to cheaper LLM training and inference

---

### 17. Ask Before You Optimize: Dynamic Pre-Formulation Clarification for Interactive Optimization
**Authors:** Sihan Ge, Yichen Lin, Chenyu Zhou, Jianghao Lin, Tao Yao, Dongdong Ge
**arXiv:** [arxiv.org/abs/2609.05258](https://arxiv.org/abs/2609.05258)
**Summary:** Large language models (LLMs) are increasingly used to formulate optimization models from natural-language problem descriptions, yet realistic operations research (OR) requests are often incomplete: missing objectives, constraints, or business rules can change the resulting mathematical program. Existing evaluations largely assume a complete specification and therefore overlook whether an agent knows when clarification is needed before modeling.
**Trending because:** 17 HuggingFace upvotes + tests whether optimization agents know when to ask for missing requirements

---

### 18. ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation
**Authors:** Javier del Pino, Salvador Rodríguez, Alejandro Garabito, Javier Álvarez, Chema Garabito
**arXiv:** [arxiv.org/abs/2609.03756](https://arxiv.org/abs/2609.03756)
**Summary:** We present ENEAS, a unified, text-promptable method for instance tracking and semantic discovery. Text-promptable segmentation models, including the latest foundation models such as SAM 3, still suffer from temporal hallucinations, spatial fragmentation, and semantic misclassification: they fail to report target absence when an object leaves the field of view, segment local textures instead of the complete object during extreme close-ups, and prioritize visual features over ontological reality, so that visually similar artifacts such as statues, paintings, or reflections are segmented as target entities.
**Trending because:** 17 HuggingFace upvotes + addresses temporal and semantic failures in text-prompted segmentation and tracking

---

### 19. Select, Compress, Reinvest: A Controlled Study of Visual-Token Allocation in Long-Video MLLMs
**Authors:** Prakhar Khatri
**arXiv:** [arxiv.org/abs/2609.03820](https://arxiv.org/abs/2609.03820)
**Summary:** Long-video language models cannot look at every frame: an hour sampled once per second is 3,600 images, and a system keeps only a small fixed slice of that pool. Which frames survive that slice is usually treated as a preprocessing detail; we test whether it should be.
**Trending because:** 15 HuggingFace upvotes + isolates visual-token selection as a key bottleneck for long-video multimodal models

---

### 20. QCell: Recombining and Aligning Cell Queries for Overlapping Instance Segmentation
**Authors:** Yaroslav Prytula, Anton Popov, Dmytro Fishman
**arXiv:** [arxiv.org/abs/2608.29253](https://arxiv.org/abs/2608.29253)
**Summary:** Instance segmentation of overlapping cells in microscopy remains challenging due to semi-transparent structures that produce weak boundaries and mixed visual evidence in overlap regions. Existing methods address this through local regions of interest or shape priors but lack global reasoning across overlapping objects.
**Trending because:** 14 HuggingFace upvotes + adds global reasoning for difficult overlapping-cell instance segmentation
