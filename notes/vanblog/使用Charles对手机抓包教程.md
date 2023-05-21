# 简介
Charles是一款HTTP代理/HTTP监视器/反向代理工具，它能够让开发人员查看他们的计算机与互联网之间的所有HTTP和SSL/HTTPS流量。这包括请求、响应和HTTP头（其中包含cookies和缓存信息）。

使用Charles，您可以截获并查看您的网络应用程序或浏览器发送和接收的所有数据，包括请求头、查询参数、cookies和缓存信息。这对于调试网络应用程序、测试API接口、分析网络性能等非常有用。


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/9ec5ddf36429ae460456e5ad117618c7.image.png)

官网：https://www.charlesproxy.com/

<!-- more -->

# 配置
## PC端设置
### 1. 安装证书
"Help>SSL Proxying>Install Charles Root Certificate"

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2595119c7f00ba1590e3a9dace24e532.image.png)

一直ok，直到  

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0b00cd4e470a36ccddbd343b05ee9807.image.png)

最后一直确定，完成。  
### 2. 查看代理ip和端口

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/239161f03df0b5856176bd46d9a29712.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/9bf0bffd95ea48a076de5e5b2fad6a93.image.png)

### 3. 设置https代理

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2840deec450718d30dc09b8767e49450.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/6c4e15a9b18bfcb8673878cfb635d47c.image.png)

## 手机端设置(以Android为例)
### 1. 设置charles为网络代理

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/5a9f695dc65e398f776000584c55aa1c.image.png)

填写pc上charles的代理  

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ae118bc20a9408343fd62f4dfbe6ca9a.image.png)

**此时，电脑上应该会收到确认连接的对话框，点击确认。**

### 2. 手机上安装证书
访问`chls.pro/ssl`,下载安装证书

# 基本使用

配置好后，应该可以看到类似下面的界面。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/54c3a14720a76ba347a59f9772de7c60.image.png)

## 如何过滤信息
1. 左下角的Filter：可以过滤出指定域名或IP
2. Ctrl+F:  

可以搜索感兴趣的域名和IP等。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/39f00cea282603d302e6498dedf17d56.image.png)

3. Focus:  

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a4f373a253c8ebd707371dfc4aea30f8.image.png)

Focus之后，关注的域名会被置顶，其余的会被统一归到"Other Hosts"中。  


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/940ad7be204faa50e81dd427257fbb97.image.png)

4. Record Settings:  


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ee4f7935271cb07a961da12a03f9e626.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/1fc38497295fc314df7b317234e9b62c.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/91d2222bb2525fdb3d50d9279513cf5e.image.png)


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/065710691c804875c8f3a7d2018cb7bb.image.png)


# 参考
1. https://blog.csdn.net/qq_45564088/article/details/121864553
