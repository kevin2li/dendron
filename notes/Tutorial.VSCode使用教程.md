---
id: 7twx9ycf6a3z5nkpj9k3wt7
title: VSCode使用教程
desc: ''
updated: 1683372524153
created: 1682510699184
---

## 简介


VS Code（Visual Studio Code）是一款免费、开源的代码编辑器，由微软开发和维护。它支持多种编程语言和框架，并提供了丰富的扩展功能，可以轻松地满足开发者的不同需求。

以下是 VS Code 的一些主要特点：

1. 跨平台：VS Code 可以在 Windows、macOS 和 Linux 上运行。

2. 内置调试器：VS Code 内置了调试器，支持多种语言和框架的调试。

3. 丰富的扩展功能：VS Code 有大量的扩展可供选择，可以满足不同开发者的需求。

4. 集成终端：VS Code 内置了终端，可以在编辑器内进行命令行操作。

5. Git 支持：VS Code 提供了 Git 集成，可以轻松地进行版本控制操作。

6. 快速编辑：VS Code 提供了多种快捷键和编辑工具，可以提高开发效率。

总之，VS Code 是一款功能强大的代码编辑器，可帮助开发者更高效地进行开发工作。

官网：https://code.visualstudio.com/  
文档：https://code.visualstudio.com/docs 
扩展市场：https://marketplace.visualstudio.com/VSCode

<!-- more -->



## 常用快捷键
### 查看、修改、新建、删除快捷键
1. 方法一  
可以通过快捷键`Ctrl+K Ctrl+S`打开快捷键面板，在其中可以查看、修改、新建和删除快捷键
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/70441e60710328da639205b3a400a875.image.png)

2. 方法二  

`Ctrl+Shift+P`找到想要的功能，然后点击该条最右侧的齿轮图标，可以直接跳转到快捷键分配界面

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/f49e26fd591331f0962810c874e2805c.image.png)

### 光标操作
#### 光标移动

##### 行内跳转

| 快捷键       | 功能             |
| ------------ | ---------------- |
| `Ctrl+Right` | 光标右移一个单词 |
| `Ctrl+Left`  | 光标左移一个单词 |
| `Fn+Left`    | 光标移到行首     |
| `Fn+Right`   | 光标移到行尾     |


