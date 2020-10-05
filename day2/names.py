import copy
#name = "ZhangYang Guyun Xiangpeng XuLiangChen"
name = ['ZhangYang','Guyun','Xiangpeng',['alex','jack'],'XuLiangChen']
print(name)
# print(name[0],name[1])
# print(name[1:3])    #结尾闭区间，切片
# print(name[-2])   #切片
# print(name[-3:-1]) #切片

# name.append('LeiHaidong')   #追加
# name.insert(1,'ChenRonghua')    #插入
# name[2] = 'XieDi'       #修改
# name.remove('ChenRonghua')  #删除
#del name[2]        #删除,可输入下标值，删除指定元素
# print(name.pop(2))      #删除，可输入下标值，删除指定元素。默认最后一个，有返回值。
# print(name)


# print(name.index('Guyun'))  #根据元素取出下标
# name.reverse()  #反转列表元素
# name.sort() #对元素进行排序
# name1 = [1,2,3]
# name.extend(name1)   #合并列表
# print(name)

# name2 = name.copy()
# name[1] = "顾云"
# name[3][0]='ALEX'
# print(name)
# print(name2)

# name2 = copy.deepcopy(name)     #引入copy模块，deepcopy(),深度copy,独立数据
# name[1] = '顾云'
# name[3][0] = 'ALEX'
# print(name)
# print(name2)

# print(name[::2])
# print(name[:])
#
# for i in range(0,10,2):
#     print(i)




