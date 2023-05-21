# 简介
参考： https://www.programiz.com/cpp-programming/variables-literals

<!-- more -->

# 语法
## Hello World
```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello world!" << endl;
    return 0;
}
```

## 基本I/O

```cpp
#include <iostream>
using namespace std;

int main() {
    char a;
    int num;

    cout << "Enter a character and an integer: ";
    cin >> a >> num;

    cout << "Character: " << a << endl;
    cout << "Number: " << num;

    return 0;
}

```
## 变量
### 声明

```cpp
// 变量声明及初始化
int age = 14;   // age is 14
age = 17;       // age is 17

// 常量声明
const int LIGHT_SPEED = 299792458;
LIGHT_SPEED = 2500 // Error! LIGHT_SPEED is a constant.
```
### 数据类型
基本类型：  

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0599938bd9f21256faf2e6fff390a4b0.image.png)

延申类型：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0b012b5b62b8bd5345aa2fa60d9abefc.image.png)

### 类型转换
1. 隐式转换  
可能存在精度损失(由大转小)。
```cpp
// assigning an int value to num_int
int num_int = 9;

// declaring a double type variable
double num_double;

// implicit conversion
// assigning int value to a double variable
num_double = num_int;

cout << "num_int = " << num_int << endl;
cout << "num_double = " << num_double << endl;
```
3. 显式转换

```cpp
// initializing a double variable
double num_double = 3.56;
cout << "num_double = " << num_double << endl;

// C风格转换：C-style conversion from double to int
int num_int1 = (int)num_double;
cout << "num_int1   = " << num_int1 << endl;

// 函数式转换：function-style conversion from double to int
int num_int2 = int(num_double);
cout << "num_int2   = " << num_int2 << endl;
```

### 存储类(Storage Class)
#### 局部变量(Local Variable)
定义在函数内部的变量，生命周期只存在于函数内部，当函数退出后就会销毁。

#### 全局变量(Global Variable)
位于所有函数外部的变量。
生命周期从程序开始直到程序结束。

#### 静态局部变量(Static Local variable)

```cpp
int main()
{
   static float a;
   ... .. ...
}
```
生命周期从第一次函数调用开始，直到整个程序结束。

#### 寄存器变量(Register Variable)
存储在寄存器中，相比内存速度更快，在C++11中被弃用。

#### 线程局部变量(Thread Local Storage)
参考： http://www.codeproject.com/Articles/8113/Thread-Local-Storage-The-C-Way

## 算子
### 赋值运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/6d9b3f3c26ca49538a161e20820b6d70.image.png)

### 算术运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/dc1f2a6c843dc607c2e1535f5282fc2a.image.png)

### 逻辑运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/b7321f347263f64ed4b4c5e224f9b8bf.image.png)

### 比较运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/6bc82d2235e1c88634c298caa52aff5e.image.png)
### 位运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/71d085d7f5e4eff231a2a505484df6b1.image.png)
### 其他算子

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/55544574d42ea96b4e7c83c5712c79c5.image.png)

## 字符串
### C-Style String
```cpp
char str[] = "C++";
```
### String Class


```cpp
#include <iostream>
using namespace std;

int main()
{
    // Declaring a string object
    string str;
    cout << "Enter a string: ";
    getline(cin, str);

    cout << "You entered: " << str << endl;
    return 0;
}
```

## 数组
### 数组声明
#### 一维数组
格式：
```cpp
dataType arrayName[arraySize];
```

举例：

```cpp
int x[6];

// declare and initialize and array
int x[6] = {19, 10, 8, 17, 9, 15};

// declare and initialize an array
int x[] = {19, 10, 8, 17, 9, 15};

// store only 3 elements in the array
int x[6] = {19, 10, 8};
```
#### 多维数组

```cpp
int  test[2][3] = { {2, 4, 5}, {9, 0, 19}};

int test[2][3][4] = {
    { {3, 4, 2, 3}, {0, -3, 9, 11}, {23, 12, 23, 2} },
    { {13, 4, 56, 3}, {5, 9, 3, 5}, {5, 1, 4, 9} }
}
```

### 数组基本操作
- 遍历数组
```cpp
int numbers[5] = {7, 5, 6, 12, 35};
for (const int &n : numbers) {
    cout << n << "  ";
}
```
## 函数
### 函数声明
格式：

```cpp
returnType functionName (parameter1, parameter2,...) {
    // function body   
}
```

举例：

```cpp
#include <iostream>
using namespace std;

// declaring a function
int add(int a, int b) {
    return (a + b);
}

int main() {

    int sum;
    
    // calling the function and storing
    // the returned value in sum
    sum = add(100, 78);

    cout << "100 + 78 = " << sum << endl;

    return 0;
}
```

