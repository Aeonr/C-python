import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['STSong']
plt.rcParams['axes.unicode_minus'] = False


def DS(Fx, t, U1, U2, U3, U4, U5, U6, c1, c2, c3, R1, R2, R3, a1, a2, a3, I1, I2, I3, W1, W2, W3, O1, O2, Q, F1, F2, b1, b2):
    x, y, z = Fx.tolist()
    return x * (1 - x) * (y * (U1 - O2 * R1 - O1 * c1) + z * (U2 + I1 + W1) + (-c1 + R1 + O1 * c1 - a1 * R1)), \
           y * (1 - y) * (x * (U3 + O1 * c1 + O2 * R1) + z * (U4 + b1 * F1 - Q + I1 + b2 * F2 + W2) + (-c2 + R2 - a2 * R2)), \
           z * (1 - z) * (x * U5 + y * (U6 + Q + (1 - b1) * F1) + (-c3 + R3 - a3 * R3))

fig, ax = plt.subplots()
t = np.arange(0, 1, 0.05)
args = (10, 10, 10, 10, 10, 10, 100, 100, 50, 150, 200, 100, 0.7, 0.8, 0.5, 20, 20, 40, 20, 20, 40, 0.1, 0.2, 15, 30, 20, 0.5, 0.4)
track1 = odeint(DS, (0.5, 0.5, 0.5), t, args)

plt.stem(t, track1[:, 0], linefmt="r-.", markerfmt="r+", basefmt="r--")
plt.stem(t, track1[:, 1], linefmt="b-.", markerfmt="bo", basefmt="b--")
plt.stem(t, track1[:, 2], linefmt="m-.", markerfmt="m^", basefmt="m--")
plt.xticks(np.arange(0, 1.01, step=0.2))
plt.yticks(np.arange(0, 1.01, step=0.2))
plt.legend(labels=('x=0.2', 'y=0.2', 'z=0.2'))
ax.set_xlabel("t", labelpad=-5)
ax.set_ylabel("x0/y0/z0", labelpad=-5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("图1  " + r'$x$' + '、' + r'$y$' + '、' + r'$z$' + "不同时的演化仿真图", y=-0.15)
plt.grid(True)
plt.show()