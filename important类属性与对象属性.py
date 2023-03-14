import sys

from  PyQt5.Qt import *
##区别类属性与实例属性、类方法和实例方法
##【对比参考】上海 2018版 Python3.0培训 -基础班-面向对象-050-53章
class Tool(object):
    #定义类属性#
    num=0
    def __init__(self,av):
        #定义对象属性
        Tool.num+=1
        print('我是{}'.format(av))
        print('我是第{}种工具'.format(Tool.num))
        print('--'*10)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    hutou = Tool('老虎钳')
    qizi=Tool('起子')
    print('--'*10)
    print('总共有{}种工具'.format(Tool.num))
    print('--' * 10)
    print('总共有{}种工具'.format(qizi.num))#类属性可以用实例名调用,如果对象属性没有num属性，就会向上到类属性查找
    hutou.num=99#添加hutou对象的属性，初始值为99
    print('--' * 10)
    print(hutou.num)
    print(qizi.num)
    print(Tool.num)#类属性的值未跟着改
    sys.exit(app.exec_())