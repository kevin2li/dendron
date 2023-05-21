# 安装
```bash
sudo apt-get install tmux
```

# 基本命令
## session管理
```bash
# 查看已有会话
tmux ls
`<prefix>, s`

# 新建会话
tmux new -s <session-name>

# 分离会话
`<prefix>, d`

# 删除会话
tmux kill-session -t <session-name>

# 接入会话
tmux attach -t <session-name>

# 切换会话
tmux switch -t <session-name> 

# 重命名会话
tmux rename -t <old-name> <new-name>
`<prefix>, $`
```

<!-- more -->

## window管理
```bash
# 创建新窗口
`<prefix>, c`

# 重命名窗口
`<prefix>, ,`

# 切换窗口
鼠标点选
`<prefix>, <id>`: 切换到<id>窗口
`<prefix>, w`：列出所有窗口来选择切换
`<prefix>, n`: 切换到下个窗口
`<prefix>, p`：切换到上个窗口

# 删除窗口
tmux kill-window -t 1

```

## panel管理
```bash
# 创建panel
`<prefix>, |`: vertical split window
`<prefix>, -`: horizontal split window

# 删除panel
`<prefix>, x`

# 调整大小
`<prefix>, Alt + <arrow>`
`<prefix>, z`: 将当前panel最大化(复制时有用)

# 查看panel编号
`<prefix>, q`

# 交换panel位置
`<prefix>, {`：与上一个编号的panel交换
`<prefix>, }`：与下一个编号的panel交换

# 旋转panel
`<prefix>, Ctrl+o`: 逆时针
`<prefix>, Alt+o`：顺时针

```
# 进阶使用
## 复制粘贴
1. 方法：按住shift，鼠标左键选择，Ctrl+C复制，Ctrl+V粘贴
  
:::tip{title="提示"}
当横向有多个panel时，可以先最大化再复制
:::
2. Vim中粘贴内容出现缩进错误
在`~/.vimrc`中加入下面代码：
```bash
" 解决tmux中粘贴缩进混乱
if &term =~ "screen"                                                   
    let &t_BE = "\e[?2004h"                                              
    let &t_BD = "\e[?2004l"                                              
    exec "set t_PS=\e[200~"                                              
    exec "set t_PE=\e[201~"                                              
endif
```

## 插件管理
### 插件管理器`tpm`
1. 安装tmux插件管理工具
```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```
2. 将下面代码放到`~/.tmux.conf`配置文件最后
```bash
# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'github_username/plugin_name#branch'
# set -g @plugin 'git@github.com:user/plugin'
# set -g @plugin 'git@bitbucket.com:user/plugin'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
```
要安装插件就新增一个条目：`set -g @plugin '...'`，然后`<prefix> + I`安装。

插件安装目录为：`~/.tmux/plugins/`

3. 使配置文件生效
```bash
tmux source ~/.tmux.conf
```
4. 快捷键
- 下载安装插件: `<prefix> + I`
- 更新插件：`<prefix> + U`
- 卸载插件: `<prefix> + alt + u`

### 恢复会话插件

```bash
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
```
- `tmux-resurrect`

github: https://github.com/tmux-plugins/tmux-resurrect

保存会话：`prefix + Ctrl-s`  
恢复会话：`prefix + Ctrl-r`  

- `tmux-continuum`  

github: https://github.com/tmux-plugins/tmux-continuum


# 自用配置文件
最后奉上自用的配置文件，供大家参考。
```bash
# Improve colors
set -g default-terminal 'screen-256color'

# Set scrollback buffer to 10000
set -g history-limit 10000

# Customize the status line
set -g status-fg  green
set -g status-bg  black

set -g mouse on

unbind '"'
bind - splitw -v -c '#{pane_current_path}' # 垂直方向新增面板，默认进入当前目录
unbind %
bind | splitw -h -c '#{pane_current_path}' # 水平方向新增面板，默认进入当前目录

# 绑定hjkl键为面板切换的上下左右键
bind -r k select-pane -U # 绑定k为↑
bind -r j select-pane -D # 绑定j为↓
bind -r h select-pane -L # 绑定h为←
bind -r l select-pane -R # 绑定l为→

set -g prefix C-a #
unbind C-b # C-b即Ctrl+b键，unbind意味着解除绑定
bind C-a send-prefix # 绑定Ctrl+a为新的指令前缀

setw -g mode-keys vi

# ------------------tpm------------------------
# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @continuum-restore 'on'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
```