### 函数重载

:::info{title="什么是函数重载"}
**函数重载**是指在同一作用域中的某个函数和运算符指定多个定义，分别称为函数重载和运算符重载。

重载声明是指一个与之前已经在该作用域内声明过的函数或方法具有相同名称的声明，但是它们的参数列表和定义（实现）不相同。

当您调用一个重载函数或重载运算符时，编译器通过把您所使用的参数类型与定义中的参数类型进行比较，决定选用最合适的定义。选择最合适的重载函数或重载运算符的过程，称为重载决策。


```cpp
// same name different arguments
int test() { }
int test(int a) { }
float test(double a) { }
int test(int a, double b) { }
```
注意：不能仅仅是返回值类型不同，参数列表需要有所变化(数量或类型上)
:::

举例：
```cpp
#include <iostream>
using namespace std;

// function with 2 parameters
void display(int var1, double var2) {
    cout << "Integer number: " << var1;
    cout << " and double number: " << var2 << endl;
}

// function with double type single parameter
void display(double var) {
    cout << "Double number: " << var << endl;
}

// function with int type single parameter
void display(int var) {
    cout << "Integer number: " << var << endl;
}

int main() {

    int a = 5;
    double b = 5.5;

    // call function with int type parameter
    display(a);

    // call function with double type parameter
    display(b);

    // call function with 2 parameters
    display(a, b);

    return 0;
}
```
### 操作符重载
格式：

```cpp
class className {
    ... .. ...
    public
       returnType operator symbol (arguments) {
           ... .. ...
       } 
    ... .. ...
};
```
举例：
```cpp
// Overload ++ when used as prefix

#include <iostream>
using namespace std;

class Count {
   private:
    int value;

   public:

    // Constructor to initialize count to 5
    Count() : value(5) {}

    // Overload ++ when used as prefix
    void operator ++ () {
        ++value;
    }

    void display() {
        cout << "Count: " << value << endl;
    }
};

int main() {
    Count count1;

    // Call the "void operator ++ ()" function
    ++count1;

    count1.display();
    return 0;
}
```
### 默认参数

```cpp
// Invalid
void add(int a, int b = 3, int c, int d);

// Invalid
void add(int a, int b = 3, int c, int d = 4);

// Valid
void add(int a, int c, int b = 3, int d = 4);
```
注意： 默认参数必须放在参数列表最后

## 指针
### 指针声明
```cpp
int *pointVar;
int* pointVar; // preferred syntax
int* pointVar, p; // 只有前者是指针
```

### 指针基础操作

```cpp
int* pointVar, var;
var = 5;

// 指针赋值：assign address of var to pointVar
pointVar = &var;

// 访问指针指向元素值：access value pointed by pointVar
cout << *pointVar << endl;   // Output: 5

// 修改指针指向元素值
*pointVar = 16;
```
## 结构体

```cpp
#include <iostream>
using namespace std;

struct Person
{
    char name[50];
    int age;
    float salary;
};

int main()
{
    Person p1;
    
    cout << "Enter Full name: ";
    cin.get(p1.name, 50);
    cout << "Enter age: ";
    cin >> p1.age;
    cout << "Enter salary: ";
    cin >> p1.salary;

    cout << "\nDisplaying Information." << endl;
    cout << "Name: " << p1.name << endl;
    cout <<"Age: " << p1.age << endl;
    cout << "Salary: " << p1.salary;

    return 0;
}
```

## 枚举

```cpp
#include <iostream>
using namespace std;

enum week { Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday };

int main()
{
    week today;
    today = Wednesday;
    cout << "Day " << today+1; // Day 4
    return 0;
}
```
## 控制流
### 条件
### `?:`算子

格式：
`condition ? expression1 : expression2;`

举例：

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
  int number = -4;
  string result;

  // Using ternary operator
  result = (number > 0) ? "Positive Number!" : "Negative Number!";

  cout << result << endl;

  return 0;
}
```
#### `if`  

格式：

```cpp
if (condition1) {
  // code block 1
}
else if (condition2){
  // code block 2
}
else {
  // code block 3
}
```
举例：
```cpp
// Program to check whether an integer is positive, negative or zero

#include <iostream>
using namespace std;

