import tkinter as tk
from tkinter import ttk
root = tk.Tk()
# print(type(root))
root.geometry('420x540')
root.title('成绩表2022')
# print(root.geometry)
tk.Label(root,text='成绩表').pack()
area=('#','数学','语文','英语')
ac=('all','m','c','e')
data=[('张三','90','88','95'),
      ('李四','100','92', '90'),
      ('王二','88','90', '91')
      ]
tv=ttk.Treeview(root,columns=ac,show='headings',
                height=3)
for i in range(4):
    tv.column(ac[i],width=50,anchor='e')
    tv.heading(ac[i],text=area[i])
tv.pack()
for i in range(3):
    tv.insert('','end',values=data[i])
def column():
    tv.column(2,width=50)
ttk.Button(root,text='Column',command=column).pack()
root.mainloop()
# root.mainloop()