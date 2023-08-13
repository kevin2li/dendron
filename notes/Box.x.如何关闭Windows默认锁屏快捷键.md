---
id: 1xad776tbc5khbh8va0065b
title: 如何关闭Windows默认锁屏快捷键
desc: ''
updated: 1686832239431
created: 1686831728652
---

## 方法

打开注册表编辑器：

转到`计算机\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies`

![](https://minio.kevin2li.top/image-bed/blog/20230615202219.png)

新建一个`System`的项。  

在`System`项下面再新建一个`DWORD(32位)值`,命名为`DisableLockWorkstation`

![](https://minio.kevin2li.top/image-bed/blog/20230615202447.png)

![](https://minio.kevin2li.top/image-bed/blog/20230615202815.png)