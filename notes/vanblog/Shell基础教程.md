# 简介
Shell是一种计算机程序，称为命令行解释器，它允许Linux和Unix用户使用命令行界面控制操作系统。Shell允许用户高效、直接地与操作系统通信。
<!-- more -->

# 语法
## 模式扩展
Shell 接收到用户输入的命令以后，会根据空格将用户的输入，拆分成一个个词元（token），然后，Shell 会扩展词元里面的**特殊字符**，扩展完成后才会调用相应的命令。这种特殊字符的扩展，称为模式扩展。

常用扩展模式如下：

- `~`: 自动扩展成当前用户的主目录
- `?`: 匹配任意单个字符
- `*`: 匹配任意数量的任意字符
- `[..]`: 匹配方括号中的任意一个字符
- `[start-end]`: 匹配连续范围内的字符，如`[a-zA-Z]`,`[0-9]`
- `{..}`: 分别扩展成大括号里面的所有值，如`{a,b,c}.txt`=>`a.txt b.txt c.txt`
- `{start..end}`: 分别扩展成大括号里面连续序列的所有值，如`{a..c}.txt`=>`a.txt b.txt c.txt`.此外还支持指定步长，格式为`{start..end..step}`，如`{0..8..2}`=>`0 2 4 6 8`

:::info{title="常见用法"}
```bash
# 用法一：用在for循环
for i in {1..4}
do
  echo $i
done

# 用法二：创建规则目录
mkdir {2007..2009}-{01..12}

# 用法三：匹配多个后缀
echo .{mp{3..4},m4{a,b,p,v}} # .mp3 .mp4 .m4a .m4b .m4p .m4v

```
:::
- `${varname}`: 变量扩展
- `$(...)`: 子命令扩展, 如`$(date)`
- `$((...))`: 算术扩展，如`$((2+2))`
- `[[:class:]]`: 字符类扩展，如`[[:upper:]]`匹配任意大写字母A-Z

:::info{title="常用字符类"}

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/4443d94d6a332ab8bc7b13360f1e82ec.image.png)

:::


## 变量
### 环境变量和自定义变量  

**环境变量**是 Bash 环境自带的变量，进入 Shell 时已经定义好了，可以直接使用。它们通常是系统定义好的，也可以由用户从父 Shell 传入子 Shell。

:::tip{title="提示"}
`env`命令或`printenv`命令，可以显示所有环境变量
```bash
# 查看所有环境变量
env

# 查看PATH环境变量
echo $PATH
printenv PATH
```
:::

**自定义变量**是用户在当前 Shell 里面自己定义的变量，仅在当前 Shell 可用。一旦退出当前 Shell，该变量就不存在了。

:::tip{title="提示"}
`set`命令可以显示所有变量（包括环境变量和自定义变量），以及所有的 Bash 函数
:::

### 变量创建、读取、修改、删除
- 变量创建  

命名规范：由字母、数字、下划线组成，第一个字符必须为字母或下划线。  
变量创建示例：
```bash
a=z                     # 变量 a 赋值为字符串 z
b="a string"            # 变量值包含空格，就必须放在引号里面
c="a string and $b"     # 变量值可以引用其他变量的值
d="\t\ta string\n"      # 变量值可以使用转义字符
e=$(ls -l foo.txt)      # 变量值可以是命令的执行结果
f=$((5 * 7))            # 变量值可以是数学运算的结果
```

- 变量读取

三种方式：`$varname`,`${varname}`,`${!varname}`

```bash
a=USER

# 方式1
$a # USER

# 方式2：在字符串拼接时可以避免变量名歧义，明确变量名边界
${a} # USER

# 方式3：!a就相当于读了一次变量值，外面再套层${}再读了一次变量值
${!a} # kevin2li
```

- 变量修改  

对变量重新赋值即可，类似变量创建

- 变量删除  

可以使用`unset`命令
```bash
foo="123"
unset foo
# or
foo=""
```
由于bash中不存在的变量都会解释为空字符串，所以，删除一个变量，也可以将这个变量设成空字符串。

