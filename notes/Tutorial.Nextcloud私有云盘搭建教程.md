---
id: xdr7xmc83rtay1xto8n8dy0
title: Nextcloud私有云盘搭建教程
desc: ''
updated: 1684307948516
created: 1682589844148
---
#  简介
Nextcloud是一款优秀的私人网盘软件，使用简单方便，特性包括：
- 数据完全自主可控，安全性高
- 免费
- 界面美观
- 插件系统丰富，包含了大量实用插件
- 支持webdav
- 支持多种文件分享方式，以及设置不同的分享权限
- 支持windows、Mac、Linux、android、IOS等多平台
- ...

![20221211191728.png](https://minio.kevin2li.top/image-bed/vanblog/img/6215d4aa3fd52eb1dab01d007ad87d07.20221211191728.png)
官网：https://nextcloud.com/  
Github: https://github.com/nextcloud  
Dockerhub: https://hub.docker.com/_/nextcloud/  

<!-- more -->

# 安装
nextcloud有多种安装方式，本教程主要介绍docker版的安装方法，其他方法可自行查阅官方文档。  
> 参考：https://github.com/nextcloud/docker  

```bash
mkdir nextcloud
cd nextcloud
vim docker-compose.yaml # 文件内容见下方
docker compose up -d
```

其中，`docker-compose.yaml`内容如下：
```yaml
version: "3.9"
services:
  nextcloud:
    container_name: nextcloud
    hostname: nextcloud-host
    image: nextcloud:latest
    privileged: true
    ports:
      - "8888:80"
    volumes:
      - ${PWD}/nextcloud-data:/var/www/html
    networks:
      - nextcloud-net
    environment:
      - NEXTCLOUD_ADMIN_USER=admin      # 设置web页面的管理员账户
      - NEXTCLOUD_ADMIN_PASSWORD=123456 # 设置web页面的管理员密码
      - MYSQL_USER=root
      - MYSQL_PASSWORD=123456
      - MYSQL_DATABASE=nextcloud
      - MYSQL_HOST=mysql-host
    depends_on:
      - mysql
    restart: "always"
  mysql:
    container_name: mysql
    hostname: mysql-host
    image: mysql:8.0
    volumes:
      - ${PWD}/mysql-data:/var/lib/mysql
    networks:
      - nextcloud-net
    environment:
      - MYSQL_ROOT_PASSWORD=123456
      - MYSQL_DATABASE=nextcloud
      - MYSQL_LOG_CONSOLE=true
    restart: "always"
networks:
  nextcloud-net:
    driver: bridge
    name: nextcloud-net
```
启动成功后，本机可通过`http://localhost:8888`进行访问。

![](https://minio.kevin2li.top/image-bed/vanblog/img/5c566def2a4e0606ab8491e9f75a3da3.20221211213702.png)

当然，正常使用过程中从外部访问的情况还是居多，所以还需要在`config/config.php`中设置`trusted_domains`以允许从外部登录，否则就可能会导致下面的错误：

![](https://minio.kevin2li.top/image-bed/vanblog/img/df9632df9b6e7bf80e25856e0a101e45.20221211220713.png)

设置方法：  
在`nextcloud-data/config/config.php`中找到`trusted_domains`字段，并根据自身情况进行修改。

```bash
sudo vim nextcloud-data/config/config.php
```
找到并修改下面条目：
```yaml
'trusted_domains' =>
array (
  0 => 'localhost',
  1 => '127.0.0.1',
  2 => 'nextcloud.xxx.com',
),
```

其他配置：

- 自动检测文件变化
```php
'filesystem_check_changes' => true,
```
# 进阶
## 外网可访问
1. 内网穿透  
如果你的nextcloud部署在内网机器上(无公网ip)，不做额外设置的话，就只能内网访问，还是不够方便。如果能够外网访问的话，随时随地都能查看自己的文件。为达到这点，我们需要一台具有公网IP的云服务器做个内网穿透，将内网机器上nextcloud服务的端口映射到云服务器上的指定端口，这样就可以通过云服务器来访问了。这类工具有很多，比如[Frp](https://blog.kevin2li.top/post/9), [nps](https://blog.kevin2li.top/post/17)等，前面都有做过教程，可自行去查看。

3. 反向代理  
在上步完成后，应该已经可以通过公网ip加端口号来访问了。但是为了设置https(windows挂载webdav目录需要)，不妨再设置一个域名，配上反向代理实现更加人性化的使用体验。

具体来说，你需要：  
- 购买域名：如`xxx.com`
- 申请ssl证书：最好泛域名证书，可通过[acme.sh](https://github.com/acmesh-official/acme.sh)申请
- 设置反向代理：如可通过`https://nextcloud.xxx.com`反向代理到`http://127.0.0.1:<port>`来访问nextcloud服务，注意设置好ssl证书

:::tip 提示  
设置https后，需要在`nextcloud-data/config/config.php`添加如下配置，否则app端可能会登录不了。
```php
'overwriteprotocol' => 'https',
'overwrite.cli.url' => 'https://nc.example.com',
'overwritehost' => 'nc.example.com',
'trusted_proxies' => ['10.0.0.1'],
'overwritecondaddr' => '^10\.0\.0\.1$',
// 'overwritewebroot' => '',
```
参考：https://docs.nextcloud.com/server/26/admin_manual/configuration_server/reverse_proxy_configuration.html

:::

## windows挂载目录
1. 获取nextcloud的webdav地址并拷贝备用  

![](https://minio.kevin2li.top/image-bed/vanblog/img/a4cf536b46a7485a10f297fefaee92e8.20221211224704.png)

2. windows设置映射网络驱动器  

windows文件资源管理器中，右击"此电脑"，选择"映射网络驱动器"(也可以选择"添加一个网络位置"，步骤类似这里不另做演示)

![](https://minio.kevin2li.top/image-bed/vanblog/img/5167ea96b62e11eff084bde97490eba8.20221211200157.png)

粘贴上一步中拷贝的webdav地址，注意协议要设置为https，否则会导致映射失败。

![](https://minio.kevin2li.top/image-bed/vanblog/img/3fd8a1c781364db61e4f2d26e18e25c3.20221211200330.png)

点击此电脑，如果出现新设置的网络驱动器，表示设置成功。

## 挂载外部目录
安装smbclient
>参考：
>1. https://github.com/nextcloud/docker/tree/master/.examples#php-module-smbclient
>2. https://cloud.tencent.com/developer/article/1754566?from=15425

1. 进入nextcloud容器并执行命令
```bash
docker exec -it nextcloud bash # 进入容器
#-------BEGIN---------
apt update
apt install smbclient libsmbclient-dev
pecl install smbclient
docker-php-ext-enable smbclient
#-------END-----------
<Ctrl>+D # 退出容器
docker commit -m "add smnbclient" nextcloud nextcloud-smbclient
```
2. 修改`docker-compose.yaml`
```yaml
version: "3.9"
    services:
        nextcloud:
        container_name: nextcloud
        hostname: nextcloud-host
        image: nextcloud-smbclient # <=== 改为安装smbclient后的镜像名称
```
重新启动：`docker compose up -d`

3. 添加外部存储
- 在插件市场下载并启用“External storage support”插件

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c4d82f649fdb8241fbafe1413a3addf6.image.png)

- 挂载外部存储
> docker运行下，需要事先在`docker-compose.yaml`中将待挂载的目录映射到容器内  

nextcloud支持挂载多种类型的外部存储，这里以挂载本地目录为例，依次填写目录名称、存储类型选择“本地”、挂载目录路径，然后确认即可。在文件标签页下出现新挂载的目录表示挂载成功。

![](https://minio.kevin2li.top/image-bed/vanblog/img/ee7e360517cf8cd7179d3031632a8505.20221211205725.png)

:::warning{title="文件权限问题"}
挂载的外部目录后，可能会出现无法新建或编辑文件的问题，即没有写权限，此时需要将外部目录的用户加入的http用户组中。
```bash
sudo  usermod -aG http <username>
```
:::
## 安装onlyoffice
1. 下载并启用"onlyoffice"插件
2. onlyoffice容器运行
> 参考：https://hub.docker.com/r/onlyoffice/documentserver/

4. 连接onlyoffice
