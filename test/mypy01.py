'''
a = "我叫{0},今年{1}岁"
print(a.format('yyf','23'))
print("{:*^10}".format('123'))
'''


# a = input("请输入一个数：")
# if int(a) < 10:
#     print("{0}<10".format(a))
# else:
#     print("{0}>10".format(a))


'''
a = input("输入一个数字：")
print("小于10") if int(a) < 10 else print("数字大于10")
'''


# score = int(input("请输入你的考试分数："))
# if score<0 or score >100:
#     print("请输入0-100的数字")
# else:
#     if score > 90:
#         print('优秀')
#     elif score > 80:
#         print("良好")
#     elif score > 70:
#         print('较好')
#     elif score > 60:
#         print('及格')
#     else:
#         print('不及格')

'''
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
    print("{0}==>{1}".format(i-1,sum))
'''

'''
a = {"a":'1','b':'2','c':'3','d':'4'}
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
'''


'''
for i in range(1,10):
    for j in range(1,i+1):
            print("{0}x{1}={2}".format(i,j,(i*j)),end='\t')
    print()
'''


'''
info = [{"name：":"高小一","年龄：":"18","薪资：":"30000","城市：":"北京"},{"name：":"高小二","年龄：":"19","薪资：":"20000","城市：":"上海"},{"name：":"高小三","年龄：":"20","薪资：":"10000","城市：":"深圳"}]
for i in info:
    if int(i.get("薪资：")) > 20000:
        print(i)
'''