### 特殊变量
- `$?`: 上一个命令的退出码，用来判断上一个命令是否执行成功。返回值是0，表示上一个命令执行成功；如果不是0，表示上一个命令执行失败
- `$$`: 当前 Shell 的进程 ID
- `$_`: 上一个命令的最后一个参数
- `$!`: 最近一个后台执行的异步命令的进程 ID
- `$0`: 当前shell的名称
- `$-`: 当前shell的启动参数
- `$@`: 脚本的参数值，各个参数间用空格拼接
- `$#`: 脚本的参数总数

### 命令声明变量
- `declare`  
格式：
```bash
declare OPTION VARIABLE=value
```
![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0c05e06efb4ddc4dfc33a72243d9de9b.image.png)

- `readonly`  
声明只读变量，不能改变变量值，相当于`declare -r`

```bash
readonly foo=1
```

- `let`  
声明变量时，可以直接执行算术表达式
```bash
let foo=1+2
echo $foo # 3
```

## 算术运算
### 算术表达式
`((...))`语法可以进行各类运算  

`$((...))`可以拿到运算结果的值  

`$((varname=...))`可以将运算结果的值赋值给变量`varname`  

### 算术运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a1800dae5d25654317d39bc9591f52d3.image.png)

:::info{title="数值的进制"}

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/051fdda4ed86a9c6d2c82357c7a2a1f1.image.png)
:::

### 位运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a84c47457d649d2b6aadc45fb136a3ae.image.png)

### 逻辑运算

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/0907a9b96e3fe49b219b4e6b94bec1cf.image.png)

## 字符串操作
### 获取字符串长度

格式： `${#varname}`
```bash
a="kevin"
echo ${#a} # 5
```
### 提取子串

格式：`${varname:offset:length}`  

:::tip{title="提示"}
1. `length`参数可省略，表示读取到字符串结尾
2. `length`参数可为负值，表示从字符串的末尾开始算起的偏移位置(不包含)
3. `offset`参数可为负值，表示从字符串的末尾开始算起，不过注意，**负数前面必须有一个空格**
:::

```bash
a="hello world"
echo ${a:6:3}   # wor
echo ${a:6}     # world
echo ${a: -3:2} # rl
echo ${a:3:-2}  # lo wor
```
### 改变大小写
全部转大写：`${varname^^}`  
全部转小写：`${varname,,}`
```bash
a="HeLLo"
echo ${a^^} # HELLO
echo ${a,,} # hello
```

### 搜索和替换

参考：https://wangdoc.com/bash/string

## 数组
### 数组创建
```bash
# 方式1：逐个赋值
ARRAY[INDEX]=value

# 方式2：一次性赋值
ARRAY=(value1 value2 ... valueN)

# 等同于
ARRAY=(
  value1
  value2
  value3
)
```

### 数组读取
- 读取单个元素: `${array[i]}` (如果不加索引，会读取首成员的值)
- 读取所有元素: `${array[@]}`或`${array[*]}`
- 读取数组长度：`${#array[*]}`或`${#array[@]}`
- 读取数组切片：`${array[@]:position:length}`
- 读取数组序号：`${!array[@]}`或`${!array[*]}` (返回数组的成员序号，即哪些位置是有值的)

举例：
```bash
activities=( swimming "water skiing" canoeing "white-water rafting" surfing )
for act in "${activities[@]}";
do 
    echo "Activity: $act"; 
done
```

输出：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/a10f4952101f714e7739d3c8bb33b88c.image.png)

:::info{title="注意"}
遍历时一般把`${activities[@]}`放在双引号之中，否则可能会得到错误的结果，如上面的例子，如果不放到双引号内会返回7个成员。
:::

### 数组修改
- 修改成员值
```bash
array[i]=new_val
```
- 追加成员: `+=`
```bash
foo=(a b c)
foo+=(d e f) # (a b c d e f)
```

### 删除数组

```bash
foo=(a b c d e)

# 删除数组成员
unset foo[1] # (a c d e)

# 删除整个数组
unset foo # 空
```

