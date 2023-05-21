# Proxmox VE安装
1. 下载镜像
传送门：https://www.proxmox.com/en/downloads/category/iso-images-pve
3. 制作启动盘
建议使用ventoy，将下载好的镜像拖进U盘即可。
5. BIOS设置开机启动项顺序
将usb启动设为第一启动项
7. 重启安装
根据提示安装即可。

<!-- more -->

# Proxmox VE 联网
由于我的笔记本没有网线可用，只能使用wifi。而刚安装好的pve又是缺少无线网络连接相关包(如nmcli等)的，导致无法使用nmcli连接wifi。后来想到可以用手机usb共享网络给笔记本使用，问题才解决。下面是具体过程：
1. 手机通过数据线链上pve，并开启"usb共享网络"
2. 查看网络接口并获取ip
```
ip addr show  # 此时应该会有一个usb0的网络接口出现
dhclient usb0 # 自动获取ip
ip addr show  # 查看usb0接口的ip
```
3. 检查网络
```bash
ping baidu.com # 此时应该可以上网了
```
4. 无线连接  
为了摆脱使用usb网络带来的不便，需要设置无线连接。
```bash
# 依赖安装
sudp apt update
sudo apt install net-tools wireless-tools network-manager iw

# 查看wifi网卡名称
iw dev # 如我的网卡名称为：wlp2s0

# 查看wifi网卡状态
iw wlp2s0 link

# 启用wifi网卡
ip link set wlp2s0 up

# 使用指定网卡扫描wifi
iw dev wlp2s0 scan | grep SSID

# 开启wifi
nmcli radio wifi on

# 查看网络设备列表
nmcli dev

# 查看wifi列表
nmcli dev wifi list

# 连接wifi
nmcli dev wifi connect <SSID> password <password> ifname wlp2s0

# 断开连接
nmcli dev disconnect wlp2s0
```

:::tip{title="nmcli查看设备出现unmanaged状态？"}
参考：https://askubuntu.com/questions/71159/network-manager-says-device-not-managed
1. 方法一： 清空/etc/network/interfaces后，并加入下面两行后，重启
```bash
# The loopback network interface
auto lo
iface lo inet loopback
```
2. 方法二：
```bash
vim /etc/NetworkManager/NetworkManager.conf
```
```bash
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true # => 将false改为true
```
重启服务：`systemctl restart NetworkManager`
:::

# 虚拟机创建
## ikuai软路由安装
1. 开启dhcp
3. 更改访问ip
4. 外部访问
```bash
firewall-cmd --add-forward-port=port=80:proto=tcp:toaddr=10.1.2.1:toport=80
```
## win10安装
1. iso镜像制作
2. 上传至pve
3. 创建虚拟机

## 群晖NAS安装
群晖安装分为引导文件(多为img格式)和固件系统(多为pat格式)两部分，不像其他系统一个iso文件就够了。
注意：
1. 其中引导文件可支持引导的固件系统是有限制的，不是所有的固件系统都能被引导，因此要和固件系统相匹配。
2. 引导文件可在[黑群晖各版本引导](https://itho.cn/?post=148)下载，固件系统可在群晖官方网站下载：[https://archive.synology.com/download/Os/DSM](https://archive.synology.com/download/Os/DSM)

# 问题记录
1. 虚拟机上访问不了外网？  
>参考：
>1. https://pve.proxmox.com/wiki/Network_Configuration#sysadmin_network_masquerading
>2. https://bobcares.com/blog/setup-nat-on-proxmox/
>3. https://foxi.buduanwang.vip/virtualization/pve/1951.html/
>4. https://yxz.me/2018/05/20/proxmox-ve-manual/
>5. [同时使用防火墙版设置教程](https://aljax.us/how-to-setup-nat-on-your-pve-node/)

宿主机上执行：
```bash
apt install firewalld
# 开启地址伪装(NAT)
firewall-cmd --permanent --zone=public --add-masquerade
```
编辑`/etc/network/interfaces`, 在需要nat的网卡接口尾部上添加:
```bash
post-up   echo 1 > /proc/sys/net/ipv4/ip_forward
post-up   iptables -t nat -A POSTROUTING -s '10.1.2.0/24' -o wlp2s0 -j MASQUERADE
post-down iptables -t nat -D POSTROUTING -s '10.1.2.0/24' -o wlp2s0 -j MASQUERADE
```
其中`wlp2s0`需要更改为自己的网卡接口。
最后，重启网络：`ifreload -a`。

2. 外网访问不了虚拟机？  
设置端口转发
```bash
# option1:
iptables -t nat -A PREROUTING -i vmbr1 -p tcp --dport 3033 -j DNAT --to 192.168.1.2:22
# option2:
firewall-cmd --add-forward-port=port=80:proto=tcp:toaddr=192.168.0.1:toport=8080
```

3. 重置`/etc/network/interfaces`  
参考：https://unix.stackexchange.com/questions/304617/accidentally-deleted-etc-network-interfaces-on-ubuntu
```bash
rm /etc/network/interfaces
vim /etc/network/interfaces
```
内容如下：
```bash
# The loopback network interface
auto lo
iface lo inet loopback
```
重新启动服务：`systemctl restart networking`