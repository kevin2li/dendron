---
id: eo5jdpna8r59ea9rkg1ufia
title: k3s使用教程
desc: ''
updated: 1685004864794
created: 1682762017570
---

## 简介
K3s 是轻量级的 Kubernetes。K3s 易于安装，仅需要 [Kubernetes](https://kubernetes.io/zh-cn/) 内存的一半，所有组件都在一个小于 100 MB 的二进制文件中。

![](https://minio.kevin2li.top/image-bed/blog/20230525165033.png)

官网: https://k3s.io/  

文档: https://docs.k3s.io/zh/  

Github: https://github.com/k3s-io/k3s

## 安装
1. master节点
``` bash 
curl -sfL https://get.k3s.io | sh -

# 国内用户
curl -sfL https://rancher-mirror.rancher.cn/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
```

server安装完成后会自动将配置写入`/etc/rancher/k3s/k3s.yaml`, 并自动启动服务.

开放6443端口，否则agent可能会连接不上
``` bash 
sudo firewall-cmd --permanent --zone=public --add-port 6443/tcp
sudo firewall-cmd --reload
```

2. agent节点  

其中`K3S_TOKEN`位于server下的`/var/lib/rancher/k3s/server/node-token`
```bash
curl -sfL https://get.k3s.io | K3S_URL=https://myserver:6443 K3S_TOKEN=mynodetoken sh -

# 国内用户
curl -sfL https://rancher-mirror.rancher.cn/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn K3S_URL=https://myserver:6443 K3S_TOKEN=mynodetoken sh -
```

3. 验证

全部安装完成后，可在master节点上输入下面命令查看所有节点：

``` bash 
kubectl get nodes
```

![](https://minio.kevin2li.top/image-bed/blog/20230525164726.png)

## 使用
### 常用命令

``` bash 
# 卸载server
/usr/local/bin/k3s-uninstall.sh

# 卸载agent
/usr/local/bin/k3s-agent-uninstall.sh
```

### Pod

``` yaml 

```


### Deployment

### Service

## 参考