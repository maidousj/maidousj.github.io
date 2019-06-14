---
title: FTRL online learning algorithm
layout: post
date: 2017-06-28 22:56
image: /assets/images/slamdunk.jpg
headerImage: true
category: blog
tag:
- FTL
- FTRL
- Online Learning
author: Sun
---

### Summary

两种在线学习算法，一种是Online Bayesian Learning，另一种是FTRL(Follow The Regularized Leader)。
提到FTRL就要先了解FTL，FTL的思想是**每次找到让之前所有损失函数之和最小的参数**。 

#### FTL

流程：

> 初始化$w$ 
>
> for $t=1,\dots, n$  
>
> > 损失函数$f_t$
> >
> > 更新
> >
> > $$w = \mathop{argmin}_{w} \sum_{i=1}^t f_i(w)$$



而FTRL算法就是在FTL的优化目标的基础上，加入了正则化项，防止过拟合：

$$w = \mathop{argmin}_{w} \sum_{i=1}^t f_i(w) + R(w) $$

FTRL算法的损失函数，一般也不是能够很快求解的，这种情况下，一般需要找一个代理的损失函数。

代理损失函数需要满足几个要求：

1. 代理损失函数比较容易求解，最好是有解析解
2. 优化代理损失函数求的解，和优化原函数得到的解差距不能太大

为了衡量条件2中的两个解的差距，这里需要引入regret的概念。

假设每一步用的代理函数是$h_t(w)$

$$w_t = \mathop{argmin}_w h_{t-1}(w)$$

$$Regret_t = \sum_{t=1}^T f_t(w_t) - \sum_{t=1}^T f_t(w^*)$$

其中$w^* = \mathop{argmin}\limits_{w} \sum_{i=1}^t f_i(w)  $是原函数的最优解。所以regret的含义就是每次代理函数求出解，和真正损失函数求出解的**损失差距**。这个损失必须满足一定条件，Online Learning才可以有效：

$$\mathop{\lim}_{t \rightarrow \infty} \frac{Regret_t}{t} = 0 \tag{1}$$

随着训练样本的增多，这两个优化目标优化出的参数的实际损失值差距越来越小。



如果$f_t(w)$是凸函数，我们可以用如下的代理损失函数：

$$h_t = \sum_{i=1}^t g_i \cdot w + \sum_{i=1}^t(\frac{1}{2 \eta_t} -\frac{1}{2 \eta_t} ) ||w-w_t||^2$$

其中$g_i$是$f_i(w_i)$的次梯度（如果$f_i(w_i)$是可导的，次梯度就是梯度）。$\eta_t$满足：

$$\eta_{t} = \frac{\alpha}{\sqrt{\sum_{i=1}^{t} g_{t}^{2}}}$$

只要$f_i(w_i)$是凸函数，上面的代理函数一定满足条件(1)。



上面的式子我们可以得出$w$的解析解：

$$w_{t+1,i} = \left\{\begin{array}{ll}0 & |z_{t,i}| < \lambda_{1} \newline-\eta_{t}(z_{t,i} - sgn(z_{t,i})\lambda_{1})  & otherwise \end{array}\right.$$

其中

$$z_{t,i} = \sum_{s=1}^{t}g_{s,i} + \sum_{s=1}^{t}\left( \frac{1}{ \eta_{t,i}} - \frac{1}{ \eta_{t-1,i}} \right) w_{t,i}$$

— — 

whywhy




$$w_{t+1,i} = \left\{\begin{array}{ll}0 & |z_{t,i}| < \lambda_{1} \newline-\eta_{t}(z_{t,i} - sgn(z_{t,i})\lambda_{1})  & otherwise \end{array}\right.$$

可以得到FTRL的更新流程如下：

> 输入$\alpha, \lambda_1$
>
> 初始化 $w_{1…N}, z_{1…N} = 0, n_{1…N} = 0$
>
> for $t = 1 … T$
>
> > 损失函数 $f_t$ for $i = 1 ...N$
> >
> > > 计算
> > >
> > > $$g_{t,i} = \frac{\partial f_i(w_{t-1})}{w_{t-1,i}} $$
> > >
> > > $$z_{t} += g_{t,i} + \frac{1}{\alpha} \left( \sqrt{n_{i} + g_{t,i}^{2}} -\sqrt{ n_{i} } \right) w_{t,i}$$
> > >
> > > $$n_i += g_{t,i}^2 $$
> > >
> > > 更新
> > >
> > > $$w_{t+1,i} = \left\{\begin{array}{ll}0 & |z_{t,i}| < \lambda_{1} \newline-\eta_{t}(z_{t,i} - sgn(z_{t,i})\lambda_{1})  & otherwise \end{array}\right.$$




最后一个公式哪儿去了。

PS: 上述内容整理自美团技术团队的[Online Learning算法理论与实践](http://tech.meituan.com/online-learning.html?utm_source=tuicool&utm_medium=referral)

老！子！看！的！很！晕！



