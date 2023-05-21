# 简介

参考：https://www.programiz.com/javascript/get-started
<!-- more -->

# 语法
## Hello world
```js
console.log("I love JS");
```

## 变量
### 变量声明
使用`var`或`let`声明变量，使用`const`声明常量。
```js
// 变量声明
let x = 5, y = 6, z = 7;

// 常量声明
const x = 5;
x = 10;  // Error! constant cannot be changed.
console.log(x)
```

:::info{title="var和let的区别"}
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/74940e7f35fb9151eb56e3bea2882076.image.png)

推荐使用`let`.
:::

### 数据类型
8种数据类型：  
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/cf9d63ede2d956df84618869b419f933.image.png)

```js
// Number
const number1 = 3;
const number2 = 3.433;
const number3 = 3e5 // 3 * 10^5

// BigInt value: 在最后追加字母n
const value1 = 900719925124740998n;

// Boolean
const dataChecked = true;
const valueCounted = false;

// undefined
let name;
console.log(name); // undefined

// null
const number = null;

// Object
const value1 = Symbol('hello');

// Symbol
const student = {
    firstName: 'ram',
    lastName: null,
    class: 10
};
```

:::tip{title="如何判断变量类型"}
可以使用`typeof`函数：
```js
const name = 'ram';
typeof(name); // returns "string"

const number = 4;
typeof(number); //returns "number"

const valueChecked = true;
typeof(valueChecked); //returns "boolean"

const a = null;
typeof(a); // returns "object"
```
:::

## 算子
### 算术

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/3acd9306a6f62bf7ad7873cef3757292.image.png)

```js
let x = 5;
let y = 3;

// addition
console.log('x + y = ', x + y);  // 8

// subtraction
console.log('x - y = ', x - y);  // 2

// multiplication
console.log('x * y = ', x * y);  // 15

// division
console.log('x / y = ', x / y);  // 1.6666666666666667

// remainder
console.log('x % y = ', x % y);   // 2

// increment
console.log('++x = ', ++x); // x is now 6
console.log('x++ = ', x++); // prints 6 and then increased to 7
console.log('x = ', x);     // 7

// decrement
console.log('--x = ', --x); // x is now 6
console.log('x-- = ', x--); // prints 6 and then decreased to 5
console.log('x = ', x);     // 5

//exponentiation
console.log('x ** y =', x ** y);
```
### 比较

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/c258c4e1acee5fdac6991dd9952e8c1b.image.png)

```js
// equal operator
console.log(2 == 2); // true
console.log(2 == '2'); // true

// not equal operator
console.log(3 != 2); // true
console.log('hello' != 'Hello'); // true

// strict equal operator
console.log(2 === 2); // true
console.log(2 === '2'); // false

// strict not equal operator
console.log(2 !== '2'); // true
console.log(2 !== 2); // false

```
### 逻辑

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/e80e287a5958e1cf769a5af32d538c7a.image.png)

```js
// logical AND
console.log(true && true); // true
console.log(true && false); // false

// logical OR
console.log(true || false); // true

// logical NOT
console.log(!true); // false
```
### 位运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/d791cf978ef540621328b404c5cdd99c.image.png)
## 字符串
- 变量拼接
```js
const name = 'Jack';
console.log(`Hello ${name}!`); // Hello Jack!
```
- ``字符串  
允许在里面使用单引号或双引号，无需转义
```js
const str1 = `This is a string`;
const str2 = `This is a string with a 'quote' in it`;
const str3 = `This is a string with a "double quote" in it`;
```
## 数组
### 声明数组
```js
const words = ['hello', 'world', 'welcome'];
const array2 = new Array("eat", "sleep");
```
### 数据基础操作
- 获取数组长度

```js
const dailyActivities = [ 'eat', 'sleep'];

// this gives the total number of elements in an array
console.log(dailyActivities.length); // 2
```
- 尾部追加元素
```js
let dailyActivities = ['eat', 'sleep'];

// add an element at the end
dailyActivities.push('exercise');

console.log(dailyActivities); //  ['eat', 'sleep', 'exercise']
```
- 首部添加元素

```js
let dailyActivities = ['eat', 'sleep'];

//add an element at the start
dailyActivities.unshift('work'); 

console.log(dailyActivities); // ['work', 'eat', 'sleep']
```

- 删除尾部元素

```js
let dailyActivities = ['work', 'eat', 'sleep', 'exercise'];

// remove the last element
dailyActivities.pop();
console.log(dailyActivities); // ['work', 'eat', 'sleep']

// remove the last element from ['work', 'eat', 'sleep']
const removedElement = dailyActivities.pop();

//get removed element
console.log(removedElement); // 'sleep'
console.log(dailyActivities);  // ['work', 'eat']
```
- 删除首部元素

