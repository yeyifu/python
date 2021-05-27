"""
自定义模块
    实现数学四则运算
    两个数的加减乘除
"""

def add(a,b):
    """
    加法运算
    :return:两个数的和
    """
    return a + b

def sub(a,b):
    """
    减法运算
    :return: 两个数的差
    """
    return a - b


def mul(a,b):
    """
    乘法运算
    :return: 两个数的乘积
    """
    return a*b

def div(a,b):
    """
    除法运算
    :return: 两个数的商
    """
    return a / b

if __name__ == '__main__':
    a = 10
    b = 2
    print("和：{}".format(add(a,b)))
    print("减：{}".format(sub(a,b)))
    print("乘：{}".format(mul(a,b)))
    print("除：{}".format(div(a,b)))
