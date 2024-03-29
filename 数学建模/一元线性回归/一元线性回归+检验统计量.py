import statsmodels.api as sm
import numpy as np

a = np.loadtxt('E:\\python\数学建模\\模拟数据\\一元线性回归模拟数据.txt')
x = a[:, 0]
y = a[:, 1]
print(x)
df = {'x': x, 'y': y}
res = sm.formula.ols('y~x', data=df).fit()
print(res.summary(), '\n')
