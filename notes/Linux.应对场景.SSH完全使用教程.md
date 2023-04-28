---

id: znr93qj63atdv9d3ywquziu
title: SSH完全使用教程
desc: ''
updated: 1682656686008
created: 1682483879682
tag: 
  - ssh
---

## 简介

SSH（安全外壳协议）是一种加密的网络传输协议，可在不安全的网络中为网络服务提供安全的传输环境。它通过在网络中创建安全隧道来实现SSH客户端和服务器之间的连接。最早的时候，互联网通信都是明文通信，一旦被截获，内容就会被暴露。1995年，芬兰学者Tatu Ylonen设计了SSH协议，将登录信息全部加密，成为互联网安全的一个基本解决方案，迅速在全世界获得推广，目前已经成为所有操作系统的标准配置。

## 安装

### Windows

1.  Openssh

:::info 安装 OpenSSH
参考：[安装 OpenSSH \| Microsoft Learn](https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse)

若要安装 OpenSSH 组件：

1.  打开"设置"，选择"应用"\>"应用和功能"，然后选择"可选功能" 。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/8913cd5522dc757fdd0cdcfae266e9b4.image.png)
2. 扫描列表，查看是否已安装 OpenSSH。 如果未安装，请在页面顶部选择"添加功能"，然后：

-   查找"OpenSSH 客户端"，再单击"安装"\
-   查找"OpenSSH 服务器"，再单击"安装"

设置完成后，回到"应用"\>"应用和功能"和"可选功能"，你应会看到已列出 OpenSSH。
:::

<!-- more -->

1.  Copssh

Copssh功能更全面，弥补了上面Openssh在某些参数上不支持的不足(如`ControlMaster`等)。

:::info Copssh介绍
Copssh 是一个用于 Windows 系统的 OpenSSH 服务器和客户端实现。它打包了便携式 OpenSSH、Cygwin 和一些流行的实用程序，并实现了一些关于安全性的最佳实践。您可以使用 Copssh 进行远程管理您的系统或以安全的方式收集远程信息。

官网：https://www.itefix.net/copssh
:::

### Ubuntu

很多设备默认都安装了ssh客户端程序，如果需要让别的机器登录到本机，则还需要安装服务端程序。

``` bash
sudo apt install openssh-server
```

## 常用命令

### 基本参数介绍

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/7721142d6d5b6bcb8406b1ff14970189.image.png)

:::info 常用参数

-   `-C`: 数据压缩
-   `-f`:后台运行
-   `-N`: 只转发端口，不执行远程命令
-   `-g`: 允许远程主机连接到本地转发端口
-   `-T`: 禁止终端分配
-   `-J`: 设置跳板机
-   `-X`: 允许x11转发
-   `-v`：显示详细日志
-   `-o`: 设置选项，如`-o Port=22`

``` bash
# 举例：本地端口转发
ssh -CNfTL 9999:localhost:8000 user@host

# 举例：远程端口转发(使用场景：可以在云服务器上使用本机的科学上网代理)
ssh -CNfTR 9150:localhost:8888 temp@39.108.XXX.XXX
```

:::

### 登录

#### 直接登录

``` bash
# Connect to a remote server:
ssh {{username}}@{{remote_host}}

# Connect to a remote server with a specific identity (private key):
ssh -i {{path/to/key_file}} {{username}}@{{remote_host}}

# Connect to a remote server using a specific port:
ssh {{username}}@{{remote_host}} -p {{2222}}
```

#### 使用代理登录

为了能够从外部访问内网的机器，有时需要进行内网穿透，将内网机器的ssh端口映射到一台公网机器的指定端口上，但是这样很有可能会遭到外网的恶意机器通过公网暴露的端口对内网机器进行弱口令爆破。安全起见，公网机器的端口暴露越少越好，因此考虑设置代理服务器，让自己的受信任设备通过代理服务器登录，这样映射的ssh端口可以不用暴露到公网，只用暴露代理服务器的一个端口即可。

