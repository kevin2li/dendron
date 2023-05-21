
# 常用服务管理命令
```bash
# 重新载入服务
systemctl daemon-reload

# 查看服务状态
systemctl status sshd

# 启动服务
systemctl start sshd

# 停止服务
systemctl stop sshd

# 重启服务
systemctl restart sshd

# 开机自启
systemctl enable sshd

# 取消开机自启
systemctl disable sshd

```

<!-- more -->

# 自定义服务示例
## Frp客户端(frpc)

1. 编写服务文件

位置：`/etc/systemd/system/frpc.service`，内容如下：

```ini
[Unit]
Description=frpc service
After=network.service

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/root
ExecStart=sh /home/kevin2li/frp_0.44.0_linux_amd64/frp_start.sh
PrivateTmp=true
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

2. 重新载入文件

`systemctl daemon-reload`

3. 启动服务

`systemctl start frpc`