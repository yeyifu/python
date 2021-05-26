#多态
class Man:
    pass


class Chinese(Man):
    def eat(self):
        print("筷子吃饭")

class English(Man):
    def eat(self):
        print("刀叉吃饭")

class Indian(Man):
    def eat(self):
        print("用手吃饭")


def manEat(m):
    if isinstance(m,Man):
        m.eat() #多态，一个方法调用，根据对象不同调用不同的方法
    else:
        print("不能吃饭")

manEat(Chinese())
manEat(English())
