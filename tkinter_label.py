# import tkinter
# from tkinter import *
# if __name__=='__main__':
#     win=tkinter.Tk()
#     win.title('南风、轻语')
#     screenwidth=win.winfo_screenwidth()
#     screenheight=win.winfo_screenheight()
#     # print(screenwidth)
#     # print(screenheight)
#     width=500
#     height=300
#     x=int((screenheight-width)/2)
#     y=int((screenwidth-height)/2)
#     print(x,y)
#     win.geometry('{}x{}+{}+{}'.format(width,height,x,y))
#
#     label=Label(
#         master=win,#父容器
#         text='标签',#文本
#         bg='yellow',#背景颜色
#         fg='red',#文本颜色
#         activebackground='pink',#状态为active时的背景颜色
#         activeforeground='blue',#状态为active时文本颜色
#         relief='flat',#边框的3D样式
#         bd=3,#边框大小
#         height=2,#高度
#         width=5,#宽度
#         padx=1,#内间距,字体与边框的x距离
#         pady=1,#字体与边框的Y距离
#         state='normal',#设置状态
#         cursor='arrow',#鼠标移动样式
#         font=('黑体',20)
#     )
# label.pack
#
# win.mainloop

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root, columns=('col1', 'col2', 'col3'))
tree.column('col1', width=100, anchor='center')
tree.column('col2', width=100, anchor='center')
tree.column('col3', width=100, anchor='center')
tree.heading('col1', text='col1')
tree.heading('col2', text='col2')
tree.heading('col3', text='col3')


def onDBClick(event):
    item = tree.selection()[0]
    print("you clicked on ", tree.item(item, "values"))


for i in range(10):
    tree.insert('', i, values=('a' + str(i), 'b' + str(i), 'c' + str(i)))
tree.bind("<Double-1>", onDBClick)

tree.pack()
root.mainloop()
