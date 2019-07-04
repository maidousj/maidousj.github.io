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

由于隐私问题和有限的带宽，移动端的数据最好可以以本地的方式来训练模型。



#### Reference

[1] H.Brendan McMahan,Eider Moore,Daniel Ramage,and Blaise Agüeray Arcas. 2016. Federated Learning of Deep Networks using Model Averaging. CoRR abs/1602.05629 (2016). arXiv:1602.05629 