---
title: DP-ERM系列二：DP SGD notes
layout: post
date: 2019-08-24 15:18
image: /assets/images/
headerImage: false
category: blog
tag:
- DP
- Logistic Regression
- Kamalika Chaudhuri
author: Sun
---

DP-SGD主要是利用了差分隐私对梯度下降过程进行扰动，以达到学习出一个满足差分隐私的模型：Song S, Chaudhuri K, Sarwate A D. Stochastic gradient descent with differentially private updates[C]//2013 IEEE Global Conference on Signal and Information Processing. IEEE, 2013: 245-248.

#### Stochastic Gradient Descent

训练线性分类器就是解决如下的凸优化问题：

$$w^{*}=\underset{w \in \mathbb{R}^{d}}{\operatorname{argmin}} \frac{\lambda}{2}\|w\|^{2}+\frac{1}{n} \sum_{i=1}^{n} \ell\left(w, x_{i}, y_{i}\right)$$

SGD的表达式如下：

$$w_{t+1}=w_{t}-\eta_{t}\left(\lambda w_{t}+\nabla \ell\left(w_{t}, x_{t}, y_{t}\right)\right)$$

SGD with mini-batch:

$$w_{t+1}=w_{t}-\eta_{t}\left(\lambda w_{t}+\frac{1}{b} \sum_{\left(x_{i}, y_{i}\right) \in B_{t}} \nabla \ell\left(w_{t}, x_{i}, y_{i}\right)\right)$$

#### DP-SGD

每次更新时，在梯度上加入噪声，以实现满足$\epsilon$-DP的算法。

$$w_{t+1}=w_{t}-\eta_{t}\left(\lambda w_{t}+\nabla \ell\left(w_{t}, x_{t}, y_{t}\right)+Z_{t}\right)$$,

其中$Z_t\sim \mathbb{R}^d$是服从以下概率密度的随机向量，

$$\rho(z) \propto e^{-(\alpha / 2)\|z\|}$$.

对于mini-batch来说，

$$w_{t+1}=w_{t}-\eta_{t}\left(\lambda w_{t}+\frac{1}{b} \sum_{\left(x_{i}, y_{i}\right) \in B_{t}} \nabla \ell\left(w_{t}, x_{i}, y_{i}\right)+\frac{1}{b} Z_{t}\right)$$.

![](/assets/images/2019-08-24-pplr2/image-20190825231923025.png)

定理这里说如果$\|\nabla \ell(w, x, y)\| \leq 1$。

$$\Delta_{g r e d}=\sup \left\|\nabla \ell(w, x, y)-\nabla \ell\left(w, x^{\prime}, y^{\prime}\right)\right\|=2$$



