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

<!--more-->

`#systemProp.socks.proxyHost=127.0.0.1 #systemProp.socks.proxyPort=1086 #systemProp.https.proxyHost=127.0.0.1 #systemProp.https.proxyPort=1086 #systemProp.https.proxyHost=socks5://127.0.0.1 #systemProp.https.proxyPort=1086 `

正确设置方法应该是这样： 

`org.gradle.jvmargs=-DsocksProxyHost=127.0.0.1 -DsocksProxyPort=7077 `

修改 $HOME/.gradle/gradle.properties 文件,加入上面那句，这样就可以全局开启 gradle 代理。

顺带记录一下后续遇到的问题，升级AS到3.5.1，手机是API28的版本，原先的程序会遇到闪退问题，查到说需要迁移到Android X上。

1. 采用最低4.6的gradle-all.zip

2. 去掉AndroidMainfest中的最低版本“android:minSdkVersion=xxx”

3. Annotation processors must be explicitly declared now. butterknife-7.0.1.jar

   `annotationProcessor 'com.jakewharton:butterknife:7.0.1'`

   https://developer.android.com/studio/build/dependencies?utm_source=android-studio#annotation_processor

4. 错误: 找不到符号
   符号:   变量 MATRIX_SAVE_FLAG
   位置: 类 Canvas

   解决办法：直接调`canvas.save();`
   google在android P中删除了`canvas.save(int);`方法

5. java.lang.NoClassDefFoundError: Failed resolution of: Lorg/apache/http/params/BasicHttpParams;

   https://developers.google.com/maps/documentation/android-sdk/config#specify_requirement_for_apache_http_legacy_library

   ```
   <uses-library
         android:name="org.apache.http.legacy"
         android:required="false" />
   ```

6. Andorid API 28 (android 9.0)后不能加载http的url，报错net : err_cleartext_not_permitted

   在manifest 中application节点添加

   ```xml
   android:usesCleartextTraffic="true"
   ```

7. Fragment not attached to a context错误导致通过getResources().getString()获取字符串的错误

   