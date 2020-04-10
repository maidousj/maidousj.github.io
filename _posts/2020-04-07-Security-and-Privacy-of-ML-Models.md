---
title: 机器学习模型安全与隐私研究综述(四)--模型隐私风险与保护
layout: post
date: 2020-04-07 18:30
image: /assets/images/
headerImage: false
category: Blog
tag:
- PPML
- Attack
- Defence
author: Sun
---

纪守领老师综述的第四部分，讲述模型隐私风险与保护。主要场景是机器学习即服务(MLaaS)，数据持有者可以利用第三方提供的模型和算法以及平台提供的计算资源，训练用于特定任务的模型。尽管这种模式给用户训练和发布模型提供了便利，但同时也使得**隐私数据**面临泄漏风险。

这种场景中的攻击是通过某种手段来窃取模型信息或者通过部分恢复数据的方式来推断用户数据中的某些隐私信息。根据窃取目标不同，攻击可以分为训练数据窃取（Training Data Extraction）攻击和模型萃取（Model Extraction）攻击。

####1. 训练数据窃取

通过获取训练数据的大致分布 或者 根据模型的预测结果推断训练数据中是否包含某个具体的成员数据 的方式窃取训练数据中的隐私信息。



##### 1.1 数据窃取攻击(Data Extraction Attack). 

[Fredrikson M, Lantz E, Jha S, et al. Privacy in pharmacogenetics: An end-to-end case study of personalized warfarin dosing[C]. 23rd {USENIX} Security Symposium ({USENIX} Security 14), 2014: 17-32]通过分析药物推荐系统中人口统计信息和推荐药物的输出结果之间的相关性，可以逆向推出病患的遗传信息。

[Fredrikson M, Jha S, Ristenpart T. Model inversion attacks that exploit confidence information and basic countermeasures[C]. Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security, 2015: 1322-1333.]发现攻击者利用机器学习模型的预测结果可以重建模型训练时使用的人脸数据。

[Song C, Ristenpart T, Shmatikov V. Machine learning models that remember too much[C]. Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security, 2017: 587-601]发现攻击者通过在训练阶段，将训练数据编码到模型参数中，然后在预测阶段对参数进行解码来窃取训练数据。

[Shokri R, Shmatikov V. Privacy-preserving deep learning[C]. Proceedings of the 22nd ACM SIGSAC conference on computer and communications security, 2015: 1310-1321.]提出了协作式深度学习(Collaborative Deep Learning)模型，每个参与者通过本地训练和定期更新交换参数来构建联合模型，以保护各自数据的隐私。（这篇文章的方案实际上加入的噪声很小，完全不算什么保护）

[Hitaj B, Ateniese G, Pérez-Cruz F. **Deep models under the GAN: information leakage from collaborative deep learning**[C]. Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security, 2017: 603-618.]发现任何隐私保护的协作深度学习其实并没有真正地保护用于训练的人脸数据，应用于模型共享参数的记录层面(Record-level)上的差分隐私机制对于作者提出的基于GAN的攻击是无效的。

[Salem A, Bhattacharya A, Backes M, et al. Updates-Leak: Data Set Inference and Reconstruction Attacks in Online Learning[J]. arXiv preprint arXiv:1904.01067, 2019.]在Online Learning场景下，提出基于GAN的混合生成网络(BM-GAN)，利用模型在更新前后针对同样样本预测结果的变化来窃取用于更新模型的训练数据信息。(各种encoder和decoder，可以跑一下实验了解一下)



##### 1.2 属性推断攻击(Property Inference Attack).

窃取训练数据的隐私属性。

172[Ateniese G, Felici G, Mancini L V, et al. Hacking smart machines with smarter ones: How to extract meaningful data from machine learning classifiers[J]. arXiv preprint arXiv:1306.4447, 2013] 首次􏰀出了基于元分类器(Meta-classifier)的属性推断攻击并且证明仅􏰀供**记录级隐私的差分隐私机制无法有效地防御属性推断攻击**。然而，尽管该属性推断攻击方法针对隐马尔可夫模型(HMM)和支持向量机 (SVM)有很强的攻击效果，但由于深度神经网络模型的复杂性使得训练元分类器变得困难，导致严重地削弱了 该攻击在深度神经网络上的攻击效果。

173[Ganju K, Wang Q, Yang W, et al. Property inference attacks on fully connected neural networks using permutation invariant representations[C]. Proceedings of the 2018 ACM SIGSAC Conference on Computer and Communications Security, 2018: 619-633] 为了解决深度神经网络上攻击效果不佳的问题，提出了新的针对全连接神经网络 (FCNNs)的属性推断攻击方法,简化了元分类器的训练过程。

174[Melis L, Song C, De Cristofaro E, et al. Exploiting unintended feature leakage in collaborative learning[C], 2019] 发现在协同式深度学习模式下，针对训练数据子集的属性推断攻击仍然能够成功。



##### 1.3 成员推断攻击(Membership Inference Attack).

利用模型的预测结果来推断模型训练数据中是否包含某个训练样本。

