---
title: Improve-Gaussian-Mechanism
layout: post
date: 2019-08-29 14:29
image: /assets/images/
headerImage: false
category: blog
tag:
- DP
- Gaussian Mechanism
author: Sun
---

提出了两种方法让bound更紧 

> The first improvement is an algorithmic noise calibration strategy that uses numerical evaluations of the Gaussian cumulative density function (CDF) to obtain the optimal variance to achieve DP using Gaussian perturbation. 

用CDF来得到更优的方差 

> The second improvement equips the Gaussian perturbation mechanism with a post-processing step which denoises the output using adaptive estimation techniques from the statistics literature. 

用后处理的步骤，用适应性估计技术对output降噪 

存在的问题： 

1. 经典高斯机制：$Z\sim N(0, \sigma^2)$, For any $\epsilon, \delta \in (0,1), \sigma = \Delta\sqrt{2\log(1.25/\delta)}/\epsilon$, 可以保证$(\epsilon,\delta)$-DP 

   很自然的两个疑问是：

   a. 该$\sigma$取值在满足DP的前提下，是否保证是最小的噪声量 

   b. 当$\epsilon \ge 1$会发生什么。 

   这篇文章指出当$\epsilon \rightarrow 0$ (high privacy regime)，$\sigma$是次优的。 

   large values of ε the standard deviation of a Gaussian perturbation that provides (ε, δ)-DP must scale like Ω(1/√ε). 

2. Limitations of Privacy Loss Analyses 