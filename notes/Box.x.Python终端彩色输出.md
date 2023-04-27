---
id: m7wf2abasold6zw7eg78v40
title: Python终端彩色输出
desc: ''
updated: 1682589246605
created: 1682589238394
---
# 简介
ANSI颜色格式是一种将特定的数字序列映射到不同的文本颜色和样式的标准。 在终端中使用这些数字序列可以使我们在控制台中输出彩色文本。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/6a2222e2888a93e76a1dfa0477a06c56.image.png)

ANSI颜色格式有以下格式：

```
\033[格式代码m 加颜色的文本 \033[0m
```

其中，`\033` 表示转义字符，`[ ]` 表示可选项，格式代码表示颜色和样式代码。

<!-- more -->

例如，`\033[31m` 表示将文本变成红色。以下是一些常用的ANSI颜色代码：

- `30m` 黑色
- `31m` 红色
- `32m` 绿色
- `33m` 黄色
- `34m` 蓝色
- `35m` 紫色
- `36m` 青色
- `37m` 白色

ANSI格式还支持设置颜色和样式的组合，如下所示：

- `1m` 粗体
- `4m` 下划线
- `5m` 闪烁
- `7m` 反色
- `8m` 隐藏

例如，`\033[31;4m` 表示将文本设置为红色和下划线。

需要注意的是，不是所有的终端都支持ANSI颜色格式，因此在编写程序时需要根据不同的终端做出相应的调整。


# 方法

```python
def print红(*args,**kwargs):
    print("\033[0;31m",*args,"\033[0m",**kwargs)
def print绿(*args,**kwargs):
    print("\033[0;32m",*args,"\033[0m",**kwargs)
def print黄(*args,**kwargs):
    print("\033[0;33m",*args,"\033[0m",**kwargs)
def print蓝(*args,**kwargs):
    print("\033[0;34m",*args,"\033[0m",**kwargs)
def print紫(*args,**kwargs):
    print("\033[0;35m",*args,"\033[0m",**kwargs)
def print靛(*args,**kwargs):
    print("\033[0;36m",*args,"\033[0m",**kwargs)

def print亮红(*args,**kwargs):
    print("\033[1;31m",*args,"\033[0m",**kwargs)
def print亮绿(*args,**kwargs):
    print("\033[1;32m",*args,"\033[0m",**kwargs)
def print亮黄(*args,**kwargs):
    print("\033[1;33m",*args,"\033[0m",**kwargs)
def print亮蓝(*args,**kwargs):
    print("\033[1;34m",*args,"\033[0m",**kwargs)
def print亮紫(*args,**kwargs):
    print("\033[1;35m",*args,"\033[0m",**kwargs)
def print亮靛(*args,**kwargs):
    print("\033[1;36m",*args,"\033[0m",**kwargs)
```

# 演示

```python
text = "Hello World!!!"
print红(text)
print绿(text)
print黄(text)
print蓝(text)
print紫(text)
print靛(text)
print("-"*20)
print亮红(text)
print亮绿(text)
print亮黄(text)
print亮蓝(text)
print亮紫(text)
print亮靛(text)
```
效果：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/44b1ae51bf1e6818f9b3e4f3533f2f14.image.png)