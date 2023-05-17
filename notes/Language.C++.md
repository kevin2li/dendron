---
id: opbxfa5jie5tzo1s0glei45
title: C++
desc: ''
updated: 1683432262812
created: 1682484483225
---

# 作用域

- 复合语句(块语句)：A **compound statement** (also called a block, or block statement) is a group of zero or more statements that is treated by the compiler as if it were a single statement.

## 自定义命名空间  

定义命名空间(namespace):
``` c++
#include <iostream>

namespace foo // define a namespace named foo
{
    // This doSomething() belongs to namespace foo
    int doSomething(int x, int y)
    {
        return x + y;
    }
}

namespace goo // define a namespace named goo
{
    // This doSomething() belongs to namespace goo
    int doSomething(int x, int y)
    {
        return x - y;
    }
}

int main()
{
    std::cout << foo::doSomething(4, 3) << '\n'; // use the doSomething() that exists in namespace foo
    return 0;
}
```
注意：  
1. 使用`::`域解析操作符指定对象, 例如`foo::doSomething()`。
2. 如果`::`前不加prefix，如`::doSomething()`, 则默认使用全局命名空间，这对于在命名空间内部调用全局函数有用，与该命名空间内部的同名函数区分开。
3. 允许在多个地方定义同一个命名空间(不同block、不同file等)，表示属于该命名空间的一部分。也可以向已有的命名空间中继续添加自己的函数，但是不建议向`std`空间加(事实上也不允许)。
4. 命名空间允许嵌套定义，访问时类似`foo::goo::add`.
``` c++
#include <iostream>

namespace foo
{
    namespace goo // goo is a namespace inside the foo namespace
    {
        int add(int x, int y)
        {
            return x + y;
        }
    }
}

int main()
{
    std::cout << foo::goo::add(1, 2) << '\n';
    return 0;
}
```
5. 允许设备命名空间别名

``` c++
namespace active = foo::goo; // active now refers to foo::goo
std::cout << active::add(1, 2) << '\n'; // This is really foo::goo::add()
```

