import sys
from PyQt5.QtWidgets import QWidget,QTreeWidget,QApplication,QLabel,QCheckBox,QPushButton
from PyQt5.QtGui import QIcon,QFont
import random

class Game(QWidget):
    def __init__(self):
        super(Game, self).__init__()
        self.ds = None
        self.initUI()
    def initUI(self):
        self.result=QLabel(self)
        self.setGeometry(300, 300, 590, 550)
        self.setWindowTitle('剪刀石头布')
        self.result.setText("结局一篇空白")
        self.result.setFont(QFont('microsoft Yahei', 20))
        self.result.move(200,200)
        self.ds = QLabel(self)
        self.ds.setText("我是标签")
        self.ds.move(100, 100)
        self.ds.setWindowIcon(QIcon("favicon.ico"))


        btn1=QPushButton("石头",self)
        btn1.move(50,50)
        print(id(btn1))
        btn2 = QPushButton("剪刀", self)
        btn2.move(200, 50)
        btn3 = QPushButton("布", self)
        btn3.setObjectName("g")
        btn3.move(350, 50)

        btn1.clicked.connect(self.pusheds)
        btn2.clicked.connect(self.pusheds)
        btn3.clicked.connect(self.pusheds)
        print(btn3.receivers(btn3.objectNameChanged))
        btn3.setObjectName("湖")
        self.show()
    def pusheds(self):
        ls=["石头","剪刀","布"]
        # print(id(self.sender()),"被按下了")
        print(self.sender().text(), "是您的选择")
        a=random.choice(ls)
        print("而电脑选择的是",a)

        if a=="石头":
            if self.sender().text()=="石头":
                self.result.setText("平局")
            elif self.sender().text() == "剪刀":
                self.result.setText("你输了")
            else:
                self.result.setText("你赢了")
        if a=="剪刀":
            if self.sender().text()=="石头":
                self.result.setText("你赢了")
            elif self.sender().text() == "剪刀":
                self.result.setText("平局")
            else:
                self.result.setText("你输了")
        if a=="布":
            if self.sender().text()=="石头":
                self.result.setText("你输了")
            elif self.sender().text() == "剪刀":
                self.result.setText("你赢了")
            else:
                self.result.setText("你赢了")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    # ds=QLabel(ex)
    # ds.setText("我是标签")
    # ds.move(500,600)
    # # ds.setWindowIcon(QIcon("favicon.ico"))
    def cao(d):
        print("标题改变了")
        ex.windowTitleChanged.disconnect()
        ex.setWindowTitle("fsd"+d)



    ex.windowTitleChanged.connect(cao)
    ex.setWindowTitle("gd")

    ex.show()


    sys.exit(app.exec_())