```js
let dailyActivities = ['work', 'eat', 'sleep'];

// remove the first element
dailyActivities.shift();

console.log(dailyActivities); // ['eat', 'sleep']
```
- 拷贝数组

```js
const arr1 = ['one', 'two'];
const arr2 = [...arr1, 'three', 'four', 'five'];

console.log(arr2); 
//  Output:
//  ["one", "two", "three", "four", "five"]
```

:::info{title="常用数组函数"}

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/33f88677b7f4e821c772ce2a8e82bd87.image.png)
:::

## 字典Map

```js
// create a set
let map1 = new Map();

// 插入元素：insert key-value pair
map1.set('info', {name: 'Jack', age: 26});
console.log(map1); // Map {"info" => {name: "Jack", age: 26}}

// 查看元素数量
console.log(map1.size); // 1

// 访问元素：access the elements of a Map
console.log(map1.get('info')); // {name: "Jack", age: "26"}

// 检查元素是否存在：check if an element is in Set
console.log(map1.has('info')); // true

// 删除指定元素：removing a particular element
map1.delete('address'); // false
console.log(map1); // Map {"info" => {name: "Jack", age: "26"}} 

map1.delete('info'); // true
console.log(map1); // Map {}

// 删除所有元素：removing all element
map1.clear();
console.log(map1); // Map {}

```
- 遍历字典  

方式一：  
```js
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through Map
for (let [key, value] of map1) {
    console.log(key + '- ' + value);
}
```
方式二：  
```js
// using forEach method()
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through Map
map1.forEach(function(value, key) {
  console.log(key + '- ' + value)
})
```
方式三：  

```js
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through the Map
for (let elem of map1.entries()) {
    console.log(`${elem[0]}: ${elem[1]}`);
}
```

- 只遍历key

```js
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through the Map
for (let key of map1.keys()) {
  console.log(key)
}
```
- 只遍历value

```js
let map1 = new Map();
map1.set('name', 'Jack');
map1.set('age', '27');

// looping through the Map
for (let values of map1.values()) {
    console.log(values);
}
```
## 集合Set

```js
// create Set
const set1 = new Set(); // an empty set
console.log(set1); // Set {}

// Set with multiple types of value
const set2 = new Set([1, 'hello', {count : true}]);
console.log(set2); // Set {1, "hello", {count: true}}

// 查看所有元素：access the elements of a Set
console.log(set1.values()); // Set Iterator [1, 2, 3]

// 判断元素是否存在：check if an element is in Set
console.log(set1.has(1));

// 添加元素：adding new elements
set.add(3);

// 删除指定元素：removing a particular element
set.delete(2);

// 删除所有元素：remove all elements of Set
set.clear();
```
- 遍历集合

```js
const set = new Set([1, 2, 3]);

// looping through Set
for (let i of set) {
    console.log(i);
}
```
## 控制结构
### 条件
#### `condition ? expression1 : expression2`

```js
let marks = prompt('Enter your marks :');

let result = (marks >= 40) ? 'pass' : 'fail';

console.log(`You ${result} the exam.`);
```
#### `if`

```js
const number = prompt("Enter a number: ");

if (number > 0) {
    console.log("The number is positive");
}
else if (number == 0) {
  console.log("The number is 0");
}
else {
    console.log("The number is negative");
}

console.log("The if...else if...else statement is easy");
```

#### `switch`

```js
let a = 2;
switch (a) {

    case 1:
        a = 'one';
        break;
    case 2:
        a = 'two';
        break;
    default:
        a = 'not found';
        break;
}
console.log(`The value is ${a}`);
```

### 循环
#### `for`
```js
const n = 5;

for (let i = 1; i <= n; i++) {
    console.log(i);     // printing the value of i
}
```

### `for...of`

```js
for (element of iterable) {
    // body of for...of
}
```

```js
// array
const students = ['John', 'Sara', 'Jack'];

// using for...of
for ( let element of students ) {

    // display the values
    console.log(element);
}
```
#### `while`

```js
let i = 1, n = 5;

while (i <= n) {
    console.log(i);
    i += 1;
}
```
## 函数
### 普通函数
```js
// program to add two numbers
// declaring a function
function add(a, b) {
    return a + b;
}

// take input from the user
let number1 = parseFloat(prompt("Enter first number: "));
let number2 = parseFloat(prompt("Enter second number: "));

// calling function
let result = add(number1,number2);

// display the result
console.log("The sum is " + result);
```
### 箭头函数

