# 简介

LATEX（发音为“LAY-tek”或“LAH-tek”）是一种用于排版专业外观文档的工具。然而，LaTeX的操作方式与您可能使用过的许多其他文档制作应用程序（如Microsoft Word或LibreOffice Writer）非常不同：这些“所见即所得”的工具为用户提供了一个交互式页面，用户可以在其中输入和编辑文本并应用各种形式的样式。LaTeX的工作方式非常不同：相反，您的文档是一个纯文本文件，其中夹杂着LaTeX命令，用于表达所需的（排版）结果。要生成可见的、排版好的文档，您的LaTeX文件将由一种称为TeX引擎的软件处理，该软件使用嵌入在您的文本文件中的命令来指导和控制排版过程，将LaTeX命令和文档文本转换为专业排版PDF文件。这意味着您只需要关注文档内容，并通过计算机、LaTeX命令和TeX引擎来处理视觉外观（格式化）。它非常适用于生成高印刷质量的科技和数学类文档，对于生成复杂表格和数学公式，这一点表现得尤为突出。

<!-- more -->

# 语法
## 文章结构
一个最简单的示例如下：
```latex
\documentclass{article}
\begin{document}
First document. This is a simple example, with no 
extra parameters or packages included.
\end{document}
```
它会得到如下的输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/89dcddf72e66479e264acbc7a60e70e0.image.png)

## 标题

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/fdbd3fb48a39f13849201213e92b5507.image.png)

通常，`\section`是大多数文档中的顶级文档命令。然而，在报告或书籍以及类似的长文档中，这将是`\chapter` 或 `\part`。

## 样式
- 粗体：`\textbf{your_text}`
- 斜体：`\textit{your_text}`
- 下划线：`\underline{your_text}`

示例：
```latex
Some of the \textbf{greatest}
discoveries in \underline{science} 
were made by \textbf{\textit{accident}}.
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2ff45ba8e89f09e7b5516e9258c2b102.image.png)

## 公式
### 行内公式
示例：
```latex
This formula $f(x) = x^2$ is an example.
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/34e0ddeb500498f5ea31d3c3157d0a22.image.png)

### 独立公式
- 简单公式：`\equation`
```latex
# 加*表示无编号，不加表示有编号
\begin{equation*}
  1 + 2 = 3 
\end{equation*}
```
输出：
$$
\begin{equation*}
  1 + 2 = 3 
\end{equation*}
$$

- 公式对齐: `\align`
```latex
\begin{align*}
  1 + 2 &= 3\\
  1 &= 3 - 2
\end{align*}
```
输出：
$$
\begin{align*}
  1 + 2 &= 3\\
  1 &= 3 - 2
\end{align*}
$$

### 分段函数
```latex
\begin{equation*}
    y=
    \begin{cases}
    x, & x>0,\\
    -x, & x \le 0
    \end{cases}
\end{equation*}
```
输出：
$$
    y=
    \begin{cases}
    x, & x>0,\\
    -x, & x \le 0
    \end{cases}
$$
### 上下标、分数、根
```latex
x^2,x_1,\sqrt{x},\sqrt[3]{x},\frac{1}{\sqrt{a+b}}
```
输出：
$$
x^2, x_1, \sqrt{x}, \sqrt[3]{x}, \frac{1}{\sqrt{a+b}}
$$


**补充**：下标标注在字母正下方

``` latex
% 格式：
expr1\limits_{expr2}^{expr3}
```
举例：
- `$ \sum_{i=0}^5x_i $`: $ \sum_{i=0}^5x_i $
- `$ \sum\limits_{i=0}^5x_i $`: $ \sum\limits_{i=0}^5x_i $

如果`expr1`不是数学符号(会报错)，可以通过`\mathop`转换为数学符号
- `$max=\limits_{i\in U}x_i$`: $max\limits_{i\in U}x_i$
- `$\mathop{max}\limits_{i\in U}x_i$`: $\mathop{max}\limits_{i\in U}x_i$

### 大算子

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ffdef23305ff06e6026c5d7fa810ea6b.image.png)

### 矩阵
方括号矩阵：
```latex
\left[
\begin{array}
{ccc}
1&2&3\\
4&5&6
\end{array}
\right]
```
输出：
$$
\left[
\begin{array}
{ccc}
1&2&3\\
4&5&6
\end{array}
\right]
$$

小括号矩阵：
```latex
\left(
\begin{array}
{ccc}
1&2&3\\
4&5&6\\
7&8&9\\
0&0&0
\end{array}
\right)
```
输出：
$$
\left(
\begin{array}
{ccc}
1&2&3\\
4&5&6\\
7&8&9\\
0 & 0& 0
\end{array}
\right)
$$