176[Shokri R, Stronati M, Song C, et al. Membership inference attacks against machine learning models[C]. 2017 IEEE Symposium on Security and Privacy (SP), 2017: 3-18.] 首先利用训练数据和目标模型返回的预测概率向量及标签**训练**一个与目标模型架构相似的**影子模型**(Shadow Model)，以得到某条数据是否属于影子模型训练集的标签；然后将这些数据输入目标模型，利用模型预测接口返回的预测类别、置信度以及该数据是否在训练集中的二值标签训练一个分类模型；最后，给定一条待推断数据，通过将目标模型针对该数据返回的预测概率和标签输入到训练所得分类模型来判断该数据是否属于目标模型的训练数据集。

然而，这种攻击基于的假设条件较强(如攻击者必须了解目标模型结构、拥有与目标模型训练数据分布相同的数据集等)，因此攻击实施的成本较高。177[Salem A, Zhang Y, Humbert M, et al. Ml-leaks: Model and data independent membership inference attacks and defenses on machine learning models[J]. arXiv preprint arXiv:1806.01246, 2018.] 放宽了这些关键假设，并且证明改进后的攻击方法能显著地减低攻击成本。



#### 2. 模型萃取

由于机器学习模型通常是由一系列参数决定的，因此通过求解模型参数就可以实现模型萃取。

2[]发现攻击者理论上只需要通过预测借口进行$n+1$次查询就能窃取到输入为$n$维的线性模型。

178[Oh S J, Augustin M, Schiele B, et al. Towards reverse-engineering black-box neural networks[J]. arXiv preprint arXiv:1711.01768, 2017.]表明攻击者可以从一系列的查询结果中逆向􏰀取得到诸如训练数据、模型架构以及优化过程等神经网络的内部信息，而这些暴露的内部信息将有助于攻击者生成针对黑盒模型的更有效的对抗样例，从而显著􏰀高黑盒对抗攻击方法的攻击效果。

179[Wang B, Gong N Z. Stealing hyperparameters in machine learning[C]. 2018 IEEE Symposium on Security and Privacy (SP), 2018: 36-52.]􏰀出了超参数窃取攻击(Hyperparameter Stealing Attacks)，研究结果证明该攻击适用于诸如岭回归、逻辑回归、支持向量机以及神经网络等各种流行的机器学习算法。



#### 3. 隐私保护方法

##### 3.1 基于差分隐私的数据隐私保护

差分隐私将隐私定义为添加或移除输入数据中的任何一条记录不会显著影响算法输出结果的一种属性。为了提供任何有意义的差分隐私保护，必须随机化机器学习系统的部分管线，**这种随机化过程既可以在训练阶段完成，也可以在模型推理阶段通过随机化选择模型预测结果来实现**。

* **训练阶段的DP.** 典型方法是数据满足局部差分隐私(LDP)[181Kairouz P, Oh S, Viswanath P. **Extremal mechanisms for local differential privacy**[C]. Advances in neural information processing systems, 2014: 2879-2887]。

  182[Erlingsson Ú, Pihur V, Korolova A. Rappor: Randomized aggregatable privacy-preserving ordinal response[C]. Proceedings of the 2014 ACM SIGSAC conference on computer and communications security, 2014: 1054-1067.]提出了RAPPOR，允许浏览器的开发人员在满足隐私前􏰀下收集并使用来自浏览器用户的有意义的统计数据。具体地，RAPPOR机制在用户将数据发送到用于收集数据以训练模型的集中式服务器时，采用随机响应来保护用户隐私，即用户在响应服务器查询时以 q 的概率返回真实答案或以 1-q 的概率返回随机值。

  183[Liu C, Mittal P. LinkMirage: Enabling Privacy-preserving Analytics on Social Relationships[C]. NDSS, 2016.]􏰀出了一种保护用户社交网络隐私信息的方法 LinkMirage，该方法通过模糊社交网络的拓扑结构，从而允许不受信任的外部应用程序能够收集有意义的、具有隐私保护的用户社交网络信息以用于模型训练。

  其他则通过在训练过程中向损失函数[184 Chaudhuri K, Monteleoni C, Sarwate A D. Differentially private empirical risk minimization[J]. Journal of Machine Learning Research, 2011, 12(Mar): 1069-1109.]、梯度[185 Abadi M, Chu A, Goodfellow I, et al. Deep learning with differential privacy[C]. Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security, 2016: 308-318.]、参数值[169 Shokri R, Shmatikov V. Privacy-preserving deep learning[C]. Proceedings of the 22nd ACM SIGSAC conference on computer and communications security, 2015: 1310-1321.]添加随机噪声的方式来保证$\varepsilon$-DP。

