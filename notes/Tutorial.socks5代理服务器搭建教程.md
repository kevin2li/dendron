---
id: lseo2fenqcnu2yvgyxegqfw
title: socks5代理服务器搭建教程
desc: ''
updated: 1682588855752
created: 1682510000115
---
# 简介
socks是一种网络传输协议，主要用于客户端与外网服务器之间通讯的中间传递。根据OSI七层模型来划分，SOCKS属于会话层协议，位于表示层与传输层之间。

当防火墙后的客户端要访问外部的服务器时，就跟socks代理服务器连接。该协议设计之初是为了让有权限的用户可以穿过过防火墙的限制，使得高权限用户可以访问外部资源。经过10余年的时间，大量的网络应用程序都支持socks5代理。

这个协议最初由DavidKoblas开发，而后由NEC的Ying-DaLee将其扩展到版本4，最新协议是版本5，与前一版本相比，socks5做了以下增强：

- 增加对UDP协议的支持；

- 支持多种用户身份验证方式和通信加密方式；

- 修改了socks服务器进行域名解析的方法，使其更加优雅；

# 方法
## 代理服务器搭建

参考：https://www.digitalocean.com/community/tutorials/how-to-set-up-dante-proxy-on-ubuntu-20-04

### 安装

```bash
sudo apt update
sudo apt install dante-server
```

<!-- more -->

验证：
```bash
systemctl status danted.service
```

### 配置

配置文件路径：`/etc/danted.conf`

```yaml
logoutput: syslog
user.privileged: root
user.unprivileged: nobody

# The listening
network interface or address.
internal: 0.0.0.0 port=10080

# The proxying network interface or address.
external: eth0

# socks-rules determine what is proxied through the external interface.
socksmethod: username

# client-rules determine who can connect to the internal interface.
clientmethod: none

client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
}

socks pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
}
```

重启服务：

```bash
sudo systemctl restart danted.service
```

### 服务器开放端口

```bash
# 端口与配置文件指定的端口一致
sudo firewall-cmd --permanent --zone=public --add-port 10080/tcp
sudo firewall-cmd --reload
```


### 创建用户

```bash
sudo useradd -r -s /bin/false your_dante_user
sudo passwd your_dante_user
```

### 测试

```bash
curl -v -x socks5://your_dante_user:your_dante_password@your_server_ip:10080 http://www.baidu.com/
```

## 客户端连接
### Windows
#### 使用SSH
1. 使用动态端口转发将目标机器作为本机的代理
```bash
ssh -CD 9999 user@server
```
2. 设置浏览器代理  

以火狐浏览器为例：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/d7cbb2413fd6c2c765d3d7e62a988995.image.png)

3. 测试


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/22ae082a75faffb08d76cf77d2ed59ff.image.png)

可以看到，显示的ip已经为目标服务器的ip了。


:::tip{title="提示"}
此方法其实不需要目标服务器安装代理软件，属于ssh使用的一个技巧，可以临时使用。
:::
#### 使用Proxifier
1. 下载安装proxifier  

:::info{title="proxifier介绍"}
Proxifier是一款代理客户端软件，可以让不支持代理服务器工作的程序变的可行。支持各种操作系统和各代理协议，它的运行模式可以指定端口，指定程序的特点。
:::
下载地址： https://www.proxifier.com/

2. 添加代理服务器

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/4623a6801f2be7a3fb2775dde8299487.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/5fd1890cb2f586965621ed69f2aaddb9.image.png)

3. 添加规则

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/512e6f4f1aef63b71566f97a66e99e0d.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/6aa34cd73e901fadb9e09eb374081d34.image.png)

4. 测试
- 查看出口ip
```powershell
curl.exe cip.cc
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e417faf4d97fefc856ca437e8e41967c.image.png)

可以看到已经在走代理服务器的流量

- 通过代理登录服务器

```bash
ssh -p 22 kevin2li@10.0.4.13
```
能登录上，说明配置成功。

### Ubuntu
1. 安装`proxychains`

:::info{title="ProxyChains介绍"}
ProxyChains是Linux和其他Unix下的代理工具。 它可以使任何程序通过代理上网， 允许TCP和DNS通过代理隧道， 支持HTTP、 SOCKS4和SOCKS5类型的代理服务器， 并且可配置多个代理。 ProxyChains通过一个用户定义的代理列表强制连接指定的应用程序， 直接断开接收方和发送方的连接。

GitHub：https://github.com/rofl0r/proxychains-ng
:::
```bash
sudo apt update
sudo apt install proxychains
```
2. 配置  

配置文件路径：` /etc/proxychains.conf `

代理配置格式：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/5a737a40f64e072b85d0e818a923d2fb.image.png)

在配置文件中找到`ProxyList`并添加代理：
```ini
[ProxyList]
# add proxy here ...
socks5 	127.0.0.1 10080 <your_user> <your_password>
```
如果填写了多个代理，那么 proxychains 将会将这些代理组成链。

:::warning{title="注意"}
在配置文件中要取消`proxy_dns`选项：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/3aa265cdda489d970e8f11907ca4ecf9.image.png)

:::

3. 使用

在需要使用代理的程序前加上`proxychains`即可使用代理：

举例：
```bash
proxychains curl cic.cc
proxychains git clone https://github.com/rofl0r/proxychains-ng
```

:::tip{title="科学上网"}
如果你在其他机器上设置好了[clash代理](https://blog.kevin2li.top/post/10)，也可借用代理实现科学上网。

修改配置文件`/etc/proxychains.conf`，将代理只保留下面这个(将ip修改为你的clash客户端运行机器的ip)：

```bash
socks5 192.168.2.121 7890
```

测试：
```bash
proxychains curl https://www.google.com
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/79d19a9dbcf66cdf83a69bd5358cfcdf.image.png)
:::
