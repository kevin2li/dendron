---
id: fxx5840yugr5v98flyg1phm
title: matplotlib
desc: ''
updated: 1682652980816
created: 1682589693513
---

## 简介

Matplotlib是Python中最常用的可视化工具之一，可以非常方便地创建海量类型地2D图表和一些基本的3D图表，可根据数据集的特点选择不同的绘图方式。Matplotlib是一个开源的Python 2D绘图库，可以轻松地将数据图形化，并且提供多种格式的输出。

官网：https://matplotlib.org/  
用户手册：https://matplotlib.org/stable/users/index

## 教程

### 认识图表

![](https://minio.kevin2li.top/image-bed/vanblog/img/80f220d35de57a7d3b33ccf2a09fe6a1.2022-09-19-11-01-41.png)


### 基本配置

``` python 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 修复减号显示异常

plt.style.available # 查看所有style列表
plt.style.use('seaborn-whitegrid') # 设置风格
```

### 创建图表

``` python  
# 创建一行一列的简单图表
fig, ax = plt.subplots()

# or
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/807ecae0639ef4601048603e26f22518.image.png)

``` python  
# 创建2行2列的图表,并指定图片大小和dpi
fig, axs = plt.subplots(2, 2, layout="constrained", figsize=(12,6), dpi=1000)
axs[0, 0].set_title("Sub1")
axs[0, 1].set_title("Sub2")
axs[1, 0].set_title("Sub3")
axs[1, 1].set_title("Sub4")
fig.suptitle("Big Title")
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2d19a10cd365fc00bbfb5c41521e96cd.image.png)

### 标题设置

-   `ax.set_title()`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/7a4f09910ecceeb3cae6e56be201033a.image.png)

其中，`fontdict`默认参数为：

``` python 
{
    'fontsize': rcParams['axes.titlesize'],
    'fontweight': rcParams['axes.titleweight'],
    'color': rcParams['axes.titlecolor'],
    'verticalalignment': 'baseline',
    'horizontalalignment': loc
}
```

举例：

``` python 
fig, ax = plt.subplots()
ax.set_title("Demo Figure", loc='center', y=1, pad=10, fontdict={'color':'red', 'fontsize': 20})
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/74193be4f29e7dcceed23ec4a58e06c5.image.png)
- `fig.suptitle()`

设置整张图片的标题

### 图例设置

-   `ax.legend()`

常用参数：
- `labels`: 图例名称
- `loc`: 图例位置
- `bbox_to_anchor`: 图例位置

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/d198bbeb5453ed2616833669d3849159.image.png)

-   `nrow`：图例占多少行
-   `ncol`: 图例占多少列
-   `frameon`: 是否显示图例边框

举例：

``` python 
x = np.linspace(0, 2 * np.pi, 200)
y1 = np.sin(x)
y2 = y1 + 1
fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)
ax.legend(labels=["y1", "y2"], loc="upper right", ncol=2)
ax.set_title("Legend Demo")
plt.show()
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/5a00f79b722b770241e374367d18504d.image.png)

### 坐标轴设置

#### 标签设置

-   `ax.set_xlabel`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0913434fde994fc7d26cb63d6f85056e.image.png)

-   `ax.set_ylabel`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/164ba51104b512871ec9f263fc750dc3.image.png)

示例：

``` python 
np.random.seed(23)
y = np.random.randint(0,20,(10,))
fig, ax = plt.subplots()
ax.plot(y)
ax.set_xlabel("x", loc='center', labelpad=2, fontdict={"color":"blue", 'fontsize': 20})
ax.set_ylabel("y", loc='center',labelpad=5, fontdict={"color":"red", 'fontsize': 20})
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/8852def4bdfd2693f90f10ca1bb2d963.image.png)

#### 范围设置

-   `ax.set_xlim`
-   `ax.set_ylim`
-   `ax.axis`

#### 刻度设置

-   `ax.set_xticks`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/cac691874d1bf38147f8c9ee8e5f839f.image.png)

-   `ax.set_yticks`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/ac91d44ce692b540320229e5158bc033.image.png)

-   `ax.tick_params`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/692ffde6cb53f83777b6c1111334378f.image.png)

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/b742ba442ea415f8be41682b6306e4ea.image.png)

示例：

``` python 
fig, ax = plt.subplots()
data1, data2 = np.random.randint(0, 10, (10, 2)).T
ax.plot(data1, label="1")
ax.plot(data2, label="2")
ax.set( title="Demo", xticks=range(10), yticks=range(10),
)
ax.legend(bbox_to_anchor=(1., 0.67))
ax.grid(True)
ax.tick_params(axis='x', direction='in', labelrotation=15, length=6, width=2, colors='black', grid_color='b', grid_alpha=0.2)
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/5405eba61435a16cb4e93c37547de2c8.image.png)

