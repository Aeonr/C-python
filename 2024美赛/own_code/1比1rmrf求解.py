import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0.0, 1.1, 0.1)
total_t = 2000
result = np.zeros(2)
k = 0.5
env = 300
m_best = []
f_best = []

for rm in x:
    for rf in x:
        m = np.zeros(total_t)
        f = np.zeros(total_t)
        m[0] = 10
        f[0] = 10
        for t in range(1, total_t):
            m[t] = m[t - 1] + rm * m[t - 1] * (1 - (m[t - 1] + f[t - 1])/env)
            f[t] = f[t - 1] + rf * f[t - 1] * (1 - (m[t - 1] + f[t - 1])/env)
            if t == total_t - 1:
                e = m[total_t-1] / (m[total_t-1] + f[total_t-1])
                if abs(e - 0.56) < k:
                    result[0] = rm
                    result[1] = rf
                    m_best = m
                    f_best = f
                    k = abs(e - 0.56)
                else:
                    continue

plt.figure()
plt.plot(m_best, label='m')
plt.plot(f_best, label='f')
plt.legend()
plt.show()

print(result)
print(k)


