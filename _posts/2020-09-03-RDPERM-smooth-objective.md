---
title: Renyi Differentially Private ERM for Smooth Objectives ntoes
layout: post
date: 2020-09-03 21:58
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- PPML
- DP
- RDP
- Output Perturbation
author: Sun
---

Chen C, Lee J, Kifer D. Renyi differentially private erm for smooth objectives[C]//The 22nd International Conference on Artificial Intelligence and Statistics. 2019: 2037-2046.

为凸ERM问题提出了RDP-SGD。利用了输出扰动和SGD本身对随机性，创造了“随机的敏感度”来减少噪声量的添加。输出扰动的好处之一是，可以合并一个定期求平均的步骤，以进一步降低敏感度，同时提高精度（将SGD的众所周知的振荡行为降低至最佳水平）。RDP提供的$(\epsilon,\delta)$-DP保证，比之前的工作性能更好。

<!--more-->

本文的方案基于SGD和输出扰动，提出了满足RDP的针对convex ERM优化问题的解决方案。

本文的解决方案有以下特征：

1. 利用了mini-batch SGD的一种变体：这一选择和full-batch梯度下降相比，可以加速计算，对足够大的数据集来说，SGD训练模型的迭代次数远比full-batch的小，因此每个数据对最优解的影响很小；
2. 利用了输出扰动：此选择使我们可以对SGD中遇到的中间参数向量进行周期性的平均。在凸的ERM中，这种平均可以帮助加速收敛（直觉上想，减少了震荡）。同时，还可以帮助**用更少的噪声来保护隐私**。此外，当最初对输入数据进行重新排列(permuted)时，SGD更新是收缩映射和扩展映射的随机组合。 这种随机行为使我们可以进一步减少保护隐私所需的噪声。

