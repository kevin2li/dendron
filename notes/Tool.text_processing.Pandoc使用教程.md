---
id: wc045m3k1xs9k2cprt8ubpm
title: Pandoc使用教程
desc: ""
updated: 1682652980876
created: 1682507066339
---

## 简介
Pandoc 是一个强大的文档转换工具，可以将各种不同格式的文档互相转换，如将 Markdown 转换成 HTML、PDF、Word、LaTeX 等格式，同时支持各种不同的标记语言。
> If you need to convert files from one markup format into another, pandoc is your swiss-army knife. (来自官网介绍)

官网：https://pandoc.org/  
文档: https://pandoc.org/MANUAL.html

## 使用场景举例
### 文档格式转换
#### 将 Markdown 转换成 HTML

使用以下命令可以将一个 Markdown 文件转换成 HTML 格式：

```bash 
pandoc input.md -o output.html
```

其中 `input.md` 是要转换的 Markdown 文件，`output.html` 是生成的 HTML 文件。你可以根据需要修改文件名和路径。

#### 将 Markdown 转换成 PDF

使用以下命令可以将一个 Markdown 文件转换成 PDF 格式：

```bash 
pandoc input.md -o output.pdf
```

注意，这需要先安装 LaTeX 环境。如果你的系统中没有安装 LaTeX，可以参考官方文档进行安装：https://www.latex-project.org/get/。

#### 将 Markdown 转换成 Word

使用以下命令可以将一个 Markdown 文件转换成 Word 格式：

```bash 
pandoc input.md -o output.docx
```

注意，这需要先安装 LibreOffice 或 Microsoft Word。如果你使用的是 Windows 系统，需要将 Word 添加到系统的环境变量中。

#### 将 LaTeX 转换成 PDF

使用以下命令可以将一个 LaTeX 文件转换成 PDF 格式：

```bash 
pandoc input.tex -o output.pdf
```

#### 将 HTML 转换成 Markdown

使用以下命令可以将一个 HTML 文件转换成 Markdown 格式：

``` bash 
pandoc -s input.html -t markdown -o output.md
```

其中 `-s` 选项表示输入文件是一个 standalone HTML 文件， `-t` 选项表示输出文件的格式是 Markdown， `-o` 选项表示输出文件的名称。


### 文档格式调整
#### 转换标题层级
根据[markdownlint-rules#25](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md025---multiple-top-level-headings-in-the-same-document)，一个 Markdown 文件中，一级标题 `# Heading 1` 应该用作文章标题，有且只有一个，因此正文中最高的标题层级只能是二级标题 `## Heading 2`。但是这不是强制的，有时候没有这样做，有些场合下就需要进行相应转换。

``` bash 
# -1表示升1级，1表示降1级
pandoc input.md --shift-heading-level-by=-1 -o output.md
```

#### 转换参考文献
与 LaTeX 相比，在 Markdown 中 引用文献 简单得多。假设你的文章存储在一个 Markdown 文件 `input.md` 中，参考文献数据存储在一个 BibTeX 文件 `bib.bib` 中，那么就可以在 `input.md` 中通过 `[@citekey]` 的方式来引用文献，其中的 citekey 是 BibTeX 文件中对应的 Citation Key.

``` bash 
pandoc --citeproc --bibliography bib.bib input.md -o output.docx
```

### 媒体资源提取
#### 提取媒体文件
``` bash 
# 将包含图片的 Word 文件转换为 Markdown
pandoc test.docx --extract-media=. -o test.md

# 新建一个文件夹 media，将图床中的远程图片下载到本地并保存在该文件夹中，然后再输出为一个新的 Markdown 文件
pandoc --wrap=preserve input.md --extract-media=media -o output.md
```
### 参考
1. [少数派 | Pandoc 从入门到精通，你也可以学会这一个文本转换利器](https://sspai.com/post/77206)