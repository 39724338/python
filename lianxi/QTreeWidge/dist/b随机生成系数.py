import sys, os
#现在有1个数组(a=[0,0,0])，以及1个2元2次方程(t=a[0]v**2+a[1]v+a[2],请用python定义一个类
#求解a数组并输出，满足下列条件:v的值在0-9420之间时，t的值在0-3之间.
import sys, os
#现在有1个数组(a=[0,0,0])，以及1个2元2次方程(t=a[0]v**2+a[1]v+a[2],请用python定义一个类
#求解a数组并输出，满足下列条件:v的值在0-9420之间时，t的值在0-3之间.
import random
import numpy as np
import matplotlib.pyplot as plt

class GenerateCoefficients:
    def __init__(self):
        self._a = [0, 0, 0]#什么意思？#初始化a数组
        self.generate_a()

    def equation(self, v):
        t = self._a[0] * v ** 2 + self._a[1] * v + self._a[2]
        return t

    def check_condition(self, a):
        v_array = np.linspace(0, 9420, 1000)
        t_array = np.array([self.equation(v) for v in v_array])
        if (np.any(v_array == 9420) and np.max(t_array) < 3) or (np.all(t_array >= 0) and np.min(t_array) >= 0):
            return True
        else:
            return False

    def generate_a(self):
        while True:
            a = [random.uniform(-1, 1) for i in range(3)]
            if self.check_condition(a):
                break

        self._a = a
        self._a = [abs(x) for x in self._a]


    @property
    def a(self):
        return self._a

    def plot(self):
        v_array = np.linspace(0, 9420, 1000)
        t_array = np.array([self.equation(v) for v in v_array])

        plt.plot(v_array, t_array)
        plt.xlabel('v')
        plt.ylabel('t')
        plt.title('v-t Relationship')
        plt.show()
# a11=GenerateCoefficients()
# a11.plot()
# print(a11._a)