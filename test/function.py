#函数


a=4
#定义函数
def test01():
    '''函数定义'''
    print('a'*10)
    print(type(test01))
    print(id(test01))
    print(test01)

#打印函数文档字符串
#help(test01)


def add(a,b):
    print("{0}加{1}等于{2}".format(a,b,a+b))
    return(a+b)

print(add(1,4))


def test02(x,y,z):
    return [x*10,y*10,z*10]
print(test02(1,2,3))


def test03():
    a=''
    b=3

print(globals()) #打印全局变量
print("#"*10)
print(locals()) #打印局部变量
