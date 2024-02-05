import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, norm
from scipy import stats
import random
import math

np.random.seed(43)
a = stats.norm.rvs(650, 100, 100)  # 随机生态位
print(a)

total_t = 1000

m1_total = []
m2_total = []
f1_total = []
f2_total = []

for k in range(100):
    m_1 = np.zeros(total_t)
    f_1 = np.zeros(total_t)
    m_2 = np.zeros(total_t)
    f_2 = np.zeros(total_t)
    m_1[0] = 10
    f_1[0] = 10
    m_2[0] = 10
    f_2[0] = 10

    for t in range(1, total_t):
        m_1[t] = m_1[t - 1] + 0.6 * m_1[t - 1] * (1 - (m_1[t - 1] + 0.65 * f_1[t - 1]) / a[k])
        f_1[t] = f_1[t - 1] + 0.5 * f_1[t - 1] * (1 - (0.9 * m_1[t - 1] + f_1[t - 1]) / a[k])
        m_2[t] = m_2[t - 1] + 0.95 * m_2[t - 1] * (1 - (m_2[t - 1] + f_2[t - 1]) / a[k])
        f_2[t] = f_2[t - 1] + 0.85 * f_2[t - 1] * (1 - (m_2[t - 1] + f_2[t - 1]) / a[k])
        if m_1[t]< 0:
            m_1[t] = 0
        if f_1[t] < 0:
            f_1[t] = 0
        if m_2[t] < 0:
            m_2[t] = 0
        if f_2[t] < 0:
            f_2[t] = 0

    m1_total.append(m_1)
    m2_total.append(m_2)
    f1_total.append(f_1)
    f2_total.append(f_2)

population1_result = np.zeros(100)
population2_result = np.zeros(100)

for i in range(100):
    population1_result[i] = m1_total[i][-1] + f1_total[i][-1]
    population2_result[i] = m2_total[i][-1] + f2_total[i][-1]

plt.figure()
plt.plot(population1_result, label='lamprey')
plt.plot(population2_result, label='bio B')
plt.legend(loc='upper right')
plt.show()
print(population1_result)
print(population2_result)