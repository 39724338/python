import sys

from  PyQt5.Qt import *
##区别类属性与实例属性、类方法和实例方法
##【对比参考】上海 2018版 Python3.0培训 -基础班-面向对象-050-53章
class Tool(object):
    #定义类属性#
    num=0
    @classmethod
    def tool_methon(cls):
        print('工具数量为{}'.format(cls.num))
        print('--' * 10)
    def __init__(self,name):
        #定义对象属性
        self.name=name
        Tool.num+=1
    def run(self):
        print('aa')
        pass


if __name__ == '__main__':
    app=QApplication(sys.argv)
    hutou = Tool('老虎钳')
    qizi=Tool('起子')
    Tool.tool_methon()


    sys.exit(app.exec_())