### 行列式
```latex
\left|
\begin{array}
{ccc}
1&2&3\\
4&5&6\\
7&8&9
\end{array}
\right|
```

输出：
$$
\left|
\begin{array}
{ccc}
1&2&3\\
4&5&6\\
7&8&9
\end{array}
\right|
$$

:::info 常用符号
希腊字母：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/58d014e1eb07e8d4bc9b0922d90e1dfb.image.png)

集合和逻辑：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0034aaadd3c741e30c3656dab7f5c6e0.image.png)

装饰：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/b928c3641300ca83d8acde121062dbd5.image.png)

花体：
``` latex 
\mathcal{L}
```
如：$\mathcal{L}$

> 参考  
> 1. [Cheatsheet for LaTeX Math Commands](https://tilburgsciencehub.com/building-blocks/collaborate-and-share-your-work/write-your-paper/amsmath-latex-cheatsheet/)
> 2. [LATEX Math for Undergrads](http://tug.ctan.org/info/undergradmath/undergradmath.pdf)
:::


## 列表
### 无序列表
示例：
```latex
\documentclass{article}
\begin{document}
\begin{itemize}
  \item The individual entries are indicated with a black dot, a so-called bullet.
  \item The text in the entries may be of any length.
\end{itemize}
\end{document}
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a1c9ac434d153ab6dd43c0db295a87ec.image.png)

### 有序列表

示例：
```latex
\documentclass{article}
\begin{document}
\begin{enumerate}
  \item This is the first entry in our list.
  \item The list numbers increase with each entry we add.
\end{enumerate}
\end{document}
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/16161345f114d36d5bf1bce9a59e6224.image.png)
## 表格
示例：
```latex
Table \ref{table:data} shows how to add a table caption and reference a table.

\begin{table}[h!]
\centering
\begin{tabular}{||c c c c||} 
 \hline
 Col1 & Col2 & Col2 & Col3 \\ [0.5ex] 
 \hline\hline
 1 & 6 & 87837 & 787 \\ 
 2 & 7 & 78 & 5415 \\
 3 & 545 & 778 & 7507 \\
 4 & 545 & 18744 & 7560 \\
 5 & 88 & 788 & 6344 \\ [1ex] 
 \hline
\end{tabular}
\caption{Table to test captions and labels.}
\label{table:data}
\end{table}
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e46d6e095cf7e860f4deec0fed6e3cc2.image.png)

表格自动生成器：https://www.tablesgenerator.com/

## 图片

核心参数：

```latex
\documentclass{article}
\usepackage{graphicx}    % 导入图片包
\graphicspath{{images/}} % 设置图片基路径

\begin{document}

% 图片样式设置(长宽、缩放、旋转)
\includegraphics[width=5cm, height=4cm，scale=1.2, angle=45]{overleaf-logo} % 插入图片，参数为图片名，不带后缀

\end{document}

```
### 单张图片
示例：
```latex
\documentclass{article}
\usepackage{graphicx}
\graphicspath{{images/}}
 
\begin{document}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.75\textwidth]{mesh} 
    \caption{A nice plot.}
    \label{fig:mesh1}
\end{figure}
 
As you can see in figure \ref{fig:mesh1}, the function grows near the origin. This example is on page \pageref{fig:mesh1}.

\end{document}
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ae8d4f89449768e47e580a64ad1cf55c.image.png)

### 多张图片
示例：
```latex
% 在preamble导入subcaption包
\usepackage{subcaption}

Praesent in sapien. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Duis fringilla tristique neque...

\begin{figure}[h]

\begin{subfigure}{0.5\textwidth}
\includegraphics[width=0.9\linewidth, height=6cm]{overleaf-logo} 
\caption{Caption1}
\label{fig:subim1}
\end{subfigure}

\begin{subfigure}{0.5\textwidth}
\includegraphics[width=0.9\linewidth, height=6cm]{mesh}
\caption{Caption 2}
\label{fig:subim2}
\end{subfigure}

\caption{Caption for this figure with two images}
\label{fig:image2}
\end{figure}

Praesent blandit blandit mauris. Praesent lectus tellus, aliquet aliquam, luctus a, egestas a, turpis. Mauris lacinia lorem sit amet ipsum. Nunc quis urna dictum turpis accumsan semper.
```
输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/dc3bd0d8147b7f9313781dc2299e3010.image.png)

### Figure环境位置参数
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/9e85ce4a21b939140ac04d14f61c0b4a.image.png)

## 补充
### Latex长度单位
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/165f2048c03275c33ac9f5b6a7d864ae.image.png)

# 参考
[1] [Overleaf-Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)