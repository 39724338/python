from PyQt5.QtWidgets import QDialog,QPushButton,QVBoxLayout
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication


class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.setWindowTitle('Dialog窗口')
        self.setGeometry(300,100,300,200)
        self.initUI()

    def initUI(self):
        closeBtn = QPushButton('点击关闭按钮关闭',self)


        closeBtn.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(closeBtn)

        self.setLayout(layout)
    def close(self,event) -> bool:#重写close方法
        print("关闭窗口")
        print(type(event))
        print(event)
        return super().close()
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:#重写closeEvent方法
        print("点击右上角关闭按钮关闭窗口")
        return super().closeEvent(a0)
if  __name__ == '__main__':

    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())