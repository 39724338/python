import openpyxl
import matplotlib.pyplot as plt

# 读取 Excel 文件
wb = openpyxl.load_workbook('workbook.xlsx')
sheet = wb.active

data = []
for row in sheet.iter_rows(min_row=2,values_only=True):#从第二行开始读取
    row = [float(i) if i is not None else 0 for i in row[1:]]#将读取的数据转换为浮点数
    # print(row)
    data.append(row)
    # print(data)
# print(data[1][2])

# print(data)

mileage = [row[0] for row in data]#读取第一列数据
print(mileage)
wear = [[thickness for thickness in row[1:]] for row in data]
print(wear)
x = mileage
# y1, y2 = zip(*wear)
# y1, y2 = [], []
n = len(wear[0])  # 定义数组个数
y_list = [[] for i in range(n)]  # 用列表推导式定义多个空数组

# 分别将 y_list 中的每个元素赋值给 y1, y2, y3, ..., yn
y1, y2, y3, ..., yn = y_list#这里的y1,y2,y3...yn是变量名，可以随便取，只要和上面的y_list中的元素个数一致就行


for i in range(len(wear[0])):
    wear_col = [row[i] for row in wear]  # 取 wear 列表中第 i 列的数据
    print(wear_col)
    y1.append(wear_col[0])
    print(y1)
    y2.append(wear_col[1])
    print(y2)
# print(y1)
# print(y2)

# plt.scatter(x, y1, color='blue', label='y1')
# plt.scatter(x, y2, color='green', label='y2')
# plt.xlabel('a')
# plt.ylabel('b')
# plt.legend()
# plt.show()