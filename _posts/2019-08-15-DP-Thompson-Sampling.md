---
title: On The Differential Privacy of Thompson Sampling With Gaussian Prior notes
layout: post
date: 2019-08-15 14:16
image: /assets/images/
headerImage: false
category: blog
tag:
- DP
- Thompson Sampling
author: Sun
---

这是arxiv上的一个占坑文吧。好像也没有写出后续。

> Tossou A C Y, Dimitrakakis C. On The Differential Privacy of Thompson Sampling With Gaussian Prior[J]. arXiv preprint arXiv:1806.09192, 2018.

主要结论是说基于高斯先验的TS算法 ([1]中的算法2) 已经是满足DP的。

![image-20190815142143457](/assets/images/2019-08-15-DP-Thompson-Sampling/image-20190815142143457.png){:width = 400}

理论1表明T轮迭代后的privacy loss是$O(\ln^2 T)$的。

理论2表明可以通过调整高斯后验的方差来控制privacy loss的level。

> Thompson Sampling is a randomized algorithm that works in a Bayesian framework.



#### Reference

[1] Agrawal, Shipra and Goyal, Navin. Further optimal regret bounds for thompson sampling. In *Artificial Intelligence and Statistics*, pp. 99–107, 2013.