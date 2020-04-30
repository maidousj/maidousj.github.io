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

之前提出的基于DP的用来解决凸优化问题的算法都不能部署到实践中。本文提出了Approximate Minima Pertubation，可以针对当前的任何优化器实现隐私保护算法，并且不需要超参数的调整；其次做了一些评估比较，和当前的DP凸优化方法进行了比较；最后给出了开源实现。

<!--more-->

### Introduction

本文的目标是基于目标扰动的方式对实际的(practical)DP凸优化问题进行深入了解，主要的技术贡献是设计了一种新的隐私保护凸优化算法，该算法适用于现实情况，并提供隐私和实用性保证。

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

[16 R. Bassily, A. Smith, and A. Thakurta, “Private empirical risk minimization: Efficient algorithms and tight error bounds,” in Foundations of Computer Science (FOCS), 2014 IEEE 55th Annual Symposium on. IEEE, 2014, pp. 464–473] 提出了另一种private SGD，给出了optimal risk bounds。

[12 X. Wu, F. Li, A. Kumar, K. Chaudhuri, S. Jha, and J. Naughton, “Bolt-on differential privacy for scalable stochastic gradient descent-based analytics,” in Proceedings of the 2017 ACM In- ternational Conference on Management of Data, ser. SIGMOD ’17. New York, NY, USA: ACM, 2017, pp. 1307–1322.] 提出了output扰动的变体，需要使用permutation-based SGD，用这种算法的性质减少了敏感度。

[D. Kifer, A. Smith, and A. Thakurta, “Private convex empirical risk minimization and high-dimensional regression,” Journal of Machine Learning Research, vol. 1, p. 41, 2012.] [A. Smith and A. Thakurta, “Differentially private feature selec- tion via stability arguments, and the robustness of the lasso,” in COLT, 2013.] 针对高维度的稀疏回归，但是这些算法也需要获取到最小值。

Fast context-aware recommendations with factorization machines

Predicting response in mobile advertising with hierarchical importance-aware factorization machine









#### Experiments

实验将回答三个问题：

1. What is the cost (to accuracy) of privacy?

   DP model 得到的结果和non-private的差距有多大？真实环境中cost是否足够低，以保证DP的实用性。

   实验结果表明，数据集足够大的话，损失是可以忽略的。（分别在低维、高维和真实数据中做了测试。**甚至在真实数据中，DP model可以达到比non-private的更好的准确率**）

2. Which algorithm provides the best accuracy in practice?

   所有的算法性能的顺序是否一致，针对不同的数据集是否会有所差别？

   基本上本文提出的AMP都效果更好一些。

3. Can Approximate Minima Perturbation be deployed without hyperparameter tuning?

   是否可以不受超参数的影响？



##### Experiment Setup

分别对比四种方法中的算法：目标扰动、输出扰动、private梯度下降和private Frank-Wolfe算法。

对于目标扰动，实现了AMP算法，分别对比评估通过grid search调整超参的方案和不受超参影响的AMP变体；

对于输出扰动，实现了Private Permutation-based SGD(PSGD，文章里似乎写错了，写的Perturbation-based)算法[12]，对比了凸和强凸两种变体，都是mini-batch形式的。对凸的，评估了三种不同的学习率(常数、下降的、平方根的)，本文实验表明常数学习率是效果最好的；

对于private梯度下降，实现了private SGD[16]的变体，利用了[15]提出的Moments Accountant，加入了batch处理，并根据所需的迭代次数（与[16]中的固定$n^2$次迭代相比）设置了噪声参数。

对于private Frank-Wolfe，实现了[17 K. Talwar, A. Thakurta, and L. Zhang, “Private empirical risk minimization beyond the worst case: The effect of the constraint set geometry,” CoRR, vol. abs/1411.5417, 2014.]中的算法，根据[26 M. Jaggi, “Revisiting frank-wolfe: projection-free sparse convex optimization,” in Proceedings of the 30th International Confer- ence on International Conference on Machine Learning-Volume 28. JMLR. org, 2013, pp. I–427]的建议，采用减小的学习率来取得更好的准确率。和其他算法不同，这种算法拥有几乎和维度无关的error bounds，因此应该在高维数据中有更好的效果。

##### Datasets

低维数据表示数据个数远大于数据维度，高维数据则表示数据个数小于等于数据维度。随机shuffle数据，训练集和测试集8比2.

##### Sample clipping

评估的每种算法的损失函数都需要有一个**Lipschitz常数**。可以通过对每个样本进行bound the norm操作来实现这个需求。

对于除了private Frank-Wolfe之外的算法，为了使损失函数有**$L_2$-Lipschitz常数L**，可以把样本$(x_i,y_i)$的特征向量$x_i$ 裁剪为$(x_i\cdot \min(1,\frac{L}{\Vert x_i\Vert}))$。

而对private Frank-Wolfe算法，需要损失函数有**a relaxed $L_1$-Lipschitz常数L**，可以通过bound $L_{\infin}$-norm of each sample $(x_i,y_i)$ by L来实现[41 定理1]。具体地，通过clip每个维度$x_{i,j}$为$\min(x_{i,j}, L)$，其中$j\in [d]$。

##### Hyperparameters

为了保证端到端的DP，对超参的调整也应该保证private的方式进行。







[15 M. Abadi, A. Chu, I. Goodfellow, H. B. McMahan, I. Mironov, K. Talwar, and L. Zhang, “Deep learning with differential pri- vacy,” in Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security, ser. CCS ’16. New York, NY, USA: ACM, 2016, pp. 308–318.]

[41 R. Paulaviˇcius and J. Zilinskas,ˇ “Analysis of different norms and corresponding lipschitz constants for global optimization,” Ukio Technologinis ir Ekonominis Vystymas, vol. 12, no. 4, pp. 301– 306, 2006.]



