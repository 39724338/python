import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        self.setWindowTitle('表格视图')
        self.resize(500,300)
        self.model=QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['ID','年龄','fdsa'])
        self.tableview=QTableView()
        self.tableview.setModel(self.model)

        item11=QStandardItem('1')
        item12 = QStandardItem('33')
        item13 = QStandardItem('范德萨')
        self.model.setItem(0,0,item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)
        # self.model.item(0,0)
        index1=self.model.index(0,0)
        # print(self.model.index(0,0))



        layout=QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main12=TableView()
    main12.show()
    sys.exit(app.exec_())

