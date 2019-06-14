---
title: R语言安装
layout: post
date: 2017-07-01 10:49
image: /assets/images/
headerImage: false
category: blog
tag:
- R
- Software install
author: Sun
---

### Summary

略微低端，只是记录 ubuntu14.04环境下的

 [R语言](https://zh.wikipedia.org/wiki/R语言)一种自由软件编程语言与操作环境，主要用于统计分析、绘图、数据挖掘。R本来是由来自新西兰奥克兰大学的罗斯·伊哈卡和罗伯特·杰特曼开发（也因此称为R），现在由“R开发核心团队”负责开发。R基于S语言的一个GNU计划项目，所以也可以当作S语言的一种实现，通常用S语言编写的代码都可以不作修改的在R环境下运行。R的语法是来自Scheme。


#### Install

在"/etc/apt/source.list"中添加

```shell
deb https://cloud.r-project.org/bin/linux/ubuntu trusty
```

执行

```Shell
$ sudo apt-get update
```

遇到错误

```shell
W: GPG error: https://cloud.r-project.org trusty/ Release: The following signatures could not be verified because the public key is not available: NO_PUBKEY 51716619E084DAB9
```

执行命令

```shell
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9
```

安装完备的 R 系统：

```shell
$ sudo apt-get install r-base
```

