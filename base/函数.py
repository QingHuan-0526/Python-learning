from functools import reduce
# 函数定义


# 无返回值 参数
def first_function():
    print("This is my first function")


# 有返回值 参数
def second_function(width, height):
    area = width * height
    return area


# 参数设置默认值  python中没有Java的函数重载 不过可以通过默认值和可变参数的方式实现类似重载
def third_function(width=10, height=20):
    area = width * height
    return area


# 可变参数有两种*和**  *的参数作为元组传入  **参数作为字典传入
def four_function(*numbers, weight=1):
    total = 0.0
    for number in numbers:
        total += number
    return total * weight


# **可变参数
def fifth_function(**students):
    for key, value in students.items():
        print("{0}---->{1}".format(key, value))


# 函数调用
first_function()
# 默认调用
res = second_function(10, 22)
print(res)
# 关键字调用
res = second_function(width=10, height=22)
print(res)
res = third_function()
print(res)
res = third_function(15, 25)
print(res)
res = four_function(12, 15, 79, 52.6, 143.9, weight=2)
print(res)
fifth_function(name='lzx', age=21, sex=1)


# 生成器
# 获取一个平方数列
def square(number):
    list1 = []
    for i in range(number + 1):
        list1.append(i * i)
    return list1


for item in square(5):
    print(item, end=" ")


# 获取一个平方数列
def square2(number):
    for i in range(number + 1):
        yield i * i


for item in square2(5):
    print(item, end=" ")
print("----------------------------------")
res = square2(5)
print(res.__next__())
print(res.__next__())
print(res.__next__())


# 嵌套函数
def calculate(n1, n2, opr):
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    if opr == '+':
        return add(n1, n2)
    elif opr == '-':
        return sub(n1, n2)
    else:
        return 0


print(calculate(10, 15, '+'))


# 函数式编程
# 函数类型
def calculate(n1, n2, opr):
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    if opr == '+':
        return add
    elif opr == '-':
        return sub


f = calculate(10, 15, '+')
print(type(f))
print("10 + 5 = {0}".format(f(10, 5)))


# Lambda表达式
def calculate3(opr):
    if opr == '+':
        return lambda a, b: (a + b)
    elif opr == '-':
        return lambda a, b: (a - b)


f = calculate3('+')
print(type(f))
print("5 + 10 = {0}".format(f(5, 10)))


# filter
users = ['tony', 'Tom', 'Ben', 'Alex']
users_filter = filter(lambda u: u.startswith('A'), users)
print(type(users_filter))
print(list(users_filter))

# map
users = ['tony', 'Tom', 'Ben', 'Alex']
users_map = map(lambda u: u.lower(), users)
print(type(users_map))
print(list(users_map))

# reduce  对数列求和
a = (1, 2, 3, 4)
res = reduce(lambda acc, i: acc + i, a)
res = reduce(lambda acc, i: acc + i, a, 2)
print(res)
