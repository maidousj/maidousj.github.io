---
title: Updates-Leak Data Set Inference and Reconstruction Attacks in Online Learning notes
layout: post
date: 2019-11-25 21:28
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- Online Learning
- Dataset Reconstruction
- Attack
author: Sun
---

USENIX Security 2020.

### Abstract

本文研究了对于黑盒的ML模型的输出在更新前后的更改是否会泄漏用于执行更新的数据的信息。这引出了一种针对黑盒模型的新攻击，这种信息的泄漏会严重损害ML模型拥有者/提供者的intellectual property和数据隐私。和membership推断攻击相比，本文采用了encoder/decoder formulation，可以推断从**详细的特征**到**数据集的完整重构**。

本文采用了混合生成模型(BM-GAN)，它是基于GAN的，但是包含了一个可以生成准确sample的重构损失(reconstructive loss)。实验表明可以有效地预测数据集特征，甚至是challenging conditions下的完整重构。

<!--more-->

### Introduction

主要研究问题：大概是说，在线学习中，模型是增量更新的，这一过程中，某个数据集被用来训练前和训练后，对同样的sample会产生不同的输出，本文研究这个不同的输出，会不会泄漏被用来更新模型的数据集的信息。

针对黑盒模型，提出了4种不同的攻击，可以被分为两类：*single-sample attack*和*multi-sample attack*。

四种攻击中，有两种旨在重构updating set(每类一种)。理论上，membership推断可以被用来重构黑盒模型的数据集，但是，**membership推断并不适用扩展于真实世界中的，因为敌手需要收集大量数据样本，而该样本恰好包含目标模型的所有训练集样本**。

**General Attack Construction.** 本文的四种攻击都基于通用的结构，可以概括为encoder-decoder style。encoder是由多层感知机(MLP)以不同的目标模型的输出(称作*posterior difference*)为输入，而decoder针对不同的攻击产生有关更新集的不同类型的信息。

为了获取到posterior difference，随机选择了固定的数据样本，称为探测集合(*probing set*)，用来探测不同版本的目标模型。然后，计算两次posterior集合的不同，作为四种攻击encoder的输入。

**Single-sample Attack Class.** 包含两种攻击: single-sample label inference attack和single-sample reconstruction attack。

前者用来预测单个样本的标签，对应的decoder由一个两层感知机实现。

后者是对更新数据集的重构。首先通过不同的数据集合训练一个autoencoder(AE)，然后将AE的decoder转移到本文的攻击模型中作为样本重构器。

**Multi-sample Attack Class.** 也包含两种攻击：multi-sample label distribution estimation attack和multi-sample reconstruction attack。

前者估计updating set的标签分布，decoder用多层感知机实现，拥有一个全连接层和一个softmax层。用KL散度作为模型的损失函数。

后者用来生成updating set的所有数据集。decoder由两部分组成，第一部分用来学习数据的分布，用BM-GAN实现，它引入了一个"Best Match"损失来确保每个样本都被重构了。第二部分decoder依赖于机器学习中的聚类，将BM-GAN生成的数据聚类，用中心节点作为重构的样本。

实验结果都贼吊！



### Conclusion

目前只针对了online learning场景。





