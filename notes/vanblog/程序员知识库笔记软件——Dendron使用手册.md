# 简介
[Dendron](https://www.dendron.so/)是一款专门面向程序员群体的笔记软件，主体功能都是由在程序员中广泛流行的编辑器VS Code的插件提供的，如下是软件界面截图。

![](https://minio.kevin2li.top/image-bed/vanblog/img/f5603b78ee66446c949e0fd0c1339e79.20221020092948.png)

特性：
- 双链笔记：支持反向链接，并提供图形视图可视化你的知识库
- 灵活与一致：采用"."命名法来构建知识库体系结构，易于重构和扩展(只需要重命名即可)
- 本地优先：所有笔记都是Markdown文件，可以通过git来进行版本控制，也易于迁移到其他平台
- ...

<!-- more -->

# 使用指南
## 安装
需要安装[VS Code](https://code.visualstudio.com/download), 以及安装两个插件：
1. [dendron](https://marketplace.visualstudio.com/items?itemName=dendron.dendron)
2. [Dendron Paste Image](https://marketplace.visualstudio.com/items?itemName=dendron.dendron-paste-image): 可以快速粘贴图片

## 写作
采用纯Markdown写作，[Dendron支持的Markdown语法](https://wiki.dendron.so/notes/ba97866b-889f-4ac6-86e7-bb2d97f6e376/)包含丰富的类型，诸如标题、列表、引用、表格、图片、Mermaid画图等等

## 常用快捷键：
快捷键列表：https://wiki.dendron.so/notes/eea2b078-1acc-4071-a14e-18299fc28f47/#copy-note-url
- 查找和创建note: `Ctrl+L`
- 查找和创建schema: `Ctrl+Shift+L`
- 复制ref: `Ctrl+Shift+R`
- 复制link: `Ctrl+Shift+C`
- 删除note: `Ctrl+Shift+D`
- 重命名note: ·`Ctrl+Shift+P`, `Dendron: Rename Note`
- 转到父note: `Ctrl+Shift+upArrow`
- 转到子note: `Ctrl+Shift+downArrow`
- 新建journal note: `Ctrl+Shift+I`
- 打开预览: `Ctrl+K V`
- 粘贴图片: `Ctrl+Alt+V`

## 以下命令为`Ctrl+Shift+P`下使用：
- 打开全局配置文件dendron.yml: `Dendron: Configure (yaml)`
- 重命名：`Dendron: Rename Note`
- 导出笔记：`Dendron: Export Pod`
- 创建schema：`Dendron ： Create Schema From Note Hierarchy`
<!-- vault相关 -->
- 创建新的workspace: `Dendron: lnitialize Workspace`
- 切换workspace: `Dendron: Change Workspace`
- 添加并提交workspace: `Dendron: Workspace: Add a nd Commit`
- 创建Vault：`Dendron: Vault Add`
- 删除Vault：`Dendron: Vault Remove`

## Schema的使用
创建schema可以在创建新note的时候出现提示，使得创建的note更符合一致性

![](https://minio.kevin2li.top/image-bed/vanblog/img/4c1e2bd4575205f56f20db5653dcb272.2022-09-15-23-07-17.png)

创建或修改schema后，要`Dendron: Reload Index`使其生效

## Template的使用
1. 在schema中指定

![](https://minio.kevin2li.top/image-bed/vanblog/img/14f8255cfc8f26d85a7424334d4b00e1.2022-09-15-23-48-45.png)

在创建“工具.笔记软件.xx”时会自动应用模板

2. 手动应用模板
在当前note下，执行`Dendron: Apply Template`，模板必须放在template下

