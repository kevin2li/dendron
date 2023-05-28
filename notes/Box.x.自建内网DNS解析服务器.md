---
id: at610f8wnh3ymy6cr8mseh6
title: 自建内网DNS解析服务器
desc: ''
updated: 1684938394487
created: 1684924978431
---


## 简介
背景：  
由于本人在内网搭建了不少服务，如文件共享、私有云盘、个人博客等等，然后通过内网穿透将其映射到公网云服务器上，再通过反向代理来访问服务。但是大多数情况下，我还是处在和服务器相同的内网环境下的，每次都从公网访问服务属于绕远路了，因此考虑自建一个内网的DNS解析服务器，将域名直接解析到内网ip上，而当我脱离内网环境时，则可以使用公共DNS继续从公网IP访问服务。

目前主流的内网DNS服务器软件主要有[BIND](https://www.isc.org/bind/)和[dnsmasq](https://thekelleys.org.uk/dnsmasq/doc.html)，前者功能强大完备，通常被用于大型企业，比较重量级，而后者适用于小型网络、家庭网络等场景，比较轻量化,比较适合我目前的需求。因此，本文主要介绍dnsmasq的安装与使用方法。

**科普：**
::: tip  什么是DNS服务器
DNS（Domain Name System，域名系统）服务器是一种网络服务，用于将域名解析成 IP 地址或者将 IP 地址解析成域名。DNS 服务器是互联网中的重要组成部分，它们负责将域名映射到相应的 IP 地址，实现网络通信。

DNS 服务器通常分为递归 DNS 服务器和权威 DNS 服务器两种类型。递归 DNS 服务器是用于向客户端提供 DNS 解析服务，它会根据客户端的请求逐级向上查询 DNS 记录，直到找到所需的解析记录或者查询失败。权威 DNS 服务器则存储特定域名的 DNS 记录，它会为请求该域名的客户端提供相应的解析记录。

DNS 服务器按照数据分布方式可分为以下几种类型：

- 根 DNS 服务器（Root DNS Server）：是 DNS 系统的顶级 DNS 服务器，存储了所有顶级域名（如 .com、.org、.net 等）的权威 DNS 服务器的 IP地址。根 DNS 服务器的数量很少，通常由 13 台服务器组成。

- 顶级域名服务器（Top-Level Domain DNS Server）：是权威 DNS 服务器的一种，负责管理顶级域名（如 .com、.org、.net 等）下的所有二级域名（如 google.com、apple.com 等）的 DNS 记录。

- 权威 DNS 服务器（Authoritative DNS Server）：存储特定域名的 DNS 记录，为请求该域名的客户端提供相应的解析记录。

- 本地 DNS 服务器（Local DNS Server）：也称为递归 DNS 服务器，通常位于本地网络中，为本地网络的客户端提供 DNS 解析服务。本地 DNS 服务器会逐级向上查询 DNS 记录，直到找到所需的解析记录或者查询失败。如果本地 DNS 服务器无法找到所需的解析记录，则会向其他递归 DNS 服务器发出查询请求。

DNS 服务器的工作原理通常分为以下几个步骤：

1. 客户端向本地 DNS 服务器发送DNS 查询请求，请求解析指定的域名。

2. 如果本地 DNS 服务器已经缓存了请求的 DNS 记录，则直接返回缓存中的记录。否则，本地 DNS 服务器会向根 DNS 服务器发送查询请求，请求根 DNS 服务器返回顶级域名服务器的 IP 地址。

3. 根 DNS 服务器会将请求转发给相应的顶级域名服务器，顶级域名服务器会返回该域名的权威 DNS 服务器的 IP 地址。

4. 本地 DNS 服务器向权威 DNS 服务器发出查询请求，请求返回该域名的 DNS 记录。

5. 权威 DNS 服务器返回请求的 DNS 记录给本地 DNS 服务器。

6. 本地 DNS 服务器将 DNS 记录缓存起来，并将解析结果返回给客户端。

总之，DNS 服务器是实现域名解析的核心组件之一，负责将域名映射到相应的 IP 地址或者将 IP 地址解析成域名。在互联网中，DNS 服务器的分布和数量是非常多样化的，这些 DNS 服务器相互协作，构成了一个庞大的 DNS 系统。
:::


::: tip  递归DNS服务器和权威DNS服务器的区别

递归 DNS 服务器（Recursive DNS Server）和权威 DNS 服务器（Authoritative DNS Server）是两种不同的 DNS 服务器类型，它们的主要区别如下：

- 功能不同：递归 DNS 服务器用于向客户端提供 DNS 解析服务，它会根据客户端的请求逐级向上查询 DNS 记录，直到找到所需的解析记录或者查询失败。而权威 DNS 服务器则存储特定域名的 DNS 记录，它会为请求该域名的客户端提供相应的解析记录。

- 数据来源不同：递归 DNS 服务器在查询 DNS 记录时，会从其他 DNS 服务器中逐级向上查询，直到找到所需的解析记录。而权威 DNS 服务器则直接存储特定域名的 DNS 记录，它是该域名 DNS 记录的最终来源。

- 所在位置不同：递归 DNS 服务器通常位于本地网络中，为本地网络的客户端提供 DNS 解析服务。而权威 DNS 服务器则通常由域名注册商或者网站管理员管理，用于存储特定域名的 DNS 记录。

- 接受查询的方式不同：递归 DNS 服务器通常接受来自本地网络中的客户端的 DNS 查询请求，然后向其他 DNS 服务器发出查询请求，最终返回所需的 DNS 记录。而权威 DNS 服务器只接受来自其他 DNS 服务器的查询请求，在查询到所需的 DNS 记录后，会将其返回给发出查询请求的 DNS 服务器。

总之，递归 DNS 服务器和权威 DNS 服务器都是 DNS 系统中不可缺少的组成部分，但其作用和功能不同。递归 DNS 服务器主要为客户端提供 DNS 解析服务，而权威 DNS 服务器则存储特定域名的 DNS 记录，并为请求该域名的客户端提供相应的解析记录。

:::

## dnsmasq安装与使用
### 安装

``` bash 
sudo apt-get update
sudo apt-get install dnsmasq
```
### 使用
配置文件路径：`/etc/dnsmasq.conf`  

重要参数说明：
| 名称           | 含义                                                                                                                                                                                                                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| resolv-file    | 指定上游DNS服务器文件的路径，默认为`/etc/resolv.dnsmasq.conf`                                                                                                                                                                                                                                                                                     |
| strict-order   | 默认情况下，dnsmasq 查询上游 DNS 服务器时采用的是并行查询的方式，即同时向所有的上游 DNS 服务器发送 DNS 查询请求，并使用最先收到的响应结果作为查询结果。<br/>当 strict-order 参数被设置为 true 时，dnsmasq 将按照配置文件中指定的顺序查询上游 DNS 服务器，即先查询第一个 DNS 服务器，如果没有响应或者响应超时，则查询第二个 DNS 服务器，以此类推。 |
| interface      | 指定监听的网卡，默认监听所有，可以使用多个interface参数来指定                                                                                                                                                                                                                                                                                     |
| listen-address | 指定监听的ip地址，局域网使用填写内网ip                                                                                                                                                                                                                                                                                                            |
| server         | 指定dnsmasq使用的上游 DNS 服务器地址,可以使用多个server参数来指定,如`server=/taobao.com/223.5.5.5`                                                                                                                                                                                                                                                                                 |
| address        | 为指定的主机名指定 IP 地址, 例如，可以使用 `address=/example.com/192.168.0.2` 将 example.com 域名解析为 192.168.0.2。                                                                                                                                                                                                                             |
| no-resolv      | 禁用系统的 /etc/resolv.conf 文件，并使用 dnsmasq 的上游 DNS 服务器                                                                                                                                                                                                                                                                                |
| no-hosts       | 用于控制是否使用系统的 /etc/hosts 文件。当 no-hosts 参数被设置为 true 时，dnsmasq 将不使用系统的 /etc/hosts 文件，而是仅使用其他来源（例如上游 DNS 服务器）提供的 DNS 记录来解析主机名。                                                                                                                                                          |
| addn-hosts     | 用于指定额外的 DNS 记录。当 addn-hosts 参数被设置时，dnsmasq 将从指定的文件中读取额外的 DNS 记录，并将其添加到本地 DNS 缓存中，以提供更准确和定制化的 DNS 解析服务。                                                                                                                                                                              |

推荐配置：  

- `/etc/dnsmasq.conf`：dnsmasq配置文件

``` conf 
resolv-file=/etc/resolv.dnsmasq.conf
strict-order
# 本机使用只加环回IP，全网使用需要在环回后加本机IP
listen-address=192.168.1.106,127.0.0.1

# 为域名配置指定dns
# server=/taobao.com/223.5.5.5

# 为域名配置指定ip(相当于dns劫持)
# address=/example.com/192.168.0.2

# 1)不使用通配符
# address=/app.kevin2li.top/192.168.1.106

# 2)使用通配符解析 *.kevin2li.top
# address=/.kevin2li.top/192.168.1.106

# 开启日志(debug时可以用)
# log-queries

```

- `/etc/resolv.dnsmasq.conf`： 配置上游DNS服务器
``` conf
# 阿里
nameserver 223.5.5.5
nameserver 223.6.6.6

# 114
nameserver 114.114.114.114
nameserver 114.114.115.115

# 谷歌
nameserver 8.8.8.8
nameserver 8.8.4.4
```

- `/etc/resolv.conf`：默认`systemd-resolvd`配置文件

``` conf 
# 只保留下面这一个，删除其他的nameserver(保证解析请求从dnsmasq走)
nameserver 127.0.0.1
```

修改完配置后，重启：
``` bash 
sudo systemctl restart dnsmasq
```

本机验证：

![](https://minio.kevin2li.top/image-bed/blog/20230524205136.png)


::: tip  与`systemd-resolvd`冲突？
可以关闭`systemd-resolvd`:
``` bash 
# 停止
sudo systemctl stop systemd-resolvd

# 关闭开机自启
sudo systemctl disable systemd-resolvd
```  
:::


为了让局域网其他设备也使用dnsmasq服务器解析域名，可以手动修改设备的dns地址，也可以直接在路由器DHCP设置中指定dns地址，这样连接上的设备会自动设置好dns。

![](https://minio.kevin2li.top/image-bed/blog/20230524221335.png)

### FAQ
1. 查看域名查询日志

在`/etc/dnsmasq.conf`中加入
``` conf 
# For debugging purposes, log each DNS query as it passes through dnsmasq.
log-queries
```

重启：
``` bash 
sudo systemctl restart dnsmasq
```

查看：
``` bash 
sudo less /var/log/syslog | grep dnsmasq 
```
![](https://minio.kevin2li.top/image-bed/blog/20230524220053.png)

2. 局域网设备设置dns为dnsmasq服务器ip后后无法解析域名  

一般由于服务器防火墙拦截导致，可以通过下面命令放行dnsmasq服务：
``` bash 
sudo firewall-cmd --permanent --zone=public --add-port 53/udp # 一定要加(实测)
sudo firewall-cmd --permanent --zone=public --add-port 53/tcp
sudo firewall-cmd --reload
```

### 参考
1. [Linux安装DNSmasq搭建自己的公共DNS](https://blog.xiaoz.org/archives/8303)
2. [dnsmasq 使用教程](https://blog.niekun.net/archives/1869.html)