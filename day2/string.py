name = 'my name is yeyifu'
print(name.capitalize())    #首字母大写
print(name.count('y'))  #统计y的个数
print(name.center(50,'-'))
print(name.endswith('fu'))  #判断以'fu'结尾是否为真
print(name[name.find('name'):]) #切片
print('+'.join(['1','2','3']))
print(name.strip()) #去掉空格和换行
print(name.replace('y','Y',1))  #替换字符串，默认全局，第3个参数指定替换个数
print(name.split()) #默认按照空格转换从列表

