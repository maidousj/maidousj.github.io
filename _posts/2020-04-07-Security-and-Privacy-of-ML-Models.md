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

1. 训练数据窃取

   通过获取训练数据的大致分布 或者 根据模型的预测结果推断训练数据中是否包含某个具体的成员数据 的方式窃取训练数据中的隐私信息。

   1.1 数据窃取攻击(Data Extraction Attack). 

   [Fredrikson M, Lantz E, Jha S, et al. Privacy in pharmacogenetics: An end-to-end case study of personalized warfarin dosing[C]. 23rd {USENIX} Security Symposium ({USENIX} Security 14), 2014: 17-32]通过分析药物推荐系统中人口统计信息和推荐药物的输出结果之间的相关性，可以逆向推出病患的遗传信息。

   [Fredrikson M, Jha S, Ristenpart T. Model inversion attacks that exploit confidence information and basic countermeasures[C]. Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security, 2015: 1322-1333.]发现攻击者利用机器学习模型的预测结果可以重建模型训练时使用的人脸数据。

   [Song C, Ristenpart T, Shmatikov V. Machine learning models that remember too much[C]. Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security, 2017: 587-601]发现攻击者通过在训练阶段，将训练数据编码到模型参数中，然后在预测阶段对参数进行解码来窃取训练数据。

   [Shokri R, Shmatikov V. Privacy-preserving deep learning[C]. Proceedings of the 22nd ACM SIGSAC conference on computer and communications security, 2015: 1310-1321.]提出了协作式深度学习(Collaborative Deep Learning)模型，每个参与者通过本地训练和定期更新交换参数来构建联合模型，以保护各自数据的隐私。（这篇文章的方案实际上加入的噪声很小，完全不算什么保护）
   
   [Hitaj B, Ateniese G, Pérez-Cruz F. **Deep models under the GAN: information leakage from collaborative deep learning**[C]. Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security, 2017: 603-618.]发现任何隐私保护的协作深度学习其实并没有真正地保护用于训练的人脸数据，应用于模型共享参数的记录层面(Record-level)上的差分隐私机制对于作者提出的基于GAN的攻击是无效的。
   
   [Salem A, Bhattacharya A, Backes M, et al. Updates-Leak: Data Set Inference and Reconstruction Attacks in Online Learning[J]. arXiv preprint arXiv:1904.01067, 2019.]在Online Learning场景下，提出基于GAN的混合生成网络(BM-GAN)，利用模型在更新前后针对同样样本预测结果的变化来窃取用于更新模型的训练数据信息。(各种encoder和decoder，可以跑一下实验了解一下)
   
   1.2 属性推断攻击(Property Inference Attack).
   
   窃取训练数据的隐私属性。

