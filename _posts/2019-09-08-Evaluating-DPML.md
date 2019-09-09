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

#### Introduction

[1] 中的$\varepsilon$达到了百万级，对于隐私保护毫无意义。

对于给定的隐私预算，提高utility的一种途径是tighten the composition of DP。[2,3,4]通过提供tighter analysis of the privacy budget under composition，在添加同样噪声量的情况下，可以达到更好的privacy(更小的$\varepsilon$)，因此可以在给定$\varepsilon$的情况下获得更好的utility。但是在adversarial场景下，泄漏了多少privacy呢？因此本文评估了不同DP变体不同隐私预算下的隐私泄露情况，包括在membership inference attacks下会有多少条个体训练数据被泄露。

#### Related works

[5,6]对现有的DP实现进行了*correctness*的评估。[7]提供了*effectiveness* of DP against attacks，但是没有明确回答$\varepsilon$应该用多少，也没有提供privacy leakage的评估。[8]考虑了放松DP notion的方式来取得更好的utility，但是也没有评估leakage。[9]是最接近本文的，评估了DP implementations against membership inference attacks，但是也没有评估不同DP变体的privacy leakage。[10]reported on extensive hypothesis testing differentially private machine learning using the Neyman-Pearson criterion, 给出了基于敌手先验知识的privacy budget设置的指导。











#### Conclusion

通常使用的$\varepsilon$ values的组合和各种DP的变体，并不能提供很好的utility-privacy trade-offs。What the state-of-the-art inference attacks can infer和DP可以提供的保证之间还存在巨大的差距。

直白一点就是，较好的utility下，任何DP变体提供的隐私保证基本上是无意义的，尽管通过attack观察到的泄露也是相对较低的（为什么这么说，泄露低了不就是良好的保证么？？）。

> Research is needed to understand the limitations of inference attacks, and eventually to develop solutions that provide desirable, and well understood, utility-privacy trade-offs.

#### Reference

[1] Reza Shokri and Vitaly Shmatikov. Privacy-preserving deep learning. In ACM Conference on Computer and Communications Security, 2015.

[2] Mark Bun and Thomas Steinke. Concentrated differential privacy: Simplifications, extensions, and lower bounds. In Theory ofCryptography Conference, 2016.

[3] Cynthia Dwork and Guy N. Rothblum. Concentrated differential privacy. arXiv:1603.01887, 2016.

[4] Ilya Mironov. Rényi differential privacy. In IEEE Computer Security Foundations Symposium, 2017.

[5] Zeyu Ding, Yuxin Wang, Guanhong Wang, Danfeng Zhang, and Daniel Kifer. Detecting violations of differential privacy. In ACM Conference on Computer and Communications Security, 2018.

[6] Michael Hay, Ashwin Machanavajjhala, Gerome Miklau, Yan Chen, and Dan Zhang. Principled evaluation of differentially private algorithms using DPBench. In ACM SIGMOD Conference on Management of Data, 2016.

[7] Nicholas Carlini, Chang Liu, Jernej Kos, Úlfar Erlingsson, and Dawn Song. The Secret Sharer: Evaluating and testing unintended memorization in neural networks. In USENIX Security Symposium, 2019.

[8] Ninghui Li,Wahbeh Qardaji, Dong Su,Yi Wu, andWein- ing Yang. Membership privacy: A unifying framework for privacy definitions. In ACM Conference on Computer and Communications Security, 2013.

[9] Md Atiqur Rahman, Tanzila Rahman, Robert Laganière, Noman Mohammed, and Yang Wang. Membership inference attack against differentially private deep learning model. Transactions on Data Privacy, 2018.

[10] Changchang Liu, Xi He, Thee Chanyaswad, Shiqiang Wang, and Prateek Mittal. Investigating statistical privacy frameworks from the perspective of hypothesis testing. Proceedings on Privacy Enhancing Technolo- gies, 2019.













