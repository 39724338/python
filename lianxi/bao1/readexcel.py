import xlrd


workbookname=xlrd.open_workbook('D:\\python\\lianxi\\bao1\\bom树形图（v2.0）制动.xls')#打开工作簿
sheet1=workbookname.sheet_by_index(0)#打开第一张表
row_value=sheet1.row_values(0,12,22)#获取第一行的值
print(row_value)
colunm_value=sheet1.col_values(0,2,12)#获取第一列的值
print(colunm_value)
print(sheet1.nrows)#获取总行数
print(sheet1.ncols)#获取总列数
print(sheet1.cell(0,0).value)#获取第一行第一列的值





