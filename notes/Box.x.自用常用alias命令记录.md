---
id: 3qhd5ajq4nwhcppd6oevrdr
title: 自用常用alias命令记录
desc: ''
updated: 1685339673329
created: 1685337692204
---

``` bash 
## 防火墙管理
alias fw_add='sudo firewall-cmd --permanent --zone=public --add-port'
alias fw_del='sudo firewall-cmd --permanent --zone=public --remove-port'
alias fw_reload='sudo firewall-cmd --reload'
alias fw_view='sudo firewall-cmd --list-all'

## git
alias git_acp="git add . && git commit -m 'update' && git push"

# 服务
alias service_status="sudo systemctl status "
alias service_start="sudo systemctl start "
alias service_restart="sudo systemctl restart "
alias service_stop="sudo systemctl stop "
```

