#传递不可变对象时，不可变对象里面包含的子对象是可变的，则方法内修改了这个可变对象，源对象也发生变化
a = (10,20,[5,6])
#print("a:",id(a))

def test01(m):
    print("m:",id(m))
    m[2][0] = 88
    print(m)
    print("m:",id(m))

test01(a)
print(a)


#eval()函数
eval("print('hello world')")