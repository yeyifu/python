#私有属性
class Employee:

    __company = "百战程序员" #定义类属性

    def __init__(self,name,age):
        self.name = name
        self.__age = age        #私有属性

    def __work(self):   #私有方法
        print("好好工作")
        print("年龄：{0}".format(self.__age))
        print(Employee.__company)




e = Employee("yeyifu",'23')

print(e.name)
print(e._Employee__age)

e._Employee__work() #调用私有方法

print(e._Employee__company)

