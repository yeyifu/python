#super()，代表父类的定义，而不是父类对象
class A:
    def say(self):
        print("A：",self)

class B(A):
    def say(self):
        #A.say(self)
        super().say()   #调用父类say()方法
        print("B：",self)

B().say()