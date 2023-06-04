---
id: lptxrb2f6pp294lk0ehh9d7
title: x86_64汇编
desc: ''
updated: 1685629951072
created: 1685619996534
---

## 寄存器
在Intel CPU中，通常有以下类型的寄存器：

- **通用寄存器**：通用寄存器是最常用的寄存器类型，它们用于存储整数数据。在64位系统中，有16个通用寄存器，每个寄存器大小为64位。这些寄存器的名称是RAX、RBX、RCX、RDX、RSI、RDI、RBP、RSP、R8-R15。

| 寄存器名称 | 描述 |
| --- | --- |
| RAX | 累加器寄存器（Accumulator Register），用于存储算术和逻辑运算的操作数和结果。在函数调用中，它通常用于存储函数的返回值。 |
| RBX | 基址寄存器（Base Register），用于存储数据的基地址。在一些内存寻址方式中，它通常用于存储变量的地址。 |
| RCX | 计数寄存器（Counter Register），用于在循环中计数。在函数调用中，它通常用于存储函数的参数。 |
| RDX | 数据寄存器（Data Register），用于存储算术和逻辑运算的操作数和结果。在函数调用中，它通常用于存储函数的参数。 |
| RSI | 源索引寄存器（Source Index Register），用于字符串操作中的源地址。 |
| RDI | 目的索引寄存器（Destination Index Register），用于字符串操作中的目的地址。 |
| RBP | 基址指针寄存器（Base/Frame Pointer Register），用于存储当前栈帧的基址。在函数调用中，它通常用于存储上一个栈帧的基址。 |
| RSP | 栈指针寄存器（Stack Pointer Register），用于存储当前栈顶的地址。在函数调用和异常处理中，它通常用于存储函数的返回地址和异常处理的返回地址。 |
| R8-R15 | 扩展寄存器（Extended Register），这些寄存器是在64位系统中新增的。它们用于存储算术和逻辑运算的操作数和结果，以及函数调用的参数和返回值。 | 

这些通用寄存器在程序设计中非常常用，它们可以用于存储各种类型的数据，包括整数、指针、地址等等。同时，它们也在汇编语言和计算机体系结构中扮演着重要的角色，对于理解程序的运行机制和进行编程优化都有着重要的意义。

- **段寄存器**：段寄存器用于存储内存段的地址和访问权限。在Intel CPU中，有4个段寄存器，分别是CS（代码段）、DS（数据段）、SS（堆栈段）和ES（附加数据段）。

- **控制寄存器**：控制寄存器用于控制CPU的工作模式和运行状态。在Intel CPU中，有多个控制寄存器，包括CR0、CR2、CR3、CR4等。

- **标志寄存器**：标志寄存器用于存储CPU的运行状态和结果。在Intel CPU中，标志寄存器的名称是RFLAGS。它包含了多个标志位，例如进位标志、零标志、符号标志、溢出标志等等。

- **浮点寄存器**：浮点寄存器用于存储浮点数和向量数据。在Intel CPU中，有8个浮点寄存器，每个寄存器可以存储64位或者128位的数据。这些寄存器的名称是XMM0-XMM7。

- **SIMD寄存器**：SIMD寄存器用于存储向量数据和执行SIMD指令。在Intel CPU中，有16个SIMD寄存器，每个寄存器可以存储128位的数据。这些寄存器的名称是XMM0-XMM15。

- **Debug寄存器**：Debug寄存器用于调试程序和CPU。在Intel CPU中，有多个Debug寄存器，包括DR0、DR1、DR2、DR3、DR6、DR7等。

- **指令指针寄存器**： 指令指针寄存器（Instruction Pointer Register），也称为程序计数器（Program Counter, PC）。`%rip`寄存器存储了CPU当前正在执行的指令的地址. 它不能被直接修改。它的值只能通过CPU执行指令时自动更新。因此，在程序中，%rip寄存器通常用于间接寻址，例如通过相对地址或者基址加偏移量来访问内存中的数据。

这些寄存器在CPU的运行过程中发挥着不同的作用，例如通用寄存器用于存储运算数据、段寄存器用于管理内存访问、标志寄存器用于存储运算结果状态等等。它们在计算机体系结构中扮演着非常重要的角色，对于理解计算机硬件和编程语言都有着重要的意义。

名称表示：

![](https://minio.kevin2li.top/image-bed/blog/20230601195711.png)

## 指令表示
操作码(opcode)+操作数(operand)

![](https://minio.kevin2li.top/image-bed/blog/20230601223156.png)

操作数的形式：
- 常量：例如`$0x2`
- 寄存器：例如`%eax`
- 内存: 例如`-0x4(%rbp)`

![](https://minio.kevin2li.top/image-bed/blog/20230601201305.png)

常用指令：

![](https://minio.kevin2li.top/image-bed/blog/20230601221513.png)

## 指令执行过程

取指令->分析指令->执行指令->存储结果

![](https://minio.kevin2li.top/image-bed/blog/20230601222201.png)

## 程序内存空间

![](https://minio.kevin2li.top/image-bed/blog/20230601201818.png)


## 用户态和内核态
> 操作系统概念,p22

![](https://minio.kevin2li.top/image-bed/blog/20230601221309.png)