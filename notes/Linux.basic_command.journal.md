---
id: 9d3keo1gmaf5titr8qnh2gx
title: journal
desc: ''
updated: 1682484254194
created: 1682484254194
---


## 日志管理
- `journalctl`  
`journalctl`是一种用于查看Systemd系统日志的命令行工具。它可以帮助你查找特定的日志数据或浏览整个日志文件，以便审查系统活动或故障。以下是一些journalctl的常用用法：

1. 列出所有日志条目： 

```
journalctl
```

2. 根据服务名称列出所有与该服务相关的日志条目：

```
journalctl -u service_name
```

3. 根据日期和时间过滤日志词条。例如，列出12月3日之后的所有日志：

```
journalctl --since "2019-12-03"
```

4. 使用实时输出功能实时查看系统日志：

```
journalctl -f
```

5. 通过系统日志查找与特定进程相关的条目：

```
journalctl _PID=process_id
```

6. 列出指定进程名称的所有日志条目：

```
journalctl _COMM=process_name
```

7. 列出最近特定行数的日志：

```
journalctl -n number_of_lines
```

8. 列出日志文件大小，磁盘使用量和剩余磁盘空间：

```
journalctl --disk-usage
```

9. 显示特定时间段内的内核消息：

```
journalctl --dmesg
```

- `last`

```bash
# View last logins, their duration and other information as read from `/var/log/wtmp`:
last

# Specify how many of the last logins to show:
last -n login_count

# Print the full date and time for entries and then display the hostname column last to prevent truncation:
last -F -a

# View all logins by a specific user and show the IP address instead of the hostname:
last username -i

# View all recorded reboots (i.e., the last logins of the pseudo user "reboot"):
last reboot

# View all recorded shutdowns (i.e., the last logins of the pseudo user "shutdown"):
last shutdown

```
- `lastb`

```bash
# Show a list of all last logged in users:
sudo lastb

# Show a list of all last logged in users since a given time:
sudo lastb --since YYYY-MM-DD

# Show a list of all last logged in users until a given time:
sudo lastb --until YYYY-MM-DD

# Show a list of all logged in users at a specific time:
sudo lastb --present hh:mm

# Show a list of all last logged in users and translate the IP into a hostname:
sudo lastb --dns
```
- `lastlog`

```bash
# Display the most recent login of all users:
lastlog

# Display the lastlog record of the specified user:
lastlog --user username

# Display records older than 7 days:
lastlog --before 7

# Display records more recent than 3 days:
lastlog -time 3
```
- `watch`

```bash
# Monitor files in the current directory:
watch ls

# Monitor disk space and highlight the changes:
watch -d df

# Monitor "node" processes, refreshing every 3 seconds:
watch -n 3 "ps aux | grep node"
```