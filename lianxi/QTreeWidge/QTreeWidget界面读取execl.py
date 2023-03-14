import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,QTreeView,QVBoxLayout
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from openpyxl import load_workbook
import xlrd

class ExcelTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setHeaderHidden(True)
        # self.data = self.read_excel_file('QTreeWidget.xlsx')
        # self.show_data()#显示数据

        #读取excel文件
        workbookname = xlrd.open_workbook('D:\\python\\lianxi\\bao1\\bom树形图（v2.0）制动.xls')  # 打开工作簿
        sheet1 = workbookname.sheet_by_index(1)  # 打开第一张表
        # sheet2= workbookname.get_active_sheet()
        # print(sheet2)

        self.col_len = sheet1.ncols
        self.row_len=sheet1.nrows
        print("找到数据表，有%s行,有%s列"%(self.row_len,self.col_len))

        # #将数据表写入数组
        self.data=[]
        for i in range(0,self.row_len):
            row_data=[]
            for j in range(0,self.col_len):
                cell_value=sheet1.cell(i,j).value
                row_data.append(cell_value)
            self.data.append(row_data)
        print("数据已写入数组，第1行是：",self.data[0])

        #创建树形控件,并设置列数和表头
        self.QTreeWidget = QTreeWidget()
        self.QTreeWidget.setColumnCount(self.col_len)
        self.QTreeWidget.setHeaderLabels(self.data[0])

        print(self.data[1])#打印第一行的值
        print(self.data[2][2])#打印第二行的值
        child1 = QTreeWidgetItem(self.QTreeWidget)
        child1.setText(0, 'Child 1')
        print(self.data[1][1])#打印第二行第二列的值
        child1.setText(1, str(self.data[1][1]))
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
        child2 = QTreeWidgetItem(self.QTreeWidget)
        child2.setText(0, 'Child 2')
        child2.setText(1, '4')
        #
        grandchild3 = QTreeWidgetItem(child2)  # 孙子节点
        grandchild3.setText(0, 'Grandchild 2.1')
        grandchild3.setText(1, '5')



        QTreeView.expandAll(self.QTreeWidget)#展开所有节点
        QVLayout = QVBoxLayout()
        QVLayout.addWidget(self.QTreeWidget)
        self.setLayout(QVLayout)
        print(QTreeWidget.__base__)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ExcelTreeWidget()
    widget.show()
    sys.exit(app.exec_())