---
title: 差分隐私的组合性质总结
layout: post
date: 2019-01-23 17:22
image: /assets/images/
headerImage: false
category: Blog
tag:
- course
- CSE660
- DP
- composition theorem
author: Sun
---

[从这来的](https://www.acsu.buffalo.edu/~gaboardi/teaching/cse660-Fall17/CSE660-18.pdf)，记录一下作为总结，之前各种survey看的云里雾里的，总算找到一个清晰的。

<!--more-->

#### 组合性

首先是pure DP的组合性，所谓pure DP就是指$\epsilon$-DP。

- 定理1 ($\epsilon$-DP的标准组合性)：对于$1\leq i \leq k$，如果$M_i: \chi^n \rightarrow R_i$是$\epsilon_i$-DP的算法，那么组合性被定义为，$M(D) = (M_1(D), M_2(D), \dots, M_k(D))$是$\sum_{i=1}^k \epsilon_i$-DP的。

  

- 定理2 ($(\epsilon,\delta)$-DP的标准组合性)：和定理1类似，对于$1\leq i \leq k$，如果$M_i: \chi^n \rightarrow R_i$是$(\epsilon_i, \delta_i)$-DP的算法，那么组合性被定义为，$M(D) = (M_1(D), M_2(D), \dots, M_k(D))$是$(\sum_{i=1}^k \epsilon_i, \sum_{i=1}^k \delta_i)$-DP的。

  

- 定理3 (高级组合性)：对于$1\leq i \leq k$并且**$k < 1/\epsilon$**，$\delta'>0$，如果$M_i: \chi^n \rightarrow R_i$是$(\epsilon, \delta)$-DP的算法，那么组合性被定义为，$M(D) = (M_1(D), M_2(D), \dots, M_k(D))$是$(O(\sqrt{2k\ln(1/\delta')})\epsilon, k\delta + \delta')$-DP的。

#### 可以回答多少查询（queries）

* A single query
  * Randomized Response
  * Laplace Mechanism
  * Exponential Mechanism
* Multiple queries
  * Standard composition -- $\sqrt n$ queries
  * Advanced composition -- $n$ queries

#### 高斯机制

大概是当$\sigma = \frac{\sqrt{2\ln(1.25/\delta)}\Delta_2 f}{\epsilon}$时，对函数$f$加入服从高斯分布的噪声 $nosie \sim N(0, \sigma^2)$，可以满足$(\epsilon, \delta)$-DP.

#### $\delta$的作用

1. 当作DP失败的概率；
2. 在高级组合定理中，当组合了n个查询时，对隐私成本$\epsilon$的增长可以得到更好的bound；
3. 用来对高斯机制进行分析。

其中，**2和3是最初引入$(\epsilon, \delta)$-DP的动机。**

