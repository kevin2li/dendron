# 方法
## 通过手机USB共享网络
参考：  
https://blog.51cto.com/u_15077549/4316908

在只有命令行界面的系统上，可以通过usb临时共享手机网络，安装相关包，然后设置无线连接
```bash
# 查看ip(应该会多一个usb0的接口)
ip addr
# 为网络接口分配ip地址
dhclient usb0
# 再次查看ip
ip addr
```

<!-- more -->

## 连接无线
参考：https://jsrun.net/note/s6Bpp
```bash
# 安装依赖
sudo apt install net-tools wireless-tools network-manager

# 查看wifi网卡名称
iw dev

# 查看wifi网卡连接状态
iw wlp2s0 link

# 启动wifi网卡
ip link set wlp2s0 up
# ifconfig wlp2s0 up
```

### nmcli
```bash
# 指定wifi网卡扫描wifi
iw dev wlp2s0 scan|grep SSID

# 开启wifi
nmcli radio wifi on

# 查看网络设备列表
nmcli dev
#tips: 如果列出的设备状态为unmanaged的，需要清空/etc/network/interfaces后重启

# 查看wifi列表
nmcli dev wifi list

# 连接wifi
nmcli dev wifi connect <SSID> password <password> ifname wlp2s0