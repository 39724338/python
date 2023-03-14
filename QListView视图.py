import sys

from PyQt5.QtWidgets import QApplication, QWidget,QTableView,QListView,QVBoxLayout,QMessageBox,QAbstractItemView
from PyQt5.QtCore import QStringListModel

class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        self.setWindowTitle('列表视图')
        self.resize(300,200)
        layout=QVBoxLayout()
        listview=QListView()
        #
        listmodel=QStringListModel()
        self.list=['列表项1','列表项2','列表项2']
        listmodel.setStringList(self.list)
        listview.setModel(listmodel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)
        self.setLayout(layout)
def clicked(self,item):
    QMessageBox.information(self,'QListView','你选择了：'+self.list[item.row()])



if __name__=='__main__':
    app=QApplication(sys.argv)
    win=ListView()
    win.show()
    sys.exit(app.exec_())

