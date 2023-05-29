---
id: 3qhd5ajq4nwhcppd6oevrdr
title: 自用常用alias命令记录
desc: ''
updated: 1685338000862
created: 1685337692204
---

``` bash 
## 防火墙管理
fw_add='sudo firewall-cmd --permanent --zone=public --add-port'
fw_del='sudo firewall-cmd --permanent --zone=public --remove-port'
fw_reload='sudo firewall-cmd --reload'
fw_view='sudo firewall-cmd --list-all'

## git
alias git_acp="git add . && git commit -m 'update' && git push"
