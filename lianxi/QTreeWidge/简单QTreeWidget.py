from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,\
     QPushButton, QHBoxLayout,QToolBox,QTreeWidgetItem

import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题与初始大小
        self.setWindowTitle('QTreewidget Demo')
        self.resize(400, 300)

        # 创建QTreewidget，并设置列数和表头标签
        self.treeWidget = QTreeWidget(self)#QTreeWidget是一个树形结构
        self.treeWidget.setColumnCount(2)#设置列数
        self.treeWidget.setHeaderLabels(['Key', 'Value',"asf"])#设置表头标签

        # 添加根节点,类似EAS项目中的根节点
        # root = QTreeWidgetItem(self.treeWidget)#QTreeWidgetItem是一个分支
        # root.setText(0, 'Root')#设置根节点的文本
        # root.setText(1, '0')##  设置根节点的文本
        # root.setExpanded(True)#设置根节点展开
        # # root.setFlags(root.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)#设置根节点的标志
        # root.treeWidget()#设置根节点的树形结构
        # 添加子节点及孙子节点
        child1 = QTreeWidgetItem(self.treeWidget)
        child1.setText(0, 'Child 1')
        child1.setText(1, '1')
        child1.setText(2, '的')
        #
        grandchild1 = QTreeWidgetItem(child1)
        grandchild1.setText(0, 'Grandchild 1.1')
        grandchild1.setText(1, '2')
        #
        grandchild2 = QTreeWidgetItem(child1)
        grandchild2.setText(0, 'Grandchild 1.2')
        grandchild2.setText(1, '3')
        #
        child2 = QTreeWidgetItem(self.treeWidget)
        child2.setText(0, 'Child 2')
        child2.setText(1, '4')
        #
        grandchild3 = QTreeWidgetItem(child2)#孙子节点
        grandchild3.setText(0, 'Grandchild 2.1')
        grandchild3.setText(1, '5')
        qpushbutton1 = QPushButton('选好了')
        qpushbutton2=QPushButton('取消')
        QHBoxLayout1=QHBoxLayout()
        QHBoxLayout1.addWidget(qpushbutton1)
        QHBoxLayout1.addWidget(qpushbutton2)

    #     qpushbutton.clicked.connect(lambda: self.get_checked(self.treeWidget))#绑定槽函数
    # def get_checked(self, node: QTreeWidgetItem) -> list:
    #     """ 得到当前节点选中的所有分支， 返回一个 list """
    #     temp_list = []
    #     # 此处看下方注释 1
    #     for item in node.takeChildren():
    #         # 判断是否选中
    #         if item.checkState(0) == Qt.Checked:
    #             temp_list.append(item.text(0))
    #             # 判断是否还有子分支
    #             if item.childCount():
    #                 temp_list.extend(self.get_checked(item))
    #         node.addChild(item)
        # 创建垂直布局
        qvboxlayout2=QVBoxLayout()
        qvboxlayout2.addWidget(self.treeWidget)
        layout = QVBoxLayout(self)
        layout.addLayout(qvboxlayout2)
        layout.addLayout(QHBoxLayout1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())