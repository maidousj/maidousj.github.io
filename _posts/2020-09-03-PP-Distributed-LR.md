---
title: Privacy-Preserving Distributed Linear Regression on High-Dimensional Data (Skimming)
layout: post
date: 2020-09-03 09:43
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- PPML
- Garbled Circuits
- High-Dimensional Data
author: Sun
---

Gascón A, Schoppmann P, Balle B, et al. Privacy-preserving distributed linear regression on high-dimensional data[J]. Proceedings on Privacy Enhancing Technologies, 2017, 2017(4): 345-364.

为分布式的线性模型设计了隐私保护的协议。提出了一种混合的多方计算协议，该协议将Yao的乱码电路与tailored protocols相结合，用于计算内积。对比了包括共轭梯度算法在内的不同的安全计算技术。本文提出的算法适用于安全计算，因为它为实数提供了有效的定点表示，同时保持了与使用浮点数的经典解决方案所能获得的精度和收敛速率。本文的方法改进了privacy-preserving ridge regression (S&P 2013)。实现了一个完整的系统，并证明了本文的方法具有高度的可扩展性，可以在不到一小时的总运行时间内解决具有一百万条记录和一百个特征的数据分析问题。

<!--more-->

相关度不高，有需要再细看。



