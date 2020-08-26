name_list = ['tom','lily','rose','lily']

# print(name_list.index('rose'))
# print(len(name_list))
# print(name_list.count('lily'))
# name = input('请输入你的名字：')
# print('你的名字已存在') if name in name_list else print('没找到你的名字')


# name_list.append('yyf');
# name_list.append(['12','34'])
# name_list.extend(['12','34'])
# name_list.insert(1,'dd')
# name_list.insert(1,['aa','bb'])
# del name_list
# del name_list[1]

# print(name_list.pop(2))
# print(name_list.pop())

# name_list.clear()
# print(name_list)


# list = [1, 2, 3, 6, 7, 0, 9]
# # list.reverse()
# list.sort(reverse=True)
# print(list)


# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1


# lists = [[1,2,3],[4,5,6],[7,8,9]]
# for list in lists:
#     for i in list:
#         print(i)
import random
teachers = ['A','B','C','D','E','F','G','H',]
offices = [[],[],[]]
for teacher in teachers:
    offices[random.randint(0,2)].append(teacher)

print(offices)



