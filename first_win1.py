import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolTip
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI2022()


    def initUI2022(self):
        # QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('这是提示')#设置窗口提示
        self.setWindowTitle('第一个主窗口应用')#设置窗口标题
        self.setGeometry(300 , 300,250,250)#设置窗口位置和大小
        # self.show()
    # def showMessage(self):
    #     from PyQt5.QtWidgets import QMessageBox
    #     QMessageBox.information(QMainWindow,)

# if __name__=='__main__':
    # app = QApplication(sys.argv)
    # win = Window()
    # win.show()
    # sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # win12 = Window()
    # win12.show()
    # sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication
#
#
# class Window(QMainWindow):
#     def __init__(self):
#         super(Window, self).__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("第一个主窗口")
#         self.setGeometry(300, 300, 250, 250)

#
if __name__=='__main__':
    app = QApplication(sys.argv)#创建应用程序对象
    win = Window()
    win.setWindowFlag(Qt.WindowCloseButtonHint)#设置窗口关闭按钮
    win.show()
    sys.exit(app.exec_())