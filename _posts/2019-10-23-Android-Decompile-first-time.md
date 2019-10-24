---
title: 第一次Android反编译记录
layout: post
date: 2019-10-23 13:35
image: /assets/images/
headerImage: false
category: Blog
tag:
- Android
- Decompile
author: Sun
---

1. 下载[apktool](https://ibotpeaches.github.io/Apktool/install/)、[dex2jar](https://sourceforge.net/projects/dex2jar/files/)、[jd-gui](https://github.com/java-decompiler/jd-gui)三个工具

   apktool按照官网提示，重命名和apktool.jar一起放到/usr/local/bin目录下

   dex2jar直接解压即可

<!--more-->

2. 开始反编译

   2.1 apktool对需要反编译的apk文件进行反编译

   ```shell
   apktool d xxx.apk
   ```

   反编译后apk中的xml文件即可查看。

   

   2.2 dex2jar进行class.dex的反编译

   首先把xxx.apk改成xxx.rar然后直接解压，解压后可以看到class.dex class2.dex等文件。

   把这几个dex文件放入dex2jar解压后的目录中，执行

   ```shell
   sh d2j-dex2jar.sh classes.dex 
   ```

   这个过程中在mac上可能遇到错误：

   ```shell
   d2j-dex2jar.sh: line 36: ./d2j_invoke.sh: Permission denied
   ```

   原因是d2j_invoke.sh没有执行权限，执行如下命令可解决：

   ```shell
   chmod +x d2j_invoke.sh
   ```

   d2j-dex2jar.sh执行完后可以得到classes-dex2jar.jar文件。

3. 使用jd-gui工具打开这个jar包就可以看到java源代码了。