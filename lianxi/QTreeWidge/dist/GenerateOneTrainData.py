import numpy as np
import GenerateOneBrakedData
import sys, os


class GenerateOneTrainData(object):
    def __init__(self,num,S_total,S_interval):
        self.num=num#第几个
        self.S_total=S_total#总运用里程
        self.S_interval=S_interval#检查间隔
        self.wear_data0 = []
        self.generate()
    def generate(self):
        for i in range(self.num):
            self.wear_datai=GenerateOneBrakedData.GenerateOneBrakedData(i,self.S_total,self.S_interval).wear_data
            self.wear_data0.append(self.wear_datai)

    def get_train_data(self):
        return self.wear_data0



# aa00=GenerateOneTrainData(8,80,2)
# print(aa00.get_train_data())