# 简介
Frp是一个高性能的内网穿透反向代理应用，可以将内网服务访问端口映射到公网机器指定端口上，这样便可以在公网环境下访问到内网的服务,包括但不限于：
- 各类web服务(个人网站、文件共享等)
- SSH
- 远程桌面
- ...

通过它，你可以自由访问家中的电脑、路由器、摄像头等各种设备。
# 基本原理
如下是frp的基本原理图，其中下方的虚线框是位于内网机器上的各类服务，中间的椭圆框是拥有公网IP的机器，上方的圆角矩形框是位于公网环境下的普通用户。可以看到，用户能够访问到内网服务都是要通过中间的公网机器中转来实现的。

![](https://minio.kevin2li.top/image-bed/vanblog/img/530fc52d6aed332e6c281b8cdc6f9187.20221019102104.png)

<!-- more -->

# 安装
项目地址：https://github.com/fatedier/frp
1. 首先去项目[Release](https://github.com/fatedier/frp/releases)版块下载适合自己平台的最新的安装包, 当前的最新版是0.44。

![](https://minio.kevin2li.top/image-bed/vanblog/img/922ccfe1b121efcb8ecaaa118ca704cb.20221019103417.png)

我选用的是`linux_amd64`平台的, 可以通过下面命令下载：
```bash
wget https://github.com/fatedier/frp/releases/download/v0.44.0/frp_0.44.0_linux_amd64.tar.gz
```
注意: 在内网机器和公网机器上都需要下载frp安装包

2. 解压下载的压缩包  
可以看到里面包含如下内容：

![](https://minio.kevin2li.top/image-bed/vanblog/img/4466daf6df51f4c94d56acf0434bbd9b.20221019123139.png)

一共7个文件，可分为三组：

内网机器上使用：
- fprc: frp客户端可执行文件
- frpc.ini：frpc的配置文件，内网机器上各种内网穿透服务的设置都是修改这个文件控制的
- frpc_full.ini：frpc的完整配置文件

公网机器上使用：
- frps：frp服务端可执行文件
- frps.ini：frps的配置文件
- frps_full.ini：frps的完整配置文件

许可证文件：
- License：使用Apache许可证

# 基本使用
下面以一个具体场景为例来说明frp的使用方法。

:::info{title="假设场景"}
我在内网上有多台机器A，B，C，有一台公网机器D，其公网IP为`x.x.x.x`，现在我在内网机器A上新开了一个web服务，取名叫`my_web_service`, 访问端口为8000，如何使其可通过公网访问？
:::
**使用方法：**
1. 内网机器A上的设置：  
首先查看一下当前默认的`frpc.ini`的配置：
```ini
[common]
server_addr = 127.0.0.1
server_port = 7000

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6000
```
其中`common.server_addr`表示需要改为自己的公网机器的IP: `x.x.x.x`，

:::tip{title="提示"}
`common.server_addr`是frps与frpc程序之间通信的端口，如果为了更安全，也可以改为其他高端口，服务端frps.ini也要同步修改，无所谓的话可以直接忽略。
:::


默认的配置文件中自带了一个`ssh`的内网穿透服务，其表示将内网机器的22端口(ssh应用默认端口)映射到公网机器的6000端口。

现在为了添加自己的其他服务，我们在`frpc.ini`文件尾部再新增一个配置项，内容如下：
```ini
[my_web_service]
type = tcp
local_ip = 127.0.0.1
local_port = 8000  # 内网机器服务访问端口
remote_port = 8000 # 映射到公网机器的端口
```
目前完整的`frpc.ini`文件内容如下：
```ini
[common]
server_addr = x.x.x.x # 公网IP地址
server_port = 7000

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6000

[my_web_service]
type = tcp
local_ip = 127.0.0.1
local_port = 8000  # 内网机器服务访问端口
remote_port = 8000 # 映射到公网机器的端口
```
:::warning{title="注意"}
这里设置的`server_port`和所有服务的`remote_port`都要在公网机器上保持开放状态，否则会导致连接失败。
(如果觉得在服务器上开放太多端口不安全，后面可以使用nginx等工具设置反向代理,这样公网服务器只需暴露少数几个常用入口端口即可)
:::
2. 公网机器D上的设置：  
- **确保云服务器安全组策略里开放了相应端口**  
不同云服务器厂商设置可能不太一样，下面是我用的腾讯云服务器的示例：

![](https://minio.kevin2li.top/image-bed/vanblog/img/8c0ae72c2a98a176eb9cbd8b2be82f80.20221019110457.png)

因为我在服务器上另外装了防火墙，所以这里允许所有的流量进入。
- **确保防火墙开放了相应端口**  
防火墙管理相关命令：
```bash
# 安装防火墙
sudo apt update
sudo apt install firewalld

# 查看已开放端口
sudo firewall-cmd --permanent --zone=public --list-ports

# 添加端口
sudo firewall-cmd --permanent --zone=public --add-port 8000/tcp

# 移除端口
sudo firewall-cmd --permanent --zone=public --remove-port 8000/tcp
```
大家核对下自己映射到公网服务器的端口是否处于放行状态，没有的话按照上面的命令添加一下。
- 修改配置文件

首先查看一下当前默认的`frps.ini`
```ini
[common]
bind_port = 7000
```

增加管理后台：
```ini
[common]
bind_port = 7000

dashboard_port = 9000 # dashboard访问端口
dashboard_user = admin
dashboard_pwd = admin
```

3. 测试

先启动frps，再启动frpc。
```bash
# 公网机器(在frp安装目录下执行)
./frps -c frps.ini

# 内网机器(在frp安装目录下执行)
./frpc -c frpc.ini
```

如果顺利的话，现在应该能够通过`x.x.x.x:8000`访问内网机器上的服务了
举例：
- 如果你的服务是web:
浏览器访问`x.x.x.x:8000`应该能打开对应的网页
- 如果你的服务是ssh：
可以通过下面命令连接上内网机器
```bash
ssh -oPort=6000 username@x.x.x.x
```
- 如果你的服务是微软远程桌面：
你可以这样连接:

![](https://minio.kevin2li.top/image-bed/vanblog/img/baba663ee3fc3ea8f293dfb8626ded0c.20221019135553.png)
- ...
你还可以访问`x.x.x.x:9000`来查看所有内网穿透服务的连接状态等信息

![](https://minio.kevin2li.top/image-bed/vanblog/img/b566f75561af8bf1abac25e33b73bb88.20221019133335.png)

4. 后台运行  
为了让程序一直挂在后台运行，可以使用`nohup`命令，不过更推荐的做法是下面章节介绍的服务化，更方便管理。
```bash
# frpc
nohup ./frpc -c frpc.ini >frpc.log 2>&1 &

# frps
nohup ./frps -c frps.ini >frps.log 2>&1 &
```

# 进阶使用
## 服务化
为了方便frp应用的管理，将其编写为系统服务，方便管理状态(启动、停止、开机自启等)。
### 客户端服务配置

编写如下两个文件，将`<your_frp_dir>`替换为你的frp绝对安装路径。
1. `/etc/systemd/system/frpc.service`
```ini
[Unit]
Description=frpc service
After=network.service

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/root
ExecStart=sh <your_frp_dir>/frpc_start.sh
PrivateTmp=true
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
2. `<your_frp_dir>/frpc_start.sh`:
```bash
cd <your_frp_dir>
./frpc -c frpc.ini >frps.log 2>&1
```

frpc服务管理：
```bash
# 重新加载服务(每次添加新服务后，都要先执行下此命令)
sudo systemctl daemon-reload
# 启动
sudo systemctl start frpc
# 停止
sudo systemctl stop frpc
# 查看状态
sudo systemctl status frpc
# 设置开机自启
sudo systemctl enable frpc
# 取消开机自启
sudo systemctl disable frpc
```

### 服务端服务配置
编写如下两个文件，将`<your_frp_dir>`替换为你的frp绝对安装路径。
1. `/etc/systemd/system/frps.service`
```ini
[Unit]
Description=frps service
After=network.service

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/root
ExecStart=sh <your_frp_dir>/frps_start.sh
PrivateTmp=true
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
2. `<your_frp_dir>/frps_start.sh`
```bash
cd <your_frp_dir>
./frps -c frps.ini >frps.log 2>&1
```

frps服务管理：
```bash
# 重新加载服务(每次添加新服务后，都要先执行下此命令)
sudo systemctl daemon-reload
# 启动
sudo systemctl start frps
# 停止
sudo systemctl stop frps
# 查看状态
sudo systemctl status frps
# 设置开机自启
sudo systemctl enable frps
# 取消开机自启
sudo systemctl disable frps
```

## 域名访问
当设置的内网穿透应用逐渐增多后，每次访问不同的服务都要输入公网IP和对应的端口号，感觉不是太方便，也不太优雅。由于没有设置https，安全性也没有保证。综合考虑，决定给不同的应用分配一个域名，并升级为https来解决上面的问题。关于这部分内容下期再介绍。
