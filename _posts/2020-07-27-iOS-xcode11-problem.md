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

#### Unkown type name 'tls_protocol_version_t'

Google半天，最靠谱的是https://www.jianshu.com/p/5abbcf9601bd。

按照他的说法，是引入security.framework时出现了问题。检查了一下，果然security.framework是工程目录下的，并没有tls_protocol_version_t所需要的<Security/SecProtocolTypes.h>这个头文件。

于是在target->General->Framewroks, Libraries and Embedded Content下删掉security.framework。

在Build Phases->Link Binary With Libraries下加入系统自带(iOS 13.6)的security.framework。

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



再放一个xcode 10的：https://github.com/CoderJYZhu/libstdc-/tree/master/libstdc%2B%2B



#### UIKit.framework: bundle format unrecognized, invalid, or unsuitable Command CodeSign failed with a nonzero exit code

把报错的相应地framework从Build Phases的embedded framework中去掉。（这个是我手贱，把target->General->Framewroks, Libraries and Embedded Content 的库都给改成了Embed&Sign，后来发现，把embedded framework中去掉以后，这里会变成"Do Not Embed"）



好不容易编译通过了，结果安不到手机了。。



#### Unable to install "xxx"

Domain: com.apple.dt.MobileDeviceErrorDomain

Code: -402653103

完整的错误是：

> Unable to install "***"
>
> Domain: com.apple.dt.MobileDeviceErrorDomain
>
> Code: -402653103
>
> \--
>
> Could not inspect the application package.
>
> Domain: com.apple.dt.MobileDeviceErrorDomain
>
> Code: -402653103
>
> User Info: {
>
>   DVTRadarComponentKey = 282703;
>
>   MobileDeviceErrorCode = "(0xE8000051)";
>
>   "com.apple.dtdevicekit.stacktrace" = (
>
> 0  DTDeviceKitBase           0x000000011dbd081a DTDKCreateNSErrorFromAMDErrorCode + 233
>
> 1  DTDeviceKitBase           0x000000011dc11f70 _*90-[DTDKMobileDeviceToken installApplicationBundleAtPath:withOptions:andError:withCallback:]*block*invoke + 155
>
> ​	2  DVTFoundation            0x00000001050b3f35 DVTInvokeWithStrongOwnership + 73
>
> ​	3  DTDeviceKitBase           0x000000011dc11ca8 -[DTDKMobileDeviceToken installApplicationBundleAtPath:withOptions:andError:withCallback:] + 1654
>
> ​	4  IDEiOSSupportCore          0x000000011da88e91* *118-[DVTiOSDevice(DVTiPhoneApplicationInstallation) processAppInstallSet:appUninstallSet:installOptions:completionBlock:]*block*invoke.352 + 4165
>
> ​	5  DVTFoundation            0x00000001051e75d4 DVT*
>
> CALLING*CLIENT*BLOCK
>
>  \+ 7
>
> 6  DVTFoundation            0x00000001051e9216 _*DVTDispatchAsync*block*invoke + 1194
>
> ​	7  libdispatch.dylib          0x00007fff675e66c4* dispatch*call*block*and*release + 12
>
> 8  libdispatch.dylib          0x00007fff675e7658 *dispatch*client*callout + 8
>
> ​	9  libdispatch.dylib          0x00007fff675ecc44* dispatch*lane*serial*drain + 597
>
> ​	10 libdispatch.dylib          0x00007fff675ed5d6* dispatch*lane*invoke + 363
>
> 11 libdispatch.dylib          0x00007fff675f6c09 *dispatch*workloop*worker*thread + 596
>
> 12 libsystem*pthread.dylib       0x00007fff67841a3d* pthread*wqthread + 290
>
> ​	13 libsystem*pthread.dylib       0x00007fff67840b77 start_wqthread + 15
>
> );
>
> }



这个问题查了半天，还在苹果开发者论坛发了下。后来有个别人的回答，从控制台看手机的相关输出是什么样的。

于是从控制台的手机输出上找了半天，忘了是什么了，然后改了下就能装到手机了。

但是会闪退。报的错是



#### dyld: Library not loaded: @rpath/libswiftCore.dylib

```swift
Reason: image not found 
```

这个问题找了有一周了。期间把上一版本的代码搞下来跑也不行。但是换了xcode10.3就可以了。

输出是和我用的开源库countrypickerview有关的，所以升级了这个库。

好像是升级了这个库然后可以安装了，但是一登录就闪退，而且页面变成了卡片式。

#### 卡片式改成全屏

这个问题就参考了[iOS 13 的 present modally 變成更方便的卡片設計!](https://medium.com/彼得潘的-swift-ios-app-開發問題解答集/ios-13-的-present-modally-變成更方便的卡片設計-fb6b31f0e20e)

想要改成全屏的只要修改相应controller view的Presentation属性。

![](https://miro.medium.com/max/2120/1*0-8Nn9Kfly0ZLJNij21UOQ.jpeg)

结果还是不行。原来是代码里也写死了这个属性。。

```objectivec
cv.modalPresentationStyle = UIModalPresentationFullScreen;
```

然后全局搜索了modalPresentationStyle这个属性，发现果然很多地方都是设置成了UIModalPresentationFormSheet。修改成全屏属性，搞定。

#### 仍然闪退

此时app已经可以正常启动了，但是输入账号密码登录后就闪退。

仔细观察崩溃日志，错误提示是



#### iflyMSC.framework  "The file “Info.plist” doesn’t exist

还报过这个错，后来证明和这个无关。当时我把这个库相关的都注释了。





#### 结论

复现一下出现问题的过程：

升级了最新版本的mac OS 10.15.6和xcode11.6。

原来可以跑通的代码先是蹦出了'libBaiduMobStatSimulator.a'缺arm64架构

> The linked library 'libBaiduMobStatSimulator.a' is missing one or more architectures required by this target: arm64.

因为本身模拟器的库，要什么arm架构，而且我们的项目要用蓝牙，必须是真机调试的，所以我直接把这个库删掉了。

然后就报最开始的那个错，替换了security.Framework就可以。







后来就变成了我用的那个countrypickerview的开源库，image not found.

然后升级了这个库，结果还是有问题。