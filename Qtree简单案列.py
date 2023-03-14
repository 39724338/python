# class Demo():
#
#     def fun1(self):
#         pass
#
#     @classmethod
#     def fun2(cls):
#         pass
#
#     @staticmethod
#     def fun3(self):
#         pass
#
#
# demo = Demo()
# print(demo)
# print(demo.fun1)
# print(demo.fun2)
# print(demo.fun3)
# class A:
#
#     def __init__(self):
#         print("Enter A")
#
#         print("Leave A")
#
#
# class B(A):
#
#     def __init__(self):
#         print("Enter B")
#
#         A.__init__(self)
#
#         print("Leave B")
#
#
# class C(A):
#
#     def __init__(self):
#         print("Enter C")
#
#         A.__init__(self)
#
#         print("Leave C")
#
#
# class D(A):
#
#     def __init__(self):
#         print("Enter D")
#
#         A.__init__(self)
#
#         print("Leave D")
#
#
# class E(B, C, D):
#
#     def __init__(self):
#         print("Enter E")
#
#         B.__init__(self)
#
#         C.__init__(self)
#
#         D.__init__(self)
#
#         print("Leave E")
#
#
# a=E()
# class A:
#
#     def __init__(self):
#         print("Enter A")
#
#         print("Leave A")
#
#
# class B(A):
#
#     def __init__(self):
#         print("Enter B")
#
#         super(B, self).__init__()
#
#         print("Leave B")
#
#
# class C(A):
#
#     def __init__(self):
#         print("Enter C")
#
#         super(C, self).__init__()
#
#         print("Leave C")
#
#
# class D(A):
#
#     def __init__(self):
#         print("Enter D")
#
#         super(D, self).__init__()
#
#         print("Leave D")
#
#
# class E(B, C, D):
#
#     def __init__(self):
#         print("Enter E")
#
#         super(E, self).__init__()
#
#         print("Leave E")
#
#
#
# B1=B()
# # print(super(B))
# class A:
#     def __init__(self):
#         print('A')
#
#
# class B(A):
#     def m(self):
#         print('B')
#         super().__init__()
#
#
#
# aa=B().m()
# print(B())
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication,QLabel
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
import sys, random

# class Tetris(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         '''initiates application UI'''
#         self.tboard = QLabel(self)
#         self.tboard.move(20, 50)
#         self.setCentralWidget(self.tboard)
#         self.statusbar = self.statusBar()
#
#         self.show()
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Tetris()
#     sys.exit(app.exec_())
# from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
# from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
# from PyQt5.QtGui import QPainter, QColor
# import sys, random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class TreeWidgetDemo(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('TreeWidget 例子')

        self.tree = QTreeWidget()
        # 设置列数
        self.tree.setColumnCount(3)
        # 设置树形控件头部的标题
        self.tree.setHeaderLabels(['Key', 'Value','Number'])
    #
    #     # 设置根节点
        root = QTreeWidgetItem(self.tree)
        print(root)
        root.setText(0, 'Root1')

        root.setIcon(0, QIcon('./images/root.png'))
    #
    #     # todo 优化2 设置根节点的背景颜色
        brush_red = QBrush(Qt.green)
        root.setBackground(0, brush_red)
        brush_blue = QBrush(Qt.blue)
        root.setBackground(1, brush_blue)
    #
        # 设置树形控件的列的宽度
        self.tree.setColumnWidth(0, 150)
    #
    #     # 设置子节点1
        child1 = QTreeWidgetItem()
        child1.setText(0, 'child1')
        child1.setText(1, 'ios')
        child1.setIcon(0, QIcon('./images/IOS.png'))
    #
    #     # todo 优化1 设置节点的状态
        child1.setCheckState(0, Qt.Checked)

        root.addChild(child1)
    #
    #     # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '')
        child2.setIcon(0, QIcon('./images/android.png'))

        # 设置子节点3
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, 'android')
        child3.setIcon(0, QIcon('./images/music.png'))
    #
    #     # 加载根节点的所有属性与子控件
        self.tree.addTopLevelItem(root)
    #
    #     # TODO 优化3 给节点添加响应事件
        self.tree.clicked.connect(self.onClicked)
    #
    #     # 节点全部展开
        self.tree.expandAll()
        self.setCentralWidget(self.tree)
    #
    def onClicked(self, qmodeLindex):
        item = self.tree.currentItem()
        print('Key=%s,value=%s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec_())
# def demo(obj):
#     print('原值:',obj)
#     obj+=obj
#
# print("="*10,'值传递','='*10)
# list1=['唯有在被追赶时，才能真正地奔跑','\t',"你知道吗\n","这就是实际情况"]
# print('函数调用前:',list1)
# demo(list1)
# print('函数调用后:',list1)
