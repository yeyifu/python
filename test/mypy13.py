#测试对象的浅拷贝，深拷贝
import copy
class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculater(self):
        print("你是什么东西")
        print("cpu对象：",self)

class Screen:
    def show(self):
        print("显示器")
        print("screen对象：", self)

#变量赋值
c1 = CPU()
c2 = c1
print(c1)
print(c2)

#浅复制
print("浅拷贝"+"#"*50)
s1 = Screen()
m1 = MobilePhone(c1,c2)
m2 = copy.copy(m1)
print(m1,m1.cpu,m1.screen)
print(m2,m2.cpu,m2.screen)

#深复制
print("深拷贝"+"#"*50)
m3 = copy.deepcopy(m1)
print(m1,m1.cpu,m1.screen)
print(m3,m3.cpu,m3.screen)