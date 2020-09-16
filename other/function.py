# 定义函数说明文档
def info_print():
    """函数说明文档"""
    print(1+2)
info_print()


# 查看函数文档
help(info_print)


# 一个函数返回多个值
def return_num():
    # return 1, 3 #返回的是元组(默认)
    # return(10,20) #返回的是元组
    # return[10,20]   #返回的是列表
    return {'name':'python','age':'30'} #返回的是字典
print(return_num())


#函数的参数
# 1.位置参数：传递和定义参数的顺序及个数必须一致
def user_info(name,age,add):
    print(f'我叫{name},今年{age}岁，来自{add}')
user_info('yyf',20,'china')