# 简介

FreshRSS 是一款基于 PHP 编写的 RSS 服务，它是一个轻量级、界面漂亮的 RSS 阅读器，支持离线缓存，包括图片离线访问（需要使用 ImageProxyExtension 插件），支持多种语言，如英语、法语、德语、意大利语、西班牙语等。相比较同是由 PHP 编写、名气更大的 TT-RSS ，FreshRSS 的因为持续耕耘 GitHub 开源社区，功能和迭代保持的更好。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/895a18c30af87b691d56d2567d769cb4.image.png)

官网：https://www.freshrss.org/  
信息源： https://rsshub.netlify.app/  
微信公众号源： https://github.com/feeddd/feeds  

<!-- more -->

:::info{title="什么是RSS"}
RSS 的全称是 Really Simple Syndication（简易信息聚合），它是一种消息来源的格式规范，网站可以按照这种格式规范提供文章的标题、摘要、全文等信息给订阅用户，用户可以通过订阅不同网站 RSS 链接的方式将不同的信息源进行聚合，在一个工具里阅读这些内容。 RSS 阅读器是一种软件或是说一个程序，这种软件可以自由读取 RSS 和 Atom 两种规范格式的文档，且这种读取 RSS 和 Atom 文档的软件有多个版本，由不同的人或公司开发，有着不同的名字。RSS 软件能够实现大致相同的功能，其实质都是为了方便地读取 RSS 和 Atom 文档。

使用RSS的好处有很多, 以下是一些常见的好处：  
- 可以让你更快速地获取信息，不需要浏览多个网站。
- 可以让你更方便地获取信息，不需要记住多个网站的地址。
- 可以让你更加高效地获取信息，不需要等待网站加载。
- 可以让你更加自由地获取信息，不需要担心被推送广告或者被跟踪。
- 可以让你更加精准地获取信息，只需要订阅自己感兴趣的内容
- ...
:::



# 方法
1. `docker`、`docker compose`环境配置

参考：https://blog.kevin2li.top/post/29

2. 配置`docker-compose.yaml`  

如下是使用PostgreSQL数据库的示例文件：
```yaml
version: "3"

services:
  freshrss-db:
    image: postgres:latest
    container_name: freshrss-db
    hostname: freshrss-db
    restart: unless-stopped
    volumes:
      - freshrss-db:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: freshrss
      POSTGRES_PASSWORD: freshrss
      POSTGRES_DB: freshrss

  freshrss-app:
    image: freshrss/freshrss:latest
    container_name: freshrss-app
    hostname: freshrss-app
    restart: unless-stopped
    ports:
      - "8081:80"
    depends_on:
      - freshrss-db
    volumes:
      - ./data:/var/www/FreshRSS/data
      - ./extensions:/var/www/FreshRSS/extensions
    environment:
      CRON_MIN: '*/45'
      TZ: Asia/Shanghai

volumes:
  freshrss-db:
```
3. 启动
```bash
docker compose up -d
```

# 参考
1. [腾讯云-使用 Docker 部署 FreshRSS 自建专属 RSS 服务](https://cloud.tencent.com/developer/article/1964176)