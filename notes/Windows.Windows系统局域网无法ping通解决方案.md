---
id: vpctmnqeyiu18x8w4ur2jsx
title: Windows系统局域网无法ping通解决方案
desc: ''
updated: 1684850003748
created: 1684849250699
---

## 方法

这是防火墙拦截导致的，可以关闭防火墙，或者放行ICMP协议请求。

输入`Win+R`，在对话框中输入`wf.msc`打开防火墙高级设置。

![](https://minio.kevin2li.top/image-bed/blog/20230523214231.png)

在入站规则里，找到"文件和打印机共享（回显请求 - ICMPv4-In）",右键选择“启用规则”。在局域网内需要进行ping测试的windows设备上都进行此设置。

![](https://minio.kevin2li.top/image-bed/blog/20230523214848.png)

完毕后，重新进行ping测试：

![](https://minio.kevin2li.top/image-bed/blog/20230523215257.png)

成功ping通。