1.  云服务器搭建socks代理服务

参考：https://www.digitalocean.com/community/tutorials/how-to-set-up-dante-proxy-on-ubuntu-20-04
1) 安装：

``` bash
sudo apt update
sudo apt install dante-server
```

2) 验证：

``` bash
systemctl status danted.service
```

3) 配置

配置文件路径：`/etc/danted.conf`

``` yaml
logoutput: syslog
user.privileged: root
user.unprivileged: nobody

# The listening
network interface or address.
internal: 0.0.0.0 port=10080

# The proxying network interface or address.
external: eth0

# socks-rules determine what is proxied through the external interface.
socksmethod: username

# client-rules determine who can connect to the internal interface.
clientmethod: none

client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
}

socks pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
}
```

重启服务：

``` bash
sudo systemctl restart danted.service
```

4) 开放端口：

``` bash
# 端口与配置文件指定的端口一致
sudo firewall-cmd --permanent --zone=public --add-port 10080/tcp
sudo firewall-cmd --reload
```

5) 创建用户

``` bash
sudo useradd -r -s /bin/false your_dante_user
sudo passwd your_dante_user
```

6) 测试

``` bash
curl -v -x socks5://your_dante_user:your_dante_password@your_server_ip:10080 http://www.baidu.com/
```

2.  客户端登录

1) 安装`ncat`
- Ubuntu

``` bash
sudo apt update
sudo apt install ncat
```

-   Windows

下载： https://nmap.org/download.html#windows

2) 连接：

-   命令行：

``` bash
ssh -o "ProxyCommand ncat --proxy-type socks5 --proxy <proxy_ip>:<proxy_port> %h %p --proxy-auth <proxyuser>[:pass]" -p 11005 kevin2li@localhost
```

-   配置文件：`~/.ssh/config`:

``` yaml
Host PC
    HostName localhost
    Port 11005
    User kevin2li
    ProxyCommand ncat --proxy-type socks5 --proxy <proxy_ip>:<proxy_port> %h %p --proxy-auth <proxy_user>:<password>
```

可使用下面命令连接：

``` bash
ssh PC
```

### 密钥管理

#### 生成密钥

``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"

# If you are using a legacy system that doesn't support the Ed25519 algorithm, use:
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

#### 拷贝密钥到服务器

-   Linux

``` bash
# Copy your keys to the remote machine:
ssh-copy-id {{username@remote_host}}

# Copy the given public key to the remote:
ssh-copy-id -i {{path/to/certificate}} {{username}}@{{remote_host}}

# Copy the given public key to the remote with specific port:
ssh-copy-id -i {{path/to/certificate}} -p {{port}} {{username}}@{{remote_host}}
```

-   Windows

方式一:

``` sh
# ed25519公钥
cat $env:USERPROFILE\.ssh\id_ed25519.pub | ssh {{username}}@{{remote_host}} "cat - >> .ssh/authorized_keys"

# rsa公钥
cat $env:USERPROFILE\.ssh\rsa.pub | ssh {{username}}@{{remote_host}} "cat - >> .ssh/authorized_keys"
```

方式二：

``` bash
# ed25519公钥
ssh {{username}}@{{remote_host}}  "cat - >> ~/.ssh/authorized_keys" <  ~/.ssh/id_ed25519.pub

# rsa公钥
ssh {{username}}@{{remote_host}}  "cat - >> ~/.ssh/authorized_keys" <  ~/.ssh/id_rsa.pub
```

### 隧道搭建

参考：https://phoenixnap.com/kb/ssh-port-forwarding

#### 本地转发

作用：将本地端口的请求转发的远程主机上

格式：

``` bash
ssh -L local_port:destination_server_ip:remote_port ssh_server_hostname
```

举例：

``` bash
ssh –L 5901:188.17.0.5:4492 pnap@ssh.server.com
```

