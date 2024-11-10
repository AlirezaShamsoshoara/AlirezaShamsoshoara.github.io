---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

## 1) SwapTransformer: Highway overtaking tactical planner model via imitation learning on OSHA dataset
Paper: [IEEE-Access](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10540008)<br/>
Dataset: [IEEE-Dataport](https://ieee-dataport.org/documents/osha-dataset-overtaking-simulated-highways).<br/>
Preprint: [Arxiv](https://arxiv.org/pdf/2012.14036.pdf)<br/>
Demo: [YouTube](https://www.youtube.com/watch?v=gNKsLh06eAg)<br/>
Code: [GitHub](https://github.com/VWIECCResearch/Swaptransformer)

### Abstract:

* A short video of the simulation and planner is available on YouTube:

{% include youtubePlayer_swaptransformer.html %}

This paper investigates the high-level decision-making problem in highway scenarios regarding lane changing and over-taking other slower vehicles. In particular, this paper aims to improve the Travel Assist feature for automatic overtaking and lane changes on highways. About 9 million samples including lane images and other dynamic objects are collected in simulation. This data; Overtaking on Simulated HighwAys (OSHA) dataset is released to tackle this challenge. To solve this problem, an architecture called SwapTransformer is designed and implemented as an imitation learning approach on the OSHA dataset. Moreover, auxiliary tasks such as future points and car distance network predictions are proposed to aid the model in better understanding the surrounding environment. The performance of the proposed solution is compared with a multi-layer perceptron (MLP) and multi-head self-attention networks as baselines in a simulation environment. We also demonstrate the performance of the model with and without auxiliary tasks. All models are evaluated based on different metrics such as time to finish each lap, number of overtakes,
and speed difference with speed limit. The evaluation shows that the SwapTransformer model outperforms other models in different traffic densities in the inference phase.

<hr style="border:2px solid gray">


## 2) FLAME (Fire Luminosity Airborne-based Machine learning Evaluation) Dataset: Aerial Imagery Pile burn detection using Deep Learning
Dataset: [IEEE-Dataport](https://ieee-dataport.org/open-access/flame-dataset-aerial-imagery-pile-burn-detection-using-drones-uavs).<br/>
Preprint: [Arxiv](https://arxiv.org/pdf/2012.14036.pdf).

### Implementation
In this project, we implemented two machine-learning approaches on the proposed dataset. First, a problem of 'Fire_vs_No-Fire' image classification is defined. Next, a second problem for the fire segmention is also considered including Ground Truth Mask data. The code for these approaches on the FLAME dataset is written in Python 3.6 using Tensorflow and Keras.
For more information about the **code** please visit the [Github repository](https://github.com/AlirezaShamsoshoara/Fire-Detection-UAV-Aerial-Image-Classification-Segmentation-UnmannedAerialVehicle).

### Abstract:

* A short sample video of the dataset is available on YouTube:

{% include youtubePlayer_Fire.html %}


Wildfires are one of the costliest and deadliest natural disasters in the US, causing damage to millions of hectares of forest resources and threatening the lives of people and animals. Of particular importance are risks to firefighters and operational forces, which highlights the need for leveraging technology to minimize danger to people and property. ***FLAME (Fire Luminosity Airborne-based Machine Learning Evaluation)*** offers a dataset of aerial images of fires along with methods for fire detection and segmentation which can help firefighters and researchers to develop optimal fire management strategies. This study provides a fire image dataset collected by drones during a prescribed burning of piled detritus in an Arizona pine forest. The dataset includes video recordings and thermal heatmaps captured by infrared cameras. The captured videos and images are annotated, and labeled frame-wise to help researchers easily apply their fire detection and modeling algorithms. This study also highlights solutions to two machine learning problems: (1) Binary classification of video frames based on the presence [and absence] of fire flames. An Artificial Neural Network (ANN) method was developed that achieved a 76% classification accuracy. (2) Fire detection using segmentation methods to precisely determine fire borders. A deep learning method is designed based on the U-Net up-sampling and down-sampling approach to extract a fire mask from the video frames. Our FLAME method approached a precision of 92%, and recall of 84%.

<hr style="border:2px solid gray">



## 3) UAV-Assisted Communication in Remote Disaster Areas Using Imitation Learning
Article: [IEEE](https://ieeexplore.ieee.org/abstract/document/9381488).<br/>
GitHub: [Repository](https://github.com/AlirezaShamsoshoara/Imitation-Learning-Behavioral-Cloning-UAV-Assisted-Communication).

### Implementation
The implementation is based on Imitation Learning (IL) via Behavioral cloning using a deep learning approach for UAV-Assisted Communication in Remote Disaster Areas. 
For more information about the **code** please visit the [Github repository](https://github.com/AlirezaShamsoshoara/Imitation-Learning-Behavioral-Cloning-UAV-Assisted-Communication).

### Abstract:

* A short sample video of the simulator and the process of imitation learning using Behavioral Cloning (BC) is available on YouTube:

{% include youtubePlayer_imitation_BC.html %}


The damage to cellular towers during natural and man-made disasters can disturb the communication services for cellular users. One solution to the problem is using unmanned aerial vehicles to augment the desired communication network. The paper demonstrates the design of a UAV-Assisted Imitation Learning (UnVAIL) communication system that relays cellular users’ information to a neighbor base station. Since the user equipment (UEs) are equipped with buffers with limited capacity to hold packets, UnVAIL alternates between different UEs to reduce the chance of buffer overflow, positions itself optimally close to the selected UE to reduce service time and uncovers a network pathway by acting as a relay node. UnVAIL utilizes Imitation Learning (IL) as a data-driven behavioral cloning approach to accomplish an optimal scheduling solution. Results demonstrate that UnVAIL performs similarly to a human expert knowledge-based planning in communication timeliness, position accuracy, and energy consumption with an accuracy of 97.52% when evaluated on a developed simulator to train the UAV.

<hr style="border:2px solid gray">

## 4) An Autonomous Spectrum Management Scheme for Unmanned Aerial Vehicle Networks in Disaster Relief Operations using Multi Independent Agent Reinforcement Learning
Article: [IEEE](https://ieeexplore.ieee.org/abstract/document/9046033).

### Implementation
In this project, we used the MARL approach using the Q learning for multi-independent Agents (UAVs). Each UAV operates in a separate region but all of them have the same goal. A centralized approach allocates them and distributes them in their regions then the UAVs autonomously find their best spots for throughput maximization. For more information about the **code** please visit the [Github repository](https://github.com/AlirezaShamsoshoara/Multi-Independent-Agent-Reinforcement-Learning-UAV-Autonomous-Spectrum-QLearning).

### Abstract:

* The system model of this paper is based on:
![Alt text](/images/system_Hybrid.JPG)
![Alt text](/images/system_Hybrid2.JPG)

This study investigates the problem of spectrum shortage in an unmanned aerial vehicle (UAV) network during critical missions such as wildfire monitoring, search and rescue, and disaster monitoring. Such applications involve a high demand for high-throughput data transmissions such as real-time video-, image-, and voice- streaming where the assigned spectrum to the UAV network may not be adequate to provide the desired Quality of Service (QoS). In these scenarios, the aerial network can borrow an additional spectrum from the available terrestrial networks in the trade of a relaying service for them. We propose a spectrum-sharing model in which the UAVs are grouped into two classes relaying UAVs that service the spectrum owner and the sensing UAVs that perform the disaster relief mission using the obtained spectrum. The operation of the UAV network is managed by a hierarchical mechanism in which a central controller assigns the tasks of the UAVs based on their resources and determines their operation region based on the level of priority of impacted areas and then the UAVs autonomously fine-tune their position using a model-free reinforcement learning algorithm to maximize the individual throughput and prolong their lifetime. We analyze the performance and the convergence for the proposed method analytically and with extensive simulations in different scenarios.

<hr style="border:2px solid gray">

## 5) A solution for Dynamic Spectrum Management in Mission-Critical UAV Networks using Team Q learning as a Multi-Agent Reinforcement Learning Approach
Article: [IEEE](https://ieeexplore.ieee.org/abstract/document/8824917).

### Implementation
In this project, we used team Q learning which is one of the approaches of reinforcement learning (RL) techniques for Multi-Agent (RL) problems. The implemented solution is available in Python. For more information about the **code** please visit the [Github repository](https://github.com/AlirezaShamsoshoara/Reinforcement_Learning_Team_Q_learnig_MARL_Multi_Agent_UAV_Spectrum_task).

### Abstract:
—In this paper, we study the problem of spectrum scarcity in a network of unmanned aerial vehicles (UAVs) during mission-critical applications such as disaster monitoring and public safety missions, where the preallocated spectrum is not sufficient to offer a high data transmission rate for real-time video streaming. In such scenarios, the UAV network can lease part of the spectrum of a terrestrial licensed network in exchange for providing relaying service. In order to optimize the performance of the UAV network and prolong its lifetime, some of the UAVs will function as a relay for the primary network while the rest of the UAVs carry out their sensing tasks. Here, we propose a team reinforcement learning algorithm performed by the UAV’s controller unit to determine the optimum allocation of sensing and relaying tasks among the UAVs as well as their relocation strategy at each time. We analyze the convergence of our algorithm and present simulation results to evaluate the system throughput in different scenarios.

* The system model of this paper is based on:
![Alt text](/images/system_solution_teamqlearning.JPG)

