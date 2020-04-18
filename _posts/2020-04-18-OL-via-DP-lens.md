---
title: Online Learning via the Differential Privacy Lens notes
layout: post
date: 2020-04-18 11:27
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- PPML
- Online Learning
- DP
author: Sun
---

> Abernethy J D, Jung Y H, Lee C, et al. Online Learning via the Differential Privacy Lens[C]//Advances in Neural Information Processing Systems. 2019: 8892-8902.

#### Abstract

DP框架"less about privacy and more about algorithmic stability"。本文提出一种one-step differential stability，便于对在线学习进行更精细的regret分析。这种稳定性的提法对于follow-the-perturbed-leader算法的一阶regret bounds十分适用，这也是以前工作留下的问题。同时，本文提出了一种标准的max-divergence来得到更为宽广的一类*Tsallis max-divergences*。

