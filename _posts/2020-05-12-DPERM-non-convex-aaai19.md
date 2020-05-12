---
title: "Differentially private empirical risk minimization with smooth non-convex loss functions: A non-stationary view" notes
layout: post
date: 2020-05-12 09:47
image: /assets/images/
headerImage: false
category: Blog
tag:
- DPML
- ERM
- DP
- Non-convex
author: Sun
---

Wang D, Xu J. Differentially private empirical risk minimization with smooth non-convex loss functions: A non-stationary view[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2019, 33: 1182-1189.

本文研究了DP-ERM在损失函数是非凸情况下的一些utility的上界。首先考虑了**低维空间**的问题，对于DP-ERM with non-smooth regularizer，通过用projected gradient的l2-norm来测量utility的方法，generalize一个现有的工作。同时，使用期望的梯度l2范数首次将误差范围的度量从经验风险(empirical risk)扩展到总体风险(population risk)。

然后研究了**高维空间**的问题，发现通过使用弗兰克-沃尔夫间隙（Frank-Wolfe gap）测量效用(utility)，可以用约束集的高斯宽度（而不是基础空间的维数p）来约束效用。我们进一步证明，通过测量投影梯度的l2范数可以证明此结果的优点。

一个令人惊讶的发现是，尽管两种测量方法有很大不同，但在某些假设下，它们引起的效用上限渐近相同。 我们还表明，某些特殊的非凸损失函数的效用可以降低到类似于凸损失函数的水平（即，仅取决于$\log{p}$）。 最后，在合成数据集和真实数据集上测试了我们提出的算法，实验结果证实了我们的理论分析。

<!--more-->

