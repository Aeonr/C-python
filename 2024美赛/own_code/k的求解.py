from sympy import symbols, Function, Eq, dsolve
import numpy as np
import matplotlib.pyplot as plt

result = 0
k = 0.5
m_best = []
f_best = []
e_list = []
for i in range(0, 1000):
        m = np.zeros(50)
        f = np.zeros(50)
        m[0] = 10
        f[0] = 10
        for t in range(1, 50):
            m[t] = m[t - 1] + 0.1 * m[t - 1] * (1 - (m[t - 1] + 0.1 * f[t - 1])/(1000 - i))
            f[t] = f[t - 1] + 0.1 * f[t - 1] * (1 - (0.3 * m[t - 1] + f[t - 1])/(1000 - i))
            if t == 49:
                e = m[49] / (m[49] + f[49])
                e_list.append(e)
                if abs(e - 0.78) < k:

                    result = 1000 - i
                    m_best = m
                    f_best = f
                    k = abs(e - 0.78)
                else:
                    continue

plt.figure()
plt.plot(m_best, label='m')
plt.plot(f_best, label='f')
plt.legend()

plt.figure(2)
plt.plot(e_list, label='e')
plt.legend()

plt.show()

print(m_best)
print(f_best)
print(result)
