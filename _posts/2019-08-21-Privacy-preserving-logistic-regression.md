---
title: DP-ERM系列一：Privacy preserving logistic regression notes
layout: post
date: 2019-08-21 16:16
image: /assets/images/
headerImage: false
category: blog
tag:
- DP
- Logistic Regression
- Kamalika Chaudhuri
author: Sun
---

大神Kamalika Chaudhuri这一系列的开坑之作，发表在nips2008上。主要思路就是Output Perturbation。

在背景介绍里提到[1]虽然加更少的噪声（smoothed-sensitivity）就可以保护隐私，但是某个函数的smoothed sensitivity比较难计算。

#### A Simple Algorithm (Output Perturbation)

![](/assets/images/2019-08-21-pplr/image-20190821164957915.png)

上述算法可以很容易地看出，在输出上直接加入了来自Gamma分布的噪声。

$$w^* = \arg\min_w \frac{1}{n}\sum_{i=1}^n l(w, (x_i,y_i))+\frac{1}{2}\Vert w\Vert^2$$

$$w^{priv}=w^*+b, b\sim \Gamma(d,\frac{2}{n\lambda})$$ (d应该是x的维度？b是个向量，是每个都不一样还是一组一样大小的元素？)

![](/assets/images/2019-08-21-pplr/image-20190821172118987.png)

以上主要给出sensitivity的大小。

参考[2]，给出计算sensitivity的过程。

$$G(w) = J(w,D)=\frac{1}{n}\sum_{i=1}^n l(w,(x_i,y_i))+\frac{1}{2}\Vert w \Vert^2$$

$$g(w)=\frac{1}{n}(l(y'_n, w^Tx'_n)-l(y_n, w^Tx_n)), J(w,D')=G(w)+g(w)$$

$$\Delta_{\arg\min}=\Vert \arg\min_w G(w)-\arg\min_w (G+g)(w) = \Vert w_1-w_2 \Vert$$

$$\nabla G(w_1)=\nabla G(w_2)+\nabla g(w_2)=0$$

$G(w)$是$\lambda$-强凸的，因此$(\nabla G(w_1)-\nabla G(w_2))^T(w_1-w_2) \geq \lambda\Vert w_1-w_2 \Vert^2$ 

$$\Vert w_1-w_2 \Vert\cdot\Vert\nabla g(w_2)\Vert \geq (w_1-w_2)^T \nabla g(w_2)\geq \lambda\Vert w_1-w_2\Vert^2$$

所以$\Vert w_1-w_2 \Vert\leq \frac{1}{\lambda}\max_w \nabla\Vert g(w) \Vert$

$$\nabla g(w)=\frac{1}{n}(y_n l'(y_n w^Tx_n)x_n - y'_n l'(y'_n w^Tx'_n)x'_n)$$ (有点不确定？)

又因为$\vert l'\vert\leq 1, \Vert x\Vert\leq 1, \vert y\vert \leq 1$,所以$\Vert\nabla g(w)\Vert \leq \frac{2}{n}$, $\Delta_{\arg\min} \leq\frac{2}{n\lambda}$.

![](/assets/images/2019-08-21-pplr/image-20190821202229018.png)

这个是性能 (learning performance) 差距的bound。

#### A New Algorithm (Objective Perturbation)

![](/Users/sunjie/Documents/workspace/maidousj.github.io/assets/images/2019-08-21-pplr/image-20190821203206628.png)

同样需要$\Vert x_i \Vert \leq 1$。这个$b$也是个向量？是一堆一样大小的噪声 还是每个大小不一样？

> We observe that our method solves a convex programming problem very similar to the logistic regression convex program, and therefore it has running time similar to that of logistic regression.

算法2解决了一个凸规划问题，和lr很像。相当于是针对目标函数的扰动。





#### Reference 

[1] K. Nissim, S. Raskhodnikova, and A. Smith. Smooth sensitivity and sampling in private data analysis. In D. S. Johnson and U. Feige, editors, STOC, pages 75–84. ACM, 2007.

[2] [满足差分隐私的经验误差最小化方法](https://zhuanlan.zhihu.com/p/55757642)



