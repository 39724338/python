from PyQt5.QtWidgets import QDialog, QPushButton,QApplication,\
    QMessageBox,QHBoxLayout,QLabel,QVBoxLayout,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from dialog0 import MyDialog0
import sys

class MyDialog(QDialog):#继承QDialog类
    def __init__(self):
        super(MyDialog, self).__init__()
        self.loginUI()

    def loginUI(self):
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowTitle("登录界面")
        self.resize(400, 200)

        #设置提示信息
        self.qlabel0=QLabel("信息查询系统",self)
        self.qlabel0.setFont(QFont("Roman times", 15, QFont.Bold))
        self.qlayout0=QHBoxLayout()
        self.qlayout0.addWidget(self.qlabel0)#
        self.qlayout0.setAlignment(Qt.AlignCenter)#设置居中

        #设置用户名
        self.qlabel1=QLabel("用户名",self)
        self.qlabel1.setFont(QFont("Roman times", 10, QFont.Bold))
        self.qlineedit1=QLineEdit(self)
        self.qlineedit1.setPlaceholderText("请输入用户名")
        # self.qlineedit1.setEchoMode(QLineEdit.Password)
        self.qloyout1=QHBoxLayout()
        self.qloyout1.addWidget(self.qlabel1)
        self.qloyout1.addWidget(self.qlineedit1)

        #设置密码
        self.qlabel2 = QLabel("密码", self)
        self.qlabel2.setFont(QFont("Roman times", 10, QFont.Bold))
        self.qlineedit2 = QLineEdit(self)
        self.qlineedit2.setPlaceholderText("请输入密码")
        self.qlineedit2.setEchoMode(QLineEdit.Password)
        self.qloyout2 = QHBoxLayout()
        self.qloyout2.addWidget(self.qlabel2)
        self.qloyout2.addWidget(self.qlineedit2)


        #设置登录按钮
        self.button1 = QPushButton("登录", self)
        self.button2 = QPushButton("退出", self)
        self.QHBoxLayout1=QHBoxLayout()#纵向布局

        self.QHBoxLayout1.addWidget(self.button1)
        # self.QHBoxLayout1.addStretch(0.2)#间隔调节
        # self.QHBoxLayout1.setSpacing(50)
        self.QHBoxLayout1.addWidget(self.button2)
        self.QHBoxLayout1.setAlignment(Qt.AlignCenter)

        self.qvlayout=QVBoxLayout()
        self.qvlayout.addLayout(self.qlayout0)
        self.qvlayout.addLayout(self.qloyout1)
        self.qvlayout.addLayout(self.qloyout2)
        self.qvlayout.addLayout(self.QHBoxLayout1)
        self.qvlayout.setAlignment(Qt.AlignCenter)
        self.qvlayout.setSpacing(50)

        self.setLayout(self.qvlayout)

        self.button1.clicked.connect(self.login)
        self.button2.clicked.connect(self.close)
    def login(self):
        if  self.qlineedit1.text()=='admin' or self.qlineedit2.text()=='123123':
            qm = QMessageBox.information(self, '注册成功', '欢迎您，%s' % self.qlineedit1.text(), QMessageBox.Yes)
            print("登录成功")
            qdialog0 = MyDialog0()
            qdialog0.exec_()#弹出框
            self.close()
        else:
            qm = QMessageBox.warning(self, '错误', '用户名或密码错误', QMessageBox.Yes)
            print("登录失败")
            self.qlineedit1.clear()#清空输入框
            self.qlineedit2.clear()
            self.qlineedit1.setFocus()
            self.qlineedit2.setFocus()#设置焦点

    def ingnore(self):
        self.qlineedit1.clear()
        self.qlineedit2.clear()
        print("清空输入框")
    def close(self) -> bool:#重写关闭事件
        reply = QMessageBox.question(self, '确认对话框', '是否退出登录界面', QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.accept()#点击登录按钮后，调用accept方法，关闭对话框
            print("点击退出按钮退出")

        else:
            self.ingnore()#返回到登录界面

    def closeEvent(self,a0: 'QCloseEvent'):
        print("点击右上角叉叉退出")
        return super().closeEvent(a0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())

