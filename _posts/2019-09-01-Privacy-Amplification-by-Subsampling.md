---
title: Privacy Amplification by Subsampling: Tight Analyses via Couplings and Divergences notes
layout: post
date: 2019-09-01 14:03
image: /assets/images/
headerImage: false
category: blog
tag:
- DP
- Privacy Amplification
author: Sun
---

Balle B, Barthe G, Gaboardi M. Privacy amplification by subsampling: Tight analyses via couplings and divergences[C]//Advances in Neural Information Processing Systems. 2018: 6277-6287.

#### Introduction

提出了一种通用的框架，适用于任何subsampling策略的方案，提供tight privacy amplification results。基于$\alpha$-divergences[1]来推导bound，之前都是用在program verification上的，这是第一次用在算法分析的场景里。为此提出了两种分析工具，*advanced joint convexity*---关于混合分布的$\alpha$-divergences属性，和*privacy profile*---描述算法可以提供的privacy guarantees。

#### Background

![](/assets/images/2019-09-01-privacy-amplification/image-20190902103116396.png)

用$\alpha$-divergence把DP转换了一下。

*privacy profile*表示所有隐私参数的集合，这些参数都可以保证DP。定义了一条在$[0, \infty) \times[0,1]$上划分隐私参数空间的曲线，这条曲线把隐私参数分成了满足DP和不满足DP的两个区域。定义为

$$\delta_M(\varepsilon)=\sup _{x \simeq X^{ x^{\prime}}} D_{e^{\varepsilon}}\left(\mathcal{M}(x) \| \mathcal{M}\left(x^{\prime}\right)\right)$$.

*group-privacy profiles*定义为

$$\delta_{\mathcal{M}, k}(\varepsilon)=\sup _{d\left(x, x^{\prime}\right) \leq k} D_{e^{\varepsilon}}\left(\mathcal{M}(x) \| \mathcal{M}\left(x^{\prime}\right)\right).$$





#### Reference

[1] Gilles Barthe and Federico Olmedo. Beyond differential privacy: Composition theorems and relational logic for f-divergences between probabilistic programs. In International Colloquium on Automata, Languages, and Programming, pages 49–60. Springer, 2013.