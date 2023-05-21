

# Ubuntu安装教程
参考：
- https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-22-04
## 安装桌面环境
```bash
sudo apt-get update
sudo apt install xfce4 xfce4-goodies
```
<!-- more -->

## 安装vnc
```bash
sudo apt install tigervnc-standalone-server tigervnc-xorg-extension tigervnc-viewer
```

## 配置vnc
```bash
# 新建桌面
vncserver
vncserver :1

# 关闭5901端口的桌面
vncserver -kill :1

# 列出当前桌面会话
vncserver -list

# 更改密码
vncpasswd

# 备份
mv ~/.vnc/xstartup ~/.vnc/xstartup.bak

vim ~/.vnc/xstartup
```

` ~/.vnc/xstartup`内容如下：
```bash
#!/bin/bash
xrdb $HOME/.Xresources
startxfce4 &
```

```bash
chmod +x ~/.vnc/xstartup
```
## 连接

客户端下载：https://github.com/TigerVNC/tigervnc/releases

```bash
# 建立安全隧道
ssh -L 5901:127.0.0.1:5901 -p 53217 kevin2li@kevin2li.top 
# 连接
# 地址：127.0.0.1:5901
```


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/490930c65aea873ae4d8dc52d805032a.image.png)

## 配置为系统服务
- `/etc/systemd/system/vncserver@.service`
```bash
[Unit]
Description=Start TightVNC server at startup
After=syslog.target network.target

[Service]
Type=forking
User=kevin2li
Group=kevin2li
WorkingDirectory=/home/kevin2li

PIDFile=/home/sammy/.vnc/%H:%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1280x800 -localhost :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]
WantedBy=multi-user.target
```
## 运维命令
```bash
# 重载
sudo systemctl daemon-reload
# 启动
sudo systemctl start vncserver@1
# 查看状态
sudo systemctl status vncserver@1
# 停止
sudo systemctl stop vncserver@1
```

---


# Manjaro安装教程
参考：
- https://wiki.archlinux.org/title/TigerVNC
- https://forum.manjaro.org/t/root-tip-how-to-tigervnc-over-ssh/75087
- https://archived.forum.manjaro.org/t/tigervnc-on-manjaro-arm-rpi4-running-gnome/123415/2

## 查看与安装桌面环境
```bash
# 安装
sudo pacman -S tigervnc

# 查看已有桌面环境
ls /usr/share/xsessions
# gnome-classic.desktop  gnome-classic-xorg.desktop  gnome.desktop  gnome-xorg.desktop

# 设置密码
vncpasswd

```
## 配置：`~/.vnc/config`
```bash
session=gnome
geometry=1280x720
localhost
dpi=96
```
## 配置允许用户：`/etc/tigervnc/vncserver.users`
```bash
# TigerVNC User assignment
#
# This file assigns users to specific VNC display numbers.
# The syntax is <display>=<username>. E.g.:
#
# :2=andrew
# :3=lisa
:1=kevin2li
```
## 运维命令
```bash
# 配置开机自启
systemctl enable vncserver@:1
# 重启
reboot

# 启动
vncserver :1

# 连接
# 搭建隧道
ssh WS -L 9901:localhost:5901
# vnc连接地址：localhost:9901
```