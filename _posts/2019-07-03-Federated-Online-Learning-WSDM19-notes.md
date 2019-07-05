---
title: Federated Online Learning to Rank with Evolution Strategies notes
layout: post
date: 2019-07-03 10:33
image: /assets/images/
headerImage: false
category: blog
tag:
- Online Learning
- Federated Learning
- Privacy Preserving
- DP
- Local DP
author: Sun
---

Kharitonov E. Federated Online Learning to Rank with Evolution Strategies[C]//Proceedings of the Twelfth ACM International Conference on Web Search and Data Mining. ACM, 2019: 249-257.

WSDM, CCF B类会议, 数据库方向。

#### Abstract

> In this work, we consider Federated Online Learning to Rank setup (FOLtR) where on-mobile ranking models are trained in a way that respects the users’ privacy. *We require that non-privatized user data, such as queries, results, and their feature representations are never communicated for the purpose of the ranker’s training.* We believe this setup is interesting, as it combines unique requirements for the learning algorithm: (a) preserving the user privacy, (b) low communication and computation costs, (c) learning from noisy bandit feedback, and (d) learning with non-continuous ranking quality measures.

考虑联邦在线学习进行排名，其中移动排名模型以尊重用户隐私的方式进行培训。（斜体这句为什么说需要非隐私数据never用来做排名的训练？）

提出了满足上述需求的算法FOLtR-ES。其中一部分是privatization procedure，允许它提供$\epsilon$-local DP，即保护客户免受可以访问通信消息的对手的攻击。此过程可应用于任何绝对在线度量，该度量采用有限多个值或可离散化为有限域。

实验是基于点击模拟的方法和公开的数据集MQ2007和MQ2008。和离线的训练进行了对比如线性回归模型和RankingSVM。实验结果表明，FOLtR-ES可以优化排序模型，在optimized online metric, Max Reciprocal Rank方面和baseline性能相似。



#### Introduction

由于隐私问题和有限的带宽，移动端的数据最好可以以本地的方式来训练模型。联邦学习(Federated Learning)就适合于这种场景，是一种客户端仅发送足以执行协调优化(的内容)的学习方式[1]。

本文将在线学习的排序问题扩展到了联邦学习的设定，叫做Federated Online Learning to Rank (FOLtR)。具体场景是当移动应用有一个机器学习的排序模型时，我们需要通过用户交互的反馈来训练这个模型，同时又需要non-privatized user data (queries, documents seen and clicked, and feature representations. 小疑问，这不应该是private data嘛。。) 不离开用户的设备。

> An example could be a Wikipedia application with its index stored on-device. Whenever the user submits their query to the application, the retrieval and ranking is done locally. Periodically, the application communicates a statistic to the central server and downloads an updated model when it is available.

作者提出的一些挑战：处理有噪声的反馈、非连续特性的测量、探索潜在ranker的空间[2]。还需要保证低的通信开销和隐私。

本文提出了FOLtR-ES算法，其核心是一个0阶优化方法，Evolution Strategies (ES) [3,4]。引入了极小的不依赖于the size of ranker's model的通信开销并且可以optimize non-continuous quality measures。此外，还为the ranking quality metrics that can take
finitely many values提供了$\epsilon$-local DP的保证。

> The code for the experiments in this paper is available at https://github.com/facebookresearch/foltr-es.

#### Background

##### Online learning to rank

在线学习排序的最初的方法是根据点击的反馈推断document的偏好，利用RankingSVM [5]。接下来的工作集中于假设文档的结构来优化排名列表[6,7]，或者是a fixed stochastic model of the user interaction with a result page [8,9,10]。

由于绝对点击反馈受到查询间和用户间差异的影响，因此提出了成对交错评估方法[5,11]。Yue和Joachims [12]提出了一种从成对反馈进行在线学习的算法Dueling Bandit Gradient Descent (DBGD) 。该算法成为多个应用程序和扩展的基础。

现有的online learning to rank都是集中式学习的，ranker的训练方法需要知道用户的查询和点击。本文提出的学习算法没有关于用户与结果列表交互方式和优化质量度量的假设，因此它无缝地解决了结果的相互依赖性，多样性要求，位置偏差等。

最近的集中式在线学习排序算法，主要考虑learn with interleaving/multileaving feedback，比如Multileave Gradient Descent [13]



#### Reference

[1] H.Brendan McMahan,Eider Moore,Daniel Ramage,and Blaise Agüeray Arcas. 2016. Federated Learning of Deep Networks using Model Averaging. CoRR abs/1602.05629 (2016). arXiv:1602.05629 

[2] Katja Hofmann, Shimon Whiteson, and Maarten de Rijke. 2013. Balancing exploration and exploitation in listwise and pairwise online learning to rank for information retrieval. Information Retrieval 16, 1 (2013), 63–90. 

[3] I. Rechenberg and M. Eigen. 1973. Evolutionsstrategie: Optimierung technischer Systeme nach Prinzipien der biologischen Evolution. Frommann-Holzboog Stuttgart (1973). 

[4] Tim Salimans, Jonathan Ho, Xi Chen, Szymon Sidor, and Ilya Sutskever. 2017. Evolution strategies as a scalable alternative to reinforcement learning. arXiv:1703.03864 (2017). 

[5] Thorsten Joachims. 2002. Optimizing search engines using clickthrough data. In SIGKDD. 

[6] Filip Radlinski, Robert Kleinberg, and Thorsten Joachims. 2008. Learning diverse rankings with multi-armed bandits. In ICML. 

[7] Aleksandrs Slivkins, Filip Radlinski, and Sreenivas Gollapudi. 2013. Ranked bandits in metric spaces: learning diverse rankings over large document collections. JMLR 14 (2013). 

[8] Branislav Kveton, Csaba Szepesvari, Zheng Wen, and Azin Ashkan. 2015. Cascading bandits: Learning to rank in the cascade model. In ICML. 

[9] Tor Lattimore, Branislav Kveton, Shuai Li, and Csaba Szepesvari. 2018. TopRank: A practical algorithm for online stochastic ranking. arXiv:1806.02248 (2018). 

[10] Masrour Zoghi, Tomas Tunys, Mohammad Ghavamzadeh, Branislav Kveton, Csaba Szepesvari, and Zheng Wen. 2017. Online learning to rank in stochastic click models. arXiv:1703.02527 (2017). 

[11] OlivierChapelle,ThorstenJoachims,FilipRadlinski,andYisongYue.2012.Large-scale validation and analysis of interleaved search evaluation. TOIS (2012). 

[12] Yisong Yue and Thorsten Joachims. 2009. Interactively optimizing information retrieval systems as a dueling bandits problem. In ICML. 

[13] AnneSchuth,HarrieOosterhuis,ShimonWhiteson,andMaartendeRijke.2016. Multileave gradient descent for fast online learning to rank. In WSDM. 