下面功能的依赖插件[Quick and Simple Text Selection](https://marketplace.visualstudio.com/items?itemName=dbankier.vscode-quick-select):

| 快捷键     | 功能                                                 |
| ---------- | ---------------------------------------------------- |
| `Ctrl+K (` | 选中`()`之间的内容，然后使用左右方向键移到`()`前或后 |
| `Ctrl+K [` | 选中`[]`之间的内容，然后使用左右方向键移到`[]`前或后 |
| `Ctrl+K <` | 选中`<>`之间的内容，然后使用左右方向键移到`<>`前或后 |
| `Ctrl+K '` | 选中`''`之间的内容，然后使用左右方向键移到`''`前或后 |
| `Ctrl+K "` | 选中`""`之间的内容，然后使用左右方向键移到`""`前或后 |
| `Ctrl+K {` | 选中`{}`之间的内容，然后使用左右方向键移到`{}`前或后 |

##### 当前文件跳转
| 快捷键         | 功能                                                                                                                                                                  |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Ctrl+G`       | 快速跳转到指定行                                                                                                                                                      |
| `Ctrl+Shift+O` | 跳转到选中变量的首次定义位置。使用`@:`还可以将变量按类型分组![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/12ce447858bd81b0104d7e4f8063c764.image.png) |
| `Ctrl+U`       | 跳转到上次光标所在位置                                                                                                                                                |

下面功能的依赖插件[Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)：
- `Ctrl+Alt+L`：跳转到下一个bookmark位置
- `Ctrl+Alt+J`：跳转到上一个bookmark位置


##### 跨文件跳转
| 快捷键      | 功能                                                                                                                                           |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `Alt+Right` | 切换回打开过的前一个文件                                                                                                                       |
| `Alt+Left`  | 切换到打开过的后一个文件                                                                                                                       |
| `Alt+Click` | 按住`Alt`，鼠标选中某个函数即可跳转                                                                                                            |
| `Ctrl+T`    | 在工作区内查找指定对象定义位置并跳转 ![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/517890c7c8806dc2713b3754added173.image.png) |

#### 多光标
| 快捷键          | 功能                              |
| --------------- | --------------------------------- |
| `Ctrl+Alt+Up`   | 在上一行添加一个光标              |
| `Ctrl+Alt+Down` | 在下一行添加一个光标              |
| `Alt+Click`     | 按住`Alt`再用鼠标点选设置多个光标 |

### 文本操作
#### 文本删除
| 快捷键           | 功能             |
| ---------------- | ---------------- |
| `Ctrl+Backspace` | 向左删除整个单词 |
| `Ctrl+Del`       | 向右删除整个单词 |
| `Ctrl+X`         | 删除当前行       |

#### 文本插入
| 快捷键             | 功能                                   |
| ------------------ | -------------------------------------- |
| `Ctrl+Enter`       | 在当前行下方插入空行, 不需要光标在行尾 |
| `Ctrl+Shift+Enter` | 在当前行上方插入空行                   |

#### 文本复制
| 快捷键           | 功能               |
| ---------------- | ------------------ |
| `Shift+Alt+Up`   | 复制当前行到上一行 |
| `Shift+Alt+Down` | 复制当前行到下一行 |

#### 文本移动
| 快捷键     | 功能             |
| ---------- | ---------------- |
| `Alt+Up`   | 与上一行交换顺序 |
| `Alt+Down` | 与下一行交换顺序 |

#### 文本合并
| 快捷键   | 功能       |
| -------- | ---------- |
| `Ctrl+J` | 合并下一行 |

#### 文本选择
| 快捷键            | 功能                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Ctrl+D`          | 选中光标所在单词，再次执行会选中下一个与当前单词相同的单词。<br> `Alt+C`: 切换大小写匹配(默认是忽略大小写) <br> `Alt+W`: 切换全词匹配(默认是忽略全词匹配) <br> `Alt+R`: 切换正则匹配(默认不开启) |
| `Ctrl+Shift+L`    | 可以选中当前文件中所有当前出现的光标所在单词                                                                                                                                                     |
| `Ctrl+A`          | 选中所有文本                                                                                                                                                                                     |
| `Ctrl+L`          | 选中当前行文本                                                                                                                                                                                   |
| `Shift+Alt+Click` | 鼠标拖选，可以纵向选择文本                                                                                                                                                                       |

下面功能的依赖插件[Quick and Simple Text Selection](https://marketplace.visualstudio.com/items?itemName=dbankier.vscode-quick-select)：

| 快捷键     | 功能               |
| ---------- | ------------------ |
| `Ctrl+K (` | 选中`()`之间的内容 |
| `Ctrl+K [` | 选中`[]`之间的内容 |
| `Ctrl+K <` | 选中`<>`之间的内容 |
| `Ctrl+K '` | 选中`''`之间的内容 |
| `Ctrl+K "` | 选中`""`之间的内容 |
| `Ctrl+K {` | 选中`{}`之间的内容 |


下面功能的依赖插件[Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)：

| 快捷键        | 功能                                     |
| ------------- | ---------------------------------------- |
| `Shift+Alt+R` | 选中从当前位置到下一个bookmark之间的文本 |
| `Shift+Alt+L` | 选中从当前位置到上一个bookmark之间的文本 |

#### 文本查找
##### 当前文件查找
| 快捷键        | 功能         |
| ------------- | ------------ |
| `Ctrl+F`      | 查找指定符号 |
| `Enter`       | 查找下一个   |
| `Shift+Enter` | 查找上一个   |

##### 跨文件查找
| 快捷键         | 功能         |
| -------------- | ------------ |
| `Ctrl+Shift+F` | 查找指定符号 |

#### 文本替换
| 快捷键   | 功能           |
| -------- | -------------- |
| `Ctrl+H` | 查找并替换文本 |

#### 变量重命名
| 快捷键 | 功能                                   |
| ------ | -------------------------------------- |
| `F2`   | 选中一个变量，按`F2`输入重命名后的变量 |

#### 文本折叠与展开
| 快捷键         | 功能               |
| -------------- | ------------------ |
| `Ctrl+Shift+[` | 折叠`[]`之间的内容 |
| `Ctrl+Shift+]` | 展开`[]`之间的内容 |
| `Ctrl+Shift+{` | 折叠`{}`之间的内容 |
| `Ctrl+Shift+}` | 展开`{}`之间的内容 |


#### 文本注释
| 快捷键   | 功能                           |
| -------- | ------------------------------ |
| `Ctrl+/` | 注释当前行(再次执行会取消注释) |

#### 文本自动换行
| 快捷键  | 功能             |
| ------- | ---------------- |
| `Alt+Z` | 是否触发自动换行 |

#### 文本排序
| 快捷键         | 功能                                    |
| -------------- | --------------------------------------- |
| `Ctrl+Shift+P` | 输入`Sort Lines AScending`升序排列文本  |
| `Ctrl+Shift+P` | 输入`Sort Lines Descending`降序排列文本 |

#### 文本格式化
| 快捷键         | 功能               |
| -------------- | ------------------ |
| `Shift+Alit+F` | 格式化整个文档     |
| `Ctrl+K+F`     | 格式化当前选中文本 |

### 文件操作

#### 文件路径
| 快捷键                | 功能                                            |
| --------------------- | ----------------------------------------------- |
| `Shift+Alt+C`         | 复制当前文件绝对路径(同样适用于文件Explore面板) |
| `Shift+Alt+R`         | 在文件资源管理器中打开当前文件                  |
| `Ctrl+K Shift+Ctrl+C` | 复制当前文件相对路径                            |

#### 文件查找
| 快捷键          | 功能                                                             |
| --------------- | ---------------------------------------------------------------- |
| `Ctrl+P`        | 选择跳转到已打开的编辑器文件(在打开的文件过多折叠到一起时很有用) |
| `Ctrl+K Ctrl+P` | 选择跳转到已打开的编辑器文件，并且按文件组分好类                 |

#### 文件对比
| 快捷键      | 功能                       |
| ----------- | -------------------------- |
| `Ctrl++K C` | 将当前文件与剪贴板内容对比 |


### 终端
| 快捷键              | 功能                       |
| ------------------- | -------------------------- |
| `Ctrl+反引号`       | 打开内置终端               |
| `Ctrl+Shift+反引号` | 新建终端                   |
| `Ctrl+G`            | 从列表中选择切换到目标目录 |
| `Ctrl+Up`           | 滚动到命令执行开始处       |
| `Ctrl+Down`         | 滚动到命令执行结束处       |

### 屏幕操作
#### 屏幕滚动
| 快捷键       | 功能                                                           |
| ------------ | -------------------------------------------------------------- |
| `Ctrl+Up`    | 界面向下滚动(光标位置不变)                                     |
| `Ctrl+Down`  | 界面向上滚动(光标位置不变)                                     |
| `Alt+Scroll` | 按住`Alt`再滚动，可以实现5倍速的快速滚动，对于阅读长文件时有用 |

#### 分屏

| 快捷键     | 功能     |
| ---------- | -------- |
| `Ctrl + \` | 横向分屏 |

### 编辑器操作
#### 文件(夹)打开与关闭 

| 快捷键               | 功能                         |
| -------------------- | ---------------------------- |
| `Ctrl++N`            | 打开新的空白文件             |
| `Ctrl++O`            | 从列表中选择打开文件         |
| `Ctrl+K Ctrl++O`     | 打开目录                     |
| `Ctrl++W`            | 关闭当前文件                 |
| `Ctrl+Shift+T`       | 恢复刚刚关闭的文件           |
| `Ctrl+Shift+E`       | 在文件Explorer中聚焦当前文件 |
| `Ctrl+Shift+N`       | 新建一个编辑器窗口           |
| `Ctrl+K+O`           | 打开指定的文件目录           |
| `Ctrl+R`             | 打开最近打开的文件目录       |
| `Alt+F4`             | 关闭当前编辑器窗口           |
| `Ctrl+K Shift+Enter` | 固定当前编辑器窗口           |

#### 编辑器组
| 快捷键     | 功能             |
| ---------- | ---------------- |
| `Ctrl+K+W` | 关闭所有编辑器组 |

##### 聚焦
| 快捷键          | 功能                                |
| --------------- | ----------------------------------- |
| `Ctrl+1`        | 聚焦到第1个编辑器组                 |
| `Ctrl+2`        | 聚焦到第2个编辑器组(如果没有则新建) |
| `Ctrl+3`        | 聚焦到第3个编辑器组                 |
| `Ctrl+PageUp`   | 聚焦到第上个编辑器                  |
| `Ctrl+PageDown` | 聚焦到第下个编辑器                  |

##### 布局调整
| 快捷键         | 功能                 |
| -------------- | -------------------- |
| `Ctrl+K Left`  | 向左移动当前编辑器组 |
| `Ctrl+K Right` | 向右移动当前编辑器组 |
| `Ctrl+K Up`    | 向上移动当前编辑器组 |
| `Ctrl+K Down`  | 向下移动当前编辑器组 |


##### 编辑器移动 
| 快捷键           | 功能                         |
| ---------------- | ---------------------------- |
| `Ctrl+Alt+Left`  | 将当前文件移动到上个编辑器组 |
| `Ctrl+Alt+Right` | 将当前文件移动到下个编辑器组 |
| `Ctrl+Alt+Right` | 将当前文件移动到下个编辑器组 |

##### 编辑器切换 
| 快捷键     | 功能                         |
| ---------- | ---------------------------- |
| `Ctrl+Tab` | 在当前编辑器组内选择文件打开 |

### 其他
| 快捷键         | 功能                            |
| -------------- | ------------------------------- |
| `Ctrl+Shift+P` | 打开命令面板                    |
| `Ctrl+,`       | 打开settings                    |
| `Ctrl+Shift+B` | 运行build任务                   |
| `Ctrl+B`       | 显示/隐藏侧边栏                 |
| `Ctrl+K V`     | 打开预览，支持markdown、latex等 |


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

### 切换不同Profile
参考: [Profiles in Visual Studio Code](https://code.visualstudio.com/docs/editor/profiles)  

::: tip  背景
vscode有很多设置项、很多扩展,以及很多UI设置项,此功能允许对不同的项目需要进行不同的配置,并实现快速切换,甚至与他人共享设置.
:::
支持的操作:  

![](https://minio.kevin2li.top/image-bed/20230428162041.png)

## 插件推荐
| 插件                                                                                                                | 功能                                                                 |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager)                  | 将多个工程目录归档到一起，方便切换                                   |
| [Quick and Simple Text Selection](https://marketplace.visualstudio.com/items?itemName=dbankier.vscode-quick-select) | 支持快速选中双引号、单引号、小括号等配对符号内的文本，非常推荐使用！ |
| [Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)                              | 在代码指定位置添加标记，方便在文件不同位置来回跳转                   |
| [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)                | 文件(夹)图标美化                                                     |
| [Blockman - Highlight Nested Code Blocks](https://marketplace.visualstudio.com/items?itemName=leodevbro.blockman)   | 代码块加边框，使代码更加清晰易读                                     |
| [Color Highlight](https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight)                      | 将16进制颜色代码高亮显示，方便查看其具体颜色                         |
| [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)                                 | 将git提交历史可视化展示                                              |
| [Gitlens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)                                      | git仓库管理工具                                                      |
| [Peacock](https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock)                              | 修改vscode窗口颜色,当同时打开多个不同的vscode窗口时更方便区分        |
| [Better Align](https://marketplace.visualstudio.com/items?itemName=Chouzz.vscode-better-align)                      | 代码对齐                                                             |
| `Rainbow CSV`                                                                                                       | 将csv文件每列设置不同的颜色，方便查看                                |
| `Tabnine`                                                                                                           | 基于AI的代码智能补全插件，非常推荐！                                 |
| `Todo Tree`                                                                                                         | 将代码中的todo、fixme的记号高亮显示                                  |
| `Database Client`                                                                                                   | 连接数据库工具，支持mysql、mongodb等多种数据库                       |
| `LeetCode`                                                                                                          | 算法刷题插件                                                         |


## Cheetsheet
![](https://minio.kevin2li.top/image-bed/vanblog/img/6222e6c763413175ed72a5d43b158aff.2022-09-13-22-21-14.png)
