---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---
## 1) FLAME (Fire Luminosity Airborne-based Machine learning Evaluation) Dataset: Aerial Imagery Pile burn detection using Deep Learning
You can find the dataset in [IEEE-Dataport](https://ieee-dataport.org/open-access/flame-dataset-aerial-imagery-pile-burn-detection-using-drones-uavs).<br/>
You can find the preprint of this article in [Preprint](https://arxiv.org/pdf/2012.14036.pdf).

### Code
In this project, we implemented two machine learning approaches on the proposed dataset. First, a problem of 'Fire_vs_No-Fire' image classification is defined. Next, a second problem for the fire segmention is also considered including Ground Truth Mask data. The code for these approaches on the FLAME dataset is written in Python 3.6 using Tensorflow and Keras.
For more information about the **code** please visit the [Github repository](https://github.com/AlirezaShamsoshoara/Fire-Detection-UAV-Aerial-Image-Classification-Segmentation-UnmannedAerialVehicle).

### Abstract:

* A short sample video of the dataset is available on YouTube:

{% include youtubePlayer_Fire.html %}


Wildfires are one of the costliest and deadliest natural disasters in the US, causing damage to millions of hectares of forest resources and threatening the lives of people and animals. Of particular importance are risks to firefighters and operational forces, which highlights the need for leveraging technology to minimize danger to people and property. ***FLAME (Fire Luminosity Airborne-based Machine learning Evaluation)*** offers a dataset of aerial images of fires along with methods for fire detection and segmentation which can help firefighters and researchers to develop optimal fire management strategies. This study provides a fire image dataset collected by drones during a prescribed burning piled detritus in an Arizona pine forest. The dataset includes video recordings and thermal heatmaps captured by infrared cameras. The captured videos and images are annotated, and labeled frame-wise to help researchers easily apply their fire detection and modeling algorithms. This study also highlights solutions to two machine learning problems: (1) Binary classification of video frames based on the presence [and absence] of fire flames. An Artificial Neural Network (ANN) method is developed that achieved a 76% classification accuracy. (2) Fire detection using segmentation methods to precisely determine fire borders. A deep learning method is designed based on the U-Net up-sampling and down-sampling approach to extract a fire mask from the video frames. Our FLAME method approached a precision of 92%, and recall of 84%.

<hr style="border:2px solid gray"> </hr>

## 2) An Autonomous Spectrum Management Scheme for Unmanned Aerial Vehicle Networks in Disaster Relief Operations using Multi Independent Agent Reinforcement Learning
You can find the full text of the related paper to this project in [Article](https://ieeexplore.ieee.org/abstract/document/9046033).
### Code
In this project, we used MARL approach using the Q learning for multi independent Agents (UAVs). Each UAV operates in a seperate region but all of them have the same goal. A centralized approach allocates them and distributes them in their regions then the UAVs autonomously find their best spots for the throughput maximization. For more information about the **code** please visit the [Github repository](https://github.com/AlirezaShamsoshoara/Multi-Independent-Agent-Reinforcement-Learning-UAV-Autonomous-Spectrum-QLearning).

### Abstract:

* The system model of this paper is based on:
![Alt text](/images/system_Hybrid.JPG)
![Alt text](/images/system_Hybrid2.JPG)

This study investigates the problem of spectrum shortage in an unmanned aerial vehicle (UAV) network during critical missions such as wildfire monitoring, search and rescue, and disaster monitoring. Such applications involve a high demand for high-throughput data transmissions such as real-time video-, image-, and voice- streaming where the assigned spectrum to the UAV network may not be adequate to provide the desired Quality of Service (QoS). In these scenarios, the aerial network can borrow an additional spectrum from the available terrestrial networks in trade of a relaying service for them. We propose a spectrum sharing model in which the UAVs are grouped into two classes of relaying UAVs that service the spectrum owner and the sensing UAVs that perform the disaster relief mission using the obtained spectrum. The operation of the UAV network is managed by a hierarchical mechanism in which a central controller assigns the tasks of the UAVs based on their resources and determine their operation region based on the level of priority of impacted areas and then the UAVs autonomously fine-tune their position using a model-free reinforcement learning algorithm to maximize the individual throughput and prolong their lifetime. We analyze the performance and the convergence for the proposed method analytically and with extensive simulations in different scenarios.

<hr style="border:2px solid gray"> </hr>

## 3) A solution for Dynamic Spectrum Management in Mission-Critical UAV Networks using Team Q learning as a Multi-Agent Reinforcement Learning Approach
You can find the full text of the related paper to this project in [Article](https://ieeexplore.ieee.org/abstract/document/8824917).

### Code
In this project, we used team Q learning which is one of the approaches of reinforcement learning (RL) techniques for Multi Agent (RL) problems. The implented solution is available in Python. For more information about the **code** please visit the [Github repository](https://github.com/AlirezaShamsoshoara/Reinforcement_Learning_Team_Q_learnig_MARL_Multi_Agent_UAV_Spectrum_task).

### Abstract:
—In this paper, we study the problem of spectrum scarcity in a network of unmanned aerial vehicles (UAVs) during mission-critical applications such as disaster monitoring and public safety missions, where the preallocated spectrum is not sufficient to offer a high data transmission rate for real-time video-streaming. In such scenarios, the UAV network can lease part of the spectrum of a terrestrial licensed network in exchange for providing relaying service. In order to optimize the performance of the UAV network and prolong its lifetime, some of the UAVs will function as a relay for the primary network while the rest of the UAVs carry out their sensing tasks. Here, we propose a team reinforcement learning algorithm performed by the UAV’s controller unit to determine the optimum allocation of sensing and relaying tasks among the UAVs as well as their relocation strategy at each time. We analyze the convergence of our algorithm and present simulation results to evaluate the system throughput in different scenarios.

* The system model of this paper is based on:
![Alt text](/images/system_solution_teamqlearning.JPG)

