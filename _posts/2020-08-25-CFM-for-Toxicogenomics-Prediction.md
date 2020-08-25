---
title: Convex Factorization Machine for Toxicogenomics Prediction notes (Skmming)
layout: post
date: 2020-08-25 21:40
image: /assets/images/
headerImage: false
category: Blog
tag:
- FM
- Convex
author: Sun
---

Yamada M, Lian W, Goyal A, et al. Convex factorization machine for toxicogenomics prediction[C]//Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 2017: 1215-1224.

凸FM用在毒理基因组预测上的文章。

提出Convex FM，采用线性+平方的模型。对线性项进行l2正则，平方项进行trace norm正则。然后将CFM优化公式化为半定规划问题，并提出了采用Hazan算法的高效优化程序。CFM相对于现有FM的关键优势在于，它可以找到全局最优解，而FM可能无法获得理想的局部最优解，因为FM的目标函数是非凸的。另外，所提出的算法简单而有效，并且易于实现。

通过合成的和传统上使用的movielens数据集，我们首先表明，提出的CFM获得了与FM竞争的结果。 然后，我们在毒物基因组学预测任务中表明，CFM可以比最先进的张量因子分解方法更好地预测药物集合的毒性结果。