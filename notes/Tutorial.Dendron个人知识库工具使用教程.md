---
id: w856oji82penovksem8vhl3
title: Dendron个人知识库工具使用教程
desc: ''

updated: 1684480559455
created: 1682510384431
---

## 简介
Dendron是一款面向程序员的知识库软件，它基于文本文件，使用Markdown语言进行格式化，允许用户创建和组织个人知识库，并快速查找和共享这些信息。Dendron的设计理念是将知识组织成树状结构，以便于用户快速定位和理解各个知识点之间的关系。

![](https://minio.kevin2li.top/image-bed/20230428185627.png)

Dendron提供了多种功能，包括创建多个笔记本、在笔记中添加文本、代码块、图片等内容、使用标签、链接、目录等功能进行组织和分类、强大的搜索功能以及与其他知识库软件的集成等。

对于程序员来说，Dendron非常适合用于存储和组织代码、API文档、技术博客、笔记等信息。通过使用Dendron，程序员可以更加高效地管理和利用自己的知识库，提高工作效率和代码质量。

官网: [https://www.dendron.so/](https://www.dendron.so/)

文档: [https://wiki.dendron.so/](https://wiki.dendron.so/)

## 方法

>背景：由于Dendron很多功能都没有设置快捷键，使用起来不是很方便，但是可以自己为其指定快捷键。VSCode中指定快捷键的方式可以参考：
![[快捷键设置|Tutorial.VSCode使用教程#查看修改新建删除快捷键]]

### note管理

| 快捷键                | 功能                                                       |
| --------------------- | ---------------------------------------------------------- |
| `Ctrl+L`              | 创建/查找note                                              |
| `Ctrl+K Ctrl+Shift+X` | 重命名note                                                 |
| `Ctrl+Shift+D`        | 删除当前note                                               |
| `Ctrl+K Shift+Alt+R`  | Refactor Hierachy, 把所有文件名中匹配到的部分替换为其他    |
| `Ctrl+K Ctrl+Shift+H` | Move Header, 把当前note光标下的标题移动到其他note尾部      |
| `Ctrl+K Ctrl+Shift+S` | Move Selection, 把当前note鼠标选中的部分移动到其他note尾部 |
| `Ctrl+K Ctrl+Shift+T` | Apply Template, 在当前note中应用模板                       |
| `Ctrl+K Ctrl+Enter`   | Go to Note, 跳转到目标note，没有会自动新建                 |

当创建很长名字的note时，可以先在文档中编辑好，然后光标放在名称上，然后使用`Dendron: Go to Note`会自动创建。

### link管理
| 快捷键         | 功能                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------ |
| `Ctrl+Shift+C` | 获取当前激活note的link，插入后只会显示一个超链接。如果在标题处使用则会生成直接指向目标标题的链接 |
| `Ctrl+Shift+R` | 获取当前激活note的reference，插入后会在当前页面显示目标页面                                      |

1. 获取note部分内容的link

2. 引用note

3. 部分引用note


### schema管理
参考: [dendron | Schemas](https://wiki.dendron.so/notes/c5e5adde-5459-409b-b34d-a0d75cbb1052/)

设置`schema`可以从已有的markdown文件中生成结构和类型提示,在创建新note时可以进行参考,也可以指定应用模板.
其中`schema`中的`id`和`pattern`是会去匹配文件名的属性.

#### 方式一: `childred`属性下指定孩子节点的`id`
``` yaml 
version: 1
schemas:
# this will match "cli.*" notes
- id: cli 
  # human readable description of hierarchy
  desc: command line interface reference
  # add this to the domain of your schema hierarchy
  parent: root
  # when a schema is a namespace, it can have arbitrary children. equivalent to cli.* glob pattern
  namespace: true 
  children:
    - cmd
    - env
# will match cli.*.env
- id: env
  desc: cli specific env variables
# will match cli.*.cmd.*
- id: cmd
  desc: subcommands 
  namespace: true
```

匹配的结构如下:

![](https://minio.kevin2li.top/image-bed/20230428182504.png)

#### 方式二(推荐): `childred`属性下指定孩子的`pattern`
``` yaml 
version: 1
schemas:
  # Daily is the top most schema since its parent is 'root' it must have an identifier
  # this identifier 'daily' will be used when using 'Lookup (schema)' command.
  - id: daily
    parent: root
    # Children of the top most schema do not need to contain identifier and just 
    # require a 'pattern' to be set to match the hierarchy of notes.
    children:
      - pattern: journal
        children:
          - pattern: "[0-2][0-9][0-9][0-9]"
            children:
              - pattern: "[0-1][0-9]"
                children:
                  - pattern: "[0-3][0-9]"
                    # As with regular schema we can set the template to be used with
                    # the match of our notes. Below is an example usage of shorthand template
                    # definition (which defaults to type: note). 
                    template: templates.daily
```
此方式更容易看出层级结构.

::: tip  重建索引
修改完schema后可能不会立即生效,可以重建索引或者重新加载窗口重试一下.

重建索引快捷键如下(需要自己设置):

`Ctrl+K Ctrl+Shift+R`: `Dendron: Reload Index`
:::
### 模板(Template)
#### 方式一: 当前页面应用
任意新建一个文件, 一般位于`template`目录下,然后可以使用`Ctrl+K Ctrl+Shift+T`在当前页面应用模板

#### 方式二: 与schema绑定自动应用
``` yaml 
version: 1
schemas:
- id: blog
  title: Blog
  desc: ""
  parent: root
  children:
    - pattern: "+([!])"
      template: template.blog
```
在与`pattern`同层级加入`template`属性来指定应用的模板.

`pattern`语法:
| name               | function                                   |
| ------------------ | ------------------------------------------ |
| "[!0-9]"           | will match anything that's not a digit     |
| "*([0-9])"         | will match 0 or more digits                |
| "+([0-9])"         | will match 1 or more digits                |
| "*"                | will match 0 or more of any character      |
| "+([!])"           | will match 1 or more of any character      |
| "@(left \| right)" | will match left or right, but nothing else |
| "!(thing)"         | will match anything other than thing       |


模板变量:
| name                         | function                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------- |
| `CURRENT_YEAR`               | The current year                                                                      |
| `CURRENT_MONTH`              | The month as two digits (example: 02 for February)                                    |
| `CURRENT_WEEK`               | The week of the year as two digits (example: 17)                                      |
| `CURRENT_DAY`                | The day of the month as two digits (example: 08)                                      |
| `CURRENT_HOUR`               | The current hour in 24-hour clock format (example: 23)                                |
| `CURRENT_MINUTE`             | The current minute as two digits (example: 05)                                        |
| `CURRENT_SECOND`             | The current second as two digits (exmplae: 32)                                        |
| `CURRENT_QUARTER`            | The current quarter as one-indexed single digit number (example: 1 for first quarter) |
| `CURRENT_MONTH_NAME`         | The month as string name (example: January)                                           |
| `CURRENT_MONTH_NAME_SHORT`   | The month as abbreviated string name (example: Jan for January)                       |
| `CURRENT_DAY_OF_WEEK`        | equivalent of javascript getDay method (example: 3 for Monday)                        |
| `CURRENT_DAY_OF_WEEK_ABBR`   | The day of week, as an abbreviated localized string (example: Wed for Wednesday)      |
| `CURRENT_DAY_OF_WEEK_FULL`   | The day of week, as an unabbreviated localized string (example: Wednesday),           |
| `CURRENT_DAY_OF_WEEK_SINGLE` | (example: W for Wednesday),                                                           |
| `TITLE`                      | The title of the note as appeared on frontmatter                                      |
| `FNAME`                      | name of current file                                                                  |
| `DESC`                       | description of current file (equivalent to the desc field in the Dendron frontmatter) |

可以使用`{{ VARIABLE }}`在正文中引用变量.

### Markdown快捷键
依赖插件:[Dendron Markdown Shortcuts](https://marketplace.visualstudio.com/items?itemName=dendron.dendron-markdown-shortcuts)

| 快捷键          | 功能                                                                             |
| --------------- | -------------------------------------------------------------------------------- |
| `Ctrl+M Ctrl+M` | 调出常用md格式: <br>![](https://minio.kevin2li.top/image-bed/20230428180010.png) |

## 参考

1. [https://wiki.dendron.so/](https://wiki.dendron.so/)