参考： [6.2 — User-defined namespaces and the scope resolution operator](https://www.learncpp.com/cpp-tutorial/user-defined-namespaces-and-the-scope-resolution-operator/)

## 局部变量

哪些是局部变量：
   - 函数参数
   - 块内定义的变量

注意：
- 局部变量具有块作用域
- 同一个作用域下的变量名必须唯一
- 局部变量具有自动存储周期(`automatic storage duration`)
- 局部变量创建没有联系(linkage)
>An identifier’s **linkage** determines whether other declarations of that name refer to the same object or not.
``` c++
int main()
{
    int x { 2 }; // local variable, no linkage

    {
        int x { 3 }; // this identifier x refers to a different object than the previous x
    }

    return 0;
}
```
- 变量遮蔽(`Variable shadowing`, `name hiding`)：当内层block定义的变量与外层block定义的变量同名时，内层定义的变量有效。
> 尽量避免出现这种情况，使用不同的标识符名称 #最佳实践

## 全局变量
哪些是全局变量：
   - 函数外定义的变量

> Consider using a “g” or “g_” prefix when naming non-const global variables, to help differentiate them from local variables and function parameters #最佳实践
``` c++
int g_x {}; // global variable g_x
```

注意：
- 全局变量具有文件作用域(`file scope, global scope, global namespace scope`三者同一个意思)
- 全局变量具有静态存储周期(`static duration`)
- 常量全局变量必须初始化，否则会报错

### 如何让全局变量跨文件访问
#### 1. 公共头文件

`constants.h`:
``` cpp 
#ifndef CONSTANTS_H
#define CONSTANTS_H

// define your own namespace to hold constants
namespace constants
{
    // constants have internal linkage by default
    constexpr double pi { 3.14159 };
    constexpr double avogadro { 6.0221413e23 };
    constexpr double myGravity { 9.2 }; // m/s^2 -- gravity is light on this planet
    // ... other related constants
}
#endif
```

`main.cpp`: 
``` cpp 
#include "constants.h" // include a copy of each constant in this file

#include <iostream>

int main()
{
    std::cout << "Enter a radius: ";
    int radius{};
    std::cin >> radius;

    std::cout << "The circumference is: " << 2.0 * radius * constants::pi << '\n';

    return 0;
}
```
::: warning  优缺点
优点:
1. 每个引用头文件的源代码文件都有全局常量的副本, 利于编译器优化

缺点:
1. 更改一个常量的值, 所有引用头文件的源代码文件都要重新编译,大项目里会导致冗长的编译时间
2. 如果常量很大并且无法优化的话, 会占用很大内存
:::

#### 2. 外部链接变量

`contants.cpp`:
``` cpp 
#include "constants.h"

namespace constants
{
    // actual global variables
    extern const double pi { 3.14159 };
    extern const double avogadro { 6.0221413e23 };
    extern const double myGravity { 9.2 }; // m/s^2 -- gravity is light on this planet
}
```

`contants.h`:
``` cpp 
#ifndef CONSTANTS_H
#define CONSTANTS_H

namespace constants
{
    // since the actual variables are inside a namespace, the forward declarations need to be inside a namespace as well
    extern const double pi;
    extern const double avogadro;
    extern const double myGravity;
}

#endif
```

`main.cpp`:
``` cpp 
#include "constants.h" // include all the forward declarations

#include <iostream>

int main()
{
    std::cout << "Enter a radius: ";
    int radius{};
    std::cin >> radius;

    std::cout << "The circumference is: " << 2.0 * radius * constants::pi << '\n';

    return 0;
}
```

::: tip  缺点
不利于编译器优化
:::

#### 3. 公共头文件中使用内联变量
`constants.h`:
``` cpp
#ifndef CONSTANTS_H
#define CONSTANTS_H

// define your own namespace to hold constants
namespace constants
{
    inline constexpr double pi { 3.14159 }; // note: now inline constexpr
    inline constexpr double avogadro { 6.0221413e23 };
    inline constexpr double myGravity { 9.2 }; // m/s^2 -- gravity is light on this planet
    // ... other related constants
}
#endif
```

`main.cpp`:
``` cpp 
#include "constants.h"

#include <iostream>

int main()
{
    std::cout << "Enter a radius: ";
    int radius{};
    std::cin >> radius;

    std::cout << "The circumference is: " << 2.0 * radius * constants::pi << '\n';

    return 0;
}
```
## 链接(Linkage)
An identifier’s **linkage** determines whether other declarations of that name refer to the same object or not.
### 无链接(no linkage)
局部变量
### 内部链接(internal linkage)

An identifier with **internal linkage** can be seen and used within a single translation unit, but it is not accessible from other translation units (that is, it is not exposed to the linker).

注意：
1. 全局常量(const global variable)
`const` and `constexpr` global variables have internal linkage by default.
2. 全局变量(non-constant global variable)
To make a non-constant global variable internal, we use the `static` keyword.
3. 函数(function)
Functions default to external linkage (which we’ll cover in the next lesson), but can be set to internal linkage via the `static` keyword

### 外部链接(external linkage)

An identifier with external linkage can be seen and used both from the file in which it is defined, and from other code files (via a forward declaration).

2. 全局变量(non-constant global variable)
- 全局变量默认是`external`的，可以通过`static`变为`internal`
- 全局常量默认是`internal`的，可以通过`extern`变为`external`


``` cpp 
// External global variable definitions:
int g_x;                       // defines non-initialized external global variable (zero initialized by default)
extern const int g_x{ 1 };     // defines initialized const external global variable
extern constexpr int g_x{ 2 }; // defines initialized constexpr external global variable

// Forward declarations
extern int g_y;                // forward declaration for non-constant global variable
extern const int g_y;          // forward declaration for const global variable
extern constexpr int g_y;      // not allowed: constexpr variables can't be forward declared
```

- 内联变量(inline variable)默认是外部链接的
- 全局变量容易导致bug
参考：[why-non-const-global-variables-are-evil](https://www.learncpp.com/cpp-tutorial/why-non-const-global-variables-are-evil/)

**non-const global variables** are dangerous is because 
1) their values can be changed by any function that is called, and there is no easy way for the programmer to know that this will happen.
2) Global variables also make your program less modular and less flexible. 


**Local variables** are much safer because other functions can not affect them directly.

>Use local variables instead of global variables whenever possible. #最佳实践

> 适合使用全局变量的场景: 日志文件
- 全局变量初始化顺序

  * 静态初始化: In the static initialization phase, global variables with constexpr initializers (including literals) are initialized to those values. Also, global variables without initializers are zero-initialized.
  * 动态初始化:  the gist of it is that global variables with non-constexpr initializers are initialized.

