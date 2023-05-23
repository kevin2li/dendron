---
id: s3p0r5dow6tt9ovb39khw82
title: 备份工具Kopia安装与使用教程
desc: ''
updated: 1684819122537
created: 1684818211858
---


## 简介
Kopia是一个快速而安全的开源备份/还原工具，允许您创建加密的数据快照并将其保存到您选择的远程或云存储、网络附加存储或服务器，或本地计算机上。 Kopia不会“映像”整个计算机。相反，Kopia允许您备份/还原您认为重要或关键的任何文件/目录。

Kopia有CLI（命令行界面）和GUI（图形用户界面）版本，使其成为高级用户和普通用户的完美工具。您可以阅读有关Kopia独特功能的更多信息，包括压缩，去重，端到端“零知识”加密和纠错，以更好地了解Kopia的工作原理。

Github: https://github.com/kopia/kopia  
文档: https://kopia.io/docs/


## 安装
参考: https://kopia.io/docs/installation/


## 使用
### 选择备份存储位置

支持本地存储、SFTP、WebDAV、谷歌云、Amazon S3等多种存储源.

![](https://minio.kevin2li.top/image-bed/blog/20230523130909.png)

### 创建快照
![](https://minio.kevin2li.top/image-bed/blog/20230523131325.png)

### 配置备份策略

可以在策略(Policy)标签页下进行设置:

![](https://minio.kevin2li.top/image-bed/blog/20230523131505.png)

可以从以下多个维度进行策略配置,包括快照保留、文件、压缩算法、调度等.

![](https://minio.kevin2li.top/image-bed/blog/20230523131410.png)

### 还原
在快照标签页下点开一个路径,可以看到该路径的快照历史

![](https://minio.kevin2li.top/image-bed/blog/20230523131710.png)

点开其中一个快照历史,可以选择将其挂载到本地或者恢复到指定目录

![](https://minio.kevin2li.top/image-bed/blog/20230523131725.png)