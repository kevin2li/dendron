---
id: eo5jdpna8r59ea9rkg1ufia
title: k3s使用教程
desc: ''
updated: 1682762606016
created: 1682762017570
---




## 简介
K3s 是轻量级的 Kubernetes。K3s 易于安装，仅需要 [Kubernetes](https://kubernetes.io/zh-cn/) 内存的一半，所有组件都在一个小于 100 MB 的二进制文件中。

![](https://minio.kevin2li.top/image-bed/202304291755923.png)

官网: https://k3s.io/  

文档: https://docs.k3s.io/zh/  

Github: https://github.com/k3s-io/k3s

## 教程
### 安装

``` bash 
# server节点安装
curl -sfL https://get.k3s.io | sh -

# agent节点安装(其中`K3S_TOKEN`位于server下的`/var/lib/rancher/k3s/server/node-token`)
curl -sfL https://get.k3s.io | K3S_URL=https://myserver:6443 K3S_TOKEN=mynodetoken sh -
```

server安装完成后会自动将配置写入`/etc/rancher/k3s/k3s.yaml`, 并自动启动服务.

### 术语

### 常用命令


### 卸载

``` bash 
# 卸载server
/usr/local/bin/k3s-uninstall.sh

# 卸载agent
/usr/local/bin/k3s-agent-uninstall.sh
```

## 参考