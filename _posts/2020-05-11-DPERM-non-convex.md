---
title: Differentially Private Empirical Risk Minimization with Non-convex Loss Functions notes
layout: post
date: 2020-05-11 10:42
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- DPML
- ERM
- DP
- Non-convex
author: Sun
---

Wang D, Chen C, Xu J. Differentially private empirical risk minimization with non-convex loss functions[C]//International Conference on Machine Learning. 2019: 6526-6535.

本文研究了DP-ERM with (smooth) non-convex loss function问题。我们首先研究预期的过量经验（或总体）风险，**该风险主要用作衡量凸损失函数质量的工具**。

> We first study the expected excess empirical (or population) risk, which was primarily used as the utility to measure the quality for convex loss functions.

在$(\epsilon,\delta)$-DP中，上述risk的上界是$\tilde{O}(\frac{d \log(1/\delta)}{\log n\epsilon^2})$，n是数据总数，d是空间的维度。通过对时间平均误差的高度平凡的分析，$\frac{1}{\log n}$项可以进一步提高到$\frac{1}{n^{\Omega(1)}}$（当d维常数的时候）。

为了得到更有效的解决方案，考虑了DP和近似local最小值的联系。特别地，当n足够大时，存在$(\epsilon,\delta)$-DP算法，可以在约束和非约束条件下大概率找到经验风险的近似局部最小值。

<!--more-->

