
# 简介
Vim是Linux下经典的文本编辑器之一，因其功能强大，素有“编辑器之神”的美誉。但是其学习曲线也是比较陡峭的，本文将对其使用方法做一个简单的介绍和总结，希望能对大家快速上手这款编辑器提供帮助。
# 基本使用
- 键位图

![](https://minio.kevin2li.top/image-bed/vanblog/img/00cecf1d98a4d0858aac8f05ef032ba8.20221019174721.png)

这张图囊括了Vim操作的核心，可以细细品味。既可以作为初学者入门的指南，也可以作为学习过后的总结凝练。
<!-- more -->
## 光标移动
1. 方向键
- `h`: 光标左移1格
- `j`: 光标下移1格
- `k`: 光标上移1格
- `l`: 光标右移1格
3. 其他移动
- 光标移动行首(包含字符空)：`0`
- 光标移到行尾(包含空字符)：`$`
- 光标移到行首(不包含空字符): `^`
- 光标移动行尾(不包含空字符): `g_`
- 光标移到下一个单词头: `w`
- 光标移到下一个单词尾: `e`
- 光标移到上一个单词头：`b`
- 光标移到上一个单词尾：`ge`
- 光标移到下一个`a`字符(包含): `fa`
- 光标移到上一个`a`字符(包含): `Fa`
- 光标移到下一个`a`字符(不包含): `ta`
- 光标移到上一个`a`字符(不包含): `Ta`
- 光标移到下一个句子头: `(`
- 光标移到上一个句子头: `)`
- 光标移到段首：`{`
- 光标移到段尾：`}`
- 光标移到首行第一个字符(不包含空字符)：`gg`
- 光标移到末行第一个字符(不包含空字符): `G`
- 光标移到屏幕顶行：`H`
- 光标移到屏幕中间：`M`
- 光标移到屏幕底行：`L`

## 文本选择
在普通文本编辑器中，要对文本进行复制、剪切等操作会先选中文本，再进行相应的操作。在Vim中也可以继续沿用这样的逻辑，如下面的方式一。此外，Vim还有一些高级操作，不用显式地先选中文本，就可以进行复制、删除等操作。
方式一：进入`可视模式`进行选择

## 文本复制、剪切(删除)与粘贴
- 复制整行: `yy`
- 复制当前单词: `yaw`
- 剪切整行: `dd`
- 剪切整行并重新输入: `cc`
- 剪切当前单词: `daw`
- 在光标后粘贴: `P`(小写)
- 在光标前粘贴: `P`(大写)
- 删除当前单词并重输入：`caw`

## 文本替换
- 替换光标所在字符：`r`
- 进入`替换模式`替换：`R`

## 其他
- 撤销：`u`
- 恢复：`Ctrl+r`
- 标记: `mx`
- 回到指定标记处：`x

# 插件管理
## Vim-Plug安装
github: https://github.com/junegunn/vim-plug
```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```
## 管理
以下命令在vim窗口下进行
- `:source ~/.vimrc`
- `:PlugInstall`: 安装插件
- `:PlugUpdate`: 插件更新
- `:PlugClean`: 插件清理

## 配置文件
自用配置文件，供参考：
```bash
# ~/.vimrc
set nocompatible    "去掉有关vi一致性模式,避免以前版本的bug和局限
set history=1000    "记录历史的行数
set background=dark "背景使用黑色
set guioptions-=T   "去除vim的GUI版本中得toolbar
set vb t_vb=        "当vim进行编辑时,如果命令错误,会发出警报,该设置去掉警报
set nohls           "默认情况下,寻找匹配是高亮度显示,该设置关闭高亮显示
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set number
set linebreak	"Break lines at word (requires Wrap lines)
set showbreak=+++	"Wrap-broken line prefix
set textwidth=100	"Line wrap (number of cols)
set showmatch	"Highlight matching brace
set visualbell	"Use visual bell (no beeping)
set hlsearch	"Highlight all search results
set smartcase	"Enable smart-case search
set ignorecase	"Always case-insensitive
set incsearch	"Searches for strings incrementally
set autoindent	"Auto-indent new lines
set shiftwidth=4	"Number of auto-indent spaces
set smartindent	"Enable smart-indent
set smarttab	"Enable smart-tabs
set softtabstop=4	"Number of spaces per Tab
set ruler	"Show row and column ruler information
set undolevels=1000	"Number of undo levels
set backspace=indent,eol,start

call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'

" Make sure you use single quotes

Plug 'Yggdroot/LeaderF', { 'do': './install.sh' }
Plug 'jiangmiao/auto-pairs'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'preservim/nerdtree'
Plug 'ghifarit53/tokyonight-vim'
Plug 'Yggdroot/indentLine'
Plug 'preservim/tagbar'

" Initialize plugin system
" - Automatically executes `filetype plugin indent on` and `syntax enable`.
call plug#end()
" You can revert the settings after the call like so:
"   filetype indent off   " Disable file-type-specific indentation
"   syntax off            " Disable syntax highlighting
"

" auto pairs配置
au Filetype FILETYPE let b:AutoPairs = {"(": ")"}
au FileType php      let b:AutoPairs = AutoPairsDefine({'<?' : '?>', '<?php': '?>'})

" airline配置
set laststatus=2  "永远显示状态栏
let g:airline_powerline_fonts = 1  " 支持 powerline 字体
" let g:airline#extensions#tabline#enabled = 1 “ 显示窗口tab和buffer
" let g:airline_theme='moloai'  " murmur配色不错

if !exists('g:airline_symbols')
let g:airline_symbols = {}
endif
let g:airline_left_sep = '▶'
let g:airline_left_alt_sep = '❯'
let g:airline_right_sep = '◀'
let g:airline_right_alt_sep = '❮'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'

" 解决tmux中粘贴缩进混乱
if &term =~ "screen"                                                   
    let &t_BE = "\e[?2004h"                                              
    let &t_BD = "\e[?2004l"                                              
    exec "set t_PS=\e[200~"                                              
    exec "set t_PE=\e[201~"                                              
endif

```