---
title: Learning Privately from Multiparty Data 阅读
layout: post
date: 2019-06-25 10:06
image: /assets/images/
headerImage: false
category: blog
tag:
- Learning-Privately-from-Multiparty-Data-notes
- DP
author: Sun
---

Hamm J, Cao Y, Belkin M. Learning privately from multiparty data[C]//International Conference on Machine Learning. 2016: 555-563.

#### Abstract

在多方场景下，怎样在不获取其他party's private data的情况下，通过组合本地训练的分类器，训练一个准确的符合DP的分类模型？本文提出了

> transfer the ‘knowledge’ of the local classifier ensemble by first creating labeled data from auxiliary unlabeled data, and then train a global $\epsilon$-differentially private classifier.

本文指出大部分的voting都太敏感，因此提出了新的risk weighted by class probabilities estimated from the ensemble。相对于非隐私的方案，误差控制在$O(\epsilon^{-2} M^{-2})$之内，$M$是parties的数量。

#### Introduction

[1] 提出了通过平均local分类器的参数来得到global分类器，通过DP机制来防止平均参数时造成的隐私泄露。平均参数是一个简单并且实用的步骤，可以通过Yao提出的SMC来实现。但是，对于非数值型的参数，比如决策树或者聚合不同类型的分类器时，直接平均参数并不适用。

本文提出了通过两个步骤来组合local分类器为一个global分类器的方法：第一步，本地训练的分类器被一个信任的实体收集，但是直接使用DP处理过的参数并不实用，

> Instead, we use the classifier ensemble to generates (pseudo)labels for auxiliary *unlabeled* data, thus transferring the knowledge of the ensemble to the auxiliary data.

第二步，用标记过的辅助数据找到一个empirical risk minimizer，然后通过output pertubation[2] 的方法release一个DP的分类器。

当用ensemble of classifiers为辅助数据生成label时，最简单的方法就是majority voting。本文量化的表明了这种训练方式对于local分类器的vote是highly sensitive的（是说对于差分隐私敏感度高吗？）。这样一来会造成很大的性能损失。所以本文提出新的risk insensitive to individual votes，每个采样根据ensemble的confidence来分配权重。

> One of our main results is in Theorem 4: we can achieve $\epsilon$-differential privacy with a generalization error of $O(\epsilon^{-2} M^{−2})$ and $O(N^{−1})$ terms, relative to the expected risk of a non-private solution, where M is the number of parties and N is the number of samples in auxiliary data. This result is especially useful in a scenario where there are a large number of parties with weak local classifiers such as a group of connected smart devices with limited computing capability.

本文的三个优点：

* flexible: 可以组合不同类型的local分类器
* 误差收敛快
* provides $\epsilon$-differential privacy to all samples of a party and not just a single sample.

#### Preliminary

直接用[2]中的对参数加噪声的方式，不同点是：

> One important difference of our setting to previous work is that we consider $\epsilon$-differential privacy of all samples of a party, which is much stronger than $\epsilon$-differential privacy of a single sample. 

然后提了一些假设，类似于[2]中的：

<img src="../assets/images/snapshot4paper/icml16-assume.png " width = "400" align=center />





#### Reference

[1] Pathak, Manas, Rane, Shantanu, and Raj, Bhiksha. Multiparty differential privacy via aggregation of locally trained classifiers. In *Advances in Neural Information Processing Systems*, pp. 1876–1884, 2010.

[2] Chaudhuri, Kamalika, Monteleoni, Claire, and Sarwate, Anand D. Differentially private empirical risk minimization. *The Journal of Machine Learning Research*, 12:1069–1109, 2011.