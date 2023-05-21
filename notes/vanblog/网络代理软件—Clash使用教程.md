# 简介
Clash是一个 Go 语言开发的多平台代理客户端, 目前github stars已经超过32k。  

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/aa3c17033472e2b231d89b713ac25e8e.image.png)

项目地址：https://github.com/Dreamacro/clash

:::info{title="说明"}
原始的Clash只是一个命令行工具，为了更加方便使用，基于该项目衍生了一些图形化的代理软件，比如:
- [Clash for Windows](https://github.com/Fndroid/clash_for_windows_pkg/)  
该软件为Windows平台的图形化客户端软件，使用文档可见：https://docs.cfw.lbyczf.com/
- [CLsah X](https://github.com/yichengchen/clashX)  
该软件为Mac平台的图形化客户端
- [Clash for Android](https://github.com/Kr328/ClashForAndroid)  
该软件为Android平台的图形化客户端软件
:::
上述图形化客户端使用较为简单，本文专注于Linux服务器上无图形界面环境下使用Clash的教程。

<!-- more -->

# 安装
## 下载可执行文件
去项目[Releases](https://github.com/Dreamacro/clash/releases)版块下载最新的安装包，解压后里面会有一个可执行文件，为了方便将其重命名为`clash`,后文将以`clash`指代这个可执行文件.
```bash
# linux-amd64 下载
wget https://github.com/Dreamacro/clash/releases/download/v1.11.8/clash-linux-amd64-v1.11.8.gz
# 解压
tar -xvf clash-linux-amd64-v1.11.8.gz
```

## 修改配置文件
如下是一个极简的配置文件：
```yaml
mixed-port: 7890
allow-lan: true
bind-address: '*'
mode: rule
log-level: info
external-controller: '127.0.0.1:9090'
```
实际使用时，要添加进去自己的代理信息，也可以直接使用自己其他clash图形化客户端的配置文件。

## 启动
```bash
clash -f <config_path> # config_path为配置文件路径
```
为了方便管理，可以将其设置为系统服务：  
服务文件路径：`/etc/systemd/system/clash.service`，内容如下：
```ini
[Unit]
Description=clash service
After=network.service

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/root
ExecStart=/home/kevin2li/clash/clash -f /home/kevin2li/clash/clash_config.yml ;这里要根据自己情况修改路径
PrivateTmp=true
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
clash服务管理：
```bash
# 重载服务
sudo systemctl daemon-reload
# 启动
sudo systemctl start clash
# 停止
sudo systemctl stop clash
# 查看状态
sudo systemctl status clash
# 加入开机自启
sudo systemctl enable clash
```

## 控制
由于Clash没有图形界面，但是它公开了[RESTful API](https://clash.gitbook.io/doc/restful-api)接口，可以通过发送对应请求来获取或修改相关设置。
幸运的是，目前已有一些工具实现了这些接口，比如：
- 网页端控制工具：[razord](http://clash.razord.top/#/proxies)  
使用前需要开放服务器对应控制端口(由配置文件中`external-controller`字段指定)

![](https://minio.kevin2li.top/image-bed/vanblog/img/ebd5ba2744089b2670830fc6e9769c23.20221019212451.png)

- 命令行工具：[clashcli](https://github.com/shunf4/clashcli)

![](https://minio.kevin2li.top/image-bed/vanblog/img/f1039244c3c6814532c88ba7cd6baaf6.20221019212745.png)

常用命令：
```bash
clashcli -t # 测试延迟
clashcli -s # 选择节点
```

# 使用

## 在终端中使用
```bash
# bash
export https_proxy="http://127.0.0.1:7890" && export http_proxy="http://127.0.0.1:7890"

# powershell
$https_proxy="http://127.0.0.1:7890"
$http_proxy="http://127.0.0.1:7890"
```
## 在Python中使用
```python
import os
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
```