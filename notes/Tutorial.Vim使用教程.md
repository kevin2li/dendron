---
id: unvhobazy97207p5sknvdz9
title: Vim使用教程
desc: ''
updated: 1683258456075
created: 1682939832694
---


## 简介
Vim是一款文本编辑器，它可以在终端或命令行界面下使用。Vim最初是由Bram Moolenaar在1991年发布的，并基于另一款文本编辑器Vi开发而来。

Vim具有强大的编辑功能，可以帮助用户快速编辑和处理文本文件。它支持多种编辑模式，包括命令模式、插入模式和可视模式，可以通过快捷键在不同的模式之间切换。Vim还支持多种自定义配置选项，可以让用户根据自己的需求进行定制。

由于Vim可以在终端下运行，因此它特别适合在远程服务器上进行编辑操作。Vim也有广泛的使用者社群和丰富的插件生态系统，可以通过插件扩展其功能。由于Vim的学习曲线较陡峭，因此需要一定的学习成本。但是一旦掌握了Vim的基本用法，就能够大幅提高文本编辑效率。

官网：https://www.vim.org/  

## 教程
### 模式

![](https://minio.kevin2li.top/image-bed/202305012047948.png)

#### 命令模式
##### 窗口管理
| 功能                 | 按键       |
| -------------------- | ---------- |
| 关闭当前窗口         | `:q`       |
| 保存并关闭当前窗口   | `:wq`      |
| 关闭当前窗口(不保存) | `:q!`      |
| 水平分割窗口         | `Ctrl-W s` |
| 垂直分割窗口         | `Ctrl-W v` |

##### tab页管理
| 功能              | 按键             |
| ----------------- | ---------------- |
| 在新tab页打开文件 | `:tabnew {file}` |
| 切换到下一个tab   | `:tabn`          |
| 切换到上一个tab   | `:tabp`          |
| 关闭其他tab       | `:tabo`          |

##### 文本内容处理

| 功能                   | 按键      |
| ---------------------- | --------- |
| 复制第49到51行的内容   | `:49,51y` |
| 删除第30到第34行的内容 | `:30,34d` |
| 删除当前行及下面两行   | `:.,+2d`  |
| 删除整个文档           | `:%d`     |

##### 其他
1. 保存需要用sudo权限保存的文件
`:w !sudo tee %`

##### 光标移动
| 功能             | 按键   |
| ---------------- | ------ |
| 光标向上移动10行 | `:-10` |
| 光标向下移动10行 | `:+10` |
| 移动到第123行    | `:123` |
| 移动到首行       | `:0`   |
| 移动到末行       | `:$`   |

#### 输入模式
| 功能                 | 按键       |
| -------------------- | ---------- |
| 在光标前输入         | `i`        |
| 在光标后输入         | `a`        |
| 在行首输入           | `I`        |
| 在行尾输入           | `A`        |
| 在下一行开头输入     | `o`        |
| 在上一行开头输入     | `O`        |
| 修改当前char         | `s`        |
| 删除前一个char       | `Ctrl-H`   |
| 删除前一个word       | `Ctrl-W`   |
| 删除当前行光标前内容 | `Ctrl-U`   |
| 回到上次修改位置     | `gi`       |
| 粘贴寄存器`x`的内容  | `Ctrl-R x` |

#### 替换模式
- `r`: 进入char替换模式
#### 可视模式
| 功能                    | 按键     |
| ----------------------- | -------- |
| 进入char-level可视模式  | `v`      |
| 进入line-level可视模式  | `V`      |
| 进入block-level可视模式 | `Ctrl-V` |

### 语法

```bash
# 格式1：
[count] [operator] [motion | text objects]

# 格式2：
[operator]  [count] [motion | text objects]
```

说明：
- `count`: 命令执行次数
- `operator`: 命令类型，包括`y`、`d`、`c`、`x`等
- `motion`: 指明光标移动范围
- `text objects`: 文本块对象

例如：
- `caw`: 修改当前word
- `yaw`: 复制当前word
- `dl`: 删除当前字符
- `ct.`: 修改直到`.`前面的内容
- `3dd`: 删除3行
- `d2w`: 向后删除2个word


#### 文本对象(text object)
在Vim中，text objects（文本对象）是一种用于快速选择和操作文本块的功能。它可以让用户在编辑时快速选择一段文本，而不需要使用鼠标进行拖拽或者键盘进行移动光标来选择。text objects可以让用户通过一些命令快速选择文本对象，然后进行复制、剪切、粘贴或其他操作。

在Vim中，text objects有多种类型，例如：
| type        | command                |
| ----------- | ---------------------- |
| word        | `aw`或`iw`             |
| sentence    | `as`或`is`             |
| paragraph   | `ap`或`ip`             |
| string      | `a"`或`i"`, `a'`或`i'` |
| code        | `` a` `` 或 `` i` ``   |
| parentheses | `a(`或`i(`             |
| brackets    | `a[`或`i[`             |
| braces      | `a{`或`i{`             |
| tags        | `at`或`it`             |

其中, `a`表示`around`，包含定界符； `i`表示`inside`，不包括定界符

#### 动作(motion)
在vim中，motion表示移动光标的操作。具体来说，motion是指通过键盘输入一系列命令来使光标在文本中向前或向后移动的操作，这些命令通常与方向键（如上、下、左、右）无关，而是使用vim的特殊命令，例如单词、行、段落等。

motion是vim中的重要概念之一，熟练掌握各种motion的使用可以提高vim的操作效率。

下面介绍vim中常见的motion：

##### 行内移动

###### 移动到行首/行尾

| 功能               | 按键 |
| ------------------ | ---- |
| 移动到行首         | `0`  |
| 移动到行尾         | `$`  |
| 移动到行首(非空白) | `^`  |
| 移动到行尾(非空白) | `g_` |

###### 按单词移动

> ![](https://minio.kevin2li.top/image-bed/202305041804096.png)
> word和Word的区别

| 功能                 | 按键 |
| -------------------- | ---- |
| 移动到下一个word开头 | `w`  |
| 移动到上一个word开头 | `b`  |
| 移动到下一个word结尾 | `e`  |
| 移动到上一个word结尾 | `ge` |
| 移动到下一个WORD开头 | `W`  |
| 移动到上一个WORD开头 | `B`  |
| 移动到下一个WORD结尾 | `E`  |
| 移动到上一个WORD结尾 | `gE` |


###### 按括号移动

| 功能                                 | 按键 |
| ------------------------------------ | ---- |
| 移动到对应括号匹配位置(支持`{[()]}`) | `%`  |

###### 按指定字符移动
| 功能                 | 按键      |
| -------------------- | --------- |
| 移到到下一个`char`   | `f{char}` |
| 移到到上一个`char`   | `F{char}` |
| 移到直到下一个`char` | `t{char}` |
| 移到直到上一个`char` | `T{char}` |

::: tip  查找匹配
查找下一个： `;`  
查找上一个： `,`
:::

##### 跨行移动

| 功能                    | 按键                                  |
| ----------------------- | ------------------------------------- |
| 移动到首行              | `gg`                                  |
| 移动到尾行              | `G`                                   |
| 移动到`{line-number}`行 | `{line-number}gg` 或 `{line-number}G` |
| 移动到屏幕顶端          | `H`                                   |
| 移动到屏幕中端          | `M`                                   |
| 移动到屏幕底端          | `L`                                   |
| 向下翻页半个屏幕        | `Ctrl+d`                              |
| 向上翻页半个屏幕        | `Ctrl+u`                              |
| 向下翻页整个屏幕        | `Ctrl+f`                              |
| 向上翻页整个屏幕        | `Ctrl+b`                              |
| 向下滚动                | `Ctrl+e`                              |
| 向上滚动                | `Ctrl+y`                              |

### 文本操作
#### 复制/剪切/修改/粘贴
![](https://minio.kevin2li.top/image-bed/202305041810287.png)
##### 复制
| 功能                  | 按键             |
| --------------------- | ---------------- |
| 复制一个letter        | `yl`             |
| 复制当前行            | `yy` or `Y`      |
| 复制`text object`内容 | `y{text object}` |
| 复制`motion`内容      | `y{motion}`      |


##### 粘贴
| 功能                                        | 按键  |
| ------------------------------------------- | ----- |
| 在当前光标后粘贴 (结束后光标置于粘贴内容前) | `p`   |
| 在当前光标前粘贴 (结束后光标置于粘贴内容前) | `P`   |
| 在当前光标后粘贴 (结束后光标置于粘贴内容后) | `gp`  |
| 在当前光标前粘贴 (结束后光标置于粘贴内容后) | `gP`  |
| 拷贝当前行到下一行                          | `yyp` |
| 交换上下两行                                | `ddp` |

##### 剪切
| 功能                  | 按键             |
| --------------------- | ---------------- |
| 剪切当前字符          | `x`              |
| 剪切当前行            | `dd`             |
| 剪切至行尾            | `D`              |
| 交换左右字母顺序      | `dlp` 或 `xp`    |
| 剪切`text object`内容 | `d{text object}` |
| 剪切`motion`内容      | `d{motion}`      |


##### 修改
| 功能                  | 按键             |
| --------------------- | ---------------- |
| 修改当前行            | `cc`             |
| 修改至行尾            | `C`              |
| 修改`text object`内容 | `c{text object}` |
| 修改`motion`内容      | `c{motion}`      |


#### 查找

格式：
- `/pattern`: 向后查找`{pattern}`
- `?pattern`: 向后查找`{pattern}`
- `*`: 向后查找光标下所在单词, 相当于`/pattern`
- `#`: 向前查找光标下所在单词, 相当于`?pattern`

::: tip  查找匹配
- `n`: 查找下一个
- `N`: 查找上一个
:::

==与`.`配合使用，可以实现对匹配项的批量修改或删除==

例如：

> 测试文本：
cucumber carrot lettuce
cabbage carrot lettuce cucumber
cucumber cucumber carrot
kale cucumber kale

操作序列：
``` bash 
/cucumber<Enter>    # 查找匹配项
cgnfoo<ESC>         # 执行对匹配项的修改: 将匹配项修改为foo
.                   # 重复执行修改
```

::: tip  `gn`的作用
在Vim中，"gn"是一种高级文本对象的选择方式，可以选中下一个匹配项。"gn"命令的作用是在当前光标位置查找下一个与当前选中文本相同的文本，然后选中该文本。如果没有选中文本，"gn"会选中当前光标所在单词。
:::

> 结果：
> foo carrot lettuce
> cabbage carrot lettuce foo
> foo foo carrot
> kale foo kale

#### 替换
格式：

``` bash 
:[range]s/{pattern}/{substitute}/[flags]
```
说明：
- `range`: 作用范围，如：
  - `%`表示整个文档
  - `3,5`表示第3行至第5行
  - `1,$`表示第1行至最后一行
  - `.,+2`表示当前行及后面两行
- `pattern`: 表示匹配的模式
- `substitute`: 表示替换的内容
- `flags`: 替换标志位，如：
  - `g`: 表示全部匹配项替换
  - `i`: 表示忽略大小写
  - `c`: 表示替换前提示要求确认

例如：
``` bash 
# 将第296行至299行中的所有cucumber替换为foo
:296,299s/cucumber/foo/g

# 将整个文档中所有cucumber替换为foo
:%s/cucumber/foo/g

# 将当前行所有cucumber替换为foo
:s/cucumber/foo/g
```

#### 环绕

| 功能               | 按键       | 说明                   |
| ------------------ | ---------- | ---------------------- |
| 删除环绕           | `ds`       |                        |
| 添加环绕           | `ys`       |                        |
| 添加环绕           | `S{word}`  | 需要先选中再使用       |
| 修改环绕           | `cs'"`     | 将'修改为"             |
| 将指定单词环绕符号 | `ysiw<li>` | 将指定单词用`<li>`包裹 |


#### 其他

| 功能           | 按键     |
| -------------- | -------- |
| 交换大小写     | `~`      |
| 交换整行大小写 | `g~~`    |
| 增加缩进       | `>>`     |
| 减少缩进       | `<<`     |
| 自增1          | `Ctrl-A` |
| 自减1          | `Ctrl-X` |

### 寄存器(register)
> 参考：https://www.iteye.com/blog/liuzhijun-1830931

| 类型                                | 名称  | 作用                                                                                              |
| ----------------------------------- | ----- | ------------------------------------------------------------------------------------------------- |
| 未命名寄存器(unamed register)       | `"`   | 复制/剪切默认的寄存器存储位置                                                                     |
| 命名寄存器(named register)          | `a-z` | 由用户自定义存储内容                                                                              |
| 复制寄存器(yank register)           | `0`   | 存储最近复制的内容                                                                                |
| 剪切寄存器(cut register)            | `1-9` | 存储最近9次剪切的内容(以行为单位),其中1表示最近1次剪切的内容，2表示倒数第二次剪切的内容，以此类推 |
| 小删除寄存器(small delete register) | `-`   | 相比1-9寄存器以行为单位，这个粒度更细, 可以存储char、word等                                       |
| 系统寄存器(system register)         | `*`   | 系统寄存器，可以与vim共享内容                                                                     |

查看寄存器内容：`:reg`
![](https://minio.kevin2li.top/image-bed/202305042145955.png)

语法
- 通过`"x`语法来指定使用命名寄存器`x`，向其中覆盖写入内容
- 通过`"X`语法来指定使用命名寄存器`x`，向其中追加写入内容


| 功能                    | 按键                                            |
| ----------------------- | ----------------------------------------------- |
| 存储内容到命名寄存器`a` | `"ay{motion}` 或 `"ad{motion}` 或 `"ac{motion}` |
| 粘贴命名寄存器`a`的内容 | `"ap`                                           |
| 粘贴系统剪贴板内容      | `"*p`                                           |

### 宏(macro)
- `q{register}<Command>q`: 录制宏, 以`q`为界开始录制，以`q`为界结束录制
- `@{register}`: 调用宏

``` bash 
# 自增序号宏录制
qa
"xyiwjdiw"xp<Ctrl>-a
q

# 调用
@a  # 调用1次
5@a # 调用5次
@@  # 重复上次调用
```
### 标记(mark)
- `m{register}`: 添加标记到`register`中，`register`可以为`a-zA-Z`
- `` `{register} ``: 跳转到`register`存储的标记处
- ` '{register} `: 跳转到`register`存储的标记处行首
- ``` `` ``` : 在当前光标处与标记处来回切换
- `''` : 当前光标所在行处与标记处来回切换，光标定位在行首
### 重复执行
- `.`: 重复执行上次修改

### 撤销和恢复
- `u`: 撤销上次更改
- `Ctrl+R`: 恢复上次更改


### 配置
#### 常用基础配置

| 配置选项                      | 说明                                                       |
| ----------------------------- | ---------------------------------------------------------- |
| `set number`                  | 显示行号                                                   |
| `set autoindent`              | 自动缩进                                                   |
| `set smartindent`             | 智能缩进，根据上一行的缩进方式来缩进                       |
| `set tabstop=4`               | tab 为 4 个空格                                            |
| `set shiftwidth=4`            | 设置每次缩进的空格数为 4                                   |
| `set autoread`                | 当文件被改动时自动载入                                     |
| `syntax on`                   | 语法高亮                                                   |
| `set ignorecase`              | 搜索时忽略大小写                                           |
| `set smartcase`               | 搜索时区分大小写，但如果搜索词全小写则忽略大小写           |
| `set mouse=a`                 | 鼠标支持                                                   |
| `set clipboard=unnamedplus`   | 允许使用鼠标复制和粘贴                                     |
| `set backupdir=~/.vim/backup` | 备份文件目录                                               |
| `set expandtab`               | 将 tab 转为空格                                            |
| `set hlsearch`                | 高亮显示搜索结果                                           |
| `set incsearch`               | 在搜索时逐步显示结果                                       |
| `set showmatch`               | 在插入括号时高亮显示匹配的括号                             |
| `set nowrap`                  | 不折行显示内容                                             |
| `set wrap`                    | 折行显示内容                                               |
| `set noswapfile`              | 禁止创建 swap 文件                                         |
| `set path=.,**`               | 设置 Vim 的寻找文件路径，在当前目录和所有子目录下查找文件  |
| `set ruler`                   | 显示当前光标所在行和列的位置                               |
| `set spell`                   | 开启拼写检查功能                                           |
| `set spelllang=en_us`         | 设置拼写检查语言为英语                                     |
| `set foldmethod=indent`       | 按照缩进级别进行折叠                                       |
| `set foldcolumn=2`            | 设置折叠列的宽度为 2                                       |
| `set scrolloff=3`             | 设置距离屏幕顶端和底端的距离，以保证光标始终在屏幕中央     |
| `set textwidth=80`            | 设置每行最大字符数为 80                                    |
| `set undofile`                | 开启撤销文件功能，每次编辑时都会自动生成一个撤销文件       |
| `set undolevels=1000`         | 设置撤销文件保存的最大历史记录数为 1000                    |
| `set undoreload=10000`        | 设置 Vim 自动重新加载撤销文件的时间间隔为 10000 次编辑操作 |
| `set nofoldenable`            | 禁用折叠功能                                               |
| `set foldenable`              | 启用折叠功能                                               |
| `set cursorline`              | 高亮显示当前行                                             |
| `set cursorcolumn`            | 高亮显示当前列                                             |
| `set list`                    | 显示行尾空格等不可打印字符                                 |
| `set clipboard=unnamed`       | 允许与系统剪贴板交互                                       |
| `export VISUAL=vim`           | 将 Vim 设置为默认编辑器                                    |

#### 插件管理
插件管理器：[vim-plug]( https://github.com/junegunn/vim-plug )
- 安装
``` bash 
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```
- 使用

添加插件示例(支持多种格式)：

``` bash 
call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'

" Make sure you use single quotes

" Shorthand notation; fetches https://github.com/junegunn/vim-easy-align
Plug 'junegunn/vim-easy-align'

" Any valid git URL is allowed
Plug 'https://github.com/junegunn/vim-github-dashboard.git'

" Multiple Plug commands can be written in a single line using | separators
Plug 'SirVer/ultisnips' | Plug 'honza/vim-snippets'

" On-demand loading
Plug 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }
Plug 'tpope/vim-fireplace', { 'for': 'clojure' }

" Using a non-default branch
Plug 'rdnetto/YCM-Generator', { 'branch': 'stable' }

" Using a tagged release; wildcard allowed (requires git 1.9.2 or above)
Plug 'fatih/vim-go', { 'tag': '*' }

" Plugin options
Plug 'nsf/gocode', { 'tag': 'v.20150303', 'rtp': 'vim' }

" Plugin outside ~/.vim/plugged with post-update hook
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

" Unmanaged plugin (manually installed and updated)
Plug '~/my-prototype-plugin'

" Initialize plugin system
" - Automatically executes `filetype plugin indent on` and `syntax enable`.
call plug#end()
" You can revert the settings after the call like so:
"   filetype indent off   " Disable file-type-specific indentation
"   syntax off            " Disable syntax highlighting

```

命令说明：

| Command                             | Description                                                       |
| ----------------------------------- | ----------------------------------------------------------------- |
| `PlugInstall [name ...] [#threads]` | Install plugins                                                   |
| `PlugUpdate [name ...] [#threads]`  | Install or update plugins                                         |
| `PlugClean[!]`                      | Remove unlisted plugins (bang version will clean without prompt)  |
| `PlugUpgrade`                       | Upgrade vim-plug itself                                           |
| `PlugStatus`                        | Check the status of plugins                                       |
| `PlugDiff`                          | Examine changes from the previous update and the pending changes  |
| `PlugSnapshot[!] [output path]`     | Generate script for restoring the current snapshot of the plugins |
#### 推荐配置

> 参考： https://github.com/amix/vimrc

安装：
``` bash 
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh
```

此时，会生成一个默认的`~/.vimrc`文件，包含了该项目为我们指定的推荐配置。
我们可以将自己补充的配置添加在`~/.vim_runtime/my_configs.vim`中。

``` bash 
set number
set mouse=a

" 解决tmux中粘贴缩进混乱
if &term =~ "screen"                                                   
    let &t_BE = "\e[?2004h"                                              
    let &t_BD = "\e[?2004l"                                              
    exec "set t_PS=\e[200~"                                              
    exec "set t_PE=\e[201~"                                              
endif

call plug#begin()

Plug 'https://github.com/tpope/vim-surround'
Plug 'jiangmiao/auto-pairs'

call plug#end()
```

### Cheatsheet
![](https://minio.kevin2li.top/image-bed/202305012053709.png)

## 参考
1. https://vim.rtorr.com/
2. https://www.lesswrong.com/posts/ioGf4LHid42mCK3SK/vim
3. [Learn Vim | vscode插件](  https://marketplace.visualstudio.com/items?itemName=vintharas.learn-vim )

