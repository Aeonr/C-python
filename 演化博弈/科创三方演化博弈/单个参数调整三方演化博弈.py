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

plt.close("all")
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.arange(0, 50, 0.005)
args = (10,  5, 20, 10,  6, 10, 30, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'r+')
args = (10,  5, 20, 10,  6, 10, 55, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'b-')
args = (10,  5, 20, 10,  6, 10, 80, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 150, 100, 70, 0.1, 0.5, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax.plot(track5[:, 0], track5[:, 1], track5[:, 2], 'g--')

ax.view_init(elev=20, azim=-130)
ax.set_facecolor('w')

ax.set_xlabel(r"$x$", labelpad=0)
ax.set_ylabel(r"$y$", labelpad=0)
ax.set_zlabel(r"$z$", labelpad=0)

ax.set_xlim3d(xmin=0, xmax=1)
ax.set_ylim3d(ymin=0, ymax=1)
ax.set_zlim3d(zmin=0, zmax=1)

plt.legend(labels=('$c_1$=1000', '$c_1$=1500', '$c_1$=2000'), loc=(0.7, 0.5))
plt.title("图５", x=0.5, y=-0.1, fontsize=15, fontweight='bold')

plt.xticks(np.arange(0.2, 1.01, step=0.2))
plt.yticks(np.arange(0.2, 1.01, step=0.2))
ax.set_zticks(np.arange(0, 1.01, step=0.2))

left, bottom, width, height = 0.26, 0.35, 0.2, 0.2
ax1 = fig.add_axes([left, bottom, width, height])

args = (10,  5, 20, 10,  6, 10, 30, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 200, 100, 70, 0.1, 0.3, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax1.plot(track5[:, 0], track5[:, 2], 'r+')

args = (10,  5, 20, 10,  6, 10, 55, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 200, 100, 70, 0.1, 0.3, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax1.plot(track5[:, 0], track5[:, 2], 'b-')

args = (10,  5, 20, 10,  6, 10, 80, 100, 50, 110, 140, 100, 0.55, 0.5, 0.3, 80, 50, 60, 200, 100, 70, 0.1, 0.3, 5, 50, 60, 0.8, 0.7)
track5 = odeint(DS, (0.2, 0.2, 0.2), t, args)
ax1.plot(track5[:, 0], track5[:, 2], 'g--')

plt.grid()
ax1.set_facecolor('whitesmoke')
plt.xticks(np.arange(0, 1, step=0.2))
plt.yticks(np.arange(0, 1, step=0.2))
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
plt.text(0.8, 0.1, s="x", transform=ax1.transAxes, fontsize=15)
plt.text(0.1, 0.8, s="z", transform=ax1.transAxes, fontsize=15)
plt.text(0.46, 0.02, s="0", transform=ax.transAxes, fontsize=10)
plt.show()