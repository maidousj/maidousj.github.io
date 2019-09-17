---
title: The Central Limit Theorem in Differential Privacy (Skimming)
layout: post
date: 2019-09-17 09:55
image: /assets/images/
headerImage: false
category: Paper Reading
tag:
- DP
- zCDP
- RDP
author: Sun
---

Sommer D M, Meiser S, Mohammadi E. Privacy loss classes: The central limit theorem in differential privacy[J]. Proceedings on Privacy Enhancing Technologies, 2019, 2019(2): 245-269.

量化隐私保护机制中的privacy loss是一个复杂的问题。本文通过利用机制的隐私损失分布(privacy loss distribution, PLD)统一了之前的工作。研究表明，对于非适应性(non-adaptive)的机制，顺序组合下的隐私损失经过卷积并将收敛到高斯分布(DP的中央极限定理)。本文还得出了几个相关的见解：可以通过他们的隐私损失类来(privacy loss class)表征机制，即通过他们的PLD收敛到高斯分布来表征机制，这样可以基于他们的隐私损失类给出机制的新的ADP(approximate DP)界限; 我们得到了近似随机响应机制的精确分析保证和高斯机制的精确解析和闭合公式，也就是，给定$\varepsilon$，计算$\delta$，使得，机制是$(\varepsilon,\delta)$-ADP（不是过度近似界）。

<!--more-->

最近的结果表明，更好的拟合最坏情况分布可以导致组合性质下的明显更严格的界限。











