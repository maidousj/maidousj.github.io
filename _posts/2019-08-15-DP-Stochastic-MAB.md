---
title: (Nearly) Optimal Differentially Private Stochastic Multi-Arm Bandits notes
layout: post
date: 2019-08-15 16:46
image: /assets/images/
headerImage: false
category: blog
tag:
- DP
- Multi-armed Bandit
author: Sun
---

> Mishra N, Thakurta A. (Nearly) optimal differentially private stochastic multi-arm bandits[C]//Proceedings of the Thirty-First Conference on Uncertainty in Artificial Intelligence. AUAI Press, 2015: 592-601.

#### Introduction

UAI 2015的文章，主要是针对UCB算法和TS算法进行了隐私保护，声称达到了接近于non-private版本算法的效果(较低的regret)。

在motivation中提到了**practical**的一点，是说在广告点击中，可以获得点击广告的反馈，而未点击的候选广告则没有任何反馈，而bandit learning的方式正适用于这一点，且有良好的理论保证。（这就很practical了？）

#### Tree based aggregation

[1,2]中介绍了基于树的聚合方法。树聚合的方法可以用于处理流数据，对于一个数据集$D = \{f_1,\dots,f_T\}$，每个时刻只有一个$f_t \in [0,1]$到达。在时刻t，该机制输出$v_t=\sum_{\tau=1}^t f_\tau$并保证输出序列$\{f_1,\dots,f_T\}$满足$\epsilon$-DP。

> One can design an algorithm (using a binary tree based aggregation), which assures an additive error of $O(\frac{\log^{1.5}T}{\epsilon})$ 􏰈 per query. 
>
> Moreover, it can be extended to the case where $f_t \in \mathbb{R}^p$ and $\Vert f_t \Vert _2 \leq 1$ for all $t \in [T]$.

可以扩展。

#### Private UCB Sampling

UCB的regret bound是$O(\log T)$的。

每个arm对应的reward总值$r_a(t)$只依赖于我们想要保护的数据集，因此只要保证了$r_a(t) \ \ t\in[T]$ **序列**的隐私性就可以保证整个算法的隐私性，也就是只要每个arm满足$\epsilon/k$-DP，整个算法就满足$\epsilon$-DP。

![image-20190816161000372](/assets/images/2019-08-15-DP-Stochastic-MAB/privateUCB.png){:width = 400}

> Additionally, to counter the noise added to the empirical mean, we loosen the confidence interval for the biases of each arm.

从算法1中可以看出，在第4和12行将每次获取的reward值$f_t(a_t)$通过基于树的聚合机制实现了隐私保护。在第7行，为了“counter the noise added to the empirical mean”，加入了这个数值用来放松每个arm的置信区间。

##### Privacy Guarantee

k个arm，维护k棵树，每棵树保证是$\epsilon/k$-DP，整个算法就满足$\epsilon$-DP。

##### Utility Guarantee

![image-20190816162305967](/assets/images/2019-08-15-DP-Stochastic-MAB/utility_private_ucb.png){:width = 400}

整个算法的regret可以由$\mathbb{E}[\sum_{a \in C: \mu_a < \mu_a^* } \Delta_a n_a(T)]$给出，其中$\Delta_a = \mu_a^*-\mu_a$。首先通过计算整个reward总值中被加入的噪声量的bound，然后用这个bound可以表明次优的arm被选的次数很少。然后通过分析次优arm的exploration and exploitation阶段，表明在$O(\frac{k\log^2T \log(kT)}{\epsilon\Delta^2})$轮的选择后，就大概率不会再被选了。（这种方法主要是按照non-private UCB sampling [3]来分析的）。

![](/assets/images/2019-08-15-DP-Stochastic-MAB/lamma5-1.png){:width = 400}

![](/assets/images/2019-08-15-DP-Stochastic-MAB/lamma5-2.png){:width = 400}

![](/assets/images/2019-08-15-DP-Stochastic-MAB/lamma6.png){:width = 400}

#### Reference

[1] TH Hubert Chan, Elaine Shi, and Dawn Song. Private and continual release of statistics. In *ICALP*. 2010 

[2] Cynthia Dwork, Moni Naor, Omer Reingold, Guy Roth- blum, and Salil Vadhan. On the complexity of differentially private data release: efficient algorithms and hardness re- sults. In *STOC*, pages 381–390, 2009. 

[3] Kamalika Chaudhuri. Topics in online learning: Lecture notes. 2011. 

