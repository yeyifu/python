#方法重写
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_age(self):
        print("我的年龄是：{0}".format(self.age))

    def say_introduce(self):
        print("我的名字是：{0}".format(self.name))


class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age,)
        self.score = score

    def say_introduce(self):
        print("子类重写了父类方法")

s = Student('yeyifu',23,76) #实例化对象
s.say_age() #调用对象方法
s.say_introduce()

s1 = Person('yyf',24)
print(dir(s))
print(dir(s1))
