---
title: iOS problem
layout: post
date: 2019-11-05 15:39
image: /assets/images/
headerImage: false
category: Blog
tag:
- Pod
- iOS
author: Sun
---

记录项目中遇到的一些问题。iOS纯新手。

<!--more-->

### 项目中的电话输入框前加country code picker

先尝试项目https://github.com/Dwarven/PhoneCountryCodePicker.git

打开demo编译后发现有两个文件无法打开：

```shell
/PhoneCountryCodePicker/PCCPDemo/PCCPDemo.xcodeproj The file “Pods-PCCPDemo.release.xcconfig” couldn’t be opened because there is no such file. (/PhoneCountryCodePicker/PCCPDemo/Pods/Target Support Files/Pods-PCCPDemo/Pods-PCCPDemo.release.xcconfig)
```



![](/assets/images/2019-11-05-iOS-overseas-problem/image-20191105154757188.png){:width="400"}

解决方案：

先安个pods试试，pods可以简单理解为iOS的依赖管理器吧，类似于Java中的Maven。

```shell
sudo gem install cocoapods
```

然后进入project所在目录，有podfile文件，执行

```shell
pod install
```

报错

```shell
Adding spec repo `trunk` with CDN `https://cdn.cocoapods.org/`
[!] CDN: trunk Repo update failed - 5 error(s):
CDN: trunk URL couldn't be downloaded: https://raw.githubusercontent.com/CocoaPods/Specs/master/Specs/d/3/5/Phone-Country-Code-and-Flags/0.1.0/Phone-Country-Code-and-Flags.podspec.json, error: Failed to open TCP connection to raw.githubusercontent.com:443 (Connection refused - connect(2) for "raw.githubusercontent.com" port 443)
```

肉眼可见是网络问题，将raw.githubusercontent.com添加到梯子的手动规则中，请求复制到浏览器可以拿到json文件，但是在terminal中依然超时。接着报错：

```shell
[!] CDN: trunk Repo update failed - 5 error(s):
CDN: trunk URL couldn't be downloaded: https://raw.githubusercontent.com/CocoaPods/Specs/master/Specs/d/3/5/Phone-Country-Code-and-Flags/0.1.0/Phone-Country-Code-and-Flags.podspec.json, error: execution expired
```





### 国际化

参考[3分钟实现iOS语言本地化/国际化（图文详解）](https://www.jianshu.com/p/88c1b65e3ddb). 简单记一下。

1. 应用名国际化

* 在Project的设置中通过点击"+"添加需要本地化的语言。

* 在Xcode右侧的File inspection中点击Localize，选中需要本地化App名称的语言。

* 在每个语言对应的文件中以key = value(CFBundleDisplayName = "App名称";);的形式设置App的名称。

2. 代码中字符串的本地化

   和1类似。

3. 图片的本地化

   用了参考中的第一种方法：

   ```objective-c
   NSString *imageName = NSLocalizedString(@"icon", nil);
   UIImage *image = [UIImage imageNamed:imageName];
   self.imageView.image = image;
   ```

   但是把英文版图片直接拖入Images.xcassets相应的imageset文件夹时遇到警告：

   ```
   The image set "xxx" has an unassigned child
   ```

   

4. 设置为固定语言，不跟随系统变化

   参考[iOS开发——iOS国际化 APP内语言切换](https://juejin.im/post/5aa69e9c6fb9a028e52d7e23)。







