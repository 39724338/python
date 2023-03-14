import os,sys,PyQt5
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication,QMessageBox,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget,QDialog
from dialog0 import Dialog10

class Login0(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUI()#初始化界面
         



    def setupUI(self):
        self.setWindowTitle("登录")#
        self.resize(300,200)
        self.move(500,500)
        self.label=QLabel()
        self.label.setText("欢迎登录")
        self.label.setFont(QFont("Roman times", 20, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFrameStyle(QFrame.Box|QFrame.Raised)
        self.label1=QLabel()
        self.label1.setText("用户名")
        self.label1.setFont(QFont("Roman times", 10, QFont.Bold))
        self.lineEdit1=QLineEdit()
        self.lineEdit1.setPlaceholderText("请输入用户名")
        self.lineEdit1.setEchoMode(QLineEdit.Password)
        self.lineEdit1.setMaxLength(10)
        self.lineEdit1.setClearButtonEnabled(True)
        self.qvbox1=QVBoxLayout()
        self.qvbox1.addWidget(self.label)
        self.qvbox1.addWidget(self.label1)
        self.qvbox1.addWidget(self.lineEdit1)
        self.qvbox1.addStretch(1)
        self.qvbox1.setSpacing(10)
        self.qpb1=QPushButton("登录")
        self.qpb2=QPushButton("退出")
        self.qvbox1.addWidget(self.qpb1)
        self.qvbox1.addWidget(self.qpb2)
        self.setLayout(self.qvbox1)
        self.qpb1.clicked.connect(self.login0)

    @pyqtSlot()
    def login0(self):
        print("登录")

        QDialog00 = Dialog10()#创建一个对话框
        QDialog00.exec_()#弹出对话框





        #QDialog00.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)#创建一个应用程序对象
    login0 = Login0()
    login0.show()
    sys.exit(app.exec_())
