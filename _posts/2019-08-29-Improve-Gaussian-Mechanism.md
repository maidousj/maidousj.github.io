title: Improving the Gaussian Mechanism notes
layout: post
date: 2019-08-29 14:29
image: /assets/images/
headerImage: false
category: Paper Reading
tag:

- DP
- Gaussian Mechanism
author: Sun

Balle B, Wang Y X. Improving the gaussian mechanism for differential privacy: Analytical calibration and optimal denoising[J]. arXiv preprint arXiv:1805.06530, 2018.

提出了两种方法让bound更紧：

> The first improvement is **an algorithmic noise calibration strategy** that uses numerical evaluations of the Gaussian cumulative density function (CDF) to obtain the optimal variance to achieve DP using Gaussian perturbation. 

第一种是通过高斯的CDF来直接调整方差，以得到更优的高斯机制。

<!--more-->

> The second improvement equips the Gaussian perturbation mechanism with a post-processing step which denoises the output using adaptive estimation techniques from the statistics literature. 

第二种用后处理的步骤，用统计学上的适应性估计技术对output降噪。

#### 经典高斯机制的限制

经典高斯机制：$Z\sim N(0, \sigma^2)$, For any $\epsilon, \delta \in (0,1), \sigma = \Delta\sqrt{2\log(1.25/\delta)}/\epsilon$, 可以保证$(\epsilon,\delta)$-DP 

很自然的两个疑问是：

a. 该$\sigma$取值在满足DP的前提下，是否保证是最小的噪声量 

b. 当$\epsilon \ge 1$会发生什么。 

这篇文章指出当$\epsilon \rightarrow 0$ (high privacy regime)，$\sigma$是次优的。 

而当$\varepsilon >1$时，

> large values of $\varepsilon$ the standard deviation of a Gaussian perturbation that provides $(\varepsilon, \delta)$-DP must scale like $\Omega(1/\sqrt{\varepsilon})$. 

1. Limitations in the High Privacy Regime

   ![](/assets/images/2019-08-29-Improved-Gaussian/image-20190906135254057.png){:width="400"}

   接下来会解释为什么经典高斯机制不能导出$\varepsilon \to 0$时的tight bounds，这也会说明定理2不是一个极端的例子，而是a fundamental limitation of trying to establish $(\varepsilon,\delta)$-DP through said sufficient condition.

2. Limitations of Privacy Loss Analyses 

   加一个服从高斯分布的噪声时，隐私损失也是服从高斯分布的[1]：

   ![](/assets/images/2019-08-29-Improved-Gaussian/image-20190906164622596.png)

   经典高斯机制的隐私分析需要以下条件：

   a mechanism M is $(\varepsilon,\delta)$-DP if the privacy loss $L_{M,x,x'}$ satisfies

   $$\forall x\simeq x': \mathbb{P}[L_{M,x,x' \ge \varepsilon}\leq \delta]$$

   引理3表明高斯机制的privacy loss也是一个高斯随机变量，对任何一对使得$f(x)\ne f(x')$数据集，有$\mathbb{P}[L_{M,x,x'}>0]\ge 1/2$。这一点说明通常不可能用满足$(\varepsilon,\delta)$-DP的充分条件去证明高斯机制可以在任何$\delta<1/2$的情况下达到$(0,\delta)$-DP。也就是说，充分条件对于$\varepsilon \to 0$是不必要的。

3. Limitations in the Low Privacy Regime

   ![](/assets/images/2019-08-29-Improved-Gaussian/image-20190906175109564.png)

   当$\varepsilon \to \infty$时，$\delta$会收敛到1/2.











#### Reference

[1] Dwork, C. and Rothblum, G. N. Concentrated differential privacy. arXiv preprint arXiv:1603.01887, 2016.



