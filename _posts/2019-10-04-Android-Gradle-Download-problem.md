---
title: Android Gradle Download problem
layout: post
date: 2019-10-04 21:35
image: /assets/images/
headerImage: false
category: Blog
tag:
- Android
- Gradle
author: Sun
---

之前一直没搞定的，编译android时总是卡在gradle.pom文件的下载上，直接用地址下是没有问题的 ，但是Android Studio里一直卡在这里。终于找到一种靠谱的解决方案，来自[知乎](https://www.zhihu.com/question/37810416/answer/82464203)，记录一下。

`#systemProp.socks.proxyHost=127.0.0.1 #systemProp.socks.proxyPort=1086 #systemProp.https.proxyHost=127.0.0.1 #systemProp.https.proxyPort=1086 #systemProp.https.proxyHost=socks5://127.0.0.1 #systemProp.https.proxyPort=1086 `

正确设置方法应该是这样： 

`org.gradle.jvmargs=-DsocksProxyHost=127.0.0.1 -DsocksProxyPort=7077 `

修改 $HOME/.gradle/gradle.properties 文件,加入上面那句，这样就可以全局开启 gradle 代理

