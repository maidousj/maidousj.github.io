---
title: An adaptive and fast convergent approach to DPDL notes
layout: Paper Reading
date: 2019-12-10 10:58
image: /assets/images/
headerImage: false
category: Blog
tag:
- DP
- DL
- Adaptive
- PPML
author: Sun
---

Infocom 2020, Zhiying Xu, Shuyu Shi, etc.

###Abstract
提出一种适应性的快速的保护隐私学习算法，ADADP。该算法通过适应性的学习率提高了收敛速度从而极大的减少了privacy cost，同时通过引入适应性的噪声量，缓和了DP对模型正确率的负面影响。
<!--more-->

###Introduction
对于学习率，根据历史记录以适应性的方式对更新较为频繁的部分分配较大的学习率；
观察到训练数据中不同的维度之间的敏感度是不同的，提出对不同维度加入不同的噪声，从而实现适应性的扰动方式。

和已有的方案相比，优势是：

1. privacy cost会降低，因为适应性的学习率会提高收敛速度；
2. ADADP拥有可证明的隐私保证和与非隐私版本模型相当的准确率，噪声的适应依赖于different gradient components和不同的训练次数；
3. computationally efficient, 因为不需要在每次迭代中解决任何额外的优化问题来决定噪声的分布。作为对比，[1]需要解决大量的非凸优化问题。

###Approach

具体方法就是对学习率和噪声量进行适应性修改。

####Adaptive Learning Rate
对于学习率：采用类似于RMSPROP的适应性策略。

####Adaptive Noise
对于噪声量，文章首先证明对于不同维度上进行不同量的扰动（均值方差不同的高斯噪声），与所有维度都加相同分布的扰动（均值方差都相同，但是量是随机的），这二者可以达到相同的$(\epsilon, \delta)-DP。



###Reference

[1] L. Xiang, J. Yang, and B. Li, “Differentially-private deep learning from an optimization perspective,” in Proceedings of 38th Annual IEEE Conference on Computer Communications (INFOCOM), 2019, pp. 559–567.

