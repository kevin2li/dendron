# 简介

Python中可以处理pdf的库有好几个，如PyMuPDF、PDFrw、PikePDF、PyPDF2等，本文主要介绍如PyMuPDF的用法。该库相比于同类其他库，支持格式丰富，包括PDF、XPS、EPUB、MOBI FB2、CBZ、SVG、Image等多种格式，且各方面(拷贝页面、提取文字等)处理速度具有明显优势。

![](https://minio.kevin2li.top/image-bed/blog/20230604095112.png)

GitHub: https://github.com/pymupdf/PyMuPDF  
PyPi: https://pypi.org/project/PyMuPDF/   
文档：https://pymupdf.readthedocs.io/en/latest/index.html

<!-- more -->

# 教程
## 安装

```python
python -m pip install --upgrade pip
python -m pip install --upgrade pymupdf
```

## 开始使用
### 读取文件
- 读取普通文件
```python
input_path = "/home/kevin2li/计算机操作系统(第4版)_汤子丹.pdf"
doc: fitz.Document = fitz.open(input_path)
```

- 读取加密文件

```pythpn
doc.isEncrypted # True
doc: fitz.Document = fitz.open(input_path)
doc.authenticate("password")
doc.isEncrypted # False
```

:::info 如何加密PDF
可以使用WPS:

![](https://minio.kevin2li.top/image-bed/blog/20230604094848.png)

![](https://minio.kevin2li.top/image-bed/blog/20230604094908.png)

:::
- 取消密码

```pythpn
doc: fitz.Document = fitz.open(input_path)
doc.authenticate("password")
n = doc.page_count
doc.select(range(n))
doc.save("out.pdf")
```
这样新保存的`out.pdf`就没有密码了。

- 查看总页数

```python
doc.page_count # 418
```
- 查看元信息

```python
doc.metadata
```

- 查看目录

```python
doc.get_toc() # []
```

- 读取指定页面
```python
page = doc.load_page(1) # loads page number 'pno' of the document (0-based)

# 当前页码
page.number
```
- 遍历页面

```python
for page in doc:
    # do something with 'page'

# ... or read backwards
for page in reversed(doc):
    # do something with 'page'

# ... or even use 'slicing'
for page in doc.pages(start, stop, step):
    # do something with 'page'
```

### 写入文件
```python
doc.save("out.pdf")
```

### 删除页面

```python
# 删除单页
doc.delete_page(3)

# 删除页面范围
doc.delete_pages(1, 3)
doc.delete_pages(from_page=1, to_page=3)
doc.delete_pages([1,3,5,9])
```
示例：
```python
input_path = "aaa.pdf"
doc: fitz.Document = fitz.open(input_path)
doc.delete_page(0)
doc.save("out3.pdf")
```
### 截取页面
```python
input_path = "aaa.pdf"
doc: fitz.Document = fitz.open(input_path)
doc.select(range(2, 10))
doc.save("out.pdf")
```
### 插入页面

```python
doc.insert_page(pno, text=None, fontsize=11, width=595, height=842, fontname='helv', fontfile=None, color=None)
```

```python
page = doc.new_page(to = -1,  # insertion point: end of document
                    width = 595,  # page dimension: A4 portrait
                    height = 842)
```

```python
doc.insert_pdf(docsrc, from_page=-1, to_page=-1, start_at=-1, rotate=-1, links=1, annots=1, show_progress=0, final=1, _gmap=None)
```

### 旋转页面
```python
# Open the PDF document
doc = fitz.open("document.pdf")

# Iterate over all the pages in the document
for page in doc:
    # Rotate the page by 90 degrees
    page.set_rotation(90)

# Save the changes to the PDF
doc.save("rotated_document.pdf")
```
### 调整页面顺序
```python
input_path = "out.pdf"

doc: fitz.Document = fitz.open(input_path)
# 把第s页-第t页(包含)移到第p页后面(从1起)
s, t, p = 2, 5, 7
seq = list(range(doc.page_count))
new_seq = seq[:s-1] + seq[t:p] + seq[s-1:t] + seq[p:]
doc.select(new_seq)
doc.save("out.pdf")
```

### 添加目录
书籍页码可以去网上书店查看复制，保存到txt文件中。

页码文件格式如下：


![](https://minio.kevin2li.top/image-bed/blog/20230604094627.png)

```python
import fitz
import re

input_path = "/home/kevin2li/计算机操作系统(第4版)_汤子丹.pdf"
toc_path = "/home/kevin2li/toc.txt"
offset = 9 # 书籍页码与实际页码的差值

doc: fitz.Document = fitz.open(input_path)
n = doc.page_count
# doc.select(range(2,n))

toc = []
with open(toc_path, "r") as f:
    for line in f:
        parts = line.split()
        pno = int(parts[-1]) + offset
        title = " ".join(map(lambda x: x.strip(), parts[:-1]))
        if re.match("第.章 .+", title) or "参考文献" in title:
            toc.append([1, title, pno])
        else:
            toc.append([2, title, pno])
doc.set_toc(toc)
doc.save("out.pdf")
```

### PDF转图片

```python
pix = page.get_pixmap()
pix.save(f"page-{page.number}.png")

```

### 合并文件

```python
import fitz


# Open the first PDF document
doc1 = fitz.open('document1.pdf')

# Open the second PDF document
doc2 = fitz.open('document2.pdf')

# Insert the second document into the first document
doc1.insert_pdf(doc2)

# Save the merged PDF
doc1.save('merged.pdf')
```
# 参考
1. [Medium-Handling PDF files in Python using PyMuPDF](https://gggauravgandhi.medium.com/handling-pdf-files-in-python-using-pymupdf-ba0b0b12ddc4#:~:text=To%20rotate%20pages%20in%20a%20PDF%20document%20using,get%20the%20rotation%20value%20of%20the%20current%20page.)
