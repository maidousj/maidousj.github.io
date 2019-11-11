---
title: Android海外版发布问题
layout: post
date: 2019-11-11 18:27
image: /assets/images/
headerImage: false
category: Blog
tag:
- Android
- Google Play
- Deploy
author: Sun
---

Google要求海外版上线在19/8/1后需要支持64位版本的。以前的代码问题不大，用新的AS编译就好，但是加入的动态链接库(*.so)可能就需要找64位版本了。

<!--more-->

参考：

[Android jniLibs下目录详解（.so文件）](https://www.jianshu.com/p/b758e36ae9b5)

[ANDROID动态加载 使用SO库时要注意的一些问题](https://segmentfault.com/a/1190000005646078)

