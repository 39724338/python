import xlrd
x1=xlrd.open_workbook(r'C:\Users\grape\Desktop\daoru.xls')
table=x1.sheets()[0]
rows = table.nrows#行数
column=table.ncols#列数
room=[]
for i in range(1,rows+1):
    room.append([])
    for j in range(1,column+1):
        room[i-1].append(table.cell(i-1,j-1).value)
print(room)

