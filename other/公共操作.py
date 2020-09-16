str1 = 'aa'
str2 = 'bb'

list1 = [1,2]
list2 = [10,20]

tuple1 = (1,2)
tuple2 = (10,20)

dict1 = {'name':'python'}
dict2 = {'age':30}

# +:合并 ,支持字符串，列表，元祖
# print(str1+str2)
# print(list1+list2)
# print(tuple1+tuple2)

# *:复制 ,支持字符串，列表，元祖
# print(str1*3)
# print(list1*3)
# print(tuple1*3)

# in:元素是否存在 ,支持字符串，列表，元祖，字典
# print('a' in str1)
# print(1 in list1)
# print(1 in tuple1)
# print('address' not in dict1)

#len() 计算容器中元素个数
#del() 删除
#max()返回容器中元素最大值
#min()返回容器中元素最小值
#range(start,end,step) 生成从start到end的数字，步长为step，供for循环使用
# enumerate(可遍历对象,start=1) start参数用来设置遍历数据的下标起始值，默认为0
# list = ['a', 'b', 'c', 'd']
# for i in enumerate(list,start=1):
#     print(i)


#容器类型转换
# list3 = [10,20,30,20,40,50]
# set3 = {2,4,5,7,4,0}
# tuple3 = ('a','b','c','d')
# #tuple()：转换成元祖
# print(tuple(list3))
# print(tuple(set3))
# #list()：转换成列表
# print(list(set3))
# print(list(tuple3))
# #set()：转换成集合
# print(set(list3))
# print(set(tuple3))

#----------
#for循环实现
# mylist = []
# for i in range(10):
#     mylist.append(i)
# print(mylist)

#列表推导式实现
#print([i for i in range(10)])


# print([i for i in range(10) if i%2==0])

# print([(i,j) for i in range(1,3) for j in range(3)])

#字典推导式
# dict3 = dict()
# for i in range(1,6):
#     dict3[i] = i**2
# print(dict3)
#
# print({i:i**2 for i in range(1,6)})

list4 = ['name','age','gender']
list5 = ['tom','32','M']

# dict4 = dict()
# i=0
# while i< 3:
#     dict4[list4[i]] = list5[i]
#     i += 1
# print(dict4)

# print({list4[i]:list5[i] for i in range(len(list4))})

#提取字典中目标数据
# counts = {'MBP': 268,'HP': 201,'Lenovo': 199,'acer': 99}
# # 获取值大于200的键值
# print({key:value for key,value in counts.items() if value >=200})


# 集合推导式,集合能去重
list1 = [1,1,2]
set1={i ** 2 for i in list1}
print(set1)
