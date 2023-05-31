---
id: ijaxewrm8gwvx0mgp04z4i2
title: Linux命令三剑客学习
desc: ''
updated: 1685516950238
created: 1685511599074
---
## grep
grep是一个命令行文本搜索工具，它可以在文件或标准输入中搜索指定的文本模式并输出匹配的行。grep命令通常用于命令行管道中，可以与其他命令一起使用，例如find、ls等命令，以便在文件系统中搜索特定的文件。

``` bash 
# 普通搜索
grep 'hello' example.txt

# 正则搜索
grep '^a\w*' example.txt

# 输出匹配行号
grep -n 'hello' example.txt

# 递归搜索
grep -r 'hello' /home/user
```

## sed
Sed（Stream Editor）是一个流式文本编辑器，它在文本流中进行操作并将结果输出到标准输出。它是一个非交互式的命令行工具，通常在命令行管道中用于处理文本数据。

Sed命令的主要功能是在文本文件中进行搜索和替换操作。它可以对文件进行编辑，也可以通过管道读取标准输入并输出结果。Sed命令可以用正则表达式进行搜索和替换，也可以使用行号等方法来指定要编辑的行。它还可以将多个编辑命令组合在一起，以便对文本进行更复杂的处理。

``` bash 
# 将foo替换为bar
sed 's/foo/bar/g' input.txt > output.txt

# 删除含有foo的行
sed '/foo/d' input.txt > output.txt

# 在第5行之前插入文本
sed '5i This is a new line' input.txt > output.txt

# 组合命令
sed -e 's/foo/bar/g' -e '/^#/d' input.txt > output.txt
```
## awk
awk是一种文本处理工具，常用于在Unix/Linux系统中对文本进行格式化和数据处理。它的名字是由它的创始人Alfred Aho，Peter Weinberger和Brian Kernighan的姓氏首字母组成的。

### 基本语法
``` bash 
awk [options] 'pattern {action}' file
```
awk会根据`pattern`匹配到的行执行后面的`action`操作。

::: tip  演示样例文件

`grades.csv`
``` csv
Alice,85,89,92
Bob,76,80,91
Charlie,92,78,85
David,68,74,88
```
:::


### pattern
可取值：
- `BEGIN`：表示在处理输入行之前执行的操作，通常用于初始化变量、打印表头等操作
- `END`：表示在处理完所有输入行后执行的操作，通常用于计算或输出总结信息，例如计算平均值、总和、最大值、最小值等。
- `expression`: 表达式，如`$2>90`、`/regex/`、`$2 ~ /^9/`等

``` bash 
# BEGIN示例
awk -F ',' 'BEGIN {print "Name,Grade"} {print $0}' grades.csv | sort -k 2 -r

# END示例
awk -F ',' -v total=0 -v count=0 '{total+=$2; count++} END {print "Average grade: " total/count}' grades.csv

# expression示例
awk -F ',' '$2 >= 90 {print $0 > "high_grades.csv"}' grades.csv

## 逻辑关系：&&,||,!
awk -F ',' '$2 >= 60 &&  $2 < 80 {print $0 }' grades.csv
```

### options
| options | 解释                                     |
| ------- | ---------------------------------------- |
| -F      | 指定输入文件的分隔符(`FS`)，默认为制表符 |
| -v      | 定义一个变量并赋值                       |
| -f      | 指定一个包含awk脚本的文件                |

``` bash 
# 打印所有用户名
awk -F: '{print $1}' /etc/passwd

# 变量使用
awk -F ',' -v total=0 -v count=0 '{total+=$2; count++} END {print "Average grade: " total/count}' grades.csv
```

### action

| action    | 解释                         |
| --------- | ---------------------------- |
| print     | 打印指定的文本或变量。       |
| getline   | 从文件中读取下一行文本。     |
| if/else   | 基于某个条件执行不同的操作。 |
| for/while | 循环执行某个操作。           |


#### 条件(if/else)
``` bash 
# 打印以lib开头的用户名
awk -F: '{if($1 ~ /^lib/) print $1}' /etc/passwd

# 根据等级打印成绩
awk -F ',' '{if ($2 >= 90) {print $0" "$1" 优秀"} else if($2>=80) {print $0" "$1" 良好"} else {print $0" "$1" 一般"}}' grades.csv 
```

#### 循环(for/while)

``` bash 
# 打印每个同学总分
awk -F ',' '{sum = 0; for (i = 2; i <= NF; i++) sum += $i; print $1, sum / (NF - 1)}' grades.csv
```
### 内置变量

| 变量名          | 解释                                          |
| --------------- | --------------------------------------------- |
| `FS`            | Input Field Separator，输入文件的字段分隔符   |
| `OFS`           | Output Field Separator，输出文件的字段分隔符  |
| `RS`            | Input Record Separator，输入文件的记录分隔符  |
| `ORS`           | Output Record Separator，输出文件的记录分隔符 |
| `NR`            | Number of Records，当前记录的编号（行号）     |
| `NF`            | Number of Fields，当前记录中字段的数量        |
| `$0`            | 当前记录的完整文本                            |
| `$1`, `$2`, ... | 当前记录中第1, 2, ...个字段的文本             |
| `FILENAME`      | 当前输入文件的文件名                          |
| `FNR`           | 当前记录在当前输入文件中的编号                |
| `ARGC`          | 命令行参数的个数                              |
| `ARGV`          | 命令行参数的数组                              |

### 内置函数
| 函数签名                           | 解释                                                                               |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| length(str)                        | 返回字符串str的长度                                                                |
| substr(str, start, length)         | 返回字符串str中从位置start开始、长度为length的子字符串                             |
| index(str, sub)                    | 返回字符串sub在字符串str中第一次出现的位置                                         |
| split(str, array, sep)             | 将字符串str以分隔符sep为标志进行分割，并将分割后的字符串存入数组array中            |
| sprintf(format, expr1, expr2, ...) | 返回根据格式化字符串format生成的字符串。类似于C语言中的printf函数                  |
| gsub(regexp, replacement, str)     | 使用replacement替换字符串str中所有匹配正则表达式regexp的子串，并返回替换后的字符串 |
| match(str, regexp)                 | 在字符串str中查找正则表达式regexp，返回第一个匹配的位置和长度，如果没有找到则返回0 |
| toupper(str)                       | 将字符串str中的字母转换为大写字母                                                  |
| tolower(str)                       | 将字符串str中的字母转换为小写字母                                                  |
| rand()                             | 返回一个0到1之间的随机数                                                           |
| int(expr)                          | 对expr进行截断取整操作，返回整数部分                                               |
| sin(expr)                          | 返回expr的正弦值                                                                   |
| cos(expr)                          | 返回expr的余弦值                                                                   |
| atan2(y, x)                        | 返回以弧度表示的(y, x)的反正切值                                                   |

### 正则匹配
``` bash 
# 匹配以lib开头的用户名
awk -F: '$1 ~ /^lib/ {print $1}' /etc/passwd

# 匹配不以lib开头的用户名
awk -F: '$1 !~ /^lib/ {print $1}' /etc/passwd
```