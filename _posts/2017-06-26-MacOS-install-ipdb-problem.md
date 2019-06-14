---
title: "MacOS下安装ipdb的问题"
layout: post
date: 2017-06-26 22:07
category: blog
tag:
- pip
- ipdb
author: Sun
---

以下方法没有测试：
> 由于El Capitan引入了SIP机制(System Integrity Protection)，默认下系统启用SIP系统完整性保护机制，无论是对于硬盘还是运行时的进程限制对系统目录的写操作。 这也是我们安装ipdb/ipython失败的原因….
> 现在的解决办法是取消SIP机制，具体做法是：
> 重启电脑，按住Command+R(直到出现苹果标志)进入Recovery Mode(恢复模式)
> 左上角菜单里找到实用工具 -> 终端
> 输入csrutil disable回车
> 重启Mac即可
> 如果想重新启动SIP机制重复上述步骤改用csrutil enable即可
> 我们现在再看看sip的状态, 这样再安装ipdb/ipython、gevent再也不会提示无法写入的权限提示了

```latex
$ csrutil status
System Integrity Protection status: disabled.
```

如果在mac下碰到OSError: [Errno 1] Operation not permitted:的问题，就算用sudo 也无法解决，那肯定是sip在作怪了.

本人测试了另一种**更为优雅**的方法，基于普通用户的权限来安装。
此外，本人还遇到了提示版本的问题。

```python
error in ipdb setup command: Invalid environment marker: python_version >= "3.3"

$ pip install ipdb==0.10.2 --user -U
```