## 字典
Bash 的新版本才支持。
```bash
declare -A colors
colors["red"]="#ff0000"
colors["green"]="#00ff00"
colors["blue"]="#0000ff"

echo ${colors["blue"]}
```

## 条件语句
格式：
```bash
if commands; then
  commands
[elif commands; then
  commands...]
[else
  commands]
fi
```
示例：
```bash
if test $USER = "foo"; then
  echo "Hello foo."
else
  echo "You are not foo."
fi
```

```bash
echo -n "输入一个1到3之间的数字（包含两端）> "
read character
if [ "$character" = "1" ]; then
    echo 1
elif [ "$character" = "2" ]; then
    echo 2
elif [ "$character" = "3" ]; then
    echo 3
else
    echo 输入不符合要求
fi
```

:::info{title="test命令"}
```bash
# 写法一
test expression

# 写法二
[ expression ]

# 写法三
[[ expression ]]
```
**注意：** 第二种和第三种写法，[和]与内部的表达式之间必须有空格

示例：
```bash
# 写法一
if test -e /tmp/foo.txt ; then
  echo "Found foo.txt"
fi

# 写法二
if [ -e /tmp/foo.txt ] ; then
  echo "Found foo.txt"
fi

# 写法三
if [[ -e /tmp/foo.txt ]] ; then
  echo "Found foo.txt"
fi
```
常用判断命令：
- `[ -e file ]`: 如果 file 存在，则为true
- `[ -d file ]`: 如果 file 存在，并且为目录，则为true
- `[ -w file ]`: 如果 file 存在，并且可写，则为true
- `[ -n string ]`: 如果string长度大于0，则为true
- `[ -z string ]`: 如果string长度等于0，则为true
- `[ string1 != string2 ]`: 如果string1和string2不相同，则为true
- `[ integer1 -eq integer2 ]`: 如果integer1等于integer2，则为true

详情：https://wangdoc.com/bash/condition
:::



## 循环语句
- while循环

格式：
```bash
while condition; do
  commands
done
```
示例：
```bash
number=0
while [ "$number" -lt 10 ]; do
  echo "Number = $number"
  number=$((number + 1))
done
```

- for循环

格式：
```bash
for (( initializer; condition; step )); do
  commands
done
```

示例：
```bash
for (( c=1; c<=5; c++ ))
do 
   echo "Welcome $c times"
done
```

- for...in循环

格式：
```bash
for VARIABLE in list
do
    command1 on $VARIABLE
    command2
    commandN
done
```
示例：
```bash
for i in {1..4}
do
  echo $i
done
```

```bash
for i in word1 word2 word3; do
  echo $i
done
```
```bash
for i in *.png; do
  ls -l $i
done
```

## 函数
```bash
# 第一种
fn() {
  # codes
}

# 第二种
function fn() {
  # codes
}
```
- 参数变量(可在函数内部直接引用)：

![image.png](https://minio.kevin2li.top/image-bed/vanblog/img/128926b0a3ccf26547b6f0f2db9a55ba.image.png)

- `return`命令  
可以在`$?`中拿到函数执行的返回结果

# Q&A
1. `()`和`(())`的区别  
在Bash中，括号`()`用于命令分组和子shell，而双括号`(())`用于算术运算，例如加法、减法、乘法、除法、模数、变量的增量和减量。 括号()用于将命令分组在一起并在子shell中运行。

2. `[]`和`[[]]`的区别  
在Bash中，方括号`[]`和双方括号`[[]]`都用于测试条件。 但是，双方括号`[[]]`比方括号`[]`更强大，因为它支持更多的模式匹配和正则表达式操作。 双方括号`[[]]`还支持嵌套和逻辑运算符。

3. `''`和`""`的区别  
在Bash中，单引号`''`和双引号`""`都用于字符串。 但是，双引号`""`允许在字符串中使用变量和转义字符，而单引号`''`不允许。 双引号`""`还支持命令替换。

# 参考
[1] [阮一峰的网络日志-Bash 脚本教程](https://wangdoc.com/bash/intro)