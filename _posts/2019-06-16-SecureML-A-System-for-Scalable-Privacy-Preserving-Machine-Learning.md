---
title: SecureML 阅读
layout: post
date: 2019-06-16
category: blog
tag:
- PPML 
- Oblivious Transfer
- Garbled Circuit
author: Frank

---

Mohassel P, Zhang Y. Secureml: A system for scalable privacy-preserving machine learning[C]//2017 IEEE Symposium on Security and Privacy (SP). IEEE, 2017: 19-38.

#### Abstract

本论文在特定计算场景下实现了安全多方计算的优化。针对线性回归、逻辑回归、神经网络训练问题，本论文给出了优化方案，并通过理论证明和实际验证说明了方案的可行性。

在两个不会合作的server模型上实现的协议。

>  Our protocols fall in the two-server model where data owners distribute their private data among two non-colluding servers who train various models on the joint data using secure two-party computation. We develop new techniques to support secure arithmetic operations on shared decimal numbers, and propose MPC-friendly alternatives to non-linear functions such as sigmoid and softmax that are superior to prior work.

#### Introduction
本文聚焦于two server model。
综合使用了Secret sharing and arithmetic with precomputed triplets + Garbled circuit

##### Related Work


#### Preliminaries
##### Secure Computation
* **Oblivious Transfer.** OT是一种常被用在MPC中的加密原语。在OT协议中，发送者S有两个输入$x_0, x_1$，接收者R有选择位b，想不泄漏b给S的情况下获取到$x_b$。本文用OT在offline协议中来**生成乘法三元组**；在online阶段为LR和神经网络训练，安全地计算激活函数。

   本文的OT用了[correlated OT extension][1]，其中发送者的两个输入是相关的：一个随机值$s_0$和$s_1 = f(s_0)$。COT的通信：$l$-bit messages，需要$\lambda + l$ bits，计算包括3次哈希。
   
* **Garbled Circuit 2PC** [混淆电路][2]包括带有随机种子$\sigma$的混淆算法和一个函数$f$，生成混淆电路$F$和解码表(decoding table)$dec$；编码算法(encoding algorithm)将$x$和随机种子$\sigma$作为输入生成混淆输入$\hat{x}$；评估算法(evaluation algorithm)将$\hat{x}$和$F$作为输入，返回混淆的输出$\hat{z}$；最后，解码算法(decoding algorithm)将$dec$和$\hat{z}$作为输入，返回$f(x)$.
  
   接下来就可以设计一个安全的两方通信协议：Alice生成随机种子$\sigma$，为函数$f$运行混淆算法得到混淆电路$GC$；利用$\sigma$，将输入$x$编码成$\hat{x}$。
   Alice把$\hat{x}$和$GC$发给Bob。
   Bob利用OT将输入$y$的每一位编码得到$\hat{y}$。运行评估算法，输入为$GC$,$\hat{x}$,$\hat{y}$，得到garbled output $\hat{z}$。
   接下来
   
> We can have Alice, Bob, or both learn an output by communicating the decoding table accordingly.The above protocol securely realizes the ideal functionality $F_f$ that simply takes the parties inputs and computes $f$ on them.
  
* Secret Sharing and Multiplication Triplets.
  所有中间数据的传输都是secret-shared。有三种：***Additive sharing, Boolean sharing and Yao sharing***. [3]中是详细的介绍。
  

  
#### Reference
[1] Asharov G, Lindell Y, Schneider T, et al. More efficient oblivious transfer and extensions for faster secure computation[C]//Proceedings of the 2013 ACM SIGSAC conference on Computer & communications security. ACM, 2013: 535-548.
[2] Yao A C C. Protocols for secure computations[C]//FOCS. 1982, 82: 160-164.
[3] Demmler D, Schneider T, Zohner M. ABY-A Framework for Efficient Mixed-Protocol Secure Two-Party Computation[C]//NDSS. 2015.

##### 结论
有点不想看了。就是大概了解一下目前OT和GC怎么用，细节还是挺难看的。。主要和目前研究的东西不太相关，需要的话等有空再补坑吧。