* **预测阶段的DP.** 通过随机化模型预测行为的方式，提供DP保证。然而，随着查询次数的增加，引入的噪声量也随之增长，导致模型预测的准确性降低。

  为克服这一缺陷，[186 Papernot N, Abadi M, Erlingsson U, et al. Semi-supervised knowledge transfer for deep learning from private training data[J]. arXiv preprint arXiv:1610.05755, 2016.]设计了一种保护数据隐私的通用型框架——PATE (Private Aggregation of Teacher Ensembles)，它不仅能够提供正式的差分隐私保障，也􏰀供一定的直观隐私(Intuitive Privacy)保障。具体地，该框架先将训练数据划分成 N 个不相交的子集，然后用这些子集分别训练不同的模型，得到 N 个独立的教师模型，最后在预测阶段通过统计每个教师模型的预测结果并选取票数最高的结果将预测结果聚合起来。如果大部分教师模型都同意某一个预测结果，那么就意味着它**不依赖于具体的分散数据集**，所以隐私成本很小；但如果有两类预测结果有相近的票数，那么**这种不一致或许会泄露隐私信息**。因此,作者在统计票数时引入了拉普拉斯噪声，把票数的统计情况打乱，从而保护隐私。事实上，每次查询聚合教师模型时都会增加隐私成本，因为它每次给出的结果或多或少都会透露一些隐私信息。因此，作者利用聚合教师模型以隐私保护的方式对未标记的公共数据进行标注，然后用标记好的数据训练学生模型，最终将学生模型部署到用户设备上。**这种做法可以防范攻击者窃取隐私训练数据，因为在最坏情况下攻击者也只能得到学生模型的训练数据，即带有隐私保护标注信息的公开数据**。

* **防御成员推断攻击.** 

  [177 ]认为成员推断攻击之所以能够成功，原因之一在于机器学习模型在训练过程中普遍存在过拟合现象。基于这一认知，作者􏰀出了利用随机失活(Dropout)和模型集成(Model Stacking) 的方法来防御成员推断攻击。

  [187 Nasr M, Shokri R, Houmansadr A. Machine learning with membership privacy using adversarial regularization[C]. Proceedings of the 2018 ACM SIGSAC Conference on Computer and Communications Security, 2018: 634-646.]引入了一种隐私机制来训练机器学习模型并将其形式化为最小--最大博弈优化问题，利用对抗性训练算法使模型的分类损失和成员关系推理攻击的最大增益最小化，以使攻击者无法区分最终训练所得模型对其训练数据以及对同一分布中其他数据点的预测结果。

  [188 Hagestedt I, Zhang Y, Humbert M, et al. MBeacon: Privacy-Preserving Beacons for DNA Methylation Data[C]. Proceedings of the 2019 Network and Distributed System Security Symposium (NDSS). Internet Society, 2019.]􏰀提出了 一种新的差分隐私机制 SVT2，能够显著降低 DNA 甲基化(DNA Methylation)等生物医学数据的成员隐私风险。



##### 3.2 基于密码学的模型隐私保护

在机器学习领域，同态加密、安全多方计算等技术也被广泛应用于保护机器学习模型的安全与隐私。

[189 Gilad-Bachrach R, Dowlin N, Laine K, et al. Cryptonets: Applying neural networks to encrypted data with high throughput and accuracy[C]. International Conference on Machine Learning, 2016: 201-210]将同态加密技术引入到神经网络中，以允许神经网络在不解密数据的情况下直接处理加密数据。由于同态加密技术将给机器学习模型的体系结构设计引入额外的约束。因此该方法受限于同态加密的性能开销以及所支持的有限算术运算集。

为解决这一问题，[190 Liu J, Juuti M, Lu Y, et al. Oblivious neural network predictions via minionn transformations[C]. Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security, 2017: 619-631.]为神经网络中诸如线性转换、激活函数和池化等常用操作设计了不经意(Oblivious)协议，并结合乱码电路、同态加密等密码学相关理论􏰀出了MiniONN，这种方法可以在不需要改变模型训练方式的情况下将普通神经网络转换为不经意神经网络(Oblivious Neural Networks)以支持保护隐私的模型预测。

此外，安全多方计算应用于协同式机器学习框架中(比如岭回归[191 Nikolaenko V, Weinsberg U, Ioannidis S, et al. Privacy-preserving ridge regression on hundreds of millions of records[C]. 2013 IEEE Symposium on Security and Privacy, 2013: 334-348.]、线性回归[192 Gascón A, Schoppmann P, Balle B, et al. **Privacy-preserving distributed linear regression on high-dimensional data**[J]. Proceedings on Privacy Enhancing Technologies, 2017, 2017(4): 345-364.])。

[193 Bonawitz K, Ivanov V, Kreuter B, et al. Practical secure aggregation for privacy-preserving machine learning[C]. Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security, 2017: 1175-1191.]􏰀出了一种**移动应用场景**下的数据聚合安全协议，该协议利用安全多方计算的方式计算自各个用户设备的模型参数更新总和，以确保客户端设备的输入仅由服务器进行聚合学习。该协议不仅开销低，而且还可以容忍大量的设备故障，因此是移动应用的理想选择。

[194 Mohassel P, Zhang Y. Secureml: A system for scalable privacy-preserving machine learning[C]. 2017 IEEE Symposium on Security and Privacy (SP), 2017: 19-38.]􏰀出了一种基于安全多方计算的、适用于线性回归、逻辑回归和神经网络的模型训练保密协议，**该协议大幅度提升了已有最先进的解决方案效率。**







