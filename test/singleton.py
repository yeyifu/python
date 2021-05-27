#单例模式

class MySingleton:
    __obj = None
    __init_flag = True
    def __new__(cls,*args,**kwargs): #重写__new__()方法
      if cls.__obj == None: #如果对象为NONE
          cls.__obj = object.__new__(cls) #创建对象

      return cls.__obj #返回对象

    def __init__(self,name):
      if MySingleton.__init_flag: #当已经执行初始化后不在执行初始化
        print("init...")
        self.name = name
        MySingleton.__init_flag = False

a = MySingleton("aa")
b = MySingleton("bb")
print(a)
print(b)
c = MySingleton("cc")
print(c)