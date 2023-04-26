---
id: wc045m3k1xs9k2cprt8ubpm
title: Pandoc使用教程
desc: ""
updated: 1682507399716
created: 1682507066339
---

Pandoc 是一个强大的文档转换工具，可以将各种不同格式的文档互相转换，如将 Markdown 转换成 HTML、PDF、Word、LaTeX 等格式，同时支持各种不同的标记语言。以下是一些常用的 Pandoc 用法介绍：

1. 将 Markdown 转换成 HTML：使用以下命令可以将一个 Markdown 文件转换成 HTML 格式：

```
pandoc input.md -o output.html
```

其中 `input.md` 是要转换的 Markdown 文件，`output.html` 是生成的 HTML 文件。你可以根据需要修改文件名和路径。

2. 将 Markdown 转换成 PDF：使用以下命令可以将一个 Markdown 文件转换成 PDF 格式：

```
pandoc input.md -o output.pdf
```

注意，这需要先安装 LaTeX 环境。如果你的系统中没有安装 LaTeX，可以参考官方文档进行安装：https://www.latex-project.org/get/。

3. 将 Markdown 转换成 Word：使用以下命令可以将一个 Markdown 文件转换成 Word 格式：

```
pandoc input.md -o output.docx
```

注意，这需要先安装 LibreOffice 或 Microsoft Word。如果你使用的是 Windows 系统，需要将 Word 添加到系统的环境变量中。

4. 将 LaTeX 转换成 PDF：使用以下命令可以将一个 LaTeX 文件转换成 PDF 格式：

```
pandoc input.tex -o output.pdf
```

5. 将 HTML 转换成 Markdown：使用以下命令可以将一个 HTML 文件转换成 Markdown 格式：

```
pandoc -s input.html -t markdown -o output.md
```

其中 `-s` 选项表示输入文件是一个 standalone HTML 文件， `-t` 选项表示输出文件的格式是 Markdown， `-o` 选项表示输出文件的名称。

这些只是 Pandoc 的一些常用用法，Pandoc 还有许多高级的功能和选项，可以参考官方文档了解更多详细信息：https://pandoc.org/MANUAL.html。
