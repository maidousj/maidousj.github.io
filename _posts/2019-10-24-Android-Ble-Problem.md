---
title: Android蓝牙打开问题和同样的countrypicker打开颜色不同的问题
layout: post
date: 2019-10-24 20:00
image: /assets/images/
headerImage: false
category: Blog
tag:
- Android
- Ble
- Huawei
author: Sun
---

今天是程序员节，先节日快乐吧。谁能想到遇到两个坑。

<!--more-->

1. Android蓝牙打开问题

   因为某种需求，需要在进行某个操作之前判断蓝牙是否打开，否的话就给它打开。

   看起来多正常一需求，只要用BluetoothAdapter来判断一下，如果没打开就给调用enable()。

   ```java
   BluetoothManager manager = (BluetoothManager) getActivity()
                   .getSystemService(Context.BLUETOOTH_SERVICE);
   BluetoothAdapter bleAdapter = manager.getAdapter();
   if(!bleAdapter.isEnable()) {
     	bleAdapter.enable();
   }
   ```

   本来也没问题，但是放我们项目中，遇到华为手机就完犊子了。甲方大爷说“我们操作时弹出打开蓝牙请求，打开了然后进行操作，结果巨慢；但是当一次操作以后，后边就快了”。这能忍？找日志一看：

   ![](/assets/images/2019-10-24-android-ble-problem/image-20191024202015069.png)

   这两步之间就差了7秒，这之后我们的操作才能正常进行。这个日志在别的手机上暂时还没测出来，而且别的手机进行类似操作也挺快。

   而且以前的android版本可能bleAdapter.enable()不会弹出对话框，就直接打开了，所以以前的代码里这样就直接返回打开，然后手机上提示打开蓝牙成功。但是！现在的版本会弹出对话框问你打不打开，如果不打开的话，这步走完，我们的代码继续给出成功的提示。所以，需要找到一个回调来判断是不是打开成功，并给出正确的提示。

   于是找到一种办法：

   ```java
   Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
   startActivityForResult(enableBtIntent, REQUEST_ENABLE_BT);
   ```

   然后在onActivityResult()方法中根据requestCode==REQUEST_ENABLE_BT来得到回调位置，然后根据resultCode判断是否操作成功，类似于

   ```java
   public void onActivityResult(int requestCode, int resultCode, Intent data) {
   		if (requestCode == BaseOperFragment.REQUEST_ENABLE_BT) {
   				if (resultCode == RESULT_OK) {
   						//提示成功
   				}
   		} else {
   				//提示失败
   		}
   }
   ```

   这样搞完以后，发现华为手机上还是慢，可能那个日志出现前蓝牙的确已经打开了，但是还有一些需要初始化的工作？？这个实在是没什么办法了，于是根据Build.MANUFACTURER判断了下是不是华为手机，是的话就弹了一个对话框等待个几秒，期待能顺利初始化完成。目前来看这个土办法奏效了。

2. 第二个坑是，找了一个countrypicker的库，结果却是，layout里include的同一个country picker，但是在不同的activity中却出现了不一致的情况，一个是白色背景，一个是黑色背景。

   仔细看了半天，发现这两个activity的确不一样，选中字体后的颜色就不一样。如下两个图：

![](/assets/images/2019-10-24-android-ble-problem/ppp.png){:width="400"}

![](/assets/images/2019-10-24-android-ble-problem/image-20191024200342010.png){:width="400"}

​	找了半天，在countrypicker代码里所有setTextColor的地方打了断点，发现传入的值完全一致。又重写了activity对应的layout，发现还不行。最后想是不是调用这个activity的地方做了什么设置，一搜调用，果然在AndroidManifest.xml中发现了不一样，有一个activity设置了一个自己的style，如下图：

![](/assets/images/2019-10-24-android-ble-problem/image-20191024200707113.png){:width="400"}

这个能影响背景的，我猜应该是高亮的那部分原因，具体懒得测了。毕竟程序员节呢，还没吃饭呢哎。

------------

1029修改：

蓝牙部分的处理逻辑又改了，这样的比之前的土办法更为周全一些。

主要思想就是希望能**找到一个地方可以判断不论是什么手机，我都保证打开蓝牙而且设备正常的情况下可以很快的操作**。由于之前就是系统层面接口给出的方案中，蓝牙打开后不知道还有些品牌会进行一些什么处理，导致第一次操作十分慢。

蓝牙操作是分几步的，首先要调用startScan()，一旦查找到指定设备，就可以继续进行连接、操作、断开连接等等步骤。

于是，找到我们的sdk封装的扫描设备操作，在扫描操作开始前进行弹窗，有倒计时提示（设置为20s超时），然后在扫描的回调（表明扫描到特定设备，也就是不管什么手机，蓝牙已经正常开启，可以继续操作了）中，将弹窗关掉，同时提示蓝牙打开成功。此时继续执行操作，经测试比较正常。这种方案规避了不同设备之间蓝牙的差异，而且比较快的手机中，倒计时框也消失的比较快；华为锤子之类可能出问题的手机上，也不会耗掉20s的时间。总之，这样一改，用户接下来的操作就很顺畅了，算是在找到具体底层蓝牙差异之前的一个比较靠谱的解决办法了。