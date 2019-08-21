---
title: TS for learning in online decision making notes
layout: post
date: 2019-08-19 15:10
image: /assets/images/
headerImage: false
category: blog
tag:
- Multi-armed Bandit
- Thompson Sampling
author: Sun
---

> https://www.youtube.com/watch?v=o6HBIGzQfJs
>
> youtube看到的视频，底下有个评论说讲的清楚，记一些有用的结论留存。

![](/assets/images/2019-08-19-TS-for-learning/image-20190819153456044.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819164113355.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819164257356.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819164723254.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819165336226.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819170427790.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819174515090.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819181353599.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819181244874.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190819181801446.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820095824548.png) 

![](/assets/images/2019-08-19-TS-for-learning/image-20190820100517116.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820102506039.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820103059444.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820103913501.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820105747868.png)

这种情况下，arm对应的reward不再是固定的，取决于在时刻t，arm $i$所面对的context，也就是$x_{i,t}$

![](/assets/images/2019-08-19-TS-for-learning/image-20190820111048606.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820124429465.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820124528540.png)

结果不依赖于arm的个数。$d$是$\theta$的维度。只假设了分布是bounded或者sub-Gaussian noise（这个是什么意思？）

![](/assets/images/2019-08-19-TS-for-learning/image-20190820135651783.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820135720500.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820143903339.png)

用Dirichlet分布作为后验分布，有n个参数，如果有某个状态发生变化，就把相应的参数增加。

![](/assets/images/2019-08-19-TS-for-learning/image-20190820144808757.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820145151327.png)

![](/assets/images/2019-08-19-TS-for-learning/image-20190820145534993.png)

