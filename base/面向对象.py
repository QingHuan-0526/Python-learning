# 面向对象


# 定义类
# 定义一个继承自object的类 pass是占位符 不执行任何动作
class MyFirstClass(object):
    # 类体
    pass


# 创建对象
c1 = MyFirstClass()
print(c1)


class Animal(object):
    # 类变量
    is_alive = True

    # 构造方法 定义实例变量
    def __init__(self, age, sex=1):
        self.age = age
        self.sex = sex

    # 实例方法
    def grow(self):
        self.age += 1

    # 类方法
    @classmethod
    def kill(cls):
        cls.is_alive = False

    # 静态方法
    @staticmethod
    def run():
        print("The Animal is Runing!")


dog = Animal(2, 1)
# 通过对象.实例变量名调用实例变量
print("年龄是：{0}".format(dog.age))
# 通过类.类变量名调用类变量
print("是否存活：{0}".format(Animal.is_alive))
# 通过对象.类变量名调用类变量
print("是否存活：{0}".format(dog.is_alive))
# 查看实例的所有实例变量
print(dog.__dict__)
# 通过对象修改类变量
dog.is_alive = False
# 再次查看实例的所有实例变量  发现多了一个实例变量
print(dog.__dict__)
# 查看类变量 未修改
print(Animal.is_alive)
print(dog.age)
# 调用实例方法
dog.grow()
print(dog.age)
print(Animal.is_alive)
# 调用类方法
Animal.kill()
print(Animal.is_alive)
# 调用静态方法
Animal.run()


class Animal2(object):

    # 构造方法 定义实例变量
    def __init__(self, age, sex=1):
        # 私有变量
        self.__age = age
        self.sex = sex

    # 私有方法
    def __grow(self):
        # 私有变量可以类内部访问
        self.__age += 1


cat = Animal2(1)
print(cat.sex)


# print(cat.age)


class Animal3(object):

    # 构造方法 定义实例变量
    def __init__(self, age, sex=1):
        # 私有变量
        self.__age = age
        self.__sex = sex

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


a1 = Animal3(10, 0)
print(a1.get_age())
a1.set_age(16)
print(a1.get_age())


# 属性
class Animal4(object):

    # 构造方法 定义实例变量
    def __init__(self, age, sex=1):
        # 私有变量
        self.__age = age
        self.__sex = sex

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


a2 = Animal4(5, 1)
print(a2.age)
a2.age = 2
print(a2.age)


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("名字-》{0}，年龄-》{1}".format(self.name, self.age))


class Student(Person):

    def __init__(self, name, age, tel):
        super(Student, self).__init__(name, age)
        self.tel = tel

    def info(self):
        print("名字-》{0}，年龄-》{1}，电话-》{2}".format(self.name, self.age, self.tel))


stu1 = Student("lzx", 21, 17629154010)
