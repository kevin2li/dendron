# 简介

下面以一个具体案例说明代理服务器的设置与使用。

![aaa.png](https://minio.kevin2li.top/image-bed/vanblog/img/4a8beba732acf8366dbf9df2db03ab6b.aaa.png)


如图，我的台式机目前无法上网，现在想借助代理服务器上网。

<!-- more -->


# 方法
## 配置代理服务器
首先，需要选择一款支持http/https代理服务的软件，本文以[Tinyproxy](https://github.com/tinyproxy/tinyproxy)为例进行配置。

:::info{title="Tinyproxy介绍"}
Tinyproxy是一个轻量级的开源HTTP/HTTPS代理守护程序，它从一开始就设计得既快又小，是一个理想的解决方案，适用于需要全功能HTTP代理的嵌入式部署等用例，但无法使用较大代理的系统资源。

Github: https://github.com/tinyproxy/tinyproxy
:::

### 安装
```bash
# For Ubuntu:
sudo apt install tinyproxy
```

### 编辑配置
配置文件位置：`/etc/tinyproxy/tinyproxy.conf`

基本配置：
```bash
User tinyproxy
Group tinyproxy
Port 8888
Timeout 600

# Allow 127.0.0.1
# Allow ::1
# Allow 192.168.0.0/16
# Allow 172.16.0.0/12
# Allow 10.0.0.0/8

# BasicAuth user password

```
### 重启服务

```bash
sudo systemctl restart tinyproxy
sudo systemctl status tinyproxy
```

### 验证
```bash
curl -x localhost:8888 https://www.baidu.com
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c16d97cf866dcbaa1007cf7b4553bb95.image.png)

这样，代理服务器的设置就基本完成了。

## 路由器端口转发

由于代理服务器位于内网上，我的台式机无法直接访问，需要对路由器管理界面上设置端口转发，将路由器的指定端口(如8888)转发到内网代理服务器的端口8888上。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c925af43acab6e24e16a25a28ac04388.image.png)

如此，便可通过`10.14.129.235:8888`访问到内网代理服务器`192.168.2.1:8888`的服务。

## 客户端设置代理
### 终端设置代理
先简单测试一下：
```bash
curl -x 10.14.129.235:8888 https://www.baidu.com

```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e97d3f89030eca4c1a18ddc51375ba43.image.png)

成功！

如果只是在当前终端临时使用，可以输入如下命令：

```bash
export http_proxy="http://10.14.129.235:8888"
export https_proxy="http://10.14.129.235:8888"

# socks代理
export http_proxy="socks5://dante_user:123456@127.0.0.1:1080"
export https_proxy="socks5://dante_user:123456@127.0.0.1:1080"
```

如果经常使用，可以把它写入配置文件(如`/etc/profile`,`~/.bashrc`等)最后，每次自动加载。


:::warning{title="注意"}
由于tinyproxy代理http/https流量，因此ping命令可能还是ping不通(走的ICMP协议)。
:::

### Ubuntu-apt设置使用代理
参考：https://askubuntu.com/questions/23666/apt-get-does-not-work-with-proxy

当设置好代理后，发现apt命令仍然无法正常使用，需要手动进行下面的设置。

配置文件路径：`/etc/apt/apt.conf`，添加下面内容：

```sh
Acquire::http::proxy "http://User:Password@host:port/";

Acquire::ftp::proxy "ftp://User:Password@host:port/";

Acquire::https::proxy "https://User:Password@host:port/";
```

### docker设置使用代理
参考：https://docs.docker.com/network/proxy/

- 全局代理(应用到所有容器)
在`~/.docker/config.json`中加入下面条目：
```json
{
 "proxies":
 {
   "default":
   {
     "httpProxy": "http://192.168.1.12:3128",
     "httpsProxy": "http://192.168.1.12:3128",
     "noProxy": "*.test.example.com,.example2.com,127.0.0.0/8"
   }
 }
}
```
- 局部代理(指定容器使用代理)
```bash
# 使用宿主机代理(进入容器内部执行)
export ALL_PROXY=http://host.docker.internal:7890
```
### 代码中设置代理
- `Python`
```python
import os
os.environ["http_proxy"] = "http://10.14.129.235:8888"
os.environ["https_proxy"] = "http://10.14.129.235:8888"
```