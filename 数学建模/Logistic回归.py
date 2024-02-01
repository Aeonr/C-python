# 用概率去进行回归
import numpy as np
import statsmodels.api as sm

a = np.loadtxt("E:\\repository_local\\python\\数学建模\\模拟数据\\Logistic回归模拟数据.txt")
x = a[:, 0]
pi = a[:, 2] / a[:, 1]
print(pi)
X = sm.add_constant(x)
yi = np.log(pi / (1 - pi))
md = sm.OLS(yi, X).fit()  # 拟合模型
print(md.summary())
b = md.params  # 回归系数
p0 = 1 / (1 + np.exp(-np.dot(b, [1, 9])))
print(p0)
