from sympy import symbols, Function, Eq, dsolve
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0.0, 1.1, 0.1)
d = np.arange(1, 2.1, 0.1)
total_t = 2000
result = np.zeros(4)
k = 0.5
m_best_1000 = []
f_best_1000 = []
m_best_300 = []
f_best_300 = []
for a in d:
    for b in d:
        m = np.zeros(total_t)
        f = np.zeros(total_t)
        m[0] = 10
        f[0] = 10
        for t in range(1, total_t):
            m[t] = m[t - 1] + 0.9 * m[t - 1] * (1 - (m[t - 1] + a * f[t - 1]) / 300)
            f[t] = f[t - 1] + 0.5 * f[t - 1] * (1 - (b * m[t - 1] + f[t - 1]) / 300)
            if t == total_t - 1:
                e = m[total_t - 1] / (m[total_t - 1] + f[total_t - 1])
                if abs(e - 0.78) < k:
                    result[2] = a
                    result[3] = b
                    m_best_1000 = m
                    f_best_1000 = f
                    k = abs(e - 0.78)
                else:
                    continue

plt.figure()
plt.plot(m_best_1000, label='m_1000')
plt.plot(f_best_1000, label='f_1000')
# plt.figure()
# plt.plot(m_best_300, label='m_300')
# plt.plot(f_best_300, label='f_300')
plt.legend()
plt.show()
print(result)
