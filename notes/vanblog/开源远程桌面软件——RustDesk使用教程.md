# 简介
![](https://minio.kevin2li.top/image-bed/vanblog/img/901aaaa32b73193420138a46953eb05c.20221113203003.png)

RustDesk是一款开源的远程桌面软件，主要由rust语言开发，支持全平台(Windows、Max、Linux、Android等)，目前在[Github](https://github.com/rustdesk/rustdesk)上已获得高达32k的star。  
官网：https://rustdesk.com/zh/
<!-- more -->
# 背景
之所以选择这款远控软件主要是因为主流的远控软件如向日葵、todesk等均使用他们自家的公用服务器做中转，如果想要获得更高的服务质量就需要升级套餐。而这款软件可以使用自己搭建的服务器作为中继服务器，服务质量(如延迟、画质等方面)更有保障，且支持全平台。(其实，微软自带的远程桌面通过内网穿透后也可以达到类似的效果，不过仅限于windows设备使用)。因此，本教程主要介绍自己搭建服务器的用法。



# 安装与使用教程
## 前提
1. 需要一台有公网ip的机器(可以去阿里云、腾讯云等云服务器厂商购买)
2. 服务器上安装好docker、docker-compose
## 安装
1. 云服务器安全组策略里放行所有端口  
(不同服务器厂商操作不一，可自行查找设置)
2. 云服务器开放防火墙端口

:::note{title="端口说明"}
默认情况下，hbbs 监听21115(tcp), 21116(tcp/udp), 21118(tcp)，hbbr 监听21117(tcp), 21119(tcp)。务必在防火墙开启这几个端口， 请注意21116同时要开启TCP和UDP。其中21115是hbbs用作NAT类型测试，21116/UDP是hbbs用作ID注册与心跳服务，21116/TCP是hbbs用作TCP打洞与连接服务，21117是hbbr用作中继服务, 21118和21119是为了支持网页客户端。如果您不需要网页客户端（21118，21119）支持，对应端口可以不开。
:::

```bash
# 1. 先查看已开放端口
sudo firewall-cmd --permanent --zone=public --list-ports

# 2. 添加端以下口
sudo firewall-cmd --permanent --zone=public --add-port 21115/tcp
sudo firewall-cmd --permanent --zone=public --add-port 21116/tcp
sudo firewall-cmd --permanent --zone=public --add-port 21117/tcp
sudo firewall-cmd --permanent --zone=public --add-port 21118/tcp
sudo firewall-cmd --permanent --zone=public --add-port 21119/tcp
sudo firewall-cmd --permanent --zone=public --add-port 21116/udp

# 3. 重新载入
sudo firewall-cmd --reload
```
3. 使用docker运行服务  

依次执行下面命令：
```bash
mkdir rustdesk
cd rustdesk
vim docker-compose.yaml
```
其中，`docker-compose.yaml`内容如下：
```yaml
version: '3.9'
services:
    rustdesk-hbbs:
        container_name: rustdesk-hbbs
        image: rustdesk/rustdesk-server
        hostname: rustdesk-host
        network_mode: "host"
        ports:
          - "21115:21115"
          - "21116:21116"
          - "21116:21116/udp"
          - "21118:21118"
        volumes:
            - './data:/root'
        command: "hbbs -r 1.2.3.4:21117" # 注意修改为你的云服务器公网ip
        restart: 'unless-stopped'
    rustdesk-hbbr:
        container_name: rustdesk-hbbr
        image: rustdesk/rustdesk-server
        hostname: rustdesk-host
        network_mode: "host"
        ports:
          - "21117:21117"
          - "21119:21119"
        volumes:
            - './data:/root'
        command: "hbbr"
        restart: 'unless-stopped'
```
启动服务：`docker compose up -d`  
第一次启动时，程序会自动拉取镜像并启动。

:::tip{title="tips: 常用服务管理命令"}
```bash
# 启动服务
docker compose up -d
# 停止服务
docker compose down
# 重启服务
docker compose restart
```
:::
4. 客户端连接设置  
所有客户端都要连接上中继服务器，下面以windows客户端为例演示(其他平台客户端操作类似)：
- 首先，打开连接设置菜单

![](https://minio.kevin2li.top/image-bed/vanblog/img/1baeb54f81c9156d60645a49ac939a18.20221113201922.png)

- 然后，填写ID服务器的ip或域名(就是你的云服务器ip)，其余的可不填(会自动推导).

![](https://minio.kevin2li.top/image-bed/vanblog/img/adc3a60ed90d2d84ce643bec82e242ba.20221113202133.png)

当底部状态栏显示“就绪”时，说明连接中继服务器成功。
- 最后，连接一台设备测试一下

:::info{title="Ubuntu客户端设置"}
由于我的另一台设备是Ubuntu的，直接连接可能会出现下面的错误：


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/1f7a1bce238c78bed89e6000beec1adb.image.png)

下面介绍下被控端为Ubuntu时的额外设置：
1) 设置X11 display server

参考：https://askubuntu.com/questions/1260142/ubuntu-set-default-login-desktop
```bash
# 查看当前拥有的桌面环境
ls /usr/share/xsessions
# ubuntu.desktop  ubuntu-xorg.desktop
```
修改`/var/lib/AccountsService/users/<your_username>`文件内容:  
将XSession的值设置为上述桌面环境之一，名称务必保证正确，否则可能导致无法登录。
```bash
[User]
Session=
Icon=/home/kevin2li/.face
SystemAccount=false
XSession=ubuntu-xorg
[InputSource0]
xkb=us
```

2) 关闭Wayland  
在`/etc/gdm/custom.conf` 或 `/etc/gdm3/custom.conf`文件中设置如下参数：
```bash
WaylandEnable=false
```
重启服务：`sudo systemctl restart gdm3`
:::

连接成功截图：

![](https://minio.kevin2li.top/image-bed/vanblog/img/850ebf9563d75ef5e8b30bfa406d7181.20221114094153.png)