#### 尺度设置

-   `ax.set_yscale`

示例：

``` python 
np.random.seed(19680801)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
fig, axs = plt.subplots(2,2, layout="constrained")

# linear
axs[0,0].plot(x, y)
axs[0,0].set_yscale('linear')
axs[0,0].set_title('linear')
axs[0,0].grid(True)

# log
axs[0,1].plot(x, y)
axs[0,1].set_yscale('log')
axs[0,1].set_title('log')
axs[0,1].grid(True)

# symmetric log
axs[1,0].plot(x, y - y.mean())
axs[1,0].set_yscale('symlog', linthresh=0.01)
axs[1,0].set_title('symlog')
axs[1,0].grid(True)

# logit
axs[1,1].plot(x, y)
axs[1,1].set_yscale('logit')
axs[1,1].set_title('logit')
axs[1,1].grid(True)
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e391c1f8e32550606f03f2000c0efe18.image.png)

#### 多坐标轴设置

-   `ax.twinx`
-   `ax.twiny`

举例：

``` python 
fig, ax = plt.subplots()
data1 = np.random.randn(30)
data2 = 10*np.random.randn(30)
l1, = ax.plot(data1, "r-")

ax2 = ax.twinx() 
l2, = ax2.plot(data2, "g-")
ax2.legend([l1, l2], ["y1(left)", "y2(right)"])
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/18f6d033c9930f4f66a82590b44b83ce.image.png)

-   `ax.secondary_xaxis`
-   `ax.secondary_yaxis`

### 网格设置

-   `ax.grid`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/da69ea4f6a0fedd033cd2c354a404198.image.png)

示例：

``` python 
np.random.seed(23)
y = np.random.randint(0,20,(10,))
fig, ax = plt.subplots()
ax.plot(y)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_yticks(range(0,20,5))
ax.set_yticks(range(0,20,1),minor=True)
ax.grid(axis='y',which='major')
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e85fd0eab28454c4383feeefa38ac547.image.png)

-   `ax.tick_params`

设置网格线颜色、粗细、样式等\
详见："坐标轴设置\>刻度设置"一节

### 外边框设置(spine)

``` python 
# 隐藏上边框和右边框
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)

# 隐藏所有边框
for pos in ['top','right','bottom','left']:
    ax.spines[pos].set_visible(False)
```

### 样式设置

-   `color`: 颜色
-   `linewidth`或`lw`: 粗细
-   `linestyle`或`ls`: 风格

::: info 线条风格
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/99084bccbd941831966d7e8406c608b5.image.png)

参考：https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
:::

-   `marker`: 标记形状

::: info 标记形状(部分)
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/615672e518ba2007c0c651bb2be1cfa4.image.png)

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/376deaedcff26d7f33b9dcdcc5087ef5.image.png)

参考：https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
:::

### 文本/注解设置

-   `ax.text`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/16d2efaa8f73bd5d7563545a6dd8e7d9.image.png)

举例：

``` python 
np.random.seed(23)
fig, ax = plt.subplots()
data = np.random.randint(0, 10, (7,))
ax.plot(data, "b-")
ax.text(4, 5.5, "I'm here!", fontdict={"color": "red"})
ax.text(1.8, 7, r'$\mu=115,\ \sigma=15$', fontdict={"color": "green"}) # 支持LaTex语法
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2afa4af9783bf5775127782d8d1081d0.image.png)

-   `ax.annotate`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/3acc2b6ee0c14c0469185d852cf2ec3d.image.png)

参考：https://matplotlib.org/stable/tutorials/text/annotations.html

举例：

