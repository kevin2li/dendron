---
id: cgnymkueocfyxulqqn56f81
title: Zotero文献管理软件安装与使用教程
desc: ''
updated: 1684831327637
created: 1684826464055
---

## 简介
![](https://minio.kevin2li.top/image-bed/blog/20230523152342.png)

Zotero是一款免费而开源的参考文献管理软件，它可以帮助用户收集、整理和分享学术文献。Zotero支持多种平台，包括Windows、macOS和Linux，并提供了浏览器插件，可以方便地从网页中捕获参考文献信息。此外，Zotero还支持多种文献格式，如APA、MLA、Chicago等，并可与Microsoft Word、LibreOffice、Google Docs等文本编辑器集成，方便地插入参考文献和生成参考文献列表。

Zotero的主要特点包括：

- **参考文献管理**：Zotero允许用户创建个人文献库，方便地存储和管理参考文献，支持多种文献格式，如图书、期刊文章、报告、网页等。

- **检索和导入**：Zotero提供了浏览器插件，可以方便地从网页中捕获参考文献信息，并将其导入到个人文献库中。用户还可以通过检索在线数据库，如PubMed、Google Scholar等，检索并导入参考文献信息。

- **文献管理工具**：Zotero提供了丰富的文献管理工具，如标签、文件夹、搜索、排序等，方便用户对文献进行组织和查找。

- **参考文献格式化**：Zotero支持多种参考文献格式，如APA、MLA、Chicago等，用户可以根据需要选择相应的格式，并自动格式化参考文献列表。

- **文本编辑器集成**：Zotero可以与Microsoft Word、LibreOffice、Google Docs等文本编辑器集成，方便地插入参考文献和生成参考文献列表。

- **多平台支持**：Zotero支持多种平台，包括Windows、macOS和Linux，用户可以在不同的平台上使用Zotero，并同步其文献库和设置。

- **共享**：Zotero提供了共享功能，用户可以将其文献库共享给其他用户，也可以加入其他用户的共享库。

总之，Zotero是一款功能强大的参考文献管理工具，可以帮助用户轻松地收集、整理和分享学术文献，提高学术写作的效率和质量。

官网: https://www.zotero.org/  
文档: https://www.zotero.org/support/

# 安装

参考: https://www.zotero.org/download/

## 使用
### 基本使用
1. 语言设置

"编辑>首选项>高级>常规"

![](https://minio.kevin2li.top/image-bed/blog/20230523153552.png)

2. 添加附件

![](https://minio.kevin2li.top/image-bed/blog/20230523163059.png)

3. 附件存储位置  

"编辑>首选项>高级>文件和文件夹"

![](https://minio.kevin2li.top/image-bed/blog/20230523153712.png)

设置根目录后,附件会使用相对路径存储,当迁移设备时,只要修改一下根目录,还可以方便链接到附件地址.

3. 备份  

为了方便在不同设备间同步,需要注册一个zotero账号,然后在附件同步时可以选择一个支持webDAV协议的同步盘进行存储,如[坚果云](https://www.jianguoyun.com/)等,或者自己搭建WebDAV网盘.

![](https://minio.kevin2li.top/image-bed/blog/20230523154014.png)

由于Zotero附件的默认存储位置位于`C:\Users\{username}\Zotero`. 我们可以借助`ZotFile`插件(后面会介绍)将附件自动移动到指定的附件存储目录中,只需要在不同设备上同步该附件目录,并设置好根目录路径,即可跨设备访问.


4. 标签  

在主面板右侧,有个标签选项卡,可以进行标签设置,左下角可以进行标签的筛选.

![](https://minio.kevin2li.top/image-bed/blog/20230523163523.png)

### 常用插件
1. ZotFile  
一款管理附件的插件，可以帮助用户更好地管理和存储参考文献附件，如PDF、图片等，并支持将文件重命名、移动、复制等操作。  
地址: http://zotfile.com/

**配置:**

- 打开配置界面:

![](https://minio.kevin2li.top/image-bed/blog/20230523154725.png)

- 指定移动到新目录的路径,可以设置为你的附件同步目录的路径,这样每次新文献的附件都会移动到同步目录中.

![](https://minio.kevin2li.top/image-bed/blog/20230523154915.png)

还可以勾选上"Use subfolder defined by"选项,并指定自定义的规则,这样可以将附件按照你指定的规则分门别类放好,而不是全部集中在一个文件夹下.

- 移动重命名时的规则:

![](https://minio.kevin2li.top/image-bed/blog/20230523155009.png)

- 打开"Always rename",这样每次新附件都会自动重命名并移动到指定的目录.

![](https://minio.kevin2li.top/image-bed/blog/20230523155230.png)

2. Zutilo  
一款Zotero增强工具，提供了许多实用的功能，如批量修改、批量搜索、批量删除等。  
地址: https://github.com/wshanks/Zutilo

**配置:**

默认配置下, Zutilo的上下文菜单只有右下角红框中的四条.

![](https://minio.kevin2li.top/image-bed/blog/20230523160307.png)

但实际上, Zutilo支持的设置项非常丰富.

![](https://minio.kevin2li.top/image-bed/blog/20230523160637.png)

![](https://minio.kevin2li.top/image-bed/blog/20230523160515.png)

这里我们把`修改附件`这项勾选.


下面演示一下使用场景:

比如这里有一篇文献,它的路径存在问题导致Zotero找不到它的附件地址.

![](https://minio.kevin2li.top/image-bed/blog/20230523161232.png)

但是我们知道这篇文献其实是位于`\\ws.kevin2li.top\hdd\zotero`目录下的, 而不是原来的`E:\zotero_attachment`目录下, 并且文件名相同(如果你采用的是相对路径存储附件,文件名一般都是相同的).

我们可以右键选中这篇文献,然后选择Zutilo的`修改附件路径`功能

![](https://minio.kevin2li.top/image-bed/blog/20230523162309.png)

输入要替换的旧路径:

![](https://minio.kevin2li.top/image-bed/blog/20230523162434.png)

输入新路径:

![](https://minio.kevin2li.top/image-bed/blog/20230523162459.png)

确认之后,附件的路径就从原来的父目录`E:\zotero_attachment`修改为了`\\ws.kevin2li.top\hdd\zotero`,这样就可以正确打开附件了.

该功能还可以批量选择文献,从而进行批量修改路径.

::: tip  如何安装插件
- 下载`xpi`格式插件

- "工具>附加组件"

![](https://minio.kevin2li.top/image-bed/blog/20230523153054.png)

- "Install Add-on From File"

![](https://minio.kevin2li.top/image-bed/blog/20230523153159.png)

在弹出的对话框中选择下载的`xpi`插件进行安装.

:::

## 参考

1. [少数派 | 文献管理神器 Zotero 学习路径指南](https://sspai.com/post/56724)
2. [少数派 | 文献管理利器 Zotero 设置技巧](https://sspai.com/post/59035#!)