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

本文采用了混合生成模型(BM-GAN)，它是基于GAN的，但是包含了一个可以生成准确sample的重构损失(reconstructive loss)。实验表明可以有效地预测数据集特征，甚至是chanllenging conditions下的完整重构。

<!--more-->

