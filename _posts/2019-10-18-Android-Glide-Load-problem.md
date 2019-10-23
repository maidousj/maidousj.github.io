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



获取到的图片验证码，和下一次对验证码的验证需要处于同一session，所以需要找到Glide在load时发出请求后，服务器返回的sessionID（cookie）。找了大半天，终于[1]帮了大忙。

具体就是在Glide通过url来装载图片之前，想办法让请求通过OkHttpClient来处理，这样可以获取到和服务器交互后的cookie，从而得到sessionID。具体如下：

```java
//初始化okhttp，
OkHttpClient mOkHttpClient = new OkHttpClient.Builder()
        .cookieJar(sessionUtil)   //cookie管理
        .build();

//通过注册，使得图片请求经过OkHttpClient
Glide.get(activity)
        .register(GlideUrl.class
                , InputStream.class
                , new OkHttpUrlLoader.Factory(mOkHttpClient));
```

其中sessionUtil是实现CookieJar接口来保存和载入cookie的：

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import okhttp3.Cookie;
import okhttp3.CookieJar;
import okhttp3.HttpUrl;


public class SessionUtil implements CookieJar {

    //保存每个url的cookie
    private HashMap<HttpUrl, List<Cookie>> cookieStore = new HashMap<>();

    //上一个请求url
    private HttpUrl url;

    public HashMap getCookieStore() {
        return cookieStore;
    }

    public HttpUrl getHttpUrl() {
        return url;
    }

    @Override
    public void saveFromResponse(HttpUrl httpUrl, List<Cookie> list) {
        //保存链接的cookie
        cookieStore.put(httpUrl, list);
        //保存上一次的url，提供下一次cookie的提取。
        url = httpUrl;
    }

    @Override
    public List<Cookie> loadForRequest(HttpUrl httpUrl) {

        //加载上一个链接的cookie
        List<Cookie> cookies = cookieStore.get(url);
        return cookies != null ? cookies : new ArrayList<Cookie>();

    }
}
```

接下来再发送图形验证码的验证请求时，把获取到的sessionID加入到请求的头部即可：

```java
//获取服务器返回cookie，主要是sessionid
HashMap cookieStore = sessionUtil.getCookieStore();
HttpUrl keyUrl = sessionUtil.getHttpUrl();
List<Cookie> cookieList = (List<Cookie>) cookieStore.get(keyUrl);
Cookie cookie = cookieList.get(0);
//cookie字段的格式
String header = "Cookie";
String value = cookie.name() + "=" + cookie.value();

// cookie加入到新的验证请求，以保证和获取图形验证码是同一session
verifyImageCodeRequest.getHttpClient().addHeader(header, value);
```



#### Reference

[1] https://www.twblogs.net/a/5b8d1f742b717718833ba71c