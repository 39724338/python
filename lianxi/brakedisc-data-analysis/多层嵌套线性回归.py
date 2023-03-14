import numpy as np
from sklearn.linear_model import LinearRegression

# 创建一个样本数据集
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([50, 60, 70, 80, 90])
y = np.array([1000, 2100, 3400, 4900, 6600])

# 第一层线性回归
X1 = np.array([x1]).T
regr1 = LinearRegression()
regr1.fit(X1, y)
b1, a1 = regr1.coef_[0], regr1.intercept_

# 第二层线性回归
X2 = np.array([(x2-a1)/b1]).T
regr2 = LinearRegression()
regr2.fit(X2, y)
b2, a2 = regr2.coef_[0], regr2.intercept_

# 预测房价
x1_new = 6
x2_new = 100
y_pred = a1 + b1 * x1_new + a2 + b2 * (x2_new-a1)/b1
print("预测房价：", y_pred)