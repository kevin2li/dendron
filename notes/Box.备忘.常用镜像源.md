---
id: 10egb6fgplgoxmuboxfaz6d
title: 常用镜像源
desc: ''
updated: 1682652980790
created: 1682589480746
---
## Ubuntu

阿里云镜像：https://developer.aliyun.com/mirror/ubuntu\
清华源镜像：https://mirror.tuna.tsinghua.edu.cn/help/ubuntu/

方法：
- 修改配置文件\
配置文件路径：`/etc/apt/sources.list`

``` bash 
# 备份
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

# 替换内容
sudo tee /etc/apt/sources.list << EOF
```

Ubuntu22.04示例：

``` bash 
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse

# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse

deb http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse
# deb-src http://security.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
```

<!-- more -->

## Debian

清华源：https://mirror.tuna.tsinghua.edu.cn/help/debian/

Debian11示例：

``` yaml 
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free

deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free

deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free

# deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free

deb https://security.debian.org/debian-security bullseye-security main contrib non-free
# deb-src https://security.debian.org/debian-security bullseye-security main contrib non-free
```

## pip

阿里云：https://developer.aliyun.com/mirror/pypi?spm=a2c6h.13651102.0.0.59f71b112m674E\
清华源： https://mirror.tuna.tsinghua.edu.cn/help/pypi/
- 终端临时使用

``` bash 
# 阿里云
pip install <package> -i https://mirrors.aliyun.com/pypi/simple/

# 清华源
pip install <package> -i https://pypi.tuna.tsinghua.edu.cn/simple
```

-   写入配置文件

配置文件路径：`~/.pip/pip.conf`

内容：

``` ini 
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

## conda

清华源：https://mirror.tuna.tsinghua.edu.cn/help/anaconda/\
- 写入配置文件\
配置文件路径：`~/.condarc`

``` yaml 
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

## docker镜像加速站

阿里云：https://help.aliyun.com/document_detail/60750.html
- 写入配置文件

配置文件路径：`/etc/docker/daemon.json` (没有则新建)

添加下面条目：

``` json 
{
    "registry-mirrors": ["<镜像加速器地址>"]
}    
```

登录[容器镜像服务控制台](https://cr.console.aliyun.com/?spm=a2c4g.60750.0.0.19e66bbcTKDXGa)，在左侧导航栏选择`镜像工具 > 镜像加速器`，在镜像加速器页面获取镜像加速地址。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e610718cf7b68cbaf6d9eef84efe82af.image.png)

重启服务：

``` bash 
sudo systemctl daemon-reload
sudo systemctl restart docker
```

验证：

``` bash 
docker info
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/24dd7526da3770d004d7b057f3ab8804.image.png)

能找到刚才自己设的`Registry Mirrors`，说明设置成功。

## npm

参考： https://npmmirror.com/

``` bash
 npm install -g <package> --registry=https://registry.npmmirror.com
```

## Go

参考：https://goproxy.cn/

``` bash
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
```
