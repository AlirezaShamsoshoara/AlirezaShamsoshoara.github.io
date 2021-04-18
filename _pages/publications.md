---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on [my Google Scholar profile](https://scholar.google.com/citations?user=1IDrN5QAAAAJ&hl=en&oi=ao).

Journals
==========
* **Shamsoshoara, A.**, Afghah, F., Razi, A., Zheng, L., Fulé, P.Z. and Blasch, E., 2020. "Aerial Imagery Pile burn detection using Deep Learning: the FLAME dataset." Computer Networks (2021): 108001. [[link](https://www.sciencedirect.com/science/article/pii/S1389128621001201)]
* **Shamsoshoara, A. **, Fatemeh Afghah, Erik Blasch, Jonathan Ashdown, and Mehdi Bennis. "UAV-Assisted Communication in Remote Disaster Areas using Imitation Learning." IEEE Open Journal of the Communications Society (2021). [[link](https://ieeexplore.ieee.org/abstract/document/9381488)]
* **Shamsoshoara, A.**, Afghah, F., Razi, A.,  Mousavi S., Ashdown, J. and Turk, K., 2020. An Autonomous Spectrum Management Scheme for Unmanned Aerial Vehicle Networks in Disaster Relief Operations. IEEE Access, 8, pp.58064-58079. [[link](https://ieeexplore.ieee.org/abstract/document/9046033)]
* **Shamsoshoara, A.**, Korenda, A., Afghah, F. and Zeadally, S., 2020. A survey on physical unclonable function (PUF)-based security solutions for Internet of Things. Computer Networks, p.107593. [[link](https://www.sciencedirect.com/science/article/pii/S1389128620312275)]

Conferences 
==========
* Belen, J., Mousavi, S, **Shamsoshoara, A.**, Afghah., 2020. An Uncertainty Estimation Framework for Risk Assessment in Deep Learning-based Atrial Fibrillation Classification. In IEEE Signal Processing Society, 2020 Asilomar Conference on Signals, Systems, and Computers. IEEE. [[Preprint](https://arxiv.org/pdf/2011.00121.pdf)]
* Keshavarz, M., **Shamsoshoara, A.**, Afghah, F. and Ashdown, J., 2020. A Real-time Framework for Trust Monitoring in a Network of Unmanned Aerial Vehicles. In IEEE INFOCOM 2020-IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS) (pp. 677-682). IEEE. [[link](https://ieeexplore.ieee.org/abstract/document/9162761)]
* Wu, H., Li, H., **Shamsoshoara, A.**, Razi, A. and Afghah, F., 2020, March. Transfer Learning for Wildfire Identification in UAV Imagery. In 2020 54th Annual Conference on Information Sciences and Systems (CISS) (pp. 1-6). IEEE. [[link](https://ieeexplore.ieee.org/abstract/document/9086204)]
* **Shamsoshoara, A.**, Khaledi, M., Afghah, F., Razi, A., Ashdown, J. and Turck, K., 2019, June. A solution for dynamic spectrum management in mission-critical UAV networks. In 2019 16th Annual IEEE International Conference on Sensing, Communication, and Networking (SECON) (pp. 1-6). IEEE. [[link](https://ieeexplore.ieee.org/abstract/document/8824917)]
* **Shamsoshoara, A.**, Khaledi, M., Afghah, F., Razi, A. and Ashdown, J., 2019, January. Distributed cooperative spectrum sharing in uav networks using multi-agent reinforcement learning. In 2019 16th IEEE Annual Consumer Communications & Networking Conference (CCNC) (pp. 1-6). IEEE. [[link](https://ieeexplore.ieee.org/abstract/document/8651796)]
* Afghah, F., **Shamsoshoara, A.**, Njilla, L. and Kamhoua, C., 2018, April. A reputation-based stackelberg game model to enhance secrecy rate in spectrum leasing to selfish iot devices. In IEEE INFOCOM 2018-IEEE Conference on Computer Communications Workshops (INFOCOM WKSHPS) (pp. 312-317). IEEE. [[link](https://ieeexplore.ieee.org/abstract/document/8406970)]
* **Shamsoshoara, A.** and Darmani, Y., 2015, May. Enhanced multi-route ad hoc on-demand distance vector routing. In 2015 23rd Iranian Conference on Electrical Engineering (pp. 578-583). IEEE. [[link](https://ieeexplore.ieee.org/abstract/document/7146282)]

Dataset
==========
* The Flame Dataset: Aerial Imagery Pile Burn Detection Using Drones (UAVs), IEEE Dataport 2020, [[link](https://ieee-dataport.org/open-access/flame-dataset-aerial-imagery-pile-burn-detection-using-drones-uavs)]

Book and Book Chapter 
==========
* (Book Chapter) Afghah, F., **Shamsoshoara, A.**, Njilla, L.L. and Kamhoua, C.A., 2020. Cooperative Spectrum Sharing and Trust Management in IoT Networks. Modeling and Design of Secure Internet of Things, pp.79-109. [[link](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119593386.ch4)]
* (Book) **Shamsoshoara, A.**, Karimi, R., 2016, Overview of Network Simulator NS2, pp.1-859. [[link](https://www.researchgate.net/publication/337670285_Overview_of_Network_Simulator_NS2)]

Reports 
==========
* **Shamsoshoara, A.**, 2019. Overview of Blakley's Secret Sharing Scheme. arXiv preprint arXiv:1901.02802. [[link](https://arxiv.org/pdf/1901.02802.pdf)]
* **Shamsoshoara, A.**, 2019. Ring oscillator and its application as physical unclonable function (puf) for password management. arXiv preprint arXiv:1901.06733. [[link](https://arxiv.org/pdf/1901.06733.pdf)]

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
