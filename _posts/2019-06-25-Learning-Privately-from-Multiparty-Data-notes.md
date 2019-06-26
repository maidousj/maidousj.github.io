---
title: Learning Privately from Multiparty Data 阅读
layout: post
date: 2019-06-25 10:06
image: /assets/images/
headerImage: false
category: blog
tag:
- PPML
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

![](/assets/images/snapshot4paper/icml16-assume.png){:width="400"}

#### Transferring knowledge of ensemble 

##### Local classifiers

假设local分类器是M个黑盒(可以是不同类型的分类器)，每个分类器通过本地的训练集训练，数据是独立同分布的。切分数据通过sample without replacement [3]。

##### Privacy issues of direct release

第一步中，local分类器被一个可信任的实体收集。最简单的方法就是在DP处理后直接释放所有M个分类器参数。但是这种操作需要一个恒定的敏感度(sensitivity)，不如直接释放统计数据的平均值，这样敏感度为$O(M^{-1})$。此外有效的DP机制只能用在特定类型的分类器上[4]。

另一种方法是，将ensemble当成一种服务来对test data进行预测。如果用majority voting来为测试样本做预测，Report Noisy Max[5] 可以被用来sanitize the votes for a single query。但是当查询次数变多时，noise是和查询次数线性成比例的，这在现实中很不实用。

##### Leveraging auxiliary data

为了解决上述问题，提出transfer the knowledge of the ensemble to a global classifier using auxiliary unlabeled data。具体地，利用ensemble来为辅助数据生成标签，然后再用来训练global分类器。辅助数据的数量不影响privacy (就因为没有标签就可以不影响privacy吗？)，反而数据量越大，分类器越接近于原始的ensemble，bound是$O(N^{-1})$。和用ensemble预测对比，the sanitized global classifier可以被用来任意多的查询次数，而不影响privacy。

#### Finding a global private classifier

##### First attempt: ERM with majority voting

利用M个local分类器的majority voting来生成辅助数据。就是超过半数的分类器对当前数据的预测标签作为该数据的标签。

![image-20190626110203554](/assets/images/snapshot4paper/icml16-alg1.png){:width="400"}

如图算法1表示了这种方法。公式6就是majority voting。公式8是ERM的损失函数

$$R_{S}^{\lambda} (w) = \frac{1}{N} \sum_{(x,v \in S)} l(h(x;w),v) + \frac{\lambda}{2} \Vert w \Vert ^2 \tag{8}$$

(后边还列了一下这个式子有和没有正则项的期望，这不是纯凑吗？还没看到用得着的地方啊。。)

> **Theorem 1.** *The perturbed output* $w_p = w_s + \eta$ *from Algorithm 1 with* $p(\eta) \propto e^{-\frac{\lambda \epsilon}{2} \Vert \eta \Vert}$ *is* $\epsilon$*-differentially private.*

Proof. Suppose $D = (S^{(1)}, \dots, S^{(M)})$ 是M个训练集，$D' = (S'^{(1)}, \dots, S^{(M)})$是相邻的数据集，通过$D$和$D'$计算出相应的local分类器$H = (h_1, \dots, h_M)$和$H' = (h'_1, \dots, h_M)$。通过投票生成相应的辅助数据$S = \{x_i, v(x_i)\}$和$S' = \{x_i, v'(x_i)\}$，同样的features但是可能不同的labels。$R_S^{\lambda} (w)$和$R_{S'}^{\lambda} (w)$分别是基于$S$和$S'$的regularized empirical risks。$w_s$和$w_{s'}$是对应risk的minimizer。根据[2]的推论7和8可以得出

$$\Vert w_s - w_{s'} \Vert \leq \frac{1}{\lambda} \max _w \Vert \nabla g(w) \Vert,$$

其中，$g(w)$ is the risk difference $R_S^{\lambda} (w) - R_{S'}^{\lambda} (w)$，本文中

$$ \Vert \nabla g(w) \Vert  \leq \frac{1}{N} \sum_{i=1}^{N} \Vert v(x_i) x_i l'(v(x_i) w^T x_i) - v'(x_i) x_i l'(v'(x_i) w^T x_i) \Vert$$

$$ \leq \frac{1}{N} \sum_{i=1}^{N} \Vert x_i \Vert \times \vert l'(w^Tx_i) + l'(-w^Tx_i) \vert . \tag{*}$$

注意到假设了$\Vert x \Vert \leq 1 \text{ and } \vert l'(\cdot) \vert \leq 1$。最坏的情况是每个$v(x_i)$和$v'(x_i)$都不相同，因此the RHS of $*$ is bounded by 2. 因此，$w_s$的$L_2$ sensitivity是

$$\max_{S,S'} \Vert w_s - w_{s'} \Vert \leq \frac{2}{\lambda}$$.

因此得证。

##### Performance issues of 





#### Reference

[1] Pathak, Manas, Rane, Shantanu, and Raj, Bhiksha. Multiparty differential privacy via aggregation of locally trained classifiers. In *Advances in Neural Information Processing Systems*, pp. 1876–1884, 2010.

[2] Chaudhuri, Kamalika, Monteleoni, Claire, and Sarwate, Anand D. Differentially private empirical risk minimization. *The Journal of Machine Learning Research*, 12:1069–1109, 2011.

[3] Politis, D. N., Romano, J. P., and Wolf, M. *Subsampling*. Springer Verlag, 1999.

[4] Ji, Zhanglong, Jiang, Xiaoqian, Wang, Shuang, Xiong, Li, and Ohno-Machado, Lucila. Differentially private distributed logistic regression using private and public data. *BMC medical genomics*, 7(Suppl 1):S14, 2014.

[5] Dwork, Cynthia and Roth, Aaron. The algorithmic foundations of differential privacy. *Theoretical Computer Science*, 9(3-4): 211–407, 2013.