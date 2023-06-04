---
id: v7zr15tix9020twco2r0460
title: CPU原理
desc: ''
updated: 1685760174144
created: 1685755357776
---


## 冯 • 诺依曼结构

![](https://minio.kevin2li.top/image-bed/blog/20230601221654.png)

### 运算器
功能：执行算术逻辑运算
组成：
- ALU: 用于执行各种算术和逻辑运算，包括加、减、乘、除、与、或、非、移位等。
- 数据寄存器： 用于存储运算器中的操作数和运算结果。
- 状态寄存器：用于存储运算器的运算状态，例如运算结果是否为零、是否溢出等。

### 控制器
功能：从内存中加载程序指令并提供给运算器所需的操作数和操作码，驱动程序指令的执行。
组成：
- 指令寄存器(IR): 存储从存储器加载的当前正在执行的指令
- 程序计数器(PC): 保存下一条要执行的指令的存储器地址
- 指令译码器: 用于将指令解码成控制信号，以便控制器可以控制其他组件执行指令
- 时序逻辑：用于根据指令译码器解码出的指令信息，生成控制信号，控制其他组件执行指令
- 中断控制器：用于处理计算机中的中断请求，以便及时响应外部设备的请求并完成相应的处理任务

### 存储器
功能：用于存储程序和数据，程序和数据都以二进制形式存储，并且存储器中的地址是连续的。程序和数据都可以通过地址来访问和操作。
组成：
- 主存储器（Main Memory）

通常是指随机存储器（Random Access Memory，RAM），它具有随机访问的特性，可以在短时间内存取或写入任意存储单元中的数据。

- 辅助存储器（Secondary Storage）

通常是指硬盘、光盘、U盘等外部存储设备，它们通常具有较大的存储容量和较慢的读写速度，但可以永久保存数据和程序。

### 输入设备

功能：允许用户或程序从外部输入数据，常见的输入设备有键盘、鼠标、摄像头、麦克风等

### 输出设备

功能：允许将程序的输出结果展示到外部设备中，常见的输出设备有显示器、扬声器等


其中，运算器和控制器合称为CPU。



## 工作流程
1. 取指令  

控制器的PC寄存器存放了下一条指令的地址，将该地址放到地址总线上，控制总线上发出`read`信号，内存将该地址的数据放到数据总线上，结果保存到IR寄存器中，PC寄存器自动增加以指向下一条指令

![](https://minio.kevin2li.top/image-bed/blog/20230603094903.png)

1. 分析指令  

根据指令集的定义区分操作码和操作数，并去指定位置(立即数、寄存器、内存)取操作数，输入到运算器中

![](https://minio.kevin2li.top/image-bed/blog/20230603095222.png)

3. 执行指令  

运算器执行相应的运算

![](https://minio.kevin2li.top/image-bed/blog/20230603095522.png)

4. 存储结果  

将运算结果保存到指定位置，如这里是保存到内存中

![](https://minio.kevin2li.top/image-bed/blog/20230603095542.png)

## 电路实现

思路：先设计简单的1个bit的电路，可以列真值表设计出逻辑电路结构，(可以的话将其优化一下)，然后将其当作黑箱封装，作为基本块一步步设计更复杂的电路


### 运算电路
以加法器为例：

真值表：

![](https://minio.kevin2li.top/image-bed/blog/20230603100128.png)

``` bash 
SUM: (NOT(A) AND B) OR (A AND NOT(B)) # 1 when exactly one of A or B is 1
CARRY OUT: A AND B # 1 when both A and B are 1
```

一位加法器：

![](https://minio.kevin2li.top/image-bed/blog/20230603100048.png)

四位加法器：

![](https://minio.kevin2li.top/image-bed/blog/20230603100613.png)

### 控制电路

- **复用器**：从多个输入中选择一个作为输出

1bit的2路复用器：

![](https://minio.kevin2li.top/image-bed/blog/20230603100957.png)

1bit的4路复用器：

![](https://minio.kevin2li.top/image-bed/blog/20230603101101.png)

- **分用器**：从多个输出中选择一个来接收输入

![](https://minio.kevin2li.top/image-bed/blog/20230603101419.png)

- **解码器**：输入N-bit的值，将结果传输到$2^N$个输出之一

![](https://minio.kevin2li.top/image-bed/blog/20230603101258.png)

### 存储电路

- **锁存器**

RS锁存器：

![](https://minio.kevin2li.top/image-bed/blog/20230603101722.png)

门控D锁存器：

![](https://minio.kevin2li.top/image-bed/blog/20230603101802.png)

寄存器可由多个门控D锁存器实现。

![](https://minio.kevin2li.top/image-bed/blog/20230603101838.png)


## 设计

Register File:

![](https://minio.kevin2li.top/image-bed/blog/20230603102750.png)

CPU: 

![](https://minio.kevin2li.top/image-bed/blog/20230603102707.png)

时钟信号：

![](https://minio.kevin2li.top/image-bed/blog/20230603103012.png)

时钟边缘触发电路状态变化，驱动指令执行。
- 上升沿：输入稳定，可以进行下一步操作
- 下降沿：输出稳定，可以读取结果

![](https://minio.kevin2li.top/image-bed/blog/Snipaste_2023-06-03_10-33-05.png)

时钟周期的长度要保证电路传播耗时最长的阶段能够完成，一般是执行指令阶段。

## 优化

### 流水线

- 没有流水线：

![](https://minio.kevin2li.top/image-bed/blog/20230603103721.png)

每条指令需要的时钟周期数CPI = 4

- 使用流水线：

![](https://minio.kevin2li.top/image-bed/blog/20230603103856.png)

每条指令需要的时钟周期数CPI = 1


**流水线的不足**：
- 数据方面：
  - 指令需要的时钟周期数不一致
  
  ![](https://minio.kevin2li.top/image-bed/blog/20230603104117.png)
  
  - 结果不一致
   
   ![](https://minio.kevin2li.top/image-bed/blog/20230603104157.png)

- 控制方面

分支跳转

![](https://minio.kevin2li.top/image-bed/blog/Snipaste_2023-06-03_10-42-36.png)