int main() {

  int number;

  cout << "Enter an integer: ";
  cin >> number;

  if (number > 0) {
    cout << "You entered a positive integer: " << number << endl;
  } 
  else if (number < 0) {
    cout << "You entered a negative integer: " << number << endl;
  } 
  else {
    cout << "You entered 0." << endl;
  }

  cout << "This line is always printed.";

  return 0;
}
```

#### `switch`

格式：


```cpp
switch (expression)  {
    case constant1:
        // code to be executed if 
        // expression is equal to constant1;
        break;

    case constant2:
        // code to be executed if
        // expression is equal to constant2;
        break;
        .
        .
        .
    default:
        // code to be executed if
        // expression doesn't match any constant
}
```

举例：


```cpp
// Program to build a simple calculator using switch Statement
#include <iostream>
using namespace std;

int main() {
    char oper;
    float num1, num2;
    cout << "Enter an operator (+, -, *, /): ";
    cin >> oper;
    cout << "Enter two numbers: " << endl;
    cin >> num1 >> num2;

    switch (oper) {
        case '+':
            cout << num1 << " + " << num2 << " = " << num1 + num2;
            break;
        case '-':
            cout << num1 << " - " << num2 << " = " << num1 - num2;
            break;
        case '*':
            cout << num1 << " * " << num2 << " = " << num1 * num2;
            break;
        case '/':
            cout << num1 << " / " << num2 << " = " << num1 / num2;
            break;
        default:
            // operator is doesn't match any case constant (+, -, *, /)
            cout << "Error! The operator is not correct";
            break;
    }

    return 0;
}
```
### 循环
#### `for`
- 方法一：经典for  
格式：

```cpp
for (initialization; condition; update) {
    // body of-loop 
}
```

举例:

```cpp
for (int i = 1; i <= 5; ++i) {
    cout << i << " ";
}
```

- 方法二：`for each`

格式：

```cpp
for (variable : collection) {
    // body of loop
}
```

举例：

```cpp
int num_array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
for (int n : num_array) {
    cout << n << " ";
}
```
#### `while`

格式：


```cpp
while (condition) {
    // body of the loop
}
```


举例：

```cpp
int i = 1; 
// while loop from 1 to 5
while (i <= 5) {
    cout << i << " ";
    ++i;
}
```


## 面向对象
### 类
#### 类声明
声明举例：
```cpp
class Room {
    public:
        double length;
        double breadth;
        double height;   

        double calculateArea(){   
            return length * breadth;
        }

        double calculateVolume(){   
            return length * breadth * height;
        }

};
```

使用举例：
```cpp
// Program to illustrate the working of
// objects and class in C++ Programming

#include <iostream>
using namespace std;

// create a class
class Room {

   public:
    double length;
    double breadth;
    double height;

    double calculateArea() {
        return length * breadth;
    }

    double calculateVolume() {
        return length * breadth * height;
    }
};

int main() {

    // create object of Room class
    Room room1;

    // assign values to data members
    room1.length = 42.5;
    room1.breadth = 30.8;
    room1.height = 19.2;

    // calculate and display the area and volume of the room
    cout << "Area of Room =  " << room1.calculateArea() << endl;
    cout << "Volume of Room =  " << room1.calculateVolume() << endl;

    return 0;
}
```
#### 构造函数

```cpp
#include <iostream>
using namespace std;

// declare a class
class Wall {
  private:
    double length;
    double height;

  public:

    // 参数化构造：initialize variables with parameterized constructor
    Wall(double len, double hgt) {
      length = len;
      height = hgt;
    }

    // 拷贝式构造：copy constructor with a Wall object as parameter
    // copies data of the obj parameter
    Wall(Wall &obj) {
      length = obj.length;
      height = obj.height;
    }

    double calculateArea() {
      return length * height;
    }
};

int main() {
  // create an object of Wall class
  Wall wall1(10.5, 8.6);

  // copy contents of wall1 to wall2
  Wall wall2 = wall1;

  // print areas of wall1 and wall2
  cout << "Area of Wall 1: " << wall1.calculateArea() << endl;
  cout << "Area of Wall 2: " << wall2.calculateArea();

  return 0;
}
```
#### 权限控制
1. `public`  
用来创建公有成员(数据或方法)，可在整个程序内访问。

3. `private`  
用来创建私有成员(数据或方法)，只能在类的内部访问，但是友元类和友元函数可以访问。

5. `protected`  
用来创建保护成员(数据或方法)，可在当前类以及其派生子类中访问。


![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/8ced491cc150be5587c075746a11011e.image.png)

注意：C++的默认成员权限是`private`

### 继承
#### 继承语法
```cpp
class Animal {
    // eat() function
    // sleep() function
};

