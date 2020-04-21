---
title: Differentially Private Meta Learning notes
layout: post
date: 2020-04-19 23:32
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- PPML
- Meta Learning
- DP
author: Sun
---

> Li J, Khodak M, Caldas S, et al. Differentially private meta-learning[J]. arXiv preprint arXiv:1909.05830, 2019.

#### Abstract

参数传递是元学习的一种众所周知的通用方法，其应用包括few-shot学习，联邦学习和强化学习。但是，参数传递算法通常需要共享已对来自特定任务的样本进行过训练的模型，从而使任务所有者容易受到隐私的侵犯。

本文在这种情况下进行了隐私的首次正式研究，并将任务全局差分隐私（task-global dp）的概念形式化为对更常见的威胁模型的实际放宽。然后，我们针对基于梯度的参数传递提出了一种新的差分隐私算法，该算法不仅满足此隐私要求，而且在凸设置中保留了可证明的传递学习保证。从经验上讲，我们将分析应用于具有个性化和few-shot分类的联邦学习问题，这表明允许从较普遍研究的局部隐私（local privacy）概念放宽到任务全局隐私会使rnn类的自然语言处理问题和图像分类问题的性能大幅提升。