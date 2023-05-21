# 简介
crontab命令是Unix和Linux用于设置周期性被执行的指令。该命令从标准输入设备读取指令，并将其存放于“crontab”文件中，以供之后读取和执行。crontab命令常见于 Unix 和 类Unix 的操作系统之中。通常，crontab储存的指令被守护进程激活， crond常常在后台运行，每一分钟检查是否有预定的作业需要执行。

该命令依赖于`cron`，可通过下面命令安装和启用：
```bash
# 安装
sudo apt-get install cron

# 启动
systemctl start cron

# 查看状态
systemctl status cron
```

<!-- more -->

# 基本命令
```bash
# 查看当前用户定时任务
crontab -l

# 指定用户查看
crontab -u root -l

# 编辑当前用户定时任务
crontab -e

# 删除当前用户的定时任务
crontab -r
```


示例：
```bash
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command
5 * * * *  ddns -c /home/likai/ddns/config.json
```

5个*分别表示：`minute,hour,day,month,weekday`

# 加入日志记录
```bash
# 运行下面命令后找到包含cron的行，就前面的#去掉
sudo vim /etc/rsyslog.d/50-default.conf

# 重启rsyslog
sudo systemctl restart rsyslog

# 日志路径
sudo less /var/log/cron.log
```