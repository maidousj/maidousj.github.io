---
title: Unknown typne name 'tls_protocol_version_t' 
layout: post
date: 2020-07-27 16:28
image: /assets/images/
headerImage: false
category: Blog
tag:
- iOS
author: Sun
---

iOS app提交时不支持旧版本的xcode，为了升级xcode，被迫升级了mac OS 10.15.6。

怕什么来什么，果然写好的代码编译出了问题。纯记录当前工程是怎么解决的，不深究原因。

####Unkown type name 'tls_protocol_version_t'

Google半天，最靠谱的是https://www.jianshu.com/p/5abbcf9601bd。

按照他的说法，是引入security.framework时出现了问题。检查了一下，果然security.framework是工程目录下的，并没有tls_protocol_version_t所需要的<Security/SecProtocolTypes.h>这个头文件。

于是在target->General->Framewroks, Libraries and Embedded Content下删掉security.framework。

在Build Phases->Embedded Frameworks下加入系统自带(iOS 13.6)的security.framework。

重新编译后，Unkown type name 'tls_protocol_version_t'，Could not build module 'xxx'问题没有了。



新问题是

#### Library not found for -lstdc++.6.0.9

参考：https://www.codenong.com/cs105358811/ 

(想起来了，上次升级了xcode好像也遇到了这个问题，这种旧的依赖其实应该换掉，但为了节省时间，先找旧的拷贝至相应位置)

在以下路径拷贝libstdc++.6.0.9.tbd文件：

> /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/usr/lib
>
> /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneOS.sdk/usr/lib

将libstdc++.6.0.9.dylib，libstdc++.6.dylib，libstdc++.dylib文件拷贝到以下路径：

> /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Library/Developer/CoreSimulator/Profiles/Runtimes/iOS.simruntime/Contents/Resources/RuntimeRoot/usr/lib

文件获取链接直接用参考给出的：https://pan.baidu.com/s/1evpM29cusH5KwWecwE1I8g 密码:r445



####UIKit.framework: bundle format unrecognized, invalid, or unsuitable Command CodeSign failed with a nonzero exit code

把报错的相应地framework从Build Phases的embedded framework中去掉。



好不容易编译通过了，结果安不到手机了。。

####Unable to install "xxx"

Domain: com.apple.dt.MobileDeviceErrorDomain

Code: -402653103