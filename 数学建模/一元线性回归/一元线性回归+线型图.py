import matplotlib.pyplot as plt
import numpy as np

a = np.loadtxt('..\\模拟数据\\一元线性回归模拟数据.txt')
x = a[:, 0]
y = a[:, 1]

plt.plot(x, y, '+k', label="原始数据点")
p = np.polyfit(x, y, deg=1)  # 拟合一次多项式

print("拟合的多项式为：{}*x+{}".format(p[0], p[1]))
plt.rc('font', size=16, family='SimHei')
plt.plot(x, np.polyval(p, x), label="拟合的直线")
plt.show()
