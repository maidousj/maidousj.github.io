---
title: git push本地分支问题
layout: post
date: 2019-12-06 15:23
image: /assets/images/
headerImage: false
category: Blog
tag:
- Git
author: Sun
---

项目需要，在本地创建了新的分支，但是在push的时候遇到了问题。

<!--more-->

```shell
git push --set-upstream origin newbranch
```

执行上述命令push时，遇到了

```shell
error: RPC failed; result=56, HTTP code = 0
fatal: The remote end hung up unexpectedly
fatal: The remote end hung up unexpectedly
```

网上大部分解决方案是增加http提交方式的缓存(好像开始时不是这个错误，但是缓存的确不够，按照如下命令增加缓存以后，提交会报如上错误)：

```shell
git config http.postBuffer 200M
```

修改后依然报错，终于找到了这篇博客[《Solve Git Push Issue: (efrror: RPC failed; result=56, HTTP code = 0)》](https://blog.csdn.net/Dream_loving/article/details/15812311)，里面用修改http提交方式为ssh提交方式的办法解决了我的问题：

```shell
git remote -v
```

查看当前仓库的提交方式，我的是http方式，修改它：

```shell
git remote set-url origin git@github.com:xxx/xxx.git
```

然后再push，终于搞定。

