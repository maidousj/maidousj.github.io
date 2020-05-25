---
title: Differentially Private Empirical Risk Minimization with Sparsity-Inducing Norms (Skimming)
layout: post
date: 2020-05-24 16:20
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- PPML
- DP
- ERM
author: Sun
---

Sesh Kumar K S, Deisenroth M P. Differentially Private Empirical Risk Minimization with Sparsity-Inducing Norms[J]. arXiv preprint arXiv:1905.04873, 2019.



本文考虑DPERM with regularizers thath induce structured sparsity。这些正则项是凸的，但常常不可微。本文分析了标准的DP算法，比如输出扰动(output perturbation)，Frank-Wolfe和目标扰动(objective perturbation)。

输出扰动在强凸的条件下表现较好。之前的工作导出的risk bound不依赖于维度。这篇文章我们假设一类特殊的凸但不平滑的正则项为广义线性模型引入结构化的稀疏性和损失函数。

同样考虑了用DP-FW算法来优化risk minimization问题的对偶。给出了这些算法的risk bounds。**bounds依赖于对偶范数的单位球的高斯宽度**。

还表明了目标扰动和对偶优化问题的输出扰动是等价的。

是第一个考虑DP下ERM的对偶优化问题的工作。



<!--more-->