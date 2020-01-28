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

# 字符串格式化输出
name = "lzx"
age = 22
money = 2559.6
res = "他的名字是{0:s}，年龄是{1:d}，剩余金钱是{2:.3f}".format(name,age,money)
print(res)
res2 = "他的名字是{n:s}，年龄是{a:d}，剩余金钱是{m:f}".format(n=name,a=age,m=money)
print(res2)


# 字符串查找
str5 = "This is a demo a"
print(len(str5))
print(str5[10])
print(str5.find("a"))
print(str5.rfind("a"))
print(str5.find("a",0,10))
print(str5.rfind("a",0,10))

# 字符串和数字转换
str6 = "9.6"
print(float(str6))
print(type(float(str6)))
num = 12.6
print(str(num))
print(type(str(num)))
