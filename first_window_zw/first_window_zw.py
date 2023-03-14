import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
class Example(QWidget):
    """建造第一个邹伟的PyQt窗口控件
    注意父类是QWidget，界面的基本控件
    """
    def __init__(self):
        super().__init__()
        self.initUI
    def initUI(self):
        self.resize(450,300)#添加窗口大小
        self.move(100,100)#窗口移动
        self.setWindowTitle('邹伟的第一个窗口')#窗口名字，也可以是sys.argv
        self.setWindowIcon(QIcon('favicon.ico'))
        self.show()     #让控件在桌面上显示出来
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())










