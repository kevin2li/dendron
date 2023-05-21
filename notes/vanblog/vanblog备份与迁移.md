# 旧设备
## 备份

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/29b58896f9d628d9413403c4a1e0bd48.image.png)

导出的文件包含如下字段：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/72dd20cdd379f67ddd16d5de126e156c.image.png)

注意： 该步骤只保留了文章图片的链接，图片文件需要自己备份。

图片目录：`~/docker_apps/vanblog/data/static/img`

<!-- more -->

# 新设备
## 启动

```bash
mkdir ~/docker-apps/vanblog
cd ~/docker-apps/vanblog
vim docker-compose.yaml
```

其中`docker-compose.yaml`内容如下：

```yaml
version: "3.9"

services:
  vanblog:
    image: mereith/van-blog:latest
    container_name: vanblog
    restart: always
    environment:
      TZ: "Asia/Shanghai"
      # 图片资源允许的域名，英文逗号分隔。作者 logo 加载不出来请检查此项。不要带协议！
      VAN_BLOG_ALLOW_DOMAINS: "www.kevin2li.top,kevin2li.top,blog.kevin2li.top"
      # 邮箱地址，用于自动申请 https 证书
      EMAIL: "kevin2li@qq.com"
    volumes:
      # 图床文件的存放地址，按需修改。
      - ${PWD}/data/static:/app/static
      # 日志文件
      - ${PWD}/log:/var/log
      # caddy 配置存储
      - ${PWD}/caddy/config:/root/.config/caddy
      # caddy 证书存储
      - ${PWD}/caddy/data:/root/.local/share/caddy
    ports:
      # 前面的是映射到宿主机的端口号，改端口的话改前面的。
      # - 80:80
      # - 443:443
      - 9000:80 # 搭隧道用
    networks:
      - internal
  mongo:
    # 某些机器不支持 avx 会报错，所以默认用 v4 版本。有的话用最新的。
    image: mongo:4.4.16
    # image: mongo:latest
    container_name: vanblog-mongo
    restart: always
    environment:
      TZ: "Asia/Shanghai"
    volumes:
      - ${PWD}/data/mongo:/data/db
    networks:
      - internal

networks:
  internal:
    driver: bridge
    name: vanblog-network
```

从旧设备上拷贝图片到新设备：

图片目录：`~/docker_apps/vanblog/data/static/img`

```bash
sudo rsync -avP <旧设备图片路径> <新设备图片路径>
```

一切准备就绪后，启动容器：
```bash
docker compose up -d
```

## 恢复

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a7a6ecf2995b412ee0c42cb3be4ad973.image.png)

## 重建分类

刚迁移过来后，分类说空的，导致主页看不到文章，需要重建一下分类。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/28fc883020ad6ceb2df942e157e4fed9.image.png)

## 添加看板娘
给博客添加看板娘。

github: https://github.com/stevenjoezhang/live2d-widget

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/03373bd1a8ebccee7f682b657606fb43.image.png)

效果：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/4ad88183b21462af904515274e9008ee.image.png)