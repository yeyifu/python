import copy

a = [1,2,3,4,['a','b']]
b = copy.copy(a)
print("a:",a)
print("b:",b)

b.append(30)
b[4].append(7)
print("浅拷贝.....")
print("a:",a)
print("b:",b)

a = [1,2,3,4,['a','b']]
b = copy.deepcopy(a)
print("a:",a)
print("b:",b)

b.append(30)
b[4].append(7)
print("深拷贝.....")
print("a:",a)
print("b:",b)