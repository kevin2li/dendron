---
id: 8jlo6kijuuk6ye2a90uqp2m
title: 使用mkcert签发本地自签名证书教程
desc: ''
updated: 1684845557237
created: 1684838428137
---


## 简介
mkcert可以在本地生成自签名证书，这些证书可以被本地信任，并且可以用于本地开发、测试和调试HTTPS应用程序，避免了使用公共CA证书的安全性和费用问题。

mkcert的主要特点包括：

- **本地信任**：mkcert生成的证书可以被本地信任，避免了使用公共CA证书的安全性和费用问题。

- **自签名证书**：mkcert可以在本地生成自签名证书，可以用于本地开发、测试和调试HTTPS应用程序。

- **多平台支持**：mkcert可以运行在多种操作系统上，如Windows、macOS、Linux等，可以满足不同平台和环境的需求。

- **简单易用**：mkcert使用简单，只需要几个命令即可生成证书，并且可以与常见的Web服务器集成，如Apache、Nginx等。

- **安全性**：mkcert生成的证书采用了最新的加密算法和安全标准，保证了生成的证书的安全性和可靠性。

- **免费开源**：mkcert是一款开源的工具，可以免费使用和分发，没有任何使用限制和费用。

总之，mkcert是一款功能强大的本地信任SSL/TLS证书生成工具，可以帮助用户生成本地信任的SSL/TLS证书，避免了使用公共CA证书的安全性和费用问题，具有简单易用、安全可靠、免费开源等特点，是现代Web开发中不可或缺的工具之一。

Github: https://github.com/FiloSottile/mkcert  

## 安装

下载二进制： https://github.com/FiloSottile/mkcert/releases

注： 该工具是个命令行工具，没有图形界面，需要在终端中使用。


## 使用

### 参数说明
![](https://minio.kevin2li.top/image-bed/blog/20230523184812.png)


### 安装根证书
``` powershell
.\mkcert-v1.4.4-windows-amd64.exe -install
```
命令执行后会出现弹窗：

![](https://minio.kevin2li.top/image-bed/blog/20230523185000.png)

选择“是”，即可安装证书到系统。

验证：

`Win+R`打开运行窗口，输入`certmgr.msc`回车打开证书管理器。

![](https://minio.kevin2li.top/image-bed/blog/20230523185313.png)

可以看到，根证书被安装到本地计算机的"受信任的根证书颁发机构"存储库中。

![](https://minio.kevin2li.top/image-bed/blog/20230523185919.png)

### 签发证书

mkcert支持生成下面类型的证书：
- "example.com"
- "*.example.com"
- "example.test"
- "localhost"
- "127.0.0.1"
- "::1"

以`app-local.kevin2li.top`为例，可以通过下面命令签发：

``` powershell 
.\mkcert-v1.4.4-windows-amd64.exe app-local.kevin2li.top
```

可以看到，它会在当前目录下生成`pem`格式的证书文件和密钥文件。

![](https://minio.kevin2li.top/image-bed/blog/20230523190155.png)

此外，它还可以一次签发多个域名证书以及泛域名证书。

### 分发根证书

为了让局域网内其他设备能够使用，我们需要将根证书分发到局域网其他机器上，可以通过下面命令查看根证书路径：

``` powershell
.\mkcert-v1.4.4-windows-amd64.exe -CAROOT
```

![](https://minio.kevin2li.top/image-bed/blog/20230523190859.png)

将`rootCA.pem`复制并重命名为`rootCA.crt`，这样windows设备直接双击就可以安装了。

![](https://minio.kevin2li.top/image-bed/blog/20230523191431.png)

在选择证书存储路径时，要选择“受信任的根证书颁发机构”

![](https://minio.kevin2li.top/image-bed/blog/20230523191757.png)

### 使用自签证书
前面我们签发了一个`app-local.kevin2li.top`的证书，下面来使用它。  

先准备一段python代码。

``` python
# ~/mkcert/main.py
import http.server
import ssl

# 配置服务器参数
HOST = 'app-local.kevin2li.top'
PORT = 443
CERTFILE = './app-local.kevin2li.top.pem'  # SSL证书文件路径
KEYFILE = './app-local.kevin2li.top-key.pem'   # SSL证书私钥文件路径

# 创建HTTP服务器
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer((HOST, PORT), handler)

# 添加SSL支持
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=CERTFILE, keyfile=KEYFILE, server_side=True)

# 启动服务器
print(f'Starting HTTPS server on https://{HOST}:{PORT}')
httpd.serve_forever()
```

运行`python main.py`

![](https://minio.kevin2li.top/image-bed/blog/20230523200655.png)

**域名解析：**

由于是在内网环境下，没有公共DNS解析，也没有设置内网DNS解析服务器，简单起见，我们通过修改`hosts`文件来将域名映射到ip。

`hosts`文件路径：
- Windows系统：C:\Windows\System32\drivers\etc\hosts
- macOS系统：/private/etc/hosts
- Linux系统：/etc/hosts

在`hosts`文件最后添加下面内容，将域名映射到本机地址或内网地址(二选一)：
``` bash 
# 127.0.0.1 app-local.kevin2li.top
192.168.1.104 app-local.kevin2li.top
```

**本机浏览器访问：**

![](https://minio.kevin2li.top/image-bed/blog/20230523200615.png)

可以看到实现了内网的https访问。  

点击浏览器的地址栏旁边的小锁图标，在“连接安全”里可以看到具体的证书信息。

![](https://minio.kevin2li.top/image-bed/blog/20230523202425.png)

**局域网其他设备访问：**

通过导入根证书，并修改`hosts`文件将域名指向内网服务器ip，也可以达到一样的效果。

![](https://minio.kevin2li.top/image-bed/blog/20230523203359.png)

## 参考
1. [云创源码 | 利用mkcert快速一键自签名局域网SSL证书本地 https 实现](https://www.loowp.com/24938.html)