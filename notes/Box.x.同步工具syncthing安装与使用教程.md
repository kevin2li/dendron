---
id: 89hl0uzyone0lhu83yi56dw
title: 同步工具syncthing安装与使用教程
desc: ''
updated: 1684651462068
created: 1684650877007
---


## 简介
Syncthing是一个开源的文件同步工具，用于在不同设备之间实现文件的自动同步和共享。它允许您安全地在多个计算机、手机或其他设备之间同步文件和文件夹，而无需依赖云存储或第三方服务器。

![](https://minio.kevin2li.top/image-bed/blog/20230521143949.png)

以下是Syncthing的一些主要特点和功能：

- 去中心化：Syncthing基于对等（peer-to-peer）原则，不依赖集中式服务器进行文件同步。每个设备都可以直接与其他设备通信，实现点对点的同步和共享。
- 安全性：Syncthing使用强大的加密技术（TLS）保护数据传输，确保文件在传输和存储过程中的安全性。数据在发送和接收设备之间以加密形式进行传输，只有授权设备可以解密和访问文件。
- 全平台支持：Syncthing支持多个操作系统，包括Windows、macOS、Linux、Android等。这使得您可以在不同类型的设备上使用Syncthing来实现跨平台的文件同步。
- 自动同步：Syncthing能够自动检测和同步文件的更改。一旦您在一个设备上修改、添加或删除文件，Syncthing将自动将更改应用于其他设备，确保所有设备上的文件保持同步。
- 灵活的配置：Syncthing提供了灵活的配置选项，允许您选择要同步的文件和文件夹，并设置同步规则和优先级。您可以根据需要自定义同步行为和文件过滤器。
- Web界面：Syncthing提供了一个易于使用的Web界面，用于配置和监视同步进程。您可以通过Web界面查看同步状态、设备连接情况、文件冲突等信息。
- 社区支持：Syncthing是一个活跃的开源项目，拥有庞大的用户社区。您可以从社区中获取支持、参与讨论，以及获取最新的更新和改进。

总体而言，Syncthing是一个强大而灵活的文件同步工具，提供了安全、去中心化的方式来实现多设备之间的文件同步和共享。无论是用于个人使用还是小团队协作，Syncthing都是一个值得考虑的选择。

官网：https://syncthing.net/  
下载地址：https://syncthing.net/downloads/
## 安装
- windows  

可以使用集成了syncthing的系统托盘插件[SyncTrayzor](https://github.com/canton7/SyncTrayzor/releases/latest)来更方便管理和使用。

注：该插件内置的syncthing可能不是最新版，有可能导致启动失败，可去官网下载最新的`syncthing.exe`覆盖插件安装目录下内置的`syncthing.exe`。

- Android  
F-Droid: https://f-droid.org/packages/com.nutomic.syncthingandroid/
