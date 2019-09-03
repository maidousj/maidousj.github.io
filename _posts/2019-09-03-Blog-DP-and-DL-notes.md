---
title: Deep learning and differential privacy notes
layout: post
date: 2019-09-03 18:08
image: /assets/images/
headerImage: false
category: Blog
tag:
- DP
- DL
author: Sun
---

大佬博文[Deep learning and differential privacy](https://github.com/frankmcsherry/blog/blob/master/posts/2017-10-27.md)阅读。

这篇博文是大佬Frank McSherry在看了[Privacy-Preserving Deep Learning (CCS15)](http://www.shokri.org/files/Shokri-CCS2015.pdf)和[Deep Models Under the GAN: Information Leakage from Collaborative Deep Learning (CCS17)](https://arxiv.org/pdf/1702.07464.pdf)之后写的。这两篇文章，一篇说自己用DP进行了保护隐私的federated learning，很强大，一篇说以DP的方式来分享模型参数是不行的，不信你看我拿出了训练数据集中的数据。于是大佬觉得，这不矛盾吗：

> Well, *at least* one of the two of them has to be wrong. Just because they can't both be right doesn't mean they can't both be wrong, which to my reading they both are.

<!--more-->

#### Privacy-Preserving Deep Learning

直接上大佬的结论：直接共享梯度而不是数据并不能保证数据不泄漏。

> Gradient updates can reveal much of your source data in the clear. Just dropping a few of the updates doesn't help. Note that the above isn't a demonstration of an attack, which would be much clearer about whether I am making this up, but it should at least convince you that "releasing gradients, not data" is not especially indirect leakage.

文章中讨论了在每一次update时候添加噪声，当这updates累积起来的时候，噪声可以被抵消掉。但实际上，“this guarantees that you leak at most epsilon differential privacy with each update to a perceptron.” 

![](/Users/sunjie/Documents/workspace/maidousj.github.io/assets/images/2019-09-03-DPDL/2015.png){width="400"}

作者实验部分的$\varepsilon$在计算时实际上需要乘以参数的个数，也就是总的隐私预算：

$$\varepsilon = per-parameter * theta*105,506$$

"Standalone"那条线(baseline)表示每个参与者只用了自己的数据，没有sharing data。

> The measurements where the "differential privacy" lines cross that horizontal baseline all have privacy guarantees of (using the formula above) 10,550.6 differential privacy. That's not so great.

更为惨的是，这只是per-epoch的DP cost。。

直接把大佬的结论留这把，有点刻薄啊感觉。

> ##### Conclusions
>
> I don't think the techniques the authors propose provide "privacy", in any sense other than that you don't literally directly reveal your naughty photos to everyone, which might remove some of the social awkwardness. Except that you mostly do, if you use the multilayer perceptron. The "fractions of gradients reported" is probably not a valuable privacy quantification, in that the multilayer perceptron gives each pixel multiple chances to be revealed, and what we probably want is the total number of parameters updated. The "per-parameter differential privacy" guarantee is similarly problematic, in that you still have to multiply by the number of parameters revealed each epoch, and then by the number of epochs (which are not reported).
>
> This sounds a bit grim, so I'm happy to slot in any further illumination the authors would like to provide. It is possible that I've misread something, of course. If the "negligible utility loss" comes with either "releasing pixels in the clear" or "10,550.6 differential privacy", it doesn't seem like a great trade-off yet.

#### Deep Models Under the GAN

第二篇CCS17是站在CCS15对立面的，他们说任何collaborative deep learning approach都容易受到他们的攻击。

> Unfortunately, we show that any privacy-preserving collaborative deep learning is susceptible to a powerful attack that we devise in this paper.

(这个当时组里的小朋友分享这篇的时候提到过，这篇文章把符合DP的算法用的数据集偷到了，是不是DP不靠谱，我记得我当时还说15年那篇也没定理说它是满足DP的，但是人CCS17的paper，既然说可以攻击DP的算法，那是不是因为本来DP定义就是在相邻数据集输出很像，所以即使是加了噪声的图像也可能看起来很像。现在看起来自己还是应该在深入的想一下呀，跑跑代码什么的。。)

