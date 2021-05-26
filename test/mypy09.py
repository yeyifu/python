#mro()方法解析顺序
class A:
    def aa(self):
        print("aa")

class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBB")

class C(B,A):
    def cc(self):
        print("cc")


c = C()
c.cc()
c.bb()
c.aa()
print(C.mro())  #打印类的层次结构
c.say()