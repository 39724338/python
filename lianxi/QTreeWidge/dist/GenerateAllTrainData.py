import GenerateOneTrainData
import numpy as np
import os,sys
import pandas as pd
import openpyxl
import xlsxwriter

class GenerateAllTrainData(object):
    def __init__(self):
        self.array = []
        self.train_data0 = []
        self.S_interval=2
        self.definearray()
        self.train_num = len(self.array)
        self.generate()

    def definearray(self):
        print("请输入每个测量的万公里数，回车表示确认，再次回车表示结束。")
        #如果输入的非数字，会报错。如果输入的数字不在10-100之间，会报错。
        #如果输入的数字不是整数，会报错。
        #如果输入的为空，会报错。
        self.array = []
        self.enter_count = 0
        while True:
            num = input("请输入数字：")
            if not num:
                self.enter_count += 1
                if self.enter_count == 2:
                    break
                else:
                    continue
            self.enter_count = 0
            if num.strip() == 'exit' or num.strip() == 'quit' or num.strip() == '退出':
                break
            if not num.isdigit():  # 判断输入是否为数字
                print("输入错误，请输入0-100之间的数字！")
                continue
            num = int(num)
            if num < 0 or num > 100:  # 判断数字是否在0-100之间
                print("输入错误，请输入0-100之间的数字！")
                continue
            self.array.append(num)
            if num == " ":
                break
            print("当前数组：", self.array, "当前数组长度：", len(self.array))





    def generate(self):
        for i in range(self.train_num):
            self.train_datai=GenerateOneTrainData.GenerateOneTrainData(i,self.array[i],self.S_interval).get_train_data()
            self.train_data0.append(self.train_datai)
    def get_all_train_data(self):
        return self.train_data0
    def ploy(self):
        # import matplotlib.pyplot as plt
        # for i in range(self.train_num):
        #     plt.plot(self.train_data0[i][0],self.train_data0[i][1])
        # plt.show()
        print(self.train_data0)
S_interval = 2
gat = GenerateAllTrainData()

# 逐个生成列车数据
train_data = []
for i in range(len(gat.array)):
    train_datai = GenerateOneTrainData(i, gat.array[i], S_interval).get_train_data()
    train_data.append(train_datai)

# 将所有列车数据转换为DataFrame对象
df = pd.DataFrame(train_data)

# 将数据保存到Excel文件中
sheet_name = 'train_data'
excel_path = 'train_data.xlsx'
writer = pd.ExcelWriter(excel_path, engine='xlsxwriter') # 使用xlsxwriter引擎

df.to_excel(writer, sheet_name=sheet_name, index=False)

# 对表单应用格式设置来美化表格
header_format = writer.book.add_format({'bold': True, 'text_wrap': True, 'valign': 'top', 'border': 1})
header_format.set_align('center')

for col_num, value in enumerate(df.columns.values):#列名
    writer.sheets[sheet_name].write(0, col_num, value, header_format)

for i, col in enumerate(df.columns):
    maxwidth = max(df[col].apply(lambda x: len(str(x))).max(), len(col))
    writer.sheets[sheet_name].set_column(i, i, maxwidth + 1)

writer.save()