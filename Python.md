# Python基础

## Python介绍

### Python历史

1991 年第一个 Python解释器公开版发布，它是用 C 语言编写实现的，并能够调用 C 语言的库文件。 Python 一诞生就己经具有了类、 函数和异常处理等内容， 包含字典、列表等核心数据结构，以及模块为基础的拓展系统。

2000 年 Python 2.0 发布， Python 2.0 的最后一个版本是 2.7，它还会存在较长的一段时间， Python 2.7 支持时间延长到 2020 年。 

2008 年 Python 3.0 发布，Python 3 与 Python 2 是不兼容的，由于很多 Python 程序和库都是基于 Python 2 的， 所以 Python 2 和 Python 3 程序会长期并存， 不过 Python 3 的 新功能吸引 了很多开发人员，很多开发人员正从 Python 2 升级到 Python 3 。

### Python特点

- 简单易学
- 面向对象
- 解析型语言
- 免费开源
- 可移植性强
- 胶水语言
- 丰富的库
- 规范的代码
- 函数式编程
- 动态类型

### Python应用

- Web
- 大数据
- 测试运维
- 科学计算
- 数据可视化
- 网络爬虫
- 人工智能

## Python开发环境

- PyCharm
- Eclipse + PyDev插件
- VSC

## Python基础概念

- Python标识符，关键字和Java等其他语言基本保持一致
- Python变量声明时不需要指定数据类型，与Kotlin不同，Kotlin虽然也不需要指定数据类型，但编译器会自动推断数据类型，而且指定之后不可修改数据类型，而Python的数据类型可以随意修改
- 严格意义来说，Python没有常量，只能变量当常量使用，代码安全需要程序员自己检查
- Python注释

```python
# 单行注释 ： #开头加一个空格
#

# 多行注释 ： """   """
"""
  这是一段注释
"""
```

- Python中一个文件就是一个模块，模块内可以声明变量，常量，函数，属性和类等元素，一个模块可以提供对另一个模块的访问
  - 引入另一个模块时，会将该模块执行一遍
  - 通过import关键字引入，可以全部引入，也可以引入部分元素
  - 可以通过as起别名

```python
module1:
y = True
z = 5.26

print("进入module1模块！")

module2:
import module1
from module1 import z

y = 20

# 访问当前模块 y
print(y)
# 访问module的y
print(module1.y)
# 访问module1的z
print(z)

执行结果：
进入module1模块！
20
True
5.26
```

- Python中的包和Java类似，是一种命名空间，用于解决名称冲突问题，引入模块时前面加上包名即可

## Python中的命名规范

- 包名：全小写，用"."分隔
- 模块名：全小写，用"_"分隔
- 类名，异常名：驼峰命名法
- 变量名，函数名，方法名：全小写，用"_"分隔
- 常量名：全大写，用"_"分隔

## Python中的数据类型

在Python中所有的数据类型都是类，每一个变量都是类的实例，没有基本数据类型的概念。

Python提供了6种标准数据类型：数字，字符串，列表，元组，集合和字典，其中后四项为封装的数据结构。

### 数字类型

Python 数字类型有 4 种： 整数类型、浮点类型、复数类型和布尔类型。需要注意的是，布尔类型也是数字类型，它事实上是整数类型的一种。 

#### 整数

与Java不同，Python不再区分short，int，long，统称为整型，用int表示，有二进制，八进制，十进制和十六进制。

#### 浮点数

Python中的浮点数只有float

#### 复数类型

复数在数学中是非常重要的概念，无论是在理论物理学，还是在电气工程实践中都经常使用。但是很多计算机语言都不支持复数，而 Python 是支持复数的，这使得 Python 能够很好地用来进行科学计算。 

Python 中复数类型为 complex，例如1+2j 表示的是实部为 1、虚部为 2 的复数。

#### 布尔类型

Python 中布尔类型为 boo， bool 是 int 的子类，它只有两个值： True 和 False 

任何类型数据都可以通过 boo（）函数转换为布尔值，那些被认为“没有的”“空的” 值会转换为 False，反之转换为 True。 如 None （空对象）、 False、 0、 0.0、 0j （复数）、 ""（空字符串）、 ［］ （空列表）、（）（空元组）和｛｝ （空字典）这些数值会转换为 False，否则是 True

#### 数字之间的转换

- 数字类型之间进行计算时会进行隐式转换

