# 简介
Cockpit是一款基于web的图形化服务器管理工具，支持系统信息概览、网络管理、kvm虚拟机管理、容器管理、存储管理、网页终端等多重功能，极大地方便运维执行常用操作。目前该工具在Github已获得7.6k的stars。

![](https://minio.kevin2li.top/image-bed/vanblog/img/cb29b164ef0e198d9c03f634a57c3468.20221209195503.png)

Github: https://github.com/cockpit-project/cockpit  
官网：https://cockpit-project.org/  
使用文档：[documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_systems_using_the_rhel_9_web_console/cockpit-add-ons-_system-management-using-the-rhel-9-web-console#installing-add-ons_cockpit-add-ons)

<!-- more -->

# 安装
- Ubuntu安装
```bash
. /etc/os-release
sudo apt install -t ${VERSION_CODENAME}-backports cockpit cockpit-machines cockpit-podman
```
- 其他系统安装

![](https://minio.kevin2li.top/image-bed/vanblog/img/5c4161972338806f521e4635690a4285.20221209195903.png)

见 https://cockpit-project.org/running.html

# 使用
```bash
# 查看状态
sudo systemctl status cockpit
# 启动
sudo systemctl start cockpit
# 停止
sudo systemctl stop cockpit
```

:::tip{title="提示"}
cockpit会占用9090端口，如果端口被占用可能会导致启动失败。
可通过`lsof -i:9090`命令查看占用端口的程序，关掉后再重新启动。
:::

外部访问：`http://<server_ip>:9090`
