---
title: Towards Practical Differentially Private Convex Optimization notes
layout: post
date: 2020-01-06 12:41
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- DP
- Convex Optimization
- Practical
author: Sun
---

IEEE Symposium on Security and Privacy 2019

### Abstract

之前提出的基于DP的用来解决凸优化问题的算法都不能部署到实践中。本文提出了Approximate Minima Pertubation，可以针对当前的任何优化器实现隐私保护算法；其次做了一些评估比较，和当前的DP凸优化方法进行了比较；最后给出了开源实现。

<!--more-->

### Introduction

Objective Perturbation针对目标函数进行扰动，然后计算新的最小值。然而，这种方法**只有在可以求得perturbed objective的精确最小值的条件下才能保证隐私**。实践中，解决凸优化经常引入一阶迭代方法，比如SGD。但是，SGD的收敛情况经常依赖于迭代次数，不能保证在有限次数内达到最小值。

因此，本文的目标是解决这样一个问题：**在同时保证隐私和可用性的情况下，是否可以释放一个noisy "approximate" minima of the  perturbed objective**。

本文提出了Approximate Minima Perturbation(AMP)，噪声量包含一个代表最大梯度范数容忍度的参数(maximum tolerable gradient norm)。这提供了一个梯度范数bound（也就是加入approximate minima的噪声量）和difficulty(根据norm bound来获取approximate minima的难度)之间的trade-off。如果norm bound设置为0，这个方法就会退化成标准的objective perturbation。AMP具有如下优势：

* 适用于所有的凸目标函数，之前的目标扰动只适用于目标函数是线性模型；两者都需要一些标准属性如Lipschitz continuity和smoothness。
* 第一个可行的可以利用任何现成的optimizer的满足DP的方法。
* 有competitive hyperparameter-free变体。

### Related Work

DP convex ERM:

[K. Chaudhuri, C. Monteleoni, and A. D. Sarwate, “Differentially private empirical risk minimization,” JMLR, 2011.] 提出了output和objective扰动；

[P. Jain and A. Thakurta, “(near) dimension independent risk bounds for differentially private learning,” in Proceedings of the 31st International Conference on International Conference on Machine Learning - Volume 32, ser. ICML’14. JMLR.org, 2014, pp. I–476–I–484.] 提出了几乎是维度独立的安全学习算法，但是只适用于标准setting。

[S. Song, K. Chaudhuri, and A. D. Sarwate, “Stochastic gradient descent with differentially private updates,” in Global Conference on Signal and Information Processing (GlobalSIP), 2013 IEEE. IEEE, 2013, pp. 245–248.]第一次提出了private SGD。

[R. Bassily, A. Smith, and A. Thakurta, “Private empirical risk minimization: Efficient algorithms and tight error bounds,” in Foundations of Computer Science (FOCS), 2014 IEEE 55th Annual Symposium on. IEEE, 2014, pp. 464–473] 提出了另一种private SGD，给出了optimal risk bounds。

[X. Wu, F. Li, A. Kumar, K. Chaudhuri, S. Jha, and J. Naughton, “Bolt-on differential privacy for scalable stochastic gradient descent-based analytics,” in Proceedings of the 2017 ACM In- ternational Conference on Management of Data, ser. SIGMOD ’17. New York, NY, USA: ACM, 2017, pp. 1307–1322.] 提出了output扰动的变体，需要使用permutation-based SGD，用这种算法的性质减少了敏感度。

[D. Kifer, A. Smith, and A. Thakurta, “Private convex empirical risk minimization and high-dimensional regression,” Journal of Machine Learning Research, vol. 1, p. 41, 2012.] [A. Smith and A. Thakurta, “Differentially private feature selec- tion via stability arguments, and the robustness of the lasso,” in COLT, 2013.] 针对高维度的稀疏回归，但是这些算法也需要获取到最小值。

Fast context-aware recommendations with factorization machines

Predicting response in mobile advertising with hierarchical importance-aware factorization machine

















