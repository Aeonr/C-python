import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random
import math
import seaborn as sns
from openpyxl import load_workbook

np.random.seed(43)
total_t = 100

a = np.zeros(total_t)
for c in range(50):
    a[c] = 1000
a[50] = 300
for c in range(49):
    a[16+c] = 300 + 14*c
print(a)
print(len(a))

a[0] = stats.norm.rvs(650, 116, 1)  # 随机生态位

i = np.zeros(total_t)
j = np.zeros(total_t)
k = np.zeros(total_t)

i[0] = 10
j[0] = 10
k[0] = 10

for t in range(1, total_t):
    i[t] = i[t - 1] + 0.6 * i[t - 1] * (1 - (i[t - 1] - 0.5 * j[t - 1] + 0.3 * k[t - 1]) / a[t]) - 0.5 * i[t - 1] + math.cos(i[t - 1])
    j[t] = j[t - 1] + 0.6 * j[t - 1] * (1 - (j[t - 1] - 0.5 * i[t - 1] + 0.4 * k[t - 1]) / a[t]) - 0.5 * j[t - 1] + math.cos(j[t - 1])
    k[t] = j[t - 1] + 0.6 * k[t - 1] * (1 - (k[t - 1] + 0.3 * i[t - 1] + 0.4 * j[t - 1]) / a[t]) - 0.5 * k[t - 1] + math.cos(k[t - 1])
    if i[t] < 0:
        i[t] = 0
    if j[t] < 0:
        j[t] = 0
    if k[t] < 0:
        k[t] = 0


b = [a.T]
sns.heatmap(b, cmap='viridis', annot=True, cbar=False)

fig, ax = plt.subplots()
ax.plot(i, label='i')
ax.plot(j, label='j')
ax.plot(k, label='k')

ax.imshow(b, extent=ax.get_xlim() + ax.get_ylim(), aspect='auto', origin='lower', alpha=0.5, cmap='viridis')
ax.legend()

plt.show()

print(i)
print(j)
print(k)

