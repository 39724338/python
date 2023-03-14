import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap


class Example(QMainWindow):
    """建造第一个邹伟的PyQt窗口控件
    注意父类是QWidget或者QMainWindow，界面的基本控件
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(450, 300)  #添加窗口大小
        self.move(100, 100)#窗口移动
        self.setWindowTitle('邹伟的第一个窗口')#窗口名字，也可以是sys.argv
        self.setWindowIcon(QIcon('favicon.ico'))
        self.a=QLabel(self)
        self.a.setText('防守打法')
        self.a.move(100, 200)
        self.b = QLabel(self)
        self.b.setText('fas')
        self.b.move(150, 150)
        self.setToolTip('这是气泡')
        self.c=QLineEdit(self)
        self.c.move(120, 100)
        self.c.setPlaceholderText('啊啊')
        button1=QPushButton(QIcon('favicon.ico'),'as',self)
        button1.move(30,50)
        print(QLabel(self))
        print(self.b)
        print(button1)
        self.show()     #让控件在桌面上显示出来
if __name__=='__main__':
    app=QApplication(sys.argv)
    print(app)
    print(sys.argv)
    ex=Example()
    print(ex.c)
    sys.exit(app.exec_())











