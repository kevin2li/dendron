---
id: d8oh9z0w3guuue7xocdig2l
title: Windows文件共享教程
desc: ''
updated: 1685323285411
created: 1685323275136
---


## 简介
文件共享即允许计算机之间共享文件和文件夹。Windows提供了简单方便地在局域网内共享文件夹的方式，您可以轻松在多个Windows计算机之间共享文档、音乐、照片等文件。共享文件夹还可以被Mac和Linux计算机访问,只需要知道其IP地址或计算机名即可。

## 如何开启共享

1. 新建一个文件夹，名称自定义，我这里取名“共享文件夹测试”
2. 选中新建的文件夹，右击选择“属性”，切到“共享”选项卡。

里面提供了`简单共享`和`高级共享`两种方式。

![](https://minio.kevin2li.top/image-bed/blog/20230529094556.png)

- 简单共享

  > 不太推荐使用，会暴露目标文件夹的父级目录内容，不安全，可以参考“高级共享”

  ![](https://minio.kevin2li.top/image-bed/blog/20230529094922.png)

  ![](https://minio.kevin2li.top/image-bed/blog/20230529095007.png)

  ![](https://minio.kevin2li.top/image-bed/blog/20230529095039.png)

  成功，可以在局域网其他设备上测试连接。

- 高级共享

  ![](https://minio.kevin2li.top/image-bed/blog/20230529095908.png)

  进行用户添加和权限设置

  ![](https://minio.kevin2li.top/image-bed/blog/20230529095812.png)

  启用共享

  ![](https://minio.kevin2li.top/image-bed/blog/20230529100037.png)

  局域网其他设备连接测试：

  ![](https://minio.kevin2li.top/image-bed/blog/20230529100208.png)

  成功！

## 如何关闭共享

打开计算机管理，找到“共享文件夹”，在“共享”下找到目标共享名，右击选择“停止共享”。

![](https://minio.kevin2li.top/image-bed/blog/20230529095512.png)

