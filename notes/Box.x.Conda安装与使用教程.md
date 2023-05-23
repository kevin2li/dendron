---
id: bnwnow1xtfn6spib69ngxl1
title: Conda安装与使用教程
desc: ''
updated: 1684846043104
created: 1684841520728
---



## 简介

![](https://minio.kevin2li.top/image-bed/blog/20230523204215.png)

Conda是一个流行的开源软件包管理系统和环境管理系统，用于管理多个软件包和其依赖关系。Conda可以在多个操作系统上使用，如Windows、macOS和Linux，并且可以管理多种编程语言的软件包，如Python、R、Julia等。Conda提供了一个命令行界面，也可以通过Anaconda Navigator等图形用户界面进行管理。

Conda的主要特点包括：

- **软件包管理**：Conda可以管理多个软件包及其依赖关系，可以安装、更新、卸载和查看软件包信息，方便用户管理和使用软件包。

- **环境管理**：Conda可以创建、激活和删除多个环境，每个环境可以拥有自己的软件包和依赖关系，可以方便地管理不同项目的依赖关系。

- **跨平台支持**：Conda可以在多个操作系统上使用，如Windows、macOS和Linux，并且可以管理多种编程语言的软件包，如Python、R、Julia等，方便用户在不同平台和编程语言之间进行切换和管理。

- **自动依赖解决**：Conda可以自动解决软件包之间的依赖关系，确保安装的软件包和其依赖的软件包版本兼容，并且不会产生冲突或错误。

- **离线安装**：Conda支持离线安装，可以将软件包和依赖关系打包成一个离线安装包，方便用户在没有网络连接或有限带宽的环境中安装软件包。

- **快速安装**：Conda的软件包和依赖关系都是预编译的，可以加快软件包的安装和使用速度。

- **免费开源**：Conda是一款开源的软件，可以免费使用和分发，没有任何使用限制和费用。

总之，Conda是一个流行的开源软件包管理系统和环境管理系统，可以方便地管理多个软件包和其依赖关系，支持跨平台使用和多种编程语言，具有自动依赖解决、离线安装、快速安装等特点。使用Conda可以通过命令行或图形用户界面进行软件包和环境管理，方便用户进行项目开发和科学计算。

## 安装
### Windows
1. 下载安装包  

下载地址：https://docs.conda.io/en/latest/miniconda.html

选择适合自己系统版本的进行安装。

![](https://minio.kevin2li.top/image-bed/blog/20230523194825.png)

2. 配置环境变量

打开环境变量设置，找到系统`PATH`环境变量进行编辑

![](https://minio.kevin2li.top/image-bed/blog/20230523194635.png)

将下面红框标注的路径添加到**系统**`PATH`环境变量中(仅供参考，具体路径根据你的安装路径确定)，这些目录下包含了`python.exe`、`conda.exe`等二进制执行文件。

![](https://minio.kevin2li.top/image-bed/blog/20230523194419.png)

3. 设置权限(可选)   

> 参考：https://learn.microsoft.com/zh-cn/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3

由于conda初始化时候会执行脚本，

![](https://minio.kevin2li.top/image-bed/blog/20230523193323.png)

而系统默认执行策略为`Restricted`，该策略下是不允许执行脚本的，所以会出现上面红色错误(如果你没有这个问题，可跳过此步骤)。


解决方法： 通过以管理员权限打开终端，输入下面命令修改执行策略来允许运行脚本。

``` powershell
# 查看当前执行策略
Get-ExecutionPolicy

# 修改策略(管理员权限)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```
![](https://minio.kevin2li.top/image-bed/blog/20230523193555.png)

两种策略对比：

![](https://minio.kevin2li.top/image-bed/blog/20230523193924.png)

4. 初始化  

``` powershell
conda init powershell 
```

![](https://minio.kevin2li.top/image-bed/blog/20230523194119.png)

重新启动终端，可以看到已经可以识别python环境名称了。

![](https://minio.kevin2li.top/image-bed/blog/20230523194234.png)

## Ubuntu
xx

# 使用
## 镜像源配置

- 清华源：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

方法：用国内源覆盖`$HOME/.condarc`的内容。

>注意: windows用户需要先通过命令`conda config --set show_channel_urls yes`生成`.condarc`文件再进行配置。

## 环境管理

``` bash 
# 查看已有环境
conda env list

# 导出环境
xx

# 迁移环境
xx
```