#### 远程转发

作用：将远程端口的请求转发的本地主机上\
格式：

``` bash
ssh -R remote_port:localhost:local_port ssh_server_hostname
```

举例：

``` bash
ssh –R 8080:localhost:5534 pnap@ssh.server.com
```

#### 动态转发

作用：可视为本地转发特殊形式，本地转发是一对一，这个可以一对多

格式：

``` bash
ssh –D local_port ssh_server_hostname
```

举例：

``` bash
ssh –D 5534 pnap@ssh.server.com
```

::: tip{title="使用场景举例"}
可以将其作为代理使用，如图，主机A通过主机B代理上外网：

![drawio.png](https://minio.kevin2li.top/image-bed/vanblog/img/273658d0ed35bf517dd0d87c6caf58b7.%C3%A6%C2%9C%C2%AA%C3%A5%C2%91%C2%BD%C3%A5%C2%90%C2%8D%C3%A7%C2%BB%C2%98%C3%A5%C2%9B%C2%BE-%C3%A7%C2%AC%C2%AC%2014%20%C3%A9%C2%A1%C2%B5.drawio.png)

``` bash
# hostA执行
ssh -D 9999 userB@hostB
# hostA测试
curl -v -x socks5://localhost:9999 https://www.baidu.com
```

将本地主机A发往9999端口的网络请求通过隧道传输到主机B，主机B解析出网络请求的目标地址后，代理访问目标并将结果通过隧道返回给主机A。

注意：为了使所有的网络请求走代理进入隧道，需要在系统设置或浏览器设置里配置好socks代理
:::

#### X协议转发

作用：将服务器上带有图形化界面(GUI)的程序转发到本地

参考: https://kb.iu.edu/d/bdnt

### 文件传输

-   `scp`

``` bash
# Copy a local file to a remote host:
scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}

# Use a specific port when connecting to the remote host:
scp -P {{port}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}

# Copy a file from a remote host to a local directory:
scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}

# Recursively copy the contents of a directory from a remote host to a local directory:
scp -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}

# Copy a file between two remote hosts transferring through the local host:
scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_directory}}

# Use a specific username when connecting to the remote host:
scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_directory}}

# Use a specific ssh private key for authentication with the remote host:
scp -i {{~/.ssh/private_key}} {{local_file}} {{remote_host}}:{{/path/remote_file}}
```

-   `rsync`

``` bash
# Transfer file from local to remote host:
rsync {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}

# Transfer file from remote host to local:
rsync {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}

# Transfer file in [a]rchive (to preserve attributes) and compressed ([z]ipped) mode with [v]erbose and [h]uman-readable [P]rogress:
rsync -azvhP {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}

# Transfer a directory and all its children from a remote to local:
rsync -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}

# Transfer directory contents (but not the directory itself) from a remote to local:
rsync -r {{remote_host}}:{{path/to/remote_directory}}/ {{path/to/local_directory}}

# Transfer a directory [r]ecursively, in [a]rchive to preserve attributes, resolving contained soft[l]inks , and ignoring already transferred files [u]nless newer:
rsync -rauL {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}

# Transfer file over SSH and delete remote files that do not exist locally:
rsync -e ssh --delete {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}

# Transfer file over SSH using a different port than the default and show global progress:
rsync -e 'ssh -p {{port}}' --info=progress2 {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}
```

-   `sshfs`

安装：

``` bash
# For Ubuntu
sudo apt update
sudo apt install sshfs
```

挂载目录：

参考：[How To Use SSHFS to Mount Remote File Systems Over SSH](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)

``` bash
sudo mkdir /mnt/droplet
sudo sshfs -o allow_other,default_permissions sammy@your_other_server:~/ /mnt/droplet
```

### 跳板机

参考： https://goteleport.com/blog/ssh-proxyjump-ssh-proxycommand/
- 命令行

``` bash
# 使用ProxyJump(推荐)
ssh -J <jump server1>,<jump server2>,<jump server3> <remote server>
ssh -J <user@jump-host:port> <user@remote-target:port> <remote server>
# e.g.
ssh -J kevin2li@192.168.2.121 -p 24 likai@10.14.132.126

# 使用ProxyCommand
ssh -o ProxyCommand="ssh -W %h:%p <jump server>" <remote server>
# e.g.
ssh -o ProxyCommand="ssh -W %h:%p kevin2li@192.168.2.121" -p 24 likai@10.14.132.126
```

-   配置文件

场景：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/bb0c4301d1af94203123536352b3f817.image.png)

