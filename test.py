import xlrd
x1=xlrd.open_workbook(r'C:\Users\grape\Desktop\daoru.xls')
table=x1.sheets()[0]
# print(table)
rows = table.nrows#行数
# print(rows)
# print(dir(table))
column=table.ncols#列数
# print(column)
# row = table.row_values(0)#获取指定行的列表
# print(row)
# col = table.col_values(0)#获取指定列的列表
# print(col)
# data = table.cell(1,1).value#获取指定位置的 值，浮点数

print(data)
room=[]
for i in range(1,rows+1):
    room.append([])
    for j in range(1,column+1):
        # value_table=table.cell(i-1,j-1)
        room[i-1].append(table.cell(i-1,j-1).value)
print(room)


# room1=[[None]*5,[None]*5,[None]*5]#创建二维列表
# room2=[]
# for i in range(1,5):
#     room2.append([])#加行
#     for j in range(1,7):
#         room2[i-1].append(i*100+10+j)#嵌套加列
# # print(room1,room2)
# room3=[[i*100+10+j for j in range(1,7)]for i in range(1,5)]
# print(room3)