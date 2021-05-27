"""
1.模块的发布
    a.为什么要发布
        自定义模块，切换项目之后，不好用
        系统模块，切换到新的项目中，好用
    b.sys.path
        导入模块时，搜索路径列表
        如果所有路径中没有要导入的模块，会导致，无法导入目标模块
    解决方案：
        1.将模块所在路径，手动加入到sys.path中  #sys.path.append("G:\projects\python\module\package1")
        2.将自定义模块，发布到系统目录
            发布自定义模块的步骤：
                1.确定发布的模块(目录结构)
                |--setup.py
                |--package1
                    |--自定义模块 MyPath
                2.setup的编辑工作
                    setup()
                3.构建模块
                    python setup.py build
                4.发布模块
                    python setup.py sdist

2.模块的安装
    2.1 通过命令完成安装(推荐) 更安全
        a.找到之前发布的压缩包，解压操作
        b.python setup.py install
    2.2 暴力安装
        文件拷贝

"""

# import sys
# list1 = sys.path
# for i in list1:
#     print(i)

import MyMath
print(MyMath.add(6,12))