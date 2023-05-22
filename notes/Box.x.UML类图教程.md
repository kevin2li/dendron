---
id: 2bix40fp24gidreqj0g77n6
title: UML类图教程
desc: ''
updated: 1682744337182
created: 1682740022468
---


## 简介
UML（统一建模语言）类图是一种用于可视化和描述系统中的对象和它们之间的关系的图表。它是一种静态结构图，用于展示系统中的类、接口、对象和它们之间的关系，以及它们的属性和方法。类图通常用于软件设计和开发，以帮助开发人员更好地理解系统的结构和组成部分，以及它们之间的交互。

在UML类图中，一个类通常表示一个对象或一组相关的对象，具有属性和方法，以及与其他类之间的关系，例如继承、实现、聚合和组合等。类图还可以包括接口、枚举类型、抽象类、泛型等元素，以及它们之间的关系。通过使用UML类图，开发人员可以更好地设计、实现和维护复杂的软件系统。

## 教程
### 实体
#### 类(Class)
1. 类的表示

![](https://minio.kevin2li.top/image-bed/20230429115341.png)

2. 成员可见性(Class Visibility)

![](https://minio.kevin2li.top/image-bed/20230429115127.png)

3. 参数方向性(Parameter Directionality)

![](https://minio.kevin2li.top/image-bed/20230429115233.png)

#### 接口(Interface)

![](https://minio.kevin2li.top/image-bed/202304291241293.png)

#### 包(Package)

![](https://minio.kevin2li.top/image-bed/202304291242751.png)

### 关系

![](https://minio.kevin2li.top/image-bed/20230429115420.png)

#### 继承关系(Inheritance)
![](https://minio.kevin2li.top/image-bed/202304291244709.png)

在UML类图中，泛化关系用空心三角和实线组成的箭头表示，从子类指向父类.

#### 实现关系(Aggregation)
![](https://minio.kevin2li.top/image-bed/202304291249118.png)

实现关系是指接口及其实现类之间的关系。在UML类图中，实现关系用空心三角和虚线组成的箭头来表示，从实现类指向接口.


#### 关联关系(Association)
![](https://minio.kevin2li.top/image-bed/202304291245448.png)
在UML图中，双向关联关系用带双箭头的实线或者无箭头的实线双线表示。单向关联用一个带箭头的实线表示，箭头指向被关联的对象.
>关联关系（Association）是指对象和对象之间的连接，它使一个对象知道另一个对象的属性和方法。在Java中，关联关系的代码表现形式为一个对象含有另一个对象的引用。也就是说，如果一个对象的类代码中，包含有另一个对象的引用，那么这两个对象之间就是关联关系。
>
>关联关系有单向关联和双向关联。如果两个对象都知道（即可以调用）对方的公共属性和操作，那么二者就是双向关联。如果只有一个对象知道（即可以调用）另一个对象的公共属性和操作，那么就是单向关联。大多数关联都是单向关联，单向关联关系更容易建立和维护，有助于寻找可重用的类。
#### 依赖关系(Dependency)
![](https://minio.kevin2li.top/image-bed/202304291246875.png)
在UML类图中，依赖关系用一个带虚线的箭头表示，由使用方指向被使用方，表示使用方对象持有被使用方对象的引用.

>依赖关系在Java中的具体代码表现形式为B为A的构造器或方法中的局部变量、方法或构造器的参数、方法的返回值，或者A调用B的静态方法。

#### 聚合关系(Aggregation)
![](https://minio.kevin2li.top/image-bed/202304291247951.png)
在UML图中，聚合关系用空心菱形加实线箭头表示，空心菱形在整体一方，箭头指向部分一方.

>聚合（Aggregation）是关联关系的一种特例，它体现的是整体与部分的拥有关系，即 “has a” 的关系。此时整体与部分之间是可分离的，它们可以具有各自的生命周期，部分可以属于多个整体对象，也可以为多个整体对象共享，所以聚合关系也常称为共享关系。例如，公司部门与员工的关系，一个员工可以属于多个部门，一个部门撤消了，员工可以转到其它部门。

#### 组合关系(Composition)
![](https://minio.kevin2li.top/image-bed/202304291248679.png)

>组合（Composition）也是关联关系的一种特例，它同样体现整体与部分间的包含关系，即 “contains a” 的关系。但此时整体与部分是不可分的，部分也不能给其它整体共享，作为整体的对象负责部分的对象的生命周期。这种关系比聚合更强，也称为强聚合。如果A组合B，则A需要知道B的生存周期，即可能A负责生成或者释放B，或者A通过某种途径知道B的生成和释放。

### 数量

![](https://minio.kevin2li.top/image-bed/202304291157763.png)

## 示例
### 订单系统
![](https://minio.kevin2li.top/image-bed/202304291158916.png)

### GUI系统
![](https://minio.kevin2li.top/image-bed/202304291159104.png)

## 参考

1. [The Easy Guide to UML Class Diagrams | Class Diagram Tutorial](https://creately.com/blog/software-teams/class-diagram-tutorial/)
2. [UML Class Diagram Tutorial](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/)
3. [30分钟学会UML类图](https://zhuanlan.zhihu.com/p/109655171)