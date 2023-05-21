# 介绍
内存分为三块：静态区域、堆区域和栈区域。

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/43850d78b59887f24d94d9db234df2bb.image.png)

其中堆区域和栈区域是相向而行的，这样可以最大化利用内存空间，而静态区域大小固定，不会随者程序运行而变化。

<!-- more -->

## 静态区域(Static Storage)
不在函数内部或类内部声明的变量，或者使用`static`关键字声明的变量，和整个程序具有相同的生命周期。

注意：
1. `static`声明的变量只会在第一次执行时初始化一次。  
2. 类中的`static`变量属于整个类，而不是某个类的对象

## 栈区域(Automatic Storage)

当函数被调用时，函数参数和函数内局部变量会入栈，当函数退出时，这些变量又会出栈。

## 堆区域(Dynamic Storage)
由具体的指令手动申请分配的区域，允许在运行时决定占用空间大小。

# 参考
https://www.cs.odu.edu/~zeil/cs361/latest/Public/storageModels/index.html