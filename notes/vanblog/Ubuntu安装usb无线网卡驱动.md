# 方法
## 安装驱动
1. 插入usb无线网卡，查看usb设备列表

```bash
lsusb
```

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/560db883867e1bb8ad7df449267eadf7.image.png)

2. 克隆仓库

```bash
mkdir -p code
cd code
git clone git@github.com:morrownr/88x2bu-20210702.git
```
<!-- more -->

3. 安装依赖

```bash
sudo apt update && sudo apt upgrade
sudo apt install -y build-essential dkms git iw
```
5. 编译安装

```bash
cd 88x2bu-20210702
make
sudo make install
```

插拔一下设备

```bash
nmcli dev
```
可以看到已经识别到网卡了

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e75aa30f7e86d8c616dc747df2772aa5.image.png)

## 连接网络
参考：https://blog.kevin2li.top/post/14

```bash
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

# 参考
1. https://github.com/morrownr/88x2bu-20210702
2. https://github.com/morrownr/USB-WiFi
3. https://zhuanlan.zhihu.com/p/584242562
