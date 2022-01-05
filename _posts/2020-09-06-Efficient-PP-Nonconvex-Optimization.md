---
title: Efficient Privacy-Preserving Nonconvex Optimization (Skimming)
layout: post
date: 2020-09-06 21:14
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- PPML
- RDP
- Nonconvex Optimization
author: Sun
---

Wang L, Jayaraman B, Evans D, et al. Efficient Privacy-Preserving Nonconvex Optimization[J]. arXiv preprint arXiv:1910.13659, 2019.

为非凸ERM的优化问题提供了隐私保护。提出了一种DPSGD，给出了privacy、gradient complexity和utility的tight analysis。可以达到目前已知最好的utility保证[WANG, D., YE, M. and XU, J. (2017). Differentially private empirical risk minimization revisited: Faster and more general. In *Advances in Neural Information Processing Systems*.]，同时降低gradient complexity。可以用于分布式的设定中。

<!--more-->

#### Main Idea

提出的算法就是对stochastic ecursive variance-reduced gradient descent algorithm[1,2,3]中的梯度进行扰动。

![](/assets/images/2020-09-06-Efficient-PP-Nonconvex-Optimization/image-20200906213819230.png){:width="400"}

其实主要是想学习下用RDP的证明。云里雾里的唉。



pdf test:

 [Conditional gradient method.pdf](/assets/pdf/cgd.pdf) 



#### Reference

[1] NGUYEN, L. M., LIU, J., SCHEINBERG, K. and TAKA ́ Cˇ , M. (2017). Sarah: A novel method for machine learning problems using stochastic recursive gradient. In *34th* *International Conference on Machine Learning*.

[2] FANG, C., LI, C. J., LIN, Z. and ZHANG, T. (2018). Spider: Near-optimal non-convex optimization via stochastic path-integrated differential estimator. In *Advances in Neural Information Processing Systems*.

[3] ZHOU, D., XU, P. and GU, Q. (2018). Stochastic nested variance reduction for nonconvex optimization. In *32nd* *International Conference on Neural Information Processing Systems*.

