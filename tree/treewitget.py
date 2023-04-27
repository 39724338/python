import pandas as pd
from PyQt5.QtWidgets import QApplication, QTreeView, QFileSystemModel, QWidget, QVBoxLayout

df = pd.read_excel('path/to/excel/file.xlsx')#读取excel文件

df = df.sort_values(by=['级数'])#按照级数排序
model = QFileSystemModel()#创建一个文件系统模型
model.setRootPath('')#设置根路径
tree = QTreeView()#创建一个树形视图
tree.setModel(model)#设置模型
for i in range(len(df)):#遍历列表，创建树形视图

    parent = model.index(0, 0, tree.rootIndex())
    for j in range(1, df.iloc[i]['级数']):
        parent = model.index(j-1, 0, parent)
    model.insertRow(i, parent)
    index = model.index(i, 0, parent)
    model.setData(index, df.iloc[i]['名称'], 0)