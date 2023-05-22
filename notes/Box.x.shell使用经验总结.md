---
id: 3u9zp9mnos2wn5j8labzoj6
title: shell使用经验总结
desc: ''
updated: 1684724043785
created: 1684722933268
---

## 路径后带与不带"/"的区别

对大多数命令无影响，对个别命令有影响。

### 对`rm`的影响
``` bash 
rm -rf dir # 删除目录下所有内容，包括目录本身
rm -rf dir/* # 清空目录下内容，但保留目录本身
```

### 对`cp`的影响
命令格式：`cp [OPTION]... SOURCE... DIRECTORY`
``` bash 
cp -r dirA dirB # dirA成为dirB的子目录
cp -r dirA dirB/ # dirB与dirB有相同结构
```

## `rm`使用技巧
### 排除文件夹删除
1. bash
``` bash 
rm -rf dirA/!(dirB)      # 删除dirA中除了dirB的内容
rm -rf dirA/!(dirB|dirC) # 删除dirA中除了dirB和dirC的内容
``
