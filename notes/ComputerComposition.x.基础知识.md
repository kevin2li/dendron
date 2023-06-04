---
id: 1lpv6k6h4z6y2yrfi1ls7og
title: 基础知识
desc: ''
updated: 1685630352606
created: 1685582970816
---

## 字节序
- **大端法**：高字节存储在低地址，网络传输中采用，又叫网络字节序
- **小端法**：高字节存储在高地址，现代PC基本采用，又叫主机字节序

以`0x01234567`为例：

![](https://minio.kevin2li.top/image-bed/blog/20230601093023.png)

当格式化的数据（比如32 bit整型数和16 bit短整型数）在两台使用不同字节序的主机之间直接传递时，接收端必然错误地解释之。

**解决问题的方法是**：发送端总是把要发送的数据转化成大端字节序数据后再发送，而接收端知道对方传送过来的数据总是采用大端字节序，所以接收端可以根据自身采用的字节序决定是否对接收到的数据进行转换（小端机转换，大端机不转换）。

需要指出的是，即使是同一台机器上的两个进程（比如一个由C语言编写，另一个由JAVA编写）通信，也要考虑字节序的问题（JAVA虚拟机采用大端字节序）。


## 编译过程
>csapp,p41

![](https://minio.kevin2li.top/image-bed/blog/20230601111232.png)

## 计算机组成
>csapp, p44

![](https://minio.kevin2li.top/image-bed/blog/20230601111356.png)

## 内存层次
>csapp, p50

![](https://minio.kevin2li.top/image-bed/blog/20230601111539.png)

>dive into system, p478
![](https://minio.kevin2li.top/image-bed/blog/20230601223856.png)

## 进程上下文切换
>csapp, p53

![](https://minio.kevin2li.top/image-bed/blog/20230601111934.png)

进程虚拟地址空间

![](https://minio.kevin2li.top/image-bed/blog/20230601112109.png)

## 数据表示

- 浮点数
>csapp, p149
![](https://minio.kevin2li.top/image-bed/blog/20230601112530.png)