``` python 
np.random.seed(23)
fig, ax = plt.subplots()
data = np.random.randint(0, 10, (7,))
ax.plot(data, "b-")
ax.annotate("I'm here!", [4,6], [5,5], arrowprops={"arrowstyle":"->","facecolor":'black'})
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/86cc4177032978a5bd6bc692c1343b14.image.png)

::: info{title="箭头样式"}
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0fb00d176992c3f8eacec2b2b19f1ad7.image.png)
:::

### 颜色设置

参考：https://matplotlib.org/stable/tutorials/colors/colormaps.html

``` python 
CB91_Blue   = '#2CBDFE'
CB91_Green  = '#47DBCD'
CB91_Pink   = '#F3A0F2'
CB91_Purple = '#9D2EC5'
CB91_Violet = '#661D98'
CB91_Amber  = '#F5B14C'
color_list = [CB91_Blue, CB91_Pink, CB91_Green, CB91_Amber, CB91_Purple, CB91_Violet]
# color_list=["#4E79A7","#A0CBE8","#F28E2B","#FFBE7D","#59A14F","#8CD17D","#B6992D","#F1CE63","#499894","#86BCB6","#E15759","#E19D9A"]

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
```

### 字体设置

``` python 
msyh = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")        # 微软雅黑
simfang = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/simfang.ttf")  # 仿宋
simsun = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/simsun.ttc")    # 宋体
simhei = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/simhei.ttf")    # 黑体
simkai = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/simkai.ttf")    # 楷体

# 在需要设置中文的地方设置fontproperties属性
ax.set_title("This is a Chinese Demo\n这是一个中文示例", fontproperties=msyh)
```

### 子图布局设置

-   `plt.GridSpec`

``` python 
fig = plt.figure(constrained_layout=True)

gs = plt.GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])

ax1.set_title("Sub1")
ax2.set_title("Sub2")
ax3.set_title("Sub3")
ax4.set_title("Sub4")
ax5.set_title("Sub5")

fig.suptitle("GridSpec")
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/2c30828f60a41e3128f7a605b37db610.image.png)

-   `plt.subplot_mosaic`

``` python 
x = [['A panel', 'A panel', 'B panel'],
     ['C panel', 'C panel', 'B panel']]
fig, axs = plt.subplot_mosaic(x, layout="constrained")
axs['A panel'].set_title("A panel")
axs['B panel'].set_title("B panel")
axs['C panel'].set_title("C panel")
fig.suptitle("Big Title")
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0c1eb3d92eea6cb881388b3073ff9fd2.image.png)

### 主题设置

所有样式预览：https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

``` python 
plt.style.available # 查看所有style列表
plt.style.use('seaborn-whitegrid') # 设置风格
```

### 图片保存

``` python 
# 输出为矢量图，不管放大或缩小，图形皆不会失真
plt.savefig("test.svg", format="svg")

# 输出为常规的png格式
plt.savefig("test.png", format="png")

# 输出为常规的jpg格式
plt.savefig("test.jpg", format="jpg")

# 图例超出图片外使用
fig.savefig("test.png", bbox_inches="tight")
```

## 经典图表绘制

### 条形图

``` python 
x = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
data = np.random.randint(30, 100, (7,))
colors=["#4E79A7","#A0CBE8","#F28E2B","#FFBE7D","#59A14F","#8CD17D","#B6992D","#F1CE63","#499894","#86BCB6","#E15759","#E19D9A"]
fig, ax = plt.subplots(layout="constrained")
handle = ax.bar(x, data, color=colors)
ax.bar_label(handle, data, padding=2)
ax.set_title("Test Bar Graph")
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/60c536fba2d0ce56eaaaa63f29d631cf.image.png)

### 折线图

``` python 
t = np.arange(0.0, 2.0, 0.05)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s, color="blue", ls=(0,(5,10)), lw=1, marker='^')
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')
ax.grid()
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e8a431e4438dd12c95c1bb778c356bd7.image.png)

### 饼图

``` python 
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/dfa8b54a28c3a28600ad59656627fcde.image.png)

### 散点图

-   `ax.scatter`

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/023f38e412d15a48c6b2bde3e732782b.image.png)

举例：

``` python 
np.random.seed(23)
x = np.random.rand(20)
y = np.random.rand(20)
z = np.random.randint(50, 400, (20,))
fig, ax = plt.subplots()
ax.scatter(x,y,s=z,c=z, marker='o')
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/413cffc198723310a1a95a1c5c0e2a34.image.png)

## 参考

![](https://minio.kevin2li.top/image-bed/vanblog/img/128b5802c567f542172fa611ead053b1.2022-09-19-17-32-24.png)

![](https://minio.kevin2li.top/image-bed/vanblog/img/f44e4d50574036d977c0bcd8f0b65824.2022-09-19-17-32-46.png)
