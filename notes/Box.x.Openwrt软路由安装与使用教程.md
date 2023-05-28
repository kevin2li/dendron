---
id: y27ozphocjmnk2yujkwkf10
title: Openwrt软路由安装与使用教程
desc: ''
updated: 1685013281786
created: 1684560392862
---
## 简介
OpenWrt是一个用于嵌入式设备的自由开源操作系统，旨在替代设备制造商提供的原始固件。它基于Linux内核，并提供了一个灵活且可定制的操作环境，使用户能够完全控制设备的功能和配置。

OpenWrt的设计目标是为路由器、无线接入点、媒体播放器和其他网络设备提供高度定制的固件。它提供了一系列强大的功能，包括网络地址转换（NAT）、防火墙、虚拟专用网络（VPN）、负载平衡、带宽控制、无线网络支持等。通过使用OpenWrt，用户可以将普通的网络设备转变为高度可定制的、功能丰富的路由器和网络服务器。

OpenWrt的主要特点包括：

1. 自由开源：OpenWrt是一个开源项目，遵循GPL许可证，允许用户自由修改、分发和使用。
2. 定制性强：OpenWrt提供了一个完整的软件包管理系统，用户可以选择安装所需的软件包，以满足特定的需求和用途。
3. 轻量级：OpenWrt专注于资源效率，设计精简，能够在低端硬件上运行，包括一些老旧的路由器和嵌入式设备。
4. 安全性：OpenWrt的开发团队致力于及时修复漏洞，并提供安全更新，确保系统的安全性和稳定性。
5. 社区支持：OpenWrt拥有活跃的社区，用户可以从社区中获取支持、解决问题和共享经验。

通过使用OpenWrt，用户可以利用其强大的功能和灵活的定制性，将普通的网络设备转化为更强大和高度可定制的设备，满足各种个性化的网络需求。

## 安装
### 镜像下载
参考：
1. https://github.com/kenzok8/openwrt_Build
2. https://supes.top/?version=22.03&target=x86%2F64&id=generic
3. https://openwrt.club/dl

本文采用的是[openwrt-04.18.2023-x86-64-generic-squashfs-combined.img.gz](https://supes.top/releases/targets/x86/64/openwrt-04.18.2023-x86-64-generic-squashfs-combined.img.gz)镜像。

### 安装类型
#### U盘安装
- **ventoy**
https://www.ventoy.net/cn/doc_openwrt.html

#### 物理机安装
> 写盘工具`physdiskwrite`下载：https://m0n0.ch/wall/physdiskwrite.php  

通过`WePE`写入PC硬盘。

注：写入前，可能需要先用`DiskGenius`将目标硬盘数据清空。
```powershell
physdiskwrite.exe -u <img_path>
```
写入完成后，还可以用`DiskGenius`工具扩容下分区。

重启，拔掉U盘将直接从硬盘启动。

### BIOS设置
按`F2`进入BIOS。
1. 关闭`fast boot`、`secure boot`
2. `boot options`将`USB启动`设置为第一个

### 正式安装

## 使用
### 修改默认ip
1. 方法一：改配置文件  
配置文件路径：`/etc/config/network`

``` bash
vi /etc/config/network
# 修改lan下的ip
```
修改完后执行命令`service network restart`立即生效，或者重启生效。

2. 方法二：网页控制台修改  

路径：网络>接口>LAN

![](https://minio.kevin2li.top/image-bed/blog/20230521093825.png)

![](https://minio.kevin2li.top/image-bed/blog/20230521093930.png)

> 修改无法生效？ 参考：https://www.right.com.cn/forum/thread-8241568-1-1.html

### 设置旁路由
旁路由（Pass-through routing）是一种网络配置方式，用于将一个网络设备（通常是路由器）放置在主网络之外，以扩展网络的功能或增加网络的安全性。

在旁路由设置中，主网络由一个主要路由器（通常是ISP提供的路由器）管理，而旁路由器则连接到主网络上，并通过其自身的功能和配置提供额外的服务或安全层。

1. 类型一：全部设备走旁路由  
步骤： 
   - 1) 主路由开启DHCP，并将网关指向旁路由  
     以TP-Link为例：
     ![](https://minio.kevin2li.top/image-bed/blog/20230521131657.png)
     
     注：部分路由器可能不支持此设置，可尝试由旁路由托管DHCP服务，请参考其他博客。

   - 2) 旁路由网关指向主路由


1. 类型二：指定设备走旁路由  
步骤：  
   - 1) 主路由开启DHCP
   - 2) 旁路由网关指向主路由
   - 3) 需要走旁路由的设备把网关指向旁路由
     - 移动设备：将IP获取方式由`DHCP`改为`静态`，然后手动指定IP,并把网关IP设置为旁路由IP。
     - PC: 同理。
### 插件安装
- openclash  
参考：https://github.com/vernesong/OpenClash/wiki/%E5%AE%89%E8%A3%85

1）安装依赖：
```bash
opkg install luci
opkg install luci-base
opkg install iptables
opkg install dnsmasq-full
opkg install coreutils
opkg install coreutils-nohup
opkg install bash
opkg install curl
opkg install jsonfilter
opkg install ca-certificates
opkg install ipset
opkg install ip-full
opkg install iptables-mod-tproxy
opkg install kmod-tun # (TUN模式)
opkg install luci-compat # (Luci-19.07)
```
2）安装插件：  
下载地址：https://github.com/vernesong/OpenClash/releases  
```bash
#上传IPK文件至您路由器的 /tmp 目录下

#假设安装包名字为
luci-app-openclash_0.33.7-beta_all.ipk

#执行安装命令
opkg install /tmp/luci-app-openclash_0.33.7-beta_all.ipk
```
安装完成后刷新LUCI页面（不行就重启），在菜单栏 -> 服务 -> OpenClash 进入插件页面

3）配置节点订阅  
网络订阅：  

![](https://minio.kevin2li.top/image-bed/blog/20230521121824.png)

或者上传配置文件：  

![](https://minio.kevin2li.top/image-bed/blog/20230521121920.png)

成功截图：

![](https://minio.kevin2li.top/image-bed/blog/20230521121712.png)

- PassWall  

在节点订阅处，点击“添加”，填写名称和订阅网址。

![](https://minio.kevin2li.top/image-bed/blog/20230521123053.png)

在“基本设置”中，打开"主开关"，选择tcp和udp使用的节点，然后“保存并应用”即可。应用成功后，可点击上方的网站进行测试。

![](https://minio.kevin2li.top/image-bed/blog/20230521123303.png)

## 参考

1. [什么值得买 | 如何安装软路由？ 篇三：软路由系统的安装-物理机OpenWRT](https://post.smzdm.com/p/ad2ok5ok/)
2. [知乎 | 从听说到上手，人人都能看懂的旁路由入门指南](https://zhuanlan.zhihu.com/p/122233420)
3. [知乎 | 旁路由设置教程](https://zhuanlan.zhihu.com/p/112484256?utm_campaign=shareopn&utm_medium=social&utm_oi=790165242284998656&utm_psn=1643401677880307712&utm_source=wechat_session&s_r=0&utm_id=0)
4. [LEDE(OpenWrt)安装openclash ｜旁路由技巧 ｜ 配置网络流量全部通过旁路由](https://cloud.tencent.com/developer/article/1693260)