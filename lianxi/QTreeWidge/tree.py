import sys
from PyQt5.QtWidgets import QTreeWidgetItem, QTreeWidget, QWidget, QVBoxLayout, QPushButton, QApplication
from PyQt5.QtCore import Qt


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        # 实例化一个树形结构，隐藏了header
        self.tree = QTreeWidget()#QTreeWidget是一个树形结构
        self.tree.setHeaderHidden(True)#隐藏了header
        # 顶级分支
        self.tree_main = QTreeWidgetItem(self.tree)#QTreeWidgetItem是一个分支
        self.tree_main.setText(0, '商品种类')
        # 设置一些二级分支
        tree_second = ['电子产品', '水果', '日用品', '喜欢的人']
        # self.gen_branch(self.tree_main, tree_second)
        # 设置一些三级分支
    #     tree_fruit = ['苹果', '香蕉', '梨']
    #     tree_daily_use = ['纸巾', '毛巾']
    #     tree_lovers = ['迪迪1号', '迪迪2号']
    #     # child(1) 意思是分支的第1个节点, 序号从0算起
    #     self.gen_branch(self.tree_main.child(1), tree_fruit)
    #     self.gen_branch(self.tree_main.child(2), tree_daily_use)
    #     self.gen_branch(self.tree_main.child(3), tree_lovers)
    #     # 一个按钮
    #     self.pushButton = QPushButton('选好了')
    #     # 显示出来
    #     self.qvl = QVBoxLayout()
    #     self.qvl.addWidget(self.tree)
    #     self.qvl.addWidget(self.pushButton)
    #     self.setLayout(self.qvl)
    #
    #     # 绑定一下槽函数，传入主要的分支节点
    #     self.pushButton.clicked.connect(lambda: self.get_checked(self.tree_main))
    #
    @staticmethod
    def gen_branch(node: QTreeWidgetItem, texts: list):
        """ 给定某个节点和列表 在该节点生成列表内分支"""
        for text in texts:
            item = QTreeWidgetItem()
            item.setText(0, text)
            item.setCheckState(0, Qt.Unchecked)
            node.addChild(item)
    #
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
    #     print(temp_list)
    #     return temp_list


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Demo()
    win.show()
    sys.exit(app.exec_())