# 元组
# 创建元祖
a = (12,5,6.12,True)
print(a)
b = tuple([12.9,54,-8,False])
print(b)
print("-------------------------------------")


# 注意情况
c = (21)
print(type(c))
d = (21,)
print(type(d))
e = ()
print(type(e))
print("-------------------------------------")


# 元组访问
arr = ("hello","world","Java",87,True)
print(arr[0])
print(arr[0:3])
print(arr[0:4:2])
print("-------------------------------------")

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

# 元组遍历
for item in arr:
    print(item)

# 遍历时同时获取索引
for i,item in enumerate(arr):
    print("{0}-------{1}".format(i,item))
print("-------------------------------------")


# 列表
# 列表创建
list1 = [15,89,21.5,True,"dadas"]
print(list1)
print("-------------------------------------")
list2 = list(arr)
print(list2)
print("-------------------------------------")

# 追加元素  追加单个元素用append方法  追加另一个列表用extend方法或者+
list1.append("demo")
print(list1)
print("-------------------------------------")
list1.extend(list2)
print(list1)
print("-------------------------------------")
print(list1 + list2)
print("-------------------------------------")

# 插入元素  insert方法可以向指定位置插入一个元素
list3 = [15,89]
list3.insert(0,"demo")
print(list3)

# 替换元素
list3[0] = "newDemo"
print(list3)

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
print("-------------------------------------")

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
print("--------------------------------------")


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
print("--------------------------------------")
list9 = [i ** 2 for i in range(0,99) if i % 2 == 0 if i % 5 == 0]
print(list9)
print("--------------------------------------")


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
print("------------------------------------------")

# 遍历集合
for item in set2:
    print(item)
print("------------------------------------------")
for i,item in enumerate(set2):
    print("{0}--->{1}".format(i,item))
print("-------------------------------------------")

# 创建不可变集合
set5 = frozenset(("dada",True,False,True,5292,26.8))
print(set5)
print("--------------------------------------")

# 集合推导式
set6 = {x ** 2 for x in range(100) if x % 2 == 0}
print(set6)

# 字典
# 创建字典
dict1 = {15:"zh",18:"qi",97.6:True}
print(dict1)
print("---------------------------------------")
dict2 = dict([(26,"dad"),(98,"dagg")])
print(dict2)
print("------------------------------------")

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
print("-------------------------------")


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

# 字典推导式
res = {k:v for k,v in dict3.items() if k % 5 == 0}
print(res)
print("---------------------------------------")
res2 = {k for k,v in dict3.items() if v == "gegr"}
print(res2)


