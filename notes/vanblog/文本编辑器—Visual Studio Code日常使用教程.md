## Cheetsheet
![](https://minio.kevin2li.top/image-bed/vanblog/img/6222e6c763413175ed72a5d43b158aff.2022-09-13-22-21-14.png)

<!-- more -->

## 常用快捷键

:::tip{title="如何查看所有快捷键列表"}
`Ctrl+K Ctrl+S`
:::

### 光标操作
#### 光标移动

##### 行内跳转
- `Ctrl+Right`: 光标右移一个单词
- `Ctrl+Left`: 光标左移一个单词
- `Fn+Left`: 光标移到行首
- `Fn+Right`: 光标移到行尾

##### 当前文件跳转
- `Ctrl+G`：快速跳转到指定行
- `Ctrl+Shift+O`：跳转到选中变量的首次定义位置

下面功能的依赖插件`Bookmarks`：
- `Ctrl+Alt+L`：跳转到下一个bookmark位置
- `Ctrl+Alt+J`：跳转到上一个bookmark位置


##### 跨文件跳转
- `Alt+Right`: 切换回打开过的前一个文件
- `Alt+Left`: 切换到打开过的后一个文件
- `Alt+Click`: 按住`Alt`，鼠标选中某个函数即可跳转


#### 多光标
- `Ctrl+Alt+Up`：在上一行添加一个光标
- `Ctrl+Alt+Down`：在下一行添加一个光标
- `Alt+Click`: 按住`Alt`再用鼠标点选设置多个光标

### 文本操作
#### 文本删除
- `Ctrl+Backspace`: 向左删除整个单词
- `Del+Backspace`: 向右删除整个单词
- `Ctrl+X`：删除当前行

#### 文本插入
- `Ctrl+Enter`：在当前行下方插入空行
- `Ctrl+Shift+Enter`：在当前行上方插入空行

#### 文本复制
- `Shift+Alt+Up`: 复制当前行到上一行
- `Shift+Alt+Down`：复制当前行到下一行

#### 文本移动
- `Alt+Up`：与上一行交换顺序
- `Alt+Down`: 与下一行交换顺序

#### 文本合并
- `Ctrl+J`：合并下一行

#### 文本选择
- `Ctrl+D`：选中光标所在单词，再次执行会选中下一个与当前单词相同的单词
- `Ctrl+A`：选中所有文本
- `Shift+Alt+Click`：鼠标拖选，可以纵向选择文本

下面功能的依赖插件`Quick and Simple Text Selection`：
- `Ctrl+K (`：选中`()`之间的内容
- `Ctrl+K [`：选中`[]`之间的内容
- `Ctrl+K <`：选中`<>`之间的内容
- `Ctrl+K '`：选中`''`之间的内容
- `Ctrl+K "`：选中`""`之间的内容
- `Ctrl+K {`：选中`{}`之间的内容


下面功能的依赖插件`Bookmarks`：
- `Shift+Alt+R`：选中从当前位置到下一个bookmark之间的文本
- `Shift+Alt+L`：选中从当前位置到上一个bookmark之间的文本


#### 文本查找
##### 当前文件查找
- `Ctrl+F`: 查找指定符号
- `Enter`: 查找下一个
- `Shift+Enter`: 查找上一个
##### 跨文件查找
- `Ctrl+Shift+F`: 查找指定符号

#### 文本替换
- `Ctrl+H`: 查找并替换文本

#### 变量重命名
- `F2`: 选中一个变量，按`F2`输入重命名后的变量

#### 文本折叠与展开
- `Ctrl+Shift+[`: 折叠`[]`之间的内容
- `Ctrl+Shift+]`: 展开`[]`之间的内容
- `Ctrl+Shift+{`: 折叠`{}`之间的内容
- `Ctrl+Shift+}`: 展开`{}`之间的内容


#### 文本注释
- `Ctrl+/`: 注释当前行(再次执行会取消注释)

#### 文本排序
- `Ctrl+Shift+P`: 输入`Sort Lines AScending`升序排列文本
- `Ctrl+Shift+P`: 输入`Sort Lines Descending`降序排列文本

### 文件操作

#### 文件路径
- `Shift+Alt+C`: 复制当前文件绝对路径(同样适用于文件Explore面板)
- `Ctrl+K Shift+Ctrl+C`: 复制当前文件相对路径

#### 文件查找
- `Ctrl+P`：选择跳转到已打开的编辑器文件(在打开的文件过多折叠到一起时很有用)
- `Ctrl+K Ctrl+P`：选择跳转到已打开的编辑器文件，并且按文件组分好类

#### 文件对比
- `Ctrl++K C`: 将当前文件与剪贴板内容对比

#### 文件格式化
- `Shift+Alit+F`: 格式化当前文档


### 终端
- `Ctrl+反引号`: 打开内置终端
- `Ctrl+Shift+反引号`: 新建终端
- `Ctrl+G`: 从列表中选择切换到目标目录
- `Ctrl+Up`: 滚动到命令执行开始处
- `Ctrl+Down`: 滚动到命令执行结束处

### 屏幕操作
#### 屏幕滚动
- `Ctrl+Up`: 界面向下滚动(光标位置不变)
- `Ctrl+Down`: 界面向上滚动(光标位置不变)

#### 分屏
- `Ctrl + \`：横向分屏

### 编辑器操作
#### 文件(夹)打开与关闭
- `Ctrl++N`: 打开新的空白文件
- `Ctrl++O`: 从列表中选择打开文件
- `Ctrl+K Ctrl++O`: 打开目录
- `Ctrl++W`: 关闭当前文件
- `Ctrl+Shift+T`: 恢复刚刚关闭的文件
- `Ctrl+Shift+E`: 在文件Explorer中聚焦当前文件
- `Ctrl+Shift+N`: 新建一个编辑器窗口
- `Ctrl+K+O`: 打开指定的文件目录
- `Ctrl+R`: 打开最近打开的文件目录
- `Alt+F4`: 关闭当前编辑器窗口

#### 编辑器组
- `Ctrl+K+W`:关闭所有编辑器组

##### 聚焦
- `Ctrl+1`: 聚焦到第1个编辑器组
- `Ctrl+2`: 聚焦到第2个编辑器组(如果没有则新建)
- `Ctrl+3`: 聚焦到第3个编辑器组

##### 布局调整
- `Ctrl+K Left`:向左移动当前编辑器组
- `Ctrl+K Right`:向右移动当前编辑器组
- `Ctrl+K Up`:向上移动当前编辑器组
- `Ctrl+K Down`:向下移动当前编辑器组

##### 编辑器移动
- `Ctrl+Alt+Left`: 将当前文件移动到上个编辑器组
- `Ctrl+Alt+Right`: 将当前文件移动到下个编辑器组
- `Ctrl+Alt+Right`: 将当前文件移动到下个编辑器组

##### 编辑器切换
`Ctrl+Tab`: 在当前编辑器组内选择文件打开

### 其他

- `Ctrl+Shift+P`：打开命令面板
- `Ctrl+Shift+B`：运行build任务
- `Ctrl+B`：显示/隐藏侧边栏
- `Ctrl+K V`:打开预览，支持markdown、latex等

## 使用Tips
### 快速删除空行
`Ctrl+H`在替换窗口勾选正则表达式按钮，在第一个文本框输入`^\s*(?=\r?$)\n`,选择全部替换即可。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/d57619681e2bdf744cc0649f132fef14.image.png)

### 自定义snippets
> 参考：https://code.visualstudio.com/docs/editor/userdefinedsnippets#_assign-keybindings-to-snippets

1. 打开snippets配置
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ce8137e4fbc1efa3888bee9dff8634ca.image.png)

选择要设置snippet的语言，然后添加snippet

样例：
```json
"Print to console": {
	"prefix": "log",
	"body": [
		"console.log('$1');",
		"$2"
	],
	"description": "Log output to console"
}
```
2. 为snippet设置快捷键

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/23bbd953e8d5d8ebf7a00d11295410ec.image.png)


添加条目，示例如下：
```json
  {
    "key": "ctrl+k 3",
    "command": "editor.action.insertSnippet",
    "when": "editorTextFocus",
    "args": {
      "langId": "python",
      "name": "# %%"
    }
  }
```

### 编辑需要sudo权限的文件
先占有文件，修改完后，再复原
```bash
sudo chown kevin2li <path_to_file>
code <path_to_file>
sudo chown root <path_to_file>
```

### 终端打开远程目录

```bash
 code --folder-uri=vscode-remote://ssh-remote+WS/home/kevin2li/
```

## 插件推荐

- `Database Client`  
连接数据库工具，支持mysql、mongodb等多种数据库
- `Blockman - Highlight Nested Code Blocks`  
代码块加边框，使代码更加清晰易读
- `Bookmarks`  
在代码指定位置添加标记，方便在文件不同位置来回跳转
- `Color Highlight`  
将16进制颜色代码高亮显示，方便查看其具体颜色
- `Git Graph`  
将git提交历史可视化展示
- `Gitlens`  
git仓库管理工具
- `LeetCode`  
算法刷题插件
- `Material Icon Theme`  
文件(夹)图标美化
- `Project Manager`  
将多个工程目录归档到一起，方便切换
- `Quick and Simple Text Selection`  
支持快速选中双引号、单引号、小括号等配对符号内的文本，非常推荐使用！
- `Rainbow CSV`  
将csv文件每列设置不同的颜色，方便查看
- `Tabnine`  
基于AI的代码智能补全插件，非常推荐！
- `Todo Tree`  
将代码中的todo、fixme的记号高亮显示
- `Color Highlight`  
代码中16进制颜色高亮
- `Better Align`  
代码对齐





