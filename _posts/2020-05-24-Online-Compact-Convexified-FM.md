---
title: Online Compact Convexified Factorization Machine notes
layout: post
date: 2020-05-24 17:37
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- FM
- Online Learning
- Online Convex Optimization
author: Sun
---

Lin X, Zhang W, Zhang M, et al. Online compact convexified factorization machine[C]//Proceedings of the 2018 World Wide Web Conference. 2018: 1633-1642.



Factorization Machine不能直接用于online learning的场景。最初的挑战是，没有任何先前的FM公式可以直接满足在线凸优化（OCO）的要求（OCO是在线学习算法设计的最重要框架）。为此，本文提出了一种新的凸化方案，该方案导致了紧凑型凸面FM（Compact Convexified FM），可以无缝满足OCO的要求。

**但是在在线学习的场景下，绝大部分现有的算法需要承受昂贵的映射操作**。因此，本文遵循在线条件梯度（Online Conditional Gradient）的通用的免投影算法框架，并提出了一种在线紧凑型凸因子分解机（OCCFM）算法，该算法通过有效的线性优化步骤来避免投影操作。

同时，给出了OCCFM的理论bound，可以达到次线性。

在6个真实数据集上进行了在线分类和在线回归的实验对比，结果比online FM强。

<!--more-->



#### Introduction

FM在工业界和比赛界都有很广泛的应用。不幸的是，现存的公式不能直接满足OCO的两个基本要求：（i）所有参数的任何实例都应表示为凸紧致决策集中的单个点； （ii）预测产生的损失应公式化为决策集上的凸函数。事实上，**FM的损失函数相对于因式特征交互矩阵而言是非凸的**，从而违反了要求（ii）。有的工作虽然提出了凸FM的公式，纠正了非凸问题，但是它们仍然把特征的权重向量和特征交互矩阵作为分开的参数，破坏了要求(i)。

为此，提出了新的凸化方案。具体来说，将全局偏差，特征权向量和特征交互矩阵重写为紧凑的扩充对称矩阵，并用核范数约束约束扩充矩阵，这是低秩约束的凸替代。因此，扩充后的矩阵形成了一个凸紧凑决策集，该决策集**实质上是一个对称的有界核范数球**。 然后我们将FM的预测重写为相对于增广矩阵的凸线性函数，因此预测引起的损失是凸的。 基于凸化方案，紧凑的FM（CCFM）的最终配方可以无缝地满足OCO框架的上述要求。

此外，之前的online learning算法中，大部分需要在每次迭代中引入一个映射步骤。当决策集合是有界核范数球的时候，映射相当于计算上昂贵的奇异值分解（SVD），因此限制了大多数在线学习算法的适用性。 值得注意的是，一种特殊的算法是在线条件梯度（OCG），该算法通过线性优化步骤来避免投影操作。 将OCG应用于核范数球时，线性优化相当于计算矩阵的最大奇异向量，这要简单得多。 但是，从理论上来说，对于有界核标准球的特定子集，是否仍存在类似于OCG的算法，这一点在理论上仍然未知。 

对此，本文为CCFM提出了一种在线学习算法，证明了，当决策集是对称核范数球时，仍然存在类似OCG的算法所需的线性优化，即相当于**计算了特定对称矩阵的最大奇异向量**。 基于此发现，提出了一种类似于OCG的OCCFM在线学习算法。 由于OCCFM是OCG的变体，因此我们证明了OCG的理论分析仍然适合OCCFM，从而实现了以$O(T^{3/4})$的顺序的次线性regret bound。然后做了大量实验。



#### Preliminaries

有两个工作把非凸的FM搞成凸的。

[3 Mathieu Blondel, Akinori Fujino, and Naonori Ueda. 2015. Convex factorization machines. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Springer, 19–35.]

[33 Makoto Yamada,Wenzhao Lian, Amit Goyal, Jianhui Chen, Kishan Wimalawarne, Suleiman A. Khan, Samuel Kaski, Hiroshi Mamitsuka, and Yi Chang. 2017. Convex Factorization Machine for Toxicogenomics Prediction. In Proceedings ofthe 23rd ACMSIGKDD International Conference on Knowledge Discovery and Data Mining (KDD ’17). ACM, New York, NY, USA, 1215–1224.]

它们就是把特征交互的矩阵直接建模为$Z\in\mathbb{R}^{d\times d}$，而不是$VV^T$，后者带来了非凸性（这俩有什么区别？）。然后将矩阵Z施加到有界核规范约束上，以保持低秩属性。 通常，凸的FM允许对特征交互进行更一般的建模，并且在实践中非常有效。 两种公式之间的区别在于，是否在预测中使用Z的对角线上条目。



#### Online Compact Convexified FM

**再次重申OCO框架所需要的两个基础要求：**

> 1. Any instance of all the model parameters should be represented as a single point from a convex compact decision set;
> 2. The loss incurred by the prediction should be formulated as a convex function over the decision set.

Vanilla FMde特征向量w和分解后的特征交互向量V，它们是分开的部分，不能公式化为决策集合上的单个点，所以不能直接用OCO框架，不满足要求1；FM的预测值y相对于V是非凸的，因此放到损失函数里，得到的损失也是相对于V非凸的。

尽管之前的两个工作提出了两种凸FM的公式，但是仍然不适用于OCO框架，因为它们将w和Z分开对待，打破了要求1。

##### Compact Convexified FM

为了满足OCO，先设计了CCFM。主要思想是把所有的参数（包括偏置、一阶特征矩阵和二阶特征交互矩阵），都放到了一个增广矩阵中，然后强制为低秩。由于低秩属性并不是凸约束，因此我们将其与有界核范数约束近似，这是机器学习社区中的常见做法[3，13，26]。

首先像工作[3,33]一样，把特征交互的矩阵直接建模为$Z\in\mathbb{R}^{d\times d}$。然后把$w_0,w,Z$重写到单个紧致的增广矩阵C中：

$$C=\left[ \begin{matrix}   Z & w \\ w^T & 2w_0  \end{matrix}  \right]$$

其中$Z=Z^T\in\mathbb{R}^{d\times d}, w\in\mathbb{R}^d, w_0\in\mathbb{R}$。

为了降低复杂度，需要把C弄成低秩矩阵。但是矩阵秩的约束是非凸的，不适合OCO框架。**矩阵C的秩的典型近似是它的核范数$\Vert C\Vert_{tr}=tr(\sqrt{C^T C})=\sum_{i=1}^{d}\sigma_i$，其中$\sigma_i$是C的第i个奇异值。**由于奇异值非负，因此核范数本质上是矩阵秩的凸替代[3、13、26]。因此，考虑用有界核范数$\Vert C\Vert_{tr}\le \delta$来作为一种松弛来代替秩约束。

 ![](/assets/images/2020-05-24-Online-Compact-Convexified-FM/image-20200525195418734.png){:width="400"}





















#### Reference

[13 Elad Hazan and Satyen Kale. 2012. Projection-free Online Learning. In Proceedings ofthe 29th International Coference on International Conference on Machine Learning (ICML’12). Omnipress, USA, 1843–1850]

[26 Shai Shalev-Shwartz. 2012. Online Learning and Online Convex Optimization. Found. Trends Mach. Learn. 4, 2 (Feb. 2012), 107–194.]









