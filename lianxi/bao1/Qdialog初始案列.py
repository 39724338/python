from PyQt5.QtWidgets import QDialog, QPushButton,QApplication,QMessageBox
from PyQt5.QtCore import Qt
import sys

class MyDialog(QDialog):#继承QDialog类
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(200, 100)

        self.setWindowTitle("My Dialog")
        self.button = QPushButton("登录", self)
        # self.show()
        # self.button.clicked.connect(self.accept)#点击登录按钮后，调用accept方法，关闭对话框
        self.button.clicked.connect(self.on_click)
    def on_click(self,event):
        reply = QMessageBox.question(self, "提示", "登录成功", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)#弹出登录成功提示框
        if reply == QMessageBox.Yes:
            print("登录成功")
            print(event)
            self.accept()#点击登录按钮后，调用accept方法，关闭对话框
        else:
            print("登录失败")
            print(event)
            self.close()#点击登录按钮后，调用accept方法，关闭对话框
            # event.reject()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())

