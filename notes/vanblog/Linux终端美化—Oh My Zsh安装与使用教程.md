
## 安装
```bash
# 安装zsh
sudo apt install zsh

# 安装oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
<!-- more -->

## 推荐插件
```bash
# 1. 自动补全
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
# 2. 语法高亮
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
# 3. 历史命令搜索
git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
# 4. 快捷目录跳转
git clone https://github.com/agkozak/zsh-z ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-z
```
## 推荐主题

```bash
# 安装主题(p10k)
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
# 配置主题偏好
p10k configure
```

## 更新配置文件: `~/.zshrc`
```ini
ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(
    git
    zsh-syntax-highlighting
    zsh-autosuggestions
    zsh-history-substring-search
    z
    docker
    sudo
)
```

## 其他
1. conda自动补全
参考：https://www.cxymm.net/article/zhanghm1995/120010254
- 下载插件
```bash
git clone https://github.com/esc/conda-zsh-completion $ZSH_CUSTOM/plugins/conda-zsh-completion
```
- 更改`~/.zshrc`
```bash
fpath+=$ZSH_CUSTOM/plugins/conda-zsh-completion # 在"source $ZSH/oh-my-zsh.sh"前加
compinit conda # 文件最后加
```
- 使配置生效
```bash
source ~/.zshrc
```
- 测试
```bash
conda ac<Tab> # 此时应该会自动补全，再次按tab会弹出环境名
```