import sys

from  PyQt5.Qt import *

class Btn(QPushButton):
    def hitButton(self, at):
        # print(at)
        # return True
        if at.x()>self.width()/2:
            return True
        else:
            return False

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('窗口')
        self.resize(500, 500)
        self.initUI()

    def initUI(self):
        # pass
        btn=Btn(self)
        btn.setText('按钮')
        btn.move(100,100)

        Menu = QMenu()
        btn.setMenu(Menu)
        zuijing=QMenu(Menu)
        zuijing.setTitle('最近打开')
        zuijing.addAction('发生')

        # xj = QAction('新建',Menu)
        # # xj.setText('新建1')
        # Menu.addAction(xj)
        Menu.addAction('打开')
        Menu.addSeparator()
        Menu.addAction('关闭')
        Menu.addMenu(zuijing)
    # btn.pressed.connect(lambda :print('按钮被点击了'))




if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Win()

    win.show()

    sys.exit(app.exec_())