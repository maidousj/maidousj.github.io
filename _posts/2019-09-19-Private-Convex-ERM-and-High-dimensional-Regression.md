---
title: Private Convex ERM and High dimensional Regression (Skimming)
layout: post
date: 2019-09-19 16:30
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- DP
- ERM
- Objective Perturbation
author: Sun
---

Kifer D, Smith A, Thakurta A. Private convex empirical risk minimization and high-dimensional regression[C]//Conference on Learning Theory. 2012: 25.1-25.40.

本文考虑了sparse learning problems。首先扩展了“objective perturbation”的分析到凸的ERM问题上，表明可以采用更少的noise(更准确)；其次，给出了针对高维数据(p远大于n)下的sparse regression的两种隐私保护算法，表明解决sparse regression问题的随机算法可以同时保证稳定性和准确性，这在确定性算法中是不可能的。

<!--more-->

#### Related work

Objective perturbation是由Chaudhuri提出的，[1]进行了进一步的研究（没有Google到）。

[2]提出了设计private算法的通用技术，有很多实现方式，[3]把它用在了一类统计问题的解决中，包括低维的ERM。

Output扰动比目标扰动需要更少的假设，二者的理论保证是差不多的，比[3,4]要强。实验中，目标扰动比输出扰动强不少。

但是，以上工作都是在低维领域的，当$p\gg n$时，它们都不好使。

#### Contributions

##### Improving Objective Perturbation

**More Accurate Objective Perturbation.** Chaudhuri是加入了服从gamma分布的噪声在目标函数中。本文表明，如果加入服从高斯分布的噪声，可以给utility带来$\tilde{\Omega}(\sqrt{p})$的提升，privacy guarantee则从$\varepsilon$-DP放松为$(\varepsilon,\delta)$-DP。

**Generalized Privacy Analysis and a Limit Theorem for DP.** 本文还证明了即使convex regularizer是不可微的，而且参数向量$\theta$是被限定在closed convex set中的，这时目标扰动仍然是private的。

本文的分析还把目标扰动的应用范围扩大了，比如Lasso(regularizer is L1 norm)，核正则项的最小化(以前的工作不行)。分析主要应用的工具就是*limit theorem for DP*。

> The theorem states that if a sequence of $(\varepsilon, \delta)$-differentially private algorithms $A_1, A_2,$ . . . converges in a weak sense, then the limiting algorithm $A = \lim_{i\to\infin}A_i$ is also $(\varepsilon, \delta)$-differentially private.

（什么是converge in a weak sense?）

![](/assets/images/2019-09-19-Private-Convex-ERM/image-20190920111409934.png)

扩展（泛化）这种目标扰动的分析主要思想是，把不可微的有限定条件的问题转化为一系列可微的无限制的问题，然后应用我们的极限定理。

**Data-dependent Utility Analysis.** 提出了数据依赖的可用性分析。

##### Sparse Regression

考虑高维学习问题。提出了两步的方法：首先选择一个小的support集合(a support set with small size)；然后通过目标扰动算法找出这个集合上的参数。

第一步有两个算法：一种是*Superpolynomial
time, via exponential sampling:* 应用[5]提出的指数机制来采样；另一种是*Polynomial
time, via sample-and-aggregate:* 利用[6]提出的sample and aggregate框架，将数据划分成不相交的block，

> select a support set for each block and then aggregates the results via a novel "voting" aggregation algorithm.

#### DP Convex Optimization

##### Tool: A limit theorem for differentially private algorithms
![](/assets/images/2019-09-19-Private-Convex-ERM/image-20190920143729775.png)

（我觉得这个定理大概就是说一堆目标函数中加了噪声b的算法，不对，没有理解，i趋向无穷怎么讲。。先往下看看）

##### Application: Private Constrained Optimization

![](/assets/images/2019-09-19-Private-Convex-ERM/image-20190920155542516.png)

$\hat{\mathcal{L}}(\theta;\mathcal{D})=\frac{1}{n}\sum_{i=1}^n \ell(\theta;d_i)$是二次连续可微凸损失函数，$r$是任意凸正则项(可能是不可微的)。加上$\frac{\Delta}{2n}\Vert\theta\Vert_2^2$保证了目标函数是$\frac{\Delta}{n}$-强凸的，减少了单个数据的影响。$\frac{b^T \theta}{n}$的加入保证了隐私性。

![](/assets/images/2019-09-19-Private-Convex-ERM/image-20190920161526144.png)

$\zeta$是Hessian矩阵的上界，$\lambda$是Hessian矩阵特征值的上界，$\Delta\geq\frac{2\lambda}{\epsilon}$。定理2表明算法1满足DP。其思想是应用了两次定理1。

> We first consider **unconstrained optimization** and convolve the regularizer $r$ with a sequence $K1,K2,$. . . of infinitely differentiable kernels. This results in a sequence of smooth optimization problems that can be solved differentially privately by the results of Chaudhuri(2011). We prove pointwise convergence of their differentially private solutions and then invoke Theorem 1. For **constrained optimization**, we replace the hard constraint $\theta\in \mathbb{F}$ with a sequence of soft constraints by adding penalties for $\theta\notin\mathbb{F}$ that depend on the distance from $\theta$ to $\mathbb{F}$. We again show pointwise convergence and invoke Theorem 1.

(真的是。。没看懂。unconstrained和constrained这俩对应的是什么具体例子)















#### Reference

[1] Cynthia Dwork, Parikshit Gopalan, Huijia Lin, Toniann Pitassi, Guy Rothblum, Adam Smith, and Sergey Yekhanin. An analysis of the Chaudhuri and Monteleoni algorithm. Technical Re- port NAS-TR-0156-2012, Network and Security Research Center, Pennsylvania State University, USA, February 2012.（没找到）

[2] Kobbi Nissim, Sofya Raskhodnikova, and Adam Smith. Smooth sensitivity and sampling in private data analysis. In STOC, 2007.

[3] Adam Smith. Privacy-preserving statistical estimation with optimal convergence rates. In STOC, 2011.

[4] Cynthia Dwork and Jing Lei. Differential privacy and robust statistics. In STOC, 2009.

[5] Frank McSherry and Kunal Talwar. Mechanism design via differential privacy. In FOCS, 2007.

[6] Kobbi Nissim, Sofya Raskhodnikova, and Adam Smith. Smooth sensitivity and sampling in private data analysis. In STOC, 2007.







