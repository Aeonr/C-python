import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import random as r
from random import randint
from scipy.stats import expon, norm
from scipy import stats
import math

# 定义微分方程
a = stats.norm.rvs(0, 0.5, 1)
print(a)
b = stats.norm.rvs(0, 0.5, 1)
c = stats.norm.rvs(0, 0.5, 1)
def system(y, t):
    i, j, k = y
    didt = 0.6 * i * (1 - (i - 0.5 * j + 0.3 * k)/1000) - 0.78 * i + math.cos(i)
    djdt = 0.6 * j * (1 - (j - 0.5 * i + 0.4 * k)/1000) - 0.5 * j + math.cos(j)
    dkdt = 0.6 * k * (1 - (k + 0.3 * i + 0.4 * j)/1000) - 0.5 * k + math.cos(k)
    return [didt, djdt, dkdt]

# 初始条件
y0 = [10, 10, 10]

# 时间点
t = np.linspace(0, 10, 100)

# 求解微分方程
solution = odeint(system, y0, t)

# 提取结果
i, j, k = solution[:, 0], solution[:, 1], solution[:, 2]

# 绘图
plt.plot(t, i, label='i(t)')
plt.plot(t, j, label='j(t)')
plt.plot(t, k, label='k(t)')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.show()