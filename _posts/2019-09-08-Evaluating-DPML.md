---
title: Evaluating Differentially Private Machine Learning in Practice notes
layout: post
date: 2019-09-08 15:24
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- DP
- CDP
- RDP
- zCDP
author: Sun
---

Jayaraman B, Evans D. Evaluating Differentially Private Machine Learning in Practice[C]//28th USENIX Security Symposium (USENIX Security 19). Santa Clara, CA: USENIX Association. 2019.

#### Abstract

在实现PPML时，为了提高模型的可用性，常会选择较大的$\varepsilon$，而对这些选择对有意义的隐私所产生的影响知之甚少；此外，在使用迭代学习方法的场景中，差分隐私的变种可以提供更严密的分析，被用于降低所需的隐私预算，但隐私性和实用性之间存在难以理解的权衡。所以本文量化了这些影响。

<!--more-->

本文发现“可以保证的隐私损失的上界(即使是高级机制)”和“可以被inference attack衡量的有效的隐私损失”存在一个巨大的鸿沟。现有的DPML方法很少为复杂的学习任务提供可接受的utility-privacy trade-offs。













