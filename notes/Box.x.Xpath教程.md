---
id: mlbj2teyso64mjmtvzn2mqp
title: Xpath教程
desc: ''
updated: 1685776327934
created: 1685766752828
---

## 格式

![](https://minio.kevin2li.top/image-bed/blog/20230603123531.png)

## 常用场景
### 提取标签
``` bash 
//html/div/a
```

### 按标签属性提取
``` bash
# 提取含有class属性的div标签
//div[@class]

# id为123的任意元素
//*[@id="123"]

# className为123的任意元素
//*[@class="123"]

# 类型为submit的input
//input[@type="submit"]
```

### 按函数匹配提取
``` bash 
# href以"/"开头的a标签
//a[starts-with(@href, '/')]

# href以".pdf"结尾的a标签 
//a[ends-with(@href, '.pdf')]

# href中包含"://"的a标签
//a[contains(@href, '://')]

# 文本中包含'://'的a标签
//a[contains(text(), '://')]

```

### 按顺序提取

``` bash 
# 提取ul元素下的第二个li标签
//ul/li[2]

# 提取ul元素下的最后一个li标签
//ul/li[last()]
```

### 提取指定元素的文本或属性

``` bash 
# 提取span元素的文本
//span/text()

# 提取a标签的href属性
//div[@class='lessontable-row-title']/a/@href"
```

### 逻辑连接
``` bash 
# 类型为submit 或者name属性为btnReset的元素
//*[@type='submit' or @name='btnReset']

# 类型为submit 并且name属性为btnLogin的元素
//input[@type='submit' and @name='btnLogin']

```

### axes方法

| Axes 方法          | 描述                                           |
| ------------------ | ---------------------------------------------- |
| following          | 返回当前节点之后的所有节点                     |
| following-sibling  | 返回当前节点之后的所有同级节点                 |
| preceding          | 返回当前节点之前的所有节点                     |
| preceding-sibling  | 返回当前节点之前的所有同级节点                 |
| parent             | 返回当前节点的父节点                           |
| child              | 返回当前节点的所有子节点                       |
| ancestor           | 返回所有祖先节点，包括父节点和更高层的祖先节点 |
| ancestor-or-self   | 返回所有祖先节点和当前节点本身                 |
| descendant         | 返回当前节点的所有后代节点，不包括自身         |
| descendant-or-self | 返回当前节点的所有后代节点，包括自身           |
| namespace          | 返回当前节点的所有命名空间节点                 |
| attribute          | 返回当前节点的所有属性节点                     |
| self               | 返回当前节点本身                               |

使用举例：
``` bash 
# 当前节点之后的所有input标签
//*[@type='text']//following::input

# 当前节点的所有祖先节点中的div标签
//*[text()='Enterprise Testing']//ancestor::div[1]

# 当前节点的孩子节点中的li标签
//*[@id='java_technologies']//child::li
```
## 参考
1. https://www.guru99.com/xpath-selenium.html
