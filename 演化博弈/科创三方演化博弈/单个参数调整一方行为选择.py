import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['STSong']
plt.rcParams['axes.unicode_minus'] = False

def DS(Fx, t, a1, b1, c1, d1, e1, f1, a2, b2, c2, d2, e2, f2, a3, b3, c3, d3, e3, f3, g1):
    x, y, z = Fx.tolist()
    return x * (1 - x) * ((d1 * z + e1 * (z - 1)) * (y - 1) - d1 * y + y * (d1 - a1 + f1) + (y - 1) * (a1 - d1 - f1 + (b1 + c1) * (z - 1))), \
           y * (1 - y) * (b2 - a2 + c2 + d2 + f2 + b1 * x - b2 * z - c2 * z + e2 * x - d2 * z - b1 * x * z), \
           z * (1 - z) * (c3 - b3 + d3 + g1 + c1 * x + b2*y + e3*x + f3*y - c1*x*y)
#  基础参数 (15, 10, 5, 5, 10, 20, 10, 5, 10, 15, 25, 10, 10, 15, 5, 5, 10, 15, 5)
#          (a1, b1, c1, d1, e1, f1, a2, b2, c2, d2, e2, f2, a3, b3, c3, d3, e3, f3, g1)

fig, ax = plt.subplots()
t = np.arange(0, 1, 0.005)
args = (15, 10, 5, 5, 10, 20, 5, 5, 10, 15, 25, 10, 10, 15, 5, 5, 10, 15, 5)
track6 = odeint(DS, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track6[:, 1], 'r-.', markevery=2, markerfacecolor="None")
args = (15, 10, 5, 5, 10, 20, 10, 5, 10, 15, 25, 10, 10, 15, 5, 5, 10, 15, 5)
track6 = odeint(DS, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track6[:, 1], 'b-', markevery=2, markerfacecolor="None")
args = (15, 10, 5, 5, 10, 20, 15, 5, 10, 15, 25, 10, 10, 15, 5, 5, 10, 15, 5)
track6 = odeint(DS, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track6[:, 1], 'g--', markevery=2, markerfacecolor="None")
args = (15, 10, 5, 5, 10, 20, 20, 5, 10, 15, 25, 10, 10, 15, 5, 5, 10, 15, 5)
track6 = odeint(DS, (0.5, 0.5, 0.5), t, args)
plt.plot(t, track6[:, 1], 'y-', markevery=2, markerfacecolor="None")

plt.xticks(np.arange(0, 1.01, step=0.1))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('$c_b$=5', '$c_b$=10', '$c_b$=15', '$c_b$=20'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("Y", labelpad=-5)
ax.set_xlim(0, 0.7)
ax.set_ylim(0.4, 1)
# plt.title("图b " + "平台激励不同时农户的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()
