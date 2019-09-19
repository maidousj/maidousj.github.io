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

**More Accurate Objective Perturbation.** Chaudhuri是加入了服从gamma分布的噪声在目标函数中。本文表明，如果加入服从高斯分布的噪声，可以给utility带来$\tilde{\Omega}(\sqrt{p})$的提升，













#### Reference

[1] Cynthia Dwork, Parikshit Gopalan, Huijia Lin, Toniann Pitassi, Guy Rothblum, Adam Smith, and Sergey Yekhanin. An analysis of the Chaudhuri and Monteleoni algorithm. Technical Re- port NAS-TR-0156-2012, Network and Security Research Center, Pennsylvania State University, USA, February 2012.（没找到）

[2] Kobbi Nissim, Sofya Raskhodnikova, and Adam Smith. Smooth sensitivity and sampling in private data analysis. In STOC, 2007.

[3] Adam Smith. Privacy-preserving statistical estimation with optimal convergence rates. In STOC, 2011.

[4] Cynthia Dwork and Jing Lei. Differential privacy and robust statistics. In STOC, 2009.









