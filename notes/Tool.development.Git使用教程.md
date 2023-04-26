---
id: wc3jyj5e6t4zp0kg2bg2tal
title: Git使用教程
desc: ''
updated: 1682509814067
created: 1682509781052
---

# 简介
Git是一个开源的分布式版本控制系统，可以有效、高速地处理从很小到非常大的项目版本管理。它是Linus Torvalds为了帮助管理Linux内核开发而开发的一个开放源码的版本控制软件。Git的作用就是对文件进行版本管理，方便在不同版本进行切换修改，类似文件分不同时间备份让后需要时找回其中一份代替，不过更方便使用。

Git文件流：
![image.png](https://blog.kevin2li.top/static/img/5ca15d0a60362cb3f0ad630d0615d394.image.png)


<!-- more -->

# 安装
- Linux系统  
```bash
# Ubuntu为例
sudo apt-get update 
sudo apt install git
```

- Windows系统  
可以从[Git官方网站](https://git-scm.com/)下载Git for Windows，也可以安装GitHub Desktop，该安装程序包含图形化和命令行版本的Git

# 使用教程
## 配置管理
```bash
# 设置用户名
git config --global user.name="kevin2li"

# 设置邮箱
git config --global user.email="kevin2li@qq.com"

# 设置初始化分支名称
git config --global init.defaultBranch main

# 设置命令别名
git config --global alias.co checkout
git config  --global alias.br  branch

# 查看配置
git config --list
```

## 仓库管理
```bash
# 初始化仓库
git init

# 克隆仓库(将myrepo仓库克隆到/path/to/folder文件夹中，不给参数2将克隆到当前目录)
git clone https://github.com/username/myrepo.git /path/to/folder

# 查看远程仓库
git remote -v

# 添加远程仓库
git remote add origin git@github.com:Nyr/openvpn-install.git

# 删除远程仓库
git remote remove origin

# 重命名远程仓库
git remote rename origin origin-tencent
```

## 提交管理
```bash
# 添加文件
git add a.txt

# 删除文件
git rm a.txt

# 删除文件(暂存区删除)
git rm --cached a.txt

# 撤销文件更改
git restore a.txt

# 创建提交
git commit -m "message" 

# 补充提交
git commit --amend -m "message"

# 回退提交(reset): 不会产生新提交，适用于已经commit但是没有push的情形
git reset <ID>

# 回退提交(revert): 会产生新提交
git revert <ID>

```

:::info{title="git reset回退的三种模式区别"}
![image.png](https://blog.kevin2li.top/static/img/a4c1e10cc0f0ecc5fbdb1e8d69136988.image.png)

`git reset` 有三种模式，分别是 `--soft`、`--mixed` 和 `--hard`。它们之间的区别如下：  
`--soft`：此模式只重置 HEAD 到所选提交。它基本上与 git checkout 相同，但不会创建分离的 HEAD 状态。  
`--mixed`：默认模式，此模式将 HEAD 重置为所选提交，同时在历史记录和索引中撤消更改。  
`--hard`：此模式将 HEAD 重置为所选提交，并在历史记录和索引中撤消更改，同时还将工作树重置为所选提交。  
:::

:::tip{title="git reset与git revert的区别"}
`git reset`: 此命令用于通过删除所需提交后的所有更改来将分支的状态重置为先前状态。此命令更改提交历史记录。  
`git revert`：此命令用于通过创建新的还原提交并保留原始提交来重置到先前状态。此命令不更改提交历史记录。
:::

## 标签管理
```bash
# 设置标签
git tag v1.0 main

# 删除标签
git tag -d v1.0
```

## 分支管理
```bash
# 创建分支
git checkout -b feature-xx
git checkout -b totallyNotMain o/main #跟踪远程分支
git branch dev
git branch dev HEAD~3

# 删除分支
git branch -d feature-xx

# 重命名分支
git branch -M main

# 设置远程分支追踪
git branch -u origin/dev dev

# 切换分支
git checkout <branch>
git switch <branch>

# 推送分支
git push -u origin main
git push origin dev:main

# 打包分支
git archive -o main.zip main

# 修改分支指向点
git branch -f main HEAD^

# 合并分支(merge)
git merge --no-ff dev

# 合并分支(rebase)
git rebase main # 将当前分支以main分支为基合并
git rebase main dev # 将dev分支以main分支为基合并

```

## 运维管理
```bash
# 查看git历史
git log --oneline --decorate --graph

# 查看完整git历史
git reflog

# 查看文件修改
git show main.py

# 查看当前状态
git status

# 查看文件修改
git diff

```

## 进阶
- 暂存修改：`git stash`
```bash
# 列出stash的所有记录
git stash list

# 保存当前未commit的代码
git stash

# 应用最近一次的stash，随后删除该记录
git stash pop

# 保存当前未commit的代码并添加备注
git stash save "备注的内容"

# 删除stash的所有记录
git stash clear

# 应用最近一次的stash
git stash apply

# 删除最近的一次stash
git stash drop
```

- 整理提交顺序
```bash
# 在当前位置应用所选的commit
git cherry-pick <ID1> <ID2> <ID3>

# 打开交互式窗口编辑顺序
git rebase -i <ID>
```
