---
title: Nearly-Optimal-Private-LASSO (Skimming)
layout: post
date: 2020-05-23 11:09
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- PPML
- DP
- LASSO
author: Sun
---

Talwar K, Thakurta A G, Zhang L. Nearly optimal private lasso[C]//Advances in Neural Information Processing Systems. 2015: 3025-3033.

提出DP-LASSO。可以保护每个训练样本。假设训练样本是$l_{\infin}$范数的，与non-private版本的算法相比，本文提出算法的excess risk可以达到$\tilde{O}(\frac{1}{n^{2/3}})$。在不对design matrix做任何假设的情况下，首次得到不多项式依赖于p的boud。同时表明，在所有DP算法中，该误差范围几乎是最佳的。

<!--more-->

首个针对LASSO进行隐私保护的工作。算法结合了经典的Frank-Wolfe算法和指数机制。