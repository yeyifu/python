#创建字典
# #1.初始化值
# ict1 = {'name':'yyf','age':23,'gender':'M'}
# print(type(dict1))
# #2.定义空字典
# dict2 = {}
# print(type(dict2))
# #3.函数声明
# dict3 = dict();
# print(type(dict3))

# dict = {'name':'yyf','age':23,'gender':'M'}
# dict['id'] = '00001'
# dict['name'] = 'yeyifu'
# del(dict['age']) #删除
# dict.clear() #清空


# #查找字典
# dict = {'name':'yyf','age':23,'gender':'M'}
# print(dict['name'])
# print(dict.get('name'))
# print(dict.get('names'))
# print(dict.get('names','yeyfiu')) #如果value存在则输出，否则输出none或默认值
# print(dict.keys())
# print(dict.values())
# print(dict.items())

# 遍历字典
dict = {'name':'yyf','age':23,'gender':'M'}
#遍历key
# for key in dict.keys():
#     print(key)

#遍历values
# for values in dict.values():
#     print(values)

#遍历key-value
# for items in dict.items():
#     print(items)

#遍历key-value，拆分
# for items in dict.items():
#     print(f'{items[0]}={items[1]}')

# for key,value in dict.items():
#     print(f'{key}={value}')