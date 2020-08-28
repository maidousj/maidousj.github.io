---
title: (Near) Dimension Independent Risk Bounds for Differentially Private Learning skimming
layout: post
date: 2020-08-28 17:21
image: /assets/images/
headerImage: false
category: Blog
tag:
- DP
- ERM
- Dimension Independent
author: Sun
---

Jain, P., & Thakurta, A. (2014). (Near) dimension independent risk bounds for differentially private learning. *31st International Conference on Machine Learning, ICML 2014*, *1*, 728–739.

回答了“是否可以高效地计算DPERM，risk bounds不明确地依赖于维度，同时也不需要结构性的假设，比如严格凸“这一问题。本文表明，在一定的假设下，输出扰动和目标扰动算法都可以不明显的依赖于维度，risk依赖于L2-norm of the true risk minimizer and that of training points.

然后，提出了一种新颖的隐私保护算法，用于广义线性模型中的单纯形风险最小化，其中损失函数是一个双微分凸函数。假设训练集的边界为$L_{\infin}$-范数，我们的算法提供的风险边界仅对p有对数依赖性。 还将这一技术应用到在线学习环境中，并获得了对p具有类似对数依赖关系的regret。之前的工作是$O(\sqrt{p})$。

<!--more-->

只要参数被bound在L2-norm内，private模型和non-private模型的“距离”多项式依赖于维度p，risk不依赖于维度。

之前的output和objective扰动，generalized linear models (GLM)中ERM的风险分析多项式依赖于p。本文表明，可以tighten他们的分析，以消除对p的明确依赖，而仅依赖于输入数据和输出参数向量的L2范数。