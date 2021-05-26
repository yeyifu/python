#继承
class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def say_age(self):
        print("我是Person父类")



class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age)  #调用父类构造函数
        self.score = score



stu = Student('yyf',23,67)
stu.say_age()
print(stu.score)
print(stu._Person__age) #调用父类私有属性