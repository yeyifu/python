# import sys
# print(sys.argv)
# num1 = 1
# num2 = 1.1
# print(type(num2))
# name = 'tom'
# age = 18
# weight = 55.5
# stu_id = 2
# print('我叫%s,学号是%.10d,今年%d岁,体重%.2f' % (name, stu_id, age, weight))
# print(f'我叫{name},学号是{stu_id}')
# print('hello\nworld')
# print('hello\tworld')

# print('hello', end='\t')
# print('world')

#输入
# str = input('请输入字符:')
# print(str)

#数据转换
# str = input(f'请输入：')
# print(type(str))
# num = int(str)
# print(type(num))
# print(float(str, 2))

#eval()
# str1 = '4'
# print(type(eval(str1)))

# str = input('请输入年龄：')
# if int(str) < 18:
#     print('童工')
# elif 18 <= int(str) <= 60:
#     print('合法')
# else:
#     print('年龄过大')

# import random
# print(random.randint(1,3))

# i=1
# while i<10:
#     print(i)
#     i = i+1


# str = '01234545678'
# print(str[1:8:2])
# print(str[-1:1:-1])
# print(str.find('34'))
# print(str.count('45',4,10))
# print(str.find('45'))
# print(str.count('45'))



str = '  hello World and itcast and itheima and pythoN'
str3 = 'df34d6f'
num='123456'
# print(str.replace('and','he'))
# print(str.split('and',3))

str1 = ['hello world ', ' itcast ', ' itheima ', ' python']
str2 = ''.join(str1)
# print(str2)
# print(''.join(str1).replace(' ',''))
# print(str.capitalize())
# print(str.title())
# print(str.lower())
# print(str.strip())
# # str.ljust()
# # str.rjust()
# # str.center()
#
# print(str.startswith(''))
# print(str.endswith('n'))
# print(str.isalpha())
# print(num.isdigit())
print(str3.isalnum())
