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

`org.gradle.jvmargs=-DsocksProxyHost=127.0.0.1 -DsocksProxyPort=1086 `

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

  解决方案：我们的代码里，基类的fragment是在onCreate()方法中初始化对话框时候通过getActivity()获取到了context，所以子类中之要在super.onCreate()方法之后调用getResources()就没有问题了。之所以报错是由于，有几个变量的初始化写在了类中，这样这些变量的初始化会先于onCreate()方法被执行，此时如果想通过getResources()来获取context是会造成空指针异常的。
  
  解决的思想就是，调用getResources()之前，保证context已经可以获取到就可以了，当然更好的习惯是加上try catch，这样即使空指针也不会引起app闪退。

-----------------------

 以下是因为有个按钮变的贼丑，所以用旧版本的AS 3.0.1打开试试遇到的问题。

1. Error:No such property: GradleVersion for class: JetGradlePlugin

   gradle版本不匹配的原因。由于3.5.1的AS编译出原app的按钮有变化，所以降级用3.0.1的AS试一下，结果报了这个错。把gradle-wrapper中的distributionUrl修改一下：

   `Error:No such property: GradleVersion for class: JetGradlePlugin`

2. 报错：gradle ---> read time out

   查到说修改jdk，使用系统jdk，别用AS自带的。查看jdk路径方法：

   `/usr/libexec/java_home -V`

   结果还是time out....

   应该还是网络的问题，下载xxx.pom时候超时了。

   后更：也可以说不是网络问题，因为我的网络可以下到，但是gradle3.2.0这个目录在jcenter里没有？？但是AS 3.5.1可以顺利编译啊。。没办法，把gradle换成了2.3.2(和旧版本的一样)

   **终于找到原因了：**gradle那个配置。。在项目的gradle.properties文件中，弹出代理设置对话框时候手贱选了https，所以应该是global的gradle.properties文件中的设置没有用了，所以无论是换成google还是aliyun的源都超时。另外，**jcenter没有gradle3.2.0了**。

3. 又报错：Failed to solve 什么什么的. 

   ```
   targetSdkVersion 换成了26 原先是28
   ```

4. 依然是AS 3.0.1，原先的app编译后闪退，于是按照先前用3.5.1闪退时候的步骤，API改成了28（因为手机是API 28的），然后之前的错都没了，app闪退。。。

   报错Unable to instantiate appComponentFactory                                                           java.lang.ClassNotFoundException: Didn't find class "android.support.v4.app.CoreComponentFactory"

5. 不是API的原因，gradle换成了和旧版本一样的4.1, targetAPI什么的也都还原了，用3.5.1编译没问题了。

----------

**终于找到按钮出问题的原因了！！！**

最开始用新的android studio 3.5.1编译的时候，按钮那个代码里报错了，我查了下就注释掉换了一种写法，这基本上是最先修改的错了，早就忘了，然后我改回原先到写法，发现不报错了。（当然可能是gradle版本的问题，已经全改的和旧的一样了，所以没报错）。build.gradle也是和旧的一样了。贴出那个代码，单打开文件依然是红的。

![](/assets/images/2019-10-04-dd-problem/image-20191012160603840.png)

但是！用AS 3.0.1编译同样的代码，依然闪退！还是奇葩的！（当然，大概率原因还是在自己。。好歹新环境可以用了，所以先不管了）

### 经验

以后换新的IDE，编译报错，先找版本原因，从gradle版本，API版本等，实在不是版本原因再改代码。。。。





-----------------

10.23更新

为了彻底杜绝像锤子手机那种奇葩，决定把countrypicker库的源文件拿来作为子项目添加进去，然后把string.xml中的汉语彻底替换掉（最土的做法。。）

这样为了把countrypicker工程加入到现有的工程中，把countrypicker的代码先拷贝到原工程中。然后countrypicker的build文件中有“api 'io.michaelrocks:libphonenumber-android:8.10.16'”，估计是为了解决手机号格式的库。这玩意报错：

```java
Could not find method api() for arguments [io.michaelrocks:libphonenumber-android:8.10.16] on object of type org.gradle.api.internal.artifacts.dsl.dependencies.DefaultDependencyHandler.
```

额。。gradle版本太低的过，以前是2.3.2，换成了3.2.0.



