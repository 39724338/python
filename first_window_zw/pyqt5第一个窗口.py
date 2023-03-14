import sys      #标准库system
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
import random
class Example(QWidget):
    '''
    QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。
    '''
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # self.resize(450,350) #窗口宽450px，高350px
        # self.move(300, 300)  #把控件放置到屏幕坐标的(300, 300)的位置;注：屏幕坐标系的原点是屏幕的左上角。
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle(sys.argv[0])  #窗口添加了一个标题  sys.argv[0]
        self.setWindowIcon(QIcon('bitbug.ico'))
        '''
        添加了窗口图标
        需要导入from PyQt5.QtGui import QIcon
        需要通用格式的图片，例如png，ico等
        QIcon识别图片
        '''
        self.show() #让控件在桌面上显示出来

if __name__ == '__main__':
    '''
    if __name__ == '__main__':的两种使用功能：
    情况1、直接执行本py代码文件时，把包含的代码块视为脚本代码顺序执行
    情况2、当本py代码文件作为其他代码import对象时，不执行如下被包含的代码块
    '''
    app = QApplication(sys.argv)
    '''
    QApplication管理GUI程序的控制流和主要设置,
    sys.argv是一个从程序外部获取参数的桥梁
    '''
    ex = Example()
    sys.exit(app.exec_())
