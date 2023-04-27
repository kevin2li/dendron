---
id: opbxfa5jie5tzo1s0glei45
title: C++
desc: ''
updated: 1682587130235
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

## Linkage
### `no linkage`:
### `internal linkage`

An identifier with **internal linkage** can be seen and used within a single translation unit, but it is not accessible from other translation units (that is, it is not exposed to the linker).

注意：
1. `const` and `constexpr` global variables have internal linkage by default.
2. To make a non-constant global variable internal, we use the `static` keyword.
 Functions default to external linkage (which we’ll cover in the next lesson), but can be set to internal linkage via the static keyword

### `external linkage`
