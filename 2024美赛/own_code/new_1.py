import random as r
from random import randint
import scipy.stats as stats
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import seaborn as sns

a = [r.randint(56, 79) for _ in range(50)]
# t = list(range(1, 51))
# x = np.array(a)
# y = np.array(t)
# d0 = 1
# b0 = 2
# c0 = 3

m = np.zeros(50)
f = np.zeros(50)

# f[t] = (1 - np.exp(-0.5 * t)) / 0.5
# m[t] = (a[t] / 100 - np.exp(-0.5 * t)) / 0.5

for t in range(0, 50):
    m[t] = ((a[t] * γ) / 100 - np.exp(-0.5 * t)) / 0.5
    f[t] = (γ - np.exp(-0.5 * t)) / 0.5

a = np.array(a)
print(a.T)
b = [a.T]
sns.heatmap(b, cmap='viridis', annot=True, cbar=False)
fig, ax = plt.subplots()

ax.plot(m, label='m_1')
ax.plot(f, label='f_1')
ax.imshow(b, extent=ax.get_xlim() + ax.get_ylim(), aspect='auto', origin='lower', alpha=0.5, cmap='viridis')
ax.legend()
plt.show()


# # 定义非线性函数
# def func(p, x):
#    d, b, c = p
#    return d * np.exp(-b * x) + c
#
# # 定义误差函数
# def error(p, x, y):
#    return y - func(p, x)
#
# # 初始化参数
# p0 = [d0, b0, c0]
#
# # 计算拟合
# result = leastsq(error, p0, args=(x, y))
#
# d, b, c = result[0]
# print("d:", d)
# print("b:", b)
# print("c:", c)