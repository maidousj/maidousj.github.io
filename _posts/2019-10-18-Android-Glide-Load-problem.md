---
title: Android Glide加载图片只显示三张问题
layout: post
date: 2019-10-18 14:15
image: /assets/images/
headerImage: false
category: Blog
tag:
- Android
- Glide
author: Sun
---

如题目，用glide加载图形验证码，设置点击验证码可以刷新，但是每次都三张以后就不显示新的了。

<!--more-->

解决方案是设置跳过图片缓存：

.skipMemoryCache(true) 

具体代码如下：

```java
Glide.with(this)
        .load(getString(R.string.text_verify_image_url))
        .diskCacheStrategy(DiskCacheStrategy.NONE)
        .skipMemoryCache(true)
        .error(R.drawable.getimage)
        .into(mImage);
```

