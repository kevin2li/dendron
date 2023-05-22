---
created: 1682573131987
id: bwmouyxtd6gzwl1033tx4fx
title: 使用Minio与Picgo搭建个人图床
updated: 1684678667853
---

## 简介
### Minio
Minio是一款开源的对象存储服务器，可以在自己的服务器上免费部署，相比于付费的云存储服务，成本更低。使用Minio搭建个人图床，用户可以完全控制自己的数据，而不必将其存储在第三方服务提供商的服务器上，从而保护自己的隐私和数据安全。

### PicGo
PicGo是一款基于Electron的开源图片上传工具，可以方便地将本地图片上传到云存储或者自建图床。它支持多种图床，如七牛云、腾讯云、阿里云等，同时也支持自定义图床。PicGo的特点是可以自定义快捷键、自动压缩图片、支持截图上传、支持拖拽上传等功能，简单易用。PicGo也支持插件，用户可以自由地扩展功能。PicGo还有一个图床分发中心，用户可以在中心下载其他用户共享的图床配置，方便快捷。

将这两个工具结合，可以得到一个方便易用、注重隐私和安全、不用担心跑路的个人图床搭建方案。

## 方法

### Minio

#### 拉取镜像，运行容器

`docker-compose.yaml`如下：

``` yaml 
version: "3.9"

services:
  minio:
    image: minio/minio:latest
    container_name: minio
    restart: unless-stopped # always
    
    environment:
      MINIO_ROOT_USER: user
      MINIO_ROOT_PASSWORD: pass
    # 数据卷设置
    volumes:
      - ${PWD}/data:/data
      - ${PWD}/config:/root/.minio
    
    # 端口映射
    ports:
      - 9000:9000
      - 9001:9001
    command: 'server /data --console-address ":9001"'
```

> 注意: `9001`端口是网页控制台端口, `9000`是后端接口

启动：

``` bash
docker compose up -d
```

#### 配置

-   创建存储桶

![](https://minio.kevin2li.top/image-bed/Snipaste_2023-04-27_13-29-34.png)

这里设置的图床名称为`image-bed`。

![](https://minio.kevin2li.top/image-bed/20230427143555.png)

-   设置存储桶访问权限

默认新建的存储桶访问策略为`privete`，但是作为图床使用需要将其设置为`public`，其他人才能访问。

![](https://minio.kevin2li.top/image-bed/20230427142129.png)

-   创建`access key`

![](https://minio.kevin2li.top/image-bed/Snipaste_2023-04-27_13-30-31.png)

![](https://minio.kevin2li.top/image-bed/Snipaste_2023-04-27_13-31-52.png)

下载保存生成的`access key`和`secret key`

![](https://minio.kevin2li.top/image-bed/Snipaste_2023-04-27_13-32-44.png)

### 公网访问

#### nps隧道搭建

由于我的minio对象存储服务搭建在本地机器上，需要将其通过内网穿透使其可以公网访问。

本文通过[nps](https://github.com/ehang-io/nps)这一内网穿透工具实现隧道搭建，将本地的`9000`端口映射到公网云服务器的`9200`端口。

![](https://minio.kevin2li.top/image-bed/20230427144720.png)

注：同时要在云服务器开放`9200`端口

#### caddy反向代理

在`/etc/caddy/Caddyfile`中加入下面配置：

``` json
minio.example.com {
    encode gzip
    reverse_proxy 127.0.0.1:9200
}
```

重启caddy服务：

``` bash
sudo systemctl restart caddy
```

或者使用nginx:
```nginx
# minio
server {
  server_name minio.kevin2li.top;
  listen 443 ssl http2;
  ssl_certificate /etc/nginx/ssl/kevin2li.top/fullchain.cer;
  ssl_certificate_key /etc/nginx/ssl/kevin2li.top/kevin2li.top.key;
  ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
  
  # listen 80 default;
  listen 80;
  if ($scheme = http) {
    return 301 https://$host:443$request_uri;
  }

  location / {
    proxy_pass http://127.0.0.1:9200;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $http_host;
    proxy_set_header X-Forwarded-Port $server_port;
    proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection upgrade;
          proxy_set_header Accept-Encoding gzip;
    proxy_redirect http:// https://;
  }
}
```
``` bash
sudo nginx -s reload
```
#### 子域名配置

由于上面使用`minio.example.com`作为域名，需要在云服务厂商的域名控制台新建这个子域名，也可以使用[ddns](https://github.com/NewFuture/DDNS)快速配置：

``` bash
ddns --id <your_id> --token <your_token> --index4 "public" --dns "dnspod" --ipv4 "minio.example.com"
```

### PicGo

#### 安装minio插件

在插件设置中，搜索`minio`插件，点击安装即可。

![](https://minio.kevin2li.top/image-bed/20230427144902.png)

#### 配置minio图床
安装完成后，图床设置板块会多出一个MinIO图床，点击进行相关配置。 
- `endPoint`: 填写公网服务器的IP 
- `port`: 填写minio服务的端口 
- `accessKey`: 之前下载保存的文件里有 
- `secretKey`:之前下载保存的文件里有 
- `bucket`: 存储桶名称

![](https://minio.kevin2li.top/image-bed/20230427145101.png)

![](https://minio.kevin2li.top/image-bed/20230427145151.png)
填写完成后，确定即可生效。然后可以在上传区上传一张图片测试一下效果。

## 参考

1.  [掘金------Docker 搭建 Minio 对象存储服务](https://juejin.cn/post/7203258813893345340)
2.  [博客园------PicGo minio 图床](https://www.cnblogs.com/mikemhm/p/16160988.html)
