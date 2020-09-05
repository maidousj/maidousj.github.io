---
title: Differentially Private Iterative Gradient Hard Thresholding for Sparse Learning (Skimming)
layout: post
date: 2020-09-05 09:49
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- PPML
- DP
- Sparse Learning
author: Sun
---

Wang L, Gu Q. Differentially Private Iterative Gradient Hard Thresholding for Sparse Learning[C]//IJCAI. 2019: 3740-3747.

考虑保护隐私的sparse learning。提出了DP iterative gradient hard thresholding算法，拥有线性收敛率和很强的utility保证。对于稀疏线性回归，本文提出的算法无需先前工作中使用的任何额外支持，即可获得最好的utlity保证[Kifer 2012]。 对于稀疏的逻辑回归，本文的算法可以获得对问题维度的对数依赖的utlity保证。 在合成数据和现实世界数据集上的实验证明了本文提出的算法的有效性。

<!--more-->

用zCDP做了分析。方案是基于梯度扰动的。

![](/assets/images/2020-09-05-DP-iterative-gradient-sparse-learning/image-20200905151241715.png){:width="400"}

从算法看起来和对梯度进行扰动一样。不同之处在于这个hard thresholding：

![](/assets/images/2020-09-05-DP-iterative-gradient-sparse-learning/image-20200905152037875.png){:width="400"}

DP-IGHT算法是线性收敛率的，因此比现有的工作更有效。



本想看下关于满足RDP的证明，可惜没有找到。