- 可以通过type()函数查看类型
- 也可以通过bool()，float()，int()函数进行显式转换

### 字符串类型

由字符组成的一串字符序列称为“字符串 ”， 字符串是有顺序的，从左到右，索引从 0 开始依次递增。 Python 中字符串类型是 str

#### 字符串表示方式

- 普通字符串：'demo'或"demo"
- 原始字符串：在普通字符串的前面加r，表示字符串里的特殊字符不需要转义
- 长字符串：包含换行缩进等固定格式的字符串，通过'''或者"""表示

```python
# 字符串表示

# 普通字符串
str1 = 'demo\tdemo'
print(str1)
str2 = "demo\tdemo"
print(str2)

# 原始字符串
str3 = r"demo\tdemo"
print(str3)

# 长字符串
str4 = """
    demo\tdemo
"""
print(str4)

结果：
demo	demo
demo	demo
demo\tdemo

    demo	demo

```

#### 字符串格式化输出

```python
# 字符串格式化输出
name = "lzx"
age = 22
res = "他的名字是{0}，年龄是{1}".format(name,age)
print(res)
res2 = "他的名字是{n}，年龄是{a}".format(n=name,a=age)
print(res2)

他的名字是lzx，年龄是22
他的名字是lzx，年龄是22

# 字符串格式化输出
name = "lzx"
age = 22
money = 2559.6
res = "他的名字是{0:s}，年龄是{1:d}，剩余金钱是{2:.3f}".format(name,age,money)
print(res)
res2 = "他的名字是{n:s}，年龄是{a:d}，剩余金钱是{m:f}".format(n=name,a=age,m=money)
print(res2)


他的名字是lzx，年龄是22，剩余金钱是2559.600
他的名字是lzx，年龄是22，剩余金钱是2559.600000
```

String的format函数可以格式化输出，通过下标或者占位符为对应位置赋值，同时可以指定数据类型

#### 字符串查找

字符串类（str）中提供了 find 和 rfind 方法用于查找子字符串 ，返回值是查找到的子字符串所在的位置，没有找到返回-1

- str.find(sub,start,end）：在索引 start 到 end 之间查找子字符串 sub，如果找到返回最左端位置的索引，如果没有找到返回-1 
- str.rfind(sub, start,end）：与 find 方法类似，区别是如果找到返回最右端位置的索引。

```python
# 字符串查找
str5 = "This is a demo a"
print(len(str5))
print(str5[10])
print(str5.find("a"))
print(str5.rfind("a"))
print(str5.find("a",0,10))
print(str5.rfind("a",0,10))


16
d
8
15
8
8
```

#### 字符串与数字相互转换

int(),float(),bool(),str()函数

```python
# 字符串和数字转换
str6 = "9.6"
print(float(str6))
print(type(float(str6)))
num = 12.6
print(str(num))
print(type(str(num)))


9.6
<class 'float'>
12.6
<class 'str'>
```

## Python中的运算符

#### 算数运算符

Python 中的算术运算符用来组织整型和浮点型数据的算术运算，按照参加运算的操作数的不同可以分为一元运算符和二元运算符。

- 一元运算符
  - -：取反
- 二元运算符
  - +
  - -
  - *
  - /
  - %
  - **：幂
  - //：除了之后取整

```python
# 算数运算符

# 取反运算符 ： -
a = 16
print(-a)
# +
b = 12
print(a + b)
# -
print(a - b)
# *
print(a * b)
# /
print(a/b)
# ** 幂
print(a**b)
# // 除取整
print(a//b)

-16
28
4
192
1.3333333333333333
281474976710656
1
```

#### 关系运算符

 关系运算是比较两个表达式大小关系的运算，它的结果是布尔类型数据， 即 True 或False，关系运算符有6种

- ==
- !=
- <
- \>
- <=
- \>=

```python
# 关系运算符  除了可以用来比较int外 数组 元组之类的也可以进行比较
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)

False
True
False
True
True
False
```

#### 逻辑运算符

逻辑运算符对布尔型变量进行运算，其结果也是布尔型

- and
- or
- not

```python
# 逻辑运算符  与Java一致 也可能造成短路现象
print(True and False)
print(True and True)
print(True or False)
print(True or True)
print(not True)

False
True
True
True
False
```

需要注意的时，与Java一致，Python里的and和or运算符也可能造成短路

#### 位运算符

位运算是以二进位（ bit）为单位进行运算的，操作数和结果都是整型数据

- ~：位反
- &：与
- |：或
- ^：异或
- \>\>：右移
- <<：左移

```python
# 位运算
c = 0b10110010
d = 0b01011110
print(~c)
print(c | d)
print(c & d)
print(c ^ d)
print(c >> 2)
print(c << 2)

-179
254
18
236
44
712
```

#### 赋值运算符

赋值运算符只是一种简写，一般用于变量自身的变化

- +=
- -=
- *=
- /=
- %=
- **=
- //=
- &=
- |=
- ^=
- \>\>=
- <<=

#### 其他运算符

除了前面介绍的主要运算符， Python 还有一些其他运算符

- 同一性测试运算符：测试是否是同一个对象（地址相同）
  - is
  - is not
- 成员测试运算符：测试一个集合中是否包含某个元素
  - in
  - not in

#### 运算符优先级

大致优先级为：

- 算数运算符
- 位运算符
- 关系运算符
- 逻辑运算符
- 赋值运算符

## Python控制语句

### 分支语句

- if
- if else
- if elif else

```python
# if
score = 95
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >=60:
    print("C")
else:
    print("D")
    
# 三元表达式
a = 9
res = a if a > 10 else 10
print(res)
```

### 循环语句

- while
- for

```python
# while
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# for
for num in range(0,10):
    print(num)
arr = [12,85,79,0,42,16]
for num in arr:
    print(num)
```

for类似于ava里的增强for循环，一遍用于遍历某个集合

### 跳转语句

- break：跳出循环
- continue：进入下一次循环
- while和for里的else：当循环全部结束之后执行一次

```python
# break
j = 0
while j <= 10:
    if j==3:
        break
    j += 1
    print(j)
print("----------------------------------------")

# continue
k = 0
while k <= 10:
    k += 1
    print(k)
    if k == 3:
        continue
print("----------------------------------------")

# while中的else
z = 0
while z <= 10:
    z += 1
else:
    print(z)
print("----------------------------------------")


# for中的else
for item in range(0,5):
    print(item)
else:
    print("xxx")
```

range函数：生成一个范围内的集合

```python
# range
for i in range(0,10,2):
    print(i)
print("----------------------------------------")
for i in range(10,-10,-2):
    print(i)
    
----------------------------------------
0
2
4
6
8
----------------------------------------
10
8
6
4
2
0
-2
-4
-6
-8
```

- 第一个参数：起始数
- 第二个参数：终止数
- 第三个参数：步长

# Python进阶

## 数据结构

Python里的数据结构类似于Java的util包里提供的一些容器，是对一些基本数据结构的封装，类似于List，Set，Map等

### 元组

在介绍元组之前，首先介绍一下序列的概念。

序列是一种可迭代的、元素有序的、可以重复出现的数据结构。序列可以通过索引访问元素。序列包括的结构有：列表，字符串，元组，范围（range）和字节序列（bytes）。序列可进行的操作有索引，分片，加和乘。

元组是一种序列结构，类似于Java中的List的概念，但是元组创建之后就不可变。

#### 创建元组

元组是一种不可变序列，一旦创建就不能修改。 创建元组可以使用 tuple(） 函数或者直接用逗号","将元素分隔。

```python
# 创建元祖
a = (12,5,6.12,True)
print(a)
b = tuple([12.9,54,-8,False])
print(b)

(12, 5, 6.12, True)
(12.9, 54, -8, False)
```

tuple()函数的参数是一个可迭代对象，例如列表等

```python
# 注意情况
c = (21)
print(type(c))
d = (21,)
print(type(d))
e = ()
print(type(e))

<class 'int'>
<class 'tuple'>
<class 'tuple'>
```

当创建元组只有一个元素时，末尾的","不能省略，否则会被识别为int类型

#### 访问元组

元组作为序列可 以通过下标索引访问其中的元素，也可以对其进行分片。 

```python
# 元组访问
arr = ("hello","world","Java",87,True)
print(arr[0])
print(arr[0:3])
print(arr[0:4:2])

hello
('hello', 'world', 'Java')
('hello', 'Java')
```

#### 元组拆包

Python支持将元组中的元素拆包，赋值给某些变量

```python
# 元组拆包
str1,str2,str3,num,t = arr
print(str1)
print(str2)
print(str3)
print(num)
print(t)
print("-------------------------------------")
str1,str2,*t = arr
print(str1)
print(str2)
print(t)
print("-------------------------------------")

-------------------------------------
hello
world
Java
87
True
-------------------------------------
hello
world
['Java', 87, True]
-------------------------------------
```

#### 遍历元组

一般用for循环遍历元组

```python
# 元组遍历
for item in arr:
    print(item)
# 遍历时同时获取索引
for i,item in enumerate(arr):
    print("{0}-------{1}".format(i,item))
```


### 列表

列表 (list) 也是一种序列结构，与元组不同 ，列表具有可变性，可 以追加、插入、删除和替换列表中的元素。

#### 列表创建

```python
# 列表
# 列表创建
list1 = [15,89,21.5,True,"dadas"]
print(list1)
print("-------------------------------------")
list2 = list(arr)
print(list2)
print("-------------------------------------")
```

#### 列表追加

```python
# 追加元素  追加单个元素用append方法  追加另一个列表用extend方法或者+
list1.append("demo")
print(list1)
print("-------------------------------------")
list1.extend(list2)
print(list1)
print("-------------------------------------")
print(list1 + list2)
print("-------------------------------------")
```

#### 插入元素

```python
# 插入元素  insert方法可以向指定位置插入一个元素
list3 = [15,89]
list3.insert(0,"demo")
print(list3)
```

#### 替换元素

```python
# 替换元素
list3[0] = "newDemo"
print(list3)
```

#### 删除元素

```python
# 删除元素 remove删除指定元素  pop弹出一个元素 返回该元素
list3.remove(15)
print(list3)
res = list3.pop()
print(res)
print(list3)
print("-------------------------------------")
list4 = [15,78,49,326,158]
list4.pop(3)
print(list4)
```

#### 其他常用方法

- reverse()：倒置列表
- copy()：复制列表
- clear()：清除列表所有元素
- index(x,i,j)：查找i和j范围内第一次出现的x的下标
- count(x)：返回x出现的次数

```python
# 其他常用方法
list5 = [0,15,94,0,84,32,0,1]
list5.reverse()  # 倒置列表
print(list5)
print("-------------------------------------")
list6 = list5.copy()
print(list6)
print("-------------------------------------")
index = list5.index(84)  # 查找84的索引
print(index)
number = list5.count(0)   # 统计0的个数
print(number)
list5.clear()  # 清空所有元素
print(list5)
```

#### 列表推导式

Python 中有一种特殊表达式一一推导式，它可以将一种数据结构作为输入，经过过滤、计算等处理， 最后输出另一种数据结构。根据数据结构的不同可分为列表推导式、集合推导式和字典推导式。

```python
# 列表推导式
# 获得 0～9 中偶数的平方数列
list7 = []
for i in range(0,10):
    if i % 2 == 0:
        list7.append(i ** 2)
print(list7)
print("--------------------------------------")
# 用列表表达式实现
list8 = []
list8 = [i ** 2 for i in range(0,10) if i % 2 == 0]
print(list8)
```

其中后面的代码就是列表推导式，输出的结果与 for 循环是一样的。如下图所示是列表推导式语法结构，其中 in 后面的表达式是“输入序列”； for 前面的表达式是“输出表达式”，它的运算结果会保存一个新列表中： if 条件语句用来过滤输入序列，符合条件的才传递给输出表达式，“条件语句”是可以省略的，所有元素都传递给输出表达式。

![image-20200127231125711](https://github.com/QingHuan-0526/Python-learning/blob/master/images/image-20200127231125711.png)

条件语句可以包含多个条件，例如找出 0～99 可以被 5 整除的偶数数列，实现代码如下。

```python
list9 = [i ** 2 for i in range(0,99) if i % 2 == 0 if i % 5 == 0]

```

### 集合

集合(set)是一种可迭代的、无序的、不能包含重复元素的数据结构。类似于Java中的Set。

集合又分为可变集合（set）和不可变集合（frozenset）。

#### 创建集合

```python
# 集合
# 创建可变集合  如果有重复元素会自动剔除
set1 = {15,"ads",True,89,15,True}
set2 = set(("dasd",515,12.6,False,515))
print(set1)
print("--------------------------------------")
print(set2)
print("--------------------------------------")
print(len(set2))   # 获取元素个数
set3 = {}   # 此种方式创建出来的是字典 要创建空集合 需要用set函数
print(type(set3))
set4 = set()
print(type(set4))

{89, True, 'ads', 15}
--------------------------------------
{False, 515, 12.6, 'dasd'}
--------------------------------------
4
<class 'dict'>
<class 'set'>
```

#### 修改集合

```python
# 修改可变集合
# 添加元素 如果已存在 则不能添加 不抛出异常
set4.add(True)
print(set4)
print("---------------------------------------")
set4.add(True)
print(set4)
print("---------------------------------------")
# 删除元素 若不存在则抛出错误
set4.remove(True)
print(set4)
print("----------------------------------------")
# set4.remove(True)
print("-------------------------------------")
# 删除元素 若不存在不会抛出异常
set4.discard(True)
print(set4)
print("------------------------------------------")
# 删除集合中随机一个元素 返回删除的值
set4.add(85)
set4.add(97)
set4.add("dada")
res = set4.pop()
print(res)
print(set4)
print("------------------------------------------")
# 清空集合元素
set4.clear()
print(set4)

{True}
---------------------------------------
{True}
---------------------------------------
set()
----------------------------------------
-------------------------------------
set()
------------------------------------------
97
{85, 'dada'}
------------------------------------------
set()
```

#### 遍历集合

集合是无序的，没有索引，不能通过下标访问单个元素。但可以遍历集合，访问集合每一 个元素

```python
# 遍历集合
for item in set2:
    print(item)
print("------------------------------------------")
for i,item in enumerate(set2):
    print("{0}--->{1}".format(i,item))
```

#### 不可变集合

不可变集合类型是 frozenset，创建不可变集合应使用 frozenset(）函数，不能使用大括号｛｝

```python
# 创建不可变集合
set5 = frozenset(("dada",True,False,True,5292,26.8))
print(set5)

frozenset({False, True, 5292, 'dada', 26.8})
```




#### 集合推导式

集合推导式与列表推导式类似， 区别只是输出结果是集合。

```python
# 集合推导式
set6 = {x ** 2 for x in range(100) if x % 2 == 0}
print(set6)
```



### 字典

字典（dieο 是可迭代的、可变的数据结构，通过键来访问元素。字典结构比较复杂，它是由两部分视图构成的， 一个是键（ key）视图，另一 个是值（value）视图 。键视图不能包含重复元素， 而值集合可以，键和值是成对出现的。 

字典类似于Java中的Map。

#### 创建字典

字典类型是 diet，创建字典可以使用 dict（）函数，或者用大括号｛｝将“键：值” 对括起来，“键：值”对之间用逗号分分隔。

```python
# 字典
# 创建字典
dict1 = {15:"zh",18:"qi",97.6:True}
print(dict1)
print("---------------------------------------")
dict2 = dict([(26,"dad"),(98,"dagg")])
print(dict2)
```

#### 修改字典

```python
# 修改字典
dict1[15] = "new"
print(dict1)
print("-------------------------------------")
del dict1[18]       # 删除指定key-value  不存在时抛出异常
print(dict1)
print("---------------------------------------")
value = dict1.pop(19,"default")    # 删除key-value 不存在时使用默认值
print(value)
item = dict1.popitem()   # 随机删除一组 返回删除的值
print(item)
```

#### 访问字典

```python
# 访问字典
# get方法 通过键返回值 不存在则返回默认值
dict3 = {15:"dwe",97:"dada",85:"gegr"}
print(dict3.get(15,"default"))
print(dict3.get(19,0))
print("------------------------------------")
# items方法 返回字典的所有键值对
print(dict3.items())
print("------------------------------------")
# keys 返回所有key
print(dict3.keys())
print("---------------------------------------")
# values 返回所有value
print(dict3.values())
print("-------------------------------------")
```

#### 遍历字典

```python
# 字典遍历
for key in dict3.keys():
    print(key)
print("-------------------------------------------")
for value in dict3.values():
    print(value)
print("-----------------------------------------")
for key,value in dict3.items():
    print("key:{0},value:{1}".format(key,value))
print("------------------------------------------")
```

#### 字典推导式

```python
# 字典推导式
res = {k:v for k,v in dict3.items() if k % 5 == 0}
print(res)
print("---------------------------------------")
res2 = {k for k,v in dict3.items() if v == "gegr"}
print(res2)
```

## 函数式编程







## 面向对象





## 异常处理





## 常用模块





## 正则表达式





## 文件操作





## 数据格式





## 数据库





## 网络编程





## wxPython图形化界面





## Python多线程





# Python框架