```js
let myFunction = (arg1, arg2, ...argN) => {
    statement(s)
}
```

```js
let sum = (a, b) => {
    let result = a + b;
    return result;
}

let result1 = sum(5,7);
console.log(result1); // 12
```
### 默认参数

```js
function sum(x = 3, y = 5) {

    // return sum
    return x + y;
}

console.log(sum(5, 15));  // 20 
console.log(sum(7));        // 12
console.log(sum());          // 8
```

### rest参数

```js
let func = function(...args) {
    console.log(args);
}

func(3); // [3]
func(4, 5, 6); // [4, 5, 6]
```

## 面向对象
### 构建
#### 通过object创建
- `object`
```js
// object creation
const person = { 
    name: 'John',
    age: 20
};
console.log(typeof person); // object

// accessing property
console.log(person.name); // John
console.log(person["name"]); // John
```

- `nested object`
```js
// nested object
const student = { 
    name: 'John', 
    age: 20,
    marks: {
        science: 70,
        math: 75
    }
}

// accessing property of student object
console.log(student.marks); // {science: 70, math: 75}

// accessing property of marks object
console.log(student.marks.science); // 70
```
- 带`method`
```js
const person = {
    name: 'Sam',
    age: 30,
    // using function as a value
    greet: function() { console.log('The name is' + ' ' + this.name); }
}

person.greet(); // hello
```

#### 通过function创建
```js
// constructor function
function Person (person_name, person_age, person_gender) {

   // assigning  parameter values to the calling object
    this.name = person_name,
    this.age = person_age,
    this.gender = person_gender,

    this.greet = function () {
        return ('Hi' + ' ' + this.name);
    }
}


// creating objects
const person1 = new Person('John', 23, 'male');
const person2 = new Person('Sam', 25, 'female');

// accessing properties
console.log(person1.name); // "John"
console.log(person2.name); // "Sam"
```
#### 通过class构建

```js
class Person {
    constructor(name) {
    this.name = name;
  }

    // defining method
    greet() {
        console.log(`Hello ${this.name}`);
    }
}

let person1 = new Person('John');

// accessing property
console.log(person1.name); // John

// accessing method
person1.greet(); // Hello John
```
### 继承和重载

```js
// parent class
class Person { 
    constructor(name) {
        this.name = name;
        this.occupation = "unemployed";
    }
    
    greet() {
        console.log(`Hello ${this.name}.`);
    }
 
}

// inheriting parent class
class Student extends Person {

    constructor(name) {
        
        // call the super class constructor and pass in the name parameter
        super(name);
        
        // Overriding an occupation property
        this.occupation = 'Student';
    }
    
    // overriding Person's method
    greet() {
        console.log(`Hello student ${this.name}.`);
        console.log('occupation: ' + this.occupation);
    }
}

let p = new Student('Jack');
p.greet();
```

### 参数解构

```js
// assigning object attributes to variables
const person = {
    name: 'Sara',
    age: 25,
    gender: 'female'    
}

// destructuring assignment
let { name, age, gender } = person;

console.log(name); // Sara
console.log(age); // 25
console.log(gender); // female
```


```js
const person = {
    name: 'Jack',
    age: 26,
    hobbies: {
        read: true,
        playGame: true
    }
}
// nested destructuring 
const {name, hobbies: {read, playGame}} = person;

console.log(name); // Jack
console.log(read); // true
console.log(playGame); // true
```
## 模块
### 常规导出
假设`module.js`内容如下:
```js
// exporting the variable
export const name = 'JavaScript Program';

// exporting the function
export function sum(x, y) {
    return x + y;
}
```
在`main.js`文件中可以这样导入：
```js
import { name, sum } from './module.js';

console.log(name);
let add = sum(4, 9);
console.log(add); // 13
```

### 默认导出
假设`module.js`内容如下:
```js
// default export
export default function greet(name) {
    return `Hello ${name}`;
}

export const age = 23;
```
在`main.js`文件中可以这样导入：

```js
import random_name from './greet.js';
```
**说明：**  
1. 一个文件中只能有一个`default eport`
2. 导入时可以不用使用`{}`，并且名称随意

### 重命名导出
方式一：
```js
// inside module.js
export {
    function1,
    function2
};

// when you want to use the module
// import in the required file with different name

import { function1 as newName1, function2 as newName2 } from './module.js';
```

方式二：

```js
// renaming import inside module.js
export {
    function1 as newName1,
    function2 as newName2
};

// when you want to use the module
// import in the main file
import { newName1, newName2 } from './module.js';
```