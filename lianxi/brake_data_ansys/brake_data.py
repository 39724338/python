import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 定义一个获取数据集C的函数
def get_data():
    t = np.random.normal(0, 1, 100)
    v = 2*t**2 + np.random.normal(0, 0.5, 100)
    x = 3*v + np.random.normal(0, 1, 100)
    return pd.DataFrame({'t': t, 'v': v, 'x': x})

# 定义一个获取数据集B的函数
def get_B():
    B = []
    for i in range(8):
        b = get_data()
        B.append(b)
    return B

# 定义一个获取数据集A的函数
def get_A():
    A = []
    for i in range(30):
        A.append(get_B())
    return A

# 获取A中所有数据集B，并将它们合并成一个大的数据集B_all
B_all = []
for b in get_A():
    B_all += b
B_all = pd.concat(B_all, ignore_index=True)

# 运行线性回归(V与X的关系)，计算拟合系数和截距
regression = LinearRegression().fit(B_all[['v']], B_all['x'])
slope = regression.coef_[0]
intercept = regression.intercept_

# 计算每个数据集C中t和x之间的关系
for i, b in enumerate(B_all.groupby(np.arange(len(B_all))//100)):
    v = np.array(b[1]['v']).reshape(-1,1) # 将v作为自变量x
    x = np.array(b[1]['x']).reshape(-1,1) # 将x作为因变量y
    t = np.array(b[1]['t']).reshape(-1,1) # 将t作为自变量z
    predicted_x = slope*v + intercept # 预测x对应的值
    quadratic = PolynomialFeatures(degree=2) # 定义2阶多项式回归模型
    X_quadratic = quadratic.fit_transform(np.hstack([t, predicted_x])) # 获取高次方项
    regression = LinearRegression().fit(X_quadratic, x) # 拟合回归模型
    # 输出系数
    print(f"Data Set {i+1}:\nQuadratic Coefficients: {regression.coef_}\n")