在配置文件`~/.ssh/config`中可按如下配置：

``` yaml
Host remoteserver
  HostName 192.168.200.200
  User dev
  IdentityFile ~/.ssh/<your_key>
  Port 2048
  ProxyJump jumpserver

Host jumpserver
  Hostname <jumpserver_ip>
  User <user_name>
```

使用下面命令即可登录：

``` bash
ssh remoteserver
```

## 配置文件

### 系统服务配置文件

配置文件路径：`/etc/ssh/sshd_config`

常用配置：

``` bash
Port 22
PubkeyAuthentication yes
# PermitRootLogin yes

# 是否允许密码登录：To disable tunneled clear text passwords, change to no here!
PasswordAuthentication no

X11Forwarding yes

# 保活
ClientAliveInterval 60
ClientAliveCountMax 60
```

### 个人配置文件

配置文件路径：`~/.ssh/config`

示例如下：

``` yaml
Host *
  TCPKeepAlive yes
  Compression yes
  ForwardAgent yes
  IdentityFile ~/.ssh/id_ed25519
  
  # 保活
  ServerAliveInterval 60
  ServerAliveCountMax 60
  
  # 多路复用(windows暂不支持)
  # ControlMaster auto
  # ControlPath ~/.ssh/control:%h:%p:%r
  # ControlPersist 1h
  
Host Server
  HostName 192.168.2.121
  User kevin2li
  Port 22
```

完整参数可详见：https://man.openbsd.org/ssh_config.5

::: info{title="SSH多路复用"}
参考：https://docs.cci.rpi.edu/examples/Advanced_SSH/
:::

这样就可以通过下面命令简化登录：

``` bash
ssh Lab
```

## 日志查看

``` bash
journalctl -u ssh

# 查看最近登陆的记录
last

# 查看到登陆失败的记录
lastb

# 查看最近登陆的记录
lastlog

# 检查当前在线用户
who
```

可以检查的文件：
- `/var/log/auth.log`
- `/var/log/secure`

## 安全增强

为了防止被弱口令爆破，常见的可以通过修改默认登录端口、关闭密码登录方式、使用第三方拦截软件等方式来提高安全性。

### 1. 修改SSH默认的22端口

1.  编辑配置文件`/etc/ssh/sshd_config`:

``` bash
sudo vim /etc/ssh/sshd_config
```

2.  修改配置文件：

``` yaml
# 改为>1024的其他端口号
Port 8022
```

3.  重启sshd服务

``` bash
sudo systemctl restart sshd
```

### 2. 关闭密码登录，采用密钥登录

1.  编辑配置文件`/etc/ssh/sshd_config`:

``` bash
sudo vim /etc/ssh/sshd_config
```

2.  修改配置文件：

``` yaml
# 禁用密码验证
PasswordAuthentication no

# 启用密钥验证
PubkeyAuthentication yes
```

3.  重启sshd服务

``` bash
sudo systemctl restart sshd
```

4.  验证：

通过密码登录被拒绝，则为成功。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/505f1dd7fed0f2140c490791c5aefafe.image.png)

### 3. 使用第三方的拦截软件

比如：[Fail2ban](https://github.com/fail2ban/fail2ban)。