class Dog : public Animal {
    // bark() function
};
```

#### 继承访问控制
1. 公有继承：`public inheritance`  
父类public成员仍然public,  
父类protected成员仍然protected,  
父类private成员无法访问,

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/65360be5b9350dc91195e7f935d3dd63.image.png)

3. 私有继承：`private  inheritance`  
父类public成员变为private,  
父类protected成员变为private,  
父类private成员无法访问,

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/d5ce0d8e85d674da7f1465a9a5512641.image.png)

5. 保护继承：`protected inheritance`  
父类public成员变为protected,  
父类protected成员仍然protected,  
父类private成员无法访问,

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/916530e94a192b434e9c1d3f58d513bf.image.png)

#### 多继承

```cpp
#include <iostream>
using namespace std;

class Mammal {
  public:
    Mammal() {
      cout << "Mammals can give direct birth." << endl;
    }
};

class WingedAnimal {
  public:
    WingedAnimal() {
      cout << "Winged animal can flap." << endl;
    }
};

class Bat: public Mammal, public WingedAnimal {};

int main() {
    Bat b1;
    return 0;
}
```
输出：
```log
Mammals can give direct birth.
Winged animal can flap.
```

#### 友元函数(friend function)和友元类(friend class)

可以访问类的私有成员
1. 友元函数
```cpp
// C++ program to demonstrate the working of friend function

#include <iostream>
using namespace std;

class Distance {
    private:
        int meter;
        
        // friend function
        friend int addFive(Distance);

    public:
        Distance() : meter(0) {}
        
};

// friend function definition
int addFive(Distance d) {

    //accessing private members from the friend function
    d.meter += 5;
    return d.meter;
}

int main() {
    Distance D;
    cout << "Distance: " << addFive(D);
    return 0;
}
```
2. 友元类

```cpp
// C++ program to demonstrate the working of friend class

#include <iostream>
using namespace std;

// forward declaration
class ClassB;

class ClassA {
    private:
        int numA;

        // friend class declaration
        friend class ClassB;

    public:
        // constructor to initialize numA to 12
        ClassA() : numA(12) {}
};

class ClassB {
    private:
        int numB;

    public:
        // constructor to initialize numB to 1
        ClassB() : numB(1) {}
    
    // member function to add numA
    // from ClassA and numB from ClassB
    int add() {
        ClassA objectA;
        return objectA.numA + numB;
    }
};

int main() {
    ClassB objectB;
    cout << "Sum: " << objectB.add();
    return 0;
}
```

### 多态
父类指针指向子类对象，实现根据对象的不同执行不同的函数。
#### 场景举例

```cpp
#include <iostream> 
using namespace std;
 
class Shape {
   protected:
      int width, height;
   public:
      Shape( int a=0, int b=0)
      {
         width = a;
         height = b;
      }
      int area()
      {
         cout << "Parent class area :" <<endl;
         return 0;
      }
};
class Rectangle: public Shape{
   public:
      Rectangle( int a=0, int b=0):Shape(a, b) { }
      int area ()
      { 
         cout << "Rectangle class area :" <<endl;
         return (width * height); 
      }
};
class Triangle: public Shape{
   public:
      Triangle( int a=0, int b=0):Shape(a, b) { }
      int area ()
      { 
         cout << "Triangle class area :" <<endl;
         return (width * height / 2); 
      }
};

// 程序的主函数
int main( )
{
   Shape *shape;
   Rectangle rec(10,7);
   Triangle  tri(10,5);
 
   // 存储矩形的地址
   shape = &rec;
   // 调用矩形的求面积函数 area
   shape->area();
 
   // 存储三角形的地址
   shape = &tri;
   // 调用三角形的求面积函数 area
   shape->area();
   
   return 0;
}
```
#### 虚函数(virtual function)
虚函数是 C++ 实现动态多态性的方式。当某个虚函数通过指针或者引用调用时，编译器产生的代码直到运行时才能确定到底调用哪个版本的函数。被调用的函数是与绑定到指针或者引用上的对象的动态类型相匹配的那个。因此，借助虚函数，我们可以实现多态性。
```cpp
#include <iostream>
using namespace std;

class Base {
   public:
    virtual void print() {
        cout << "Base Function" << endl;
    }
};

class Derived : public Base {
   public:
    void print() {
        cout << "Derived Function" << endl;
    }
};

int main() {
    Derived derived1;

    // pointer of Base type that points to derived1
    Base* base1 = &derived1;

    // calls member function of Derived class
    base1->print();

    return 0;
}
```
输出：

```log
Derived Function
```
## STL
### `vector`
### `stack`
### `queue`
### `map`
### `unordered_map`

# 参考
[1] https://www.programiz.com/cpp-programming/variables-literals