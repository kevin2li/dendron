# 简介

Samba协议是一种文件共享协议，用于在不同操作系统之间共享文件和打印机。它允许Linux和Unix系统与Windows系统之间进行文件和打印机共享。Samba协议是开放源代码的，它的实现是基于SMB/CIFS协议。Samba协议是一种客户端/服务器协议，它使用TCP/IP协议进行通信。Samba协议支持许多不同的操作系统，包括Windows、Linux、Unix、Mac OS等。

自1992年以来，Samba一直为所有使用SMB/CIFS协议的客户端（例如所有版本的DOS和Windows，OS/2，Linux和许多其他客户端）提供安全、稳定、快速的文件和打印服务。

docker镜像： https://hub.docker.com/r/dperson/samba  

<!-- more -->

# 方法
## 使用Docker安装
1. 配置docker、docker-compose环境  
参考：https://blog.kevin2li.top/post/29

2. 编写docker compose文件
```bash
mkdir -p ~/docker-apps/samba
cd ~/docker-apps/samba
vim docker-compose.yaml
```
`docker-compose.yaml`内容如下：

```yaml
version: '3'

services:
  samba:
    image: dperson/samba
    container_name: samba
    environment:
      TZ: 'Asia/Shanghai'
      USER: "smb_user;password1"
      USER2: "smb_admin;password2"
    networks:
      - default
    ports:
      - "137:137/udp"
      - "138:138/udp"
      - "139:139/tcp"
      - "445:445/tcp"
    read_only: true
    tmpfs:
      - /tmp
    restart: unless-stopped
    stdin_open: true
    tty: true
    volumes:
      - './data1:/mount1'
      - './data2:/mount2'
      - './conf:/etc/samba'
    command: '-p'

networks:
  default:
```

3. 填写配置文件
```bash
mkdir conf
vim conf/smb.conf
```
`conf/smb.conf`内容如下：

```ini
# This is the main Samba configuration file. You should read the
# smb.conf(5) manual page in order to understand the options listed
# here. Samba has a huge number of configurable options (perhaps too
# many!) most of which are not shown in this example
#
# For a step to step guide on installing, configuring and using samba, 
# read the Samba-HOWTO-Collection. This may be obtained from:
#  http://www.samba.org/samba/docs/Samba-HOWTO-Collection.pdf
#
# Many working examples of smb.conf files can be found in the 
# Samba-Guide which is generated daily and can be downloaded from: 
#  http://www.samba.org/samba/docs/Samba-Guide.pdf
#
# Any line which starts with a ; (semi-colon) or a # (hash) 
# is a comment and is ignored. In this example we will use a #
# for commentry and a ; for parts of the config file that you
# may wish to enable
#
# NOTE: Whenever you modify this file you should run the command "testparm"
# to check that you have not made any basic syntactic errors. 
#
#======================= Global Settings =====================================
[global]
   workgroup = MYGROUP
   server string = Samba Server
   server role = standalone server
   ; guest account = pcguest
   log file = /dev/stdout
   max log size = 50
   dns proxy = no 

   pam password change = yes
   map to guest = bad user
   usershare allow guests = yes
   create mask = 0664
   force create mode = 0664
   directory mask = 0775
   force directory mode = 0775
   force user = smbuser
   force group = smb
   follow symlinks = yes
   load printers = no
   printing = bsd
   printcap name = /dev/null
   disable spoolss = yes
   strict locking = no
   aio read size = 0
   aio write size = 0
   vfs objects = catia fruit recycle streams_xattr
   recycle:keeptree = yes
   recycle:maxsize = 0
   recycle:repository = .deleted
   recycle:versions = yes

   # Security
   client ipc max protocol = SMB3
   client ipc min protocol = SMB2_10
   client max protocol = SMB3
   client min protocol = SMB2_10
   server max protocol = SMB3
   server min protocol = SMB2_10

   # Time Machine
   fruit:delete_empty_adfiles = yes
   fruit:time machine = yes
   fruit:veto_appledouble = no
   fruit:wipe_intentionally_left_blank_rfork = yes

include = /etc/samba/%U.smb.conf

[共享文件夹1]
   path = /mount1/
   browsable = yes
   read only = no
   guest ok = no
   admin users = smb_user,smb_admin
   read list = smb_user,smb_admin
   write list = smb_user,smb_admin
   comment = 共享文件夹1的说明
```
5. 启动
```bash
docker compose up -d
```

## 裸机安装
参考：https://ubuntu.com/tutorials/install-and-configure-samba#2-installing-samba

1. 安装
``` bash 
sudo apt update
sudo apt install samba
```

2. 创建共享目录

```bash
mkdir /home/samba/public
```

3. 修改配置文件: `/etc/samba/smb.conf`
``` ini
# 定义共享目录及权限
[public]
  path = /home/samba/public
  comment = public directory
  browsable = yes
  read only = no
  writable = yes
  valid users = user1,user2
  create mask = 0666 # 创建文件权限
  directory mask = 0777 # 创建目录权限
  guest ok = yes
```

权限说明：
- `browsable`: 用于定义共享目录是否可浏览。如果设置为Yes，则共享目录可以被浏览，用户可以在网络上看到该共享目录，并访问其中的文件和子目录。如果设置为No，则共享目录不可以被浏览，用户无法看到该共享目录，也无法访问其中的文件和子目录。

- `read only`：指定共享目录是否只读。如果设置为Yes，则用户只能读取共享目录中的文件和目录，不能进行创建、修改和删除操作。如果设置为No，则用户可以进行读写操作。

- `writable`：指定共享目录是否可以被写入。如果设置为Yes，则用户可以进行创建、修改和删除操作。如果设置为No，则用户只能读取共享目录中的文件和目录，不能进行写入操作。

4. 启动服务
``` bash 
# 启动服务
sudo systemctl start smbd

# 查看服务状态
sudo systemctl status smbd
```

5. 防火墙放行
``` bash 
sudo firewall-cmd --permanent --zone=public --add-service=samba
sudo firewall-cmd --reload
```
6. 添加用户

由于samba不使用系统账户的密码，需要单独为用户指定samba密码。

``` bash 
# 设置smb密码
sudo smbpasswd -a username

# 查看samba用户列表
sudo pdbedit -w -L
```

7. 连接

- Windows

路径：`\\{server-ip}\{dir}`  

可以`Win+R`输入，或者在文件资源管理器地址栏输入。

为了访问方便，还可以将其加入网络位置。

![](https://minio.kevin2li.top/image-bed/blog/20230521210408.png)

![](https://minio.kevin2li.top/image-bed/blog/20230521210106.png)

- Linux  

路径：`smb://{server-ip}/{dir}`

打开文件管理器:

![](https://minio.kevin2li.top/image-bed/blog/20230528112248.png)

![](https://minio.kevin2li.top/image-bed/blog/20230528112357.png)

挂载成功

![](https://minio.kevin2li.top/image-bed/blog/20230528112613.png)

- Mac  

路径：`smb://{server-ip}/{dir}`

![](https://minio.kevin2li.top/image-bed/blog/20230528091742.png)

![](https://minio.kevin2li.top/image-bed/blog/20230528092723.png)

![](https://minio.kevin2li.top/image-bed/blog/20230528092910.png)
