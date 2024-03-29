import numpy as np
from sklearn.linear_model import LinearRegression

a = np.loadtxt("E:\\python\数学建模\\模拟数据\\多元线性回归模拟数据.txt")
print(a[:,:2])
md = LinearRegression().fit(a[:, :2], a[:, 2])  # 构建拟合模型
y = md.predict(a[:, :2])  # 求预测值
b0 = md.intercept_
b12 = md.coef_  # 输出回归系数
R2 = md.score(a[:, :2], a[:, 2])  # 计算R^2
print(b0, b12[0], b12[1])
print(R2)  # 线性方程：y=b0+b12[0]x1+b12[1]x2
# 三个自变量的多元线性回归
# import numpy as np
# from sklearn.linear_model import LinearRegression
# a=np.loadtxt("多元线性回归模拟数据.txt")
# md=LinearRegression().fit(a[:,:3],a[:,3])
# y=md.predict(a[:,:3])
# b0=md.intercept_;b12=md.coef_
# R2=md.score(a[:,:3],a[:,3])
# print(b0,b12[0],b12[1],b12[2])
# print(R2)   三个以上的变量相互之间可能会有强烈的相关关系即不再选用多元线性回归，选用岭回归和LASSO回归进行补充，岭回归和LASSO回归更具有实用价值
